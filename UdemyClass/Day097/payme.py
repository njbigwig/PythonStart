# by Copilot

# pip install -r requirements.txt

from flask import Flask, render_template, redirect, url_for, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm
import stripe
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('DAY97_SECRET')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db = SQLAlchemy(app)

# Stripe setup
stripe.api_key = os.environ.get('DAY97_STRIPE')
#

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ---------------- Models ---------------- #
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # price in cents

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------- Routes ---------------- #
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = Product.query.filter(Product.id.in_(session.get('cart', []))).all()
    return render_template('cart.html', cart_items=cart_items)

@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    cart_items = Product.query.filter(Product.id.in_(session.get('cart', []))).all()
    total_amount = sum(item.price for item in cart_items)

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': item.name},
                'unit_amount': item.price,
            },
            'quantity': 1,
        } for item in cart_items],
        mode='payment',
        success_url=url_for('index', _external=True),
        cancel_url=url_for('cart', _external=True),
    )
    return redirect(checkout_session.url, code=303)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Add sample products if empty
        if not Product.query.first():
            db.session.add(Product(name="Cool T-Shirt", price=2000))  # $20.00
            db.session.add(Product(name="Coffee Mug", price=1500))    # $15.00
            db.session.commit()

    app.run(debug=True)


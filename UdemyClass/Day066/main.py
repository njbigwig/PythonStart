
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
from sqlalchemy.sql import func

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
def rest_api_del_record(db, id):
    print("REST API Call - del_record()")
    print(f"DELETE: id={id}")
    
    cafe = db.session.get(Cafe, id)
    
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200    
   


def rest_api_update_record(db, id, new_price):
    print("REST API Call - update_record()")
    print(f"UPDATE: id={id} Price: {new_price}")
    
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == int(id))).scalar()
    
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Updated price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a Cafe with that id was not found in the database."}), 404
    
    #return redirect(url_for("home"))
    

def rest_api_add_record(table, cafename, mapurl):
    print("REST API Call - add_record()")
    print(f"ADD: name={cafename} map_url={mapurl}")
    
  
    return redirect(url_for("home"))
    #return jsonify(all_cafes=all_cafe_dict)

def rest_api_search(table, location):
    print("REST API Call - search()")
    
    print(f"Location Search: {location}")
    
    result = table.session.execute(select(Cafe).where(Cafe.location == location))
    
    all_cafes = result.scalars().all()
    print(f"Number of Cafes Found: {len(all_cafes)}")
    
    all_cafe_dict = {}
    
    errorno = None
     
    for cafes in all_cafes:
        cafe_dict = cafes.convert_to_dict()
        all_cafe_dict[cafes.id] = cafe_dict
    
    if len(all_cafe_dict) == 0:
        all_cafe_dict["error"] = "Sorry - no cafes found at that location"
        errorno = 404
    
    #return(jsonify(all_cafes=all_cafe_dict))
    return jsonify(all_cafe_dict), errorno
    
    
def rest_api_all_records(table):
    print("REST API Call - all_records()")
    
    result = table.session.execute(table.select(Cafe))
    all_cafes = result.scalars().all()
    
    all_cafe_dict = {}
    
    for cafes in all_cafes:
        print(cafes.name)
        cafe_dict = cafes.convert_to_dict()
        all_cafe_dict[cafes.id] = cafe_dict    
        
    
    #return redirect(url_for("home"))
    return jsonify(all_cafes=all_cafe_dict)


def rest_api_random_record(app_ref, table):
    print("REST API Call - random_record()")
    
    with app_ref.app_context():
        random_cafe = table.session.query(Cafe).order_by(func.random()).first()
        print(random_cafe.name)
        
    return jsonify(id=random_cafe.id, \
           name=random_cafe.name, \
           map_url=random_cafe.map_url, \
           img_url=random_cafe.img_url, \
           location=random_cafe.location, \
           seats=random_cafe.seats, \
           has_toilet=random_cafe.has_toilet, \
           has_wifi=random_cafe.has_wifi, \
           has_sockets=random_cafe.has_sockets, \
           can_take_calls=random_cafe.can_take_calls, \
           coffee_price=random_cafe.coffee_price)
        
    
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def convert_to_dict(self):
        
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # where the key is the name of the column & the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
            
        return dictionary


with app.app_context():
    db.create_all()
    
@app.route("/report-closed",methods=["DELETE"])
def delete_record(): 
    rec_data = request.get_json()  # Extract JSON body
    id = rec_data.get("id")
    api_key = rec_data.get("api_key")
    
    if api_key == "TopSecretAPIKey":
        return rest_api_del_record(db, id)
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
            
    


@app.route("/update-price",methods=["PATCH"])
def update_record(): 
    rec_data = request.get_json()  # Extract JSON body
    id = rec_data.get("id")
    new_price = rec_data.get("new_price")
    
    return(rest_api_update_record(db, id, new_price))

# @app.route("/add", methods=["POST"])
# def post_new_cafe():
#     new_cafe = Cafe(
#         name=request.form.get("name"),
#         map_url=request.form.get("map_url"),
#         img_url=request.form.get("img_url"),
#         location=request.form.get("location"),
#         has_sockets=bool(request.form.get("sockets")),
#         has_toilet=bool(request.form.get("toilet")),
#         has_wifi=bool(request.form.get("wifi")),
#         can_take_calls=bool(request.form.get("calls")),
#         seats=request.form.get("seats"),
#         coffee_price=request.form.get("coffee_price"),
#     )
#     db.session.add(new_cafe)
#     db.session.commit()
#     return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/add",methods=["POST"])
def add_record(): 
    rec_data = request.get_json()  # Extract JSON body
    new_name = rec_data.get("name")
    new_mapurl = rec_data.get("map_url")
    
    return(rest_api_add_record(db, new_name, new_mapurl))


@app.route("/search",methods=["GET"])
def search_records():   
    location_query = request.args.get("location")
    
    if not location_query:
        return jsonify(error="Missing 'location' query parameter"), 400
    else:
        return(rest_api_search(db, location_query))


@app.route("/all",methods=["GET"])
def get_all_records():   
    
    return(rest_api_all_records(db))


@app.route("/random",methods=["GET"])
def get_record():   
    
    return(rest_api_random_record(app, db))  


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

class User1:
    pass # for an empty class

# Attributes = what a class has
# Methods = what a class can do

class User:
    def __init__(self, user_id, user_name):
        print("Constructor: new user being created...") # called whenever Constructor is called
        self.id = user_id # Attributes
        self.username = user_name
        self.followers = 0
        self.following = 0
    def follow(self, user): # Method
        user.followers += 1 # call a method from another object
        self.following += 1


    
# dynamically add a attribute or a variable associated with an object
user_1 = User1()
user_1.id = "001"
user_1.username = "angela"
print(user_1.username)

user_2 = User1()
user_2.id = "002"
user_2.username = "joe"
print(user_2.username)

# using Constructor
user_3 = User("003", "Dave")
print(user_3)
print(user_3.id, user_3.username, user_3.followers, user_3.following)

user_4 = User("004", "Maximus")
print(user_4)
print(user_4.id, user_4.username, user_4.followers, user_4.following)

print("Before user 3 follows user 4...")
user_3.follow(user_4)

print("After user 3 follows user 4...")
print(user_3.id, user_3.username, user_3.followers, user_3.following)
print(user_4.id, user_4.username, user_4.followers, user_4.following)


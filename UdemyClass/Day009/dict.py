# An example dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

#Will print "green"
print(colours["pear"])

#This is how to create an empty dictionary:
my_empty_dictionary = {}

#This is how you can add new items to an existing dictionary:
colours["peach"] = "pink"

print(f"Size of color dictionary: {len(colours)}")


#This is also how you can edit an existing value in a dictionary:
colours["apple"] = "green"

#This is how to loop through a dictionary and print all the keys:
for key in colours:
    print(key)

#This is how to loop through a dictionary and print all the values:
for key in colours:
    print(f"{key} = {colours[key]}")
    
#try to add an existing key
programming_dictionary["Loop"] = "The action of doing something over and over again."

for term in programming_dictionary:
    print(f"{term} = {programming_dictionary[term]}")
    
#retrieve a dictory entry
print(programming_dictionary["Bug"])

#attempt to get an entry which does not exist
#print(programming_dictionary["NOP"]) = generates a run time error
#if programming_dictionary["NOP"] == False:
#    print("No such term")

#update an entry
programming_dictionary["Bug"] ="A moth in your computer."

for term in programming_dictionary:
    print(f"{term} = {programming_dictionary[term]}")
    
capitals = {
  "France": "Paris",
  "Germany": "Berlin"  
}

# I travel to France, need a dictory to record the cities I visited, need a nest list within a dictionary
travel_log = {
    "France": ["Paris", "Normandy", "Le Mans"],
    "Germany": ["Berlin", "Nuremberg"] 
}


for country in travel_log:
    print(f"{travel_log[country]}")
    

city_list = travel_log["France"]
for city in city_list:
    print(f"{city}")
    
#2nd entry
print(f"#1 {city_list[1]}")
print(f"#2 {travel_log["France"][1]}")

#nested list
nested_list = ["A", "B", ["C","D"]]

#print out C
print(f"{nested_list[2][0]}")

#next dictionaries
travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Normandy", "Le Mans"],
        "total_visits": 1
    },
    "Germany": {
        "cities_visited": ["Berlin", "Nuremberg"],
        "total_visits": 1
    }
}

for country in travel_log2:
    print(f"{travel_log2[country]} = {travel_log2[country]["total_visits"]}")

#how would I print out Nuremberg?
print(f"{travel_log2["Germany"]["cities_visited"][1]}")
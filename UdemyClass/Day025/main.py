# Pandas package
import pandas
import csv

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame
# https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series

# # method 1 read in CSV file as a list
# print("CSV read using readlines()")
# weatherlist = []
# with open("weather_data.csv") as csvfile:
#     weatherlist = csvfile.readlines()
  
# print(f"Len={len(weatherlist)}")  
# for day in weatherlist:
#     print(f"element=[{day.strip()}]")
    
# print("\n")
    
    
# # method 2 using csv package
# print("CSV read using csv.reader()")
# weatherlist = []
# temperaturelist = []

# with open("weather_data.csv") as csvfile:
#     weatherlist = csv.reader(csvfile)
#     for row in weatherlist:
#         print(row)
#         print(row[0], row[1], row[2])
#         if row[1] != "temp":
#             temperaturelist.append(int(row[1]))
        
# for t in temperaturelist:
#     print(t)

# print("\n")
   
# print(weatherlist)
# print(type(weatherlist))

# print("\n")

# # method 3 using Pandas package
# print("CSV read using Pandas - only 3 lines!!!")
# weatherdata = pandas.read_csv("weather_data.csv")
# print(type(weatherdata))
# print("Entire table:")
# print(weatherdata)
# print("\n")

# print("Temp column:")
# print(weatherdata["temp"])
# print(type(weatherdata["temp"]))

# data_dict = weatherdata.to_dict()
# print(data_dict)

# temp_list = weatherdata["temp"].to_list()
# print(temp_list)
# print(f"Mean Temp #1 = {weatherdata["temp"].mean()}")
# print(f"Mean Temp #2 = {weatherdata["temp"].sum()/weatherdata["temp"].count()}")
# print(f"Max Temp = {weatherdata["temp"].max()}")

# # data in rows
# print(weatherdata[weatherdata["day"]=="Monday"])

# # find the row with the highest temperature
# print(weatherdata[weatherdata["temp"]==weatherdata["temp"].max()])

# monday = weatherdata[weatherdata["day"]=="Monday"]
# print(f"Monday condition = {monday["condition"]}")
# print(f"Monday Temp F = {(monday["temp"]*(9/5))+32}")

# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# newdata = pandas.DataFrame(data_dict)
# print(newdata)

# # create CSV file
# newdata.to_csv("newdata.csv")
# 2018 Central Park Squirrel Census
print("Reading CSV file with Pandas....")
squirreldata = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250111.csv")
print(type(squirreldata))

grays = squirreldata[squirreldata["Primary Fur Color"]=="Gray"].shape
# alt: gray_squirrel_count = len(squirreldata[squirreldata["Primary Fur Color"]=="Gray"])
graycount = grays[0]
print(f"Gray = {graycount}")

cinnamons = squirreldata[squirreldata["Primary Fur Color"]=="Cinnamon"].shape
cinnamoncount = cinnamons[0]
print(f"Cinnamon = {cinnamoncount}")

blacks = squirreldata[squirreldata["Primary Fur Color"]=="Black"].shape
blackcount = blacks[0]
print(f"Black = {blackcount}")

print("\n")

# create a squirrel color dataframe from scratch
colors_dict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [graycount, cinnamoncount, blackcount]
}

# create new fur color CSV file
squirrelcolors = pandas.DataFrame(colors_dict)
print(squirrelcolors)

squirrelcolors.to_csv("squirrel_fur_colors")



print("\n")



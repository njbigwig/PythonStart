import turtle
import pandas

FONT = ("Courier", 7, "normal")

def get_mouse_click_coor(x, y):
    print(f"X: {x} /  Y:{y}")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

# get state data using Pandas
statedata = pandas.read_csv("50_states.csv")

all_states = statedata["state"].to_list()
# print(all_states)

turtle.onscreenclick(get_mouse_click_coor)

game_is_on = True

correct_states = 0

correct_guesses = []

statetext = turtle.Turtle()
statetext.penup()
statetext.hideturtle()


while game_is_on == True and correct_states < 50:
    answer_state = screen.textinput(title=f"{correct_states}/50 Correct", prompt="What's another state's name?")
    #print(answer_state)
    if answer_state != None:
        # pull out matching row => series index value
        statefind = statedata[statedata["state"] == answer_state.title()]
    
        if statefind.empty == False and (answer_state.title() in correct_guesses) == False:
            correct_guesses.append(answer_state.title())
            correct_states += 1
            statetext.teleport(int(statefind["x"].loc[statefind.index[0]]), int(statefind["y"].loc[statefind.index[0]]))
            statetext.write(f"{statefind["state"].loc[statefind.index[0]]}", align="left", font=FONT)
            #print(f"State = {statefind["state"].loc[statefind.index[0]]}")
            #print(f"X = {statefind["x"].loc[statefind.index[0]]}")
            #print(f"Y = {statefind["y"].loc[statefind.index[0]]}")
            
            # better way to get a value from a series
            # print(f"X={statefind["x"].item()}")
    else:
        game_is_on = False
        

# find which states we missed
# for state in correct_guesses:
#     if state in all_states:
#         all_states.remove(state)

# find which states we missed - using list comprehension
# new_list = [new_item for item in list if test]
states_to_learn = []
states_to_learn = [state for state in all_states if state not in correct_guesses ]
#print(correct_guesses)

# print(all_states)   
#missed_data = pandas.DataFrame(all_states)
missed_data = pandas.DataFrame(states_to_learn)
missed_data.to_csv("states_to_learn.csv") 

#turtle.mainloop()



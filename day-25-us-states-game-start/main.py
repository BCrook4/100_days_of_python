import turtle
import pandas
from game_manager import Manager

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

manager = Manager()
correct_guesses = []

# get state data
game_data = pandas.read_csv("50_states.csv")

states = game_data.state.to_list()

while len(correct_guesses) < 50:
    answer_state = manager.get_answer()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_guesses]
        missing_csv = pandas.DataFrame(missing_states)
        missing_csv.to_csv("missing_states.csv")
        break

    if answer_state in game_data.values and answer_state not in correct_guesses:
        row = game_data[game_data.state == answer_state]
        x = row.x.item()
        y = row.y.item()
        manager.write_state(answer_state, x, y)
        correct_guesses.append(answer_state)



# screen.exitonclick()
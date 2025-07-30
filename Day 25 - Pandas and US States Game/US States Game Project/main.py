import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name a state in the US:").title()
    if answer_state == 'Exit':
        # not_guessed_states = []
        # for i in all_states:
        #     if i not in guessed_states:
        #         not_guessed_states.append(i)
        not_guessed_states = [state for state in all_states if state not in guessed_states]
        states_dataframe = pandas.DataFrame(not_guessed_states)
        states_dataframe.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_row = data[data.state == answer_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(state_row.x.item(), state_row.y.item())
        state_name.write(answer_state, align="center", font=("Courier", 12, "bold"))



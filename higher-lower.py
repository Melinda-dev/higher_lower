from flask import Flask
import random
import time

app = Flask(__name__)

computer_answer = random.randint(0,9)
print(computer_answer)

@app.route('/')
def hello_world():
    return '<h1 >Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'


@app.route("/<int:your_guess>")
def enter_number(your_guess):
        if your_guess > computer_answer:
            return '<h1>Too high</h1>'\
                    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
        if your_guess < computer_answer:
            return '<h1>Too low</h1>' \
                   '<img src="https: // media.giphy.com / media / jD4DwBtqPXRXa / giphy.gif"/>'
        if your_guess == computer_answer:
            return '<h1>You are correct</h1>' \
                   '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'

if __name__ == "__main__":
    app.run(debug=True)









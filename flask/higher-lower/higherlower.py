from flask import Flask
import random
from functools import wraps

app = Flask(__name__)

# This decorator logs the user's guess and the result of the game.
def log_guess(func):
    @wraps(func)
    def wrapper(numberguess):
        result = func(numberguess)
        print(f"[LOG] User Guess : {numberguess}\nCorrect Number: {guess.number}\nResults: {result[:30]}")
        return result
    return wrapper
# This class generates a random number between 0 and 9 and allows refreshing the number.
class Guess: 
    def __init__(self, number):
        self.number = number
        
    def refresh(self):
        self.number = random.randint(0, 9)
        return self.number
# This instance of the Guess class is created to store the random number.    
guess = Guess(0)
# This route is the home page of the application. It refreshes the random number and displays a message to the user.
@app.route('/')
def home():
    guess.refresh()
    return "<h1> GUESS A NUMBER BETWEEN 0 AND 9 </h1>" \
           "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGNrdGlyODhlbnd2dm1tdjV3NjBsaWs4YW5hN3BlNDh3ZzU5NWNmeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fDUOY00YvlhvtvJIVm/giphy.gif' alt='Gif'>"
# This route handles the user's guess. It compares the user's guess with the random number and returns a message indicating whether the guess was too high, too low, or correct.
@app.route('/<int:numberguess>')
@log_guess
def logic_game(numberguess):
    if guess.number < numberguess:
        return "<h1 style='color: red'>Too high, try again!</h1>" \
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcG9tZWdiaG4ydm5sMXZiZ2tkZ2ZrZ25la2c3OXhvMTAzM2UxNTAzNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JT7Td5xRqkvHQvTdEu/giphy.gif' alt='Gif'>"
    elif guess.number > numberguess:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcG9tZWdiaG4ydm5sMXZiZ2tkZ2ZrZ25la2c3OXhvMTAzM2UxNTAzNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JT7Td5xRqkvHQvTdEu/giphy.gif' alt='Gif'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzM3dTFzeXJrcmN2aDc5YnRzd3pmM2tzdDk0M3BzNHJsc3RtczR1byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tf9jjMcO77YzV4YPwE/giphy.gif' alt='Gif'>"


if __name__ == "__main__":
    app.run(debug=True)
 

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Game logic
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    user_choice = data["choice"]
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

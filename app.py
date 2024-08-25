from flask import Flask, render_template, request, redirect, url_for
import random
import json

app = Flask(__name__)

# Load data from JSON file
def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"users": {}, "total_mined_coins": 0}
    return data

# Save data to JSON file
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Initialize data
data = load_data()
users = data['users']
total_mined_coins = data['total_mined_coins']
total_supply = 10000000  # 10 million coins

@app.route('/')
def home():
    question, answer = generate_question()
    return render_template('index.html', question=question, answer=answer)

@app.route('/answer', methods=['POST'])
def answer():
    global total_mined_coins
    username = request.form['username']
    user_answer = int(request.form['answer'])
    correct_answer = int(request.form['correct_answer'])

    if user_answer == correct_answer:
        coins_awarded = 1  # You can adjust this value
        if username not in users:
            users[username] = {"coins": 0, "solved_questions": 0}

        users[username]["coins"] += coins_awarded
        users[username]["solved_questions"] += 1
        total_mined_coins += coins_awarded

        # Save updated data to JSON file
        save_data({"users": users, "total_mined_coins": total_mined_coins})

        return redirect(url_for('leaderboard'))
    else:
        return redirect(url_for('home'))

@app.route('/leaderboard')
def leaderboard():
    sorted_users = sorted(users.items(), key=lambda x: x[1]["coins"], reverse=True)
    coin_value = total_supply / max(total_mined_coins, 1)
    return render_template('leaderboard.html', users=sorted_users, coin_value=coin_value)

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f"What is {num1} + {num2}?"
    answer = num1 + num2
    return question, answer

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/get_random_number/<int:min>/<int:max>')
def get_random_number(min, max):
    if min >= max:
        return jsonify({'error': 'Invalid input. Please enter valid numbers, with the minimum value less than the maximum value.'}), 400

    random_number = random.randint(min, max)
    return jsonify({'random_number': random_number})

if __name__ == '__main__':
    app.run()

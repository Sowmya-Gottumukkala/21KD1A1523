from flask import Flask, jsonify, request
import requests
from collections import deque
from time import time

app = Flask(__name__)

WINDOW_SIZE = 10
NUMBER_STORE = deque()
LAST_REQUEST_TIME = {}

# Helper function to fetch numbers from the test server
def fetch_numbers(number_id):
    urls = {
        'p': 'http://20.244.56.144/test/primes',
        'f': 'http://20.244.56.144/test/fibo',
        'e': 'http://20.244.56.144/test/even',
        'r': 'http://20.244.56.144/test/rand'
    }
    url = urls.get(number_id)
    if url is None:
        return None
    
    try:
        response = requests.get(url, timeout=0.5)  # 500 ms timeout
        response.raise_for_status()
        data = response.json()
        return data.get('numbers', [])
    except (requests.RequestException, ValueError):
        return None

# Route to handle number requests
@app.route('/numbers/<string:number_id>', methods=['GET'])
def get_numbers(number_id):
    global NUMBER_STORE, LAST_REQUEST_TIME

    if number_id not in ['p', 'f', 'e', 'r']:
        return jsonify({'error': 'Invalid number ID'}), 400

    current_time = time()
    numbers = fetch_numbers(number_id)

    if numbers is None:
        return jsonify({'error': 'Failed to fetch numbers or response took too long'}), 500

    # Update the store with the new numbers, ensuring uniqueness
    new_numbers = list(set(numbers) - set(NUMBER_STORE))
    if len(NUMBER_STORE) + len(new_numbers) > WINDOW_SIZE:
        while len(NUMBER_STORE) + len(new_numbers) > WINDOW_SIZE:
            NUMBER_STORE.popleft()

    NUMBER_STORE.extend(new_numbers)

    # Calculate the average
    avg = sum(NUMBER_STORE) / len(NUMBER_STORE) if NUMBER_STORE else 0

    # Response format
    response = {
        'windowPrevState': list(NUMBER_STORE),
        'windowCurrState': list(NUMBER_STORE),
        'numbers': numbers,
        'avg': round(avg, 2)
    }

    # Update last request time
    LAST_REQUEST_TIME[number_id] = current_time

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876, threaded=True)

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize a global counter variable
request_counter = 0

@app.route('/count-requests', methods=['GET'])
def count_requests():
    global request_counter
    request_counter += 1
    # Return the counter as a JSON response
    return jsonify({"request_count": request_counter})

@app.route('/reset-counter', methods=['POST'])
def reset_counter():
    global request_counter
    request_counter = 0
    # Return a confirmation message as JSON
    return jsonify({"message": "Counter has been reset.", "request_count": request_counter})

if __name__ == '__main__':
    app.run(debug=True)

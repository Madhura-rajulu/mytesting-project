from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

@app.route('/api/message')
def message():
    return jsonify({'message': 'heloo!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

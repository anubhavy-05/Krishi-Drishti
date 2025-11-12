from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Server is running!"

@app.route('/api/test')
def test():
    return jsonify({"status": "ok", "message": "API is working"})

if __name__ == '__main__':
    print("Starting simple test server...")
    app.run(debug=True, host='0.0.0.0', port=5000)

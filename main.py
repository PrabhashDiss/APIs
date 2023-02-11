from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def index():
    return "Hello, World!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "foo": "bar",
        "baz": 42
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000 ,debug=True)
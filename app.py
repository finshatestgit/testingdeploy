from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dialogflow-webhook', methods=['POST'])
def test_endpoint():
    return jsonify({"message": "Endpoint is working!"})

if __name__ == "__main__":
    app.run(debug=True)
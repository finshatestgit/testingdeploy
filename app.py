from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dialogflow-webhook', methods=['POST'])
def dialogflow_webhook():
    data = request.get_json()
    intent_name = data['queryResult']['intent']['displayName']

    # Handling only the default welcome intent
    if intent_name == "Default Welcome Intent":
        return jsonify({"fulfillmentText": "Welcome! This is a test response."})
    else:
        return jsonify({"fulfillmentText": "Sorry, I can only respond to the welcome intent in this test version."})

if __name__ == "__main__":
    app.run(debug=True)

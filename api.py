from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def receive_message():
    incoming_message = request.values.get('Body', '')
    # Process the incoming message here
    response = MessagingResponse()
    # Prepare the response to be sent back to the sender
    response.message("You said: " + incoming_message)
    return str(response)

if __name__ == "__main__":
    app.run()

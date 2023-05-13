import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
openai.api_key = "YOUR_API_KEY"

@app.route("/webhook", methods=['POST'])
def receive_message():
    incoming_message = request.values.get('Body', '')
    response = generate_chat_response(incoming_message)
    return str(response)

def generate_chat_response(user_message):
    chat_history = [
        {"role": "user", "content": user_message}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    assistant_response = response['choices'][0]['message']['content']

    twilio_response = MessagingResponse()
    twilio_response.message(assistant_response)

    return twilio_response

if __name__ == "__main__":
    app.run(host="localhost", port=int("5003"))

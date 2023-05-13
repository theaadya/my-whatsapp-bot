# mybot
## Description
A project that utilizes OpenAI's GPT-3.5 language model to provide automated responses to incoming messages on WhatsApp. It uses Flask to create a web server that listens for incoming messages, processes them using the OpenAI API, and sends back appropriate responses.

The goal of this project is to create a versatile chatbot that can handle a wide range of user inputs and provide meaningful and helpful responses.

## Features
- Receives incoming messages from WhatsApp
- Utilizes OpenAI's GPT-3.5 language model for automated responses
- Provides flexible and versatile conversation capabilities

## Prerequisites
- Python 3.6 or above
- Flask
- Twilio (for WhatsApp integration)
- ngrok (to forward the local port to a public URL)
- OpenAI API key

## Installation
1. Clone the repository: `git clone https://github.com/theaadya/mybot.git`
2. Navigate to the project directory: `cd mybot`
3. Install the required dependencies.

## Configuration
1. Obtain an OpenAI API key: Follow the OpenAI documentation to generate an API key.
2. Open the `app.py` file in a text editor.
3. Replace `"YOUR_API_KEY"` with your actual OpenAI API key.
4. Setup your Twilio account and obtain the contact number for your ChatBot.

## Usage
1. Start the Flask server: `python app.py`
2. Set up a public URL using ngrok.
3. Configure the Twilio webhook (avaialble in Sandbox Settings) to point to your server's public URL (`ngrok_public_URL/webhook`).
4. Ensure the server is accessible from the internet.
5. Test the chat assistant by sending messages to your WhatsApp number.

Note: Make sure that you have API tokens (free/paid) available for processing the requests.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or improvements, please submit a pull request or open an issue on the GitHub repository.

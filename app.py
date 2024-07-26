from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our TwiML response
    response = MessagingResponse()

    # Add a message
    response.message("The Robots are coming! Head for the hills!")

    return str(response)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
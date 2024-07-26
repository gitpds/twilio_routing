import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'



# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     """Respond to incoming messages with a friendly SMS."""
#     # Start our TwiML response
#     response = MessagingResponse()

#     # Add a message
#     response.message("The Robots are coming! Head for the hills!")

#     return str(response)



if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    print(f"Listening on port {port}")
    app.run(host='0.0.0.0', port=port)
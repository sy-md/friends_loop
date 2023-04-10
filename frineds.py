import json
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Replace with your Twilio account SID and auth token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# List of phone numbers to send messages to
phone_numbers = ['+16232971176']

# Send a message to each phone number
for number in phone_numbers:
    message = client.messages.create(
        to=number,
        from_= os.getenv("ATHENA_NUMBER"),
        body='How are you doing today? Please respond with your age.'
    )

# Save responses to a JSON file
with open('responses.json', 'w') as f:
    json.dump(message, f)

print('Responses saved to responses.json')




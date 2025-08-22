# make_call.py
from twilio.rest import Client
import os

# Load Twilio credentials from env vars or hardcode for testing
account_sid = os.getenv("TWILIO_ACCOUNT_SID", "xxxx")
auth_token = os.getenv("TWILIO_AUTH_TOKEN", "xxxxxx")
client = Client(account_sid, auth_token)

# Trigger outbound call
call = client.calls.create(
    to="‪+923235913086‬",  # callee’s real phone number
    from_="‪+1 406 812 4657‬",  # your Twilio number (must be verified in Twilio)
    url="https://0c7ecb7756cb.ngrok-free.app/answer"  # points to your Flask /answer
)

print(f"Outbound call started! SID: {call.sid}")

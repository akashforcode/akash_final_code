from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'ACb31e2c0607bfdf7a94056efeb6855b32'
auth_token = '387370462e5c2c9b09b199f28a1d7c99'
client = Client(account_sid, auth_token)

# Message details
from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox number
to_whatsapp_number = 'whatsapp:+919555711143'  # Your WhatsApp number
message_body = 'Hello from Twilio!'

# Send message
message = client.messages.create(
    body=message_body,
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

for i in range(10):
    message = client.messages.create(
    body=message_body,
    from_=from_whatsapp_number,
    to=to_whatsapp_number)
    print(f"Message SID: {message.sid}")


    
print(f"Message SID: {message.sid}")


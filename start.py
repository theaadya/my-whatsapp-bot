import os
from twilio.rest import Client

account_sid = 'AC338a93cc6c83efb67081be96124e6dd7'
auth_token = '866e05b4400e7a97223ada6927b4dc65'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Hello, there!',
                              to='whatsapp:+918851940193')

print(message.sid)

from twilio.rest import TwilioRestClient
import json

settings = json.load(open('/home/dev/sixpoints/settings.json'))

# Find these values at https://twilio.com/user/account
account_sid = settings['twilio']['sid']
auth_token = settings['twilio']['token']
client = TwilioRestClient(account_sid, auth_token)

to_num = settings['twilio']['to_num']
from_num = settings['twilio']['from_num']

message = client.messages.create(to=to_num, from_=from_num,
                                     body="What are you up to?")


#!/usr/bin/env python

from dialogflow import Dialogflow

# demo agent access token: e5dc21cab6df451c866bf5efacb40178
client_access_token = 'e5dc21cab6df451c866bf5efacb40178'
dialogflow = Dialogflow(client_access_token)
response = dialogflow.query('how are you')
print(response)
response = dialogflow.query('howz the weather today')
print(response)

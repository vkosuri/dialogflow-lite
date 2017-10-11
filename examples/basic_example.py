
from src.agent import ApiAi

# demo agent access token: e5dc21cab6df451c866bf5efacb40178
client_access_token = 'e5dc21cab6df451c866bf5efacb40178'
api_ai = ApiAi(client_access_token)
response = api_ai.query('how are you')
print(response)
response = api_ai.query('howz the weather today')
print(response)

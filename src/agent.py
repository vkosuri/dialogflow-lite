
import requests
import uuid


class ApiAi(object):
    # create session
    session = requests.Session()

    # Headers
    headers = {}

    session_id = uuid.uuid4().hex

    def __init__(self, url='https://api.api.ai/v1/query', client_access_token=None, headers={},
                 api_versioning='20150910', language='en', timezone='Asia/Kolkata'):
        """
        Create Session: create a HTTP session to a server
        """
        self.url = url

        self.headers = {
            'Authorization': 'Bearer ' + client_access_token,
        }

        self.session.headers.update(headers)
        self.session.mount('http://', requests.adapters.HTTPAdapter())
        self.session.mount('https://', requests.adapters.HTTPAdapter())

        self.api_versioning = api_versioning
        self.language = language
        self.timezone = timezone





# if __name__ == '__main__':
#     # demo agent access token: e5dc21cab6df451c866bf5efacb40178
#     client_access_token = 'e5dc21cab6df451c866bf5efacb40178'
#
#     api_ai = ApiAi(client_access_token);
#     response = api_ai.get_response('how are you')
#     print(response)
#     response = api_ai.get_response('howz the weather today')
#     print(response)

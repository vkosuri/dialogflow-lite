
import requests
import uuid


class ApiAi(object):
    # create session
    session = requests.Session()

    # Headers
    headers = {}

    session_id = uuid.uuid4().hex

    def __init__(self, **kwargs):
        """
        Create a HTTP session to a server
        :param url: API.AI base url
        :param client_access_token: client access token
        :param api_version: API version
        :param language: default locale language
        :param timezone: Current timezone
        """
        self.url = kwargs.get('query', 'https://api.api.ai/v1/')
        self.client_access_token = kwargs.get('client_access_token', '')
        self.developer_access_token = kwargs.get('developer_access_token', '')
        self.api_version = kwargs.get('api_version', '20150910')
        self.language = kwargs.get('language', 'en')
        self.timezone = kwargs.get('timezone', 'Asia/Kolkata')

        # Allow different speech recognition methods to be selected
        # See https://pypi.python.org/pypi/SpeechRecognition/
        self.recognizer_function = kwargs.get(
            'recognizer_function', 'recognize_sphinx'
        )

        self.headers = {
            'Authorization': 'Bearer ' + self.client_access_token,
        }

        self.session.headers.update(self.headers)
        self.session.mount('http://', requests.adapters.HTTPAdapter())
        self.session.mount('https://', requests.adapters.HTTPAdapter())

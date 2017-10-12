
import requests
import uuid


class Dialogflow(object):
    # create session
    session = requests.Session()

    # Headers
    headers = {}

    session_id = uuid.uuid4().hex

    def __init__(self, **kwargs):
        """
        Create a HTTP session to a Dialogflow server
        """
        self.base_url = kwargs.get('query', 'https://api.dialogflow.com/v1')
        self.client_access_token = kwargs.get('client_access_token', '')
        self.developer_access_token = kwargs.get('developer_access_token', '')
        self.api_version = kwargs.get('api_version', '20150910')
        self.language = kwargs.get('language', 'en')
        self.timezone = kwargs.get('timezone', 'Asia/Kolkata')
        verify = kwargs.get('verify', False)

        # Allow different speech recognition methods to be selected
        # See https://pypi.python.org/pypi/SpeechRecognition/
        self.recognizer_function = kwargs.get(
            'recognizer_function', 'recognize_sphinx'
        )

        self.headers = {
            'Authorization': 'Bearer ' + self.client_access_token,
        }

        if isinstance(verify, bool):
            self.session.verify = verify

        self.session.headers.update(self.headers)
        self.session.mount('http://', requests.adapters.HTTPAdapter())
        self.session.mount('https://', requests.adapters.HTTPAdapter())

        self.session.url = self.base_url

    class HTTPStatusException(Exception):
        """
        Exception raised when unexpected non-success HTTP
        status codes are returned in a response.
        """

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

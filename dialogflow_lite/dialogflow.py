#!/usr/bin/env python

from requests.adapters import HTTPAdapter
from requests.packages import urllib3
from dialogflow_lite.status import HTTP_200_SUCCESS, HTTP_200_DEPRECATED

import requests
import speech_recognition
import subprocess
import uuid


class DialogflowQueryException(Exception):
    """
    Exception raised when unexpected non-success HTTP
    status codes are returned in a response.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Dialogflow(object):
    # create session
    session = requests.Session()
    # Headers
    headers = {}
    session_id = uuid.uuid4().hex
    query_url = None
    query_response = None
    previous_query_response = None

    def __init__(self, **kwargs):
        """
        Create a HTTP session to a Dialogflow server
        """
        self.base_url = kwargs.get('url', 'https://api.dialogflow.com/v1')
        self.query_url = self.base_url + '/query'
        self.client_access_token = kwargs.get('client_access_token', '')
        self.developer_access_token = kwargs.get('developer_access_token', '')
        self.api_version = kwargs.get('api_version', '20150910')
        self.language = kwargs.get('language', 'en')
        self.timezone = kwargs.get('timezone', 'Asia/Kolkata')
        verify = kwargs.get('verify', False)

        if not self.client_access_token:
            raise DialogflowQueryException('Must have client access token to proceed.')

        # Allow different speech recognition methods to be selected
        # See https://pypi.python.org/pypi/SpeechRecognition/
        self.recognizer_function = kwargs.get(
            'recognizer_function', 'recognize_sphinx'
        )

        self.headers = {
            'Authorization': 'Bearer ' + self.client_access_token,
        }

        if not verify:
            urllib3.disable_warnings()

        if isinstance(verify, bool):
            self.session.verify = verify

        self.session.headers.update(self.headers)
        self.session.mount('http://', HTTPAdapter())
        self.session.mount('https://', HTTPAdapter())

        self.session.url = self.base_url

    def text_request(self, text):
        responses = []
        result = self._query(text)
        try:
            if result['status']['code'] == HTTP_200_SUCCESS:
                for msg in result['result']['fulfillment']['messages']:
                    responses.append(msg['speech'])
        except KeyError:
            print('No response from the agent')
        except DialogflowQueryException:
            print(
                'Failed to get response url: {} with status: {}'.format(self.query_url, result['status']['errorType']))

        return responses

    def _query(self, text):
        """
        Takes natural language text and information as query parameters and returns information as JSON.
        """
        params = (
            ('v', self.api_version),
            ('query', text),
            ('lang', self.language),
            ('sessionId', self.session_id),
            ('timezone', self.timezone),
        )
        # store query_response if required
        if self.query_response:
            self.previous_query_response = self.query_response

        self.query_response = result = self.session.get(url=self.query_url, params=params).json()

        return result

    def voice_request(self):
        # Start jack control
        self._attempt_jack_control_start()

        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        recognizer_function = getattr(recognizer, self.recognizer_function)

        try:
            result = recognizer_function(audio)
            return result
        except speech_recognition.UnknownValueError:
            return 'I am sorry, I could not understand that.'
        except speech_recognition.RequestError as e:
            m = 'My speech recognition service has failed. {0}'
            return m.format(e)

    def _attempt_jack_control_start(self):
        """
        Jack is a program that can be used to get audio
        input from your system. This command will try
        to start it when your program runs.
        """
        import warnings

        try:
            subprocess.call(['jack_control', 'start'])
        except DialogflowQueryException:
            # Note: jack_control is not a valid command in Windows
            warnings.warn(
                'Unable to start jack control.',
                RuntimeWarning
            )

    def _validate_status_code(self, response):
        code = response['status']['code']
        if code not in [HTTP_200_SUCCESS, HTTP_200_DEPRECATED]:
            raise DialogflowQueryException('{} status code received'.format(code))

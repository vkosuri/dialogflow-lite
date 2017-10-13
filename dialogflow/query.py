
from .dialogflow import Dialogflow
from .status import HTTP_200_SUCCESS, HTTP_200_DEPRECATED

import speech_recognition
import subprocess


class Query(Dialogflow):
    query_response = {}
    previous_query_response = {}
    query_url = None

    def __init__(self, **kwargs):
        super(Query, self).__init__(**kwargs)
        self.query_url = self.base_url + '/query'

        self.headers = {
            'Authorization': 'Bearer ' + self.client_access_token,
            'Content-Type': 'Application/json'
        }

        self.session.headers.update(self.headers)

    def query(self, text):
        """
        Takes natural language text and information as query parameters and returns information as JSON.
        :param text: Input text
        :return: response message
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

    def text_request(self, text):
        responses = []
        result = self.query(text)
        if result['status']['code'] == HTTP_200_SUCCESS:
            for msg in result['result']['fulfillment']['messages']:
                responses.append(msg['speech'])
        else:
            raise self.HTTPStatusException(
                'Failed to get response url: {} with status: {}'.format(self.query_url, result['status']['errorType'])
            )

        return responses

    def voice_request(self):
        # Start jack control
        self.attempt_jack_control_start()

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

    def attempt_jack_control_start(self):
        """
        Jack is a program that can be used to get audio
        input from your system. This command will try
        to start it when your program runs.
        """
        import warnings

        try:
            subprocess.call(['jack_control', 'start'])
        except self.DialogflowQueryException:
            # Note: jack_control is not a valid command in Windows
            warnings.warn(
                'Unable to start jack control.',
                RuntimeWarning
            )

    def _validate_status_code(self, response):
        code = response['status']['code']
        if code not in [HTTP_200_SUCCESS, HTTP_200_DEPRECATED]:
            raise self.HTTPStatusException('{} status code received'.format(code))

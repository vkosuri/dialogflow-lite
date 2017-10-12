
from .agent import Dialogflow
from .status import HTTP_200_SUCCESS, HTTP_200_DEPRECATED


class Query(Dialogflow):
    query_response = {}
    previous_query_response = {}

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

    def get_response_message(self, text):
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

    def _validate_status_code(self, response):
        code = response['status']['code']
        if code not in [HTTP_200_SUCCESS, HTTP_200_DEPRECATED]:
            raise self.HTTPStatusException('{} status code received'.format(code))

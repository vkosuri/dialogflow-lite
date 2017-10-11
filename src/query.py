
from .agent import Dialogflow


class Query(Dialogflow):
    def query(self, text):
        """
        Takes natural language text and information as query parameters and returns information as JSON.
        :param text: Input text
        :return: JSON response
        """
        query_url = self.uri + '/query'
        params = (
            ('v', self.api_versioning),
            ('query', text),
            ('lang', self.language),
            ('sessionId', self.session_id),
            ('timezone', self.timezone),
        )
        responses = []
        result = self.s.get(url=self.url, params=params).json()
        if result['status']['errorType'] == 'success':
            for msg in result['result']['fulfillment']['messages']:
                responses.append(msg['speech'])
        else:
            print('Failed to response from: ' + query_url)

        return responses

from unittest import TestCase
from mock import Mock
from src.query import Query
from src import agent


class MockResponse(object):
    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data

    def json(self):
        return self.data


def mock_get_response(*args, **kwargs):
    url = kwargs['url']
    endpoints = {
        'https://api.dialogflow.com/v1/query': MockResponse(200, {
            "id": "b340a1f7-abee-4e13-9bdd-5e8938a48b7d",
            "timestamp": "2017-02-09T15:38:26.548Z",
            "lang": "en",
            "result": {
                "source": "agent",
                "resolvedQuery": "my name is Sam and I live in Paris",
                "action": "greetings",
                "actionIncomplete": "false",
                "parameters": {},
                "contexts": [],
                "metadata": {
                  "intentId": "9f41ef7c-82fa-42a7-9a30-49a93e2c14d0",
                  "webhookUsed": "false",
                  "webhookForSlotFillingUsed": "false",
                  "intentName": "greetings"
                },
                "fulfillment": {
                    "speech": "Hi Sam! Nice to meet you!",
                    "messages": [
                        {
                            "type": 0,
                            "speech": "Hi Sam! Nice to meet you!"
                        }
                    ]
                },
                "score": 1
            },
            "status": {
                "code": 200,
                "errorType": "success"
            },
            "sessionId": "4b6a6779-b8ea-4094-b2ed-a302ba201815"
        })
    }

    return endpoints[url]


class QueryTests(TestCase):
    def setUp(self):
        super(QueryTests, self).setUp()
        self.dialogflow = Query(
            url='https://api.dialogflow.com/v1',
            client_access_token='adaf757eb6714a4d',
        )
        agent.requests.Session.get = Mock(side_effect=mock_get_response)

    def test_validate_status_code_200(self):
        response = self.dialogflow.query('my name is Sam and I live in Paris')

        try:
            self.dialogflow._validate_status_code(response)
        except Query.HTTPStatusException:
            self.fail('Test raised HTTPStatusException unexpectedly!')

    def test_validate_response(self):
        responses = self.dialogflow.get_response_message('my name is Sam and I live in Paris')
        self.assertEqual(responses[0], 'Hi Sam! Nice to meet you!')

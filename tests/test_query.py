#!/usr/bin/env python

from dialogflow import Dialogflow
from dialogflow import dialogflow
from mock import Mock
from unittest import TestCase


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


def mock_get_without_response(*args, **kwargs):
    """
    Usually this will happen if we used dummy client access token
    """
    url = kwargs['url']
    endpoints = {
        'https://api.dialogflow.com/v1/query': MockResponse(200, {
            'id': 'b75bb996-cee3-41cd-a6eb-dd081c766fe0',
            'timestamp': '2017-10-13T19:08:46.599Z',
            'lang': 'en',
            'sessionId': '8c3d0ff681a1460ba6ed45dec4eda2fb',
            'result': {
                'contexts': [],
                'score': 0.0,
                'fulfillment': {
                    'speech': ''
                },
                'resolvedQuery': 'how are you',
                'metadata': {},
                'source': 'agent'
            },
            'status': {
                'errorType': 'success',
                'code': 200
            }
        })
    }
    return endpoints[url]


class QueryGetSuccessTests(TestCase):
    def setUp(self):
        super(QueryGetSuccessTests, self).setUp()
        self.dialog = Dialogflow(
            url='https://api.dialogflow.com/v1',
            client_access_token='adaf757eb6714a4d',
        )
        dialogflow.requests.Session.get = Mock(side_effect=mock_get_response)

    def test_validate_status_code_200(self):
        response = self.dialog._query('my name is Sam and I live in Paris')

        try:
            self.dialog._validate_status_code(response)
        except Dialogflow.DialogflowQueryException:
            self.fail('Test raised HTTPStatusException unexpectedly!')

    def test_validate_response_text(self):
        responses = self.dialog.text_request('my name is Sam and I live in Paris')
        self.assertEqual(responses[0], 'Hi Sam! Nice to meet you!')

    def test_validate_response(self):
        response = self.dialog._query('my name is Sam and I live in Paris')
        self.assertEqual(response['sessionId'], '4b6a6779-b8ea-4094-b2ed-a302ba201815')
        self.assertEqual(response['result']['score'], 1)
        self.assertEqual(response['result']['metadata']['intentName'], 'greetings')


class QueryGetSuccessWithoutResponseTests(TestCase):
    def setUp(self):
        super(QueryGetSuccessWithoutResponseTests, self).setUp()
        self.dialog = Dialogflow(
            url='https://api.dialogflow.com/v1',
            client_access_token='adaf757eb6714a4d',
        )
        dialogflow.requests.Session.get = Mock(side_effect=mock_get_without_response)

    def test_validate_sucess_without_response(self):
        response = self.dialog._query('how are you')
        try:
            self.dialog._validate_status_code(response)
        except Dialogflow.DialogflowQueryException:
            self.fail('Test raised HTTPStatusException unexpectedly!')

    def test_validate_exception(self):
        try:
            self.dialog.text_request('how are you')
        except KeyError:
            self.assertEqual("KeyError: 'messages'", KeyError.__cause__)

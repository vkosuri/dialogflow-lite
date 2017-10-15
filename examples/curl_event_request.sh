#!/usr/bin/env bash
curl -H "Content-Type: application/json; charset=utf-8" -H "Authorization: Bearer YOUR_ACCESS_TOKEN" --data "{'query':'and for tomorrow', 'timezone':'GMT-5', 'lang':'en', 'contexts':[{ 'name': 'weather', 'parameters':{'city': 'London'}, 'lifespan': 4}], 'sessionId':'1234567890'}" "https://api.dialogflow.com/v1/query?v=20150910"

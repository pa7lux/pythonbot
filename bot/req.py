from requests import get, post
import json

def call(url, method='GET', data={}, headers={}):
	if method is 'GET':
		request = get(url, params=data, headers=headers)
	else:
		request = post(url, data=json.dumps(data), headers=headers)

	request.encoding = 'utf-8'

	return request.text

def _get(url, data={}, headers={}):
	return call(url, 'GET', data, headers)

def _post(url, data={}, headers={}):
	return call(url, 'POST', data, headers)
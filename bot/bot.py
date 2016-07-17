from bot import req
import json

from django.http import HttpResponse

token = '254968587:AAE1TDdb0f__jl_LDKkpCjtd2eE4UHsTn1Y'
api = 'https://api.telegram.org/bot{token}/{method}'

chat_id = '183765525'

def call_telegram_method(method, data={}):
	return req._get(api.format(token=token, method=method), data)

def init():
	result = call_telegram_method('setWebhook', {
		'url': 'https://mcs-python-bot.herokuapp.com/bot'
	})
	print(result)
	send(chat_id, 'Server started')


def send(chat_id, message):
	return call_telegram_method('sendMessage', {
		'chat_id': chat_id,
		'text': message
	})

def process(request):
	data = json.loads(request.body, encoding='utf-8')

	message = data.get('message', {})
	text = message.get('text')
	sender_id = message.get('from', {}).get('id')

	if message == 'Hello':
		send(sender_id, 'Hello yourself')

	return HttpResponse('test')
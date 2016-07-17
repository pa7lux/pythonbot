from bot import req
import json
import codecs

reader = codecs.getreader("utf-8")

from django.http import HttpResponse

token = '254968587:AAE1TDdb0f__jl_LDKkpCjtd2eE4UHsTn1Y'
api = 'https://api.telegram.org/bot{token}/{method}'
weather_api_key = '54995be76b41b08edc2635c6ba445725'

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
	body = request.read().decode('utf-8')
	data = json.loads(body)

	print(data)
	
	message = data.get('message', {})
	text = message.get('text')
	sender_id = message.get('from', {}).get('id')


	if text.lower() == 'hello':
		send(sender_id, 'Hello yourself')

	if text.lower() == 'cat':
		call_telegram_method('sendSticker', {
			'chat_id': sender_id,
			'sticker': 'BQADAgADBQADIyIEBsnMqhlT3UvLAg'
		})

	return HttpResponse('')
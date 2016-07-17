from django.conf.urls import include, url
from django.contrib import admin

from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello')

def some_url(request, path):
	gets = request.GET
	print(gets)

	response = path + '<br>'
	
	for key in gets:
		print('Key is:' + key)
		print('Value is:' + gets.get(key))

		response += '{key} = {value} <br>'.format(key=key, value=gets.get(key))

	return HttpResponse(response)

urlpatterns = [
	url(r'^$', index),
	url(r'^bot$', 'bot.bot.process')
]

from django.shortcuts import render
from django.http import HttpResponse
import requests
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
print(env('MAILGUN_API_KEY'))


def send_simple_message(name, email, message):
    return requests.post(
        env('MAILGUN_URL'),
        auth=("api", env('MAILGUN_API_KEY')),
        data={"from": "{} <mailgun@{}>".format(name, env('SEND')),
              "to": ["ayaung@163.com",],
              "subject": "Double Yang website message",
              "text": "name: " + name + "  email: " + email + "  " + message})


def home(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        send_simple_message(name, email, message)
        print("Message sent")
    return render(request, 'me.html')

# Create your views here.
from django.http import HttpResponse
from apps.core.rabbitmq import RabbitMQ
from django.shortcuts import render

def index(request):
    return render(request, 'rabbit/home.html')

def send_message(request):
    queue_name = 'my_queue'
    message = 'Hello world!'
    RABBITMQ_HOST ='localhost'
    RABBITMQ_PORT='15672'
    rabbitmq = RabbitMQ(RABBITMQ_HOST, RABBITMQ_PORT)
    rabbitmq.publish_message(queue_name, message)
    rabbitmq.close()

    return HttpResponse('Message sent!')

def receive_messages(request):
    queue_name = 'my_queue'

    def callback(message):
        print(message)

    RABBITMQ_HOST ='localhost'
    RABBITMQ_PORT='15672'
    rabbitmq = RabbitMQ(RABBITMQ_HOST, RABBITMQ_PORT)
    rabbitmq.consume_messages(queue_name, callback)
    rabbitmq.close()

    return HttpResponse('Messages received!')
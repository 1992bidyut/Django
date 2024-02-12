from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return render(request, 'rabbitmq.html')


def chat_data(request):
    return render(request, 'chat_data.html')


def mqtt(request):
    return render(request, 'rabbitmq.html')

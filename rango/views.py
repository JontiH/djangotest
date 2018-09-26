from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):

    context_dict = {'boldmessage': "silly stuff"}

    response = render(request, 'rango/index.html', context=context_dict)

    return response



def about(request):
    response =  HttpResponse("A TO THE B TO THE O U T. I LIKE TO DO STUFF AND I DRINK A LOT OF TEA")
    response.write('<p><a href= "/" >click here to go to BACK TO WHENCE U CAME</a></p>')
    return response

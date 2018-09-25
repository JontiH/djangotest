from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    response = HttpResponse("YO WASSUP DOG")
    response.write('<p><a href= "rango/about/" >click here to go to about</a></p>')
    response.write("<p>ggg</p>")
    return response



def about(request):
    response =  HttpResponse("A TO THE B TO THE O U T. I LIKE TO DO STUFF AND I DRINK A LOT OF TEA")
    response.write('<p><a href= "/" >click here to go to BACK TO WHENCE U CAME</a></p>')
    return response

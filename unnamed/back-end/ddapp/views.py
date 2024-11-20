from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def sample_data(request):
    data = {"message": "Hello from Django!"}
    return Response(data)


def index(request):
    return HttpResponse("Welcome")
from django.shortcuts import render
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from wsgiref.util import FileWrapper
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'api/index.html', context=None)

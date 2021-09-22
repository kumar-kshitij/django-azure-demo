import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import os
from django.http import HttpResponse
import random
# Create your views here.
def index(request):
    return render(request, 'api/index.html', context=None)

class DummyView(APIView):
    def get(self,request):
        json_body={}
        param = self.request.query_params.get('q', None)
        if param == 'orders':
            json_body = [
                    {
                        "orderId":"EFHNCIDJ2143534TF",
                        "productId": "TDHDMH5GRSPZ3DNM",
                        "title": "Newhide Designer",
                        "orderDate": "25/09/2021",
                        "statusDetails":"In Transit at gurgaon",                        
                    },
                    {
                        "orderId":"EYHNCIWE2143454TF",
                        "productId": "9788129135728",
                        "title": "Toshiba 81 cm LED TV HD Ready",
                        "orderDate": "20/09/2021",
                        "statusDetails":"In Transit at kolkata",                        
                    },
                    {
                        "orderId":"EYRTYIWE2144584TF",
                        "productId": "TVSDD2DSPYU3BFZY",
                        "title": "Titan Analog Watch",
                        "orderDate": "01/08/2021",
                        "statusDetails":"Delivered",                        
                    }
                ]
        elif param == 'cc':
            json_body = [
                {
                    "cardName":"AmEx",
                    "cardNumber":"343434343434343",
                    "balance": "$14534",
                    "billDue":"07/10/2021"
                },
                {
                    "cardName":"Visa",
                    "cardNumber":"4444333322221111",
                    "balance": "$9462",
                    "billDue":"14/10/2021"
                }
            ]
        elif param =='supercoin_bal':
            json_body = {
                'balance' : random.randint(10, 1000)
            }
            
            

        return Response(json_body,status = status.HTTP_200_OK)

        
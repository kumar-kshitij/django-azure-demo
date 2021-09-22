import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.http import HttpResponse
import random
import os
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


class V1View(APIView):
    def post(self, request):
        
        CHATBOT_API = os.environ['CHATBOT_BASE_URL']+'/webhooks/rest/webhook'
        COGNITIVE_API='https://api.cognitive.microsofttranslator.com/translate'
        received_text = request.data['message']
        received_lang = 'en'
        if 'language' in request.data:
            received_lang=request.data['language']
        
        if received_lang!='en':
        
            params = {
                'api-version': '3.0',
                'from': received_lang,
                'to': 'en'
            }

            headers = {
                'Ocp-Apim-Subscription-Key': '9b892b453868462e8ef70b511fa84e77',
                'Ocp-Apim-Subscription-Region':'global',
            }
            payload = [{
                'text': received_text
            }]
            cognitive_response = requests.post(COGNITIVE_API, params=params, headers=headers, json=payload)
            received_text = cognitive_response.json()[0]['translations'][0]['text']
        
        print(received_text)
        myobj = {
        "sender": "Frontend",
        "message": received_text,
        }
        x = requests.post(CHATBOT_API, json = myobj)
        json_data = x.json()
        reply=[]
        for i in range(len(json_data)):
            resp_text = json_data[i]['text']
            if received_lang!='en':
            
                params = {
                    'api-version': '3.0',
                    'from': 'en',
                    'to': received_lang
                }

                headers = {
                    'Ocp-Apim-Subscription-Key': '9b892b453868462e8ef70b511fa84e77',
                    'Ocp-Apim-Subscription-Region': 'global',
                }
                payload = [{
                    'text': resp_text
                }]
                cognitive_response = requests.post(COGNITIVE_API, params=params, headers=headers, json=payload)
                resp_text = cognitive_response.json()[0]['translations'][0]['text']
                    
            
            reply.append(resp_text)
        
        return Response({"bot_reply":reply},status=status.HTTP_200_OK)
        
    def get(self,request):
        return Response(status = status.HTTP_204_NO_CONTENT)
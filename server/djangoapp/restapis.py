# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv
import requests
from django.http import JsonResponse
import logging

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logger.error(f'HTTP error occurred: {http_err}')
        return JsonResponse({'error': 'HTTP error occurred', 'details': str(http_err)}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f'Network exception occurred: {req_err}')
        return JsonResponse({'error': 'Network exception occurred', 'details': str(req_err)}, status=500)

def analyze_review_sentiments(text):
    print(sentiment_analyzer_url)
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
# Add code for posting review

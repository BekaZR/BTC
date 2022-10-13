from django.shortcuts import render
import requests
import json


def index(request):
    response = requests.get(url="https://yobit.net/api/3/info")

    list_currencly = json.loads(response.text).get('pairs').keys()
    
    if request.method == 'GET':
        
        context = {
            "list_currencly": list_currencly,
            }
        return render(request, 'mainapp/index.html', context)
    
    if request.method == "POST":
        method_ = request.POST.get('method')
        currencly = request.POST.get('currencly')
        if method_ == "depth":
            data = requests.get(url=f"https://yobit.net/api/3/depth/{currencly}?ignore_invalid=1").text
            context = {
                "asks": json.loads(data).get(f'{currencly}').get('asks'),
                "bids": json.loads(data).get(f'{currencly}').get('bids'),
                "list_currencly": list_currencly,
                }
            print("\n"*10, data)
            return render(request, 'mainapp/index.html', context)
    


def depth(request):
    if request.method == "POST":
        method_ = request.POST.get('method')
        currencly = request.POST.get('currencly')
        if method_ == "depth":
            data = requests.get(url=f"https://yobit.net/api/3/depth/{currencly}?ignore_invalid=1").text
            context = {
                "asks": json.loads(data).get(f'{currencly}').get('asks'),
                "bids": json.loads(data).get(f'{currencly}').get('bids'),
                }
            print("\n"*10, data)
            return render(request, 'mainapp/depth.html', context)
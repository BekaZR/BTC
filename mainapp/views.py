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


def action_(request):
    if request.method == "POST":
        method_ = request.POST.get('method')
        currencly = request.POST.get('currencly')
        if method_ == "depth":
            data = requests.get(url=f"https://yobit.net/api/3/{method_}/{currencly}?ignore_invalid=1").text
            context = {
                "data": data,
                }
            return render(request, 'mainapp/depth.html', context)
    



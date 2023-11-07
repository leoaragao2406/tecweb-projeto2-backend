from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.http import HttpResponse
from .models import Coin
from .serializers import CoinSerializer


def index(request):
    return HttpResponse("Olá! essa é minha API")

@api_view(['GET', 'POST', 'DELETE'])
def api_user_infos(request, user_id):
    try:
        coin = Coin.objects.get(id=user_id)
    except Coin.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        new_user_data = request.data
        coin.title = new_user_data['title']
        coin.action = new_user_data['action']
        coin.value = new_user_data['value']
        coin.quant = new_user_data['quant']
        coin.save()
    
    if request.method == 'DELETE':
        coin.delete()
        return HttpResponse(status=204)

    serialized_infos = CoinSerializer(coin)
    return Response(serialized_infos.data)

@api_view(['GET', 'POST'])
def api_user_all(request):
    if request.method == 'POST':
        new_user_data = request.data
        new_user = Coin(title = new_user_data['title'],
                        action = new_user_data['action'],
                        value = new_user_data['value'],
                        quant = new_user_data['quant'])
        
        new_user.save()

    users_all = Coin.objects.all()
    serialized_infos = CoinSerializer(users_all, many = True)
    return Response(serialized_infos.data)

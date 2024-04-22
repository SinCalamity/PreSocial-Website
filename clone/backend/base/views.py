from django.shortcuts import render
from django.http import JsonResponse
from base.creators import creators
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request): 
    routes = [
        'api/creator/',
        'api/creator/create/',
        'api/creator/upload/',
        'api/creator/<id>/reviews',
        'api/creator/top/',
        'api/creator/<id>/',
        'api/creator/delete/<id>',
        'api/creator/<update>/<id>',
    ]
    return Response(routes)
@api_view(['GET'])
def getCreators(request):

    return JsonResponse(creators, safe=False)

@api_view(['GET'])
def getCreator(request, pk):
    creator = None
    for i in creators:
        if i['_id'] == pk:
            creator = i
            break
        return Response(creator)

# Create your views here.

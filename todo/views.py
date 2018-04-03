from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
@csrf_exempt
def todo_list(request):
    if request.method == "GET":
        tasks = Task.objects.filter(is_active=True)
        ser = TaskSerializer(tasks, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        print(request.body)
        data = JSONParser().parse(request)
        ser = TaskSerializer(data=data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def todo_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id, is_active=True)
    except Exception as e:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ser = TaskSerializer(task)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        ser = TaskSerializer(task, data=data)

        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=200)
        return JsonResponse(ser.errors, status=400)

    elif request.method == "DELETE":
        data = {
            "is_active": False,
        }
        ser = TaskSerializer(task, data=data)

        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=200)
        return JsonResponse(ser.errors, status=400)

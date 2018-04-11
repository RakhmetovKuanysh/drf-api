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
def contacts_list(request):
    try:
        if request.method == "GET":
            contacts = Contact.objects.filter(is_active=True)
            ser = ContactSerializer(contacts, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            data = JSONParser().parse(request)
            ser = ContactSerializer(data=data)

            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def contact_detail(request, contact_id):
    try:
        try:
            contact = Contact.objects.get(pk=contact_id, is_active=True)
        except Exception as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            ser = ContactSerializer(contact)
            return Response(ser.data, status=status.HTTP_200_OK)

        elif request.method == "PUT":
            data = JSONParser().parse(request)
            ser = ContactSerializer(contact, data=data)

            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_200_OK)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            data = {
                "is_active": False,
            }
            ser = ContactSerializer(contact, data=data)

            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_200_OK)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

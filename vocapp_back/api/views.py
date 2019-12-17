from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User # STEP 1: Import the user


from foundation.models import Daily,Vocabulary


from rest_framework import status, response, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from api.serializers.gateway import RegisterSerializer, LoginSerializer
from api.serializers.dashboard import VocaddSerializer

import csv


#----gateway----


class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data,
        )



class LoginAPI(views.APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={
            'request': request,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                 'details': 'You have been logged in successfully!'
            },
        )




class LogoutAPI(views.APIView):
    def post(self,request):
        try:
            logout(request)
            return response.Response(
                status=status.HTTP_200_OK,
                data={
                 "was_logged_out": True,
                 "reason": None,
            })
        except Exception as e:
            print(e)
            return response.Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                 "was_logged_out": False,
                 "reason": str(e),
            })
        return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                'ERROR' : str(e)
                })


# -----Dashboard------
def post_instruments_create_api(request):
    name = request.POST.get("name")
    print(name)
    try:
        instrument = Instrument.objects.create(
            name=name,
            user=request.user
        )
        print("INSTRUMENT ID", instrument.id)
        return JsonResponse({
         'was_created': True,
        })
    except Exception as e:
        return JsonResponse({
         'was_created': False,
         'reason': str(e),
        })



class VocAddAPI(views.APIView):
    def post(self, request):
        serializer = VocaddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data,
        )

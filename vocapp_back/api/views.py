

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User # STEP 1: Import the user


from foundation.models import Instrument,TimeSeriesDatum,Sensor



from rest_framework import status, response, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from api.serializers.gateway import RegisterSerializer, LoginSerializer
from api.serializers.dashboard import DashboardSerializer
from api.serializers.instrument import InstrumentRetrieveSerializer
from api.serializers.sensor import SensorRetrieveSerializer
import csv





# ---- homepage -----



def api_version(request):
    return JsonResponse({'version': 'Melody'})


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


def post_logout_api(request):
    try:
        logout(request)
        return JsonResponse({
             "was_logged_out": True,
             "reason": None,
        })
    except Exception as e:
        print(e)
        return JsonResponse({
             "was_logged_out": False,
             "reason": str(e),
        })

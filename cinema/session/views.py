from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
#from django.contrib.auth.models import User

from session.models import *


class GetAllFilms(APIView):

    def get(self, request):
        #films = Film.objects.all()
        return Response('test')

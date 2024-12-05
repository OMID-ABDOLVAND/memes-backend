from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from airdrops.models import Account
from .serializers import AirdropParticipantSerializer

class RegisterWalletView(APIView):
    def post(self, request):
        serializer = AirdropParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Wallet registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

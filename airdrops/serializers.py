from rest_framework import serializers
from airdrops.models import Account


class AirdropParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['wallet_address', 'email']


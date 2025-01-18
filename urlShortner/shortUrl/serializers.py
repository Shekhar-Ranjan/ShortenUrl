from rest_framework import serializers
from .models import URL, Analytics

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['original_url', 'short_url', 'creation_time', 'expiry_time']

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = ['short_url', 'access_time', 'ip_address']

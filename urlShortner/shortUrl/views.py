from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URL, Analytics
from .serializers import URLSerializer, AnalyticsSerializer
# import datetime
from datetime import datetime, timedelta

class ShortenURLView(APIView):
    def post(self, request):
        data = request.data
        original_url = data.get('original_url')
        expiry_hours = data.get('expiry_hours', 24)

        if not original_url:
            return Response({'error': 'Original URL is required'}, status=status.HTTP_400_BAD_REQUEST)

        expiry_time = datetime.now() + timedelta(hours=expiry_hours)
        url, created = URL.objects.get_or_create(original_url=original_url, defaults={'expiry_time': expiry_time})

        serializer = URLSerializer(url)
        return Response(serializer.data)

class RedirectView(APIView):
    def get(self, request, short_url):
        url = get_object_or_404(URL, short_url=short_url)

        if now() > url.expiry_time:
            return Response({'error': 'URL has expired'}, status=status.HTTP_410_GONE)

        # Log analytics
        Analytics.objects.create(short_url=url, ip_address=request.META.get('REMOTE_ADDR'))

        return redirect(url.original_url)

class AnalyticsView(APIView):
    def get(self, request, short_url):
        url = get_object_or_404(URL, short_url=short_url)
        analytics = url.analytics.all()
        serializer = AnalyticsSerializer(analytics, many=True)
        return Response(serializer.data)

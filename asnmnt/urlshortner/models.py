from django.db import models
import hashlib
import time

class URL(models.Model):
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=10, unique=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    expiry_time = models.DateTimeField()
    password = models.CharField(max_length=128, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate short URL based on hash
        if not self.short_url:
            self.short_url = hashlib.md5(self.original_url.encode()).hexdigest()[:6]
        super().save(*args, **kwargs)

class Analytics(models.Model):
    short_url = models.ForeignKey(URL, on_delete=models.CASCADE, related_name='analytics')
    access_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
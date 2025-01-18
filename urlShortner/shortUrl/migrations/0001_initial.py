# Generated by Django 5.1.5 on 2025-01-18 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=500)),
                ('short_url', models.CharField(max_length=10, unique=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('expiry_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_time', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('short_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='shortUrl.url')),
            ],
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-15 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savesounds', '0005_accesstoken_refresh_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesstoken',
            name='refresh_token',
        ),
    ]

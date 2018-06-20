import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import soundcloud

# Create your views here.
from .models import AccessToken, User


def index(request):
    context = {'user': 'Some user'}  # TODO: actually swap out with logged in user
    return render(request, 'savesounds/index.html', context)


def home(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'savesounds/home.html', context)


def likes(request, username):
    user = User.objects.get(username=username)
    access_token = user.access_token
    client = soundcloud.Client(access_token=access_token)

    userId = client.get('/me').obj['id']
    activities = client.get('/me/activities').obj
    tracks = client.get(f'/users/{userId}/favorites')

    # for track in tracks:
    # for k, v in activities.items():
    #     print(f'ACTIVITYYYYYYYYYYYYYYYYYYYYYYYY--------------------------{k}: {v}')
    context = {'tracks': tracks}
    return render(request, 'savesounds/likes.html', context)


def reposts(request, username):
    user = User.objects.get(username=username)
    access_token = user.access_token
    client = soundcloud.Client(access_token=access_token)
    activities = client.get('/me/activities').obj
    return HttpResponse("Things I have Reposted")


def login(request):
    client = soundcloud.Client(
        client_id="1NPiMO4NA1swhQ0NVYdct6qT95r7w281",
        client_secret="0QRconN6Vf1vQJU52X1JElduUIIK9IvZ",
        redirect_uri="http://localhost:8080/safe-and-soundcloud/callback.html"
    )
    return HttpResponseRedirect(client.authorize_url())


def auth_callback(request):
    client = soundcloud.Client(
        client_id="1NPiMO4NA1swhQ0NVYdct6qT95r7w281",
        client_secret="0QRconN6Vf1vQJU52X1JElduUIIK9IvZ",
        redirect_uri="http://localhost:8080/safe-and-soundcloud/callback.html")
    access_token_data = client.exchange_token(request.GET.get('code')).obj
    user_data = client.get('/me').obj
    for attr in user_data:
        print(f'USER INFO: {attr}: {user_data[attr]}')

    try:
        user = User.objects.get(username=user_data['username'])
        user.access_token = access_token_data['access_token']
        user.save()
    except:
        user = User(username=user_data['username'],
                    permalink=user_data['permalink'],
                    permalink_url=user_data['permalink_url'],
                    avatar_url=user_data['avatar_url'],
                    access_token=access_token_data['access_token'])
        user.save()

    return HttpResponseRedirect(f'/home/{user.username}')

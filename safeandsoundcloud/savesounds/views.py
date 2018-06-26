import json

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import soundcloud
from django.views import generic

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View

from .models import User
from django.contrib.auth.decorators import login_required


def index(request):
    context = {'user': 'Some user'}  # TODO: actually swap out with logged in user
    return render(request, 'savesounds/index.html', context)


class HomeView(View):
    template_name = "savesounds/home.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/")
        else:
            return render(request, self.template_name, context=None)


@login_required
def home(request):
    user = request.user
    context = {'user': user}
    return render(request, 'savesounds/home.html', context)


@login_required
def likes(request):
    user = request.user
    # user = User.objects.get(username=username)
    # access_token = user.access_token
    client = soundcloud.Client(access_token=user.access_token)

    userId = client.get('/me').obj['id']
    # activities = client.get('/me/activities').obj
    tracks = client.get(f'/users/{userId}/favorites')

    # for track in tracks:
    # for k, v in activities.items():
    #     print(f'ACTIVITYYYYYYYYYYYYYYYYYYYYYYYY--------------------------{k}: {v}')
    context = {'tracks': tracks}
    return render(request, 'savesounds/likes.html', context)


@login_required
def reposts(request, username):
    user = User.objects.get(username=username)
    access_token = user.access_token
    client = soundcloud.Client(access_token=access_token)
    activities = client.get('/me/activities').obj
    return HttpResponse("Things I have Reposted")


def custom_login(request):
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
        login(request, user)
        if user.access_token is not None:
            pass
        else:
            user.access_token = access_token_data['access_token']
            user.save()
    except:
        # user = User.objects.create_user(user_data['username'], , 'johnpassword')

        user = User(username=user_data['username'],
                    permalink=user_data['permalink'],
                    permalink_url=user_data['permalink_url'],
                    avatar_url=user_data['avatar_url'],
                    access_token=access_token_data['access_token'])
        user.save()

    return HttpResponseRedirect(f'/home/')


#
# class CustomLoginView(LoginView):
#     template_name = "savesounds/login.html"
#
#
#
# class LikesView(AccessMixin, generic.ListView):
#
#     template_name = "savesounds/likes.html"
#     context_object_name = "tracks"
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#
#     def get_context_data(self, *, object_list=None, **kwargs):

def custom_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
    return render(request, 'savesounds/login.html')

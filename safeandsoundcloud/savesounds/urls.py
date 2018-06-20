from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('home/<username>/', views.home, name='home'),

    # /likes
    path('likes/<username>/', views.likes, name='likes'),

    # /reposts
    path('reposts/<username>/', views.reposts, name='reposts'),

    # /login
    path('login/', views.login, name='login'),

    # /safe-and-soundcloud/callback.html
    path('safe-and-soundcloud/callback.html', views.auth_callback, name='callback'),

    # authentication urls
    path('accounts/', include('django.contrib.auth.urls')),
]

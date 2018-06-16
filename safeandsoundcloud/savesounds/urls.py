from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # /likes
    path('likes/', views.likes, name='likes'),

    # /reposts
    path('reposts/', views.reposts, name='reposts'),

    # /login
    path('login/', views.login, name='login'),

    # /safe-and-soundcloud/callback.html
    path('safe-and-soundcloud/callback.html', views.auth_callback, name='callback')
]

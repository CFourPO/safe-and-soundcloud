from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('home/', views.HomeView.as_view(), name='home'),

    # /likes
    path('likes/', views.likes, name='likes'),

    # /reposts
    path('reposts/', views.reposts, name='reposts'),

    # /login
    path('login/', views.custom_login, name='login'),

    path('logout/', views.custom_logout, name='logout'),

    # /safe-and-soundcloud/callback.html
    path('safe-and-soundcloud/callback.html', views.auth_callback, name='callback'),

    # authentication urls
    path('accounts/', include('django.contrib.auth.urls')),

]

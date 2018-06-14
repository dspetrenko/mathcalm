from django.urls import path

import django.contrib.auth.views as auth_views

from .views import competitions
from .views import main

urlpatterns = [
    path('', main),
    path('login/', auth_views.login, {'extra_context': {'next': '/'}}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}),
    path('competitions/', competitions),
]

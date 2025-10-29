from django.urls import path
from .views import *

app_name = 'rost'

urlpatterns = [
    path('', home, name='home'),
    path('login_user/', login_user, name='login_user'),
]

from mclaren.views import *
from django.urls import path


app_name='mclaren'

urlpatterns=[
    path('driver1/', driver1, name='driver1'),
    path('driver2/', driver2, name='driver2'),
    
]
from django.urls import path
from . import views

app_name = 'pagin'
urlpatterns = [
    path('', views.pagin, name='home'),
]

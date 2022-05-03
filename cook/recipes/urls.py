from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.recipies_list, name='blog'),
    path('recipe/<name>', views.recipe, name='recipe'),

]

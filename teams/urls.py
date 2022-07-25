"""""""""""""""""""""""""""""""""""""""""""""""""""
Intro
""""""""""""""""""""""""""""""""""""""""""""""""""""""
Author: Dishant Mittal
Version: 1.0
Email: dishantmittal31@gmail.com
Date Created: 2022-07-25
"""""""""""""""""""""""""""""""""""""""""""""""""""

from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'teams'
urlpatterns = [

    path('get-happiness/', views.get_avg_happ, name='happ_get'),

]
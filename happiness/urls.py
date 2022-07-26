from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'happiness'
urlpatterns = [

    path('post-happiness/', views.add_todays_happ, name='happ_post'),

]
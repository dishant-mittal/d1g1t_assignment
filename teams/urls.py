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
    # path('realize/invoices/', views.LoadInvoiceMeta.as_view(), name='invoice_metas'),
    # path('realize/invoice/<int:pk>', views.RealizationCreate.as_view(), name='realize_invoices'),

    path('get-happiness/', views.get_avg_happ, name='happ_get'),
    # path('team-stats/', views.team_stats, name='team_h_stats'),
    # path('average-stats/', views.load_buyers, name='avg_h_stats'),
]
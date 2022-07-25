from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'happiness'
urlpatterns = [
    # path('realize/invoices/', views.LoadInvoiceMeta.as_view(), name='invoice_metas'),
    # path('realize/invoice/<int:pk>', views.RealizationCreate.as_view(), name='realize_invoices'),

    path('get-happiness/', views.get_avg_happ, name='happ_get'),
    path('post-happiness/', views.add_todays_happ, name='happ_post'),
    # path('team-stats/', views.team_stats, name='team_h_stats'),
    # path('average-stats/', views.load_buyers, name='avg_h_stats'),
]
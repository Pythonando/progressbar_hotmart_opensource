from django.urls import path
from . import views

urlpatterns = [
    path('h/<str:offer_code>/', views.progressbar, name='progressbar'),
    path('webhook_hotmart/', views.WebhookHotmartView.as_view(), name="webhook_hotmart"),
]

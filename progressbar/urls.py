from django.urls import path
from . import views

urlpatterns = [
    path('/h/<str:offer_code>/', views.progressbar, name='progressbar'),
    path('webhook_hotmart/', views.webhook_hotmart, name="webhook_hotmart"),
]

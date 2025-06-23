from django.urls import path
from .views import dashboard_view
from events.views import event_list

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
]
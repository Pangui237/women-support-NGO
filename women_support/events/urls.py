from django.urls import path
from . import views

urlpatterns = [
    # admin/dashboard routes (login required)
    path('dashboard/', views.event_list, name='event_list'),
    path('dashboard/create/', views.event_create, name='event_create'),
    path('dashboard/<int:pk>/edit/', views.event_update, name='event_update'),
    path('dashboard/<int:pk>/delete/', views.event_delete, name='event_delete'),

    # public routes
    path('', views.public_event_list, name='public_event_list'),
    path('<int:pk>/', views.public_event_detail, name='public_event_detail'),
]

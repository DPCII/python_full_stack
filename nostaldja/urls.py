from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('fad/', views.fad_list, name='fad_list'),
    path('fad/<int:pk>', views.fad_detail, name='fad_detail'),
    path('decade/', views.decade_list, name='decade_list'),
    path('decade/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fad/<int:pk>/edit/', views.fad_edit, name='fad_edit'),
    path('fad/create/', views.fad_create, name='fad_create'),
    path('fad/delete/<int:pk>', views.fad_delete, name='fad_delete'),
]

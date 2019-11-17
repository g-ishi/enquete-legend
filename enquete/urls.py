from django.urls import path

from . import views

app_name = 'enquete'

urlpatterns = [
    path('list/', views.enqueteList.as_view(), name='enquete_list'),
    path('create/', views.enqueteCreate.as_view(), name='member_create')
    ]

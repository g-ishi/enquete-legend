from django.urls import path

from . import views

app_name = 'message'

urlpatterns = [
    path('list/', views.MessageList.as_view(), name='message_list'),
    path('list/<int:page>', views.MessageList.as_view(),
         name='message_list_page'),
    path('form_test/', views.FormTest.as_view(), name='form_test'),
]

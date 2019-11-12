"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import Enquetedashborad, EnqueteDetail, EnqueteAnswer
from .views import EnqueteCreate, EnqueteDelete
from .views import Test


urlpatterns = [
    path('dashborad/', Enquetedashborad.as_view(), name='dashborad'),
    path('detail/<int:pk>', EnqueteDetail.as_view(), name='detail'),
    path('answer/<int:pk>', EnqueteAnswer.as_view(), name='answer'),
    path('create/', EnqueteCreate.as_view(), name='create'),
    path('delete/<int:pk>', EnqueteDelete.as_view(), name='delete'),
    path('test/', Test.as_view()),
    ]

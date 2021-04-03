from django.contrib import admin
from django.urls import path, include
from SearchQuery import views
from django.conf.urls import url

urlpatterns = [
    path('',views.renderHome, name = 'HomePage'),

]
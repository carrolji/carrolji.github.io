from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bucketlist', views.bucket_list, name='bucket_list'),
]
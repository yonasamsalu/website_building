

from django.urls import path
from website_to_me import views

urlpatterns = [
    path('interface', views.website_develop)
]

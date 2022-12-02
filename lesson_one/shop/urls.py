from django.urls import path

from .views import *

urlpatterns = [
    path('shop/', index),
    path('shop/buy/<int:page_id>/', buy),
    path('sell/', sell),
]




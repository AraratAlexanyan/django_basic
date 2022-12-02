from django.urls import path

from .views import *

urlpatterns = [
    path('archive/', main_page),
    path('archive/<int:year>/', index)

]

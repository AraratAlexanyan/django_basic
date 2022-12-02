from django.urls import path

from .views import *

urlpatterns = [
    path('blog/', index),
    path('blog/ask', ask),
    path('blog/questions', questions),
]

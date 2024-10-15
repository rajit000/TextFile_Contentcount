from django.urls import path
from .views import *

urlpatterns = [
    path('upload',TextFileUploadView.as_view(),name='file-upload'),
]

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path ('', IndexTestView.as_view(), name='index'),
    path('createclasses/', createclasses, name='createclasses'),
]
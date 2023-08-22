from django.urls import path
from core.views import *


urlpatterns = [
    path('q10/', Q10View.as_view(), name='q10'),
    path('q11/', Q11View.as_view(), name='q11'),
]


from django.urls import path
from APP2000.views import home

urlpatterns = [
    path('', home,name='home'),
]
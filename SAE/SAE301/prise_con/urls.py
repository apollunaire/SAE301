from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('led1/',views.led),
    path('led1ON/',views.led_ON),
    path('led1OFF/',views.led_OFF),
]
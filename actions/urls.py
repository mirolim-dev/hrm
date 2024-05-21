from django.urls import path
from .views import home, actions, finance, staffs, go_admin

urlpatterns = [
    path("", home, name="home"),
    path('actions/', actions, name='actions'),
    path('finance/', finance, name="finance"),
    path('staffs/', staffs, name='staffs'),
    path('go-admin/', go_admin, name='go-admin')
]

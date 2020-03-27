from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inputs/', views.InputDeviceList.as_view()),
    path('outputs/', views.OutputDeviceList.as_view()),
    path('controllers/', views.ControllerList.as_view()),
    path('current_user/', views.current_user),
    path('users/', views.UserList.as_view()),
]

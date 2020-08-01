from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index,name="index"),
    path('dashBoard',views.Home,name="Home"),
    path('addMarks',views.addMarks,name="Add"),
    path('viewMarks',views.viewMarks,name="view"),
    path('updateMarks',views.updateMarks,name="update"),
    path('logout',views.userLogOut,name="logout")
]
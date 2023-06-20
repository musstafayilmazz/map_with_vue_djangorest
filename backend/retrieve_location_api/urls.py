from django.urls import path
from . import views 

urlpatterns = [
    path("list", views.location_list,name = "location-list"),
    path("create",views.location_create),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('create',views.location_record),
    path('list',views.location_list),
    path("list-coordinates",views.coordinates),
    
]

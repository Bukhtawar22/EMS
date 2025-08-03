
from django.urls import path
from .views import*

urlpatterns = [
   path("home/" , home ),
   path("order/" , order_add ),
   path("bill/" , bill ),
  
]

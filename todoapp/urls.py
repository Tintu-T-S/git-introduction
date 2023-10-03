
from django.urls import path

from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:playerid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
]
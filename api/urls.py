from django.urls import path
from .import views

urlpatterns = [
    path('', views.getRoutes, name='index'),
    path('notes',views.getNotes,name='notes'),
    path('notes/<int:id>',views.getNote,name='notes'),
   
]

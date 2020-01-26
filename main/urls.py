from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo', views.addtodo, name='addtodo'),
    path('delete_todo/<int:item_id>/', views.delete_todo, name='delete_todo')
]

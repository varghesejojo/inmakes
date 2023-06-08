from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('ItemList/',views.ItemList.as_view(),name='ItemList')
    
]

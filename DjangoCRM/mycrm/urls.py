from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('record/<int:id>',views.record,name='record'),
    path('delete/<int:id>',views.delete_record,name='delete'),
    path('add_record/',views.add_record,name='add_record'),
    path('update_record/<int:id>',views.update_record,name='update_record')
]   

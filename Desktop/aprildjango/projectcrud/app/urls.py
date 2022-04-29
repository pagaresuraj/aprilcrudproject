from django.urls import path
from app import views

urlpatterns = [
    path('',views.home),
    path('branches/',views.about),
    path('create/',views.create),
    path('schoolview/',views.schoolview),
    path('addform/',views.addform),
    path('updateview/<id>',views.updateview),
    path('deleteview/<id>', views.deleteview),


]


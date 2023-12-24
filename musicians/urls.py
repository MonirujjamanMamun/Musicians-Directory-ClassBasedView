from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogOut.as_view(), name='logout'),
    path('add/', views.AddMusicians.as_view(), name='add_musicians'),
    path('edit/<int:id>', views.EditMusicians.as_view(), name='edit_musicians'),
]

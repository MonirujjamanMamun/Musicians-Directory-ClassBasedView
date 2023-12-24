from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.AddAlbum.as_view(), name='add_album'),
    path('edit/<int:id>', views.AlbumEdit.as_view(), name='add_edit'),
    path('delete/<int:id>', views.AlbumDelete.as_view(), name='add_delete'),
]

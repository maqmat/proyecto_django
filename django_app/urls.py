from django.urls import path
from .views import (
    PostView, 
    postdetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostManagementView # NUEVO
)

urlpatterns = [
    # R - Read (Lista) - Página principal
    path('', PostView.as_view(), name='post_list'), 
    
    # CENTRO DE ADMINISTRACIÓN: Donde se verán los posts para editar
    path('manage/', PostManagementView.as_view(), name='post_management'), 
    
    # C - Create (Se accederá desde el Centro de Administración)
    path('new/', PostCreateView.as_view(), name='post_new'),
    
    # R - Read (Detalle)
    path('post/<int:pk>/', postdetailView.as_view(), name='post_detail'),
    
    # U - Update (Edición)
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    
    # D - Delete (Eliminar)
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
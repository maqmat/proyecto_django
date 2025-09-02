from django.urls import path
from .views import PostView, postdetailView

urlpatterns = [
    path('', PostView.as_view(), name='post_list'),  # Cambiado a usar PostView
    path('post/<int:pk>/', postdetailView.as_view(), name='post_detail'),
]
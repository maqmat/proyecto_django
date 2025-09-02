from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Vista para listar los posts
class PostView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

# Vista para mostrar el detalle de un post
class postdetailView(DetailView):
    model = Post
    template_name = 'description.html'
    context_object_name = 'post'



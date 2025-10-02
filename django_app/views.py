from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# C - CREAR un nuevo Post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'price', 'category', 'image']

# R - LISTAR todos los Posts (PÁGINA PRINCIPAL con filtro)
class PostView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'object_list' # Usamos object_list para coincidir con la plantilla

    def get_queryset(self):
        # 1. Obtener el parámetro 'category' de la URL (si existe)
        category_slug = self.request.GET.get('category')
        
        # 2. Si se proporciona una categoría y no es 'Todos', filtramos
        if category_slug and category_slug != 'Todos':
            # Filtramos por la categoría específica
            return Post.objects.filter(category=category_slug)
        else:
            # Si no hay parámetro, o es 'Todos', devolvemos todos los posts
            return Post.objects.all()

# R - NUEVA VISTA: Centro de Administración (Donde se editará)
class PostManagementView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_management.html'
    context_object_name = 'user_posts'
    
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-id')

# R - MOSTRAR DETALLE de un Post
class postdetailView(DetailView):
    model = Post
    template_name = 'description.html'
    context_object_name = 'post'

# U - ACTUALIZAR un Post existente
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'price', 'category', 'image'] 

# D - ELIMINAR un Post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_management')
    template_name = 'post_confirm_delete.html'
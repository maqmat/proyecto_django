# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Importamos la clase forms para heredar de ella
from django import forms



def home(request):
    return render(request, 'home.html')


# Creamos una clase para traducir las etiquetas del formulario de registro
class CustomUserCreationForm(UserCreationForm):
    # Definimos la clase Meta para asociarla al modelo User
    class Meta(UserCreationForm.Meta):
        # Campos que queremos mostrar en el formulario
        fields = UserCreationForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Traducimos las etiquetas
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password2'].label = 'Confirmación de contraseña'
        
        
        # Elimina la línea siguiente que estaba causando el error:
        # self.fields['password'].label = 'Contraseña'
        

class CustomLoginView(LoginView):
    template_name = 'login.html'

def signup(request):
    if request.method == 'POST':
        # Usamos nuestro formulario personalizado en lugar del original
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        # Usamos nuestro formulario personalizado para mostrarlo
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
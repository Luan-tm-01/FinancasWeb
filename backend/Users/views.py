from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Perfil
from django.contrib.auth import login

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('lista_compras'))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('lista_compras'))
    
    context = {'form': form}
    return render(request, 'register.html', context)


def register(request):
    form = CustomUserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        Perfil.objects.create(
            user=user
        )

        login(request, user)
        return redirect('lista_compras')

    return render(request, 'register.html', {'form': form})
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response

from .forms import formUser


def handleLogin(request):
    if request.method == 'POST':
        form = formUser(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return HttpResponse("Login com sucesso  -  código 200.")
            else:
                return HttpResponse("Acesso Proibido    -  código 403.")
    else:
        form = formUser()

    return render(request, 'login.html', {'form': form})

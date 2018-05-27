from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import ImportFile

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        files = models.File.getAllFiles(models.File)
        return render(request, 'list_imports.html', {'files': files})
    else:
        return render(request, 'user_not_logged.html')

def read(request, id):
    if request.user.is_authenticated:
        data = models.File.readFile(models.File, id)
        return render(request, 'file_details.html', {'data': data[0], 'filename': data[1]})
    else:
        return HttpResponse("Usuário não logado")

def upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ImportFile(request.POST, request.FILES)
            file = request.FILES['file']
            if form.is_valid():
                models.File.uploadFile(models.File, file)
            else:
                return HttpResponse("Formulário Inválido")
        else:
            form = ImportFile()
        return render(request, 'forms/upload_file.html', {'form': form})
    else:
        return render(request, 'user_not_logged.html')

def removeFile(request, id):
    return models.File.deleteFile(models.File, id)

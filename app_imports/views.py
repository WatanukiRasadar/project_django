from . import models
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from app_imports.forms import ImportFileForm
import os

class ImportsListView(ListView):
    model = models.File
    template_name = "list_imports.html"

class ImportDetailView(DetailView):
    model = models.File
    template_name = "file_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        try:
            with open(str(self.object.filename), mode="r") as details:
                for detail in details:
                    try:
                        data.append(detail.split(';', 1))
                    except ValueError:
                        print("Linha %s com valor incorreto" % (detail))
                        pass
                context['object'] = data
                return context
        except IOError:
            print("Arquivo não encontrado")
            pass

class ImportCreateView(CreateView):
    model = models.File
    form_class = ImportFileForm
    success_url = '/admin/imports'
    template_name = "forms/app_imports_form.html"

class ImportDeleteView(DeleteView):
    model = models.File
    success_url = "/admin/imports"
    template_name = 'forms/file_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        try:
            os.remove(str(self.object.filename))
            return HttpResponse("Success Delete")
        except IOError:
            return HttpResponse("Arquivo não encontrado")
            pass
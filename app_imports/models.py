from django.db import models
from django.conf import settings
from django.http import HttpResponse
import os

class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='project_one/uploads')

    def getAllFiles(self):
        files = self.objects.filter().values()
        return files

    def getOneFile(self, file_id):
        file = self.objects.get(pk=file_id)
        return file

    def readFile(self, file_id):
        try:
            file = self.objects.get(pk=file_id) 
            with open(str(file.file), mode="r") as _file:
                data = []
                for f in _file:
                    try:    
                        (key, value) = f.split(';', 1)
                        data.append({key: value})
                    except:
                        print("Erro na linha: %s" % (f))
                        pass
                return (data, _file.name)
        except IOError:
            print("Arquivo com ID: %s não encontrado" % (file_id))
            pass

    def deleteFile(self, file_id):
        try:
            self.getOneFile(file_id)
            _delete = self.objects.get(pk=file_id)
            _delete.delete()
            try:
                os.remove(str(_delete.file))
                return HttpResponse("Arquivo %s deletado com sucesso" % (str(_delete.file)))
            except IOError:
                return HttpResponse("Arquivo não encontrado")
                pass
        except:
            return HttpResponse("Arquivo %s não foi encontrado" % (file_id))

    def uploadFile(self, file):
        if str(file).endswith('.csv') or str(file).endswith('.txt'):
            _file = self(None, file)
            _file.save()
            self.handle_uploaded_file(file)
        else:
            return HttpResponse("É permitida somente extenções .csv e .txt")


    def handle_uploaded_file(file):
        with open("%s/%s" % (settings.UPLOAD_URL, file.name), 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
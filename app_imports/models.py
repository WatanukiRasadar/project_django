from django.db import models

class File(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.FileField(upload_to='project_one/uploads')
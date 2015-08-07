from django.db import models
from storages import RenameStorage

# Create your models here.
'''class SecurityFile(models.Model):
	public = models.FileField()
    private = models.FileField(storage=security_storage)
'''


class FileRename(models.Model):
	name = models.CharField(max_length=64)
	storefile = models.FileField(upload_to='photo')

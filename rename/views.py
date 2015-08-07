from django.shortcuts import render
from models import *

# Create your views here.
def home(request):
	if request.method == 'GET':
		return render(request,'home.html')
	elif request.method == 'POST':
		filerecv = request.FILES['file']
		name = request.POST['name']
		files = FileRename()
		files.name = name
		files.storefile = filerecv
		files.storefile.name = hehehe
		files.save()
		return render(request, 'home.html')


def update_filename(instance, filename):
    path = "photo"
    format = instance.userid + instance.transaction_uuid + instance.file_extension
    return os.path.join(path, format)
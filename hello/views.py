from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .mlmodels.formula1classifier import handle_uploaded_file
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']\
        and request.FILES['myfile'].content_type == 'image/jpeg':\

        image_data = request.FILES['myfile']

        imageLocation = 'hello/static/predicate.jpg'
        default_storage.delete(imageLocation)
        default_storage.save(imageLocation, ContentFile(image_data.read()))

        classifiedImageName = handle_uploaded_file(image_data)
        return render(request, 'hello/ml/upload.html', {
            'classification': classifiedImageName
        })
    return render(request, 'hello/ml/upload.html')



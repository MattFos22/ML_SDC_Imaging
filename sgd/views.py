from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .mlmodels.fileuploadclassifier import handle_uploaded_file
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import json

def home(request):
    return HttpResponse("Hello, Django!")


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']\
        and request.FILES['myfile'].content_type == 'image/jpeg':\

        predictions = handle_uploaded_file(request.FILES['myfile'])

        return render(request, 'sgd/ml/upload.html', {
            'predicate': predictions['raw'],
            'probabilities': predictions['friendly']
        })
    return render(request, 'sgd/ml/upload.html')

def movie_review(request):
    return render(request, 'sgd/ml/movie_review.html')



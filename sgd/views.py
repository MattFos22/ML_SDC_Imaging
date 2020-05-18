from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .mlmodels.fileuploadclassifier import handle_uploaded_file
from .mlmodels.moviereviewclassifier import handle_movie_review
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
            'raw': predictions['raw'],
            'probabilities': predictions['friendly']
        })
    return render(request, 'sgd/ml/upload.html')

def movie_review(request):
    if request.method == 'POST' and request.POST.get('reviewtext'):
        predictions = handle_movie_review(request.POST.get('reviewtext', 'This movie was great'))
        return render(request, 'sgd/ml/movie_review.html', {
            'raw': predictions['raw'],
            'review': predictions['originalReview']
        })
    return render(request, 'sgd/ml/movie_review.html')



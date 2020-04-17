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
import json

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'sgd/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']\
        and request.FILES['myfile'].content_type == 'image/jpeg':\

        image_data = request.FILES['myfile']

        imageLocation = 'sgd/static/subject.jpg'
        default_storage.delete(imageLocation)
        default_storage.save(imageLocation, ContentFile(image_data.read()))

        predictions = handle_uploaded_file(imageLocation)
        probabilitiesFriendly = getFriendlyProbabilities(predictions)

        return render(request, 'sgd/ml/upload.html', {
            'predicate': predictions,
            'probabilities': probabilitiesFriendly
        })
    return render(request, 'sgd/ml/upload.html')


def getFriendlyProbabilities(predictions):
    categories = {'bmw': 0, 'mercedes':1, 'tesla':2}
    categoriesWithProbabilities = list(map(lambda category: (extractProbability(category, predictions)), categories.items()))
    return categoriesWithProbabilities

def extractProbability(category, predictions):
    raw = str(predictions[2].data[category[1]])
    parsed = re.search('(?<=\()(.*?)(?=\))', raw)
    return category[0] + ' - ' + parsed.group(1)

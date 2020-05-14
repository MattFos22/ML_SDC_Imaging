from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def save(image):
    imageLocation = 'sgd/static/subject.jpg'
    default_storage.delete(imageLocation)
    default_storage.save(imageLocation, ContentFile(image.read()))
    return imageLocation
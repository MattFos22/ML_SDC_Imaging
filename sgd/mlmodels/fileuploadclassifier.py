from fastai.vision import (
    ImageDataBunch,
    learner,
    open_image,
    get_transforms,
    models,
)
from sgd.repos.simple_upload import save

def handle_uploaded_file(image):
    imageLocation = save(image)
    image = open_image(imageLocation)
    path = 'sgd/static'
    learn = learner.load_learner(path)
    predictions = dict()
    predictions['raw']= learn.predict(image)
    predictions['friendly'] = getFriendlyProbabilities(predictions['raw'])
    return predictions

def getFriendlyProbabilities(predictions):
    categories = {'bmw': 0, 'mercedes':1, 'tesla':2}
    categoriesWithProbabilities = list(map(lambda category: (extractProbability(category, predictions)), categories.items()))
    return categoriesWithProbabilities

def extractProbability(category, predictions):
    raw = str(predictions[2].data[category[1]])
    parsed = re.search('(?<=\()(.*?)(?=\))', raw)
    return category[0] + ' - ' + parsed.group(1)
from fastai.vision import (
    ImageDataBunch,
    learner,
    open_image,
    get_transforms,
    models,
)

def handle_uploaded_file(savedImageLocation):
    image = open_image(savedImageLocation)
    path = 'sgd/static'
    learn = learner.load_learner(path)
    pred_class = learn.predict(image)
    return pred_class
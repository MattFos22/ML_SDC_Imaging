from fastai.vision import (
    ImageDataBunch,
    learner,
    open_image,
    get_transforms,
    models,
)

def handle_movie_review(movieReview):
    path = 'sgd/static/trained/natural-language-processor'
    learn = learner.load_learner(path)
    predictions = dict()
    predictions['raw']= learn.predict(movieReview)
    predictions['originalReview'] = movieReview
    return predictions
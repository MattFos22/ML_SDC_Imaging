from fastai.vision import (
    ImageDataBunch,
    ConvLearner,
    open_image,
    get_transforms,
    models,
)
import torch

# def handle_uploaded_file(f):
#     return 'Its a car man!'
f1_data = ImageDataBunch.from_name_re(
    cat_images_path,
    cat_fnames,
    r"/([^/]+)_\d+.jpg$",
    ds_tfms=get_transforms(),
    size=224,
)

f1_learner = ConvLearner(f1_data, models.resnet34)
f1_learner.model.load_state_dict(
    torch.load("f1_teams_model.pth", map_location="cpu")
)

def handle_uploaded_file(image):
    _,_,losses = learner.predict(image)
    return {
        "predictions": sorted(
            zip(cat_learner.data.classes, map(float, losses)),
            key=lambda p: p[1],
            reverse=True
        )
    }
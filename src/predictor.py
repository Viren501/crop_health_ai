from transformers import pipeline
from PIL import Image


MODEL_NAME = "wambugu71/crop_leaf_diseases_vit"


classifier = pipeline(
    "image-classification",
    model=MODEL_NAME
)


def predict(image, top_k=3):

    if not isinstance(image, Image.Image):
        image = Image.open(image).convert("RGB")

    else:
        image = image.convert("RGB")

    results = classifier(
        image,
        top_k=top_k
    )

    return results
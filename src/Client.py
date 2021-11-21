import io
import os

from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="res\Key.json"

client = vision.ImageAnnotatorClient()

def detect_labels(path):

    file_name = os.path.abspath(path)


    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels

def detect_text(path):

    file_name = os.path.abspath(path)


    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    return texts

def localize_objects(path):

    file_name = os.path.abspath(path)


    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    objects = client.object_localization(
        content=content).localized_object_annotations

    return objects
import io
import os

from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="res\.json"

client = vision.ImageAnnotatorClient()

file_name = os.path.abspath('res/teste.jpg')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)
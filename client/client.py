import requests
from PIL import Image
import io

def image_to_byte_array(image: Image) -> bytes:
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format=image.format)
    img_byte_array = img_byte_array.getvalue()
    return img_byte_array

urls = {
    'yolo_v1': 'http://127.0.0.1:5000/process_image_v1',
    'yolo_v2': 'http://127.0.0.1:5000/process_image_v2',
    'yolo_v3': 'http://127.0.0.1:5000/process_image_v3',
}

img = Image.open("imgs/img1.jpg")

img_bytes = image_to_byte_array(img)

resp = requests.post(urls["yolo_v1"], data=img_bytes)

response_json = resp.json()
verdict = response_json['verdict']
prob = response_json['prob']

print(f"{prob}, {verdict}")


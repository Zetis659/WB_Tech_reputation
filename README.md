# WB Tech Reputation

Проект представляет собой Flask-приложение для распознавания СПАМа на фото. Он использует модели машинного обучения для определения мошеннических СПАМ слов и объектов на изображениях с помощью YOLO.

### Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)


## Install
```bash
   git clone https://github.com/Zetis659/WB_Tech_reputation.git
   cd WB_Tech_reputation
   docker-compose up --build
```

## How to use
Распознавание СПАМА на одном фото:
```Python
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

img = Image.open('imgs/img1.jpg')

img_bytes = image_to_byte_array(img)

resp = requests.post(urls['yolo_v1'], data=img_bytes)

response_json = resp.json()
verdict = response_json['verdict']
prob = response_json['prob']

print(f'{prob}, {verdict}')
```

   

import os
import gdown
from ultralytics import YOLO

def load_model_and_fraud_words():
    model_path = None
    fraud_words_path = None
    models_folder = os.path.join(os.getcwd(), 'models')
    
    if not os.path.exists(models_folder):
        os.makedirs(models_folder)

    for file in os.listdir(models_folder):
        if 'yolo_model.pt' in file:
            model_path = os.path.join(models_folder, file)
            break
    
    if model_path is None:
        yolo_model_url = 'https://drive.google.com/uc?id=1SX5qBj0kZKoYO5HFB1Pm3pQ4ZkjioP5r'
        yolo_model_path = os.path.join(models_folder, 'yolo_model.pt')
        gdown.download(yolo_model_url, yolo_model_path, quiet=False)
        model_path = yolo_model_path
    
    model = YOLO(model_path)
    
    for file in os.listdir(models_folder):
        if 'fraud_words' in file:
            fraud_words_path = os.path.join(models_folder, file)
            break
    
    if fraud_words_path is None:
        fraud_words_url = 'https://drive.google.com/uc?id=1o1p1Mupl8nsh38gz2IiDdMlj-QjafQEr'
        fraud_words_path = os.path.join(models_folder, 'fraud_words.txt')
        gdown.download(fraud_words_url, fraud_words_path, quiet=False)
    
    with open(fraud_words_path, 'r', encoding='utf-8') as file:
        fraud_words = [word.strip() for line in file for word in line.split(',')]
    
    return model, fraud_words

from flask import Flask, request, jsonify
from app.model_loader import load_model_and_fraud_words
from app.models.yolo_model_v1 import process_single_image as process_single_image_v1
from app.models.yolo_model_v2 import process_single_image as process_single_image_v2
from app.models.yolo_model_v3 import process_single_image as process_single_image_v3

app = Flask(__name__)

@app.route('/process_image_v1', methods=['POST'])
def process_image_route_v1():
    image_bytes = request.data
    yolo_model, fraud_words = load_model_and_fraud_words()
    verdict, probability = process_single_image_v1(image_bytes, yolo_model, fraud_words)
    return jsonify({'prob': probability, 'verdict': verdict})

@app.route('/process_image_v2', methods=['POST'])
def process_image_route_v2():
    image_bytes = request.data
    yolo_model, fraud_words = load_model_and_fraud_words()
    verdict, probability = process_single_image_v2(image_bytes, yolo_model, fraud_words)
    return jsonify({'prob': probability, 'verdict': verdict})

@app.route('/process_image_v3', methods=['POST'])
def process_image_route_v3():
    image_bytes = request.data
    yolo_model, fraud_words = load_model_and_fraud_words()
    verdict, probability = process_single_image_v3(image_bytes, yolo_model, fraud_words)
    return jsonify({'prob': probability, 'verdict': verdict})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


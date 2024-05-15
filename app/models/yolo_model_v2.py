from PIL import Image
import io
import easyocr

def text_recognition(image_bytes):
    reader = easyocr.Reader(['ru', 'en'])
    result = reader.readtext(image_bytes, detail=0)
    return result

def detect_fraud_words(image_text, fraud_words):
    found_words = set()
    for word in image_text.lower().split():
        if word in fraud_words:
            found_words.add(word)
    return found_words

def process_image(image_bytes, model):
    image = Image.open(io.BytesIO(image_bytes))
    results = model.predict(image, save=False)
    probs = results[0].probs
    top_category = probs.top1
    total_prob = round(float(probs.top1conf), 2)
    second_prob = round(float(probs.top5conf[1]), 2) 
    return top_category, total_prob, second_prob

def process_single_image(image_bytes, yolo_model, fraud_words):
    result = text_recognition(image_bytes)
    
    if len(result) > 0:
        found_words = detect_fraud_words(' '.join(result), fraud_words)
        
        if found_words:
            return 1, 1 
        else:
            top_category, total_prob, second_prob = process_image(image_bytes, yolo_model)
            if total_prob >= 0.95 and top_category != 0:
                return 1, total_prob  
            else:
                return 0, second_prob
    else:
        return 0, 1  

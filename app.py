from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

# Initialize Flask app
app = Flask(__name__)

# Load the fine-tuned model and tokenizer from TensorFlow weights
model = MarianMTModel.from_pretrained('tf_model/', from_tf=True)  # Use from_tf=True
tokenizer = MarianTokenizer.from_pretrained('tf_model/')

# Define translation function
def translate_text(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# API endpoint for translation
@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    translation = translate_text(text)
    return jsonify({"translation": translation})

if __name__ == '__main__':
    app.run(port=5000)

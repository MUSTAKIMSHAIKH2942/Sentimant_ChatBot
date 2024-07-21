from flask import Flask, request, jsonify, render_template
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import random
import pandas as pd

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Check if CUDA is available and use GPU if possible
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
model.eval()

# Load responses from CSV file
responses_df = pd.read_csv('responses.csv')

def predict_sentiment(text):
    inputs = tokenizer.encode_plus(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
    
    scores = outputs.logits
    probs = torch.softmax(scores, dim=1)
    sentiment = torch.argmax(probs, dim=1).item()
    
    return sentiment  # sentiment score (0-4) where 4 is the most positive

def generate_response(user_input, sentiment):
    # Filter responses based on sentiment
    filtered_responses = responses_df[responses_df['sentiment'] == sentiment]['response'].tolist()
    if not filtered_responses:
        return "I'm not sure how to respond to that. Can you tell me more?"
    
    # Select a random response
    response = random.choice(filtered_responses)
    return response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    
    # Predict sentiment
    sentiment = predict_sentiment(user_input)
    
    # Generate a response based on the sentiment
    response = generate_response(user_input, sentiment)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

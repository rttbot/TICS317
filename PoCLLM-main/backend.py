"""
API REST para generación de texto usando el modelo LLM entrenado.
Carga el modelo y el tokenizer, y expone un endpoint para generar texto.
"""

from flask import Flask, request, jsonify
import json
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import joblib
import random
import nltk
from nltk.corpus import brown

app = Flask(__name__)

# Endpoint para obtener la lista de dichos
@app.route('/proverbs', methods=['GET'])
def get_proverbs():
    with open('proverbs.json', 'r') as f:
        proverbs = json.load(f)
    return jsonify(proverbs)

# 1. Cargar el modelo entrenado y el tokenizer
model = load_model('model.h5')
tokenizer = joblib.load('tokenizer.pkl')
max_seq_length = model.input_shape[1] + 1  # Ajusta si es necesario

# 2. Función para generar texto (idéntica a la usada en el entrenamiento)
def generate_text(seed_text, next_words):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_seq_length - 1, padding='pre')
        predicted = model.predict(token_list, verbose=0)
        predicted_word_index = np.argmax(predicted, axis=1)[0]
        predicted_word = tokenizer.index_word.get(predicted_word_index, '')
        seed_text += " " + predicted_word
    return seed_text

# 3. Endpoint para obtener una secuencia aleatoria y la palabra real siguiente
def prepare_sequences():
    nltk.download('brown')
    sequences = []
    min_len = 3
    max_len = 7
    for sent in brown.sents():
        if len(sent) > min_len:
            for n in range(min_len, min(max_len, len(sent))):
                seq = sent[:n]
                next_word = sent[n] if n < len(sent) else None
                if next_word:
                    sequences.append({
                        "sequence": " ".join(seq),
                        "next_word": next_word
                    })
    return sequences

sequences = prepare_sequences()

@app.route('/nextword', methods=['GET'])
def nextword():
    item = random.choice(sequences)
    return jsonify({
        "sequence": item["sequence"],
        "next_word": item["next_word"]
    })

# 4. Endpoint para generación de texto
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    seed_text = data['seed_text']
    next_words = data.get('next_words', 1)
    generated_text = generate_text(seed_text, next_words)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
"""
Entrenamiento de un modelo de lenguaje simple (LLM) usando el corpus Brown de NLTK.
Este script:
- Descarga y preprocesa los datos
- Tokeniza y convierte el texto en secuencias
- Entrena un modelo LSTM
- Guarda el modelo y el tokenizer para su uso posterior

Recomendado para Mac con Apple Silicon:
- Instala TensorFlow optimizado:
    pip uninstall tensorflow
    pip install tensorflow-macos tensorflow-metal
- Usa batch_size grande (256 o más) para aprovechar la GPU.
"""

import tensorflow as tf
import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import brown, stopwords
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import joblib
import os

def preprocess(data):
    stop_words = set(stopwords.words('english'))
    processed_data = []
    for sentence in data:
        # Minúsculas y eliminación de palabras no alfabéticas
        sentence = [word.lower() for word in sentence if word.isalpha()]
        # Eliminación de stopwords
        sentence = [word for word in sentence if word not in stop_words]
        if len(sentence) > 1:
            processed_data.append(sentence)
    return processed_data

def generate_text(seed_text, next_words, tokenizer, model, max_seq_length):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_seq_length - 1, padding='pre')
        predicted = model.predict(token_list, verbose=0)
        predicted_word_index = np.argmax(predicted, axis=1)[0]
        predicted_word = tokenizer.index_word.get(predicted_word_index, '')
        seed_text += " " + predicted_word
    return seed_text

def main():
    # 1. Descarga y carga de datos
    nltk.download('brown')
    data = brown.sents()[:10000]  # Usa solo 5,000 oraciones para pruebas
    print(f'Total de oraciones usadas: {len(data)}')
    print('Primeras oraciones del corpus:', data[:2])

    # 2. Preprocesamiento de datos
    nltk.download('stopwords')
    processed_data = preprocess(data)
    print(f'Oraciones preprocesadas: {len(processed_data)}')
    print('Primeras oraciones preprocesadas:', processed_data[:2])

    # 3. Tokenización y secuenciación
    print('Tokenizando y generando secuencias...')
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(processed_data)
    sequences = tokenizer.texts_to_sequences(processed_data)

    input_sequences = []
    for sequence in sequences:
        for i in range(1, len(sequence)):
            n_gram_sequence = sequence[:i+1]
            input_sequences.append(n_gram_sequence)

    max_seq_length = max([len(seq) for seq in input_sequences])
    input_sequences = pad_sequences(input_sequences, maxlen=max_seq_length, padding='pre')

    # 4. Preparación de datos para entrenamiento
    input_sequences = np.array(input_sequences)
    X = input_sequences[:, :-1]
    y = input_sequences[:, -1]
    # Codificación one-hot para la salida
    y = tf.keras.utils.to_categorical(y, num_classes=len(tokenizer.word_index) + 1)

    # 5. Definición y entrenamiento del modelo LSTM
    vocab_size = len(tokenizer.word_index) + 1
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=100, input_length=max_seq_length - 1))
    model.add(LSTM(128))
    model.add(Dense(vocab_size, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    print('Entrenando el modelo...')
    try:
        history = model.fit(X, y, epochs=50, batch_size=64, verbose=1)  # Menor batch y menos épocas para evitar OOM
    except KeyboardInterrupt:
        print('Entrenamiento interrumpido por el usuario.')
        history = None
    except Exception as e:
        print(f'Error durante el entrenamiento: {e}')
        history = None

    # 6. Evaluación y visualización
    if history:
        plt.plot(history.history['accuracy'])
        plt.title('Precisión del modelo')
        plt.ylabel('Precisión')
        plt.xlabel('Época')
        plt.show()

    print('Ejemplo de texto generado:', generate_text("The future of AI", 10, tokenizer, model, max_seq_length))

    # 8. Guardar el modelo y el tokenizer para el backend
    if history:
        print('Guardando modelo y tokenizer...')
        model.save('model.h5')
        joblib.dump(tokenizer, 'tokenizer.pkl')
        print('¡Listo! Modelo y tokenizer guardados.')
    else:
        print('No se guardó el modelo porque el entrenamiento falló.')

if __name__ == "__main__":
    main()
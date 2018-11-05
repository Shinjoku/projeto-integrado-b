#!/usr/bin/env python

import speech_recognition as sr


# Palavras que sao reconhecidas como gatilhos para que o som seja diminuido
KEYWORDS = (
    'ola',
    'alo',
    'o som ta muito alto',
    'hi',
    'hello',
    "it's too loud here"
)

def recognize(audioSource):
    # Inicializa reconhecedor
    r = sr.Recognizer()

    # Identifica a frase a partir do audio
    res = r.recognize_google(audioSource)

    return res in KEYWORDS
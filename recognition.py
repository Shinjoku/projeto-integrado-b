#!/usr/bin/env python

import speech_recognition as sr


KEYWORDS = (
    'ola',
    'hello',
    'alo',
    'hi'
)


def recognize(audioSource):
    # Inicializa reconhecedor
    r = sr.Recognizer()

    # Identifica a frase a partir do audio
    res = r.recognize_google(audio)

    if (res in KEYWORDS):
        return true
    else:
        return false
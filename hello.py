#!/usr/bin/env python

import os

__version__ = "0.0.1"
__author__  = "Adriano Santos"
__license__ = "Unlicense"

current_language = os.getenv("LANG", "pt_PT")[:5]

msg = "\nHello, Word!"

if  current_language == "pt_PT":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
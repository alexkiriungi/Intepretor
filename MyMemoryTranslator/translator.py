"""
   Two functions that translate text from English to French and vice versa 
"""
from deep_translator import MyMemoryTranslator
def english_to_french(text):
    '''function translates English to French'''
    translated = MyMemoryTranslator(source="english", target="french").translate(text)
    return translated

def french_to_english(text):
    '''function translates French to English'''
    translated = MyMemoryTranslator(source="french", target="english").translate(text)
    return translated

TEXT = "Good morning"
RESULT = english_to_french(TEXT)
print(RESULT)

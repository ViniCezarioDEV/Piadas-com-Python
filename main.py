import pyjokes
from translate import Translator




piada = pyjokes.get_joke(language='en',category='neutral')
piada = piada.casefold()
translator= Translator(to_lang="pt")
translation = translator.translate(piada)
print(translation)

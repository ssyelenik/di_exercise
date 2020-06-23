from translate import Translator
translator=Translator(to_lang="he")

fr_en_dictionary={}
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
for word in french_words:
    translation = translator.translate(word)
    fr_en_dictionary[word]=translation

print(fr_en_dictionary)

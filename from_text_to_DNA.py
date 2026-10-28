# Import what's nedeed
import re

# Introduce sentence
sentence = input("Introduce a string of text: ")

# Delete commas and diacritics for the nitrogenous bases (for text in other languages)
symbol_eraser = sentence.maketrans("ÁáÄäÀàÂâÃãÅåĂăĀāČčĆćÇçČčĈĉĊċṪṫŤťĞğĠġĜĝǦǧǤǥ,",
                                   "AAAAAAAAAAAAAAAACCCCCCCCCCCCTTTTGGGGGGGGGG ")
sentence_without_symbols = sentence.translate(symbol_eraser)

# Turn the sentence into DNA
DNA_sentence = sentence_without_symbols.replace(" ", "").upper()
DNA = re.sub(r"[^A, T, G, C\s]", "", DNA_sentence)
print(DNA)


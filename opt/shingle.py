import os

def k_shingles(text, k=3):
    """
    Erzeugt eine Menge von k-Shingles aus dem gegebenen Text.
    """
    text = text.lower().strip()
    shingles = set()
    for i in range(len(text) - k + 1):
        shingles.add(text[i:i+k])
    return shingles

def jaccard_similarity(set1, set2):
    """
    Berechnet die Jaccard-Ähnlichkeit zwischen zwei Mengen.
    """
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def load_text_from_file(file_path):
    """
    Lädt Text aus einer Datei.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Pfade zu den Textdateien (angepasst an Ihre Dateipfade)
file_path1 = 'text1.txt'
file_path2 = 'text2.txt'

# Texte aus Dateien laden
text1 = load_text_from_file('/content/Text4.md')
text2 = load_text_from_file('/content/Text5.md')

# Shingles erzeugen
shingles1 = k_shingles(text1, k=3)
shingles2 = k_shingles(text2, k=3)

# Ähnlichkeit berechnen
similarity = jaccard_similarity(shingles1, shingles2)
print(f"Die Jaccard-Ähnlichkeit zwischen den Dokumenten beträgt: {similarity:.2f}")

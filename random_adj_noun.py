import random
import nltk
from nltk.corpus import wordnet as wn

# Download required NLTK data if not already present
def ensure_nltk_data():
    try:
        wn.synsets('dog')
    except LookupError:
        nltk.download('wordnet')
        nltk.download('omw-1.4')

def get_adjectives():
    # Get all unique adjectives from WordNet
    adjectives = set()
    for synset in wn.all_synsets('a'):
        for lemma in synset.lemma_names():
            adjectives.add(lemma.replace('_', ' '))
    return list(adjectives)

def get_nouns():
    # Get all unique nouns from WordNet
    nouns = set()
    for synset in wn.all_synsets('n'):
        for lemma in synset.lemma_names():
            nouns.add(lemma.replace('_', ' '))
    return list(nouns)

def generate_pair(adjectives, nouns):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

if __name__ == "__main__":
    ensure_nltk_data()
    adjectives = get_adjectives()
    nouns = get_nouns()
    print("Random Adjective-Noun Pair Generator (NLTK)")
    while True:
        pair = generate_pair(adjectives, nouns)
        print(pair)
        cont = input("Generate another? (y/n): ").strip().lower()
        if cont != 'y':
            break

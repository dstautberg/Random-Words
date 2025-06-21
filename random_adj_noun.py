import random
import nltk
import argparse
from nltk.corpus import wordnet as wn

# Download required NLTK data if not already present
def ensure_nltk_data():
    try:
        wn.synsets('dog')
    except LookupError:
        nltk.download('wordnet')
        nltk.download('omw-1.4')

def get_adjectives():
    adjectives = set()
    for synset in wn.all_synsets('a'):
        for lemma in synset.lemma_names():
            adjectives.add(lemma.replace('_', ' '))
    return list(adjectives)

def get_nouns():
    nouns = set()
    for synset in wn.all_synsets('n'):
        for lemma in synset.lemma_names():
            nouns.add(lemma.replace('_', ' '))
    return list(nouns)

def generate_pair(adjectives, nouns, alliteration=False):
    max_attempts = 100
    attempts = 0

    while attempts < max_attempts:
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        if not alliteration or adjective[0].lower() == noun[0].lower():
            return f"{adjective} {noun}"
        attempts += 1
    return None  # Fallback if no alliterative pair found

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--alliteration", action="store_true", help="Only generate adjective-noun pairs that start with the same letter")
    args = parser.parse_args()

    ensure_nltk_data()
    adjectives = get_adjectives()
    nouns = get_nouns()

    print("Random Adjective-Noun Pair Generator (NLTK)\n")
    while True:
        print("-" * 59)
        for _ in range(20):
            pair = generate_pair(adjectives, nouns, alliteration=args.alliteration)
            if pair:
                print(pair)
        print("-" * 59)
        cont = input("Press [enter] to generate another 20, or enter 'q' to quit: ").strip().lower()
        if cont == 'q':
            break

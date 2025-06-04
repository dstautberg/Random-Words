import random
import nltk
from nltk.corpus import wordnet as wn
import argparse
import urllib.request
import os

# Download required NLTK data if not already present
def ensure_nltk_data():
    try:
        wn.synsets('dog')
    except LookupError:
        nltk.download('wordnet')
        nltk.download('omw-1.4')

def get_common_words():
    url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt"
    local_path = "common_10000.txt"
    if not os.path.exists(local_path):
        print(f"Downloading 10,000 most common English words to {local_path}...")
        urllib.request.urlretrieve(url, local_path)
    with open(local_path, 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f if word.strip())

def get_adjectives():
    common_words = get_common_words()
    adjectives = set()
    for synset in wn.all_synsets('a'):
        for lemma in synset.lemma_names():
            word = lemma.replace('_', ' ')
            if word in common_words:
                adjectives.add(word)
    return list(adjectives)

def get_nouns():
    common_words = get_common_words()
    nouns = set()
    for synset in wn.all_synsets('n'):
        for lemma in synset.lemma_names():
            word = lemma.replace('_', ' ')
            if word in common_words:
                nouns.add(word)
    return list(nouns)

def generate_combo(adjectives, nouns, capitalize=False, symbol=None, symbol_pos='end', number_range=(0, 9999)):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = str(random.randint(*number_range))
    if capitalize:
        adjective = adjective.capitalize()
        noun = noun.capitalize()
    else:
        adjective = adjective.lower()
        noun = noun.lower()
    # Replace spaces with dashes
    adjective = adjective.replace(' ', '-')
    noun = noun.replace(' ', '-')
    combo = f"{adjective}-{noun}-{number}"
    if symbol:
        if symbol_pos == 'end':
            combo = f"{combo}{symbol}"
        else:
            combo = f"{symbol}{combo}"
    return combo

def main():
    ensure_nltk_data()
    adjectives = get_adjectives()
    nouns = get_nouns()

    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument('--capitalize', action='store_true', help='Capitalize the first letter of each word')
    parser.add_argument('--symbol', type=str, default='', help='Symbol to add to the start or end')
    parser.add_argument('--symbol-pos', choices=['start', 'end'], default='start', help='Add symbol to start or end')
    parser.add_argument('--count', type=int, default=20, help='Number of combinations per batch')
    parser.add_argument('--min', dest='min_value', type=int, default=0, help='Minimum number value')
    parser.add_argument('--max', dest='max_value', type=int, default=9999, help='Maximum number value')
    args = parser.parse_args()

    print("Random Password Generator")
    while True:
        print("-" * 50)
        for _ in range(args.count):
            combo = generate_combo(
                adjectives, nouns,
                capitalize=args.capitalize,
                symbol=args.symbol if args.symbol else None,
                symbol_pos=args.symbol_pos,
                number_range=(args.min_value, args.max_value)
            )
            print(combo)
        print("-" * 50)
        cont = input(f"Press enter to generate another {args.count}, or 'q' to quit: ").strip().lower()
        if cont == 'q':
            break

if __name__ == "__main__":
    main()

# Random Adjective-Noun Pair & Password Generator

This repository contains two Python scripts that generate random word-based combinations using the NLTK WordNet corpus and the 10,000 most common English words.

## Features

- Uses open source NLTK WordNet database for word selection
- Filters words to the 10,000 most common English words (auto-downloads if needed)
- Automatically downloads required NLTK data if missing
- Batch generation and interactive prompts

## Scripts

### 1. random_adj_noun.py

Generates 20 random adjective-noun pairs per batch.

- Press [enter] to generate another batch, or 'q' to quit.

#### Usage

```sh
python random_adj_noun.py
```

### 2. random_password_generator.py

Generates random adjective-noun-number combinations, suitable for memorable passwords or passphrases.

- Filters adjectives and nouns to the 10,000 most common English words (downloads automatically from Google 10k list)
- Options for capitalization, symbol placement, number range, and batch size
- All spaces are replaced with dashes, and numbers are zero-padded to 4 digits

#### Example usage

```sh
python random_password_generator.py --capitalize --symbol ! --symbol-pos start --count 10 --min 100 --max 9999
```

#### Command line options

- `--capitalize` : Capitalize the first letter of each word
- `--symbol SYMBOL` : Add a symbol to the start or end
- `--symbol-pos start|end` : Position of the symbol (default: start)
- `--count N` : Number of combinations per batch (default: 20)
- `--min N` : Minimum number value (default: 0)
- `--max N` : Maximum number value (default: 9999)

## Requirements

- Python 3.7+
- `nltk` library

## Installation

1. Clone or download this repository.
2. Install the required Python package:

   ```sh
   pip install nltk
   ```

## License

This project is open source and uses the NLTK WordNet corpus and the Google 10,000 English words list.

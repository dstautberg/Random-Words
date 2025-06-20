# Random Adjective-Noun Pair & Password Generator

This repository contains two Python scripts that generate random word-based combinations using the NLTK WordNet corpus and the 10,000 most common English words.

## Features

- Uses open source NLTK WordNet database for word selection
- Filters down to the 10,000 most common English words 
- Automatically downloads required NLTK data if missing
- Batch generation and interactive prompts
- **Windows executable generation supported (see below)**

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

## Windows Executable

You can generate a standalone Windows executable for either script using [PyInstaller](https://pyinstaller.org/):

1. Install PyInstaller:

   ```sh
   pip install pyinstaller
   ```

2. Build the executable (example for password generator):

   ```sh
   pyinstaller --onefile random_password_generator.py
   ```

   The executable will be created in the `dist` folder.

### Download the Windows Executable

A pre-built Windows `.exe` for the password generator is available on the [GitHub Releases page](https://github.com/your-username/your-repo/releases). Download the latest `random_password_generator.exe` from the Releases section—no Python installation required.

> **Note:** If you want to build your own executable, see the instructions above under "Windows Executable."

### Distributing the Executable

To share the `.exe` file, use [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases):

1. Go to your repository on GitHub.
2. Click on "Releases" > "Draft a new release".
3. Upload the `.exe` file (from the `dist` folder) as a release asset.
4. Publish the release. Users can then download the executable directly from the Releases page.

> **Note:** Do not commit the `.exe` file to your repository. Use Releases for binary distribution.

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

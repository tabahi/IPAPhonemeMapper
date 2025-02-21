
Under construction.


# IPAPhonemeMapper

A Python library that bridges the gap between linguistic phoneme representations and machine learning systems by providing standardized mappings of International Phonetic Alphabet (IPA) symbols.

## Motivation

The International Phonetic Alphabet (IPA) is a comprehensive system for representing speech sounds, based on their articulatory properties - how they are physically produced by the human vocal tract. While this system is excellent for linguistic analysis, it presents challenges for automatic speech recognition (ASR) and other machine learning applications:

1. **Granularity Mismatch**: IPA captures extremely fine phonetic distinctions (e.g., aspirated vs. unaspirated consonants, or slight vowel quality differences) that may not be reliably distinguishable by ASR systems or relevant for specific applications.

2. **Symbol Complexity**: IPA uses a rich set of diacritics and modifiers that can make computational processing challenging. For example, the same basic sound might be represented with different combinations of base characters and diacritics.

3. **Perceptual vs. Articulatory**: While IPA is organized around how sounds are produced (articulatory features), ASR systems often work better with representations that align with how sounds are perceived (acoustic features).

IPAPhonemeMapper addresses these challenges by:
- Providing a standardized mapping from detailed IPA symbols to a simplified set of phonemes
- Grouping perceptually similar sounds that may be represented differently in IPA
- Offering numeric indices for machine learning applications
- Handling edge cases and unknown symbols gracefully

This makes it easier to:
- Preprocess linguistic data for ASR systems
- Standardize phonetic transcriptions across different sources
- Convert between different phonemic representation systems
- Create consistent input features for speech recognition models


## Features

- Standardize raw IPA phonemes to a consistent set using predefined mapping models
- Convert phonemes to numeric indices for machine learning tasks
- Handle unknown phonemes gracefully with configurable fallback options
- Process both individual phonemes and space-delimited phoneme strings
- Built-in validation for phoneme mappings and indices

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/your-username/IPAPhonemeMapper.git
cd IPAPhonemeMapper
```

2. Copy the required files to your project:

- ipa_phoneme_mapper.py
- models/phoneme_model_65.py

3. Use in your code:

```python
from ipa_phoneme_mapper import IPAPhonemeMapper

# Initialize the mapper with the 65-phoneme model
mapper = IPAPhonemeMapper(model="65_phoneme")

# Standardize a single phoneme
raw_phoneme = "ɑ"
standardized = mapper.standardize_phoneme(raw_phoneme)
print(f"Raw phoneme: {raw_phoneme} -> Standardized: {standardized}")

# Get numeric index for a phoneme
index = mapper.standardize_phoneme(raw_phoneme, return_index=True)
print(f"Index for {standardized}: {index}")

# Process a string of space-separated phonemes
phoneme_string = "h ɛ l oʊ"
processed = mapper.process_phoneme_string(phoneme_string)
print(f"Raw string: {phoneme_string}")
print(f"Processed string: {processed}")

# Get numeric tokens for a phoneme string
tokens = mapper.process_phoneme_string(phoneme_string, return_indices=True)
print(f"Numeric tokens: {tokens}")

''' prints:
Raw phoneme: ɑ -> Standardized: a
Index for a: 18

Raw string: h ɛ l oʊ
Processed string: h ɛ l oʊ
Numeric tokens: [50, 7, 56, 26]
'''
```


## Models

### 65-Phoneme Model (`phoneme_model_65`)

The default model maps over 600 IPA phonemes to a standardized set of 67 phonemes (65 base phonemes + 2 special tokens).

#### Model Structure

The model consists of:
- 67 total tokens (indexed 0-66)
- 65 base phonemes
- 2 special tokens: 'SIL' (silence) and 'noise'

#### Phoneme Categories

1. **Vowels** (27 tokens)
   - High front: i, i:, ɨ, ɪ
   - Mid front: e, e:, ɛ
   - Central: ə, ɚ, ʌ
   - Back: u, u:, ʊ, ɯ, o, o:, ɔ
   - Low: a, a:, æ
   - Front rounded: y, ø
   - Diphthongs: aɪ, eɪ, aʊ, oʊ, ɔɪ

2. **Consonants** (38 tokens)
   - Stops: p, b, t, d, k, g, q
   - Affricates: ts, tʃ, dʒ
   - Fricatives: s, z, ʃ, ʒ, ɕ, f, v, θ, ð, ç, x, ɣ, h, ʁ
   - Nasals: m, n, ɲ, ŋ
   - Liquids & Approximants: l, ɭ, ɾ, ɹ, j, w
   - Palatalized consonants: tʲ, nʲ, rʲ, ɭʲ

3. **Special Tokens** (2 tokens)
   - SIL (silence): Index 0
   - noise: Index 66

#### Key Features

- **Consistent Length Handling**: Common long vowels are preserved as distinct phonemes (e.g., i vs i:)
- **Cross-linguistic Adaptations**: Handles various transcription systems and language-specific markers
- **Palatalization**: Preserves high-frequency palatalized consonants while mapping rare ones
- **Special Case Handling**: 
  - Maps language markers to 'SIL'
  - Maps error cases and unknown sequences to 'noise'
  - Handles various diacritics and modifiers systematically

#### Common Mappings

The model applies systematic mappings for:
- Aspirated consonants → unaspirated counterparts
- Geminate (doubled) consonants → single consonants
- Nasalized vowels → oral counterparts
- Rare diphthongs → common diphthongs
- Complex consonant sequences → simpler forms
- Breathy and creaky voiced sounds → modal voice

This model is particularly useful for:
- Speech recognition tasks
- Cross-linguistic phoneme analysis
- Standardizing phonetic transcriptions
- Reducing phonetic complexity for machine learning


## Validation
The library includes built-in validation tools. You can run them using the provided test script:

```python
from test_phoneme_mapper import validate_phoneme_mapper, check_missing_phonemes

# Validate the mapper configuration
validate_phoneme_mapper()

# Check for missing phonemes in the current model
check_missing_phonemes()

''' prints:

IPAPhonemeMapper initialized with model: 65_phoneme

Validating mappings against indices...
Total unique mapped values: 65
Total unique tokens: 67
Total mappings: 594
Unique keys in mapping: 594
All mapped values have corresponding indices!
----------------------------------------
---------- Check missing phonemes ----------
bad phoneme: ʔ standardized: noise
bad phoneme: c standardized: -
bad phoneme: ɭ standardized: -
bad phoneme: ʔ standardized: noise
bad phoneme: c standardized: -
bad phoneme: q standardized: -
bad phoneme: l̩ standardized: -
bad phoneme: ɨː standardized: -
bad phoneme: ɭ standardized: -
bad phoneme: ʔʷ standardized: noise
missing_phonemes: ['ʔ', 'c', 'ɭ', 'ʔ', 'c', 'q', 'l̩', 'ɨː', 'ɭ', 'ʔʷ']
----------------------------------------

'''
```

# API Reference

## IPAPhonemeMapper

```python
mapper = IPAPhonemeMapper(model="65_phoneme")
```

## Methods

- `standardize_phoneme(raw_phoneme: str, return_index: bool = False) -> Union[str, int]`

    - Standardizes a single IPA phoneme
    - Returns either the standardized phoneme or its numeric index
    - Returns "-" for unknown phonemes, or the 'noise' index if return_index is True

- `process_phoneme_string(phoneme_string: str, delimiter: str = " ", return_indices: bool = False) -> Union[str, List[int]]`

    - Processes a string of space-separated phonemes
    - Returns either a standardized phoneme string or list of numeric indices

- `get_all_mappings() -> Dict[str, str]`

    - Returns all current phoneme mappings

- `get_all_indices() -> Dict[str, int]`

    - Returns all current phoneme indices

# Contributing
I am looking for contributions! Please feel free to submit a Pull Request. See instructions in [CONTRIBUTING.md](CONTRIBUTING.md)


# License
This project is licensed under the GPLv3 License - see the LICENSE file for details.
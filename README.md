
Under construction.


# IPAPhonemeMapper

A Python library that bridges the gap between linguistic phoneme representations and machine learning systems by providing standardized mappings of International Phonetic Alphabet (IPA) symbols.

What does it do: 
Converts phoneme sequences (e.g., h ɛ l oʊ for hello) into standardized numerical tokens [50, 7, 56, 26] optimized for machine learning applications.

The base phoneme system is purposefully designed to be augmented with nuance annotations at a later stage. Instead of developing a complex system that must recognize hundreds of phonemes and their variants from the outset, this approach begins with a simpler phoneme recognition system that can be enhanced with nuance detection capabilities as needed.

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


Our project aims to develop a two-tier phoneme recognition system that prioritizes accuracy and scalability. The primary objective is to create a robust base system capable of recognizing fundamental phonemes, which will serve as the foundation for more sophisticated sound analysis. This base system will then be augmented with a complementary mechanism designed to detect and classify phonetic nuances and allophonic variations.



## Features

- Standardize raw IPA phonemes to a consistent set using predefined mapping dictionaries
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
- dictionaries/phoneme_65_empirical.py
- test_phoneme_mapper.py

3. Use in your code:

```python
from ipa_phoneme_mapper import IPAPhonemeMapper

# Initialize the mapper with the 65-phoneme dictionary
mapper = IPAPhonemeMapper(dictionary="phoneme_65_empirical")

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


## Dictionaries

### 65-Phoneme (`phoneme_65_empirical`)

The default dictionary maps over 600 IPA phonemes to a standardized set of 67 phonemes (65 base phonemes + 2 special tokens). This mapping is mostly empirically driven and somewhat systematic. In other words, there is no linguistic rule being followed, it is based on what is more frequent and causes less confusion. For example, not all consonants have palatalized variants (tʲ, nʲ, rʲ, ɭʲ) because not all are as common.

#### Structure

The dictionary consists of:
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

The 'noise' token implies "to be ignored" due to either ambiguity or due to lack of proper knowledge about the rare phonemes. However, with this mapping system it's rare in non-tonal languages.

#### Key Features

- **Consistent Length Handling**: Common long vowels are preserved as distinct phonemes (e.g., i vs i:)
- **Cross-linguistic Adaptations**: Handles various transcription systems and language-specific markers
- **Palatalization**: Preserves high-frequency palatalized consonants while mapping rare ones
- **Special Case Handling**: 
  - Maps language markers to 'SIL'
  - Maps error cases and unknown sequences to 'noise'
  - Handles various diacritics and modifiers systematically

#### Common Mappings

The dictionary applies somewhat systematic mappings for:
- Aspirated consonants → unaspirated counterparts
- Geminate (doubled) consonants → single consonants
- Nasalized vowels → oral counterparts
- Rare diphthongs → common diphthongs
- Complex consonant sequences → simpler forms
- Breathy and creaky voiced sounds → modal voice

This dictionary is particularly useful for:
- Speech recognition tasks
- Cross-linguistic phoneme analysis
- Standardizing phonetic transcriptions
- Reducing phonetic complexity for machine learning


## Validation - Contribute new dictionaries


If you want to start from the basics then edit the mappings in [`dictionaries/draft_new_mapping.py`](dictionaries/draft_new_mapping.py), then validate to see what's left to map. The library includes built-in [`validation tools`](test_phoneme_mapper.py). You can run them using the provided test script:

```python
from test_phoneme_mapper import validate_phoneme_mapper, check_missing_phonemes

validate_phoneme_mapper(dictionary_name = "draft_new_mapping")

check_missing_phonemes(dictionary_name = "draft_new_mapping")

''' prints:
Validating mappings against indices...
Total unique mapped values: 50
Total unique tokens: 50
Total mappings: 73
All mapped values exits in the standard index (have token numbers).
All tests passed!
----------------------------------------
---------- Check missing phonemes ----------
bad phoneme: d͡ʒ standardized: -  ('-' implies no mapping, 'noise' implies deliberate ignorance)
bad phoneme: ʃʲ standardized: -
bad phoneme: ɜ standardized: -
bad phoneme: ɘ standardized: -
bad phoneme: t͡ʃʰ standardized: -
bad phoneme: ä standardized: -
bad phoneme: t͡ʃ standardized: -
bad phoneme: ə̆ standardized: -
bad phoneme: pʰ standardized: -
'''
```

Or you can customize the extensive default phoneme dictionary, which already covers most common use cases but remains open to refinement [`dictionaries/phoneme_65_empirical.py`](dictionaries/phoneme_65_empirical.py).

```python
from test_phoneme_mapper import validate_phoneme_mapper, check_missing_phonemes

# Validate the mapper configuration
validate_phoneme_mapper(dictionary_name = "phoneme_65_empirical")

# Check for missing phonemes in the current dictionary
check_missing_phonemes(dictionary_name = "phoneme_65_empirical")

''' prints:
Validating mappings against indices...
Total unique mapped values: 67
Total unique tokens: 67
Total mappings: 619
All mapped values exits in the standard index (have token numbers).
All tests passed!
----------------------------------------
---------- Check missing phonemes ----------
bad phoneme: ʔ standardized: noise
bad phoneme: ʔ standardized: noise
bad phoneme: ʔʷ standardized: noise
missing_phonemes: ['ʔ', 'ʔ', 'ʔʷ']
----------------------------------------
'''
```

# API Reference

## IPAPhonemeMapper

```python
mapper = IPAPhonemeMapper(dictionary="phoneme_65_empirical")
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
Seeking contributions particularly from linguists and phonology experts. Whether it's expanding phoneme coverage, improving phonetic mappings, or enhancing language support, your expertise is valuable. Please feel free to submit a Pull Request. See instructions in [CONTRIBUTING.md](CONTRIBUTING.md)


# License
This project is licensed under the GPLv3 License - see the LICENSE file for details.
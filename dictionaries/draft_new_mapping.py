# Core phoneme indices for standard IPA representation
phoneme_mapped_index = {
    # Special token
    'SIL': 0,      # Silence
    
    # Front vowels
    'i': 1,        # High front unrounded (as in "see")
    'ɪ': 2,        # Near-high front unrounded (as in "bit")
    'e': 3,        # Mid front unrounded (as in "bay")
    'ɛ': 4,        # Open-mid front unrounded (as in "bed")
    'æ': 5,        # Near-open front unrounded (as in "cat")
    
    # Central vowels
    'ə': 6,        # Mid central (schwa, as in "about")
    'ʌ': 7,        # Open-mid back unrounded (as in "but")
    'ɚ': 8,        # R-colored schwa (as in "butter")
    
    # Back vowels
    'u': 9,        # High back rounded (as in "boot")
    'ʊ': 10,       # Near-high back rounded (as in "put")
    'o': 11,       # Mid back rounded (as in "boat")
    'ɔ': 12,       # Open-mid back rounded (as in "thought")
    'ɑ': 13,       # Open back unrounded (as in "father")
    
    # Common diphthongs
    'aɪ': 14,      # As in "bite"
    'aʊ': 15,      # As in "bout"
    'eɪ': 16,      # As in "bait"
    'oʊ': 17,      # As in "boat"
    'ɔɪ': 18,      # As in "boy"
    
    # Stops
    'p': 19,       # Voiceless bilabial stop
    'b': 20,       # Voiced bilabial stop
    't': 21,       # Voiceless alveolar stop
    'd': 22,       # Voiced alveolar stop
    'k': 23,       # Voiceless velar stop
    'g': 24,       # Voiced velar stop
    
    # Fricatives
    'f': 25,       # Voiceless labiodental fricative
    'v': 26,       # Voiced labiodental fricative
    'θ': 27,       # Voiceless dental fricative (as in "thin")
    'ð': 28,       # Voiced dental fricative (as in "this")
    's': 29,       # Voiceless alveolar fricative
    'z': 30,       # Voiced alveolar fricative
    'ʃ': 31,       # Voiceless postalveolar fricative (as in "ship")
    'ʒ': 32,       # Voiced postalveolar fricative (as in "measure")
    'h': 33,       # Voiceless glottal fricative
    
    # Affricates
    'tʃ': 34,      # Voiceless postalveolar affricate (as in "church")
    'dʒ': 35,      # Voiced postalveolar affricate (as in "judge")
    
    # Nasals
    'm': 36,       # Bilabial nasal
    'n': 37,       # Alveolar nasal
    'ŋ': 38,       # Velar nasal (as in "sing")
    
    # Liquids and glides
    'l': 39,       # Lateral approximant
    'ɹ': 40,       # Alveolar approximant (as in American "red")
    'j': 41,       # Palatal approximant (as in "yes")
    'w': 42,       # Labial-velar approximant
    
    # Common length and stress markers
    'ː': 43,       # Length marker
    'ˈ': 44,       # Primary stress
    'ˌ': 45,       # Secondary stress
    
    # Additional phonemes for broader language coverage
    'ç': 46,       # Voiceless palatal fricative (German "ich")
    'x': 47,       # Voiceless velar fricative (German "Bach")
    'ɲ': 48,       # Palatal nasal (Spanish "ñ")
    
    # Special token
    'noise': 49    # Noise token
}

# Mapping to convert various IPA symbols to standard set
phoneme_mapping = {
    'SIL': 'SIL',
    'i': 'i',
    'ɪ': 'ɪ',
    'e': 'e',
    'ɛ': 'ɛ',
    'æ': 'æ',
    'ə': 'ə',
    'ʌ': 'ʌ',
    'ɚ': 'ɚ',
    'u': 'u',
    'ʊ': 'ʊ',
    'o': 'o',
    'ɔ': 'ɔ',
    'ɑ': 'ɑ',
    'aɪ': 'aɪ',
    'aʊ': 'aʊ',
    'eɪ': 'eɪ',
    'oʊ': 'oʊ',
    'ɔɪ': 'ɔɪ',
    'p': 'p',
    'b': 'b',
    't': 't',
    'd': 'd',
    'k': 'k',
    'g': 'g',
    'f': 'f',
    'v': 'v',
    'θ': 'θ',
    'ð': 'ð',
    's': 's',
    'z': 'z',
    'ʃ': 'ʃ',
    'ʒ': 'ʒ',
    'h': 'h',
    'tʃ': 'tʃ',
    'dʒ': 'dʒ',
    'm': 'm',
    'n': 'n',
    'ŋ': 'ŋ',
    'l': 'l',
    'ɹ': 'ɹ',
    'j': 'j',
    'w': 'w',
    'ː': 'ː',
    'ˈ': 'ˈ',
    'ˌ': 'ˌ',
    'ç': 'ç',
    'x': 'x',
    'ɲ': 'ɲ',
    'noise': 'noise',
    
    # Variants
    'iː': 'i',
    'uː': 'u',
    'aː': 'ɑ',
    'eː': 'e',
    'oː': 'o',
    'ɨ': 'ɪ',
    'ʉ': 'u',
    'ɯ': 'u',
    'ø': 'o',
    'y': 'i',
    'ɒ': 'ɔ',
    'a': 'ɑ',
    
    # Consonant variants
    'ɾ': 't',      # Tap/Flap
    'r': 'ɹ',      # Trill
    'ʁ': 'ɹ',      # Uvular fricative
    'ɬ': 'l',      # Voiceless lateral
    'ʎ': 'l',      # Palatal lateral
    'ɕ': 'ʃ',      # Alveolo-palatal fricative
    'ʑ': 'ʒ',      # Voiced alveolo-palatal fricative
    'ʔ': 'SIL',       # Glottal stop (SIL will be used to actually learn it, use 'noise' to ignore it completely
    
    # Affricates
    'ts': 's',
    'dz': 'z',
    
    # Special tokens
    'SIL': 'SIL',
    'noise': 'noise',
    '': 'SIL',
    
    # Preserve core phonemes
    'i': 'i', 'ɪ': 'ɪ', 'e': 'e', 'ɛ': 'ɛ', 'æ': 'æ',
    'ə': 'ə', 'ʌ': 'ʌ', 'ɚ': 'ɚ', 
    'u': 'u', 'ʊ': 'ʊ', 'o': 'o', 'ɔ': 'ɔ', 'ɑ': 'ɑ',
    'p': 'p', 'b': 'b', 't': 't', 'd': 'd', 'k': 'k', 'g': 'g',
    'f': 'f', 'v': 'v', 'θ': 'θ', 'ð': 'ð', 
    's': 's', 'z': 'z', 'ʃ': 'ʃ', 'ʒ': 'ʒ', 'h': 'h',
    'm': 'm', 'n': 'n', 'ŋ': 'ŋ', 
    'l': 'l', 'ɹ': 'ɹ', 'j': 'j', 'w': 'w',
    'ç': 'ç', 'x': 'x', 'ɲ': 'ɲ'
}


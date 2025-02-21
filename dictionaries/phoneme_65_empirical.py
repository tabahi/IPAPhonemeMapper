# Index mapping for the standardized phonemes


phoneme_mapped_index = {
    # Special token
    'SIL': 0,
    
    # High front vowels and commonly confused similar vowels
    'i': 1,        # High front unrounded
    'i:': 2,       # Long high front unrounded
    'ɨ': 3,        # High central (grouped here due to high confusion with 'i')
    'ɪ': 4,        # Near-high front unrounded
    
    # Mid front vowels
    'e': 5,        # Mid front unrounded
    'e:': 6,       # Long mid front unrounded
    'ɛ': 7,        # Open-mid front unrounded
    
    # Central vowels
    'ə': 8,        # Schwa (mid central)
    'ɚ': 9,        # R-colored schwa
    'ʌ': 10,       # Open-mid back unrounded
    
    # Back vowels
    'u': 11,       # High back rounded
    'u:': 12,      # Long high back rounded
    'ʊ': 13,       # Near-high back rounded
    'ɯ': 14,       # High back unrounded
    'o': 15,       # Mid back rounded
    'o:': 16,      # Long mid back rounded
    'ɔ': 17,       # Open-mid back rounded
    
    # Low vowels
    'a': 18,       # Open central/front unrounded
    'a:': 19,      # Long open central/front unrounded
    'æ': 20,       # Near-open front unrounded
    
    # Front rounded vowels
    'y': 21,       # High front rounded
    'ø': 22,       # Mid front rounded
    
    # Diphthongs
    'aɪ': 23,      # Open central to high front
    'eɪ': 24,      # Mid front to high front
    'aʊ': 25,      # Open central to high back
    'oʊ': 26,      # Mid back to high back
    'ɔɪ': 27,      # Open-mid back to high front
    
    # Stops (organized by place of articulation)
    'p': 28,       # Voiceless bilabial
    'b': 29,       # Voiced bilabial
    't': 30,       # Voiceless alveolar
    'd': 31,       # Voiced alveolar
    'k': 32,       # Voiceless velar
    'g': 33,       # Voiced velar
    'q': 34,       # Voiceless uvular
    
    # Affricates and related sibilant fricatives (grouped by similarity)
    'ts': 35,      # Voiceless alveolar affricate
    's': 36,       # Voiceless alveolar fricative
    'z': 37,       # Voiced alveolar fricative
    'tʃ': 38,      # Voiceless postalveolar affricate
    'dʒ': 39,      # Voiced postalveolar affricate
    'ʃ': 40,       # Voiceless postalveolar fricative
    'ʒ': 41,       # Voiced postalveolar fricative
    'ɕ': 42,       # Voiceless alveolo-palatal fricative
    
    # Other fricatives (organized by place)
    'f': 43,       # Voiceless labiodental
    'v': 44,       # Voiced labiodental
    'θ': 45,       # Voiceless dental
    'ð': 46,       # Voiced dental
    'ç': 47,       # Voiceless palatal
    'x': 48,       # Voiceless velar
    'ɣ': 49,       # Voiced velar
    'h': 50,       # Voiceless glottal
    'ʁ': 51,       # Voiced uvular
    
    # Nasals (organized by place)
    'm': 52,       # Bilabial
    'n': 53,       # Alveolar
    'ɲ': 54,       # Palatal
    'ŋ': 55,       # Velar
    
    # Liquids and approximants
    'l': 56,       # Alveolar lateral
    'ɭ': 57,       # Retroflex lateral
    'ɾ': 58,       # Alveolar tap
    'ɹ': 59,       # Alveolar approximant
    'j': 60,       # Palatal approximant
    'w': 61,       # Labial-velar approximant
    
    # Palatalized consonants
    'tʲ': 62,      # Palatalized t
    'nʲ': 63,      # Palatalized n
    'rʲ': 64,      # Palatalized r
    'ɭʲ': 65,      # Palatalized retroflex lateral
    
    # Special token
    'noise': 66
}

# Mapping dictionary for standardizing phonemes
phoneme_mapping = {
    
    # Core vowels - simplified based on confusion patterns
    'ə': 'ə', 
    #'ʌ': 'ə',  # Merge due to high confusion
    'ʌ': 'ʌ', # didn't work well before but still keep it
    'ɪ': 'ɪ', 'i': 'i', 
    'iː': 'i:',
    'ʊ': 'ʊ',
    'u': 'u',
    'uː': 'u:',
    'ɛ': 'ɛ', 'e': 'e', 'eː': 'e:',
    'ɔː': 'ɔ', 'ɔ': 'ɔ',
    #'ɒ': 'ɒ', # Merge to 'a' due to 100% wrong predictions in confusion matrix (23 Jan)
    'ɒ': 'a',
    'æ': 'æ', # DO NOT merge
    
    'ɑː': 'a:', 
    'ɑ': 'a', 
    'a': 'a',
    'ɜː': 'ʌ',
    'ɜ': 'ʌ',
    'ɚ': 'ɚ',
    'o': 'o',
    'ɨ': 'ɨ',
    'ɨ': 'ɨ',
    
    # Common diphthongs - keep distinct ones
    'eɪ': 'eɪ', 'aɪ': 'aɪ', 'ɔɪ': 'ɔɪ',
    'aʊ': 'aʊ', 'oʊ': 'oʊ',
    
    # Less common diphthongs - map to similar common ones
    'ʌʊ': 'aʊ', 'eʊ': 'aʊ', 'ɛʊ': 'aʊ', 'əʊ': 'oʊ',
    'ɛɪ': 'eɪ', 'ʊɪ': 'aɪ', 'ea': 'eɪ',
    'aʊ̯': 'aʊ', 'aɪ̯': 'aɪ', 'ɔʏ̯': 'ɔɪ',
    
    # Core consonants
    'p': 'p', 'b': 'b', 't': 't', 'd': 'd',
    'k': 'k', 'g': 'g', 'm': 'm', 'n': 'n',
    'ŋ': 'ŋ', 'f': 'f', 'v': 'v', 'θ': 'θ',
    'ð': 'ð', 's': 's', 'z': 'z', 'ʃ': 'ʃ',
    'ʒ': 'ʒ', 'h': 'h', 'l': 'l', 'ɹ': 'ɹ',
    'j': 'j', 'w': 'w', 'ɲ': 'ɲ', 'ɾ': 'ɾ',
    
    # Consonant mergers based on confusion
    # 'ɣ': 'g',      # Merge with closest stop
    'ɣ': 'ɣ',  # emprically confused but will keep it
    #'ʁ': 'ɹ',      # Map to rhotic
    'ʁ': 'ʁ',
    'r': 'ɹ',      # Map to rhotic
    #'x': 'h',      # Map to closest fricative
    'x': 'x',
    #'ç': 'ʃ',      # Map to closest fricative
    #'ç': 's',      # Based on empirical confusion
    'ç': 'ç',
    'ʂ': 'ʃ',      # Map to closest fricative
    'ʐ': 'ʒ',      # Map to closest fricative
    #'ɕ': 'ʃ',      # Map to closest fricative
    'ɕ': 'ɕ',       # keep it
    'ʑ': 'ʒ',      # Map to closest fricative
    
    # Simplify affricates to their primary component
    #'ts': 't',
    'ts': 'ts',
    'dz': 'dʒ',
    #'tʃ': 'ʃ',
    'tʃ': 'tʃ',
    #'dʒ': 'ʒ',
    'dʒ': 'dʒ',
    'tɕ': 'tʃ',
    'dʑ': 'dʒ',
    'pf': 'f',
    
    #'tʲ': 't', 
    'tʲ': 'tʲ',  # high freuqncy, keep it
    #'nʲ': 'n', 
    'nʲ': 'nʲ', # high freuqncy, keep it
    #'rʲ': 'ɹ',
    'rʲ': 'rʲ', # high freuqncy, keep it
    # Remove palatalization
    'lʲ': 'l',  
    'dʲ': 'd', 'sʲ': 's', 'vʲ': 'v',
    'fʲ': 'f', 'mʲ': 'm',
    'pʲ': 'p', 'kʲ': 'k', 'bʲ': 'b',
    'ɲʲ': 'ɲ', 'dʒʲ': 'dʒ',
    
    # Simplify geminate consonants
    'tː': 't', 'dː': 'd', 'kː': 'k',
    'gː': 'g', 'pː': 'p', 'bː': 'b',
    'fː': 'f', 'vː': 'v', 'sː': 's',
    'zː': 'z', 'ʃː': 'ʃ', 'ʒː': 'ʒ',
    'mː': 'm', 'nː': 'n', 'ŋː': 'ŋ',
    'lː': 'l', 'rː': 'ɹ', 'jː': 'j',
    
    # Nasal vowels to oral counterparts
    'ɑ̃': 'a', 'ɛ̃': 'ɛ', 'ɔ̃': 'ɔ',
    'ũ': 'u', 'õ': 'oʊ', 'ɐ̃': 'ʌ',
    
    # R-colored vowels
    'ɑːɹ': 'ɚ', 'ɔːɹ': 'ɚ',
    'ʊɹ': 'ɚ', 'ɪɹ': 'ɚ', 'ɛɹ': 'ɚ',
    'oːɹ': 'ɚ',
    
    # Vowel sequences
    'ia': 'i:', 'ua': 'u:',
    'ɔø': 'ɔ', 'iːɛ': 'i:',
    'ʊə': 'ʊ', 'iə': 'i:',
    'eə': 'ɛ',
    
    # Common sequences
    # 'əl': 'əl',  # Keep this distinct sequence
    #'əl': 'o', # based on empirical confusion. theoretically, this should be merged with 'l' or 'e' but it's most confused with 'o'
    'əl': 'l',
    'n̩': 'n',
    'ʃf': 'ʃ',
    'eð': 'ð',
    'ns': 'n',
    'nd': 'n',
    'ʃts': 'ts',
    
    # Special symbols
    'SIL': 'SIL',
    'noise': 'noise',   # noise will be ignored by the model. CTC will take it as blank token.
    '': 'SIL',
    'ʔ': 'noise',
    
    # Language markers to silence
    '(en)': 'SIL', '(es)': 'SIL', '(fr)': 'SIL',
    '(de)': 'SIL', '(it)': 'SIL', '(nl)': 'SIL',
    '(pl)': 'SIL', '(ru)': 'SIL', '(ptpt)': 'SIL',
    
    # Error cases to noise
    '??': 'noise', 'uk': 'noise', 'it': 'noise',
    'ɡd': 'noise', 'rd': 'noise', 'as': 'noise',
    'up': 'noise', 'os': 'noise', 'kf': 'noise',
    '1': 'noise', 'ʃd': 'noise', 'ʃz': 'noise',
    'ʃn': 'noise',



    # Vowels
    'y': 'y',        # Map to existing long form
    'yː': 'y',       # Keep distinct high front rounded vowel
    'œ': 'ø',         # Map to closest unrounded vowel
    'ø': 'ø',        # Map to long version
    'øː': 'ø',       # Keep distinct mid front rounded vowel
    'ɐ': 'ʌ',         # Map to schwa
    'aː': 'a:',       # Keep long a
    #'oː': 'ɔ',       # Map to similar long vowel
    'oː': 'o:',       # Keep distinct long o
    'ɛː': 'ɛ',        # Map to base form
    'ɪː': 'i:',       # Map to similar long vowel
    'ɵ': 'ʊ',         # Map to closest vowel
    'ᵻ': 'ɪ',         # Map to similar vowel
    
    # Double vowels (map to their long counterparts)
    'aa': 'a',
    'ɐɐ': 'a',
    'ææ': 'æ',
    
    # Diphthongs
    'yʊ': 'u',       # Map to similar monophthong
    'œy': 'ɔɪ',       # Map to similar diphthong
    'uɪ': 'aɪ',       # Map to existing diphthong
    'oɪ': 'ɔɪ',       # Map to similar diphthong
    'iʊ': 'u',       # Map to similar monophthong
    'aɪə': 'aɪ',      # Map to base diphthong
    'aɪɚ': 'aɪ',      # Map to base diphthong
    
    # Nasal vowels
    'ɐ̃ʊ̃': 'aʊ',      # Map to oral diphthong
    'œ̃': 'ɛ',         # Map to oral vowel
    
    # Consonants
    'ʝ': 'j',         # Map to similar approximant
    'ɟ': 'ʒ',        # Map to similar affricate
    'ʋ': 'v',         # Map to similar fricative
    'd̪': 'd',         # Map dental to alveolar
    't̪': 't',         # Map dental to alveolar
    'ɬ': 'l',         # Map to plain lateral
    'ʎ': 'l',         # Map to plain lateral
    'β': 'v',         # Map to similar fricative
    'ɡ': 'g',         # Standardize to 'g'
    
    # Geminate consonants
    'ɡː': 'g',        # Map to single consonant
    'tsː': 'ts',      # Map to single affricate
    'dzː': 'd',      # Map to single affricate
    #'tʃː': 'ʃ',      # Map to single affricate
    'tʃː': 'tʃ',      # Map to single affricate
    'dʒː': 'dʒ',      # Map to single affricate
    'ss': 's',        # Map to single consonant
    
    # Palatalized consonants
    'ɡʲ': 'g',        # Map to plain consonant
    
    # Sequences
    'dɔ': 'noise',     # Map unusual sequence to noise


    # These are found (with counts) in Google MSWC data, but not in the OpenSLR-MLS data
    # Complex sequences with frequency counts
    'ja': 'j',      # Common sequence (36,809) -> simplify to first component
    'ju': 'j',      # Common sequence (19,620) -> simplify to first component  
    'tʃʲ': 'tʃ',     # Common palatalized affricate (32,707) -> map to fricative
    #'ɭ': 'l',       # Very common retroflex lateral (78,504) -> map to alveolar
    'ɭ': 'ɭ',
    'ɭʲ': 'ɭʲ',      # Common palatalized retroflex (61,298) -> map to plain lateral
    'u"': 'u',     # Quote variant (7,265) -> normalize to standard long u
    'ɪ^': 'ɪ',      # Rare diacritic variant (2,222) -> remove diacritic
    'sz': 's',      # Rare sequence (5) -> simplify to first component
    #'q': 'k',       # Common uvular stop (75,838) -> map to velar
    'q': 'q',     # keep it EVEN though it's relively rare (45k)
    #'qː': 'k',      # Rare long uvular (103) -> map to velar
    'qː': 'q',
    'r̝̊': 'ɹ',      # Rare trilled/fricative r (3,099) -> map to approximant
    'r̝': 'ɹ',      # Rare variant (1,702) -> map to approximant
    'r̩': 'ɹ',      # Rare syllabic (1,272) -> map to approximant
    'l̩': 'l',      # Rare syllabic (536) -> map to standard lateral
    'c': 'k',       # Uncommon palatal stop (4,195) -> map to velar

    # Vowel sequences
    'uɨ': 'ɨ',     # Common sequence (20,396) -> map to monophthong
    'aɨ': 'aɪ',     # Common sequence (13,971) -> map to similar diphthong
    'ɨu': 'u:',     # Less common (7,653) -> map to monophthong
    'ɪu': 'u:',     # Uncommon (4,320) -> map to monophthong
    'ɨː': 'ɨ',      # Common variant (15,065) -> remove length marker
    'ɑɨ': 'aɪ',     # Common sequence (24,604) -> map to diphthong
    'əɪ': 'eɪ',     # Common sequence (12,209) -> map to similar diphthong
    'əɨ': 'ɨ',      # Less common (5,629) -> simplify to first component
    'ɔɨ': 'ɔɪ',     # Common sequence (16,178) -> map to similar diphthong
    'ɪuː': 'u:',    # Rare sequence (37) -> map to monophthong

    # Rare sequences: 1-5 occurrences ---------------------------------------
    # Some of the extremely rare consonant-consonant and vowel-consonant sequences map to 'noise' (i.e., ignored), most don't.
    
    # More nasal sequences
    'nm': 'n',    # was 'noise', map to alveolar nasal
    'nn': 'n',    # was 'noise', map to single nasal
    'mn': 'm',    # was 'noise', map to bilabial nasal
    'mm': 'm',    # was 'noise', map to single nasal
    'na': 'n',    # was 'noise', preserve nasal
    'maː': 'm',   # was 'noise', preserve nasal
    'mz': 'm',    # was 'noise', preserve nasal
    'ms': 'm',    # was 'noise', preserve nasal
    'mf': 'm',    # was 'noise', preserve nasal
    'mɡ': 'm',    # was 'noise', preserve nasal
    'mx': 'm',    # was 'noise', preserve nasal
    'mv': 'm',    # was 'noise', preserve nasal
    'mʃ': 'm',    # current mapping is good
    
    # Stop sequences
    'dk': 'd',    # was 'noise', preserve first stop
    'dp': 'd',    # was 'noise', preserve first stop
    'db': 'd',    # was 'noise', preserve first stop
    'td': 't',    # was 'noise', preserve first stop
    'tb': 't',    # was 'noise', preserve first stop
    'tn': 't',    # was 'noise', preserve stop
    
    # Long vowel sequences
    'eːs': 'e:',  # was 'noise', preserve long vowel
    'eːt': 'e:',  # was 'noise', preserve long vowel
    'eːp': 'e:',  # was 'noise', preserve long vowel
    'eːf': 'e:',  # current mapping is good
    'eːz': 'e:',  # current mapping is good
    'eːj': 'e:',  # current mapping is good
    'eːx': 'e:',  # current mapping is good
    'eːʃ': 'e:',  # current mapping is good
    'oːs': 'o:',  # current mapping is good
    'oːb': 'o:',  # current mapping is good
    
    # Vowel sequences
    'ɑj': 'aɪ',   # was 'noise', map to diphthong
    'ɑh': 'a',    # was 'noise', preserve vowel
    'ɑm': 'a',    # was 'noise', preserve vowel
    'ɑk': 'a',    # was 'noise', preserve vowel
    'ɑn': 'a',    # was 'noise', preserve vowel
    'ɑq': 'a',    # was 'noise', preserve vowel
    'ɑt': 'a',    # was 'noise', preserve vowel
    'ɑo': 'a',    # was 'noise', preserve first vowel
    'ɑa': 'a',    # was 'noise', preserve first vowel
    'ɑaː': 'a:',  # was 'noise', map to long vowel
    'ɑuː': 'aʊ',  # was 'noise', map to diphthong
    
    # Other sequences
    'dʒv': 'dʒ',  # current mapping is good
    'bv': 'b',    # was 'noise', preserve stop
    'bh': 'b',    # was 'noise', preserve stop
    'ɡh': 'g',    # was 'noise', preserve stop
    'ɡz': 'g',    # was 'noise', preserve stop
    'hx': 'x',    # current mapping is good
    'ʃj': 'ʃ',    # was 'noise', preserve fricative
    
    # Special cases
    '(fa)': 'SIL',  # current mapping is good
    'bb': 'b',      # current mapping is good

    'uːb': 'u:',
    'uːk': 'u:',
    'laɪ': 'noise',
    # ---------------------------------------  End of rare sequences

    # Vowels and length variants
    'əː': 'ə',         # Long schwa maps to schwa (index 18)
    'æː': 'æ',         # Long ash maps to ash (index 32)
    'æi': 'eɪ',        # Map to similar diphthong (index 23)
    'æiː': 'eɪ',       # Map to similar diphthong (index 23)
    'ɵː': 'ʊ',         # Long rounded vowel maps to nearest equivalent (index 22)
    #'ɯ': 'ʊ',         # Unrounded high back vowel maps to nearest equivalent (index 22)
    'ɯ': 'ɯ',

    # Alternative transcription formats
    'e:': 'e:',        # Long e
    'eː': 'e:',        # Normalize colon to IPA length mark (index 43)
    #'e:': 'e',          # NOT merged due to high confusion
    'o:': 'o:',
    'y:': 'y',        # Normalize colon to IPA length mark (index 39)
    'u:': 'u:',        # Normalize colon to IPA length mark (index 5)
    'i:': 'i:',        # Normalize colon to IPA length mark (index 12)
    'ɑ:': 'a',        # Normalize colon to IPA length mark (index 13)
    'oe:': 'ø',       # Normalize colon to IPA length mark (index 40)
    'oe': 'ø',        # Map to equivalent (index 40)
    
    # ASCII-based transcription variants
    'S': 's',          # ASCII variant of 's' (index 21)
    'N': 'n',          # ASCII variant of 'n' (index 11)
    'X': 'k',          # ASCII variant, typically representing 'k' (index 27)
    'tS': 'tʃ',         # ASCII variant of 'tʃ' (index 1)
    'dZ': 'dʒ',         # ASCII variant of 'dʒ' (index 2)
    
    # Special characters and diacritics
    't^': 't',         # Remove diacritic (index 4)
    's^': 's',         # Remove diacritic (index 21)
    'd^': 'd',         # Remove diacritic (index 9)
    't^ː': 't',        # Remove diacritic and length (index 4)
    't[': 't',         # Remove bracket notation (index 4)
    'd[': 'd',         # Remove bracket notation (index 9)
    
    # Arabic phonemes
    'ʕ': 'h',          # Voiced pharyngeal fricative maps to nearest fricative (index 37)
    'ħ': 'h',          # Voiceless pharyngeal fricative maps to 'h' (index 37)
    'dˤ': 'd',         # Pharyngealized 'd' maps to plain 'd' (index 9)
    's̪': 's',          # Dental 's' maps to plain 's' (index 21)
    'χ': 'x',          # Voiceless uvular fricative maps to 'h' (index 37)
    'dˤdˤ': 'd',       # Doubled pharyngealized 'd' maps to 'd' (index 9)
    'dd': 'd',         # ASCII variant of doubled/pharyngealized 'd' (index 9)
    
    # Dot notation variants
    'i.ː': 'i:',       # Normalize dot notation (index 12)
    'a.ː': 'a:',       # Normalize dot notation (index 13)
    'u.ː': 'u:',       # Normalize dot notation (index 5)
    
    # Lateral approximant variant
    'ɫ': 'l',          # Velarized lateral maps to plain 'l' (index 16)
    
    # Consonant sequences (map to noise)
    'kt': 'noise',     # Consonant sequence (index 50)
    'd̪w': 'noise',     # Consonant sequence (index 50)
    'wb': 'noise',     # Consonant sequence (index 50)
    'fm': 'noise',     # Consonant sequence (index 50)
    
    # Vowel-consonant sequences (map to noise)
    'ʊːt': 'noise',    # Vowel-consonant sequence (index 50)
    'aɪp': 'noise',    # Vowel-consonant sequence (index 50)
    'əm': 'noise',     # Vowel-consonant sequence (index 50)
    'aːn': 'a:',    # Vowel-consonant sequence (index 50)
    'iːe': 'i:',    # Vowel-vowel sequence (index 50)
    'yi': 'i:',     # Vowel-vowel sequence (index 50)
    
    # Language markers (map to SIL)
    '(tt)': 'SIL',      # Language marker (index 0)

    # Double long vowel - map to standard long vowel
    'iːː': 'i:',       # Excessive length mark, normalize to standard long i (index 12)
    
    # Doubled diphthong - map to single diphthong
    'aɪaɪ': 'aɪ',      # Repeated diphthong, map to single instance (index 7)
    
    # Consonant sequences - map to noise like other sequences
    'ndʒ': 'dʒ',    # Consonant cluster (index 50)
    'tr': 'noise',     # Consonant cluster (index 50)
    'eβ': 'noise',     # Vowel-consonant sequence (index 50)


    # Double palatalization - map to single palatalized form then apply existing mappings
    'ʂʲ': 'ʃ',         # Map palatalized retroflex to palato-alveolar (index 1)
    'nʲʲ': 'nʲ',        # Double palatalized nasal to plain nasal (index 11)
    'tsʲ': 'ts',        # Palatalized affricate follows affricate mapping (index 4)
    'xʲ': 'h',         # Palatalized velar fricative to h (index 37)
    'dʑʲ': 'dʒ',        # Palatalized voiced affricate to voiced palato-alveolar (index 2)
    'ɕʲ': 'ɕ',         # Palatalized alveolo-palatal to palato-alveolar (index 1)
    'tɕʲ': 'ʃ',        # Palatalized affricate to palato-alveolar (index 1)
    'tʲʲ': 'tʲ',        # Double palatalized stop to plain stop (index 4)
    'ʒʲ': 'ʒ',        # Palatalized palato-alveolar remains (index 2)
    'ʃʲʲ': 'ʃ',        # Double palatalized palato-alveolar remains (index 1)
    'tsʲʲ': 'ts',       # Double palatalized affricate to stop (index 4)
    'ɾʲʲ': 'ɾ',        # Double palatalized tap remains (index 48)
    'zʲʲ': 'z',        # Double palatalized fricative remains (index 36)
    'ɾʲ': 'rʲ',         # Palatalized tap remains (index 48)
    'ʃʲ': 'ʃ',         # Palatalized palato-alveolar remains (index 1)
    'mʲʲ': 'm',        # Double palatalized nasal to plain (index 28)
    'ʲ': 'noise',      # Isolated palatalization mark to noise (index 50)

    # Vowel sequences - map to nearest phoneme or diphthong
    'uo': 'oʊ',        # Map to nearest diphthong (index 24)
    'ee': 'i:',        # Map to long vowel (index 12)
    'ie': 'i:',        # Map to long vowel (index 12)
    'ai': 'aɪ',        # Map to standard diphthong (index 7)
    'ui': 'u:',        # Map to long vowel (index 5)
    'au': 'aʊ',        # Map to standard diphthong (index 8)
    'eɑ': 'ɛ',         # Map to nearest monophthong (index 6)
    'iu': 'u:',        # Map to long vowel (index 5)
    'auː': 'aʊ',       # Map to standard diphthong (index 8)
    'ei': 'eɪ',        # Map to standard diphthong (index 23)
    'eu': 'oʊ',        # Map to nearest diphthong (index 24)
    'aiː': 'aɪ',       # Map to standard diphthong (index 7)
    'iuː': 'u:',       # Map to long vowel (index 5)
    'eiː': 'eɪ',       # Map to standard diphthong (index 23)
    'euː': 'oʊ',       # Map to nearest diphthong (index 24)
    'ɔa': 'ɔ',        # Map to long vowel (index 3)
    'yɪ': 'y',        # Map to long vowel (index 39)
    'iɪ': 'i:',        # Map to long vowel (index 12)
    'eo': 'oʊ',        # Map to nearest diphthong (index 24)

    # Special notations
    'cː': 'k',         # Long palatal stop to velar (index 27)

    # All Chinese tonal patterns (with numbers) and complex sequences map to 'noise'
    # Examples:
    'iɜk': 'noise', 'onɡ5': 'noise', 'ts.': 'ts', 'ə5': 'noise',
    'ŋf': 'noise', 'u2': 'noise', 'oɜɕ': 'noise', 'iɜ': 'noise',

    # MLS-fr
    # Consonant sequences to noise
    'ls': 'noise',     # Lateral + fricative sequence maps to noise (50)
    'll': 'noise',     # Double lateral sequence maps to noise (50)
    
    # Vowel-consonant sequences to noise
    'øːl': 'noise',    # Long oe + lateral sequence maps to noise (50)
    'øːs': 'noise',    # Long oe + fricative sequence maps to noise (50)


    # from UCLA Phonetics Dataset

    # Syllabic consonants - map to their non-syllabic counterparts
    'h̩': 'h',      # Syllabic h to h (37)
    'ɹ̩': 'ɹ',      # Syllabic r to r (17)
    'ŋ̩': 'ŋ',      # Syllabic ng to ng (34)
    'ɫ̩': 'l',      # Syllabic dark l to l (16)
    'v̩': 'v',      # Syllabic v to v (15)
    'm̩': 'm',      # Syllabic m to m (28)

    # Aspirated consonants - map to unaspirated counterparts
    'pʰ': 'p',     # Aspirated p to p (25)
    'tʰ': 't',     # Aspirated t to t (4)
    'kʰ': 'k',     # Aspirated k to k (27)
    'sʰ': 's',     # Aspirated s to s (21)
    'ʃʰ': 'ʃ',     # Aspirated sh to sh (1)
    'cʰ': 'k',     # Aspirated c to k (27)
    't͡sʰ': 'ts',    # Aspirated ts to t (4)
    't͡ʃʰ': 'tʃ',    # Aspirated tsh to sh (1)
    'ɕʰ': 'ɕ',     # Aspirated alveolo-palatal to sh (1)

    # Labialized consonants - map to base consonants
    'tʷ': 't',     # Labialized t to t (4)
    'kʷ': 'k',     # Labialized k to k (27)
    'pʷ': 'p',     # Labialized p to p (25)
    'ʒʷ': 'ʒ',     # Labialized zh to zh (2)
    'xʷ': 'h',     # Labialized x to h (37)
    'dʷ': 'd',     # Labialized d to d (9)
    'bʷ': 'b',     # Labialized b to b (26)
    'mʷ': 'm',     # Labialized m to m (28)
    'ŋʷ': 'ŋ',     # Labialized ng to ng (34)
    
    # Retroflexes - map to closest non-retroflex
    'ʈ': 't',      # Retroflex t to t (4)
    'ɖ': 'd',      # Retroflex d to d (9)
    'ɳ': 'n',      # Retroflex n to n (11)
    'ɻ': 'ɹ',      # Retroflex r to r (17)
    'ɽ': 'ɾ',      # Retroflex flap to tap (48)

    # Breathy voiced - map to regular voiced
    'n̤': 'n',      # Breathy n to n (11)
    'b̤': 'b',      # Breathy b to b (26)
    'j̤': 'j',      # Breathy j to j (29)
    'a̤': 'a',     # Breathy a to long a (30)
    'i̤ː': 'i:',    # Breathy long i to long i (12)
    'o̤': 'o',      # Breathy o to o (44)
    'o̤ː': 'o:',     # Breathy long o to o (44)
    
    # Nasalized vowels - map to oral counterparts
    'ãː': 'a:',    # Nasalized long a to long a (30)
    'ẽ': 'e',      # Nasalized e to e (42)
    'ɪ̃': 'ɪ',      # Nasalized short i to short i (31)
    'ỹ': 'y',     # Nasalized y to long y (39)
    'õː': 'o:',     # Nasalized long o to o (44)
    'æ̃': 'æ',      # Nasalized ae to ae (32)
    'ʌ̃': 'ʌ',      # Nasalized wedge to schwa (18)
    'ə̃': 'ə',      # Nasalized schwa to schwa (18)
    'ã': 'a',     # Nasalized a to long a (30)
    'ĩ': 'i:',     # Nasalized i to long i (12)
    'ĩː': 'i:',    # Nasalized long i to long i (12)
    'ũː': 'u:',    # Nasalized long u to long u (5)
    
    # Affricates - map to primary component
    't͡s': 'ts',     # ts to t (4)
    't͡ʃ': 'tʃ',     # tsh to sh (1)
    'd͡ʒ': 'dʒ',     # dzh to zh (2)
    't͡ɬ': 't',     # tl to t (4)
    
    # Ejectives - map to non-ejective counterparts
    'tʼ': 't',     # Ejective t to t (4)
    'kʼ': 'k',     # Ejective k to k (27)
    'qʼ': 'q',     # Ejective q to k (27)
    'pʼ': 'p',     # Ejective p to p (25)
    'sʼ': 's',     # Ejective s to s (21)
    
    # Additional vowels
    'ʏ': 'ɪ',      # Near-close near-front rounded to short i (31)
    'ʏː': 'y',    # Long near-close near-front rounded to long y (39)
    'ʊː': 'ʊ',     # Long near-close near-back rounded to short u (22)
    'ɤ': 'ə',      # Close-mid back unrounded to schwa (18)
    'ɤː': 'ə',     # Long close-mid back unrounded to schwa (18)
    'œː': 'ø',    # Long open-mid front rounded to long oe (40)
    'ɯː': 'u:',    # Long close back unrounded to long u (5)
    'ɛ̤': 'ɛ',      # Breathy open-mid front unrounded to epsilon (6)
    
    # Short/reduced vowels
    'ĕ': 'e',      # Short e to e (42)
    'ă': 'a',     # Short a to long a (30)
    'ĭ': 'ɪ',      # Short i to short i (31)
    'ŏ': 'o',      # Short o to o (44)
    'ŭ': 'ʊ',      # Short u to short u (22)
    
    # Laryngealized/creaky vowels - map to regular vowels
    'ḛ': 'e',      # Creaky e to e (42)
    'ḭ': 'i',      # Creaky i to i (41)
    'o̰': 'o',      # Creaky o to o (44)
    'ɛ̰': 'ɛ',      # Creaky epsilon to epsilon (6)
    'a̰': 'a',     # Creaky a to long a (30)
    'ʊ̰': 'ʊ',      # Creaky upsilon to upsilon (22)
    
    # Additional consonants
    'ɦ': 'h',      # Voiced h to h (37)
    'ʍ': 'w',      # Voiceless w to w (47)
    'ɢ': 'g',      # Uvular g to g (10)
    'ɱ': 'm',      # Labiodental nasal to m (28)
    'ʔ': 'noise',  # Glottal stop to noise (50)
    'ɮ': 'z',      # Voiced lateral fricative to z (36)
    'ɸ': 'f',      # Bilabial fricative to f (20)
    
    # Co-articulated stops 
    'k͡p': 'k',    # was 'noise', map to velar stop as it's typically more salient
    'ɡ͡b': 'g',    # was 'noise', map to velar stop (voiced counterpart)
    'p͡t': 'p',    # was 'noise', map to first stop in sequence
    'b͡d': 'b',    # was 'noise', map to first stop in sequence
    
    # Lengthened consonants
    'ʔː': 'q',    # was 'noise', map to closest glottal/uvular stop in inventory
    'hː': 'h',    # was 'noise', map to plain glottal fricative

    'æ̆': 'æ',      # Short ae to ae (32)
    'ɜ̆': 'ə',     # Short epsilon to long epsilon (33)
    'ɔ̆': 'ʌ',     # Short open-o to long open-o (3)
    'ə̠': 'ʌ',       # Retracted schwa (when it appears in stressed positions)
    'ə̆': 'ə',      # Short schwa to schwa (18)
    'ɒː': 'a:',    # Long open-o to long open-o (3)
    
    # Aspirated and modified affricates
    'd͡ʒʰ': 'dʒ',    # Aspirated dzh to zh (2)
    't͡sʼ': 'ts',    # Ejective ts to t (4)
    't͡ʃʼ': 'tʃ',    # Ejective tsh to sh (1)
    't͡ɬʼ': 't',    # Ejective tl to t (4)
    't͡ʃʲ': 'tʃ',    # Palatalized tsh to sh (1)
    'd͡ʒʲ': 'dʒ',    # Palatalized dzh to zh (2)
    
    # Voiceless sonorants
    'e̥': 'e',      # Voiceless e to e (42)
    'ɲ̥': 'ɲ',      # Voiceless ny to ny (38)
    'm̥': 'm',      # Voiceless m to m (28)
    'n̥': 'n',      # Voiceless n to n (11)
    'l̥': 'l',      # Voiceless l to l (16)
    'r̥': 'ɹ',      # Voiceless r to r (17)
    'ŋ̥': 'ŋ',      # Voiceless ng to ng (34)
    'i̥': 'i',      # Voiceless i to i (41)
    'u̥': 'u:',     # Voiceless u to long u (5)
    'ʎ̥': 'l',      # Voiceless palatal l to l (16)

    # Long consonants
    'tʰː': 't',    # Long aspirated t to t (4)
    'çː': 'ç',     # Long palatal fricative to h (37)
    'xː': 'h',     # Long x to h (37)
    'ɟː': 'ʒ',     # Long palatal stop to zh (2)
    'l̪ː': 'l',     # Long dental l to l (16)
    'pʰː': 'p',    # Long aspirated p to p (25)
    'θː': 'θ',     # Long th to th (46)
    'ɲː': 'ɲ',     # Long ny to ny (38)
    'wː': 'w',     # Long w to w (47)

    # Modified velars
    'kʰʲ': 'k',    # Palatalized aspirated k to k (27)
    'kʼʲ': 'k',    # Palatalized ejective k to k (27)
    'qʰʷ': 'q',    # Labialized aspirated q to k (27)
    'kʰʷ': 'k',    # Labialized aspirated k to k (27)
    'kʷʰ': 'k',    # Labialized aspirated k to k (27)
    'kʷʼ': 'k',    # Labialized ejective k to k (27)
    'qʷ': 'q',     # Labialized q to k (27)
    'qʷʼ': 'q',    # Labialized ejective q to k (27)
    'qʰ': 'q',     # Aspirated q to k (27)
    'q̠': 'q',      # Retracted q to k (27)
    'ɢʲ': 'g',     # Palatalized uvular g to g (10)
    'ɡʷ': 'g',     # Labialized g to g (10)

    # Rhotic vowels
    'e˞': 'ɚ',     # Rhotacized e to schwar (14)
    'a˞': 'ɚ',     # Rhotacized a to schwar (14)
    'o˞': 'ɚ',     # Rhotacized o to schwar (14)
    'u˞': 'ɚ',     # Rhotacized u to schwar (14)
    'i˞': 'ɚ',     # Rhotacized i to schwar (14)

    # Nasalized variants
    'ɛ̃ː': 'ɛ',     # Long nasalized epsilon to epsilon (6)
    'ʊ̃': 'ʊ',      # Nasalized upsilon to upsilon (22)
    'z̃': 'z',      # Nasalized z to z (36)
    'j̃': 'j',      # Nasalized j to j (29)
    'w̃': 'w',      # Nasalized w to w (47)
    'ʊ̰̃': 'ʊ',      # Creaky nasalized upsilon to upsilon (22)
    'æ̃ː': 'æ',     # Long nasalized ae to ae (32)
    'ɔ̃ː': 'ɔ',    # Long nasalized open-o to long open-o (3)
    'ɛ̰̃': 'ɛ',      # Creaky nasalized epsilon to epsilon (6)

    # Modified dentals/alveolars
    'd̪ʰ': 'd',     # Aspirated dental d to d (9)
    't̪ʰ': 't',     # Aspirated dental t to t (4)
    't̪ʲ': 'tʲ',     # Palatalized dental t to t (4)
    'tʲʰ': 'tʲ',     # Palatalized aspirated t to t (4)
    'dʰ': 'd',     # Aspirated d to d (9)
    'ðʲ': 'ð',     # Palatalized eth to eth (35)
    'zʲ': 'z',     # Palatalized z to z (36)
    'zʷ': 'z',     # Labialized z to z (36)
    
    # Complex modifications
    'ʃʷ': 'ʃ',     # Labialized sh to sh (1)
    'ɕʷ': 'ɕ',     # Labialized alveolo-palatal to sh (1)
    'ʑʷ': 'ʒ',     # Labialized voiced alveolo-palatal to zh (2)
    'ʕʷ': 'h',     # Labialized pharyngeal to h (37)
    'ħʷ': 'h',     # Labialized voiceless pharyngeal to h (37)
    'ʁʷ': 'ɹ',     # Labialized uvular to r (17)
    'χʲ': 'h',     # Palatalized x to h (37)
    'hʲ': 'h',     # Palatalized h to h (37)

    # Retracted/advanced variants
    'ɨ̠': 'ɨ',      # Retracted barred-i to barred-i (45)
    'ʊ̠': 'ʊ',      # Retracted upsilon to upsilon (22)
    'ʊ̟': 'ʊ',      # Advanced upsilon to upsilon (22)
    'æ̟': 'æ',      # Advanced ae to ae (32)
    'ə̟': 'ə',      # Advanced schwa to schwa (18)
    
    # Dental variants
    'n̪': 'n',      # Dental n to n (11)
    'l̪': 'l',      # Dental l to l (16)
    
    # Special vowels
    'ö': 'ø',     # O-umlaut to long oe (40)
    'ü': 'y',     # U-umlaut to long y (39)
    'ʉ': 'ɨ',     # Central u to long u (5)
    'ɞ': 'ə',      # Open-mid central rounded to schwa (18)
    'ɤ̈': 'ə',      # Advanced close-mid back unrounded to schwa (18)
    'ɯ̈': 'ɨ',      # Advanced high back unrounded
    
    # Implosives/ejectives/glottalized
    'ɗ': 'd',      # Implosive d to d (9)
    'ɓ': 'b',      # Implosive b to b (26)
    'ʄ': 'ʒ',      # Implosive palatal to zh (2)
    'dˀ': 'd',     # Glottalized d to d (9)
    'bˀ': 'b',     # Glottalized b to b (26)
    'ˀa': 'a',    # Preglottalized a to long a (30)

    # Modified retroflexes
    'ʈʰ': 't',     # Aspirated retroflex t to t (4)
    'ɖʰ': 'd',     # Aspirated retroflex d to d (9)

    # Remaining special cases
    'ɥ': 'j',      # Labial-palatal approximant to j (29)
    'ʀ': 'ɹ',      # Uvular trill to r (17)
    'ɹ̝': 'ɹ',      # Raised r to r (17)
    'ṽ': 'v',      # Nasalized v to v (15)
    'ə̥': 'ə',      # Voiceless schwa to schwa (18)
    'ə̯': 'ə',      # Non-syllabic schwa to schwa (18)
    'i̯': 'i',      # Non-syllabic i to i (41)
    'l̴': 'l',      # Velarized l to l (16)
    'dⁿ': 'd',     # Prenasalized d to d (9)
    'tⁿ': 't',     # Prenasalized t to t (4)
    
    # Breathy/creaky variants
    'd̪̤': 'd',     # Breathy dental d to d (9)
    'ɑ̤': 'a',     # Breathy long a to long a (13)
    'ṳː': 'u:',     # Breathy long u to long u (5)
    'ṳ': 'u:',      # Breathy u to long u (5)
    'ɯ̤': 'u:',     # Breathy unrounded u to long u (5)
    'ɪ̰': 'ɪ',      # Creaky short i to short i (31)
    'ɔ̰': 'ɔ',     # Creaky open-o to long open-o (3)
    'ɔ̤': 'ɔ',     # Breathy open-o to long open-o (3)
    
    # Height/backness variants
    'ɑ̝': 'a',     # Raised long a to long a (13)
    'ɛ̞': 'ɛ',      # Lowered epsilon to epsilon (6)
    'ɛ̝': 'ɛ',      # Raised epsilon to epsilon (6)
    'e̝': 'e',      # Raised e to e (42)
    'o̝': 'o',      # Raised o to o (44)
    'u̝': 'u:',     # Raised u to long u (5)
    'ɑ̞': 'a',     # Lowered long a to long a (13)
    'a̘': 'a',     # Advanced tongue root a to long a (30)
    'ä': 'a',     # Centralized a to long a (30)
    
    # Modified vowel quality
    'ɛ̈': 'ɛ',      # Centralized epsilon to epsilon (6)
    'œ̈': 'ø',     # Centralized oe to long oe (40)
    'ʌ̈': 'ʌ',      # Centralized wedge to schwa (18)
    'ɛ̠': 'ɛ',      # Retracted epsilon to epsilon (6)
    'a̠': 'a',     # Retracted a to long a (30)
    'o̠': 'o',      # Retracted o to o (44)
    'i̠': 'i',      # Retracted i to i (41)
    
    # Remaining consonant variants
    't̠': 't',      # Retracted t to t (4)
    'd̠': 'd',      # Retracted d to d (9)
    'n̠': 'n',      # Retracted n to n (11)
    't̟': 't',      # Advanced t to t (4)
    'r̟': 'ɹ',      # Advanced r to r (17)
    'r̠': 'ɹ',      # Retracted r to r (17)
    'rˠ': 'ɹ',     # Velarized r to r (17)
    'ɪ̥': 'ɪ',      # Voiceless short i to short i (31)
    'ʔʷ': 'noise', # Labialized glottal stop to noise (50)
    'ɕʼ': 'ɕ',     # Ejective alveolo-palatal to sh (1)
    'cʼ': 'k',     # Ejective c to k (27)
    'cʷʰ': 'k',    # Labialized aspirated c to k (27)
    'w̝': 'w',      # Raised w to w (47)

    'ʃ̠': 'ʃ',      # Retracted sh to sh (1)
    'ɪ̰̃': 'ɪ',      # Creaky nasalized short i to short i (31)
    'tʷʼ': 't',    # Labialized ejective t to t (4)
    'ŋʲ': 'ŋ',     # Palatalized ng to ng (34)
    'bʰ': 'b',     # Aspirated b to b (26)
    'æ̈': 'æ',      # Centralized ae to ae (32)
    'ɘ': 'ə',       # Close-mid central unrounded vowel to schwa (18)
    'tsʰ': 'ts',    # Aspirated ts to ts (4)
    'r̩ː': 'ɚ',     # Long rhotic schwa to schwar (14)
}
from ipa_phoneme_mapper import IPAPhonemeMapper


raw_phoneme = "ɑ"

dictionary_name = "phoneme_65_empirical"
mapper = IPAPhonemeMapper(dictionary=dictionary_name)

standardized = mapper.standardize_phoneme(raw_phoneme)
print(f"Raw phoneme: {raw_phoneme} -> Standardized: {standardized}")

# Get the index
index = mapper.standardize_phoneme(raw_phoneme, return_index=True)
print(f"Index for {standardized}: {index}")

# Example 2: Process a string of phonemes
phoneme_string = "h ɛ l oʊ"
processed = mapper.process_phoneme_string(phoneme_string)
print(f"\nRaw string: {phoneme_string}")
print(f"Processed string: {processed}")

# Get indices for the string
tokens = mapper.process_phoneme_string(phoneme_string, return_indices=True)
print(f"Standardized numeric tokens: {tokens}")


from ipa_phoneme_mapper import IPAPhonemeMapper






def check_missing_phonemes():

    print("-" * 10, "Check missing phonemes", "-" * 10)
    mapper = IPAPhonemeMapper(model="65_phoneme")

    test_phonemes = ['a', 'd͡ʒ', 'ʃʲ', 'm', 'ɜ', 'ɘ', 'ʃ', 't͡ʃʰ', 'r', 'ä', 't͡ʃ', 'ə̆', 'pʰ', 'ɜ̆', 'ʌ̈', 't', 'ʃʰ', 'kʼ', 'ʒʲ', 'ə', 'ă', 'b', 'ɨ', 'æ̈', 'j', 'ɛ̈', 'p', 'd', 'n', 'ɥ', 'ɡ', 't͡ʃʼ', 'χ', 'ˀa', 'ʒ', 'ħʷ', 'ɹ', 'ħ', 'œ̈', 'ɾ', 'ʁ', 'ɤ̈', 'z', 'i', 'χʲ', 'tʰ', 's', 'ʁʷ', 'h', 'ɛ', 'k', 'ɑ', 'x', 'ɔ', 'o', 'u', 'e', 'ɑ̃', 'ŋ', 'l', 'ʊ', 'ã', 'q̠', 'õ', 'w', 'β', 'f', 'v', 'ʎ', 'oː', 'eː', 'kʰ', 'ð', 'œ', 'ɹ̩', 'ɛ̝', 'ʔ', 'l̥', 'e̝', 'aː', 'uː', 'iː', 'ʌ̃', 'æ', 'ẽ', 'y', 'yː', 'ɪː', 'ɛː', 'øː', 'œː', 'ɑː', 'o̝', 'ʌ', 'ø', 'ɯ', 'sː', 'ɛ̃', 'c', 'ɪ', 'ɟ', 'ɲ', 'æː', 'æ̃ː', 'ʉ', 'ɫ̩', 'ʋ', 'ɫ', 'kʲ', 'ɣ', 'ɦ', 'n̩', 'ɸ', 'dʰ', 'm̩', 'h̩', 'ç', 'bʰ', 't̪', 'd̪', 'd̪̤', 'b̤', 'n̪', 'ĩ', 'ũː', 'ũ', 'j̤', 'l̪', 'pː', 'kː', 'rː', 'nː', 'l̪ː', 'bː', 'mː', 'ɞ', 't̪ʲ', 'hː', 'ʔː', 'tː', 'dː', 'ʈ', 'ɖ', 'ʂ', 'ʐ', 'r̥', 'ɔː', 'ʏː', 'ʏ', 'θ', 'n̥', 'cː', 'ɟː', 'fː', 'lː', 'ŋ̥', 'ə̯', 'ə̟', 'i̯', 'ʊ̟', 'ɛ̞', 'ʊ̠', 'r̟', 'r̠', 'ɕ', 'pʲ', 'bʲ', 'ŭ', 'tʲ', 'ĕ', 'dʲ', 'ɡʲ', 'nʲ', 'fʲ', 'zʲ', 'vʲ', 'lʲ', 'sʲ', 'xʲ', 'hʲ', 'ŏ', 'mʲ', 't͡ʃʲ', 'd͡ʒʲ', 'æ̆', 'ŋʲ', 'rʲ', 'ɾʲ', 'ĭ', 'ɔ̆', 's̪', 'ɱ', 'ɽ', 'ɳ', 'ʈʰ', 'ɖʰ', 'ɵ', 't̪ʰ', 'd͡ʒʰ', 'ɭ', 'ʊ̃', 'sʰ', 'ḭ', 'cʰ', 'ʊ̰', 'ɛ̰', 'ɪ̰', 'a̰', 'ḛ', 'o̰', 'ɛ̰̃', 'ɪ̃', 'ʊ̰̃', 'ɲ̥', 'æ̃', 'm̥', 'ɪ̰̃', 'ɔ̰', 'wː', 'ɔ̃ː', 'ɗ', 'ɔ̃', 'õː', 'ɯː', 'ə̃', 'tʰː', 'pʰː', 'vː', 'zː', 'ʃː', 'jː', 'ɲː', 'xː', 'çː', 'ɓ', 'ãː', 't͡sʼ', 'ɻ', 'ʀ', 't͡s', 'a', 'b', 'w', 'e', 'ɔ', 'p', 'ɛ', 't', 'o', 't͡ʃ', 'u', 'd', 'k', 'ɔ̃', 'kʷ', 'ɡ', 'k͡p', 'm', 'n', 'n̠', 'j', 'f', 's', 'ç', 'ɹ', 'l', 'i', 'ʍ', 'd̠', 'ʐ', 'ŋ', 'ɥ', 't̠', 'ɕʷ', 'ɕ', 'pʰ', 'tʰ', 'sʰ', 'kʰ', 'z', 'ä', 'h', 'v', 'ʃ', 'ʒ', 'r', 'ü', 'y', 'ʔ', 'ɪ', 'æ', 'ə', 'q̠', 'ɞ', 't͡ʃʰ', 'ĩ', 'ã', 'õ', 'ʋ', 'x', 'ɾ', 'ɓ', 'ɗ', 'c', 'ɟ', 'ʄ', 'aː', 'ɲ', 'ɔː', 'tʲ', 'oː', 'ɤː', 'uː', 'ʊː', 'ɳ', 'ɯː', 'ðʲ', 'tʲʰ', 'ɛ̃', 'ɣ', 'kʲ', 'ũ', 'ĩː', 'rˠ', 'ɛ̃ː', 'ãː', 'ɔ̃ː', 'ũː', 't̪', 'ʑʷ', 'ʑ', 'ɡʷ', 'ŋʷ', 'ɽ', 'o̠', 'w̃', 'ɯ', 'ö', 'ɡ͡b', 'd͡ʒ', 'ʁ', 'q', 'i̠', 'ɛ̠', 'v̩', 'l̥', 'ɤ', 'r̥', 'ɢ', 'ɢʲ', 'χ', 'kʰʲ', 'm̥', 'n̥', 'nː', 'pː', 'lː', 'rː', 'æː', 'eː', 'o˞', 'e˞', 'a˞', 'i˞', 'iː', 'u˞', 'ʕʷ', 'ʕ', 'xʷ', 'ɬ', 'qʷ', 'ɑ', 'ɪ̃', 'ẽ', 'ʊ', 'd̪', 'd͡ʒʰ', 'ɦ', 't̪ʰ', 'd̪ʰ', 'dʰ', 'bʰ', 'ʌ', 'pʼ', 'ʊ̃', 'kʼ', 'β', 'kʼʲ', 'ħ', 'qʼ', 'cʼ', 'kʰʷ', 'qʰʷ', 'ɨ', 'ð', 'ɖ', 'ɸ', 'ʏ', 'ø', 'l̩', 'dʷ', 'pʷ', 'bʷ', 'tʷ', 'ṽ', 'z̃', 'ʃʷ', 'ʒʷ', 'a̘', 't͡s', 'n̤', 'ŋ̩', 'h̩', 'ɹ̝', 'ɑː', 'ɑ̞', 'ɑ̝', 'ɛː', 'ɪː', 'u̝', 'sʲ', 'ɜ', 'ɨː', 'θ', 'l̴', 'n̩', 'j̃', 't͡ɬ', 'sʼ', 'kʷʼ', 'cʰ', 'qʷʼ', 'zʷ', 'qʰ', 'kʷʰ', 't͡ɬʼ', 'cʷʰ', 'ʁʷ', 'tʷʼ', 'a̤', 'ɔ̤', 'o̤ː', 'i̤ː', 'ṳ', 'o̤', 'ṳː', 'ɯ̤', 'tʼ', 'ɑ̃', 'ɫ', 'ɑ̤', 'ʌ̃', 'ɛ̤', 'p͡t', 'b͡d', 'mʷ', 'w̝', 'ʎ̥', 'ɮ', 'ʃ̠', 'fː', 'i̥', 'u̥', 'ɪ̥', 'zː', 'sː', 'ʎ', 'ə̥', 'ʃː', 'e̥', 'ỹ', 'ɯ̈', 'ʉ', 'ɒ', 'xː', 'l̪', 'n̪', 'θː', 'ɒː', 'dˀ', 'bˀ', 't̟', 'æ̟', 'dⁿ', 'ɨ̠', 'tⁿ', 'a̠', 't͡sʰ', 'ɕʰ', 'm̩', 'ɭ', 'ə̃', 'ɕʼ', 't͡ʃʼ', 'ʔʷ', 'tsʰ'] # from UCLA phonetics corpus, some repeated
    missing_phonemes = []
    for phoneme in test_phonemes:
        try:
            mp = mapper.standardize_phoneme(phoneme)
            if (mp == '-') or (mp == 'SIL') or (mp=='noise'):
                missing_phonemes.append(phoneme)
                print("bad phoneme:", phoneme, "standardized:", mp)
        except KeyError:
            missing_phonemes.append(phoneme)
    print("missing_phonemes:", missing_phonemes)
    print("-" * 40)

def validate_phoneme_mapper():
    model_name = "65_phoneme"
    mapper = IPAPhonemeMapper(model=model_name)
    print("IPAPhonemeMapper initialized with model:", model_name)

    print("\nValidating mappings against indices...")
    all_mappings = mapper.get_all_mappings()
    all_indices = mapper.get_all_indices()
    
    # Check that all mapped values have indices
    mapped_values = set(all_mappings.values())
    token_indices = set(all_indices.keys())

    assert 'SIL' in token_indices, "Missing 'SIL' token index"
    assert 'noise' in token_indices, "Missing 'noise' token index"
    
    print(f"Total unique mapped values: {len(mapped_values)}")
    print(f"Total unique tokens: {len(token_indices)}")
    if (not len(token_indices) == len(mapped_values)):
        sorted_mapped_values = sorted(mapped_values)
        sorted_token_indices = sorted(token_indices)
        print("mapped_values:", sorted_mapped_values)
        print("token_indices:", sorted_token_indices)
        raise ValueError("Mismatch between mapped values and token unique standard indices") # +2 for 'noise' and 'SIL'

    print(f"Total mappings: {len(mapper.phoneme_mapping)}")
    unique_keys = set(mapper.phoneme_mapping.keys())
    print(f"Unique keys in mapping: {len(unique_keys)}")
    
    assert len(mapper.phoneme_mapping) == len(unique_keys), "Perhaps there are duplicate keys in the mapping?"

    missing_indices = mapped_values - token_indices
    if missing_indices:
        raise ValueError(f"Found mapped values without corresponding indices: {missing_indices}")
    else:
        print("All mapped values have corresponding indices!")
    print("-" * 40)




def main():
    
    validate_phoneme_mapper()

    check_missing_phonemes()

if __name__ == "__main__":
    main()
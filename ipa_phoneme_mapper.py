from typing import Union, Dict, List
import importlib
#import dictionaries.phoneme_65_empirical as phoneme_65_empirical

class IPAPhonemeMapper:
    """
    A class for standardizing IPA phonemes using predefined mapping dictionaries.
    
    Attributes:
        current_dictionary (str): Name of the currently loaded mapping dictionary
        phoneme_mapping (Dict): Dictionary containing the phoneme mapping rules
        phoneme_indices (Dict): Dictionary containing the indices for standardized phonemes
    """
    
    def __init__(self, dictionary: str = "phoneme_65_empirical"):
        """
        Initialize the IPAPhonemeMapper with a specified dictionary.
        
        Args:
            dictionary (str): Name of the mapping dictionary to use (default: "phoneme_65_empirical")
        """
        self.current_dictionary = None
        self.phoneme_mapping = {}
        self.phoneme_indices = {}
        self.set_mapping_dictionary(dictionary)
    
    def set_mapping_dictionary(self, dictionary: str) -> None:
        """
        Set the phoneme mapping dictionary to use.
        
        Args:
            dictionary (str): Name of the mapping dictionary to use
        
        Raises:
            ValueError: If the specified dictionary is not supported or if mappings are invalid
        """
        dict_module_name = f"dictionaries.{dictionary}"
        try:
            
            phoneme_65_empirical = importlib.import_module(dict_module_name, package=None)
        except ImportError:
            raise ValueError("Failed to import dictionary: "+ dict_module_name, + "Please check the dictionary name and make sure it exists in the ./dictionaries directory.")
    
        self.phoneme_mapping = phoneme_65_empirical.phoneme_mapping
        self.phoneme_indices = phoneme_65_empirical.phoneme_mapped_index
        
        # Validate that all mapped values have corresponding indices
        invalid_values = []
        for value in set(self.phoneme_mapping.values()):
            if value not in self.phoneme_indices:
                invalid_values.append(value)
        
        if invalid_values:
            raise ValueError(
                f"Found mapped values without corresponding indices: {invalid_values}"
            )
    
        self.current_dictionary = dictionary
    
    def standardize_phoneme(self, raw_phoneme: str, return_index: bool = False) -> Union[str, int]:
        """
        Standardize a single raw IPA phoneme according to the current mapping dictionary.
        
        Args:
            raw_phoneme (str): The raw IPA phoneme to standardize
            return_index (bool): If True, return the index of the standardized phoneme
        
        Returns:
            Union[str, int]: Standardized phoneme or its index if return_index is True
            return "-" if phoneme is not found, or index of 'noise' if phoneme is not found and return_index is True
        """
        if not self.has_mapping(raw_phoneme):
            #raise KeyError(f"No mapping found for phoneme: {raw_phoneme}")
            return "-" if not return_index else self.phoneme_indices["noise"]
        
        standardized = self.phoneme_mapping[raw_phoneme]
        if return_index:
            return self.phoneme_indices[standardized]
        return standardized
    
    def process_phoneme_string(self, phoneme_string: str, 
                             delimiter: str = " ", 
                             return_indices: bool = False) -> Union[str, List[int]]:
        """
        Process a string of phonemes and return standardized forms.
        
        Args:
            phoneme_string (str): String of phonemes to process
            delimiter (str): Delimiter used between phonemes in the input string
            return_indices (bool): If True, return tokens instead of phonemes
        
        Returns:
            Union[str, List[int]]: Processed phoneme string or list of indices (token numbers)
        """
        phonemes = phoneme_string.strip().split(delimiter)
        processed = []
        
        for phoneme in phonemes:
            if not phoneme:  # Skip empty phonemes
                continue
            try:
                processed.append(self.standardize_phoneme(phoneme, return_indices))
            except KeyError:
                # Handle unknown phonemes (could log warning here)
                processed.append("noise" if not return_indices else self.phoneme_indices["noise"])
        
        if return_indices:
            return processed
        return delimiter.join(processed)
    
    def has_mapping(self, phoneme: str) -> bool:
        """
        Check if a phoneme exists in the current mapping dictionary.
        
        Args:
            phoneme (str): The phoneme to check
        
        Returns:
            bool: True if the phoneme has a mapping, False otherwise
        """
        return phoneme in self.phoneme_mapping
    
    def get_all_mappings(self) -> Dict[str, str]:
        """
        Get all current phoneme mappings.
        
        Returns:
            Dict[str, str]: Dictionary of all current phoneme mappings
        """
        return self.phoneme_mapping.copy()
    
    def get_all_indices(self) -> Dict[str, int]:
        """
        Get all current phoneme indices.
        
        Returns:
            Dict[str, int]: Dictionary of all current phoneme indices
        """
        return self.phoneme_indices.copy()
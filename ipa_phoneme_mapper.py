from typing import Union, Dict, List
import models.phoneme_model_65 as model_65

class IPAPhonemeMapper:
    """
    A class for standardizing IPA phonemes using predefined mapping models.
    
    Attributes:
        current_model (str): Name of the currently loaded mapping model
        phoneme_mapping (Dict): Dictionary containing the phoneme mapping rules
        phoneme_indices (Dict): Dictionary containing the indices for standardized phonemes
    """
    
    def __init__(self, model: str = "65_phoneme"):
        """
        Initialize the IPAPhonemeMapper with a specified model.
        
        Args:
            model (str): Name of the mapping model to use (default: "65_phoneme")
        """
        self.current_model = None
        self.phoneme_mapping = {}
        self.phoneme_indices = {}
        self.set_mapping_model(model)
    
    def set_mapping_model(self, model: str) -> None:
        """
        Set the phoneme mapping model to use.
        
        Args:
            model (str): Name of the mapping model to use
        
        Raises:
            ValueError: If the specified model is not supported or if mappings are invalid
        """
        if model == "65_phoneme":
            self.phoneme_mapping = model_65.phoneme_mapping
            self.phoneme_indices = model_65.phoneme_mapped_index
            
            # Validate that all mapped values have corresponding indices
            invalid_values = []
            for value in set(self.phoneme_mapping.values()):
                if value not in self.phoneme_indices:
                    invalid_values.append(value)
            
            if invalid_values:
                raise ValueError(
                    f"Found mapped values without corresponding indices: {invalid_values}"
                )
        else:
            raise ValueError(f"Unsupported model: {model}")
        
        self.current_model = model
    
    def standardize_phoneme(self, raw_phoneme: str, return_index: bool = False) -> Union[str, int]:
        """
        Standardize a single raw IPA phoneme according to the current mapping model.
        
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
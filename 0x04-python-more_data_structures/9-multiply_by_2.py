#!/usr/bin/python3

from typing import Dict

def double_dictionary_values(input_dict: Dict[str, int]) -> Dict[str, int]:
    new_dict = input_dict.copy()

    for key in new_dict:
        new_dict[key] *= 2

    return new_dict


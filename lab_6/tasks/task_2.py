"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re
from pathlib import Path


def check_animal_list(file_path):
    id_char = '[\da-fA-F]'
    small_id_regex = f'{id_char}{{4}}-'
    id_regex = f'{id_char}{{8}}-{small_id_regex*3}{id_char}{{12}}'
    gender_regex = '[FM]'
    mass_regex = r'\d\.\d{3}e[-\+]\d{2}\n'
    regex = f'{id_regex}_{gender_regex}_{mass_regex}'
    with open(Path(file_path)) as _file:
        _file.readline()
        lines = _file.readlines()
    f_count = 0
    m_count = 0
    for line in lines:
        if re.fullmatch(regex, line):
            if re.search('_F_', line):
                f_count += 1
            else:
                m_count += 1
    return f_count, m_count


if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 0)

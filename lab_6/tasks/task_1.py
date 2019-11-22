"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
import csv
from collections import OrderedDict


def select_animals(input_path, output_path, compressed=False):
    with open(input_path) as _file:
        reader = csv.DictReader(_file)
        animals = {}
        for row in reader:
            if row['genus'] in animals.keys():
                if row['gender'] in animals[row['genus']].keys():
                    if mass_to_number(row['mass']) < mass_to_number(animals[row['genus']][row['gender']]['mass']):
                        animals[row['genus']][row['gender']] = row
                else:
                    animals[row['genus']][row['gender']] = row
            else:
                animals[row['genus']] = {row['gender']: row}
    sorted_animals = OrderedDict(sorted((animals.items())))
    out = []
    for species in sorted_animals.values():
        one_species = [gen for gen in species.values()]
        one_species.sort(key=lambda i: i['name'])
        out.extend(one_species)
    with open(output_path, 'w') as _file:
        if compressed:
            _file.write('uu')
            gender_dict = {'female': 'F', 'male': 'M'}
            writer = csv.DictWriter(_file, ['id', 'gender', 'mass'], extrasaction='ignore', delimiter='_')
            for animal in out:
                animal['mass'] = f"{mass_to_number(animal['mass']):.3e}"
                animal['gender'] = gender_dict[animal['gender']]
        else:
            writer = csv.DictWriter(_file, out[0].keys())
        writer.writeheader()
        writer.writerows(out)

def mass_to_number(mass):
    sufix = {
        'mg': 1e-6,
        'kg': 1,
        'g' : 1e-3,
        'Mg': 1e3}

    num, suf = mass.split()
    number = float(num)*sufix[suf]
    return number

if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()

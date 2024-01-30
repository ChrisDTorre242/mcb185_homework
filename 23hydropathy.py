# Kyte-Doolittle hydrophobicity Scale

import math 

## Amino acid hydropathy score reference values
def kyte_doolitle_hydropathy (aa) :
    KDH = {
        'I' : 4.5,
        'V' : 4.2,
        'L' : 3.8,
        'F' : 2.8,
        'C' : 2.5,
        'M' : 1.9,
        'A' : 1.8,
        'G' : -0.4,
        'T' : -0.7,
        'S' : -0.8,
        'W' : -0.9,
        'T' : -1.3,
        'P' : -1.6,
        'H' : -3.2,
        'E' : -3.5,
        'Q' : -3.5,
        'D' : -3.5,
        'N' : -3.5,
        'K' : -3.9,
        'R' : -4.5,
        }

    return KDH.get (aa, None)

## Amino acid sequence examples
AA_1 = ['A' , 'K' , 'I' , 'L' , 'M' , 'C' , 'D' , 'R' , 'T']
AA_2 = ['K' , 'R' , 'O' , 'N' , 'A']
AA_3 = ['E' , 'R' , 'R' , 'Q' , 'X' , 'R']

for aa in AA_1:
    hydropathy = kyte_doolitle_hydropathy(aa)
    if hydropathy is not None:
        print(f'KDH value of {aa}: {hydropathy}')
    else:
        print(f'This {aa} is not valid')

for aa in AA_2:
    hydropathy = kyte_doolitle_hydropathy(aa)
    if hydropathy is not None:
        print(f'KDH value of {aa}: {hydropathy}')
    else:
        print(f'This {aa} is not valid')

for aa in AA_3:
    hydropathy = kyte_doolitle_hydropathy(aa)
    if hydropathy is not None:
        print(f'KDH value of {aa}: {hydropathy}')
    else:
        print(f'This {aa} is not valid')
               
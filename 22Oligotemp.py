#Calculating the melting temperature of an oligo sequence

### Melting Temperature Rules 
    #For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
    #For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)

import math

def Oligo_Tm (sequence):
    A = sequence.count('A')
    T = sequence.count('T')
    G = sequence.count('G')
    C = sequence.count('C')

    if (A + T) <= 13:                   #Calcuates the melting temp for an oligo with 13 or less nt
        Tm = (A + T) * 2 + (G + C) * 4
    
    else:                               #Calcuates the melting temp for an oligo with 13 or more nt
        Tm = 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)

    return Tm

# Examples sequences
Oligo_1 = 'ATCCGGTCTCGA'
Oligo_2 = 'GCGCTTATAGCATATACGGGCC'

Tm1 = Oligo_Tm (Oligo_1)
Tm2 = Oligo_Tm (Oligo_2)

print (f'Tm of Oligo_1 is {Tm1} C')
print (f'Tm of Oligo_2 is {Tm2} C')
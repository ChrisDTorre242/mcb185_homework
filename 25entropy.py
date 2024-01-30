# Calculating Shannon Entropy for DNA sequences

## Equation => - [Sum (Probablity of (x)) * log2 (P(x))]
## Equation expanded    H(X) = - ((P(A)*log(P(A)) + (P(T)*log(P(T)) + (P(C)*log(P(C)) + (P(G)*log(P(G)))
import math

def shannon_entropy(A, T, G, C):

    # Calculating the probabilities
    total_count = A + T + G + C

    PA = A / total_count if total_count != 0 else 0
    PT = T / total_count if total_count != 0 else 0
    PG = G / total_count if total_count != 0 else 0
    PC = C / total_count if total_count != 0 else 0

    # Avoiding unreal number erro from log(0) by setting it to 0.

    PA_term = PA * math.log2(PA) if PA != 0 else 0
    PT_term = PT * math.log2(PT) if PT != 0 else 0
    PG_term = PG * math.log2(PG) if PG != 0 else 0
    PC_term = PT * math.log2(PC) if PC != 0 else 0

    # Calculating Shannon entropy

    sh_entropy = - (PA_term + PT_term + PG_term + PC_term)

    return sh_entropy

# DNA nucleotide count examples

entropy1 = shannon_entropy(10, 5, 8, 7)
entropy2 = shannon_entropy(15, 20, 0, 100)
entropy3 = shannon_entropy(25, 37, 50, 45)

print(f'Shannon entropy for seq1 is: {entropy1}')
print(f'Shannon entropy for seq2 is: {entropy2}')
print(f'Shannon entropy for seq3 is: {entropy3}')

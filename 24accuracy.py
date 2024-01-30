# Determiining Accuracy and F1 score

## Equation for accuracy => (Tp + Tn) / (Tp + Tn + Fp +Fn)

## Equation for F1 score => 2 * (precision * recall) / (precision + recall)

import math 

def experimental_data (Tp, Fp, Tn, Fn):
    # Calculating accuracy
    accuracy = (Tp + Tn) / (Tp + Fp + Tn + Fn) if (Tp + Fp + Tn + Fn) != 0 else 0

    # Calculating precision and recall to deterrmine F1 score
    precision = Tp / (Tp + Tp) if (Tp + Fp) != 0 else 0
    recall = Tp / (Tp + Fn) if (Tp + Fn) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    return accuracy, f1_score

# Examples values for experimental data

true_positives = 35
false_positives = 5
true_negatives = 48
false_negatives = 8

# Calculating accuracy and F1 score

accuracy, f1_score = experimental_data(true_positives, false_positives, true_negatives, false_negatives)

print(f'Accuracy: {accuracy}')
print(f'F1 Score: {f1_score}')
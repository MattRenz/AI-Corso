
def levenshtein_distance_batch(reference_word, words):
    distances = []
    
    for word in words:
        len1 = len(reference_word)
        len2 = len(word)
        
        # Creazione di una matrice di dimensioni (len1 + 1) x (len2 + 1)
        matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        # Inizializzazione della prima riga e della prima colonna
        for i in range(len1 + 1):
            matrix[i][0] = i
        for j in range(len2 + 1):
            matrix[0][j] = j
        
        # Calcolo della distanza di Levenshtein
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                cost = 0 if reference_word[i - 1] == word[j - 1] else 1
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,                     # Cancellazione
                    matrix[i][j - 1] + 1,                     # Inserimento
                    matrix[i - 1][j - 1] + cost                # Sostituzione
                )
        
        distances.append(matrix[len1][len2])
    
    return distances

# reference_word = "python"
# word_list = ["pyhton"]
# distances = levenshtein_distance_batch(reference_word, word_list)

# print(distances)  # Output: [1, 2, 1, 2]


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    # return previous_row[-1]/float(len(s1))
    return previous_row[-1]



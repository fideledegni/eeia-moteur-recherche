import re
import numpy as np


def generate_tokens(text):
    """ Split the text into words by removing punctuation except for
        apostrophies.

        Args:
            text (str): The text to split into words
    """
    # see: https://stackoverflow.com/a/12705513
    return re.findall(r"(\w[\w']*\w|\w)", text.lower())


def levenshtein(a, b):
    """Compute the Levenshtein distance between two strings a and b.

    Args:
        a (str): 1st string
        b (str): 2nd string

    Returns:
        int: the levenshtein distance between a and b
    
    Note:
        See https://en.wikipedia.org/wiki/Levenshtein_distance#Iterative_with_two_matrix_rows
    """
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)
    
    m, n = len(a), len(b)
    previous = list(range(n+1))
    current = [0] * (n+1)
    for i in range(m):
        current[0] = i + 1
        for j in range(n):
            substitution_cost = int(a[i] != b[j]) + previous[j]
            current[j + 1] = min(previous[j + 1] + 1, current[j] + 1, substitution_cost)
        current, previous = previous, current
    return previous[-1]


def damerau_levenshtein(a, b):
    """Compute the true (unrestricted) Damerau-Levenshtein distance between
    two strings a and b.

    Args:
        a (str): 1st string
        b (str): 2nd string

    Returns:
        int: the damerau levenshtein distance between a and b
    
    Note:
        See https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance#Distance_with_adjacent_transpositions
    """
    m, n = len(a), len(b)
    char = {} # instead of the 'da' matrix in the wiki pseudocode (see link above)
    distances = np.zeros((m+2, n+2), dtype=int)
    maxdist = m + n
    distances[0, 0] = maxdist
    
    # Filling the first 2-rows and 2-columns
    for i in range(1, m + 2):
        distances[i, 0] = maxdist
        distances[i, 1] = i - 1
    for j in range(1, n + 2):
        distances[0, j] = maxdist
        distances[1, j] = j - 1
    
    # Compute the remaining distances
    for i in range(m):
        db = 0
        for j in range(n):
            k = char.get(b[j], 0)
            l = db
            cost = int(a[i] != b[j])
            db = (1 - cost) * (j + 1)
            # new distance
            distances[i+2, j+2] = min(
                distances[i+1, j+1] + cost,         # substitution
                distances[i+2, j+1] + 1,            # insertion
                distances[i+1, j+2] + 1,            # deletion
                distances[k, l] + 1 + max(i-k, j-l) # transpostion
            )
        char[a[i]] = i + 1
    return distances[-1, -1]

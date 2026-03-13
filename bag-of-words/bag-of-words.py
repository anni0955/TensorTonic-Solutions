import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    map = {}
    for word in tokens:
        if word in map:
            map[word] += 1
        else: 
            map[word] = 1

    ans = []
    for word in vocab:
        if word in map:
            ans.append(map[word])
        else:
            ans.append(0)
    ans = np.array(ans, dtype=int)
    return ans
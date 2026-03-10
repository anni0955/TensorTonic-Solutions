def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    a = set(set_a)
    b = set(set_b)

    common = []
    for ele in a: 
        if ele in b:
            common.append(ele)

    union = set_a + set_b
    union = set(union)
    union = list(union)
    if len(union) == 0:
        return 0
    return len(common)/len(union)
    
    
def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    map = {}
    for sen in sentences:
        for word in sen:
            if word not in map:
                map[word] = 1

            else:
                map[word] += 1

    return map
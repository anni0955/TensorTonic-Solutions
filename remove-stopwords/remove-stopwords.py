def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    ans=[]
    for word in tokens:
        if word in stopwords:
            continue
        else:
            ans.append(word)

    return ans
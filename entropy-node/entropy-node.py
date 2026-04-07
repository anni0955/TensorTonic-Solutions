import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0:
        return 0.0
    map = {}
    for ele in y:
        if ele not in map:
            map[ele] = 1
        else:
            map[ele] += 1

    ans = 0
    for ele in map.items():
        val = ele[1] / len(y)
        ans += (val * np.log2(val))
    return -ans
    
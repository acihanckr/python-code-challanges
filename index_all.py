import numpy as np
def index_all(lst, val):
    indices = []
    for i, element in enumerate(lst):
        if element == val:
                indices.append([i])
        elif isinstance(element, list):
            for index in index_all(element,val):
                indices.append([i] + index)
    return indices

print(index_all([[[1,2,2],2,[1,2]],[1,2,3]],2))
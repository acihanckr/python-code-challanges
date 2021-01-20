def index_all(lst, val):
    
    indices = []
    for i, element in enumerate(lst):
        if element == val:
            return i
        elif isinstance(element,list):
            index = index_all(element,val)
            if isinstance(index, list):
                indices.append([i] + index)
            else:
                indices.append([i,index])
    return indices

print(index_all([[[1,2,3],2,[1,3]],[1,2,3]],2))
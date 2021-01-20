def sort_words(string):
    string_lst = string.split()
    string_dict = {v.lower():v for v in string_lst}
    sorted_values = [string_dict[k] for k in sorted(string_dict.keys())]
    string = ''
    for word in sorted_values:
        string += word + ' '
    
    return string[:-1]

print(sort_words('banana ORANGE apples'))
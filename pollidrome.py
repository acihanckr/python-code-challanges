def is_poll(string):
    string_lst = [char for char in string if char.isalpha()]
    string_lst_reverse = string_lst[::-1]
    string = ''
    string_reverse = ''
    for char in string_lst:
        string += char
    for char in string_lst_reverse:
        string_reverse += char
    return string_reverse.lower()==string.lower()

print(is_poll("Go hang a salami - I'm a lasagna hog"))
print(is_poll('Race car'))
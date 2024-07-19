call = 0
def count_call():
    global call
    call = call + 1
def string_info(str):
    count_call()
    r = len(str)
    str1 = str.upper()
    str2 = str.lower()
    return r, str1, str2
def is_contains(string, list_to_search):
    count_call()
    flag = True
    for i in range(len(list_to_search)):
        if string.upper() == list_to_search[i].upper():
            flag = True
        else: flag = False
    return flag
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urban']))
print(is_contains('cycle',['recycling', 'cyclic']))
print(call)


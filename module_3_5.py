def get_multiplied_digits(number):
    str_numder = str(number)
    first = int(str_numder[0])
    if len(str_numder) > 1:
        return first * get_multiplied_digits(int(str_numder[1:]))
    else: return first


result = get_multiplied_digits(40203)
print(result)
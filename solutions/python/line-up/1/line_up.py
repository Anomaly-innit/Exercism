def line_up(name, number):
    result = ""
    str_number = str(number)
    if str_number.endswith("1") and not str_number.endswith("11"):
        result = f"{name}, you are the {str_number}st customer we serve today. Thank you!"
    elif str_number.endswith("2") and not str_number.endswith("12"):
        result = f"{name}, you are the {str_number}nd customer we serve today. Thank you!"
    elif str_number.endswith("3") and not str_number.endswith("13"):
        result = f"{name}, you are the {str_number}rd customer we serve today. Thank you!"
    else:
        result = f"{name}, you are the {str_number}th customer we serve today. Thank you!"
    return result
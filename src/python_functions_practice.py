def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2 

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number( num1, num2 ):
    return int(num1) + int(num2)

def number_to_full_month_name(month):
    months_of_year_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months_of_year_list[int(month) - 1] 

def number_to_short_month_name(short_month):
    month_list_abbreviated = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return month_list_abbreviated[int(short_month)- 1]


def volume_of_cube(size1, size2, size3):
    return size1 * size2 *size3



    
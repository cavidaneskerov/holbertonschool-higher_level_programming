#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                raise TypeError("wrong type")
            division = num1 / num2
        except IndexError:
            print("out of range")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        finally:
            result.append(division)
    return result

#Example COMP1020
#March 14 2023

from foo import whiz_bang, beep_boop

def run_whiz_bang():
    whiz_bang(True, True)

def run_beep_boop():
    beep_boop(10, 3)

def run_whiz_boop():
    pass

def sum_int_and_string_value(int_value, str_value):
    """
    Sums an integer and a string representing an integer.

    :param int_value: An integer value
    :param str_value: A string representation of an integer value
    :return: An integer which is the sum of the two values.
    """
    sum = int_value + int(str_value)
    return sum

def main():
    run_whiz_bang()
# Not needed to see error with whiz_bang
#    run_beep_boop()
#    run_whiz_boop()

#Working with Truthiness
    # my_list = []
    # not_a_list = None
    # if not not_a_list:
    #     print("not_a_list is not a list")
    # if my_list == False:
    #     print("it's true!")
    # if not my_list:
    #     print("it's non-empty!")
    # if bool(my_list) == False:
    #     print("boolean is true!")
    #
    # print(bool([1,2,3]))
    # print([1,2,3] == [1,2,3])
    # print(bool([]))
    # print([1,2,3]!=None)

# Demonstrating Docstrings
    help(print)
    help(whiz_bang)
    print(sum_int_and_string_value(4, "5"))
    help(sum_int_and_string_value)

if __name__ == "__main__":
    main()

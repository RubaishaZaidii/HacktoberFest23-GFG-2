def largest_element(input_list):
    if not input_list:
        return None  
    else:
        return max(input_list)

my_list = [10, 25, 5, 99, 50, 42, 88]

largest = largest_element(my_list)

if largest is not None:
    print("The largest element in the list is:", largest)
else:
    print("The list is empty.")

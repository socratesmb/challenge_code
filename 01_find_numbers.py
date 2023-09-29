def match_number(list, target):
    # New objet for save numbers in list
    list_numb = set()
    # Scroll numbers in list
    for number in list:
        # Calculated complement whit operation
        comp = target - number
        # Validation if exits complement in list
        if comp in list_numb:
            # Show exit in format like example
            print(f"+ {number},{comp}")
        # End process and add list numbers
        list_numb.add(number)

if __name__ == "__main__":
    inp = input("List of numbers separated by ,: ")
    # Input number cast to int
    target = int(input("Value Target: "))
    # Convert text to list
    list = [int(num) for num in inp.split(',')]
    # Run function
    match_number(list, target)
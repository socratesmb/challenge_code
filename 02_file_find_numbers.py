import time
def match_number(list, target):
    list_numb = set()
    for number in list:
        comp = target - number
        if comp in list_numb:
            print(f"+ {number},{comp}")
        list_numb.add(number)

if __name__ == "__main__":
    # Var for save name document
    file_name = 'numbers.txt'
    try:
        # Open and read data
        with open(file_name, 'r') as document:
            list_text = document.readline().strip()
        list = [int(num) for num in list_text.split(',')]
        target = int(input("Value Target: "))
        star_time=time.time()
        match_number(list, target)
        end_time = time.time()
        print('Time:', star_time -  end_time)
        
    except FileNotFoundError:
        print(f"File '{file_name}' no found")
    except ValueError:
        print("Data numbers in file not valid")
import sys

total = 0
#numbers = ['','1', '2', '', '', '', '3,6', '4', '-5', '6', '', '', '', '']

def file_input():
    first_line = sys.stdin.readline().strip()

    if ' ' in first_line or '\t' in first_line:
        numbers = first_line.split()
    else:
        numbers = [first_line]
        for line in sys.stdin:
            number = line.strip()
            numbers.append(number)

    print(numbers)
    return numbers

numbers = file_input()

def remove_white_chars(numbers):
    index_to_delete = []        
    for i in range(0, len(numbers)):
        if numbers[i] == '':
            index_to_delete.append(i)
    num_of_deletions = 0
    for index in index_to_delete:
        index -= num_of_deletions
        del numbers[index]
        num_of_deletions += 1

remove_white_chars(numbers)

print(numbers)

def format_floats(numbers):
    i = 0
    for number in numbers:
        if '.' in number:
            numbers[i] = float(number)
        elif ',' in number:
            numbers[i] = numbers[i].replace(",",".")
            numbers[i] = float(numbers[i])
        else:
            numbers[i] = int(number)
        i += 1

format_floats(numbers)   

for number in numbers:
    print(type(number))


# for number in numbers:
#     if type(number) == int or type(number) == float:
#         continue
#     else:
#         raise ValueError(f"err - {number}")

def palindrome_checker(word):
    if word == word[::-1]:
        return True
    return False

# print(palindrome_checker("hannah"))

# fibonacci = 0, 1, 1, 2, 3, 5, 8 etc
            # 1, 2, 3, 4, 5, 6

def fibonacci_number(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci_number(number-1) + fibonacci_number(number-2)

# print(fibonacci_number(35))

repeats_list = ["red", "blue", "blue", "red", "green", "green", "yellow", "yellow", "blue", "blue", "yellow", "yellow", "pink", "pink"]

def unique_repeat_count(list):
    counter = 0
    repeated_words = []
    for index in range(0, len(list)-1):
        if (list[index] not in repeated_words) and (list[index] == list[index + 1]):
            counter += 1
            repeated_words.append(list[index])
    return counter

print(unique_repeat_count(repeats_list))

START_NUMBER = 1 
MULTIPLES_LIST = []
LIMIT = 1000

def generate_multiples(limit, start_number):
    """
    Generates a list of natural numbers that are multiples of 3 or 5 up to a given limit.
    """
    number = start_number
    while number < limit:
        if number % 3 == 0 or number % 5 == 0:
            MULTIPLES_LIST.append(number)
        number += 1

def calculate_sum(numbers_list):
    """
    Calculates the sum of a list of numbers.
    """
    total = sum(numbers_list)
    return total

if __name__ == "__main__":
    generate_multiples(LIMIT, START_NUMBER)
    print(MULTIPLES_LIST)
    total_sum = calculate_sum(MULTIPLES_LIST)
    print(total_sum)
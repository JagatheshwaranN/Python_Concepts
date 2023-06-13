def sum_of_numbers(numbers):
    if not numbers:
        return 0
    else:
        # print("Calling sum_of_numbers(%s)" % numbers[1:])
        remaining_sum = sum_of_numbers(numbers[1:])
        # print("Call to Sum_of_numbers(%s) returning %d + %d" %(numbers, numbers[0], remaining_sum))
        return numbers[0] + remaining_sum


print(sum_of_numbers([1, 2, 3, 4]))

def steps(number):
    if number < 1:
        raise ValueError('Positive number required')
    so_far = 0
    while number > 1:
        so_far += 1
        number = number / 2 if number % 2 == 0 else 3*number + 1
    return so_far

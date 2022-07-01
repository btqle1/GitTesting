from random import randint

def solution(xs):

    negative_counter = 0
    non_zero_counter = 0
    smallest = 0
    solution = 1
    temp = []

    # subset of 1. return that single one
    if len(xs) == 1:
        return(str(xs[0]))

    # check for number of negatives. place negatives into a temp array
    for i in range(len(xs)):
        if xs[i] < 0:
            negative_counter = negative_counter + 1
            temp.append(xs[i])
        if xs[i] != 0:
            non_zero_counter = non_zero_counter + 1

    # subet of only 1 negative and zeros
    if non_zero_counter == 1 & negative_counter == 1:
        return str(0)

    # check even/odd number of negatives
    negative_counter = negative_counter % 2

    # subset of only 0s
    if non_zero_counter == 0:
        return str(0)

    # find the absolute value smallest in temp list
    if len(temp) > 0:
        smallest = temp[0]
        for i in range(len(temp)):
            if temp[i] > smallest:
                smallest = temp[i]

    # if negatives amount is even, then just multiply all. skip 0s
    if negative_counter == 0:
        for i in range(len(xs)):
            if xs[i] == 0:
                continue
            solution = solution * xs[i]
        return str(solution)

    # if negatives amount is odd, skip the smallest (one instance only), then multiply all. skip 0s
    if negative_counter == 1:

        for i in range(len(xs)):
            if xs[i] == 0:
                continue
            solution = solution * xs[i]
        solution = int(solution / smallest)
        return str(solution)

big_array = [randint(-1000, 1000) for _ in range(51)]
#xs = [696, 254, 707, 730, 252, 144, 18, -678, 921, 681, -665, 421, -501, 204, 742, -609, 672, -72, 339, -555, -736, 230, -450, 375, 941, 50, 897, -192, -912, -915, 609, 100, -933, 458, -893, 932, -590, -209, 107, 473, -311, 73, 68, -229, 480, 41, -235, 558, -615, -289, -643]
xs = [0, -5]

x = solution(xs)
# print(big_array)
print(x)


# Find the largest palindrome made from the product of two 3-digit numbers

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else :
        return False

#
def biggest_palindrome(num):
    biggestDigit = "9"
    smallestDigit = "1"
    for i in range(num-1):
        biggestDigit += str(9)
        smallestDigit += str(0)

    biggestDigit, smallestDigit = int(biggestDigit), int(smallestDigit)

    a, b = smallestDigit, smallestDigit
    big_num_a, big_num_b = 0, 0
    palindrome = 0

    while b != biggestDigit+1:
        prodNumber = a * b
        if is_palindrome(prodNumber) and (prodNumber > palindrome):
            palindrome = prodNumber
            big_num_a = a
            big_num_b = b
        else:
            a += 1
            if a > biggestDigit:
                b += 1
                a = b

    return palindrome, big_num_a, big_num_b


print(biggest_palindrome(3))
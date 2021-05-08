# factors
def getFactors(n):
    # Create an empty list for factors
    factors = []

    # Loop over all factors
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    # Return the list of factors
    return factors


# Call the function with a given value
print(getFactors(256))


def fizzbuzz(v):
    if v % 3 == 0 and v % 5 == 0:
        print("frizznuss")
    elif v % 5 == 0:
        print("buzz")
    elif v % 3 == 0:
        print("frizz")
    else:
        return False


print(fizzbuzz(73))


# power of x ^ y

def power(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res


print(power(1, 0))

s = "W3resource"
d = l = 0
for c in s:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    else:
        pass
print("Letters", l)
print("Digits", d)


# Function for nth Fibonacci number
def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Driver Program
print(Fibonacci(9))

# This code is contributed by Saket Modi
# then corrected and improved by Himanshu Kanojiya

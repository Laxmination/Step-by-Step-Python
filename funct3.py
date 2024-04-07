#WAF to find the factorial of n. (n is the parameter)
def calc_fact(n):
    fac =1

    for i in range (1, n+1):
        fac *= i

    print("Factorial of given number is: ", fac)
    return fac

calc_fact(5)
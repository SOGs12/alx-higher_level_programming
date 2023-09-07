#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # Perform calculations and print results
    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    # Print the results with the desired format
    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_sub))
    print("{} * {} = {}".format(a, b, result_mul))
    print("{} / {} = {}".format(a, b, result_div))

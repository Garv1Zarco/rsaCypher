from src.mathTools import MathTools


def euler_phi_function_test():
    a = MathTools.euler_phi_function(1998)
    b = MathTools.euler_phi_function(1023)
    c = MathTools.euler_phi_function(4982)

    print(a)
    print(b)
    print(c)

    if a == 648 and b == 600 and c == 2392:
        print("euler_phi_function works correcly!")
    else:
        print("euler_phi_function does not work correcly")


def inv_mod_test():
    a = MathTools.inv_mod(12, 19)
    b = MathTools.inv_mod(11, 94)

    if a == 7 and b == 2:
        print("Modular inverse works")
    else:
        print("modular inverse does not work")


print(MathTools.is_coprime(686871, 435397))
print(MathTools.inv_mod(686871, 435397))
print((435397 * 125089) % MathTools.euler_phi_function(686871))


def low_prime_test():
    a = MathTools.low_prime_gen()
    b = MathTools.low_prime_gen()

    print(a, b)

    print(MathTools.get_roots(a), MathTools.get_roots(b))


low_prime_test()

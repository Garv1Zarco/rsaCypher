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


MathTools.inv_mod(9840, 17)

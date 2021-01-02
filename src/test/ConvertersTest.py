from src.mathTools import Converters


def str2int_int2str_test():
    m = "jajajaja hola que tal me cago en la puta"
    mc = Converters.str2int(m)
    mx = Converters.int2str(mc)
    if mx != m:
        print("Is not working")
    else:
        print("It works")

str2int_int2str_test()

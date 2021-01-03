from modules import rsaEntity
from modules import UserEntity
from mathTools import MathTools


def main():
    rsa = rsaEntity.Rsa()
    rsa.key_gen()
    print("Is coprime: ", MathTools.is_coprime(rsa.e, rsa.n))
    print("Value of n: ", rsa.n)
    print("This value have to be 1: ", (rsa.d * rsa.e) % MathTools.euler_phi_function(rsa.n))
    sender = UserEntity.User()
    reciever = UserEntity.User()
    m = "me"
    c = sender.cypher(rsa, m)
    m = reciever.decipher(rsa, c)
    print("Final message: ", m)


main()

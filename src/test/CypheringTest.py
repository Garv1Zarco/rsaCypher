from src.modules import rsaEntity
from src.mathTools import Converters
from src.mathTools import MathTools
from src.modules import UserEntity


def cypher_test(m):
    x = 0
    iterations = 1000
    for i in range(iterations):

        # --------  RSA Generation  -------- #

        rsa = rsaEntity.Rsa()
        rsa.key_gen()
        public_key = rsaEntity.Rsa.get_public_key(rsa)
        private_key = rsaEntity.Rsa.get_private_key(rsa)
        p = rsa.p
        q = rsa.q
        e = public_key[1]
        ne = public_key[0]
        d = private_key[1]
        nd = private_key[0]

        mb = Converters.str2int(m)
        n = nd

        # --------  Error messages  -------- #

        if nd != ne:
            print("n's does not belong")
        if (e * d) % MathTools.euler_phi_function(p, q) != 1:
            print("d and e does not belong")
        if rsa.n < mb:
            print("WARNING: n is lower than message")

        # --------  Value messages  -------- #

        n = nd
        print("Values of RSA variables nº", i, ":")
        print("p = ", p)
        print("q = ", q)
        print("n = ", n)
        print("e = ", e)
        print("d = ", d)
        print("phi(n) = ", MathTools.euler_phi_function(p, q))

        print("p roots: ", MathTools.get_roots(p), "q roots: ", MathTools.get_roots(q))

        # --------  Cyphering and Deciphering processes  -------- #

        sender = UserEntity.User()
        receiver = UserEntity.User()

        c = sender.cypher(rsa, m)
        mx = receiver.decipher(rsa, c)

        # --------  Conclusion messages  -------- #

        if m != mx:
            print("/////Cyphering did not work/////")
        else:
            x = x + 1
            print("-----Cyphering successed-----")

    print((x / iterations) * 100, "%")

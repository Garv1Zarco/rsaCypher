from src.modules import rsaEntity
from src.mathTools import Converters
from src.mathTools import MathTools


def cypher_test():
    x = 0
    iterations = 1000
    for i in range(iterations):
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

        m = "a"

        mb = Converters.str2int(m)
        n = nd

        if nd != ne:
            print("n's does not belong")
        if (e * d) % MathTools.euler_phi_function(n) != 1:
            print("d and e does not belong")
        if rsa.n < mb:
            print("WARNING: n is lower than message")

        n = nd
        print("p = ", p)
        print("q = ", q)
        print("n = ", n)
        print("e = ", e)
        print("d = ", d)
        print("phi(n) = ", MathTools.euler_phi_function(n))

        print("p roots: ", MathTools.get_roots(p),"p roots: ", MathTools.get_roots(q))

        c = pow(mb, e, n)
        mbx = pow(c, d, n)
        mx = Converters.int2str(mbx)

        if m != mx:
            print("Cyphering did not work")
        else:
            x = x + 1
            print("Cyphering successed")
    print((x/iterations)*100, "%")
cypher_test()



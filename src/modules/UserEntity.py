from src.modules import rsaEntity
from src.mathTools import Converters


class User:
    def cypher(Self, Rsa, m):
        public_key = rsaEntity.Rsa.get_public_key(Rsa)
        e = public_key[1]
        n = public_key[0]
        mb = Converters.str2int(m)

        c = pow(mb, e, n)
        return c

    def decypher(Self, Rsa, c):
        private_key = rsaEntity.Rsa.get_private_key(Rsa)
        d = private_key[1]
        n = private_key[0]

        mb = pow(c, d, n)

        m = Converters.int2str(mb)
        return m

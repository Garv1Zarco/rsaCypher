from src.modules import rsaEntity
from src.mathTools import Converters


# The User object is able to do 2 actions, cypher and decipher from a given RSA object
# and a message m


class User:

    def cypher(Self, Rsa, m):  # Returns a cyphered message c from a plain message m
        public_key = rsaEntity.Rsa.get_public_key(Rsa)  # Public key get
        e = public_key[1]
        n = public_key[0]
        mb = Converters.str2int(m)  # Message m coded (mb)

        c = pow(mb, e, n)  # c = (mb ** e) mod n
        return c

    def decipher(Self, Rsa, c):  # Returns a deciphered message m from a plain message c
        private_key = rsaEntity.Rsa.get_private_key(Rsa)  # Private key get
        d = private_key[1]
        n = private_key[0]

        mb = pow(c, d, n)  # mb = (c ** d) mod n

        m = Converters.int2str(mb)  # Message received mb decoded (m)
        return m

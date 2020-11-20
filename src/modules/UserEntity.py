from src.modules import rsaEntity
import binascii


def str2int(m):
    mb = 0
    for i in m:
        chi = ord(i)
        if len(str(chi)) < 3:
            mb = mb + "0"
        mb = str(mb) + str(chi)
    mb = mb[1:]
    mb = int(mb)
    return mb


def int2str(mb):
    m = ""
    mb = str(mb)
    for j in range(int(len(mb)/3)):
        chi = ""
        ch = ""
        for i in range(3):
            chi = mb[j+i]
            ch = ch + chi
        m = m + chr(int(ch))
    return m


class User():
    def cypher(Self, Rsa, m):
        public_key = rsaEntity.Rsa.get_public_key(Rsa)
        e = public_key[1]
        n = public_key[0]
        mb = str2int(m)

        c = (mb ** e) % n
        return c

    def decypher(Self, Rsa, c):
        private_key = rsaEntity.Rsa.get_private_key(Rsa)
        d = private_key[1]
        n = private_key[0]

        mb = (c ** d) % n

        m = int2str(mb)
        return m

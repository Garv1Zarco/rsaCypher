from src.mathTools import MathTools
import random


class Rsa:

    # Definition of the main parameters of a RSA cypher
    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.e = 0
        self.d = 0
        self.public_key = []
        self.private_key = []

    def key_gen(self):  # This method generates the values of the main variables for an RSA object

        while self.p == self.q:
            self.p = MathTools.low_prime_gen()  # Prime number p
            self.q = MathTools.low_prime_gen()  # Prime number q
            self.n = self.p * self.q  # n = p * q

        phi_n = MathTools.euler_phi_function(self.p, self.q)  # Euler phi function for n

        coprime = False

        while not coprime:  # This loop makes sure e and phi_n are coprimes
            self.e = random.randint(2, phi_n - 1)
            coprime = MathTools.is_coprime(self.e, phi_n)

        self.d = MathTools.inv_mod(phi_n, self.e)  # Generation of d -> d*e = 1 mod(phi_n)

        self.public_key = [self.n, self.e]
        self.private_key = [self.n, self.d]

    # Getters for public and private keys:
    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key

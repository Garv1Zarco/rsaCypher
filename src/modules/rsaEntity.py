from typing import Any

from src.mathTools import MathTools
import random


class Rsa:

    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.e = 0
        self.d = 0
        self.public_key = []
        self.private_key = []

    def key_gen(self):

        while self.p == self.q:
            self.p = MathTools.low_prime_gen()
            self.q = MathTools.low_prime_gen()
        self.n = self.p * self.q
        phi_n = MathTools.euler_phi_function(self.n)

        coprime = False

        while not coprime:
            self.e = random.randint(2, phi_n - 1)
            coprime = MathTools.is_coprime(self.e, phi_n)

        self.d = MathTools.inv_mod(phi_n, self.e)

        self.public_key = [self.n, self.e]
        self.private_key = [self.n, self.d]

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key


from utils import *
import sympy


class RSA:
    def __init__(self):
        p, q = getRandomPrimes(512, 2)
        phi = (p - 1) * (q - 1)
        self.N = p * q
        self.e = 0x10001
        self.d = sympy.mod_inverse(self.e, phi)

    def encrypt(self, m):
        return pow(m, self.e, self.N)

    def decrypt(self, c):
        return pow(c, self.d, self.N)


if __name__ == "__main__":
    rsa = RSA()

    m = [10, 7, 4, 3, 2]
    print(f"Message: {m}")
    c = [rsa.encrypt(i) for i in m]
    print(f"Encrypt: {c}")
    d = [rsa.decrypt(i) for i in c]
    print(f"Decrypt: {d}")

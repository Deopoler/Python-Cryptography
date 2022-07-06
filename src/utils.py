import sympy

def getRandomPrimes(bits, count):
    results = []
    for _ in range(count):
        founded = False
        while not founded:
            founded = True
            x = sympy.randprime(2 ** (bits - 1), 2 ** (bits))
            for i in results:
                if i % x == 0 or x % i == 0:
                    founded = False

        results.append(x)

    return results

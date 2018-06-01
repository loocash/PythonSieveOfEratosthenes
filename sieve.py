# Sieve of Eratosthenes

from bisect import bisect_right
from math import sqrt, floor


class Sieve:

    def first(self, k):
        return self.primes[:k]

    def up_to(self, k):
        index = bisect_right(self.primes, k)
        return self.primes[:index]

    def __init__(self, size):
        assert (1 < size < 2 ** 30)
        self.size = size
        self._sieve()
        self._make_primes()

    def _sieve(self):
        is_prime = [True for _ in range(self.size + 1)]

        is_prime[0], is_prime[1] = False, False
        bound = int(floor(sqrt(self.size + 1)))
        for i in range(2, bound):
            if not is_prime[i]:
                continue
            for j in range(i * i, self.size + 1, i):
                is_prime[j] = False

        self.is_prime = is_prime

    def _make_primes(self):
        self.primes = list(filter(lambda x: self.is_prime[x], range(self.size + 1)))

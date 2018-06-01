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
        self.isPrime = [True for _ in range(self.size + 1)]
        self.isPrime[0] = self.isPrime[1] = False
        bound = int(floor(sqrt(self.size + 1)))
        for i in range(2, bound):
            if self.isPrime[i]:
                for j in range(i * i, self.size + 1, i):
                    self.isPrime[j] = False

    def _make_primes(self):
        self.primes = list(filter(lambda x: self.isPrime[x], range(self.size + 1)))

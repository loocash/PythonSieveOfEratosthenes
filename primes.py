r"""
An implementation of the ``Sieve of Eratosthenes`` algorithm.
For a given upper bound of ``n`` performs O(n lg lg n) preprocessing
and then answers the question of primality of a number from a range
[2; n] (including n) in O(1) (constant) time.

>>> primes = Primes(100)
>>> print(primes.up_to(20))
[2, 3, 5, 7, 11, 13, 17, 19]
>>> print(primes.is_prime[83])
True
>>> print(primes.is_prime[100])
False
>>> print(primes.first(5))
[2, 3, 5, 7, 11]
"""

from bisect import bisect_right
from math import sqrt, floor


class Primes:

    def first(self, k):
        return self.primes[:k]

    def up_to(self, k):
        index = bisect_right(self.primes, k)
        return self.primes[:index]

    def __init__(self, size):
        self.size = size
        self._sieve()
        self._make_primes()

    def _sieve(self):
        is_prime = [True] * (self.size + 1)

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

    def __repr__(self):
        module = self.__class__.__module__
        name = self.__class__.__name__
        return f"{module}.{name}({self.size})"

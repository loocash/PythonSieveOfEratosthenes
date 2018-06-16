import unittest
from primes import Primes


class TestSieve(unittest.TestCase):
    def setUp(self):
        self.primes = Primes(100)

    def test_size(self):
        self.assertEqual(self.primes.size, 100)

    def test_isPrime_83(self):
        self.assertEqual(self.primes.is_prime[83], True)

    def test_first_5_primes(self):
        self.assertEqual(self.primes.first(5), [2, 3, 5, 7, 11])

    def test_primes_up_to_13(self):
        self.assertEqual(self.primes.up_to(13), [2, 3, 5, 7, 11, 13])

    def test_primes_up_to_100(self):
        self.assertEqual(self.primes.up_to(100),
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                          97])

    def test_primes_1000th_prime_is_7919(self):
        s = Primes(10000)
        self.assertEqual(s.first(1000)[-1], 7919)


if __name__ == '__main__':
    unittest.main()

import unittest
from sieve import Sieve

class TestSieve(unittest.TestCase):
  def setUp(self):
    self.sieve = Sieve(100)

  def test_size(self):
    self.assertEqual(self.sieve.size, 100)

  def test_isPrime_83(self):
    self.assertEqual(self.sieve.isPrime[83], True)

  def test_first_5_primes(self):
    self.assertEqual(self.sieve.first(5), [2, 3, 5, 7, 11])

  def test_primes_upto_13(self):
    self.assertEqual(self.sieve.upto(13), [2, 3, 5, 7, 11, 13])

  def test_primes_upto_100(self):
    self.assertEqual(self.sieve.upto(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

  def test_primes_1000th_prime_is_7919(self):
    s = Sieve(10000)
    self.assertEqual(s.first(1000)[-1], 7919)

if __name__ == '__main__':
  unittest.main()

import math
import unittest
import random

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15,
                            msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")

    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01,
                            msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


def wallis(n):
    p = 1
    t=2
    for i in range(n):
        left = t/(t-1)
        right = t/(t+1)
        p *= left * right
        t = t+2

    return p*2

def monte_carlo(n):
    circle = 0
    square = 0
    for i in range(n ** 2):
        x = random.random()
        y = random.random()
        cent = x ** 2 + y ** 2
        if cent <= 1:
            circle += 1
        square += 1
        pi_mc = 4 * circle / square
    return pi_mc


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)

        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05,
                         "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4,
                            msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")



if __name__ == "__main__":
    unittest.main()

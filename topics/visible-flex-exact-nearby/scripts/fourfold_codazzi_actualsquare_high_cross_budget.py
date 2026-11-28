"""Exact rational comparisons for ASQ5. No numerical producer is imported."""
from fractions import Fraction as F


def compare():
    theta = F(17082, 1000)
    assert F(10123545, 1000000) + F(6957962, 1000000) < theta
    assert 1 + (4 * 96) ** 2 < 2 ** 18
    assert 2 + 2 ** 6 / F(4) < 2 ** 5
    assert 17 + 316 + 9 - 1536 == -1194
    assert 199 - 1536 == -1337
    results = []
    for exponent, allowance in ((1335, F(5695, 1000)), (1330, F(135, 1000)),
                                (1293, F(1, 2**38))):
        high = F(1, 2**44) + F(2**exponent, 2**1337)
        full = high + F(1, 2**1194)
        assert high < 1
        assert theta * full / (1 - high) < allowance
        results.append((exponent, str(allowance)))
    return results


if __name__ == "__main__":
    for threshold, cost in compare():
        print(f"C_add <= 2^{threshold}: added whole-matrix cost < {cost} times delta_X")

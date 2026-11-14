#!/usr/bin/env python3
"""Independent forward/reverse arithmetic checks for primitive cube denominators.

The unlimited completeness argument is in the companion note.  These finite
checks verify its identities, signs, parity cases, and inverse reconstruction.
"""
import sys
sys.dont_write_bytecode = True

from collections import Counter, defaultdict
from math import gcd, isqrt
import json


def F(a, b):
    return a**4 - 18*a*a*b*b - 27*b**4


def G(a, b):
    return 27*b**4 - 18*a*a*b*b - a**4


def fourth_root(n):
    assert n > 0
    root = isqrt(isqrt(n))
    assert root**4 == n
    return root


def recover(X, T, W):
    assert X > T and W != 0
    assert X**3 - T**3 == 27*W*W
    assert gcd(X, T) == 1 and (X*T) % 3
    A = X-T
    B = X*X + X*T + T*T
    assert gcd(A, B) == 3
    assert A % 9 == 0 and B % 3 == 0
    V, U = isqrt(A//9), isqrt(B//3)
    assert 9*V*V == A and 3*U*U == B and U*V == abs(W)
    assert gcd(U, V) == 1 and U % 3
    R = 2*U - (2*T+9*V*V)
    S = 2*U + (2*T+9*V*V)
    assert R > 0 and S > 0 and R*S == 27*V**4
    scale = 1 if V % 2 else 4
    assert gcd(R, S) == scale
    if R % 3:
        a, b = fourth_root(R//scale), fourth_root(S//(27*scale))
        form, polynomial = "G", G
    else:
        a, b = fourth_root(S//scale), fourth_root(R//(27*scale))
        form, polynomial = "F", F
    assert gcd(a, b) == 1 and a % 3
    if V % 2:
        assert a % 2 and b % 2 and V == a*b
        assert T == polynomial(a, b)//4
        assert polynomial(a, b) % 4 == 0
    else:
        assert (a+b) % 2 and V == 2*a*b and V % 4 == 0
        assert T == polynomial(a, b)
    return form, V % 2, a, b


def main():
    forward = Counter()
    residues = defaultdict(set)
    for a in range(1, 65):
        for b in range(1, 65):
            if gcd(a, b) != 1 or a % 3 == 0:
                continue
            assert F(a, b) == 4*a**4 - 3*(a*a+3*b*b)**2
            assert G(a, b) == 3*(a*a-3*b*b)**2 - 4*a**4
            odd = a % 2 == b % 2 == 1
            if not odd:
                assert (a+b) % 2
                U, V = a**4 + 27*b**4, 2*a*b
                cases = [("I", "F", F(a,b)), ("III_odd_X", "G", G(a,b))]
            else:
                assert F(a,b) % 32 == 20 and G(a,b) % 32 == 8
                U, V = (a**4+27*b**4)//4, a*b
                cases = [("III_even_X", "F", F(a,b)//4), ("II", "G", G(a,b)//4)]
                hp, hm = (a*a+3*b*b)//2, (a*a-3*b*b)//2
                assert gcd(a,hp) == gcd(a,hm) == 1
                assert F(a,b)//4 == a**4-3*hp*hp
                assert G(a,b)//4 == 3*hm*hm-a**4
            for name, form, T in cases:
                X = T+9*V*V
                W = U*V
                assert X**3-T**3 == 27*W*W
                assert gcd(X,T) == gcd(X,W) == gcd(T,W) == 1
                assert (X*T) % 3
                if name == "I":
                    assert X % 4 == 1 and W % 2 == 0
                elif name == "III_odd_X":
                    assert X % 4 == 3 and W % 2 == 0
                elif name == "III_even_X":
                    assert X % 8 == 6 and T % 8 == 5 and W % 2
                else:
                    assert X % 8 == 3 and T % 8 == 2 and W % 2
                for sign in (1,-1):
                    assert recover(X,T,sign*W) == (form,int(odd),a,b)
                    forward[name] += 1
                    residues[name].add((X % 8,T % 8,sign*W % 8))

    reverse = Counter()
    signs = Counter()
    bound = 1000
    for T in range(-bound, bound+1):
        if T % 3 == 0:
            continue
        for X in range(T+1,bound+1):
            if X % 3 == 0 or gcd(X,T) != 1:
                continue
            numerator = X**3-T**3
            if numerator % 27:
                continue
            W = isqrt(numerator//27)
            if W == 0 or W*W != numerator//27:
                continue
            form, odd, a, b = recover(X,T,W)
            assert recover(X,T,-W) == (form,odd,a,b)
            reverse[f"{form}, V_{'odd' if odd else 'even'}"] += 1
            signs[f"X_{'positive' if X>0 else 'negative'}, T_{'positive' if T>0 else 'negative'}"] += 1
    assert len(reverse) == 4
    assert signs["X_negative, T_negative"] > 0
    assert signs["X_positive, T_negative"] > 0
    assert signs["X_positive, T_positive"] > 0
    print(json.dumps({
        "forward_parameter_range": [1,64],
        "forward_signed_W_counts": dict(sorted(forward.items())),
        "forward_residues_mod_8": {k:sorted(v) for k,v in sorted(residues.items())},
        "reverse_box_abs_X_T_at_most": bound,
        "reverse_positive_W_counts": dict(sorted(reverse.items())),
        "reverse_sign_cases": dict(sorted(signs.items())),
        "status": "all exact assertions passed"
    },ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()

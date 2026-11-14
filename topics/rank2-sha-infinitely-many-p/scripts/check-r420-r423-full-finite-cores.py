#!/usr/bin/env python3
"""Exact finite-center checks for R420/R423; no numerical theta evaluation."""

from collections import deque


def canonical(k, ell):
    k, ell = k % 8, ell % 8
    return min((k, ell), ((k + 4) % 8, (ell + 4) % 8))


POINTS = sorted(
    {
        canonical(k, ell)
        for k in range(8)
        for ell in range(8)
        if (k - ell) % 2 == 0
    }
)
INDEX = {point: index for index, point in enumerate(POINTS)}
IDENTITY = tuple((index, 0) for index in range(16))
NEGATIVE_IDENTITY = tuple((index, 8) for index in range(16))


def compose(left, right):
    """Permutation matrices with exact coefficients zeta_16**exponent."""
    return tuple(
        (left[index][0], (exponent + left[index][1]) % 16)
        for index, exponent in right
    )


def power(matrix, exponent):
    answer = IDENTITY
    for _ in range(exponent):
        answer = compose(matrix, answer)
    return answer


def translation(first, second):
    """Canonical two-factor T_(s+r*omega)/8, at levels 136 and 152."""
    ss, rr = first
    tt, uu = second
    answer = []
    for k, ell in POINTS:
        exponent = (
            17 * ss * rr
            + 34 * ss * k
            + 19 * tt * uu
            + 38 * tt * ell
        ) % 16
        answer.append((INDEX[canonical(k + rr, ell + uu)], exponent))
    return tuple(answer)


def u_translation(r, ss):
    return translation((ss, r), (ss, r))


def v_translation(r, ss):
    return translation((-ss, -r), (ss, r))


def build_a():
    answer = []
    for k, ell in POINTS:
        hh = ((k + 3 * ell) // 2) % 4
        rr = (-hh if hh % 2 else 2 - hh) % 4
        answer.append(
            (INDEX[canonical(k + rr, ell + rr)], 0 if hh % 2 else 8)
        )
    return tuple(answer)


A = build_a()
B = tuple(
    (INDEX[canonical(3 * k + 4, ell)], (8 * k) % 16)
    for k, ell in POINTS
)
R = tuple((INDEX[canonical(-k, ell)], 0) for k, ell in POINTS)
GLOBAL_REFLECTION = tuple(
    (INDEX[canonical(-k, -ell)], 0) for k, ell in POINTS
)

assert power(A, 2) == power(B, 2) == power(R, 2) == IDENTITY
assert power(compose(A, B), 3) == NEGATIVE_IDENTITY
assert compose(B, R) == compose(R, B)
assert power(compose(A, R), 3) == tuple(
    (index, (exponent + 8) % 16) for index, exponent in GLOBAL_REFLECTION
)

# Both sides retain full central phases, not only their torsion-point labels.
for rr in range(4):
    for ss in range(4):
        assert compose(compose(A, u_translation(rr, ss)), A) == u_translation(
            3 * rr, 3 * ss
        )
        actual_image = translation(
            (4 * ss - 4 * rr, 4 * ss),
            (6 * ss - 4 * rr, 4 * ss + 2 * rr),
        )
        assert compose(compose(A, v_translation(rr, ss)), A) == actual_image


def single_translation(vector, ss, rr, odd_level):
    return {
        (index + rr) % 8: (
            exponent + odd_level * ss * rr + 2 * odd_level * ss * index
        )
        % 16
        for index, exponent in vector.items()
    }


# The central correction epsilon is + on E[2], - on E[4] \ E[2].
for odd_level in (17, 19):
    for vector in ({0: 0, 4: 0}, {2: 0, 6: 0}):
        for rr in range(4):
            for ss in range(4):
                actual = single_translation(
                    vector, 11 * ss - 8 * rr, 8 * ss + 3 * rr, odd_level
                )
                reflected = single_translation(vector, -ss, -rr, odd_level)
                correction = 0 if rr % 2 == ss % 2 == 0 else 8
                assert actual == {
                    index: (exponent + correction) % 16
                    for index, exponent in reflected.items()
                }


def finite_group(generators, identity, multiplication):
    found = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            result = multiplication(generator, current)
            if result not in found:
                found.add(result)
                queue.append(result)
    return found


assert len(finite_group((A, B, R), IDENTITY, compose)) == 96


def multiply_four(left, right):
    return tuple(
        sum(left[4 * row + kk] * right[4 * kk + col] for kk in range(4))
        for row in range(4)
        for col in range(4)
    )


I4 = tuple(int(row == col) for row in range(4) for col in range(4))
A4 = (
    0, 1, 0, 0,
    1, 0, 0, 0,
    0, 0, -1, 0,
    0, 0, 0, -1,
)
B4 = (
    1, 0, 0, 0,
    0, 0, 1, 0,
    0, 1, 0, 0,
    0, 0, 0, 1,
)
R4 = (
    1, 0, 0, 0,
    0, 0, -1, 0,
    0, -1, 0, 0,
    0, 1, 1, 1,
)
GROUP4 = finite_group((A4, B4, R4), I4, multiply_four)
assert len(GROUP4) == 48
ORBIT4 = {tuple(matrix[4 * row] for row in range(4)) for matrix in GROUP4}
POSITIVE_REPRESENTATIVES = {
    (1, 0, 0, 0),
    (1, 0, 0, 1),
    (0, 1, 0, 0),
    (0, 1, 0, -1),
    (0, 0, 1, 0),
    (0, 0, 1, -1),
}
assert ORBIT4 == POSITIVE_REPRESENTATIVES | {
    tuple(-entry for entry in point) for point in POSITIVE_REPRESENTATIVES
}

print("R420: all canonical lift, epsilon, covariance and cubic identities passed.")
print("R423: full binary group 96; actual four-source image 48; source orbit 12.")

#!/usr/bin/env python3
"""Exact polynomial check of R59, modulo c^2+s^2=1.

The derivative rules are the moving-frame identities obtained directly from
X_theta=a' T+a T_r. All arithmetic is symbolic over the rational numbers.
This is an independent algebra check, not a numerical or analytic estimate.
"""
import sympy as S


def main():
    a, ap, c, s, h, v, z, P, P1, P2, u, u1, u2, p, p1, p2, q, q1, q2 = S.symbols(
        'a ap c s h v z P P1 P2 u u1 u2 p p1 p2 q q1 q2')
    Q, R = c*z-s*h, c*h+s*z
    rules = {a: 0, ap: 0, c: -s*u, s: c*u, h: ap*c-a*q*s+P*v,
             v: a*p*c-P*h, z: ap*s+a*q*c, P: P1, P1: P2,
             u: u1, u1: u2, p: p1, p1: p2, q: q1, q1: q2}

    def dt(value):
        return S.expand(sum(S.diff(value, key)*derivative for key, derivative in rules.items()))

    def reduce(value):
        return S.rem(S.Poly(S.expand(value), c), S.Poly(c*c+s*s-1, c)).as_expr().expand()

    T, X = S.Matrix([c, 0, s]), S.Matrix([h, v, z])
    Tt, Tr = S.Matrix([-s*u, P*c, c*u]), S.Matrix([-s*q, p*c, c*q])
    D, M = P*c*Q-u*v, p*c*Q-q*v
    A, B, C = P1*c-2*P*u*s, P*q-u*p, P*P*c*s+u1
    AM, CM = p1*c-(p*u+q*P)*s, p*P*c*s+q1
    Q1, R1 = a*q-P*s*v-u*R, ap+P*c*v+u*Q
    v1, h1 = a*p*c-P*h, ap*c-a*q*s+P*v
    A1 = P2*c-3*P1*u*s-2*P*u1*s-2*P*u*u*c
    B1 = P1*q+P*q1-u1*p-u*p1
    C1 = 2*P*P1*c*s+P*P*(c*c-s*s)*u+u2
    AM1 = p2*c-(2*p1*u+p*u1+q1*P+q*P1)*s-(p*u+q*P)*u*c
    CM1 = (p1*P+p*P1)*c*s+p*P*(c*c-s*s)*u+q2
    Q2 = a*q1-(P1*s+P*u*c)*v-P*s*v1-u1*R-u*R1
    v2 = a*(p1*c-p*u*s)-P1*h-P*h1
    checks = {
        'n': T.cross(X).dot(Tt)+D,
        'm': T.cross(X).dot(Tr)+M,
        'G': T.cross(X).dot(T.cross(X))-(Q*Q+v*v),
        'Qtheta': dt(Q)-Q1,
        'Rtheta': dt(R)-R1,
        'Dtheta': dt(D)-(A*Q+a*c*B-C*v),
        'Dtheta2': dt(dt(D))-(A1*Q+A*Q1+a*(-s*u*B+c*B1)-C1*v-C*v1),
        'Mtheta': dt(M)-(AM*Q+c*B*R-CM*v),
        'Mtheta2': dt(dt(M))-(AM1*Q+AM*Q1+(-s*u*B+c*B1)*R
                             +c*B*R1-CM1*v-CM*v1),
        'Gtheta': dt(Q*Q+v*v)-2*(a*(q*Q+p*c*v)-R*(u*Q+P*c*v)),
        'Gtheta2': dt(dt(Q*Q+v*v))-2*(Q1*Q1+Q*Q2+v1*v1+v*v2),
    }
    for name, value in checks.items():
        remainder = reduce(value)
        print(name, str(remainder), flush=True)
        if remainder != 0:
            raise SystemExit('nonzero exact polynomial remainder: '+name)


if __name__ == '__main__':
    main()

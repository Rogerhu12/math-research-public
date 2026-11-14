#!/usr/bin/env python3
"""Check R438 in the original model and its specified Hensel coordinate family.

The Hensel substitution is a conditional finite model, not another arithmetic
source.  No finite check is used as a cross-prime nonvanishing argument.
"""
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent


def import_script(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


r425 = import_script("r425", "check-r425-complete-central-four-row.py")
r428 = import_script("r428", "explore-rank2-central-hensel-schur.py")


def run():
    p, s = 101, 17
    G = r425.series(p, 1, 3*s+1)
    m, a = G.mod, G.ap
    alpha = 36*pow(17, -1, m) % m
    theta = G.exp(G.scale(G.add(G.log(G.g), G.scale(G.log(G.d), -1)), pow(17, -1, m)))
    X = G.one[:]
    X[1] = -pow(7, -1, m) % m
    for n in range(2, G.L):
        X[n] = sum(X[i]*X[n-i] for i in range(1, n))*pow((6*n+1)*(n-1), -1, m) % m
    tm = G.add(G.one, G.scale(G.t, -1))
    v1 = G.add(G.one, G.scale(G.t, -4))
    v2 = G.add(G.add(G.one, G.scale(G.t, -20)), G.scale(G.mul(G.t, G.t), -8))
    v3 = G.add(G.add(G.add(G.one, G.scale(G.t, 96)), G.scale(G.power(G.t, 2), 48)), G.scale(G.power(G.t, 3), -64))
    pg = G.add(G.add(G.add(G.one, G.scale(G.t, 30)), G.scale(G.power(G.t, 2), -144)), G.scale(G.power(G.t, 3), 32))
    assert G.add(G.mul(v1, v3), G.scale(G.mul(G.d, pg), -1)) == G.scale(G.mul(G.t, G.power(v1, 2)), 54)

    def sources(th):
        aa = G.mul(G.mul(G.mul(G.power(th, 8), G.power(X, -1)), tm), G.d)
        ff = G.scale(G.mul(G.mul(G.power(th, 9), G.power(X, -2)), G.h), pow(7, -1, m))
        gg = G.mul(G.power(th, 9), pg)
        cc = G.mul(aa, gg)
        ss = [0]+G.mul(aa, ff)[:-1]
        ee = G.mul(G.mul(G.power(th, 10), G.d), v2)
        ll = G.mul(G.mul(G.mul(G.power(th, 19), v1), v2), v3)
        bb, dd = G.mul(ee, gg), G.mul(ee, ff)
        nn = G.mul(G.mul(G.mul(G.power(th, 19), G.t), v2), G.power(v1, 2))
        tt = G.mul(ss, ll)
        assert G.mul(ss, gg) == [0]+G.mul(cc, ff)[:-1]
        assert ll == G.add(bb, G.scale(nn, 54))
        assert tt == G.add([0]+G.mul(cc, dd)[:-1], G.scale(G.mul(ss, nn), 54))
        return {"S": ss, "G": gg, "C": cc, "F": ff, "L": ll, "T": tt}

    def central(series, charge):
        return (charge*charge*series[s]-p*charge*series[2*s]+2*p*p*series[3*s]) % m

    def cross(ss, hh, k):
        return sum(ss[h*s+i]*hh[(k-h)*s-i]
                   for h in range(k) for i in range(1, s)) % m

    def check_rows(data, conditional=False):
        ss, gg, cc, ff, ll, tt = [data[key] for key in ("S", "G", "C", "F", "L", "T")]
        z = []
        for k in (1, 2, 3):
            other = sum(cc[h*s+i]*ff[(k-h-1)*s+s-1-i]
                        for h in range(k) for i in range(s)) % m
            zk = (other-cross(ss, gg, k)) % m
            assert zk == sum(ss[h*s]*gg[(k-h)*s] for h in range(1, k+1)) % m
            z.append(zk)
        cs, ct = central(ss, a), central(tt, alpha*a)
        predicted = ((a*a+p*a*gg[s]+2*p*p*(gg[s]*gg[s]-gg[2*s]))*z[0]
                     +(-p*a-2*p*p*gg[s])*z[1]+2*p*p*z[2]) % m
        assert cs == predicted
        u = [cross(ss, ll, k) for k in (1, 2, 3)]
        assert tt[s] == (ss[s]+u[0]) % m
        assert tt[2*s] == (ss[2*s]+ss[s]*ll[s]+u[1]) % m
        assert tt[3*s] == (ss[3*s]+ss[2*s]*ll[s]+ss[s]*ll[2*s]+u[2]) % m
        difference = (alpha*alpha*a*a*u[0]-p*alpha*a*u[1]+2*p*p*u[2]
                      +p*a*alpha*(alpha-1)*ss[2*s]+2*p*p*(1-alpha*alpha)*ss[3*s]
                      -p*alpha*a*ss[s]*ll[s]+2*p*p*(ss[2*s]*ll[s]+ss[s]*ll[2*s])) % m
        assert difference == (ct-alpha*alpha*cs) % m
        if conditional:
            assert cs == ct == 0
            assert u[0] % p == 0
            unit = (a*alpha*(alpha-1)+p*(2-alpha)*ll[s]) % (p*p)
            assert unit % p
            numerator = (alpha*alpha*a*a*(u[0]//p)-alpha*a*u[1]+2*p*u[2]
                         +2*p*(1-alpha*alpha)*ss[3*s]) % (p*p)
            assert ss[2*s] % (p*p) == -numerator*pow(unit, -1, p*p) % (p*p)
            assert ss[s] == (p*pow(a, -1, m)*ss[2*s]-2*p*p*pow(a*a, -1, m)*ss[3*s]) % m
        return {"S_three_weight_value_mod_p3": cs,
                "T_three_weight_value_mod_p3": ct,
                "all_cross_carries_checked": True,
                "conditional_model": conditional}

    base = sources(theta)
    assert base["T"] == G.Treg
    pair, _, _ = r428.central_solution(p)
    h = G.zero[:]
    h[s-2], h[s-1] = pair
    theta_changed = G.mul(theta, G.exp(G.scale(h, pow(17, -1, m))))
    changed = sources(theta_changed)
    assert changed["S"] == G.mul(base["S"], G.exp(h))
    assert changed["T"] == G.mul(base["T"], G.exp(G.scale(h, alpha)))
    return {"p": p, "regularized_coefficients_through": 3*s,
            "original_actual_source": check_rows(base),
            "unique_hensel_coordinate_family": check_rows(changed, True),
            "conditional_family_asserted_arithmetic": False,
            "cross_prime_nonvanishing_claim": False}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))

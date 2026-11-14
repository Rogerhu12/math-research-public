#!/usr/bin/env python3
"""Exact auxiliary checks for an audit of the current infinite-tail gap.

This does not prove an infinite nonlinear extension of a checkpoint. It
checks source-parameter compatibility, a 3Z ideal spectrum, and the cost of
the published R46 sufficient constants using exact rational arithmetic.
"""
import argparse
import gzip
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def rep(x):
    x = F(x)
    return {"numerator": str(x.numerator), "denominator": str(x.denominator),
            "display": float(x)}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("checkpoint", type=Path)
    ap.add_argument("source_root", type=Path)
    ap.add_argument("output", type=Path)
    a = ap.parse_args()
    if a.output.exists():
        raise SystemExit("Refusing to overwrite an earlier audit")
    rec = json.loads(gzip.decompress(a.checkpoint.read_bytes()))
    p = rec["response"]["checkpoint"]["parameters"]
    d, c, wc, lam = [F.from_float(float(p[k])) for k in
                     ["delta0", "etaRatioAtN0", "wCut", "rCuff"]]
    assert d == F(3458764513820541, 576460752303423488)
    assert c == F(3602879701896397, 72057594037927936)
    assert wc == F(1, 2)
    invariant = c*c/d
    assert F(2, 5) < invariant < F(1, 2)
    assert invariant != F(1, 32)
    # q=2^(-3/2)<3/8 and 1/sqrt(12)<3/10. Thus the
    # exact unit-cuff epsilon has an entirely rational majorant.
    assert F(3, 8)**2 > F(1, 8)
    assert F(3, 10)**2 > F(1, 12)
    Y_upper = 6*d + F(48, 5)*d*c
    exponent_upper = F(21, 10)*Y_upper
    assert exponent_upper < F(1, 11)
    # exp(t)<1/(1-t)<11/10, then compare fourth powers.
    assert (wc*F(11, 10))**4 < (2**17)**4 * (2*d)**11
    # beta=2^(1/4) enclosed by rational values; all comparisons below
    # use rational powers, never rounded eigenvalues or logarithms.
    beta_lo, beta_hi = F(118920711500, 10**11), F(118920711501, 10**11)
    assert beta_lo**4 < 2 < beta_hi**4
    # The raw large-root magnitude L obeys 64*nu <= L <
    # (65+65/384)*nu because d_a=2^(-11/4)<1/6.
    assert F(1, 6)**4 > F(1, 2**11)
    upper_factor = F(65) + F(65, 384)
    rows = []
    for j in range(1, 32):
        m = 3*j
        nu = F(m*m*(m*m-1), 12)
        lower = F(64)*nu/(32*beta_hi**m)
        assert lower > F(219, 200)
        rows.append({"j": j, "m": m, "large_root_weighted_lower": rep(lower)})
    m = 96
    nu = F(m*m*(m*m-1), 12)
    upper96 = upper_factor*nu/(32*beta_lo**m)
    assert upper96 < F(7, 8)
    # For m>=96, nu(m+3)/nu(m)<((m+3)/(m-1))^4 and
    # 2^(-3/4)<2/3. The displayed upper envelope decreases forever.
    assert F(3, 2)**4 < 8
    tail_ratio = F(99, 95)**4*F(2, 3)
    assert tail_ratio < 1
    small_upper = F(1, 32*64*6)
    assert small_upper < F(1, 2048)
    # R46 uses C_E=D_(2 J0), J0=16384. Since
    # D_m >= 27 B_m exp(36 B_m), B_m=80(1+m)^4, its condition
    # C_G C_E sqrt(d 2^-N)<=1/4 forces
    # N log 2 > 72 B_m - 6. With log 2<7/10 this gives the
    # following lower bound for N satisfying those particular criteria.
    J0 = 2**14
    B = 80*(1+2*J0)**4
    N_forced_lower = F(10, 7)*(72*B-6)
    assert N_forced_lower > 9*10**21
    # At n=160, the specified M(delta) is already >10016*128,
    # while d>2^-8 implies delta^(-1/16)<2^11. Hence the local
    # proof's low-window condition fails at that index.
    assert d > F(1, 2**8)
    assert 10016*128 > 2**11
    source = a.source_root/"topics/large-amplitude-twist-flex/results"
    refs = [source/n for n in [
        "R20-mild-r64-c2-single-tail.md",
        "R42-r20-47-parameter-analytic-tail.md",
        "R44-current-deep-tail-material-identity.md",
        "R46-actual-r64-47-parameter-deep-tail.md"]]
    out = {
        "scope": "Exact auxiliary arithmetic for a gap audit. The 3Z result here is only the ideal spectral split; no actual infinite nonlinear checkpoint extension, practical starting index, or arbitrary Dirichlet map is established.",
        "status": "PASS auxiliary checks",
        "source_sha256": {str(f.resolve()): sha(f) for f in
                          [Path(__file__), a.checkpoint]+refs},
        "source": {"delta0": rep(d), "etaRatioAtN0": rep(c),
                   "rCuff": rep(lam), "wCut": rep(wc),
                   "width_invariant": rep(invariant),
                   "unit_cuff_epsilon_strict_upper": 2**17,
                   "Y0_upper": rep(Y_upper),
                   "exponential_argument_upper": rep(exponent_upper)},
        "ideal_3Z": {"unstable_physical_modes": list(range(3, 94, 3)),
                     "count": 31, "unstable_lower_checks": rows,
                     "m96_large_root_upper": rep(upper96),
                     "subsequent_upper_ratio": rep(tail_ratio),
                     "all_small_roots_upper": rep(small_upper)},
        "published_R46_cost": {"J0": J0, "B_2J0": str(B),
                               "N_forced_strict_lower": rep(N_forced_lower),
                               "meaning": "Only a lower bound on N that satisfies R46's displayed sufficient constants; not a lower bound for any true solution or for an improved proof.",
                               "specified_local_M_window_fails_at_n160": True},
    }
    a.output.write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps({"status": out["status"], "3Z_unstable": 31,
                      "epsilon_upper": 2**17,
                      "R46_sufficient_N_must_exceed": float(N_forced_lower)}))


if __name__ == "__main__":
    main()

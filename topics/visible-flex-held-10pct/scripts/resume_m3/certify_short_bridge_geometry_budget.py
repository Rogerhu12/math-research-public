#!/usr/bin/env python3
"""Strict scalar geometry budget for the exact ShortBridge reference.

This builds an exact auxiliary rotational surface, with true trigonometric
integrals. It does not modify the actual target metric and does not read a
nonrotating field. The future difference V must use the same reference
coordinates (an endpoint-preserving reparametrization may be used).
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse
import hashlib
import json
import mpmath as mp

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--first-panels", type=int, default=512)
p.add_argument("--last-panels", type=int, default=128)
p.add_argument("--port", type=Path, required=True)
p.add_argument("--out", type=Path, required=True)
args = p.parse_args()
if min(args.first_panels, args.last_panels) < 1:
    raise ValueError("Positive panel counts required")
mp.mp.dps = 100
mp.iv.dps = 75
iv = mp.iv

def q(n, d=1):
    return iv.mpf(n) / d

def lo(x):
    return mp.make_mpf(x._mpi_[0])

def hi(x):
    return mp.make_mpf(x._mpi_[1])

def span(a, b):
    if a > b:
        raise ArithmeticError("empty interval")
    return iv.mpf([a, b])

def exact_mpf(x):
    sign, mantissa, exponent, _ = x._mpf_
    value = Q((-1 if sign else 1) * mantissa)
    return value * (2 ** exponent) if exponent >= 0 else value / (2 ** (-exponent))

def bounds(x):
    return {"lower_exact": str(exact_mpf(lo(x))),
            "upper_exact": str(exact_mpf(hi(x))),
            "lower_display": float(lo(x)), "upper_display": float(hi(x))}

def exact_value(x):
    return {"exact": str(exact_mpf(x)), "display": float(x)}

port_bytes = args.port.read_bytes()
if len(port_bytes) > 100000:
    raise ValueError("Port metadata exceeds the declared small-input limit")
port = json.loads(port_bytes)
cut = port["cut"]
R_exact = Q.from_float(float(cut["radius"]))
w_exact = Q.from_float(float(cut["backgroundSlope"]))
wr_exact = Q.from_float(float(cut["backgroundSecond"]))
if not (Q(299, 1000) < R_exact < Q(301, 1000)
        and Q(799, 10000) < w_exact < Q(801, 10000)
        and Q(-1868, 1000) < wr_exact < Q(-1865, 1000)):
    raise ValueError("This certificate is for the current small-cut bridge")
w = q(w_exact.numerator, w_exact.denominator)
wr = q(wr_exact.numerator, wr_exact.denominator)
R = q(R_exact.numerator, R_exact.denominator)
pt = iv.atan2(q(1), w)
peak = pt + (iv.pi / 2 - pt) / 5
epsilon = peak - pt
ps = wr / ((1 + w*w) * iv.sqrt(1 + w*w))
L1 = q(3, 8) * peak
L3 = 2 * epsilon / (-ps)
z0lo, z0hi = q(7, 20), q(51, 100)

def make_piece(kind, panels):
    rows = []
    sin_sum, cos_sum = q(0), q(0)
    dt = q(1, panels)
    for j in range(panels):
        t0, t1 = q(j, panels), q(j+1, panels)
        if kind == 0:
            left = peak * (3*t0*t0 - 2*t0*t0*t0)
            right = peak * (3*t1*t1 - 2*t1*t1*t1)
            phi = span(lo(left), hi(right))
        else:
            left, right = peak-epsilon*t0*t0, peak-epsilon*t1*t1
            phi = span(lo(right), hi(left))
        ss, cc = iv.sin(phi), iv.cos(phi)
        if lo(ss) < 0 or lo(cc) <= 0:
            raise ArithmeticError("Reference turning leaves its declared quadrant")
        rows.append((phi, ss, cc, dt))
        sin_sum += dt*ss
        cos_sum += dt*cc
    return rows, sin_sum, cos_sum

first, S1, C1 = make_piece(0, args.first_panels)
last, S3, C3 = make_piece(2, args.last_panels)
radial1, radial3 = L1*S1, L3*S3
height1, height3 = L1*C1, L3*C3
L2 = (1-R-radial1-radial3)/iv.sin(peak)
if lo(L2) <= 0:
    raise ArithmeticError("No certified positive bridge plateau")
if hi(-ps) >= 2:
    raise ArithmeticError("Terminal meridian curvature bound failed")
a1, h1 = 1-radial1, height1
a2 = a1-L2*iv.sin(peak)
h2 = h1+L2*iv.cos(peak)
total_height = h2+height3
total_length = L1+L2+L3

max_norm2 = mp.mpf(0)
min_support = mp.inf
piece_summary = []

def record_box(name, a, h, phi):
    global max_norm2, min_support
    # The exactly normalized reference decreases from 1 to R.
    a = span(max(lo(a), lo(R)), min(hi(a), mp.mpf(1)))
    n2 = a*a+(z0hi+h)*(z0hi+h)
    support = a*iv.cos(phi)+(z0lo+h)*iv.sin(phi)
    max_norm2 = max(max_norm2, hi(n2))
    min_support = min(min_support, lo(support))
    return hi(n2), lo(support)

def curve_piece(name, rows, length, a_start, h_start):
    acc_s, acc_c = q(0), q(0)
    pmax, pmin = mp.mpf(0), mp.inf
    for phi, ss, cc, dt in rows:
        ds, dc = length*dt*ss, length*dt*cc
        a = span(lo(a_start-acc_s-ds), hi(a_start-acc_s))
        h = span(lo(h_start+acc_c), hi(h_start+acc_c+dc))
        n2, supp = record_box(name, a, h, phi)
        pmax, pmin = max(pmax, n2), min(pmin, supp)
        acc_s += ds
        acc_c += dc
    piece_summary.append({"piece": name, "boxes": len(rows),
                          "norm_squared_upper": exact_value(pmax),
                          "support_lower": exact_value(pmin)})

curve_piece("initial cubic turn", first, L1, q(1), q(0))

# The constant-angle meridian is a straight line: squared radius is convex,
# while its support is exactly constant, so its endpoints suffice.
plateau_n2 = max(hi(a1*a1+(z0hi+h1)**2),
                 hi(a2*a2+(z0hi+h2)**2))
plateau_support = lo(a1*iv.cos(peak)+(z0lo+h1)*iv.sin(peak))
max_norm2, min_support = max(max_norm2, plateau_n2), min(min_support, plateau_support)
piece_summary.append({"piece": "constant-angle plateau", "boxes": 1,
                      "norm_squared_upper": exact_value(plateau_n2),
                      "support_lower": exact_value(plateau_support)})
curve_piece("terminal quadratic turn", last, L3, a2, h2)

R0 = Q(121, 100)
sigma0 = Q(37, 50)
if exact_mpf(max_norm2) >= R0**2 or exact_mpf(min_support) <= sigma0:
    raise ArithmeticError("Requested strict reference envelope not paid")

# Exact rational perturbation allowance, independent of any field samples.
V0, eta1, eta2 = Q(13, 100), Q(3, 25), Q(11, 2)
gamma = Q(99, 70)*eta1 + eta1**2/2  # 99/70 > sqrt(2)
normal_change = 2*gamma/(1-gamma)
support = sigma0-R0*normal_change-V0
curvature = (Q(4001, 1000)+eta2)/(1-eta1)**2
assert support > Q(87, 1000)
assert curvature < Q(123, 10)
assert R0+V0 == Q(67, 50)
assert Q(11, 10)*Q(160219, 346275) < Q(51, 100)
assert exact_mpf(lo(total_height)) > Q(3801, 10000)
assert exact_mpf(hi(total_height)) < Q(3813, 10000)
cut_height = [Q(7, 20)+Q(3801, 10000)-V0,
              Q(51, 100)+Q(3813, 10000)+V0]
assert cut_height == [Q(6001, 10000), Q(10213, 10000)]

out = {
    "scope": __doc__,
    "status": "strict_reference_geometry_and_conditional_perturbation_bounds_passed",
    "nonrotating_field_audited": False,
    "reference_metric_used_only_for_geometry_norms": True,
    "input_port_sha256": hashlib.sha256(port_bytes).hexdigest(),
    "reference": {"r_cut": str(R_exact), "w_cut": str(w_exact),
                  "w_r_cut": str(wr_exact),
                  "turn_curvature": "4", "peak_fraction": "1/5",
                  "entry_height_interval": ["7/20", "51/100"],
                  "L1": bounds(L1), "L2": bounds(L2), "L3": bounds(L3),
                  "length": bounds(total_length), "height": bounds(total_height)},
    "precision": {"mpmath": mp.__version__, "iv_digits": 75,
                  "first_panels": args.first_panels, "last_panels": args.last_panels},
    "global_reference_norm_squared_upper": exact_value(max_norm2),
    "global_reference_support_lower": exact_value(min_support),
    "reference_safe_bounds": {"norm_strict_upper": str(R0),
                              "support_strict_lower": str(sigma0),
                              "principal_curvature_upper": "4"},
    "field_conditions": {"sup_V": str(V0), "eta1": str(eta1), "eta2": str(eta2)},
    "conditional_field_bounds": {
        "norm_strict_upper": str(R0+V0),
        "support_strict_lower": str(support),
        "principal_curvature_upper": str(curvature),
        "normal_change_upper": str(normal_change),
        "cut_height_strict_lower": str(cut_height[0]),
        "cut_height_strict_upper": str(cut_height[1])},
    "pieces": piece_summary,
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
args.out.parent.mkdir(parents=True, exist_ok=True)
args.out.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({k: out[k] for k in ("status", "global_reference_norm_squared_upper",
                                     "global_reference_support_lower",
                                     "reference_safe_bounds", "conditional_field_bounds",
                                     "nonrotating_field_audited", "source_sha256")}))


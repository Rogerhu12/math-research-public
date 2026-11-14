#!/usr/bin/env python3
"""R33 angular-domain budget for a fixed complete finite cut polynomial.

The H/P coefficients are selected from a saved stored-metric response and
regarded as exact dyadic reference data on the separately certified real
outer cut. This does not transport the saved trajectory to the real source.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb, ctx, fmpq
from closure_real_head_source_enclosure import ball_record


def q(x):
    x = x if isinstance(x, F) else F.from_float(x)
    return arb(fmpq(x.numerator, x.denominator))


def endpoint(x):
    return arb((int(x["mantissa"]), x["binary_exponent"]))


def enclosure(x):
    return endpoint(x["lower"]).union(endpoint(x["upper"]))


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw), hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--response", type=Path, required=True)
    parser.add_argument("--real-source", type=Path, required=True)
    parser.add_argument("--real-radius", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    data, response_hash = read(args.response)
    source, source_hash = read(args.real_source)
    radius, radius_hash = read(args.real_radius)
    jets = data["response"]["jets"]
    H, P = jets["height"], jets["slope"]
    if len(H) != len(P) or not H:
        raise ValueError("Complete nonmean H and P vectors are required")
    r = enclosure(radius["outer_radius"])
    w = enclosure(source["outer_cut"]["scalars"]["w"])
    if not (r > 0 and w > 0 and w < arb(1)/2):
        raise ValueError("R33 real-background domain fails")
    bases = [(1+2*(i+1))*(2*(i+1)*abs(q(h))/(r*w)+abs(q(p))/w)
             for i, (h, p) in enumerate(zip(H, P))]

    def contributions(tau):
        return [(q(tau)*2*(i+1)).exp()*a for i, a in enumerate(bases)]

    def norm(tau):
        return sum(contributions(tau), arb(0))

    rows = []
    for tau in map(F, ("0", "1/256", "1/128", "1/64", "1/32", "1/16", "1")):
        values = contributions(tau)
        value = sum(values, arb(0))
        rows.append(dict(tau=str(tau), relative_first_order_norm=ball_record(value),
            below_R33_working_radius=bool(value < arb(1)/64),
            below_holomorphic_mean_domain=bool(value < arb(1)/32),
            working_radius_margin=ball_record(arb(1)/64-value),
            contributions=[dict(mode=2*(i+1), value=ball_record(v)) for i, v in enumerate(values)]))

    brackets = []
    for target in (F(1,64), F(1,32)):
        lo, hi = F(0), F(1)
        if not (norm(lo) < q(target) and norm(hi) > q(target)):
            raise ValueError("The requested critical-width bracket is unavailable")
        for unused in range(64):
            mid = (lo+hi)/2
            value = norm(mid)
            if value < q(target):
                lo = mid
            elif value > q(target):
                hi = mid
            else:
                break
        assert norm(lo) < q(target) and norm(hi) > q(target)
        brackets.append(dict(target=str(target), exact_lower=str(lo), exact_upper=str(hi),
            decimal_lower=float(lo), decimal_upper=float(hi),
            lower_norm=ball_record(norm(lo)), upper_norm=ball_record(norm(hi)),
            justified_by="All nonnegative terms are strictly increasing in tau."))

    result = dict(
        status="Certified finite reference-cut strip domain; no real radial solution is asserted",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        precision_bits=ctx.prec,
        coefficient_definition="All saved binary64 H/P entries are fixed exact dyadic coefficients; none are dropped.",
        background_definition="The certified real R26 outer radius and w, separately from the saved stored-metric cut.",
        Fourier_definition="m=2,4,...; the sum of both complex-conjugate coefficients equals the absolute cosine/sine amplitude.",
        norm_formula="R_tau=sum_m (1+m)*exp(tau*m)*(m*abs(H_m)/(r*w)+abs(P_m)/w)",
        modes=list(range(2,2*len(H)+1,2)),
        real_radius=ball_record(r), real_slope=ball_record(w),
        rows=rows, critical_width_brackets=brackets,
        actual_real_head_closure_paid=False,
        complete_radial_domain_paid=False,
        exact_nonlinear_DN_on_real_source_paid=False,
        input_hashes={str(args.response):response_hash, str(args.real_source):source_hash,
                      str(args.real_radius):radius_hash},
        source_hashes={Path(__file__).name:hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                       "closure_real_head_source_enclosure.py":hashlib.sha256(Path(__file__).with_name("closure_real_head_source_enclosure.py").read_bytes()).hexdigest()},
        limits=[
            "Only one cut and one explicitly chosen finite reference polynomial are enclosed.",
            "The full mean is to be obtained from the R33 exact mean root; the saved mean is not imported.",
            "These source-coordinate fields are not Cartesian radial boundary traces.",
            "A radial approximate center and its complete Fourier residual are still needed for a strong full-head theorem.",
            "No high Fourier coefficient is discarded to improve the strip bound."])
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    selected = rows[3]
    print(json.dumps(dict(output=str(args.out), modes=len(H), tau=selected["tau"],
        relative_first_order_norm=selected["relative_first_order_norm"]["display"],
        working_radius_margin=selected["working_radius_margin"]["display"],
        actual_real_head_closure_paid=False)))


if __name__ == "__main__":
    main()

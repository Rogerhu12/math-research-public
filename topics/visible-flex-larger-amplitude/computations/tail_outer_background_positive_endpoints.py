#!/usr/bin/env python3
"""Positive-endpoint arithmetic adapter for the frozen outer-flow helper.

The actual first execution of tail_outer_background_column_flow.py stopped
when a wide symmetric product ball crossed zero despite positive factors.
This adapter computes the two monotone endpoint products separately.  It
changes no equation, source panel, Peano product gate, parameter, or column.
The original actually executed source and failure packet remain untouched.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from pathlib import Path
import json
import sys

from flint import arb
import tail_outer_background_column_flow as original


ORIGINAL_SHA = "5b548692afa79035e8ac612c8148de0f4ed2a22e9c40ee7592fa36913156193c"
STATS = dict(positive_integral_pairs=0, nonnegative_hull_fallbacks=0,
             separate_strict_positive_endpoints_checked=True)


def positive_hull(lower, upper):
    """Enclose [lower, upper] without a spurious negative lower endpoint.

    The separately computed true lower endpoint remains strictly positive.
    A nonnegative zero lower bound is permitted in the Peano enclosure: its
    mathematical hypotheses require a,b >= 0, not a positive stored radius.
    """
    lower, upper = lower.lower(), upper.upper()
    if not lower > 0 or not upper >= lower or not upper.is_finite():
        raise ArithmeticError("Separate positive integral endpoints failed")
    enclosure = lower.union(upper)
    if enclosure.lower() < 0:
        # Arb's radius uses a shorter positive mantissa than its midpoint.
        # An exact 24-bit dyadic midpoint/radius gives precisely [0,U].
        mantissa, exponent = map(int, upper.man_exp())
        shift = max(0, mantissa.bit_length()-24)
        if shift:
            mantissa = (mantissa+(1 << shift)-1) >> shift
            exponent += shift
        enclosure = arb((mantissa, exponent-1), (mantissa, exponent-1))
        STATS["nonnegative_hull_fallbacks"] += 1
    if (not enclosure.lower() >= 0 or not enclosure.contains(lower)
            or not enclosure.contains(upper)):
        raise ArithmeticError("The nonnegative integral enclosure is invalid")
    return enclosure


def positive_integrals(row, mode, rc, mu_star, sqrt12):
    r, w, width = (original.ball(row[key]) for key in ("radius", "w", "width"))
    if not all(x > 0 for x in (r, w, width, rc, mu_star, sqrt12)):
        raise ArithmeticError("A real positive panel factor is missing")
    u = mode*mode-4
    if u < 0:
        raise ValueError("The declared even modes begin at two")
    nu = arb(mode*mode*(mode*mode-1))/12
    rl, ru, wl, wu = r.lower(), r.upper(), w.lower(), w.upper()
    dl, du = width.lower(), width.upper()
    cl, cu = rc.lower(), rc.upper()
    ml, mu = mu_star.lower(), mu_star.upper()
    sl, su = sqrt12.lower(), sqrt12.upper()
    # These products bound exactly the SAME two positive dr-integrals:
    # A = sqrt12 mu* (rc/r)^(2u) r^-8 dr/w,
    # B = nu sqrt12/mu* (r/rc)^(2u) r^6 w dr.
    # Only their interval evaluation changes; the original source panels,
    # real positive width, and strict positivity are all retained.
    al = (sl*ml*(cl/ru)**(2*u)*ru**(-8)*dl/wu).lower()
    au = (su*mu*(cu/rl)**(2*u)*rl**(-8)*du/wl).upper()
    bl = (nu.lower()*sl/mu*(rl/cu)**(2*u)*rl**6*dl*wl).lower()
    bu = (nu.upper()*su/ml*(ru/cl)**(2*u)*ru**6*du*wu).upper()
    A, B = positive_hull(al, au), positive_hull(bl, bu)
    STATS["positive_integral_pairs"] += 1
    return A, B, r, w


def main():
    old_path = Path(original.__file__)
    if original.digest(old_path) != ORIGINAL_SHA:
        raise ValueError("The actually executed r1 source changed")
    own_path = Path(__file__)
    original.FROZEN[own_path.name] = original.digest(own_path)
    original.positive_integrals = positive_integrals
    try:
        original.main()
    finally:
        # This is an independent arithmetic provenance record.  Original
        # result/checkpoint packets are not edited after being produced.
        if "--out" in sys.argv:
            out = Path(sys.argv[sys.argv.index("--out")+1])
            audit = out.with_name(out.stem+"-positive-endpoints.json")
            if not audit.exists():
                audit.write_text(json.dumps(dict(
                    status="Arithmetic adapter accounting; consult the actual resource exit and flow packet",
                    original_source_sha256=ORIGINAL_SHA,
                    adapter_sha256=original.digest(own_path),
                    statistics=STATS,
                    mathematical_change=False,
                    statement="Same A/B dr-integrals, source panels and Peano gates; separate monotone endpoints with a nonnegative enclosing ball",
                    complete_outer_solution_claimed=False), indent=2)+"\n")


if __name__ == "__main__":
    main()

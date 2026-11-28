#!/usr/bin/env python3
"""Exact physical-knot Bernstein bounds for a complete polar correction W.

Saved binary64 knots/coefficients are interpreted as exact rationals. Exact
Boehm insertion, differentiation and convex hulls bound W through order 3
on every whole radial span and every real angle. This bounds W only: no
source-background, metric, total curvature or reach certificate is implied.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
import time

BITS = 96
SCALE = 1 << BITS


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def q(value):
    return Q.from_float(float(value))


def up(value):
    return Q(-((-value.numerator*SCALE)//value.denominator), SCALE)


def shown(value):
    value = up(value)
    return dict(exactUpper=str(value), display=float(value))


def extract(knots, coefficients, insert):
    channels = len(coefficients[0])
    zero = [Q(0)]*channels
    control = [zero.copy() for _ in range(3)]+coefficients+[zero.copy() for _ in range(3)]
    if len(control) != len(knots)-6:
        raise ValueError("Full actual zero-trace coefficient count changed")
    breaks = sorted(set(knots))
    if knots[:6] != [breaks[0]]*6 or knots[-6:] != [breaks[-1]]*6:
        raise ValueError("Complete physical clamped quintic spline required")
    for value in breaks[1:-1]:
        if knots.count(value) > 3:
            raise ValueError("Actual interior spline is not C2")
        for unused in range(5-knots.count(value)):
            knots, control = insert(knots, control, 5, value)
    if len(control) != 5*(len(breaks)-1)+1:
        raise ArithmeticError("Incomplete exact physical Bernstein extraction")
    return [(lo, hi, control[5*i:5*i+6]) for i,(lo,hi) in enumerate(zip(breaks[:-1], breaks[1:]))]


def derivatives(control, width):
    out = [control]
    for order in range(1, 4):
        previous = out[-1]
        degree = 6-order
        out.append([[degree*(b-a)/width for a,b in zip(left,right)]
            for left,right in zip(previous[:-1], previous[1:])])
    return out


def main():
    ap = argparse.ArgumentParser()
    for key in ("scripts", "state", "output"):
        ap.add_argument("--"+key, type=Path, required=True)
    args = ap.parse_args()
    start = time.monotonic()
    state = json.loads(args.state.read_text())
    model = state["modelDefinition"]
    if canonical(model) != state["modelDefinitionSHA256"]:
        raise ValueError("Actual model definition changed")
    basis = model["basis"]
    if (basis["degree"] != 5 or basis["dimension"] != 12789
            or basis["radialBasisCount"] != 87 or basis["angularChannels"] != 147
            or not basis.get("physicalKnotsAuthoritative") or not basis.get("allPeriodicCartesianComponents")):
        raise ValueError("Actual full polar Cartesian physical-knot basis required")
    channels = basis["channelOrder"]
    if len(channels) != 147 or any(c["kind"] not in ("sin", "cos") for c in channels):
        raise ValueError("Every original real Fourier channel required")
    if len(state["z"]) != 12789:
        raise ValueError("All stored coefficient directions are required")
    knots = list(map(q, basis["physicalKnots"]))
    coefficients = [list(map(q, state["z"][147*i:147*(i+1)])) for i in range(87)]
    helper = args.scripts/"6a65-m12-local-bernstein-angular-metric-budget.py"
    spec = importlib.util.spec_from_file_location("polar_exact_Boehm", helper)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    pieces = extract(knots, coefficients, module.insert_knot)
    orders = [(a,b) for a in range(4) for b in range(4-a)]
    global_values = {f"s{a}u{b}":Q(0) for a,b in orders}
    global_positions = {}
    previous = None
    rows = []
    exact_zero_endpoint_jets = True
    for index,(lo,hi,control) in enumerate(pieces):
        jets = derivatives(control, hi-lo)
        if previous is not None and any(previous[a][-1] != jets[a][0] for a in range(3)):
            raise ArithmeticError("Exact Cartesian coefficient field lost C2 at an internal knot")
        if index == 0:
            exact_zero_endpoint_jets &= all(value == 0 for a in range(3) for value in jets[a][0])
        if index == len(pieces)-1:
            exact_zero_endpoint_jets &= all(value == 0 for a in range(3) for value in jets[a][-1])
        row = dict(physicalSpanExact=[str(lo),str(hi)], physicalSpanDisplay=[float(lo),float(hi)],
            bounds={})
        for a,b in orders:
            # Each derivative of a real sine/cosine channel has absolute
            # value <= k^b. Bernstein weights are nonnegative and sum to 1.
            # Euclidean vector norm <= sum of all component term magnitudes.
            values = [sum((abs(value)*int(channel["frequency"])**b
                for value,channel in zip(control_row,channels)), Q(0)) for control_row in jets[a]]
            bound = max(values)
            name = f"s{a}u{b}"
            row["bounds"][name] = shown(bound)
            if bound > global_values[name]:
                global_values[name] = bound
                global_positions[name] = index
        rows.append(row)
        previous = jets
    if not exact_zero_endpoint_jets:
        raise ArithmeticError("Actual saved correction must retain both zero two-jets")
    out = dict(schema="2ecf-polar-actual-Cartesian-physical-Bernstein-correction-budget-v1",
        stateSHA256=sha(args.state), modelDefinitionSHA256=state["modelDefinitionSHA256"],
        sourceIdentity=model["sourceIdentity"], entrySHA256=sha(__file__),
        exactBoehmHelperSHA256=sha(helper), actualCoefficientCount=len(state["z"]),
        physicalKnotsInterpretedAsExactStoredDyadics=True,
        normalizedDisplayKnotsNotUsed=True, coefficientsInterpretedAsExactStoredDyadics=True,
        fullRadialSpans=len(pieces), allRealAnglesIncluded=True,
        allInternalKnotsC2CheckedByExactFractionEquality=True,
        bothEndpointZeroTwoJetsCheckedExactly=True,
        thirdDerivativesBoundedOnEachClosedOneSidedPiece=True,
        fullCorrectionVectorNormUpper={key:shown(value) for key,value in global_values.items()},
        maximizingSpanIndices=global_positions, spans=rows,
        sourceBackgroundNotIncluded=True, totalMetricNotCertified=True,
        totalCurvatureNotCertified=True, reachNotCertified=True,
        finiteSamplesUsedForBounds=False, seconds=time.monotonic()-start)
    if args.output.exists():
        raise FileExistsError("Fresh exact actual-field budget output required")
    args.output.write_text(json.dumps(out,separators=(",",":"),allow_nan=False)+"\n")
    print(json.dumps(dict(event="actual_exact_full_correction_budget", SHA256=sha(args.output),
        seconds=out["seconds"], maximum=out["fullCorrectionVectorNormUpper"])), flush=True)


if __name__ == "__main__":
    main()

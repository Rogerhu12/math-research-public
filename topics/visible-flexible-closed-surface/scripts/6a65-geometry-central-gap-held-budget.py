#!/usr/bin/env python3
"""Exact central-ellipse and conditional fixed-position held budgets.

The observation record is not an exact continuous geometric certificate.
No new gap field is generated or evaluated by this script.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path


def perimeter_over_pi(A, B, terms=32):
    if not A >= B > 0:
        raise ValueError("Positive ordered semi-axes required")
    h = ((A - B) / (A + B)) ** 2
    coefficient = F(1)
    power = F(1)
    total = F(1)
    for n in range(1, terms + 1):
        coefficient *= F(3 - 2 * n, 2 * n) ** 2
        power *= h
        total += coefficient * power
    next_coefficient = coefficient * F(1 - 2 * terms, 2 * (terms + 1)) ** 2
    tail = next_coefficient * power * h / (1 - h)
    return (A + B) * total, (A + B) * (total + tail)


P0 = perimeter_over_pi(F(7, 5), F(1, 2))


def central_box(gap, denominator=10**12):
    low = int(F(1, 5) * denominator)
    high = int(F(3, 5) * denominator)
    while high - low > 1:
        middle = (low + high) // 2
        B = F(middle, denominator)
        q = perimeter_over_pi(B + gap, B)
        if q[1] < P0[0]:
            low = middle
        elif q[0] > P0[1]:
            high = middle
        else:
            raise ArithmeticError("Increase exact series precision")
    B0, B1 = F(low, denominator), F(high, denominator)
    left = perimeter_over_pi(B0 + gap, B0)
    right = perimeter_over_pi(B1 + gap, B1)
    assert left[1] < P0[0] and right[0] > P0[1]
    return (B0 + gap, B1 + gap), (B0, B1)


def box_text(pair):
    return [str(x) for x in pair]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--recorded-input",
        action="store_true",
        help="Input is an explicitly reconstructed observation record, not the original baseline.",
    )
    ap.add_argument("input_json")
    ap.add_argument("output")
    args = ap.parse_args()
    start = time.time()
    outpath = Path(args.output)
    if outpath.exists():
        raise ValueError("Fresh budget output required")
    source = json.loads(Path(args.input_json).read_text())
    if args.recorded_input:
        if source.get("recordedNotOriginalBaseline") is not True:
            raise ValueError("Recorded mode requires an explicit reconstructed-record marker")
        input_identity = dict(
            inputKind="recorded-observation-summary",
            sourceBaselineSHA256=None,
            sourceObservationRecordSHA256=sha256(args.input_json),
            recordedOriginalBaselineSHA256=source["recordedOriginalBaselineSHA256"],
            recordedOriginalBaselinePath=source["recordedOriginalBaselinePath"],
            originalBaselineBytesAvailableToThisRun=False,
        )
    else:
        if source.get("recordedNotOriginalBaseline"):
            raise ValueError("Reconstructed observations require --recorded-input")
        input_identity = dict(
            inputKind="actual-baseline-report",
            sourceBaselineSHA256=sha256(args.input_json),
            sourceObservationRecordSHA256=None,
            recordedOriginalBaselineSHA256=None,
            originalBaselineBytesAvailableToThisRun=True,
        )
    geo = source["evaluation"]["geometry"]
    d0, W = F("0.6263963"), F("0.8283680")
    R, target, guide = F(".097"), F(".64"), F(".65")
    if F(str(geo["minHeldDistance"])) < d0 or F(str(geo["maxAbsoluteY"])) > W:
        raise ValueError("Declared rational bounds unsupported by supplied observations")
    Aold, Bold = central_box(F(1))
    rows, cases = [], {}
    for label in [
        "1", "1.04", "1.041", "1.05", "1.06", "1.067",
        "1.068", "1.072", "1.075", "1.089", "1.09",
    ]:
        gap = F(label)
        A, B = central_box(gap)
        delta = F(0) if gap == 1 else A[0] - Aold[1]
        kappa = (A[0] / B[1] ** 2, A[1] / B[0] ** 2)
        nmin = (B[0] / A[1] ** 2, B[1] / A[0] ** 2)
        held2 = d0 * d0 + 2 * delta * (Aold[0] - W) + delta * delta
        ball2 = A[1] * A[1] + F(13, 128) ** 2
        row = dict(
            gap=label,
            AInterval=box_text(A),
            BInterval=box_text(B),
            centralKappaInterval=box_text(kappa),
            centralMinimumCurvatureInterval=box_text(nmin),
            conditionalHeldSquaredLower=str(held2),
            centralBallSquaredUpper=str(ball2),
            held064MarginSquared=str(held2 - target * target),
            held065MarginSquared=str(held2 - guide * guide),
            trueCurvatureCapSatisfied=kappa[1] < 1 / R,
            curvatureGuide9p5Satisfied=kappa[1] < F(19, 2),
            centralBall1p6Satisfied=ball2 < F(64, 25),
            capCentralSupportSatisfied=A[0] > F(7, 5),
            display=dict(
                A=[float(x) for x in A],
                B=[float(x) for x in B],
                kappa=[float(x) for x in kappa],
                nmin=[float(x) for x in nmin],
                conditionalHeldLower=math.sqrt(float(held2)),
            ),
        )
        rows.append(row)
        cases[gap] = (A, B, kappa, held2)
    assert cases[F("1.041")][3] > target * target
    assert cases[F("1.089")][2][1] < 1 / R < cases[F("1.09")][2][0]
    assert cases[F("1.067")][2][1] < F(19, 2) < cases[F("1.068")][2][0]
    assert cases[F("1.072")][3] > guide * guide
    witness = geo["witnesses"]["held_plus"]["X"]
    wx, wy, wz = [F(str(x)) for x in witness]
    xbar, zbar, ylo = F(".0000611"), F(".137981"), F(".8250138")
    assert abs(wx) <= xbar and abs(wz) <= zbar and ylo <= wy <= Aold[0]
    Abar = cases[F("1.068")][0][1]
    witness065upper = xbar * xbar + (Abar - ylo) ** 2 + zbar * zbar
    assert witness065upper < guide * guide
    a0box = (P0[0] / 2, P0[1] / 2)
    A05, B05 = cases[F("1.05")][:2]
    n0box = (B05[0] / A05[1] ** 2, B05[1] / A05[0] ** 2)
    entry_budget = (
        a0box[0] ** 2 * n0box[0] ** 2,
        a0box[1] ** 2 * n0box[1] ** 2,
    )
    ramp_rows = []
    for v in [F(".05"), F(".045")]:
        L = F(".06")
        fp = v / 2
        fpp = v / L * F(630, 256)
        fmid = (
            a0box[0] + v * L * F(63, 1024),
            a0box[1] + v * L * F(63, 1024),
        )
        required_n = (R * fpp / fmid[1], R * fpp / fmid[0])
        ratio = (required_n[0] / n0box[1], required_n[1] / n0box[0])
        Jrequired = (
            (R * R * fpp * fpp + fp * fp - entry_budget[1]) / 2,
            (R * R * fpp * fpp + fp * fp - entry_budget[0]) / 2,
        )
        ramp_rows.append(
            dict(
                gap="21/20", slope=str(v), length=str(L),
                midpointRadiusInterval=box_text(fmid),
                midpointSlope=str(fp), midpointSecondDerivative=str(fpp),
                entryMinimumCurvatureInterval=box_text(n0box),
                requiredMidpointNormalCurvatureInterval=box_text(required_n),
                requiredToEntryRatioInterval=box_text(ratio),
                necessarySignedIntegralThresholdInterval=box_text(Jrequired),
                necessaryConditionOnlyTrueRampNotEvaluated=True,
                display=dict(
                    requiredNormalCurvature=[float(x) for x in required_n],
                    requiredToEntryRatio=[float(x) for x in ratio],
                    signedIntegralThreshold=[float(x) for x in Jrequired],
                ),
            )
        )
    v, Lr, Lc, Lright = F(".045"), F(".06"), F(".02"), F(".7956739498716915")
    fcoast = tuple(x + v * Lr / 2 + v * Lc for x in a0box)
    right_target = tuple((v - (F(".8") - x) / Lright) / (1 + v) for x in fcoast)
    I7 = F(46079328383180761, 155186468939000213)
    I8 = F(3008062272705324698929883, 10483830270076968893338822)
    beta = ((right_target[1] - I7) / (I8 - I7), (right_target[0] - I7) / (I8 - I7))
    assert 0 < beta[0] <= beta[1] < 1
    c = F(13, 128)
    report = dict(
        schema="6a65-exact-central-gap-and-existing-position-conditional-held-budget-v2",
        exactPerimeterDefinition="P(A,B)=P(7/5,1/2), A-B=gap",
        seriesTerms=32, normalizedPerimeterInterval=box_text(P0),
        a0Interval=box_text(a0box),
        originalCentralAInterval=box_text(Aold), originalCentralBInterval=box_text(Bold),
        fixedPositionAssumptions=dict(
            minimumBothHeldDistance=str(d0), maximumAbsY=str(W), positionsUnchanged=True
        ),
        exactShiftIdentity="d_new^2 >= d0^2+2*Delta*(A_old-W)+Delta^2",
        rows=rows,
        certifiedCentralAndConditionalHeld064GapInterval=["1041/1000", "1089/1000"],
        certifiedWithCentralGuide9p5GapInterval=["1041/1000", "1067/1000"],
        conditionalHeld065ExampleGap="134/125",
        unchangedWitnessObstructsHeld065UnderCentralGuide9p5=dict(
            witness=witness, rationalAbsXUpper=str(xbar),
            rationalAbsZUpper=str(zbar), rationalYLower=str(ylo),
            newCentralAUpper=str(Abar), distanceSquaredUpper=str(witness065upper),
            strictSquaredMargin=str(guide * guide - witness065upper),
            displayDistanceUpper=math.sqrt(float(witness065upper)),
        ),
        rampMidpointNecessaryConditions=ramp_rows,
        selectedCoupledCandidate=dict(
            gap="21/20", rampSlope=str(v), rampLength=str(Lr), coastLength=str(Lc),
            centralLength=str(c), rightLength=str(Lright),
            rightPower=7, rightBetaInterval=box_text(beta),
            rightTargetIntegralInterval=box_text(right_target), I7=str(I7), I8=str(I8),
            fCoastEndInterval=box_text(fcoast), fCut="4/5", fCuff="8/25",
            physicalCut=str(c + Lr + Lc + Lright),
            physicalFlatCuff=str(c + Lr + Lc + Lright + F(".48")),
            trueTailAmplitudeSourceValue=".8746432018013935",
            trueTailZ="51/100",
            status="single proposed new geometry input; no new field evaluated",
        ),
        actualNewGapFieldEvaluations=0,
        unchangedFinitePositionBoundsNotContinuousCertificate=True,
        wholeNewCoreMetricAndReachUnproved=True,
        rampCodazziAngularCouplingMustNotBeDiscarded=True,
        scriptSHA256=sha256(__file__),
        seconds=time.time() - start,
        **input_identity,
    )
    outpath.parent.mkdir(parents=True, exist_ok=True)
    outpath.write_text(json.dumps(report, indent=2) + "\n")
    print(
        json.dumps(
            dict(
                output=str(outpath), outputSHA256=sha256(outpath),
                scriptSHA256=report["scriptSHA256"], inputKind=report["inputKind"],
                rows=len(rows), exactAssertionsPassed=True,
                actualNewGapFieldEvaluations=0, seconds=report["seconds"],
            )
        )
    )


if __name__ == "__main__":
    main()

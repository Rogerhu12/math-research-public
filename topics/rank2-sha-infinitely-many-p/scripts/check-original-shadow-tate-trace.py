#!/usr/bin/env sage-python
"""Validate R883(G) against the independent full scalar-trace formula.
Fixed r=29,41 only; include all base ell-torsion, both auxiliary exceptions,
and genuine ell^2 points over residue degree ell.  This is an implementation
check, not an original-shadow calculation or an infinite-prime assertion.
All arithmetic runs only in the public repository Actions; summaries only.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in public repository Actions.")
import hashlib
import json
import time
from pathlib import Path
from sage.all import ZZ, GF, PolynomialRing, EllipticCurve, set_random_seed
from original_shadow_relative_six_tools import verified_torsion_basis
from original_shadow_tate_trace_tools import OriginalTateTraceReader

STARTED = time.monotonic()
def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def coords(P):
    if P.is_zero():
        return {"infinity": True}
    return {"x": [int(c) for c in P[0].polynomial().list()],
            "y": [int(c) for c in P[1].polynomial().list()]}
def progress(stage, **kwargs):
    print("RANK2_TATE_TRACE_CHECK_STAGE "+canonical(
        dict(stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kwargs)), flush=True)
def embed_point(P, target_curve, embedding):
    return target_curve(0) if P.is_zero() else target_curve(
        [embedding(P[0]), embedding(P[1])])

record_hash = hashlib.sha256()
case_summaries = []
for r in (29, 41):
    set_random_seed(883000+r)
    ell = (r+1)//6
    fp = GF(r)
    R = PolynomialRing(fp, "om")
    om = R.gen()
    k = GF(ZZ(r)**2, "omega", modulus=om**2+om+1)
    omega = k.gen()
    assert omega**2+omega+1 == 0
    torsion = verified_torsion_basis(k, omega, r)
    reader = OriginalTateTraceReader(torsion, r)
    E = torsion["curve"]
    progress("actual base pairing calibrated", prime=r, ell=ell,
             calibration=reader.calibration)

    def check_point(P, K, embedding, d, tag):
        point, audit = reader.six_trace(P, K, embedding, d)
        numerator = ZZ(1)-ZZ(-r)**d
        assert numerator % ell == 0
        scalar_point = (numerator//ell)*P
        assert ell*scalar_point == P.curve()(0)
        assert embed_point(point, P.curve(), embedding) == scalar_point
        record_hash.update(canonical(dict(
            prime=r, degree=d, tag=tag, input=coords(P),
            output=coords(point), scalar_trace=coords(scalar_point),
            audit=audit)).encode())
        record_hash.update(b"\n")
        return not point.is_zero()

    nonzero = 0
    for P in torsion["coordinates"]:
        nonzero += check_point(P, k, lambda c:k(c), 1, "all_base_ell_torsion")
    assert nonzero == ell**2-1
    # This includes O, -U, -2U for both choices of the Miller first variable.
    assert reader.second_auxiliary_choices > 0
    case_summaries.append(dict(
        prime=r, residue_degree=1, points=ell**2, nonzero_traces=nonzero,
        all_base_torsion_and_auxiliary_exception_points=True))
    progress("all actual base torsion agrees with full scalar trace",
             prime=r, count=ell**2, nonzero_traces=nonzero)

    for d in (2, ell):
        K = GF(ZZ(r)**(2*d), "residue")
        omega_image = K.multiplicative_generator()**((K.cardinality()-1)//3)
        assert omega_image != 1 and omega_image**2+omega_image+1 == 0
        embedding = k.hom([omega_image], K)
        assert embedding(omega) == omega_image
        EQ = EllipticCurve(K, [0, 0, 0, 0, 1])
        N = abs(ZZ(-r)**d-1)
        points = [EQ(0)]
        raw_points = []
        primitive = []
        primitive_cyclic = set()
        for n in range(512):
            # A fixed small list of finite-field points, never a target-prime scan.
            x = K.gen()+K(n % r)+K(n//r)*K.gen()**2
            y2 = x**3+1
            if not y2.is_square():
                continue
            P = EQ([x, y2.sqrt()])
            if len(raw_points) < 12:
                raw_points.append(P)
            if d == ell:
                assert N % (ell**2) == 0 and N % (ell**3) != 0
                Q = (N//(ell**2))*P
                if ell*Q != EQ(0):
                    assert ell**2*Q == EQ(0)
                    if not primitive:
                        primitive.append(Q)
                        primitive_cyclic = {j*(ell*Q) for j in range(ell)}
                    elif len(primitive) == 1 and ell*Q not in primitive_cyclic:
                        primitive.append(Q)
            if len(raw_points) == 12 and (d != ell or len(primitive) == 2):
                break
        assert len(raw_points) == 12
        points += raw_points
        points += [embed_point(P, EQ, embedding) for P in torsion["basis"]]
        if d == ell:
            assert len(primitive) == 2
            P0, P1 = primitive
            points += [P0, P1, -P0, -P1, P0+P1, P0-P1, 2*P0+P1]
            # Genuine ell^2 input with NONZERO full trace when ell divides d.
            for Q in primitive:
                assert ell*Q != EQ(0) and ell**2*Q == EQ(0)
                assert ((ZZ(1)-ZZ(-r)**d)//ell)*Q != EQ(0)
        nonzero = sum(check_point(P, K, embedding, d,
                                 "residue_degree_divisible_by_ell"
                                 if d == ell else "quadratic_residue_field")
                      for P in points)
        if d == ell:
            assert nonzero >= 2
            for P in torsion["basis"]:
                PP = embed_point(P, EQ, embedding)
                trace, _ = reader.six_trace(PP, K, embedding, d)
                assert trace.is_zero()
        case_summaries.append(dict(
            prime=r, residue_degree=d, points=len(points),
            nonzero_traces=nonzero, full_exponent_retained=True,
            genuine_independent_ell_squared_points=len(primitive),
            original_base_embedding=True))
        progress("full residue trace comparison complete",
                 **case_summaries[-1])
    assert reader.divisible_degree_calls > 0
    progress("one prime complete", prime=r, trace_reader=reader.summary())

root = Path(__file__).resolve().parent
names = ("check-original-shadow-tate-trace.py",
         "original_shadow_relative_six_tools.py",
         "original_shadow_tate_trace_tools.py")
result = dict(
    kind="rank2_original_tate_trace_implementation_check",
    status="complete_fixed_prime_scalar_comparison",
    source=os.environ.get("RANK2_SOURCE_SHA"),
    run=os.environ.get("RANK2_RUN_ID"),
    source_sha256={n:hashlib.sha256((root/n).read_bytes()).hexdigest()
                   for n in names},
    cases=case_summaries,
    complete_records_sha256=record_hash.hexdigest(),
    all_compared_points_equal_to_full_scalar_trace=True,
    degree_divisible_by_ell_and_nonzero_trace_tested=True,
    original_map_certificate_asserted=False,
    original_shadow_nonzero_asserted=False,
    elapsed_seconds=time.monotonic()-STARTED,
    readme_blobs={
        "README.md":os.environ.get("RANK2_ROOT_README_SHA"),
        "topic":os.environ.get("RANK2_TOPIC_README_SHA")})
payload = canonical(result)
print("RANK2_TATE_TRACE_CHECK_RESULT "+payload, flush=True)
print("RANK2_TATE_TRACE_CHECK_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)

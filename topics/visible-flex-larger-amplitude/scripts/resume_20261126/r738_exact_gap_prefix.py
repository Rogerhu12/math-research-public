#!/usr/bin/env python3
"""R738 equation (4) on the complete original 415-cell R690 Hermite input."""
import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, isqrt
import os
from pathlib import Path
import subprocess

import r734_exact_core_and_prefix as old


BITS = 112
DEN = 1 << BITS
BASE_DEPTH = 5
LAST_DEPTH = 29
MSTAR, MSTAR_UP = Q(1, 5), Q(7)
NOTE734 = "notes/r734-actual-Hermite-46139111288-1.json"
PROOF738 = "results/R738-noncooperative-actual-core-characteristic-gap-and-prefix.md"
SOURCE_PINS = {
    "results/R734-hyperbolic-core-continuation-computable-width-and-normal-balls.md":
        "be29f68feb15a8bbb6bc41c1990d224248a84092aa7bc9409d9127718296dd48",
    NOTE734: "0abf51d64551fe9deedb8da98806a0207c9ed2367375fa7e104e4d6deefc43b4",
    PROOF738: "2f050cc5947e8bf14a117365c51b89bcdbba9014dde11baaeaccb87422592d14",
    "scripts/resume_20261126/r734_exact_core_and_prefix.py":
        "3f053c7dcea8fe99e039b7069ec0991fb0e628e620ddf43be01756f12233db03",
}


def down(q):
    return Q((q.numerator * DEN) // q.denominator, DEN)


def up(q):
    return -down(-q)


def sqrt_down(q):
    return Q(isqrt((q.numerator * DEN * DEN) // q.denominator), DEN)


def words(values):
    return [str(t) for t in values]


def halves(b):
    lo, hi = [b[0]], [b[-1]]
    while len(b) > 1:
        b = [(x+y)/2 for x, y in zip(b, b[1:])]
        lo.append(b[0])
        hi.append(b[-1])
    return lo, list(reversed(hi))


def split(curves):
    pairs = [halves(b) for b in curves]
    return tuple(p[0] for p in pairs), tuple(p[1] for p in pairs)


def local_sign(b, strict, global_ok):
    if global_ok:
        return True
    if min(b) >= 0 and (not strict or min(b[0], b[-1]) > 0):
        return True
    if min(b[0], b[-1]) < 0 or (strict and min(b[0], b[-1]) == 0):
        return False
    # Express this same restricted Bernstein polynomial in the local power basis.
    n = len(b) - 1
    p = []
    for j in range(n + 1):
        p.append(comb(n, j)*b[0])
        b = [v-u for u, v in zip(b, b[1:])]
    return old.decide(old.trim(p), strict)["holds"]


def curves_and_signs(co, width):
    ap = old.scale(old.derivative(co), 1/width)
    app = old.scale(old.derivative(ap), 1/width)
    appp = old.scale(old.derivative(app), 1/width)
    prod = old.times(co, app)
    adverse_numerator = old.add(old.times(ap, app), old.scale(old.times(co, appp), -1))
    polys = (co, app, ap, prod, adverse_numerator)
    signs = [old.decide(p, strict) for p, strict in zip(polys, (True, True, False))]
    return tuple(old.bernstein(p) for p in polys), signs


def enclosure(curves, global_signs):
    a, app, ap, prod, adverse = curves
    checks = [local_sign(b, strict, ok) for b, strict, ok in
              zip(curves, (True, True, False), global_signs)]
    if not all(checks):
        return "scalar sign disproved on closed leaf", None, checks
    al, kl = min(a), min(app)
    if min(al, kl) <= 0:
        return "Bernstein denominator lower bound inconclusive", None, checks
    pl = max(min(prod), al * kl)
    d = sqrt_down(pl)
    if d <= 0:
        return "positive square root has zero dyadic lower bound", None, checks
    C, H = up(max(ap)/al), up(max(app)/al)
    E = up(max(Q(0), max(adverse))/(4*pl))
    return "bounds", (C, H, E, d, up(max(a))), checks


def trial(state, h, bounds):
    m, M, Y, T = state
    C, H, E, d, _ = bounds
    he1 = h*(C*(2+4*MSTAR_UP**2*H)+2*E)
    he2 = h*C*H*MSTAR_UP**2
    if max(he1, he2) >= 1:
        return "Gronwall denominator inconclusive", None
    y = up(Y/(1-he1))
    t = up((T+h*H*y)/(1-he2))
    v = up(h*E*t/d)
    next_state = (down(m-v), up(M+h*C*MSTAR_UP*(1+H*MSTAR_UP**2)+v), y, t)
    if next_state[0] <= MSTAR or next_state[1] >= MSTAR_UP:
        return "strict extrema margin inconclusive", next_state
    return "accepted", next_state


def previous_and_formula(topic, full, params, binding):
    for path, expected in SOURCE_PINS.items():
        if sha256((topic/path).read_bytes()).hexdigest() != expected:
            raise ValueError("source binding differs: "+path)
    report = json.loads((topic/NOTE734).read_bytes())
    if old.json_bytes(report["binding"]) != old.json_bytes(binding):
        raise ValueError("recovered original scalar binding differs from published R734 binding")
    w = full.x[1]-full.x[0]
    cs = full.coefficients[0]
    k0 = Q.from_float(float(params["geometry"]["initial_law"]["k0"]))
    if list(cs[:3]) != [1, 0, w*w*k0/2] or full.x[0] != 0:
        raise ValueError("actual origin jet differs")
    b3 = sum((j*(j-1)*(j-2)*abs(cs[j]) for j in range(3,6)), Q(0))/w**3
    tstar = min(w, Q(1,200), k0/(2*(1+b3)), 1/(25*(4+7*b3/(2*k0))))
    if (str(tstar) != report["core"]["Tstar"] or words(cs) != report["core"]["first_fullhold_coefficients"]
            or str(b3) != report["core"]["B3"]):
        raise ValueError("actual first width or original coefficients differ from published R734")
    tdag = min(w, Q(1,1000), k0/(2*(1+b3)))
    return report, {"w":str(w), "k0":str(k0), "B3":str(b3), "coefficients":words(cs),
            "Tstar":str(tstar), "Tdagger":str(tdag), "Tdagger_approx":float(tdag),
            "Tdagger_over_Tstar":str(tdag/tstar), "Tdagger_at_least_ten_Tstar":tdag>=10*tstar,
            "larger_formula_width":str(max(tdag,tstar))}


def value(p, t):
    v=Q(0)
    for c in reversed(p):
        v=v*t+c
    return v


def cooperative_restart(full, origins, previous):
    # Restart R734 (9) only from an actual (4) state at an original knot.
    # All exact whole signs are known from the full closed-piece computation.
    flags=previous["cell_status_columns"][:4]
    begin=next((i for i in range(1,len(origins))
                if origins[i] is not None and all(s[i]=="1" for s in flags)),None)
    if begin is None:
        return {"start":None,"reason":"no origin-reached positive cooperative original cell start"}
    start=full.x[begin]
    cs=full.coefficients[begin]
    w=full.x[begin+1]-start
    a0,ap0=cs[0],cs[1]/w
    m,M,Y,T=origins[begin]
    zlower=a0**2/m**2+ap0**2
    zupper=a0**2/M**2+ap0**2
    end=start
    lower2,upper2=m*m,M*M
    supK=Q(0)
    failure=None
    whole=begin
    for i in range(begin, len(full.coefficients)):
        co=full.coefficients[i]
        left,right=full.x[i:i+2]
        w=right-left
        polys=old.predicates(co,w)[:4]
        ap=polys[2]
        test=old.add([zupper],old.scale(old.times(ap,ap),-1))
        def signs(t):
            return [old.decide(old.restriction(p,t),strict)["holds"]
                    for p,strict in zip(polys+[test],(True,True,False,False,True))]
        # On the fully positive branch a' is nonnegative and strictly increasing.
        # An exact endpoint comparison decides its closed-cell upper denominator.
        mask=[s[i]=="1" for s in flags]
        den=(zupper-value(ap,Q(1))**2>0 if all(mask[:3]) else old.decide(test,True)["holds"])
        yes=mask+[den]
        take=Q(1)
        if not all(yes):
            lo,hi=Q(0),Q(1)
            at0=signs(lo)
            if all(at0):
                for _ in range(48):
                    mid=(lo+hi)/2
                    if all(signs(mid)):
                        lo=mid
                    else:
                        hi=mid
            else:
                hi=Q(0)
            take=lo
            failure={"piece_zero_based":i,"whole_conditions":yes,"lower":str(left+w*lo),
                     "upper":str(left+w*hi),"lower_conditions":signs(lo),"upper_conditions":signs(hi),
                     "bisections":48 if all(at0) else 0,
                     "order":["a>0","a_ss>0","a_s>=0","a*a_sss+3*a_s*a_ss>=0","Z_upper-a_s^2>0"]}
        if take>0:
            ar,apr=value(co,take),value(ap,take)
            end=left+w*take
            lower2=ar**2/(zlower-apr**2)
            upper2=ar**2/(zupper-apr**2)
            # Along this entire connected branch a>=a0 since a'>=0.
            H=up(max(old.bernstein(old.restriction(polys[1],take)))/a0)
            supK=max(supK,H)
        if failure is not None:
            break
        whole=i+1
    # Both equal-state comparison functions are nondecreasing on this branch.
    return {"start_piece_zero_based":begin,"start":str(start),"origin_m_M_Y_T":words((m,M,Y,T)),
        "initial_a_ap":words((a0,ap0)),"Z_lower":str(zlower),"Z_upper":str(zupper),
        "end":str(end),"end_approx":float(end),"whole_original_pieces_including_origin":whole,
        "lower_field_bound_squared_at_end":str(lower2),"upper_field_bound_squared_at_end":str(upper2),
        "global_K_upper_on_restart_branch":str(supK),
        "II_operator_bound_squared_on_restart_branch":str(max(1/m**2,supK**2*upper2)),
        "first_unadmitted":failure,"proof":"R734 section 4 equal-state restart (9). The strict upper denominator is independent of the fixed rectangle used by R738. Passing its test yields full-circle isometry only; failure of this sufficient bound does not decide the true lifespan."}


def compute(repo, work, summary):
    if os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public" or os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("public project Actions required")
    work.mkdir(parents=True,exist_ok=True)
    topic = repo / old.TOPIC
    full, params, binding = old.recover(repo, work)
    previous, formula = previous_and_formula(topic, full, params, binding)
    if len(full.x)!=416 or len(full.coefficients)!=415:
        raise ValueError("complete original 416-knot representation required")
    columns = [[], [], []]
    ready_count = []
    origins = []
    failure = None
    state = (old.RMINUS, old.RPLUS, Q(64), Q(0))
    prefix = geo = Q(0)
    geom_open = True
    supK = Q(0)
    accepted = whole = 0
    census = Counter()
    raw = work/"r738-all-415-closed-leaves.ndjson"
    with raw.open("wb") as out:
        def emit(obj):
            out.write(old.json_bytes(obj))
        emit({"schema":"r738-closed-leaves-v1","binding":binding,"source_pins":SOURCE_PINS,
              "start_m_M_Y_T":words(state),"formula":formula,"binary_fraction_bits":BITS,
              "bernstein_bounds_order":["a","a_ss","a_s","a*a_ss","a_s*a_ss-a*a_sss"],
              "bound_order":["upper_c","upper_K","upper_A_minus","lower_sqrt_a_ass","upper_a"],
              "leaf_address":"piece i, dyadic index j at depth n, normalized closed [j/2^n,(j+1)/2^n]"})
        for i, (left, right, co) in enumerate(zip(full.x, full.x[1:], full.coefficients)):
            origins.append(state if failure is None and prefix==left else None)
            width = right-left
            curves, signs = curves_and_signs(co, width)
            ok = [item["holds"] for item in signs]
            for column, yes in zip(columns, ok):
                column.append("1" if yes else "0")
            emit({"piece":i, "domain":words((left,right)), "six":words(co),
                  "original_endpoint_indices":[i,i+1], "whole_scalar_signs":signs})
            ready = 0

            def visit(bs, j, n, base_mesh):
                nonlocal state, prefix, geo, geom_open, failure, supK, accepted, ready
                h = width/(1 << n)
                s = left+j*h
                tag, bounds, signs_here = enclosure(bs, ok)
                row = {"i":i,"j":j,"n":n,"base_mesh":base_mesh,
                       "exact_scalar_signs":signs_here,"scalar_reason":tag,
                       "bernstein_hulls":[words((min(b),max(b))) for b in bs]}
                he_ok = False
                if bounds is not None:
                    C,H,E,d,amax = bounds
                    he1,he2 = h*(C*(2+4*MSTAR_UP**2*H)+2*E), h*C*H*MSTAR_UP**2
                    row["bounds"] = words(bounds)
                    row["h_e1_e2"] = words((he1,he2))
                    he_ok = max(he1,he2)<1
                if base_mesh:
                    census[tag]+=1
                    if he_ok:
                        ready+=1
                if failure is not None:
                    row["origin"]="unreached"; emit(row)
                    return
                if s != prefix:
                    raise ArithmeticError("origin continuation lost its physical adjacency")
                status, ns = trial(state,h,bounds) if bounds is not None else (tag,None)
                row["origin"]=status
                row["entry_m_M_Y_T"]=words(state)
                if ns is not None:
                    row["trial_m_M_Y_T"]=words(ns)
                emit(row)
                if status=="accepted":
                    prefix=s+h
                    state=ns
                    accepted+=1
                    supK=max(supK,bounds[1])
                    # a(0)=1 and nonnegative a' imply a>=1 on this contiguous prefix.
                    if geom_open and bounds[1]<=Q(3,8) and bounds[4]<=Q(1001,1000):
                        geo=min(prefix,Q(1,200))
                        geom_open=prefix<Q(1,200)
                    else:
                        geom_open=False
                    return
                if n<LAST_DEPTH:
                    l,r=split(bs)
                    visit(l,2*j,n+1,False)
                    if failure is None:
                        visit(r,2*j+1,n+1,False)
                    return
                failure={"piece_zero_based":i,"dyadic_index":j,"depth":n,
                         "left":str(s),"right":str(s+h),"status":status,
                         "actual_closed_leaf_scalar_signs":signs_here,
                         "entry_m_M_Y_T":words(state),"trial_m_M_Y_T":words(ns) if ns is not None else None,
                         "bounds_C_H_E_d_amax":words(bounds) if bounds is not None else None}

            def base_leaves(bs, j=0, n=0):
                if n==BASE_DEPTH:
                    visit(bs,j,n,True)
                    return
                l,r=split(bs)
                base_leaves(l,2*j,n+1)
                base_leaves(r,2*j+1,n+1)

            base_leaves(curves)
            ready_count.append(ready)
            if prefix==right:
                whole=i+1
    scalar_words=["".join(col) for col in columns]
    old_cols=previous["cell_status_columns"]
    baseline=old_cols[:3]
    if scalar_words!=baseline:
        raise ArithmeticError("whole-piece exact sign classification differs from published R734")
    hybrid=cooperative_restart(full,origins,previous)
    protected=max(geo,Q(formula["larger_formula_width"]))
    conclusion={"schema":"r738-original-all415-rational-comparison-v1",
        "repository":os.environ["GITHUB_REPOSITORY"],"run":os.environ["GITHUB_RUN_ID"],
        "attempt":os.environ["GITHUB_RUN_ATTEMPT"],"rules_read_commit":os.environ["R738_RULES_COMMIT"],
        "trigger_commit":os.environ["GITHUB_SHA"],
        "source_commit":subprocess.check_output(["git","rev-parse","HEAD"],cwd=repo,text=True).strip(),
        "script":old.ident(Path(__file__).read_bytes()),"source_pins":SOURCE_PINS,"binding":binding,
        "R734_result":old.ident((topic/NOTE734).read_bytes()),"R734_all_rows":previous["all_415_rows"],
        "R734_cooperative_whole_pieces":previous["complete_core_prefix_piece_count"],
        "formula":formula,"knots":len(full.x),"pieces":len(full.coefficients),"base_depth":BASE_DEPTH,
        "base_closed_leaves":len(full.coefficients)*(1<<BASE_DEPTH),"maximum_origin_depth":LAST_DEPTH,
        "fractional_bits_for_outward_rounding":BITS,
        "scalar_order":list(old.PREDICATES[:3]),"exact_whole_piece_scalar_columns":scalar_words,
        "base_leaf_scalar_reasons":dict(census),
        "conditional_ready_base_leaves_per_piece":ready_count,
        "conditional_ready_definition":"Both h*e_j<1 and complete scalar enclosure; the strict entry-state margins still have to pass.",
        "uninterrupted_origin":{"end":str(prefix),"end_approx":float(prefix),"whole_original_pieces":whole,
           "accepted_closed_leaves":accepted,"last_m_M_Y_T":words(state),
           "sup_K_upper":str(supK),"II_operator_upper":str(max(1/MSTAR,MSTAR_UP*supK)),
           "first_unadmitted_leaf":failure,
           "meaning":"Full-circle fixed-metric C2 mirrored immersion through accepted closed leaves. An inconclusive leaf is not a physical breakdown or a bound on the true lifespan."},
        "cooperative_restart_after_noncooperative_origin":hybrid,
        "proved_fixed_metric_halfwidth":str(max(prefix,Q(hybrid.get("end","0")),Q(formula["larger_formula_width"]))),
        "two_sided_ordered_radius_0_16":{"formula_halfwidth":formula["larger_formula_width"],
           "separately_checked_leaf_halfwidth":str(geo),"proved_halfwidth":str(protected),
           "proof":"R734 section 6 with R738 sections 2-3; on the additional contiguous leaves width<=1/200, 1<=a<=1.001, K<=3/8, and strict rectangle. No remote-pair claim beyond this signed strip."},
        "all_piece_leaf_ledger":file_identity(raw),"raw_uploaded":False,
        "ledger_recipe":"One NDJSON header, then each source piece, all base leaves, and any attempted origin refinements. Each leaf has exact Bernstein hulls, decisions, and if available C,H,E,d,amax and h*e_j. Margins propagate from the genuine core only.",
        "physical_F_array":None,"Jacobian":None,"normal_roots":None}
    summary.write_bytes(old.json_bytes(conclusion))


def file_identity(path):
    digest=sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1048576),b""):
            digest.update(block)
    return {"bytes":path.stat().st_size,"sha256":digest.hexdigest()}


if __name__=="__main__":
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--repo",type=Path,required=True)
    cli.add_argument("--work",type=Path,required=True)
    cli.add_argument("--summary",type=Path,required=True)
    args=cli.parse_args()
    compute(args.repo.resolve(),args.work.resolve(),args.summary.resolve())

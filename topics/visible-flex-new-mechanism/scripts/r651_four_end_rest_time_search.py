"""Find and enclose actual positive four-end rest times, using the R651 chart."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
import os
import time

import numpy as np
from scipy.optimize import differential_evolution


class SearchFinished(Exception):
    pass


def emit(tag, **record):
    print("R651_"+tag+" "+json.dumps(record, sort_keys=True, allow_nan=False), flush=True)


def motion(t, leg):
    """Return the original fields and t-derivatives on one unit reference segment."""
    kind, h0, h1, k0, k1, eta0, duration = leg
    if kind == "center":
        shape = t*(1+t*t*(4+t*(-7+3*t)))
        shape_t = (1-t)**2*(15*t*t+2*t+1)
    else:
        shape = t**3*(10+t*(-15+6*t))
        shape_t = 30*t*t*(1-t)**2
    if kind == "height":
        h = h0+(h1-h0)*shape
        k = k0
        eta = eta0
        h_t = (h1-h0)*shape_t
        k_t = 0
    else:
        h = h0
        k = k0+(k1-k0)*shape
        eta = eta0+(k-k0)/(2*h)
        h_t = 0
        k_t = (k1-k0)*shape_t
    d = h*eta-k
    u = h_t/h/duration
    v = (h_t*eta-k_t/2)/duration
    q = 1+d*d
    return (duration*(k*k-1-u*u), duration*(-k*d),
            duration*(eta*d*(k*d-1)/h-v*v/h**2),
            duration*(q*(k*k+2*k*d-1)+u*u*q-2*u*d*v)/h**2)


def stationary(h, k, eta):
    d = h*eta-k
    return (k*k-1, -k*d, eta*d*(k*d-1)/h, (1+d*d)*(k*k+2*k*d-1)/h**2)


def pieces(p):
    H, a = p["H"], p["a"]
    ys, order, times = p["levels"], p["order"], p["durations"]
    heights = [2*H*y for y in ys]
    eta = -a/(2*H)
    moving = [("center", H, H, 0, -a, 0, times[0])]
    for j in range(3):
        left, right = heights[order[j]], heights[order[j+1]]
        moving.append(("height", left, right, -a, -a, eta, times[j+1]))
    extra = p.get("excursion")
    rest = None
    if extra is not None:
        height = heights[extra["level"]]
        other, T = extra["other_k"], extra["leg_duration"]
        at_rest = eta+(other+a)/(2*height)
        moving.extend([("k",height,height,-a,other,eta,T), ("k",height,height,other,-a,at_rest,T)])
        rest = (extra["hold"], stationary(height,other,at_rest))
        # Insert the out-and-back at this stop in the chronological path.
        # Its terminal h,k,eta equal the initial h,k,eta, so the original
        # four transition integrals commute with its contribution to b.
    return moving, rest, [stationary(h,-a,eta) for h in heights]


def parameters(x, order, with_loop):
    a = x[0]
    H = max(.802, a/2+.002)
    upper = (3-.004)/(2*H)
    levels = [.5]
    for val in x[1:4]:
        levels.append(levels[-1]+(upper-levels[-1])*val)
    durations = [a*(9/4)/6+.003+x[4]]
    for left,right,z in zip(order,order[1:],x[5:8]):
        durations.append(2*H*abs(levels[right]-levels[left])*(15/8)/6+.003+z)
    p = {"H":H,"a":a,"levels":levels,"order":list(order),"durations":durations}
    if with_loop:
        other = x[8]
        p["excursion"] = {"level":order[-1], "other_k":other,
            "leg_duration":abs(other+a)*(15/8)/6+.003+x[9], "hold":x[10]}
    return p


def length_of_motion(p):
    extra = p.get("excursion")
    return sum(p["durations"]) + (0 if extra is None else 2*extra["leg_duration"]+extra["hold"])


def candidate(p, t, weights):
    moving, rest, columns = pieces(p)
    b = np.zeros(4)
    for leg in moving:
        for j,v in enumerate(motion(t,leg)):
            b[j] += np.sum(v*weights)
    if rest is not None:
        b += rest[0]*np.asarray(rest[1])
    matrix = np.asarray(columns).T
    dwell = np.linalg.solve(matrix, -b)
    length = length_of_motion(p)+float(np.sum(dwell))
    score = min(*dwell, length-2.1, 7.9-length)
    if rest is not None:
        e = p["excursion"]
        h = 2*p["H"]*p["levels"][e["level"]]
        eta = -p["a"]/(2*p["H"])+(e["other_k"]+p["a"])/(2*h)
        score = min(score, 1-abs(eta))
    return float(score), {"parameters":p,"four_dwell_times":dwell.tolist(),"length":length,
        "four_moving_end_integrals":b.tolist(),"true_four_end_float_reconstruction":(b+matrix@dwell).tolist()}


def rationalize(p):
    f = lambda x: F(f"{x:.10f}")
    out = {"H":f(p["H"]), "a":f(p["a"]), "durations":[f(x) for x in p["durations"]],
           "levels":[f(x) for x in p["levels"]], "order":p["order"]}
    if "excursion" in p:
        e=p["excursion"]
        out["excursion"]={k:(v if k=="level" else f(v)) for k,v in e.items()}
    return out


def exact_inverse(columns):
    aug = [[F(columns[j][i]) for j in range(4)]+[F(int(i==j)) for j in range(4)] for i in range(4)]
    for idx in range(4):
        pivot = next(j for j in range(idx,4) if aug[j][idx])
        aug[idx],aug[pivot] = aug[pivot],aug[idx]
        pivot_value=aug[idx][idx]
        aug[idx]=[v/pivot_value for v in aug[idx]]
        for j in range(4):
            if j != idx:
                scale=aug[j][idx]
                aug[j]=[v-scale*w for v,w in zip(aug[j],aug[idx])]
    return [row[4:] for row in aug]


def physical_bounds(p):
    H, a=p["H"],p["a"]
    heights=[2*H*y for y in p["levels"]]
    moving, _, _ = pieces(p)
    vmax=F(0)
    gmax=F(0)
    kmax=abs(a)
    emax=abs(a/(2*H))
    for kind,h0,h1,k0,k1,e0,T in moving:
        if T<=0:
            raise ValueError("A moving segment has nonpositive physical duration")
        gmax=max(gmax,F(15,8)*abs(h1-h0)/T)
        vmax=max(vmax,(F(9,4) if kind=="center" else F(15,8))*abs(k1-k0)/T)
        kmax=max(kmax,abs(k0),abs(k1))
        emax=max(emax,abs(e0),abs(e0+F(k1-k0)/(2*h0)))
    cert={"h_lower":min(heights),"h_upper":max(heights),"abs_k_upper":kmax,
          "abs_eta_upper":emax,"abs_gamma_upper":gmax,"abs_upsilon_upper":vmax,
          "center_B2":-H*(a/p["durations"][0])**2/4}
    return (F(4,5)<min(heights) and max(heights)<3 and kmax<2 and emax<1 and gmax<6
            and vmax<6 and cert["center_B2"]<0
            and (p.get("excursion",{}).get("hold",0)>=0)),cert


def rigorous(p, counts, deadline):
    from flint import acb, arb, ctx, fmpq

    ctx.prec = 128
    def rational(x):
        x = F(x)
        return fmpq(x.numerator,x.denominator)
    def ball(x):
        return acb(rational(x))
    geometry_ok, bounds = physical_bounds(p)
    result={"parameters_exact":json.loads(json.dumps(p,default=str)),
        "whole_segment_physical_bounds":{k:str(v) for k,v in bounds.items()},
        "geometry_certified":geometry_ok,"certified":False, "motion_integrals":[]}
    if not geometry_ok:
        return result
    moving,rest,columns=pieces(p)
    inverse=exact_inverse(columns)
    b=[acb(0) for _ in range(4)]
    for segment,leg in enumerate(moving):
        ball_leg=(leg[0], *(ball(x) for x in leg[1:]))
        for row in range(4):
            def integrand(t, analytic):
                counts["ball_integrand_calls"]+=1
                if time.monotonic()>deadline or not t.is_finite():
                    return acb(arb.nan(),arb.nan())
                # All expressions are rational and holomorphic wherever h
                # is nonzero; division over a ball containing zero returns
                # a nonfinite enclosure and forces subdivision by Arb.
                return motion(t,ball_leg)[row]
            if time.monotonic()>deadline:
                result.update(pending_segment=segment,pending_row=row)
                return result
            value=acb.integral(integrand,0,1,abs_tol=1.e-22,rel_tol=1.e-22,
                               eval_limit=16000,depth_limit=80)
            counts["ball_segment_row_integrals"]+=1
            result["motion_integrals"].append({"segment":segment,"row":row,"enclosure":value.str(28)})
            if not value.is_finite() or not value.imag.contains(0):
                result.update(pending_segment=segment,pending_row=row)
                return result
            b[row]+=value
    if rest is not None:
        for j,rate in enumerate(rest[1]):
            b[j]+=ball(rest[0]*rate)
    tballs=[-sum((ball(v)*bj for v,bj in zip(row,b)),acb(0)).real for row in inverse]
    length=arb(rational(length_of_motion(p)))+sum(tballs,arb(0))
    result.update(four_original_moving_ends=[v.real.str(28) for v in b],
        positive_duration_enclosures=[v.str(28) for v in tballs],length_enclosure=length.str(28),
        exact_durations_defined_by="minus exact rational stationary matrix inverse times original continuous moving moments",
        certified=bool(all(v.lower().fmpq()>0 for v in tballs) and
                       length.lower().fmpq()>fmpq(21,10) and length.upper().fmpq()<fmpq(79,10)))
    return result


def main():
    if not (os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY","").lower()
            =="rogerhu12/math-research-public" and os.environ.get("GITHUB_RUN_ID","").isdigit()):
        raise RuntimeError("This scientific computation requires the bound public repository Actions run")
    parser=argparse.ArgumentParser()
    parser.add_argument("--max-seconds",type=float,required=True)
    parser.add_argument("--reserve-seconds",type=float,required=True)
    parser.add_argument("--seed",type=int,required=True)
    parser.add_argument("--evaluations-per-family",type=int,required=True)
    args=parser.parse_args()
    started=time.monotonic()
    search_end=started+args.max_seconds-args.reserve_seconds
    nodes,weights=np.polynomial.legendre.leggauss(24)
    nodes,weights=(1+nodes)/2,weights/2
    counts=Counter()
    best=None
    family_records=[]
    proof=None
    status="finite_search_incomplete_no_infeasibility_claim"
    families=[([0,1,2,3],False),([0,1,2,3],True),([0,2,1,3],True),
              ([0,3,1,2],True),([0,2,1,3],False),([0,3,1,2],False)]
    try:
        for index,(order,excursion) in enumerate(families):
            report={"order":order,"with_excursion":excursion,"calls":0,"best":None}
            family_records.append(report)
            now = time.monotonic()
            family_end = now+max(0,search_end-now)/(len(families)-index)
            def objective(x):
                nonlocal best
                if time.monotonic()>=family_end or report["calls"]>=args.evaluations_per_family:
                    raise SearchFinished()
                report["calls"]+=1
                counts["candidate_calls"]+=1
                p=parameters(x,order,excursion)
                score,data=candidate(p,nodes,weights)
                if report["best"] is None or score>report["best"]:
                    report.update(best=score,parameters=p)
                if best is None or score>best["score"]:
                    best={"score":score,"family":index,**data}
                if score>1.e-5:
                    raise SearchFinished()
                return -score
            limits=[(1.005,1.97),(.04,.62),(.12,.82),(.35,.995),(.002,1.8),
                    (.002,1.0),(.002,1.0),(.002,1.0)]
            if excursion:
                limits += [(-1.985,1.985),(.001,.75),(.001,1.8)]
            try:
                differential_evolution(objective,limits,popsize=12,maxiter=1000,tol=1.e-9,
                    polish=False,rng=np.random.default_rng(args.seed+index),updating="immediate",workers=1)
            except SearchFinished:
                pass
            emit("FAMILY",**report)
            if best is not None and best["score"]>1.e-5:
                proof=rigorous(rationalize(best["parameters"]),counts,started+args.max_seconds)
                if proof["certified"]:
                    status="continuous_four_even_end_input_certified_full_ruling_open"
                else:
                    status="candidate_with_open_interval_or_physical_qualification"
                break
            if time.monotonic()>=search_end:
                break
    except Exception as exc:
        status="attempt_failed_with_inputs_and_costs_preserved"
        emit("EXCEPTION",type=type(exc).__name__,message=str(exc))
    emit("FOUR_END_FINAL",status=status,best_candidate=best,ball_result=proof,
        families=family_records,counts=dict(counts),new_science_seconds=time.monotonic()-started,
        absent_feasible_sample_implies_infeasibility=False,
        four_end_closure_implies_original_ruling_or_README_completion=False)


if __name__=="__main__":
    main()

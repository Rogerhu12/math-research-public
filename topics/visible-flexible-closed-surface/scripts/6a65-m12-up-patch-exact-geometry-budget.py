#!/usr/bin/env python3
"""Exact rational local geometry budget for the frozen v2 Cartesian up patch.

Finite binary jets and coefficients are interpreted as rational numbers. The
large regenerated NPZ and output JSON belong in a temporary directory. This
script bounds all source-cell interiors by coefficient absolute sums; it does
not infer continuous bounds from samples. R21/R25/R114 scalar certificates are
explicit hypotheses, not newly recomputed whole-surface certificate files.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("m12_recovery",HERE/"6a65-m12-weak-stress-recovered-v2.py")
screen=importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)
q=screen.q
DATA_SHA=screen.DATA_SHA


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def span_power(raw, cell):
    mesh, jets, inc=raw["mesh"],raw["jets"],raw["mean_increments"]
    h=q(mesh[cell+1])-q(mesh[cell])
    columns=[]
    for j in range(jets.shape[-1]):
        y0,y1,d0,d1,z0,z1=(q(jets[a,b,j]) for a,b in
                          [(0,cell),(0,cell+1),(1,cell),(1,cell+1),(2,cell),(2,cell+1)])
        delta=q(inc[cell]) if j==jets.shape[-1]-1 else y1-y0
        c0=Q(0) if j==jets.shape[-1]-1 else y0
        # c0 for the mean height may be set to zero: every bound below uses
        # a positive s derivative or an angular derivative which kills it.
        c1,c2=h*d0,h*h*z0/2
        r0=delta-c1-c2
        r1=h*(d1-d0)-h*h*z0
        r2=h*h*(z1-z0)
        columns.append([c0,c1,c2,10*r0-4*r1+r2/2,
                        -15*r0+7*r1-r2,6*r0-3*r1+r2/2])
    return h,columns


def coefficient_bounds(h,columns,derivative):
    result=[]
    for row in columns:
        result.append(sum((abs(row[j])*Q(math.factorial(j),math.factorial(j-derivative))
                           for j in range(derivative,6)),Q(0))/h**derivative)
    return result


def angle_l1(row,M,order):
    if order not in (1,2):
        raise ValueError("Only derivative orders 1,2")
    v=row[0]
    for j in range(1,M+1):
        k=3*j
        v+=(k+1)**order*(row[j]+row[M+j])+k**order*row[2*M+j]
    return v


def chart_bounds(meta,end,left,right):
    knots,coeff=screen.exact_clamped_spline(meta["chart"])
    x0,x1=left/end,right/end
    if not 0<=x0<x1<Q(3,4):
        raise ValueError("Patch reaches chart cutoff")
    warp=8*q(meta["warp_reference_q"])
    bounds=[Q(0)]*3
    selected=0
    for j,cs in enumerate(coeff):
        if knots[j+1]<=x0 or knots[j]>=x1:
            continue
        # A full spline-piece absolute sum encloses the intersected subpiece.
        h=knots[j+1]-knots[j]
        for d in range(3):
            bd=warp/end**d*sum((abs(cs[k])*Q(math.factorial(k),math.factorial(k-d))*h**(k-d)
                               for k in range(d,4)),Q(0))
            bounds[d]=max(bounds[d],bd)
        selected+=1
    return bounds,selected


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data",type=Path,required=True)
    ap.add_argument("--parameters",type=Path,required=True)
    ap.add_argument("--geometry",type=Path,default=HERE.parent/"notes"/screen.META_NAME)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh output")
    start=time.monotonic()
    if sha(args.data)!=DATA_SHA:
        raise ValueError("Frozen payload SHA mismatch")
    meta=json.loads(args.geometry.read_text())
    params=json.loads(args.parameters.read_text())
    if params["geometry_sha256"]!=sha(args.geometry) or params["data_sha256"]!=DATA_SHA:
        raise ValueError("Frozen geometry identity mismatch")
    rg=screen.regions(meta)[0]
    left,right=rg["left"],rg["right"]
    if params["regions"][0]["support_rational"]!=[str(left),str(right)]:
        raise ValueError("Support mismatch")
    hexes=params["regions"][0]["fit"]["coefficients_hex"]
    coeff=[float.fromhex(x) for x in hexes]
    if len(coeff)!=24 or [float(x) for x in params["regions"][0]["fit"]["coefficients"]]!=coeff:
        raise ValueError("Exact hexadecimal coefficient mismatch")
    with np.load(io.BytesIO(gzip.decompress(args.data.read_bytes())),allow_pickle=False) as f:
        raw={k:f[k].copy() for k in ("mesh","jets","mean_increments")}
    M=(raw["jets"].shape[-1]-2)//3
    if M!=24 or raw["jets"].shape!=(3,2570,74):
        raise ValueError("Unexpected source shape")
    mesh=[q(x) for x in raw["mesh"]]
    if right>=mesh[meta["correction_start_index"]]:
        raise ValueError("Patch intersects common-cut correction")
    bpsi=bss=bsp=bpp=Q(0)
    cells=0
    for cell in range(len(mesh)-1):
        if mesh[cell+1]<=left or mesh[cell]>=right:
            continue
        h,power=span_power(raw,cell)
        b0,b1,b2=[coefficient_bounds(h,power,d) for d in range(3)]
        bpsi=max(bpsi,angle_l1(b0,M,1))
        bss=max(bss,sum(b2,Q(0)))
        bsp=max(bsp,angle_l1(b1,M,1))
        bpp=max(bpp,angle_l1(b0,M,2))
        cells+=1
    (e0,e1,e2),chart_cells=chart_bounds(meta,mesh[-1],left,right)
    rho=1-e0
    if rho<=0:
        raise ArithmeticError("Chart inverse bound unresolved")
    A=e1/(3*rho)
    Css=(e2/3+2*e1*A+3*e0*A*A)/rho
    Csu=(e1+3*e0*A)/(rho*rho)
    Cuu=3*e0/(rho**3)
    Hss=bss+2*A*bsp+A*A*bpp+Css*bpsi
    Hsu=(bsp+A*bpp)/rho+Csu*bpsi
    Huu=bpp/(rho*rho)+Cuu*bpsi
    # Physical sigma=s/lambda, lambda<2; original target radius f>=2/5.
    C_X=4*Hss+10*Hsu+Q(25,4)*Huu
    w=screen.exact_budget(coeff,right-left)
    WB={k:Q(v) for k,v in w["bounds_rational"].items()}
    eta=WB["W"]
    C_W=4*WB["Wss"]+10*WB["Wsu"]+Q(25,4)*WB["Wuu"]
    d,p,newd=Q(257212,10**13),Q(9,10**9),Q(44,10**9)
    # sqrt(2(1+d)) < 3/2 and normalization Lipschitz estimate.
    normal_change=(3*p+p*p)/(1-d)
    prefix_K=(Q(5547266,10**6)*(1+d)+normal_change*C_X+C_W)/(1-newd)
    support=Q(737,1000)-Q(19,10)*normal_change-eta
    tail_K=Q(4763997235009095,562949953421312)
    radius=Q(2131902881202937,1125899906842624)+eta
    diameter=2*radius
    reach_ratio=1/(tail_K*diameter)
    hold_ratio=(Q(19989114,10**8)-2*eta)/diameter
    H_ratio=Q(35426,10**4)/diameter
    # Unmarked old body: support>.7, radius<2 => area<150. Tube |t|<eta
    # has Jacobian <=(1+9 eta)^2; |(x+iy)^3|<8 on the swept region.
    moment_change=2*eta*150*(1+9*eta)**2*8
    checks=dict(
        chart_positive=rho>0,
        dW_budget=all(w["strict_limits"].values()) and w["dW_g_less_than_9e_9"],
        global_metric=w["original_global_metric_budget_less_than_4_4e_8"],
        C_X_less_than_1e6=C_X<10**6,
        normal_estimate_hypothesis=2*(1+d)<Q(9,4),
        normal_change_less_than_4e_8=normal_change<Q(4,10**8),
        new_prefix_K_less_than_6=prefix_K<6,
        unchanged_tail_dominates=tail_K>6,
        support_greater_than_0_736=support>Q(736,1000),
        support_exceeds_inverse_curvature=support>1/tail_K,
        reach_ratio_greater_than_0_0312=reach_ratio>Q(312,10**4),
        hold_ratio_greater_than_0_05278=hold_ratio>Q(5278,10**5),
        fixed_H_ratio_greater_than_0_93=H_ratio>Q(93,100),
        moment_change_less_than_1e_7=moment_change<Q(1,10**7),
        activity_real_moment_greater_than_0_44=Q(44016,10**5)-moment_change>Q(44,100),
        tube_smaller_than_original_reach=eta<1/tail_K,
        original_surface_area_less_than_150=Q(4)*Q(22,7)*8/Q(7,10)<150)
    values=dict(native_Xpsi=bpsi,native_Xss=bss,native_Xspsi=bsp,native_Xpsipsi=bpp,
                chart_e=e0,chart_ep=e1,chart_epp=e2,chart_rho_lower=rho,
                material_Xss=Hss,material_Xsu=Hsu,material_Xuu=Huu,C_X=C_X,C_W=C_W,
                normal_change=normal_change,new_prefix_curvature=prefix_K,new_support=support,
                diameter_upper=diameter,reach_ratio_lower=reach_ratio,hold_ratio_lower=hold_ratio,
                fixed_H_ratio_lower=H_ratio,moment_change=moment_change)
    out=dict(status="EXACT_RATIONAL_BUDGET_PASS" if all(checks.values()) else "FAILED",
             source_sha256=sha(__file__),screen_source_sha256=sha(HERE/"6a65-m12-weak-stress-recovered-v2.py"),
             data_sha256=DATA_SHA,geometry_sha256=sha(args.geometry),parameters_sha256=sha(args.parameters),
             source_cells=cells,chart_pieces=chart_cells,
             inherited_hypotheses="R21 exact metric and prefix/tail curvature/support; R25 enclosing ball; R114 coordinate lambda<2 and f>=2/5. No new G5 convergence claim.",
             exact={k:str(v) for k,v in values.items()},display={k:float(v) for k,v in values.items()},
             checks=checks,all_checks_pass=all(checks.values()),seconds=time.monotonic()-start)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="exact"},indent=2))
    if not out["all_checks_pass"]:
        raise SystemExit(1)


if __name__=="__main__":
    main()


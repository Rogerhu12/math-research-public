#!/usr/bin/env python3
"""R168 exact rational budgets for two complete R121 corner-cap variants.

Only proven scalar inequalities are evaluated. No mesh, body, BVP or
approximate surface is used. I = integral_0^pi sqrt(sin t) dt is enclosed
by the exact inequalities 2 < I < 22/7. Decimal fields are display only.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import isqrt
from pathlib import Path


def record(q):
    q = Q(q)
    return dict(exact=str(q), approximate=float(q))


def square_root_enclosure(q, digits=35):
    q = Q(q)
    if q < 0:
        raise ValueError('Negative radicand')
    scale = 10**digits
    n = isqrt(q.numerator*scale*scale//q.denominator)
    lo = Q(n,scale)
    hi = lo if lo*lo == q else Q(n+1,scale)
    assert lo*lo <= q <= hi*hi
    return lo,hi


COMMON = dict(A=Q(32,25), slab=Q(17,20), neck=Q(3,10), cuff=Q(8,25),
    lam=Q(1,100), epsilon=Q(1,10000), delta=Q(1,1000000))
VARIANTS = {
    'D4':dict(D=Q(4),R=Q(121,1000),c=Q(14,25),b=Q(211,200),
        h=Q(153,100),H=Q(39,20),Zmax=Q(29,25),tail_Zmin=Q(229,250),
        loose_budget_ceiling=Q(59,50)),
    'D375':dict(D=Q(15,4),R=Q(113,1000),c=Q(27,50),b=Q(26,25),
        h=Q(349,250),H=Q(91,50),Zmax=Q(21,20),tail_Zmin=Q(853,1000),
        loose_budget_ceiling=Q(107,100)),
}


def height_budget_limit(D):
    """Closure supremum of the stated sufficient ball/marker inequalities.

    A is the fixed conservative central-support lower bound 1.28. This is
    not an obstruction to other caps, other ball proofs or larger actual A.
    Strict reach/quotient margins approach but do not attain R0,b0 below.
    """
    A,W,a,e,d,lam = (COMMON[k] for k in ('A','slab','neck','epsilon','delta','lam'))
    B = D/2
    R = 3*D/100
    b = W+D/20+e
    radlo,radhi = square_root_enclosure(A*A-b*b)
    clo=max(a+R+d,A-radhi);chi=max(a+R+d,A-radlo)
    hsqlo=(B-R-e)**2-chi*chi-(b-R)**2
    hsqhi=(B-R-e)**2-clo*clo-(b-R)**2
    hlo=square_root_enclosure(hsqlo)[0]
    hhi=square_root_enclosure(hsqhi)[1]
    zlo=hlo-e-3*R-R*lam*Q(22,7)
    zhi=hhi-e-3*R-2*R*lam
    return dict(scope='Supremum only within these sufficient inequalities at fixed A_min=1.28 and W=.85; not geometric nonexistence',
        limiting_R=record(R),limiting_b=record(b),
        limiting_c_interval=[record(clo),record(chi)],
        ceiling_Z_interval=[record(zlo),record(zhi)],
        exact_formula='sqrt((D/2-R-epsilon)^2-c_min^2-(b-R)^2)-epsilon-3R-lambda*R*I',
        I_definition='integral_0^pi sqrt(sin(t)) dt, with 2<I<22/7',
        strict_ratio_limits_not_attained=True)


def budget(name):
    v=VARIANTS[name];A,W,a,ac,lam,e,d=(COMMON[k] for k in
        ('A','slab','neck','cuff','lam','epsilon','delta'))
    D,R,c,b,h,H,Zmax,Ztail=(v[k] for k in
        ('D','R','c','b','h','H','Zmax','tail_Zmin'))
    B=D/2;gap=D/5
    zclo=h-e-3*R-R*lam*Q(22,7)
    zchi=h-e-3*R-2*R*lam
    hmin=gap+e+3*R+2*R*lam
    Hmin=hmin+H-h
    dep=Q(69,250);tailR=Q(736,4725);cut=Q(4,5)
    qlower=b-e-W
    margins=dict(
        mollifier_level=e-d,
        pyramid_height=H-R-h,
        flat_base_disk=min(c,b-R)-d-a-R,
        neck_radius_minus_reach=a-R*(1+2*lam)-R,
        annulus_width=ac-a,
        whole_convex_body_ball=(B-R-e)**2-c*c-(b-R)**2-h*h,
        top_ball=B-H-e,
        neck_annulus_ball=B*B-ac*ac-(h-e-R)**2,
        cap_x_slab=W-c-R-e,
        central_marker_inball=2*A*c-c*c-b*b,
        translated_marker_height=hmin-b,
        opposite_caps_separation=2*gap-2*R,
        fixed_grip_diameter=2*Hmin-2*e-gap,
        selected_Zmax_below_accurate_reference=zclo-Zmax,
        reach_ratio=R/D-Q(3,100),
        quotient_ratio=qlower/D-Q(1,20),
        tail_radius=tailR-R,
        tail_to_opposite_tail=2*(Ztail-dep)-2*R,
        tail_within_ball=B*B-cut*cut-Zmax*Zmax,
        tail_slab=W-cut,
        tail_control_held=(A-cut)**2+(Ztail-dep)**2-gap*gap,
        tail_Z_interval=Zmax-Ztail)
    zero_allowed={'tail_control_held'}
    for key,value in margins.items():
        if (value<0 if key in zero_allowed else value<=0):
            raise AssertionError((name,key,str(value)))
    assert gap<=Ztail<=Zmax<zclo<zchi
    lim=height_budget_limit(D)
    assert Q(lim['ceiling_Z_interval'][1]['exact'])<v['loose_budget_ceiling']
    values=dict(diameter_upper=D,ball_radius=B,held_radius=gap,reach_radius=R,
        central_axis_support_lower=A,active_halfwidth=W,corner_x=c,corner_y=b,
        reference_side_height=h,reference_pole_height=H,cuff_radius=ac,neck_radius=a,
        cap_Zmin=gap,chosen_cap_Zmax=Zmax,reference_Z_lower=zclo,reference_Z_upper=zchi,
        uniform_flat_tail_Zmin=Ztail,tail_depression_upper=dep,
        cap_x_halfwidth=c+R+e,cap_y_halfwidth=b+e,
        translated_side_height_lower=hmin,translated_pole_height_lower=Hmin,
        fixed_grip_diameter_lower=2*Hmin-2*e,
        quotient_lower=qlower,held_ratio_lower=gap/D,
        quotient_ratio_lower=qlower/D,reach_ratio_lower=R/D,
        available_principal_curvature_cap=1/R,
        conservative_budget_Z_ceiling=v['loose_budget_ceiling'])
    return dict(variant=name,theorem='R168',
        definition=dict(P0_vertices=[[str(s*c),str(t*(b-R)),str(h)]
                for s in (-1,1) for t in (-1,1)]+[['0','0',str(H-R)]],
            P='sublevel (distance_to_P0 convolved with the R111 radial delta-mollifier) <= epsilon',
            K='P + B_R; full convex cap minus the lower circular joining disk',
            neck='R113 full meridian with a=.30, variant R, lambda=.01; add actual .30<=r<=.32 flat annulus',
            placement='upper translate by -(zc-Z) ez, lower reflect; choose actual Z once for the entire phase family'),
        values={k:record(q) for k,q in values.items()},
        exact_margins={k:record(q) for k,q in margins.items()},
        all_required_rational_comparisons_passed=True,
        flat_tail_parameter_box=dict(family='R132 positive Bernstein',control_count='any finite count, including current16',
            each_control_interval=['0','6/5'],cuff_radius='8/25',cut_radius='4/5',flat_radius='17/50'),
        fixed_A_height_tradeoff=lim,
        remaining_actual_conditions=[
            'One common-g embedded C2 core phase family with exact phase-fixed .32 flat disks at +/- actual Z',
            'Global all-phase reach at least variant R of the original flat-disk closed core, not only local curvature',
            'Whole actual core in the variant origin-centered ball and |z|<=actual Z',
            'Phase-zero whole active core |y|<=.85',
            'Actual central points (+/-Aq,0,0), Aq>=1.28, and phase interval containing pi/2',
            'Whole phase-zero core excludes the actual ball centered at (0,Aq,0) of radius D_upper/5',
            'For the optional R132 tail, true prefix-tail full two-jet registration and cross-piece normal-ball inequalities'],
        actual_core_solved=False,strong_target_completed=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh exact-budget report')
    report=dict(schema='fd2d-smaller-complete-corner-caps-exact-budget-v1',
        theorem='R168',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        exact_common_parameters={k:record(v) for k,v in COMMON.items()},
        variants=[budget(name) for name in VARIANTS],
        all_arithmetic_certificates_rational=True,body_or_BVP_runs=0)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(report=str(args.out),passed=True,
        variants={v['variant']:{k:v['values'][k]['approximate'] for k in
            ('diameter_upper','held_radius','reach_radius','chosen_cap_Zmax',
             'uniform_flat_tail_Zmin','quotient_ratio_lower','reach_ratio_lower')}
             for v in report['variants']})),flush=True)
    return 0


if __name__=='__main__':
    raise SystemExit(main())

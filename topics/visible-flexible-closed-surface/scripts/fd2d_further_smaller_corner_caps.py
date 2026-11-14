#!/usr/bin/env python3
"""R179: exact complete-cap budgets for D=3.5 and D=3.2, extending R168.

All computations use Fractions. The full cap is the R168 distance-
mollified convex pyramid, parallel body, neck and actual flat annulus.
No body, nonlinear field, solver or geometry sampling is constructed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time

import fd2d_smaller_corner_caps as parent


COMMON = dict(parent.COMMON)
VARIANTS = {
    'D35': dict(D=Q(7, 2), R=Q(53, 500), c=Q(13, 25), b=Q(513, 500),
                h=Q(251, 200), H=Q(17, 10), Zmax=Q(93, 100),
                Zmin_old=Q(393, 500), Zmin_extended=Q(171, 200)),
    'D32': dict(D=Q(16, 5), R=Q(97, 1000), c=Q(1, 2), b=Q(1011, 1000),
                h=Q(27, 25), H=Q(31, 20), Zmax=Q(39, 50),
                Zmin_old=Q(18, 25), Zmin_extended=Q(77, 100)),
}


def record(value):
    value = Q(value)
    return dict(exact=str(value), approximate=float(value))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cap_budget(name, tail_upper=Q(6, 5)):
    U = Q(tail_upper)
    if U not in (Q(6, 5), Q(3, 2)):
        raise ValueError('Only the two explicitly proved tail function domains are included')
    v = VARIANTS[name]
    D, R, c, b, h, H, Zmax = (v[k] for k in ('D', 'R', 'c', 'b', 'h', 'H', 'Zmax'))
    A, W, a, ac, lam, e, d = (COMMON[k] for k in
        ('A', 'slab', 'neck', 'cuff', 'lam', 'epsilon', 'delta'))
    Zmin = v['Zmin_old' if U == Q(6, 5) else 'Zmin_extended']
    B, g = D / 2, D / 5
    zclo = h - e - 3 * R - lam * R * Q(22, 7)
    zchi = h - e - 3 * R - 2 * lam * R
    hzmin = Zmin + e + 3 * R + 2 * lam * R
    Hzmin = hzmin + H - h
    cut, flat, width = Q(4, 5), Q(17, 50), Q(23, 50)
    dep = U * width / 2
    kappa = Q(630, 256) * U / width
    tail_radius = 1 / kappa
    quotient = b - e - W
    support = min(Zmin, flat * Q(99, 100) + Zmin * Q(7, 100))
    margins = dict(
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
        actual_translated_marker_height=hzmin-b,
        opposite_caps_separation=2*Zmin-2*R,
        fixed_grip_diameter=2*Hzmin-2*e-g,
        selected_Zmax_below_accurate_reference=zclo-Zmax,
        reach_ratio=R/D-Q(3,100),
        quotient_ratio=quotient/D-Q(1,20),
        tail_radius=tail_radius-R,
        tail_to_opposite_tail=2*(Zmin-dep)-2*R,
        tail_within_ball=B*B-cut*cut-Zmax*Zmax,
        tail_slab=W-cut,
        tail_function_held=(A-cut)**2+(Zmin-dep)**2-g*g,
        actual_Z_above_held_radius=Zmin-g,
        actual_Z_interval=Zmax-Zmin,
        tail_support_above_seven_twentieths=support-Q(7,20),
    )
    for key, value in margins.items():
        assert value > 0, (name, str(U), key, str(value))
    assert Zmin < Zmax < zclo < zchi
    values = dict(diameter_upper=D, ball_radius=B, held_radius=g,
        reach_radius=R, local_curvature_cap=1/R,
        central_axis_support_lower=A, active_halfwidth=W,
        cap_corner_x=c, cap_corner_y=b, reference_side_height=h,
        reference_pole_height=H, reference_Z_lower=zclo,
        reference_Z_upper=zchi, actual_Z_lower=Zmin, actual_Z_upper=Zmax,
        actual_marker_height_lower=hzmin, actual_pole_height_lower=Hzmin,
        fixed_grip_diameter_lower=2*Hzmin-2*e,
        tail_function_upper=U, tail_depression_upper=dep,
        tail_curvature_upper=kappa, complete_tail_normal_radius=tail_radius,
        tail_support_lower=support, quotient_lower=quotient,
        held_ratio_lower=g/D, quotient_ratio_lower=quotient/D,
        reach_ratio_lower=R/D,
        old_actual_Z_lower_for_Delta_7_over_50=Zmin+Q(7,50),
        old_actual_Z_upper_for_Delta_7_over_50=Zmax+Q(7,50),
        old_actual_Z_strict_upper_for_any_column_deletion_less_than_point32=Zmax+Q(8,25))
    return dict(
        variant=name,
        definition=dict(
            P0_vertices=[[str(s*c),str(t*(b-R)),str(h)] for s in (-1,1) for t in (-1,1)]
                +[['0','0',str(H-R)]],
            P='sublevel of distance_to_P0 convolved with the R111 radial delta-mollifier at epsilon',
            K='P + B_R, with the actual circular opening replaced by the full R168 neck and .30<=r<=.32 flat annulus',
            upper_placement='translate by -(zc-Z) ez once; actual Z is fixed for every phase',
            lower_placement='z-reflection',
            tail_function_domain=['0',str(U)],
            tail_source='R132/R170 when U=6/5; R177 when U=3/2; unchanged exact function formula',
            cap_parameters_are_new=True,
        ),
        values={k:record(x) for k,x in values.items()},
        exact_margins={k:record(x) for k,x in margins.items()},
        all_required_rational_comparisons_passed=True,
        remaining_actual_inputs=[
            'A common-g C2 embedded core family with exact fixed .32 disks and full two-jet seams at actual +/-Z',
            'Global all-phase reach of that complete old flat-disk core at least R, including prefix-tail and all opposite-half pairs',
            'The entire actual core in B_(D/2) and |z|<=actual Z, and the phase-zero full active core in |y|<=.85',
            'True central points (+/-Aq,0,0), Aq>=1.28, and phase interval including pi/2',
            'The phase-zero whole core excludes the actual ball centered at (0,Aq,0) of radius D/5',
            'If deleting exact central cylinder, actual translated whole-core position/held/opposite-half conditions are paid anew',
        ],
        actual_core_solved=False, strong_target_completed=False,
    )


def limited_budget_floor():
    """Necessary failure at D<=3.05 only for the stated R168 sufficient proof.

    The proof requires h_Z>=b, hence h>=b. The weak ball/marker conditions
    then force F(D)>0. This is not a general geometric nonexistence result.
    """
    A, W, e = (COMMON[k] for k in ('A','slab','epsilon'))
    Dlo, Dhi = 2*A, Q(61,20)
    R0 = Q(3,100)*Dhi
    b0 = W+Dhi/20+e
    c_lower_at_Dhi = Q(12,25)
    F_upper = (Dhi/2-R0-e)**2-c_lower_at_Dhi**2-(b0-R0)**2-b0**2
    sqrt_lower = Q(3,4)
    sqrt_margin = A*A-b0*b0-sqrt_lower**2
    c_lower_margin = (A-c_lower_at_Dhi)**2-(A*A-b0*b0)
    derivative_lower = Q(109,250)*Dlo-Q(47,50)*e-Q(7,50)*(W+e)-2*A*b0/(20*sqrt_lower)
    assert sqrt_margin>0 and c_lower_margin>0 and derivative_lower>0 and F_upper<0
    return dict(
        scope='Only the original origin-ball plus h_Z>=b four-corner sufficient budget at fixed A_min=1.28 and W=.85; other caps or marker proofs are not excluded.',
        necessary_lower_D_from_core_ball=record(Dlo),
        ruled_out_budget_D_upper=record(Dhi),
        limiting_definitions=dict(R0='.03 D',b0='.85+.05 D+.0001',
            c0='1.28-sqrt(1.28^2-b0^2)',
            F='(.47 D-epsilon)^2-c0^2-(b0-.03 D)^2-b0^2'),
        monotonic_interval=[record(Dlo),record(Dhi)],
        exact_derivative_lower=record(derivative_lower),
        exact_sqrt_lower=record(sqrt_lower),
        exact_sqrt_margin=record(sqrt_margin),
        exact_c_lower_at_Dhi=record(c_lower_at_Dhi),
        exact_c_lower_margin=record(c_lower_margin),
        exact_F_upper_at_Dhi=record(F_upper),
        general_surface_nonexistence_claim=False,
        exact_optimal_D_claim=False,
    )


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh exact-budget report')
    start=time.perf_counter()
    report=dict(schema='fd2d-further-smaller-complete-caps-rational-budget-v1',
        theorem='R179',
        source_sha256=sha(__file__),parent_R168_budget_source_sha256=sha(parent.__file__),
        common_parameters={k:record(v) for k,v in COMMON.items()},
        variants=[cap_budget(name,U) for name in VARIANTS for U in (Q(6,5),Q(3,2))],
        sufficient_budget_floor=limited_budget_floor(),
        all_arithmetic_certificates_rational=True,
        body_or_BVP_runs=0,solver_or_saved_field_mutations=0)
    report['elapsed_seconds']=time.perf_counter()-start
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(report=str(args.out),passed=True,
        variants=[dict(name=v['variant'],U=v['values']['tail_function_upper']['exact'],
            Z=[v['values']['actual_Z_lower']['exact'],v['values']['actual_Z_upper']['exact']],
            held=v['values']['held_radius']['exact']) for v in report['variants']],
        budget_floor_F_upper=report['sufficient_budget_floor']['exact_F_upper_at_Dhi']['exact'],
        elapsed_seconds=report['elapsed_seconds'])),flush=True)
    return 0


if __name__=='__main__':
    raise SystemExit(main())

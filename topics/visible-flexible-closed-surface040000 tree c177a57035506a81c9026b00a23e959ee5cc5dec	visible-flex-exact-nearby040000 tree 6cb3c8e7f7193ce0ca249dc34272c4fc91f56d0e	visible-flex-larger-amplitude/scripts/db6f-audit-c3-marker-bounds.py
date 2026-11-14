#!/usr/bin/env python3
"""Exact fixed N=7,r=3/20 width and fixed-marker budgets.

Only Fraction polynomial identities and integer square-root enclosures.
No actual candidate, nonlinear solve, LP, angular sampling or optimization.
"""
import argparse
from fractions import Fraction as Q
from math import comb, isqrt
from pathlib import Path
import hashlib
import json


def encode(x):
    if isinstance(x,Q):
        return {'numerator':str(x.numerator),'denominator':str(x.denominator)}
    if isinstance(x,dict):
        return {k:encode(v) for k,v in x.items()}
    if isinstance(x,list):
        return [encode(v) for v in x]
    return x


def decimal_floor(x,places=14):
    scale=10**places
    n=(x.numerator*scale)//x.denominator
    sign='-' if n<0 else ''
    a=abs(n)
    return sign+str(a//scale)+'.'+str(a%scale).zfill(places)


def sqrt_box(x,bits=120):
    assert x>=0
    scale=1<<bits
    n=isqrt((x.numerator*scale*scale)//x.denominator)
    lo=Q(n,scale)
    hi=lo if lo*lo==x else Q(n+1,scale)
    assert lo*lo<=x<=hi*hi
    return lo,hi


def chebyshev(degree):
    t=[[Q(1)],[Q(0),Q(1)]]
    for k in range(2,degree+1):
        p=[Q(0)]*(k+1)
        for j,v in enumerate(t[-1]):
            p[j+1]+=2*v
        for j,v in enumerate(t[-2]):
            p[j]-=v
        t.append(p)
    return t[:degree+1]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    topic=Path(__file__).resolve().parents[1]
    source_specs={
      'results/R28-finite-positive-c3-core-and-conditional-held-transfer.md':
        '663d67283aaffe49169af3eb5b74c67e0c70e6c4bbd6d7894b7fa863654bca00',
      'results/R29-c3-mechanism-interface-and-convex-held-envelope.md':
        'a4274cb2f6a931b59c7af94945d91eb1e74610fe6d511bfbadae8ae131ab82c1',
      'results/R31-finite-rational-support-certificate-completeness.md':
        'a1a9e6e2a4aa647de805b98de40703c31233de25d96200f80c9c2a9f5a2a3a90'
    }
    sources=[]
    for rel,want in source_specs.items():
        data=(topic/rel).read_bytes()
        assert hashlib.sha256(data).hexdigest()==want
        sources.append({'path':rel,'bytes':len(data),'sha256':want})
    n=7;r=Q(3,20)
    a={k:Q(n+1-abs(k),n+1) for k in range(-n,n+1)}
    c={j:sum((a.get(k,Q(0))*a.get(j-k,Q(0))
              for k in range(-n,n+1)),Q(0)) for j in range(2*n+1)}
    assert c[0]==Q(43,8)
    b={j:c[j]/c[0] for j in range(1,2*n+1)}
    assert all(0<v<1 for v in b.values())
    ts=chebyshev(n)
    p=[sum((b[2*k]*ts[k][j]/(36*k*k-1)
            for k in range(1,n+1) if j<len(ts[k])),Q(0))
       for j in range(n+1)]
    derivative=[Q(j+1)*p[j+1] for j in range(n)]
    # P'(-1+2u), degree 6, as a power polynomial.
    power=[Q(2**j)*sum((derivative[k]*comb(k,j)*(-1)**(k-j)
             for k in range(j,len(derivative))),Q(0))
           for j in range(len(derivative))]
    degree=len(power)-1
    bern=[sum((power[j]*Q(comb(i,j),comb(degree,j))
               for j in range(i+1)),Q(0)) for i in range(degree+1)]
    # Independent exact expansion of the Bernstein representation.
    reconstructed=[Q(0)]*(degree+1)
    for i,beta in enumerate(bern):
        for j in range(degree-i+1):
            reconstructed[i+j]+=beta*comb(degree,i)*comb(degree-i,j)*(-1)**j
    assert reconstructed==power
    assert len(bern)==7 and all(v>Q(1,100) for v in bern)
    diameter=2-4*(1-r)*sum((b[2*k]*(-1)**k/(36*k*k-1)
                             for k in range(1,n+1)),Q(0))
    coarse=2+4*(1-r)*sum((b[2*k]/(36*k*k-1)
                           for k in range(1,n+1)),Q(0))
    delta=4*(1-r)*sum((b[j]/(9*j*j-1)
                       for j in range(1,2*n+1,2)),Q(0))
    H=1+2*(1-r)*sum(((-1)**(j+1)*b[j]/(9*j*j-1)
                       for j in range(1,2*n+1)),Q(0))
    hmin=H-delta
    assert 2*H==4+delta-coarse
    assert coarse>diameter>2 and H>1 and hmin>=Q(23,40)
    Rbound=Q(57,40)

    def marker_case(name,z,halfheight,rad,e0,e1,d):
        assert z>=halfheight>=0 and rad>=0 and e0>=0 and e1>=0
        Z=z+halfheight
        L2=4*H*H+Z*Z
        U2=d*d+Z*Z
        Llo,Lhi=sqrt_box(L2)
        Ulo,Uhi=sqrt_box(U2)
        assert rad<=Ulo
        core_diam2=d*d+4*halfheight*halfheight
        assert core_diam2<=U2
        room=9*Llo-10*Uhi
        used=rad+18*e0+20*e1
        margin=room-used
        assert margin>0
        lower=Llo+rad-2*e0
        upper=Uhi+rad+2*e1
        assert lower>0 and upper<Q(9,10)*lower
        ratio=(lower-upper)/(2*lower)
        initial_cross2=(Rbound+H)**2+Z*Z
        _,initial_cross_hi=sqrt_box(initial_cross2)
        _,core_hi=sqrt_box(core_diam2)
        initial_up=max(core_hi,2*rad,initial_cross_hi+rad)+2*e0
        return {
          'name':name,'z':z,'core_halfheight':halfheight,'marker_radius':rad,
          'epsilon0':e0,'epsilon1':e1,'core_diameter_used':d,
          'L0_squared':L2,'U1_squared':U2,
          'L0_lower':Llo,'L0_upper':Lhi,'U1_lower':Ulo,'U1_upper':Uhi,
          'sqrt_boxes_verified_by_exact_squares':True,
          'diameter_cases':{'core_core_squared':core_diam2,
              'marker_marker_upper':2*rad,'core_marker_upper':Uhi+rad},
          'all_final_diameter_cases_bounded_by_U1_plus_a':True,
          'thickness_budget_lower':room,'budget_consumption':used,
          'strict_budget_margin':margin,
          'actual_initial_diameter_lower_after_error':lower,
          'actual_final_diameter_upper_after_error':upper,
          'rigid_quotient_ratio_lower':ratio,
          'ratio_lower_decimal_down':decimal_floor(ratio),
          'complete_initial_diameter_upper_from_R29_ball_bound':initial_up,
          'one_twentieth_gate_pass':True
        }

    models=[
      marker_case('coarse_point_z_1_5',Q(1,5),Q(0),Q(0),Q(0),Q(0),coarse),
      marker_case('sharp_point_z_4_5',Q(4,5),Q(0),Q(0),Q(0),Q(0),diameter),
      marker_case('sharp_cap_z_3_10_a_2_25',Q(3,10),Q(0),Q(2,25),Q(1,200),Q(1,200),diameter),
      marker_case('sharp_cap_z_2_5_a_1_10',Q(2,5),Q(0),Q(1,10),Q(1,200),Q(1,200),diameter),
      marker_case('positive_band_cap_z_2_5_a_1_10',Q(2,5),Q(1,100),Q(1,10),Q(1,200),Q(1,200),diameter)
    ]
    final=models[-1]
    Dstar=Q(11,4);fixed_disk_radius=Q(3,10);rho_target=Q(3,100)*Dstar
    assert final['complete_initial_diameter_upper_from_R29_ball_bound']<Dstar
    assert 2*fixed_disk_radius>Q(1,5)*Dstar
    assert fixed_disk_radius<Q(23,40)
    assert r>rho_target and final['marker_radius']>rho_target
    gap_z=final['z']-final['marker_radius']-final['core_halfheight']
    gap_disk=Q(23,40)-fixed_disk_radius
    assert gap_z>2*rho_target and gap_disk>2*rho_target

    # Four-vertex triangular-core comparison, not a smooth surface.
    tetra_L2=Q(17,4);tetra_U2=Q(13,4)
    tetra_margin=Q(81,100)*tetra_L2-tetra_U2
    assert tetra_margin==Q(77,400)>0

    result={
      'status':'EXACT_FINITE_C3_WIDTH_AND_CONDITIONAL_FIXED_MARKER_BUDGETS',
      'scope':'Geometric compact-set/convex-hull models and sufficient bounds only; no connected closed isometric family.',
      'source_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'sources':sources,'N':n,'r':r,'c0':c[0],
      'b_j':[b[j] for j in range(1,2*n+1)],
      'P_power_coefficients':p,
      'P_derivative_power_coefficients':derivative,
      'P_derivative_at_minus1_plus_2u_power_coefficients':power,
      'bernstein_degree':degree,
      'bernstein_coefficients':bern,
      'bernstein_reexpanded_identity_exact':True,
      'all_bernstein_coefficients_gt_one_hundredth':True,
      'exact_core_diameter':diameter,
      'coarse_core_diameter_bound':coarse,
      'halfphase_support_gap':delta,'H_support_value':H,'h_min':hmin,
      'H_identity_uses_coarse_bound_not_exact_diameter':True,
      'decimal_displays_down':{'diameter':decimal_floor(diameter),
        'coarse_bound':decimal_floor(coarse),'H':decimal_floor(H),
        'Delta':decimal_floor(delta),'bernstein_min':decimal_floor(min(bern))},
      'marker_models':models,
      'additional_size_compatibility_only':{
        'Dstar':Dstar,'fixed_disk_radius':fixed_disk_radius,
        'fixed_disk_diameter':2*fixed_disk_radius,
        'README_grip_diameter_required_at_Dstar':Dstar/5,
        'README_reach_target_at_Dstar':rho_target,
        'core_curvature_radius_lower':r,
        'spherical_marker_curvature_radius':final['marker_radius'],
        'marker_to_band_vertical_gap_lower':gap_z,
        'disk_to_core_horizontal_gap_lower':gap_disk,
        'local_radius_and_separation_budget_only':True,
        'whole_closed_surface_reach_proved':False,
        'fixed_material_H_constructed':False
      },
      'finite_four_vertex_model':{
        'core':'equilateral unit-radius triangle in z=0',
        'fixed_point':['-1','0','1/2'],
        'initial_diameter_squared':tetra_L2,
        'halfphase_diameter_squared':tetra_U2,
        'strict_squared_one_twentieth_margin':tetra_margin,
        'not_a_smooth_surface':True
      },
      'new_solver_or_optimizer_calls':0,
      'actual_candidate_data_read':False,
      'closed_surface_or_common_metric_constructed':False
    }
    out=Path(args.out).resolve();assert not out.exists()
    with out.open('x',encoding='utf-8') as f:
        f.write(json.dumps(encode(result),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],
       'diameter_decimal_down':decimal_floor(diameter),
       'positive_Bernstein_count':len(bern),
       'positive_band_ratio_lower_decimal_down':final['ratio_lower_decimal_down'],
       'report_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
       'bytes':out.stat().st_size}))


if __name__=='__main__':
    main()

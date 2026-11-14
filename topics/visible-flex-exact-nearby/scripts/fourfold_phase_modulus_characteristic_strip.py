#!/usr/bin/env python3
"""Moving-frame complex-angle modulus gate for the exact R57 control box.

The real radial cells and infinite-primitive bounds come from the completed
R57 certificate. Only theta is complex. This is a coefficient-domain gate,
not a validated flow or conjugacy. Rebuilt after the executor loss; old
partial numerical results are not imported. All scalar budgets are outward.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_interval_scalar import interval_exp
from fourfold_phase_characteristic_strip import product, total
from fourfold_phase_core_N_interval import CoreNGate, ClosedSpanSplineBox
from fourfold_phase_root_interval import Box, interval_dot
from fourfold_phase_uniform_tail import (
    exact_iv, endpoint_up, exp_up, weighted_sum_up, mul_up,
    power_up, derivative_coefficients, down, up,
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def hyperbolic_weights(width, modes):
    lo, hi, sinh = [], [], []
    for frequency in 4*np.arange(1, modes+1):
        v=exact_iv(width)*int(frequency)
        ep,em=interval_exp(v),interval_exp(-v)
        c=(ep+em)/2
        lo.append(-endpoint_up(-c));hi.append(endpoint_up(c))
        sinh.append(endpoint_up((ep-em)/2))
    return Box(np.asarray(lo),np.asarray(hi)),np.asarray(sinh)


def quotient_bounds(f0,f1,f2,n1,n2,denominator):
    inv=float((Box(1)/Box(denominator)).hi)
    return [product(f0,inv),
            total(product(f1,inv),product(f0,n1,inv,inv)),
            total(product(f2,inv),product(2.,f1,n1,inv,inv),
                  product(f0,n2,inv,inv),product(2.,f0,n1,n1,inv,inv,inv))]


def strip_cell(beta,gamma,radius,real,width,weights,gate):
    """Uniform over one exact real radial cell and its whole control box."""
    b,g=beta.abs_upper(),gamma.abs_upper()
    frequency=4*np.arange(1,b.shape[-1]+1)
    cosh_box,sinh=weights;cosh=cosh_box.hi
    def moment(values,radial,order):
        return float(weighted_sum_up(values[radial],mul_up(power_up(frequency,order),cosh)))
    Iphi=total(width,weighted_sum_up(b[0],sinh))
    Igamma=float(weighted_sum_up(g[0],sinh))
    Gamma=moment(g,0,0)
    ef=float(exp_up(Iphi));c=float(exp_up(Igamma));s=product(Gamma,c)
    P,P1,P2=total(1.,moment(b,0,1)),moment(b,0,2),moment(b,0,3)
    u,u1,u2=moment(g,0,1),moment(g,0,2),moment(g,0,3)
    p,p1,p2=moment(b,1,0),moment(b,1,1),moment(b,1,2)
    q,q1,q2=moment(g,1,0),moment(g,1,1),moment(g,1,2)
    a,ap=float(radius[0].abs_upper()),float(radius[1].abs_upper())
    alo=float(radius.lo[0])
    hx1=product(ef,total(product(ap,c),product(a,p,c),product(a,q,s)))
    zx1=total(product(ap,s),product(a,q,c))
    hv=product(total(real['Fx_horizontal_upper'],product(width,hx1)),ef)
    z=total(real['Fx_z_abs_upper'],product(width,zx1))
    Q=total(product(c,z),product(s,hv))
    R=total(product(c,hv),product(s,z))
    Q1=total(product(a,q),product(P,s,hv),product(u,R))
    R1=total(ap,product(P,c,hv),product(u,Q))
    v1=total(product(a,p,c),product(P,hv))
    h1=total(product(ap,c),product(a,q,s),product(P,hv))
    Q2=total(product(a,q1),product(total(product(P1,s),product(P,u,c)),hv),
             product(P,s,v1),product(u1,R),product(u,R1))
    v2=total(product(a,total(product(p1,c),product(p,u,s))),
             product(P1,hv),product(P,h1))

    # n=-a^2 D, D=P*c*Q-u*v. Exact theta identities appear in R59.
    A=total(product(P1,c),product(2.,P,u,s))
    A1=total(product(P2,c),product(3.,P1,u,s),product(2.,P,u1,s),
             product(2.,P,u,u,c))
    B=total(product(P,q),product(u,p))
    B1=total(product(P1,q),product(P,q1),product(u1,p),product(u,p1))
    C=total(product(P,P,c,s),u1)
    C1=total(product(2.,P,P1,c,s),product(P,P,total(product(c,c),product(s,s)),u),u2)
    n1=product(a,a,total(product(A,Q),product(a,c,B),product(C,hv)))
    n2=product(a,a,total(product(A1,Q),product(A,Q1),
                product(a,total(product(s,u,B),product(c,B1))),
                product(C1,hv),product(C,v1)))
    old_re_upper=float((Box(-real['raw_minus_n_lower'])+Box(product(.5,width,width,n2))).hi)

    # Boundary Re P is computed with interval cosh, including signed beta.
    # Periodic harmonic minimum then covers the entire intervening strip.
    boundary=interval_dot(gate.cosine,(beta[0]*frequency*cosh_box).reshape(-1,1))
    Plo=float((Box(1)+Box(float(boundary.lo.min()))-Box(product(float(gate.half_gap),P1))).lo)
    clo=float((Box(1)-Box(Gamma)*Gamma/2).lo)
    z2=total(product(ap,u,c),product(a,q1,c),product(a,q,u,s))
    zlo=float((Box(real['Fx_z_lower'])-Box(product(.5,width,width,z2))).lo)
    # This is a MODULUS lower bound for Q=c*z-s*h, not a Re Q claim.
    Qlo=float((Box(clo)*zlo-Box(product(s,hv))).lo)
    positive=bool(Plo>0 and clo>0 and zlo>0 and Qlo>0 and alo>0)
    Dlo=float((Box(Plo)*clo*Qlo-Box(product(u,hv))).lo) if positive else 0.
    modulus=float((Box(alo)*alo*Dlo).lo) if positive and Dlo>0 else 0.
    old_modulus=float(down(-old_re_upper)) if old_re_upper<0 else 0.
    den=max(modulus,old_modulus)
    row=dict(radial_interval=real['interval'],passed=bool(den>0),
        P_real_part_lower=Plo,cos_gamma_real_part_lower=clo,
        Fx_z_real_part_lower=zlo,normal_component_modulus_lower=Qlo,
        moving_factor_modulus_lower=Dlo,positive_multiplier_conditions=positive,
        moving_frame_Nraw_modulus_lower=modulus,Nraw_modulus_lower=den,
        old_second_order_Nraw_real_part_upper=old_re_upper,
        real_Nraw_upper=-real['raw_minus_n_lower'],radius_lower=alo,radius_upper=a,
        imaginary_phi_upper=Iphi,imaginary_gamma_upper=Igamma,gamma_abs_upper=Gamma,
        frame_projection_upper=hv,Fx_z_strip_abs_upper=z,
        P_derivative_bounds=[P,P1,P2],u_derivative_bounds=[u,u1,u2],
        p_derivative_bounds=[p,p1,p2],q_derivative_bounds=[q,q1,q2],
        Q_derivative_bounds=[Q,Q1,Q2],v_derivative_bounds=[hv,v1,v2],
        Nraw_derivative_bounds=[product(a,a,total(product(P,c,Q),product(u,hv))),n1,n2])

    # M=p*c*Q-q*v; its first derivative is AM*Q+c*B*R-CM*v.
    MA=total(product(p1,c),product(total(product(p,u),product(q,P)),s))
    MA1=total(product(p2,c),
        product(total(product(2.,p1,u),product(p,u1),product(q1,P),product(q,P1)),s),
        product(total(product(p,u),product(q,P)),u,c))
    MC=total(product(p,P,c,s),q1)
    MC1=total(product(total(product(p1,P),product(p,P1)),c,s),
              product(p,P,total(product(c,c),product(s,s)),u),q2)
    m0=product(a,a,total(product(p,c,Q),product(q,hv)))
    m1=product(a,a,total(product(MA,Q),product(c,B,R),product(MC,hv)))
    m2=product(a,a,total(product(MA1,Q),product(MA,Q1),
        product(total(product(s,u,B),product(c,B1)),R),product(c,B,R1),
        product(MC1,hv),product(MC,v1)))
    g0=product(a,a,total(product(Q,Q),product(hv,hv)))
    g1=product(2.,a,a,total(product(a,total(product(q,Q),product(p,c,hv))),
                           product(R,total(product(u,Q),product(P,c,hv)))))
    g2=product(2.,a,a,total(product(Q1,Q1),product(Q,Q2),product(v1,v1),product(hv,v2)))
    row.update(Mraw_derivative_bounds=[m0,m1,m2],G_derivative_bounds=[g0,g1,g2])
    if den>0:
        row.update(drift_derivative_bounds=quotient_bounds(m0,m1,m2,n1,n2,den),
                   wave_factor_derivative_bounds=quotient_bounds(g0,g1,g2,n1,n2,den))
    return row


def read_report(path):
    data=gzip.decompress(path.read_bytes()) if path.suffix=='.gz' else path.read_bytes()
    return json.loads(data)


def write_report(path,report):
    raw=(json.dumps(report,indent=2)+'\n').encode()
    if len(raw)>1_000_000 and path.suffix!='.gz':
        raise ValueError('data larger than 1MB requires a .gz output path')
    data=gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw
    if len(data)>5_000_000:raise ValueError('split the report below the per-file limit')
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.tmp');temporary.write_bytes(data);temporary.replace(path)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--direction',type=Path,required=True)
    ap.add_argument('--real-certificate',type=Path,required=True)
    ap.add_argument('--width',type=float,default=1/64)
    ap.add_argument('--indices',help='comma-separated probe indices; omitted means full coverage')
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--resume',action='store_true')
    args=ap.parse_args()
    if not 0<args.width<=.02:raise ValueError('physical theta strip must lie in (0,.02]')
    real=read_report(args.real_certificate)
    if (real['kind']!='directed_uniform_real_parameter_N_tube_for_explicit_symmetric_R33_family'
        or real['status']!='complete' or not real['uniform_parameter_N_negative_proved']
        or real['failures'] or real['pending']):
        raise ValueError('completed R57 real independent-control-box certificate required')
    if sha(args.inputs)!=real['origin_inputs_sha256'] or sha(args.direction)!=real['frozen_direction_sha256']:
        raise ValueError('input/direction does not match the exact R57 object')
    with np.load(args.inputs,allow_pickle=False) as z:frozen={k:z[k].copy() for k in z.files}
    with np.load(args.direction,allow_pickle=False) as z:direction={k:z[k].copy() for k in z.files}
    if json.loads(str(direction['metadata']))['origin_inputs_sha256']!=sha(args.inputs):
        raise ValueError('direction origin mismatch')
    gate=CoreNGate(frozen,real['quarter_nodes'],real['angular_nodes'])
    delta=Box(*real['exact_parameter_interval'])
    raw=Box(frozen['phase_coefficients'])+delta*direction['phase_direction_coefficients']
    phase=ClosedSpanSplineBox.__new__(ClosedSpanSplineBox);phase.states=[]
    t,k,lo,hi=frozen['phase_knots'],5,raw.lo,raw.hi
    for order in range(6):
        phase.states.append((t,k,lo,hi))
        if order<5:t,k,lo,hi=derivative_coefficients(t,k,lo,hi)
    gate.target.phase=phase
    gate.target.alpha=[Box(a)+delta*d for a,d in zip(frozen['alpha'],direction['alpha_direction'])]
    cells=sorted(real['rows'],key=lambda row:row['interval'][0])
    if (cells[0]['interval'][0]!=0 or cells[-1]['interval'][1]!=real['core'][1]
        or any(x['interval'][1]!=y['interval'][0] for x,y in zip(cells,cells[1:]))):
        raise ValueError('exact dyadic closed-cell coverage gap')
    requested=list(range(len(cells))) if args.indices is None else [int(v) for v in args.indices.split(',')]
    if requested!=sorted(set(requested)) or any(i<0 or i>=len(cells) for i in requested):
        raise ValueError('indices must be sorted, unique and valid')
    common=dict(kind='continuous_moving_frame_modulus_gate_on_R57_independent_control_box',
        origin_inputs_sha256=sha(args.inputs),frozen_direction_sha256=sha(args.direction),
        real_certificate_sha256=sha(args.real_certificate),source_sha256=sha(__file__),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ['fourfold_phase_characteristic_strip.py','fourfold_phase_core_N_interval.py',
             'fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']},
        radial_core=real['core'],exact_parameter_interval=real['exact_parameter_interval'],
        angular_strip_width=args.width,angular_coordinate='physical theta; normalized x=4theta width is four times this',
        requested_indices=requested,total_real_cells=len(cells),
        limitations=['Modulus nonzero claim, not Re Nraw<0 from the moving-frame gate',
            'Only theta is complex; radial variables and the whole independent control box are real',
            'Actual infinite R33 graph and primitive certificate, no rounded affine-vector substitution',
            'No validated return map, Wiener residual, parameter flow jets or full PDE solution'])
    rows=[]
    if args.resume and args.out.exists():
        old=read_report(args.out)
        for key,value in common.items():
            if old.get(key)!=value:raise ValueError('resume mismatch: '+key)
        rows=old['cells']
        if [r['cell_index'] for r in rows]!=requested[:len(rows)]:raise ValueError('non-prefix saved coverage')
    weights=hyperbolic_weights(args.width,gate.target.modes)
    def save():
        complete=len(rows)==len(requested)
        coverage=complete and requested==list(range(len(cells)))
        report=dict(**common,status='complete' if complete else 'running',cells=rows,
                    cell_count=len(rows),complete_radial_coverage=coverage,
                    all_passed=all(r['passed'] for r in rows),
                    proved_uniform_denominator_nonzero=bool(coverage and all(r['passed'] for r in rows)))
        if rows:
            report.update(minimum_Nraw_modulus_lower=min(r['Nraw_modulus_lower'] for r in rows),
                maximum_old_second_order_Nraw_real_part_upper=max(r['old_second_order_Nraw_real_part_upper'] for r in rows))
            if all(r['passed'] for r in rows):
                for field in ['drift_derivative_bounds','wave_factor_derivative_bounds']:
                    report['maximum_'+field]=[max(r[field][j] for r in rows) for j in range(3)]
        write_report(args.out,report)
        return report
    for i in requested[len(rows):]:
        beta,gamma,radius,slope=gate.target.scalars(Box(*cells[i]['interval']))
        row=strip_cell(beta,gamma,radius,cells[i],args.width,weights,gate)
        row['cell_index']=i;rows.append(row)
        if len(rows)%25==0:
            save()
            print(json.dumps(dict(covered=len(rows),total=len(requested),failed=sum(not r['passed'] for r in rows))),flush=True)
    report=save()
    print(json.dumps({k:v for k,v in report.items() if k not in ['cells','requested_indices']},indent=2),flush=True)
    if not report['all_passed']:raise SystemExit('preserved complex-angle gate failures')


if __name__=='__main__':main()

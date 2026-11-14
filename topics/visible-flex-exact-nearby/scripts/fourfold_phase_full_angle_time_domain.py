#!/usr/bin/env python3
"""Whole physical-angle strip and complex-time domain for exact affine germs.

R59 supplies a real-radius strip lower bound for the same D=-n/a^2.  A
Fourier/time enclosure bounds each analytic germ away from an anchor in its
actual closed span.  Both Fourier alias/truncation and full time tails are
paid before dividing by D or selecting sqrt(-K).  Every required germ is
included; extending a germ is never identified with the actual off-span field.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,acb,ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_field_time_refined_root import prepare_refined_root,RefinedGermTimeModel
from fourfold_phase_field_time_germ_union import radial_cover
from fourfold_phase_reference_time_sample import internal_rational_time
from fourfold_phase_time_outer_taylor_gate import coarse_outer_invariants,time_disk_range
from fourfold_phase_uniform_field_time_grid import uniform_primitive
from fourfold_phase_uniform_field_time_grid_fast import uniform_phases,f_invariants


def document(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix=='.gz' else raw)


def hashed(row):
    path=Path(row['path'])
    if sha(path)!=row['sha256']:raise ValueError('input hash mismatch: '+str(path))
    return path,document(path)


def fraction_endpoint(value):
    return Fraction(str(value.fmpq()))


def frame_membership(obj,r59,delta):
    if (not r59.get('proved_uniform_denominator_nonzero')
        or not r59['complete_radial_coverage'] or not r59['all_passed']
        or r59['origin_inputs_sha256']!=obj['origin_inputs']['sha256']
        or r59['frozen_direction_sha256']!=obj['direction']['sha256']):
        raise ValueError('R59 certificate belongs to a different or incomplete control box')
    lo,hi=map(Fraction.from_float,r59['exact_parameter_interval'])
    if not lo<=delta<=hi:raise ValueError('exact affine parameter leaves R59 independent box')
    cells=r59['cells']
    if (not cells or cells[0]['radial_interval'][0]!=0
        or cells[-1]['radial_interval'][1]!=r59['radial_core'][1]
        or any(a['radial_interval'][1]!=b['radial_interval'][0] for a,b in zip(cells,cells[1:]))):
        raise ValueError('R59 closed radial coverage has a gap')
    return dict(exact_delta=str(delta),exact_control_parameter_interval=[str(lo),str(hi)],
                exact_parameter_membership=True,D_identity='D=-Nraw/a^2; same phase-frame convention',
                interpretation='the exact affine curve is a subset of the certified independent control box')


def real_anchor(model,r59):
    """Anchor at an actual point of this germ, never at an off-span center."""
    left,right=model.cell
    center_lo,center_hi=map(fraction_endpoint,[model.center.lower(),model.center.upper()])
    if left<=center_lo and center_hi<=right:
        radial_interval=(center_lo,center_hi);u=arb(0);anchor=None
    else:
        center=(center_lo+center_hi)/2
        anchor=min(max(center,left),right)
        radial_interval=(anchor,anchor)
        u=((exact_arb(anchor)/model.root).asin()-model.tau0)/model.h
    lo,hi=radial_interval
    if lo<0 or hi>Fraction.from_float(r59['radial_core'][1]):
        raise ValueError('this positive-side anchor leaves the proved R59 radial core')
    rows=[row for row in r59['cells'] if Fraction.from_float(row['radial_interval'][0])<=hi
          and Fraction.from_float(row['radial_interval'][1])>=lo]
    if (not rows or Fraction.from_float(rows[0]['radial_interval'][0])>lo
        or Fraction.from_float(rows[-1]['radial_interval'][1])<hi):
        raise ValueError('R59 rows do not cover the complete real anchor')
    lowers=[]
    for row in rows:
        raw=(arb(float(row['Nraw_modulus_lower']))/arb(float(row['radius_upper']))**2).lower()
        direct=arb(float(row['moving_factor_modulus_lower'])) if row['positive_multiplier_conditions'] else arb(0)
        lowers.append(max(raw,direct).lower())
    lower=min(lowers).lower()
    if not lower>0:raise ValueError('real-anchor strip D lower bound is not positive')
    return u,lower,dict(radial_interval=list(map(str,radial_interval)),
        exact_radial_anchor=None if anchor is None else str(anchor),
        center_is_an_actual_germ_point=anchor is None,u_anchor=ball_record(u),
        R59_cell_indices=[row['cell_index'] for row in rows],D_anchor_lower=ball_record(lower))


def fourier_fee(N,K,wide,narrow):
    """Full error per unit strip modulus: retained aliases plus omitted modes."""
    if not 0<=K<N//2 or not wide>narrow>=0:raise ValueError('invalid Fourier parameters')
    denominator=1-(-wide*N).exp();alias=arb(0)
    for k in range(-K,K+1):
        term=(-wide*(N-abs(k))).exp()+(-wide*(N+abs(k))).exp()
        alias+=term/denominator*(narrow*abs(k)).exp()
    tail=2*(-(wide-narrow)*(K+1)).exp()/(1-(-(wide-narrow)).exp())
    return alias.upper(),tail.upper()


def whole_invariants(model,N,K,inner_time,outer_time,narrow,wide):
    """True time coefficients, then rigorous full Fourier norm enclosures."""
    theta=[acb(arb(0,arb.pi()/4),0)]
    narrow_bounds,KM,analytic_K,narrow_info=coarse_outer_invariants(model,theta,outer_time,narrow)
    wide_bounds,_,_,wide_info=coarse_outer_invariants(model,theta,outer_time,wide)
    if not analytic_K:raise ValueError('K is not proved analytic on the larger time disk')
    X,Xfee=uniform_primitive(model,N,Fraction(0));phases=uniform_phases(model,N,Fraction(0))
    values=np.empty((N,3),object)
    for j in range(N):values[j]=f_invariants(X[j],phases[j])
    coeff=model.target.fourier.fft(values)/N
    R,S=exact_arb(inner_time),exact_arb(outer_time)
    angular_inner,angular_outer=4*exact_arb(narrow),4*exact_arb(wide)
    alias,tail=fourier_fee(N,K,angular_outer,angular_inner)
    modes=list(range(K+1))+list(range(N-K,N))
    weights={k:(angular_inner*abs(k if k<N//2 else k-N)).exp() for k in modes}
    norms=[]
    for component,name in enumerate(['D','M','W']):
        retained=[];full=[]
        for i in range(model.precision):
            finite=sum((abs(coeff[k,component][i])*weights[k] for k in modes),arb(0)).upper()
            fee=(wide_bounds[name]*(alias+tail)/S**i).upper()
            retained.append(finite);full.append((finite+fee).upper())
        time_tail=(narrow_bounds[name]*(R/S)**model.precision/(1-R/S)).upper()
        modulus=(sum((value*R**i for i,value in enumerate(full)),arb(0))+time_tail).upper()
        norms.append(dict(name=name,full=full,retained=retained,time_tail=time_tail,modulus=modulus,
                          wide_modulus=wide_bounds[name],narrow_modulus=narrow_bounds[name]))
    Krange,Ktail=time_disk_range(model.K,R,S,KM)
    return norms,Krange,dict(primitive_infinite_error=ball_record(Xfee),
        Fourier_alias_per_unit_modulus=ball_record(alias),Fourier_omitted_per_unit_modulus=ball_record(tail),
        coarse_narrow_domain={k:ball_record(v) for k,v in narrow_info.items()},
        coarse_wide_domain={k:ball_record(v) for k,v in wide_info.items()},
        K_larger_time_modulus=ball_record(KM),K_time_tail=ball_record(Ktail)),narrow_bounds


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--retarget',type=Path,required=True);p.add_argument('--leg',choices=['forward','backward'],default='forward')
    p.add_argument('--segment',type=int,default=419);p.add_argument('--sub-left',default='0');p.add_argument('--sub-right',default='1')
    p.add_argument('--R59',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_parameter_modulus_complex_angle_1over64.json.gz'))
    p.add_argument('--time-radius',default='3');p.add_argument('--larger-time-radius',default='4')
    p.add_argument('--theta-strip',default='1/64');p.add_argument('--wider-theta-strip',default='1/32')
    p.add_argument('--time-order',type=int,default=40);p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--cutoff',type=int,default=255);p.add_argument('--primitive-nodes',type=int,default=512)
    p.add_argument('--bits',type=int,default=192);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();started=time.monotonic();ctx.prec=args.bits;ctx.cap=max(21,args.time_order+4)
    desc=document(args.retarget)
    op,obj=hashed(desc['target_object']);rp,root=hashed(desc['target_root'])
    gp,grid=hashed(desc['old_'+args.leg+'_reference']);r59=document(args.R59)
    delta=Fraction(int(obj['delta_fraction']['numerator']),int(obj['delta_fraction']['denominator']))
    membership=frame_membership(obj,r59,delta)
    narrow,wide=Fraction(args.theta_strip),Fraction(args.wider_theta_strip)
    R,S=Fraction(args.time_radius),Fraction(args.larger_time_radius)
    if not 0<narrow<=Fraction.from_float(r59['angular_strip_width']) or not wide>narrow or not S>R>1:
        raise ValueError('invalid strip or time radii')
    ta,tb=map(internal_rational_time,grid['exact_time_endpoints'][args.segment:args.segment+2])
    l,r=Fraction(args.sub_left),Fraction(args.sub_right)
    if not 0<=l<r<=1:raise ValueError('invalid exact reference subspan')
    a,b=ta+(tb-ta)*l,ta+(tb-ta)*r;c,h=(a+b)/2,(b-a)/2
    package=prepare_refined_root(op,rp,nodes=args.primitive_nodes)
    # A first model supplies the finite union; enumerate before constructing
    # the explicit germs because an ordinary one-cell constructor must reject
    # a complete segment that actually crosses a knot.
    from fourfold_phase_beta_affine import AffineBulkTarget
    target=AffineBulkTarget(op,args.primitive_nodes,args.primitive_nodes,Fraction(3,1000),Fraction(1,400),Fraction(8,25))
    radial,radial_interval,cells,crossed=radial_cover(target,package.root,c,h)
    dependencies=['fourfold_phase_field_time_refined_root.py','fourfold_phase_field_time_germ_union.py',
        'fourfold_phase_time_outer_taylor_gate.py','fourfold_phase_uniform_field_time_grid.py',
        'fourfold_phase_uniform_field_time_grid_fast.py','fourfold_phase_beta_interval.py',
        'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_affine.py']
    report=dict(kind='full_physical_angle_strip_complex_time_germ_union_domain',complete=False,
        source_sha256=sha(__file__),dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in dependencies},
        retarget_descriptor_sha256=sha(args.retarget),target_object_sha256=sha(op),target_root_sha256=sha(rp),
        source_time_grid_sha256=sha(gp),source_time_grid_exact_delta=grid['trace_identity']['exact_delta_fraction'],
        exact_delta_fraction=str(delta),R59_sha256=sha(args.R59),membership=membership,
        exact_time_endpoints=list(map(str,[a,b])),leg=args.leg,segment=args.segment,normalized_subspan=[str(l),str(r)],
        time_radius=str(R),larger_time_radius=str(S),physical_theta_strip=str(narrow),wider_physical_theta_strip=str(wide),
        time_order=args.time_order,angles=args.angles,cutoff=args.cutoff,primitive_nodes=args.primitive_nodes,bits=args.bits,
        actual_radial_cover=list(map(str,radial_interval)),required_common_spans=[list(map(str,cell)) for cell in cells],
        strictly_crossed_knots=list(map(str,crossed)),refined_root=package.provenance,germs=[],
        limitations=['This is a full-angle/time coefficient-domain gate, not a reference residual or a true-flow comparison.',
            'Each off-span polynomial extension is only used for the actual portion belonging to its closed span.',
            'The old delta4 reference contributes its time grid only; the target is explicitly delta5.'])
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        raw=(json.dumps(report,indent=2)+'\n').encode()
        if len(raw)>1_000_000 and args.out.suffix!='.gz':raise ValueError('large report requires gzip')
        payload=gzip.compress(raw,mtime=0) if args.out.suffix=='.gz' else raw
        if len(payload)>5_000_000:raise ValueError('split report below 5MB')
        temporary=args.out.with_name(args.out.name+'.tmp');temporary.write_bytes(payload);temporary.replace(args.out)
    save()
    for cell in cells:
        before=time.monotonic()
        model=RefinedGermTimeModel(op,rp,c,h,cell=cell,refined_root=package,nodes=args.primitive_nodes,
            order=args.time_order,outer_radius=R,branch_sign=int(grid['trace_identity']['sign']))
        anchor,base,anchordoc=real_anchor(model,r59)
        alpha=abs(anchor).upper()
        if not alpha<exact_arb(S):raise ValueError('actual germ anchor leaves the larger time disk')
        norms,Krange,fees,coarse=whole_invariants(model,args.angles,args.cutoff,R,S,narrow,wide)
        D=norms[0];Rb,Sb=exact_arb(R),exact_arb(S)
        anchor_tail=(D['narrow_modulus']*(alpha/Sb)**model.precision/(1-alpha/Sb)).upper()
        variation=(sum((D['full'][i]*(Rb**i+alpha**i) for i in range(1,model.precision)),arb(0))
                   +D['time_tail']+anchor_tail).upper()
        lower=(base-variation).lower();Kpositive=(-Krange).real.lower()
        passed=bool(lower>0 and Kpositive>0)
        row=dict(common_span=list(map(str,cell)),anchor=anchordoc,
            full_D_difference_from_actual_anchor=ball_record(variation),D_lower=ball_record(lower),
            minus_K_real_lower=ball_record(Kpositive),K_modulus=ball_record(abs(Krange).upper()),
            time_and_Fourier_fees=fees,passed=passed,
            invariant_bounds={item['name']:dict(
                whole_strip_time_modulus=ball_record(item['modulus']),
                true_time_coefficient_norms=[ball_record(v) for v in item['full']],
                retained_DFT_coefficient_norms=[ball_record(v) for v in item['retained']],
                larger_time_narrow_angle_modulus=ball_record(item['narrow_modulus']),
                larger_time_wide_angle_modulus=ball_record(item['wide_modulus']),
                full_time_tail=ball_record(item['time_tail'])) for item in norms})
        if passed:
            rt=(abs(model.root)*(abs(model.h)*Rb).cosh()).upper();kap=abs(Krange).sqrt().upper()
            M,W=norms[1]['modulus'],norms[2]['modulus']
            field=(rt*(M+kap*W)/lower).upper()
            first=(rt*((coarse['M1']+kap*coarse['W1'])/lower+
                   (M+kap*W)*coarse['D1']/lower**2)).upper()
            second=(rt*((coarse['M2']+kap*coarse['W2'])/lower+
                (2*(coarse['M1']+kap*coarse['W1'])*coarse['D1']+(M+kap*W)*coarse['D2'])/lower**2+
                2*(M+kap*W)*coarse['D1']**2/lower**3)).upper()
            row['true_field_moduli']={k:ball_record(v) for k,v in dict(f=field,f_theta=first,f_theta2=second,r_tau=rt).items()}
        row['elapsed_seconds']=time.monotonic()-before;report['germs'].append(row);save()
        print(json.dumps(dict(cell=list(map(str,cell)),passed=passed,D_lower=str(lower),minus_K_real_lower=str(Kpositive),
                              elapsed_seconds=row['elapsed_seconds'])),flush=True)
    report['complete']=True
    report['complete_common_span_coverage']=len(report['germs'])==len(cells)
    report['proved_full_physical_angle_and_complex_time_domain']=bool(report['complete_common_span_coverage'] and all(row['passed'] for row in report['germs']))
    save();print(json.dumps(dict(complete=True,proved=report['proved_full_physical_angle_and_complex_time_domain'],sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()

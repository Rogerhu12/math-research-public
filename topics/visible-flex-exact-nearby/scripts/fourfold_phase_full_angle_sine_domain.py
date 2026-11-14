#!/usr/bin/env python3
"""Whole-angle time domains including negative radius and exact turns.

Ordinary germs use the exact sine displacement, and the turning collar uses
the separately certified root-deflated Q.  The independent R59 box is only
used at a genuine real anchor, reflected by D(-r,theta)=D(r,theta) if needed.
No incomplete report or failed gate is a flow or conjugacy certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
from types import SimpleNamespace
import time
import numpy as np
from flint import arb,ctx

from fourfold_phase_beta_affine import AffineBulkTarget,sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_field_time_refined_root import prepare_refined_root
from fourfold_phase_field_time_germ_union import radial_cover
from fourfold_phase_field_time_turn_collar import PiTime,TurnCollarTimeModel
from fourfold_phase_time_outer_taylor_gate import time_disk_range
from fourfold_phase_sine_time_geometry import SineGermTimeModel,whole_angle_outer_invariants
from fourfold_phase_full_angle_time_domain import document,hashed,frame_membership,real_anchor,fourier_fee
from fourfold_phase_uniform_field_time_grid import uniform_primitive
from fourfold_phase_uniform_field_time_grid_fast import uniform_phases,f_invariants


def reflected_anchor(model,r59):
    """Only the anchor lower bound is reflected; all actual jets stay original."""
    reflected=bool(model.center.upper()<0)
    if reflected:
        proxy=SimpleNamespace(cell=(-model.cell[1],-model.cell[0]),center=-model.center,
                              root=model.root,tau0=-model.tau0,h=-model.h)
    else:proxy=model
    u,lower,report=real_anchor(proxy,r59)
    report['explicit_radial_reflection_used']=reflected
    report['reflection_identity']='D(-r,theta)=D(r,theta); M odd; W and target K even'
    report['actual_germ_span']=list(map(str,model.cell))
    return u,lower,report


def invariant_enclosures(model,N,K,R,S,narrow,wide):
    bounds,KM,analytic_K,info=whole_angle_outer_invariants(model,S,narrow)
    wide_bounds,_,_,wide_info=whole_angle_outer_invariants(model,S,wide)
    X,Xfee=uniform_primitive(model,N,Fraction(0));phase=uniform_phases(model,N,Fraction(0))
    values=np.empty((N,3),object)
    for j in range(N):values[j]=f_invariants(X[j],phase[j])
    coeff=model.target.fourier.fft(values)/N
    Rb,Sb=exact_arb(R),exact_arb(S)
    alias,tail=fourier_fee(N,K,4*exact_arb(wide),4*exact_arb(narrow))
    modes=list(range(K+1))+list(range(N-K,N))
    weights={k:(4*exact_arb(narrow)*abs(k if k<N//2 else k-N)).exp() for k in modes}
    rows=[]
    for field,name in enumerate(['D','M','W']):
        retained=[];full=[]
        for i in range(model.precision):
            finite=sum((abs(coeff[k,field][i])*weights[k] for k in modes),arb(0)).upper()
            fee=(wide_bounds[name]*(alias+tail)/Sb**i).upper()
            retained.append(finite);full.append((finite+fee).upper())
        time_tail=(bounds[name]*(Rb/Sb)**model.precision/(1-Rb/Sb)).upper()
        modulus=(sum((v*Rb**i for i,v in enumerate(full)),arb(0))+time_tail).upper()
        rows.append(dict(name=name,full=full,retained=retained,time_tail=time_tail,modulus=modulus,
                         narrow_modulus=bounds[name],wide_modulus=wide_bounds[name]))
    fees=dict(primitive_infinite_error=ball_record(Xfee),Fourier_alias_per_unit_modulus=ball_record(alias),
        Fourier_omitted_per_unit_modulus=ball_record(tail),
        coarse_narrow_domain={k:ball_record(v) for k,v in info.items()},
        coarse_wide_domain={k:ball_record(v) for k,v in wide_info.items()},ordinary_curvature_analytic_on_larger_disk=analytic_K)
    return rows,bounds,KM,analytic_K,fees


def gate(model,r59,N,K,R,S,narrow,wide,turn):
    started=time.monotonic();u,base,anchor=reflected_anchor(model,r59)
    alpha=abs(u).upper();Rb,Sb=exact_arb(R),exact_arb(S)
    if not alpha<Sb:raise ValueError('genuine germ anchor leaves the larger time disk')
    rows,coarse,KM,analytic_K,fees=invariant_enclosures(model,N,K,R,S,narrow,wide)
    D=rows[0]
    anchor_tail=(D['narrow_modulus']*(alpha/Sb)**model.precision/(1-alpha/Sb)).upper()
    variation=(sum((D['full'][i]*(Rb**i+alpha**i) for i in range(1,model.precision)),arb(0))
               +D['time_tail']+anchor_tail).upper()
    lower=(base-variation).lower()
    if turn:
        if not model.outer>=Sb:raise ValueError('turn Q was not paid on the entire larger time disk')
        Qrange,Qtail=time_disk_range(model.Q,Rb,Sb,abs(model.Q_outer).upper())
        positive=Qrange.real.lower()
        H=abs(model.eta1)*Rb
        sin_bound=(abs(model.eta0.sin())*H.cosh()+abs(model.eta0.cos())*H.sinh()).upper()
        rt=(abs(model.root)*sin_bound).upper();kap=(sin_bound*abs(Qrange).sqrt()).upper()
        curvature=dict(kind='root_deflated_Q',Q_real_lower=ball_record(positive),Q_modulus=ball_record(abs(Qrange).upper()),
            full_Q_time_tail=ball_record(Qtail),full_Q_outer= dict(real=ball_record(model.Q_outer.real),imag=ball_record(model.Q_outer.imag)),
            full_radial_D_tail=ball_record(model.D_tail),full_radial_Q_tail=ball_record(model.Q_tail),
            curvature_radial_radius=ball_record(model.RK),root_radial_image=ball_record(model.rho_outer),
            root_curvature_domain={k:ball_record(v) for k,v in model.K_domain.items()},
            exact_time_endpoint_locations=model.endpoint_locations,sin_eta_modulus=ball_record(sin_bound),
            root_newton_trace=model.root_newton_trace,
            branch_identity='sqrt(-K)=sin(eta)*sqrt(Q) on the real inner collar, analytically extended through the turn')
    else:
        if not analytic_K:raise ValueError('ordinary curvature not proved analytic on the larger disk')
        Krange,Ktail=time_disk_range(model.K,Rb,Sb,KM);positive=(-Krange).real.lower()
        rt=(abs(model.root)*(abs(model.h)*Rb).cosh()).upper();kap=abs(Krange).sqrt().upper()
        curvature=dict(kind='ordinary_negative_curvature',minus_K_real_lower=ball_record(positive),
            K_modulus=ball_record(abs(Krange).upper()),K_time_tail=ball_record(Ktail),
            K_larger_time_modulus=ball_record(KM),refined_root=model.root_package.provenance)
    passed=bool(lower>0 and positive>0)
    report=dict(common_span=list(map(str,model.cell)),anchor=anchor,passed=passed,D_lower=ball_record(lower),
        full_D_difference_from_actual_anchor=ball_record(variation),curvature=curvature,time_and_Fourier_fees=fees,
        invariant_bounds={row['name']:dict(whole_strip_time_modulus=ball_record(row['modulus']),
            true_time_coefficient_norms=[ball_record(v) for v in row['full']],
            retained_DFT_coefficient_norms=[ball_record(v) for v in row['retained']],
            larger_time_narrow_angle_modulus=ball_record(row['narrow_modulus']),
            larger_time_wide_angle_modulus=ball_record(row['wide_modulus']),full_time_tail=ball_record(row['time_tail'])) for row in rows})
    if passed:
        M,W=rows[1]['modulus'],rows[2]['modulus']
        field=(rt*(M+kap*W)/lower).upper()
        first=(rt*((coarse['M1']+kap*coarse['W1'])/lower+(M+kap*W)*coarse['D1']/lower**2)).upper()
        second=(rt*((coarse['M2']+kap*coarse['W2'])/lower+
            (2*(coarse['M1']+kap*coarse['W1'])*coarse['D1']+(M+kap*W)*coarse['D2'])/lower**2+
            2*(M+kap*W)*coarse['D1']**2/lower**3)).upper()
        report['true_field_moduli']={k:ball_record(v) for k,v in dict(f=field,f_theta=first,f_theta2=second,r_tau=rt,wave_factor=kap).items()}
    report['elapsed_seconds']=time.monotonic()-started
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--retarget',type=Path,required=True);p.add_argument('--leg',choices=['forward','backward'],default='forward')
    p.add_argument('--segment',type=int,required=True);p.add_argument('--mode',choices=['ordinary','turn'],required=True)
    p.add_argument('--sub-left',default='0');p.add_argument('--sub-right',default='1')
    p.add_argument('--R59',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_parameter_modulus_complex_angle_1over64.json.gz'))
    p.add_argument('--time-radius',default='3');p.add_argument('--larger-time-radius',default='4')
    p.add_argument('--theta-strip',default='1/64');p.add_argument('--wider-theta-strip',default='1/32')
    p.add_argument('--time-order',type=int,default=40);p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--cutoff',type=int,default=255);p.add_argument('--primitive-nodes',type=int,default=512)
    p.add_argument('--curvature-radius',default='1/500');p.add_argument('--radial-degree',type=int,default=48)
    p.add_argument('--bits',type=int,default=192);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();started=time.monotonic();ctx.prec=args.bits;ctx.cap=max(21,args.time_order+4)
    desc=document(args.retarget);op,obj=hashed(desc['target_object']);rp,_=hashed(desc['target_root'])
    gp,grid=hashed(desc['old_'+args.leg+'_reference']);r59=document(args.R59)
    delta=Fraction(int(obj['delta_fraction']['numerator']),int(obj['delta_fraction']['denominator']))
    membership=frame_membership(obj,r59,delta)
    narrow,wide=Fraction(args.theta_strip),Fraction(args.wider_theta_strip);R,S=Fraction(args.time_radius),Fraction(args.larger_time_radius)
    if not 0<narrow<=Fraction.from_float(r59['angular_strip_width']) or not wide>narrow or not S>R>1:
        raise ValueError('invalid analytic radii')
    a,b=map(PiTime.from_record,grid['exact_time_endpoints'][args.segment:args.segment+2])
    l,r=Fraction(args.sub_left),Fraction(args.sub_right)
    if not 0<=l<r<=1:raise ValueError('invalid exact subspan')
    a,b=a+(b-a)*l,a+(b-a)*r;c,h=(a+b)/2,(b-a)/2
    mode=args.mode;sign=int(grid['trace_identity']['sign'])
    if mode=='turn':
        side=1 if c.ball()>0 else -1
        model=TurnCollarTimeModel(op,rp,a,b,side=side,nodes=args.primitive_nodes,order=args.time_order,
            radial_degree=args.radial_degree,outer_radius=S,curvature_radius=Fraction(args.curvature_radius),branch_sign=sign)
        models=[model];cells=[model.cell]
    else:
        if c.p or h.p:raise ValueError('ordinary intervals must have exact rational endpoints')
        package=prepare_refined_root(op,rp,nodes=args.primitive_nodes)
        target=AffineBulkTarget(op,args.primitive_nodes,args.primitive_nodes,Fraction(3,1000),Fraction(1,400),Fraction(8,25))
        _,_,cells,_=radial_cover(target,package.root,c.q,h.q)
        models=None
    dependencies=['fourfold_phase_sine_time_geometry.py','fourfold_phase_full_angle_time_domain.py',
        'fourfold_phase_field_time_turn_collar.py','fourfold_phase_field_time_refined_root.py',
        'fourfold_phase_uniform_field_time_grid.py','fourfold_phase_uniform_field_time_grid_fast.py',
        'fourfold_phase_time_outer_taylor_gate.py','fourfold_phase_beta_interval.py','fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_affine.py']
    report=dict(kind='full_angle_sine_geometry_and_exact_turn_time_domain',complete=False,
        source_sha256=sha(__file__),dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in dependencies},
        retarget_descriptor_sha256=sha(args.retarget),target_object_sha256=sha(op),target_root_sha256=sha(rp),
        time_grid_manifest_sha256=sha(gp),old_time_grid_delta=grid['trace_identity']['exact_delta_fraction'],
        exact_delta_fraction=str(delta),R59_sha256=sha(args.R59),membership=membership,mode=mode,
        leg=args.leg,segment=args.segment,normalized_subspan=[str(l),str(r)],branch_sign=sign,
        turn_side=side if mode=='turn' else None,curvature_radius=str(Fraction(args.curvature_radius)),
        curvature_radial_degree=args.radial_degree,
        exact_time_endpoints=[a.record(),b.record()],time_radius=str(R),larger_time_radius=str(S),
        physical_theta_strip=str(narrow),wider_physical_theta_strip=str(wide),time_order=args.time_order,
        angles=args.angles,cutoff=args.cutoff,primitive_nodes=args.primitive_nodes,bits=args.bits,
        required_common_spans=[list(map(str,cell)) for cell in cells],germs=[],
        limitations=['A domain proof on the stated segment, not a true-flow or residual certificate.',
            'Negative-radius anchor bounds use the exact radial reflection only.',
            'True root-deflated Q and its tails are recomputed for every turning interval.'])
    def save():
        report['elapsed_seconds']=time.monotonic()-started;args.out.parent.mkdir(parents=True,exist_ok=True)
        raw=(json.dumps(report,indent=2)+'\n').encode()
        if len(raw)>1_000_000 and args.out.suffix!='.gz':raise ValueError('large report requires gzip')
        payload=gzip.compress(raw,mtime=0) if args.out.suffix=='.gz' else raw
        if len(payload)>5_000_000:raise ValueError('report must be split')
        tmp=args.out.with_name(args.out.name+'.tmp');tmp.write_bytes(payload);tmp.replace(args.out)
    save()
    for j,cell in enumerate(cells):
        if mode=='ordinary':
            model=SineGermTimeModel(op,rp,c.q,h.q,refined_root=package,cell=cell,
                nodes=args.primitive_nodes,order=args.time_order,outer_radius=R,branch_sign=sign)
        else:model=models[j]
        row=gate(model,r59,args.angles,args.cutoff,R,S,narrow,wide,mode=='turn')
        report['germs'].append(row);save()
        print(json.dumps(dict(leg=args.leg,segment=args.segment,mode=mode,passed=row['passed'],
            D_lower=row['D_lower']['ball'],elapsed_seconds=report['elapsed_seconds'])),flush=True)
    report['complete']=True;report['complete_common_span_coverage']=len(report['germs'])==len(cells)
    report['proved_full_physical_angle_and_complex_time_domain']=bool(report['complete_common_span_coverage'] and all(row['passed'] for row in report['germs']))
    save();print(json.dumps(dict(complete=True,proved=report['proved_full_physical_angle_and_complex_time_domain'],sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()

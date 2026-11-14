#!/usr/bin/env python3
"""True angular-boundary modulus and winding of one actual D germ.

The exact midpoint polygon is homotopic to the true analytic boundary only
when every whole-cell derivative disk avoids zero.  The resulting winding,
together with the existing nonzero real-axis gate, counts zeros in the upper
periodic strip.  Finite sampled signs alone do not establish any zero count.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
from types import SimpleNamespace
import time

from flint import arb,acb,ctx
from fourfold_phase_beta_affine import AffineBulkTarget,sha
from fourfold_phase_beta_bulk_interval import exact_arb,complex_pad
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_field_time_refined_root import prepare_refined_root
from fourfold_phase_field_time_turn_collar import PiTime
from fourfold_phase_field_time_taylor import phase_evaluation
from fourfold_phase_time_outer_taylor_gate import frame_invariants
from fourfold_phase_full_angle_time_domain import document,hashed,frame_membership,real_anchor
from fourfold_phase_sharp_time_domain_cover import sharp_cover,write_report
from fourfold_phase_sine_time_geometry import SineGermTimeModel,whole_angle_outer_invariants
from fourfold_phase_actual_angle_anchor_domain import static_grid,D_and_first


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--retarget',type=Path,required=True);p.add_argument('--segment',type=int,default=419)
    p.add_argument('--width',default='1/32');p.add_argument('--nodes',type=int,default=8192)
    p.add_argument('--primitive-nodes',type=int,default=512);p.add_argument('--bits',type=int,default=192)
    p.add_argument('--R59',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_parameter_modulus_complex_angle_1over64.json.gz'))
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();started=time.monotonic();ctx.prec=args.bits;ctx.cap=21
    desc=document(args.retarget);op,obj=hashed(desc['target_object']);rp,_=hashed(desc['target_root'])
    gp,grid=hashed(desc['old_forward_reference']);a,b=map(PiTime.from_record,grid['exact_time_endpoints'][args.segment:args.segment+2])
    c,h=(a+b)/2,(b-a)/2
    if c.p or h.p:raise ValueError('ordinary rational center required')
    package=prepare_refined_root(op,rp,nodes=args.primitive_nodes)
    target=AffineBulkTarget(op,args.primitive_nodes,args.primitive_nodes,
        exact_arb(Fraction(3,1000)),exact_arb(Fraction(1,400)),exact_arb(Fraction(8,25)))
    cells,cover=sharp_cover(target,package.root,a,b)
    if len(cells)!=1:raise ValueError('this entry requires a proved single actual common germ')
    model=SineGermTimeModel(op,rp,c.q,h.q,refined_root=package,cell=cells[0],nodes=args.primitive_nodes,
        order=4,outer_radius=3,branch_sign=int(grid['trace_identity']['sign']))
    if not exact_arb(model.cell[0])<=model.center.lower() or not model.center.upper()<=exact_arb(model.cell[1]):
        raise ValueError('the selected real center is not an actual point of this germ')
    r59=document(args.R59);membership=frame_membership(obj,r59,package.exact_delta)
    ua,real_lower,real_gate=real_anchor(model,r59)
    if not ua==0 or not real_lower>0:raise ValueError('actual real-axis nonzero gate failed')
    width=Fraction(args.width)
    if not 0<width<Fraction(2,25):raise ValueError('boundary leaves the paid primitive angular source strip')
    point=SimpleNamespace(target=model.target,root=model.root,tau0=model.tau0,h=arb(0),
        center=model.center,R0=model.R0,RE=model.RE,sigma=model.sigma,nodes=model.nodes)
    coarse,_,_,_=whole_angle_outer_invariants(point,Fraction(1),width)
    B2=coarse['D2'];step=(arb.pi()/(2*args.nodes)).upper()
    X,phases,Xerror=static_grid(model,args.nodes,width)
    Ds=[];first=[];vertices=[];errors=[]
    for j in range(args.nodes):
        D,D1=D_and_first(X[j],phases[j],model.a[0]);z=acb(D.real.mid(),D.imag.mid())
        Ds.append(D);first.append(abs(D1).upper());vertices.append(z);errors.append(abs(D-z).upper())
    # Independent direct Fourier summation and exact phase evaluation at four nodes.
    checks=[]
    for j in sorted(set([0,args.nodes//7,args.nodes//3,args.nodes-1])):
        theta=acb(arb.pi()*j/(2*args.nodes),exact_arb(width))
        directX=[acb(0),acb(0),acb(0)]
        for k,n in enumerate(model.target.frequency):
            factor=(acb(0,int(n))*theta).exp()
            for component in range(3):directX[component]+=model.X_coefficient[k,component][0]*factor
        directX=[complex_pad(v,Xerror)for v in directX]
        phase=phase_evaluation(*[[v[0]for v in row]for row in
            [model.beta,model.gamma,model.beta_r,model.gamma_r]],theta)
        direct=frame_invariants(directX,model.a[0],model.ar[0],*phase)
        if not (direct['D'].real.overlaps(Ds[j].real)and direct['D'].imag.overlaps(Ds[j].imag)):
            raise ValueError('static angular FFT and direct full primitive D disagree')
        gridD,gridD1=D_and_first(X[j],phases[j],model.a[0])
        if not (direct['D1'].real.overlaps(gridD1.real)and direct['D1'].imag.overlaps(gridD1.imag)):
            raise ValueError('true moving-frame D derivative and direct derivative disagree')
        checks.append(dict(index=j,D_and_Dtheta_overlap=True,
            D_difference_modulus=ball_record(abs(gridD-direct['D']).upper()),
            Dtheta_difference_modulus=ball_record(abs(gridD1-direct['D1']).upper())))
    minimum_margin=arb.pos_inf();minimum_D=arb.pos_inf();maximum_fee=arb(0)
    sum_angle=arb(0);all_positive_ratios=True;critical=None
    for j,z in enumerate(vertices):
        znext=vertices[(j+1)%args.nodes]
        curve_fee=(errors[j]+step*first[j]+B2*step**2/2).upper()
        polygon_fee=abs(znext-z).upper();fee=max(curve_fee,polygon_fee)
        margin=(abs(z).lower()-fee).lower()
        if margin<minimum_margin:minimum_margin=margin;critical=j
        minimum_D=min(minimum_D,abs(Ds[j]).lower());maximum_fee=max(maximum_fee,fee)
        if z.contains(0):all_positive_ratios=False;continue
        ratio=znext/z
        if not ratio.real>0:all_positive_ratios=False
        sum_angle+=ratio.log().imag
    winding=sum_angle/(2*arb.pi());candidate=int(round(float(winding.mid())))
    isolated=bool(winding>arb(candidate)-arb(1)/4 and winding<arb(candidate)+arb(1)/4)
    passed=bool(minimum_margin>0 and all_positive_ratios and isolated)
    report=dict(kind='directed_actual_D_boundary_homotopy_and_periodic_strip_zero_count',
        proved=passed,source_sha256=sha(__file__),target_object_sha256=sha(op),target_root_sha256=sha(rp),
        time_grid_sha256=sha(gp),exact_delta_fraction=str(package.exact_delta),segment=args.segment,
        exact_time_center=c.record(),actual_radial_center=ball_record(model.center),
        sharp_actual_germ_cover=cover,common_span=list(map(str,model.cell)),physical_theta_strip=str(width),
        nodes=args.nodes,primitive_nodes=args.primitive_nodes,bits=args.bits,R59_sha256=sha(args.R59),
        exact_box_membership=membership,actual_real_axis_gate=real_gate,
        primitive_infinite_error=ball_record(Xerror),whole_strip_Dtheta2_modulus=ball_record(B2),
        exact_step='pi/(2*N)',minimum_true_node_D_modulus=ball_record(minimum_D),
        maximum_whole_cell_homotopy_fee=ball_record(maximum_fee),
        minimum_homotopy_margin=ball_record(minimum_margin),critical_cell=critical,
        all_exact_midpoint_ratios_positive_real=all_positive_ratios,
        angle_sum=ball_record(sum_angle),winding_ball=ball_record(winding),isolated_integer=candidate if isolated else None,
        true_top_boundary_winding=candidate if passed else None,
        upper_strip_zero_count=-candidate if passed else None,
        direct_four_node_checks=checks,elapsed_seconds=time.monotonic()-started,
        dependency_sha256={name:sha(Path(__file__).with_name(name))for name in
            ['fourfold_phase_actual_angle_anchor_domain.py','fourfold_phase_sharp_time_domain_cover.py',
             'fourfold_phase_sine_time_geometry.py','fourfold_phase_time_outer_taylor_gate.py']},
        limitations=['Only the actual central time and exact delta5 germ, not a full time disk',
            'A negative real part alone was not used to infer a zero',
            'Zero count is asserted only if the whole-cell nonzero homotopy and integer isolation both pass',
            'A narrower characteristic strip remains available; this is not a PDE nonexistence claim'])
    write_report(args.out,report)
    print(json.dumps({k:report[k]for k in ['proved','minimum_true_node_D_modulus','minimum_homotopy_margin',
        'winding_ball','upper_strip_zero_count','elapsed_seconds']},indent=2),flush=True)


if __name__=='__main__':main()

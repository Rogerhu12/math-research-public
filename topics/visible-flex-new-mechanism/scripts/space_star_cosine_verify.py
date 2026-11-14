#!/usr/bin/env python3
"""Independent continuous verification of one frozen cosine-lift core.

No optimization, coefficient elimination, re-selection, or automatic change of
height offset occurs here. Exact rational physical parameters are consumed from
the design report. Research interval runs belong in this public repo Actions.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D
from fractions import Fraction as R
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np

from folded_reference_geometry import I,PI,UP,DOWN,sincos
from star_core_geometry import clipped,square,unit_enclosures
from space_star_flat_core import absolute_interval
from space_star_lift_design import rational_interval,load_planar
from space_star_frozen_lift_verify import trig_multiples,invariant_frame
from cosine_rectifying_core import (CosineRectifyingCore,canonical_identity,
    identity_hash,exact_rational,rational_json)


def height_at_vertex(s,c,heights,offset):
    _,_,trig=trig_multiples(s,c,len(heights))
    return offset+sum((h*cc for h,(ss,cc) in zip(heights,trig)),I(0))


def moving_frame_jets(s,c,a,b,heights,offset):
    """Physical derivatives in one common proper polar frame, using cos lifts."""
    c3,s3,trig=trig_multiples(s,c,len(heights))
    c6=clipped(2*square(c3)-1);s6=clipped(2*s3*c3)
    r=[1+a*c3+b*c6,-3*a*s3-6*b*s6,-9*a*c3-36*b*c6,
       27*a*s3+216*b*s6,81*a*c3+1296*b*c6]
    z=[]
    for order in range(5):
        value=sum((height*(3*j)**order*[cc,-ss,-cc,ss][order%4]
                   for j,(height,(ss,cc)) in enumerate(zip(heights,trig),1)),I(0))
        z.append(value+offset if order==0 else value)
    radial=[r[0],r[1],r[2]-r[0],r[3]-3*r[1],r[4]-6*r[2]+r[0]]
    angular=[I(0),r[0],2*r[1],3*r[2]-r[0],4*r[3]-4*r[1]]
    return [[radial[k],angular[k],z[k]] for k in range(5)]


def symmetry_certificates(a,b,heights,width):
    result=[]
    for sign,label in [(1,'tip'),(-1,'valley')]:
        r=1+a*sign+b;r2=-9*a*sign-36*b;r4=81*a*sign+1296*b
        radial=r2-r;fourth=r4-6*r2+r
        z2=sum((-(3*j)**2*h*sign**j for j,h in enumerate(heights,1)),R(0))
        z4=sum(((3*j)**4*h*sign**j for j,h in enumerate(heights,1)),R(0))
        rr,rad,ff,zz,vv=[rational_interval(x) for x in [r,radial,fourth,z2,z4]]
        denominator=square(rad)+square(zz)
        item={'location':label,'torsion_exactly_zero_by_even_reflection':True,
              'exact_r':rational_json(r),'exact_r2_minus_r':rational_json(radial),
              'exact_z2':rational_json(z2),'exact_z4':rational_json(z4)}
        if denominator.lo<=0:
            item.update(resolved=False,q_ell_enclosure=None,J_lower=None,
                        whole_width_principal_curvature_upper=None)
        else:
            root=denominator.sqrt()
            kappa=root/square(rr)
            qell=(zz*ff-rad*vv)/(root**3)
            J=1-rational_interval(width)*I(qell.abs_upper())
            item.update(resolved=True,kappa_enclosure=kappa.json(),q_ell_enclosure=qell.json(),
                        J_lower=str(J.lo),whole_width_principal_curvature_upper=
                        str((kappa/J).hi) if J.lo>0 else None)
        result.append(item)
    return result


def cosine_certificate(a_exact,b_exact,heights,offset,width_exact,planar,nodes):
    vertices,cells=unit_enclosures(nodes)
    a,b=rational_interval(a_exact),rational_interval(b_exact)
    hh=[rational_interval(x) for x in heights];w=rational_interval(width_exact)
    zz0=rational_interval(offset);step=2*PI/nodes
    M2_exact=sum((R((3*j)**2)*abs(h) for j,h in enumerate(heights,1)),R(0))
    M2=rational_interval(M2_exact)
    height_vertex=D(0);height_vertex_lower=D(0)
    for s,c in vertices:
        value=height_at_vertex(s,c,hh,zz0)
        height_vertex=max(height_vertex,value.abs_upper())
        av=absolute_interval(value);height_vertex_lower=max(height_vertex_lower,av.lo)
    height_remainder=(M2*square(step)/8).hi
    sharp_height=UP.add(height_vertex,height_remainder)
    unresolved=0;nonpositive_J=0;Jlower=D(1);kappa_lower=None
    lambda_upper=D(0);lambda_lower=D(0);lambda0_upper=D(0);qell_upper=D(0)
    cell_height=D(0);perimeter=I(0);worst_J_cell=None;worst_curvature_cell=None
    for index,(s,c) in enumerate(cells):
        jets=moving_frame_jets(s,c,a,b,hh,zz0)
        cell_height=max(cell_height,jets[0][2].abs_upper())
        frame=invariant_frame(jets);perimeter+=step*frame['speed']
        if not frame['resolved']:
            unresolved+=1
            continue
        kappa=frame['kappa'];qa=absolute_interval(frame['q_ell']);lambda0=frame['lambda0']
        localJ=1-w*I(qa.hi)
        if localJ.lo<Jlower:
            Jlower=localJ.lo;worst_J_cell=index
        qell_upper=max(qell_upper,qa.hi);lambda0_upper=max(lambda0_upper,lambda0.hi)
        kappa_lower=kappa.lo if kappa_lower is None else min(kappa_lower,kappa.lo)
        lambda_lower=max(lambda_lower,lambda0.lo)
        if localJ.lo<=0:
            nonpositive_J+=1
            continue
        curvature=(lambda0/localJ).hi
        if curvature>lambda_upper:
            lambda_upper=curvature;worst_curvature_cell=index
        lambda_lower=max(lambda_lower,(I(lambda0.lo)/(1-w*I(qa.lo))).lo)
    regular=unresolved==0 and nonpositive_J==0 and Jlower>0
    center_regular=unresolved==0 and kappa_lower is not None and kappa_lower>0
    radial_lower=1-abs(a_exact)-abs(b_exact)
    height_upper=min(sharp_height,cell_height)
    d=I(planar['continuous_distance_q_to_filled_star_domain']['lower'])
    Dxy=I(planar['continuous_full_curve_diameter']['upper'])
    Dlower=I(planar['continuous_full_curve_diameter']['lower'])
    Dcore=(square(Dxy+2*w)+square(2*(I(height_upper)+w))).sqrt()
    witness=I(max(D(0),(d-w).lo));ratio=witness/I(Dcore.hi)
    curvature_ratio=(I(1)/(I(lambda_lower)*Dlower)).hi if lambda_lower>0 else None
    allowed2=square(witness/I('.3'))-square(Dxy+2*w)
    height_budget=(I(max(D(0),allowed2.lo)).sqrt()/2-w).lo if allowed2.lo>0 else D(0)
    physical={'height_basis':'cosine','a':str(a_exact),'b':str(b_exact),'half_width':str(width_exact),
        'height_coefficients':[rational_json(x) for x in heights],'height_offset':rational_json(offset)}
    return {'nodes':nodes,'height_basis':'cosine','physical_identity_sha256':identity_hash(physical),
        'exact_height_coefficients_used':True,
        'exact_height_offset_used':True,'fixed_physical_parameters':True,'optimization_performed':False,
        'invariant_calculation_frame':'common proper polar rotation of physical derivatives',
        'unresolved_frame_cells':unresolved,'cells_without_positive_J_certificate':nonpositive_J,
        'whole_core_immersion_and_angular_closure_certified':regular,
        'central_curve_embedding_proved_from_positive_radial_projection':radial_lower>0,
        'planar_radial_lower_exact':rational_json(radial_lower),
        'zero_framing_proved':bool(center_regular and radial_lower>0),
        'framing_degree_exact':0 if center_regular and radial_lower>0 else None,
        'framing_proof':'both blackboard normal components are even functions; each sector retraces',
        'J_lower':str(Jlower) if unresolved==0 else None,
        'kappa_positive_lower':str(kappa_lower) if unresolved==0 else None,
        'q_ell_absolute_upper':str(qell_upper) if unresolved==0 else None,
        'central_principal_curvature_upper':str(lambda0_upper) if unresolved==0 else None,
        'whole_width_principal_curvature_upper':str(lambda_upper) if regular else None,
        'principal_curvature_max_lower_from_resolved_cells':str(lambda_lower),
        'necessary_reach_over_D_upper_from_curvature_lower':None if curvature_ratio is None else str(curvature_ratio),
        'worst_J_cell_index':worst_J_cell,'worst_curvature_upper_cell_index':worst_curvature_cell,
        'height_vertex_max_upper':str(height_vertex),'height_vertex_max_lower':str(height_vertex_lower),
        'height_second_derivative_absolute_bound_exact':rational_json(M2_exact),
        'height_chord_remainder_upper':str(height_remainder),
        'height_vertex_plus_remainder_upper':str(sharp_height),
        'height_whole_cell_interval_upper':str(cell_height),
        'central_height_absolute_upper':str(height_upper),
        'height_budget_for_conditional_amplitude':str(height_budget),
        'height_budget_margin_lower':str(DOWN.subtract(height_budget,height_upper)),
        'perimeter':perimeter.json(),'a0_exact_enclosure':(perimeter/(2*PI)).json(),
        'projection_padding_upper':str(w.hi),'core_diameter_upper':str(Dcore.hi),
        'conditional_witness_distance_lower':str(witness.lo),
        'conditional_witness_over_core_D_lower':str(ratio.lo),
        'conditional_witness_ratio_at_least_03':ratio.lo>=D('.3'),
        'local_curvature_ceiling_sufficient_for_003_Dcore_budget':regular and
            (I(lambda_upper)*I('.03')*I(Dcore.hi)).hi<=1,
        'tip_valley_exact_formula_certificates':symmetry_certificates(a_exact,b_exact,heights,width_exact),
        'full_transition_and_caps_share_projection_height_budget_proved':False,
        'whole_core_embedding_proved':False,'embedding_proved':False,
        'reach_lower_proved':False,'closed_surface_constructed':False,'task_complete':False}


def numerical_interface_audit(core):
    theta=np.array([.19,.71,1.31,2.27]);s=.19*core.width
    eps=min(2e-6,core.width/20)
    d=core.evaluate(s,theta)
    sp,sm=core.evaluate(s+eps,theta),core.evaluate(s-eps,theta)
    tp,tm=core.evaluate(s,theta+eps),core.evaluate(s,theta-eps)
    pairs={'X_s':((sp['X']-sm['X'])/(2*eps),d['Xs']),
           'X_theta':((tp['X']-tm['X'])/(2*eps),d['Xtheta']),
           'X_ss':((sp['Xs']-sm['Xs'])/(2*eps),d['Xss']),
           'X_st_from_s':((sp['Xtheta']-sm['Xtheta'])/(2*eps),d['Xst']),
           'X_st_from_theta':((tp['Xs']-tm['Xs'])/(2*eps),d['Xst']),
           'X_tt':((tp['Xtheta']-tm['Xtheta'])/(2*eps),d['Xtt'])}
    errors={name:float(np.max(np.linalg.norm(left-right,axis=-1)/(1+np.linalg.norm(right,axis=-1))))
            for name,(left,right) in pairs.items()}
    mirror=core.evaluate(s,-theta)['X']
    reflection_error=float(np.max(np.abs(mirror-d['X']*np.array([1.,-1.,1.]))))
    ports=[core.evaluate(side*core.width,theta) for side in [-1,1]]
    residual=max([d['material_equation_residual_max']]+[p['material_equation_residual_max'] for p in ports])
    return {'evaluation_is_numerical_not_continuous_certificate':True,'a0_numerical':core.a0,
            'arclength_quadrature_cells':core.arc_cells,'arclength_quadrature_order':core.quadrature,
            'position_two_jet_finite_difference_relative_errors':errors,
            'same_side_mirror_position_error':reflection_error,'material_equation_residual_max':residual,
            'both_signed_ports_evaluated':True,'all_port_J_samples_positive':bool(all(np.min(p['J'])>0 for p in ports)),
            'maximum_jet_check_error':max(errors.values()),'no_higher_mixed_jets_supplied':True}


def developer_check():
    identity={'height_basis':'cosine','a':'7/100','b':'1/200','half_width':'1/50',
        'height_coefficients':[rational_json(x) for x in [R('.04'),R('.003'),R('-.0005'),R('.00008')]],
        'height_offset':rational_json(R('.013'))}
    core=CosineRectifyingCore(identity,arc_cells=64,quadrature=16)
    audit=numerical_interface_audit(core)
    hh=[rational_interval(x) for x in core.heights_exact]
    comparisons=[]
    for text_phi in ['.173','.417','.813']:
        phi=D(text_phi);ss,cc=sincos(I(phi-D('1e-12'),phi+D('1e-12')))
        frame=invariant_frame(moving_frame_jets(ss,cc,rational_interval(core.a_exact),
            rational_interval(core.b_exact),hh,rational_interval(core.offset_exact)))
        point=core.frame(np.asarray(float(phi)))
        differences={}
        for key in ['kappa','tau','q_ell']:
            value=float(point[key]);interval=frame[key]
            differences[key]=max(0.,float(interval.lo)-value,value-float(interval.hi))
        comparisons.append(differences)
    exact_symmetry=symmetry_certificates(core.a_exact,core.b_exact,core.heights_exact,core.width_exact)
    symmetry_errors=[]
    for phi,item in zip([0.,np.pi/3],exact_symmetry):
        f=core.frame(np.asarray(phi))
        interval=item['q_ell_enclosure'];q=float(f['q_ell'])
        symmetry_errors.append({'tau_absolute':abs(float(f['tau'])),
            'q_ell_distance_from_exact_interval':max(0.,float(interval['lower'])-q,q-float(interval['upper']))})
    circle_identity=dict(identity,a='0',b='0',
                         height_coefficients=[rational_json(R(0))],height_offset=rational_json(R('.13')))
    circle=CosineRectifyingCore(circle_identity,arc_cells=16,quadrature=8)
    theta=np.array([.23,.7,1.9]);s=.007
    xyz=circle.evaluate(s,theta)
    expected=np.stack((np.cos(theta),np.sin(theta),np.full_like(theta,.13+s)),axis=-1)
    circle_error=float(np.max(np.abs(xyz['X']-expected)))
    exact_circle=invariant_frame(moving_frame_jets(I(0),I(1),I(0),I(0),[I(0)],I('.13')))
    circle_interval_ok=exact_circle['kappa'].lo<=1<=exact_circle['kappa'].hi
    circle_interval_ok=circle_interval_ok and exact_circle['tau'].lo<=0<=exact_circle['tau'].hi
    passed=(audit['maximum_jet_check_error']<5e-5 and audit['same_side_mirror_position_error']<1e-9
        and max(max(v.values()) for v in comparisons)<1e-8
        and max(max(v.values()) for v in symmetry_errors)<1e-8
        and circle_error<1e-11 and circle_interval_ok)
    return {'schema':'space-star-cosine-verifier-development-v1','development_check_only':True,
        'research_geometry_evaluated':False,'optimization_performed':False,
        'synthetic_material_interface':audit,'synthetic_interval_invariant_comparisons':comparisons,
        'synthetic_tip_valley_checks':symmetry_errors,'exact_circle_position_error':circle_error,
        'exact_circle_interval_identity_passed':bool(circle_interval_ok),'passed':bool(passed)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--planar-report',type=Path)
    parser.add_argument('--nodes',type=int,default=32768)
    parser.add_argument('--arc-cells',type=int,default=512)
    parser.add_argument('--quadrature',type=int,default=16)
    parser.add_argument('--skip-numerical-interface',action='store_true')
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();started=time.monotonic()
    if args.check_only:
        result=developer_check()
    else:
        if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
            parser.error('frozen research verification runs in this public repository Actions')
        if args.input is None or args.planar_report is None or args.nodes<32:
            parser.error('need one frozen public input, a planar report, and nodes >=32')
        repo=Path(__file__).resolve().parents[3]
        note_root=repo/'topics'/'visible-flex-new-mechanism'/'notes'
        allowed=[note_root.resolve()]
        if os.environ.get('RUNNER_TEMP'):allowed.append(Path(os.environ['RUNNER_TEMP']).resolve())
        if not any(args.input.resolve().is_relative_to(root) for root in allowed):
            parser.error('design input must be a public topic note or this Actions runner temporary output')
        args.planar_report.resolve().relative_to(note_root.resolve())
        raw=args.input.read_bytes();source=json.loads(raw)
        if source.get('schema')!='space-star-cosine-design-v1':
            raise ValueError('need the cosine designer schema, not a re-labelled sine candidate')
        identity=canonical_identity(source['frozen_physical_identity']);digest=identity_hash(identity)
        if source.get('frozen_physical_identity_sha256')!=digest:
            raise ValueError('design physical identity hash mismatch')
        planar_hash=hashlib.sha256(args.planar_report.read_bytes()).hexdigest()
        if planar_hash!=source['planar_certificate_source']['sha256']:
            raise ValueError('planar certificate differs from the frozen design source')
        a,b=R(identity['a']),R(identity['b']);width=R(identity['half_width'])
        heights=[exact_rational(x) for x in identity['height_coefficients']]
        offset=exact_rational(identity['height_offset'])
        planar=load_planar(args.planar_report,str(a),str(b))
        certificate=cosine_certificate(a,b,heights,offset,width,planar,args.nodes)
        interface=None
        if certificate['whole_core_immersion_and_angular_closure_certified'] and not args.skip_numerical_interface:
            try:
                core=CosineRectifyingCore(identity,args.arc_cells,args.quadrature,certificate)
                interface=numerical_interface_audit(core)
            except (ValueError,RuntimeError,FloatingPointError) as error:
                interface={'evaluation_is_numerical_not_continuous_certificate':True,
                           'interface_check_failed':True,'error':str(error)}
        result={'schema':'space-star-frozen-cosine-verification-v1',
            'status':'frozen_exact_cosine_parameters_continuous_certificate_attempt',
            'source_report':str(args.input),'source_report_sha256':hashlib.sha256(raw).hexdigest(),
            'source_design_status':source.get('status'),'source_solver':source.get('solver'),
            'source_dense_frozen_audit':source.get('dense_frozen_audit'),
            'frozen_physical_identity':identity,'frozen_physical_identity_sha256':digest,
            'coefficient_freezing':source.get('coefficient_freezing'),
            'optimization_performed':False,'automatic_coefficient_reselection_or_refitting_performed':False,
            'height_offset_changed':False,'old_sine_tip_valley_elimination_used':False,
            'planar_report_sha256':planar_hash,'continuous_certificate':certificate,
            'numerical_material_interface':interface,'task_complete':False}
    names=['space_star_cosine_verify.py','cosine_rectifying_core.py','space_star_frozen_lift_verify.py',
           'space_star_lift_design.py','space_star_flat_core.py','star_core_geometry.py','folded_reference_geometry.py']
    result['source_files_sha256']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in names}
    result['elapsed_seconds']=time.monotonic()-started
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'passed':result.get('passed'),
        'elapsed_seconds':result['elapsed_seconds'],'continuous':result.get('continuous_certificate')}),flush=True)
    if args.check_only and not result['passed']:
        raise SystemExit(1)


if __name__=='__main__':
    main()

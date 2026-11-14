#!/usr/bin/env python3
"""Verify a published frozen multi-harmonic rectifying core without optimizing.

Uses exact saved rational height coefficients, a vertex-plus-second-derivative
height enclosure, and cellwise lambda0/(1-w*abs(q_ell)).  The physical curve
derivatives are expressed in the rotating polar orthonormal frame before
forming invariant dot/cross products, reducing interval dependency without
changing the curve.  Research verification runs only in public Actions.
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

from folded_reference_geometry import I,PI,UP,DOWN
from star_core_geometry import clipped,square,unit_enclosures
from space_star_flat_core import dot,cross,norm,absolute_interval
from space_star_lift_design import (HeightElimination,LiftProblem,rational_interval,
    generic_interval_jets,load_planar,normal_chord_sample)


def trig_multiples(s,c,count):
    c3=clipped(4*c*c*c-3*c);s3=clipped(3*s-4*s*s*s)
    out=[];cc,ss=I(1),I(0)
    for _ in range(count):
        cc,ss=clipped(cc*c3-ss*s3),clipped(ss*c3+cc*s3)
        out.append((ss,cc))
    return c3,s3,out


def height_at_vertex(s,c,heights):
    _,_,trig=trig_multiples(s,c,len(heights))
    return sum((h*ss for h,(ss,cc) in zip(heights,trig)),I(0))


def moving_frame_jets(s,c,a,b,heights):
    """Physical Cartesian derivatives, all in the same rotated basis at phi.

    These are not successive derivatives of the moving-frame components.
    Rotating each physical derivative by the same proper rotation preserves
    every dot product, cross-product norm, and scalar triple product used.
    """
    c3,s3,trig=trig_multiples(s,c,len(heights))
    c6=clipped(2*square(c3)-1);s6=clipped(2*s3*c3)
    r=[1+a*c3+b*c6,-3*a*s3-6*b*s6,-9*a*c3-36*b*c6,
       27*a*s3+216*b*s6,81*a*c3+1296*b*c6]
    z=[]
    for order in range(5):
        z.append(sum((height*(3*j)**order*[ss,cc,-ss,-cc][order%4]
                      for j,(height,(ss,cc)) in enumerate(zip(heights,trig),1)),I(0)))
    radial=[r[0],r[1],r[2]-r[0],r[3]-3*r[1],r[4]-6*r[2]+r[0]]
    angular=[I(0),r[0],2*r[1],3*r[2]-r[0],4*r[3]-4*r[1]]
    return [[radial[k],angular[k],z[k]] for k in range(5)]


def invariant_frame(jets):
    _,v1,v2,v3,v4=jets
    speed=norm(v1);C=cross(v1,v2);W=norm(C)
    if speed.lo<=0 or W.lo<=0:
        return {'resolved':False,'speed':speed}
    determinant=dot(C,v3);determinant_p=dot(v1,cross(v2,v4))
    vp=dot(v1,v2)/speed;Wp=dot(C,cross(v1,v3))/W
    kappa=W/(speed**3);tau=determinant/square(W)
    qphi=(determinant_p*speed**3/W**3+3*determinant*square(speed)*vp/W**3-
          3*determinant*speed**3*Wp/W**4)
    return {'resolved':True,'speed':speed,'kappa':kappa,'tau':tau,
            'q_ell':qphi/speed,'lambda0':kappa+square(tau)/kappa}


def frozen_certificate(a_exact,b_exact,heights,width_text,planar,nodes):
    vertices,cells=unit_enclosures(nodes)
    a,b=rational_interval(a_exact),rational_interval(b_exact)
    hh=[rational_interval(x) for x in heights];w=I(width_text)
    if w.lo<=0:
        raise ValueError('positive half width is required')
    step=2*PI/nodes
    M2_exact=sum((R((3*j)**2)*abs(h) for j,h in enumerate(heights,1)),R(0))
    M2=rational_interval(M2_exact)
    height_vertex=D(0);height_vertex_lower=D(0)
    for s,c in vertices:
        value=height_at_vertex(s,c,hh)
        height_vertex=max(height_vertex,value.abs_upper())
        av=absolute_interval(value);height_vertex_lower=max(height_vertex_lower,av.lo)
    height_remainder=(M2*square(step)/8).hi
    sharp_height=UP.add(height_vertex,height_remainder)
    unresolved=0;nonpositive_J=0;Jlower=D(1);kappa_lower=None
    lambda_upper=D(0);lambda_lower=D(0);lambda0_upper=D(0);qell_upper=D(0)
    cell_height=D(0);perimeter=I(0);worst_J_cell=None;worst_curvature_cell=None
    for index,(s,c) in enumerate(cells):
        jets=moving_frame_jets(s,c,a,b,hh)
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
    height_upper=min(sharp_height,cell_height)
    d=I(planar['continuous_distance_q_to_filled_star_domain']['lower'])
    Dxy=I(planar['continuous_full_curve_diameter']['upper'])
    Dlower=I(planar['continuous_full_curve_diameter']['lower'])
    Dcore=(square(Dxy+2*w)+square(2*(I(height_upper)+w))).sqrt()
    witness=I(max(D(0),(d-w).lo));ratio=witness/I(Dcore.hi)
    curvature_ratio=(I(1)/(I(lambda_lower)*Dlower)).hi if lambda_lower>0 else None
    allowed2=square(witness/I('.3'))-square(Dxy+2*w)
    height_budget=(I(max(D(0),allowed2.lo)).sqrt()/2-w).lo if allowed2.lo>0 else D(0)
    return {'nodes':nodes,'exact_height_coefficients_used':True,
        'fixed_physical_parameters':True,'optimization_performed':False,
        'invariant_calculation_frame':'common proper polar rotation of physical derivatives',
        'unresolved_frame_cells':unresolved,'cells_without_positive_J_certificate':nonpositive_J,
        'whole_core_immersion_and_angular_closure_certified':regular,
        'J_lower':str(Jlower) if unresolved==0 else None,
        'kappa_positive_lower':str(kappa_lower) if unresolved==0 else None,
        'q_ell_absolute_upper':str(qell_upper) if unresolved==0 else None,
        'central_principal_curvature_upper':str(lambda0_upper) if unresolved==0 else None,
        'whole_width_principal_curvature_upper':str(lambda_upper) if regular else None,
        'principal_curvature_max_lower_from_resolved_cells':str(lambda_lower),
        'necessary_reach_over_D_upper_from_curvature_lower':None if curvature_ratio is None else str(curvature_ratio),
        'worst_J_cell_index':worst_J_cell,'worst_curvature_upper_cell_index':worst_curvature_cell,
        'height_vertex_max_upper':str(height_vertex),'height_vertex_max_lower':str(height_vertex_lower),
        'height_second_derivative_absolute_bound_exact':{'numerator':str(M2_exact.numerator),'denominator':str(M2_exact.denominator)},
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
        'full_transition_and_caps_share_projection_height_budget_proved':False,
        'embedding_proved':False,'reach_lower_proved':False,'task_complete':False}


def saved_candidate(path,trial_specification):
    report=json.loads(path.read_text())
    if report.get('schema')!='space-star-lift-design-v1' or report.get('status')!='geometry_design_then_frozen_certificate_attempt':
        raise ValueError('input must be the published frozen lift design report')
    if trial_specification=='selected':
        candidate=report['selected_frozen_candidate']
    else:
        matches=[r for r in report['optimization_trials'] if R(r['initial_lift'])==R(trial_specification)]
        if len(matches)!=1:
            raise ValueError('trial specification must select one stored candidate')
        candidate=matches[0]
    definition=report['definition'];a,b=R(definition['a']),R(definition['b'])
    heights=[R(int(h['numerator']),int(h['denominator'])) for h in candidate['height_coefficients_exact_rational']]
    if len(heights)!=int(definition['height_modes']):
        raise ValueError('height mode count differs from source definition')
    elimination=HeightElimination(a,b,len(heights))
    free=[R(x) for x in candidate['free_coefficients_exact_decimal']]
    if len(free)!=len(elimination.free_indices):
        raise ValueError('saved free coefficient count does not match the elimination identity')
    reconstructed=[sum(c*x for c,x in zip(row,free)) for row in elimination.exact]
    if reconstructed!=heights or sum(c*x for c,x in zip(elimination.tip,heights))!=0 or sum(c*x for c,x in zip(elimination.valley,heights))!=0:
        raise ValueError('saved exact coefficients do not match their exact elimination identity')
    identity={'a':str(a),'b':str(b),'half_width':str(R(str(definition['half_width']))),
              'height_coefficients':[{'numerator':str(x.numerator),'denominator':str(x.denominator)} for x in heights]}
    identity_hash=hashlib.sha256(json.dumps(identity,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return report,candidate,a,b,heights,elimination,free,identity,identity_hash


def developer_check():
    # Artificial input, three pointwise invariant comparisons; no candidate scan.
    a,b=R('0.17'),R('0.023');heights=list(map(R,['.11','.02','-.005']))
    aa,bb=rational_interval(a),rational_interval(b);hh=list(map(rational_interval,heights))
    from folded_reference_geometry import sincos
    overlaps=[]
    for angle in [PI/7,PI/5,3*PI/4]:
        s,c=sincos(angle)
        cartesian=invariant_frame(generic_interval_jets(s,c,aa,bb,hh))
        moving=invariant_frame(moving_frame_jets(s,c,aa,bb,hh))
        for name in ['speed','kappa','tau','q_ell','lambda0']:
            x,y=cartesian[name],moving[name]
            overlaps.append(max(x.lo,y.lo)<=min(x.hi,y.hi))
    circle_planar={'continuous_distance_q_to_filled_star_domain':{'lower':'0'},
                   'continuous_full_curve_diameter':{'lower':'2','upper':'2'}}
    circle=frozen_certificate(R(0),R(0),[R(0)],'.02',circle_planar,24)
    circle_ok=(circle['whole_core_immersion_and_angular_closure_certified'] and
               D(circle['J_lower'])>D('.999999999999') and
               abs(D(circle['whole_width_principal_curvature_upper'])-1)<D('1e-40') and
               D(circle['central_height_absolute_upper'])<D('1e-40') and
               not circle['conditional_witness_ratio_at_least_03'])
    return {'schema':'frozen-lift-verifier-development-check-v1','development_check_only':True,
        'research_candidate_evaluated':False,'pointwise_invariant_interval_overlap_checks':overlaps,
        'exact_circular_cylinder_check':circle,'passed':bool(all(overlaps) and circle_ok)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--trial',default='selected',help='selected, or a stored initial_lift label')
    parser.add_argument('--planar-report',type=Path)
    parser.add_argument('--nodes',type=int,default=32768)
    parser.add_argument('--samples',type=int,default=384)
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();started=time.monotonic()
    if args.check_only:
        result=developer_check()
    else:
        if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
            parser.error('frozen research verification runs in this public repository Actions')
        if args.input is None or args.planar_report is None or args.nodes<32 or args.samples<16:
            parser.error('need public input, planar report, nodes >= 32, samples >= 16')
        repo=Path(__file__).resolve().parents[3]
        for path in [args.input,args.planar_report]:
            path.resolve().relative_to(repo/'topics'/'visible-flex-new-mechanism'/'notes')
        source,candidate,a,b,heights,elimination,free,identity,identity_hash=saved_candidate(args.input,args.trial)
        planar_hash=hashlib.sha256(args.planar_report.read_bytes()).hexdigest()
        if planar_hash!=source['planar_certificate_source']['sha256']:
            raise ValueError('planar certificate differs from the frozen design source')
        planar=load_planar(args.planar_report,str(a),str(b))
        width=str(source['definition']['half_width'])
        certificate=frozen_certificate(a,b,heights,width,planar,args.nodes)
        samples=None
        if certificate['whole_core_immersion_and_angular_closure_certified']:
            angles=np.arange(args.samples)*2*np.pi/args.samples
            problem=LiftProblem(elimination,angles,float(width),1.,0.,0.)
            samples=normal_chord_sample(problem,np.array([float(x) for x in free]),float(width),args.samples)
        result={'schema':'space-star-frozen-multimode-verification-v1',
            'status':'frozen_exact_parameters_continuous_certificate_attempt',
            'source_report':str(args.input),'source_report_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),
            'source_candidate_initial_lift_label':candidate['initial_lift'],
            'source_trial_selection_request':args.trial,
            'source_solver_success_preserved':candidate['solver_success'],
            'source_dense_frozen_audit':candidate['dense_frozen_audit'],
            'frozen_physical_identity':identity,'frozen_physical_identity_sha256':identity_hash,
            'exact_tip_and_valley_constraints_rechecked':True,'optimization_performed':False,
            'automatic_coefficient_reselection_or_refitting_performed':False,'planar_report_sha256':planar_hash,
            'continuous_certificate':certificate,'normal_chord_samples':samples,
            'source_files_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                for name in ['space_star_frozen_lift_verify.py','space_star_lift_design.py','space_star_flat_core.py',
                             'star_core_geometry.py','folded_reference_geometry.py']},
            'task_complete':False}
    result['elapsed_seconds']=time.monotonic()-started
    result['verifier_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'elapsed_seconds':result['elapsed_seconds'],
                     'passed':result.get('passed'),'continuous':result.get('continuous_certificate')}),flush=True)
    if args.check_only and not result['passed']:
        raise SystemExit(1)


if __name__=='__main__':
    main()

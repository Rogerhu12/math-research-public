#!/usr/bin/env python3
"""Scalar background-Hermite height diagnostic, with no physical BVP or tail.

This does not differentiate the full flexible immersion or certify diameter.
All quadrature values are ordinary floating-point diagnostics, not intervals.
"""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path


def read(path):
    data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)


def ramp(profile,n):
    delta,V,k=(float(profile[key]) for key in ('delta','vu','start_acceleration'))
    if not delta>0 or not 0<V<1 or not k>=0 or n<2 or n%2:
        raise ValueError('The positive Hermite ramp domain and even grid are required')
    S=4*delta/(V+math.sqrt(V*V+4*k*delta/3))
    b=k*S
    if not 0<=b<=3*V:
        raise ValueError('This scalar diagnostic requires the monotone speed regime')
    I=I_V=I_b=0.
    for i in range(n+1):
        u=i/n
        a=3*u*u-2*u*u*u
        c=u*(1-u)*(1-u)
        v=V*a+b*c
        z=math.sqrt(1-v*v)
        weight=1 if i in (0,n) else 4 if i%2 else 2
        I+=weight*z
        I_V-=weight*v*a/z
        I_b-=weight*v*c/z
    I/=3*n;I_V/=3*n;I_b/=3*n
    S_delta=1/(V/2+k*S/6)
    S_V=-S/(V+k*S/3)
    S_k=-S*S/(6*V+2*k*S)
    return dict(delta=delta,vu=V,start_acceleration=k,length=S,k_times_length=b,
        height=S*I,quadrature_panels=n,
        dheight_ddelta=S_delta*(I+k*S*I_b),
        dheight_dvu=S_V*(I+k*S*I_b)+S*I_V,
        dheight_dstart_acceleration=S_k*I+S*I_b*(S+k*S_k))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accepted-reference',type=Path,required=True)
    parser.add_argument('--warm-screen',type=Path,required=True)
    parser.add_argument('--actual-control-response',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    reference=read(args.accepted_reference)
    baseline=reference['frozen_profile']
    warm=read(args.warm_screen)
    profile=warm['warm_profile']
    a,b=ramp(baseline,4096),ramp(profile,4096)
    a0,b0=ramp(baseline,2048),ramp(profile,2048)
    response=read(args.actual_control_response)
    reference_sha=hashlib.sha256(args.accepted_reference.read_bytes()).hexdigest()
    if (response.get('finished') is not True
            or response['baseline']['profile']!=baseline
            or response['source_sha256'].get(str(args.accepted_reference))!=reference_sha):
        raise ValueError('The saved full actual response does not bind this exact accepted profile')
    partials=dict(delta=a['dheight_ddelta'],vu=a['dheight_dvu'],
                  start_acceleration=a['dheight_dstart_acceleration'])
    directions=[]
    for row in response['prescribed_low_core_responses']+response['additional_core_held_directions']:
        name=row.get('direction') or 'core_held_'+row['external_field']
        velocity=row['physical_profile_derivative']
        terms={key:partial*float(velocity.get(key,0.)) for key,partial in partials.items()}
        directions.append(dict(direction=name,physical_profile_derivative=velocity,
            low_core_derivative=row['core_derivative'][:3],
            initial_ramp_chain_rule_terms=terms,
            initial_ramp_total_directional_derivative=sum(terms.values()),
            doubled_initial_ramp_directional_derivative=2*sum(terms.values()),
            saved_full_field_equation_backward_error=row['equation_relative_backward_error']))
    if len(directions)!=5:
        raise ValueError('Expected the three exchanged core directions and two core-held controls')
    source={str(f):hashlib.sha256(f.read_bytes()).hexdigest()
            for f in (Path(__file__),args.accepted_reference,args.warm_screen,args.actual_control_response)}
    report=dict(scope=__doc__,source_sha256=source,
        formulas=dict(length='S=4delta/(V+sqrt(V^2+4kdelta/3))',
          speed='v(u)=V(3u^2-2u^3)+kS*u(1-u)^2',
          height='H=S*integral_0^1 sqrt(1-v(u)^2) du'),
        baseline=a,unsolved_warm=b,
        partial_derivative_scope='Each H_delta/H_vu/H_start_acceleration above holds the other two scalar ramp parameters fixed. It is not a core-held design derivative.',
        initial_ramp_partials_at_fixed_other_parameters=partials,
        saved_actual_full_field_directions=directions,
        core_held_vu_includes_induced_delta=True,
        actual_start_acceleration_response_available=False,
        no_actual_core_held_k0_claim_from_background_partial=True,
        length_change=b['length']-a['length'],
        one_initial_ramp_height_change=b['height']-a['height'],
        twice_initial_ramp_height_change=2*(b['height']-a['height']),
        whole_warm_diameter_sample=warm['warm_physical_cubic_geometry']['diameter_sample'],
        quadrature_2048_to_4096_height_changes=[a['height']-a0['height'],b['height']-b0['height']],
        physical_solves=0,physical_Jacobians=0,Node_workers=0,
        full_immersion_diameter_sensitivity=False,new_branch_acceptance=False,
        future_design_use='Use the five saved actual core/vu/first-turn directions together with the complete signed-curvature and diameter constraints. Any future k0 direction first requires its actual full-field response; the fixed-parameter background partial cannot supply it.')
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()

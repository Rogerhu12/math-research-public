#!/usr/bin/env python3
"""Consume R28 on a complete accepted fixed-g physical quintic packet.

This is the existing exact average-jet C2 repair, not a new PDE solve.
The original binary64 PPoly is never rewritten. Signed exact repaired
polynomials are generated one interval at a time; all six endpoint conditions
and all shared two-jets are verified as rational equalities. R28 bounds are
transported through the already certified fixed chart and include E12 for the
independent complete-height-mean consumer. The background/mean/PDE and closed
reach claims remain separate.
"""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import resource
import time
from flint import fmpq as Q
import root_exact_quintic_seams as R28
import strong_sameg_continuous_finite_field as finite

SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
R28_SHA='fd83b2cc2694153c2279efa3cee52294bef5098859a9b6217e510f1c0fa49859'
FINITE_SHA='8ceb28045607f7c533c134bf2281a00c644c5728c2bb3714a51238a4c4eefa12'
B=((Q(1),Q(2,5),Q(1,20)),(Q(5),Q(2),Q(1,4)),(Q(20),Q(12),Q(2)))
HL=((Q(1),Q(0),Q(0),Q(-10),Q(15),Q(-6)),
    (Q(0),Q(1),Q(0),Q(-6),Q(8),Q(-3)),
    (Q(0),Q(0),Q(1,2),Q(-3,2),Q(3,2),Q(-1,2)))
HR=tuple(tuple(sum((Q((-1)**(k+j)*math.comb(a,j))*HL[k][a]
                   for a in range(j,6)),Q(0)) for j in range(6)) for k in range(3))
COMPONENTS=('E00','E10','E01','E20','E11','E02','E12')
PHYSICAL=tuple(finite.PHYSICAL)


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)


def read_exact_record(value):
    return Q(int(value['numerator']),int(value['denominator']))


def pair(value):
    # str(fmpq) is an exact integer or a/b, never a decimal approximation.
    parts=str(value).split('/')
    return [parts[0],parts[1] if len(parts)==2 else '1']


def polynomial_record(polynomials):
    return [[pair(value) for value in row] for row in polynomials]


def piece(field,index):
    # Each returned row is ascending physical powers of (s-s_i).
    return tuple(tuple(R28.rational(field['c'][5-k,index,j]) for k in range(6))
                 for j in range(field['n']))


def left_jets(polynomials):
    return tuple((p[0],p[1],2*p[2]) for p in polynomials)


def right_jets(polynomials,length):
    return tuple(tuple(R28.jet_right(list(reversed(p)),length)) for p in polynomials)


def repaired_intervals(field):
    """Yield exact R28 signed polynomials and bounds without a rounded copy.

    field must be the unmodified result of finite.load_field().  No shared
    metadata or float array is mutated. The endpoint checks below are actual
    equalities on the complete binary input, not a floating tolerance.
    """
    x=tuple(R28.rational(value) for value in field['x'])
    count=len(x)-1
    current=piece(field,0)
    following=piece(field,1) if count>1 else None
    previous_original_right=None
    previous_repaired_right=None
    zero=tuple((Q(0),Q(0),Q(0)) for unused in range(field['n']))
    for index in range(count):
        h=x[index+1]-x[index]
        if h<=0:raise ValueError('A complete physical interval is not positive')
        old_left=left_jets(current);old_right=right_jets(current,h)
        next_left=left_jets(following) if following is not None else None
        dleft=(zero if index==0 else
            tuple(tuple((previous_original_right[j][k]-old_left[j][k])/2
                        for k in range(3)) for j in range(field['n'])))
        dright=(zero if index+1==count else
            tuple(tuple((next_left[j][k]-old_right[j][k])/2
                        for k in range(3)) for j in range(field['n'])))
        left_matrix=tuple(tuple(h**(k-a)*HL[k][a] for k in range(3)) for a in range(6))
        right_matrix=tuple(tuple(h**(k-a)*HR[k][a] for k in range(3)) for a in range(6))
        corrections=tuple(tuple(sum((left_matrix[a][k]*dleft[j][k]+
                                      right_matrix[a][k]*dright[j][k]
                                      for k in range(3)),Q(0))
                                for a in range(6)) for j in range(field['n']))
        repaired=tuple(tuple(current[j][a]+corrections[j][a] for a in range(6))
                       for j in range(field['n']))
        new_left=left_jets(repaired);new_right=right_jets(repaired,h)
        target_left=tuple(tuple(old_left[j][k]+dleft[j][k] for k in range(3))
                          for j in range(field['n']))
        target_right=tuple(tuple(old_right[j][k]+dright[j][k] for k in range(3))
                           for j in range(field['n']))
        if new_left!=target_left or new_right!=target_right:
            raise ArithmeticError('A signed R28 polynomial does not satisfy its exact six endpoint conditions')
        if index and new_left!=previous_repaired_right:
            raise ArithmeticError('Two exact repaired interior jets do not coincide')
        if (index==0 and new_left!=old_left) or (index+1==count and new_right!=old_right):
            raise ArithmeticError('An exterior endpoint jet was changed')
        errors=tuple(tuple(sum((B[ell][k]*h**(k-ell)*
                                      (abs(dleft[j][k])+abs(dright[j][k]))
                                      for k in range(3)),Q(0))
                           for j in range(field['n'])) for ell in range(3))
        right_jump=(zero if index+1==count else
            tuple(tuple(old_right[j][k]-next_left[j][k] for k in range(3))
                  for j in range(field['n'])))
        yield dict(index=index,s_left=x[index],s_right=x[index+1],length=h,
            original=current,repaired=repaired,correction=corrections,
            derivative_bounds=errors,right_unrepaired_jump=right_jump,
            complete_six_endpoint_equalities_checked=True,
            interior_shared_two_jet_checked=bool(index),
            exterior_two_jet_preserved=bool(index==0 or index+1==count))
        previous_original_right=old_right
        previous_repaired_right=new_right
        current=following
        following=piece(field,index+2) if index+2<count else None


def angular_weights(M):
    # Use exactly R28's original safe Cartesian weights, not a new optimized
    # bound: row0 radial mean; R/T rows m+1; Z rows m. Squaring pays order two.
    first=[1]+[2*(j+1)+1 for j in range(M)]*2+[2*(j+1) for j in range(M)]
    return tuple(first),tuple(value*value for value in first)


def sums(errors,first,second,gauge):
    e0,e1,e2=errors
    weighted=lambda row,weights:gauge*sum((value*weight for value,weight in zip(row,weights)),Q(0))
    return (gauge*sum(e0,Q(0)),gauge*sum(e1,Q(0)),weighted(e0,first),
        gauge*sum(e2,Q(0)),weighted(e1,first),weighted(e0,second),weighted(e1,second))


def update(target,name,value,index):
    if name not in target or value>target[name][0]:target[name]=(value,index)


def records(values):
    return {name:dict(bound=R28.record(value),interval=index) for name,(value,index) in values.items()}


def validate_chart(field,file):
    if finite.digest(file)!=finite.CHART_CERTIFICATE_SHA:
        raise ValueError('The actual exact q096 chart certificate is not the recorded one')
    chart=finite.read(file)
    if (chart['chart_source_sha256']!=finite.CHART_SOURCE_SHA or
            not all(chart['checks'].values()) or
            chart['error_input_columns']!=list(finite.AXES)):
        raise ValueError('The complete fixed-chart identity or exact gates differ')
    saved=field['record'];ci=chart['input']
    if (R28.rational(saved['meridian_length'])!=read_exact_record(ci['length']) or
            [R28.rational(v) for v in saved['chart_reference_coefficients']]!=
                [read_exact_record(v) for v in ci['coefficients']] or
            saved['chart_reference_frequencies']!=ci['frequencies']):
        raise ValueError('The input does not use this exact physical q096 chart')
    for key,default in (('chart_transition_start',0.),('chart_transition_end',1.)):
        if saved.get(key,default)!=default:
            raise ValueError('This chart certificate requires the original full-span blend')
    matrix={name:tuple(read_exact_record(v) for v in chart['exact_finite_field_transport_matrix'][name])
            for name in PHYSICAL}
    if any(len(row)!=6 or any(v<0 for v in row) for row in matrix.values()):
        raise ValueError('The chart transport is not a nonnegative six-column bound')
    return chart,matrix


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--chart-certificate',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Use a fresh exact R28 output path')
    if finite.digest(R28.__file__)!=R28_SHA or finite.digest(finite.__file__)!=FINITE_SHA:
        raise ValueError('The original R28 or complete accepted-field loader changed')
    field=finite.load_field(a.input)
    chart,matrix=validate_chart(field,a.chart_certificate)
    gauge=R28.rational(field['record']['gauge_amplitude'])
    if gauge<=0:raise ValueError('The recorded physical representation gauge must be positive')
    first,second=angular_weights(field['M'])
    maxima={};physical_maxima={}
    component_max=[[Q(0)]*field['n'] for unused in range(3)]
    component_locations=[[None]*field['n'] for unused in range(3)]
    jump_max=[(Q(0),None)]*3
    nonzero_jumps=0;completed=0;endpoint_equalities=0;shared_equalities=0
    coefficient_chain=hashlib.sha256();bound_chain=hashlib.sha256();minimum_h=None
    for row in repaired_intervals(field):
        index=row['index'];errors=row['derivative_bounds']
        values=sums(errors,first,second,gauge)
        physical={name:sum((w*v for w,v in zip(matrix[name],values[:6])),Q(0))
                  for name in PHYSICAL}
        for name,value in zip(COMPONENTS,values):update(maxima,name,value,index)
        for name,value in physical.items():update(physical_maxima,name,value,index)
        for ell in range(3):
            for j,value in enumerate(errors[ell]):
                if value>component_max[ell][j]:
                    component_max[ell][j]=value;component_locations[ell][j]=index
        if index+1<len(field['x'])-1:
            for j,jets in enumerate(row['right_unrepaired_jump']):
                for k,value in enumerate(jets):
                    if value:nonzero_jumps+=1
                    if abs(value)>jump_max[k][0]:
                        jump_max[k]=(abs(value),dict(knot=index+1,state=j))
        coefficient_chain.update(canonical(dict(index=index,
            physical_left=pair(row['s_left']),physical_right=pair(row['s_right']),
            repaired_ascending_physical_coefficients=polynomial_record(row['repaired']))).encode())
        bound_chain.update(canonical(dict(index=index,
            computational_bounds=[pair(v) for v in values],
            physical_bounds={name:pair(v) for name,v in physical.items()})).encode())
        minimum_h=row['length'] if minimum_h is None else min(minimum_h,row['length'])
        completed+=1;endpoint_equalities+=6*field['n']
        if index:shared_equalities+=3*field['n']
        if index%100==0:
            print(json.dumps(dict(event='exact_R28_actual_interval',
                complete=completed,total=len(field['x'])-1,
                seconds=time.monotonic()-started)),flush=True)
    expected=len(field['x'])-1
    if (completed!=expected or endpoint_equalities!=expected*6*field['n'] or
            shared_equalities!=max(0,expected-1)*3*field['n']):
        raise ArithmeticError('The complete actual interval verification did not finish')
    output=dict(scope=__doc__,source_sha256=SELF_SHA,
        theorem='results/R28-exact-quintic-seam-repair.md',
        original_R28_source_sha256=R28_SHA,accepted_field_loader_sha256=FINITE_SHA,
        input=field['binding'],modes=field['M'],state_count=field['n'],
        physical_interval_count=completed,all_raw_coefficient_chunks_verified=True,
        exact_binary64_interpretation=True,original_packet_modified=False,
        prescribed_background_metric_or_chart_changed=False,
        induced_metric_unchanged_claim=False,
        correction_definition='R28 exact average of the two original one-sided jets at every internal knot; original exterior one-sided two-jets preserved.',
        signed_repaired_coefficients_generated_for_every_interval=True,
        coefficient_representation='Exact rational coefficients in ascending powers of physical(s-s_left), available lazily from repaired_intervals(field); no rounded coefficient artifact.',
        exact_coefficient_stream_sha256=coefficient_chain.hexdigest(),
        exact_bound_stream_sha256=bound_chain.hexdigest(),
        exact_endpoint_equalities_verified=endpoint_equalities,
        exact_shared_internal_equalities_verified=shared_equalities,
        global_exterior_two_jets_preserved=True,
        repaired_state_curve_exactly_C2=True,
        original_state_curve_inferred_C2=False,
        nonzero_unrepaired_scalar_jet_jumps=nonzero_jumps,
        maximum_unrepaired_scalar_jumps=[dict(order=k,bound=R28.record(v),location=where)
                                         for k,(v,where) in enumerate(jump_max)],
        minimum_interval_length=R28.record(minimum_h),
        hermite_bernstein_bounds=[[str(v) for v in row] for row in B],
        computational_Fourier_jet_correction_bounds=records(maxima),
        complete_radial_mean_row0_included=True,
        physical_two_jet_correction_bounds_excluding_height_mean=records(physical_maxima),
        mean_certificate_intermediate_E12=records({'E12':maxima['E12']})['E12'],
        component_derivative_correction_bounds=[
            [dict(bound=R28.record(value),interval=component_locations[ell][j])
             for j,value in enumerate(component_max[ell])] for ell in range(3)],
        fixed_chart=dict(file=str(a.chart_certificate),sha256=finite.CHART_CERTIFICATE_SHA,
            source_sha256=finite.CHART_SOURCE_SHA,all_original_exact_chart_gates_passed=True),
        independent_height_mean_required=dict(position='add A0',s='add A1',theta=0,
            ss='add A2',s_theta=0,theta_theta=0),
        mean_and_reference_map_repaired=False,
        original_mean_quadrature_error_paid=False,
        actual_metric_equation_certified=False,
        closed_surface_or_reach_certified=False,
        convergence_to_exact_PDE_solution_claim=False,
        newton_solves=0,physical_RHS_calls=0,tail_workers=0,
        interpretation='An exact C2 state-curve representation with explicit perturbation of the original finite field. This does not transfer old PDE/metric/seam/reach gates to the repaired map without paying the displayed changes and the independent full mean/reference terms.',
        seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    content=(json.dumps(output,indent=2,allow_nan=False)+'\n').encode()
    if len(content)>=1_000_000 and a.out.suffix!='.gz':
        raise ValueError('The repository requires gzip for a data file over1MB')
    if a.out.suffix=='.gz':content=gzip.compress(content,mtime=0)
    if len(content)>=5_000_000:raise ValueError('The repository per-file limit is exceeded')
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open('xb') as stream:
        stream.write(content);stream.flush();os.fsync(stream.fileno())
    print(json.dumps(dict(event='exact_R28_actual_field_complete',output=str(a.out),
        sha256=finite.digest(a.out),intervals=completed,
        repaired_state_C2=True,complete_surface_C2_claim=False,
        physical_bounds={name:R28.record(value)['decimal_upper']
                         for name,(value,unused) in physical_maxima.items()},
        seconds=output['seconds'],peak_RSS_KiB=output['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()

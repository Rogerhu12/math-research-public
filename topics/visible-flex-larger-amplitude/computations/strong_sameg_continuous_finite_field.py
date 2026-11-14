#!/usr/bin/env python3
"""Exact all-s/all-psi bounds for two saved same-g finite cylindrical fields.

The complete vertical height mean is deliberately left as A0/A1/A2. This
program does not substitute sampled means, infer convergence to an exact
immersion, or assert that binary64 polynomial pieces join exactly C2.
It bounds both one-sided jets and reports exact finite-field knot jumps.
No Flow, RHS, Newton, tail worker or geometric solve is loaded.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import time
import numpy as np

HERE=Path(__file__).resolve().parent
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
CHART_CERTIFICATE_SHA='da4709e9bfdc6330e440c8a69a556ddd760ffd364bb05fa45a4caf28eff4e618'
CHART_SOURCE_SHA='7678b2b43984b74c94b948efb21ea014f75a25841ed40527e0b76c569190e0cb'
BASIS_SOURCE_SHA='e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2'
AXES=('E00','E10','E01','E20','E11','E02')
PHYSICAL=('position','s','theta','ss','s_theta','theta_theta')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)


def rational(value):
    return Q(int(value['numerator']),int(value['denominator']))


def rec(value):
    try:
        display=float(value)
        if not math.isfinite(display):
            display=None
    except OverflowError:
        display=None
    return dict(numerator=str(value.numerator),denominator=str(value.denominator),
                decimal_display=display)


def exact(value):
    value=float(value)
    if not math.isfinite(value):
        raise ValueError('A saved coefficient is not finite')
    return Q.from_float(value)


def local_file(parent,name):
    if Path(name).name!=name:
        raise ValueError('Stored chunks must have local basenames')
    return parent/name


def raw_grid(primary,saved):
    link=saved['raw_collocation_checkpoint']
    path=primary.parent/Path(link['file']).name
    if digest(path)!=link['sha256']:
        raise ValueError('The saved accepted raw manifest SHA differs')
    raw=read(path);identity=raw['identity']
    if (not raw.get('solver_success') or not identity['fixed'] or
            identity['profile']!=saved['frozen_profile'] or
            identity['gauge']!=saved['gauge_amplitude'] or
            identity['numerical_reference_knots']!=saved['numerical_meridian_chart']['reference_t']):
        raise ValueError('The full accepted fixed raw identity differs')
    spec=raw['arrays']['x']
    if spec['dtype']!='float64' or len(spec['shape'])!=1:
        raise ValueError('Expected the original one-dimensional raw t grid')
    values=np.empty(spec['shape'],dtype=np.float64);first=0;pieces=[]
    for part in spec['chunks']:
        file=local_file(path.parent,part['file'])
        if part['first']!=first or digest(file)!=part['sha256']:
            raise ValueError('Raw t chunk coverage or SHA differs')
        with gzip.open(file,'rb') as stream:
            array=np.load(stream,allow_pickle=False)
        if array.dtype!=np.float64 or array.shape!=(part['count'],):
            raise ValueError('Unexpected exact raw t chunk layout')
        values[first:first+len(array)]=array;first+=len(array)
        pieces.append(dict(file=str(file),sha256=part['sha256']))
    if (first!=values.size or not np.isfinite(values).all() or
            np.any(np.diff(values)<=0) or values[0]!=0 or values[-1]!=1):
        raise ValueError('Invalid original normalized t domain')
    return values,dict(file=str(path),sha256=link['sha256'],pieces=pieces)


def load_field(path):
    path=Path(path);saved=read(path)
    if (not saved.get('solver_success') or saved.get('audit_pending',True) or
            not saved['config'].get('actual_nonlinear_tail') or
            not saved['config'].get('fixed_metric')):
        raise ValueError('Both inputs must be accepted actual fixed views')
    M=int(saved['modes']);n=3*M+1
    if (int(saved['config'].get('base_mode',2))!=2 or
            saved['angular_chart']!='general-support-core-blend-v1' or
            saved['core']['frequencies']!=list(range(2,2*M+1,2))):
        raise ValueError('The explicit pinned base2 cylindrical layout is required')
    x=np.asarray(saved['mesh'],dtype=np.float64)
    if (x.ndim!=1 or len(x)<2 or not np.isfinite(x).all() or np.any(np.diff(x)<=0) or
            x[0]!=0. or x[-1]!=float(saved['meridian_length'])):
        raise ValueError('The complete physical PPoly grid differs')
    coefficients=np.empty((6,len(x)-1,n),dtype=np.float64)
    first=0;chunks=[]
    for part in saved['pp_coefficient_chunks']:
        file=local_file(path.parent,part['file'])
        lo=int(part['state_first']);hi=int(part['state_last_exclusive'])
        if lo!=first or not lo<hi<=n or digest(file)!=part['sha256'] or file.stat().st_size!=part['bytes']:
            raise ValueError('Physical coefficient chunk identity or coverage differs')
        with gzip.open(file,'rb') as stream:
            array=np.load(stream,allow_pickle=False)
        if array.dtype!=np.float64 or array.shape!=(6,len(x)-1,hi-lo) or not np.isfinite(array).all():
            raise ValueError('Expected all six exact physical quintic coefficients')
        coefficients[:,:,lo:hi]=array;first=hi
        chunks.append(dict(file=str(file),bytes=part['bytes'],sha256=part['sha256']))
    if first!=n:
        raise ValueError('The complete finite field was not restored')
    t,raw=raw_grid(path,saved)
    if len(t)!=len(x) or len(x)!=int(saved['nodes']):
        raise ValueError('Raw t and physical s grids have different node counts')
    return dict(path=path,record=saved,M=M,n=n,x=x,t=t,c=coefficients,
                binding=dict(file=str(path),sha256=digest(path),chunks=chunks,raw=raw))


def basis_weights(M):
    # Pinned row0=er; rows1..M=cos(2j psi)er;
    # rowsM+1..2M=sin(2j psi)et; rows2M+1..3M=cos(2j psi)ez.
    frequency=[2*j for j in range(1,M+1)]
    first=[1]+frequency+frequency+frequency
    second=[1]+[m*m+1 for m in frequency]*2+[m*m for m in frequency]
    return first,second


def moment_bounds(orders,first,second,gauge):
    v0,v1,v2=orders
    return [gauge*sum(v0,Q(0)),gauge*sum(v1,Q(0)),
        gauge*sum((Q(w)*v for w,v in zip(first,v0)),Q(0)),
        gauge*sum(v2,Q(0)),
        gauge*sum((Q(w)*v for w,v in zip(first,v1)),Q(0)),
        gauge*sum((Q(w)*v for w,v in zip(second,v0)),Q(0))]


def affine_power_matrix(shift,length):
    return [[Q(math.comb(k,j))*shift**(k-j)*length**j if k>=j else Q(0)
             for k in range(6)] for j in range(6)]


def normalized_power(coefficients,matrix):
    # Input coefficients are ascending powers of physical(s-original_left).
    return [sum((matrix[j][k]*coefficients[k] for k in range(j,6)),Q(0)) for j in range(6)]


def derivative_hull(power,length,order):
    degree=5-order
    derivative=[power[j+order]*Q(math.factorial(j+order),math.factorial(j))/length**order
                for j in range(degree+1)]
    bernstein=[sum((derivative[j]*Q(math.comb(i,j),math.comb(degree,j))
                    for j in range(i+1)),Q(0)) for i in range(degree+1)]
    return max(map(abs,bernstein))


def physical_bounds(values,matrix):
    return {name:sum((weight*value for weight,value in zip(matrix[name],values)),Q(0))
            for name in PHYSICAL}


def update(maxima,values,witness):
    for name,value in values.items():
        if name not in maxima or value>maxima[name][0]:
            maxima[name]=(value,dict(witness))


def records(maxima):
    return {name:dict(bound=rec(value),witness=witness) for name,(value,witness) in maxima.items()}


def exact_interval(field,index):
    return [[exact(field['c'][5-k,index,j]) for k in range(6)] for j in range(field['n'])]


def mapped_coarse_index(j,old_M,new_M):
    if j<=new_M:
        return j if j<=old_M else None
    if j<=2*new_M:
        mode=j-new_M
        return old_M+mode if mode<=old_M else None
    mode=j-2*new_M
    return 2*old_M+mode if mode<=old_M else None


def knot_jumps(field,transport,gauge):
    first,second=basis_weights(field['M'])
    exact_x=[exact(v) for v in field['x']]
    current=exact_interval(field,0);maxima={};raw_maxima={}
    all_zero=True
    for knot in range(1,len(exact_x)-1):
        next_coefficients=exact_interval(field,knot)
        length=exact_x[knot]-exact_x[knot-1]
        orders=[[],[],[]]
        for channel,(left,right) in enumerate(zip(current,next_coefficients)):
            for order in range(3):
                value=sum((left[k]*Q(math.factorial(k),math.factorial(k-order))*length**(k-order)
                           for k in range(order,6)),Q(0))
                value-=right[order]*math.factorial(order)
                orders[order].append(abs(value))
                all_zero=all_zero and value==0
        values=moment_bounds(orders,first,second,gauge)
        witness=dict(knot=knot,s=rec(exact_x[knot]))
        update(raw_maxima,dict(zip(AXES,values)),witness)
        update(maxima,physical_bounds(values,transport),witness)
        current=next_coefficients
    return dict(scope='Finite cylindrical field only; common background and separate height mean not tested',
        knots=max(0,len(exact_x)-2),all_finite_field_jet_jumps_exactly_zero=all_zero,
        computational_jet_jump_bounds=records(raw_maxima),
        physical_jet_jump_bounds_excluding_height_mean=records(maxima))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('coarse','fine','chart-certificate','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args();started=time.monotonic()
    if args.out.exists():
        raise FileExistsError('Use a fresh exact finite-field output path')
    if digest(args.chart_certificate)!=CHART_CERTIFICATE_SHA:
        raise ValueError('The actual exact q096 chart certificate differs')
    certificate=read(args.chart_certificate)
    if certificate['chart_source_sha256']!=CHART_SOURCE_SHA or not all(certificate['checks'].values()):
        raise ValueError('The continuous chart certificate did not pass')
    transport={name:[rational(value) for value in certificate['exact_finite_field_transport_matrix'][name]]
               for name in PHYSICAL}
    if certificate['error_input_columns']!=list(AXES) or any(value<0 for row in transport.values() for value in row):
        raise ValueError('The exact transport matrix schema differs')
    coarse,fine=load_field(args.coarse),load_field(args.fine)
    old,new=coarse['record'],fine['record']
    if fine['M']<=coarse['M'] or new.get('same_g_spectral_refinement',{}).get('solver_success') is not True:
        raise ValueError('The fine input must be the accepted explicit same-g spectral extension')
    common_keys=('frozen_profile','physical_tail_parameters','physical_tail_cut','gauge_amplitude',
                 'meridian_length','angular_chart','chart_reference_coefficients','chart_reference_frequencies')
    for key in common_keys:
        if canonical(old[key])!=canonical(new[key]):
            raise ValueError('A physical metric/reference datum changed: '+key)
    for key in ('reference_t','physical_s'):
        if canonical(old['numerical_meridian_chart'][key])!=canonical(new['numerical_meridian_chart'][key]):
            raise ValueError('The fixed numerical/physical knot map changed: '+key)
    for key,default in (('chart_transition_start',0.),('chart_transition_end',1.)):
        if old.get(key,default)!=default or new.get(key,default)!=default:
            raise ValueError('This exact chart certificate uses the original full-span blend')
    ci=certificate['input']
    if (exact(old['meridian_length'])!=rational(ci['length']) or
            [exact(value) for value in old['chart_reference_coefficients']]!=[rational(value) for value in ci['coefficients']] or
            old['chart_reference_frequencies']!=ci['frequencies']):
        raise ValueError('The exact continuous chart certificate has different real parameters')
    fine_t_bits={struct.pack('<d',float(value)) for value in fine['t']}
    if not all(struct.pack('<d',float(value)) in fine_t_bits for value in coarse['t']):
        raise ValueError('An original raw numerical t node was dropped')
    gauge=abs(exact(old['gauge_amplitude']))
    first,second=basis_weights(fine['M'])
    common=sorted(set(coarse['x'].tolist())|set(fine['x'].tolist()))
    exact_common=[exact(value) for value in common]
    coarse_x=[exact(value) for value in coarse['x']]
    fine_x=[exact(value) for value in fine['x']]
    index_old=index_new=0;cached_old=cached_new=-1
    raw_maxima={};physical_maxima={};mean_mixed_maxima={};chain=hashlib.sha256()
    for panel,(lo,hi) in enumerate(zip(exact_common,exact_common[1:])):
        while coarse_x[index_old+1]<=lo:
            index_old+=1
        while fine_x[index_new+1]<=lo:
            index_new+=1
        if hi>coarse_x[index_old+1] or hi>fine_x[index_new+1]:
            raise ValueError('The union is not a common physical partition')
        if cached_old!=index_old:
            old_coefficients=exact_interval(coarse,index_old);cached_old=index_old
        if cached_new!=index_new:
            new_coefficients=exact_interval(fine,index_new);cached_new=index_new
        length=hi-lo
        old_matrix=affine_power_matrix(lo-coarse_x[index_old],length)
        new_matrix=affine_power_matrix(lo-fine_x[index_new],length)
        orders=[[],[],[]]
        for j in range(fine['n']):
            pnew=normalized_power(new_coefficients[j],new_matrix)
            old_j=mapped_coarse_index(j,coarse['M'],fine['M'])
            pold=[Q(0)]*6 if old_j is None else normalized_power(old_coefficients[old_j],old_matrix)
            power=[a-b for a,b in zip(pnew,pold)]
            for order in range(3):
                orders[order].append(derivative_hull(power,length,order))
        values=moment_bounds(orders,first,second,gauge)
        witness=dict(panel=panel,lo=rec(lo),hi=rec(hi),coarse_interval=index_old,fine_interval=index_new)
        update(raw_maxima,dict(zip(AXES,values)),witness)
        update(physical_maxima,physical_bounds(values,transport),witness)
        # velocity_s differentiates F_psipsi once in s. This E12 is an
        # intermediate input to the independent mean A2 certificate.
        e12=gauge*sum((Q(w)*v for w,v in zip(second,orders[1])),Q(0))
        update(mean_mixed_maxima,dict(E12=e12),witness)
        chain.update(canonical(dict(panel=panel,lo=rec(lo),hi=rec(hi),bounds=[rec(v) for v in values],mean_E12=rec(e12))).encode())
        if panel%100==0:
            print(json.dumps(dict(event='exact_finite_field_panel',completed=panel+1,total=len(common)-1,
                seconds=time.monotonic()-started)),flush=True)
    jumps={name:knot_jumps(field,transport,gauge) for name,field in (('coarse',coarse),('fine',fine))}
    result=dict(scope=__doc__,source_sha256=SELF_SHA,
        source_basis_sha256=BASIS_SOURCE_SHA,source_chart_sha256=CHART_SOURCE_SHA,
        coarse=coarse['binding'],fine=fine['binding'],
        chart_certificate=dict(file=str(args.chart_certificate),sha256=CHART_CERTIFICATE_SHA),
        original_t_nodes_retained_bitwise=True,all_common_physical_intervals_covered=True,
        physical_interval_count=len(common)-1,all_angular_points_covered=True,
        complete_radial_mean_row0_included=True,all_original_and_new_finite_modes_included=True,
        gauge=rec(gauge),coarse_modes=coarse['M'],fine_modes=fine['M'],
        common_partition_bound_stream_sha256=chain.hexdigest(),
        computational_finite_field_jet_bounds=records(raw_maxima),
        mean_certificate_intermediate_mixed_bound=records(mean_mixed_maxima),
        physical_finite_field_jet_bounds_excluding_height_mean=records(physical_maxima),
        independent_height_mean_terms=dict(position='add A0',s='add A1',theta=0,ss='add A2',s_theta=0,theta_theta=0),
        mean_anchor_rule='If the exact means share H(0)=0 and sup|delta H prime|<=A1, one may take A0<=L*A1. Numeric quadrature and angular alias errors still require separate payment.',
        exact_finite_field_knot_jumps=jumps,
        continuous_complete_map_C2_bound=False,convergence_to_exact_solution_claim=False,
        physical_RHS_calls=0,tail_workers=0,newton_solves=0,
        interpretation='Binary64 stored quintic coefficients/knots are exact real numbers. The hull includes both one-sided limits; no floating-point evaluation error or exact knot continuity is inferred.',
        limitations=['A complete mean certificate is absent; A0/A1/A2 are not set to zero.',
            'This is a two-finite-field difference, not an a posteriori error bound to the exact PDE.',
            'Uniform angular bounds do not alone establish the separate closed-family phase action or reach.',
            'A nonzero exact knot jump must be paid by a separately declared C2 repair or exact Hermite interpretation.'],
        seconds=time.monotonic()-started)
    data=(json.dumps(result,indent=2,allow_nan=False)+'\n').encode()
    if len(data)>=5_000_000:
        raise ValueError('Exact finite-field result exceeds the repository file-size limit')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('xb') as stream:
        stream.write(data);stream.flush();os.fsync(stream.fileno())
    print(json.dumps(dict(event='exact_finite_field_comparison_complete',file=str(args.out),
        sha256=digest(args.out),complete_map_C2_claim=False,seconds=result['seconds'])),flush=True)


if __name__=='__main__':
    main()

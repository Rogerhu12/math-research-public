#!/usr/bin/env python3
"""Exact C2 repair bounds for the stored Fourier-state quintic pieces.

All binary64 coefficients and physical mesh points are interpreted as exact
rationals. At an internal knot, the repaired common jets are the average of
the two one-sided value/first/second jets. Each piece receives the unique
quintic endpoint-jet correction. This program computes exact bounds without
changing the saved packet. It does not repair the background profile, certify
isometry, or turn an open prefix into a closed surface.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import resource
import time
import numpy as np
from flint import fmpq


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rational(value):
    return fmpq(*float(value).as_integer_ratio())


def record(value):
    exact=Fraction(str(value))
    upper=float(exact)
    if Fraction.from_float(upper)<exact:
        upper=math.nextafter(upper,math.inf)
    return dict(numerator=str(exact.numerator),denominator=str(exact.denominator),
                decimal_upper=upper)


def jet_right(coefficients,h):
    value=coefficients[0];first=fmpq(0);second=fmpq(0)
    for coefficient in coefficients[1:]:
        value,first,second=value*h+coefficient,first*h+value,second*h+2*first
    return [value,first,second]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();started=time.monotonic()
    raw=args.input.read_bytes()
    packet=json.loads(gzip.decompress(raw) if args.input.suffix=='.gz' else raw)
    if not packet.get('solver_success') or packet.get('audit_pending',False):
        raise ValueError('A complete successful physical packet is required')
    if packet['angular_chart']!='general-support-core-blend-v1':
        raise ValueError('Only the recorded cylindrical Fourier-state representation is supported')
    M=int(packet['config']['modes']);base=int(packet['config'].get('base_mode',2))
    q=rational(packet['gauge_amplitude']);chunks=[];end=0
    for item in packet['pp_coefficient_chunks']:
        path=args.input.parent/item['file']
        if Path(item['file']).name!=item['file'] or sha(path)!=item['sha256'] or item['state_first']!=end:
            raise ValueError('Coefficient identity or layout mismatch')
        with gzip.open(path,'rb') as stream:chunk=np.load(stream,allow_pickle=False)
        end=item['state_last_exclusive'];chunks.append(chunk)
    coefficients=np.concatenate(chunks,axis=2)
    mesh=list(map(rational,packet['mesh']));count=len(mesh)-1;states=3*M+1
    if coefficients.shape!=(6,count,states) or not q>0:
        raise ValueError('Unexpected quintic shape or nonpositive gauge')
    if any(b<=a for a,b in zip(mesh[:-1],mesh[1:])):
        raise ValueError('Physical knots must be strictly ordered')
    # Bernstein coefficient absolute maxima for the three left Hermite
    # basis functions, with the right functions related by reflection.
    B=[[fmpq(1),fmpq(2,5),fmpq(1,20)],
       [fmpq(5),fmpq(2),fmpq(1,4)],
       [fmpq(20),fmpq(12),fmpq(2)]]
    angular1=[1]+[base*(j+1)+1 for j in range(M)]*2+[base*(j+1) for j in range(M)]
    angular2=[w*w for w in angular1]
    names=['position','radial_first','radial_second','angle_first','angle_second','mixed']
    worst={name:(fmpq(0),None) for name in names}
    max_jump=[(fmpq(0),None)]*3
    left=[[fmpq(0)]*3 for _ in range(states)]
    nonzero=0;minimum_h=None
    for i in range(count):
        h=mesh[i+1]-mesh[i]
        if minimum_h is None or h<minimum_h:minimum_h=h
        right=[]
        for j in range(states):
            if i+1==count:
                jump=[fmpq(0)]*3
            else:
                rr=jet_right([rational(v) for v in coefficients[:,i,j]],h)
                ll=[rational(coefficients[5,i+1,j]),rational(coefficients[4,i+1,j]),2*rational(coefficients[3,i+1,j])]
                jump=[a-b for a,b in zip(rr,ll)]
                for k,v in enumerate(jump):
                    if v:nonzero+=1
                    if abs(v)>max_jump[k][0]:max_jump[k]=(abs(v),dict(knot=i+1,state=j))
            right.append(jump)
        errors=[]
        for derivative in range(3):
            errors.append([sum((B[derivative][k]*h**(k-derivative)*(abs(left[j][k])+abs(right[j][k]))/2
                                for k in range(3)),fmpq(0)) for j in range(states)])
        bounds=[q*sum(row,fmpq(0)) for row in errors]
        bounds+=[q*sum((w*v for w,v in zip(weights,row)),fmpq(0))
                 for weights,row in ((angular1,errors[0]),(angular2,errors[0]),(angular1,errors[1]))]
        for name,bound in zip(names,bounds):
            if bound>worst[name][0]:worst[name]=(bound,dict(interval=i,s_left=packet['mesh'][i],s_right=packet['mesh'][i+1]))
        left=right
    output=dict(scope=__doc__,input=str(args.input),input_sha256=sha(args.input),
        source_sha256=sha(Path(__file__)),physical_state_count=states,interval_count=count,
        internal_seam_count=count-1,nonzero_scalar_jet_jumps=nonzero,
        physical_mesh_exact_binary=True,coefficients_exact_binary=True,
        correction_definition='Common interior jets are exact averages; exterior endpoint jets stay unchanged; unique degree-at-most-five Hermite correction on each original physical interval.',
        repaired_vector_curve_is_exactly_C2=True,original_packet_modified=False,
        background_profile_repaired=False,exact_isometry_certified=False,
        min_interval_length=record(minimum_h),hermite_bernstein_bounds=[[str(v) for v in row] for row in B],
        max_unrepaired_state_jump=[dict(order=k,**record(v),location=where) for k,(v,where) in enumerate(max_jump)],
        cartesian_Fourier_perturbation_bounds={name:dict(**record(v),location=where) for name,(v,where) in worst.items()},
        coordinate_scope='Derivatives in physical meridian s and computational angle eta. Material-angle conversion is separate; the same smooth reference map must be added to both expressions.',
        seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),seconds=output['seconds'],peak_RSS_KiB=output['peak_RSS_KiB'],
        bounds={k:v['decimal_upper'] for k,v in output['cartesian_Fourier_perturbation_bounds'].items()})),flush=True)


if __name__=='__main__':main()

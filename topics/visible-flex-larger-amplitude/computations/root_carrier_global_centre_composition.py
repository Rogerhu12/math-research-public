#!/usr/bin/env python3
"""Compose the actual old/carrier reference bridges in ONE left gauge.

This is exact rational arithmetic on two completed archived ledgers.
It never asserts existence of the true exterior solution, an exact normal,
or portability to a different core/metric/reference height vector.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import json
from pathlib import Path

DRIFT='2026-11-13-geometry-original64-centre-drift-r1-summary.json'
BRIDGE='2026-11-13-geometry-same-measure-r1-summary.json'

def dyadic(a):
    n,e=int(a[0]),int(a[1])
    return Q(n)*(Q(2)**e)

def rational(x):
    return {'numerator':str(x.numerator),'denominator':str(x.denominator),
            'display_only':float(x)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--notes',type=Path,required=True)
    ap.add_argument('--drift-sha256',required=True)
    ap.add_argument('--bridge-sha256',required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise FileExistsError('Use a new output path')
    inputs={}
    data=[]
    for filename,expected in ((DRIFT,a.drift_sha256),(BRIDGE,a.bridge_sha256)):
        p=a.notes/filename;b=p.read_bytes();actual=hashlib.sha256(b).hexdigest()
        if actual!=expected:raise ValueError('Actual archived input changed: '+filename)
        inputs[filename]=actual;data.append(json.loads(b))
    d,b=data
    if not (all(v is True for v in d['gates'].values()) and
            all(v is True for v in b['gates'].values())):
        raise ValueError('Every original completed mathematical gate is required')
    if not (d['cell']==0 and d['segment']==7 and d['original_leaves']==1740
            and d['positive_bins']==64 and b['old_leaves']==37
            and b['new_common_leaves']==111):
        raise ValueError('The complete intended source cover is required')
    z=b['complete_difference_maxima']
    original_drift=dyadic(d['all_segment_radial_to_centred_position_upper'])
    radial_bridge=dyadic(z['radial_reference_position_left_gauge'])
    centred_horizontal=dyadic(z['centred_xy'])
    centred_height=dyadic(z['h_left'])
    reference_vector=dyadic(z['reference_vector'])
    centred_bridge=centred_horizontal+centred_height
    total=original_drift+radial_bridge+centred_bridge
    cap=Q(2663,10**10)
    gates={
        'all_original_two_ledger_gates':True,
        'actual_old_drift_positive':original_drift>0,
        'centred_euclidean_bridge_less_than_2168e_12':centred_bridge<Q(2168,10**12),
        'carrier_whole_seg7_drift_less_than_2663e_10':total<cap,
        'reference_vector_less_than_576e_9':reference_vector<Q(576,10**9),
        'conditional_position_8192_plus_reference_less_than_8000':Q(1,8192)+total<Q(1,8000),
        'conditional_vector_4096_plus_reference_less_than_4000':Q(1,4096)+reference_vector<Q(1,4000),
    }
    out={
        'status':'Exact composition of actual reference comparisons; true exterior remains unpaid',
        'inputs_sha256':inputs,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'gauge':'sigma(r,0)=0; one common left circle; Delta h0(rL)=0; C_O(rL)=C_CF(rL)=0; no resets',
        'scope':'Only the original cell0/seg7 metric and original R48/carrier references',
        'terms':{k:rational(v) for k,v in {
            'old_all_eight_parts_drift':original_drift,'left_radial_bridge':radial_bridge,
            'centred_horizontal_bridge':centred_horizontal,'complete_height_bridge':centred_height,
            'centred_euclidean_bridge':centred_bridge,'carrier_all_eight_parts_drift':total,
            'old_carrier_reference_vector_difference':reference_vector}.items()},
        'rational_cap':rational(cap),'strict_margin':rational(cap-total),
        'gates':gates,'all_gates':all(gates.values()),
        'conditional_last_two_gates_are_not_true_solution_error_certificates':True,
        'full_closed_surface_or_reach_claimed':False,
    }
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    if not out['all_gates']:raise ArithmeticError('An exact composition bound failed')
    print(json.dumps({'all_gates':True,'carrier_drift_upper_display':float(total),
        'strict_margin_display':float(cap-total),'output':str(a.out)}))

if __name__=='__main__':main()

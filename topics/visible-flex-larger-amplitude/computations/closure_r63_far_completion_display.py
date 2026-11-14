#!/usr/bin/env python3
"""Exact displayed-bound consequences of the explicit R63 far completion."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def e(d):
    m,k=int(d['mantissa']),int(d['binary_exponent'])
    return Fraction(m << k) if k>=0 else Fraction(m,1 << -k)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Use a fresh display-ledger path')
    d=json.loads(a.input.read_text())
    if not d['all_gates']:raise ValueError('The full exact completion is required')
    limits={2:(Fraction('9.6530184e-48'),Fraction('9.6530185e-48')),
            4:(Fraction('-1.057652e-52'),Fraction('1.409564e-52'))}
    gates={}
    for row in d['corrected_R70_rows']:
        m=row['mode'];v=row['complete_corrected_centre_interval']
        gates['R70_mode'+str(m)+'_lower']=limits[m][0]<e(v['lower'])
        gates['R70_mode'+str(m)+'_upper']=e(v['upper'])<limits[m][1]
    for row in d['corrected_R71_rows']:
        m=row['mode'];v=row['complete_corrected_centre_interval']
        gates['R71_mode'+str(m)+'_display'] = max(abs(e(v['lower'])),abs(e(v['upper']))) < (Fraction('1.088656e-56') if m==2 else Fraction('1.409564e-52'))
    for row in d['corrected_R63_cut_rows']:
        m=row['mode']
        gates['R63_mode'+str(m)+'_complete_difference_display']=e(row['complete_actual_minus_candidate_Wsigma1_upper']['upper']) < (Fraction('2.686774e-37') if m==2 else Fraction('2.321477e-43'))
    result={'status':'Exact displayed bounds after the explicit nonzero far addition',
        'gates':gates,'all_gates':all(gates.values()),
        'input':str(a.input),'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic':'Exact fractions.Fraction only; no floating comparison'}
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
    if not result['all_gates']:raise SystemExit(1)


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Exact presentation inequalities for the completed R71 two-cell candidate.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def q(e):
    return F(int(e['mantissa']))*F(2)**int(e['binary_exponent'])


def cap(r):
    return max(abs(q(r['lower'])), abs(q(r['upper'])))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('input','old','out'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists(): raise FileExistsError('Use a fresh rational ledger')
    d=json.loads(a.input.read_text());old=json.loads(a.old.read_text())
    if not d['all_gates'] or not old['all_gates'] or d['panels']!=10793:
        raise ValueError('Both completed certificates are required')
    checks=[]
    def lt(name,value,bound):
        ok=value<F(bound)
        checks.append(dict(name=name,strict_bound=bound,passed=ok))
        if not ok: raise ArithmeticError(name)
    lt('physical shared height change',cap(d['exact_candidate_change']['physical_height_change']),'3.340350e-47')
    lt('complete mean total height change',cap(d['complete_mean_height_total_change_upper']),'1.005408e-62')
    rows={r['mode']:r for r in d['functional_rows']}
    for m,b in ((2,'1.542922e-65'),(4,'3.457076e-61')):
        lt('complete source functional change m'+str(m),cap(rows[m]['complete_new_minus_old_forcing_upper']),b)
    lt('new complete m2 centre absolute value',cap(rows[2]['new_complete_candidate_centre_residual_canonical_Q']),'1.088656e-56')
    lt('new complete m2 old-axis ratio',cap(rows[2]['new_axis_ratio_upper']),'136.6721')
    cells={}
    for r in d['cell_reports']:
        p=Path(r['path'])
        if sha(p)!=r['sha256']: raise ValueError('A completed cell changed')
        cells[r['cell']]=json.loads(p.read_text())
    for n,b in ((11,'1.565127e-28'),(10,'1.320659e-30')):
        lt('complete state change cell'+str(n),cap(cells[n]['whole_cell']['dR']['upper']),b)
    for n,b in ((11,'3.429795e-18'),(10,'1.118059e-13')):
        lt('whole connecting state domain cell'+str(n),cap(cells[n]['whole_cell']['Rnew']['upper']),b)
    old2=next(r for r in old['rows'] if r['mode']==2)['complete_candidate_centre_residual_canonical_Q']
    gain=q(old2['lower'])/cap(rows[2]['new_complete_candidate_centre_residual_canonical_Q'])
    scope=dict(gain_strictly_more_than29_bits=gain>2**29,
        gain_not_claimed30_bits=gain<2**30,
        node10_complete_linear_residual_explicitly_unchanged=d['further_outer_linear_centre_residual_unchanged'],
        complete_outer_solution_not_claimed=d['complete_outer_nonlinear_Green_Schur_not_claimed'])
    if not all(scope.values()): raise ArithmeticError('Scope/gain claim failed')
    a.out.write_text(json.dumps(dict(status='Exact rational R71 presentation bounds',all_gates=True,
        checks=checks,scope=scope,input_hashes={str(a.input):sha(a.input),str(a.old):sha(a.old)},
        source_sha256=sha(Path(__file__))),indent=2)+'\n')
    print(json.dumps(dict(event='complete',output=str(a.out),all_gates=True,checks=len(checks))))


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Enlarge parameter axes inside the SAME already paid lifted-state budget.

All arithmetic is exact Fraction.  Each new axis v_j is chosen so that
A_nj*v_j <= R*l_n for every cell and E_j*v_j/Z <= R*e.  The old full641
lifted-map and domain inequalities therefore remain valid.  No new
fixed-point solve, kernel or approximation is introduced.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()


def pair(m,e):
    return F(m*(1<<e),1) if e>=0 else F(m,1<<(-e))


def upper(record):
    return pair(int(record['upper']['mantissa']),int(record['upper']['binary_exponent']))


def lower(record):
    return pair(int(record['lower']['mantissa']),int(record['lower']['binary_exponent']))


def compact(record):return pair(int(record[0]),int(record[1]))


def endpoint(q):
    if q.denominator & (q.denominator-1):raise ValueError('A dyadic endpoint is required')
    return dict(mantissa=str(q.numerator),binary_exponent=1-q.denominator.bit_length())


def record(lo,hi=None):
    if hi is None:hi=lo
    return dict(lower=endpoint(lo),upper=endpoint(hi))


def floorlog2(q):
    if not q>0:raise ValueError('A strictly positive ratio is required')
    e=q.numerator.bit_length()-q.denominator.bit_length()
    if pair(1,e)>q:e-=1
    if not pair(1,e)<=q<pair(1,e+1):raise AssertionError('Exact power-of-two floor failed')
    return e


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('lifts','parameter-ball','axes','out'):
        p.add_argument('--'+name,type=Path,required=True)
    args=p.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh balanced-axis ledger')
    docs={};hashes={}
    for name in ('lifts','parameter_ball','axes'):
        path=getattr(args,name);docs[name],hashes[str(path)]=read(path)
    lifts,domain,axes=(docs[name] for name in ('lifts','parameter_ball','axes'))
    if not domain['all_gates'] or not all(domain['gates'].values()) or not all(axes['checks'].values()):
        raise ValueError('Use the actual paid full641 parameter domain and real physical-axis ledger')
    if domain['input_hashes'].get(str(args.lifts))!=hashes[str(args.lifts)]:raise ValueError('The actual true parameter columns differ')
    for name in ('lifts','parameter_ball'):
        if axes['input_hashes'].get(str(getattr(args,name)))!=hashes[str(getattr(args,name))]:
            raise ValueError('The true cut-height axes use another parameter domain')
    if lifts['modes']!=list(range(2,93,2)) or lifts['cells']!=list(range(12,225)):
        raise ValueError('All46 modes and all213 true cells are required')
    R=upper(domain['parameter_radius']);Z=upper(lifts['parameter_far_scale'])
    if R!=lower(domain['parameter_radius']) or Z!=lower(lifts['parameter_far_scale']):raise ValueError('The chosen radii must be exact points')
    ell=[upper(row['l']) for row in lifts['parameter_cell_lift']]
    e=upper(lifts['parameter_far_lift'])
    A=[[compact(v) for v in row] for row in lifts['A_upper']]
    E=[compact(v) for v in lifts['far_E_upper']]
    if len(A)!=213 or any(len(row)!=46 for row in A) or len(E)!=46:raise ValueError('The complete true lift is missing')
    hfactor=axes['Q_to_physical_H_factor'];hlog=axes['Q_to_physical_H_log2_factor']
    units=[];rows=[]
    for j in range(46):
        bounds=[(R*ell[n]/A[n][j],'cell',12+n) for n in range(213) if A[n][j]>0]
        bounds.append((R*e*Z/E[j],'far',225))
        bound,kind,where=min(bounds,key=lambda x:x[0])
        exponent=floorlog2(bound);unit=pair(1,exponent);old=R*upper(domain['parameter_units'][j])
        if not unit>=old:raise AssertionError('The new axis must contain the originally paid dyadic axis')
        if not all(A[n][j]*unit<=R*ell[n] for n in range(213)) or not E[j]*unit<=R*e*Z:
            raise AssertionError('A new axis exceeds a previously paid physical/far lift budget')
        units.append(unit)
        rows.append(dict(j=j+1,physical_mode=2*(j+1),canonical_Q_axis=record(unit),canonical_Q_axis_log2=exponent,
            previous_Q_axis_log2=axes['rows'][j]['canonical_Q_axis_log2'],
            enlargement_log2=exponent-axes['rows'][j]['canonical_Q_axis_log2'],
            limiting_lift=dict(kind=kind,cell=where),
            actual_physical_height_axis=record(lower(hfactor)*unit,upper(hfactor)*unit),
            guaranteed_physical_height_axis=record(lower(hfactor)*unit),
            actual_physical_height_axis_log2=record(lower(hlog)+exponent,upper(hlog)+exponent)))
    newell=[max(A[n][j]*units[j] for j in range(46)) for n in range(213)]
    newe=max(E[j]*units[j]/Z for j in range(46))
    checks=dict(all46_axes_present=len(rows)==46,all46_new_axes_positive=all(v>0 for v in units),
        all46_previous_axes_contained=all(row['enlargement_log2']>=0 for row in rows),
        all213_lift_budgets_not_increased=all(newell[n]<=R*ell[n] for n in range(213)),
        complete_far_lift_budget_not_increased=newe<=R*e,
        all641_original_lifted_inclusions_inherited=domain['gates']['all641_lifted_map_inclusions'],
        original_full_state_mean_far_and_metric_inherited=all(domain['gates'].values()))
    result=dict(status='Balanced full46 parameter axes certified inside the unchanged already-paid lifted budget',
        checks=checks,all_gates=all(checks.values()),new_parameter_radius=record(F(1)),
        new_parameter_norm='sum_j |delta Q_(2j)(b)|/v_j <=1, with exact positive dyadic v_j in rows; an l1 ball, not the product of its axis intervals.',
        original_scalar_radius=domain['parameter_radius'],original_scalar_radius_log2=domain['parameter_radius_log2'],
        unchanged_original641_radii_and_J_and_W=True,
        inheritance_reason='Every actual parameter lift in the new l1 ball has each cell norm <= max_j A_nj*v_j <=R*l_n and true far norm <=R*e. Monotonicity of the same positive parameter columns transfers every original strict641 lifted inclusion and full-state domain unchanged.',
        true_cut_radius=axes['true_cut_radius'],Q_to_physical_H_factor=hfactor,Q_to_physical_H_log2_factor=hlog,
        physical_height_convention='H=b^4 Q at the same true node12; no extra w. Listed positive lower endpoints give guaranteed physical axis intercepts.',
        rows=rows,cells=[dict(cell=12+n,lift_upper=record(newell[n]),retained_budget=record(R*ell[n])) for n in range(213)],
        far_lift_upper=dict(numerator=str(newe.numerator),denominator=str(newe.denominator)),
        input_hashes=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        exact_arithmetic='fractions.Fraction only; dyadic output bounds and exact rational inequalities',
        new_matrix_inverses=0,new_radial_integrations=0,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='done',checks=checks,
        first_Q_axis_log2=rows[0]['canonical_Q_axis_log2'],last_Q_axis_log2=rows[-1]['canonical_Q_axis_log2'],
        maximum_axis_enlargement_bits=max(row['enlargement_log2'] for row in rows),
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    if not all(checks.values()):raise SystemExit(1)


if __name__=='__main__':main()

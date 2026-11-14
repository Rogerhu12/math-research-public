#!/usr/bin/env python3
"""Index the completed R125 exact dyadic kernels without changing their bounds.

Read and hash every original target/cut output, check all modes and both
component suprema, and expose Gamma[norm][target][source][power_index].
The max-mode matrix requires a shared sum of radial modal suprema at source.
This is an exact Fraction interface check, not a new Green computation.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

MODES = list(range(2,93,2))
POWERS = [2,1,0]
NORMS = ['sigma0','common_sigma']
SOURCE_SHA = '13daf8abed64b73681b7db6f768d745c6945a582a2a1e1c202ce7b78bd6c8d5a'
SUMMARY_SHA = '6375e1ada4c9124482f9d8f92875c0f4cb26e31354e7037f1e3aa5d74fde7a95'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    b = Path(path).read_bytes()
    return json.loads(gzip.decompress(b) if str(path).endswith('.gz') else b)


def exact(point):
    m,e = map(int,point)
    return Q(m)*(Q(2)**e)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--summary',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    began=time.monotonic()
    if args.out.exists() or args.out.suffix!='.gz':
        raise ValueError('Use a fresh compressed exact aggregate index')
    if digest(args.summary)!=SUMMARY_SHA:
        raise ValueError('Require the completed frozen R125 original summary')
    d=read(args.summary)
    if (not d['all_gates'] or d['modes']!=MODES or d['powers']!=POWERS
            or d['norms']!=NORMS or len(d['comparison_partition'])!=25
            or d['original_parent_count']!=10793 or d['complete_geometry_subpanels']!=10878
            or SOURCE_SHA not in d['source_and_input_sha256'].values()):
        raise ValueError('The completed physical kernel object differs')
    matrix=lambda:{n:[[[None for _ in POWERS] for _ in range(25)] for _ in range(25)] for n in NORMS}
    maximum,summed=matrix(),matrix()
    identities=[]
    comparisons=0
    target_ids=[]
    for rec in d['target_records']:
        i=rec['target_block'];target_ids.append(i)
        p=Path(rec['path'])
        if digest(p)!=rec['sha256'] or p.stat().st_size!=rec['bytes']:
            raise ValueError('An actual target kernel chunk changed')
        t=read(p)
        if (t['target_block']!=i or t['target_partition']!=d['comparison_partition'][i]
                or t['modes']!=MODES or t['powers']!=POWERS or t['norms']!=NORMS
                or len(t['kernels'])!=75 or not t['max_mode_aggregate_requires_common_source_mass']):
            raise ValueError('Target kernel schema or source-norm qualification differs')
        seen=set()
        for row in t['kernels']:
            j,power=row['source_block'],row['power'];pi=POWERS.index(power)
            if not 0<=j<25 or (j,pi) in seen or [v['mode'] for v in row['mode_rows']]!=MODES:
                raise ValueError('Every target/source/material requires all46 modes once')
            seen.add((j,pi))
            for norm in NORMS:
                values=[]
                for v in row['mode_rows']:
                    pair=[exact(v[norm][k]) for k in ('P','K')]
                    if any(q<0 for q in pair):
                        raise ArithmeticError('A physical kernel bound became negative')
                    values.append(sum(pair,Q(0)));comparisons+=2
                a=row['aggregates'][norm]
                if (exact(a['max_mode_P_plus_K'])<max(values)
                        or exact(a['sum_modes_P_plus_K'])<sum(values,Q(0))):
                    raise ArithmeticError('An aggregate omitted a component or modal sup')
                comparisons+=2
                maximum[norm][i][j][pi]=a['max_mode_P_plus_K']
                summed[norm][i][j][pi]=a['sum_modes_P_plus_K']
        if len(seen)!=75:
            raise ValueError('Missing target/source/material entries')
        identities.append(rec)
    if target_ids!=list(range(25)) or any(v is None for n in NORMS for row in maximum[n] for col in row for v in col):
        raise ValueError('The complete25 by25 by3 matrix was not populated')
    cutrec=d['cut_record'];p=Path(cutrec['path'])
    if digest(p)!=cutrec['sha256'] or p.stat().st_size!=cutrec['bytes']:
        raise ValueError('The original46-mode cut kernel changed')
    cut=read(p)
    cutmax={name:[[None for _ in POWERS] for _ in range(25)] for name in ('S','T')}
    cutsum={name:[[None for _ in POWERS] for _ in range(25)] for name in ('S','T')}
    seen=set()
    for row in cut['rows']:
        j,power=row['source_block'],row['power'];pi=POWERS.index(power)
        if (j,pi) in seen or [v['mode'] for v in row['mode_rows']]!=MODES:
            raise ValueError('The actual cut kernel omitted or repeated modes')
        seen.add((j,pi))
        values=[exact(v['raw_original_axis_cut']) for v in row['mode_rows']]
        if any(v<0 for v in values):raise ArithmeticError('Negative actual cut coefficient')
        comparisons+=46
        for name,subset in (('S',values[:6]),('T',values[6:])):
            if (exact(row[name+'_max_mode'])<max(subset)
                    or exact(row[name+'_sum_modes'])<sum(subset,Q(0))):
                raise ArithmeticError('An actual cut aggregate lost its norm')
            comparisons+=2
            cutmax[name][j][pi]=row[name+'_max_mode']
            cutsum[name][j][pi]=row[name+'_sum_modes']
    if len(seen)!=75:raise ValueError('All25 sources and3 materials are required at cut')
    result=dict(schema='r125-low46-block-kernel-index-v1',scope=__doc__,all_exact_checks_passed=True,
        exact_comparisons=comparisons,source_sha256=digest(__file__),original_summary_sha256=SUMMARY_SHA,
        original_producer_sha256=SOURCE_SHA,powers=POWERS,modes=MODES,norms=NORMS,
        comparison_partition=d['comparison_partition'],
        layout='Gamma[norm][target_block][source_block][power_index]; power_index0,1,2 means2,1,0.',
        Gamma_max_mode=maximum,Gamma_sum_modes=summed,
        source_common_mass='sum_m sup_source exp(m sigma(y)) |f_m^cos(y)|/(c_bg V^p); maximum matrix consumes this once.',
        pointwise_sup_of_sum_not_substituted=True,separate_P_K_radial_suprema_preserved=True,
        original_target_records=identities,original_cut_record=cutrec,
        cut_max_mode=cutmax,cut_sum_modes=cutsum,
        cut_layout='cut_[max_mode or sum_modes][S or T][source_block][power_index]; original R100 axes, no target angular factor.',
        new_ODE_or_Green_computation=False,new_fixed_point_claimed=False,
        elapsed_seconds=time.monotonic()-began,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    data=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(data)>=5_000_000:raise ValueError('Index exceeds the artifact budget')
    args.out.write_bytes(data)
    print(json.dumps(dict(output=str(args.out),sha256=digest(args.out),bytes=len(data),
        exact_checks=comparisons,all_exact_checks_passed=True)),flush=True)


if __name__=='__main__':
    main()

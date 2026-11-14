#!/usr/bin/env python3
"""Exact saved-array audit of restricted DQ and its 46 low input columns.
No ODE or repeat source production.  This checks saved identity, support,
the original common-low majorant and coefficientwise material domination.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import fmpq
from closure_split_joint_io import iter_array, metadata_without_array, digest

PRIMARY_SHA='d519f6e5d8f0a8bb06c5d87f9257f6b9c01a19bfd04ce394a661ff3ffa3857ac'
INPUT_SHA='d74b5972d555086b0e5dc9b7b63f6b7ee0a6399838f077da538bd79cfd497968'

def q(x):
    m,e=int(x[0]),int(x[1])
    return fmpq(m*(1<<e)) if e>=0 else fmpq(m,1<<(-e))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('primary','input','resource','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError(a.out)
    if digest(a.primary)!=PRIMARY_SHA or digest(a.input)!=INPUT_SHA:
        raise ValueError('Actual saved producer/input identity changed')
    usage=json.loads(a.resource.read_text())
    if usage['exitcode']!=0 or usage['termination_signal'] is not None or not usage['wait4_observed']:
        raise ValueError('Actual producer did not formally complete')
    meta=metadata_without_array(a.primary,'rows')
    if not meta['all_gates'] or not all(meta['gates'].values()) or meta['low_singleton_input_modes']!=list(range(2,93,2)):
        raise ValueError('Full original gate or low spectrum is absent')
    windows=meta['windows_out'];counts=dict(row_identity=0,reference_mode_identity=0,
        saved_nonnegative_coefficients=0,exact_low_support=0,
        low_singletons_bounded_by_original_low_column=0,positive_common_material_domination=0)
    maximum_ratio=fmpq(0)
    cells=[]
    for r,c in zip(iter_array(a.primary,'rows'),iter_array(a.input,'rows')):
        ncell=r['cell'];cells.append(ncell)
        if ncell!=c['cell'] or r['reference_strong_pair_caps']!=c['Cs_plus_Lambda_pair_caps'] or r['reference_common_cap']!=c['Cs_plus_Lambda_common_cap']:
            raise ValueError('The saved restricted source identity differs')
        counts['row_identity']+=1;counts['reference_mode_identity']+=46
        ss,ee=r['low_singleton_kernels_s_upper'],r['low_singleton_kernels_ell_upper']
        if len(ss)!=13 or len(ee)!=13:raise ValueError('Wrong output-window shape')
        for wi,(lo,hi) in enumerate(windows):
            if len(ss[wi])!=46 or len(ee[wi])!=46:raise ValueError('Missing low mode')
            coarse_s=q(r['kernels_s_upper'][wi][0]);coarse_e=q(r['kernels_ell_upper'][wi][0])
            for ni,n in enumerate(range(2,93,2)):
                gs,ge=q(ss[wi][ni]),q(ee[wi][ni])
                if gs<0 or ge<0:raise ArithmeticError('Negative saved positive coefficient')
                counts['saved_nonnegative_coefficients']+=2
                active=any(lo<=k+n<=hi for k in range(2,93,2))
                if ((gs>0)!=active) or ((ge>0)!=active):raise ArithmeticError('Saved exact quadratic support changed')
                counts['exact_low_support']+=2
                if gs>coarse_s or ge>coarse_e:raise ArithmeticError('A low singleton escaped the original low input maximum')
                counts['low_singletons_bounded_by_original_low_column']+=2
                if ge>gs:raise ArithmeticError('Saved common material domination failed')
                counts['positive_common_material_domination']+=1
                if coarse_s:maximum_ratio=max(maximum_ratio,gs/coarse_s)
                if coarse_e:maximum_ratio=max(maximum_ratio,ge/coarse_e)
    if cells!=list(range(12,225)):raise ValueError('Actual full cell coverage changed')
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if peak>98304:raise MemoryError('Independent saved gate exceeded96MiB')
    d=dict(schema='restricted-DQ-saved-low46-exact-audit-v1',all_gates=True,
        primary_sha256=PRIMARY_SHA,input_sha256=INPUT_SHA,
        resource_sha256=digest(a.resource),source_sha256=digest(__file__),
        streaming_helper_sha256=digest(Path(__file__).with_name('closure_split_joint_io.py')),
        cells=cells,low_modes=list(range(2,93,2)),counts=counts,
        maximum_singleton_to_coarse_low_ratio=[str(maximum_ratio.p),str(maximum_ratio.q)],
        inequality_direction='Each singleton is bounded by the old one-column low maximum; finer caps may now be consumed individually.',
        exact_s_material_dominates_ell_at_every_saved_low_entry=True,
        original_nonlinear_mean_inverse_Q_and_T_remain_separate=True,
        new_ODE_or_source_integrations=0,elapsed_seconds=time.monotonic()-start,peak_rss_kib=peak)
    a.out.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=digest(a.out),all_gates=True,counts=counts,
        elapsed_seconds=d['elapsed_seconds'],peak_rss_kib=peak)),flush=True)

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Small whole-map inverse comparison; no BVP, Jacobian or body solve."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
import resource
import time
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity, save_npz
from fd2d_gc_positive_trace_native_field_v2 import PositiveTraceNativeField
from fd2d_gc_fast_material_inverse import FastMaterialInverseMixin


class FastReader(FastMaterialInverseMixin, PositiveTraceNativeField):
    pass


def maximum(x):
    return float(np.max(np.abs(x), initial=0.))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field',type=Path,required=True)
    ap.add_argument('--run-report',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh inverse comparison stem')
    started=time.monotonic();settings=json.loads(args.run_report.read_text())['settings']
    kw=dict(reference_inlet=Path(settings['reference_inlet']),reference_cache=Path(settings['reference_cache']))
    old=PositiveTraceNativeField(args.field,Path(settings['candidate']),**kw)
    new=FastReader(args.field,Path(settings['candidate']),**kw)
    old_chart=old.chart;new_chart=new.chart;counts={'old':0,'new':0}
    def oc(*a,**k):counts['old']+=1;return old_chart(*a,**k)
    def nc(*a,**k):counts['new']+=1;return new_chart(*a,**k)
    old.chart=oc;new.chart=nc
    u=np.r_[2*np.pi*np.arange(64)/64,-np.pi/4,2*np.pi,5*np.pi/2]
    points=[.57,float((old.nodes[63]+old.nodes[64])/2),
        float((old.nodes[71]+old.nodes[72])/2),1.1,
        float((old.trace_ramp_stop+old.trace_cut)/2),float(old.trace_cut)]
    rows=[];samples={'s':np.array(points),'u':u};sources=Path(__file__).resolve().parent
    keys=[name+suffix for name in ('n','m','l') for suffix in ('','_u','_uu')]
    for i,s in enumerate(points):
        begin=dict(counts);t0=time.monotonic();a=old.physical_angular(s,u);old_seconds=time.monotonic()-t0
        t0=time.monotonic();b=new.physical_angular(s,u);new_seconds=time.monotonic()-t0
        aa=np.stack([a[k] for k in keys],axis=-1);bb=np.stack([b[k] for k in keys],axis=-1)
        actual_new_error=maximum(b['angle_inverse_error'])
        turns=np.floor(u/(2*np.pi));target=u-turns*(2*np.pi)
        original_tolerance=32*np.finfo(float).eps*(1+np.abs(target))
        # Full unwrapped re-evaluation can add one final turn-addition ulp;
        # the stopping condition itself is reported on the reduced full map.
        info=dict(new._last_material_inverse_info)
        if info['maximum_residual_to_original_tolerance']>1:
            raise ArithmeticError('Changed original inverse stopping tolerance')
        scale=np.maximum(1,np.maximum(np.abs(aa),np.abs(bb)))
        row=dict(s=s,old_seconds=old_seconds,new_seconds=new_seconds,
            old_chart_calls=counts['old']-begin['old'],new_chart_calls=counts['new']-begin['new'],
            old_inverse_error=maximum(a['angle_inverse_error']),new_inverse_error=actual_new_error,
            maximum_field_absolute_difference=maximum(aa-bb),maximum_field_scaled_difference=maximum((aa-bb)/scale),
            new_inverse_info=info, exact_cut=bool(s==old.trace_cut))
        rows.append(row);samples[f'old_{i}']=aa;samples[f'new_{i}']=bb
        print(json.dumps({'s':s,'old_calls':row['old_chart_calls'],'new_calls':row['new_chart_calls'],
            'old_seconds':old_seconds,'new_seconds':new_seconds,'scaled':row['maximum_field_scaled_difference']}),flush=True)
    report=dict(schema='fd2d-actual-material-inverse-comparison-v1',
        input_field=identity(args.field),input_run_report=identity(args.run_report),
        sources=[identity(sources/n) for n in ('fd2d-root-fast-material-inverse-check.py','fd2d_gc_fast_material_inverse.py',
            'fd2d_gc_positive_trace_native_field_v2.py','fd2d_gc_raw_native_field.py','fd2d_gc_frozen_ruling_atlas.py')],
        completed=True,no_BVP=True,no_body=True,no_Jacobian=True,physical_field_changed=False,
        angle_count=len(u),physical_sections=len(points),fields=keys,rows=rows,
        old_seconds=sum(x['old_seconds'] for x in rows),new_seconds=sum(x['new_seconds'] for x in rows),
        maximum_scaled_field_difference=max(x['maximum_field_scaled_difference'] for x in rows),
        original_inverse_stopping_tolerance_preserved=True,finite_check_only=True,
        seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    save_npz(stem.with_name(stem.name+'-samples.npz'),**samples)
    stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('completed','old_seconds','new_seconds','maximum_scaled_field_difference','seconds','peak_rss_kib')}),flush=True)


if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Reuse immutable completed continuous cells without repeating their proof.

Every source/input/configuration binding is checked against the closed
report. Native cell endpoints are compared as exact rationals. The new
posterior is recomputed from its true inlet in the original full order.
"""
import argparse
import copy
import gzip
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
spec=importlib.util.spec_from_file_location('fd2d_gc_primitive_resume_base',HERE/'fd2d-metric-gc-primitive-continuous.py')
base=importlib.util.module_from_spec(spec);sys.modules[spec.name]=base;spec.loader.exec_module(base)


def option(name,default=None):
    return sys.argv[sys.argv.index(name)+1] if name in sys.argv else default


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--reuse-report',type=Path,action='append',required=True)
    known,rest=parser.parse_known_args()
    sys.argv=[sys.argv[0]]+rest
    current={
        'source':HERE/'fd2d-metric-gc-primitive-continuous.py',
        'interval_models':HERE/'fd2d_gc_interval_models.py',
        'interval_polynomial_backend':HERE/'db6f-audit-metric-polynomial.py',
        'interval_elementary_backend':HERE/'db6f-audit-continuous-hermite.py',
        'normal_range_adapter':HERE/'fd2d-metric-normal-interval-arithmetic.py',
        'field':Path(option('--field')),'accurate_profile':Path(option('--profile')),
        'chart':Path(option('--chart',ROOT/'notes/2026-11-12-fd2d-balanced-chart-fourier-tail-01.json')),
        'inlet':Path(option('--inlet',ROOT/'notes/2026-11-12-fd2d-metric-gc-p148-small01-native-bounds-01.json'))}
    settings={key:int(option(flag,default)) for key,flag,default in (
        ('radial_degree','--degree',16),('native_exponential_order','--exp-order',8),
        ('reciprocal_q_order','--reciprocal-order',5),('finite_chart_modes','--chart-modes',160),
        ('angular_arcs','--arcs',1024))}
    rows={};bindings=[]
    for path in known.reuse_report:
        report=base.load_json(path)
        if not report['complete_requested_interval']:raise ValueError('Reuse requires an actually completed continuous interval')
        for key,source in current.items():
            if base.identity(source)['sha256']!=report[key]['sha256']:raise ValueError('Changed reuse binding: '+key)
        for key,value in settings.items():
            if report['auxiliary_approximation'][key]!=value:raise ValueError('Changed reuse approximation: '+key)
        source=base.locate_near(path,report['rows'])
        decoded=[json.loads(line) for line in gzip.decompress(source.read_bytes()).splitlines()]
        if [row['cell'] for row in decoded]!=report['completed_cells']:raise ValueError('Closed cell list differs from bound rows')
        for row in decoded:
            if row['cell'] in rows:raise ValueError('Duplicate reuse cell')
            rows[row['cell']]=row
        bindings.append(dict(report=base.identity(path),rows=base.identity(source)))
    original=base.consume_cell;reused=[]
    def consume(index,actual,*args,**kwargs):
        if index not in rows:return original(index,actual,*args,**kwargs)
        row=copy.deepcopy(rows[index])
        if row['left_exact']!=str(actual.mesh[index]) or row['right_exact']!=str(actual.mesh[index+1]):raise ValueError('Reuse cell endpoints changed')
        row.pop('posterior_after_cell',None)
        row['strict_bound_reused_from_closed_report']=True
        reused.append(index)
        return row
    base.consume_cell=consume
    base.main()
    output=Path(option('--out'));report=base.load_json(output)
    report.update(operational_resume_adapter=base.identity(__file__),reused_strict_inputs=bindings,
                  reused_native_cells=reused,all_inlet_propagation_recomputed_in_original_order=True)
    output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(reused_native_cells=reused,final_report=base.identity(output))),flush=True)


if __name__=='__main__':main()

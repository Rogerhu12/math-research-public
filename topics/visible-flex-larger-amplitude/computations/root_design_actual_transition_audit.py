#!/usr/bin/env python3
"""Compare a finite linear-port design and its first actual-tail solution.

The metric, material coordinates, gauge and geometric parameters must remain
identical. The boundary problem changes from the finite linear port to the
complete represented nonlinear tail. Consequently this is a transition
diagnostic, never a refinement or convergence claim for one fixed boundary
problem. Only two fully audited successful physical packages are accepted.
"""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import gzip
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys
import time
import textwrap
from types import SimpleNamespace, MethodType

HERE=Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':')).encode()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('design','actual','source-topic','port','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--angular',type=int,default=384)
    parser.add_argument('--batch',type=int,default=8)
    args=parser.parse_args();start=time.monotonic()
    if not 1<=args.batch<=32:
        raise ValueError('Use an independent radial batch between 1 and 32')
    design,actual=(document(p) for p in (args.design,args.actual))
    for data in (design,actual):
        if not data.get('solver_success') or data.get('audit_pending',True):
            raise ValueError('Both packages must be successful and fully audited')
    if (design['config'].get('actual_nonlinear_tail')
            or not actual['config'].get('actual_nonlinear_tail')
            or not actual['config'].get('fixed_metric')):
        raise ValueError('Expected a linear-port design and first fixed-metric actual solution')
    keys=('frozen_profile','physical_tail_parameters','physical_tail_cut',
          'angular_chart','chart_reference_coefficients','chart_reference_frequencies',
          'gauge_amplitude','meridian_length')
    for key in keys:
        if canonical(design[key])!=canonical(actual[key]):
            raise ValueError('A fixed physical datum changed: '+key)
    pullback=module('root_transition_pullback',HERE/'geometric-checkpoint-core-pullback.py')
    utility=module('root_transition_comparison',HERE/'geometric-fixed-dual-prefix.py')
    old,_=pullback.load_saved(args.design,args.source_topic,args.port,args.angular)
    new,_=pullback.load_saved(args.actual,args.source_topic,args.port,args.angular)
    transformations=[]
    # Preserve the exact original quadrature and accumulation order while
    # bounding only independent radial batches. Source files stay unchanged.
    import numpy as np
    for role,saved in (('design',old),('actual',new)):
        original=textwrap.dedent(inspect.getsource(saved.flow.height_integral.__func__))
        if original.count('128')!=3:
            raise ValueError('Original mean quadrature batch sites changed')
        changed=original.replace('128',str(args.batch));scope={'np':np}
        exec(compile(changed,'<transition-bounded-mean>','exec'),scope)
        saved.flow.height_integral=MethodType(scope['height_integral'],saved.flow)
        transformations.append(dict(role=role,kind='mean radial batch only',old_batch=128,
            new_batch=args.batch,original_sha256=hashlib.sha256(original.encode()).hexdigest(),
            transformed_sha256=hashlib.sha256(changed.encode()).hexdigest()))
    original=inspect.getsource(utility.compare_shape)
    first='for first in range(0,len(ss),32):';second='sl=slice(first,first+32);'
    if original.count(first)!=1 or original.count(second)!=1:
        raise ValueError('Original material comparison batch sites changed')
    changed=original.replace(first,f'for first in range(0,len(ss),{args.batch}):').replace(
        second,f'sl=slice(first,first+{args.batch});')
    scope=dict(utility.__dict__);exec(compile(changed,'<transition-bounded-jets>','exec'),scope)
    transformations.append(dict(kind='point and jet independent radial batch only',old_batch=32,
        new_batch=args.batch,original_sha256=hashlib.sha256(original.encode()).hexdigest(),
        transformed_sha256=hashlib.sha256(changed.encode()).hexdigest()))
    comparison=scope['compare_shape'](old,SimpleNamespace(flow=lambda:new.flow),new.sol,args.angular)
    output=dict(scope=__doc__,same_metric_and_physical_data=True,
        same_finite_boundary_problem=False,refinement_claim=False,
        fixed_data_sha256={k:hashlib.sha256(canonical(design[k])).hexdigest() for k in keys},
        source_sha256={str(path):digest(path) for path in (
            Path(__file__),HERE/'geometric-checkpoint-core-pullback.py',
            HERE/'geometric-fixed-dual-prefix.py',args.design,args.actual,args.port)},
        design=dict(file=str(args.design),modes=design['modes'],nodes=design['nodes'],
            actual_primary_amplitude=design['actual_primary_amplitude'],summary=design['summary']),
        actual=dict(file=str(args.actual),modes=actual['modes'],nodes=actual['nodes'],
            actual_primary_amplitude=actual['actual_primary_amplitude'],summary=actual['summary'],
            true_tail_residual=actual['actual_tail']['residual']),
        comparison=comparison,angular=args.angular,independent_batch_transformations=transformations,
        seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(event='design_to_actual_transition',
        maximum_material_point_displacement_sample=comparison['maximum_material_point_displacement_sample'],
        physical_material_jet_differences_max_sample=comparison['physical_material_jet_differences_max_sample'],
        refinement_claim=False)),flush=True)


if __name__=='__main__':
    main()

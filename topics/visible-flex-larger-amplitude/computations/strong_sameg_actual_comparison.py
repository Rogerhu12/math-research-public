#!/usr/bin/env python3
"""Compare two accepted actual-tail spectral discretizations at one metric.

The full final profile, complete physical tail/cut, gauge, reference material
angle and numerical reference are fixed. Both endpoints have passed their own
original true-H/full-Jacobian/audit gates. Only spectrum and representation
resolution may differ. Complete actual quintic jets and height means are
compared at common physical points, including both interior second-jet lobes.
These are finite samples, not a continuous C2 or reach certificate.
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
COPIED_COMPARISON_SOURCE_SHA256='dbe8fdf9fe1a1d7ea571dfe7a3816222c34e69f52f5baafff6421989c6905fa2'


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
    parser.add_argument('--coarse',dest='design',type=Path,required=True)
    parser.add_argument('--fine',dest='actual',type=Path,required=True)
    for name in ('source-topic','port','out'):
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
    if not all(data['config'].get('actual_nonlinear_tail') and
               data['config'].get('fixed_metric') for data in (design,actual)):
        raise ValueError('Both endpoints must be real accepted fixed actual solutions')
    if int(actual['modes'])<=int(design['modes']):
        raise ValueError('The fine endpoint must increase the complete represented spectrum')
    if actual.get('same_g_spectral_refinement',{}).get('solver_success') is not True:
        raise ValueError('The explicit same-g spectral entry did not finish its original gates')
    if not design.get('frozen_design_view',{}).get('raw_x_y_cubic_unchanged'):
        raise ValueError('The real fixed coarse view is required')
    for key in ('reference_t','physical_s'):
        if canonical(design['numerical_meridian_chart'][key])!=canonical(actual['numerical_meridian_chart'][key]):
            raise ValueError('The numerical/physical meridian chart changed: '+key)
    coarse_config=design['actual_tail']['config'];fine_config=actual['actual_tail']['config']
    allowed={'modes','traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'}
    configuration_changes=[]
    for key in sorted(set(coarse_config)|set(fine_config)):
        if canonical(coarse_config.get(key))!=canonical(fine_config.get(key)):
            configuration_changes.append(key)
            if key not in allowed:
                raise ValueError('A tail discretization or physical parameter changed unexpectedly: '+key)
    common_sources={}
    for key in sorted(set(design['actual_tail']['source_sha256'])&set(actual['actual_tail']['source_sha256'])):
        left=design['actual_tail']['source_sha256'][key];right=actual['actual_tail']['source_sha256'][key]
        if left!=right:
            raise ValueError('A shared actual tail numerical source changed: '+key)
        common_sources[key]=left
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
    for role,saved in (('coarse',old),('fine',new)):
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
        same_underlying_actual_tail_equations=True,numerical_spectra_differ=True,
        spectral_refinement_pair=True,continuous_convergence_claim=False,
        original_comparison_formula_source_sha256=COPIED_COMPARISON_SOURCE_SHA256,
        tail_configuration_changes=configuration_changes,common_tail_sources_unchanged=common_sources,
        all_coarse_physical_nodes_retained=bool(np.isin(old.sol.x,new.sol.x).all()),
        fixed_data_sha256={k:hashlib.sha256(canonical(design[k])).hexdigest() for k in keys},
        source_sha256={str(path):digest(path) for path in (
            Path(__file__),HERE/'geometric-checkpoint-core-pullback.py',
            HERE/'geometric-fixed-dual-prefix.py',args.design,args.actual,args.port)},
        coarse=dict(file=str(args.design),modes=design['modes'],nodes=design['nodes'],
            actual_primary_amplitude=design['actual_primary_amplitude'],summary=design['summary']),
        fine=dict(file=str(args.actual),modes=actual['modes'],nodes=actual['nodes'],
            actual_primary_amplitude=actual['actual_primary_amplitude'],summary=actual['summary'],
            true_tail_residual=actual['actual_tail']['residual']),
        comparison=comparison,angular=args.angular,independent_batch_transformations=transformations,
        seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(event='same_g_actual_spectral_comparison',
        maximum_material_point_displacement_sample=comparison['maximum_material_point_displacement_sample'],
        physical_material_jet_differences_max_sample=comparison['physical_material_jet_differences_max_sample'],
        continuous_convergence_claim=False)),flush=True)


if __name__=='__main__':
    main()

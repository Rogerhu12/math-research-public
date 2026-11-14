#!/usr/bin/env python3
"""Replay the real q122 first-append schema without a flow or nonlinear solve.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Tests the actual provider chain, exact zero-weight identity, nonzero forward
and half finite-difference constructions, and original endpoint definitions.
Numerical provider endpoint checks are not continuum roundoff certificates.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('source-dir','checkpoint','out'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Fresh actual anchor replay required')
    saved=json.loads(gzip.decompress(a.checkpoint.read_bytes()));cfg=saved['frozen_profile']
    if not saved.get('solver_success') or saved.get('audit_pending',True):raise ValueError('Real accepted profile required')
    if cfg.get('initial_speed_frontload',0)!=0 or cfg.get('initial_speed_pulse',0)!=0:raise ValueError('Original q122 zero laws required')
    expected={'alternative-neck-provider.py':'84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2',
        'strong_initial_speed_pulse.py':'f1d8c0867d598313da760fcd4910cd20c5f387afd7c6bd90a31b257848acbf73',
        'strong_monotone_initial_speed.py':'12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7'}
    for name,h in expected.items():
        if sha(a.source_dir/name)!=h:raise ValueError('Frozen original provider changed: '+name)
    sys.path.insert(0,str(a.source_dir));pulse=load('anchor_check_pulse',a.source_dir/'strong_initial_speed_pulse.py')
    old=load('anchor_check_old',a.source_dir/'strong_monotone_initial_speed.py')
    fixed=load('anchor_check_fixed',Path(__file__).with_name('strong_monotone_initial_speed_anchor.py'))
    def provider(name,hook):
        obj=load(name,a.source_dir/'alternative-neck-provider.py');pulse.install(obj);hook.install(obj);return obj
    prior=provider('anchor_check_prior_provider',old);new=provider('anchor_check_new_provider',fixed)
    first=prior.NeckPrefix(cfg);second=new.NeckPrefix(cfg);gates=[]
    def check(name,yes):
        if not yes:raise ArithmeticError(name)
        gates.append(name)
    check('all_zero_law_segment_metadata_exactly_unchanged',canon(first.segments)==canon(second.segments))
    check('all_zero_law_profile_metadata_exactly_unchanged',canon(first.cfg)==canon(second.cfg))
    for key in ('S','Tu','Td','period','aend','end','height','loop_begin'):
        check('zero_law_scalar_bits_'+key,np.float64(getattr(first,key)).tobytes()==np.float64(getattr(second,key)).tobytes())
    check('zero_law_all_breakpoints_bits_unchanged',first.breaks().tobytes()==second.breaks().tobytes())
    rows=[]
    for weight in (-.01,-.005,.005,.01,.5):
        cc=dict(cfg,initial_speed_frontload=weight);pre=new.NeckPrefix(cc);seg=pre.segments[0]
        check('nonzero_original_complete_prefix_constructs',len(pre.segments)==len(first.segments))
        check('current_actual_anchor_reaches_original_parent_append',seg['a0']==1. and seg['s0']==0. and seg['h0']==0.)
        check('first_piece_length_propagates_to_original_prefix',seg['length']==pre.S==pre.Tu)
        controls=seg['strong_initial_speed_frontload_velocity_controls'];acc=seg['strong_initial_speed_frontload_acceleration_controls']
        check('all_actual_binary_Bernstein_speeds_in_domain',all(F.from_float(c)>=0 and F.from_float(c)<=F.from_float(cfg['vu']) for c in controls))
        check('all_actual_binary_acceleration_controls_nonnegative',all(F.from_float(c)>=0 for c in acc))
        left=np.asarray(new.piece_jet(seg,np.array([0.])))[:,0]
        right=np.asarray(new.piece_jet(seg,np.array([1.])))[:,0]
        target_left=np.array([1.,0.,cfg['start_acceleration']]);target_right=np.array([1.+cfg['delta'],cfg['vu'],0.])
        left_error=np.abs(left-target_left);right_error=np.abs(right-target_right)
        check('original_endpoint_definitions_with_explicit_binary_roundoff',max(left_error.max(),right_error.max())<=64*np.finfo(float).eps)
        check('original_radius_increment_matches_complete_append',abs(seg['dr']-cfg['delta'])<=64*np.finfo(float).eps)
        check('terminal_original_radius_retained',pre.aend==first.aend)
        rows.append(dict(weight=weight,length=seg['length'],degree=seg['strong_initial_speed_frontload_degree'],
            actual_anchor=seg['a0'],left_jet=left.tolist(),right_jet=right.tolist(),
            left_endpoint_absolute_error=left_error.tolist(),right_endpoint_absolute_error=right_error.tolist(),
            physical_profile_is_new_metric=True,complete_prefix_length=pre.end,minimum_derivative_control=min(acc)))
    bad=dict(cfg,initial_speed_frontload=.01,initial_speed_pulse=.001)
    try:new.NeckPrefix(bad)
    except ValueError:gates.append('original_nonzero_pulse_frontload_combination_rejected')
    else:raise ArithmeticError('Original mutual exclusion weakened')
    try:fixed.install(prior)
    except ValueError:gates.append('already_installed_unfixed_provider_not_silently_accepted')
    else:raise ArithmeticError('Unfixed provider silently reused')
    fixed.install(new);gates.append('fixed_provider_reinstallation_idempotent')
    out=dict(schema='actual-q122-frontload-first-append-anchor-check-v1',scope=__doc__,all_gates=True,gate_count=len(gates),checks=gates,
        source_sha256={str(x):sha(x) for x in (Path(__file__),a.checkpoint,Path(__file__).with_name('strong_monotone_initial_speed_anchor.py'),*(a.source_dir/k for k in expected))},
        original_profile=cfg,adapter=fixed.source_identity(),zero_weight_full_original_arithmetic_preserved=True,
        actual_nonzero_rows=rows,Flow_ODE_Node_Newton_or_new_accepted_solution=0,
        complete_continuous_roundoff_metric_or_reach_certificate=False)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'event':'actual_frontload_anchor_check_finished','all_gates':True,'gates':len(gates),'path':str(a.out),'sha256':sha(a.out)}),flush=True)


if __name__=='__main__':main()

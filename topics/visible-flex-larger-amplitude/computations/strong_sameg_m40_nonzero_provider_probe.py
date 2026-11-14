#!/usr/bin/env python3
"""Exercise both real M40 provider-loader hooks on a saved unsolved warm profile.

Author: strong_recovery (GPT-6 Astra Pro, AI assisted), 2026-11-13.
This is a zero-ODE interface check. No accepted nonzero checkpoint, fine field,
tail response, solver acceptance or same-g convergence is manufactured.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
            'NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ENTRY='strong_sameg_m40_initial_laws_fullflow_refinement.py'
ENTRY_SHA='36f73382aaa8bf7c6d64c696543f768b912f21e43b534acd1504bdf3efe6158e'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inlet-report',type=Path,required=True)
    parser.add_argument('--inlet-sha256',required=True)
    parser.add_argument('--port',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();gates={}
    def check(key,value):
        if not value:raise ValueError(key)
        gates[key]=True
    check('entry_SHA',sha(HERE/ENTRY)==ENTRY_SHA)
    check('actual_inlet_report_SHA',sha(args.inlet_report)==args.inlet_sha256)
    report=json.loads(args.inlet_report.read_text())
    profile=report['warm_profile']
    check('actual_unsolved_warm_scope',report['finished'] and not report['nonlinear_solution'])
    check('nonzero_frontload_actual_value',profile['initial_speed_frontload']==.064)
    spec=importlib.util.spec_from_file_location('m40_nonzero_provider_probe_entry',HERE/ENTRY)
    entry=importlib.util.module_from_spec(spec);sys.modules[spec.name]=entry;spec.loader.exec_module(entry)
    base=entry.base_module()
    production_path=HERE/'root_dual_core_bvp.py'
    saved_path=HERE/'geometric-checkpoint-core-pullback.py'
    production=entry.wrap_production_loaded(entry.module('m40_probe_production_root',production_path),production_path)
    saved=entry.wrap_provider_loader(entry.module('m40_probe_saved_root',saved_path),'saved')
    provider_path=HERE/'alternative-neck-provider.py'
    pp=production.module('m40_probe_production_neck',provider_path)
    sp=saved.module('m40_probe_saved_neck',provider_path)
    necks=[p.NeckPrefix(profile) for p in (pp,sp)]
    port=json.loads(args.port.read_text())
    bridges=[p.NeckTerminalBridge(p.tagged_port(port,profile)['cut']) for p in (pp,sp)]
    check('real_loaders_both_invoked',entry.OBSERVATIONS=={'production_provider_loads':1,'saved_provider_loads':1})
    check('complete_profile_identical',all(n.cfg==profile for n in necks))
    fields=[]
    for label,pair in [('prefix',necks),('bridge',bridges)]:
        first,second=pair
        raw1=base.canonical(base.plain(first.segments));raw2=base.canonical(base.plain(second.segments))
        check(label+'_complete_segments_identical',raw1==raw2)
        check(label+'_breaks_bitwise_equal',first.breaks().tobytes()==second.breaks().tobytes())
        check(label+'_length_and_background_height_bits_equal',np.array([first.end,first.height]).tobytes()==np.array([second.end,second.height]).tobytes())
        grid=np.unique(np.r_[first.breaks(),np.concatenate([s['s0']+s['length']*np.linspace(0.,1.,65) for s in first.segments])])
        values=[pair_item.profile(grid) for pair_item in pair]
        check(label+'_radius_speed_acceleration_samples_bitwise_equal',all(np.asarray(a,dtype='<f8').tobytes()==np.asarray(b,dtype='<f8').tobytes() for a,b in zip(*values)))
        fields.append(dict(kind=label,segment_count=len(first.segments),sample_count=len(grid),
            complete_segments_sha256=hashlib.sha256(raw1).hexdigest(),length=first.end,
            background_height=first.height,segments=base.plain(first.segments),
            jet_SHA256=[hashlib.sha256(np.asarray(a,dtype='<f8').tobytes()).hexdigest() for a in values[0]]))
    first=necks[0].segments[0]
    check('genuine_nonzero_first_piece_installed',first.get('strong_initial_speed_frontload')==.064 and first.get('strong_initial_speed_frontload_degree')==22 and first.get('strong_initial_speed_frontload_nonnegative_derivative_hull') is True)
    acceleration_error=float(necks[0].profile(0.)[2])-profile['start_acceleration']
    check('first_piece_start_acceleration_rounding_only',abs(acceleration_error)<=2*np.finfo(float).eps*max(1.,abs(profile['start_acceleration'])))
    output=dict(schema='sameg-M40-nonzero-provider-loader-probe-v1',scope=__doc__,finished=True,
        checks=gates,all_checks_passed=True,actual_unsolved_warm_profile=profile,
        input=dict(file=str(args.inlet_report),sha256=sha(args.inlet_report)),
        source_sha256={str(path):sha(path) for path in [Path(__file__),HERE/ENTRY,production_path,saved_path,provider_path,*[HERE/name for name in entry.HOOKS]]},
        physical_port=dict(file=str(args.port),sha256=sha(args.port)),
        observations=dict(entry.OBSERVATIONS),complete_physical_pieces=fields,
        first_piece_initial_acceleration_error=acceleration_error,
        Node_ODE_or_J_calls=0,accepted_nonzero_checkpoint_created=False,
        nonzero_accepted_fixed_view_input_gate_exercised=False,
        future_accepted_nonzero_sameg_preflight_still_required=True)
    data=(json.dumps(output,indent=2,allow_nan=False)+'\n').encode()
    with args.out.open('xb') as f:f.write(data)
    print(json.dumps(dict(out=str(args.out),sha256=sha(args.out),checks=len(gates),Node_ODE_or_J_calls=0)),flush=True)

if __name__=='__main__':main()

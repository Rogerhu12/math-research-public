#!/usr/bin/env python3
"""Freeze a selected finite LP proposal through the real fine warm constructor.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The complete accepted M32 raw parameters and original M28 response arrays
are read and checked by the original verified constructor. The original
warm-only low-core parameter correction is replayed before inlet inspection.
This creates no Flow, ODE, new field, Jacobian, tail response or accepted solve.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np

WARM_SHA='ff5acad191d51544bfebaf46902f7e58f89a2e4575130f9b33932aa25ef8972c'
AUGMENTED_SHA='74c64ab558953c6d0378948dd4affb5d354d1faaecab7922b83cfdf76041bad7'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def one(argv,key):
    if argv.count(key)!=1:raise ValueError('Unique original argument required: '+key)
    return argv[argv.index(key)+1]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('prediction','base-resource','warm-source','out-prefix'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--prediction-sha256',required=True)
    p.add_argument('--prediction-index',type=int,default=2)
    a=p.parse_args();out=Path(str(a.out_prefix)+'-prepared-core.json')
    if out.exists():raise FileExistsError('Fresh actual full-core warm preparation required')
    if sha(a.prediction)!=a.prediction_sha256 or sha(a.warm_source)!=WARM_SHA:
        raise ValueError('Original LP proposal or verified warm source changed')
    source=a.warm_source.parent/'strong_actual_augmented_core.py'
    if sha(source)!=AUGMENTED_SHA:raise ValueError('Original warm parameter map changed')
    frozen=source.read_text()
    for code in ["p[0] = math.log(self._strong_target[0]/self.q)",
                 "p[1] = (self._strong_target[1]-self.ref_coeff[1])/self.pscale[0]",
                 "p[2] = self._strong_target[2]/self.pscale[1]",
                 "result = np.r_[self.q*math.exp(float(p[0])), p[1:self.M]*self.pscale]"]:
        if frozen.count(code)!=1:raise ValueError('Original explicit core-map source anchor changed')
    prediction=read(a.prediction);row=prediction['predictions'][a.prediction_index]
    if not row['success'] or not row['all_finite_rows_checked'] or row['finite_rows']!=14453760:
        raise ValueError('A complete checked finite geometric proposal is required')
    resource=read(a.base_resource)
    if resource['exitcode']!=0 or not resource['wait4_observed']:
        raise ValueError('The original actual zero fine-warm preparation was not completed')
    argv=list(resource['command'])[2:]
    previous=one(argv,'--out-prefix')
    argv=[value.replace(previous,str(a.out_prefix)) for value in argv]
    if '--coarse-fine-geometry-prepare-only' not in argv:raise ValueError('Use the actual prepared fine geometry command')
    controls=row['physical_steps']
    options=SimpleNamespace(coarse_reference=Path(one(argv,'--coarse-reference')),
        coarse_raw=Path(one(argv,'--coarse-raw')),coarse_tail=Path(one(argv,'--coarse-tail')),
        coarse_response_data=Path(one(argv,'--coarse-response-data')),
        coarse_control=[name+'='+repr(value) for name,value in controls.items()])
    sys.path.insert(0,str(a.warm_source.parent))
    spec=importlib.util.spec_from_file_location('actual_selected_fine_warm_constructor',a.warm_source)
    constructor=importlib.util.module_from_spec(spec);sys.modules[spec.name]=constructor;spec.loader.exec_module(constructor)
    record,warm=constructor.prepare(options,argv)
    reference=read(record['current_reference']);M=int(reference['modes'])
    if M!=32 or len(reference['parameters'])!=M:raise ValueError('The real accepted fixed p32 is required')
    scale=np.asarray(reference['central_correction_scales'],dtype=np.float64)
    parameters=np.r_[np.asarray(reference['parameters'],dtype=np.float64),np.zeros(3)]
    parameters[:M]+=warm['fixed_parameter_and_field_increment'][-M:]
    parameters[M:]=warm['geometry_increment']
    target=record['target_core'];q=reference['gauge_amplitude'];ref=reference['chart_reference_coefficients']
    parameters[0]=math.log(target[0]/q)
    parameters[1]=(target[1]-ref[1])/scale[0]
    parameters[2]=target[2]/scale[1]
    core=np.r_[q*math.exp(float(parameters[0])),parameters[1:M]*scale];core[1]+=ref[1]
    baseline=np.asarray(reference['core']['coefficients'],dtype=np.float64)
    if core[28:].tobytes()!=baseline[28:].tobytes():raise ValueError('A new fine baseline mode was changed')
    prediction_difference=float(np.max(abs(core-np.asarray(row['fine_complete_core_tail_proxy_prediction']))))
    if prediction_difference>2e-14:raise ValueError('Selected physical controls did not reproduce the complete proxy core')
    profile=dict(reference['frozen_profile'])
    for name,step in record['geometry_increment'].items():profile[name]+=step
    for name,step in record['external_shifts'].items():profile[name]=profile.get(name,0.)+step
    for name,value in controls.items():argv+=['--coarse-control',name+'='+repr(value)]
    argv.remove('--coarse-fine-geometry-prepare-only')
    command=['python','computations/root_actual_coarse_increment_geometry_points.py',*argv,
             '--point-cloud-array',str(a.out_prefix)+'-points.json']
    output=dict(schema='actual-fine-complete-core-before-full-warm-geometry-v1',scope=__doc__,
        source_sha256=sha(__file__),source_and_input_sha256={str(path):sha(path) for path in
            (a.prediction,a.base_resource,a.warm_source,source,Path(record['current_reference']))},
        selected_prediction_index=a.prediction_index,selected_finite_prediction=row,
        original_verified_coarse_warm=record,actual_reference=record['current_reference'],
        actual_reference_sha256=record['current_reference_sha256'],actual_complete_core=core.tolist(),
        original_warm_parameter_count=len(parameters),original_warm_parameters=parameters.tolist(),
        original_low_target_correction_replayed=True,new_fine_mode_baselines_bitwise_preserved=True,
        actual_core_vs_parent_float_prediction_max_difference=prediction_difference,
        requested_profile_parameters=profile,requested_profile_not_yet_evaluated=True,
        geometry_command=command,geometry_not_yet_run=True,nonlinear_solution=False,
        new_Flow_ODE_Node_Newton_calls=0)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(event='actual_selected_fine_core_prepared',file=str(out),sha256=sha(out),
        actual_core_low=core[:3].tolist(),complete_modes=M,parent_prediction_difference=prediction_difference)),flush=True)


if __name__=='__main__':main()

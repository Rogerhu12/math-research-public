#!/usr/bin/env python3
"""Compare accepted same-g spectra with each field's full production mean.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The frozen comparison's actual-solution, same-metric, chart, gauge and tail
identity gates are retained. Only its angular rules for H, H_s and H_ss are
changed to max(512,16*(3*M+1)) independently for each complete field. The
physical quintics, Gauss6 height integration, material-jet formulas and both
meshes' nodes, midpoints and two interior second-jet lobes are unchanged.
The existing initial-law saved-field loader is installed in its original
pulse-then-frontload order. Geometry defaults to 768 angles and batch 8.
Prepare-only validates source transformations without inventing endpoints,
loading a mathematical field or starting a tail worker.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
EXPECTED={
    'strong_sameg_actual_comparison.py':'7c152306f09faf7de890377af4f69406677c374ed707b2bc2e391208c8d57f57',
    'geometric-fixed-dual-prefix.py':'f189c8f94880ff5455a140a686219a1805399e1d45a3809e176630bb92772280',
    'geometric-checkpoint-core-pullback.py':'d319574d946f2f6c465b76ffeb92117201aa95bc4318e7100377b184a530fa33',
    'strong_initial_laws_interior_fullmean_audit.py':'35155b17516ce3ff72ddfc957894e53cbd2c7a4a6707d57e62887a8d72e4fbe0',
    'strong_initial_speed_pulse.py':'f1d8c0867d598313da760fcd4910cd20c5f387afd7c6bd90a31b257848acbf73',
    'strong_monotone_initial_speed.py':'12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
}


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def text_sha(value):return hashlib.sha256(value.encode()).hexdigest()


def replace_once(source,before,after):
    if source.count(before)!=1:raise ValueError('Frozen unique source site changed: '+before)
    changed=source.replace(before,after,1)
    if changed.count(after)!=1 or changed.replace(after,before,1)!=source:
        raise ValueError('Exact reverse did not recover the original source site')
    return changed


def complete_mean_source(source):
    original=source
    pairs=[
        ('    H=f.height_integral(sol,ss,angular,6);Ho=old.height_integral(saved.sol,ss,angular,6)\n',
         '    mean_angular_new=max(512,16*(3*f.M+1));mean_angular_old=max(512,16*(3*old.M+1))\n'
         '    H=f.height_integral(sol,ss,mean_angular_new,6);Ho=old.height_integral(saved.sol,ss,mean_angular_old,6)\n'),
        ('    B,B1,B2=f.basis(angular);Bo,Bo1,Bo2=old.basis(angular)\n',
         '    B,B1,B2=f.basis(angular);Bo,Bo1,Bo2=old.basis(angular)\n'
         '    complete_mean_bases={id(f):f.basis(mean_angular_new)[1:],id(old):old.basis(mean_angular_old)[1:]}\n'),
        ("        fr,Fsp,dW=flow.velocity_s(s,Y,Yp,BB1,BB2);g=fr['geo']\n",
         "        fr,Fsp,dW=flow.velocity_s(s,Y,Yp,BB1,BB2);g=fr['geo']\n"
         "        mean_B1,mean_B2=complete_mean_bases[id(flow)]\n"
         "        mean_fr,_,mean_dW=flow.velocity_s(s,Y,Yp,mean_B1,mean_B2)\n"),
        ("        Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]\n",
         "        Fsc[:,:,2]+=np.mean(mean_fr['V'][:,:,2],axis=1)[:,None]\n"),
        ("        Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]\n",
         "        Fssc[:,:,2]+=np.mean(mean_dW[:,:,2],axis=1)[:,None]\n"),
        ('                mean_height_difference_max=float(abs(H-Ho).max()),radial_samples=len(ss),angular=angular,\n',
         '                mean_height_difference_max=float(abs(H-Ho).max()),radial_samples=len(ss),angular=angular,\n'
         "                complete_mean_angular=dict(coarse=mean_angular_old,fine=mean_angular_new),\n"
         "                complete_mean_rule='max(512,16*(3*M+1)) independently for H, H_s, H_ss',\n"),
    ]
    for before,after in pairs:source=replace_once(source,before,after)
    ast.parse(source)
    reverse=source
    for before,after in reversed(pairs):reverse=replace_once(reverse,after,before)
    if reverse!=original:raise ValueError('Other comparison formulas changed')
    return source


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--prepare-only',action='store_true')
    parser.add_argument('--source-dir',type=Path,default=HERE)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--angular',type=int,default=768)
    parser.add_argument('--batch',type=int,default=8)
    own,remaining=parser.parse_known_args()
    if own.out.exists():raise FileExistsError('Use a fresh comparison output')
    if own.angular<768 or own.angular%4 or not 1<=own.batch<=8:
        raise ValueError('Use at least 768 geometry angles divisible by four and radial batch 1..8')
    for name,expected in EXPECTED.items():
        if sha(own.source_dir/name)!=expected:raise ValueError('Frozen source changed: '+name)
    sys.path.insert(0,str(own.source_dir))
    source=(own.source_dir/'strong_sameg_actual_comparison.py').read_text()
    before='    original=inspect.getsource(utility.compare_shape)\n'
    after=before+'    original=COMPLETE_MEAN_COMPARISON_SOURCE(original)\n'
    changed=replace_once(source,before,after)
    ast.parse(changed)
    tree=ast.parse((own.source_dir/'geometric-fixed-dual-prefix.py').read_text())
    comparison_node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='compare_shape')
    original_comparison=ast.get_source_segment((own.source_dir/'geometric-fixed-dual-prefix.py').read_text(),comparison_node)+'\n'
    complete_comparison=complete_mean_source(original_comparison)
    first='for first in range(0,len(ss),32):';second='sl=slice(first,first+32);'
    bounded=replace_once(complete_comparison,first,f'for first in range(0,len(ss),{own.batch}):')
    bounded=replace_once(bounded,second,f'sl=slice(first,first+{own.batch});')
    ast.parse(bounded)
    identity=dict(scope=__doc__,source_sha256={**EXPECTED,Path(__file__).name:sha(__file__)},
        original_comparison_function_sha256=text_sha(original_comparison),
        fullmean_comparison_function_sha256=text_sha(complete_comparison),
        bounded_fullmean_comparison_function_sha256=text_sha(bounded),
        original_entry_sha256=text_sha(source),transformed_entry_sha256=text_sha(changed),
        exact_reverse_recovers_frozen_sources=True,
        full_sameg_and_original_actual_acceptance_gates_preserved=True,
        original_complete_quintics_Gauss6_material_jet_formulas_and_both_meshes_retained=True,
        mean_counts_for_requested_spectral_pair={'M28':1360,'M32':1552},
        geometry_angular=own.angular,independent_radial_batch=own.batch,
        new_ODE_Node_Newton_or_accepted_endpoint_created=False,
        continuous_convergence_or_reach_certified=False)
    if own.prepare_only:
        if remaining:raise ValueError('Prepare-only takes no invented coarse or fine endpoints')
        output=dict(schema='sameg-actual-fullmean-comparison-source-preparation-v1',
            prepare_only=True,all_source_and_syntax_gates=True,loaded_actual_fields=0,
            fullmean_adapter=identity)
        own.out.parent.mkdir(parents=True,exist_ok=True)
        own.out.write_text(json.dumps(output,indent=2)+'\n')
        print(json.dumps({'event':'sameg_fullmean_comparison_source_prepared','out':str(own.out),'sha256':sha(own.out),'loaded_actual_fields':0}),flush=True)
        return
    namespace=dict(__file__=str(own.source_dir/'strong_sameg_actual_comparison.py'),
        __name__='sameg_frozen_comparison_complete_mean',
        COMPLETE_MEAN_COMPARISON_SOURCE=complete_mean_source)
    exec(compile(changed,'<sameg-original-entry-with-complete-mean>','exec'),namespace)
    loader_spec=importlib.util.spec_from_file_location('sameg_initial_laws_saved_loader',own.source_dir/'strong_initial_laws_interior_fullmean_audit.py')
    loader=importlib.util.module_from_spec(loader_spec);loader_spec.loader.exec_module(loader)
    observations=dict(provider_loads=0,saved_fields=[])
    namespace['module']=loader.install_audit_loader(namespace['module'],observations)
    previous=sys.argv
    sys.argv=[previous[0],*remaining,'--angular',str(own.angular),'--batch',str(own.batch),'--out',str(own.out)]
    try:namespace['main']()
    finally:sys.argv=previous
    if observations['provider_loads']!=2 or len(observations['saved_fields'])!=2:
        raise ValueError('The two real accepted initial-law fields were not both reloaded')
    output=json.loads(own.out.read_text())
    modes={k:int(output[k]['modes']) for k in ('coarse','fine')}
    expected={k:max(512,16*(3*m+1)) for k,m in modes.items()}
    if output['comparison']['complete_mean_angular']!=expected:
        raise ArithmeticError('The two original complete mean counts were not consumed')
    identity['provider_observations']=observations
    identity['actual_complete_mean_counts']=expected
    output['fullmean_adapter']=identity
    temp=own.out.with_name(own.out.name+'.fullmean.tmp')
    temp.write_text(json.dumps(output,indent=2)+'\n');temp.replace(own.out)


if __name__=='__main__':main()

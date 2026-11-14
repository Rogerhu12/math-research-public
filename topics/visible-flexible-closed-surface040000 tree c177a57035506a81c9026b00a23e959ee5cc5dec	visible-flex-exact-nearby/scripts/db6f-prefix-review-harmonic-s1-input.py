#!/usr/bin/env python3
"""Independent metadata/scalar-transform check; never import a numerical engine."""
import argparse
import ast
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import numpy as np

TOPIC = Path(__file__).resolve().parents[1]
REPO = TOPIC.parents[1]
STEM = TOPIC/'notes/2026-11-09-db6f-tail-harmonic-s1-from-call9'
BUILDER = TOPIC/'scripts/db6f-tail-prepare-harmonic-s1-warm.py'
BUILDER_SHA = '66094a71fd7669faf15e78584c55159e9cd244479b1dada6cffe476181ae75f6'
IO = {'initialCheckpoint','traceFile','iterationCheckpointFile','trialDiagnosticFile','trialStatePrefix'}
SOURCES = {'db6f-prefix-tail-continuation-client.py','db6f-prefix-tail-trial-worker.mjs',
 'db6f-prefix-tail-trial-core.mjs','db6f-prefix-tail-trial-split.mjs',
 '950f-tail-subdivision.mjs','950f-tail-warm-remesh.mjs',
 'closing_weighted_tail.mjs','closing_recalibrated_tail.mjs'}

def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)

def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)

def same(a,b):
    return canonical(a)==canonical(b)

def local(p):
    p=Path(p)
    return p if p.is_absolute() else REPO/p

def item(p):
    p=local(p).resolve(); b=p.read_bytes()
    return dict(path=str(p.relative_to(REPO)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def checked(row):
    actual=item(row['path'])
    assert actual['bytes']==row['bytes'] and actual['sha256']==row['sha256']
    return actual

def finite(v):
    return isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v)

def bits(v):
    return struct.pack('>d',v)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    assert not args.out.exists()
    assert item(BUILDER)['sha256']==BUILDER_SHA
    imported=[]
    for n in ast.walk(ast.parse(BUILDER.read_text())):
        if isinstance(n,ast.Import):
            imported.extend(a.name for a in n.names)
        elif isinstance(n,ast.ImportFrom):
            imported.append(n.module)
    assert set(imported)=={'argparse','copy','gzip','hashlib','json','math','pathlib','numpy'}
    warm_path=Path(str(STEM)+'-input.json.gz')
    cfg_path=Path(str(STEM)+'-config.json')
    interface_path=Path(str(STEM)+'-interface.json')
    prep_path=Path(str(STEM)+'-preparation.json')
    warm,cfg,interface,prep=map(read,(warm_path,cfg_path,interface_path,prep_path))
    assert item(warm_path)['sha256']=='c6a4c0e504802885f358c340c1a23a34355476ee4d241e3ea6b14069b2b4f927'
    source=read(local(warm['source_checkpoint']))
    target=read(local(warm['source_target_prefix']))
    cp,old=warm['checkpoint'],source['response']['checkpoint']
    assert item(local(warm['source_checkpoint']))['sha256']==warm['source_checkpoint_sha256']
    assert item(local(warm['source_target_prefix']))['sha256']==warm['source_target_prefix_sha256']
    assert source['response']['converged'] is True
    assert finite(source['response']['residual']) and 0<=source['response']['residual']<2e-9
    assert source['request']['jacobian'] is False and source['request']['audit'] is False
    assert set(source['source_sha256'])==SOURCES
    for name,digest in source['source_sha256'].items():
        assert item(TOPIC/'scripts'/name)['sha256']==digest
    bindings=[checked(row) for row in warm['definition_bindings']]
    assert len(bindings)==77
    assert hashlib.sha256(canonical(bindings).encode()).hexdigest()==warm['definition_bindings_sha256']
    assert same(interface['source_bindings'],bindings)
    assert prep['definition_bindings_count']==77
    assert prep['definition_bindings_sha256']==warm['definition_bindings_sha256']
    inputs={k:read(local(row['path'])) for k,row in prep['inputs'].items()
            if k not in {'method','method_sources'}}
    expected={}
    for row in [*inputs['launch']['bound_files'],*inputs['audit']['closed_files'],
                inputs['audit']['script'],*prep['inputs'].values(),item(BUILDER)]:
        actual=checked(row)
        assert actual['path'] not in expected or actual==expected[actual['path']]
        expected[actual['path']]=actual
    assert same(bindings,[expected[k] for k in sorted(expected)])
    assert inputs['audit']['call']==9 and inputs['audit']['scale']==13/16
    assert same(inputs['audit']['residual'],source['response']['residual'])
    assert same(source['config'],inputs['config'])
    assert warm['status']=='UNSOLVED_HARMONIC_WARM_ONLY'
    assert warm['preparation_only'] is True and type(warm['actual_solver_runs']) is int
    assert warm['actual_solver_runs']==0
    forbidden={'response','request','seam','converged','residual','history','lastIteration',
               'jets','heightJetJacobian','graphJacobian','audit'}
    assert not forbidden.intersection(warm)
    assert set(cp)==set(old)=={'parameters','states','rawNode','rawStates','cutHeight','scope'}
    assert same(cp['parameters'],old['parameters'])
    assert same(cp['rawNode'],old['rawNode'])
    assert cp['rawNode']==list(range(0,865,72))
    assert all(type(v) is int for v in cp['rawNode'])
    assert len(cp['states'])==len(old['states'])==865
    assert all(len(row)==30 and all(finite(v) for v in row) for row in cp['states'])
    assert len(cp['rawStates'])==13
    assert all(len(row)==30 and all(finite(v) for v in row) for row in cp['rawStates'])
    assert same(cp['rawStates'],[cp['states'][i] for i in cp['rawNode']])
    goal=target['predicted_cut_height']
    assert len(goal)==15 and all(finite(v) and v!=0 for v in goal)
    assert same(cp['cutHeight'],goal)
    assert np.array_equal(np.asarray(source['request']['height']),
                          np.asarray(goal)*np.float64(13/16)**np.arange(1,16))
    # Scalar multiplication is deliberately indexed through col % 15 instead
    # of using the builder's two broadcast slice assignments.
    ratio=np.float64(16)/np.float64(13)
    factors=np.power(ratio,np.arange(1,16))
    assert float(ratio).hex()==warm['transformation']['ratio_hex']
    assert [float(f).hex() for f in factors]==warm['transformation']['factor_hex']
    transformed=0
    for n in range(865):
        for col in range(30):
            wanted=float(old['states'][n][col])*float(factors[col%15])
            assert bits(wanted)==bits(cp['states'][n][col])
            transformed+=1
    assert transformed==25950
    assert goal[0]/cp['cutHeight'][0]==1.0
    changed={k for k in set(cfg)|set(inputs['config'])
             if k not in cfg or k not in inputs['config'] or not same(cfg[k],inputs['config'][k])}
    assert changed==IO
    assert cfg['initialCheckpoint']==str(warm_path)
    assert 'correctInitialBoundary' not in cfg and 'projectionFloor' not in cfg
    assert same(cfg['maxIterations'],36) and same(cfg['solveTolerance'],2e-9)
    assert same(interface['request']['jacobian'],True)
    assert same(interface['request']['audit'],True)
    assert interface['fresh_instance_required'] is True and interface['call_count']==1
    assert interface['client_sha256']==source['source_sha256']['db6f-prefix-tail-continuation-client.py']
    for row in [*interface['input_output_bindings'],*prep['outputs']]:
        checked(row)
    # Copy-branch index algebra from the read original subdivision/remesh.
    copied=set(cp['rawNode'])
    for n in range(12):
        for local_node in range(1,72):
            stage_offset=local_node-1
            raw_segment=8-stage_offset//8
            nearest=7-stage_offset%8
            raw_left=nearest/8
            assert raw_left*8==nearest
            old_index=72*n+(8-raw_segment)*8+8-nearest
            new_index=72*n+local_node
            assert old_index==new_index
            copied.add(new_index)
    assert copied==set(range(865))
    for row in bindings:
        checked(row)
    report=dict(status='PASS-INDEPENDENT-HARMONIC-WARM-METADATA-AND-SCALAR-TRANSFORM',
        scope='All 25950 stored Q/Pi products and 77 source bindings verified. No root, RK, flow, worker, solver or geometry evaluation.',
        producer=item(__file__), reviewed_builder=item(BUILDER),
        reviewed_method=item(TOPIC/'notes/2026-11-09-db6f-tail-harmonic-warm-interface.md'),
        reviewed_actual_preparation=item(TOPIC/'notes/2026-11-09-db6f-tail-harmonic-s1-from-call9-preparation.md'),
        imports=sorted(imported), bindings=bindings,
        author_outputs=[item(p) for p in (warm_path,cfg_path,interface_path,prep_path)],
        source_closed_call=9, source_scale=13/16, source_residual=source['response']['residual'],
        candidate_remains_unsolved=True, target_exact_goal_copy=True,
        full_parameters_canonical_source_copy=True,
        state_entries_checked_bitwise=transformed, raw_node_count=13,
        copy_branch_indices_checked=865, remesh_RK_calls=0,
        loader_requested_height_ratio=1.0,
        changed_config_keys=sorted(changed), original_max_iterations=36,
        original_tolerance=2e-9, default_projection_floor_preserved=True,
        default_boundary_correction_preserved=True, candidate_positive_branch_not_evaluated=True,
        new_candidate_file_written=False, mathematical_solver_calls=0)
    args.out.write_text(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    print(json.dumps({k:report[k] for k in ('status','state_entries_checked_bitwise',
        'copy_branch_indices_checked','candidate_remains_unsolved','mathematical_solver_calls')}))

if __name__=='__main__':
    main()

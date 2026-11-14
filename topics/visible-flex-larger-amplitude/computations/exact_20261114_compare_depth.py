#!/usr/bin/env python3
"""Compare two actually solved finite tails on the same stored metric and H.

This reports the finite physical-cut jets and the change in the old linear
Robin condition. It does not infer an infinite tail or a closed surface from
two finite solves, and it does not transfer a tail result to the prefix BVP.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct
import numpy as np


def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def typed(x):
    kind=x[0]
    if kind=='object': return {k:typed(v) for k,v in x[1]}
    if kind=='array': return list(map(typed,x[1]))
    if kind=='f64le': return struct.unpack('<d',bytes.fromhex(x[1]))[0]
    if kind=='null': return None
    if kind in ('boolean','string'): return x[1]
    raise ValueError(kind)


def compare(a,b):
    a=np.asarray(a,dtype=float);b=np.asarray(b,dtype=float)
    if a.shape!=b.shape or not np.isfinite(a).all() or not np.isfinite(b).all():
        raise ValueError('Nonfinite or unequal comparison arrays')
    delta=b-a
    ix=np.unravel_index(np.argmax(np.abs(delta)),delta.shape)
    return dict(max_absolute_difference=float(np.max(np.abs(delta))),
        worst_index=[int(x) for x in ix],old_value=float(a[ix]),new_value=float(b[ix]),
        difference_l1=float(np.abs(delta).sum()),
        old_max_absolute=float(np.abs(a).max()),new_max_absolute=float(np.abs(b).max()))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--topic',type=Path,required=True)
    p.add_argument('--new-dir',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();notes=a.topic/'notes';base='2026-11-13-strong-q126-m32-tail2-actual-r1'
    old_path=notes/(base+'-tail-response_0003.json.gz')
    old_packet=read(old_path);old=old_packet['response'];new=read(a.new_dir/'response.json.gz')
    run=read(a.new_dir/'result.json');ready=read(a.new_dir/'ready.json.gz')
    config=read(a.new_dir/'config.json');H=old_packet['request']['height']
    if not run['success'] or not old['converged'] or not new['converged']:
        raise ValueError('Both finite solves must actually have succeeded')
    if new['checkpoint']['cutHeight']!=H or new['residual']>=config['solveTolerance']:
        raise ValueError('Complete H or original tolerance changed')
    old_config=old_packet['config'];ignored={'depth','initialCheckpoint','traceFile','iterationCheckpointFile','trialDiagnosticFile'}
    if {k:v for k,v in old_config.items() if k not in ignored}!={k:v for k,v in config.items() if k not in ignored}:
        raise ValueError('A non-depth physical/numerical setting changed')
    old_ready=read(notes/(base+'-accepted-ready-extracted.json'))
    same_factory=old_ready['storedMetricAdapter'];new_factory=ready['storedMetricAdapter']
    factory_keys=['sourceRevision','frozenWarpAlpha','cellCount',
                  'profileFingerprintBefore','profileFingerprintAfter']
    if any(same_factory[k]!=new_factory[k] for k in factory_keys):
        raise ValueError('Stored metric factory differs')
    # The factory carries I/O and discretization fields inside the object named
    # physicalParameters. Compare every other field; depth is precisely the
    # declared new finite boundary, and the I/O paths have no mathematical role.
    old_physical={k:v for k,v in same_factory['physicalParameters'].items() if k not in ignored}
    new_physical={k:v for k,v in new_factory['physicalParameters'].items() if k not in ignored}
    if old_physical!=new_physical:
        raise ValueError('A fixed stored-metric parameter changed')
    geometry_keys=['radius','backgroundSlope','backgroundSecond','E','Ep']
    if any(struct.pack('<d',old['jets'][k])!=struct.pack('<d',new['jets'][k]) for k in geometry_keys):
        raise ValueError('Cut background has changed')
    jets={k:compare(old['jets'][k],new['jets'][k]) for k in ('height','slope','second')}
    means={k:compare([old['jets'][k]],[new['jets'][k]]) for k in
           ('meanSlope','meanSecond','meanSlopeCorrection','meanSecondCorrection')}
    old_states=np.asarray(old['checkpoint']['states']);new_states=np.asarray(new['checkpoint']['states'])
    states=compare(old_states,new_states[:len(old_states)])
    row_scale=np.maximum(np.max(np.abs(old_states),axis=1),np.finfo(float).tiny)
    states['maximum_row_relative_difference']=float(np.max(
        np.max(np.abs(new_states[:len(old_states)]-old_states),axis=1)/row_scale))
    flow_path=notes/(base+'-tail-response-full-tangent-call0003-manifest.json.gz')
    flow=read(flow_path);identity=typed(json.loads(flow['identityCanonical']))
    trace=[json.loads(line) for line in (a.new_dir/'trace.jsonl').read_text().splitlines()]
    amplitude_warm=[row for row in trace if row.get('event')=='geometric_amplitude_warm']
    graph=np.asarray(identity['farGraph']);M=len(H);cut=len(old_states)-1
    old_defect=old_states[-1,M:]-graph*old_states[-1,:M]
    new_defect=new_states[cut,M:]-graph*new_states[cut,:M]
    robin=dict(old_depth=8,graph=graph.tolist(),old_defect=old_defect.tolist(),
        refined_solution_defect_at_old_cut=new_defect.tolist(),
        old_defect_linf=float(np.abs(old_defect).max()),
        refined_defect_linf=float(np.abs(new_defect).max()),
        relative_to_old_node_scale=float(np.abs(new_defect).max()/row_scale[-1]),
        scope='Canonical finite graph defect at the former deep boundary. It need not vanish for the deeper nonlinear tail.')
    result=dict(status='actual_fixed_metric_complete_H_depth_comparison',
        source_sha256=sha(__file__),input_sha256={str(q):sha(q) for q in
            [old_path,flow_path,a.new_dir/'response.json.gz',a.new_dir/'ready.json.gz',
             a.new_dir/'result.json',a.new_dir/'config.json']},
        old_depth=8,new_depth=config['depth'],modes=M,angular_grid=config['quadrature'],
        old_shooting_nodes=len(old_states),new_shooting_nodes=len(new_states),
        exact_complete_H_unchanged=True,same_stored_metric_factory_fields=factory_keys,
        all_factory_parameters_except_declared_depth_and_IO_equal=True,
        exact_same_cut_geometry={k:old['jets'][k] for k in geometry_keys},
        depth_warm_remesh_preserved_all_original_nodes=ready['warmEmbedding']['maxExistingStateDifference']==0,
        subsequent_original_amplitude_warm=amplitude_warm,
        residuals=[old['residual'],new['residual']],original_tolerance=config['solveTolerance'],
        finite_audits=[old['audit'],new['audit']],physical_cut_jets=jets,
        physical_cut_mean_jets=means,common_canonical_nodes=states,old_boundary_robin=robin,
        limitations=['One finite-depth pair does not prove an infinite-tail limit.',
            'All-M angular and radial refinements are separate.',
            'The prefix boundary problem has not been resolved with the deeper DN in this comparison.',
            'A permanent collar, complete closed-surface reach, and amplitude requirements remain separate.'])
    with a.out.open('x') as out: json.dump(result,out,indent=2,allow_nan=False);out.write('\n')
    print(json.dumps(dict(out=str(a.out),depths=[8,config['depth']],
        slope_difference=jets['slope']['max_absolute_difference'],
        second_difference=jets['second']['max_absolute_difference'],
        former_boundary_robin=robin['refined_defect_linf'])),flush=True)


if __name__=='__main__': main()

#!/usr/bin/env python3
"""Unaccepted all-node predictor from an accepted packet's actual fresh stage J.

Every finite shooting unknown, original normalization and boundary row is
retained.  The old interior/deep residual and the complete new Dirichlet height
difference form the original Newton right hand side.  The untouched sparse
linear helper pays its original backward-error gate.  The resulting checkpoint
is an initial guess only; a later original worker must solve and audit it.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import struct
import subprocess
import sys
import time

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def load(path):
    return json.loads(Path(path).read_text())


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def read_packet(path):
    with gzip.open(path, 'rt') as stream:
        return json.load(stream)


def predict(repo, packet_path, native_runs, desired_height, outdir):
    repo, packet_path, native_runs, out = map(lambda x: Path(x).resolve(),
                                            (repo, packet_path, native_runs, outdir))
    if out == repo or repo in out.parents:
        raise ValueError('Actual fields and complete predictors stay outside Git')
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    sys.path.insert(0, str(scripts/'resume_20261126'))
    helpers = module('_tail_predictor_native_identity', scripts/'resume_20261126/seam_export_tail_geometry_v2.py')
    provenance = module('_tail_predictor_provenance', scripts/'resume_20261126/continue_original_actual_dn_chord.py')
    packet = read_packet(packet_path)
    response, cfg = packet['response'], packet['config']
    cp, M = response['checkpoint'], int(cfg['modes'])
    K, L = 2*M, len(cp['states'])-1
    target = np.asarray(desired_height, float)
    if (response.get('converged') is not True or response.get('failed')
            or packet['request'].get('audit') is not True
            or not isinstance(response.get('audit'), dict)
            or not math.isfinite(response.get('residual', math.nan))
            or response['residual'] > cfg['solveTolerance']
            or cp['cutHeight'] != packet['request']['height']
            or cp['parameters']['modes'] != M or cp['parameters']['depth'] != L
            or target.shape != (M,) or not np.all(np.isfinite(target))):
        raise ValueError('An actual complete original audited source and full finite target are required')
    states = np.asarray(cp['states'], float)
    if states.shape != (L+1,K) or not np.all(np.isfinite(states)):
        raise ValueError('Source checkpoint omits original finite unknowns')
    selected = None
    for p in sorted(native_runs.glob('*-jac-record.json'), reverse=True):
        value = load(p)
        if value.get('withJac') is True and helpers.state_match(p, packet):
            selected = p
            break
    if selected is None:
        raise ValueError('No true complete fresh native J exactly matches all accepted states')
    native_record = load(selected)
    for key in ('input','output','manifest','static_metadata'):
        if ref(native_record[key]['path']) != native_record[key]:
            raise ValueError('Changed original native evidence: '+key)
    manifest = load(native_record['manifest']['path'])
    provenance.verify_references(manifest)
    source = Path(manifest['source_topic'])
    for name, expected in packet['source_sha256'].items():
        if sha(source/'scripts'/name) != expected:
            raise ValueError('Accepted packet source differs from its actual native source: '+name)
    meta = helpers.checked(native_record['static_metadata'])
    if len(meta['stages']) != L or meta['scope']['M'] != M:
        raise ValueError('Native stage count/modes differ')
    target_path = out/'desired-height.json'
    target_path.write_text(json.dumps(target.tolist())+'\n')
    background_path = out/'original-tangent-scales.json'
    export = Path(__file__).with_name('export_tail_tangent_scales.mjs')
    command = ['node', str(export), str(source), str(packet_path), str(target_path), str(background_path)]
    with (out/'scale-export.log').open('x') as stream:
        subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, check=True)
    background = load(background_path)
    if (background['M'] != M or background['K'] != K or background['depth'] != L
            or background['rawNode'] != cp['rawNode']
            or background['portRatios'] != [row['portRatio'] for row in meta['stages']]):
        raise ValueError('Original constructor/normalization differs from actual native metadata')
    data = Path(native_record['output']['path']).read_bytes()
    expected_header = b'VFN4OUT1'+struct.pack('<4i',1,M,L,1)+native_record['payload_token'].encode('ascii')
    if data[:88] != expected_header:
        raise ValueError('Wrong actual native full-J header/identity')
    J, flows = np.empty((L,K,K)), np.empty((L,K))
    offset = 88
    for n in range(L):
        index,status = struct.unpack_from('<2i',data,offset)
        offset += 8
        if index != n or status != 0:
            raise ValueError('Native J is not a complete success in original stage order')
        state = np.frombuffer(data,dtype='<f8',count=K+2,offset=offset)
        offset += 8*(K+2)
        tangent = np.frombuffer(data,dtype='<f8',count=(K+2)*K,offset=offset).reshape(K+2,K)
        offset += 8*(K+2)*K
        ratio = background['portRatios'][n]
        flows[n] = state[:K]
        flows[n,M:] /= ratio
        J[n] = tangent[:K]
        J[n,M:,:] /= ratio
        offset += 64
    if offset != len(data) or not np.all(np.isfinite(J)) or not np.all(np.isfinite(flows)):
        raise ValueError('Native J extent or finite output changed')
    residuals = flows-states[:-1]
    deep = np.asarray(background['deepGraph'])
    deep_end = states[-1,M:]-deep*states[-1,:M]
    target_delta = np.asarray(background['desiredTarget'])-states[0,:M]
    payload = dict(mode='correction', M=M, depth=L, Js=J.reshape(L,K*K).tolist(),
        scales=background['scales'], deepGraph=background['deepGraph'],
        residuals=residuals.tolist(), deepEnd=deep_end.tolist(), targetDelta=target_delta.tolist())
    linear_path = scripts/'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'
    begun = time.monotonic()
    solved = subprocess.run([sys.executable,str(linear_path)], input=json.dumps(payload),
                            text=True,capture_output=True)
    (out/'linear.stderr').write_text(solved.stderr)
    if solved.returncode != 0:
        raise RuntimeError('Original complete linear system failed: '+solved.stderr[-2000:])
    linear = json.loads(solved.stdout)
    if not math.isfinite(linear.get('normwise_backward_error',math.nan)) or linear['normwise_backward_error'] >= 1e-11:
        raise ValueError('Original sparse full-system backward-error gate failed')
    delta = np.asarray(linear.pop('delta'),float)
    if delta.shape != states.shape or not np.all(np.isfinite(delta)):
        raise ValueError('The original linear solve lost finite node components')
    guess = states+delta
    if not np.all(np.isfinite(guess)):
        raise ValueError('Nonfinite full-state predictor')
    predicted = copy.deepcopy(cp)
    predicted.update(states=guess.tolist(), cutHeight=target.tolist(),
        rawStates=guess[np.asarray(cp['rawNode'],int)].tolist(),
        scope='UNACCEPTED all-node tangent/Newton initializer. No nonlinear residual, guard, audit, or final full-H/J acceptance is asserted.')
    artifact = out/'unaccepted-full-state-predictor.json.gz'
    artifact.write_bytes(gzip.compress((json.dumps(dict(checkpoint=predicted,accepted=False,
        predictor_kind='actual-fresh-all-stage-J-full-unknown-Newton-step',
        source_accepted_packet=ref(packet_path),source_native_record=ref(selected)),separators=(',',':'))+'\n').encode(),mtime=0))
    numeric = dict(scope=__doc__, source=ref(__file__), export_source=ref(export),
        linear_solver_source=ref(linear_path), accepted_source_packet=ref(packet_path),
        actual_fresh_native_record=ref(selected), native_manifest=native_record['manifest'],
        original_scaling=ref(background_path), desired_height=ref(target_path),
        M=M, stages=L, state_rows=L+1, state_columns=K, all_unknown_count=(L+1)*K,
        accepted_source_residual=response['residual'],
        source_height_f64le_sha256=hashlib.sha256(np.asarray(cp['cutHeight'],dtype='<f8').tobytes()).hexdigest(),
        target_height_f64le_sha256=hashlib.sha256(np.asarray(target,dtype='<f8').tobytes()).hexdigest(),
        linear=linear, wall_linear_seconds=time.monotonic()-begun,
        interior_old_residual_included=True, deep_old_residual_included=True,
        all_new_dirichlet_rows_included=True,
        original_mean_tangent_rows_excluded_from_shooting_unknowns=True,
        delta_absolute_max=float(np.max(np.abs(delta))),
        predictor=ref(artifact), predictor_accepted=False,
        full_height_J_returned=False, original_nonlinear_worker_still_required=True)
    (out/'summary.json').write_text(json.dumps(numeric,indent=2)+'\n')
    return numeric


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','packet','native-runs','height-reference','outdir'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--height-key',default='candidate_H')
    parser.add_argument('--factor',type=float,default=1.)
    a=parser.parse_args()
    height=load(a.height_reference)
    for key in a.height_key.split('.'):
        height=height[key]
    M=read_packet(a.packet)['config']['modes']
    value=np.asarray(height[:M],float)
    if not 0<a.factor<=1:
        raise ValueError('Use a positive harmonic amplitude factor at most one')
    if a.factor!=1:
        value=value*a.factor**np.arange(1,M+1)
    result=predict(a.repo,a.packet,a.native_runs,value,a.outdir)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()

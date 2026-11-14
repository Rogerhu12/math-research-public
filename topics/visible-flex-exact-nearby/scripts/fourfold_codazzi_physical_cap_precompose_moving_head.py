#!/usr/bin/env python3
"""All physical cap columns precomposed with the true moving-head inlet.

The saved binary64 matrices are exact dyadic Hermite proposals. Their
floating products and square-root normalization are not claimed exact:
the independent continuous consumer evaluates these saved bytes, and
compares the actual left trace with the directed full inlet matrix.
The physical C mean is an output/matching row, never a free Dirichlet
input. All physical states and every outer regular row remain present.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import time
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import numpy as np
from numpy.lib.format import open_memmap
from fourfold_codazzi_block_qr_persistent import atomic_json,atomic_npz
from fourfold_phase_metric_defect import sha

KIND='actual_repaired_physical128_cap_precomposed_moving96_L2_proposal_v1'
PARENT='actual_continuous_repaired_physical_cap_padded_Dirichlet_graph_proposal_v3'
MATRIX='actual_repaired_moving96_physical128_complete_C_port_matrix'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--proposal',type=Path,required=True)
    ap.add_argument('--matrix',type=Path,default=Path('notes/2026-11-14-R133-repaired-moving96-physical128-C-matrix-native.json.gz'))
    ap.add_argument('--work',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--batch',type=int,default=8)
    args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every actual earlier outcome')
    if args.batch<1:raise ValueError('positive complete radial batch required')
    parent=read(args.proposal);matrix=read(args.matrix)
    if (parent.get('kind')!=PARENT or not parent.get('complete') or parent.get('failure')
        or not parent['actual_finite_backward_check']['passed']
        or parent['complete_physical_input_columns']!=128
        or parent['complete_physical_state_dimension']!=257):
        raise ValueError('the actual complete 128-column parent cap proposal is required')
    if (matrix.get('kind')!=MATRIX or not matrix.get('complete')
        or matrix['candidate_sha256']!=CANDIDATE or matrix['derived_definition_sha256']!=REPAIR
        or matrix['exact_cut']!='9/10' or not matrix['whole_original_eta']
        or matrix['parameter_half_width']!='1/1000000000'
        or matrix['physical_rows']!=128 or len(matrix['input_columns'])!=97
        or not matrix['h1_all_columns_exactly_zero']):
        raise ValueError('the complete directed same-centre true physical inlet is required')
    if any(not g['passed'] for g in matrix['gates']):
        raise ValueError('the actual directed matrix gates were not all passed')
    model=parent['identity']['model']
    if (model['derived_centre_definition_sha256']!=REPAIR
        or model['exact_alpha']!=matrix['exact_alpha']
        or model['exact_nu']!=matrix['exact_nu']):
        raise ValueError('the parent cap and exact inlet describe different centres')
    rows=matrix['rows'];den=Fraction(matrix['dyadic_midpoint_denominator'])
    H=np.empty((128,97))
    for l,row in enumerate(rows,1):
        if row['physical_index']!=l or row['physical_frequency']!=4*l:
            raise ValueError('all physical inlet rows must be retained in their actual order')
        vals=row['exact_binary64_proposal_hex']
        if len(vals)!=97 or len(row['dyadic_midpoint_numerators'])!=97:
            raise ValueError('the true mean and every moving cosine column are required')
        for j,(value,numerator) in enumerate(zip(vals,row['dyadic_midpoint_numerators'])):
            exact=Fraction(int(numerator),int(den));value=float.fromhex(value)
            if not np.isfinite(value) or abs(Fraction.from_float(value)-exact)>Fraction(1,2**52):
                raise ValueError('the exact binary64 inlet proposal exceeds its paid rounding')
            H[l-1,j]=value
    # The true domain basis is (1,sqrt(2)cos(4phi),...). These rounded
    # normalizations are only proposal arithmetic; the endpoint consumer
    # uses exact arb sqrt(2) against the complete directed true H matrix.
    scaling=np.ones(97);scaling[1:]=np.sqrt(2.)
    T=H*scaling[None,:]
    original=Path(parent['work_directory']);inputs=[original/'matrix-RHS'/n for n in
        ('state.npy','derivative-left.npy','derivative-right.npy')]
    endpoint_path=original/'physical-endpoint-graph.npz'
    if sha(inputs[0])!=parent['full_matrix_state']['sha256'] or sha(endpoint_path)!=parent['physical_endpoint_graph']['sha256']:
        raise ValueError('the complete original matrix or endpoint bytes changed')
    endpoint=np.load(endpoint_path,allow_pickle=False);nodes=endpoint['nodes']
    input_sha={str(p):sha(p) for p in inputs+[endpoint_path]}
    identity=dict(parent_proposal_sha256=sha(args.proposal),parent_case=parent['case'],
        model=model,derived_centre_definition_sha256=REPAIR,
        physical_input_matrix_sha256=sha(args.matrix),physical_modes=128,
        moving_nonzero_modes=96,complete_even_input_columns=97,
        exact_input_basis='1 and sqrt(2)*cos(4*j*phi), j=1,...,96; actual normalized L2 circle',
        source_sha256=sha(__file__),full_parent_array_sha256=input_sha,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in
            ('fourfold_codazzi_block_qr_persistent.py','fourfold_phase_metric_defect.py')})
    case=hashlib.sha256(json.dumps(identity,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    directory=args.work/case;directory.mkdir(parents=True,exist_ok=True)
    values=directory/'matrix-RHS';values.mkdir(exist_ok=True)
    checkpoint=directory/'precomposition-progress.json'
    if checkpoint.exists():
        progress=read(checkpoint)
        if progress['identity']!=identity:raise ValueError('the exact precomposition input identity changed')
    else:
        progress=dict(identity=identity,next_array=0,next_row=0)
        atomic_json(checkpoint,progress)
    doc=dict(kind=KIND,complete=False,failure=None,identity=identity,case=case,
        work_directory=str(directory),source_sha256=sha(__file__),
        mathematical_certificate=False,parent_finite_gate_only=parent['actual_finite_backward_check'],
        exact_shared_dyadic_Hermite_definition=True,true_physical_mean_is_a_matching_output=True,
        complete_continuous_error_still_required=True)
    try:
        for k,path in enumerate(inputs):
            source=np.load(path,mmap_mode='r',allow_pickle=False)
            shape=(len(nodes)-(k!=0),257,128)
            if source.shape!=shape:raise ValueError('the full original physical matrix shape changed')
            target=values/path.name
            if k<progress['next_array']:continue
            out=np.load(target,mmap_mode='r+',allow_pickle=False) if target.exists() else open_memmap(
                target,mode='w+',dtype=np.float64,shape=(shape[0],257,97))
            if out.shape!=(shape[0],257,97):raise ValueError('the full moving inlet output shape changed')
            for first in range(progress['next_row'],shape[0],args.batch):
                last=min(shape[0],first+args.batch)
                out[first:last]=np.matmul(source[first:last],T)
                if not np.all(np.isfinite(out[first:last])):raise ValueError('nonfinite exact dyadic proposal')
                out.flush();progress.update(next_array=k,next_row=last);atomic_json(checkpoint,progress)
            progress.update(next_array=k+1,next_row=0);atomic_json(checkpoint,progress)
        state=np.load(values/'state.npy',mmap_mode='r',allow_pickle=False)
        ep=directory/'physical-endpoint-graph.npz'
        if not ep.exists():
            atomic_npz(ep,nodes=nodes,left_state=state[0],right_state=state[-1],
                inner_graph=np.vstack((state[0,:128],state[0,128:129])),
                binary64_input_transform=T,binary64_proposal_scaling=scaling,
                physical_C_mean_matching_row=np.r_[float.fromhex(
                    matrix['physical_mean_row']['exact_binary64_proposal_hex']),np.zeros(96)])
        outputs=[values/n for n in ('state.npy','derivative-left.npy','derivative-right.npy')]
        doc.update(complete=True,stage='complete_exact_dyadic_precomposed_trial',
            radial_nodes=len(nodes),complete_physical_state_dimension=257,
            complete_moving_even_input_columns=97,
            original_complete_cap_input_columns=128,
            full_matrix_inputs={str(p):sha(p) for p in outputs},
            full_matrix_state=dict(path=str(outputs[0]),sha256=sha(outputs[0])),
            physical_endpoint_graph=dict(path=str(ep),sha256=sha(ep)),
            actual_physical_inlet_matrix=dict(path=str(args.matrix),sha256=sha(args.matrix)),
            complete_physical_inlet_tail_not_deleted=True,
            no_new_finite_or_continuous_gate_claimed_from_float_matrix_multiplication=True)
    except Exception as exc:
        doc['failure']=dict(type=type(exc).__name__,message=str(exc));raise
    finally:
        doc['wall_seconds']=time.monotonic()-started;atomic_json(args.out,doc)
    print({k:doc.get(k) for k in ('complete','case','wall_seconds','failure')},flush=True)


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Complete inlet/outer-boundary terms of the precomposed cap proposal.

This is an independently usable boundary certificate, not a cap body
residual or a complete body inverse. The left C mean is retained as a
matching output and is never charged as a Dirichlet datum.
"""
import argparse
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_physical_cap_matrix_residual_v3 import (
    read,boundary_error,ffrac,CURRENT,REPAIR)
from fourfold_phase_metric_defect import save,sha,record


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--proposal',type=Path,required=True)
    p.add_argument('--inlet',type=Path,default=Path('notes/2026-11-14-R133-repaired-moving96-physical128-C-matrix-native.json.gz'))
    p.add_argument('--q-vector',type=Path,default=Path('notes/2026-11-13-R133-regular-r25over8-q256-floating.json'))
    p.add_argument('--q-native',type=Path,default=Path('notes/2026-11-13-R133-regular-r25over8-q256-long-ports-native.json.gz'))
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=256;ctx.cap=6
    if a.out.exists():raise FileExistsError('preserve all previous complete or failed certificates')
    proposal=read(a.proposal)
    if (proposal.get('kind')!='actual_repaired_physical128_cap_precomposed_moving96_L2_proposal_v1'
        or not proposal.get('complete') or proposal.get('failure')
        or proposal['identity']['derived_centre_definition_sha256']!=REPAIR
        or proposal['identity']['physical_input_matrix_sha256']!=sha(a.inlet)):
        raise ValueError('the complete same-centre precomposed matrix is required')
    directory=Path(proposal['work_directory']);files=[directory/'matrix-RHS'/n for n in
        ('state.npy','derivative-left.npy','derivative-right.npy')]
    for file in files:
        if sha(file)!=proposal['full_matrix_inputs'][str(file)]:
            raise ValueError('an exact complete Hermite input changed')
    endpoint=directory/'physical-endpoint-graph.npz'
    if sha(endpoint)!=proposal['physical_endpoint_graph']['sha256']:
        raise ValueError('the complete actual endpoint matrix changed')
    states=[np.load(file,mmap_mode='r',allow_pickle=False) for file in files]
    ep=np.load(endpoint,allow_pickle=False);nodes=list(map(ffrac,ep['nodes']))
    if states[0].shape!=(len(nodes),257,97) or states[1].shape!=(len(nodes)-1,257,97) or states[2].shape!=states[1].shape:
        raise ValueError('all physical states and all moving even input columns are required')
    result=boundary_error(*states,nodes,a.q_vector,a.q_native,a.inlet)
    if any(isinstance(v,arb) and not v.is_finite() for v in result.values()):
        raise ArithmeticError('nonfinite boundary term is not a certificate')
    save(a.out,dict(kind='actual_complete_precomposed_physical_cap_boundary_terms_v1',
        complete=True,source_sha256=sha(__file__),candidate_sha256=CURRENT,
        derived_definition_sha256=REPAIR,
        inputs={str(f):sha(f) for f in [a.proposal,a.inlet,a.q_vector,a.q_native]+files+[endpoint]},
        consumer_sha256=sha(Path(__file__).with_name('fourfold_codazzi_physical_cap_matrix_residual_v3.py')),
        exact_left='9/10',exact_right='25/8',whole_original_eta=True,
        parameter_half_width='1/1000000000',physical_modes=128,
        complete_even_moving_input_columns=97,
        exact_input_basis='1,sqrt(2)*cos(4*j*phi), j=1,...,96; normalized circle L2',
        bounds={k:(record(v) if isinstance(v,arb) else v) for k,v in result.items()},
        complete_physical_input_tail_retained=True,
        physical_C_mean_is_independent_matching_row=True,
        no_complete_cap_body_error_or_whole_inverse_claimed=True))
    print({k:float(v) for k,v in result.items() if isinstance(v,arb)},flush=True)


if __name__=='__main__':main()

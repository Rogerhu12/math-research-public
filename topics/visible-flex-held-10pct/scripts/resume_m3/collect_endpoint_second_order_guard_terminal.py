#!/usr/bin/env python3
"""Collect the complete lambda-one C2-guard failure without rerunning a solver."""
import argparse
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import sys
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    data=Path(p).read_bytes()
    return json.loads(gzip.decompress(data) if Path(p).suffix=='.gz' else data)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();run=a.run.resolve()
    launch=load(run/'continuation-command.json')
    summary=load(run/'seed-summary.json')
    wrapper=load(run/'seed-round-record.json')
    cp_path=run/'seed.json.gz';cp=load(cp_path)
    worker=load(run/'seed_tail_worker_exit.json')
    if launch.get('returncode')!=0 or worker['events'][-1]['returncode']!=0:
        raise ValueError('Expected the observed caught-error terminal, not a missing process')
    if cp['solver_success'] or summary['solver_success']:
        raise ValueError('This collector describes the recorded failed endpoint')
    if cp['actual_outer_checks'] != [{'outer':0,'inner_success':False,
            'message':'The maximum number of mesh nodes is exceeded.'}]:
        raise ValueError('The original inner stopping classification differs')
    if summary.get('tail_calls')!=2 or len(list(run.glob('seed_tail_[0-9]*.json.gz')))!=2:
        raise ValueError('The recorded run has different actual-tail calls')
    if 'summary' in cp or 'tail_seam' in cp:
        raise ValueError('The partial physical checkpoint unexpectedly has a complete audit')
    for sources in (launch['inputs'],launch['input_coefficient_chunks'],wrapper['source_hashes']):
        for path,digest in sources.items():
            if sha(path)!=digest:raise ValueError('A declared input/source changed: '+path)
    chunks=[];next_state=0
    for item in cp['pp_coefficient_chunks']:
        path=run/item['file']
        if item['state_first']!=next_state or sha(path)!=item['sha256']:
            raise ValueError('Physical quintic chunk identity/coverage mismatch')
        value=np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False)
        if value.dtype!=np.dtype('float64') or not np.isfinite(value).all():
            raise ValueError('The saved physical polynomial is not a finite float64 array')
        chunks.append(dict(path=str(path),sha256=sha(path),shape=list(value.shape),
            state_first=item['state_first'],state_last_exclusive=item['state_last_exclusive']))
        next_state=item['state_last_exclusive']
    if next_state!=3*cp['config']['modes']+1:
        raise ValueError('Incomplete physical coefficient coverage')
    tails=[];H=None
    for index in (1,2):
        path=run/f'seed_tail_{index:04d}.json.gz';record=load(path);r=record['response']
        if not r['converged'] or not math.isfinite(r['residual']) or r['residual']>=record['config']['solveTolerance']:
            raise ValueError('The unchanged starting tail did not pass its original gate')
        if H is None:H=record['request']['height']
        elif H!=record['request']['height']:raise ValueError('The two calls did not use identical original H')
        jac=r.get('heightJetJacobian') or []
        if not all(math.isfinite(x) for x in jac):raise ValueError('A returned Jacobian entry is not finite')
        tails.append(dict(call=index,path=str(path),sha256=sha(path),
            original_gate=record['config']['solveTolerance'],residual=r['residual'],
            request_jacobian=record['request']['jacobian'],request_audit=record['request']['audit'],
            returned_jacobian_entries=len(jac),full_finite_audit_returned=r.get('audit') is not None,
            last_iteration=r['history'][-1]))
    result=dict(status='Complete original-gate failure; no accepted lambda-one prefix',
        actual_execution=dict(session=14903,observed_returncode=0,
            launcher_returncode=launch['returncode'],worker_exit=worker,
            prefix_coupler_seconds=summary['seconds'],wrapper_seconds=wrapper['seconds'],
            interpretation='The wrapper catches the recorded audit exception; exit 0 is not mathematical acceptance.'),
        command=launch['command'],input_sha256=launch['inputs'],
        input_coefficient_chunks=launch['input_coefficient_chunks'],
        source_sha256=wrapper['source_hashes'],collector_sha256=sha(__file__),
        terminal_files={str(run/n):sha(run/n) for n in ['continuation-command.json',
            'seed-summary.json','seed-round-record.json','seed-c2-restart-record.json',
            'seed_tail_worker_exit.json','seed_tail_worker_stderr.log','worker-trace.jsonl']},
        partial_physical_checkpoint=dict(path=str(cp_path),sha256=sha(cp_path),chunks=chunks,
            role='Saved before adaptive.audit. Complete physical quintic representation of a failed inner iterate; '
                'not an accepted prefix or recovered original raw cubic.'),
        inner=dict(solver_success=cp['solver_success'],message=cp['message'],nodes=cp['nodes'],
            max_rms_collocation_residual=cp['max_rms_collocation_residual'],
            newton_domain_audit=cp['newton_domain_audit'],actual_outer_checks=cp['actual_outer_checks']),
        profile=cp['frozen_profile'],q_gauge=cp['gauge_amplitude'],actual_q=cp['actual_primary_amplitude'],
        core_settings=cp['core_round_settings'],numerical_rho_guard=cp['core_numerical_positivity_guard'],
        parameters=cp['parameters'],central_correction_scales=cp['central_correction_scales'],
        physical_controls=(np.asarray(cp['parameters'][1:])*np.asarray(cp['central_correction_scales'])).tolist(),
        tail_calls=tails,new_candidate_height_queried=False,
        subsequent_audit=dict(error=summary['error'],metric_report_saved=False,seam_report_saved=False,
            location_scope='Control flow and the saved pre-audit checkpoint locate the error after '
                'the inner failure, within the subsequent prefix/seam audit phase. Both adaptive.audit '
                'and the initial velocity_s in seam_audit can raise this error before another tail call. '
                'No original traceback was recorded, so the exact subcall and radial/material point '
                'are unresolved; absence of a saved metric does not prove adaptive.audit had not returned.'),
        limits='New second-order rho allowance preserved all equations and gates but did not produce a '
            'lambda-one prefix. No global metric or geometry result is available for this failed iterate; '
            'the two accepted tail responses belong only to the unchanged initial H.')
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),sha256=sha(a.out),nodes=cp['nodes'],
                         rms=cp['max_rms_collocation_residual'])),flush=True)


if __name__=='__main__':main()

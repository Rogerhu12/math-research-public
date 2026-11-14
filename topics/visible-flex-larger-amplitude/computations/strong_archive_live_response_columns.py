#!/usr/bin/env python3
"""Archive complete original external columns while the larger response runs.

AI-assisted research, strong_recovery, 2026-11-13.
Each saved full/half/forcing vector must match its actual completed original
column receipt and complete accepted baseline. The original half-step formula
is replayed on every complete vector, and both original streamed QR backward
check receipts are retained. No Jacobian, solve, forcing, exchange direction,
core-held combination, geometric field or new solution is computed here.
This partial recovery is deliberately not a finished geometry-response packet.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name] = '1'
import numpy as np
import strong_actual_fixed_control_response as original

HERE = Path(__file__).resolve().parent
ORIGINAL_SHA = 'a2552b5b67e7555b3d402f10127a89fcf99eea566d7768a4050535c8105c2de1'
PRODUCER_SHA = 'd83947ea4f7457435a272863b9ba88a9a7ddfe551e76dc4db596c63dc61de212'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('plan','archive-topic','out-prefix'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--fields',nargs='+',required=True)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text()); root = Path(plan['cwd'])
    if (sha(HERE/'strong_actual_fixed_control_response.py') != ORIGINAL_SHA
            or sha(HERE/'strong_samechart_initial_laws_anchor_response.py') != PRODUCER_SHA
            or plan['response_fields'][:len(args.fields)] != args.fields
            or len(set(args.fields)) != len(args.fields)):
        raise ValueError('The original declared response prefix/source differs')
    for name, expected in plan['source_sha256'].items():
        if sha(root/name) != expected:
            raise ValueError('A frozen response source changed: '+name)
    phase = plan['phases'][0]; command = phase['command']; prefix = root/phase['prefix']
    def argument(name):
        if command.count(name) != 1:
            raise ValueError('Expected one original argument '+name)
        return root/command[command.index(name)+1]
    hashes = {str(Path(__file__)):sha(__file__)}
    checkpoint, raw_path, tail_path = map(argument, ('--response-checkpoint','--response-raw','--response-tail'))
    saved, raw, tail, unused_vectors, identity = original.validate_inputs(checkpoint,raw_path,tail_path,hashes)
    M, nodes = int(saved['modes']), int(identity['nodes']); n = 3*M+1
    parameter_units = np.r_[saved['core']['coefficients'][0],saved['central_correction_scales']]
    physical_units = np.r_[np.full(n*nodes,saved['gauge_amplitude']),parameter_units]
    if parameter_units.shape != (M,):
        raise ValueError('The full original physical parameter units differ')
    log_path = Path(str(prefix)+'-stdout.log'); lines = log_path.read_bytes().splitlines()
    rows, solves, selected_lines, reached = [], [], [], False
    for line in lines:
        selected_lines.append(line)
        try:
            event = json.loads(line)
        except (ValueError,TypeError):
            continue
        if event.get('event') == 'disk_linear_solve_checked':
            solves.append(event)
        if event.get('event') == 'actual_fixed_external_response':
            rows.append(event)
            if len(rows) == len(args.fields):
                reached=True;break
    if (not reached or [row['field'] for row in rows] != args.fields
            or len(solves) != 2*len(rows)
            or not all(row.get('passed') and row['tolerance']==5e-11 for row in solves)):
        raise ValueError('The requested complete original column/QR receipts are not yet present')
    entries, columns = [], []
    def put(path, data, relative=None):
        name = relative or 'notes/'+path.name; destination=args.archive_topic/name
        if len(data)>=5_000_000:
            raise ValueError('A recovery file exceeds the repository limit')
        existed=destination.exists()
        if existed:
            if destination.read_bytes()!=data:raise ValueError('Immutable recovery bytes differ')
        else:
            with destination.open('xb') as stream:stream.write(data)
        item=dict(file=name,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),
                  reused_existing_archival_bytes=existed,original_file=str(path))
        entries.append(item);return item
    for index,row in enumerate(rows):
        field=row['field']; arrays={}; array_entries=[]
        for kind in ('external','external-half','forcing-full','forcing-half'):
            path=Path(str(prefix)+'-'+kind+'-'+field+'.npy.gz');data=path.read_bytes()
            value=np.load(io.BytesIO(gzip.decompress(data)),allow_pickle=False)
            if (value.shape!=(n*nodes+M,) or value.dtype!=np.float64 or not np.isfinite(value).all()):
                raise ValueError('The complete original vector differs: '+str(path))
            arrays[kind]=value;array_entries.append(put(path,data))
        scaled=physical_units*arrays['external'];scaled_half=physical_units*arrays['external-half']
        relative=float(np.max(abs(scaled-scaled_half))/max(np.max(abs(scaled)),np.finfo(float).tiny))
        width=2e-6*max(.1,abs(float(saved['frozen_profile'].get(field,0.))))
        if (relative!=row['half_step_response_relative_difference'] or relative>2e-4
                or row['width']!=width or row['half_width']!=width/2
                or not np.array_equal(parameter_units*arrays['external'][n*nodes:],row['physical_core_derivative'])):
            raise ValueError('The original complete half-step/core response did not replay exactly')
        columns.append(dict(original_receipt=row,original_QR_receipts=solves[2*index:2*index+2],
            complete_vector_shape=[n*nodes+M],complete_original_half_formula_exactly_replayed=True,
            complete_physical_core_derivative_replayed=True,arrays=array_entries))
    trace=b'\n'.join(selected_lines)+b'\n'
    trace_path=Path(str(args.out_prefix)+'-original-trace-prefix.jsonl.gz')
    with trace_path.open('xb') as stream:stream.write(gzip.compress(trace,mtime=0))
    put(trace_path,trace_path.read_bytes())
    put(Path(__file__),Path(__file__).read_bytes(),'computations/'+Path(__file__).name)
    result=dict(schema='live-original-external-full-half-response-recovery-v1',scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_sha256=sha(__file__),
        actual_original_plan=dict(file=str(args.plan),sha256=sha(args.plan)),
        original_live_prefix=str(prefix),available_external_fields=args.fields,
        declared_complete_batch_fields=plan['response_fields'],
        full_batch_finished=False,not_a_finished_geometry_response_packet=True,
        no_core_held_or_low_core_exchange_vectors_created=True,
        full_original_external_vectors_and_actual_receipts_only=True,
        complete_baseline_identity=identity,baseline_input_sha256=hashes,
        modes=M,nodes=nodes,angular=saved['config']['angular'],columns=columns,
        original_live_job_unchanged=True,new_ODE_Node_Jacobian_or_QR_started=False,
        matrix_backward_checks_are_original_receipts_not_new_recomputations=True,
        files=entries,total_bytes=sum(item['bytes'] for item in entries))
    out=Path(str(args.out_prefix)+'.json')
    with out.open('x') as stream:json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    destination=args.archive_topic/'notes'/out.name
    with destination.open('xb') as stream:stream.write(out.read_bytes())
    print(json.dumps(dict(recovery=str(destination),sha256=sha(destination),
        columns=len(columns),files=len(entries),bytes=result['total_bytes'],
        no_finished_batch_or_new_solution_claim=True)),flush=True)


if __name__=='__main__':
    main()

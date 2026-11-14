#!/usr/bin/env python3
"""Prepare the existing v5 expanded-domain cache in separate child processes.

This changes process lifetime only. Each actual proof is run by the frozen
fourfold_parameter_expanded_time_domain CLI and v5 subsequently repeats its
full identity/dependency checks. No bound or failed analytic gate is promoted
by this controller. An interrupted child is recorded and stops this command.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

from fourfold_phase_beta_affine import sha
from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_forward_density_pipeline_Q1024_v3 import save
from fourfold_forward_density_pipeline_spatial_v7 import checked_extended_domain


def cache_key(args, selected, germ):
    """Exactly the frozen v5 cache key; the consumer validates the proof."""
    proof = Path(__file__).with_name('fourfold_parameter_expanded_time_domain.py')
    half = max(Fraction(args.uniform_half_width), Fraction(args.expanded_proof_half_width))
    return dict(domain=sha(args.domain), expanded=sha(selected), germ=germ,
                descriptor=sha(args.descriptor), local_root=sha(args.local_root_jets),
                wide_root=sha(args.wide_root_jets), half_width=str(half),
                nodes=args.expanded_proof_nodes, root_nodes=args.root_nodes,
                bits=args.expanded_proof_bits, radial_degree=args.radial_degree,
                proof_source=sha(proof))


def run(args):
    started = time.monotonic()
    domain = read(args.domain)
    proof_source = Path(__file__).with_name('fourfold_parameter_expanded_time_domain.py')
    candidates = ([Path(args.expanded_domain)] if args.expanded_domain is not None else
                  sorted(args.expanded_domain_directory.glob(
                      'forward_%04d_*.json.gz' % domain['segment'])))
    result = dict(kind='separate_process_preparation_of_existing_parameter_proof_cache',
        complete=False, source_sha256=sha(__file__), actual_proof_source_sha256=sha(proof_source),
        domain_path=str(args.domain), domain_sha256=sha(args.domain),
        descriptor_sha256=sha(args.descriptor), segment=domain['segment'],
        cache_key_matches_frozen_v5=True, parameter_density_not_computed=True,
        attempts=[], children=[], actual_complete_larger_parameter_domains=[])
    args.parameter_proof_directory.mkdir(parents=True, exist_ok=True)
    args.parameter_proof_lock_directory.mkdir(parents=True, exist_ok=True)
    args.log_directory.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    for germ in range(len(domain['germs'])):
        selected = None
        for candidate in candidates:
            try:
                doc = read(candidate)
                if (doc.get('original_domain_sha256') != sha(args.domain)
                    or not doc.get('proved_selected_actual_germs')):
                    continue
                checked_extended_domain(candidate, args.domain, germ)
                selected = candidate
                break
            except (KeyError, ValueError, FileNotFoundError) as exc:
                result['attempts'].append(dict(path=str(candidate), germ=germ, rejected=str(exc)))
        if selected is None:
            continue
        key = cache_key(args, selected, germ)
        digest = hashlib.sha256(json.dumps(key, sort_keys=True).encode()).hexdigest()
        path = args.parameter_proof_directory / ('forward_%04d_%s.json.gz' % (domain['segment'], digest[:20]))
        log = args.log_directory / ('expanded_parameter_%04d_%s.log' % (domain['segment'], digest[:20]))
        with (args.parameter_proof_lock_directory / (digest+'.lock')).open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            child = dict(path=str(path), proof_key=key, reused=path.exists(), log_path=str(log))
            if not path.exists():
                command = [sys.executable, '-u', str(proof_source),
                    '--descriptor', str(args.descriptor), '--domain', str(args.domain),
                    '--expanded-domain', str(selected), '--local-root-jets', str(args.local_root_jets),
                    '--wide-root-jets', str(args.wide_root_jets), '--half-width', key['half_width'],
                    '--nodes', str(args.expanded_proof_nodes), '--root-nodes', str(args.root_nodes),
                    '--germ', str(germ), '--radial-degree', str(args.radial_degree),
                    '--bits', str(args.expanded_proof_bits), '--out', str(path)]
                child['command'] = command
                print(dict(stage='separate_parameter_proof_start', segment=domain['segment'],
                           germ=germ, path=str(path)), flush=True)
                with log.open('w') as output:
                    completed = subprocess.run(command, stdout=output, stderr=subprocess.STDOUT, env=env)
                child['returncode'] = completed.returncode
                child['log_sha256'] = sha(log)
                if completed.returncode not in (0, 2) or not path.exists():
                    result['children'].append(child)
                    result.update(process_interruption=True, cause='unresolved process termination; not a mathematical failure',
                                  wall_seconds=time.monotonic()-started)
                    save(args.out, result)
                    return 3
            doc = read(path)
            if (doc.get('kind') != 'actual_expanded_time_parameter_source_bounds'
                or doc['source_sha256'] != key['proof_source']
                or doc['domain_sha256'] != key['domain']
                or doc['expanded_true_domain_sha256'] != key['expanded']
                or doc['selected_germ_index'] != germ
                or doc['nodes'] != key['nodes'] or doc['root_nodes'] != key['root_nodes']
                or doc['bits'] != key['bits']
                or Fraction(doc['exact_parameter_half_width']) != Fraction(key['half_width'])):
                raise ValueError('existing parameter proof cache has an unexpected identity')
            child.update(sha256=sha(path), actual_proof_complete=bool(doc.get('complete')),
                         proof_failure=doc.get('failure'))
            result['children'].append(child)
            if doc.get('complete'):
                result['actual_complete_larger_parameter_domains'].append(dict(path=str(path), sha256=sha(path)))
    result.update(complete=True, all_requested_child_processes_finished=True,
                  next_density_consumer_must_run_full_checked_parameter_proof=True,
                  wall_seconds=time.monotonic()-started)
    save(args.out, result)
    print(dict(stage='separate_parameter_proof_preparation_complete', segment=domain['segment'],
               proofs=len(result['actual_complete_larger_parameter_domains']), sha256=sha(args.out)), flush=True)
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    base = Path('data/phase_ring_continuation')
    p.add_argument('--descriptor', type=Path, default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--domain', type=Path, required=True)
    p.add_argument('--expanded-domain', type=Path)
    p.add_argument('--expanded-domain-directory', type=Path, default=base/'step5_expanded_time_domain_full')
    p.add_argument('--local-root-jets', type=Path, default=base/'type_fixed_step02_d5_step5_local_parameter_root_jets_h1e14.json')
    p.add_argument('--wide-root-jets', type=Path, default=base/'type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json')
    p.add_argument('--uniform-half-width', type=Fraction, default=Fraction(0))
    p.add_argument('--expanded-proof-half-width', type=Fraction, default=Fraction(1, 10**9))
    p.add_argument('--expanded-proof-nodes', type=int, default=512)
    p.add_argument('--root-nodes', type=int, default=1024)
    p.add_argument('--expanded-proof-bits', type=int, default=320)
    p.add_argument('--radial-degree', type=int, default=40)
    p.add_argument('--parameter-proof-directory', type=Path, default=base/'step5_expanded_parameter_time_domain_full')
    p.add_argument('--parameter-proof-lock-directory', type=Path, default=Path('/tmp/visible-flex-parameter-domain-locks'))
    p.add_argument('--log-directory', type=Path, default=Path('/workspace/scratch/f6a2c7886477/parameter-density-logs'))
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if (args.uniform_half_width < 0 or args.expanded_proof_half_width < 0
        or min(args.expanded_proof_nodes, args.root_nodes, args.expanded_proof_bits, args.radial_degree) <= 0):
        raise ValueError('invalid exact parameter or proof dimensions')
    return run(args)


if __name__ == '__main__':
    raise SystemExit(main())

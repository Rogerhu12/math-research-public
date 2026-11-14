#!/usr/bin/env python3
"""Consume each complete ordinary principal chain into an actual T2 Norm."""
import argparse
from pathlib import Path
import subprocess
import sys
import tarfile
import time

from p41_ordinary_t2_etale_norm47 import read, save, sha


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--qc-dir', type=Path, required=True)
    ap.add_argument('--aggregate', type=Path, required=True)
    args = ap.parse_args()
    own = Path(__file__).parent
    expected = [7, 12, 5, 11, 15, 19, 24, 27, 28, 30, 32, 38, 39, 40, 41, 43, 45, 46, 1]
    output_dir = args.qc_dir/'ordinary-F2-norms'
    output_dir.mkdir(parents=True, exist_ok=True)
    executor = own/'p41_ordinary_t2_etale_norm47.py'
    old_executor = own/'p41_ordinary_t2_principal_norm47.py'
    completed = {}
    while len(completed) < 19:
        progress = False
        for j in expected:
            disk = 'ORD_j'+str(j).zfill(2)
            if disk in completed:
                continue
            support = output_dir/(disk+'_actual_T2_support47.json.gz')
            second = args.qc_dir/'ordinary-second-kind'/(disk+'_second_kind_complete47.json.gz')
            is_cm = j in [38, 39, 40]
            work = args.qc_dir/('CM-ordinary-abel-with-transports' if is_cm else 'ordinary-abel-with-transports')
            transport_base = args.qc_dir/('CM-ordinary-principal-transports' if is_cm else 'ordinary-principal-transports')
            transport = transport_base/disk
            multiplication = work/(disk+'_multiply47.json.gz')
            if not support.exists() or not read(support).get('complete_actual_T2_support') or not second.exists():
                continue
            if not multiplication.exists():
                continue
            if is_cm and not (transport/'transport_manifest47.json').exists():
                archive = args.qc_dir/('p41_'+disk+'_principal_transports47.tar.gz')
                assert archive.exists()
                with tarfile.open(archive, 'r:gz') as tf:
                    for member in tf.getmembers():
                        pp = Path(member.name)
                        assert member.isfile() and pp.parts[0] == 'CM-ordinary-principal-transports' and '..' not in pp.parts
                        target = args.qc_dir/pp
                        content = tf.extractfile(member).read()
                        target.parent.mkdir(parents=True, exist_ok=True)
                        if target.exists():
                            assert target.read_bytes() == content
                        else:
                            target.write_bytes(content)
            if not (transport/'transport_manifest47.json').exists():
                continue
            principal = output_dir/(disk+'_actual_principal_function47.json.gz')
            norm = output_dir/(disk+'_actual_T2_principal_norm47.json.gz')
            for target in [principal, norm]:
                seed = args.qc_dir/target.name
                if not target.exists() and seed.exists():
                    target.write_bytes(seed.read_bytes())
            if not principal.exists():
                subprocess.run([sys.executable, str(own/'p41_principal_chain_flatten47.py'),
                                '--transport-directory', str(transport), '--second-kind-certificate', str(second),
                                '--bases', str(args.script_dir/'data/p41_hecke3_abel_bases_checkpoint.json.gz'),
                                '--output', str(principal)], check=True)
            p = read(principal)
            assert p['complete_exact_integer_principal_function_expression']
            assert p['input_sha256'][second.name] == sha(second)
            wanted_source = sha(executor) if 'branch_records' in read(support) else sha(old_executor)
            valid = norm.exists() and read(norm).get('complete_actual_principal_norm_on_T2_P') and read(norm)['source_sha256'] == wanted_source
            if not valid:
                subprocess.run([sys.executable, str(executor), '--script-dir', str(args.script_dir),
                                '--support', str(support), '--principal-expression', str(principal),
                                '--transport-directory', str(transport), '--based-points', str(args.qc_dir/'p41_all19_based_points47.json.gz'),
                                '--second-kind-certificate', str(second), '--multiplication', str(multiplication),
                                '--cache-dir', str(args.qc_dir/'ordinary-norm-cache'), '--output', str(norm)], check=True)
            n = read(norm)
            assert n['disk_id'] == disk and n['input_sha256'][principal.name] == sha(principal)
            completed[disk] = {'disk_id': disk, 'support_basename': support.name, 'support_sha256': sha(support),
                               'principal_expression_basename': principal.name, 'principal_expression_sha256': sha(principal),
                               'T2_norm_basename': norm.name, 'T2_norm_sha256': sha(norm),
                               'actual_norm_mod47four': n['actual_norm_Phi_T2_P_mod47four'],
                               'actual_log_norm_mod47four': n['actual_log_norm_Phi_T2_P_mod47four'],
                               'complete_actual_principal_T2_norm': True}
            aggregate = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
                         'complete_all19_actual_T2_principal_norms': len(completed) == 19,
                         'completed_count': len(completed),
                         'records': [completed[k] for k in sorted(completed)],
                         'remaining_disk_ids': ['ORD_j'+str(k).zfill(2) for k in expected if 'ORD_j'+str(k).zfill(2) not in completed],
                         'source_sha256': sha(__file__), 'executor_sha256': sha(executor),
                         'complete_local_QC_heights': False, 'complete_common_roots': False}
            save(args.aggregate, aggregate)
            progress = True
            print('CHECKPOINT actual T2 principal Norm', len(completed), '/19', disk,
                  'log', n['actual_log_norm_Phi_T2_P_mod47four'], 'SHA', sha(norm), flush=True)
        if not progress and len(completed) < 19:
            time.sleep(10)


if __name__ == '__main__':
    main()

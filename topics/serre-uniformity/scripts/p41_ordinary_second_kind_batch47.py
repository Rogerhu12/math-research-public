#!/usr/bin/env python3
"""Consume each completed ordinary chain once and checkpoint its108 integrals."""
import argparse
from pathlib import Path
import sys
import time


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--based-points', type=Path, required=True)
    ap.add_argument('--second-kind', type=Path, required=True)
    ap.add_argument('--workdir', type=Path, required=True)
    ap.add_argument('--transport-dir', type=Path, required=True)
    ap.add_argument('--build-dir', type=Path, required=True)
    ap.add_argument('--output-dir', type=Path, required=True)
    ap.add_argument('--aggregate', type=Path, required=True)
    ap.add_argument('--disk', action='append', required=True)
    ap.add_argument('--poll-seconds', type=float, default=10)
    args = ap.parse_args()
    assert 0 < args.poll_seconds <= 30
    sys.path.insert(0, str(args.script_dir.resolve()))
    import p41_ordinary_second_kind47 as core
    read, save, sha = core.read, core.save, core.sha
    args.output_dir.mkdir(parents=True, exist_ok=True)
    E = core.Engine(args.script_dir.resolve(), args.based_points, args.second_kind, args.build_dir)
    expected = args.disk
    assert len(expected) == len(set(expected)) == 16
    completed = {}
    while len(completed) < len(expected):
        progress = False
        for disk_id in expected:
            if disk_id in completed:
                continue
            outpath = args.output_dir/(disk_id+'_second_kind_complete47.json.gz')
            abpath = args.workdir/(disk_id+'_Abel47.json.gz')
            mpath = args.workdir/(disk_id+'_multiply47.json.gz')
            directory = args.transport_dir/disk_id
            manifest_path = directory/'transport_manifest47.json'
            if not (abpath.exists() and mpath.exists() and manifest_path.exists()):
                continue
            manifest = read(manifest_path)
            if manifest['completed_Abel_sha256'] != sha(abpath):
                continue
            if outpath.exists():
                out = read(outpath)
                assert out['complete_actual54_second_kind_center_integrals']
                assert out['disk_id'] == disk_id and out['source_sha256'] == sha(core.__file__)
                assert out['input_sha256'][abpath.name] == sha(abpath)
                assert out['input_sha256'][mpath.name] == sha(mpath)
                assert out['input_sha256'][args.second_kind.name] == sha(args.second_kind)
            else:
                endpoint, actual, multiple = E.endpoint(abpath, mpath)
                chain, derivative = E.chain(disk_id, directory, multiple)
                value = E.a.scale(E.r.sub(actual, derivative), multiple['sign']*pow(multiple['target_multiplier'], -1, core.Q))
                E.covariance(value)
                out = {'level': 41, 'auxiliary_prime': core.P, 'precision': 4, 'modulus': core.Q,
                       'disk_id': disk_id, 'complete_terminal_second_kind_integrals': True,
                       'complete_actual54_second_kind_center_integrals': True,
                       'complete_local_QC_heights': False, 'complete_common_roots': False,
                       'endpoint': endpoint,
                       'pole_family2_indices_1based': E.nu['pole_indices_1based'],
                       'input_sha256': dict(E.inputs, **{abpath.name: sha(abpath), mpath.name: sha(mpath)}),
                       'native': E.native, 'source_sha256': sha(core.__file__),
                       'actual54_second_kind_integrals_of_C_mod47four': E.r.to_json(value),
                       'principal_chain': chain,
                       'formula': 'sign*m*integral_C(nu)=tiny_A1(t)(nu)+dlog((v1/f0)*(F/G))|Z2-dlog(f_final)|Z2',
                       'coordinator_sha256': sha(__file__)}
                save(outpath, out)
            ab = read(abpath)
            completed[disk_id] = {
                'disk_id': disk_id,
                'canonical_holomorphic_integrals_of_C_mod47four': ab['canonical_log_C_mod47four'],
                'cyclic_coordinates_of_C_mod47cubed': ab['actual_center_C_cyclic_coordinates_mod47cubed'],
                'second_kind_integrals_of_C_mod47four': out['actual54_second_kind_integrals_of_C_mod47four'],
                'Abel_sha256': sha(abpath), 'second_kind_certificate_sha256': sha(outpath),
                'complete_all108_actual_integrals': True,
            }
            aggregate = {
                'level': 41, 'auxiliary_prime': core.P, 'precision': 4, 'modulus': core.Q,
                'complete_all16_ordinary_deRham_integrals': len(completed) == len(expected),
                'completed_disk_count': len(completed),
                'complete_local_QC_heights': False, 'complete_common_roots': False,
                'remaining_disk_ids': [key for key in expected if key not in completed],
                'records': [completed[key] for key in expected if key in completed],
                'second_kind_basis_sha256': sha(args.second_kind),
                'input_basis_sha256': E.inputs, 'source_sha256': sha(__file__),
                'engine_sha256': sha(core.__file__),
            }
            save(args.aggregate, aggregate)
            progress = True
            print('CHECKPOINT actual ordinary108 integrals', len(completed), '/16', disk_id,
                  'certificate SHA', sha(outpath), 'aggregate SHA', sha(args.aggregate), flush=True)
        if len(completed) < len(expected) and not progress:
            time.sleep(args.poll_seconds)
    print('PASS all16 ordinary center108 actual integrals; SHA', sha(args.aggregate), flush=True)


if __name__ == '__main__':
    main()

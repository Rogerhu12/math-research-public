#!/usr/bin/env python3
"""Finish the three ordinary CM second-kind constants and audit R237 independently."""
import argparse
from pathlib import Path
import subprocess
import sys
import time


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--based-points', type=Path, required=True)
    ap.add_argument('--CM-anchors', type=Path, required=True)
    ap.add_argument('--second-kind', type=Path, required=True)
    ap.add_argument('--workdir', type=Path, required=True)
    ap.add_argument('--transport-dir', type=Path, required=True)
    ap.add_argument('--build-dir', type=Path, required=True)
    ap.add_argument('--output-dir', type=Path, required=True)
    ap.add_argument('--aggregate', type=Path, required=True)
    args = ap.parse_args()
    import p41_ordinary_second_kind47 as core
    read, save, sha = core.read, core.save, core.sha
    anchors = read(args.CM_anchors)
    assert anchors['complete_three_ordinary_CM_anchors']
    expected = {a['disk_id']: a for a in anchors['three_ordinary_CM_anchors']}
    assert sorted(expected) == ['ORD_j38', 'ORD_j39', 'ORD_j40']
    args.output_dir.mkdir(parents=True, exist_ok=True)
    completed = {}
    while len(completed) < 3:
        progress = False
        for disk_id, old in expected.items():
            if disk_id in completed:
                continue
            abpath = args.workdir/(disk_id+'_Abel47.json.gz')
            mpath = args.workdir/(disk_id+'_multiply47.json.gz')
            directory = args.transport_dir/disk_id
            manifest_path = directory/'transport_manifest47.json'
            if not (abpath.exists() and mpath.exists() and manifest_path.exists()):
                continue
            manifest = read(manifest_path)
            if manifest['completed_Abel_sha256'] != sha(abpath):
                continue
            ab = read(abpath)
            assert ab['complete_actual_center_Abel_constant']
            assert ab['actual_center_C_cyclic_coordinates_mod47cubed'] == old['actual_center_C_cyclic_coordinates_mod47cubed']
            print('PASS independent complete304-bit CM versus signed Jacobi calibration', old['discriminant'], disk_id, flush=True)
            output = args.output_dir/(disk_id+'_second_kind_complete47.json.gz')
            if not output.exists():
                command = [sys.executable, str(Path(core.__file__).resolve()),
                           '--script-dir', str(args.script_dir), '--based-points', str(args.based_points),
                           '--second-kind', str(args.second_kind), '--Abel', str(abpath), '--multiplication', str(mpath),
                           '--transport-directory', str(directory), '--build-dir', str(args.build_dir), '--output', str(output)]
                subprocess.run(command, check=True)
            data = read(output)
            assert data['complete_actual54_second_kind_center_integrals']
            assert data['input_sha256'][abpath.name] == sha(abpath)
            assert data['input_sha256'][mpath.name] == sha(mpath)
            completed[disk_id] = {
                'discriminant': old['discriminant'], 'disk_id': disk_id,
                'all54_independent_CM_holomorphic_coordinates_match_R237': True,
                'canonical_holomorphic_integrals_of_C_mod47four': ab['canonical_log_C_mod47four'],
                'cyclic_coordinates_of_C_mod47cubed': ab['actual_center_C_cyclic_coordinates_mod47cubed'],
                'second_kind_integrals_of_C_mod47four': data['actual54_second_kind_integrals_of_C_mod47four'],
                'complete_all108_actual_integrals': True,
                'Abel_sha256': sha(abpath), 'second_kind_certificate_sha256': sha(output),
            }
            aggregate = {
                'level': 41, 'auxiliary_prime': 47, 'modulus': 47**4, 'precision': 4,
                'complete_three_ordinary_CM_deRham_integrals': len(completed) == 3,
                'completed_disk_count': len(completed),
                'complete_local_QC_heights': False, 'complete_common_roots': False,
                'remaining_disk_ids': [k for k in expected if k not in completed],
                'records': [completed[k] for k in expected if k in completed],
                'independent_R237_input_sha256': sha(args.CM_anchors),
                'second_kind_basis_sha256': sha(args.second_kind),
                'source_sha256': sha(__file__), 'engine_sha256': sha(core.__file__),
            }
            save(args.aggregate, aggregate)
            print('CHECKPOINT actual CM108 integrals', len(completed), '/3', disk_id, 'SHA', sha(args.aggregate), flush=True)
            progress = True
        if len(completed) < 3 and not progress:
            time.sleep(10)
    print('PASS all3 ordinary CM108 integrals and independent R237 checks', sha(args.aggregate), flush=True)


if __name__ == '__main__':
    main()

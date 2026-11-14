#!/usr/bin/env python3
"""Actual synthetic byte/storage replay only; no mathematical solver calls."""
from __future__ import annotations

import argparse
import copy
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import traceback

import numpy as np


HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def check(ok, message):
    if not ok:
        raise AssertionError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def ident(path):
    raw = Path(path).read_bytes()
    return {'file': str(Path(path).resolve()), 'bytes': len(raw), 'sha256': sha(raw)}


def npz_payload(arrays):
    stream = io.BytesIO()
    np.savez(stream, **arrays)
    return gzip.compress(stream.getvalue(), mtime=0)


def compare_npz(original, restored):
    check(original == restored, 'Complete logical gzip/NPZ bytes differ')
    count = 0
    with np.load(io.BytesIO(gzip.decompress(original)), allow_pickle=False) as a, \
         np.load(io.BytesIO(gzip.decompress(restored)), allow_pickle=False) as b:
        check(a.files == b.files, 'NPZ member order/names differ')
        for name in a.files:
            x, y = a[name], b[name]
            check(x.dtype == y.dtype and x.dtype.descr == y.dtype.descr and
                  x.shape == y.shape and x.strides == y.strides,
                  'Saved array dtype/shape/strides differ')
            check(x.flags.c_contiguous == y.flags.c_contiguous and
                  x.flags.f_contiguous == y.flags.f_contiguous,
                  'Saved array memory order differs')
            check(x.tobytes(order='C') == y.tobytes(order='C') and
                  x.tobytes(order='F') == y.tobytes(order='F'),
                  'Saved array bit pattern differs')
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    report = {'schema': '78718-synthetic-byte-storage-check-v1',
              'status': 'STARTED_SYNTHETIC_STORAGE_ONLY', 'solver_calls': 0,
              'research_geometry_generated': False, 'production_ready': False,
              'complete_consumer_closure_checked': False,
              'python': sys.version, 'numpy': np.__version__,
              'sources': [ident(HERE/x) for x in
                  ('78718-prefix-byte-shards-v1.py', '78718-prefix-storage-v1.py',
                   '78718-prefix-check-byte-storage-v1.py')],
              'positive_cases': [], 'rejection_cases': []}
    code = 2
    try:
        c = load('check_78718_codec', HERE/'78718-prefix-byte-shards-v1.py')
        h = load('check_78718_helper', HERE/'78718-prefix-storage-v1.py')
        patterns = np.array([0x0000000000000000, 0x8000000000000000,
            0x7ff8000000000001, 0xfff8000000000042,
            0x7ff0000000000001, 0xfff0000000000007,
            0x7ff0000000000000, 0xfff0000000000000,
            0x0000000000000001, 0x8000000000000001,
            0x3ff0000000000000, 0x0010000000000000], dtype='<u8')
        bits = patterns.view('<f8')
        arrays = {
            'bit_patterns': bits.reshape(3, 4),
            'scalar_nan': bits[2:3].reshape(()),
            'empty_axes': np.empty((2, 0, 3, 0), dtype='<f8'),
            'fortran': np.asfortranarray(bits.reshape(3, 4)),
            'noncontiguous_source': np.arange(96, dtype='<i8').reshape(8, 12)[::2, ::3],
            'big_endian_bits': patterns.astype('>u8').view('>f8'),
            'complex_bits': patterns.view('<c16').reshape(2, 3),
            'integer_scalar': np.array(2**64-1, dtype='<u8'),
            'unicode': np.array([['alpha', 'beta'], ['gamma', 'delta']], dtype='<U5'),
            'byte_strings': np.array([b'\x00a', b'\xff\x00'], dtype='S3'),
        }
        payload = npz_payload(arrays)
        descriptor, pieces = c.encode_bytes(payload, part_stem='synthetic-bits', chunk_bytes=37)
        decoded = c.decode_bytes(descriptor, pieces, logical_sha256=sha(payload),
                                 logical_bytes=len(payload))
        count = compare_npz(payload, decoded)
        report['positive_cases'].append({'case': 'arbitrary_shapes_dtypes_orders_and_float_bits',
            'array_count': count, 'logical_bytes': len(payload), 'logical_sha256': sha(payload),
            'parts': len(pieces), 'contains_nan_payloads_signed_zero_and_infinity': True,
            'comparison': 'Full logical bytes and loaded dtype/shape/strides/C-and-F byte strings'})

        def reject(name, action):
            try:
                action()
            except (ValueError, OSError, TypeError, KeyError) as exc:
                report['rejection_cases'].append({'case': name, 'exception_type': type(exc).__name__})
            else:
                raise AssertionError('Corruption was accepted: '+name)

        def decode(d=descriptor, p=pieces, expected=sha(payload), size=len(payload)):
            return c.decode_bytes(d, p, logical_sha256=expected, logical_bytes=size)

        bad = dict(pieces); bad.pop(next(iter(bad)))
        reject('missing_part', lambda: decode(p=bad))
        bad = dict(pieces); bad['extra.bin.gz'] = gzip.compress(b'x', mtime=0)
        reject('extra_part', lambda: decode(p=bad))
        bad = copy.deepcopy(descriptor); bad['parts'][0], bad['parts'][1] = bad['parts'][1], bad['parts'][0]
        reject('reordered_parts', lambda: decode(d=bad))
        bad = copy.deepcopy(descriptor); bad['parts'][1]['offset'] += 1
        reject('gap_in_offsets', lambda: decode(d=bad))
        bad = copy.deepcopy(descriptor); bad['parts'][1]['offset'] -= 1
        reject('overlap_in_offsets', lambda: decode(d=bad))
        bad = copy.deepcopy(descriptor); bad['parts'][0]['index'] = False
        reject('boolean_integer', lambda: decode(d=bad))
        bad = copy.deepcopy(descriptor); bad['parts'][0]['file'] = '../outside.bin.gz'
        reject('traversal_filename', lambda: decode(d=bad))
        bad = copy.deepcopy(descriptor); bad['parts'][1]['file'] = bad['parts'][0]['file']
        reject('duplicate_filename', lambda: decode(d=bad))
        bad = copy.deepcopy(descriptor); bad['parts'][0]['raw_bytes'] = 4_600_001
        reject('raw_part_above_limit', lambda: decode(d=bad))
        bad = copy.deepcopy(descriptor); bad['parts'][0]['stored_bytes'] = 5_000_000
        reject('stored_part_at_file_limit', lambda: decode(d=bad))
        reject('wrong_outer_logical_sha', lambda: decode(expected='0'*64))
        bad = copy.deepcopy(descriptor); bad['logical_bytes'] += 1
        reject('wrong_logical_length', lambda: decode(d=bad))
        badparts = dict(pieces); name = descriptor['parts'][0]['file']
        blob = bytearray(badparts[name]); blob[-1] ^= 1; badparts[name] = bytes(blob)
        reject('stored_payload_corruption', lambda: decode(p=badparts))
        baddesc = copy.deepcopy(descriptor); badparts = dict(pieces)
        replacement = b'x'*baddesc['parts'][0]['raw_bytes']
        badparts[name] = gzip.compress(replacement, mtime=0)
        baddesc['parts'][0]['stored_sha256'] = sha(badparts[name])
        baddesc['parts'][0]['stored_bytes'] = len(badparts[name])
        reject('valid_gzip_with_wrong_raw_bytes', lambda: decode(d=baddesc, p=badparts))
        baddesc['parts'][0]['raw_sha256'] = sha(replacement)
        reject('all_local_hashes_changed_but_global_sha_bound', lambda: decode(d=baddesc, p=badparts))
        reject('duplicate_descriptor_json_key', lambda: c.parse_json(b'{"a":1,"a":2}'))
        reject('nonfinite_descriptor_json', lambda: c.parse_json(b'{"a":NaN}'))
        reject('empty_logical_payload', lambda: c.encode_bytes(b'', part_stem='empty'))

        with tempfile.TemporaryDirectory(prefix='78718-byte-storage-') as temp:
            work = Path(temp)
            entropy = hashlib.shake_256(b'78718-fixed-storage-cross-boundary-seed-v1').digest(9_300_013)
            large = npz_payload({'entropy': np.frombuffer(entropy, dtype='u1'),
                                 'preserved_bits': bits})
            check(len(large) > 2*c.MAX_RAW_PART, 'Large synthetic case did not span three real parts')
            reference = c.write_bytes(work/'large', large)
            restored, records = c.read_bytes(work/reference['descriptor_file'],
                descriptor_sha256=reference['descriptor_sha256'],
                descriptor_bytes=reference['descriptor_bytes'], logical_sha256=sha(large),
                logical_bytes=len(large))
            compare_npz(large, restored)
            check(all(r['bytes'] < 5_000_000 for r in records), 'A real physical file reached the limit')
            realdesc = c.parse_json((work/reference['descriptor_file']).read_bytes())
            check([r['raw_bytes'] for r in realdesc['parts'][:2]] == [4_600_000, 4_600_000],
                  'The actual maximum-sized byte boundary was not tested')
            report['positive_cases'].append({'case': 'actual_large_npz_disk_round_trip',
                'logical_bytes': len(large), 'logical_sha256': sha(large),
                'logical_container_written_as_one_file': False,
                'parts': len(realdesc['parts']), 'raw_max': max(r['raw_bytes'] for r in realdesc['parts']),
                'physical_max': max(r['bytes'] for r in records),
                'physical_files': [{k:r[k] for k in ('bytes','sha256')} for r in records]})
            # Reusing byte-identical content-addressed output does not replace files.
            check(c.write_bytes(work/'large', large) == reference, 'Identical storage reuse differs')
            conflict = work/realdesc['parts'][0]['file']
            original_member = conflict.read_bytes(); conflict.write_bytes(b'conflict')
            reject('existing_conflicting_content_addressed_file', lambda: c.write_bytes(work/'large', large))
            conflict.write_bytes(original_member)

            nodes, modes = 4, 2
            jets = np.arange(3*nodes*(3*modes+2), dtype='<f8').reshape(3, nodes, 3*modes+2)/128
            jets.view('<u8').ravel()[:len(patterns)] = patterns
            prefix = npz_payload({'mesh': np.arange(nodes, dtype='<f8'), 'jets': jets,
                                  'mean_increments': np.array([0., -0., 0.125], dtype='<f8')})
            storage = h.write_payload(work/'prefix', prefix, nodes=nodes, modes=modes, chunk_bytes=79)
            meta = {'nodes': nodes, 'modes': modes, 'data_storage': storage, 'data_sha256': sha(prefix)}
            meta_path = work/'prefix.json'; meta_path.write_bytes(c.canonical(meta))
            readmeta, readprefix, bindings = h.read_payload(meta_path, verify_arrays=True)
            check(readmeta == meta, 'Helper changed metadata')
            compare_npz(prefix, readprefix)
            check(all(r['bytes'] < 5_000_000 for r in bindings), 'Helper closure exceeded size limit')
            report['positive_cases'].append({'case': 'actual_helper_prefix_layout_and_nan_bits',
                'logical_sha256': sha(prefix), 'logical_bytes': len(prefix),
                'closure_files': len(bindings), 'source_hashes_checked': True})

            for name, replacement in [
                ('mixed_legacy_storage', {**meta, 'data_file': 'legacy.npz.gz'}),
                ('common_cut_mode_used_as_base_mode', {**meta, 'modes': 64}),
                ('boolean_base_nodes', {**meta, 'nodes': True}),
                ('changed_helper_source_identity', {**meta, 'data_storage': {**storage,'reader_sha256':'0'*64}}),
            ]:
                meta_path.write_bytes(c.canonical(replacement))
                reject(name, lambda: h.read_payload(meta_path, verify_arrays=False))
            meta_path.write_bytes(c.canonical(meta))

            relocated = work/'relocated'; relocated.mkdir()
            source_dir = relocated/'scripts'; source_dir.mkdir()
            for name in ('78718-prefix-byte-shards-v1.py', '78718-prefix-storage-v1.py'):
                shutil.copyfile(HERE/name, source_dir/name)
            for item in bindings:
                f = Path(item['file'])
                if f.parent == work:
                    shutil.copyfile(f, relocated/f.name)
            moved = load('relocated_78718_helper', source_dir/'78718-prefix-storage-v1.py')
            mmeta, mpayload, mbind = moved.read_payload(relocated/meta_path.name, verify_arrays=True)
            check(mmeta == meta and mpayload == prefix, 'Relocation changed logical metadata/bytes')
            check(sorted((Path(r['file']).name,r['bytes'],r['sha256']) for r in mbind) ==
                  sorted((Path(r['file']).name,r['bytes'],r['sha256']) for r in bindings),
                  'Relocated file closure identities differ')
            child = '''import importlib.util,json,sys,hashlib
from pathlib import Path
s=importlib.util.spec_from_file_location("isolated_78718_storage",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
meta,payload,records=m.read_payload(Path(sys.argv[2]),verify_arrays=False)
assert "numpy" not in sys.modules and "scipy" not in sys.modules
assert hashlib.sha256(payload).hexdigest()==meta["data_sha256"]
print(json.dumps({"numpy_imported":False,"scipy_imported":False,"closure_files":len(records),"logical_sha256":meta["data_sha256"]}))
'''
            process = subprocess.run([sys.executable, '-I', '-c', child,
                str(source_dir/'78718-prefix-storage-v1.py'), str(relocated/meta_path.name)],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            child_report = json.loads(process.stdout)
            report['positive_cases'].append({'case': 'relocated_actual_hash_only_fresh_child',
                'actual_child_exit_code': process.returncode, **child_report})
            report['temporary_fixture_cleanup'] = 'TemporaryDirectory exits after these checks; no test arrays retained.'
        report['status'] = 'PASS_SYNTHETIC_EXACT_BYTE_STORAGE_ONLY'
        code = 0
    except Exception as exc:
        report.update(status='FAIL_SYNTHETIC_STORAGE_CHECK', error=repr(exc),
                      traceback=traceback.format_exc())
    raw = (json.dumps(report, indent=2, allow_nan=False)+'\n').encode()
    check(len(raw) < 100_000, 'Unexpectedly large synthetic check report')
    with args.out.open('xb') as stream:
        stream.write(raw)
    print(json.dumps({'status': report['status'], 'positive_cases': len(report['positive_cases']),
        'rejection_cases': len(report['rejection_cases']), 'solver_calls': 0,
        'production_ready': False, 'report_bytes': len(raw), 'report_sha256': sha(raw),
        **({'error':report['error']} if 'error' in report else {})}))
    return code


if __name__ == '__main__':
    raise SystemExit(main())

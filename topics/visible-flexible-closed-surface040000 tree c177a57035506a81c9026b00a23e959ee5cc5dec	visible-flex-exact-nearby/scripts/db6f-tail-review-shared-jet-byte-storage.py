#!/usr/bin/env python3
"""Independent standard-library check of frozen storage sources and old bytes.

Does not import the codec, NumPy, any geometry reader, or a numerical backend.
Reads an existing gzip/NPZ/NPY container directly to verify exact payload
identities and its base/common-cut shape distinction. Writes small metadata
only; no descriptor, shard, container, new map, or future positive fixture.
"""
import ast
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import struct
import zipfile

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
NAME = '2026-11-09-db6f-tail-review-shared-jet-byte-storage'
AUTHOR = '2026-11-09-db6f-prefix-shared-jet-byte-storage'
sources = {}


def need(value, message):
    if not value:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve()
    blob = path.read_bytes()
    row = {'path': str(path), 'bytes': len(blob), 'sha256': hashlib.sha256(blob).hexdigest()}
    sources[str(path)] = row
    return row


def verify(row):
    need(identity(row['path']) == row, 'Changed frozen file: ' + row['path'])


def read(path):
    identity(path)
    return json.loads(Path(path).read_text())


def source(path):
    identity(path)
    return Path(path).read_text()


def exclusive(path, obj):
    with Path(path).open('x') as stream:
        json.dump(obj, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')


def function(tree, name):
    matches = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name]
    need(len(matches) == 1, 'Missing unique function: ' + name)
    return matches[0]


def write_before_size_gate(path):
    node = function(ast.parse(source(path)), 'build')
    writes = [call.lineno for call in ast.walk(node) if isinstance(call, ast.Call)
              and isinstance(call.func, ast.Attribute) and call.func.attr == 'write_bytes']
    gates = [test.lineno for test in ast.walk(node) if isinstance(test, ast.Compare)
             and any(isinstance(v, ast.Constant) and v.value == 5000000 for v in test.comparators)]
    need(len(writes) == len(gates) == 1 and writes[0] < gates[0],
         'Unexpected legacy single-container write/size order')
    return {'source': identity(path), 'write_line': writes[0], 'size_gate_line': gates[0],
            'size_gate_is_after_write': True}


def inspect_npy(blob, expected_shape):
    need(blob[:6] == b'\x93NUMPY', 'Wrong original NPY magic')
    major, minor = blob[6:8]
    need((major, minor) in {(1, 0), (2, 0), (3, 0)}, 'Unsupported original NPY version')
    if major == 1:
        hsize, start = struct.unpack('<H', blob[8:10])[0], 10
    else:
        hsize, start = struct.unpack('<I', blob[8:12])[0], 12
    header = ast.literal_eval(blob[start:start+hsize].decode('utf-8' if major == 3 else 'latin1'))
    need(type(header) is dict and set(header) == {'descr', 'fortran_order', 'shape'}, 'Wrong NPY header fields')
    need(header['descr'] == '<f8' and header['fortran_order'] is False
         and header['shape'] == expected_shape, 'Wrong original NPY dtype/order/base shape')
    payload = blob[start+hsize:]
    count = math.prod(expected_shape)
    need(len(payload) == 8*count, 'Original array byte length mismatch')
    need(all(math.isfinite(value[0]) for value in struct.iter_unpack('<d', payload)), 'Nonfinite old array payload')
    if len(expected_shape) == 1 and expected_shape == (2570,):
        previous = None
        for (value,) in struct.iter_unpack('<d', payload):
            need(previous is None or value > previous, 'Old mesh is not strictly increasing')
            previous = value
    return {'dtype': '<f8', 'shape': list(expected_shape), 'c_order_bytes': len(payload),
            'c_order_sha256': hashlib.sha256(payload).hexdigest()}


def main():
    publication_path = NOTES / (AUTHOR + '-publication.json')
    need(identity(publication_path)['sha256'] ==
         '4b7fbcbf61da527ee73f3aa2f85567242321058b9d51b9fec88dcc0fbec023f6',
         'Author storage publication changed')
    publication = read(publication_path)
    need(publication['file_count'] == len(publication['files']) == 6 and
         publication['total_bytes'] == sum(row['bytes'] for row in publication['files']) == 49050,
         'Wrong closed author file count or byte sum')
    for row in publication['files']:
        verify(row)
    ledger = read(NOTES / (AUTHOR + '-sources.json'))
    need(ledger['source_file_count'] == len(ledger['files']) == 21, 'Wrong author source count')
    for row in ledger['files'] + ledger['software']['selected_reader_source_files']:
        verify(row)

    replay_path = NOTES / '2026-11-09-db6f-tail-review-shared-jet-byte-shards-replay.json'
    author_check_path = NOTES / '2026-11-09-db6f-prefix-shared-jet-byte-shards-check.json'
    replay = read(replay_path)
    need(replay_path.read_bytes() == author_check_path.read_bytes(), 'Independent actual replay report is not byte-identical')
    need(replay['negative_case_count'] == len(replay['negative_cases']) == 37
         and all(row['rejected'] is True for row in replay['negative_cases']), 'A frozen negative protocol did not reject')
    need(len({row['case'] for row in replay['negative_cases']}) == 37, 'Repeated negative case name')

    base_path = NOTES / '2026-11-09-db6f-root-flat17-coupled-m12f24.json'
    common_path = NOTES / '2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json'
    base, common = read(base_path), read(common_path)
    data_path = base_path.parent / base['data_file']
    data = data_path.read_bytes()
    need(identity(data_path)['sha256'] == base['data_sha256'] == common['data_sha256'] == replay['logical_sha256'],
         'Old base/common logical data identity differs')
    need(len(data) == replay['logical_bytes'] == 3112330, 'Wrong existing logical byte count')
    need((base['source_modes'], base['modes'], base['nodes'], common['modes']) == (12, 24, 2570, 64),
         'Wrong source/base/common shape distinction')
    need(common['base_geometry_sha256'] == identity(base_path)['sha256'], 'Common map does not bind this base geometry')
    expected = {'mesh': (2570,), 'jets': (3, 2570, 74), 'mean_increments': (2569,)}
    independent_arrays = {}
    with zipfile.ZipFile(io.BytesIO(gzip.decompress(data))) as archive:
        need(len(archive.infolist()) == 3 and set(archive.namelist()) == {name+'.npy' for name in expected},
             'Unexpected original NPZ entries')
        for name, shape in expected.items():
            independent_arrays[name] = inspect_npy(archive.read(name+'.npy'), shape)
    need(independent_arrays == replay['array_ledger'], 'Independent standard-library NPY payload hashes differ')
    raw_total = sum(row['c_order_bytes'] for row in independent_arrays.values())
    need(raw_total == 8*(3*2570*(3*24+2)+2*2570-1) == 4605432,
         'Wrong exact original raw-array size formula')

    parts = replay['memory_only_parts']
    need(len(parts) == 4 and [part['offset'] for part in parts] == [0,1000000,2000000,3000000]
         and sum(part['raw_bytes'] for part in parts) == len(data), 'Wrong actual in-memory partition')
    need(sum(part['stored_bytes'] for part in parts) == replay['stored_total_bytes'] == 3112978
         and max(part['stored_bytes'] for part in parts) == replay['largest_part_bytes'] == 1000323,
         'Wrong actual in-memory compressed sizes')
    for part in parts:
        raw = data[part['offset']:part['offset']+part['raw_bytes']]
        need(hashlib.sha256(raw).hexdigest() == part['raw_sha256'], 'Memory part is not the precise original byte interval')
        # Independently recover the reported part bytes without the codec.
        stored = gzip.compress(raw, mtime=0)
        need(len(stored) == part['stored_bytes'] and hashlib.sha256(stored).hexdigest() == part['stored_sha256']
             and gzip.decompress(stored) == raw, 'Independent gzip slice identity mismatch')
    need(all(replay[key] == 0 for key in ('logical_data_or_parts_written','geometry_reader_calls',
         'geometry_backend_calls','solver_calls','source_root_calls','future_geometry_manifests')),
         'Unexpected author/replay execution scope')

    codec_path = HERE / 'db6f-prefix-shared-jet-byte-shards.py'
    codec_tree = ast.parse(source(codec_path))
    imports = []
    for node in ast.walk(codec_tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    need(set(imports) <= {'__future__','gzip','hashlib','io','json','pathlib','re','typing','numpy'},
         'Unexpected project/numerical-backend import in codec')
    need(not any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and
                 node.func.attr in {'write','write_text','write_bytes','savez','savez_compressed'}
                 for node in ast.walk(codec_tree)), 'Storage codec writes or resaves data')
    reader = function(codec_tree, 'read_bytes')
    need([arg.arg for arg in reader.args.kwonlyargs] ==
         ['descriptor_sha256','nodes','modes','logical_sha256'], 'Missing externally supplied storage identity')
    old_orders = [write_before_size_gate(HERE/name) for name in
                  ('950f-root-fullxyz-hermite.py','db6f-root-mirror-hermite.py')]
    identity(__file__)
    source_path = NOTES / (NAME + '-sources.json')
    frozen = sorted(sources.values(), key=lambda row: row['path'])
    exclusive(source_path, {'status':'FROZEN_PURE_STORAGE_REVIEW_SOURCES',
                           'reviewer':'/root/tail_review_continued_2', 'files':frozen, 'count':len(frozen),
                           'scope':'Frozen codec/inventory and old real M12 byte payload only; no future geometry.'})
    report_path = NOTES / (NAME + '-check.json')
    report = {'status':'PASS_INDEPENDENT_OLD_BYTES_AND_STORAGE_SOURCE_CHECK',
              'scope':__doc__, 'source_ledger':identity(source_path), 'source_count':len(frozen),
              'author_file_count':6, 'author_sources_and_software_rehashed':27,
              'actual_replay_report_byte_identical':True, 'negative_protocols':37,
              'original_logical_bytes':len(data), 'original_logical_sha256':identity(data_path)['sha256'],
              'array_ledger_from_standard_library_NPY_read':independent_arrays,
              'total_exact_raw_array_bytes':raw_total,
              'source_modes':12, 'base_modes':24, 'common_cut_modes':64, 'base_nodes':2570,
              'common_cut_mode_must_not_be_used_for_base_shape':True,
              'verified_slice_count':len(parts), 'stored_total_bytes':replay['stored_total_bytes'],
              'storage_overhead_bytes':replay['stored_total_bytes']-len(data),
              'legacy_write_size_order':old_orders,
              'codec_has_no_project_backend_import_or_write':True,
              'actual_codec_disk_read_entry_called':False,
              'new_data_files':0, 'new_geometry_objects':0, 'solver_backend_calls':0,
              'G5':False, 'README_completed':False}
    exclusive(report_path, report)
    print(json.dumps({'status':report['status'], 'report':identity(report_path),
                      'source_ledger':identity(source_path), 'source_count':len(frozen),
                      'actual_numerical_calls':0}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

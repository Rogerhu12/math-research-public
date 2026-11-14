#!/usr/bin/env python3
"""Bind archived H bits to the original binary base, preserving JSON zero facts.

The original packet and all sidecars are copied unchanged. JavaScript JSON
serialization can map negative zero to positive zero; only that exact numeric
identity is admitted in the JSON checkpoint. Every requested H bit must still
match the original complete binary base. All original nonlinear/Jacobian,
roundtrip, predictor, full-stage and compressed/raw checksum gates remain.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path

ORIGINAL_SHA = '0b8f5380eadc6255f8000a4660e0189b136201d9030550e5aa5e93d85978f8c2'


def main():
    original_path = Path(__file__).resolve().with_name('strong_archive_fullflow_tail_recovery.py')
    data = original_path.read_bytes()
    if hashlib.sha256(data).hexdigest() != ORIGINAL_SHA:
        raise ValueError('The frozen original full-tail archiver differs')
    source = data.decode()
    edits = [
        ("height.tobytes() != np.asarray(checkpoint['cutHeight'], dtype=np.float64).tobytes()",
         "not np.array_equal(height, np.asarray(checkpoint['cutHeight'], dtype=np.float64))"),
        ('    files = {args.packet, manifest_path}\n', '''    checkpoint_height = np.asarray(checkpoint['cutHeight'], dtype=np.float64)
    zero_changes = np.flatnonzero(height.view(np.uint64) != checkpoint_height.view(np.uint64))
    if np.any(height[zero_changes] != 0.) or np.any(checkpoint_height[zero_changes] != 0.):
        raise ValueError('A nonzero requested H bit changed in the original JSON checkpoint')
    base_record = stored['base']
    expected_counts = dict(states=states.size, physicalH=modes, farGraph=modes,
                           radius=1, rawNode=len(checkpoint['rawNode']))
    if (base_record['layout'] != ['states[node][Q_then_pi]', 'physical_H', 'farGraph', 'radius', 'rawNode']
            or base_record['counts'] != expected_counts
            or base_record['encoding'] != 'Float64LE-row-major-gzip-v1'):
        raise ValueError('The complete original binary base layout differs')
    if Path(base_record['file']).name != base_record['file']:
        raise ValueError('The original binary base name is not a basename')
    raw_base = gzip.decompress(checked(manifest_path.parent/base_record['file'], base_record['sha256']))
    if len(raw_base) != 8*sum(expected_counts.values()) or sha(raw_base) != base_record['rawSha256']:
        raise ValueError('The complete original binary base bits failed their hash')
    base_values = np.frombuffer(raw_base, dtype='<f8')
    binary_height = base_values[states.size:states.size+modes]
    if binary_height.tobytes() != height.astype('<f8').tobytes():
        raise ValueError('A requested H bit differs from the original complete binary base')
    height_serialization = dict(complete_request_H_binary_base_bits_equal=True,
        original_JSON_checkpoint_H_values_equal=True,
        original_JSON_checkpoint_H_bits_equal=not bool(len(zero_changes)),
        JSON_stringify_signed_zero_indices=zero_changes.tolist(),
        original_request_H_f64le_sha256=sha(height.astype('<f8').tobytes()),
        original_checkpoint_JSON_H_f64le_sha256=sha(checkpoint_height.astype('<f8').tobytes()),
        original_archiver_source_sha256='''+repr(ORIGINAL_SHA)+''',
        original_packet_and_sidecars_unchanged=True,
        scope='Only original JSON signed-zero serialization; nonzero H bits and complete binary H stay exact.')
    files = {args.packet, manifest_path}
'''),
        ('        full_height=height.tolist(), modes=modes, residual=response[\'residual\'],\n',
         "        full_height=height.tolist(), modes=modes, residual=response['residual'],\n"
         '        original_H_serialization_identity=height_serialization,\n'),
    ]
    changed = source
    for before, after in edits:
        if changed.count(before) != 1:
            raise ValueError('The exact base-H archive source site is not unique')
        changed = changed.replace(before, after, 1)
    reverse = changed
    for before, after in reversed(edits):
        if reverse.count(after) != 1:
            raise ValueError('The original archive reverse source site differs')
        reverse = reverse.replace(after, before, 1)
    if reverse != source:
        raise ValueError('An undeclared original archive operation changed')
    ast.parse(changed, filename='<original-full-tail-archive-exact-binary-H>')
    namespace = {'__name__':'_original_full_tail_archive_exact_base',
                 '__file__':str(Path(__file__).resolve())}
    exec(compile(changed, namespace['__file__'], 'exec'), namespace)
    namespace['main']()


if __name__ == '__main__':
    main()

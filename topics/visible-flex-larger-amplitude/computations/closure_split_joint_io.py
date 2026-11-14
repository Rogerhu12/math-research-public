#!/usr/bin/env python3
"""Small streaming readers shared by the R50 split proposals and row checks.

Only generated repository JSON is accepted.  The large causal triangle is
decoded one output cell at a time; its exact mathematical payload is never
replaced by a floating-point value in the strict verification program.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import gzip
import hashlib
import json
from pathlib import Path


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def opener(path):
    path = Path(path)
    return gzip.open(path, 'rt') if path.suffix == '.gz' else path.open()


def read(path):
    with opener(path) as f:
        return json.load(f)


def iter_array(path, key):
    """Decode one top-level generated array, one element at a time."""
    needle = '"' + key + '"'
    decoder = json.JSONDecoder()
    buf = ''
    with opener(path) as f:
        while True:
            more = f.read(65536)
            if not more:
                raise ValueError('Array field not found: ' + key)
            buf += more
            at = buf.find(needle)
            if at >= 0:
                tail = buf[at + len(needle):].lstrip()
                if tail.startswith(':'):
                    tail = tail[1:].lstrip()
                    if tail.startswith('['):
                        buf = tail[1:]
                        break
            buf = buf[-256:]
        while True:
            buf = buf.lstrip()
            if buf.startswith(','):
                buf = buf[1:].lstrip()
            if buf.startswith(']'):
                return
            try:
                obj, end = decoder.raw_decode(buf)
            except json.JSONDecodeError:
                more = f.read(65536)
                if not more:
                    raise ValueError('Incomplete generated JSON array')
                buf += more
                continue
            yield obj
            buf = buf[end:]


def metadata_without_array(path, key):
    """Read the small top-level metadata while replacing one large array by []."""
    needle = '"' + key + '"'
    prefix = ''
    with opener(path) as f:
        while True:
            more = f.read(65536)
            if not more:
                raise ValueError('Large array field not found: ' + key)
            prefix += more
            at = prefix.find(needle)
            if at >= 0:
                start = at + len(needle)
                while start < len(prefix) and prefix[start].isspace():
                    start += 1
                if start == len(prefix):
                    continue
                if prefix[start] != ':':
                    raise ValueError('The generated field is not an object member')
                start += 1
                while start < len(prefix) and prefix[start].isspace():
                    start += 1
                if start == len(prefix):
                    continue
                if prefix[start] != '[':
                    raise ValueError('The large generated field is not an array')
                buf = prefix[start + 1:]
                prefix = prefix[:start] + '[]'
                break
        depth = 1
        quoted = False
        escaped = False
        while True:
            for pos, ch in enumerate(buf):
                if quoted:
                    if escaped:
                        escaped = False
                    elif ch == '\\':
                        escaped = True
                    elif ch == '"':
                        quoted = False
                elif ch == '"':
                    quoted = True
                elif ch in '[{':
                    depth += 1
                elif ch in ']}':
                    depth -= 1
                    if depth == 0:
                        return json.loads(prefix + buf[pos + 1:] + f.read())
            buf = f.read(65536)
            if not buf:
                raise ValueError('The large generated array is incomplete')


def label(index, count=213):
    if index < 3 * count:
        return dict(block=('low', 'near', 'rest')[index // count],
                    cell=12 + index % count)
    return dict(block='infinite' if index == 3 * count else 'far_z', cell=None)


def validate_common(low, split, density, hashes, density_path):
    cells = list(range(12, 225))
    if low['cells'] != cells or low['modes'] != list(range(2, 93, 2)) or not low['full_range_covered']:
        raise ValueError('All46 true low modes and all213 cells are required')
    if not all(density['gates'].values()):
        raise ValueError('An existing material input has an unpaid stated gate')
    dh = hashes[str(density_path)]
    if any(dh not in doc['input_hashes'].values() for doc in (low, split)):
        raise ValueError('The exact common strip and physical norm differ')
    if not (split['continuous_strip_unchanged'] and split['independent_far_parameter']
            and split['complete_mean_and_pointwise_inverse']):
        raise ValueError('The common strip, complete mean and independent far ball must remain')
    if not (split['original_kernel_identity_bitwise'] and split['original_far_and_pure_identity_bitwise']
            and split['original_kernel_identity_count'] == 213 * 214 // 2):
        raise ValueError('The split must reproduce the complete original paid kernel')
    for name, bounds in [('near', (94, 184)), ('rest', (186, 8190))]:
        group = split['groups'][name]
        if (group['first_mode'], group['last_mode']) != bounds:
            raise ValueError('The true disjoint frequency supports changed')
    if (low['far_strip'], low['far_physical_node'], split['z_log2']) != (38, 225, -2200):
        raise ValueError('The exact R18 far normalization differs')
    if [r['cell'] for r in split['cells']] != cells or [r['cell'] for r in low['rows']] != cells:
        raise ValueError('A complete row domain is missing')
    if [r['cell'] for r in density['rows']] != cells:
        raise ValueError('The complete true material domain is missing')
    return cells

#!/usr/bin/env python3
"""Explicit provenance guards for the new strong same-q-strip rescaling.

The original successful q checker and its reader remain frozen.  Strong
uppers are required to declare their rescaling and must NOT claim that
they reproduce the original q kernel bitwise.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import json
from pathlib import Path
from closure_split_joint_io import digest, read, iter_array, metadata_without_array, label, opener
from closure_split_joint_io import validate_common as validate_q


def read_field(path, key):
    """Read one uniquely named generated field without decoding its siblings."""
    needle = '"' + key + '"'
    decoder = json.JSONDecoder()
    buf = ''
    with opener(path) as stream:
        while True:
            more = stream.read(65536)
            if not more:
                raise ValueError('The generated field is missing: ' + key)
            buf += more
            at = buf.find(needle)
            if at >= 0:
                tail = buf[at + len(needle):].lstrip()
                if tail.startswith(':'):
                    buf = tail[1:].lstrip()
                    break
            buf = buf[-256:]
        while True:
            try:
                value, end = decoder.raw_decode(buf)
                return value
            except json.JSONDecodeError:
                more = stream.read(65536)
                if not more:
                    raise ValueError('The generated field is incomplete: ' + key)
                buf += more


def validate_common(low, split, density, hashes, density_path):
    if 'q_split_origin' not in split:
        return validate_q(low, split, density, hashes, density_path)
    cells = list(range(12, 225))
    if low['cells'] != cells or low['modes'] != list(range(2, 93, 2)) or not low['full_range_covered']:
        raise ValueError('The entire true low46/cell213 domain is required')
    if not all(density['gates'].values()) or split.get('source_gates') != density['gates']:
        raise ValueError('The exact strong material/rescaling gates are not all paid')
    dh = hashes[str(density_path)]
    if any(dh not in doc['input_hashes'].values() for doc in (low, split)):
        raise ValueError('The strong low/high norms are not the same exact density')
    if not (split['continuous_strip_unchanged'] and split['independent_far_parameter']
            and split['complete_mean_and_pointwise_inverse'] and split['all46_low_parameters_retained']):
        raise ValueError('The common strip, full mean and all46 deep coordinates are required')
    if (split['original_kernel_identity_bitwise'] or split['original_far_and_pure_identity_bitwise']
            or split['original_kernel_identity_count'] != 0):
        raise ValueError('A rescaled strong kernel must not claim bitwise identity to q')
    if split['rescaled_causal_entry_count'] != 213 * 214 // 2:
        raise ValueError('The complete strong causal rescaling is required')
    if not split.get('strong_scale_semantics') or split['new_ODE_or_source_integrations'] != 0:
        raise ValueError('The explicit R42 same-strip scaling provenance is absent')
    origin = split['q_split_origin']
    qpath = Path(origin['path'])
    qsha = digest(qpath)
    if qsha != origin['sha256'] or split['input_hashes'].get(str(qpath)) != qsha:
        raise ValueError('The actual complete q split origin changed')
    qsplit = metadata_without_array(qpath, 'gamma_rows')
    for field in ('original_kernel_identity_bitwise', 'original_far_and_pure_identity_bitwise',
                  'original_kernel_identity_count'):
        if split['q_' + field] != qsplit[field]:
            raise ValueError('A q-origin identity declaration is not the saved paid one')
    if not (qsplit['original_kernel_identity_bitwise'] and qsplit['original_far_and_pure_identity_bitwise']
            and qsplit['original_kernel_identity_count'] == 213 * 214 // 2):
        raise ValueError('The q-origin kernel itself lacks its actual full identity check')
    strip = density['continuous_strip_origin']
    if split['continuous_strip_origin'] != strip:
        raise ValueError('The whole continuous strip differs between strong inputs')
    qdensity_path = Path(strip['path'])
    qdensity_hash = digest(qdensity_path)
    if qdensity_hash != strip['sha256'] or qdensity_hash not in qsplit['input_hashes'].values():
        raise ValueError('The exact original q continuous strip is unavailable')
    if qdensity_hash not in density['input_hashes'].values():
        raise ValueError('The strong density does not retain its q strip origin')
    if low['rescaling']['same_continuous_strip_as'] != str(qdensity_path):
        raise ValueError('The strong low kernel uses another continuous strip')
    if low['rescaling']['actual_full_height_modes'] != 20 or low['rescaling']['old_strong_saved_strip_reused']:
        raise ValueError('This proof is for the specified actual M20 in the explicitly chosen q strip')
    for group, bounds in [('near', (94, 184)), ('rest', (186, 8190))]:
        current = split['groups'][group]
        if (current['first_mode'], current['last_mode']) != bounds:
            raise ValueError('The actual disjoint supports differ')
    if (low['far_strip'], low['far_physical_node'], split['z_log2']) != (38, 225, -2200):
        raise ValueError('The exact R18 far normalization differs')
    if [row['cell'] for row in split['cells']] != cells or [row['cell'] for row in low['rows']] != cells:
        raise ValueError('The full strong output row domain is missing')
    if [row['cell'] for row in density['rows']] != cells:
        raise ValueError('The full strong material row domain is missing')
    return cells

#!/usr/bin/env python3
"""Read-only discovery of completed actual block leaves.

This helper never declares a leaf mathematically usable: it checks the block
and every saved byte identity, then returns a candidate to the unchanged
validate_saved / validate_parameter_report functions. A matching parameter
candidate must use the exact currently selected g0 report bytes.
"""
from __future__ import annotations

from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def leaf_key(row):
    return int(row['segment']), *map(Fraction, row['normalized_subspan'])


def checked_source(path, wanted, label):
    path = Path(path)
    if not path.is_file() or sha(path) != wanted:
        raise ValueError('completed block '+label+' source is absent or changed')


def checked_report(path, wanted, source, descriptor_sha, key, kind):
    path = Path(path)
    if sha(path) != wanted:
        raise ValueError('completed block '+kind+' report bytes changed')
    doc = read(path)
    required = ('complete_continuous_true_density_proved' if kind == 'g0'
                else 'complete_continuous_parameter_densities_proved')
    if not doc.get('complete') or not doc.get(required) or doc['source_sha256'] != source:
        raise ValueError('completed block '+kind+' report is incomplete or has another source')
    ref = doc['identity']['reference']
    if (ref['retarget_descriptor_sha256'] != descriptor_sha or ref['leg'] != 'forward'
        or leaf_key(ref) != key):
        raise ValueError('completed block '+kind+' has another exact reference interval')
    for name, digest in doc['dependency_sha256'].items():
        checked_source(Path(__file__).with_name(name), digest, kind+' dependency '+name)
    return doc


def complete_inventory(manifest_path, manifest_sha):
    """The final worker inventory includes reports, exact matrices and logs."""
    inventory_path = manifest_path.with_name('files.json')
    inventory = read(inventory_path)
    if inventory.get('block_manifest_sha256') != manifest_sha:
        raise ValueError('completed block inventory names different manifest bytes')
    entries = {}
    for row in inventory['files']:
        path = Path(row['path'])
        if str(path) in entries:
            raise ValueError('duplicate completed block inventory path')
        if not path.is_file() or path.stat().st_size != row['bytes'] or sha(path) != row['sha256']:
            raise ValueError('completed block inventory file is absent or changed: '+str(path))
        entries[str(path)] = row['sha256']
    return inventory_path, entries


def find_completed_block_seed(directory, descriptor, field_cover, key, scope, *, g0_sha256=None):
    """Return (report Path, provenance) or None; never mutate a block.

    scope is g0/center/uniform. The returned parameter report always binds to
    g0_sha256, not just the same geometric target. The caller must preserve
    provenance and then invoke its existing full mathematical validator.
    """
    if scope not in ('g0', 'center', 'uniform'):
        raise ValueError('unknown completed-block seed scope')
    if scope != 'g0' and not g0_sha256:
        raise ValueError('parameter seeds require the selected exact g0 report SHA')
    descriptor_sha, cover_sha = sha(descriptor), sha(field_cover)
    key = (int(key[0]), Fraction(key[1]), Fraction(key[2]))
    available_workers = {sha(path): path for path in
                         Path(__file__).parent.glob('fourfold_ci_density_block*.py')}
    for manifest_path in sorted(Path(directory).glob('*/block_*/block-manifest.json')):
        block = read(manifest_path)
        if (block.get('kind') != 'actual_independent_forward_density_block'
            or not block.get('complete') or not block.get('complete_requested_g0_block')
            or block.get('descriptor_sha256') != descriptor_sha
            or block.get('field_cover_sha256') != cover_sha):
            continue
        if scope != 'g0' and not block.get('complete_center_and_uniform_g2_block'):
            continue
        matching = [row for row in block['leaves'] if leaf_key(row) == key]
        if len(matching) > 1:
            raise ValueError('completed block duplicates a requested actual leaf')
        if not matching:
            continue
        row = matching[0]
        if scope != 'g0' and row['g0_report_sha256'] != g0_sha256:
            continue
        # A block still being transferred is not a completed local seed.
        if not manifest_path.with_name('files.json').is_file():
            continue
        manifest_sha = sha(manifest_path)
        if block['source_sha256'] not in available_workers:
            raise ValueError('completed block worker source is absent or changed')
        checked_source(block['g0_pipeline_path'], block['g0_pipeline_sha256'], 'g0')
        checked_source(block['parameter_pipeline_path'], block['parameter_pipeline_sha256'], 'parameter')
        if 'parameter_precompute_source_sha256' in block:
            checked_source(Path(__file__).with_name('fourfold_parameter_precompute_expanded_domain.py'),
                           block['parameter_precompute_source_sha256'], 'precompute')
        inventory_path, inventory = complete_inventory(manifest_path, manifest_sha)
        if block.get('full_forward_leg_claimed') or block.get('actual_R31_accepted'):
            raise ValueError('a partial independent block makes an inadmissible full-return claim')
        interval = list(map(int, block['requested_segment_interval']))
        if not 0 <= interval[0] <= key[0] < interval[1] <= 550:
            raise ValueError('block requested segment interval differs from its leaf')
        requested = {(str(Path(item['path'])), item['sha256'])
                     for item in block['requested_exact_domain_leaves']}
        if (row['domain_path'], row['domain_sha256']) not in requested:
            raise ValueError('completed block leaf was not in its actual domain request')
        if sha(row['domain_path']) != row['domain_sha256']:
            raise ValueError('completed block actual domain changed')
        for item in block['leaves']:
            for label in ('g0', 'center', 'uniform'):
                name, digest = item.get(label+'_report_path'), item.get(label+'_report_sha256')
                if name is not None and inventory.get(name) != digest:
                    raise ValueError('completed block report is missing from its full inventory')
        g0 = checked_report(row['g0_report_path'], row['g0_report_sha256'],
                            block['g0_pipeline_sha256'], descriptor_sha, key, 'g0')
        if g0['domain_sha256'] != row['domain_sha256']:
            raise ValueError('completed g0 report changed its requested actual germ domain')
        for label in ('center', 'uniform'):
            if label+'_report_path' not in row:
                if block.get('complete_center_and_uniform_g2_block'):
                    raise ValueError('complete parameter block omits a parameter source')
                continue
            param = checked_report(row[label+'_report_path'], row[label+'_report_sha256'],
                block['parameter_pipeline_sha256'], descriptor_sha, key, label)
            if (param['reference_certificate_sha256'] != row['g0_report_sha256']
                or param['identity']['reference'] != g0['identity']['reference']
                or param['identity']['whole_real_parameter_tube'] != (label == 'uniform')):
                raise ValueError('completed block parameters do not use its exact g0/reference/scope')
        path = Path(row[scope+'_report_path'])
        wanted = row[scope+'_report_sha256']
        if sha(manifest_path) != manifest_sha:
            raise ValueError('completed block changed during read-only validation')
        provenance = dict(block_manifest_path=str(manifest_path), block_manifest_sha256=manifest_sha,
            file_inventory_path=str(inventory_path), file_inventory_sha256=sha(inventory_path),
            block_worker_source_path=str(available_workers[block['source_sha256']]),
            block_worker_source_sha256=block['source_sha256'],
            descriptor_sha256=descriptor_sha, field_cover_sha256=cover_sha,
            requested_segment_interval=interval, selected_segment=key[0],
            normalized_subspan=[str(key[1]), str(key[2])], scope=scope,
            selected_report_path=str(path), selected_report_sha256=wanted,
            selected_g0_report_sha256=row['g0_report_sha256'],
            full_file_inventory_hashes_checked=True,
            existing_mathematical_validator_still_required=True,
            discovery_source_sha256=sha(__file__))
        return path, provenance
    return None

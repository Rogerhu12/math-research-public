"""P96 necessary rematerialization of the same four entire TC trial arrays.

The original floating trial factory reads only Qc32 and its exact base
repair offsets. The direction Z and its fourteen shards are not an input
to that factory. Omitting their unused restoration changes neither the
factory nor any byte of the four required arrays; all original SHA256s
and the exact true-root definition/partition remain mandatory.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False, allow_nan=False)+'\n').encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def restore(np, flint, c, helper, base, iterator, original_repair,
            rows, tc_manifest, tc_state, proposal_path, private, progress):
    require(os.environ.get('OPENBLAS_CORETYPE') == 'Haswell'
            and all(os.environ.get(key) == '1' for key in (
                'OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                'BLIS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')),
            'the original TC floating CPU branch and serial numerical runtime')
    require(flint.ctx.prec == tc_manifest['parameters']['arithmetic_bits'] == 320,
            'the unchanged original directed precision')
    old = tc_state['proposal']
    require(sha(Path(proposal_path).read_bytes()) == old['source_sha256'],
            'the whole unchanged original TC floating proposal source')
    proposal = load(proposal_path, '_P96_original_TC_trial_factory')
    private, arrays = Path(private), {}

    def allocate(name, shape):
        require(name not in arrays and all(type(n) is int and n > 0 for n in shape),
                'one fresh necessary original private array')
        size = math.prod(shape)*8
        require(sum(x['bytes'] for x in arrays.values())+size
                <= tc_manifest['parameters']['maximum_private_live_array_bytes'],
                'the original TC complete temporary array allowance')
        path = private/(name+'.f64')
        require(not path.exists(), 'no prior exact carrier is overwritten')
        value = np.memmap(path, dtype='<f8', mode='w+', shape=shape, order='C')
        arrays[name] = {'path': path, 'shape': shape, 'bytes': size, 'array': value}
        return value

    def release(name):
        info = arrays.pop(name)
        info['array'].flush()
        del info['array']
        info['path'].unlink()

    require(base['piece_coefficients'].shape == (4, 6144, 65),
            'the complete original Qc32 carrier')
    lower = allocate('base_offset_lower', (6144, 65))
    upper = allocate('base_offset_upper', (6144, 65))
    midpoint = allocate('base_offset_midpoint', (6144, 65))
    chain, exact_offsets, count = hashlib.sha256(), {}, 0
    for piece, offset, unused_jump in iterator(base, helper.ALPHA):
        chain.update(canonical({'piece': piece, 'physical_offset': list(map(str, offset))}))
        exact_offsets[piece] = offset
        for k, value in enumerate(offset):
            box = c.arb_box(c.exact(value))
            lower[piece, k], upper[piece, k] = float(box.lo), float(box.hi)
            midpoint[piece, k] = float(value)
        count += 1
        if piece % 256 == 0 or piece == 6143:
            progress('necessary_same_TC_base_offsets', {'pieces': piece+1, 'total': 6144})
    require(count == 6144
            and chain.hexdigest() == original_repair['definition']['offset_sequence_sha256'],
            'the entire original signed base repair chain')
    offsets = {'lower': lower, 'upper': upper, 'midpoint': midpoint}
    definition, proposal_nodes, plan = helper.complete_plan(rows, base['radial_nodes'])
    require(sha(canonical(definition)) == old['definition_sha256']
            and sha(canonical(plan)) == old['certificate_plan_sha256']
            and len(proposal_nodes) == old['complete_trial_nodes'] == 7671
            and len(plan) == old['complete_certificate_cells'] == 7724
            and definition['root_index'] == old['root_index'] == 3021
            and definition['proposal_root_dyadic'] == old['proposal_root_dyadic'],
            'the same whole true-root trial definition and complete exact partition')

    def read_ball(record):
        require(isinstance(record, dict), 'one whole original saved ball')
        if 'lower' in record and 'upper' in record:
            value = flint.arb(record['lower']).lower().union(flint.arb(record['upper']).upper())
        else:
            value = flint.arb(record['ball'])
        require(value.is_finite(), 'one entire finite original input')
        return value

    reference = proposal.FloatingCentreReference(
        np, rows, base, midpoint, helper.ALPHA, read_ball)
    progress('necessary_same_four_TC_trial_arrays', {
        'original_floating_proposal_rematerializations': 1,
        'original_nodal_QR_calls': 0,
        'old_residual_norm_pairing_or_matrix_targets': 0,
        'direction_arrays_needed_by_original_factory': 0})
    proposal.choose_all_columns(np, reference, proposal_nodes, definition['root_index'],
                                allocate, release,
                                lambda stage, detail: progress('necessary_TC_'+stage, detail))
    names = ('trial_value', 'trial_derivative_1', 'trial_derivative_2', 'trial_derivative_3')
    saved, receipts = [], []
    for name, expected in zip(names, old['complete_endpoint_arrays']):
        info = arrays[name]
        info['array'].flush()
        receipt = {'name': name, 'shape': list(info['shape']), 'bytes': info['bytes'],
                   'sha256': file_sha(info['path']),
                   'encoding': 'little-endian binary64 row-major exact dyadics'}
        require(receipt == expected and info['path'].stat().st_size == expected['bytes'],
                'each entire original TC value/derivative array matches its original SHA')
        reopened = np.memmap(info['path'], dtype='<f8', mode='r', shape=info['shape'], order='C')
        saved.append(reopened)
        receipts.append(receipt)
    require(np.array_equal(saved[0][definition['root_index'], 97:, :], np.eye(96)),
            'the same exact root-even96 identity')
    return saved, definition, plan, offsets, exact_offsets, {
        'whole_original_definition_sha256': old['definition_sha256'],
        'whole_original_certificate_plan_sha256': old['certificate_plan_sha256'],
        'complete_original_arrays': receipts,
        'all_four_original_TC_arrays_verified': True,
        'original_base_offset_chain_sha256': chain.hexdigest(),
        'original_TC_floating_proposal_rematerializations': 1,
        'original_nodal_QR_calls': 0,
        'old_completed_scientific_target_calls': 0,
        'new_trial_selected': False,
        'unused_direction_array_materializations': 0,
        'new_arrays_published': 0,
    }

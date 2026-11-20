#!/usr/bin/env python3
"""R675: same-field embedding plus exact nonzero Z-mode Hermite witnesses.

This reads the complete R671 first-geometry report and the very same bundle.
It performs no field evaluation, scalar/oracle query, angular transform,
local optimization or repeated embedding calculation. A finite coefficient
condition plus the already proved embedding rules out planar OPEN patches
in the two active sheets. The allowed flat cap interiors are excluded.

Scientific consumption is restricted to this public repository's Actions.
Missing nonzero witnesses are reported as unpaid, not as planar patches.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np


SCHEMA = 'R675-reference-tail-embedded-activity-nonplanarity-v1'
EMBEDDING_SCHEMA = 'R671-reference-tail-continuous-interval-v1'
EMBEDDING_SOURCE_SHA = 'f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha(value):
    text = json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return hashlib.sha256(text.encode()).hexdigest()


def affine_box(coefficient, constant, box):
    values = [coefficient*x+constant for x in box]
    return min(values), max(values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'bundle', 'embedding-report', 'node-report', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--embedding-source', type=Path)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise SystemExit('R675 scientific consumption belongs in this public repository Actions.')
    if args.out.exists():
        raise FileExistsError('Keep each actual same-field report separately')
    started = time.monotonic()
    paths = {key: getattr(args, key).resolve() for key in ('bundle', 'embedding_report', 'node_report')}
    source = (args.embedding_source or args.repo.resolve()/
        'topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_interval.py').resolve()
    if sha(source) != EMBEDDING_SOURCE_SHA:
        raise ValueError('Use the complete new-field embedding source stated in R675')
    embedding = json.loads(paths['embedding_report'].read_text())
    actual_bundle_sha, actual_node_sha = sha(paths['bundle']), sha(paths['node_report'])
    inputs = embedding.get('source_inputs', {})
    if (embedding.get('schema') != EMBEDDING_SCHEMA or embedding.get('mode') != 'first'
            or embedding.get('source_sha256') != EMBEDDING_SOURCE_SHA
            or inputs.get('bundle', {}).get('sha256') != actual_bundle_sha
            or inputs.get('node_report', {}).get('sha256') != actual_node_sha):
        raise ValueError('The embedding report must describe these exact field and node bytes')
    with np.load(paths['bundle'], allow_pickle=False) as data:
        jets = np.array(data['qjets'], copy=True)
        mesh = np.array(data['mesh'], copy=True)
        if 'reference_tail_model_json' not in data or 'reference_tail_lambda' not in data:
            raise ValueError('The actual canonical R671 model identity is required')
        model = json.loads(str(data['reference_tail_model_json'].item()))
        tags = {key: float(data[key]) for key in ('reference_tail_lambda', 'exact_tail_lambda') if key in data}
    J, n = len(mesh), jets.shape[-1]
    M = (n-2)//3
    if (M < 1 or n != 3*M+2 or jets.shape != (J, 3, n)
            or not np.isrealobj(jets) or not np.isfinite(jets).all()):
        raise ValueError('Need the full finite original three-jet coordinates')
    if (model.get('schema') != 'R671-exact-reference-tail-lift-v1' or model.get('M') != M
            or model.get('node_report_sha256') != actual_node_sha
            or any(value != model.get('lambda_value') for value in tags.values())
            or embedding.get('model_definition') != model
            or embedding.get('model_identity_sha256') != canonical_sha(model)):
        raise ValueError('The actual bundle and proved embedding use different physical models')
    nodes_report = json.loads(paths['node_report'].read_text())
    nodes = [(F(v['S_coefficient']), F(v['constant'])) for v in nodes_report['true_scalar_nodes']]
    S = tuple(F(nodes_report['scalar']['S'][key]) for key in ('lower_exact', 'upper_exact'))
    if (len(nodes) != J or nodes[0] != (F(0), F(0)) or nodes[-1] != (F(1), F(0))
            or nodes_report['S_carrier'] != float(mesh[-1]) or S[0] <= 0 or S[0] > S[1]):
        raise ValueError('The original exact symbolic node interface changed')
    widths = [affine_box(right[0]-left[0], right[1]-left[1], S)
              for left, right in zip(nodes, nodes[1:])]
    if any(width[0] <= 0 for width in widths):
        raise ValueError('Hermite uniqueness needs every exact original cell width to be positive')
    if embedding.get('complete_scope') is not True or [row.get('cell') for row in embedding.get('records', [])] != list(range(J-1)):
        raise ValueError('A partial cell report cannot pay the global embedding hypothesis')
    embedding_paid = embedding.get('embedding_certified') is True
    witnesses, unpaid, smallest = [], [], None
    for cell in range(J-1):
        values = jets[cell:cell+2, :, 2*M+2:]
        index = np.unravel_index(int(np.argmax(np.abs(values))), values.shape)
        value = float(values[index])
        if value == 0.:
            unpaid.append(cell)
            continue
        exact = F(value)
        if exact == 0:
            raise ArithmeticError('A selected exact binary witness vanished')
        smallest = abs(exact) if smallest is None else min(smallest, abs(exact))
        # Compact raw list, with exact binary hex rather than rounded decimal.
        witnesses.append([cell, cell+int(index[0]), int(index[1]), 1+int(index[2]), value.hex()])
    condition_paid = not unpaid
    nonplanar = bool(embedding_paid and condition_paid)
    result = dict(schema=SCHEMA, source_sha256=sha(__file__),
        execution={key: os.environ.get(key) for key in
            ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT', 'GITHUB_WORKFLOW', 'GITHUB_SHA')},
        source_inputs={key: dict(path=str(path), sha256=sha(path)) for key, path in paths.items()},
        embedding_source=dict(path=str(source), sha256=EMBEDDING_SOURCE_SHA),
        model_identity_sha256=canonical_sha(model), reference_tail_lambda=model['lambda_value'],
        J=J, M=M, exact_symbolic_positive_widths_paid=True,
        minimum_cell_width_lower_exact=str(min(width[0] for width in widths)),
        inherited_same_field_global_embedding=embedding_paid,
        all_cells_nonzero_height_mode_condition_paid=condition_paid,
        activity_nonplanarity_certified=nonplanar,
        all_original_cells_nonplanar=nonplanar,
        two_mirrored_active_sheets_included=nonplanar,
        no_planar_open_patch_meeting_activity_interiors=nonplanar,
        known_flat_cap_interiors_excluded=True,
        unpaid_height_mode_cells=unpaid,
        missing_condition_scope='A zero high-Z tuple leaves this sufficient proof unpaid; it does not prove a planar patch',
        selected_witness_count=len(witnesses),
        selected_witness_format=['cell', 'endpoint_node', 's_derivative_order', 'positive_cosine_mode', 'exact_binary_hex'],
        selected_witnesses=witnesses,
        minimum_selected_absolute_value_exact=None if smallest is None else str(smallest),
        coefficient_zero_test='Exact stored finite binary value equals zero; no floating nonzero tolerance',
        axis_trace_reason='Global embedding separates the two opposite points on each axial pair; no scalar-axis oracle is needed',
        proof='Fixed-s angle analyticity extends any plane equation around the circle; opposite axial pairs force nx=ny=0; a nonzero original quintic Z-mode Hermite datum forbids a horizontal plane on any open radial interval',
        radial_analyticity_required=False, scalar_oracle_calls=0, field_evaluations=0,
        repeated_embedding_calculation=False, new_fixtures=0,
        four_fixed_marker_construction_performed=False, Euclidean_shape_amplitude_certified=False,
        reach_certified=False, metric_certified=False,
        prerequisite_for_existing_marker_proof_only=True,
        status='proved' if nonplanar else 'unpaid_hypothesis', seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, separators=(',', ':'), allow_nan=False)+'\n')
    summary = {key: result[key] for key in ('schema', 'status', 'J', 'M',
        'inherited_same_field_global_embedding', 'activity_nonplanarity_certified',
        'selected_witness_count', 'unpaid_height_mode_cells', 'seconds')}
    summary.update(report=str(args.out.resolve()), report_sha256=sha(args.out),
                   bundle_sha256=actual_bundle_sha, model_identity_sha256=canonical_sha(model))
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()

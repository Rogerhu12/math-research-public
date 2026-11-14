#!/usr/bin/env python3
"""Archive one actually completed current-M32 design baseline without its arrays.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original accepted physical quintic and the raw-state cubic comparison
field remain distinct.  This checks saved identities and coverage; it performs
no ODE, Newton iteration, new geometry field or continuous certification.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def rat(value):
    value = Fraction(value)
    return dict(numerator=str(value.numerator), denominator=str(value.denominator))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--audit', type=Path, required=True)
    parser.add_argument('--top', type=Path, required=True)
    parser.add_argument('--tag', required=True)
    args = parser.parse_args()
    plan = read(args.plan)
    if not plan['baseline_only'] or len(plan['candidates']) != 1 or plan['modes'] != 32:
        raise ValueError('Require the unique actual current-M32 baseline plan')
    row = plan['candidates'][0]
    paths = {key: Path(row[key]) for key in ('report', 'field', 'resource')}
    screen, field, owned = (read(paths[key]) for key in ('report', 'field', 'resource'))
    grid_path = Path(plan['grid'])
    grid = read(grid_path)
    if not (owned['exitcode'] == 0 and owned['wait4_observed'] and
            owned['termination_signal'] is None and screen['finished'] and
            screen['finite_domain_passed'] and screen['worker_start_attempts'] == 0 and
            screen['complete_H_change_max'] == 0.0 and
            not screen['nonlinear_solution']):
        raise ValueError('The original completed zero-increment field gates are required')
    for path, expected in plan['source_and_input_sha256'].items():
        if sha(path) != expected:
            raise ValueError('A prepared source or input changed: ' + path)
    for path, expected in screen['source_sha256'].items():
        if sha(path) != expected:
            raise ValueError('An actual field source or input changed: ' + path)
    geometry = screen['geometry_fields']
    if not (sha(paths['field']) == geometry['sha256'] and
            sha(grid_path) == geometry['grid_sha256'] and
            field['shape'] == [len(grid['numerical_t']), 768, 3] and
            geometry['mean_quadrature']['angular'] == 1552 and
            geometry['mean_quadrature']['mean_height_first_second_same_angular_rule']):
        raise ValueError('Full current grid and complete production mean are required')
    accepted_path = Path(screen['actual_reference'])
    accepted, audit = read(accepted_path), read(args.audit)
    if not (accepted['solver_success'] and not accepted['audit_pending'] and
            accepted['modes'] == 32 and audit['input'] == str(accepted_path) and
            audit['input_sha256'] == sha(accepted_path)):
        raise ValueError('The genuinely accepted same-view quintic audit changed')
    if np.asarray(accepted['core']['coefficients'], dtype=np.float64).tobytes() != np.asarray(screen['actual_core'], dtype=np.float64).tobytes():
        raise ValueError('All thirty-two core coefficients must remain unchanged')
    cursor = 0
    complete_bytes = 0
    max_curvature = 0.0
    max_size = 0.0
    chunks = []
    for item in field['chunks']:
        path = paths['field'].parent / item['file']
        data = path.read_bytes()
        if (sha(path) != item['sha256'] or len(data) != item['bytes'] or
                item['start'] != cursor or not cursor < item['end'] <= field['shape'][0]):
            raise ValueError('An actual complete array or its coverage changed')
        value = np.load(io.BytesIO(gzip.decompress(data)), allow_pickle=False)
        if value.dtype != np.float64 or value.shape != (item['end']-cursor, 768, 3) or not np.isfinite(value).all():
            raise ValueError('The actual full finite field changed shape or contains nonfinite values')
        max_curvature = max(max_curvature, float(np.max(abs(value[:, :, :2]))))
        max_size = max(max_size, float(np.max(value[:, :, 2])))
        complete_bytes += len(data)
        chunks.append(dict(path=str(path), **item))
        cursor = item['end']
    if cursor != field['shape'][0] or max_curvature != geometry['kappa_abs_max_sample'] or max_size != geometry['twice_radius_max_sample']:
        raise ValueError('All saved extrema must be actual full-array maxima')
    witness = audit['top']['kappa']
    matching = [item for item in geometry['known_reference_witness_samples']
                if item['actual_s'] == witness['s'] and item['eta'] == witness['psi']]
    if len(matching) != 1:
        raise ValueError('The actual same-view physical witness is absent from the current grid')
    full_gap = 2*sum((Fraction.from_float(float(x)) for x in screen['actual_core'][::2]), Fraction(0))
    receipt = dict(schema='accepted-current-M32-baseline-saved-identity-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        source_sha256=sha(__file__), original_plan_sha256=sha(args.plan),
        accepted_reference=dict(path=str(accepted_path), sha256=sha(accepted_path)),
        actual_same_view_quintic_audit=dict(path=str(args.audit), sha256=sha(args.audit), witness=witness),
        complete_32_core_unchanged=True, zero_H_change=True,
        complete_grid_shape=field['shape'], original_raw_nodes=accepted['nodes'],
        all_chunks_hashed_and_consumed=True, actual_field_chunks=chunks,
        derived_array_bytes=complete_bytes, large_arrays_kept_only_in_scratch=True,
        complete_mean_angular=1552, original_mean_jet_rule_unchanged=True,
        current_witness_present=matching[0],
        raw_cubic_kappa_sample=max_curvature, size_twice_max_norm_sample=max_size,
        raw_cubic_kappa_times_size=max_curvature*max_size,
        original_quintic_kappa_sample=witness['value'],
        original_quintic_kappa_times_raw_cubic_size=witness['value']*max_size,
        full_core_axis_gap_exact_binary=rat(full_gap), full_core_axis_gap_display=float(full_gap),
        full_core_gap_over_size=float(full_gap)/max_size,
        original_physical_metric_l1=audit['top']['metric_fourier_l1']['value'],
        original_physical_darboux_l1=audit['top']['darboux_fourier_l1']['value'],
        exact_reproduction_command=plan['candidates'][0]['command'], cwd=plan['cwd'],
        no_new_ODE_Node_Jacobian_or_accepted_solution=True,
        sampled_cubic_is_not_the_original_physical_quintic=True,
        continuous_curvature_reach_closed_D_and_amplitude_certified=False)
    receipt_path = args.plan.parent/'geometry-baseline-identity-receipt.json'
    if receipt_path.exists():
        raise FileExistsError(receipt_path)
    receipt_path.write_text(json.dumps(receipt, indent=2)+'\n')
    note = f'''# Actual q126 M32: unique current geometry baseline

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Numerical design evidence.** The original q126 M32 production problem has
actually completed all of its existing acceptance gates. Its fixed view is
`{accepted_path.name}`, SHA `{sha(accepted_path)}`. The physical quintic audit
was run directly on that same fixed view; no cross-file witness relabeling is
used. The present zero-increment geometry entry retains all 32 coefficients,
all {accepted['nodes']} original raw nodes, the complete height mean and both
radial mean derivatives at 1552 angles, and the complete 768-angle comparison
grid with {field['shape'][0]} radial values. The same-view quintic witness is
explicitly present in this grid.

The comparison field uses the existing physical-arclength C2 cubic through
the saved raw states. It is a finite design comparison field, distinct from
the original accepted physical quintic. Full-array replay gives its sampled
curvature maximum {max_curvature:.17g} and size proxy
S=2 max|X|={max_size:.17g}; their product is
{max_curvature*max_size:.17g}. The actual physical quintic witness is
{witness['value']:.17g} at s={witness['s']:.17g}, psi={witness['psi']:.17g};
its product with this comparison-field S is
{witness['value']*max_size:.17g}. These remain finite samples. Neither product
is a continuous curvature/diameter certificate.

The full 32-mode axis support gap is the exact binary-rational quantity
2 sum(c[0],c[2],...,c[30]), displayed as {float(full_gap):.17g}. Its ratio to S
is {float(full_gap)/max_size:.17g}. This full-core functional, rather than
twice only the first mode, is the local amplitude design quantity. It is not
the complete closed-surface Hausdorff amplitude. The physical metric Fourier
l1 diagnostic remains {audit['top']['metric_fourier_l1']['value']:.17g},
and the Darboux l1 diagnostic remains
{audit['top']['darboux_fourier_l1']['value']:.17g}; the acceptance protocol
does not discharge the topic's continuous geometric completion requirements.

## Identity, reproduction and storage

The separate receipt rehashes every prepared source and input, reads all
{len(chunks)} saved chunks, checks their exact interval coverage, confirms all
32 saved core bits, and recomputes the reported extrema from every array
entry. The complete source command and owned wait4 resource are retained.
Original geometry execution exited 0 in {owned['wall_seconds']:.9f} seconds,
using {owned['peak_rss_kib']} KiB peak RSS. No tail worker or Jacobian was run
by this geometry entry. Complete H change is exactly zero.

The {complete_bytes} bytes of derived arrays remain in scratch under their
complete saved SHA-256 manifest. They are regenerated by the verbatim command
in the receipt from the archived accepted raw inputs, source pins and grid;
every regenerated chunk can be checked against the saved SHA and shape. The
compact archive stores the grid, plan, full small screen, chunk manifest,
identity receipt and owned resource. It does not duplicate the derived arrays.
This is the sole baseline for the forthcoming current M32 nine-control
response. A later complete plan must reuse it verbatim and compute only its
18 new two-sided direction fields.
'''
    pairs = [(Path(__file__), args.top/'computations'/Path(__file__).name),
             (args.plan, args.top/'notes'/f'{args.tag}-plan.json'),
             (grid_path, args.top/'notes'/f'{args.tag}-grid.json'),
             (paths['report'], args.top/'notes'/f'{args.tag}-screen.json'),
             (paths['field'], args.top/'notes'/f'{args.tag}-field-manifest.json'),
             (paths['resource'], args.top/'notes'/f'{args.tag}-resource.json'),
             (receipt_path, args.top/'notes'/f'{args.tag}-identity-receipt.json')]
    files = []
    for source, dest in pairs:
        data = source.read_bytes()
        if len(data) >= 1_000_000:
            raise ValueError('Keep this compact archive below one megabyte per item')
        if dest.exists():
            if dest.read_bytes() != data:
                raise ValueError('Do not modify a frozen artifact: '+str(dest))
        else:
            dest.write_bytes(data)
        files.append(dict(path=str(dest.relative_to(args.top)), sha256=sha(dest), bytes=len(data), original_path=str(source)))
    note_path = args.top/'notes'/f'{args.tag}-proof.md'
    if note_path.exists():
        raise FileExistsError(note_path)
    note_path.write_text(note)
    files.append(dict(path=str(note_path.relative_to(args.top)), sha256=sha(note_path), bytes=note_path.stat().st_size))
    manifest = args.top/'notes'/f'{args.tag}-manifest.json'
    if manifest.exists():
        raise FileExistsError(manifest)
    manifest.write_text(json.dumps(dict(schema='actual-current-M32-complete-mean-baseline-archive-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', classification='numerical design comparison',
        files=files, total_bytes=sum(item['bytes'] for item in files),
        original_owned_exitcode=0, sole_baseline=True,
        derived_arrays_archived=False, all_derived_array_hashes_preserved=True,
        original_accepted_physical_quintic_and_cubic_scopes_distinct=True), indent=2)+'\n')
    print(json.dumps(dict(manifest=str(manifest), sha256=sha(manifest), files=len(files), total_bytes=sum(item['bytes'] for item in files))), flush=True)


if __name__ == '__main__':
    main()

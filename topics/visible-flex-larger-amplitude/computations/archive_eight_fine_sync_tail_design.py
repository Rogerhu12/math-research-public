#!/usr/bin/env python3
"""Archive the reviewed synchronization-trust actual-eight design batch.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This records the existing numerical outcome and its actual wait4 resource file.
It does not rerun geometry, turn infeasibility into a theorem, or declare a new
fine32 response. Original complete array hashes and regeneration stay in the
referenced seventeen-field bridge.
"""
import argparse
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix', type=Path, required=True)
    p.add_argument('--top', type=Path, required=True)
    p.add_argument('--tag', required=True)
    a = p.parse_args()
    result_path = a.prefix.with_suffix('.json')
    resource_path = a.prefix.with_name(a.prefix.name+'-resource.json')
    bridge_path = a.prefix.with_name(a.prefix.name+'-bridge.json')
    result, owned, bridge = map(read, (result_path, resource_path, bridge_path))
    if not (owned['exitcode'] == 0 and owned['wait4_observed'] and
            owned['termination_signal'] is None and
            bridge['all_identity_and_chunk_gates'] and bridge['total_fields'] == 17):
        raise ValueError('An actual completed, identified numerical batch is required')
    for row in result['predictions']:
        if row['success'] and not (row['all_finite_rows_checked'] and
                row['finite_rows'] == 14_453_760 and
                row['explicit_physical_box_exact_binary_replay']):
            raise ValueError('A successful finite prediction lost its actual full replay')
    comp = Path(__file__).resolve().parent
    preparation = a.prefix.parent/'eight-fine-tail-sync-source-preparation-r1.json'
    producer = comp/'root_fine_core_tail_proxy_eight_sync_trust.py'
    if sha(producer) != read(preparation)['source_sha256']:
        raise ValueError('Prepared producer changed')
    manifest_path = a.top/'notes'/f'{a.tag}-manifest.json'
    if manifest_path.exists():
        raise FileExistsError('Fresh archival identity required')
    pairs = [
        (producer, a.top/'computations'/producer.name),
        (Path(__file__), a.top/'computations'/Path(__file__).name),
        (preparation, a.top/'notes'/f'{a.tag}-source-preparation.json'),
        (result_path, a.top/'notes'/f'{a.tag}-primary.json'),
        (resource_path, a.top/'notes'/f'{a.tag}-resource.json'),
        (bridge_path, a.top/'notes'/f'{a.tag}-bridge.json'),
    ]
    files = []
    for src, dest in pairs:
        data = src.read_bytes()
        if len(data) >= 1_000_000:
            raise ValueError('This small design archive must not grow into derived data')
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            if dest.read_bytes() != data:
                raise ValueError('Never alter an already frozen archival file: '+str(dest))
        else:
            dest.write_bytes(data)
        files.append(dict(path=str(dest.relative_to(a.top)), sha256=sha(dest),
                          bytes=len(data), original_path=str(src)))
    lines = [
        '# Actual eight-control fine-core tail design batch', '',
        'Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.', '',
        '**Heuristic / numerical design evidence.** This batch reuses the completed',
        'M28 q122 baseline and sixteen actual central-difference fields. The tail',
        'proxy is centred on the accepted same-metric M32 core `4c0e13b2…`.',
        'All twenty-eight original directional core entries are retained and the',
        'four extra fine modes keep their actual baseline values with zero increment.',
        'No fine Jacobian, new nonlinear solution, continuous geometry or closed',
        'surface condition is certified here.', '',
        '## Fixed inputs and method', '',
        'The explicit assembled response is `5c83df39…`, selected by the final',
        'plan key, while all original thirteen field commands remain unchanged.',
        'The actual reader verified 17 fields, 306 complete array chunks, the',
        'corrected frontload provider, all 2,587 original raw nodes, 3,764 radial',
        'samples, 768 angles and the full production angular mean of 1,360.',
        'The lambda stencil is ±0.01; the vd stencil is the actually successful',
        '±0.001 pair. The original vd +0.002 rejection remains a separate recorded',
        'outcome. Original six combined-half vectors were not saved; their absence',
        'is preserved and is not replaced by the new two measured external columns.',
        '',
        'The unchanged minimax retains four signed principal-curvature inequalities',
        'and one fixed-origin size inequality at every saved point. Each successful',
        'prediction must replay all 14,453,760 rows. Five complete-core tail budgets',
        'use physical frequencies m ≥ 16, 24, 32, 40, 48 and weights m²−1. Positive',
        'LP auxiliaries encode every absolute value. The saved complete final core',
        'is replayed with exact binary rational arithmetic and the original design',
        'relative tolerance 2e−8; this is not a bound on nonlinear remainders.', '',
        'The normalized original trust box is 256. Explicit physical increments',
        'are Δk0 ∈ [−0.064,0], Δfrontload ∈ [−0.02,0.02] and Δvd ∈ [−0.004,0.001].',
        'The final successful physical steps are compared exactly as binary rationals',
        'to those literal Float64 bounds. Negative frontload remains only an explicitly',
        'requested design range and must pass its own nonlinear physical domain.', '',
        'The smaller positive vd limit is a local design trust condition motivated by',
        'the actually observed synchronization-turn shortening. It is not an added',
        'completion criterion or a necessary condition for the mathematical problem.',
        'The original broad-box LP and its complete nonlinear warm failure remain',
        'separately frozen. No direction field has been recomputed.', '',
        '## Actual outcomes', '',
        '| Δq | Tail multiplier | Size cap / original sampled size | Outcome | Predicted κS |',
        '|---:|---:|---:|---|---:|',
    ]
    factor = result['full_core_tail_proxy_adapter']['explicit_baseline_multiplier']
    for row in result['predictions']:
        dq = row['fixed_q1_factor']*result['directions'][0]['step']
        status = 'all finite rows passed' if row['success'] else 'HiGHS numerical infeasible'
        val = format(row['predicted_kappa_times_twice_norm'], '.12g') if row['success'] else '—'
        lines.append(f"| {dq:.12g} | {factor} | {row['size_factor']:.12g} | {status} | {val} |")
    lines += ['',
        'An infeasible floating LP is recorded as a design attempt, not as a proof',
        'that no physical candidate exists. It does not claim complete replay of a',
        'nonexistent feasible point. Any successful candidate still requires its',
        'actual fine32 full-mean warm field, full core/inlet checks and the original',
        'true-tail/BVP/audit workflow before it can count as an accepted point.', '',
        f"Owned execution: exit 0, {owned['wall_seconds']:.9f} seconds, "
        f"peak {owned['peak_rss_kib']} KiB, single-threaded numerical child.", '',
        '## Reproduction and storage', '',
        'The resource JSON preserves the complete executed command and cwd follows',
        'the immutable field plan. The source preparation records every exact textual',
        'adapter change and proves the parent tail-solver AST is unchanged. The reader',
        'archive supplies all original chunk identities and coverage; its 451,721,535',
        'bytes of regenerable geometry arrays remain in scratch. No ODE, Node worker',
        'or new direction field was run in this batch.', '',
    ]
    note = a.top/'notes'/f'{a.tag}-proof.md'
    if note.exists():
        raise FileExistsError(note)
    note.write_text('\n'.join(lines))
    files.append(dict(path=str(note.relative_to(a.top)), sha256=sha(note), bytes=note.stat().st_size))
    manifest = dict(schema='actual-eight-fine-core-tail-sync-trust-design-batch-archive-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        classification='heuristic / numerical design evidence',
        producer_sha256=sha(producer), archive_source_sha256=sha(__file__),
        files=files, total_bytes=sum(r['bytes'] for r in files),
        prior_seventeen_field_archive='notes/2026-11-13-strong-q122-eight-complete-geometry-reader-r1-manifest.json',
        parent_source_sha256='a4982368cd86d09fc542ec64d4e7dd43c292cd2b6861aeca20b3f1f058176cf6',
        actual_fine_accepted_sha256='4c0e13b2ea4e2541e75891a3b4fafa93ffc2f8331cfdcdc7e4083ac3cbfef1ad',
        original_geometry_array_bytes_not_copied=bridge['total_compressed_derived_array_bytes'],
        original_17_fields_not_recomputed=True,
        true_new_solution_or_fine_Jacobian_claimed=False,
        original_owned_exitcode=owned['exitcode'])
    manifest_path.write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps(dict(manifest=str(manifest_path), sha256=sha(manifest_path),
        files=len(files), total_bytes=manifest['total_bytes'],
        successful=sum(bool(r['success']) for r in result['predictions']))), flush=True)


if __name__ == '__main__':
    main()

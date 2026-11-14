#!/usr/bin/env python3
"""Freeze the actual frontload-range diagnostic without rerunning its warm field.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The equality checked here is equality of saved finite design candidates, not an
interval optimality theorem or a new nonlinear/fine-Jacobian certificate.
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
    p.add_argument('--previous', type=Path, required=True)
    p.add_argument('--previous-index', type=int, default=1)
    p.add_argument('--top', type=Path, required=True)
    p.add_argument('--tag', required=True)
    a = p.parse_args()
    primary = a.prefix.with_suffix('.json')
    resource = a.prefix.with_name(a.prefix.name+'-resource.json')
    bridge = a.prefix.with_name(a.prefix.name+'-bridge.json')
    prep = a.prefix.parent/'eight-fine-tail-sync-frontload04-source-preparation-r1.json'
    producer = Path(__file__).with_name('root_fine_core_tail_proxy_eight_sync_frontload04.py')
    result, owned, old, bridged, preparation = map(read, (primary, resource, a.previous, bridge, prep))
    if not (owned['exitcode'] == 0 and owned['wait4_observed'] and
            owned['termination_signal'] is None and len(result['predictions']) == 1 and
            bridged['all_identity_and_chunk_gates'] and bridged['total_fields'] == 17):
        raise ValueError('A complete owned identified diagnostic is required')
    if sha(producer) != preparation['source_sha256']:
        raise ValueError('Prepared producer changed')
    if preparation['only_physical_range_change'] != {
            'initial_speed_frontload': {'old': [-.02,.02], 'new': [-.04,.04]}}:
        raise ValueError('This archive is restricted to the stated single range change')
    current, previous = result['predictions'][0], old['predictions'][a.previous_index]
    keys = ('normalized_steps', 'physical_steps', 'predicted_profile_increment',
            'predicted_complete_core_increment', 'predicted_complete_core_for_tail_proxy',
            'predicted_max_abs_curvature', 'predicted_max_twice_norm',
            'predicted_kappa_times_twice_norm', 'extrema_witnesses')
    equal = {key: current[key] == previous[key] for key in keys}
    if not all(equal.values()):
        raise ValueError('The expanded box produced a different saved candidate')
    if not (current['success'] and current['all_finite_rows_checked'] and
            current['finite_rows'] == 14_453_760 and
            current['explicit_physical_box_exact_binary_replay'] and
            result['physical_control_ranges']['initial_speed_frontload'] == [-.04,.04]):
        raise ValueError('The complete finite replay or new box was lost')
    old_warm_manifest = a.top/'notes/2026-11-13-strong-eight-sync-fine-q130-size1035-warm-r1-manifest.json'
    if sha(old_warm_manifest) != 'c39bdd33a87166422b75992b348894defc58a794c2623c1b64eb327b5cdadadb':
        raise ValueError('The already completed actual warm archive changed')
    comparison = dict(schema='actual-finite-design-expanded-box-equality-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        current=dict(path=str(primary),sha256=sha(primary),prediction_index=0),
        previous=dict(path=str(a.previous),sha256=sha(a.previous),prediction_index=a.previous_index),
        exact_saved_candidate_equalities=equal, all_saved_candidate_equalities=True,
        actual_warm_manifest=dict(path=str(old_warm_manifest),sha256=sha(old_warm_manifest)),
        frontload_step=current['physical_steps']['initial_speed_frontload'],
        frontload_strictly_inside_both_boxes=(-.02 < current['physical_steps']['initial_speed_frontload'] < .02),
        predicted_kappa_size=current['predicted_kappa_times_twice_norm'],
        previous_actual_warm_kappa_size=33.52518911003503,
        new_warm_not_run_because_all_candidate_controls_and_full_core_are_equal=True,
        numerical_optimality_is_not_an_exact_impossibility_proof=True,
        original_coarse_geometry_and_fine_core_scopes_preserved=True)
    comparison_path = a.prefix.with_name(a.prefix.name+'-candidate-equality.json')
    if comparison_path.exists():
        raise FileExistsError(comparison_path)
    comparison_path.write_text(json.dumps(comparison,indent=2)+'\n')
    proof = '''# Expanded frontload range: unchanged finite design candidate

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Heuristic / numerical design conclusion.** The actual floating LP with
frontload increment in [-0.04,0.04] returns exactly the saved candidate from
the earlier [-0.02,0.02] run at q increment 0.008, size cap 1.035 and full-core
tail multiplier 4. All eight saved controls, complete core increments, profile
increments, three extrema and reported geometry are equal as saved Float64
values. Lambda is -0.0015957928829956744, strictly inside both ranges. This run
does not support the earlier suggestion that the positive lambda bound was
the principal restriction in this particular scenario.

The actual reader retained the same seventeen fields and all 306 complete
chunks. All 14,453,760 curvature/size rows were replayed. The fine M32 core
remained the accepted q122 core, with the coarse twenty-eight directional
entries padded by four zero increments, and all five original weighted tail
budgets were replayed. The original trust 256, k0 interval [-0.064,0] and
vd interval [-0.004,0.001] were unchanged. The producer preparation preserves
the original tail-solver AST. This is an old-point design model, not a current
or fine Jacobian, a nonlinear domain certificate, or a new accepted solution.

The predicted kappa-times-size is 33.53431528137435. The identical candidate
already has a complete actual M32 warm evaluation: 33.52518911003503, above
100/3. Its original floating-grid orientation rejection and the subsequent
explicit exact-chart-order bridge remain in their original archive. The
present diagnostic does not alter those outcomes and does not rerun the
identical warm field. The exact equality comparison does not establish exact
LP optimality or impossibility of another physical construction.

The stored model has active positive vd and zero k0 bounds and weighted tail
budgets at frequencies 32 and 48, within its original floating replay
tolerances. These observations explain the returned finite candidate only;
they are not a complete dual certificate or a proof of a mathematical
obstruction. The next local model will use the genuinely accepted new M32
point and add the existing physical descending_sync_curvature control.

## Reproduction and storage

The resource file contains the exact executed command, ownership and wait4
result. Run from the original geometry-work directory with single-threaded
BLAS/OMP/MKL settings. All actual field manifests and regenerable arrays stay
under their previous identities; no new ODE, Node worker, direction field or
large data copy was used. The compact archive includes the real result and
the source preparation, not just the displayed scalar summary.
'''
    proof += f"\nOwned execution: exit 0; {owned['wall_seconds']:.9f} seconds; peak {owned['peak_rss_kib']} KiB.\n"
    pairs = [(producer,a.top/'computations'/producer.name),
             (Path(__file__),a.top/'computations'/Path(__file__).name),
             (prep,a.top/'notes'/f'{a.tag}-source-preparation.json'),
             (primary,a.top/'notes'/f'{a.tag}-primary.json'),
             (resource,a.top/'notes'/f'{a.tag}-resource.json'),
             (bridge,a.top/'notes'/f'{a.tag}-bridge.json'),
             (comparison_path,a.top/'notes'/f'{a.tag}-candidate-equality.json')]
    files=[]
    for src,dest in pairs:
        data=src.read_bytes()
        if len(data)>=1_000_000:
            raise ValueError('The compact archive must not copy large derived arrays')
        if dest.exists():
            if dest.read_bytes()!=data:raise ValueError('Never change frozen archive '+str(dest))
        else:dest.write_bytes(data)
        files.append(dict(path=str(dest.relative_to(a.top)),sha256=sha(dest),bytes=len(data),original_path=str(src)))
    note=a.top/'notes'/f'{a.tag}-proof.md'
    if note.exists():raise FileExistsError(note)
    note.write_text(proof)
    files.append(dict(path=str(note.relative_to(a.top)),sha256=sha(note),bytes=note.stat().st_size))
    manifest=a.top/'notes'/f'{a.tag}-manifest.json'
    if manifest.exists():raise FileExistsError(manifest)
    manifest.write_text(json.dumps(dict(schema='actual-expanded-frontload-design-diagnostic-archive-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',classification='heuristic / numerical design evidence',
        producer_sha256=sha(producer),archive_source_sha256=sha(__file__),files=files,
        total_bytes=sum(r['bytes'] for r in files),saved_candidate_unchanged=True,
        actual_warm_recomputed=False,new_BVP_or_fine_Jacobian=False,
        previous_seventeen_field_manifest='notes/2026-11-13-strong-q122-eight-complete-geometry-reader-r1-manifest.json'),indent=2)+'\n')
    print(json.dumps(dict(manifest=str(manifest),sha256=sha(manifest),files=len(files),
                         total_bytes=sum(r['bytes'] for r in files))),flush=True)


if __name__=='__main__':
    main()

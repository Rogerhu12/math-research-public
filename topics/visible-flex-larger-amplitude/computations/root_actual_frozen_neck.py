#!/usr/bin/env python3
"""Fixed-metric actual coupling with the verified frozen binary geometry.

This opt-in entry reuses the original resumable protocol and its acceptance
gates. The original entry files remain unchanged. Explicit in-memory source
substitutions select the frozen client and report the effective independent
radial batch size. Full boundary vectors and all solved core coefficients
are retained. The result is still a finite original-g problem. By default
the reference is an accepted actual nonlinear-tail solution. An explicit
--allow-converged-design-reference instead anchors only the metric of a
converged finite design: this starts its first actual nonlinear-tail solve
and is never described as refinement of a previous actual joined solution.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import types
import root_actual_bounded_neck as bounded
import root_radial_batching as radial

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix == '.gz'
                      else path.read_bytes())


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--frozen-reference-ready', type=Path, required=True)
    parser.add_argument('--frozen-calibration-ledger', type=Path, required=True)
    parser.add_argument('--point-cache-limit', type=int, default=8)
    parser.add_argument('--radial-batch-size', type=int, default=16)
    parser.add_argument('--collocation-batch-size', type=int, default=12)
    parser.add_argument('--allow-converged-design-reference', action='store_true')
    parser.add_argument('--extra-physical-mesh', type=Path)
    parser.add_argument('--prepare-only', action='store_true')
    options, remaining = parser.parse_known_args()
    if '--fixed-reference' not in remaining:
        raise ValueError('This entry is exclusively a fixed-metric refinement')
    if '--client' not in remaining:
        remaining += ['--client', 'stored-resumable']
    elif remaining[remaining.index('--client')+1] != 'stored-resumable':
        raise ValueError('The original resumable protocol is required')

    def argument(name):
        if name not in remaining:
            raise ValueError('Missing required argument '+name)
        return Path(remaining[remaining.index(name)+1])

    if not (1 <= options.point_cache_limit <= 96 and
            1 <= options.radial_batch_size <= 48 and
            1 <= options.collocation_batch_size <= 24):
        raise ValueError('Requested cache or independent batch size is invalid')
    out = argument('--out-prefix')
    record_file = out.with_name(out.name+'-frozen-adapter.json')
    reference = read(argument('--fixed-reference'))
    config = read(argument('--tail-config'))
    if not reference.get('solver_success'):
        raise ValueError('The metric anchor must be a converged saved finite problem')
    reference_is_actual = bool(reference['config'].get('actual_nonlinear_tail'))
    if not reference_is_actual and not options.allow_converged_design_reference:
        raise ValueError('A non-actual design anchor requires the explicit opt-in')
    reference_kind = ('accepted-actual-nonlinear-tail-solution' if reference_is_actual
                      else 'converged-design-metric-anchor-first-actual-solve')
    if not reference_is_actual:
        core = reference['core']
        modes = int(reference['modes'])
        if (len(core['coefficients']) != modes or
                core['frequencies'] != list(range(2, 2*modes+1, 2)) or
                core['coefficients'][0] != reference['actual_primary_amplitude']):
            raise ValueError('The complete actual core and its physical amplitude must be explicit')
        if reference['gauge_amplitude'] <= 0:
            raise ValueError('The representation gauge must remain a separate positive datum')
    for key, value in reference['physical_tail_parameters'].items():
        if config.get(key) != value:
            raise ValueError('Physical tail parameter differs: '+key)
    if config['modes'] != int(str(argument('--modes'))) or config['spacing'] != 2:
        raise ValueError('The complete prefix and tail spectra must agree')
    mesh_record = None
    extra_physical_s = []
    if options.extra_physical_mesh:
        mesh = read(options.extra_physical_mesh)
        restart_file = argument('--restart') if '--restart' in remaining else argument('--fixed-reference')
        donor = mesh['physical_checkpoint']
        if sha(restart_file) != mesh['source_sha256'][donor]:
            raise ValueError('The physical mesh donor differs from the restart state')
        if mesh['target_solver_tolerance'] != float(str(argument('--tol'))):
            raise ValueError('The mesh plan was prepared for a different target tolerance')
        if mesh['total_planned_physical_nodes'] > int(str(argument('--max-nodes'))):
            raise ValueError('The requested warm mesh exceeds the original node budget')
        for name, expected in mesh['source_sha256'].items():
            path = Path(name)
            if not path.is_file() and path.is_absolute():
                path = HERE/path.name
            if not path.is_file() or sha(path) != expected:
                raise ValueError('A physical mesh input or source hash differs: '+name)
        extra_physical_s = list(map(float, mesh['extra_physical_s']))
        if (len(extra_physical_s) != mesh['extra_nodes'] or
                extra_physical_s != sorted(set(extra_physical_s)) or
                not all(math.isfinite(x) and 0 < x < reference['meridian_length']
                        for x in extra_physical_s) or
                not mesh['all_old_physical_nodes_preserved_bitwise']):
            raise ValueError('Invalid additional physical restart nodes')
        mesh_record = dict(file=str(options.extra_physical_mesh),
            sha256=sha(options.extra_physical_mesh), donor_sha256=sha(restart_file),
            requested_extra_nodes=len(extra_physical_s),
            planned_total_physical_nodes=mesh['total_planned_physical_nodes'],
            selection_threshold=mesh['selection_threshold'],
            original_physical_nodes_requested_before_merge=True,
            original_normalized_chart_not_reused=True,
            new_fields_evaluated_by_original_complete_pullback=True)
    for path in (options.frozen_reference_ready, options.frozen_calibration_ledger):
        if not path.is_file():
            raise FileNotFoundError(path)
    for key, value in {
        'VISIBLE_FLEX_FROZEN_STORED_READY': options.frozen_reference_ready.resolve(),
        'VISIBLE_FLEX_FROZEN_LEDGER_READY': options.frozen_calibration_ledger.resolve(),
        'VISIBLE_FLEX_SOURCE_TOPIC': argument('--source-topic').resolve(),
        'VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT': options.point_cache_limit,
    }.items():
        os.environ[key] = str(value)

    defaults = (radial.value.__defaults__, radial.state_jacobian.__defaults__,
                bounded.blocks.prepare_sys.__defaults__)
    if defaults != ((48,), (48,), (24,)):
        raise ValueError('Reviewed independent batch defaults changed')
    radial.value.__defaults__ = (options.radial_batch_size,)
    radial.state_jacobian.__defaults__ = (options.radial_batch_size,)
    bounded.blocks.prepare_sys.__defaults__ = (options.collocation_batch_size,)

    substitutions = {
        'root_actual_neck_bvp.py': [(
            "'stored-resumable':HERE/'tail_resumable_client.py',",
            "'stored-resumable':HERE/'tail_frozen_client.py',")],
        'root_actual_fixed_refinement.py': [(
            'radial_batch_size=48,',
            'radial_batch_size='+str(options.radial_batch_size)+',')],
    }
    if not reference_is_actual:
        substitutions['root_actual_fixed_refinement.py'].append((
            "if not reference['config'].get('actual_nonlinear_tail',False):",
            "if not reference['config'].get('actual_nonlinear_tail',False) and not EXPLICIT_CONVERGED_DESIGN_REFERENCE:"))
    if extra_physical_s:
        substitutions['geometric-fixed-dual-prefix.py'] = [(
            'grid=self.inverse_chart(np.asarray(saved.sol.x),0.)',
            'grid=np.r_[self.inverse_chart(np.asarray(saved.sol.x),0.),self.inverse_chart(np.asarray(EXTRA_PHYSICAL_MESH),0.)]'), (
            'record.update(boundary_correction_max=',
            "record.update(physical_mesh_extension=dict(plan=EXTRA_PHYSICAL_MESH_RECORD,actual_merged_nodes=len(t)),boundary_correction_max=")]
    transformed = {}
    for name, changes in substitutions.items():
        original = (HERE/name).read_text()
        source = original
        for before, after in changes:
            if source.count(before) != 1:
                raise ValueError('Frozen entry source anchor differs: '+name)
            source = source.replace(before, after)
        transformed[name] = dict(original_sha256=sha(HERE/name),
            compiled_sha256=hashlib.sha256(source.encode()).hexdigest(),
            replacements=[dict(old=before, new=after, count=1) for before, after in changes])

    sources = ['root_actual_frozen_neck.py', 'root_actual_bounded_neck.py',
        'root_actual_neck_bvp.py', 'root_actual_fixed_refinement.py',
        'root_radial_batching.py', 'root_block_collocation.py',
        'tail_frozen_client.py', 'tail_frozen_worker.mjs',
        'tail_frozen_geometry.mjs', 'strong_frozen_calibration_factory.mjs']
    if extra_physical_s:
        sources += ['geometric-fixed-dual-prefix.py', 'strong_physical_rms_mesh.py']
    provenance = dict(scope=__doc__, status='prepared',
        source_sha256={name:sha(HERE/name) for name in sources},
        frozen_reference_ready=dict(file=str(options.frozen_reference_ready),
            sha256=sha(options.frozen_reference_ready)),
        frozen_calibration_ledger=dict(file=str(options.frozen_calibration_ledger),
            sha256=sha(options.frozen_calibration_ledger)),
        substitutions=transformed, point_cache_limit=options.point_cache_limit,
        reference_kind=reference_kind, reference_was_actual_nonlinear_tail=reference_is_actual,
        explicit_design_anchor_opt_in=options.allow_converged_design_reference,
        physical_mesh_extension=mesh_record,
        baseline_physical_metric_l1_sample=reference.get('summary', {}).get('metric_l1'),
        fixed_gauge_amplitude=reference['gauge_amplitude'],
        baseline_actual_core_coefficients=reference['core']['coefficients'],
        baseline_is_not_an_actual_refinement_checkpoint=not reference_is_actual,
        radial_batch_size=options.radial_batch_size,
        collocation_interval_batch_size=options.collocation_batch_size,
        physical_data_unchanged=True, original_acceptance_gates_unchanged=True,
        full_boundary_vector_retained=True, command_arguments=remaining,
        protocol_kind='stored-resumable', actual_client='tail_frozen_client.py')
    if record_file.exists():
        old = read(record_file)
        if old != provenance:
            raise FileExistsError('Output prefix already has a different adapter record')
    else:
        record_file.parent.mkdir(parents=True, exist_ok=True)
        record_file.write_text(json.dumps(provenance, indent=2)+'\n')
    if options.prepare_only:
        print(json.dumps(dict(event='frozen_actual_refinement_prepared',
            record=str(record_file), sha256=sha(record_file))), flush=True)
        return

    loader = bounded.adapter.module
    def load(name, path):
        path = Path(path)
        if path.name not in substitutions:
            return loader(name, path)
        original = path.read_text()
        if sha(path) != transformed[path.name]['original_sha256']:
            raise ValueError('Source changed after the prepared provenance')
        module = types.ModuleType(name)
        module.__file__ = str(path)
        module.EXPLICIT_CONVERGED_DESIGN_REFERENCE = options.allow_converged_design_reference
        module.EXTRA_PHYSICAL_MESH = extra_physical_s
        module.EXTRA_PHYSICAL_MESH_RECORD = mesh_record
        sys.modules[name] = module
        source = original
        for before, after in substitutions[path.name]:
            source = source.replace(before, after)
        exec(compile(source, str(path), 'exec'), module.__dict__)
        bounded.adapter.TRANSFORMS[path.name] = transformed[path.name]
        return module

    bounded.adapter.module = load
    sys.argv = [sys.argv[0]]+remaining
    try:
        bounded.main()
    finally:
        provenance['status'] = 'entry_returned_or_raised; inspect solver and resource records'
        record_file.write_text(json.dumps(provenance, indent=2)+'\n')
        for path in (out.with_suffix('.json.gz'), out.with_name(out.name+'-summary.json')):
            if not path.is_file():
                continue
            data = read(path)
            data['frozen_actual_coupling'] = provenance
            raw = (json.dumps(data, indent=2)+'\n').encode()
            path.write_bytes(gzip.compress(raw, mtime=0) if path.suffix == '.gz' else raw)


if __name__ == '__main__':
    main()

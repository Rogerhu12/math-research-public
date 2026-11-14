#!/usr/bin/env python3
"""Same physical metric M32 -> M40 refinement with explicit initial-law hooks.

Author: strong_recovery (GPT-6 Astra Pro, AI assisted), 2026-11-13.
The genuine accepted fixed view, complete raw field, actual audited tail,
profile, all physical pieces, material chart and numerical chart are required.
Only unknown-function modes 32 -> 40 and angular integration 1280 -> 1536
change. All 97 old prefix channels and all 64 old tail Q/pi channels are
embedded exactly; eight new modes start at zero and are explicitly unsolved.
The same original full-H nonlinear solve, complete Jacobian, RMS, physical BC
and final audit gates remain. No old-mode full-flow snapshot is transferred.

Nonzero frontload uses the previously identified anchor-corrected provider in
both the real production constructor and the independent saved-field loader.
The source-only and live-prefix preflight paths start no Node, ODE or Newton.
All frozen Python and MJS sources remain unchanged.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import ast
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE_NAME = 'strong_sameg_m32_fullflow_refinement_v2.py'
BASE_SHA = '202471724125bb567d622be513d2dc3ffd664d7070f8e93502a0e5537dbbe57c'
HOOKS = {
    'strong_initial_speed_pulse.py': 'f1d8c0867d598313da760fcd4910cd20c5f387afd7c6bd90a31b257848acbf73',
    'strong_monotone_initial_speed.py': '12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
    'strong_monotone_initial_speed_anchor.py': '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
}
LIVE_REFERENCE = None
OBSERVATIONS = {'production_provider_loads': 0, 'saved_provider_loads': 0}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def base_module():
    for name, wanted in {BASE_NAME: BASE_SHA, **HOOKS}.items():
        if sha(HERE/name) != wanted:
            raise ValueError('Frozen same-g entry or initial-law source changed: '+name)
    return module('sameg_m40_retained_m32_entry', HERE/BASE_NAME)


def install_provider(value, kind):
    import strong_initial_speed_pulse as pulse
    import strong_monotone_initial_speed_anchor as frontload
    pulse.install(value)
    frontload.install(value)
    OBSERVATIONS[kind+'_provider_loads'] += 1
    return value


def wrap_provider_loader(value, kind):
    if getattr(value, '_m40_initial_law_loader_installed', False):
        return value
    original = value.module
    def load(name, path):
        loaded = original(name, path)
        if Path(path).name == 'alternative-neck-provider.py':
            return install_provider(loaded, kind)
        if Path(path).name in ('root_dual_core_bvp.py', 'geometric-checkpoint-core-pullback.py'):
            return wrap_provider_loader(loaded, kind)
        return loaded
    value.module = load
    value._m40_initial_law_loader_installed = True
    return value


def wrap_production_loaded(value, path):
    if Path(path).name in ('root_dual_core_bvp.py', 'geometric-checkpoint-core-pullback.py'):
        return wrap_provider_loader(value, 'production')
    if Path(path).name == 'alternative-neck-provider.py':
        return install_provider(value, 'production')
    return value


def initial_law_input_gate(saved, report):
    profile = saved['frozen_profile']
    for key in ('initial_speed_pulse', 'initial_speed_frontload'):
        value = float(profile.get(key, 0.))
        if not __import__('math').isfinite(value):
            raise ValueError('A physical initial-law parameter is not finite')
    weight = float(profile.get('initial_speed_frontload', 0.))
    if weight and float(profile.get('initial_speed_pulse', 0.)):
        raise ValueError('The original pulse/frontload mutual-exclusion gate remains')
    if weight:
        # The genuine fixed-view converter must actually have used this hook;
        # mere presence of a nonzero JSON profile key does not establish g.
        packed = json.dumps(report, sort_keys=True, allow_nan=False)
        if HOOKS['strong_monotone_initial_speed_anchor.py'] not in packed:
            raise ValueError('Nonzero fixed view lacks its actual anchor-provider identity')


def check_installed_initial_law(flow, profile):
    neck = flow._alternative_neck
    if neck.cfg != profile or flow.cfg != profile:
        raise ValueError('A complete physical initial-law profile changed')
    weight = float(profile.get('initial_speed_frontload', 0.))
    if weight:
        first = neck.segments[0]
        if (first.get('strong_initial_speed_frontload') != weight or
                first.get('strong_initial_speed_frontload_degree') != profile.get('initial_speed_frontload_degree', 22) or
                not first.get('strong_initial_speed_frontload_nonnegative_derivative_hull')):
            raise ValueError('The actual nonzero first piece was not installed')


def dimension_function(base, name):
    """Change only explicit old/new spectrum constants in one frozen function."""
    source = (HERE/BASE_NAME).read_text()
    tree = ast.parse(source)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    original = ast.get_source_segment(source, node)
    parsed = ast.parse(original)
    replacements = []
    class Dimensions(ast.NodeTransformer):
        def visit_Constant(self, old):
            if type(old.value) is int and old.value in {28, 32, 56, 64}:
                new = {28: 32, 32: 40, 56: 64, 64: 80}[old.value]
                replacements.append(dict(line=old.lineno, old=old.value, new=new))
                return ast.copy_location(ast.Constant(new), old)
            if isinstance(old.value, str):
                text = old.value.replace('28-to-32', '32-to-40').replace('M32', 'M40').replace('q122 accepted', 'actual accepted')
                if text != old.value:
                    replacements.append(dict(line=old.lineno, old=old.value, new=text, diagnostic_only=True))
                    return ast.copy_location(ast.Constant(text), old)
            return old
    changed = ast.fix_missing_locations(Dimensions().visit(parsed))
    result = ast.unparse(changed)+'\n'
    namespace = dict(base.__dict__)
    namespace.update(LIVE_REFERENCE=LIVE_REFERENCE)
    exec(compile(result, '<sameg-M40-'+name+'>', 'exec'), namespace)
    return namespace[name], dict(function=name,
        original_function_sha256=hashlib.sha256(original.encode()).hexdigest(),
        transformed_function_sha256=hashlib.sha256(result.encode()).hexdigest(),
        replacements=replacements, only_explicit_dimensions_and_diagnostic_strings_changed=True)


def live_metric_identity(obj, saved, args, out, diagnostic):
    import numpy as np
    base = BASE
    flow = obj.flow()
    pb = module('sameg_m40_saved_physical_pullback', HERE/'geometric-checkpoint-core-pullback.py')
    wrap_provider_loader(pb, 'saved')
    old, unused = pb.load_saved(LIVE_REFERENCE, Path(args.source_topic), Path(args.port),
                                angular=int(saved['config']['angular']))
    check_installed_initial_law(old.flow, saved['frozen_profile'])
    check_installed_initial_law(flow, saved['frozen_profile'])
    before = dict(prefix=base.plain(old.flow._alternative_neck.segments), bridge=base.plain(old.flow.bridge.segments))
    after = dict(prefix=base.plain(flow._alternative_neck.segments), bridge=base.plain(flow.bridge.segments))
    if base.canonical(before) != base.canonical(after):
        raise ValueError('A physical initial-law/angle segment or phase changed')
    grid = np.unique(np.r_[flow.breaks,
        (flow.breaks[:-1, None]+np.diff(flow.breaks)[:, None]*np.array([.125, .375, .625, .875])).ravel()])
    for actual, original in zip(flow.profile(grid), old.flow.profile(grid)):
        if np.asarray(actual, dtype=np.float64).tobytes() != np.asarray(original, dtype=np.float64).tobytes():
            raise ValueError('Original metric a/as/ass callback changed')
    if (flow.cfg != old.flow.cfg or flow.end != old.flow.end or
            flow.general_core_chart.coefficients.tobytes() != old.flow.general_core_chart.coefficients.tobytes() or
            flow.general_core_chart.frequencies.tobytes() != old.flow.general_core_chart.frequencies.tobytes()):
        raise ValueError('Original profile, length, or material coordinate changed')
    record = dict(scope='Real M40 prefix constructor versus the genuinely accepted M32 metric, before any worker or Newton.',
        original_reference=str(LIVE_REFERENCE), original_reference_sha256=sha(LIVE_REFERENCE),
        complete_profile_identical=True, all_prefix_and_bridge_segments_identical=True,
        all_segment_phase_and_coefficients_identical=True, a_as_ass_callback_samples_bitwise_equal=True,
        sampled_s=grid.tolist(), complete_segment_structure_sha256=hashlib.sha256(base.canonical(before)).hexdigest(),
        physical_segments=before, original_material_chart_identical=True,
        original_numerical_reference_identical=True, original_physical_length_identical=True,
        old_modes=32, new_modes=40, old_angular=1280, new_angular=1536,
        tail_quadrature_unchanged=512, tail_worker_started=False, bvp_solved=False,
        initial_law_providers=HOOKS, initial_law_load_observations=dict(OBSERVATIONS),
        full_core_warm_embedding_in_original_raw_report=True,
        later_live_tail_still_requires_original_frozen_profile_fingerprint_gates=True)
    diagnostic['live_physical_metric_identity'] = base.write_same(out.with_name(out.name+'-live-physical-identity.json'), record)


def build(base):
    source, prior = base.build()
    original = source
    replacements = []
    def edit(before, after):
        nonlocal source
        if source.count(before) != 1:
            raise ValueError('M40 initial-law specialization anchor is not unique: '+repr(before))
        source = source.replace(before, after, 1)
        replacements.append(dict(before=before, after=after, count=1))
    edit('if (Mnew,Nnew)!=(32,1280) or old_heap<=0:', 'if (Mnew,Nnew)!=(40,1536) or old_heap<=0:')
    edit("report.get('original_parameter_count')!=31 or report.get('fixed_parameter_count')!=28", "report.get('original_parameter_count')!=35 or report.get('fixed_parameter_count')!=32")
    edit("if M!=28 or saved['modes']!=M or not ident['fixed'] or target_tol!=ident['tol']:", "if M!=32 or saved['modes']!=M or not ident['fixed'] or target_tol!=ident['tol']:")
    edit("if cfg0['modes']!=28 or cfg0['spacing']!=2 or cfg0['quadrature']!=512:", "if cfg0['modes']!=32 or cfg0['spacing']!=2 or cfg0['quadrature']!=512:")
    edit("    for key in ('initial_speed_pulse','initial_speed_frontload'):\n        if saved['frozen_profile'].get(key,0)!=0:\n            raise ValueError('Nonzero new initial laws require their explicit provider entry')",
         "    SPECTRAL_INITIAL_LAW_INPUT_GATE(saved,report)")
    edit('        loaded=old_loader(name,path)\n', '        loaded=SPECTRAL_INITIAL_LAW_LOADER(old_loader(name,path),path)\n')
    for before, after in [
        ('explicitly M32/N1280', 'explicitly M40/N1536'), ('real 31-to-28', 'real 35-to-32'),
        ('original fixed M28', 'original fixed M32'), ('original 28 core modes', 'original 32 core modes'),
        ('genuine M32 Fixed/Actual', 'genuine M40 Fixed/Actual'), ('input M28 manifest', 'input M32 manifest'),
        ('same_g_M32_source_and_data_prepared', 'same_g_M40_source_and_data_prepared'),
        ('same_g_M32_actual_refinement_complete', 'same_g_M40_actual_refinement_complete')]:
        edit(before, after)
    doc = ast.parse(source).body[0]
    edit(ast.get_source_segment(source, doc), repr(__doc__))
    reverse = source
    for row in reversed(replacements):
        if reverse.count(row['after']) != 1:
            raise ValueError('M40 reverse source anchor differs')
        reverse = reverse.replace(row['after'], row['before'], 1)
    if reverse != original:
        raise ValueError('Unlisted M40 source alteration')
    ast.parse(source)
    return source, dict(scope=__doc__, original_M32_transform=prior,
        source_sha256={BASE_NAME: BASE_SHA, **HOOKS, Path(__file__).name: sha(__file__)},
        prior_transformed_source_sha256=hashlib.sha256(original.encode()).hexdigest(),
        transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        replacements=replacements, exact_reverse_recovers_original_M32_transform=True,
        fixed_profile_and_initial_law_unchanged=True, original_complete_actual_acceptance_gates_unchanged=True,
        all_frozen_sources_and_MJS_unchanged=True)


def main():
    global LIVE_REFERENCE, BASE
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--spectral-stage-cache-directory', type=Path)
    parser.add_argument('--spectral-live-preflight-only', action='store_true')
    parser.add_argument('--spectral-source-record', type=Path)
    own, remaining = parser.parse_known_args()
    BASE = base_module()
    source, transform = build(BASE)
    if own.spectral_source_record:
        BASE.write_same(own.spectral_source_record, dict(transform=transform,
            source_preparation_only=True, actual_field_or_future_fine_input_created=False,
            Node_ODE_Newton_or_Jacobian_started=False))
        print(json.dumps(dict(event='M40_initial_law_source_prepared', record=str(own.spectral_source_record))), flush=True)
        return
    if own.spectral_stage_cache_directory is None:
        raise ValueError('An explicit task-owned exact stage cache is required')
    for key in ('--fixed-reference', '--out-prefix'):
        if remaining.count(key) != 1:
            raise ValueError('Require explicit '+key)
    LIVE_REFERENCE = Path(remaining[remaining.index('--fixed-reference')+1])
    out = Path(remaining[remaining.index('--out-prefix')+1])
    tail_builder, tail_record = dimension_function(BASE, 'spectral_tail_warm')
    ready_checker, ready_record = dimension_function(BASE, 'live_tail_metric_identity')
    transform.update(dimension_function_transforms=[tail_record, ready_record],
        stage_cache_directory=str(own.spectral_stage_cache_directory.resolve()),
        live_prefix_preflight_only=own.spectral_live_preflight_only)
    BASE.write_same(out.with_name(out.name+'-m40-initial-law-source-transform.json'), transform)
    namespace = dict(__file__=str(Path(__file__).resolve()), __name__='strong_original_spectral_M40_initial_laws',
        SPECTRAL_TAIL_BUILDER=tail_builder, SPECTRAL_LIVE_IDENTITY=live_metric_identity,
        SPECTRAL_LIVE_PREFLIGHT=own.spectral_live_preflight_only, SPECTRAL_PREFLIGHT_FINISHED=BASE.PreflightFinished,
        SPECTRAL_INITIAL_LAW_INPUT_GATE=initial_law_input_gate,
        SPECTRAL_INITIAL_LAW_LOADER=wrap_production_loaded,
        M32_EXTRA_SOURCES={**BASE.EXTRA, BASE.ORIGINAL: BASE.ORIGINAL_SHA, BASE_NAME: BASE_SHA, **HOOKS},
        M32_ORIGINAL_SOURCE_SHA=BASE.ORIGINAL_SHA)
    exec(compile(source, '<original-spectral-M40-explicit-initial-laws>', 'exec'), namespace)
    # The original resource factory calls this complete live ready comparison.
    BASE.live_tail_metric_identity = ready_checker
    namespace['resource_class'] = BASE.resource_class
    key = 'VISIBLE_FLEX_EXACT_STAGE_CACHE'
    previous, old_argv = os.environ.get(key), sys.argv
    own.spectral_stage_cache_directory.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(own.spectral_stage_cache_directory.resolve())
    snapshot = os.environ.pop('VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST', None)
    sys.argv = [old_argv[0], *remaining]
    try:
        namespace['main']()
    except BASE.PreflightFinished:
        if not own.spectral_live_preflight_only:
            raise
        terminal = json.loads(out.with_name(out.name+'-spectral-terminal.json').read_text())
        if terminal['counters'] != {'raw_spectral_embeddings': 1, 'resource_wrapped_clients': 1}:
            raise ValueError('Expected one complete raw embedding and unstarted client loader')
        if OBSERVATIONS['production_provider_loads'] < 1 or OBSERVATIONS['saved_provider_loads'] != 1:
            raise ValueError('Both actual and independent saved initial-law providers must load')
        BASE.write_same(out.with_name(out.name+'-live-preflight-result.json'), dict(
            scope=__doc__, complete_live_prefix_identity_passed=True,
            tail_worker_started=False, full_Jacobian_assembled=False, Newton_run=False,
            numerical_solution_accepted=False, source_transform=transform, terminal=terminal,
            initial_law_load_observations=dict(OBSERVATIONS)))
        print(json.dumps(dict(event='same_g_M40_initial_laws_live_prefix_preflight_complete',
            original_physical_metric_unchanged=True, numerical_solution_accepted=False,
            tail_worker_started=False, out_prefix=str(out))), flush=True)
    finally:
        sys.argv = old_argv
        if previous is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = previous
        if snapshot is not None:
            os.environ['VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST'] = snapshot


if __name__ == '__main__':
    main()

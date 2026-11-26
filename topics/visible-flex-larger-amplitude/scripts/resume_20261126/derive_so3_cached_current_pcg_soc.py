#!/usr/bin/env python3
"""Bind the complete current-SO3 eight-column PCG sources by literal derivation.

This module imports only stdlib and the already byte-bound pure predecessor
deriver. It reconstructs the complete old and new drivers, launchers and cache.
No numerical module, field, J, root, preconditioner or fixture is evaluated.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

SCHEMA = 'complete-normalized-parent-cached-current-eight-column-PCG-SOC-v1'
OLD_DERIVER_SHA = '424311d2a85ab74e14a8aeb3bdb3a0bf4f4cad07fd0abee6e4c4adef6113bacd'
OLD_DRIVER_SHA = '892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8'
OLD_LAUNCHER_SHA = '6c594f20adba3fa519a10c68669a42e099fd6d1d24f2e5f4fa49ff583b4b038e'
OLD_CACHE_SHA = '50a9a4802fb23d01659de4a5ff2e1429f52837c59d6b4c563ae72f54836a4abe'
HELPER_SHA = 'e716afd05b162baecbdddf29ec119974213745bd5235fc1a23f36b4792ecb021'
FRAME_SHA = 'ac03c43dba4c24016a79012e322d66a53b0ed155a1e5e00065e476846cc8ec33'
V5_SHA = '76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8'
DRIVER_SHA = 'a0e27f36692d565d333b1ef5a207afa425ec0fc9a120164a0df3a3057f3dc743'
LAUNCHER_SHA = '333ea5c5f9c06b434c4f16fcb8e93ec202d7f40decf819c152e26ddcef3257e2'
CACHE_SHA = '78f7924f89ee874d14ea9dd9b78630910ed6c0b5e53c9ed4771d910015fcdfb7'
DRIVER_NAME = 'fullclosed_so3_cached_current_pcg_soc.py'
LAUNCHER_NAME = 'launch_so3_cached_current_pcg_soc.py'
CACHE_NAME = 'so3_frozen_parent_cache_for_current_pcg.py'
DRIVER_PATCHES = [["\"\"\"Complete normalized-parent cached SO(3) interior restoration and all-row separation/SOC.","\"\"\"Complete same-current eight-column SO(3) PCG with unchanged restoration and SOC."],["only actual same-Phi, domain and full nonlinear geometry can accept its result.\n","only actual same-Phi, domain and full nonlinear geometry can accept its result.\nThe metric QP may use one fixed eight-column SPD preconditioner assembled from\nits current complete A/A*. It is not a field ansatz or a changed objective.\nPhase I retains the original v3, and all actual nonlinear selection is unchanged.\n"],["SCHEMA = 'complete-normalized-parent-cached-interior-separated-SOC-v1'","SCHEMA = 'complete-normalized-parent-cached-current-eight-column-PCG-SOC-v1'"],["    'reference_cache': ('scripts/resume_20261126/so3_frozen_parent_cache_for_soc.py', '50a9a4802fb23d01659de4a5ff2e1429f52837c59d6b4c563ae72f54836a4abe'),\n","    'reference_cache': ('scripts/resume_20261126/so3_frozen_parent_cache_for_current_pcg.py', '78f7924f89ee874d14ea9dd9b78630910ed6c0b5e53c9ed4771d910015fcdfb7'),\n    'predecessor_SOC_cache': ('scripts/resume_20261126/so3_frozen_parent_cache_for_soc.py', '50a9a4802fb23d01659de4a5ff2e1429f52837c59d6b4c563ae72f54836a4abe'),\n    'predecessor_SOC_driver': ('scripts/resume_20261126/fullclosed_so3_cached_interior_separation_soc.py', '892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8'),\n    'predecessor_SOC_deriver': ('scripts/resume_20261126/derive_normalized_parent_cached_soc.py', '424311d2a85ab74e14a8aeb3bdb3a0bf4f4cad07fd0abee6e4c4adef6113bacd'),\n    'current_coarse': ('scripts/resume_20261126/so3_current_eight_column_preconditioner.py', 'ac03c43dba4c24016a79012e322d66a53b0ed155a1e5e00065e476846cc8ec33'),\n    'qp_v5': ('scripts/resume_20261126/fullspace_feasible_active_pcg_v5.py', '76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8'),\n"],["    qp = load('_so3_complete_QPv3', paths['qp'])\n","    qp = load('_so3_complete_QPv3', paths['qp'])\n    qp_v5 = load('_so3_complete_current_QPv5', paths['qp_v5'])\n    current_coarse = load('_so3_complete_current_eight_column_frame', paths['current_coarse'])\n"],["        if restart.get('schema') == SCHEMA:\n","        if restart.get('schema') in (SCHEMA, 'complete-normalized-parent-cached-interior-separated-SOC-v1'):\n"],["            same_SOC_policy_continued=restart['schema'] == SCHEMA,\n            full_SOC_newly_enabled_at_this_layer=restart['schema'] != SCHEMA),\n","            same_SOC_policy_continued=restart['schema'] in (SCHEMA, 'complete-normalized-parent-cached-interior-separated-SOC-v1'),\n            full_SOC_newly_enabled_at_this_layer=restart['schema'] not in (SCHEMA, 'complete-normalized-parent-cached-interior-separated-SOC-v1'),\n            current_metric_preconditioner_newly_enabled_at_this_layer=restart['schema'] != SCHEMA),\n"],["        complete_same_parent_SOC=dict(maximum_rounds=args.soc_rounds, tau=args.soc_tau,\n","        current_full_QP_preconditioner_policy=dict(\n            schema='same-current-complete-SO3-eight-column-metric-only-PCG-policy-v1',\n            preparation_source_sha256=sha(paths['current_coarse']),\n            metric_consumer_source_sha256=sha(paths['qp_v5']),\n            original_v3_source_sha256=sha(paths['qp']),\n            coarse_column_count=8, current_complete_A_and_Atranspose_each_column=True,\n            fixed_global_SPD_for_one_complete_QP=True,\n            complete_original_QP_norm_penalty_and_C_preserved=True,\n            previous_parent_Gram_used=False, reduced_field_ansatz=False,\n            original_Phase_I_v3_unchanged=True,\n            preparation_failure_scope='Optional numeric preparation only; source/layout/current-point mismatches raise',\n            original_v3_fallback_before_PCG_only=True,\n            mid_chain_application_failure_truncates_honestly=True,\n            performance_gain_not_predeclared=True),\n        complete_same_parent_SOC=dict(maximum_rounds=args.soc_rounds, tau=args.soc_tau,\n"],["            bridge = hessian.NativeLinearization(q, x, stage_weights, parameters, spectral_module=spectral)\n            factor = math.sqrt(parameters.k/(parameters.scale**2*normalizer))\n            residual = factor*bridge.residual\n            A = LinearOperator((len(residual), q.free_size), dtype=np.float64,\n                matvec=lambda z: factor*bridge.operator.matvec(coordinates.lift(z)),\n                rmatvec=lambda v: factor*coordinates.transpose(bridge.operator.rmatvec(v)))\n            used_damping, maxiter = damping, args.maxiter\n","            bridge = hessian.NativeLinearization(q, x, stage_weights, parameters, spectral_module=spectral)\n            factor = math.sqrt(parameters.k/(parameters.scale**2*normalizer))\n            used_damping, maxiter = damping, args.maxiter\n            A, residual, current_preconditioner, preparation = current_coarse.prepare(\n                q, coordinates, bridge, x, damping=used_damping,\n                callback=lambda value: event(phase=phase, serial=serial-1, **value))\n            if (preparation['binding']['external_factor_hex'] != factor.hex()\n                    or A.shape != (len(residual), q.free_size)\n                    or preparation['enabled'] != (current_preconditioner is not None)):\n                raise ValueError('The optional same-current preparation changed the original full A, units or dispatch')\n            record['current_eight_column_preconditioner'] = preparation\n            record['actual_metric_QP_dispatch'] = dict(\n                wrapper_source_sha256=sha(paths['qp_v5']),\n                effective_solver_source_sha256=sha(paths['qp_v5'] if current_preconditioner is not None else paths['qp']),\n                fixed_global_preconditioner_used=current_preconditioner is not None,\n                unavailable_preparation_delegates_to_original_v3_before_any_PCG_chain=current_preconditioner is None,\n                mid_PCG_failure_never_restarts_with_identity=True)\n"],["        coordinate_step, qp_report = qp.solve(A, residual, solve_C, solve_bounds,\n            damping=used_damping, block_columns=args.active_block_columns,\n            parameters=qp.Parameters(maxiter=maxiter, atol=args.qp_atol, rtol=args.qp_rtol,\n                feasibility_tolerance=args.qp_feasibility_tolerance,\n                rank_tolerance=args.qp_rank_tolerance, progress_every=1),\n            callback=lambda value: event(event='SO3_actual_QP_progress', phase=phase, serial=serial-1, progress=value))\n","        if phase == 'metric':\n            coordinate_step, qp_report = qp_v5.solve(A, residual, solve_C, solve_bounds,\n                damping=used_damping, block_columns=args.active_block_columns,\n                parameters=qp.Parameters(maxiter=maxiter, atol=args.qp_atol, rtol=args.qp_rtol,\n                    feasibility_tolerance=args.qp_feasibility_tolerance,\n                    rank_tolerance=args.qp_rank_tolerance, progress_every=1),\n                callback=lambda value: event(event='SO3_actual_QP_progress', phase=phase, serial=serial-1, progress=value),\n                preconditioner=None if current_preconditioner is None else current_preconditioner.apply,\n                preconditioner_metadata=preparation, v3_source=paths['qp'])\n            del current_preconditioner\n        else:\n            coordinate_step, qp_report = qp.solve(A, residual, solve_C, solve_bounds,\n                damping=used_damping, block_columns=args.active_block_columns,\n                parameters=qp.Parameters(maxiter=maxiter, atol=args.qp_atol, rtol=args.qp_rtol,\n                    feasibility_tolerance=args.qp_feasibility_tolerance,\n                    rank_tolerance=args.qp_rank_tolerance, progress_every=1),\n                callback=lambda value: event(event='SO3_actual_QP_progress', phase=phase, serial=serial-1, progress=value))\n"]]
LAUNCHER_PATCHES = [["\"\"\"Execute complete normalized-parent cached interior restoration and all-row SOC.","\"\"\"Execute current eight-column PCG with unchanged normalized-parent full SOC."],["DRIVER_SHA = '892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8'","DRIVER_SHA = 'a0e27f36692d565d333b1ef5a207afa425ec0fc9a120164a0df3a3057f3dc743'"],["driver = source/'fullclosed_so3_cached_interior_separation_soc.py'","driver = source/'fullclosed_so3_cached_current_pcg_soc.py'"],["schema='public-actions-complete-normalized-parent-cached-interior-separated-SOC-command-v1'","schema='public-actions-complete-normalized-parent-current-eight-column-PCG-SOC-command-v1'"],["        original_234ac_and_d3f25_methods_unchanged=True,\n","        original_234ac_and_d3f25_methods_unchanged=True,\n        current_full_QP_eight_column_preconditioner=True,\n        original_norm_damping_constraints_and_SOC_preserved=True,\n        preparation_A_and_Astar_costs_are_reported_by_driver=True,\n        phase_I_uses_original_unpreconditioned_v3=True,\n        performance_improvement_claimed=False,\n"]]
CACHE_PATCHES = [["\"\"\"Explicit original/cached/SOC producer binding for the same immutable T0 cache.","\"\"\"Explicit original/cached/SOC/current-PCG producers for the same immutable T0 cache."],["CONSUMER_SCHEMA = 'complete-normalized-parent-cached-interior-separated-SOC-v1'\nCONSUMER_BASENAME = 'fullclosed_so3_cached_interior_separation_soc.py'\n","CONSUMER_SCHEMA = 'complete-normalized-parent-cached-current-eight-column-PCG-SOC-v1'\nCONSUMER_BASENAME = 'fullclosed_so3_cached_current_pcg_soc.py'\n"],["LEGACY_PRODUCERS = {\n","LEGACY_PRODUCERS = {\n    'complete-normalized-parent-cached-interior-separated-SOC-v1':\n        ('fullclosed_so3_cached_interior_separation_soc.py', '892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8'),\n"],["            allowed_cache_sources = {'4e9ed6949bf42f8ef103b06d0e15dbfa1a8f7d21317a9492f71dca33195824cd', sha(__file__)}\n","            allowed_cache_sources = {'4e9ed6949bf42f8ef103b06d0e15dbfa1a8f7d21317a9492f71dca33195824cd',\n                '50a9a4802fb23d01659de4a5ff2e1429f52837c59d6b4c563ae72f54836a4abe', sha(__file__)}\n"]]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def sha_text(value):
    return hashlib.sha256(value.encode()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def apply_exact(source, patches):
    for old, new in patches:
        if source.count(old) != 1:
            raise ValueError('A complete literal source edit must have exactly one occurrence')
        source = source.replace(old, new, 1)
    return source


def validate_source(source, name):
    tree = ast.parse(source, filename=name)
    compile(tree, name, 'exec')
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            keys = [key.value for key in node.keys if isinstance(key, ast.Constant)
                and isinstance(key.value, (str, int, float))]
            if len(keys) != len(set(keys)):
                raise ValueError('Duplicate literal dictionary key in '+name)
    if any(line != line.rstrip() for line in source.splitlines()):
        raise ValueError('Trailing whitespace in complete source '+name)
    return tree


def source_pins(source):
    matches = [ast.literal_eval(node.value) for node in ast.parse(source).body
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name)
            and t.id == 'SOURCE_PINS' for t in node.targets)]
    if len(matches) != 1:
        raise ValueError('Exactly one literal full source registry is required')
    return matches[0]


def functions(source):
    result = {}
    for node in ast.parse(source).body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            result[node.name] = node
    return result


def unchanged_driver_interfaces(old, new):
    a, b = functions(old), functions(new)
    if set(a) != set(b):
        raise ValueError('No original complete physical or phase interface may be removed')
    for name in a:
        if name != 'main' and ast.dump(a[name]) != ast.dump(b[name]):
            raise ValueError('Changed original complete interface '+name)
    aa = {n.name: n for n in a['main'].body if isinstance(n, ast.FunctionDef)}
    bb = {n.name: n for n in b['main'].body if isinstance(n, ast.FunctionDef)}
    if set(aa) != set(bb) or any(ast.dump(aa[k]) != ast.dump(bb[k]) for k in aa):
        raise ValueError('Preserve every complete same-Phi/statistics/memory/cache local function')
    marker = '        alpha = 1.'
    if old.count(marker) != 1 or new.count(marker) != 1:
        raise ValueError('Bind the unique original complete ray and SOC suffix')
    if old[old.index(marker):] != new[new.index(marker):]:
        raise ValueError('The entire physical line search, SOC, acceptance and final suffix changed')
    oldpins, newpins = source_pins(old), source_pins(new)
    for role, item in oldpins.items():
        if role != 'reference_cache' and newpins.get(role) != item:
            raise ValueError('An original complete scientific source role changed: '+role)
    if newpins['predecessor_SOC_cache'] != oldpins['reference_cache']:
        raise ValueError('Keep the original actual SOC cache source independently attributed')


def unchanged_cache_methods(old, new):
    def collect(source):
        result = {}
        for node in ast.parse(source).body:
            if isinstance(node, ast.FunctionDef):
                result[node.name] = node
            elif isinstance(node, ast.ClassDef):
                for method in node.body:
                    if isinstance(method, ast.FunctionDef):
                        result[node.name+'.'+method.name] = method
        return result
    a, b = collect(old), collect(new)
    if set(a) != set(b):
        raise ValueError('Keep the full original cache interfaces')
    for name in a:
        if name != 'FrozenParentCache._adopt' and ast.dump(a[name]) != ast.dump(b[name]):
            raise ValueError('Changed an original complete cache/query/bytes guard: '+name)


def derive(old_driver, old_launcher, old_cache):
    if (sha_text(old_driver) != OLD_DRIVER_SHA
            or sha_text(old_launcher) != OLD_LAUNCHER_SHA
            or sha_text(old_cache) != OLD_CACHE_SHA):
        raise ValueError('Bind the three complete actual predecessor sources')
    driver = apply_exact(old_driver, DRIVER_PATCHES)
    launcher = apply_exact(old_launcher, LAUNCHER_PATCHES)
    cache = apply_exact(old_cache, CACHE_PATCHES)
    for name, value, digest in ((DRIVER_NAME, driver, DRIVER_SHA),
            (LAUNCHER_NAME, launcher, LAUNCHER_SHA), (CACHE_NAME, cache, CACHE_SHA)):
        validate_source(value, name)
        if sha_text(value) != digest:
            raise ValueError('Complete derived source differs: '+name)
    unchanged_driver_interfaces(old_driver, driver)
    unchanged_cache_methods(old_cache, cache)
    oldparse = functions(old_launcher)['parse_args']
    newparse = functions(launcher)['parse_args']
    if ast.dump(oldparse) != ast.dump(newparse):
        raise ValueError('All original scientific CLI arguments must retain their meaning')
    return {DRIVER_NAME: driver, LAUNCHER_NAME: launcher, CACHE_NAME: cache}


def verify_sources(repo, *, source_directory=None):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    original = topic/'scripts/resume_20261126'
    actual = original if source_directory is None else Path(source_directory).resolve()
    derivation = original/'derive_normalized_parent_cached_soc.py'
    if sha(derivation) != OLD_DERIVER_SHA:
        raise ValueError('The complete predecessor derivation changed')
    spec = importlib.util.spec_from_file_location('_current_SO3_predecessor_pure_deriver', derivation)
    previous = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = previous
    spec.loader.exec_module(previous)
    helper = (original/'complete_normalized_parent_so3_rows_soc.py').read_text()
    oldcache = (original/'so3_frozen_parent_cache_for_soc.py').read_text()
    olddriver = (original/'fullclosed_so3_cached_interior_separation_soc.py').read_text()
    oldlauncher = (original/'launch_so3_cached_interior_separation_soc.py').read_text()
    reconstructed_old = previous.derive_driver(
        (original/'fullclosed_so3_cached_interior_restore_qp.py').read_text(), helper, oldcache)
    reconstructed_launcher = previous.derive_launcher(
        (original/'launch_so3_cached_interior_restore_actions.py').read_text(), reconstructed_old)
    if reconstructed_old != olddriver or reconstructed_launcher != oldlauncher:
        raise ValueError('The actual complete predecessor differs from its original full derivation')
    if sha_text(helper) != HELPER_SHA:
        raise ValueError('Keep the complete original same-parent SOC algebra')
    previous.unchanged_helper_methods(
        (original/'complete_axisymmetric_so3_rows_soc.py').read_text(), helper,
        changed={'CompleteSO3RowsSOC.__init__'})
    previous.unchanged_helper_methods(
        (original/'so3_frozen_parent_cache.py').read_text(), oldcache,
        changed={'FrozenParentCache._adopt'})
    derived = derive(olddriver, oldlauncher, oldcache)
    for name, expected in derived.items():
        if (actual/name).read_text() != expected:
            raise ValueError('The entire actual new source differs: '+name)
    pins = source_pins(derived[DRIVER_NAME])
    # During pure prepublication checking only these three new bodies may be
    # read from the explicitly supplied source directory. Every scientific
    # dependency retains its actual public path and exact source hash.
    local_names = set(derived)
    records = {}
    for role, (relative, digest) in pins.items():
        path = topic/relative
        if source_directory is not None and path.name in local_names:
            path = actual/path.name
        if sha(path) != digest:
            raise ValueError('Changed complete actual source role '+role)
        records[role] = dict(repo_relative_path=relative, sha256=digest)
    return dict(actual_entire_body_match=True, actual_driver_sha256=DRIVER_SHA,
        actual_launcher_sha256=LAUNCHER_SHA, complete_cache_source_sha256=CACHE_SHA,
        previous_complete_driver_sha256=OLD_DRIVER_SHA,
        previous_complete_launcher_sha256=OLD_LAUNCHER_SHA,
        previous_complete_cache_source_sha256=OLD_CACHE_SHA,
        previous_full_body_derivation_sha256=OLD_DERIVER_SHA,
        current_frame_source_sha256=FRAME_SHA, fixed_face_PCG_source_sha256=V5_SHA,
        complete_source_records=records, original_physical_sources_unchanged=True,
        exact_original_Phase_I_class_unchanged=True,
        exact_original_ray_SOC_acceptance_suffix_unchanged=True,
        every_full_same_field_statistics_and_memory_function_unchanged=True,
        scientific_modules_imported=False, scientific_execution=False,
        field_calls=0, J_calls=0, Jtranspose_calls=0,
        geometric_feasibility_or_convergence_inferred=False)


def bind_report(repo, report_path):
    identity = verify_sources(repo)
    report = json.loads(Path(report_path).read_text())
    if report.get('schema') != SCHEMA or report.get('source_sha256') != DRIVER_SHA:
        raise ValueError('The report is not this complete new source and schema')
    expected = {key: value['sha256'] for key, value in identity['complete_source_records'].items()}
    if report.get('source_sha256_by_role') != expected:
        raise ValueError('The actual report complete source registry differs')
    identity.update(actual_source_commit=report.get('source_commit'),
        model_identity_sha256=report.get('model_identity_sha256'),
        raw_scientific_arrays_recomputed=False)
    return identity


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--source-directory', type=Path)
    p.add_argument('--verify-existing', action='store_true', required=True)
    a = p.parse_args()
    result = verify_sources(a.repo, source_directory=a.source_directory)
    print(json.dumps(result, sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()

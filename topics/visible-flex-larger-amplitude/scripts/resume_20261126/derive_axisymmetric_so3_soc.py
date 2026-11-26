#!/usr/bin/env python3
"""Pure complete-source derivation of the actual SO3 separation/SOC successor.

This performs only source-byte/AST and JSON attribution. It never imports
the numerical driver, helper, NumPy, Torch, a field, a Jacobian or a QP.
The independent published original bodies remain unchanged.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

ORIGINAL_DRIVER_SHA = '606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9'
ORIGINAL_LAUNCHER_SHA = 'a94263f037dfa8535b11cf44fa93b6a4cd6df7dee1a6be35f2ea14f5abaa2690'
HELPER_SHA = '02875e4a150644f8addb6073b346e2de3b0f3cf50498e9cf6efe8fe0333d7c97'
PROJECTION_SHA = 'a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'
SCHEMA = 'complete-independent-axisymmetric-fixed-deep-so3-prior-separation-and-SOC-v1'

DERIVED_DRIVER_SHA = '359ffc94df1b33485c2cda4de0f5662ef7bc802c588f583a023fcd5723a7872d'
DERIVED_LAUNCHER_SHA = 'faf5f67000eb81a0bc6d26126641f10c606a879f935158222b1fce0f50525d02'

DRIVER_PATCHES = [
    ("SCHEMA = 'complete-independent-axisymmetric-fixed-deep-so3-meridian-QP-v1'", "SCHEMA = 'complete-independent-axisymmetric-fixed-deep-so3-prior-separation-and-SOC-v1'"),
    ("    'geometry_selector': ('scripts/resume_20261120/fullclosed_point_inequalities_v2.py', 'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'),\n}", "    'geometry_selector': ('scripts/resume_20261120/fullclosed_point_inequalities_v2.py', 'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'),\n    'complete_soc_rows': ('scripts/resume_20261126/complete_axisymmetric_so3_rows_soc.py', '02875e4a150644f8addb6073b346e2de3b0f3cf50498e9cf6efe8fe0333d7c97'),\n    'soc_projection': ('scripts/resume_20261126/full_phi_all_rows_soc.py', 'a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'),\n    'original_axisymmetric_reader': ('scripts/resume_20261126/read_axisymmetric_so3_report.py', '6d54cbba7ff998bc98b0f39c6a26ae33c16957fb0b9dc0fffced1037212455eb'),\n    'original_axisymmetric_driver': ('scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py', '606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9'),\n}"),
    ("    p.add_argument('--line-trials', type=int, default=15)\n", "    p.add_argument('--line-trials', type=int, default=15)\n    p.add_argument('--soc-rounds', type=int, default=8)\n    p.add_argument('--soc-tau', type=float, default=0.)\n    p.add_argument('--soc-inward-fraction', type=float, default=.125)\n    p.add_argument('--soc-feasibility-tolerance', type=float, default=2.e-11)\n"),
    ("    a = p.parse_args()\n", "    a = p.parse_args()\n    if (not 1 <= a.soc_rounds <= 8 or any(not math.isfinite(v) or v < 0\n            for v in (a.soc_tau, a.soc_inward_fraction, a.soc_feasibility_tolerance))):\n        raise ValueError('Declare one-to-eight complete SOC rounds and finite nonnegative inward/readback parameters')\n"),
    ("    history = load('_so3_complete_address_history', paths['history'])\n", "    history = load('_so3_complete_address_history', paths['history'])\n    soc_module = load('_so3_complete_fixed_parent_separation_SOC', paths['complete_soc_rows'])\n"),
    ("        restart = json.loads(args.restart_report.read_text())\n        if (restart.get('schema') != SCHEMA or restart.get('source_sha256') != sha(__file__)\n                or restart.get('complete') is not True\n", "        restart = json.loads(args.restart_report.read_text())\n        if restart.get('schema') == 'complete-independent-axisymmetric-fixed-deep-so3-meridian-QP-v1':\n            if restart.get('source_sha256') != SOURCE_PINS['original_axisymmetric_driver'][1]:\n                raise ValueError('The original axisymmetric parent must retain its actual complete 606 body')\n            old_reader = load('_SO3_original_complete_parent_reader', paths['original_axisymmetric_reader'])\n            old_reader.read_report(args.repo, args.restart_report, verify_final_bundle=True)\n        elif restart.get('schema') == SCHEMA:\n            if (restart.get('source_sha256') != sha(__file__)\n                    or restart.get('source_sha256_by_role') != {role: sha(path) for role, path in paths.items()}):\n                raise ValueError('A same-SOC continuation must retain this full body and every true source role')\n        else:\n            raise ValueError('Only the actual complete original or this complete separation-SOC parent is accepted')\n        if (restart.get('complete') is not True\n"),
    ("        metric_directions=[], restoration_directions=[],\n", "        complete_same_parent_SOC=dict(maximum_rounds=args.soc_rounds, tau=args.soc_tau,\n            observed_violation_inward_fraction=args.soc_inward_fraction,\n            numerical_readback_tolerance=args.soc_feasibility_tolerance,\n            prior_true_rejection_addresses_linearized_before_NEW_QP=True,\n            original_selector_and_amplitude_prefix_never_removed=True,\n            no_prior_physical_covectors_or_values_inherited=True,\n            whole_current_QP_prefix_preserved_through_every_correction=True,\n            same_parent_same_ray_anchor_every_round=True,\n            true_same_Phi_domain_and_full_geometry_required=True,\n            numerical_finite_projection_is_not_a_geometric_certificate=True),\n        metric_directions=[], restoration_directions=[],\n"),
    ("        serial += 1\n", "        soc_helper, prior_separation = None, None\n        if phase == 'metric':\n            original_rows_metadata = rows\n            soc_helper = soc_module.CompleteSO3RowsSOC(q, x, coordinates, screen,\n                C, bounds, original_rows_metadata,\n                projection_source=paths['soc_projection'],\n                parent_identity=dict(actual_driver_source_sha256=sha(__file__),\n                    actual_source_commit=source_commit,\n                    initial_reference_bundle_sha256=sha(args.reference_bundle),\n                    fixed_scalar_metric_identity_sha256=fixed_profile,\n                    screen_current_point_sha256=geometry['current_full_point_sha256'],\n                    actual_direction_serial=serial),\n                max_rounds=args.soc_rounds, block_columns=args.active_block_columns)\n            prior_separation = soc_helper.seed_before_qp((restart, report), geometry)\n            if prior_separation.get('extension_available') is not True:\n                report['prior_separation_requires_actual_parent_restoration'] = prior_separation\n                save_report()\n                raise ValueError('An actual newly separated current-parent constraint requires restoration; negative bounds are not a feasible zero')\n            for value in soc_helper.new_curvature_locations:\n                add_location(value, witnesses, q)\n            for value in soc_helper.new_radius_locations:\n                add_location(value, radius_witnesses, q)\n            soc_helper.freeze_qp_prefix()\n            C, bounds = soc_helper.C, soc_helper.b\n            rows = soc_helper.qp_metadata(original_rows_metadata)\n        serial += 1\n"),
    ("            accepted=False, trials=[], original_geometry_rows_retained=rows['original_prefix_rows'],\n", "            accepted=False, trials=[], soc_trials=[], prior_rejection_separation=prior_separation,\n            original_geometry_rows_retained=rows['original_prefix_rows'],\n"),
    ("        # Release the full positive residual-Hessian storage before trials.\n        if phase == 'metric':\n            del bridge\n        del A, residual, coordinate_step, solve_C, solve_bounds\n        alpha = 1.\n        for trial_index in range(args.line_trials):\n            trial_started = time.monotonic()\n            candidate = x+alpha*step\n            trial = dict(index=trial_index, alpha=alpha, accepted=False,\n                metric_descent_required=phase == 'metric', full_true_geometry_read=False)\n            trial_native, trial_statistics, trial_geometry = None, None, None\n            try:\n                trial_native = q.residual(candidate)\n                trial_statistics = statistics(candidate, trial_native)\n                domain_ok = (trial_statistics['min_relative_E'] > 0\n                    and trial_statistics['min_relative_determinant'] > 0)\n                trial_merit = trial_statistics['spectral'][objective_key]\n                descent = (trial_merit < old_merit and (half_slope is None or half_slope >= 0\n                    or trial_merit <= old_merit+.0002*alpha*half_slope))\n                if domain_ok and (phase == 'restoration' or descent):\n                    trial_geometry = scan(candidate)\n                    trial['full_true_geometry_read'] = True\n                trial_violation = None if trial_geometry is None else physical_violation(trial_geometry)\n                if phase == 'metric':\n                    accepted = domain_ok and descent and trial_geometry is not None and geometric_feasible(trial_geometry)\n                else:\n                    accepted = (domain_ok and trial_violation is not None\n                        and trial_violation < old_violation\n                        and trial_violation <= (1-1.e-4*alpha)*old_violation)\n                trial.update(statistics=trial_statistics, domain_feasible=domain_ok,\n                    actual_Phi_descent=descent, actual_positive_physical_g=trial_violation,\n                    full_geometry=trial_geometry, accepted=bool(accepted),\n                    physically_feasible=False if trial_geometry is None else geometric_feasible(trial_geometry))\n            except (FloatingPointError, OverflowError, ValueError, RuntimeError) as exception:\n                accepted = False\n                trial.update(actual_read_error=repr(exception), accepted=False,\n                    complete=False, scope='A true numerical trial failure, not global infeasibility')\n            trial['actual_seconds'] = time.monotonic()-trial_started\n            record['trials'].append(trial)\n            event(event='SO3_actual_trial', phase=phase, serial=serial-1,\n                index=trial_index, alpha=alpha, accepted=bool(accepted),\n                maximum_gram=None if trial_statistics is None else trial_statistics['max_relative_gram'],\n                actual_Phi=None if trial_statistics is None else trial_statistics['spectral'][objective_key],\n                actual_positive_physical_g=trial.get('actual_positive_physical_g'),\n                actual_read_error=trial.get('actual_read_error'))\n            if accepted:\n                x, native, current, geometry = candidate, trial_native, trial_statistics, trial_geometry\n                record.update(accepted=True, accepted_alpha=alpha, accepted_statistics=current,\n                    accepted_geometry=geometry)\n                accepted_path = args.outdir/f'accepted-{phase}-{record[\"index\"]:03d}.npz'\n                q.save(accepted_path, x)\n                record['accepted_bundle'] = file_record(accepted_path)\n                if phase == 'metric':\n                    ratio = (old_merit-current['spectral'][objective_key])/(-predicted) if predicted < 0 else None\n                    record['actual_to_full_prediction_ratio'] = ratio\n                    if alpha == 1 and ratio is not None and ratio > .75:\n                        damping = max(1.e-8, damping/2)\n                elif geometric_feasible(geometry):\n                    record['actual_restoration_reached_zero_true_violation'] = True\n                break\n            alpha /= 2\n", "        # Keep this one parent residual-Hessian alive: a corrected full z\n        # requires its own A*z and true same-Phi slope/model read.\n        del solve_C, solve_bounds\n        alpha = 1.\n        soc_anchor_attempted = False\n        accepted_via_soc = False\n        accepted_SOC_prediction = None\n        for trial_index in range(args.line_trials):\n            trial_started = time.monotonic()\n            candidate = x+alpha*step\n            trial = dict(index=trial_index, alpha=alpha, accepted=False,\n                metric_descent_required=phase == 'metric', full_true_geometry_read=False)\n            trial_native, trial_statistics, trial_geometry = None, None, None\n            try:\n                trial_native = q.residual(candidate)\n                trial_statistics = statistics(candidate, trial_native)\n                domain_ok = (trial_statistics['min_relative_E'] > 0\n                    and trial_statistics['min_relative_determinant'] > 0)\n                trial_merit = trial_statistics['spectral'][objective_key]\n                descent = (trial_merit < old_merit and (half_slope is None or half_slope >= 0\n                    or trial_merit <= old_merit+.0002*alpha*half_slope))\n                if domain_ok and (phase == 'restoration' or descent):\n                    trial_geometry = scan(candidate)\n                    trial['full_true_geometry_read'] = True\n                trial_violation = None if trial_geometry is None else physical_violation(trial_geometry)\n                if phase == 'metric':\n                    accepted = domain_ok and descent and trial_geometry is not None and geometric_feasible(trial_geometry)\n                else:\n                    accepted = (domain_ok and trial_violation is not None\n                        and trial_violation < old_violation\n                        and trial_violation <= (1-1.e-4*alpha)*old_violation)\n                trial.update(statistics=trial_statistics, domain_feasible=domain_ok,\n                    actual_Phi_descent=descent, actual_positive_physical_g=trial_violation,\n                    full_geometry=trial_geometry, accepted=bool(accepted),\n                    physically_feasible=False if trial_geometry is None else geometric_feasible(trial_geometry))\n            except (FloatingPointError, OverflowError, ValueError, RuntimeError) as exception:\n                accepted = False\n                trial.update(actual_read_error=repr(exception), accepted=False,\n                    complete=False, scope='A true numerical trial failure, not global infeasibility')\n            trial['actual_seconds'] = time.monotonic()-trial_started\n            record['trials'].append(trial)\n            event(event='SO3_actual_trial', phase=phase, serial=serial-1,\n                index=trial_index, alpha=alpha, accepted=bool(accepted),\n                maximum_gram=None if trial_statistics is None else trial_statistics['max_relative_gram'],\n                actual_Phi=None if trial_statistics is None else trial_statistics['spectral'][objective_key],\n                actual_positive_physical_g=trial.get('actual_positive_physical_g'),\n                actual_read_error=trial.get('actual_read_error'))\n            if (phase == 'metric' and not accepted and not soc_anchor_attempted\n                    and trial.get('domain_feasible') is True\n                    and trial.get('actual_Phi_descent') is True\n                    and trial_geometry is not None and trial_geometry.get('complete') is True\n                    and trial.get('actual_positive_physical_g') is not None\n                    and trial['actual_positive_physical_g'] > 0):\n                soc_anchor_attempted = True\n                anchor_coordinate_step = alpha*coordinate_step\n                try:\n                    soc_helper.bind_anchor(anchor_coordinate_step, alpha, candidate)\n                    rejected_geometry = trial_geometry\n                    record['SOC_anchor'] = dict(ray_index=trial_index, ray_alpha=alpha,\n                        fixed_original_QP_direction=True, fixed_current_parent=True,\n                        alpha_scaled_original_QP_prefix_is_preserved=True)\n                    for round_index in range(args.soc_rounds):\n                        soc_started = time.monotonic()\n                        soc_record = dict(index=round_index, anchor_ray_index=trial_index,\n                            anchor_alpha=alpha, accepted=False, full_true_geometry_read=False,\n                            same_original_parent_and_anchor=True,\n                            independent_Az_and_model_reread=False)\n                        extension = soc_helper.extend_from_rejected_geometry(rejected_geometry)\n                        soc_record['separation'] = extension\n                        for value in soc_helper.new_curvature_locations:\n                            add_location(value, witnesses, q)\n                        for value in soc_helper.new_radius_locations:\n                            add_location(value, radius_witnesses, q)\n                        if extension.get('extension_available') is not True:\n                            soc_record.update(stop_reason='No complete new feasible-parent separation; real restoration or another parent is required',\n                                actual_seconds=time.monotonic()-soc_started)\n                            record['soc_trials'].append(soc_record)\n                            break\n                        if round_index and not extension.get('added_rows', 0):\n                            soc_record.update(stop_reason='No new row after a previous true corrected rejection; no identical projection replay',\n                                actual_seconds=time.monotonic()-soc_started)\n                            record['soc_trials'].append(soc_record)\n                            break\n                        corrected_point, corrected_z, proposal = soc_helper.propose(\n                            tau=args.soc_tau, inward_fraction=args.soc_inward_fraction,\n                            feasibility_tolerance=args.soc_feasibility_tolerance)\n                        soc_record['proposal'] = proposal\n                        if corrected_point is None:\n                            soc_record.update(stop_reason='No complete all-row proposal within its declared numerical budget',\n                                actual_seconds=time.monotonic()-soc_started)\n                            record['soc_trials'].append(soc_record)\n                            break\n                        corrected_native, corrected_statistics, corrected_geometry = None, None, None\n                        try:\n                            corrected_linear = A.matvec(corrected_z)\n                            corrected_slope = float(residual@corrected_linear)\n                            corrected_prediction = 2*corrected_slope+float(corrected_linear@corrected_linear)\n                            soc_record.update(independent_Az_and_model_reread=True,\n                                corrected_half_objective_slope=corrected_slope,\n                                corrected_predicted_actual_Phi_change=corrected_prediction,\n                                old_actual_Phi=old_merit,\n                                corrected_coordinate_step_sha256=soc_helper.base.array_sha(corrected_z),\n                                corrected_candidate_sha256=soc_helper.base.array_sha(corrected_point))\n                            corrected_native = q.residual(corrected_point)\n                            corrected_statistics = statistics(corrected_point, corrected_native)\n                            corrected_domain = (corrected_statistics['min_relative_E'] > 0\n                                and corrected_statistics['min_relative_determinant'] > 0)\n                            corrected_merit = corrected_statistics['spectral'][objective_key]\n                            corrected_descent = (corrected_merit < old_merit\n                                and (corrected_slope >= 0 or corrected_merit <= old_merit+.0002*corrected_slope))\n                            if corrected_domain and corrected_descent:\n                                corrected_geometry = scan(corrected_point)\n                                soc_record['full_true_geometry_read'] = True\n                            corrected_violation = None if corrected_geometry is None else physical_violation(corrected_geometry)\n                            corrected_accepted = (corrected_domain and corrected_descent\n                                and corrected_geometry is not None and geometric_feasible(corrected_geometry))\n                            soc_record.update(statistics=corrected_statistics, domain_feasible=corrected_domain,\n                                actual_Phi_descent=corrected_descent, actual_positive_physical_g=corrected_violation,\n                                full_geometry=corrected_geometry, accepted=bool(corrected_accepted),\n                                physically_feasible=False if corrected_geometry is None else geometric_feasible(corrected_geometry))\n                        except (FloatingPointError, OverflowError, ValueError, RuntimeError) as exception:\n                            corrected_accepted = False\n                            soc_record.update(actual_read_error=repr(exception), accepted=False,\n                                complete=False, scope='A corrected true numerical read failure, not global infeasibility')\n                        soc_record['actual_seconds'] = time.monotonic()-soc_started\n                        record['soc_trials'].append(soc_record)\n                        event(event='SO3_actual_complete_separation_SOC_trial', serial=serial-1,\n                            round=round_index+1, anchor_alpha=alpha,\n                            all_current_rows=proposal.get('current_rows'),\n                            accepted=bool(corrected_accepted),\n                            actual_Phi=None if corrected_statistics is None else corrected_statistics['spectral'][objective_key],\n                            maximum_gram=None if corrected_statistics is None else corrected_statistics['max_relative_gram'],\n                            actual_positive_physical_g=soc_record.get('actual_positive_physical_g'),\n                            actual_read_error=soc_record.get('actual_read_error'))\n                        if corrected_accepted:\n                            accepted, accepted_via_soc = True, True\n                            accepted_SOC_prediction = corrected_prediction\n                            candidate, trial_native = corrected_point, corrected_native\n                            trial_statistics, trial_geometry = corrected_statistics, corrected_geometry\n                            record['accepted_SOC_round'] = round_index+1\n                            record['accepted_SOC_anchor_alpha'] = alpha\n                            break\n                        if (corrected_geometry is None or corrected_geometry.get('complete') is not True\n                                or not soc_record.get('domain_feasible') or not soc_record.get('actual_Phi_descent')):\n                            break\n                        rejected_geometry = corrected_geometry\n                except (FloatingPointError, OverflowError, ValueError, RuntimeError, OSError) as exception:\n                    record['SOC_unavailable_error'] = repr(exception)\n                    record['SOC_unavailable_is_geometric_infeasibility'] = False\n                finally:\n                    del anchor_coordinate_step\n            if accepted:\n                x, native, current, geometry = candidate, trial_native, trial_statistics, trial_geometry\n                record.update(accepted=True, accepted_alpha=None if accepted_via_soc else alpha,\n                    accepted_step_kind='complete_separation_SOC' if accepted_via_soc else 'original_ray',\n                    accepted_statistics=current, accepted_geometry=geometry)\n                accepted_path = args.outdir/f'accepted-{phase}-{record[\"index\"]:03d}.npz'\n                q.save(accepted_path, x)\n                record['accepted_bundle'] = file_record(accepted_path)\n                if phase == 'metric':\n                    if accepted_via_soc:\n                        record['actual_to_accepted_SOC_prediction_ratio'] = (\n                            (old_merit-current['spectral'][objective_key])/(-accepted_SOC_prediction)\n                            if accepted_SOC_prediction is not None and accepted_SOC_prediction < 0 else None)\n                        record['damping_after_SOC_policy'] = 'Retain the same actual mu; original full-ray ratio is not reused'\n                    else:\n                        ratio = (old_merit-current['spectral'][objective_key])/(-predicted) if predicted < 0 else None\n                        record['actual_to_full_prediction_ratio'] = ratio\n                        if alpha == 1 and ratio is not None and ratio > .75:\n                            damping = max(1.e-8, damping/2)\n                elif geometric_feasible(geometry):\n                    record['actual_restoration_reached_zero_true_violation'] = True\n                break\n            alpha /= 2\n        if soc_helper is not None:\n            record['final_complete_SOC_cache'] = soc_helper.cache_state()\n        if phase == 'metric':\n            del bridge\n        del A, residual, coordinate_step\n"),
    ("        del C, bounds, step\n", "        del C, bounds, step, soc_helper\n"),
    ("\"\"\"Independent axisymmetric-reference SO(3) optimization of one fixed deep g.", "\"\"\"Complete prior-separation and same-parent SOC for the actual SO3 field."),
]

LAUNCHER_PATCHES = [
    ("DRIVER_SHA = '606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9'", "DRIVER_SHA = '359ffc94df1b33485c2cda4de0f5662ef7bc802c588f583a023fcd5723a7872d'"),
    ("fullclosed_axisymmetric_so3_qp.py", "fullclosed_axisymmetric_so3_separation_soc.py"),
    ("    p.add_argument('--line-trials', type=int, default=15)\n", "    p.add_argument('--line-trials', type=int, default=15)\n    p.add_argument('--soc-rounds', type=int, default=8)\n    p.add_argument('--soc-tau', type=float, default=0.)\n    p.add_argument('--soc-inward-fraction', type=float, default=.125)\n    p.add_argument('--soc-feasibility-tolerance', type=float, default=2.e-11)\n"),
    ("    a = p.parse_args()\n", "    a = p.parse_args()\n    if (not 1 <= a.soc_rounds <= 8 or any(not math.isfinite(v) or v < 0\n            for v in (a.soc_tau, a.soc_inward_fraction, a.soc_feasibility_tolerance))):\n        raise ValueError('Declare one-to-eight complete SOC rounds and finite nonnegative inward/readback parameters')\n"),
    ("public-actions-complete-independent-axisymmetric-SO3-command-v1", "public-actions-complete-independent-axisymmetric-SO3-separation-SOC-command-v1"),
]

def sha_text(source):
    return hashlib.sha256(source.encode()).hexdigest()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def apply_exact(source, patches):
    for old, new in patches:
        if source.count(old) != 1:
            raise ValueError('Every complete source replacement has exactly one literal original occurrence')
        source = source.replace(old, new, 1)
    return source


def validate_source(source, filename):
    tree = ast.parse(source, filename=filename)
    compile(tree, filename, 'exec')
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            keys = [key.value for key in node.keys if isinstance(key, ast.Constant)
                and isinstance(key.value, (str, int, float))]
            if len(keys) != len(set(keys)):
                raise ValueError('Duplicate literal dictionary key in complete source '+filename)
    return tree


def source_pins(source):
    tree = ast.parse(source)
    matches = [ast.literal_eval(node.value) for node in tree.body
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name)
            and t.id == 'SOURCE_PINS' for t in node.targets)]
    if len(matches) != 1:
        raise ValueError('One complete literal source-role table is required')
    return matches[0]


def unchanged_functions(original, derived):
    a, b = ast.parse(original), ast.parse(derived)
    top_a = {n.name: n for n in a.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
    top_b = {n.name: n for n in b.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
    if set(top_a) != set(top_b):
        raise ValueError('No original complete top-level scientific interface is removed')
    for name in top_a:
        if name not in ('main', 'parse_args') and ast.dump(top_a[name]) != ast.dump(top_b[name]):
            raise ValueError('An unrelated complete original function changed: '+name)
    nested_a = {n.name: n for n in top_a['main'].body if isinstance(n, ast.FunctionDef)}
    nested_b = {n.name: n for n in top_b['main'].body if isinstance(n, ast.FunctionDef)}
    if set(nested_a) != set(nested_b):
        raise ValueError('Retain every complete original local statistics/geometry interface')
    for name in nested_a:
        if ast.dump(nested_a[name]) != ast.dump(nested_b[name]):
            raise ValueError('An original full local scientific read changed: '+name)


def derive_driver(original, helper):
    if sha_text(original) != ORIGINAL_DRIVER_SHA or sha_text(helper) != HELPER_SHA:
        raise ValueError('Bind the actual complete original driver and complete new helper bytes')
    result = apply_exact(original, DRIVER_PATCHES)
    validate_source(helper, 'complete_axisymmetric_so3_rows_soc.py')
    validate_source(result, 'fullclosed_axisymmetric_so3_separation_soc.py')
    unchanged_functions(original, result)
    old_pins, new_pins = source_pins(original), source_pins(result)
    for role, value in old_pins.items():
        if new_pins.get(role) != value:
            raise ValueError('An original physical/norm/objective/geometry/solver source changed: '+role)
    if sha_text(result) != DERIVED_DRIVER_SHA:
        raise ValueError('The complete derived driver does not match the declared literal body')
    return result


def derive_launcher(original, complete_driver):
    if sha_text(original) != ORIGINAL_LAUNCHER_SHA or sha_text(complete_driver) != DERIVED_DRIVER_SHA:
        raise ValueError('Bind the actual complete original launcher and complete new driver')
    result = apply_exact(original, LAUNCHER_PATCHES)
    validate_source(result, 'launch_axisymmetric_so3_separation_soc.py')
    if sha_text(result) != DERIVED_LAUNCHER_SHA:
        raise ValueError('The complete derived launcher does not match its declared body')
    return result


def bind_report(repo, report_path):
    """Entire-body source binding only; detailed actual attribution is the reader."""
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    directory = topic/'scripts/resume_20261126'
    original = directory/'fullclosed_axisymmetric_so3_qp.py'
    helper = directory/'complete_axisymmetric_so3_rows_soc.py'
    derived = directory/'fullclosed_axisymmetric_so3_separation_soc.py'
    expected = derive_driver(original.read_text(), helper.read_text())
    if derived.read_text() != expected or sha(derived) != DERIVED_DRIVER_SHA:
        raise ValueError('The actual complete driver body differs from its full declared derivation')
    report = json.loads(Path(report_path).read_text())
    if report.get('schema') != SCHEMA or report.get('source_sha256') != DERIVED_DRIVER_SHA:
        raise ValueError('The report belongs to another complete driver or representation wrapper')
    pins = source_pins(expected)
    for role, (relative, digest) in pins.items():
        if report['source_sha256_by_role'].get(role) != digest or sha(topic/relative) != digest:
            raise ValueError('Changed actual complete report source role '+role)
    return dict(actual_driver_sha256=DERIVED_DRIVER_SHA,
        actual_driver_schema=SCHEMA, actual_entire_body_match=True,
        original_complete_driver_sha256=ORIGINAL_DRIVER_SHA,
        complete_SOC_helper_sha256=HELPER_SHA, projection_sha256=PROJECTION_SHA,
        actual_source_commit=report.get('source_commit'),
        physical_model_identity_sha256=report.get('model_identity_sha256'),
        raw_scientific_arrays_recomputed=False, field_calls=0, J_calls=0,
        geometric_feasibility_or_convergence_inferred=False)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--original-driver', type=Path, required=True)
    p.add_argument('--original-launcher', type=Path, required=True)
    p.add_argument('--helper', type=Path, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    p.add_argument('--verify-existing', action='store_true')
    a = p.parse_args()
    complete_driver = derive_driver(a.original_driver.read_text(), a.helper.read_text())
    complete_launcher = derive_launcher(a.original_launcher.read_text(), complete_driver)
    outputs = dict(fullclosed_axisymmetric_so3_separation_soc_py=complete_driver,
        launch_axisymmetric_so3_separation_soc_py=complete_launcher)
    names = {'fullclosed_axisymmetric_so3_separation_soc_py': 'fullclosed_axisymmetric_so3_separation_soc.py',
        'launch_axisymmetric_so3_separation_soc_py': 'launch_axisymmetric_so3_separation_soc.py'}
    a.outdir.mkdir(parents=True, exist_ok=True)
    for key, value in outputs.items():
        path = a.outdir/names[key]
        if a.verify_existing:
            if path.read_text() != value:
                raise ValueError('Existing complete generated source differs: '+str(path))
        else:
            if path.exists():
                raise FileExistsError('Do not replace an existing complete source: '+str(path))
            path.write_text(value)
    print(json.dumps(dict(complete=True, pure_source_derivation=True,
        numerical_sources_imported=False, scientific_execution=False,
        source_sha256=sha(__file__), driver_sha256=DERIVED_DRIVER_SHA,
        launcher_sha256=DERIVED_LAUNCHER_SHA, helper_sha256=HELPER_SHA,
        complete_driver_bytes=len(complete_driver.encode()),
        complete_launcher_bytes=len(complete_launcher.encode())),
        sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()

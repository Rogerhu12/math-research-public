#!/usr/bin/env python3
"""Exact source derivation: original or R671 full driver + one parent-row SOC.

This module is stdlib source preparation only.  The numerical derived driver
requires public Actions.  Frozen inputs remain untouched.  It first applies
the published exact-location AST transform, then the enumerated SOC sites.
bind_soc_parent rebuilds this complete body for future source verification;
an unknown body or unknown provenance is never accepted by a comment alone.
"""
import argparse
import ast
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


HELPER_SHA = '5bc50d6b18223685da8ea355d179191234ad83b5e92fd6313f4070b7e02127c7'
MANIFEST_SHA = '100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622'
BASES = {
    'original': ('fullclosed_gauss_inequality_qp.py',
        '5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a'),
    'R671': ('fullclosed_gauss_exact_tail_inequality_qp.py',
        'b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8'),
}
LINEAGE_SCHEMA = 'frozen-full-driver-exact-locations-parent-row-SOC-derivation-v1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    spec = importlib.util.spec_from_file_location('soc_exact_location_derivation', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def statements(text):
    return ast.parse(text).body


def same(left, right):
    return ast.dump(left, include_attributes=False) == ast.dump(right, include_attributes=False)


def name_target(statement, name):
    return (isinstance(statement, ast.Assign)
            and len(statement.targets) == 1
            and isinstance(statement.targets[0], ast.Name)
            and statement.targets[0].id == name)


ACTUAL_TRIAL_FUNCTION = '''
def actual_parent_row_soc(index, parent_x, direction, full_point, full_trial,
                          rows, bounds, row_metadata, operator, virtual_rhs,
                          old_merit, operator_counts):
    started_soc = time.monotonic()
    before_counts = operator_counts.copy()
    engine = soc_module.ParentRowsSOC(problem, parent_x, rows, bounds, row_metadata,
        geometry_module=geometry_module, point_module=point_module,
        observed_module=implementation, inequality_module=inequality_module,
        source_sha256_by_role=report['source_sha256_by_role'],
        observation_carrier_sha256=report['observation_carrier_sha256'],
        model_definition=SOC_MODEL_DEFINITION,
        parent_bundle_sha256=report.get('current_bundle_sha256'),
        block_columns=args.active_block_columns)
    proposal = engine.propose(direction, lift, full_point, full_trial,
        tau=args.soc_tau, workdir=args.outdir/f'soc-rows-{index:03d}',
        rank_tolerance=args.qp_row_rank_tolerance,
        feasibility_tolerance=args.qp_feasibility_tolerance)
    detail = dict(proposal=proposal.report, attempted=True, accepted=False,
        original_trial_index=full_trial['index'], original_ray_alpha=1.,
        tau=args.soc_tau, original_direction_sha256=record['direction_sha256'],
        direction_scope='One correction of this returned parent QP direction, in the same augmented norm',
        additional_cost=dict(corrected_model_matvec=0, corrected_nonlinear_residual=0,
                             corrected_full_known_point_geometry=0))
    if proposal.candidate is None:
        detail['seconds'] = time.monotonic()-started_soc
        detail['additional_operator_counts'] = {key:operator_counts[key]-before_counts[key] for key in before_counts}
        return detail, None
    corrected_point = proposal.candidate
    corrected_coordinate = proposal.augmented_step
    corrected_step = lift(corrected_coordinate)
    if not np.array_equal(corrected_point, parent_x+corrected_step):
        raise ValueError('Corrected candidate differs from the literal parent plus corrected T*z')
    # A remains the PARENT exact spectral residual-Hessian model.  Read A*z
    # directly once, so the reported prediction belongs to this actual z.
    corrected_model = operator.matvec(corrected_coordinate)
    detail['additional_cost']['corrected_model_matvec'] = 1
    corrected_slope = float(virtual_rhs@corrected_model)
    corrected_energy = float(corrected_model@corrected_model)
    corrected_change = 2*corrected_slope+corrected_energy
    corrected_prediction = old_merit+corrected_change
    error = None
    try:
        corrected_residual = problem.residual(corrected_point)
        detail['additional_cost']['corrected_nonlinear_residual'] = 1
        finite = bool(np.isfinite(corrected_residual).all())
        stats = statistics(corrected_point, corrected_residual) if finite else {}
    except (FloatingPointError, OverflowError) as exception:
        corrected_residual = None
        finite = False
        stats = {}
        error = repr(exception)
    merit = objective_value(stats) if finite else float('inf')
    feasible = (finite and stats['rho_sample_min']>0 and stats['min_relative_E']>0
                and stats['min_relative_determinant']>0)
    descent = merit<old_merit and (corrected_slope>=0
                or merit<=old_merit+2e-4*corrected_slope)
    curvature = None
    filter_result = None
    curvature_feasible = True
    if feasible and descent and (args.curvature_cap is not None or args.reach_ratio is not None):
        curvature = geometry(corrected_point)
        detail['additional_cost']['corrected_full_known_point_geometry'] = 1
        filter_result = curvature_filter(corrected_point, curvature)
        curvature_feasible = filter_result['passed']
    corrected_trial = dict(kind='parent_row_soc', original_ray_alpha=1.,
        corrected_direction_alpha=1., merit=merit, finite=finite, feasible=feasible,
        descent=descent, curvature_feasible=curvature_feasible,
        curvature_points=curvature, curvature_filter=filter_result, statistics=stats,
        arithmetic_error=error, half_objective_slope=corrected_slope,
        actual_objective_directional_derivative=2*corrected_slope,
        quadratic_predicted_actual_change=corrected_change,
        quadratic_predicted_actual_objective=corrected_prediction,
        model_direction_energy=corrected_energy,
        actual_to_same_corrected_step_predicted_decrease=(
            (old_merit-merit)/(old_merit-corrected_prediction)
            if old_merit-corrected_prediction>0 else None))
    if curvature is not None:
        remembered_curvature = []
        remembered_radius = []
        for location in (curvature.get('observation_grid_worst'), curvature.get('worst')):
            value = add_actual_location(location, witnesses)
            if value is not None:
                remembered_curvature.append(value)
        value = add_actual_location(curvature.get('maximum_radius_point'), radius_witnesses)
        if value is not None:
            remembered_radius.append(value)
        corrected_trial['new_permanent_curvature_locations'] = remembered_curvature
        corrected_trial['new_permanent_radius_locations'] = remembered_radius
    # Every corrected location is retained even when this attempt is rejected.
    detail['trial'] = corrected_trial
    raw_path = args.outdir/f'direction-{index:03d}-soc.npz'
    np.savez_compressed(raw_path, step=corrected_step, augmented_step=corrected_coordinate,
        soc_correction=proposal.correction, uncorrected_augmented_step=direction,
        integrated_scale=coordinates.scale, coarse_diagonal=coarse_diagonal,
        coarse_cholesky=coarse_chol)
    detail.update(direction_path=str(raw_path), direction_sha256=sha(raw_path),
        accepted=bool(feasible and descent and curvature_feasible),
        seconds=time.monotonic()-started_soc,
        additional_operator_counts={key:operator_counts[key]-before_counts[key] for key in before_counts})
    event_trial = dict(corrected_trial)
    event_trial['curvature_points'] = compact_geometry(curvature)
    event(event='complete_parent_row_soc_actual_trial', direction=index,
        accepted=detail['accepted'], **event_trial)
    if not detail['accepted']:
        return detail, None
    djet, dheight, _ = problem.unpack(corrected_step, tangent=True)
    integrated = coordinates.scale*coordinates.project(corrected_coordinate[:ni])
    state = dict(point=corrected_point, residual=corrected_residual, statistics=stats,
        curvature=curvature, curvature_filter=filter_result, merit=merit,
        coordinate_step=corrected_coordinate, step=corrected_step,
        half_objective_slope=corrected_slope,
        quadratic_predicted_actual_change=corrected_change,
        quadratic_predicted_actual_objective=corrected_prediction,
        coordinate_norm=float(np.linalg.norm(corrected_coordinate)),
        projected_endpoint_error=float(np.max(np.abs(coordinates.endpoint(integrated)))),
        nodal_jet_step_max_by_Y_U_A=np.max(np.abs(djet), axis=(0,2)).tolist(),
        height_step=float(dheight))
    detail['seconds'] = time.monotonic()-started_soc
    return detail, state
'''


SOC_HOOK = '''
if trial_index == 0 and alpha == 1. and feasible and descent and not curvature_feasible:
    record['soc_attempted'] = True
    soc_detail, soc_state = actual_parent_row_soc(index, x, coordinate_step, point,
        trial, active_rows, active_bounds, active_metadata, A, model_residual,
        old_merit, counts)
    record['soc'] = soc_detail
    record['outside_inner_calls']['soc'] = soc_detail['additional_cost']
    event(event='complete_parent_row_soc_returned', direction=index,
        accepted=soc_detail['accepted'],
        proposal_available=soc_detail['proposal']['proposal_available'],
        reason=soc_detail['proposal']['reason'], additional_cost=soc_detail['additional_cost'],
        additional_operator_counts=soc_detail['additional_operator_counts'])
    if soc_state is not None:
        saved_names = ('direction_sha256', 'coordinate_norm', 'projected_endpoint_error',
            'half_objective_slope', 'quadratic_predicted_actual_change',
            'quadratic_predicted_actual_objective', 'nodal_jet_step_max_by_Y_U_A',
            'height_step', 'maximum_selected_linear_product', 'selected_linear_products')
        record['uncorrected_direction_model'] = {key:record[key] for key in saved_names}
        record['accepted_update_kind'] = 'parent_row_soc'
        record['accepted_direction_is_main_QP_solution'] = False
        record['main_QP_diagnostics_remain_uncorrected'] = True
        record['direction_sha256'] = soc_detail['direction_sha256']
        record['direction_path'] = soc_detail['direction_path']
        for key in ('coordinate_norm', 'projected_endpoint_error', 'half_objective_slope',
                    'quadratic_predicted_actual_change', 'quadratic_predicted_actual_objective',
                    'nodal_jet_step_max_by_Y_U_A', 'height_step'):
            record[key] = soc_state[key]
        record['selected_linear_products'] = soc_detail['proposal']['corrected_physical_linear_products']
        record['maximum_selected_linear_product'] = max(record['selected_linear_products'], default=0.)
        point = soc_state['point']
        trial_residual = soc_state['residual']
        stats = soc_state['statistics']
        curvature = soc_state['curvature']
        filter_result = soc_state['curvature_filter']
        merit = soc_state['merit']
        coordinate_step = soc_state['coordinate_step']
        step = soc_state['step']
        slope = soc_state['half_objective_slope']
        predicted_change = soc_state['quadratic_predicted_actual_change']
        linear_merit = soc_state['quadratic_predicted_actual_objective']
        feasible = descent = curvature_feasible = True
    del soc_state
'''


class SOCTransform(ast.NodeTransformer):
    def __init__(self, model, lineage):
        self.model = model
        self.lineage = lineage
        self.counts = dict(arguments=0, paths=0, helper_load=0, report=0,
            model_record=0, actual_trial_function=0, hook=0,
            early_cleanup=0, final_cleanup=0, accepted_bundle=0,
            direction_damping=0, final_damping=0)

    def visit_Module(self, node):
        node = self.generic_visit(node)
        pos = 1 if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant) else 0
        node.body[pos:pos] = statements('import os\nSOC_LINEAGE = '+repr(self.lineage))
        return node

    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if node.name != 'main':
            return node
        new = []
        for st in node.body:
            if name_target(st, 'args') and isinstance(st.value, ast.Call) and isinstance(st.value.func, ast.Attribute) and st.value.func.attr == 'parse_args':
                new.extend(statements("parser.add_argument('--soc-source',type=Path,required=True)\nparser.add_argument('--soc-tau',type=float,required=True)"))
                new.append(st)
                new.extend(statements("if not (os.environ.get('GITHUB_ACTIONS','').lower() == 'true' and os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public'):\n    raise RuntimeError('SOC scientific driver requires the public repository Actions')\nif not np.isfinite(args.soc_tau) or args.soc_tau < 0:\n    raise ValueError('SOC tau must be an explicit finite nonnegative algorithm parameter')"))
                self.counts['arguments'] += 1
                continue
            if name_target(st, 'helper') and isinstance(st.value, ast.Call) and isinstance(st.value.func, ast.Name) and st.value.func.id == 'load':
                new.extend(statements("if sha(paths['soc']) != "+repr(HELPER_SHA)+":\n    raise ValueError('The declared SOC helper identity changed')\nsoc_module=load('complete_parent_row_SOC',paths['soc'])\nsoc_module.require_actions()"))
                self.counts['helper_load'] += 1
            if name_target(st, 'residual') and same(st.value, ast.parse('problem.residual(x)',mode='eval').body):
                code = ACTUAL_TRIAL_FUNCTION.replace('SOC_MODEL_DEFINITION',
                    'None' if self.model == 'original' else 'context.definition()')
                new.extend(statements(code))
                self.counts['actual_trial_function'] += 1
            if (isinstance(st, ast.Assign) and len(st.targets) == 1
                    and same(st.targets[0], ast.parse("report['complete'] = True").body[0].targets[0])):
                new.extend(statements("report['final_damping']=damping"))
                self.counts['final_damping'] += 1
            new.append(st)
        node.body = new
        return node

    def visit_Assign(self, node):
        node = self.generic_visit(node)
        if name_target(node, 'paths') and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'dict':
            node.value.keywords.append(ast.keyword(arg='soc', value=ast.parse('args.soc_source',mode='eval').body))
            self.counts['paths'] += 1
        if name_target(node, 'report') and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'dict':
            for kw in node.value.keywords:
                if kw.arg == 'schema':
                    kw.value = ast.Constant('fullclosed-gauss-'+self.model+'-parent-row-SOC-v1')
            node.value.keywords.extend([
                ast.keyword(arg='soc_derivation', value=ast.Name(id='SOC_LINEAGE',ctx=ast.Load())),
                ast.keyword(arg='parent_row_soc', value=ast.parse(
                    "dict(enabled=True,tau=args.soc_tau,max_attempts_per_direction=1,"
                    "trigger='First full step passes true Phi/domain but fails full true known-point geometry',"
                    "helper_sha256="+repr(HELPER_SHA)+","
                    "corrected_model_used_for_acceptance_and_damping=True,"
                    "cubic_tau_is_algorithm_parameter_not_proven_threshold=True,"
                    "QP_module_or_preconditioner_changed_by_SOC=False)",mode='eval').body)])
            self.counts['report'] += 1
        if name_target(node, 'record') and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'dict':
            keys = {k.arg for k in node.value.keywords}
            if {'index','damping','active_geometry','qp'} <= keys:
                node.value.keywords.extend([
                    ast.keyword(arg='soc_attempted',value=ast.Constant(False)),
                    ast.keyword(arg='accepted_update_kind',value=ast.Constant('original_ray')),
                    ast.keyword(arg='accepted_direction_is_main_QP_solution',value=ast.Constant(True))])
                self.counts['model_record'] += 1
        return node

    def visit_Delete(self, node):
        names = [n.id for n in node.targets if isinstance(n, ast.Name)]
        if names == ['model_step','A','model_residual','djet','integrated_point','coordinate_step','active_rows','active_bounds']:
            node.targets = [ast.Name(id=n,ctx=ast.Del()) for n in ('djet','integrated_point')]
            self.counts['early_cleanup'] += 1
        elif names == ['step','bridge']:
            node.targets = [ast.Name(id=n,ctx=ast.Del()) for n in
                ('step','bridge','model_step','A','model_residual','coordinate_step','active_rows','active_bounds')]
            self.counts['final_cleanup'] += 1
        return node

    def visit_For(self, node):
        node = self.generic_visit(node)
        if isinstance(node.target, ast.Name) and node.target.id == 'trial_index':
            body = []
            target = ast.parse('feasible and descent and curvature_feasible',mode='eval').body
            for st in node.body:
                if isinstance(st, ast.If) and same(st.test,target):
                    body.extend(statements(SOC_HOOK))
                    self.counts['hook'] += 1
                    accepted = []
                    for inner in st.body:
                        accepted.append(inner)
                        if (isinstance(inner, ast.Expr) and isinstance(inner.value, ast.Call)
                                and isinstance(inner.value.func, ast.Attribute)
                                and isinstance(inner.value.func.value, ast.Name)
                                and inner.value.func.value.id == 'record' and inner.value.func.attr == 'update'
                                and any(k.arg == 'accepted_bundle_sha256' for k in inner.value.keywords)):
                            accepted.extend(statements("report['current_bundle_sha256']=record['accepted_bundle_sha256']"))
                            self.counts['accepted_bundle'] += 1
                    st.body = accepted
                body.append(st)
            node.body = body
        if isinstance(node.target, ast.Name) and node.target.id == 'index':
            body = []
            for st in node.body:
                if (isinstance(st, ast.Assign) and len(st.targets) == 1
                        and same(st.targets[0], ast.parse("record['seconds'] = 0").body[0].targets[0])):
                    body.extend(statements("record['damping_after_direction']=damping"))
                    self.counts['direction_damping'] += 1
                body.append(st)
            node.body = body
        return node


def build_ast(base, manifest_source):
    base = Path(base)
    model = next((model for model, (_, digest) in BASES.items() if sha(base) == digest), None)
    if model is None:
        raise ValueError('SOC derivation needs an exact frozen original or R671 driver')
    if sha(manifest_source) != MANIFEST_SHA:
        raise ValueError('SOC derivation needs the exact published complete-location transform')
    manifest = load(manifest_source)
    tree = ast.parse(base.read_text(), filename=str(base))
    exact = manifest.ExactLocationDriver()
    tree = exact.visit(tree)
    edits = dict(removed_arbitrary_size_checks=exact.removed_size_checks,
        exact_binary_key_replacements=exact.exact_key_replacements,
        pure_location_schema_insertions=exact.position_schema_insertions)
    if edits != dict(removed_arbitrary_size_checks=1, exact_binary_key_replacements=6,
                     pure_location_schema_insertions=1):
        raise ValueError('The frozen manifest edit sites changed')
    lineage = dict(schema=LINEAGE_SCHEMA, model=model,
        frozen_driver_sha256=sha(base), derivation_source_sha256=sha(__file__),
        manifest_derivation_sha256=MANIFEST_SHA, helper_sha256=HELPER_SHA,
        exact_location_changes=edits,
        main_QP_and_step_norm_changed=False, all_known_points_retained=True,
        one_SOC_only_after_full_true_geometry_rejection=True,
        corrected_direction_model_controls_acceptance_and_damping=True)
    transform = SOCTransform(model,lineage)
    tree = ast.fix_missing_locations(transform.visit(tree))
    if any(count != 1 for count in transform.counts.values()):
        raise ValueError('SOC frozen edit sites did not each match exactly once: '+repr(transform.counts))
    compile(tree,str(base)+'-SOC-derived','exec')
    return tree, lineage, transform.counts


def derive_driver(base, destination, manifest_source):
    tree, lineage, counts = build_ast(base, manifest_source)
    provenance = dict(**lineage, frozen_driver_path=str(Path(base).resolve()),
                      manifest_derivation_path=str(Path(manifest_source).resolve()), edit_sites=counts)
    text = ('#!/usr/bin/env python3\n# Complete parent-row SOC source derivation:\n# '
            +json.dumps(provenance,sort_keys=True)+'\n'+ast.unparse(tree)+'\n')
    destination = Path(destination)
    if destination.exists() and destination.read_text() != text:
        raise FileExistsError('Use a fresh SOC driver destination for new bytes')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text)
    return dict(path=str(destination.resolve()), sha256=sha(destination),
                bytes=destination.stat().st_size, derivation=provenance)


def bind_soc_parent(report, supplied, source_dir, manifest_source):
    """Strict future SOC-parent source binding, no arrays or driver execution."""
    path = Path(supplied).resolve()
    if report.get('source_sha256') != sha(path):
        raise ValueError('SOC report does not name the actual supplied parent source bytes')
    lineage = report.get('soc_derivation')
    if (not isinstance(lineage,dict) or lineage.get('schema') != LINEAGE_SCHEMA
            or lineage.get('derivation_source_sha256') != sha(__file__)
            or lineage.get('helper_sha256') != HELPER_SHA
            or report.get('source_sha256_by_role',{}).get('soc') != HELPER_SHA):
        raise ValueError('Unknown SOC parent derivation or helper identity')
    model = lineage.get('model')
    if model not in BASES:
        raise ValueError('Unknown SOC parent model')
    base = Path(source_dir)/BASES[model][0]
    expected, expected_lineage, counts = build_ast(base, manifest_source)
    actual = ast.parse(path.read_text(), filename=str(path))
    if lineage != expected_lineage or not same(expected,actual):
        raise ValueError('Actual SOC parent body differs from the entire exact declared derivation')
    if report.get('schema') != 'fullclosed-gauss-'+model+'-parent-row-SOC-v1':
        raise ValueError('SOC report schema differs from its bound complete body')
    return dict(path=str(path), sha256=sha(path), model=model,
        declared_derivation=expected_lineage, actual_entire_body_AST_matched=True,
        inherited_original_parent_guard_bypassed=False, edit_sites=counts)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base', type=Path, required=True)
    p.add_argument('--manifest-source', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    print(json.dumps(derive_driver(a.base,a.out,a.manifest_source),indent=2))


if __name__ == '__main__':
    main()

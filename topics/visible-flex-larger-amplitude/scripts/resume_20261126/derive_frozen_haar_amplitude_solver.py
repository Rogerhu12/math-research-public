#!/usr/bin/env python3
"""Pure source/AST derivation of the complete fixed true-material-Haar solver.

This script reads only published Python source bytes. It never imports a
scientific kernel, loads a numerical candidate, or executes a field/J/QP.
The independent derived sources run scientific work only in public Actions.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

BASE_DRIVER_SHA = '859ceb836378c3140a0d27877987f3d06546aae2baee0ef316403d3f332d911b'
BASE_LAUNCHER_SHA = 'd73ec177827fd420153dd95ceafbc3601eeb0af6e3b0c89b7b2d372c021e41e1'
BASE_READER_SHA = 'f119d9960a0e6de381b6a7ab93581a1dd785db258a6b7cd2a72546ea62c979af'
BASE_COARSE_SHA = 'a531818d75040ff571ad1249eecb3c18f7341284d1cdd86d2032b0f8f4ef9f63'
HAAR_TARGET_SHA = 'c5a717dbca55311060207672c703293403c16c6e5142b84cc522e660afc67a64'
MOMENTS_SHA = '1d12d238cd1a034cc1261ea7f23b7c223693a3cbdd769d66c376e796b0770010'
R671_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path, expected):
    data = Path(path).read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('Changed complete derivation input: '+str(path))
    return data.decode()


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Need exactly one stated source node: '+old[:140])
    return text.replace(old, new)


def function(tree, name):
    values = [node for node in ast.walk(tree)
              if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name]
    if len(values) != 1:
        raise ValueError('Need one complete function '+name)
    return values[0]


def same_ast(a, b):
    return ast.dump(a, include_attributes=False) == ast.dump(b, include_attributes=False)


def module_constant(tree, name, value):
    nodes = [node for node in tree.body if isinstance(node, ast.Assign)
             and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)]
    if len(nodes) != 1:
        raise ValueError('Need one declared source constant '+name)
    nodes[0].value = ast.parse(repr(value), mode='eval').body


def insert_derivation(tree, value):
    tree.body.insert(1, ast.parse('HAAR_SOURCE_DERIVATION = '+repr(value)).body[0])


def clean_and_write(path, tree):
    ast.fix_missing_locations(tree)
    text = '#!/usr/bin/env python3\n'+ast.unparse(tree).strip()+'\n'
    check = ast.parse(text)
    compile(check, str(path), 'exec')
    for node in ast.walk(check):
        if isinstance(node, ast.Dict):
            keys = [key.value for key in node.keys if isinstance(key, ast.Constant)]
            if len(keys) != len(set(keys)):
                raise ValueError('Duplicate literal dictionary key')
        if isinstance(node, ast.Call):
            keys = [key.arg for key in node.keywords if key.arg is not None]
            if len(keys) != len(set(keys)):
                raise ValueError('Duplicate literal call keyword')
    Path(path).write_text(text)
    return dict(path=str(Path(path).resolve()), bytes=len(text.encode()), sha256=sha(path))


def derive_coarse(path, out):
    source = read(path, BASE_COARSE_SHA)
    original = ast.parse(source)
    source = replace_once(source,
        'fixed_target_full_angles=int(frozen.target.full_angles),current_full_angles=int(o.full_N),',
        "fixed_target_full_angles=None,exact_material_Haar=True,\n"
        "        working_moment_full_angles=int(frozen.target.working_moment_full_angles),\n"
        "        working_moment_carrier=frozen.target.working_moment_carrier,\n"
        "        angular_identity_sha256=frozen.target.manifest['angular_identity_sha256'],\n"
        "        target_quadrature_nodes_define_metric=False,\n"
        "        source_derivation=HAAR_SOURCE_DERIVATION,current_full_angles=int(o.full_N),")
    tree = ast.parse(source)
    tree.body[0].value = ast.Constant(value='''Complete coarse Gram for ONE frozen accurate material-Haar target.

The complete numerical K00 contraction is the full a531 fixed-target
algorithm, with every residual mean. Its actual wrapper source is now
FrozenHaarOperator. The target is an exact full-circle integral; the
moment carrier Q is working accuracy, never a finite target definition.
Current R671 physics, all outer J/J*, H2 norm, all original rows and the
unchanged v5/v3 preconditioner semantics remain. No science runs on import.
''')
    module_constant(tree, 'SCHEMA', 'true-material-Haar-fixed-target-complete-coarse-Gram-v1')
    module_constant(tree, 'FROZEN_TRANSFORM_SHA256', HAAR_TARGET_SHA)
    derivation = dict(schema='R691-independent-complete-Haar-fixed-coarse-source-v1',
        complete_fixed_coarse_parent_sha256=BASE_COARSE_SHA,
        actual_Haar_target_source_sha256=HAAR_TARGET_SHA,
        original_R671_physical_factory_sha256=R671_SHA,
        complete_K00_numeric_contraction_unchanged=True,
        all_original_mean_rows_retained=True,
        accurate_integral_target_not_discrete_quadrature=True,
        no_scientific_evaluation_by_deriver=True)
    insert_derivation(tree, derivation)
    for name in ('prepare_current_frozen_preconditioner', '_zero_core_contract',
                 '_frozen_source', '_helpers'):
        if not same_ast(function(original, name), function(tree, name)):
            raise AssertionError('Unintended complete preconditioner/source behavior change: '+name)
    old_loop = [node for node in function(original, 'assemble_current_coarse_gram').body
                if isinstance(node, ast.For) and isinstance(node.target, ast.Name) and node.target.id == 'start']
    new_loop = [node for node in function(tree, 'assemble_current_coarse_gram').body
                if isinstance(node, ast.For) and isinstance(node.target, ast.Name) and node.target.id == 'start']
    if len(old_loop) != 1 or len(new_loop) != 1 or not same_ast(old_loop[0], new_loop[0]):
        raise AssertionError('The complete K00 numeric contraction must be unchanged')
    record = clean_and_write(out, tree)
    record.update(full_numeric_K00_loop_AST_equal=True,
        preconditioner_and_source_guard_function_AST_equal=True,
        source_guard_constant_changes_to_actual_Haar_bytes=True)
    return record


def derive_driver(path, out, coarse_sha):
    source = read(path, BASE_DRIVER_SHA)
    original = ast.parse(source)
    source = replace_once(source,
        "parser.add_argument('--frozen-target-manifest', type=Path, required=True)",
        "parser.add_argument('--frozen-target-manifest', type=Path, required=True)\n"
        "    parser.add_argument('--target-moments', type=Path)\n"
        "    parser.add_argument('--target-source-overrides', type=Path)")
    source = replace_once(source,
        "frozen_coarse=args.frozen_coarse_source or topic / 'scripts/resume_20261126/frozen_metric_coarse_moments.py'",
        "frozen_coarse=args.frozen_coarse_source or topic / 'scripts/resume_20261126/frozen_material_haar_coarse_moments.py'")
    source = replace_once(source,
        "fixed_frame, fixed_moments, centered_loss, objective_key, fixed_source_binding = fixed_sources(args, paths)",
        "fixed_frame, fixed_moments, centered_loss, objective_key, fixed_source_binding = fixed_sources(args, paths)\n"
        "    if args.tail_lambda != 1.0 or args.tail_parent_lambda not in (None, 1.0) or args.tail_migration != 'keep-q':\n"
        "        raise ValueError('This complete Haar branch preserves the actual lambda-one R671 field and keep-q coordinates')")
    source = replace_once(source,
        "target = frozen_module.FrozenMeanMetricTarget(args.frozen_target_manifest, repo=repo, input_overrides=target_overrides, stage_block=args.stage_block)",
        "target_source_overrides = None if args.target_source_overrides is None else json.loads(args.target_source_overrides.read_text())\n"
        "    target = frozen_module.FrozenHaarTarget(args.frozen_target_manifest, repo=repo, input_overrides=target_overrides, source_overrides=target_source_overrides, moment_carrier=args.target_moments, stage_block=args.stage_block)\n"
        "    if target.manifest['canonical_model']['source_sha256'] != FIXED_EXPECTED_SOURCES['exact_tail']:\n"
        "        raise ValueError('This first complete Haar solver retains the true R671 physical model; it does not relabel a deep model')")
    source = replace_once(source,
        'problem = frozen_module.FrozenMetricOperator(field_problem, target, stage_block=args.stage_block)',
        'problem = frozen_module.FrozenHaarOperator(field_problem, target, stage_block=args.stage_block)')
    old = """        parent_design = parent_report.get('mean_metric_design') or {}
        same_frozen = parent_target.get('target_identity_sha256') == target.identity
        freeze_member = parent_report.get('final_bundle_sha256') == target.manifest['inputs']['bundle']['sha256'] and parent_design.get('averaging') == target.averaging and (parent_design.get('finite_angles') == target.full_angles)
        if not same_frozen and (not freeze_member):
            raise ValueError('The comparison parent does not describe this SAME frozen metric')"""
    new = """        same_frozen = parent_target.get('target_identity_sha256') == target.identity
        freeze_member = parent_report.get('final_bundle_sha256') == target.manifest['inputs']['bundle']['sha256']
        if not same_frozen or parent_target.get('exact_material_Haar') is not True:
            raise ValueError('Stored old physical-mean or scalar Phi is not a Haar parent comparison; this new target rereads the full initial field')
        if parent_target.get('working_moment_carrier', {}).get('sha256') != target.working_moment_carrier['sha256']:
            raise ValueError('A stored parent Phi comparison needs the same working moments; otherwise reread the parent under the new accurate carrier')"""
    source = replace_once(source, old, new)
    source = replace_once(source,
        "metric_target_mode='one fixed frozen rotational mean metric'",
        "metric_target_mode='one fixed exact full-circle material-Haar metric'")
    source = replace_once(source,
        "schema='complete-fixed-frozen-target-with-held-amplitude-budgets-v1'",
        "schema='complete-fixed-true-material-Haar-with-held-amplitude-budgets-v1'")
    source = replace_once(source,
        "objective_change='ONE frozen target identity is preserved. Only Phi with identical p/epsilon/scale and identical observation measure can be subtracted; compare refinements on a common declared measure, and keep the target formula and N_star unchanged'",
        "objective_change='A NEW exact full-circle material-Haar metric is fixed before this branch. Its actual full initial field is reread. No previous physical-mean or fixed-scalar Phi is reused. Later same-target comparisons retain identical p/epsilon/scale, observation measure and working moments; Q/p of the moments never define a discrete target'")
    marker = "    report['amplitude_design_constraints'] = dict("
    addition = """    report['haar_target_contract'] = dict(schema='R691-complete-fixed-Haar-full-solver-contract-v1', source_derivation=HAAR_SOURCE_DERIVATION, target_identity_sha256=target.identity, angular_identity_sha256=target.manifest['angular_identity_sha256'], target_sources=target.manifest['sources'], working_moment_carrier=target.working_moment_carrier, working_moment_full_angles=target.working_moment_full_angles, exact_full_circle_material_integral=True, working_quadrature_is_target_definition=False, original_physical_R671_model_preserved=True, current_scalar_constraints_and_geometry_preserved=True, old_target_Phi_improvement_claimed=False, all_original_variables_mean_rows_and_H2_norm_retained=True, all_original_geometry_and_both_amplitude_branches_retained=True, continuous_metric_or_geometry_certified=False, actual_target_refinement_convergence_certified=False)
    report['frozen_metric_target'].update(exact_material_Haar=True, angular_identity_sha256=target.manifest['angular_identity_sha256'], working_moment_carrier=target.working_moment_carrier, working_moment_full_angles=target.working_moment_full_angles, finite_quadrature_nodes_define_target=False, source_sha256=sha(paths['frozen_target']))
"""
    source = replace_once(source, marker, addition+marker)
    source = replace_once(source,
        "schema='R684-fixed-frozen-target-field-v1'",
        "schema='R691-fixed-true-material-Haar-target-field-v1'")
    source = replace_once(source,
        "frozen_full_angles=target.full_angles, final_metric_frozen=True, source_commit=source_commit",
        "frozen_full_angles=None, exact_material_Haar=True, angular_identity_sha256=target.manifest['angular_identity_sha256'], working_moment_carrier_sha256=target.working_moment_carrier['sha256'], working_moment_full_angles=target.working_moment_full_angles, finite_quadrature_nodes_define_target=False, final_metric_frozen=True, source_commit=source_commit")
    source = replace_once(source,
        "report['limitations'] += ' The additional fixed Dmarked/L/Hmin inequalities",
        "report['limitations'] += ' The Haar target is the exact full-circle integral of its immutable original field. Working angular moment intervals enclose that target; their numerical midpoint use and radial/scalar arithmetic still need full outward payment. The prior physical-mean or scalar objective is not this target. The additional fixed Dmarked/L/Hmin inequalities")
    tree = ast.parse(source)
    tree.body[0].value = ast.Constant(value='''Complete all-variable QP for ONE fixed accurate material-Haar metric.

The full scalar/closed R671 physical model, all original rows and means,
H2-type mother norm, complete geometric inequalities, both marked-amplitude
witness branches, and permanent point history are retained from the full
859c solver. FrozenHaarTarget evaluates ONE full continuous frozen field;
Q/p of its accurate angular moments are working accuracy only. J/J* is
complete original physical differentiation followed by fixed positive
target scaling. There is no moving mean projection or old-Phi comparison.

The complete K00 preconditioner is the separately source-bound accurate-
Haar copy of a531. Actual physical residual, complete six-jet geometry and
both amplitude screens are reread during every potentially accepted trial.
A finite numerical solve is not a continuous certificate or convergence proof.
''')
    old_sources = [node for node in tree.body if isinstance(node, ast.Assign)
                   and any(isinstance(target, ast.Name) and target.id == 'FIXED_EXPECTED_SOURCES'
                           for target in node.targets)]
    expected = ast.literal_eval(old_sources[0].value)
    expected.update(frozen_target=HAAR_TARGET_SHA, frozen_coarse=coarse_sha, exact_tail=R671_SHA)
    module_constant(tree, 'FIXED_EXPECTED_SOURCES', expected)
    derivation = dict(schema='R691-independent-complete-fixed-Haar-amplitude-driver-v1',
        complete_fixed_target_amplitude_parent_sha256=BASE_DRIVER_SHA,
        complete_fixed_target_coarse_parent_sha256=BASE_COARSE_SHA,
        actual_frozen_Haar_target_sha256=HAAR_TARGET_SHA,
        actual_Haar_moment_source_sha256=MOMENTS_SHA,
        actual_Haar_coarse_source_sha256=coarse_sha,
        preserved_physical_R671_factory_sha256=R671_SHA,
        full_QP_direction_loop_AST_unchanged=True,
        complete_scalar_geometry_amplitude_memory_and_H2_norm_preserved=True,
        all_original_residual_mean_rows_retained=True,
        old_target_objective_values_not_reused=True,
        no_scientific_evaluation_by_deriver=True)
    insert_derivation(tree, derivation)
    preserved = ('point_geometry', 'load_witnesses', 'coarse_lift', 'coarse_transpose',
        'lift', 'transpose', 'objective_value', 'curvature_filter', 'geometry',
        'add_actual_location', 'remember_amplitude', 'compact_geometry')
    for name in preserved:
        if not same_ast(function(original, name), function(tree, name)):
            raise AssertionError('Unintended full physical/coordinate behavior change: '+name)
    old_loops = [node for node in function(original, 'main').body
                 if isinstance(node, ast.For) and isinstance(node.target, ast.Name) and node.target.id == 'index']
    new_loops = [node for node in function(tree, 'main').body
                 if isinstance(node, ast.For) and isinstance(node.target, ast.Name) and node.target.id == 'index']
    if len(old_loops) != 1 or len(new_loops) != 1 or not same_ast(old_loops[0], new_loops[0]):
        raise AssertionError('The complete QP/full trial/memory loop must remain byte-independent AST equal')
    record = clean_and_write(out, tree)
    record.update(full_QP_and_trial_loop_AST_equal=True,
        complete_preserved_function_AST_names=list(preserved),
        full_original_variables_and_rows_preserved=True,
        driver_scientific_execution=False)
    return record


def derive_launcher(path, out, driver_sha, coarse_sha):
    source = read(path, BASE_LAUNCHER_SHA)
    original = ast.parse(source)
    for old, new in (
        ("source/'fullclosed_frozen_metric_amplitude_qp.py'", "source/'fullclosed_frozen_haar_amplitude_qp.py'"),
        ("source/'frozen_mean_metric.py'", "source/'frozen_material_haar_metric.py'"),
        ("source/'frozen_metric_coarse_moments.py'", "source/'frozen_material_haar_coarse_moments.py'"),
        ("(driver,'"+BASE_DRIVER_SHA+"')", "(driver,'"+driver_sha+"')"),
        ("schema='complete-fixed-frozen-target-with-amplitude-command-v1'",
         "schema='complete-fixed-true-material-Haar-with-amplitude-command-v1'")):
        source = replace_once(source, old, new)
    source = replace_once(source,
        "    parser.add_argument('--frozen-target-source',type=Path)",
        "    parser.add_argument('--frozen-target-source',type=Path)\n"
        "    parser.add_argument('--target-moments',type=Path)\n"
        "    parser.add_argument('--target-source-overrides',type=Path)")
    source = replace_once(source,
        "    if (not 0<args.lambda_value<=1 or args.eta_start_node<1 or args.angles<4 or args.angles%4",
        "    if (args.lambda_value!=1 or args.eta_start_node<1 or args.angles<4 or args.angles%4")
    source = replace_once(source,
        "    prepared=subprocess.run(prepare,text=True,capture_output=True,check=True)",
        "    prepared=subprocess.run(prepare,text=True,capture_output=True,check=False)\n"
        "    if prepared.returncode:\n"
        "        if prepared.stdout:print(prepared.stdout,flush=True)\n"
        "        if prepared.stderr:print(prepared.stderr,file=sys.stderr,flush=True)\n"
        "        raise subprocess.CalledProcessError(prepared.returncode,prepare,\n"
        "            output=prepared.stdout,stderr=prepared.stderr)")
    source = replace_once(source,
        "    for key in ('comparison_parent_report','comparison_parent_carrier'):",
        "    for key in ('target_moments','target_source_overrides'):\n"
        "        value=getattr(args,key)\n"
        "        if value is not None:command.extend(['--'+key.replace('_','-'),str(value.resolve())])\n"
        "    for key in ('comparison_parent_report','comparison_parent_carrier'):")
    source = replace_once(source,
        "    for path,digest in ((driver,'"+driver_sha+"'),",
        "    for path,digest in ((driver,'"+driver_sha+"'),\n"
        "            (frozen,'"+HAAR_TARGET_SHA+"'),(moments,'"+coarse_sha+"'),")
    source = replace_once(source,
        "    target=target_module.read_manifest(args.frozen_target_manifest)",
        """    target=target_module.read_manifest(args.frozen_target_manifest)
    if (target['canonical_model'].get('schema')!='R671-exact-reference-tail-lift-v1'
            or target['canonical_model'].get('source_sha256')!=R671_FACTORY_SHA
            or target['canonical_model'].get('lambda_value')!=1
            or target['sources']['evaluator']['sha256']!=HAAR_TARGET_SHA):
        raise ValueError('This complete Haar solver retains the actual R671 lambda-one physical model')
    input_overrides={key:getattr(args,'target_'+key) for key in target_module.INPUT_ROLES}
    source_overrides={} if args.target_source_overrides is None else json.loads(args.target_source_overrides.read_text())
    if set(source_overrides)-set(target['sources']):
        raise ValueError('Unknown actual target source override role')
    target_inputs={key:target_module.resolve(target['inputs'][key],repo,input_overrides[key])
        for key in target_module.INPUT_ROLES}
    target_sources={key:target_module.resolve(value,repo,source_overrides.get(key))
        for key,value in target['sources'].items()}
    selected_moments=(args.target_moments.resolve() if args.target_moments is not None
        else target_module.resolve(target['working_moments'],repo))
    working=json.loads(selected_moments.read_text())
    if (working.get('schema')!='R691-true-material-Haar-angular-moments-v1'
            or working.get('complete') is not True
            or working.get('source',{}).get('sha256')!=HAAR_MOMENTS_SHA
            or working.get('source_bundle',{}).get('sha256')!=target['inputs']['bundle']['sha256']
            or working.get('angular_identity_sha256')!=target['angular_identity_sha256']
            or working.get('definition')!=target['angular_definition']
            or working.get('positivity',{}).get('positive_rho_certified') is not True):
        raise ValueError('Need complete same-frozen-field accurate working moments, never a different target')
    working_moment_record=target_module.record(selected_moments,repo)
    working_Q=working['quadrature_work']['full_angles']
    freeze_member=False
    same_Haar_parent=False""")
    source = replace_once(source,
        "        if parent.get('frozen_metric_target',{}).get('target_identity_sha256',target['target_identity_sha256'])!=target['target_identity_sha256']:\n"
        "            raise ValueError('A fixed-target continuation cannot change its frozen metric identity')",
        """        if parent.get('complete') is not True or parent.get('final_bundle_sha256')!=sha(args.bundle):
            raise ValueError('Use the actual completed parent and its byte-identical final bundle')
        freeze_member=sha(args.bundle)==target['inputs']['bundle']['sha256']
        parent_target=parent.get('frozen_metric_target') or {}
        same_Haar_parent=(parent_target.get('target_identity_sha256')==target['target_identity_sha256']
            and parent_target.get('exact_material_Haar') is True)
        if not (freeze_member or same_Haar_parent):
            raise ValueError('Initialize at the actual frozen member or continue this same exact Haar target')
        if not same_Haar_parent and args.comparison_parent_report is not None:
            raise ValueError('The first NEW Haar target must reread its initial field, not reuse an old Phi')""")
    source = replace_once(source,
        "    files.add(helper_path if args.parent_report is not None else old/'refine_fixed_g_fullclosed.py')",
        "    files.update(target_inputs.values())\n"
        "    files.update(target_sources.values())\n"
        "    files.add(selected_moments)\n"
        "    files.add(helper_path if args.parent_report is not None else old/'refine_fixed_g_fullclosed.py')")
    source = replace_once(source,
        "        '--comparison-parent-report','--comparison-parent-carrier','--amplitude-budget-evidence'}",
        "        '--comparison-parent-report','--comparison-parent-carrier','--amplitude-budget-evidence',\n"
        "        '--target-moments','--target-source-overrides'}")
    source = replace_once(source,
        "        target_angles=target['full_angles'],current_angles=args.angles,",
        """        target_angles=None,current_angles=args.angles,
        accurate_material_Haar=True,angular_identity_sha256=target['angular_identity_sha256'],
        working_moment_carrier=working_moment_record,working_moment_full_angles=working_Q,
        working_quadrature_is_target_definition=False,
        actual_parent_is_frozen_member=freeze_member,same_exact_Haar_parent=same_Haar_parent,
        new_explicit_target_initialization=not same_Haar_parent,
        old_parent_Phi_reused=False,old_target_Phi_improvement_claimed=False,
        source_derivation=HAAR_SOURCE_DERIVATION,""")
    source = replace_once(source,
        "        scope='Complete same-frozen-target solve; finite budget alone does not certify refinement convergence')",
        "        scope='Complete fixed exact material-Haar solve with all means, H2, original rows and held-amplitude constraints; reread full initial field, no old-target Phi subtraction; a finite budget is not a refinement or geometry certificate')")
    tree = ast.parse(source)
    tree.body[0].value = ast.Constant(value='''Launch the complete all-variable fixed accurate material-Haar QP in Actions.

The mathematical target is the full continuous frozen integral. Working
angular moment Q/p are not its definition. The first explicit new target
rereads the full actual frozen member; old physical-mean/scalar Phi is not
reused. A later parent must carry this same actual Haar target identity.
Every old permanent position, original row, H2 norm and both amplitude
branches are retained. Actual R671 lambda-one physics is unchanged.
''')
    tree.body[1:1] = ast.parse(
        'R671_FACTORY_SHA = '+repr(R671_SHA)+'\n'
        'HAAR_TARGET_SHA = '+repr(HAAR_TARGET_SHA)+'\n'
        'HAAR_MOMENTS_SHA = '+repr(MOMENTS_SHA)+'\n').body
    insert_derivation(tree, dict(schema='R691-independent-complete-Haar-amplitude-launcher-v1',
        complete_fixed_target_launcher_parent_sha256=BASE_LAUNCHER_SHA,
        complete_driver_sha256=driver_sha,complete_coarse_sha256=coarse_sha,
        accurate_target_source_sha256=HAAR_TARGET_SHA,accurate_moment_source_sha256=MOMENTS_SHA,
        original_complete_parent_history_sources_preserved=True,
        R676_transfer_positions_AST_unchanged=True,
        scientific_execution_by_deriver=False))
    if not same_ast(function(original,'transfer_positions'),function(tree,'transfer_positions')):
        raise AssertionError('Keep the complete real R676 transferred-position initializer')
    record=clean_and_write(out,tree)
    record.update(R676_transfer_positions_AST_equal=True,
        complete_history_collector_sources_unchanged=True,
        scientific_execution=False)
    return record


def derive_reader(path,out,driver_sha,coarse_sha):
    source=read(path,BASE_READER_SHA)
    original=ast.parse(source)
    source=replace_once(source,"    binding={}",
        "    accurate=validate_accurate_Haar_report(r)\n    binding={}")
    source=replace_once(source,
        "schema='complete-fixed-target-held-amplitude-actual-summary-v1'",
        "schema='complete-fixed-true-material-Haar-held-amplitude-actual-summary-v1'")
    source=replace_once(source,
        "        target_full_angles=r['frozen_metric_target']['frozen_full_angles'],",
        """        target_full_angles=None,accurate_material_Haar=True,
        angular_identity_sha256=accurate['angular_identity_sha256'],
        working_moment_carrier=accurate['working_moment_carrier'],
        working_moment_full_angles=accurate['working_moment_full_angles'],
        working_quadrature_is_target_definition=False,
        old_target_Phi_improvement_claimed=False,
        source_derivation=HAAR_SOURCE_DERIVATION,""")
    helper=ast.parse('''
def validate_accurate_Haar_report(r):
    value=r['haar_target_contract']
    target=r['frozen_metric_target']
    if (value.get('schema')!='R691-complete-fixed-Haar-full-solver-contract-v1'
            or value.get('exact_full_circle_material_integral') is not True
            or value.get('working_quadrature_is_target_definition') is not False
            or value.get('old_target_Phi_improvement_claimed') is not False
            or value.get('all_original_variables_mean_rows_and_H2_norm_retained') is not True
            or value.get('all_original_geometry_and_both_amplitude_branches_retained') is not True
            or value.get('original_physical_R671_model_preserved') is not True
            or value.get('current_scalar_constraints_and_geometry_preserved') is not True
            or target.get('averaging')!='exact-material-Haar'
            or target.get('exact_material_Haar') is not True
            or target.get('frozen_full_angles') is not None
            or target.get('finite_quadrature_nodes_define_target') is not False
            or target.get('all_original_mean_constraints_retained') is not True
            or target.get('moving_mean_projection') is not False
            or target.get('target_mean_recomputed_from_current_field') is not False
            or target.get('target_identity_sha256')!=value['target_identity_sha256']
            or target.get('angular_identity_sha256')!=value['angular_identity_sha256']
            or target.get('working_moment_carrier')!=value['working_moment_carrier']
            or target.get('working_moment_full_angles')!=value['working_moment_full_angles']):
        raise ValueError('The actual solve must retain one complete exact Haar target and all original rows')
    if (value['target_sources']['evaluator']['sha256']!=HAAR_TARGET_SHA
            or value['target_sources']['moments']['sha256']!=HAAR_MOMENTS_SHA
            or value['target_sources']['factory']['sha256']!=R671_FACTORY_SHA
            or r['source_sha256_by_role']['exact_tail']!=R671_FACTORY_SHA
            or r['exact_tail_lambda']!=1):
        raise ValueError('Do not relabel a finite-target or another physical-model report as accurate Haar')
    stats=[r['initial'],r['final_statistics']]
    if r.get('current') is not None:stats.append(r['current'])
    for direction in r['directions']:
        for trial in direction['trials']:
            if trial.get('finite'):
                if not isinstance(trial.get('statistics'),dict):
                    raise ValueError('Every finite trial needs its actual full target read')
                stats.append(trial['statistics'])
    if any(item.get('frozen_target_identity')!=value['target_identity_sha256']
            or item.get('mean_averaging')!='exact-material-Haar'
            or item.get('final_metric_frozen') is not True for item in stats):
        raise ValueError('Initial, final and all finite actual trials must read the same exact target')
    return value
''')
    tree=ast.parse(source)
    tree.body[0].value=ast.Constant(value='''Read only a real complete fixed accurate-Haar/amplitude solve.

All original f119 direction, true acceptance, row-count and amplitude
checks remain. The distinct actual target/source identities, working
moment carrier and initial/final/every finite trial target are checked.
No arrays, F/J, fixture or scientific solve runs in this reader.
''')
    expected_node=[node for node in tree.body if isinstance(node,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='EXPECTED' for t in node.targets)][0]
    expected=ast.literal_eval(expected_node.value)
    expected.update(driver=('fullclosed_frozen_haar_amplitude_qp.py',driver_sha),
        frozen_coarse=('frozen_material_haar_coarse_moments.py',coarse_sha),
        frozen_target=('frozen_material_haar_metric.py',HAAR_TARGET_SHA))
    module_constant(tree,'EXPECTED',expected)
    module_constant(tree,'SCHEMA','complete-fixed-true-material-Haar-with-held-amplitude-budgets-v1')
    tree.body[1:1]=ast.parse(
        'R671_FACTORY_SHA = '+repr(R671_SHA)+'\n'
        'HAAR_TARGET_SHA = '+repr(HAAR_TARGET_SHA)+'\n'
        'HAAR_MOMENTS_SHA = '+repr(MOMENTS_SHA)+'\n').body
    insert_derivation(tree,dict(schema='R691-independent-complete-Haar-actual-report-reader-v1',
        complete_fixed_target_reader_parent_sha256=BASE_READER_SHA,
        complete_driver_sha256=driver_sha,complete_coarse_sha256=coarse_sha,
        accurate_target_source_sha256=HAAR_TARGET_SHA,accurate_moment_source_sha256=MOMENTS_SHA,
        original_actual_direction_and_amplitude_checks_retained=True,
        scientific_evaluation=False))
    main_index=next(j for j,n in enumerate(tree.body)
        if isinstance(n,ast.FunctionDef) and n.name=='main')
    tree.body[main_index:main_index]=helper.body
    for name in ('sha','finite','metric','amplitude'):
        if not same_ast(function(original,name),function(tree,name)):
            raise AssertionError('Keep actual-report helper behavior '+name)
    old_loop=[node for node in function(original,'main').body if isinstance(node,ast.For)][1:]
    new_loop=[node for node in function(tree,'main').body if isinstance(node,ast.For)][1:]
    if len(old_loop)!=len(new_loop) or any(not same_ast(a,b) for a,b in zip(old_loop,new_loop)):
        raise AssertionError('Do not omit original actual direction or same-measure checks')
    record=clean_and_write(out,tree)
    record.update(original_actual_metric_and_amplitude_helpers_AST_equal=True,
        original_direction_and_same_measure_loops_AST_equal=True,scientific_evaluation=False)
    return record


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    args=parser.parse_args()
    source=args.repo.resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    args.outdir.mkdir(parents=True,exist_ok=True)
    coarse=derive_coarse(source/'frozen_metric_coarse_moments.py',
        args.outdir/'frozen_material_haar_coarse_moments.py')
    driver=derive_driver(source/'fullclosed_frozen_metric_amplitude_qp.py',
        args.outdir/'fullclosed_frozen_haar_amplitude_qp.py',coarse['sha256'])
    launcher=derive_launcher(source/'launch_frozen_metric_amplitude_actions.py',
        args.outdir/'launch_frozen_haar_amplitude_actions.py',driver['sha256'],coarse['sha256'])
    reader=derive_reader(source/'read_frozen_amplitude_report.py',
        args.outdir/'read_frozen_haar_amplitude_report.py',driver['sha256'],coarse['sha256'])
    print(json.dumps(dict(schema='R691-pure-source-complete-Haar-solver-derivation-v2',
        deriver_sha256=sha(__file__),scientific_execution=False,
        coarse=coarse,driver=driver,launcher=launcher,reader=reader),indent=2,allow_nan=False))


if __name__=='__main__':
    main()

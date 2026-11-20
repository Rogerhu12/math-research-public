#!/usr/bin/env python3
"""Continue an actual completed full-Phi parent with one optional SOC per step.

The first old parent is validated by the unmodified published original/R671
completed-report planner (18ba/425f), in --print-command mode.  Its original
driver is then replaced by the fully declared SOC source derivation.  The
same complete-history extractor resolves every old/new permanent position
only inside public Actions.  No field, oracle or solve runs in preparation.

Future SOC parents require an actual source whose entire AST is rebuilt by
the SOC deriver.  A separately identified PREPARATION-ONLY copy of the old
planner calls that explicit binder instead of the old-source binder; none
of the old binder's checks is disabled and the parent report is not edited.
Actual corrected slope/prediction drives acceptance and terminal mu.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time


HELPER_SHA = '5bc50d6b18223685da8ea355d179191234ad83b5e92fd6313f4070b7e02127c7'
DERIVER_SHA = '805823e49970246bf532b65a0caefd88244b414ee52f8f555ff28b745d2fd30a'
HISTORY_SHA = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
MANIFEST_SHA = '100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622'
PLANNERS = {
    'original': ('launch_full_phi_from_completed_report.py',
        '18ba10e5a37f5032b37388a7bfcdede97d11dc680685d73520732f9a278697f7'),
    'R671': ('launch_full_phi_exact_tail_from_completed_report.py',
        '425fd1d1254450afac26b2ca29ca4ffbb6fb93d59588163bef726e34999e4703'),
}
POSITION_SCHEMA = 'immutable-curvature-history-locations-v1'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def file_record(path):
    p = Path(path).resolve()
    return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)


def load(name,path):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def required_sha(path, digest, role):
    if sha(path) != digest:
        raise ValueError('The bound '+role+' source identity changed')


def argument(command,flag):
    if command.count(flag) != 1:
        raise ValueError('Need one actual scientific argument '+flag)
    return command[command.index(flag)+1]


def prepare_soc_parent_planner(base,destination,deriver_path,model):
    """Only the explicit source-binder changes in this preparation-only copy."""
    required_sha(base,PLANNERS[model][1],'completed-report planner')
    required_sha(deriver_path,DERIVER_SHA,'SOC body deriver')
    tree = ast.parse(Path(base).read_text(), filename=str(base))
    counts = dict(explicit_SOC_source_binding=0, preparation_only_guard=0)
    expected = ast.parse('history.bound_parent_source(report,source_dir,args.parent_source)',mode='eval').body

    class Transform(ast.NodeTransformer):
        def visit_Assign(self,node):
            node = self.generic_visit(node)
            if (len(node.targets) == 1 and isinstance(node.targets[0],ast.Name)
                    and node.targets[0].id == 'parent_source'
                    and ast.dump(node.value,include_attributes=False) == ast.dump(expected,include_attributes=False)):
                node.value = ast.parse('soc_source_binder.bind_soc_parent(report,args.parent_source,source_dir,derivation_path)',mode='eval').body
                counts['explicit_SOC_source_binding'] += 1
            return node
        def visit_FunctionDef(self,node):
            node = self.generic_visit(node)
            if node.name != 'main':
                return node
            new = []
            for st in node.body:
                new.append(st)
                if (isinstance(st,ast.Assign) and len(st.targets)==1
                        and isinstance(st.targets[0],ast.Name) and st.targets[0].id=='args'
                        and isinstance(st.value,ast.Call) and isinstance(st.value.func,ast.Attribute)
                        and st.value.func.attr=='parse_args'):
                    new.extend(ast.parse(
                        "if not args.print_command:\n"
                        "    raise RuntimeError('This source-derived SOC-parent planner is preparation-only')\n"
                        "if args.parent_source is None:\n"
                        "    raise ValueError('A future SOC parent requires its actual driver source')\n"
                        "soc_binder_path=Path("+repr(str(Path(deriver_path).resolve()))+")\n"
                        "if source_sha(soc_binder_path)!="+repr(DERIVER_SHA)+":\n"
                        "    raise ValueError('SOC parent body binder identity changed')\n"
                        "soc_source_binder=load('explicit_SOC_parent_source_binder',soc_binder_path)\n"
                    ).body)
                    counts['preparation_only_guard'] += 1
            node.body = new
            return node
    tree = ast.fix_missing_locations(Transform().visit(tree))
    if counts != dict(explicit_SOC_source_binding=1,preparation_only_guard=1):
        raise ValueError('Unknown frozen completed-planner binding sites')
    compile(tree,str(base)+'-SOC-parent-preparation','exec')
    provenance = dict(schema='completed-planner-explicit-SOC-parent-body-binding-v1',model=model,
        frozen_planner=file_record(base),deriver=file_record(deriver_path),
        preparation_source_sha256=sha(__file__),counts=counts,
        parent_report_edited=False,old_parent_guard_bypassed=False,
        scientific_execution_allowed=False)
    text = ('#!/usr/bin/env python3\n# Explicit SOC-parent preparation source:\n# '
            +json.dumps(provenance,sort_keys=True)+'\n'+ast.unparse(tree)+'\n')
    destination = Path(destination)
    if destination.exists() and destination.read_text() != text:
        raise FileExistsError('Use a fresh preparation path for different source bytes')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(text)
    return dict(**file_record(destination),derivation=provenance)


def check_SOC_terminal(history, report):
    """The bound SOC body uses the same rule with the ACTUAL accepted model."""
    trace = history.terminal_damping(report)
    if report.get('final_damping') != trace['terminal_damping']:
        raise ValueError('SOC explicit terminal damping differs from its bound replay')
    for record, step in zip(report['directions'],trace['trace']):
        if record.get('damping_after_direction') != step['damping_after']:
            raise ValueError('SOC actual direction damping differs from the bound update')
        if record.get('accepted_update_kind') == 'parent_row_soc' and record.get('accepted'):
            soc = record['soc']
            trial = soc['trial']
            if (soc.get('accepted') is not True or record.get('accepted_alpha') != 1.
                    or record.get('direction_sha256') != soc['direction_sha256']
                    or record.get('half_objective_slope') != trial['half_objective_slope']
                    or record.get('quadratic_predicted_actual_change') != trial['quadratic_predicted_actual_change']
                    or record.get('quadratic_predicted_actual_objective') != trial['quadratic_predicted_actual_objective']
                    or record.get('actual_to_full_step_predicted_decrease') != trial['actual_to_same_corrected_step_predicted_decrease']):
                raise ValueError('Accepted SOC model does not bind its actual state/damping semantics')
    return trace


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for flag in ('repo','work','parent-report','bundle','carrier','outdir'):
        p.add_argument('--'+flag,type=Path,required=True)
    p.add_argument('--model',choices=tuple(PLANNERS),required=True)
    p.add_argument('--manifest',type=Path,action='append',required=True)
    p.add_argument('--soc-tau',type=float,required=True)
    for flag in ('soc-source','soc-deriver','history-source','manifest-derivation-source',
                 'parent-planner','parent-source','qp-source','node-report','scalar-input'):
        p.add_argument('--'+flag,type=Path)
    p.add_argument('--directions',type=int,default=1)
    p.add_argument('--maxiter',type=int,default=256)
    p.add_argument('--active-rows',type=int)
    p.add_argument('--stage-block',type=int,default=64)
    p.add_argument('--qp-atol',type=float,default=0.)
    p.add_argument('--qp-rtol',type=float)
    p.add_argument('--print-command',action='store_true')
    a = p.parse_args()
    if not math.isfinite(a.soc_tau) or a.soc_tau<0:
        raise ValueError('SOC tau is an explicit finite nonnegative algorithm parameter')
    for flag in ('repo','work','parent_report','bundle','carrier','outdir'):
        setattr(a,flag,getattr(a,flag).resolve())
    source_dir = a.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    helper_path = (a.soc_source or source_dir/'full_phi_parent_row_soc.py').resolve()
    deriver_path = (a.soc_deriver or source_dir/'derive_full_phi_parent_row_soc.py').resolve()
    history_path = (a.history_source or source_dir/'launch_refinement_from_full_report.py').resolve()
    manifest_path = (a.manifest_derivation_source or source_dir/'launch_fixed_g_refinement_qp.py').resolve()
    planner_path = (a.parent_planner or source_dir/PLANNERS[a.model][0]).resolve()
    for path,digest,role in ((helper_path,HELPER_SHA,'SOC helper'),
            (deriver_path,DERIVER_SHA,'SOC deriver'),(history_path,HISTORY_SHA,'full-history helper'),
            (manifest_path,MANIFEST_SHA,'exact-position derivation'),
            (planner_path,PLANNERS[a.model][1],'completed-parent planner')):
        required_sha(path,digest,role)
    history = load('SOC_full_history',history_path)
    deriver = load('SOC_complete_source_deriver',deriver_path)
    parent = json.loads(a.parent_report.read_text())
    is_SOC_parent = 'soc_derivation' in parent
    inputs_dir = a.work/(a.outdir.name+'-continuation-inputs')
    inputs_dir.mkdir(parents=True,exist_ok=True)
    actual_planner = file_record(planner_path)
    if is_SOC_parent:
        if a.parent_source is None:
            raise ValueError('A SOC parent needs its actual source for whole-body reconstruction')
        bound = deriver.bind_soc_parent(parent,a.parent_source,source_dir,manifest_path)
        if bound['model'] != a.model:
            raise ValueError('SOC parent model differs from the requested continuation')
        check_SOC_terminal(history,parent)
        actual_planner = prepare_soc_parent_planner(planner_path,
            inputs_dir/'explicit-SOC-parent-prepare.py',deriver_path,a.model)
    invocation = [sys.executable,actual_planner['path'],'--repo',str(a.repo),
        '--work',str(a.work),'--parent-report',str(a.parent_report),
        '--bundle',str(a.bundle),'--carrier',str(a.carrier),'--outdir',str(a.outdir),
        '--history-source',str(history_path),'--derivation-source',str(manifest_path),
        '--directions',str(a.directions),'--maxiter',str(a.maxiter),
        '--stage-block',str(a.stage_block),'--qp-atol',repr(a.qp_atol)]
    for flag in ('parent-source','qp-source','active-rows','qp-rtol'):
        value = getattr(a,flag.replace('-','_'))
        if value is not None:
            invocation.extend(['--'+flag,str(value.resolve()) if isinstance(value,Path) else str(value)])
    if a.model == 'R671':
        if a.node_report is None or a.scalar_input is None:
            raise ValueError('Identical R671 continuation needs the actual node/scalar inputs')
        invocation.extend(['--node-report',str(a.node_report.resolve()),
                           '--scalar-input',str(a.scalar_input.resolve())])
    for path in a.manifest:
        invocation.extend(['--manifest',str(path.resolve())])
    # The original planners do all original/source/model/terminal-mu checks.
    # For a future SOC parent, their explicit derived binder first proves the
    # full new source body; the actual report is never rewritten as old.
    prepared = subprocess.run([*invocation,'--print-command'],check=True,capture_output=True,text=True)
    command = shlex.split(prepared.stdout.strip())
    parent_plan_path = inputs_dir/'continuation-plan.json'
    parent_plan = json.loads(parent_plan_path.read_text())
    if parent_plan.get('full_scientific_command') != command:
        raise ValueError('Actual parent planner argv differs from its recorded preparation')
    base = source_dir/deriver.BASES[a.model][0]
    derived = deriver.derive_driver(base,inputs_dir/'derived-parent-row-SOC.py',manifest_path)
    command[2] = derived['path']
    command.extend(['--soc-source',str(helper_path),'--soc-tau',repr(a.soc_tau)])
    plan_path = inputs_dir/'SOC-continuation-plan.json'
    plan = dict(schema='actual-full-Phi-parent-to-one-parent-row-SOC-v1',model=a.model,
        source=file_record(__file__),helper=file_record(helper_path),deriver=file_record(deriver_path),
        history=file_record(history_path),manifest_derivation=file_record(manifest_path),
        actual_parent_planner=actual_planner,actual_parent_preparation=file_record(parent_plan_path),
        actual_parent_preparation_argv=invocation,parent_driver=parent_plan['parent_driver'],
        inputs=parent_plan['inputs'],actual_terminal_damping=parent_plan['actual_terminal_damping'],
        parent_was_SOC=is_SOC_parent,derived_driver=derived,
        frozen_dependencies=parent_plan['frozen_dependencies'],QP_source=parent_plan['QP_source'],
        canonical_model_definition=parent_plan.get('canonical_model_definition'),
        source_and_model_transitions='Same physical model; existing planner source validation plus the exact SOC derivation. No edited parent report or bypassed old guard.',
        complete_position_union_path=parent_plan['canonical_union_path'],
        tau=a.soc_tau,tau_is_algorithm_parameter_not_Lipschitz_threshold=True,
        SOC_attempts_per_direction=1,SOC_trigger='First alpha=1 true geometry rejection after domain and true Phi pass',
        requested_directions=a.directions,maxiter=a.maxiter,qp_atol=a.qp_atol,
        scalar_mesh_M_N_observation_rows_weights_norm_and_all_permanent_points_preserved=True,
        main_QP_or_preconditioner_changed_by_SOC=False,
        full_scientific_command=command,scientific_arrays_read=False,
        scientific_execution_started=False,output=str(a.outdir))
    if plan_path.exists():
        old = json.loads(plan_path.read_text())
        if (old.get('scientific_execution_started') or old.get('inputs') != plan['inputs']
                or old.get('source') != plan['source'] or old.get('full_scientific_command') != command):
            raise FileExistsError('Use a fresh SOC continuation directory for a different or already-started budget')
    history.write_json(plan_path,plan)
    if a.print_command:
        print(shlex.join(command))
        return
    history.require_actions()
    shape = history.budget(parent)
    points = history.Locations(shape['parent_J'],shape['parent_radial_observations'],shape['parent_full_angles'])
    points.walk(parent)
    caller_records = []
    carrier_sha = history.sha(a.carrier)
    for index,path in enumerate(a.manifest):
        path = path.resolve()
        payload = json.loads(path.read_text())
        declared = payload.get('carrier_sha256',payload.get('observation_carrier_sha256'))
        if declared is not None and declared != carrier_sha:
            raise ValueError('A caller position manifest belongs to another observation carrier')
        points.walk(payload,path=('caller_manifest',index))
        caller_records.append(file_record(path))
    plan.update(scientific_execution_started=True,
        execution={key:os.environ.get(key) for key in
            ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA')})
    history.write_json(plan_path,plan)
    resolved = points.resolve_grid(a.carrier)
    supplement = Path(parent_plan['canonical_union_path'])
    union = dict(schema=POSITION_SCHEMA,bundle_sha256=history.sha(a.bundle),
        carrier_sha256=carrier_sha,parent_report=file_record(a.parent_report),
        source_sha256=sha(__file__),history_helper_sha256=HISTORY_SHA,
        **points.arrays(),values_inherited=False,decimal_position_rounding=False,
        recovered_parent_grid_points=resolved,extraction=points.summary(),caller_sources=caller_records,
        actual_SOC_parent_source_rebuilt=is_SOC_parent)
    history.write_json(supplement,union,compact=True)
    plan.update(scientific_arrays_read=True,complete_position_union=file_record(supplement),
                resolved_position_counts=points.summary())
    history.write_json(plan_path,plan)
    print(json.dumps(dict(event='complete_parent_row_SOC_continuation_started',
        plan=file_record(plan_path),parent_sha256=history.sha(a.bundle),
        damping=parent_plan['actual_terminal_damping']['terminal_damping'],
        tau=a.soc_tau,directions=a.directions,complete_positions=points.summary())),flush=True)
    environment = os.environ.copy()
    environment.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',
                       OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    started = time.monotonic()
    returned = subprocess.run(command,env=environment,cwd=a.repo)
    result = dict(returncode=returned.returncode,seconds=time.monotonic()-started)
    report_path = a.outdir/'report.json'
    if report_path.is_file():
        result['report'] = file_record(report_path)
    if returned.returncode == 0:
        outcome = json.loads(report_path.read_text())
        deriver.bind_soc_parent(outcome,derived['path'],source_dir,manifest_path)
        final = a.outdir/'final.npz'
        if (outcome.get('complete') is not True
                or outcome.get('source_sha256_by_role',{}).get('qp') != plan['QP_source']['sha256']
                or outcome.get('final_bundle_sha256') != history.sha(final)
                or outcome.get('observation_carrier_sha256') != carrier_sha):
            raise ValueError('Actual SOC return lacks a complete same-source/model/final-bundle identity')
        if a.model == 'R671' and outcome.get('exact_tail_context_final',{}).get('definition') != plan['canonical_model_definition']:
            raise ValueError('Actual R671 SOC return changed its fixed canonical model')
        trace = check_SOC_terminal(history,outcome)
        result.update(final_bundle=file_record(final),terminal_damping=trace,
            actual_direction_count=len(outcome.get('directions',[])),
            accepted_directions=sum(bool(v.get('accepted')) for v in outcome.get('directions',[])),
            SOC_attempts=sum(bool(v.get('soc_attempted')) for v in outcome.get('directions',[])),
            accepted_SOC_directions=sum(bool(v.get('accepted')) and v.get('accepted_update_kind')=='parent_row_soc'
                for v in outcome.get('directions',[])),
            final_known_point_filter=outcome.get('final_curvature_filter'))
    plan.update(scientific_execution_returned=True,actual_return=result)
    history.write_json(plan_path,plan)
    raise SystemExit(returned.returncode)


if __name__ == '__main__':
    main()

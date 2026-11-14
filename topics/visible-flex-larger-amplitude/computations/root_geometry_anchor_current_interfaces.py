#!/usr/bin/env python3
"""Source-only adapters for one genuinely accepted M32 nine-control geometry model.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original plan, complete-mean field, minimax and combined warm formulas are
unchanged. These adapters select the explicit corrected provider, retain owned
resource paths, and bind the same current accepted state and all nine responses.
"""
import ast
import hashlib
import math
from pathlib import Path

HERE=Path(__file__).resolve().parent
CONTROL_NAMES=('actual_q1','actual_q4','actual_c6','vu',
    'descending_turn_curvature','start_acceleration','initial_speed_frontload',
    'vd','descending_sync_curvature')
RESPONSE_FIELDS=('delta','boost_length','boost_speed',*CONTROL_NAMES[3:])
FROZEN={
    'root_actual_geometry_fullmean_initial_laws_plan.py':'a6c537cea001d5fcc4104164bee5194620913b9a53bfa1fad0ccf6800ddfcb34',
    'root_geometry_minimax_initial_laws_combined_plan.py':'4de2252d400731c5920f6d6d4a4e3317b3c6d6f258dd00fa7b4898eb79c35b10',
    'root_geometry_minimax_initial_laws_controls.py':'ccdcc95d3e7dd2a1447714578e6976179f1b5c32d3495e13a074399872c31e57',
    'root_geometry_minimax_from_plan.py':'4fdd46bf198e573bd83a86195143caa86d7105d3847d4e12431d844c2111e213',
    'root_actual_geometry_field_anchor.py':'da6726c130503113a9483da2365cea70e59f22f26e09eb19b08ba57632229a77',
    'strong_frontload_anchor_loader_adapter.py':'aa32079179e20a95493cd911185ea69e7df2b4d5b150a713597e9d2f9fd73c86',
    'strong_monotone_initial_speed_anchor.py':'583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
    'strong_foreground_resource_run.py':'e683fbbeb1eb579d07799acbdd08b2254917e49209566c28a85628eb9cb72bc6',
}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check_sources():
    for name,h in FROZEN.items():
        if sha(HERE/name)!=h:
            raise ValueError('A frozen current-geometry interface source changed: '+name)


def require_response(response):
    """Reject a partial/history splice; the new full current-point job owns all columns."""
    if (response.get('schema')!='fixed-actual-to-three-control-response-v1' or
            not response.get('finished') or response.get('new_solution') or
            response.get('modes')!=32 or response.get('partial_recovery',False) or
            response.get('fields')!=list(RESPONSE_FIELDS)):
        raise ValueError('Require the complete same-point M32 nine-external-field response')
    prescribed=response['prescribed_low_core_responses']
    neutral=response['additional_core_held_directions']
    if ([r['direction'] for r in prescribed]!=list(CONTROL_NAMES[:3]) or
            [r['external_field'] for r in neutral]!=list(CONTROL_NAMES[3:])):
        raise ValueError('The complete current response control ordering changed')
    for row in prescribed+neutral:
        if len(row['core_derivative'])!=32 or not all(math.isfinite(x) for x in row['core_derivative']):
            raise ValueError('A current response omitted finite core coordinates')
        key=('half_step_exchange_response_relative_difference' if 'direction' in row
             else 'half_step_combination_relative_difference')
        if not isinstance(row[key],(int,float)) or not math.isfinite(row[key]):
            raise ValueError('The actual combined half-step observation is missing')
    ksync=neutral[-1]
    if ksync['physical_profile_derivative']['descending_sync_curvature']!=1.:
        raise ValueError('The Ksync neutral direction is not in original physical units')
    if set(ksync['physical_profile_derivative'])!={'delta','boost_length','boost_speed','descending_sync_curvature'}:
        raise ValueError('Ksync must compensate only the original three exchanged controls')
    external={r['field']:r for r in response['external_responses']}
    if set(external)!=set(RESPONSE_FIELDS):
        raise ValueError('Some original full/half external response is missing')
    # Preserve the actual original observed acceptance gate, without inventing a
    # stronger gate for the exchanged or combined directions.
    for row in external.values():
        if not math.isfinite(row['half_step_response_relative_difference']) or row['half_step_response_relative_difference']>2e-4:
            raise ValueError('An original external half-step gate did not pass')
    original=float(response['baseline']['profile']['descending_sync_curvature'])
    width=2e-6*max(.1,abs(original))
    if external['descending_sync_curvature']['width']!=width or external['descending_sync_curvature']['half_width']!=width/2:
        raise ValueError('The saved Ksync external forcing step is not the original rule')


def build(role,wrapper):
    check_sources()
    wrapper=Path(wrapper).resolve()
    if wrapper.parent!=HERE:
        raise ValueError('Keep the explicitly frozen interface bundle together')
    original_name={'plan':'root_actual_geometry_fullmean_initial_laws_plan.py',
                   'combined':'root_geometry_minimax_initial_laws_combined_plan.py'}[role]
    source=original=(HERE/original_name).read_text()
    edits=[]
    def edit(before,after):
        nonlocal source
        if source.count(before)!=1:
            raise ValueError('A frozen source interface is not unique: '+before)
        source=source.replace(before,after,1)
        edits.append((before,after))
    if role=='plan':
        edit("DEFAULT_NEUTRALS=('vu','descending_turn_curvature','start_acceleration','initial_speed_frontload')",
             'DEFAULT_NEUTRALS='+repr(CONTROL_NAMES[3:]))
        edit('    args = ap.parse_args()\n',
             "    args = ap.parse_args()\n    if args.interior_audit is None:raise ValueError('Require the accepted current fixed-view quintic witness')\n")
        edit('    if not valid_controls(control_names) or len(args.steps)!=len(control_names):',
             '    if tuple(control_names)!=CONTROL_NAMES or not valid_controls(control_names) or len(args.steps)!=len(control_names):')
        edit('    chart_record = actual[\'numerical_meridian_chart\']\n',
             "    if actual['modes']!=32:raise ValueError('This current response interface is explicitly M32')\n    chart_record = actual['numerical_meridian_chart']\n")
        edit('        response=read(args.response_data)\n',
             '        response=read(args.response_data)\n        require_response(response)\n')
        edit("    wrapper=Path(__file__).with_name('root_actual_geometry_field_initial_laws.py')",
             "    wrapper=Path(__file__).with_name('root_actual_geometry_field_anchor.py')")
        edit("command=[sys.executable,str(Path(__file__).with_name('strong_resource_run.py')),\n                 '--out',str(formal),'--',*command]",
             "command=[sys.executable,str(Path(__file__).with_name('strong_foreground_resource_run.py')),\n                 '--out',str(formal),'--heartbeat',str(case)+'-heartbeat.json','--ownership',str(case)+'-ownership.json',\n                 '--task-prefix','geometry-current-nine-'+case.name,'--',*command]")
        edit('    if args.known_grid:inputs.append(args.known_grid)\n',
             "    inputs.extend(Path(__file__).with_name(n) for n in ('root_actual_geometry_fullmean_initial_laws_plan.py','root_actual_geometry_field_initial_laws.py','strong_monotone_initial_speed_anchor.py','strong_frontload_anchor_loader_adapter.py','strong_foreground_resource_run.py','root_geometry_anchor_current_interfaces.py'))\n    if args.known_grid:inputs.append(args.known_grid)\n")
        edit('    hashes.update({str(p):sha(p) for p in inputs})\n',
             "    hashes.update({str(p):sha(p) for p in inputs})\n    if not args.baseline_only:\n        baseline_plan=Path(str(prefix)+'-baseline-plan.json')\n        original_baseline=read(baseline_plan)\n        if not original_baseline['baseline_only'] or original_baseline['candidates']!=[planned[0]] or original_baseline['grid']!=str(grid_path):raise ValueError('Reuse the unique previously prepared current baseline verbatim')\n        hashes[str(baseline_plan)]=sha(baseline_plan)\n")
        edit('        baseline_only=args.baseline_only,nonlinear_solution=False,new_tail_evaluation=False,\n',
             '        baseline_only=args.baseline_only,nonlinear_solution=False,new_tail_evaluation=False,\n        current_anchor_complete_geometry_interface=INTERFACE_PROVENANCE,\n')
    else:
        edit('    model=json.loads(args.minimax.read_text())\n',
             "    model=json.loads(args.minimax.read_text())\n    if tuple(r['name'] for r in plan['directions'])!=CONTROL_NAMES or not model.get('actual_anchor_current_geometry_bridge',{}).get('all_identity_gates'):raise ValueError('Require the complete current nine-control reader bridge')\n")
        edit('    response=json.loads(response_path.read_text())\n',
             '    response=json.loads(response_path.read_text())\n    require_response(response)\n')
        edit("    for flag,value in [('--out',formal),('--out-prefix',case),\n",
             "    for flag,value in [('--out',formal),('--heartbeat',str(case)+'-heartbeat.json'),('--ownership',str(case)+'-ownership.json'),('--task-prefix','geometry-current-nine-'+case.name),('--out-prefix',case),\n")
        edit('    for path in (args.plan,args.minimax,Path(__file__)):\n',
             "    for path in (args.plan,args.minimax,Path(__file__),Path(__file__).with_name('root_geometry_minimax_initial_laws_combined_plan.py'),Path(__file__).with_name('root_geometry_anchor_current_interfaces.py')):\n")
        edit("        nonlinear_solution=False,new_tail_evaluation=False,cwd=plan['cwd'],\n",
             "        nonlinear_solution=False,new_tail_evaluation=False,cwd=plan['cwd'],\n        current_anchor_complete_geometry_interface=plan['current_anchor_complete_geometry_interface'],\n        current_anchor_combined_interface=INTERFACE_PROVENANCE,\n")
    ast.parse(source)
    reversed_source=source
    for before,after in reversed(edits):
        if reversed_source.count(after)!=1:raise ValueError('The source interface is not exactly reversible')
        reversed_source=reversed_source.replace(after,before,1)
    if reversed_source!=original:
        raise ValueError('An unlisted mathematical source change occurred')
    provenance=dict(schema='accepted-current-M32-nine-control-anchor-interface-v1',
        role=role,author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        adapter_source_sha256=sha(__file__),entry_source_sha256=sha(wrapper),
        original_source=original_name,original_source_sha256=sha(HERE/original_name),
        transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_reverse_recovers_original_source=True,source_edits=[dict(before=b,after=a) for b,a in edits],
        design_controls=list(CONTROL_NAMES),external_response_fields=list(RESPONSE_FIELDS),
        corrected_provider_sha256=FROZEN['strong_monotone_initial_speed_anchor.py'],
        expected_mean_angular=1552,geometry_angular_minimum=768,
        original_mean_field_exchange_and_minimax_formulas_unchanged=True,
        no_future_accepted_state_or_field_created=True)
    namespace=dict(__file__=str(wrapper),__name__='accepted_current_geometry_'+role,
        CONTROL_NAMES=CONTROL_NAMES,INTERFACE_PROVENANCE=provenance,require_response=require_response)
    exec(compile(source,'<frozen-'+role+'-with-current-anchor-interface>','exec'),namespace)
    return namespace,provenance

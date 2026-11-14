#!/usr/bin/env python3
"""Create fresh complete-geometry initial-law planners by exact source edits.

The original five/six-control files stay immutable. Only the reviewed
control list, optional absent frontload default, physical trust ranges,
diagnostic tail floor, and adapter identities are extended. Every original
field, complete mean, Fourier mode, and LP finite-row check is retained.
This source preparation executes no physical field, response, LP or BVP.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
PINS={
 'root_actual_geometry_fullmean_six_plan.py':'5f34aec029cfce876fc5f61957d51bb8f924f2ed08e2d01fb412c527a49b3101',
 'root_geometry_minimax_current_controls.py':'5f3b4f335489d297fca3a8c7f3aa64ed65ef35ad717b17f524eef11720afefc1',
 'root_geometry_minimax_current_combined_plan.py':'f64e0daad78d1c2b6d44d32d42ba027b1bb3408a5a7b6376b7c2f2a35f57967a',
 'root_geometry_minimax_variable_controls.py':'7b641b9b08ea61d6620541bd8ea977bb769e665a06b831a44818ca27a998cf92',
}

HELPER="""
REVIEWED_NEUTRALS=('vu','vd','start_acceleration','descending_turn_curvature',
                  'descending_sync_curvature','coast_outward','loop_ratio','initial_speed_frontload')
DEFAULT_NEUTRALS=('vu','descending_turn_curvature','start_acceleration','initial_speed_frontload')
def valid_controls(names):
    return (names[:3]==['actual_q1','actual_q4','actual_c6'] and
            3<=len(names)<=11 and len(set(names))==len(names) and
            all(n in REVIEWED_NEUTRALS for n in names[3:]))
def add_profile(profile,key,value):
    if key in ('initial_speed_pulse','initial_speed_frontload') and key not in profile:
        if value==0.:return
        profile[key]=value
    else:profile[key]+=value

"""


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-dir',type=Path,required=True)
    ap.add_argument('--record',type=Path,required=True)
    a=ap.parse_args()
    if a.record.exists():raise FileExistsError(a.record)
    records=[]
    def create(original_name,new_name,edits):
        p=HERE/original_name
        if sha(p)!=PINS[original_name]:raise ValueError('Frozen original source changed: '+original_name)
        original=p.read_text();source=original
        for before,after in edits:
            if source.count(before)!=1:raise ValueError('A source adapter anchor is not unique: '+repr(before))
            source=source.replace(before,after,1)
        ast.parse(source,filename=new_name)
        reverse=source
        for before,after in reversed(edits):
            if reverse.count(after)!=1:raise ValueError('The source adapter reverse is not unique: '+repr(after))
            reverse=reverse.replace(after,before,1)
        if reverse!=original:raise ValueError('Extra original code was modified')
        out=a.out_dir/new_name
        if out.exists():
            if out.read_text()!=source:raise FileExistsError('Use a fresh adapter destination: '+str(out))
        else:out.parent.mkdir(parents=True,exist_ok=True);out.write_text(source)
        records.append(dict(original=str(p),original_sha256=sha(p),adapter=str(out),adapter_sha256=sha(out),
            source_transforms=[dict(before=x,after=y,count=1) for x,y in edits],exact_reverse_recovers_original=True,
            source_AST_passed=True))

    create('root_actual_geometry_fullmean_six_plan.py','root_actual_geometry_fullmean_initial_laws_plan.py',[
      ('def main():\n',HELPER+'def main():\n'),
      ("    ap.add_argument('--angular', type=int, default=384)","    ap.add_argument('--angular', type=int, default=768)"),
      ("    ap.add_argument('--steps', type=float, nargs=6, required=True,\n                    help='Positive finite steps for actual_q1, actual_q4, actual_c6, vu, first-turn K, and start_acceleration.')",
       "    ap.add_argument('--neutral-controls',nargs='+',default=list(DEFAULT_NEUTRALS))\n"
       "    ap.add_argument('--steps',type=float,nargs='+',required=True,help='Positive steps for all three original core controls followed by the declared reviewed neutral controls.')"),
      ('    if args.angular < 96 or args.angular % 4 or any(not np.isfinite(x) or x<=0 for x in args.steps):',
       "    control_names=['actual_q1','actual_q4','actual_c6',*args.neutral_controls]\n"
       "    if not valid_controls(control_names) or len(args.steps)!=len(control_names):\n"
       "        raise ValueError('Require three original core controls and distinct explicitly reviewed neutrals with one step each')\n"
       '    if args.angular < 768 or args.angular % 768 or any(not np.isfinite(x) or x<=0 for x in args.steps):'),
      ("    directions=list(zip(('actual_q1','actual_q4','actual_c6','vu','descending_turn_curvature','start_acceleration'),args.steps))",
       '    directions=list(zip(control_names,args.steps))'),
      ("    wrapper=Path(__file__).with_name('root_actual_geometry_field_complete_mean.py')",
       "    wrapper=Path(__file__).with_name('root_actual_geometry_field_initial_laws.py')"),
      ('                profile[key]+=step*value','                add_profile(profile,key,step*value)'),
      ("    if args.known_grid:inputs.append(args.known_grid)",
       "    inputs.extend(Path(__file__).with_name(name) for name in ('root_actual_geometry_field_complete_mean.py','strong_initial_laws_augmented_core.py','strong_pulse_augmented_core.py','strong_initial_speed_pulse.py','strong_monotone_initial_speed.py'))\n"
       '    if args.known_grid:inputs.append(args.known_grid)'),
      ('The sixth control is the newly computed core-held start_acceleration column.',
       'The reviewed neutral list is explicit; default controls are vu, first-turn K, k0, and degree22 inlet frontload, each from the same newly computed actual core-held response.'),
      ('full thirteen-case plan','complete two-sided variable-control plan'),
    ])

    create('root_geometry_minimax_variable_controls.py','root_geometry_minimax_control_constraints.py',[
      ('                  max_rounds=60):','                  max_rounds=60,control_bounds=None):'),
      ('    bounds = [(q1_step, q1_step)]+[(-trust, trust)]*(controls-1)+[(0., None)]',
       '    bounds = [(q1_step, q1_step)]+[(-trust, trust)]*(controls-1)+[(0., None)]\n'
       '    if control_bounds is not None:\n'
       '        if len(control_bounds)!=controls:raise ValueError("Complete current control bounds required")\n'
       '        for j,pair in enumerate(control_bounds):\n'
       '            if len(pair)!=2 or not np.isfinite(pair).all() or pair[0]>pair[1]:\n'
       '                raise ValueError("Finite ordered normalized control interval required")\n'
       '            lo,hi=max(float(pair[0]),bounds[j][0]),min(float(pair[1]),bounds[j][1])\n'
       '            if lo>hi:\n'
       '                return dict(success=False,status=2,message="Declared physical interval misses the trust box",history=[],all_finite_rows_checked=False)\n'
       '            bounds[j]=(lo,hi)'),
      ('            return dict(success=True, normalized_steps=fitted.x[:controls].tolist(),',
       '            return dict(success=True, normalized_steps=fitted.x[:controls].tolist(),\n'
       '                        normalized_control_bounds=[list(z) for z in bounds[:controls]],'),
      ('This is the saved five-control algorithm with only the number of actual\ncolumns generalized.',
       'This is the saved complete variable-control algorithm with explicit normalized trust-interval intersections only.'),
    ])

    create('root_geometry_minimax_current_controls.py','root_geometry_minimax_initial_laws_controls.py',[
      ('import argparse\n','import argparse\nimport gzip\n'),
      ('from root_geometry_minimax_variable_controls import solve_minimax',
       'from root_geometry_minimax_control_constraints import solve_minimax'),
      ('def main():\n',HELPER+'def main():\n'),
      ("    ap.add_argument('--trust-factor',type=float,default=1.)",
       "    ap.add_argument('--trust-factor',type=float,default=1.)\n"
       "    ap.add_argument('--control-range',nargs=3,action='append',default=[],metavar=('NAME','LOW','HIGH'),help='Physical neutral increment interval, intersected with the original trust box; e.g. start_acceleration -.064 0.')"),
      ("    original_names=['actual_q1','actual_q4','actual_c6','vu','descending_turn_curvature']\n    names=[r['name'] for r in directions]\n    if names not in (original_names,original_names+['start_acceleration']):\n        raise ValueError('Require all five original controls and optionally current core-held start_acceleration in order')",
       "    names=[r['name'] for r in directions]\n"
       "    if not valid_controls(names):raise ValueError('Explicit complete reviewed current controls required')\n"
       "    physical_ranges={}\n"
       "    for name,lower,upper in args.control_range:\n"
       "        lo,hi=float(lower),float(upper)\n"
       "        if name not in names[3:] or name in physical_ranges or not np.isfinite([lo,hi]).all() or lo>hi:\n"
       "            raise ValueError('Use one finite physical interval per declared neutral control')\n"
       "        physical_ranges[name]=(lo,hi)"),
      ("    response=json.loads(response_path.read_text())",
       "    response=json.loads(response_path.read_text())\n"
       "    baseline_command=rows['baseline']['command']\n"
       "    tail_path=Path(baseline_command[baseline_command.index('--actual-reference-tail')+1])\n"
       "    tail_raw=tail_path.read_bytes()\n"
       "    tail=json.loads(gzip.decompress(tail_raw) if tail_path.suffix=='.gz' else tail_raw)\n"
       "    tail_floor=float(tail['response']['audit']['formalCurvature'])\n"
       "    if not tail['response']['converged'] or not np.isfinite(tail_floor) or tail_floor<=0:\n"
       "        raise ValueError('Require current accepted tail sample for the explicit design diagnostic')"),
      ('                result=solve_minimax(base,slopes,cap,qstep,trust=args.trust_factor)',
       '                normalized_bounds=[(qstep,qstep)]+[(-args.trust_factor,args.trust_factor)]*(controls-1)\n'
       '                for index,direction in enumerate(directions):\n'
       "                    if direction['name'] in physical_ranges:\n"
       "                        normalized_bounds[index]=tuple(v/direction['step'] for v in physical_ranges[direction['name']])\n"
       '                result=solve_minimax(base,slopes,cap,qstep,trust=args.trust_factor,control_bounds=normalized_bounds)'),
      ('                              other_control_trust_factor=args.trust_factor,',
       '                              other_control_trust_factor=args.trust_factor,physical_control_ranges=physical_ranges,'),
      ("                    gap=baseline['complete_core_axis_phase_gap']+2*float(inc_core[::2].sum())",
       "                    gap=baseline['complete_core_axis_phase_gap']+2*float(inc_core[::2].sum())\n"
       "                    predicted_core=np.asarray(base_field['actual_core'])+inc_core\n"
       "                    j=np.arange(1,len(predicted_core)+1)\n"
       "                    short_rho=1-float(np.sum((4*j*j-1)*predicted_core*((-1.)**j)))\n"
       "                    k0=base_field['physical_profile']['start_acceleration']+inc_profile.get('start_acceleration',0.)"),
      ('                        candidate_is_new_nonlinear_solution=False)',
       "                        predicted_R7_initial_witness_product=k0*gap*short_rho,\n"
       "                        predicted_short_axis_core_radius=short_rho,\n"
       "                        predicted_kappa_with_current_tail_floor_times_twice_norm=max(result['predicted_max_abs_curvature'],tail_floor)*result['predicted_max_twice_norm'],\n"
       '                        candidate_is_new_nonlinear_solution=False)'),
      ("sha(Path(__file__).with_name('root_geometry_minimax_variable_controls.py'))",
       "sha(Path(__file__).with_name('root_geometry_minimax_control_constraints.py'))"),
      ('        shape=list(shape),control_count=controls,directions=directions,baseline=baseline,directional_summaries=derivatives,',
       "        current_accepted_tail_sample=dict(path=str(tail_path),sha256=sha(tail_path),formalCurvature=tail_floor,new_target_tail_bound=False),\n"
       '        physical_control_ranges=physical_ranges,\n'
       '        shape=list(shape),control_count=controls,directions=directions,baseline=baseline,directional_summaries=derivatives,'),
      ('Minimize finite curvature from all five or six current-baseline controls.',
       'Minimize finite curvature from the explicit current-baseline reviewed controls and physical trust intervals.'),
      ('The optional sixth direction is core-held start_acceleration from that exact\nbaseline\'s actual full-J.',
       'Every neutral, including degree22 initial_speed_frontload, uses that exact baseline\'s actual core-held full-J response.'),
    ])

    create('root_geometry_minimax_current_combined_plan.py','root_geometry_minimax_initial_laws_combined_plan.py',[
      ('def main():\n',HELPER+'def main():\n'),
      ("'root_geometry_minimax_current_controls.py'","'root_geometry_minimax_initial_laws_controls.py'"),
      ("'root_geometry_minimax_variable_controls.py'","'root_geometry_minimax_control_constraints.py'"),
      ("    original_names=['actual_q1','actual_q4','actual_c6','vu','descending_turn_curvature']\n    names=[d['name'] for d in plan['directions']]\n    if names not in (original_names,original_names+['start_acceleration']):\n        raise ValueError('All five original controls and optional sixth actual control must remain in order')",
       "    names=[d['name'] for d in plan['directions']]\n"
       "    if not valid_controls(names):raise ValueError('All original core and declared reviewed neutral controls must remain')"),
      ("        if index and abs(normalized)>selected['other_control_trust_factor']+1e-10:",
       "        lo,hi=selected['normalized_control_bounds'][index]\n"
       "        if not lo-1e-10<=normalized<=hi+1e-10:raise ValueError('The selected step violates its explicit normalized interval')\n"
       "        if index and abs(normalized)>selected['other_control_trust_factor']+1e-10:"),
      ('            profile[key]+=step*derivative','            add_profile(profile,key,step*derivative)'),
      ('Prepare one complete warm field from an explicit five/six-control choice.',
       'Prepare one complete same-provider warm field from an explicit reviewed-control minimax choice.'),
    ])
    a.record.parent.mkdir(parents=True,exist_ok=True)
    a.record.write_text(json.dumps(dict(schema='fullmean-initial-laws-control-adapters-source-preparation-v1',
        scope=__doc__,source_sha256=sha(__file__),adapters=records,
        actual_field_response_LP_Newton_Node_executed=False,
        unchanged_original_finite_row_checks=True,original_sources_not_modified=True),indent=2)+'\n')
    print(json.dumps(dict(prepared_only=True,adapter_count=len(records),record=str(a.record),sha256=sha(a.record))),flush=True)


if __name__=='__main__':main()

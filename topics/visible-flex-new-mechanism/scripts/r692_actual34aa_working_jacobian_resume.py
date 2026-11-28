"""Restore actual 34aa/1372 after the paid, unpersisted first 40 Jacobian blocks."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import struct
import types


HERE=Path(__file__).resolve().parent
PREVIOUS=HERE/'r566_native_430_shutdown_resume_20261128.py'
PREVIOUS_SHA='9fecf7d1d7de384302a0e2d660804319c4ccb482852eee39b8d67b0ed8b7a6d5'
PARAMETER_REQUEST=HERE.parent/'computations/request-r566-0449-working2048-resume-20261128.json.gz'
PARAMETER_REQUEST_SHA='196887723f900fe96237e5e40a83f8b6aac93f7d6095f7fc187c67469a2a1a5d'
ORIGINAL_REQUEST=HERE.parent/'computations/request-r566-native-430-shutdown-resume-20261128.json.gz'
ORIGINAL_REQUEST_SHA='13287fb1992b576dfb7f9f3c41e65913a275def60071e18c1a4df2476134e834'
ORIGINAL_INPUT_SHA='a04d1b347b0648c224395f98b212c2b7c5b5478a4d25c44a5bccb38e3672e2b5'
INPUT_SHA='4c4eb424589e9608228b09ef6328474634cff15dbf5668b45d95d3904fc08af4'
TERMINAL_SHA='2b5a4bde6b618fe1f08248d8f2a89c63cba46422c540872442808f14e0839d49'
Q_SHA='34aa27480d48bba39030b7fb88104398c0570f2dc74dbdd11f4f7ba2adcb9597'
SCHEMA='r692-actual34aa-original-working-jacobian-continuation-v1'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def literal(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()


def binary64(values):
    return digest(struct.pack('<'+'d'*len(values),*values))


def source_input(args):
    raw=args.source_state_json.encode()
    if digest(raw)!=INPUT_SHA or digest(PARAMETER_REQUEST.read_bytes())!=PARAMETER_REQUEST_SHA:
        raise ValueError('The actual continuation input or previous parameters changed')
    previous=json.loads(gzip.decompress(PARAMETER_REQUEST.read_bytes()))
    if any(getattr(args,k)!=v for k,v in previous['common_parameters'].items()):
        raise ValueError('The original full physical and native working parameters differ')
    data=json.loads(raw)
    terminal=data['required_terminal_fields']
    if data['schema']!=SCHEMA or digest(literal(terminal))!=TERMINAL_SHA:
        raise ValueError('The required true terminal fields differ')
    q=terminal['actual_retained_q']
    nodes=terminal['actual_complete_required_radial_nodes']
    fine=terminal['actual_required_fine_radial_nodes']
    qualified=terminal['retained_qualification_fine_radial_nodes']
    peaks=terminal['actual_complete_required_peak_orbits']
    working=terminal['actual_working_field_orbit_rows']
    pending=terminal['recorded_unapplied_physical_peak_orbits']
    pending_work=terminal['recorded_unapplied_working_rows']
    qual=terminal['actual_retained_qualification']
    trial=terminal['last_trial_not_implicitly_accepted']
    trust=terminal['actual_backend_local_trust']
    cp=terminal['actual_curvature_checkpoint']
    trace=data['unpaid_operator_trace']
    anchor=terminal['current_backend_anchor_and_working_library']
    costs=data['current_source_cost_without_duplicating_prior']['counts']
    if (data['origin']['run_id']!=46140899878 or data['origin']['job_id']!=140966372389
            or data['origin']['original_FINAL_sha256']!='04944abc482aea081ebae869326c354ff4ae82860afe879ac73099f1457a3325'
            or len(q)!=81 or binary64(q)!=Q_SHA or terminal['actual_q_binary64_sha256']!=Q_SHA
            or terminal['reason']!='cooperative_clock_or_unresolved_localizer_checkpoint'
            or (len(nodes),len(fine),len(qualified),len(peaks),len(working),len(pending),len(pending_work))
                !=(973,1948,1940,2173,1372,0,0)
            or not set(nodes).issubset(fine) or not set(qualified).issubset(fine)
            or binary64(fine)!=terminal['actual_required_fine_radial_nodes_binary64_sha256']
            or binary64(qualified)!=terminal['retained_qualification_fine_radial_nodes_binary64_sha256']
            or qual['accepted_eta_max']!=.1847597090521258 or qual['accepted_geometry_violation_max']!=0.
            or (qual['radial_nodes'],qual['theta_nodes'],terminal['actual_uniform_angles_and_FFT_nodes'])!=(1940,3072,1536)
            or not terminal['current_complete_library_values_known_for_retained_q']
            or terminal['post_backend_trust_decision_completed'] or terminal['proposed_trust_not_yet_adopted']
            or trust!=.45050811767578125 or terminal['proposed_next_local_trust']!=trust
            or terminal['outer']!=18 or terminal['phase']!='metric' or terminal['last_backend'] is not None
            or anchor['initial_q_binary64_sha256']!=Q_SHA or anchor['actual_trust']!=trust
            or anchor['working_rows']!=1372 or anchor['initial_epigraph']!=.1847597190521258
            or terminal['retained_working_feasible_base_extra']!=anchor['initial_epigraph']
            or trial['outer']!=17 or not trial['accepted'] or trial['q_binary64_sha256']!=Q_SHA
            or trial['complete_required_scalar_rows']!=3445154 or trace['actual_outer18_scalar_rows']!=3459338
            or not all(trial[k] for k in ('full_coarse_completed','full_fine_completed','full_localization_completed'))
            or (trace['outer18_paid_direction_blocks'],trace['outer18_paid_working_value_arrays'],trace['outer18_paid_complete_J'],trace['outer18_native_calls'])!=(40,1,0,0)
            or len(cp['actual_native_or_prepared_packed_LDL'])!=3403 or cp['dimension']!=82
            or len(cp['pending_frozen_multiplier_secant']['nonzero_multipliers'])!=27
            or cp['payload_without_this_receipt']['sha256']!='9f9d03efb48a910d5f35a711741fc7c54363f25b204a83245de150d78c1fa930'
            or costs['accepted_metric_steps']!=8 or costs['outer_completed']!=18):
        raise ValueError('Actual retained curve, qualified versus required grids, pending operator or native seed differs')
    if digest(ORIGINAL_REQUEST.read_bytes())!=ORIGINAL_REQUEST_SHA:
        raise ValueError('Original physical contract request changed')
    original=json.loads(gzip.decompress(ORIGINAL_REQUEST.read_bytes()))
    saved=original['lanes']['rounded-core-B030-native-430-shutdown-resume']['source_state_json'].encode()
    if digest(saved)!=ORIGINAL_INPUT_SHA:
        raise ValueError('Original physical contract literal changed')
    original=json.loads(saved)
    props,geo=original['physical_parameters'],original['geometry_parameters']
    if (digest(literal(props))!='4fa67643c13c83e4968938a0185720522c5fb7e1349bb26c78c4af2e27f33798'
            or digest(literal(geo))!='b733187ae8b75a48b2bc386bc7b8cd23fd1d62f52c51cb193320e22d8e5b861c'):
        raise ValueError('Original physical family or acceptance geometry changed')
    source={
        'origin':data['origin'],
        'source_last_backend_extra':terminal['retained_working_feasible_base_extra'],
        'source_last_backend_required_scalar_rows':trace['actual_outer18_scalar_rows'],
        'unpaid_operator_trace':trace,
        'source_external_shutdown_resume_receipt':terminal['source_external_runner_shutdown_resume_receipt'],
        'source_cost_ledger':{
            'source_run':46140899878,'source_job':140966372389,
            'actual_new_disjoint_source_cost':data['current_source_cost_without_duplicating_prior'],
            'prior_ledger_bound_request':str(PARAMETER_REQUEST.relative_to(HERE.parents[2])),
            'prior_ledger_bound_request_sha256':PARAMETER_REQUEST_SHA,
            'prior_ledger_preserved_without_repeated_raw_copy':True,
            'source_original_FINAL_sha256':data['origin']['original_FINAL_sha256'],
            'recorded_chain_scientific_seconds_lower_bound':data['recorded_chain_scientific_seconds_lower_bound'],
            'sum_adds_only_disjoint_source_elapsed_to_earlier_lower_bound':True,
            'recorded_chain_scientific_seconds_is_exact':False,
            'earlier_censored_work_still_unknown':True,
        },
    }
    start={'initial_fine_and_observed_scan':qual,
           'initial_observed_peaks':terminal['actual_retained_observed_peak_summary']}
    return (source,source['origin'],start,driver.hard.Parameters(**props),geo,
            driver.np.asarray(q,dtype=float),driver.np.asarray(nodes,dtype=float),peaks,1536,trust,terminal)


def amended(source):
    begin='    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION",'
    end='    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT", "actual430_accepted_checkpoint_and_executed_tail_library_preserved")'
    definition=source[source.index(begin):source.index(end)+len(end)]
    replacement='''    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION", {"schema":SCHEMA,
        "source_origin":source["origin"],"required_source_state_sha256":digest(raw),
        "physical_parameters":asdict(par),"geometry_parameters":geo,
        "solver_arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "accepted_fine_1940_and_coarse_selection_3459338_reused":True,
        "required_fine_1948_awaits_a_new_actual_trial":True,
        "paid_partial_first_J_counts_without_invented_response_arrays":source["unpaid_operator_trace"],
        "full_H_and_all_27_pending_multipliers_restored":True,
        "all_original_acceptance_and_native_heuristic":CURVATURE_MODEL_IDENTITY})
    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT", "actual34aa_before_required_working_J")'''
    replacements=[
        ('    trust_decision_completed=False\n',
         '    trust_decision_completed=terminal["post_backend_trust_decision_completed"]\n'),
        ('    current_full_library_values_known = True\n',
         '    current_full_library_values_known = terminal["current_complete_library_values_known_for_retained_q"]\n'),
        (definition,replacement),
        ('        for outer in range(args.outer):','        for outer in range(terminal["outer"],terminal["outer"]+args.outer):'),
        ('                # Keep exact old fine coordinates', '''                if outer==terminal["outer"]:
                    if working!=terminal["actual_working_field_orbit_rows"] or backend_anchor_state!=terminal["current_backend_anchor_and_working_library"]:
                        raise ValueError("The original interrupted native anchor, full box or epigraph differs")
                    batches=[o.uniform.s.tolist() for o,_,_,_ in active_rows.batches]
                    if digest(compact(batches).encode())!=source["unpaid_operator_trace"]["actual_outer18_sub_radial_batches_sha256"]:
                        raise ValueError("The exact interrupted working radial subgrids differ")
                # Keep exact old fine coordinates'''),
    ]
    for before,after in replacements:
        if source.count(before)!=1:
            raise ValueError('Original startup seam is not unique')
        source=source.replace(before,after)
    return source


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific execution requires the bound public Actions repository')
    frozen=PREVIOUS.read_bytes()
    if digest(frozen)!=PREVIOUS_SHA:
        raise ValueError('Original complete working loop changed')
    global driver
    driver=types.ModuleType('r692_frozen_original_driver')
    driver.__file__=str(PREVIOUS)
    exec(compile(amended(frozen.decode()),str(PREVIOUS),'exec'),driver.__dict__)
    driver.SCHEMA=SCHEMA
    from r692_unfinished_working_derivatives import InterruptedRows
    driver.WorkingRows=InterruptedRows
    driver.source_input=source_input
    driver.main()


if __name__=='__main__':
    main()

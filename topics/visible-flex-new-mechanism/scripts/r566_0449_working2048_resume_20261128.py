#!/usr/bin/env python3
"""Continue the actual 0449 accepted state and its paid 70-row working exchange."""
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
PARAMETER_REQUEST=HERE.parent/'computations/request-r566-f2dda-peak4096-resume-20261128.json.gz'
PARAMETER_REQUEST_SHA='adde669fde0207d2b29e7e4065ce885b08f83617a356d0f1aa11832b2d6c5ccd'
ORIGINAL_REQUEST=HERE.parent/'computations/request-r566-native-430-shutdown-resume-20261128.json.gz'
ORIGINAL_REQUEST_SHA='13287fb1992b576dfb7f9f3c41e65913a275def60071e18c1a4df2476134e834'
ORIGINAL_INPUT_SHA='a04d1b347b0648c224395f98b212c2b7c5b5478a4d25c44a5bccb38e3672e2b5'
INPUT_SHA='87239a208d6d06a811423a7ab2332425e09b2e620e9ce9d80ed34d1969df9877'
TERMINAL_SHA='c1cce462d379c49a640b3c40feb327d5eaa7a1ca98c096bca8415b93955a9e55'
Q_SHA='0449014ac9ae749a8f55fcf686c2eb2002cd520b2865dff1617a781b8edf4189'
SCHEMA='r566-actual0449-working2048-continuation-v1'


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
    if previous['common_parameters']['maximum_working_rows']!=1024:
        raise ValueError('Wrong previous working capacity')
    if any(getattr(args,k)!=(2048 if k=='maximum_working_rows' else v)
           for k,v in previous['common_parameters'].items()):
        raise ValueError('Only maximum_working_rows changes in this continuation')
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
    if (data['origin']['run_id']!=46134971089 or data['origin']['job_id']!=140948104671
            or data['origin']['original_FINAL_sha256']!='bcaedfa9bd6e5462aee785ad135e63a2af623e75b72b284c7312389e703c1a9c'
            or len(q)!=81 or binary64(q)!=Q_SHA or terminal['actual_q_binary64_sha256']!=Q_SHA
            or terminal['reason']!='working_matrix_capacity_at_new_evidenced_selection'
            or (len(nodes),len(fine),len(peaks),len(working),len(pending),len(pending_work))
                !=(945,1888,2111,1018,0,70)
            or fine!=qualified or not set(nodes).issubset(fine)
            or binary64(fine)!=terminal['actual_required_fine_radial_nodes_binary64_sha256']
            or binary64(qualified)!=terminal['retained_qualification_fine_radial_nodes_binary64_sha256']
            or qual['accepted_eta_max']!=.1884024399936881 or qual['accepted_geometry_violation_max']!=0.
            or (qual['radial_nodes'],qual['theta_nodes'],terminal['actual_uniform_angles_and_FFT_nodes'])!=(1888,3072,1536)
            or not terminal['current_complete_library_values_known_for_retained_q']
            or terminal['post_backend_trust_decision_completed'] or terminal['proposed_trust_not_yet_adopted']
            or trust!=.45050811767578125 or terminal['proposed_next_local_trust']!=trust
            or terminal['outer']!=16 or terminal['phase']!='metric'
            or trial['q_binary64_sha256']!=Q_SHA or not trial['accepted']
            or not all(trial[k] for k in ('full_coarse_completed','full_fine_completed','full_localization_completed'))
            or len(cp['actual_native_or_prepared_packed_LDL'])!=3403 or cp['dimension']!=82
            or cp['payload_without_this_receipt']['sha256']!='2960e78ed4a893c436361bb19f7e8037ff70d681cfafd17ae52172c65f69c88a'
            or data['current_source_cost_without_duplicating_prior']['counts']['accepted_metric_steps']!=9):
        raise ValueError('Actual 0449 state, paid grid, working selection or heuristic H differs')
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
        # The final new coarse scan was paid, but its scalar row count was not
        # printed. This value is only displayed; never borrow the old943 count.
        'source_last_backend_required_scalar_rows':None,
        'source_external_shutdown_resume_receipt':terminal['source_external_runner_shutdown_resume_receipt'],
        'source_cost_ledger':{
            'source_run':46134971089,'source_job':140948104671,
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
        "source_same1888_fine_qualification_and_current_full_values_paid":True,
        "source70_working_rows_waiting_before_new_backend":True,
        "source_current_full_scalar_row_count_unprinted_not_borrowed":True,
        "source_outer16_has_no_backend_J_or_trust_decision_to_replay":True,
        "all_original_acceptance_and_native_heuristic":CURVATURE_MODEL_IDENTITY})
    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT", "actual0449_before_paid70_working_exchange")'''
    replacements=[
        ('    trust_decision_completed=False\n',
         '    trust_decision_completed=terminal["post_backend_trust_decision_completed"]\n'),
        ('    current_full_library_values_known = True\n',
         '    current_full_library_values_known = terminal["current_complete_library_values_known_for_retained_q"]\n'),
        (definition,replacement),
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
    driver=types.ModuleType('r566_0449_frozen_original_driver')
    driver.__file__=str(PREVIOUS)
    exec(compile(amended(frozen.decode()),str(PREVIOUS),'exec'),driver.__dict__)
    driver.SCHEMA=SCHEMA
    driver.source_input=source_input
    driver.main()


if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Continue the accepted B030 f2dda state with capacity for 4096 physical peak orbits."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import struct
import types


HERE = Path(__file__).resolve().parent
PREVIOUS = HERE / 'r566_native_430_shutdown_resume_20261128.py'
PREVIOUS_SHA = '9fecf7d1d7de384302a0e2d660804319c4ccb482852eee39b8d67b0ed8b7a6d5'
REQUEST = HERE.parent / 'computations/request-r566-native-430-shutdown-resume-20261128.json.gz'
REQUEST_SHA = '13287fb1992b576dfb7f9f3c41e65913a275def60071e18c1a4df2476134e834'
CONTRACT_SHA = 'a04d1b347b0648c224395f98b212c2b7c5b5478a4d25c44a5bccb38e3672e2b5'
INPUT_SHA = 'a589b0371db9466c78cd28ecb832f1f30310b9b95e2968f064329ad44a2b7f84'
FINAL_SHA = 'a6f60cae5cd3d6e2099e484e5e38d893acc63cdee655e1f358cf746e0080c642'
Q_SHA = 'f2dda793e7fb7439bc811c72ca32e1a8d090c77a44e11ae10fb79fa06f8e5f81'
REJECTED = 'a61655da963068a18b0ea6ac9cfae624748253eaf0f89def2f2fb1b483dfa51c'
SCHEMA = 'r566-actual-f2dda-peak4096-capacity-continuation-v1'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def literal(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()


def binary64(values):
    return digest(struct.pack('<'+'d'*len(values), *values))


def load_state(args):
    raw = args.source_state_json.encode()
    if digest(raw) != INPUT_SHA or digest(REQUEST.read_bytes()) != REQUEST_SHA:
        raise ValueError('the actual capacity continuation or the complete previous request differs')
    old = json.loads(gzip.decompress(REQUEST.read_bytes()))
    saved = old['lanes']['rounded-core-B030-native-430-shutdown-resume']['source_state_json'].encode()
    if digest(saved) != CONTRACT_SHA:
        raise ValueError('previous physical and geometry input bytes differ')
    original = json.loads(saved)
    if any(getattr(args,k) != (4096 if k=='maximum_extra_peaks' else v)
           for k,v in old['common_parameters'].items()) or old['common_parameters']['maximum_extra_peaks'] != 2048:
        raise ValueError('only the original physical peak capacity can change')
    data = json.loads(raw)
    t = data['complete_original_final']
    q, nodes, fine, qualified = (t[k] for k in ('actual_retained_q','actual_complete_required_radial_nodes',
        'actual_required_fine_radial_nodes','retained_qualification_fine_radial_nodes'))
    peaks, working = t['actual_complete_required_peak_orbits'],t['actual_working_field_orbit_rows']
    pending, pending_work = t['recorded_unapplied_physical_peak_orbits'],t['recorded_unapplied_working_rows']
    curv = t['actual_curvature_checkpoint']
    trial = t['last_trial_not_implicitly_accepted']
    qual = t['actual_retained_qualification']
    trust = t['actual_backend_local_trust']
    if (data['schema'] != SCHEMA or digest(literal(t)) != FINAL_SHA
            or len(literal(t)) != 762199 or t['reason'] != 'complete_physical_library_capacity_checkpoint'
            or len(q) != 81 or binary64(q) != Q_SHA or t['actual_q_binary64_sha256'] != Q_SHA
            or (len(nodes),len(fine),len(qualified),len(peaks),len(working),len(pending),len(pending_work))
                != (916,1834,1814,2046,650,3,25)
            or binary64(nodes) != 'bf77e1425dcae29d72081f29722bafe0d82ffb910dcae349bb794986f0cd901f'
            or binary64(fine) != t['actual_required_fine_radial_nodes_binary64_sha256']
            or binary64(qualified) != t['retained_qualification_fine_radial_nodes_binary64_sha256']
            or not set(qualified).issubset(fine) or not set(nodes).issubset(fine)
            or qual['accepted_eta_max'] != .19280516441859985 or qual['accepted_geometry_violation_max'] != 0
            or (qual['radial_nodes'],qual['theta_nodes'],t['actual_uniform_angles_and_FFT_nodes']) != (1814,3072,1536)
            or t['current_complete_library_values_known_for_retained_q'] or t['proposed_trust_not_yet_adopted']
            or not t['post_backend_trust_decision_completed'] or trust != .45050811767578125
            or trust != t['proposed_next_local_trust'] or t['phase'] != 'metric' or t['outer'] != 2
            or len(curv['actual_native_or_prepared_packed_LDL']) != 3403 or curv['dimension'] != 82
            or binary64(curv['actual_native_or_prepared_packed_LDL']) != 'fcbc551a283b0d64bdc232775ac38ba80b7b8561f3ff0a73d32c70dcae9b7628'
            or len(curv['pending_frozen_multiplier_secant']['nonzero_multipliers']) != 22
            or curv['payload_without_this_receipt']['sha256'] != '249c0c14760aeb87ae9fc4d5e5bcf709477a78754e7e8a9755dcc9080f625540'
            or trial['q_binary64_sha256'] != REJECTED or trial['accepted']
            or not all(trial[k] for k in ('full_coarse_completed','full_fine_completed','full_localization_completed'))
            or trial['reason'] != 'complete_qualified_trial_without_strict_actual_improvement'
            or t['cost']['counts']['accepted_metric_steps'] != 1):
        raise ValueError('the actual f2dda qualification, capacity, final H or rejected source point differs')
    props = original['physical_parameters']
    geo = original['geometry_parameters']
    if (digest(literal(props)) != '4fa67643c13c83e4968938a0185720522c5fb7e1349bb26c78c4af2e27f33798'
            or digest(literal(geo)) != 'b733187ae8b75a48b2bc386bc7b8cd23fd1d62f52c51cb193320e22d8e5b861c'):
        raise ValueError('original physical or geometry parameters differ')
    cost = t['cost']
    source = {'origin':data['origin'],
        'source_last_backend_extra':t['retained_working_feasible_base_extra'],
        'source_external_shutdown_resume_receipt':t['source_external_runner_shutdown_resume_receipt'],
        'source_cost_ledger':{'source_run':46132003244, 'source_job':140939000737,
            'complete_actual_source_cost':cost, 'source_FINAL_JSON_sha256':FINAL_SHA,
            'source_reason':t['reason'], 'prior_capacities_do_not_invalidate_old_costs':True,
            'source_actual_curvature_cost':curv['cost'],
            'recorded_chain_scientific_seconds_lower_bound':
                cost['prior_cost_ledger']['recorded_chain_scientific_seconds_lower_bound']+cost['elapsed_seconds'],
            'sum_adds_only_disjoint_source_elapsed_to_earlier_lower_bound':True,
            'recorded_chain_scientific_seconds_is_exact':False,'earlier_censored_work_still_unknown':True}}
    start = {'initial_fine_and_observed_scan':qual,'initial_observed_peaks':t['actual_retained_observed_peak_summary']}
    return source,props,geo,q,nodes,peaks,trust,t,start


def source_input(args):
    source,props,geo,q,nodes,peaks,trust,t,start = load_state(args)
    return (source,source['origin'],start,driver.hard.Parameters(**props),geo,
            driver.np.asarray(q,dtype=float),driver.np.asarray(nodes,dtype=float),peaks,1536,trust,t)


def amended(source):
    # The original capacity, working exchange, backend, acceptance and cost loop is immutable.
    begin = '    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION",'
    end = '    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT", "actual430_accepted_checkpoint_and_executed_tail_library_preserved")'
    definition = source[source.index(begin):source.index(end)+len(end)]
    new_definition = '''    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION", {"schema":SCHEMA,
        "source_state":json.loads(raw), "source_state_sha256":digest(raw),
        "physical_parameters":asdict(par), "geometry_parameters":geo,
        "solver_arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "source_q_qualified_on_recorded1814_fine_not_current1834":True,
        "source_3_physical_and25_working_pending_unapplied":True,
        "source_full_library_values_known":current_full_library_values_known,
        "source_completed_trust_decision":trust_decision_completed,
        "original_all_row_family_acceptance_and_native_heuristic":CURVATURE_MODEL_IDENTITY})
    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT", "actual_f2dda_capacity_checkpoint_before_pending_exchanges")'''
    changes = (
        ('    trust_decision_completed=False\n','    trust_decision_completed=terminal["post_backend_trust_decision_completed"]\n'),
        ('    current_full_library_values_known = True\n','    current_full_library_values_known = terminal["current_complete_library_values_known_for_retained_q"]\n'),
        ('    known_scalar_rows = source["source_last_backend_required_scalar_rows"]\n',
         '    known_scalar_rows = None  # newly enlarged complete library has no paid value count at this q\n'),
        (definition, new_definition),
    )
    for old,new in changes:
        if source.count(old) != 1:
            raise ValueError('the frozen B030 source lacks its unique startup seam')
        source=source.replace(old,new)
    return source


def main():
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise RuntimeError('all B030 scientific work belongs to the bound public Actions repository')
    frozen=PREVIOUS.read_bytes()
    if digest(frozen) != PREVIOUS_SHA:
        raise ValueError('the frozen B030 native continuation changed')
    global driver
    driver=types.ModuleType('r566_f2dda_frozen_driver')
    driver.__file__=str(PREVIOUS)
    exec(compile(amended(frozen.decode()),str(PREVIOUS),'exec'),driver.__dict__)
    driver.SCHEMA=SCHEMA
    driver.source_input=source_input
    driver.main()


if __name__=='__main__':
    main()

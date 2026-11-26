#!/usr/bin/env python3
"""Complete saved B030 angular brackets and lift only an independent metric e.

The localization is the bound original four-orbit objective on the identical
q/fine-grid/oracle.  No previously completed bracket or fine scan is replayed.
The helper itself does not accept a physical state or alter a backend array.
"""
import hashlib
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize_scalar

PARENT_SHA = '8cf64c40015350fca09dca3194b6c081078210d4d9146d9369922e8be7cc6930'
if hashlib.sha256(Path(__file__).with_name('r566_backend_preserving_backtrack_20261127.py').read_bytes()).hexdigest() != PARENT_SHA:
    raise RuntimeError('source B030 backend implementation differs')
from r566_backend_preserving_backtrack_20261127 import old,hard


def lift_epigraph(value, required_increment):
    """Return a distinct array and a recorded lift; never modify raw SLSQP x."""
    candidate = np.asarray(value,dtype=float).copy()
    needed = max(0.,float(required_increment))
    if not needed > 0:
        return candidate,0.
    guard = 32*np.finfo(float).eps*max(1.,abs(float(candidate[-1])),needed)
    candidate[-1] = float(candidate[-1])+needed+guard
    return candidate,float(candidate[-1]-value[-1])


def minimum_by_group(rows,values):
    result = {}
    for descriptor,value in zip(rows,values):
        name = descriptor['field']
        result[name] = min(result.get(name,float('inf')),float(value))
    return result


def geometry_minimum(groups):
    return min(value for name,value in groups.items() if not name.startswith('metric_'))


def metric_minimum(groups):
    return min((value for name,value in groups.items() if name.startswith('metric_')),default=0.)


def localize_saved_brackets(oracle,state,saved,scope,mean_floor,det_floor,margin,
                            deadline,angle_tolerance=1e-10,batch_size=512):
    """Finish exactly the saved, all-unprocessed 1353 original brackets.

    The source fine/coarse/nested observations remain paid, separate inputs.
    Reconstructing this oracle/FFT state is new necessary work and is charged
    by the caller's same OracleLedger.  We do not enumerate candidates again.
    """
    started = time.monotonic()
    qsha = hashlib.sha256(state.q.tobytes()).hexdigest()
    nt = oracle.uniform.nt
    if (qsha != scope['q_binary64_sha256'] or state.oracle_identity != scope['oracle_identity']
            or nt != scope['full_observation_FFT_nodes']
            or oracle.uniform.s.tolist() != scope['full_observation_radial_nodes']
            or len(saved) != scope['unresolved_candidate_count'] or batch_size < 1):
        raise ValueError('saved unfinished brackets do not belong to this exact q/oracle/grid')
    for item in saved:
        row,col = item['radial_index'],item['angular_index']
        edge = col == 0 or col == nt//4
        if (not 0 <= row < oracle.uniform.nr or not 0 <= col <= nt//4
                or float(oracle.uniform.s[row]) != item['s']
                or item['boundary_orbit_point'] != edge
                or float(oracle.uniform.theta[col if edge else col-1]) != item['bracket_left']
                or float(oracle.uniform.theta[col if edge else col+1]) != item['bracket_right']):
            raise ValueError('saved original bracket coordinates changed')
    peaks,evaluations,batches_started,batches_completed = [],0,0,0

    def receipt(checkpoint,message=None):
        remaining = saved[len(peaks):]
        unresolved = len(remaining)+sum(not p['localizer_success'] for p in peaks)
        result = {'status':'scientific_clock_checkpoint_with_remaining_brackets' if checkpoint
                           else 'observed_brackets_localized',
            'candidate_count':len(saved),'completed_candidate_count':len(peaks),
            'unresolved_candidate_count':unresolved,'remaining_unprocessed_candidates':remaining,
            'batch_size':batch_size,'batches_started':batches_started,'batches_completed':batches_completed,
            'clock_checkpoint':checkpoint,'clock_message':message,'peaks':peaks,'evaluations':evaluations,
            'elapsed_seconds':time.monotonic()-started,'q_binary64_sha256':qsha,
            'oracle_identity':state.oracle_identity,'continuous_angular_coverage_certified':False,
            'saved_source_candidates_resumed_without_reenumeration':True,
            'source_completed_candidate_count_was_zero':True}
        if checkpoint:
            hard.emit('THETA_PEAK_LOCALIZER_PARTIAL',{
                **result,'q':state.q.tolist(),'full_observation_radial_nodes':oracle.uniform.s.tolist(),
                'full_observation_FFT_nodes':nt,'completed_peaks_and_remaining_candidates_are_not_a_completed_scan':True})
        return result

    for first in range(0,len(saved),batch_size):
        if time.monotonic() >= deadline:
            return receipt(True,'clock before saved candidate batch')
        batches_started += 1
        stop = min(first+batch_size,len(saved))
        for item in saved[first:stop]:
            row,col = item['radial_index'],item['angular_index']
            center,sampled = float(oracle.uniform.theta[col]),item['sampled_value']
            def objective(theta):
                nonlocal evaluations
                if time.monotonic() >= deadline:
                    raise hard.EndSegment('clock inside original saved angular bracket')
                points = oracle.points([row]*4,old.orbit_angles(theta))
                values = oracle.evaluate(state,points)
                fields = old.peak_fields(values,oracle.uniform.par,mean_floor,det_floor,margin)
                evaluations += 1
                return -float(np.max(fields[item['field']].v))
            try:
                if item['boundary_orbit_point']:
                    theta,value,success = center,-objective(center),True
                else:
                    result = minimize_scalar(objective,bounds=(item['bracket_left'],item['bracket_right']),
                        method='bounded',options={'xatol':angle_tolerance,'maxiter':50})
                    theta,value,success = float(result.x),-float(result.fun),bool(result.success)
                    if value < sampled:
                        theta,value = center,-objective(center)
            except hard.EndSegment as error:
                return receipt(True,str(error))
            peaks.append({'field':item['field'],'s':item['s'],'theta':theta,'value':value,
                          'sampled_value':sampled,'localizer_success':success})
        batches_completed += 1
        hard.emit('THETA_PEAK_LOCALIZER_BATCH',{'q_binary64_sha256':qsha,
            'oracle_identity':state.oracle_identity,'candidate_count':len(saved),'batch_size':batch_size,
            'batch_first':first,'batch_stop':stop,'completed_candidate_count':len(peaks),
            'remaining_candidate_count':len(saved)-len(peaks),
            'cumulative_point_objective_evaluations':evaluations,'elapsed_seconds':time.monotonic()-started,
            'all_candidate_brackets_preserved':True,'source_saved_brackets_are_the_actual_work_queue':True})
    return receipt(False)

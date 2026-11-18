#!/usr/bin/env python3
"""Postprocess saved root traces and three explicitly new original point reads.

No point root, angular evaluate, RHS, flow, or nonlinear tail is rerun here.
Exact Fractions measure rounding of saved binary64 operands only; MP trace
comparisons remain finite printed-value evidence, not ODE error certificates.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import struct
import mpmath as mp
from record_fixed_actual import load, scalar_tree, sha

mp.mp.dps = 140


def identity(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def packed(values):
    return struct.pack('<'+'d'*len(values), *values)


def exact(value):
    return F.from_float(float(value))


def text(value):
    return mp.nstr(value, 28)


def number(value):
    if isinstance(value, str):
        return mp.mpf(value)
    return mp.mpf(float(value))


def roots(events):
    field = start = evaluation = end = stop = None
    rows = []
    for event in events:
        kind = event['event']
        if kind == 'rk_field': field = event
        elif kind == 'root_start': start = event
        elif kind == 'evaluate_start': evaluation = event
        elif kind == 'evaluate_end': end = event
        elif kind == 'root_stop': stop = event
        elif kind == 'root_return':
            if event['roundoffFallback'] or not stop['accepted'] or not evaluation['needJac']:
                raise ValueError('This read-only diagnostic expects the recorded accepted ordinary roots')
            rows.append(dict(field=field, start=start, evaluation=evaluation, end=end, stop=stop))
    return rows


def ratio(a, b):
    denominator = abs(exact(a)+exact(b))
    return float((abs(exact(a))+abs(exact(b)))/denominator) if denominator else None


def term_location(stage, point, mode):
    return dict(stage=stage, profile=point['profile'], step=point['step'],
                field=point['label'], x=float(point['x']), mode=mode)


def best(current, candidate, key):
    if current is None or (candidate[key] is None and current[key] is not None):
        return candidate
    if current[key] is not None and candidate[key] is not None and candidate[key] > current[key]:
        return candidate
    return current


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('point-summary', 'resource', 'log', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists(): raise ValueError('A completed postprocessing record already exists')
    observed = load(a.point_summary)
    for key in ('source_sha256', 'additional_original_root_sources'):
        for path, digest in observed[key].items():
            if sha(path) != digest: raise ValueError('A bound source changed: '+path)
    for key in ('capsule_summary', 'float_summary', 'mp90_summary', 'raw'):
        ref = observed[key]
        if sha(ref['path']) != ref['sha256']: raise ValueError('A bound recorded readout changed')
    resource = load(a.resource)
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] != 0:
        raise ValueError('The three new original roots need actual terminal evidence')
    fresh = load(observed['raw']['path'])
    cs = load(observed['capsule_summary']['path'])
    ms = load(observed['mp90_summary']['path'])
    for ref in (cs['coefficients'], cs['reference'], ms['raw']):
        if sha(ref['path']) != ref['sha256']: raise ValueError('A source trace/capsule changed')
    capsule, original, precise = load(cs['coefficients']['path']), load(cs['reference']['path']), load(ms['raw']['path'])
    stage_results = {}
    for fixture, old, high, new in zip(capsule['fixtures'], original['rows'], precise['rows'], fresh['rows'], strict=True):
        stage = fixture['stage']
        old_roots, high_roots = roots(old['events']), roots(high['events'])
        if len(old_roots) != 64 or len(high_roots) != 64 or new['stage'] != stage:
            raise ValueError('All original recorded roots must stay identified')
        coefficient_map = {(v['profile'], packed([v['x']])): v['coefficients'] for v in fixture['points']}
        zero_ell = zero_moment_minus_L = 0
        all_sterbenz_exact = True
        smallest_nonzero_correction = None
        max_q_cancel = max_flux_cancel = max_linear_momentum_cancel = None
        max_q_ulp_effect = max_p_ulp_effect = None
        for call, root in enumerate(old_roots):
            field, start, evaluation = root['field'], root['start'], root['evaluation']
            g = coefficient_map[(field['profile'], packed([field['x']]))]
            state, L, target, moments = start['state'], evaluation['L'], start['target'], root['end']['moments']
            h = fixture['grid'][field['profile']][field['step']]['h']
            weight = h*(1/6 if field['label'] in ('a','d') else 1/3)
            scale = fixture['normalizationScale']
            for j in range(20):
                m = (j+1)*4
                ell = L[j+1]-target[j+1]
                exact_ell = exact(L[j+1])-exact(target[j+1])
                all_sterbenz_exact = all_sterbenz_exact and exact(ell) == exact_ell
                zero_ell += ell == 0
                zero_moment_minus_L += moments[j+1] == L[j+1]
                if ell:
                    ulps = abs(ell)/math.ulp(target[j+1])
                    candidate = dict(**term_location(stage, field, m), root_call=call,
                                     represented_correction=ell, target=target[j+1],
                                     target_ulp=math.ulp(target[j+1]), correction_over_target_ulp=ulps)
                    if smallest_nonzero_correction is None or ulps < smallest_nonzero_correction['correction_over_target_ulp']:
                        smallest_nonzero_correction = candidate
                Q, momentum = state[j], state[20+j]
                p_shape = g['pNumerator'][j]*Q/g['pDenominator']
                qA, qB = (m*m-4)*Q, g['qLNumerator']*L[j+1]/g['r3']
                fluxA, fluxB = -m*L[j+1], (m*m-1)*p_shape
                flux = fluxA+fluxB
                pa, pb = 4*g['sigma']*momentum, g['fluxPrefactor']*m*flux
                for name, first, second in (('q',qA,qB),('flux',fluxA,fluxB),('p_linear',pa,pb)):
                    candidate = dict(**term_location(stage, field, m), root_call=call,
                        first=first,second=second,rounded_sum=first+second,
                        exact_sum_of_saved_operands=float(exact(first)+exact(second)),
                        addition_rounding=float(exact(first+second)-exact(first)-exact(second)),
                        cancellation_ratio=ratio(first,second))
                    if name=='q': max_q_cancel=best(max_q_cancel,candidate,'cancellation_ratio')
                    elif name=='flux': max_flux_cancel=best(max_flux_cancel,candidate,'cancellation_ratio')
                    else: max_linear_momentum_cancel=best(max_linear_momentum_cancel,candidate,'cancellation_ratio')
                ulp_L = math.ulp(L[j+1])
                q_effect = abs(weight*g['sigma']*g['qLNumerator']/g['r3'])*ulp_L/scale
                p_effect = abs(weight*g['fluxPrefactor']*m*m)*ulp_L/scale
                for name,value in (('q',q_effect),('p',p_effect)):
                    candidate=dict(**term_location(stage,field,m),root_call=call,L=L[j+1],L_ulp=ulp_L,
                                   first_stage_weight=weight,normalizationScale=scale,
                                   single_L_ulp_weighted_linear_piece=value,
                                   divided_by_original_gate=value/capsule['original_tail_gate'])
                    if name=='q':max_q_ulp_effect=best(max_q_ulp_effect,candidate,'single_L_ulp_weighted_linear_piece')
                    else:max_p_ulp_effect=best(max_p_ulp_effect,candidate,'single_L_ulp_weighted_linear_piece')
        first = old_roots[0]
        high_first = high_roots[0]
        if (packed(new['L']) != packed(first['evaluation']['L']) or packed(new['moments']) != packed(first['end']['moments']) or
                packed(new['target']) != packed(first['start']['target']) or new['originalErr'] != first['stop']['err']):
            raise ValueError('New root read is not the original saved first root')
        with mp.workdps(90):
            same_input = all(mp.mpf(value) == mp.mpf(float(fixed)) for value,fixed in zip(high_first['start']['state'],fixture['initial42'],strict=True))
        if not same_input: raise ValueError('MP first root input is not the same exact original binary64 input')
        additions=[]
        correction_errors=[]
        hidden_residuals=[]
        for j in range(21):
            L,target,quad,moments=(new[key][j]for key in('L','target','quad','moments'))
            add_round=exact(moments)-exact(L)-exact(quad)
            stable_exact=exact(L)-exact(target)+exact(quad)
            ulp_L=math.ulp(L)
            additions.append(dict(component=j,physical_mode=4*j,
                L=L,target=target,newly_captured_quad=quad,
                exact_addition_rounding=float(add_round),rounding_over_L_ulp=float(add_round/exact(ulp_L)),
                quad_over_L_ulp=abs(quad)/ulp_L,
                rounded_original_residual=new['originalResidual'][j],
                exact_residual_of_represented_L_and_new_quad=float(stable_exact),
                original_moments_equal_L=moments==L))
            if new['originalResidual'][j]==0 and stable_exact:
                hidden_residuals.append(additions[-1])
            mp_L=number(high_first['evaluation']['L'][j]);mp_target=number(high_first['start']['target'][j])
            correction_errors.append(dict(component=j,physical_mode=4*j,
                L_error=text(number(L)-mp_L),target_error=text(number(target)-mp_target),
                represented_ell_error=text(number(L)-number(target)-(mp_L-mp_target)),
                L_error_over_L_ulp=text((number(L)-mp_L)/number(ulp_L))))
        largest_add=max(additions,key=lambda row:abs(row['exact_addition_rounding']))
        largest_hidden=max(hidden_residuals,key=lambda row:abs(row['exact_residual_of_represented_L_and_new_quad'])) if hidden_residuals else None
        largest_L_error=max(correction_errors,key=lambda row:abs(mp.mpf(row['L_error'])))
        exact_norm=max(abs(exact(new['L'][j])-exact(new['target'][j])+exact(new['quad'][j])) for j in range(21))
        stage_results[str(stage)]=dict(
            saved_accepted_root_count=64, saved_nonmean_components=1280,
            represented_L_minus_target_zero_components=zero_ell,
            saved_moments_equal_L_components=zero_moment_minus_L,
            all_recorded_L_minus_target_subtractions_exact_as_binary_rationals=all_sterbenz_exact,
            smallest_nonzero_represented_correction=smallest_nonzero_correction,
            maximum_q_derivative_inside_cancellation=max_q_cancel,
            maximum_linear_flux_cancellation=max_flux_cancel,
            maximum_linear_momentum_piece_cancellation=max_linear_momentum_cancel,
            maximum_single_L_ulp_q_weighted_linear_piece=max_q_ulp_effect,
            maximum_single_L_ulp_p_weighted_linear_piece=max_p_ulp_effect,
            local_sensitivity_scope='A diagnostic of the displayed linear RHS term times one original RK weight, divided by the original stage scale. It omits implicit root/flux derivatives, other terms, and propagation through later RK fields/steps; it is not an error bound or complete Jacobian sensitivity.',
            fresh_first_point=dict(
                scope='All quad and full RHS operand data were newly observed by the bound three-root source, not inferred from old moments-L.',
                first_input_matches_original_and_MP=True,
                original_relative_residual=new['originalErr']/new['scale'],
                exact_represented_residual_with_new_quad_relative=float(exact_norm/exact(new['scale'])),
                zero_original_residual_but_nonzero_exact_represented_count=len(hidden_residuals),
                largest_moment_addition_rounding=largest_add,
                largest_hidden_represented_residual=largest_hidden,
                largest_L_error_to_MP90_same_input=largest_L_error,
                coefficient_product_identity_difference=float(exact(new['coefficientPoint']['coefficients']['fluxPrefactor'])*
                    exact(new['coefficientPoint']['coefficients']['targetFactor'])-exact(new['coefficientPoint']['coefficients']['sigma'])),
                new_quad_sha256=hashlib.sha256(packed(new['quad'])).hexdigest(),
                new_derivative42_sha256=hashlib.sha256(packed(new['originalDerivative42'])).hexdigest()))
    output=dict(
        confidence='Finite arithmetic/source evidence. No continuous error bound or new solution.',
        collector=identity(__file__), helper_sha256=sha(Path(__file__).with_name('record_fixed_actual.py')),
        point_summary=identity(a.point_summary),new_point_raw=observed['raw'],
        capsule_summary=observed['capsule_summary'],float_summary=observed['float_summary'],mp90_summary=observed['mp90_summary'],
        source_sha256=observed['source_sha256'],additional_original_root_sources=observed['additional_original_root_sources'],
        stages=stage_results,
        scope='Saved root trace postprocessing plus exactly three newly observed original first point roots and their original RHS. The old traces did not contain quad, so moments-L is never presented as an old quad observation.',
        changed_formulas_executed=False,new_flow_evaluations=0,tail_solve_invoked=False,production_changed=False,
        observer=scalar_tree(resource),observer_identity=identity(a.resource),execution_log=identity(a.log),
        future_equivalent_formula='For the frozen coefficients, represent L=target+ell and evaluate residual ell+quad(target+ell,Q). The same real root Jacobian is I+Dquad. Split RHS into the literal frozen-coefficient linear part and ell/nonlinear flux correction; do not replace independently rounded pref*targetFactor by sigma.',
        plan_status='No shifted-root or new-flow algorithm has been executed in this record. The next isolated implementation must preserve the original root tolerance/halving/domain rules, then compare its stage outputs with the frozen MP readout rather than selecting by fixed-target residual alone.',
        data_policy='Only source/input/output hashes and named scalar extrema are published; full root/RHS arrays and traces stay scratch-only.')
    encoded=json.dumps(output,ensure_ascii=False,indent=2)+'\n'
    if len(encoded.encode())>=100000:raise ValueError('Compact record exceeds100KB')
    a.out.write_text(encoded)
    print(json.dumps(dict(bytes=a.out.stat().st_size,sha256=sha(a.out))))


if __name__=='__main__':main()

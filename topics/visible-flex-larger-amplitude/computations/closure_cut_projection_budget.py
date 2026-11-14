#!/usr/bin/env python3
"""Compose the paid m2 cut mismatch with the paid two-cell outer flow.

This is exact Fraction arithmetic on saved enclosures, with no new flow.
It is a partial height-port budget at nodes11/10, not the actual complete
outer Schur problem. An upper budget above1 does not prove nonexistence.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted),2026-11-12.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import resource
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dyadic(v):
    m,e=int(v['mantissa']),int(v['binary_exponent'])
    return Fraction(m)*(2**e if e>=0 else Fraction(1,2**(-e)))


def endpoints(v):
    lo,hi=dyadic(v['lower']),dyadic(v['upper'])
    if lo>hi:raise ValueError('An outward interval is reversed')
    return lo,hi


def magnitude(v):
    lo,hi=endpoints(v)
    return max(abs(lo),abs(hi))


def positive_lower(v):
    lo,hi=endpoints(v)
    if lo>0:return lo
    if hi<0:return -hi
    raise ArithmeticError('The actual projective height chart was not paid')


def floor_log2(v):
    if v<=0:raise ValueError('A logarithm requires a positive number')
    k=v.numerator.bit_length()-v.denominator.bit_length()
    if v<(Fraction(2**k) if k>=0 else Fraction(1,2**(-k))):k-=1
    return k


def record(v):
    return dict(numerator=str(v.numerator),denominator=str(v.denominator),
                decimal_diagnostic=format(float(v),'.17g'),
                exact_floor_log2=floor_log2(v) if v>0 else None)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('cut','outer-flow','out'):p.add_argument('--'+name,type=Path,required=True)
    args=p.parse_args();start=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh partial-port budget')
    cut=json.loads(args.cut.read_text());flow=json.loads(args.outer_flow.read_text())
    if not cut['all_gates'] or not all(cut['checks'].values()) or not flow['finite_background_flow_complete']:
        raise ValueError('The actual cut and the complete requested outer range must be paid')
    if flow['start_physical_node']!=12 or flow['cells_completed']!=[11,10]:
        raise ValueError('This diagnostic is specifically the paid two-cell outer range')
    b0=next(x for x in cut['B0'] if x['mode']==2)
    initial=next(x for x in flow['initial_b0_rows'] if x['mode']==2)
    if initial['mu11_true_linear_slope']!=b0['Xi_mu11_over_Q']:
        raise ValueError('The true initial line does not have the same exact input enclosure')
    for key in set(cut['input_hashes'])&set(flow['input_hashes']):
        if cut['input_hashes'][key]!=flow['input_hashes'][key]:raise ValueError('A shared source changed')
    mu0,mu1=endpoints(cut['outer_mu11']);mf0,mf1=endpoints(flow['global_mu_star'])
    if max(mu0,mf0)>min(mu1,mf1) or mu0<=0:raise ValueError('The global mu11 conventions do not overlap')
    blo,bhi=endpoints(cut['true_radius']);wlo,whi=endpoints(cut['true_w'])
    sqrt12lo=Fraction(3464101615137754,10**15)
    if not 0<sqrt12lo*sqrt12lo<12:raise ArithmeticError('The exact square-root lower is invalid')
    inverse_K_to_Xi=bhi**4*whi**2/(sqrt12lo*mu0)
    axislo,axis=endpoints(b0['canonical_Q_axis'])
    if axislo!=axis or b0['canonical_Q_axis_log2']!=-193:raise ValueError('The actual response-based m2 axis changed')
    derivative=next(x for x in cut['nonlinear_derivative_columns'] if x['input_mode']==2)
    mant,ex=derivative['low_K_output_coefficient_caps'][0]
    coefficient_cap=Fraction(mant)*(2**ex if ex>=0 else Fraction(1,2**(-ex)))
    beta_names=['linear_reference_minus_saved_candidate_K','auxiliary_low_correction_K','full_head_low_correction_K','complete_low_K']
    budgets={k:endpoints(cut['beta']['outer'][k])[1] for k in beta_names}
    rows=[]
    for cell in flow['cell_rows']:
        m=next(x for x in cell['modes'] if x['mode']==2)
        if not m['b0_endpoint']['height_chart_excludes_zero']:raise ArithmeticError('The paid B0 chart includes0')
        # For m2, u=m^2-4=0 exactly. Q and Xi coincide with the
        # global gauge variables; the endpoint r^4 cancels in the quotient.
        phi12=magnitude(m['global_gauge_fundamental_matrix'][0][1])
        b0Q=positive_lower(m['b0_endpoint']['Q'])
        ratio=phi12/b0Q
        normalized_factor=ratio*inverse_K_to_Xi/axis
        components={k:record(normalized_factor*v/3) for k,v in budgets.items()}
        radius_needed=normalized_factor*budgets['complete_low_K']/3
        remaining_derivative=normalized_factor*coefficient_cap
        rows.append(dict(cell=cell['cell'],endpoint_physical_node=cell['endpoint_physical_node'],mode=2,
            phi_Q_from_initial_Xi_absolute_upper=record(phi12),B0_Q_absolute_lower=record(b0Q),
            pure_momentum_to_Q_parameter_ratio_upper=record(ratio*inverse_K_to_Xi),
            normalized_upper_components=components,
            current_total_upper_budget=record(radius_needed),
            sufficient_cut_Wsigma1_beta_to_fit_one_parameter_axis=record(3/normalized_factor),
            nonlinear_DeltaB_m2_to_m2_diagonal_upper=record(remaining_derivative),
            current_upper_budget_below_one=radius_needed<1,
            nonlinear_diagonal_upper_below_one=remaining_derivative<1))
    result=dict(status='Exact saved-enclosure composition for m2 partial height ports only',author='exact_closure (GPT-6 Astra Pro, AI-assisted)',
        exact_arithmetic='All rational values are exact Fraction quotients of outward dyadic endpoints. Decimal strings are diagnostics; exact_floor_log2 is integer-checked.',
        equation='For m2, a_eff = -Phi12*deltaXi/B0_Q and deltaXi=b^4*w^2*deltaK/(sqrt12*mu11). The shared W_sigma,1 beta gives |deltaK_2|<=beta/3; the extra exp(-2sigma)<1 is conservatively dropped.',
        original_height_identity='deltaQ_low=0 before the corrective parameter is chosen',
        exact_m2_gauge_exponent=0,canonical_m2_axis=record(axis),K_to_Xi_upper=record(inverse_K_to_Xi),
        rows=rows,
        physical_or_exact_solution_failure_claimed=False,
        actual_outer_end_constraint_included=False,outer_continuous_defect_included=False,
        other_low_modes_included=False,full_high_frequency_feedback_included=False,
        complete_Schur_inverse_paid=False,
        input_hashes={str(args.cut):sha(args.cut),str(args.outer_flow):sha(args.outer_flow)},source_sha256=sha(__file__),
        elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if result['peak_RSS_KiB']>40*1024:raise MemoryError('The tiny Fraction diagnostic exceeded40MiB')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='done',rows=len(rows),upper_budgets=[x['current_total_upper_budget']['decimal_diagnostic'] for x in rows],
                         derivative_diagonals=[x['nonlinear_DeltaB_m2_to_m2_diagonal_upper']['decimal_diagnostic'] for x in rows],
                         RSS_KiB=result['peak_RSS_KiB'],sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()

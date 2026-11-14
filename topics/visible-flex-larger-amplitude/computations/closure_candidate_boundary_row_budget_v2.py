#!/usr/bin/env python3
"""Combine actual R78 head rows with candidate-source rows; keep v separate."""
import argparse
import json
from fractions import Fraction
from pathlib import Path
import resource
import time

from closure_split_joint_io_v2 import read,digest
from closure_outer_source_parameter_rows import bounds,point,record


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-rows','inner-head','family','full-family','out'):
        p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args();began=time.monotonic()
    if a.out.exists():
        raise FileExistsError('Use a fresh actual candidate-boundary row budget')
    source,head,family,full=[read(x) for x in (a.source_rows,a.inner_head,a.family,a.full_family)]
    hashes={str(x):digest(x) for x in (a.source_rows,a.inner_head,a.family,a.full_family)}
    if any(not d['all_gates'] for d in (source,head,family,full)):
        raise ValueError('All complete source, true-head and actual parameter gates are required')
    link=family['complete_row_ledger']
    if (link['path']!=str(a.full_family) or link['sha256']!=hashes[str(a.full_family)]
            or link['bytes']!=a.full_family.stat().st_size):
        raise ValueError('The R74 summary must identify the exact full row ledger')
    if set(family)-set(full)!={'complete_row_ledger'}:
        raise ValueError('Unexpected R74 summary-only data')
    if any(family[k]!=full[k] for k in family if k in full):
        raise ValueError('Every shared R74 summary and full-ledger field must agree')
    if (source['input_hashes'].get(str(a.family))!=hashes[str(a.family)]
            or head['input_hashes'].get(str(a.full_family))!=hashes[str(a.full_family)]):
        raise ValueError('The source summary and true-head full ledger must be the identified R74 family')
    if head['parameter_axes']!=family['parameter_axes']:
        raise ValueError('Retain all twenty identical actual input axes')
    radius=bounds(head['interior_parameter_radius'])
    if radius!=(Fraction(3,4),Fraction(3,4)):
        raise ValueError('Retain the actual R78 certified interior parameter radius')
    hrows={r['mode']:r for r in head['actual_selected_boundary_feedback_rows']
           if r['endpoint_physical_node']==10}
    if sorted(hrows)!=[2,4] or [r['mode'] for r in source['rows']]!=[2,4]:
        raise ValueError('Retain exactly the two actually certified output rows')
    result=[]
    for row in source['rows']:
        m=row['mode'];h=hrows[m]
        if bounds(row['actual_R74_axis'])!=bounds(h['output_axis']):
            raise ValueError('The output canonical parameter units differ')
        qsrc=point(row['all20_parameter_block_row_norm'])
        qhead=bounds(h['normalized_inner_nonlinear_feedback']['first_derivative_linf_to_output_upper'])[1]
        centre=point(row['centre_axis_ratio'])
        q=qsrc+qhead;image=centre+radius[0]*q
        result.append(dict(mode=m,source_row=record(qsrc),true_head_nonlinear_row=record(qhead),
            complete_candidate_boundary_row=record(q),centre=record(centre),
            candidate_map_image_at_radius_three_quarters=record(image),
            remaining_unknown_field_value_budget=record(radius[0]-image),
            remaining_unknown_field_Lipschitz_budget=record(1-q),
            candidate_map_strictly_inside=image<radius[0],candidate_row_contracts=q<1))
    gates=dict(same_actual_twenty_parameter_axes_and_fixed_metric=True,
        summary_identifies_full_R74_ledger_by_path_size_and_hash=True,
        every_common_R74_summary_full_field_identical=True,
        actual_R78_true_head_minus_exact_linear_head_rows_used=True,
        actual_full_mean_inverse_source_rows_used=True,
        both_candidate_map_rows_strictly_inside=all(r['candidate_map_strictly_inside'] for r in result),
        both_candidate_map_rows_contract=all(r['candidate_row_contracts'] for r in result),
        unknown_outer_field_effect_not_set_to_zero_in_full_problem=True)
    out=dict(status='Two actual candidate-boundary map rows; unknown outer field remains separate',
        all_gates=all(gates.values()),gates=gates,rows=result,
        interior_parameter_radius=record(radius[0]),
        theorem_scope='For fixed other18 normalized parameters of modulus<=3/4, the candidate-source two-row map has a unique zero in the m2/m4 radius3/4 bidisc. It does not solve the actual outer PDE; N(C_eta+v)-N(C_eta) is an independent remaining operator.',
        full_outer_solution_or_Green_inverse_claimed=False,input_hashes=hashes,
        source_sha256=digest(__file__),supersedes_wrapper_only='closure_candidate_boundary_row_budget.py failed a path guard; no mathematical output from that run',helper_sha256=digest(Path(__file__).with_name('closure_outer_source_parameter_rows.py')),
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),all_gates=out['all_gates'],
        rows=[dict(mode=r['mode'],q=r['complete_candidate_boundary_row']['display'],
                   image=r['candidate_map_image_at_radius_three_quarters']['display']) for r in result],
        peak_RSS_KiB=out['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':
    main()

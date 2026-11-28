#!/usr/bin/env python3
"""Pay R87's grip/reach budget for the actual binary64 cylinder choices.

This exact rational calculation reuses the proved R87/R93 kinematics. It
does not certify any actual unmarked surface, cap, native field, or fixed-g
refinement. In particular float(.005)*2 is slightly greater than 1/100;
that literal extra cost is paid, not silently rounded back to 1/100.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]


def certificate():
    halves = [Q.from_float(.0025), Q.from_float(.005)]
    lengths = [2*v for v in halves]
    unmarked_D = Q(67, 25)
    unmarked_support = Q(87, 1000)
    marker_D_cost = Q(1, 25000)
    marker_support_lower = Q(997, 10000)
    K = Q(123, 10)
    # These two strict rational lower bounds were already proved in R87.
    H_lower = Q(2153439, 4000000)
    held_lower = Q(535357, 1968750)
    D = unmarked_D+lengths[-1]+marker_D_cost
    support = unmarked_support-halves[-1]
    reach = 1/K
    gap = lengths[-1]-lengths[0]
    margins = dict(grip_diameter=H_lower-D/5,
        whole_image_held=held_lower-D/10,
        support_above_focal_radius=support-reach,
        reach_ratio=reach-Q(3, 100)*D,
        cap_support_above_translated_lower=marker_support_lower-support,
        two_length_activity_factor=gap/2-Q(1, 400),
        exact_halfwidth_sweep=Q.from_float(.675)-Q(67, 100))
    if not all(v>0 for v in margins.values()):
        raise ArithmeticError('The literal cylinder budget did not retain every strict margin')
    if not (halves[0]>0 and lengths[-1]>Q(1, 100)
            and lengths[-1]-Q(1, 100)<Q(1, 10**17)):
        raise ArithmeticError('The actual binary64 cylinder choice changed')
    return dict(status='proved_literal_cylinder_parameter_budget_only',
        actual_half_lengths_exact=list(map(str, halves)),
        actual_full_lengths_exact=list(map(str, lengths)),
        largest_full_length_excess_over_one_hundredth_exact=str(lengths[-1]-Q(1, 100)),
        inherited_unmarked_D_upper_exact=str(unmarked_D),
        inherited_unmarked_support_lower_exact=str(unmarked_support),
        inherited_marker_D_cost_upper_exact=str(marker_D_cost),
        inherited_marker_support_lower_exact=str(marker_support_lower),
        complete_D_upper_with_literal_column_exact=str(D),
        translated_support_lower_exact=str(support),
        inherited_complete_curvature_upper_exact=str(K),
        conditional_complete_reach_lower_exact=str(reach),
        inherited_grip_diameter_strict_lower_exact=str(H_lower),
        inherited_whole_image_held_strict_lower_exact=str(held_lower),
        exact_positive_margins={k:str(v) for k,v in margins.items()},
        ratio_lower_exact=dict(H_diameter=str(H_lower/D),held=str(held_lower/D),
            reach=str(reach/D)),
        two_length_activity_factor_exact=str(gap/2),
        two_length_activity_factor_exceeds_one_four_hundredth=True,
        any_unmarked_surface_or_cap_hypotheses_paid_here=False,
        any_actual_closed_field_or_fixed_metric_refinement_constructed=False,
        final_cylinder_or_marker_choice_selected=False,
        readme_completion_claimed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    out = args.out.resolve()
    if out==REPO or REPO in out.parents:
        raise ValueError('Write the execution receipt outside the source tree')
    if out.exists():
        raise ValueError('Keep the existing exact execution receipt')
    result = certificate()
    result['source'] = dict(path=str(Path(__file__).resolve()),
        sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(status=result['status'],out=str(out),
        positive_margins=list(result['exact_positive_margins']),
        ratios_display_only={key:float(Q(value)) for key,value in result['ratio_lower_exact'].items()})),flush=True)


if __name__ == '__main__':
    main()

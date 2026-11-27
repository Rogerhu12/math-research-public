"""WRA:12 new exact saved-bound combinations for the actual-anchor weak row.

Only rational combinations of already completed constants are used.
No original numerical producer, PDE residual, geometry or signed target
is called.  The12 new comparisons were evaluated once when WRA was derived.
"""
from __future__ import annotations
from fractions import Fraction as F
import json

ROWS=("root_state_and_root_jumps","root_L2_source",
      "strict_L2_source","strict_unweighted_jumps")
COLUMNS=("outer_vertical_frame_C0","outer_vertical_frame_C1_seminorm",
         "outer_vertical_position_C1_seminorm")
SAFE=((86061,6086,2919,8098),(12531,887,441,1180),(4590,325,210,432))
BASE=(94000,6650,3000,8850)


def saved_bounds():
    b=F(9,50)
    U,NI,Jin,q0=F("173.872"),F("11.272695"),F("1.060693"),F(2669,5000)
    root=U*NI/q0
    strict=U*Jin/q0
    position=(F(70053,640),F(11367,800),F(0))
    coordinate=(F(37359,10000),F(171,200),F(5,4))
    comparisons=[]
    for name,C,c,uppers in zip(COLUMNS,position,coordinate,SAFE):
        span=b*C+c
        values=(root*span,root*span*F("0.070711"),
            strict*(b*C*F("0.337")+c*F("0.484")),strict*span)
        for row,value,upper in zip(ROWS,values,uppers):
            comparisons.append({"name":row+"__"+name,"left":str(value),
                "right":str(F(upper)),"strict":value<upper})
    if not all(item["strict"] for item in comparisons):
        raise ValueError("one new actual-anchor weak receiver comparison failed")
    return {
        "kind":"WRA_actual_anchor_complete_weak_height_receiver_v1",
        "new_exact_rational_comparisons":12,"comparisons":comparisons,
        "whole_relative_position_upper":"171/250",
        "whole_relative_position_first_derivative_upper":"37359/12500",
        "complete_position_H1_dual_coefficients":[str(x) for x in position],
        "complete_coordinate_endpoint_coefficients":[str(x) for x in coordinate],
        "source_order":list(ROWS),"anchor_order":list(COLUMNS),
        "fixed_reference_source_coefficients":list(BASE),
        "additional_source_coefficients_by_anchor":[list(x) for x in SAFE],
        "independent_varying_vertical_position_coefficient":"27/8",
        "independent_actual_world_axial_frame_coefficient":"4617/2000",
        "both_means_and_all_Fourier_modes_retained":True,
        "original_weak_root_and_strict_units_retained":True,
        "angular_world_seam_assumed_closed_without_input":False,
        "actual_anchor_C1_values_assigned":False,
        "old_scientific_target_calls":0,
        "TC_completion_or_full_Schur_asserted":False}


def exact_receiver_coefficients(a0,a1,b1):
    """Formal exact nonnegative anchor data, in the original three norms.

    Actual interval consumers should combine the displayed integer matrix
    with their whole outward input bounds; no C1 input is supplied here.
    """
    values=tuple(map(F,(a0,a1,b1)))
    if any(value<0 for value in values):
        raise ValueError("actual anchor seminorm bounds must be nonnegative")
    return tuple(F(BASE[row])+sum((values[col]*SAFE[col][row]
                 for col in range(3)),F(0)) for row in range(4))


if __name__=="__main__":
    print(json.dumps(saved_bounds(),sort_keys=True,indent=2))

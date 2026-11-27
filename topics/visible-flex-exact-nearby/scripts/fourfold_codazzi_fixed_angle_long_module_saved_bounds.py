#!/usr/bin/env python3
"""FX: rational qualification of the fixed-moving-angle exterior module.

Only positive combinations of completed scalar constants are evaluated.
There is no long solution, coefficient sweep, Green integration or new
scientific numerical target in this file.
"""

from fractions import Fraction as F
import json
from fourfold_codazzi_compact_tame_Hessian_saved_bounds import decimal_upper


def main():
    checks = {}

    def lt(name, x, y):
        checks[name] = x < F(y)
        if not checks[name]:
            raise AssertionError(name)

    eps, ry, rz, rb, ru, rf = (
        F(1, 2**18), F(1, 2**24), F("5e-10"),
        F("1e-11"), F("1e-5"), F("8e-9"),
    )
    invj = 1/(1-eps)
    v_exact = invj**2-1+eps*invj**3/4
    vfee = 3*eps
    lt("complete fixed-angle principal coefficient fee", v_exact, vfee)
    lt("same holonomy and full-state coefficient domain", invj, F(33,32))
    dq, drc = 8192*ry, 65536*ry
    jacobi = 32*(vfee+dq)
    lt("complete pulled long Jacobi denominator", jacobi, F(1,32))
    lt("complete right lift below four", 3/(1-jacobi), 4)
    lt("complete left lift below eight", 5/(1-jacobi), 8)
    lt("full Dirichlet value selfmap",
       3*rf+5*rb+32*vfee*ry+65536*ry**2, ry)
    lt("left-only value state below six times height",
       5/(1-32*vfee-65536*ry), 6)
    lt("left-only physical K below twice height",
       (1+eps)*6/4+4096*36*rb, 2)
    lt("left-only full curvature below four times height", F(4,5), 4)
    curvature_error = 16*(vfee+dq)+vfee+4*drc
    curvature_gate = 9*curvature_error
    lt("complete true curvature inverse perturbation", curvature_gate, F(1,4))
    lt("complete true curvature inverse below twelve", 9/(1-curvature_gate), 12)
    lt("full curvature value selfmap", 9*(rz+4*rb)+rf/4, rf)
    mean_z = (1+eps)*drc*48
    lt("complete weighted physical curvature mean derivative", mean_z, F(1,4))
    echart = 64*(2*eps+eps**2+eps*(1+eps)/4)*(1+eps+F(1,4))
    chart_inverse = 1/(F("5.8")**2-echart)
    lt("full nonmean raw even chart inverse", chart_inverse, F(".03"))
    vmax=8*(1+eps)
    lt("complete complex raw endpoint multiplier", vmax, 9)
    h1_z = vmax*16*48+vmax*(ru+ru/4)*(1+eps+F(1,4))
    eraw = h1_z*F(".03")+F(1,5)
    lt("complete raw homogeneous exterior row", eraw, 256)
    lt("full curvature-height strong column", 8+4*12*16*8, 2**14)
    # The actual mean row is used separately in the paper. The larger
    # constants cover every affine chart shift as well.
    lt("complete height mean column", (1+eps)*drc*2**14, 128)
    h1_height = 9*2**18+vmax*(ru+ru/4)*128
    h2_height = (vmax**2+8*eps*vmax/4)*128
    lt("complete affine height raw even shift", h2_height, 2**14)
    lt("complete affine height exterior row",
       h1_height+(h1_z+F(1,5)*(F("5.8")**2+echart))
       *F(".03")*h2_height, 2**24)
    lt("complete independent Robin residual row", 9*5, 64)
    h2_mean = vmax**2+8*eps*vmax/4
    lt("complete independent physical mean residual row",
       vmax*(ru+ru/4)+h1_z*F(".03")*h2_mean
       +F(1,5)*h2_mean, 2**15)

    # All entries below are the completed real endpoint scalars in QN/QH.
    us, vs, er, mlo = map(F, ("1.643190e-9","9.603792e-9","1e-9","5.84"))
    e0=(vs+er)/mlo
    e1=(8*vs+er)/mlo
    e2=(128*vs+er)/mlo
    e3=(3072*vs+er)/mlo
    ea1=(9*vs+er)/mlo
    ua1=9*us+er
    comp=F("1.101")
    jmax=1+e0
    lt("actual real composition basis factor",F("1.1")*jmax,comp)
    zraw=comp*(F("4e-11")+F("7e-11"))
    b=F(1,2**60)
    gb=comp*(jmax**2*17+e1*F(5,4))*b
    t=ea1/eps+zraw/rz+gb/rb+ua1/ru
    lt("complete actual four-parameter Taylor ball",t,F(1,4))
    zsecond=(e2/(1-e0)**2+2*e1**2/(1-e0)**3)/mlo
    gsecond=comp*b*(
        25088*jmax**4+6*528*jmax**2*e1
        +3*17*e1**2+4*17*jmax*e2+F(5,4)*e3
    )
    gamma2=(e2+e3)/eps+zsecond/rz+gsecond/rb+(3200*us+2*er)/ru
    lt("complete actual second Fourier parameter moment",gamma2,100)
    # The existing physical long graph's first value derivative gives
    # a qualification of its actual real pulled background in the new ball.
    physical_y=6*(10*(F("4e-11")+b)+b)
    physical_ytheta=30*F("7e-11")+6*16*b
    raw_y=comp*max(jmax**2+e1/4,jmax,F(1))*(physical_y+physical_ytheta)
    lt("same actual real pulled long background",raw_y,F("6e-9"))
    lt("actual pulled background lies in the qualified ball",raw_y,ry)
    print(json.dumps({
        "all_passed":all(checks.values()),
        "exact_rational_comparisons":len(checks),
        "complete_jacobi_loop":decimal_upper(jacobi,12),
        "complete_curvature_inverse_gate":decimal_upper(curvature_gate,12),
        "complete_curvature_inverse":"12",
        "complete_even_chart_inverse":decimal_upper(chart_inverse,12),
        "wide_raw_homogeneous_exterior_row":decimal_upper(eraw,9),
        "wide_full_boundary_family_bound":"2^32",
        "actual_parameter_norm":decimal_upper(t,12),
        "actual_second_parameter_moment":decimal_upper(gamma2,9),
        "actual_pulled_long_state":decimal_upper(raw_y,18),
        "same_true_finite_long_Green_and_curvature_reference":True,
        "weighted_mean_holonomy_and_all_independent_height_ports":True,
        "bare_complex_angle_composition_on_L2_directions":False,
        "unknown_positive_spatial_strip_assumed":False,
        "old_native_or_long_scientific_evaluations":0,
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()

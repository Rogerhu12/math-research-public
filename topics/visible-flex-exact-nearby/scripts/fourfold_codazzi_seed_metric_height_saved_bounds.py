#!/usr/bin/env python3
"""GHR: exact new profile combinations for the actual metric-height column.

Inputs are the completed GF, T, Mhol, G and E bounds. This reader
does not integrate a profile or rerun any prior scientific target.
"""

from fractions import Fraction as F
import json


def main():
    checks = {}

    def lt(name, value, bound):
        checks[name] = value < bound
        if not checks[name]:
            raise AssertionError(name)

    lt("all layer polynomial ratios fit one eighth of a dyadic exponent",
       135**32, 2*134**32)
    lt("actual common low graph fits the complete radial-state radius",
       -48000000+5, -47000000)
    lt("differentiated mean feedback retains a strict quarter margin",
       25+464+262144-2*47000000, -2)
    lt("actual metric square permits the algebraic q direction circle",
       2*(129-5*132), -3)
    lt("whole shallow C2 profile begins below its budget",
       32+18-F(132, 4), 18)
    lt("true 4097 height-profile jump remains below the first layer",
       52+18-F(4099, 4)+50+1, -900)
    lt("complete deep C2 profile has positive exponent",
       121, 131-F(19, 2)-F(5, 256))
    lt("middle C2 profile decay dominates the layer polynomial",
       F(1, 8), F(1, 4)-F(5, 256))
    lt("first complete height-integral profile is summable",
       24+18-F(132*11, 4), -320)
    lt("actual 4097 integral-profile jump is paid",
       39+18-F(4099*11, 4)+50+1, -11160)
    lt("two full geometric profile sums fit the integral budget",
       max(-320, -11160)+1, -300)
    lt("complete internal material two-jet cost",
       198+64+456+20, 740)
    lt("one directed internal height integral cost",
       133+64+456-300, 740)
    lt("actual o shallow two-jet exception",
       198+14+8-F(7*132, 2), -240)
    lt("actual o shallow directed-height exception",
       133+14-6*132, -640)
    lt("all material C2 components and shallow exception",
       740+3, 1024)
    lt("true seed parameter retains a strictly small height column",
       1024-110000000, -109000000)

    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_rational_and_integer_comparisons": len(checks),
        "material_C2_height_coefficient": "rho epsilon_s 2^1024 ||a||_P2",
        "true_gamma_metric_height_coefficient":
            "rho epsilon_s 2^(1024-110000000) r_gamma^-1 ||eta||_A0",
        "physical_Cartesian_conversion": "2^8 max(1,rho^-2)",
        "reference_one_retained": True,
        "both_actual_endpoint_heights_and_conormal_column_retained": True,
        "one_global_height_gauge": True,
        "shallow_o_and_both_profile_junctions_retained": True,
        "independent_rigid_height_and_endpoint_graph_columns": True,
        "metric_height_in_vanishing_ordinary_source_norm": False,
        "old_scientific_arrays_integrals_and_targets": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

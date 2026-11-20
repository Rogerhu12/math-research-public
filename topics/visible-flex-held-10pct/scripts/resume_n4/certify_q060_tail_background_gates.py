#!/usr/bin/env python3
"""Certify elementary all-domain gates for the q060 valley-4.625 background.

Uses the actual regenerated 512-step binary calibration constants and the
existing true-integral enclosure.  No BVP or nonlinear tail is solved.
The unchanged n>=160 source uses the precise deep-root bracket already
isolated in held10 R21, not an infinite nonlinear extension theorem.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import mpmath as mp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--constants", type=Path, required=True)
    parser.add_argument("--integrals", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.constants.read_text())
    cfg = data["parameters"]
    bounds = json.loads(args.integrals.read_text())
    assert bounds["input_sha256"] == hashlib.sha256(
        args.constants.read_bytes()).hexdigest()
    assert cfg["R"] == 64 and cfg["a"] == 2.75 and cfg["etaPower"] == 1.5
    assert cfg["rCut"] == .3 and cfg["wCut"] == .08 and cfg["width"] == .25
    assert cfg["curvatureBound"] == 8 and cfg["orientation"] == 1
    assert cfg["protectCell"] == 160 and cfg["prefixEnd"] == 15
    assert cfg["capMode"] == "cut-preserving" and cfg["rejoinR20At"] is None
    assert not cfg.get("flatOuterThroughCell", False)
    assert cfg["pulseCaps"] == [[.4, .02]] and cfg["valleyCaps"] == [.1]
    assert cfg["warpWeightLevels"] == [[1, .5, 3, .05, 1]]
    assert cfg["valleyControls"][:6] == [4.625, 2.8125, 4.0625, 5, 5.25, 4.0625]
    assert all(v == 0 for v in cfg["valleyControls"][6:])
    assert cfg["calibrationSteps"] == 512 and cfg["warpSteps"] == 16
    assert cfg["quadratureTolerance"] == 2e-10 and cfg["cuspAwareQuadrature"] is True
    assert all(.5 <= c["calibrationAlpha"] <= 2 for c in data["cells"])
    assert all(c["R"] == 64 for c in data["cells"][16:])
    assert all(c["lengthScale"] == 1 for c in data["cells"])
    mp.mp.dps = 90
    iv = mp.iv
    iv.dps = 60

    def q(x):
        f = Q(x) if isinstance(x, int) else Q.from_float(float(x))
        return iv.mpf(f.numerator)/f.denominator

    def lo(x):
        return mp.make_mpf(x._mpi_[0])

    def hi(x):
        return mp.make_mpf(x._mpi_[1])

    def display(x):
        return {"lower_display": float(lo(x)), "upper_display": float(hi(x))}

    cuff, delta, eta_ratio = q(cfg["rCuff"]), q(cfg["delta0"]), q(cfg["etaRatioAtN0"])
    Y = 6*delta+6*delta*eta_ratio/(1-iv.mpf(2)**(-iv.mpf(3)/2))
    old_cut = cuff*iv.exp(Y/iv.sqrt(12))
    gates = {
        "Y": Y,
        "exp7YoverSqrt12": iv.exp(7*Y/iv.sqrt(12)),
        "two_to_11over4": iv.mpf(2)**(iv.mpf(11)/4),
        "cut_over_oldcut_minus_one": q(cfg["rCut"])/old_cut-1,
        "raw_first_cell_plateau_slope_bound": q(cfg["wCut"])/delta*
            iv.mpf(2)**(-iv.mpf(11)/4)*iv.exp(7*Y/iv.sqrt(12)),
        "outer_last_port_slope_bound": q(cfg["wCut"])*
            iv.exp(7*delta*eta_ratio/iv.sqrt(12)),
        "last_log_jump": iv.ln(delta)+(iv.mpf(11)/4)*iv.ln(2),
        "log_point02": iv.ln(q(.02)),
        "log_four": iv.ln(4),
        "exp_three_over_two": iv.exp(iv.mpf(3)/2),
        "base_Wn_constant": q(cfg["wCut"])/delta*
            iv.mpf(2)**(-iv.mpf(11)/4)*64*iv.exp(7*Y/iv.sqrt(12)),
    }
    assert lo(cuff) > iv.mpf(1)/25
    assert hi(Y) < iv.mpf(1)/20
    assert hi(gates["exp7YoverSqrt12"]) < iv.mpf(6)/5
    assert lo(gates["two_to_11over4"]) > 6 and hi(gates["two_to_11over4"]) < 7
    assert lo(gates["cut_over_oldcut_minus_one"]) > 4
    assert hi(gates["raw_first_cell_plateau_slope_bound"]) < 4
    assert hi(gates["outer_last_port_slope_bound"]) < iv.mpf(1)/10
    assert hi(gates["last_log_jump"]) < -3
    assert hi(gates["log_point02"]) < -iv.mpf(19)/5
    assert hi(gates["log_four"]) < iv.mpf(7)/5
    assert lo(gates["exp_three_over_two"]) > 4
    assert hi(gates["base_Wn_constant"]) < 256

    normalization_lo = Q(bounds["positive_exact_normalization"]["lower_exact"])
    radius_lo = Q(bounds["cell0_inner_radius"]["lower_exact"])
    height_hi = Q(bounds["exact_background_height"]["upper_exact"])
    assert normalization_lo > 100
    assert height_hi < Q(259, 10000) < Q(29, 1000)
    angular_cell0 = Q(41, 100)/radius_lo
    assert angular_cell0 < 8
    assert Q(1, 49)/Q(1, 25) < 8
    # Last outer port: r_x/r_old_x >= t+4t^2+(10000/101)(1-t)
    # and the difference from 5 is (1-t)(10000/101-5-4t).
    assert Q(10000, 101) >= 9
    assert Q(7, 10)/(8*Q(1, 25)) < 5
    # Unchanged deep source: W_160=256*2^-280, H_160=241,
    # eta_160>=2^-240/5000 and cuff>1/25.
    deep_wr = (Q(7, 2)*Q(15, 8)*256*Q(1, 2**280)*241*25*5000*2**240
               + 7*256*Q(1, 2**280)*25)
    assert deep_wr < Q(1, 20)
    assert Q(17, 20)**4 > Q(1, 2)
    assert Q(17, 20)*Q(1212, 1205) < 1
    # The protected first port of cell159 is strictly below the cap's
    # inactive threshold .02*exp(-2), and its source derivative is tiny.
    assert hi(iv.exp(2)) < 8
    w159 = Q(256, 2**278)
    assert w159 < Q(1, 400)
    assert 7*w159*25 < 8
    # Optional broad rotational placement window, independent of the actual
    # nonrotational field: z_b in [1/10,32/25].
    support_squared_lo = Q(1, 10)**2/(1+Q(41, 100)**2)
    radius_squared_hi = Q(3, 10)**2+(Q(32, 25)+height_hi)**2
    assert support_squared_lo > Q(87, 1000)**2
    assert radius_squared_hi < Q(67, 50)**2
    result = dict(
        scope=__doc__,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        constants_sha256=hashlib.sha256(args.constants.read_bytes()).hexdigest(),
        integrals_sha256=hashlib.sha256(args.integrals.read_bytes()).hexdigest(),
        all_assertions_passed=True, interval_precision=iv.dps,
        gates={key: display(value) for key, value in gates.items()},
        exact_rational_checks=dict(
            cell0_angular_curvature_upper=str(angular_cell0),
            deep_derivative_upper=str(deep_wr),
            support_squared_lower=str(support_squared_lo),
            centered_radius_squared_upper=str(radius_squared_hi)),
        certified_background=dict(
            height_upper_exact=str(height_hi), slope_upper_exact="41/100",
            principal_curvature_absolute_upper_exact="8",
            cuff_extension="C2 flat background, using the cited deep calibration-root bracket",
            placement_cut_height_interval=["1/10", "32/25"],
            placement_support_lower_exact="87/1000",
            placement_whole_reflected_diameter_upper_exact="67/25"),
        exact_integral_metric_definition=True,
        floating_factory_profile_error_certified=False,
        nonlinear_field_certified=False, complete_surface_certified=False)
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(
        all_assertions_passed=True,
        height_upper=float(height_hi), slope_upper=.41,
        principal_curvature_bound=8,
        cell0_angular_bound=float(angular_cell0),
        deep_derivative_bound=float(deep_wr))))


if __name__ == "__main__":
    main()


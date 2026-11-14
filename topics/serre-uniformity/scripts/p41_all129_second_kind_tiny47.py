#!/usr/bin/env python3
"""All129 actual rational residue disks: regular second-kind tiny integrals.

The saved chart coordinate is z, with y=z/47.  The moving-pole identity is
mu=(nu+dF)C.  Both denominators of F and mu are explicitly checked to be units
on all129 disks, including the two disks where the old formula has 0/0.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith(".gz") else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    args.script_dir = args.script_dir.resolve()
    sys.path.insert(0, str(args.script_dir))
    from p41_actual_differentials47 import ActualModel, save
    from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm
    from p41_elliptic_coarse_atlas47 import Series
    import p41_r2_matrix as r
    import numpy as np

    install_exact_float_mm(r)
    start = time.monotonic()
    a = ActualModel(args.script_dir)
    frames = ProjectiveJetFrames(a)
    Q = r.Q
    data = args.script_dir / "data"
    inputs = {}

    def load(name):
        inputs[name] = sha(data / name)
        return read(data / name)

    old = load("p41_second_kind_connection47.json.gz")
    moved = load("p41_second_kind_move_poles47.json.gz")
    atlases = [
        ("SS", load("p41_rational_SS_residue_atlas47_complete.json.gz")),
        ("ordinary", load("p41_ordinary_rational_atlas47.json.gz")),
    ]
    assert old["all54_actual_variational_second_kind_forms_complete"]
    assert moved["all54_second_kind_poles_moved_away_from_all_SS_disks"]
    s = r.from_json(old["numerator_cubic_sections"])
    vold = r.from_json(old["denominator_linear_section"])
    v = r.from_json(moved["old_pole_denominator_v"])
    w = r.from_json(moved["new_pole_denominator_w"])
    N = r.from_json(moved["moved_form_cubic_numerators_rational_basis"])
    Fn = r.from_json(moved["moving_function_quadratic_numerators_rational_basis"])
    C = r.from_json(moved["original_to_rational_change"])
    Ci = r.from_json(moved["rational_to_original_change"])
    assert r.equal(r.mm(C, Ci), r.eye(54))
    assert r.equal(r.mm(Ci, C), r.eye(54))
    perm = old["pole_Frobenius_permutation_0based"]
    A1 = a.M["A1"]
    AK = r.from_json(a.cusp["canonical_frobenius_matrix"])
    S3, S4 = Series(a, 3), Series(a, 4)
    charts = []
    ids = []
    old_nonunits = []
    direct_count = 0
    cross_count = 0

    for origin, atlas in atlases:
        for ch in atlas["charts"]:
            W = [r.from_json(x) for x in ch["W_coefficients_0to3"]]
            V2 = [r.from_json(x) for x in ch["V2_coefficients_0to3"]]
            V3 = [r.from_json(x) for x in ch["V3_coefficients_0to3"]]
            frame = r.from_json(ch["frame"])
            coordinate = r.from_json(ch["coordinate"])
            assert r.equal(r.mm(A1, r.conjugate(frame)), frame)
            assert r.equal(r.mm(A1, r.conjugate(coordinate)), coordinate)
            assert all(r.equal(x, r.mm(r.conjugate(x), r.conjugate(A1))) for x in W)
            assert r.equal(r.mm(W[0], frame), r.column([[1, 0]] * len(ch["disk_ids"])))
            assert all(r.iszero(r.mm(x, frame)) for x in W[1:])
            H = frames.frame_derivation(frame)["H"]
            hc = [r.mm(r.mm(x, H), coordinate) for x in V3[:3]]
            assert np.all(r.units(hc[0]))
            ih = S3.inverse(hc)
            vs = [r.mm(x, v) for x in W]
            ws = [r.mm(x, w) for x in W]
            assert np.all(r.units(vs[0])) and np.all(r.units(ws[0]))
            Fc = S4.mul(
                [r.mm(x, Fn) for x in V2],
                S4.inverse(S4.mul(vs, ws)),
            )
            mu = S3.mul(
                [r.mm(x, N) for x in V3[:3]],
                S3.mul(S3.inverse(S3.mul(ws[:3], ws[:3])), ih),
            )
            nr = [r.sub(mu[k], a.scale(Fc[k + 1], k + 1)) for k in range(3)]
            nu = [r.mm(x, Ci) for x in nr]
            holomorphic = S3.mul([r.mm(x, a.K1) for x in W[:3]], ih)
            assert all(not np.any(x[1]) for x in Fc + mu + nr)
            assert all(r.equal(r.conjugate(x), r.cols(x, perm)) for x in nu)
            assert all(r.equal(r.mm(x, AK), r.conjugate(x)) for x in holomorphic)
            oldv = [r.mm(x, vold) for x in W[:3]]
            oldn = [r.mm(x, s) for x in V3[:3]]
            oldden = S3.mul(S3.mul(oldv, oldv), hc)
            product = S3.mul(nu, oldden)
            assert all(r.equal(x, y) for x, y in zip(product, oldn))
            cross_count += len(ch["disk_ids"]) * 54 * 3
            units = np.flatnonzero(r.units(oldv[0])[:, 0]).tolist()
            nonunits = sorted(set(range(len(ch["disk_ids"]))) - set(units))
            old_nonunits += [ch["disk_ids"][i] for i in nonunits]
            direct = S3.mul(
                [r.rows(x, units) for x in oldn],
                S3.inverse([r.rows(x, units) for x in oldden]),
            )
            assert all(r.equal(x, r.rows(y, units)) for x, y in zip(direct, nu))
            direct_count += len(units) * 54 * 3
            tiny = [
                a.scale(x, 47 ** (k + 1) * pow(k + 1, -1, Q))
                for k, x in enumerate(nu)
            ]
            holo_tiny = [
                a.scale(x, 47 ** (k + 1) * pow(k + 1, -1, Q))
                for k, x in enumerate(holomorphic)
            ]
            charts.append({
                "chart_0based": len(charts),
                "origin": origin,
                "origin_chart_0based": ch["chart_0based"],
                "disk_ids": ch["disk_ids"],
                "coordinate": ch["coordinate"],
                "frame": ch["frame"],
                "rational_coordinate_at_center_mod47four": ch["rational_coordinate_at_center_mod47four"],
                "mu_coefficients_0to2_mod47four": [r.to_json(x) for x in mu],
                "F_times_C_coefficients_0to3_mod47four": [r.to_json(x) for x in Fc],
                "nu_coefficients_0to2_mod47four": [r.to_json(x) for x in nu],
                "second_kind_tiny_coefficients_1to3_in_y_mod47four": [r.to_json(x) for x in tiny],
                "holomorphic_tiny_coefficients_1to3_in_y_mod47four": [r.to_json(x) for x in holo_tiny],
                "moving_denominators_and_coordinate_derivative_units": True,
                "all54_actual_Frobenius_permutations_verified": True,
                "all_original_crossmultiplied_jet_equations_verified": True,
                "direct_original_unit_formula_rows": units,
                "old_formula_removable_rows": nonunits,
            })
            ids += ch["disk_ids"]
            print("PASS", origin, ch["chart_0based"], len(ch["disk_ids"]),
                  "disks, old removable", [ch["disk_ids"][i] for i in nonunits],
                  flush=True)

    assert len(ids) == len(set(ids)) == 129
    assert sorted(old_nonunits) == ["SS_j0_20", "SS_j10_06"]
    assert direct_count == 127 * 54 * 3
    assert cross_count == 129 * 54 * 3
    out = {
        "result": "R255",
        "level": 41,
        "auxiliary_prime": 47,
        "precision": 4,
        "modulus": Q,
        "complete_all129_second_kind_tiny_integrals": True,
        "complete_all129_deRham_tiny_integrals": True,
        "complete_all129_second_kind_center_integrals": False,
        "complete_canonical_local_QC_sections": False,
        "complete_common_roots": False,
        "disk_counts": {"SS": 110, "ordinary": 19, "cusps": 0},
        "original_second_kind_basis_sha256": inputs["p41_second_kind_connection47.json.gz"],
        "all129_v_w_unit_checks": True,
        "old_formula_removable_disks": old_nonunits,
        "direct_original_unit_jet_equations": direct_count,
        "all_original_crossmultiplied_jet_equations": cross_count,
        "pole_Frobenius_permutation_0based": perm,
        "charts": charts,
        "formula": "mu=(nu+dF)C; nu=(mu-d(F C))*C^-1; y=z/47 in Z47",
        "tail_bound": "All moved denominators and Hc have unit constant term, so nu is integral regular on every disk. Terms n>=4 have v47(47^n/n)>=4; the complete integral modulo47^4 is its first three y terms.",
        "precision_note": "These are tiny differences from the recorded actual centers, not center constants. R247 SS center constants are modulo47^3.",
        "input_sha256": dict(a.inputs, **inputs),
        "source_sha256": sha(__file__),
        "runtime_seconds": round(time.monotonic() - start, 3),
    }
    digest = save(args.output, out)
    print("PASS all129 x108 actual deRham tiny functions; SHA", digest, flush=True)


if __name__ == "__main__":
    main()

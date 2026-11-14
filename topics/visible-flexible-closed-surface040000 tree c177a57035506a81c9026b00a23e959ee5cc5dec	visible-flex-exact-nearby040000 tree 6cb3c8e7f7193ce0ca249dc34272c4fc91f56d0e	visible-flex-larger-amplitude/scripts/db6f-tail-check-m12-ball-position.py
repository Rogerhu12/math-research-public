#!/usr/bin/env python3
"""Independent Fraction reconstruction of existing R21 tail/cap position bounds.

No interval backend, source integrator, root, flow or exporter is called.  Input
integral intervals and whole-map identities are already closed certificates.
This checker preserves their exact binary endpoints and the original origin.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
PREFIX = "2026-11-09-db6f-"
INPUTS = {
    "first": ("tail-first-flat17-m12-critical-r01.json", "5c2ddbfc230416cf7805bf84ea5686ed9db1427c2df2b8f1b3a8379b453e848d"),
    "height": ("audit-tail-background-height-rerun.json", "dd64e00bf25124b03e725792e321e961106c6ee643f5526e0b5b95383161ff01"),
    "budget": ("root-closed-budget-m12-critical-r01.json", "50410a4e57b8a21937dd3a99c25942b36cebd5c5819f1e10982584412ae601a7"),
    "manifest": ("tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json", "cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104"),
    "alpha": ("tail-tight-alpha.json", "04aae85c19f78fd82808ac32b104537dbb584c39cac8a648107722c855685c62"),
    "geometry": ("root-flat17-common-cut-m12-critical-r01.json", "253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2"),
    "prefix_certificate": ("root-flat17-common-cut-m12-critical-r01-geometry.json", "fc00c975f1ec9b0413d2d1c77e0dbf3dd27d35016c0b335ff439aba4aeeca462"),
    "transfer": ("audit-transfer-tight-m12-critical-r01.json", "c3dbdbe79e42528b58b033f48e3694e70776666b8b890fbcb0d5b378539d2108"),
}


def require(value, message):
    if not value:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(q):
    return {"exact": str(q), "approximate_display_only": float(q)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists(), "Refusing to overwrite a previous check")
    data, bindings = {}, {}
    for name, (suffix, expected) in INPUTS.items():
        path = TOPIC / "notes" / (PREFIX + suffix)
        require(sha(path) == expected, "Changed frozen input: " + name)
        data[name] = json.loads(path.read_text())
        bindings[name] = {"file": str(path), "sha256": expected, "bytes": path.stat().st_size}
    f, h, b, m, al, geom, pref, tr = [data[k] for k in
        ("first", "height", "budget", "manifest", "alpha", "geometry", "prefix_certificate", "transfer")]
    require(f["manifestSHA256"] == geom["tail_manifest_sha256"] == INPUTS["manifest"][1], "Actual tail identity")
    require(pref["geometry_sha256"] == INPUTS["geometry"][1] and pref["continuous_bounds_certified"] is True and
            pref["entire_finite_prefix_covered"] is True and pref["mirror_interface_certified"] is True,
            "Actual complete prefix identity")
    require(geom["representation"] == "exact-common-cut-prefix" and geom["mirror_inlet_C2_exact"] is True,
            "Original common-cut/mirror definition missing")
    for key, source in (("geometry", "geometry"), ("geometry_certificate", "prefix_certificate"),
                        ("tail_first", "first"), ("height", "height")):
        require(b["inputs"][key]["sha256"] == INPUTS[source][1], "Closed-budget identity: " + key)
    require(b["same_background_transfer"]["sha256"] == INPUTS["transfer"][1] and
            tr["finite_tail_manifest_sha256"] == INPUTS["manifest"][1] and tr["finished"] is True,
            "Same-background transfer identity")
    defs = tr["background_definition_hashes"]
    require(defs["alpha"]["sha256"] == INPUTS["alpha"][1] and
            defs["checkpoint"]["sha256"] == h["checkpointSHA256"] == al["inputs"]["checkpoint"]["sha256"],
            "Height/alpha source definition mismatch")
    require([row["segment"] for row in h["segments"]] == list(range(9)), "All nine raw cell-zero segments required")

    u = max(Q(f[part]["r0theta0Planar"]) for part in ("finite", "collar"))
    v = max(Q(f[part]["r0theta0Height"]) for part in ("finite", "collar"))
    c, a = Q(m["parameters"]["rCut"]), Q(m["parameters"]["rCuff"])
    alpha_low, alpha_high = map(Q, al["exactRadialAlpha"])
    require(0 < alpha_low <= alpha_high and 0 < a < c and a > Q(7, 50), "Frozen positive parameter bounds")
    require(Q(al["targetWarpWidth"][0]) <= c-a <= Q(al["targetWarpWidth"][1]), "Exact width outside alpha definition")
    Hlow = Q(b["tail_height_lower"]["exact"]) + v
    Hhigh = Q(b["tail_height_upper"]["exact"]) - Q(h["wholeHeightUpper"]) - v
    require(v < Hlow <= Hhigh, "Tail height is not in the upper half-space")
    Rprefix = Q(pref["norm_upper"])

    # j=8 is the cut-side profile, j=0 the innermost profile of raw cell zero.
    # A lower interval endpoint is allowed to be slightly negative; it remains
    # a valid lower bound.  Actual B is nonnegative and its lower endpoint here
    # is nonnegative, so alpha_low*B_low is a valid product lower bound.
    Lout, Hout = Q(0), Q(0)
    rows = []
    for raw in reversed(h["segments"]):
        endpoints = {k: tuple(map(Q, raw[k])) for k in ("A", "B", "AH", "BH")}
        require(all(lo <= hi for lo, hi in endpoints.values()), "Reversed integral interval")
        require(endpoints["B"][0] >= 0 and endpoints["BH"][1] >= 0, "Integral sign condition")
        Llow = endpoints["A"][0] + alpha_low * endpoints["B"][0]
        Hup = endpoints["AH"][1] + alpha_high * endpoints["BH"][1]
        require(Llow > 0 and Hup > 0, "Invalid segment length/height lower/upper")
        radius_up = c - Lout
        Hout += Hup
        zup = Hhigh + Hout + v
        norm_squared = (radius_up+u)**2 + zup**2
        require(norm_squared < Rprefix**2, "Cell-zero segment exceeds the existing prefix sphere")
        rows.append({"segment": raw["segment"], "length_lower": record(Llow), "height_increment_upper": record(Hup),
                     "radius_upper": record(radius_up), "absolute_height_upper": record(zup),
                     "norm_squared_upper": record(norm_squared),
                     "prefix_radius_squared_margin": record(Rprefix**2-norm_squared)})
        Lout += Llow

    # Use the exact actual cuff, then also reproduce the author's deliberately
    # looser 7/50 cutoff if desired.  Both are rigorous and need no new integral.
    require(a < c-Lout < c, "Invalid remaining radial region")
    Bactual = Hout + (c-Lout-a)/49
    Bcoarse = Hout + (c-Lout-Q(7, 50))/49
    inner_squared = (c-Lout+u)**2 + (Hhigh+Bactual+v)**2
    inner_coarse_squared = (c-Lout+u)**2 + (Hhigh+Bcoarse+v)**2
    cap_squared = a*a + (Hhigh+Bactual+Q(1, 2000))**2
    cap_coarse_squared = a*a + (Hhigh+Bcoarse+Q(1, 2000))**2
    require(max(inner_coarse_squared, cap_coarse_squared) < Rprefix**2,
            "Inner tail or fixed caps exceed the existing prefix sphere")

    # Independent coarser envelope: H(r)-H(c)<=min(B,W*(c-r)).  Each piece of
    # the squared position envelope is convex, so only its endpoints matter.
    W, Bold = Q(16, 15), Q(h["wholeHeightUpper"])
    transition = c - Bold/W
    require(a < transition < c, "Coarse envelope transition lies outside the tail")
    cut_squared = (c+u)**2 + (Hhigh+v)**2
    transition_squared = (transition+u)**2 + (Hhigh+Bold+v)**2
    envelope_radius = Q(963691325253, 500000000000)
    require(max(cut_squared, transition_squared) <= envelope_radius**2, "Coarse rational envelope bound")

    report = {
        "status": "PASS-independent-existing-R21-tail-cap-position-arithmetic",
        "script_sha256": sha(Path(__file__)), "inputs": bindings,
        "center": [0, 0, 0], "center_meaning": "Original axis origin in the z=0 mirror plane; no map translation or recentering.",
        "Hcut_interval": [record(Hlow), record(Hhigh)], "planar_displacement_upper": record(u),
        "height_displacement_upper": record(v), "prefix_radius_upper": record(Rprefix),
        "rows_outer_to_inner": rows,
        "cell_zero_length_lower": record(Lout), "cell_zero_height_upper": record(Hout),
        "background_height_upper_actual_cuff": record(Bactual), "background_height_upper_loose_cuff": record(Bcoarse),
        "inner_tail_norm_squared_upper_actual_cuff": record(inner_squared),
        "inner_tail_norm_squared_upper_loose_cuff": record(inner_coarse_squared),
        "caps_norm_squared_upper_actual_cuff": record(cap_squared),
        "caps_norm_squared_upper_loose_cuff": record(cap_coarse_squared),
        "coarser_global_envelope_radius": record(envelope_radius),
        "all_tail_caps_strictly_within_existing_prefix_radius": True,
        "consequent_closed_map_diameter_upper": record(2*Rprefix),
        "conditional_on_reviewed_R17_R21_assembly_and_input_certificates": True,
        "new_integration_root_flow_export_or_interval_backend_calls": 0,
        "source_map_metric_and_curvature_changed": False, "README_complete": False,
    }
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"status": report["status"], "worst_cell_zero_segment": max(rows, key=lambda row: Q(row["norm_squared_upper"]["exact"]))["segment"],
                      "diameter_approximate_display_only": float(2*Rprefix), "new_backend_calls": 0}))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Independent exact audit of the frozen cylindrical-cuff scalar/angle proof.

No author module import, candidate read, geometry flow, root or optimization.
The polynomial identities below are reconstructed from Cartesian vectors.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
P = "2026-11-09-db6f-"
PIN = {
    "notes/" + P + "audit-cylindrical-cuff-and-analytic-endpoint.md": "9509ef8a4a9d72a3c7f901a024593f01be6c8b2afa6475b460c80360ad1a1aff",
    "scripts/db6f-audit-cylindrical-cuff-interface.py": "b2a1d8bd026740805147d2748dc901237dbfaa8b318b69ab91fd7c3f3bee80db",
    "notes/" + P + "audit-cylindrical-cuff-interface.json": "f523c7088c7950938ef2a93f19416fe91c522265216efb4b56a303337e5bcd4c",
    "notes/" + P + "audit-cylindrical-cuff-sources.json": "8727f6a9b9e4954e1abbefa1bff46050b0c81cd72523bbfbd081fb58e458add7",
    "notes/" + P + "audit-cylindrical-cuff-publication.json": "f2b15f65007c88d864625bd44dcbe49458da0ce5434797caac43fde09667b547",
    "notes/" + P + "tail-cylindrical-cuff-interface-replay.json": "f523c7088c7950938ef2a93f19416fe91c522265216efb4b56a303337e5bcd4c",
}


def canonical(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), allow_nan=False)


def rational(x):
    assert isinstance(x, dict) and set(x) == {"numerator", "denominator"}
    assert isinstance(x["numerator"], str) and isinstance(x["denominator"], str)
    return F(int(x["numerator"]), int(x["denominator"]))


def encode(x):
    if isinstance(x, F):
        return {"numerator": str(x.numerator), "denominator": str(x.denominator)}
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, list):
        return [encode(v) for v in x]
    return x


# Six-variable exact polynomial ring: c,h,R,V,u,v.  Only v^2=1-u^2
# is imposed, to describe u=cos(theta), v=sin(theta) without sampling.
ZERO = (0,) * 6


def const(q):
    return {ZERO: F(q)} if q else {}


def variable(i):
    e = [0] * 6
    e[i] = 1
    return {tuple(e): F(1)}


def add(*polys):
    out = {}
    for poly in polys:
        for e, c in poly.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def mul(p, q):
    out = {}
    for a, c in p.items():
        for b, d in q.items():
            e = tuple(i + j for i, j in zip(a, b))
            out[e] = out.get(e, F(0)) + c * d
    return {e: c for e, c in out.items() if c}


def prod(*polys):
    out = const(1)
    for p in polys:
        out = mul(out, p)
    return out


def neg(p):
    return {e: -c for e, c in p.items()}


def sub(p, q):
    return add(p, neg(q))


def sq(p):
    return mul(p, p)


def reduce_circle(p):
    out = {}
    for e, coefficient in p.items():
        e = list(e)
        power = e[5] // 2
        e[5] %= 2
        term = {tuple(e): coefficient}
        replacement = sub(const(1), sq(variable(4)))
        for _ in range(power):
            term = mul(term, replacement)
        out = add(out, term)
    return out


def dot(p, q):
    return add(*(mul(a, b) for a, b in zip(p, q)))


def cross(p, q):
    return [sub(mul(p[1], q[2]), mul(p[2], q[1])),
            sub(mul(p[2], q[0]), mul(p[0], q[2])),
            sub(mul(p[0], q[1]), mul(p[1], q[0]))]


def angular_identities():
    c, h, R, V, u, v = map(variable, range(6))
    p = [mul(c, u), mul(c, v), h]
    checked = []
    for sign in (1, -1):
        q = [neg(R), {}, mul(const(sign), V)]
        d = [sub(a, b) for a, b in zip(p, q)]
        cp = cross(p, q)
        actual_A = reduce_circle(dot(cp, cp))
        actual_D = reduce_circle(dot(d, d))
        claimed_A = add(mul(sq(R), add(sq(c), sq(h))), mul(sq(c), sq(V)),
                        prod(const(2 * sign), c, h, R, V, u),
                        neg(prod(sq(c), sq(R), sq(u))))
        claimed_D = add(sq(c), sq(h), sq(R), sq(V), prod(const(2), c, R, u),
                        prod(const(-2 * sign), h, V))
        actual_p_dot = reduce_circle(dot(p, d))
        actual_q_dot = reduce_circle(dot(q, [neg(x) for x in d]))
        expected_p_dot = add(sq(c), sq(h), prod(c, R, u), prod(const(-sign), h, V))
        expected_q_dot = add(sq(R), sq(V), prod(c, R, u), prod(const(-sign), h, V))
        for name, actual, expected in (
            ("cross_product_squared", actual_A, claimed_A),
            ("distance_squared", actual_D, claimed_D),
            ("p_backward_ray_dot", actual_p_dot, expected_p_dot),
            ("q_backward_ray_dot", actual_q_dot, expected_q_dot),
        ):
            assert actual == expected, (sign, name)
            checked.append({"cap_vertical_sign": sign, "identity": name,
                            "zero_difference": True, "monomials": len(actual)})
    return checked


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out).resolve()
    assert out.parent == TOPIC / "notes" and not out.exists()
    bindings = {}

    def bind(rel, want=None, size=None):
        path = (TOPIC / rel).resolve()
        assert path.is_relative_to(TOPIC) and path.is_file()
        raw = path.read_bytes()
        item = {"path": str(path.relative_to(TOPIC)), "bytes": len(raw),
                "sha256": sha256(raw).hexdigest()}
        if want is not None:
            assert item["sha256"] == want, rel
        if size is not None:
            assert len(raw) == size, rel
        if rel in bindings:
            assert bindings[rel] == item
        bindings[rel] = item
        return raw

    for rel, want in PIN.items():
        bind(rel, want)
    publication = json.loads(bind("notes/" + P + "audit-cylindrical-cuff-publication.json"))
    for item in publication["files"]:
        bind(item["path"], item["sha256"], item["bytes"])
    ledger = json.loads(bind("notes/" + P + "audit-cylindrical-cuff-sources.json"))
    for item in [ledger["proof"]] + ledger["sources"]:
        bind(item["path"], item["sha256"], item["bytes"])
    report = json.loads(bind("notes/" + P + "audit-cylindrical-cuff-interface.json"))
    replay = bind("notes/" + P + "tail-cylindrical-cuff-interface-replay.json")
    assert replay == bind("notes/" + P + "audit-cylindrical-cuff-interface.json")
    base = json.loads(bind("notes/" + P + "audit-poisson-twin-marker-bounds.json"))
    previous = json.loads(bind("notes/" + P + "audit-positive-collar-budget.json"))

    H0 = rational(base["source_bounds"]["H_lower"])
    H1 = rational(base["source_bounds"]["H_upper"])
    L0 = rational(base["witness_and_enclosures"]["L0_lower"])
    L1 = rational(base["witness_and_enclosures"]["L0_upper"])
    m0 = rational(base["source_bounds"]["hmin_lower"])
    assert 0 < H0 < H1 and 0 < L0 < L1 and m0 > 0
    c, z, width = F(1, 10), F(1, 10), F(1, 1000)
    cap, zcap, b, chi = F(1, 10), F(3, 10), F(1, 100), F(1, 100)
    goal, tau = F(189, 2500), F(9, 100)
    h0, h1 = z - width, z + width
    # Recover the axis point using a*2H/L and a*(zcap+b)/L,
    # rather than copying the author's already simplified constants.
    R0 = H0 + cap * 2 * H0 / L1 - cap * chi
    R1 = H1 + cap * 2 * H1 / L0 + cap * chi
    V0 = zcap + cap * (zcap + b) / L1 - cap * chi
    V1 = zcap + cap * (zcap + b) / L0 + cap * chi
    host = rational(previous["fixed_flat_annuli"]["common_envelope_host_slab_disk_radius_lower"])
    assert c < F(1, 2) < host
    assert F(95, 1000) < h0 < h1 < F(105, 1000)
    assert R0 > 1 and V1 < F(2, 5) and V0 > h1 > 0
    C0, C1 = h0 * R0 - c * V1, h0 * R0 + c * V0
    assert C0 > 0 and C1 > 0
    Qm = C0 ** 2 / ((R1 - c) ** 2 + (V1 - h0) ** 2)
    Qp = C1 ** 2 / ((R1 + c) ** 2 + (V1 - h0) ** 2)
    Qo = C1 ** 2 / ((R1 - c) ** 2 + (V1 + h1) ** 2)
    backward = R0 ** 2 + V0 ** 2 - c * R1 - h1 * V1
    active_z = F(3, 200) + F(1, 10**6)
    active_r = m0 - F(1, 10**6)
    distances = {
        "active_to_caps": zcap - cap - active_z,
        "active_to_cylinders": active_r - c,
        "cylinders_to_caps": H0 - cap - c,
        "opposite_cylinders": 2 * h0,
        "opposite_caps": 2 * zcap - 2 * cap,
    }
    exact = {
        "small_upper_cap_bounds": {
            "horizontal_radius_lower": R0, "horizontal_radius_upper": R1,
            "height_lower": V0, "height_upper": V1,
        },
        "necessary_two_point_kernel_tests": {
            "same_side_line_distance_squared_lower_at_cos_minus_one": Qm,
            "same_side_line_distance_squared_lower_at_cos_plus_one": Qp,
            "same_side_all_lines_distance_strictly_above": F(79, 1000),
            "opposite_side_relevant_endpoint_line_distance_squared_lower": Qo,
            "opposite_side_backward_rays_norm_lower": c,
            "cap_based_backward_ray_dot_lower": backward,
            "active_to_cylinder_cylinder_based_center_height_lower": h0,
            "active_to_cylinder_active_based_center_horizontal_norm_lower": active_r,
            "two_cylinder_points_center_horizontal_norm_lower": c,
        },
    }
    count = 0
    for section, entries in exact.items():
        for key, value in entries.items():
            assert rational(report[section][key]) == value
            count += 1
    for key, value in distances.items():
        assert rational(report["retained_piece_geometry"]["cross_piece_distance_lower_bounds"][key]) == value
        count += 1
    for key, value in {
        "radius": c, "center_height_absolute": z, "halfheight": width,
        "slab_height_lower": h0, "slab_height_upper": h1,
        "infinite_cylinder_reach": c, "radial_support": c,
        "common_host_radius_lower": host,
    }.items():
        assert rational(report["cylindrical_cuffs"][key]) == value
        count += 1
    assert min(Qm, Qp) > F(79, 1000) ** 2 > goal ** 2
    assert Qo > c ** 2 > goal ** 2 and backward > 0
    assert active_r > c > goal and h0 > active_z and h0 > goal
    assert min(distances.values()) > 2 * tau
    assert report["closed_surface_or_common_metric_connection_constructed"] is False
    assert report["current_M15_candidate_read"] is False
    assert report["solver_root_RK_or_geometry_backend_calls"] == 0
    identities = angular_identities()
    for item in list(bindings.values()):
        bind(item["path"], item["sha256"], item["bytes"])
    result = {
        "status": "PASS_INDEPENDENT_EXACT_SCALAR_AND_CARTESIAN_IDENTITY_AUDIT",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_file_count": len(bindings), "sources": list(bindings.values()),
        "source_bytes_unchanged_at_completion": True,
        "original_script_replay_byte_identical": True,
        "independently_rebuilt_exact_report_fields": count,
        "cartesian_all_angle_identities": identities,
        "independent_topological_premises": {
            "horizontal_radius_lower": R0, "height_upper": V1,
            "R_lower_greater_than_one": True,
            "V_upper_less_than_two_fifths": True,
            "cap_latitude_V_over_R_less_than_two_fifths": True,
            "cuff_latitude": z / c,
        },
        "strict_margins": {
            "same_side_squared_above_79_over_1000_squared": min(Qm, Qp) - F(79, 1000)**2,
            "opposite_squared_above_radius_squared": Qo - c*c,
            "smallest_cross_gap_above_two_tau": min(distances.values()) - 2*tau,
        },
        "limitations": [
            "Scalar and identity audit does not numerically prove the separate analytic CK argument.",
            "All-pair bounds cover only specified retained pieces, not any unknown connector.",
            "Positive-support topology obstruction additionally requires the separating-circle layout.",
            "Analytic endpoint obstruction requires an analytic germ and connected analytic mother map.",
            "No current candidate, solver, DN, RK, BVP, optimization, or geometry backend was used.",
        ],
    }
    raw = (json.dumps(encode(result), ensure_ascii=False, indent=2) + "\n").encode()
    with out.open("xb") as f:
        f.write(raw)
    print(json.dumps({"status": result["status"], "source_files": len(bindings),
                      "exact_fields": count, "polynomial_identities": len(identities),
                      "report_bytes": len(raw), "sha256": sha256(raw).hexdigest()}))


if __name__ == "__main__":
    main()

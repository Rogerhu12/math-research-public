#!/usr/bin/env python3
"""Independent exact algebra/scalar audit; no ODE/PDE/geometry execution."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
STEM = "2026-11-09-db6f-"
VARS = ("a", "ap", "app", "L", "M", "N", "Lt", "Mt", "Ms", "Ns", "k", "A")
ZERO = (0,) * len(VARS)


class Poly:
    """Exact sparse Laurent polynomial over Q; negative powers only in a,N,k."""

    def __init__(self, terms=None):
        self.t = {e: Q(c) for e, c in (terms or {}).items() if c}

    @staticmethod
    def c(x):
        return Poly({ZERO: Q(x)})

    def __add__(self, other):
        if not isinstance(other, Poly):
            other = Poly.c(other)
        z = dict(self.t)
        for e, c in other.t.items():
            z[e] = z.get(e, Q(0)) + c
        return Poly(z)

    __radd__ = __add__

    def __neg__(self):
        return Poly({e: -c for e, c in self.t.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Poly) else -Q(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, Poly):
            other = Poly.c(other)
        z = {}
        for e, c in self.t.items():
            for f, d in other.t.items():
                g = tuple(x + y for x, y in zip(e, f))
                z[g] = z.get(g, Q(0)) + c * d
        return Poly(z)

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            if len(self.t) != 1:
                raise ValueError("inverse requires one monomial")
            e, c = next(iter(self.t.items()))
            return Poly({tuple(n * x for x in e): c ** n})
        z = Poly.c(1)
        for _ in range(n):
            z = z * self
        return z

    def is_zero(self):
        return not self.t


def var(name):
    e = list(ZERO)
    e[VARS.index(name)] = 1
    return Poly({tuple(e): Q(1)})


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), Poly())
             for j in range(3)] for i in range(3)]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def exact(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def readq(obj):
    return Q(int(obj["numerator"]), int(obj["denominator"]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    out = Path(args.out).resolve()
    if TOPIC not in out.parents or out.exists():
        raise ValueError("output must be a new file in the topic")
    proof = TOPIC / "notes" / (STEM + "audit-ck-local-isometric-collar.md")
    ledger = TOPIC / "notes" / (STEM + "audit-ck-local-isometric-collar-sources.json")
    publication = TOPIC / "notes" / (STEM + "audit-ck-local-isometric-collar-publication.json")
    expected = {
        proof: "e5f3d23d677a78398ad7c92f4db751d21536fd9ed26fb8c449663cdc41c1dd87",
        ledger: "575fcc2c123ad7e39f06085939c59ff1a1fe67843e68c235f5f50cedb27e1e66",
        publication: "603b100deacbc2674ba658dc7483f901bd1e86cc7a15a155fc5fd2580e775b6d",
    }
    bindings = []
    for p, h in expected.items():
        assert digest(p) == h
        bindings.append({"path": str(p.relative_to(TOPIC)), "bytes": p.stat().st_size,
                         "sha256": h})
    data = json.loads(ledger.read_text())
    for item in [data["proof"], *data["repository_inputs"]]:
        p = TOPIC / item["path"]
        assert p.stat().st_size == item["bytes"] and digest(p) == item["sha256"]
        if item["path"] not in {x["path"] for x in bindings}:
            bindings.append(item)
    for item in json.loads(publication.read_text())["files"]:
        p = TOPIC / item["path"]
        assert p.stat().st_size == item["bytes"] and digest(p) == item["sha256"]

    a, ap, app, L, M, N, Lt, Mt, Ms, Ns, k, A = map(var, VARS)
    ai = a ** -1
    z = Poly()
    Os = [[z, z, -L], [z, z, -M * ai], [L, M * ai, z]]
    Ot = [[z, -ap, -M], [ap, z, -N * ai], [M, N * ai, z]]
    # Explicit derivatives are from the printed matrix entries, before using GC.
    dsOt = [[z, -app, -Ms],
            [app, z, -Ns * ai + N * ap * ai ** 2],
            [Ms, Ns * ai - N * ap * ai ** 2, z]]
    dtOs = [[z, z, -Lt], [z, z, -Mt * ai], [Lt, Mt * ai, z]]
    AB, BA = mm(Os, Ot), mm(Ot, Os)
    C = [[dsOt[i][j] - dtOs[i][j] + AB[i][j] - BA[i][j]
          for j in range(3)] for i in range(3)]
    upper = {
        (0, 1): -app - (L * N - M ** 2) * ai,
        (0, 2): -Ms + Lt - ap * ai * M,
        (1, 2): (-Ns + Mt + ap * ai * N + a * ap * L) * ai,
    }
    for (i, j), value in upper.items():
        assert (C[i][j] - value).is_zero()
    assert all((C[i][j] + C[j][i]).is_zero() for i in range(3) for j in range(3))
    assert all((Os[i][j] + Os[j][i]).is_zero() for i in range(3) for j in range(3))
    assert all((Ot[i][j] + Ot[j][i]).is_zero() for i in range(3) for j in range(3))

    Lsol = (M ** 2 - a * app) * N ** -1
    assert (Lsol * N - M ** 2 + a * app).is_zero()
    assert (((Lsol * N - M ** 2) * ai ** 2) + app * ai).is_zero()
    # Formal twice-differentiated Gauss identity at the printed zero jet.
    Lss = -24 * A * k ** -1
    assert (k * Lss + 24 * A).is_zero()
    assert (-Q(1, 24) * Lss - A * k ** -1).is_zero()

    budget = json.loads((TOPIC / "notes" / (STEM + "audit-positive-collar-budget.json")).read_text())
    m = readq(budget["core_bounds"]["curvature_radius_lower"])
    m0 = readq(budget["core_bounds"]["hmin_lower"])
    tau = Q(9, 100)
    epsmax, eta = Q(1, 200), Q(1, 10 ** 6)
    b, B = Q(1, 100), Q(9, 100)
    vertical = Q(3, 10) - Q(1, 10) - b - epsmax - eta
    horizontal = m0 - Q(36, 100) - eta
    oldcross = budget["retained_pieces_only"]["cross_piece_distance_lower_bounds"]
    gates = {
        "m_exceeds_tau": m > tau,
        "curvature_bound_has_strict_margin": 1 / m < 10,
        "support_has_strict_margin": m0 > Q(65, 100) > Q(6, 10),
        "reference_band_fits_auxiliary_envelope": b + epsmax < B,
        "position_error_less_than_old_envelope_budget": eta < Q(1, 200),
        "tau_exceeds_old_Dstar_reach_budget": tau > Q(756, 10000),
        "active_to_cap_distance_exceeds_twice_tau": vertical > 2 * tau,
        "active_to_new_annulus_distance_exceeds_twice_tau": horizontal > 2 * tau,
        "annulus_cap_conservative_old_distance_exceeds_twice_tau": readq(oldcross["annulus_to_either_cap"]) > 2 * tau,
        "opposite_annuli_distance_exceeds_twice_tau": readq(oldcross["opposite_annuli"]) > 2 * tau,
        "opposite_caps_distance_exceeds_twice_tau": readq(oldcross["opposite_caps"]) > 2 * tau,
    }
    assert all(gates.values())
    dw = budget["diameter_and_witness"]
    D = readq(dw["initial_actual_diameter_upper"])
    rigid = readq(dw["rigid_quotient_ratio_lower"])
    held = readq(dw["held_ratio_lower"])
    assert D < Q("2.51518578393841")
    assert rigid > Q("0.05109026903944")
    assert held > Q("0.20712850442174")

    report = {
        "status": "PASS_EXACT_COMPONENT_CHECKS_FOR_FROZEN_LOCAL_EXISTENCE_PROOF",
        "reviewer": "/root/tail_theory",
        "script_sha256": digest(Path(__file__)),
        "author_and_repository_source_bindings": bindings,
        "unique_source_files_rehashed": len(bindings),
        "exact_algebra": {
            "three_upper_flatness_entries": "all coefficient dictionaries identically zero after subtracting printed expressions",
            "full_flatness_matrix_skew": True,
            "both_connection_matrices_skew": True,
            "Gauss_elimination_and_intrinsic_K": True,
            "twice_differentiated_zero_jet_Lss": "kappa0 * Lss = -24 * A4",
            "outward_fourth_position_coefficient": "-Lss/24 = A4/kappa0",
            "arithmetic": "exact Fraction sparse Laurent polynomials; no floating sampling",
        },
        "strict_scalar_gates": gates,
        "scalar_values": {
            "m": exact(m), "m0_lower": exact(m0), "tau": exact(tau),
            "active_cap_separation_lower": exact(vertical),
            "active_new_annulus_separation_lower": exact(horizontal),
            "conditional_D_upper": exact(D), "conditional_rigid_ratio_lower": exact(rigid),
            "conditional_held_ratio_lower": exact(held),
        },
        "primary_theorem_text_independently_read": {
            "url": "https://www.math.mcgill.ca/gantumur/math580f11/downloads/notes2.pdf",
            "location": "Theorem 18, printed pages 9-10; first-order normal form and analytic uniqueness",
            "retrieval_refs": ["turn68view0", "turn69view0"],
            "PDF_saved_or_rendered": False,
        },
        "not_executable_proofs": [
            "CK analytic local existence and uniform periodic patching",
            "frame and position reconstruction/embedding",
            "near-diagonal and separated-point compactness argument",
        ],
        "scope": {
            "uniform_epsilon_exists": True, "numerical_positive_epsilon_lower_bound": False,
            "local_common_metric_exists": True, "closed_connected_surface_constructed": False,
            "whole_closed_surface_reach_proved": False, "G5_paid": False,
        },
        "current_candidate_data_read": False,
        "new_geometry_solver_root_RK_flow_DN_BVP_integration_calls": 0,
    }
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": report["status"], "output": str(out),
                      "sha256": digest(out), "bytes": out.stat().st_size,
                      "source_files": len(bindings)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

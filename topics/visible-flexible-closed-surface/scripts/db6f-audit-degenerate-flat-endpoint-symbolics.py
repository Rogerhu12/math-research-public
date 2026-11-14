#!/usr/bin/env python3
"""Exact symbolic identities for the conditional degenerate flat-endpoint note.

This program does not solve an ODE/PDE or load an actual geometric candidate.
It does not replace the finite-dimensional uniqueness or limiting proofs.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import sympy as sp


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    r, th = sp.symbols("r theta", positive=True, real=True)
    E = sp.Function("E", positive=True)(r)
    A, B, C = [sp.Function(k)(r, th) for k in ("A", "B", "C")]
    coords = (r, th)
    metric = sp.diag(E, r*r)
    inverse = metric.inv()
    checked = []

    def verify(name, expression):
        assert sp.simplify(sp.trigsimp(expression)) == 0, name
        checked.append(name)

    gamma = [[[sp.simplify(sum(
        inverse[i, m] * (
            sp.diff(metric[m, k], coords[j])
            + sp.diff(metric[m, j], coords[k])
            - sp.diff(metric[j, k], coords[m])
        ) / 2 for m in range(2)
    )) for k in range(2)] for j in range(2)] for i in range(2)]
    wanted = {(0, 0, 0): sp.diff(E, r)/(2*E), (0, 1, 1): -r/E,
              (1, 0, 1): 1/r, (1, 1, 0): 1/r}
    for i in range(2):
        for j in range(2):
            for k in range(2):
                verify(f"christoffel_{i}{j}{k}", gamma[i][j][k]-wanted.get((i,j,k), 0))
    curvature = (
        sp.diff(gamma[0][1][1], r)-sp.diff(gamma[0][0][1], th)
        + sum(gamma[0][0][m]*gamma[m][1][1]
              - gamma[0][1][m]*gamma[m][0][1] for m in range(2))
    )
    verify("riemann_r_theta_r_theta", curvature-r*sp.diff(E,r)/(2*E**2))
    verify("gaussian_curvature", E*curvature/metric.det()-sp.diff(E,r)/(2*r*E**2))
    second = sp.Matrix([[A, B], [B, C]])

    def cov(k, i, j):
        return sp.diff(second[i,j], coords[k])-sum(
            gamma[m][k][i]*second[m,j]+gamma[m][k][j]*second[i,m]
            for m in range(2)
        )

    gauss = A*C-B*B-r*sp.diff(E,r)/(2*E)
    cod1 = sp.diff(B,r)-sp.diff(A,th)-(sp.diff(E,r)/(2*E)-1/r)*B
    cod2 = sp.diff(C,r)-sp.diff(B,th)-C/r-r*A/E
    verify("first_codazzi", cov(0,0,1)-cov(1,0,0)-cod1)
    verify("second_codazzi", cov(0,1,1)-cov(1,0,1)-cod2)

    rs = -1/sp.sqrt(E)
    ass = sp.diff(rs,r)*rs
    L, M, N = A/E, -B/sp.sqrt(E), C
    verify("coordinate_gauss", E*(L*N-M*M+r*ass)-gauss)
    s_cod1 = sp.diff(M,r)*rs-sp.diff(L,th)+(rs/r)*M
    s_cod2 = sp.diff(N,r)*rs-sp.diff(M,th)-(rs/r)*N-r*rs*L
    verify("coordinate_first_codazzi", E*s_cod1-cod1)
    verify("coordinate_second_codazzi", -sp.sqrt(E)*s_cod2-cod2)

    U = sp.Matrix([[0,0,A/sp.sqrt(E)], [0,0,-B/r], [-A/sp.sqrt(E),B/r,0]])
    V = sp.Matrix([[0,1/sp.sqrt(E),B/sp.sqrt(E)], [-1/sp.sqrt(E),0,-C/r], [-B/sp.sqrt(E),C/r,0]])
    flatness = U.diff(th)-V.diff(r)+V*U-U*V
    expected = sp.Matrix([
        [0,-gauss/(r*sp.sqrt(E)),-cod1/sp.sqrt(E)],
        [gauss/(r*sp.sqrt(E)),0,cod2/r],
        [cod1/sp.sqrt(E),-cod2/r,0],
    ])
    for i in range(3):
        for j in range(3):
            verify(f"frame_flatness_{i}{j}", flatness[i,j]-expected[i,j])
    verify("skew_U", sum(v*v for v in U+U.T))
    verify("skew_V", sum(v*v for v in V+V.T))

    w = sp.Function("w", real=True)(r)
    E0 = 1+w*w
    A0, C0 = sp.diff(w,r)/sp.sqrt(E0), r*w/sp.sqrt(E0)
    verify("background_gauss", A0*C0-r*sp.diff(E0,r)/(2*E0))
    verify("background_second_codazzi", sp.diff(C0,r)-C0/r-r*A0/E0)
    er, et, ez = sp.Matrix([sp.cos(th),sp.sin(th),0]), sp.Matrix([-sp.sin(th),sp.cos(th),0]), sp.Matrix([0,0,1])
    normal = -(w*er+ez)/sp.sqrt(E0)
    fs = (-er+w*ez)/sp.sqrt(E0)
    crossdiff = fs.cross(et)-normal
    for i in range(3):
        verify(f"background_normal_component_{i}", crossdiff[i])
    verify("background_radial_second_form", (-sp.diff(w,r)*ez).dot(normal)-A0)
    verify("background_angular_second_form", (-r*er).dot(normal)-C0)

    s = sp.symbols("s", real=True)
    a = sp.Function("a", positive=True)(s)
    beta = sp.sqrt(1-sp.diff(a,s)**2)
    nrev, lrev = a*beta, -sp.diff(a,s,2)/beta
    verify("nonanalytic_finite_mode_rotational_gauss", lrev*nrev+a*sp.diff(a,s,2))
    verify("nonanalytic_finite_mode_rotational_codazzi", sp.diff(nrev,s)-sp.diff(a,s)*nrev/a-a*sp.diff(a,s)*lrev)

    omega = 2*sp.pi/3
    rotation = sp.Matrix([[sp.cos(omega),-sp.sin(omega),0],[sp.sin(omega),sp.cos(omega),0],[0,0,1]])
    positive_diff = er.subs(th, th+omega)-rotation*er
    for i in range(3):
        verify(f"positive_material_C3_component_{i}", positive_diff[i])
    er_reverse = er.subs(th,-th)
    reverse_diff = er_reverse.subs(th,th+omega)-rotation*er_reverse
    verify("negative_material_winding_C3_norm_squared_is_three", reverse_diff.dot(reverse_diff)-3)

    base = Path(__file__).resolve().parents[1]
    proofrel = "notes/2026-11-09-db6f-audit-degenerate-flat-endpoint-interface.md"
    proofbytes = (base/proofrel).read_bytes()
    report = {
        "status": "EXACT_SYMBOLIC_IDENTITIES_PASS_ONLY",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "sympy_version": sp.__version__,
        "proof": {"path": proofrel, "bytes":len(proofbytes), "sha256":sha256(proofbytes).hexdigest()},
        "identity_count": len(checked), "identities": checked,
        "source_sign_convention": "inward r_s=-1/sqrt(E), n=(-F_r/sqrt(E)) cross (F_theta/r), h_r=-w",
        "finite_mode_uniqueness_full_proof_required": True,
        "flat_endpoint_limit_full_proof_required": True,
        "embedding_and_normal_pair_full_proof_required": True,
        "nonrotational_solution_constructed": False,
        "whole_common_metric_connection_constructed": False,
        "candidate_M14_M15_read": False,
        "BVP_DN_RK_source_integral_or_geometry_backend_calls": 0,
    }
    out=Path(args.out).resolve()
    with out.open("x") as f:
        json.dump(report,f,ensure_ascii=False,indent=2)
        f.write("\n")
    print(json.dumps({"status":report["status"],"identity_count":len(checked),"report_bytes":out.stat().st_size,"sha256":sha256(out.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()

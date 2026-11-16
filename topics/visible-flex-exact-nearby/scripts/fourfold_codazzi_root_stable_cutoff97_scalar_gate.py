#!/usr/bin/env python3
"""One new root-stable cutoff97 scalar recipe; all old targets remain read only."""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import gzip
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import time
import traceback

from flint import arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE = TOPIC + "scripts/fourfold_codazzi_root_stable_cutoff97_scalar_gate.py"
KIND = "complete_root_stable_cutoff97_scalar_gate"
MANIFEST_KIND = "complete_root_stable_cutoff97_scalar_gate_public_inputs_v1"
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0"}
OLD_RUNTIME = {"python": "3.12.14", "python_flint": "0.9.0",
               "numpy": "2.3.5", "scipy": "1.17.0"}
ROOT_RUNTIME = {"python": "3.12.14", "numpy": "2.3.5", "python_flint": "0.9.0"}
FA_RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0", "arithmetic_bits": 320}
GATE_COUNT = 22
COMPLETE_SCIENCE_MAX_BYTES = 75000
ROOT_GERM = "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
OBJECT = "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
BASE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
FOLD_PAYLOAD = "e0f1852f561b2596018e387a0b6c728441b665fee227e4c6fa85bc352060bf23"
PIN_SPECS = {"r97_contract":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-complete-root-cutoff97-scalar-recipe.md","git_blob":"cc0d98891f52a8c6ec1c718c57d7be143db0134c","bytes":20143,"sha256":"543ebc3899931db63bda92c31ce20d8f21013daac906e00eaf761a28ff582f74"},"ri_proof":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-root-stable-trace-saved-input-inventory.md","git_blob":"85d9d46e76f9104e33e60a5e4fbddb890bbee4f3","bytes":25837,"sha256":"01afb86c1d90db86732c4621abe3f35aeb7e2aea38039eaf56725127ffb8be96"},"rbo_proof":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-ordered-genuine-root-input-powers-and-complete-mean-row.md","git_blob":"6d6a8f44edaf99ae4613c53addcd3682a86df82e","bytes":18718,"sha256":"a45e0264875c1a5cded48c6f108004f3c21b6ade73247a7b02231d9b26a30f50"},"rbg_proof":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-exact-genuine-root-b-jets-with-common-radial-cancellation.md","git_blob":"6fcf438b00220d8823f86dd619aaf32659b597c8","bytes":22284,"sha256":"157795fdc7fc415156229f5c0b9674b18f92cce1e8cef8ce8df65a271775f268"},"rda_proof":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-exact-root-first-Airy-amplitude-derivative.md","git_blob":"5a7b91eea967053bb1e68e0cc60a41fd5183cd69","bytes":11486,"sha256":"8d2570c7b28304001c785e7b7a6d4261cf127909dd59d594262fd22d42caa205"},"rd_proof":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-exact-leading-root-derivative-and-complete-stable-trace-gate.md","git_blob":"24b3523585bdfe9f1d96b57e3ca2e4f0727fd2d4","bytes":17725,"sha256":"34eec24f901205c6e8002aa767484fed4832f590fbbfbb89b3a9f2ece218b81f"},"high_root":{"path":"topics/visible-flex-exact-nearby/notes/true_root_high_intrinsic_jets_v2_ci/run-43651259105-1/consumers/process.json","git_blob":"786e16432a3a6a9873b5477ce92df919525fa85e","bytes":27056,"sha256":"3b06c881b8b00f8bb830653b3eb290b09687b0a2576320b605ba758e2e706abe"},"auxiliary":{"path":"topics/visible-flex-exact-nearby/notes/auxiliary_root_complex_third_jets_ci/run-43640181602-1/consumers/process.json","git_blob":"fee96b78c80c9ce1b70755768652599a03cc54ab","bytes":38267,"sha256":"a6783642ae2c49f66c3a7b54f1506389f24771790f3bd5a324646df8229f9728"},"root_process":{"path":"topics/visible-flex-exact-nearby/notes/current_root_scalarization_ci/run-43594466882-1/consumers/process.json","git_blob":"37437b0475d8d361d3b10c4384ef486eb5be040f","bytes":4120,"sha256":"9f1d18061f1b406f028916adc33484b4deea826a8e4175fd28b0fdb5b690342d"},"potential_execution":{"path":"topics/visible-flex-exact-nearby/notes/common_radial_potential_budget_ci/run-43685624307-1/execution.json","git_blob":"9b8741b1508d7c3754d76f884d48a6af14d1194f","bytes":27645,"sha256":"d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9"},"genuine_execution":{"path":"topics/visible-flex-exact-nearby/notes/common_reference_columns_old_circle_ci/run-43688459733-1/execution.json","git_blob":"5e7669f1990e1c4e9e3769afe3641ef6d84b82a3","bytes":16120,"sha256":"fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57"},"fa_science":{"path":"topics/visible-flex-exact-nearby/notes/free_Airy_first_omitted_cut_scalars_ci/run-43763658978-1/actual-scientific-conclusion.json","git_blob":"2001f4e2eeece1cda56b18b90dccab04b7f6d336","bytes":35718,"sha256":"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2"},"root_publication":{"path":"topics/visible-flex-exact-nearby/notes/current_root_scalarization_ci/run-43594466882-1/publication.json","git_blob":"b7de74b54eda4d2bdf308c7fe5934ef22b7343d5","bytes":2005,"sha256":"89642fd97b7669449f1138d2c3de6840e19ca84dfe06b5a5a76b608239842812"},"majorants_native":{"path":"topics/visible-flex-exact-nearby/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/consumers/stages/complete-original-reference-holomorphic-majorants.json.gz","git_blob":"fe180735fb6cbfaef8dff2ef68aa511ed3ac0643","bytes":4501,"sha256":"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"},"root_native":{"path":"topics/visible-flex-exact-nearby/notes/current_root_scalarization_ci/run-43594466882-1/consumers/complete-moving-root-scalarization.json.gz","git_blob":"1b1c6f11478c800ef76e1519c266e80b9d08916c","bytes":30595,"sha256":"10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"}}
HISTORICAL_INPUTS = [{"role":"majorants_native","path":"topics/visible-flex-exact-nearby/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/consumers/stages/complete-original-reference-holomorphic-majorants.json.gz","commit":"a3d84d905ce72e3a854874bbe98d119623f3f8de","git_blob_sha":"fe180735fb6cbfaef8dff2ef68aa511ed3ac0643","bytes":4501,"sha256":"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"},{"role":"root_native","path":"topics/visible-flex-exact-nearby/notes/current_root_scalarization_ci/run-43594466882-1/consumers/complete-moving-root-scalarization.json.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","git_blob_sha":"1b1c6f11478c800ef76e1519c266e80b9d08916c","bytes":30595,"sha256":"10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"}]
PARAMETERS = {"arithmetic_bits":320,"expected_actual_gate_count":22,"exact_real_delta_radius":"1/100000000","fixed_intrinsic_parameter":"eta_0","exact_intrinsic_parameter":"-7789843107295549/4611686018427387904","exact_root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"physical_root_piece":2549,"physical_period":"pi/2","normalized_angular_measure":True,"input_cutoff_abs_j":97,"physical_minimum_frequency":388,"physical_frequency":"n=4|j|","exact_real_z_interval":["0","1/9409"],"frequency_relation":"z=j^-2=16*n^-2","retained_physical_means":2,"old_target_calls_allowed":0,"old_source_imports_allowed":0,"expected_current_inputs":16,"expected_total_inputs":18,"expected_Python_AST_files":2,"expected_historical_gzip_inputs":2,"strict_failure_is_complete_scalar_result":True,"full_complex_square_claimed":False,"full_incoming_or_finite_Schur_inverse_claimed":False}
PINNED = {key: entry["sha256"] for key, entry in PIN_SPECS.items()}
OLD_SOURCES = {
 "high_root": "c3bb77f96f05ceedd05a0fc4cda39d591065d4ee2203fd7b05be79169d04709d",
 "auxiliary": "70f848effb2e57c64b2c9e8100d6ac0af01968c13c939a4874c6f44b0a759d21",
 "root_native": "4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e",
 "potential_execution": "042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7",
 "genuine_execution": "9596ebee08e95939cf1b8a9d46a9f32053bd4706cc77e2263a80d09ede99294c",
 "fa_science": "a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954",
}
OLD_MANIFESTS = {
 "high_root": "36ed4257fae6afb0170fa937c044bece1a55db0e5a0e4c1036035b9135e68ac5",
 "auxiliary": "404e8352112f38cd5b96dc42ebe49c9c11ebab3a2f2fc53db3f1e247314285da",
 "root_process": "b1e47bdc43fdb5f9742ee8feb087f5a66dd72457439405abecb1816012b1c746",
 "potential_execution": "44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437",
 "genuine_execution": "1869212f28702ae915787a6b5189406b13e6824b93e436a8650fa83e86b11f99",
 "fa_science": "d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def original_payload_sha(value):
    # This old complete stage was hashed without a terminal LF.
    return sha(json.dumps(value, sort_keys=True, separators=(",", ":"),
                          allow_nan=False).encode("utf-8"))


def gate(doc, name, condition):
    result = bool(condition)
    doc["gates"].append({"name": name, "passed": result})
    if not result:
        raise ValueError("failed root97 structural gate: " + name)


def passed_gates(value, key, count):
    rows = value.get(key)
    return (isinstance(rows, list) and len(rows) == count
            and all(row.get("passed") is True for row in rows))


def persist(path, doc):
    raw = canonical(doc)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".atomic")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)
    return raw


def print_complete_document(doc):
    raw = canonical(doc)
    print("ROOT97_SCIENTIFIC_JSON_BEGIN", flush=True)
    print(raw.decode("utf-8"), end="", flush=True)
    print("ROOT97_SCIENTIFIC_JSON_END", flush=True)
    print(json.dumps({"complete": doc.get("complete", False),
        "stage": doc.get("stage"), "gates": len(doc.get("gates", [])),
        "bytes": len(raw), "sha256": sha(raw)}, sort_keys=True), flush=True)


def finite_tree(value):
    if isinstance(value, arb):
        return value.is_finite()
    if isinstance(value, dict):
        return all(finite_tree(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return all(finite_tree(v) for v in value)
    return True

def ex(value):
    q = Fraction(value)
    return arb(q.numerator) / arb(q.denominator)


def ball(value):
    if isinstance(value, dict):
        value = value["ball"]
    x = arb(value)
    if not x.is_finite():
        raise ArithmeticError("nonfinite original or new scalar")
    return x


def up(value):
    x = abs(ball(value)).upper()
    if not x.is_finite() or x < 0:
        raise ArithmeticError("invalid nonnegative upper")
    return x


def lower(value):
    x = ball(value).lower()
    if not x.is_finite() or not x > 0:
        raise ArithmeticError("missing strict positive lower")
    return x


def upper_sum(values):
    return up(sum(values, arb(0)))


def whole_min(values):
    candidates = [up(x) for x in values]
    if not candidates:
        raise ValueError("empty complete-bound choice")
    winner = min(range(len(candidates)), key=lambda i: candidates[i])
    return candidates[winner], winner


def symmetric(value):
    return arb(0, up(value))


def nonnegative_interval(value):
    return arb(0).union(up(value))


def encoded(value):
    if isinstance(value, arb):
        if not value.is_finite():
            raise ArithmeticError("nonfinite diagnostic")
        return value.str(75)
    if isinstance(value, dict):
        return {str(k): encoded(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encoded(v) for v in value]
    return value


def select_complete_mixed(c):
    """Read all forty old ordinary-r/physical-angle entries; no old enclosure."""
    selected, winners = {}, {}
    for name in ("U", "V"):
        matrix, choices = [], []
        for a in range(4):
            row, row_choices = [], []
            for b in range(5):
                opts = [ball(c["mixed"][name][a][b])]
                labels = ["majorants"]
                if a == 0:
                    opts.append(ball(c["root_angular"][name][b]))
                    labels.append("root_angular")
                if b == 0:
                    opts.append(ball(c["aux_radial"][name][a]))
                    labels.append("aux_radial")
                value, chosen = whole_min(opts)
                row.append(value)
                row_choices.append(labels[chosen])
            matrix.append(row)
            choices.append(row_choices)
        selected[name], winners[name] = matrix, choices
    return selected, dict(selected=selected, selected_original_source=winners,
        radial_orders=list(range(4)), physical_angular_orders=list(range(5)),
        output_norm="complete unweighted Wiener A0, including the full v mean")


def scalar_domain(c):
    beta = [ball(x) for x in c["intrinsic_beta"][:4]]
    kjets = [ball(x) for x in c["intrinsic_K"][:4]]
    eta = [up(x) for x in c["eta_moduli"]]
    eta_low = lower(c["root_potential"]["complete_gaps"]["eta_real_lower"])
    lam_low = lower(c["root_potential"]["complete_gaps"]["kappa_modulus_lower"])
    lam_up = up(c["root_potential"]["complete_modulus_upper"]["kappa"])
    qgap = lower(c["root_potential"]["complete_gaps"]["one_plus_theta_modulus_lower"])
    if not (eta[0] >= eta_low and lam_up >= lam_low and kjets[1].lower() > 0):
        raise ArithmeticError("inconsistent true-root positive domain")
    result = dict(beta=beta, K=kjets, eta=eta, eta_low=eta_low,
        lambda_low=lam_low, lambda_up=lam_up, qgap=qgap,
        k1=kjets[1], k2=kjets[2], k3=kjets[3],
        Vroot=up(c["root_potential"]["complete_modulus_upper"]["V"]),
        shear=up(c["genuine_reference"]["root_shear_uniform_modulus_upper"]),
        J0=up(c["root_inverse"]["inverse_same_space"]),
        J1=up(c["root_inverse"]["inverse_followed_by_angular_derivative"]),
        L0=up(c["root_inverse"]["L_derivative_commutator_bounds"][0]))
    return result


def real_radial_intervals(s, t):
    u, v = t["U"], t["V"]
    beta, betar = s["beta"][:2]
    k1 = s["k1"]
    mu = nonnegative_interval(u[0][0]**2)
    mv = nonnegative_interval(v[0][0]**2)
    mur = symmetric(u[0][0]*u[1][0])
    eta_actual = s["eta_low"].union(s["eta"][0])
    eta_r, eta_rr = symmetric(s["eta"][1]), symmetric(s["eta"][2])
    e1, e2 = eta_r/eta_actual, eta_rr/eta_actual
    M = beta*mu
    Mr = betar*mu + beta*(2*mur + k1*mv)
    Bm, Em = beta-M, -beta-3*M
    Bmr = betar*(1-mu)-beta*(2*mur+3*k1*mv)
    Emr = -betar*(1+3*mu)-beta*(6*mur+k1*mv)
    ac, trad = e1+Em, e1-4*M
    acp = e2-e1**2+Emr
    tradp = e2-e1**2-4*Mr
    qrad, qradp = ac-Bm, acp-Bmr
    Vm = ac*Bm-Bmr
    c2, c3 = s["k2"]/(2*k1), s["k3"]/(6*k1)
    L = e1+c2/2
    bt = (2*e1+c2)/5
    bs = ex("2/7")*((e2+c3)/2+e1*(c2-bt)/2
                    +ex("3/8")*bt**2-c2*bt/4-c2**2/8)
    bA = (bt-c2)/4-2*M
    bC = bA**2+(2*bs-bt**2-2*c3+c2**2)/4-2*Mr
    return dict(m_u=mu, m_v=mv, m_ur=mur, eta_actual=eta_actual,
        eta_r=eta_r, eta_rr=eta_rr, e1=e1, e2=e2, M=M, Mr=Mr,
        Bm=Bm, Em=Em, Bmr=Bmr, Emr=Emr, ac=ac, acp=acp,
        trad=trad, tradp=tradp, qrad=qrad, qradp=qradp, Vm=Vm,
        c2=c2, c3=c3, L=L, bt=bt, bs=bs, bA=bA, bC=bC)


def product_jet(f, ar, g, br, q):
    return upper_sum(math.comb(q, j)*f[ar][j]*g[br][q-j]
                     for j in range(q+1))


def projected_product(f, ar, g, br):
    a = product_jet(f, ar, g, br, 0)
    b = product_jet(f, ar, g, br, 1)/4
    return whole_min([a, b])[0]


def complete_root_drift(s, t, c):
    u, v = t["U"], t["V"]
    b0, b1, b2 = map(up, s["beta"][:3])
    k1, k2 = up(s["k1"]), up(s["k2"])
    ps = projected_product(u, 0, u, 0)
    psr = up(2*projected_product(u, 0, u, 1)
             +k1*projected_product(v, 0, v, 0))
    psrr = up(2*projected_product(u, 1, u, 1)
              +2*projected_product(u, 0, u, 2)
              +k2*projected_product(v, 0, v, 0)
              +4*k1*projected_product(v, 0, v, 1))
    sph = product_jet(u, 0, u, 0, 1)
    sphph = product_jet(u, 0, u, 0, 2)
    srph = up(2*product_jet(u, 0, u, 1, 1)
              +k1*product_jet(v, 0, v, 0, 1))
    old = c["root_drift"]
    aux = c["aux_drift"]
    p_candidates = [up(b0*ps), up(old[1]), up(aux[1])]
    p, p_choice = whole_min(p_candidates)
    d_candidates = [up(p/4), up(old[0]), up(aux[0])]
    d, d_choice = whole_min(d_candidates)
    pph_candidates = [up(b0*sph), up(old[2]), up(aux[2])]
    pph, pph_choice = whole_min(pph_candidates)
    pphph = up(b0*sphph)
    pr = up(b1*ps+b0*psr)
    dr = up(pr/4)
    prph = up(b1*sph+b0*srph)
    prr = up(b2*ps+2*b1*psr+b0*psrr)
    Dp = up(pr+d*pph)
    D2p_terms = [prr, up(2*d*prph), up((dr+d*p)*pph),
                up(d*d*pphph)]
    D2p = upper_sum(D2p_terms)
    values = dict(d=d, p=p, pphi=pph, pphiphi=pphph, dr=dr,
                  pr=pr, prphi=prph, prr=prr, Dp=Dp, D2p=D2p)
    return values, dict(complete_projected_S_Sr_Srr=[ps, psr, psrr],
        complete_Sphi_Sphiphi_Srphi=[sph, sphph, srph],
        complete_bound_candidates=dict(d=d_candidates, p=p_candidates,
                                       pphi=pph_candidates),
        selected_candidate=dict(d=d_choice, p=p_choice, pphi=pph_choice),
        complete_derivative_bounds=values, D2p_four_complete_terms=D2p_terms)


def complete_rational_quotient(s, t, r):
    """R97.17-22 and RBO.3, with distinct alpha frequency quotient."""
    u, v = t["U"], t["V"]
    beta = list(map(up, s["beta"]))
    k1, k2 = up(s["k1"]), up(s["k2"])
    z = ex("1/9409")
    gap = ex("193/9409")
    def pairing(f, ar, g, br, order):
        opts = [up(f[ar][a]*g[br][order-a]/(4**order))
                for a in range(order+1) if a <= 4 and order-a <= 4]
        opts.append(up(96**order*f[ar][0]*g[br][0]))
        return whole_min(opts)[0]
    U = [up(2/gap*upper_sum(math.comb(m,a)*pairing(u,a,u,m-a,2)
                             for a in range(m+1))) for m in range(3)]
    W = [up(2/gap*upper_sum(math.comb(m,a)*pairing(v,a,v,m-a,2)
                             for a in range(m+1))) for m in range(2)]
    alpha = []
    alpha_terms = []
    for m in range(4):
        terms = []
        for a in range(m+1):
            for b in range(m-a+1):
                c = m-a-b
                mult = math.factorial(m)//(math.factorial(a)*math.factorial(b)
                                          *math.factorial(c))
                terms.append(up(mult*beta[a]*pairing(u,b,v,c,1)/gap))
        alpha_terms.append(terms)
        alpha.append(upper_sum(terms))
    alpha_zero = up(beta[0]*pairing(u,0,v,0,1))
    alpha_frequency_one = up(beta[0]*pairing(u,0,v,0,3)/gap)
    em = s["eta_low"]
    E1, E2, E3 = s["eta"][1:4]
    reciprocal = [up(1/em), up(E1/em**2),
        up(E2/em**2+2*E1**2/em**3),
        up(E3/em**2+6*E1*E2/em**3+6*E1**3/em**4)]
    h = [upper_sum(math.comb(j,a)*alpha[a]*reciprocal[j-a]
                   for a in range(j+1)) for j in range(4)]
    q = s["qgap"]
    Qterms = [
        [up(2*beta[0]*U[0]), up(h[1]/q)],
        [up(2*beta[1]*U[0]), up(2*beta[0]*U[1]),
         up(2*beta[0]*k1*W[0]), up(h[2]/q), up(z*h[1]**2/q**2)],
        [up(2*beta[2]*U[0]), up(4*beta[1]*U[1]), up(2*beta[0]*U[2]),
         up((4*beta[1]*k1+2*beta[0]*k2)*W[0]),
         up(4*beta[0]*k1*W[1]), up(h[3]/q),
         up(3*z*h[1]*h[2]/q**2), up(2*z*z*h[1]**3/q**3)]]
    Q = list(map(upper_sum, Qterms))
    qDterms = [up(Q[1]/2), up(up(r["qrad"])*Q[0]/2),
               up(z*Q[0]**2/4)]
    qD = upper_sum(qDterms)
    l2 = s["lambda_low"]**2
    c0 = up(qD/l2)
    d10 = up(32*k1*s["eta"][0]*alpha_zero/l2)
    c1terms = [up(Q[2]/2), up(up(r["qradp"])*Q[0]/2),
        up(up(r["qrad"])*Q[1]/2), up(z*Q[0]*Q[1]/2),
        up(4*up(r["bt"])*qD),
        up(32*k1*s["eta"][0]*alpha_frequency_one),
        up(16*k1*alpha[0]**2)]
    c1 = up(upper_sum(c1terms)/l2)
    values = dict(C0=c0, C1=c1, d10=d10)
    audit = dict(primitive_gap_exact="193/9409", z_interval=["0","1/9409"],
        theta_gap_original=s["qgap"], U_radial_0_2=U, W_radial_0_1=W,
        alpha_radial_0_3=alpha, alpha_Leibniz_terms=alpha_terms,
        alpha_at_z_zero=alpha_zero, alpha_frequency_quotient=alpha_frequency_one,
        reciprocal_eta_ordinary_0_3=reciprocal, h_ordinary_0_3=h,
        Q1_ordinary_0_2=Q, Q1_complete_positive_groups=Qterms,
        qDelta_three_groups=qDterms, qDelta=qD,
        C1_seven_groups_before_lambda_inverse_square=c1terms,
        complete_rational_bounds=values,
        third_radial_derivative_only_in_C1_right_input_power="-10/3")
    return values, audit


def complete_correlated_coefficients(s, t, r, d, q):
    """Exact collected identities first, positive bounds second."""
    u, v = t["U"], t["V"]
    beta, betar = s["beta"][:2]
    b0, b1 = up(beta), up(betar)
    k1, k2, eta = up(s["k1"]), up(s["k2"]), s["eta"][0]
    p, dp, d2p = d["p"], d["Dp"], d["D2p"]
    M, e1, c2 = r["M"], r["e1"], r["c2"]
    A, C, T, Tp = r["bA"], r["bC"], r["trad"], r["tradp"]
    bt, bs, L = r["bt"], r["bs"], r["L"]
    Bm, Bmp, ac, acp, Vm = r["Bm"], r["Bmr"], r["ac"], r["acp"], r["Vm"]
    v1, v1p = ac+4*Bm, acp+4*Bmp
    P1 = (ex("13/10")*C+ex("4/175")*L*(3*A-T)-ex("21/5")*T*A
        +ex("4/15")*bs-ex("4/21")*bt**2
        +ex("21/10")*(Vm-Tp)+v1*A+v1p)
    P2 = (-ex("523/140")*A-ex("619/140")*T+ex("26/875")*L
        -ex("4/525")*bt+ex("21/10")*v1)
    PD = ex("3/14")*A-ex("29/14")*T+ex("2/21")*bt+v1
    delta3_terms = [up(up(ex("4/15")*bs-ex("4/21")*bt**2)*p),
        up(ex("4/525")*up(bt)*p**2), up(ex("8/7875")*p**3),
        up((ex("2/21")*up(bt)+ex("4/105")*p)*dp),
        up(ex("37/18")*d2p)]
    Pv2 = projected_product(v,0,v,0)
    ZD = up(2*b0*k1*Pv2)
    ZDD_terms = [up(up(4*betar*s["k1"]+2*beta*s["k2"])*Pv2),
        up(4*b0*k1*(2*projected_product(v,0,v,1)
                     +2*d["d"]*v[0][0]*v[0][1]))]
    ZDD = upper_sum(ZDD_terms)
    ell = up(2*b0*u[0][0]*v[0][0])
    WAC_terms = [up(ell**2), up(4*b0*eta*v[0][0]*u[0][1])]
    WAC = upper_sum(WAC_terms)
    RDterms = [up(up(P1)*p), up(up(P2)*p**2),
        up(ex("55127/12600")*p**3), up(up(PD)*dp),
        up(ex("157/84")*p*dp), up(ex("19/18")*d2p),
        up((up(A+Bm-ac)+ex("9/10")*p)*ZD), ZDD, up(k1*WAC)]
    DeltaRD = upper_sum(RDterms)
    ECO = -ex("81/70")*e1+ex("6/35")*c2+3*beta+3*M
    Eterms = [up(up(ECO)*p), up(ex("291/140")*p*p),
              up(ex("15/14")*dp), ZD]
    E = up(upper_sum(Eterms)/s["lambda_low"]**2)
    KH = -beta-M/3-ex("7/15")*e1-ex("2/5")*c2
    Hterms = [up((up(KH)+ex("2/15")*p)*E),
        up(ex("37/30")*p*s["Vroot"]),
        up(DeltaRD/(3*s["lambda_low"]**2)), up(q["d10"]/3)]
    H = upper_sum(Hterms)
    astar_scalar = e1/10-c2/5-beta-M
    astar = up(up(astar_scalar)+ex("11/10")*p)
    # At the true root, bop=beta-M+p=beta*(1-u^2), with the full mean retained.
    bop_candidates = [up(up(Bm)+p), up(b0*(1+u[0][0]**2))]
    bop, bop_choice = whole_min(bop_candidates)
    ellr = up(2*b1*u[0][0]*v[0][0]
               +2*b0*(u[1][0]*v[0][0]+u[0][0]*v[1][0]))
    ellphi = up(2*b0*(u[0][1]*v[0][0]+u[0][0]*v[0][1]))
    eta_low = s["eta_low"]
    Dl_eta_terms = [up(ellr/eta_low),
        up(ell*s["eta"][1]/eta_low**2), up(d["d"]*ellphi/eta_low)]
    Dl_eta = upper_sum(Dl_eta_terms)
    A1terms = [up(ex("6/5")*d["pphi"]), up(Dl_eta/2),
               up(ell*p/(2*eta_low))]
    A1 = upper_sum(A1terms)
    values = dict(E=E, H=H, A=astar, A1=A1, b=bop, V=s["Vroot"],
                  C0=q["C0"], C1=q["C1"], d10=q["d10"])
    audit = dict(radial_signed_collected_coefficients=dict(P1=P1,P2=P2,PD=PD,
        E0_coefficient=ECO, KH=KH, astar_scalar=astar_scalar),
        delta3_five_complete_terms=delta3_terms,
        delta3=upper_sum(delta3_terms), ZD=ZD, ZDD=ZDD,
        ZDD_two_complete_terms=ZDD_terms, WAC_two_complete_terms=WAC_terms,
        DeltaRD_nine_complete_terms=RDterms, DeltaRD=DeltaRD,
        E0_four_terms_before_lambda_inverse_square=Eterms,
        H0_four_complete_terms=Hterms, bop_complete_candidates=bop_candidates,
        bop_selected_candidate=bop_choice, ell=ell, ell_r=ellr, ell_phi=ellphi,
        D_ell_over_eta_three_terms=Dl_eta_terms,
        signed_first_amplitude_three_terms=A1terms, complete_bounds=values,
        two_frequency_signs_share_one_multiplier=True,
        nonzero_constant_d10_kept_without_z=True)
    return values, audit


def complete_profile_and_error(s, f):
    """Every RBO.11-13 term, including the positive mean-rank and I/4."""
    shear = s["shear"]
    if not (1-2*shear > 0):
        raise ArithmeticError("missing original terminal-Ai shear gap")
    Astar = up((1+2*shear)*ex("5/9"))
    Dstar = up((1+2*shear)/3)
    g = ((1-2*shear)*(ex("1/3")
        +4*s["lambda_low"]/(21*s["eta"][0]))).lower()
    if not g.is_finite() or not g > 0:
        raise ArithmeticError("nonpositive genuine diagonal lower")
    powers = {}
    for exponent in ("-1/3","-2/3","-1","-4/3","-2","-10/3","-4","-6"):
        powers[exponent] = up((ex(388).log()*ex(exponent)).exp())
    E,H,A,A1,b,V,C0,C1 = [f[k] for k in ("E","H","A","A1","b","V","C0","C1")]
    n = powers
    amp_terms = [up(Dstar*E*n["-4/3"]), up(16*Dstar*C0*n["-10/3"])]
    eamp = upper_sum(amp_terms)
    rterms = [up(A*Astar), up(A1*Astar*n["-1"]),
        up(H*Dstar*n["-4/3"]),
        up(16*(A*C0+C1/3)*Dstar*n["-10/3"]),
        up(s["lambda_up"]*V*E*Astar*n["-2"]),
        up(16*s["lambda_up"]*(E+V)*C0*Astar*n["-4"]),
        up(256*s["lambda_up"]*C0*C0*Astar*n["-6"]),
        up(b*E*Dstar*n["-4/3"])]
    r0 = upper_sum(rterms)
    IR0 = up(r0/4)
    leading_I = up(s["lambda_up"]*Dstar*n["-1/3"])
    JL = up(s["J1"]*s["L0"])
    inverse_terms = [r0, up(JL*(leading_I+IR0))]
    inverse_error = up(n["-2/3"]/s["eta_low"]*upper_sum(inverse_terms))
    e = up(eamp+inverse_error)
    # Decide on the exact balls that the final receipt will actually retain.
    retained_e = ball(e.str(75))
    retained_g = ball(g.str(75))
    margin = retained_g.lower()-retained_e.upper()
    strict = bool(retained_e.upper() < retained_g.lower())
    result = dict(cutoff_abs_j=97, physical_minimum_frequency=388,
        original_shear_uniform_upper=shear, Ai_A_upper=Astar,
        Ai_D_upper=Dstar, genuine_diagonal_lower=g,
        right_input_powers=powers, amplitude_two_terms=amp_terms,
        complete_unprojected_amplitude_upper=eamp, E2_upper=eamp,
        R0_eight_complete_terms=rterms, R0_upper=r0,
        complete_positive_mean_rank=rterms[-1],
        complete_IR0_upper=IR0, high_leading_primitive_upper=leading_I,
        same_original_J1_L0_product=JL, inverse_error_two_groups=inverse_terms,
        complete_inverse_error_upper=inverse_error,
        complete_stable_error_upper=e, strict_margin=margin,
        strict_comparison_uses_retained_75_digit_ball_endpoints=True,
        original_cutoff97_sufficient_gate_passed=strict,
        root_stable_injectivity_certified=strict,
        same_window_onto_only_with_original_SE_identity=strict,
        negative_window_numerical_inverse_claimed=False,
        complete_incoming_inverse_claimed=False, finite_Schur_inverse_claimed=False,
        physical_independent_means_retained=True, full_IR0_norm_is_not_high_cut=True)
    return result


def checked_inputs(args, doc):
    mraw = Path(args.manifest).read_bytes()
    m = json.loads(mraw)
    actual_runtime = {"Python": platform.python_version(),
        "python_flint": importlib.metadata.version("python-flint")}
    doc["runtime"] = actual_runtime
    gate(doc, "actual public Actions runtime and frozen new source",
        os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == PUBLIC
        and actual_runtime == RUNTIME and ctx.prec == args.bits == 320
        and isinstance(doc["actual_scientific_checkout_commit"], str)
        and len(doc["actual_scientific_checkout_commit"]) == 40
        and all(c in "0123456789abcdef" for c in doc["actual_scientific_checkout_commit"])
        and sha(mraw) == args.manifest_sha
        and m.get("kind") == MANIFEST_KIND and m.get("public_repository") == PUBLIC
        and m.get("scientific_runtime") == RUNTIME
        and m.get("source_path") == SOURCE
        and m.get("source_sha256") == sha(Path(__file__).read_bytes())
        and m.get("parameters") == PARAMETERS)
    files = m["files"]
    fmap = {f["role"]: f for f in files}
    current_roles = set(PINNED)-{"majorants_native","root_native"}
    expected_current = current_roles | {"source","worker","rules"}
    gate(doc, "complete current and two-history manifest closure",
        len(files) == len(fmap) == 16 and set(fmap) == expected_current
        and m.get("historical_inputs") == HISTORICAL_INPUTS
        and m.get("mathematical_input_sha256") == PINNED
        and m.get("expected_actual_gate_count") == GATE_COUNT
        and m.get("expected_current_input_count") == 16
        and m.get("expected_input_count") == 18
        and m.get("expected_immutable_AST_files") == 2
        and m.get("current_input_paths") == [f["path"] for f in files]
        and m.get("file_sha256") == {f["path"]: f["sha256"] for f in files}
        and m.get("input_paths") == {**{f["role"]: f["path"] for f in files},
              **{h["role"]: h["path"] for h in HISTORICAL_INPUTS}}
        and all(fmap[k]["path"] == PIN_SPECS[k]["path"]
            and fmap[k]["bytes"] == PIN_SPECS[k]["bytes"]
            and fmap[k]["sha256"] == PINNED[k]
            and fmap[k]["git_blob"] == PIN_SPECS[k]["git_blob"]
            for k in current_roles)
        and fmap["source"]["path"] == SOURCE
        and fmap["rules"]["sha256"] == "65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1"
        and not m.get("legacy_artifact_inputs")
        and m.get("old_successful_scientific_calls_allowed") is False
        and m.get("new_native_arrays_or_artifact_persistence_allowed") is False)
    paths = {}
    raw_objects = {}
    identities = {}
    for f in files:
        path = args.repo / f["path"]
        data = path.read_bytes()
        if len(data) != f["bytes"] or sha(data) != f["sha256"]:
            raise ValueError("changed current input: " + f["role"])
    for role, spec in PIN_SPECS.items():
        path = args.repo / spec["path"]
        data = path.read_bytes()
        if len(data) != spec["bytes"] or sha(data) != spec["sha256"]:
            raise ValueError("changed pinned mathematical input: " + role)
        paths[role] = path
        identities[role] = {"bytes": len(data), "sha256": sha(data)}
        if role.endswith("_proof") or role == "r97_contract":
            raw_objects[role] = data.decode("utf-8")
        else:
            if role in ("majorants_native", "root_native"):
                data = gzip.decompress(data)
                if len(data) > 2000000:
                    raise ValueError("old native exceeds its safe decoding limit")
            raw_objects[role] = json.loads(data)
    gate(doc, "all fifteen mathematical originals and sixteen current texts match byte pins",
        set(identities) == set(PINNED)
        and all(v["sha256"] == PINNED[k] for k,v in identities.items()))
    doc["input_sha256"] = {"manifest": sha(mraw), **PINNED}
    doc["verified_original_inputs"] = identities
    h, a, rp, pub, pe, ge, fa, rn, maj = [
        raw_objects[k] for k in ("high_root","auxiliary","root_process",
            "root_publication","potential_execution","genuine_execution",
            "fa_science","root_native","majorants_native")]
    gate(doc, "original high-root intrinsic run is complete at its fixed bump-zero root",
        h["complete"] is True and h["actual_returncode"] == 0
        and h["failure"] is None and h["mathematical_complete"] is True
        and h["mathematical_proved"] is True and h["mathematical_failure"] is None
        and str(h["run_id"]) == "43651259105" and str(h["run_attempt"]) == "1"
        and h["mathematical_source_sha256"] == OLD_SOURCES["high_root"]
        and h["manifest_sha256"] == OLD_MANIFESTS["high_root"]
        and h["runtime"] == OLD_RUNTIME and passed_gates(h,"mathematical_gates",15)
        and h["actual_intrinsic_parameter"] == "eta_0"
        and h["complete_intrinsic_delta_independence_only_on_original_bump_zero_germ"] is True
        and h["other_intrinsic_parameters_given_the_same_true_root"] is False
        and h["intrinsic_stage"]["complete"] is True
        and h["at_the_certified_true_root"]["exact_K0"] == "0"
        and h["at_the_certified_true_root"]["raw_new_K0_ball_retained"] is True
        and h["auxiliary_process_sha256"] == PINNED["auxiliary"])
    cases = {c["exact_auxiliary_radius"]: c for c in a["cases"]}
    small = cases["1/10000"]
    gate(doc, "only separately successful auxiliary cases are accepted and its global failure stays visible",
        a["complete"] is False and a["actual_returncode"] == 1
        and a["mathematical_complete"] is True and a["mathematical_proved"] is False
        and a["failure"] == {"type":"SystemExit","message":"1"}
        and str(a["run_id"]) == "43640181602" and str(a["run_attempt"]) == "1"
        and a["mathematical_source_sha256"] == OLD_SOURCES["auxiliary"]
        and a["manifest_sha256"] == OLD_MANIFESTS["auxiliary"]
        and passed_gates(a,"mathematical_gates",7)
        and a["successful_auxiliary_domains"] == ["1/10000","1/2000"]
        and set(cases) == {"1/10000","1/2000","1/1000","1/500"}
        and all(cases[k]["complete"] is True and cases[k]["proved"] is True
                and cases[k]["failure"] is None
                and cases[k]["intrinsic_domain_failure"] is None
                for k in ("1/10000","1/2000"))
        and all(cases[k]["proved"] is False for k in ("1/1000","1/500"))
        and small["accepted_original_cubic_components"] == {"candidate":65,"response":193}
        and a["failed_auxiliary_domains"] == h["original_auxiliary_failed_cases_preserved"])
    pub_native = [v for v in pub["files"]
        if v["file"] == "consumers/complete-moving-root-scalarization.json.gz"]
    pub_process = [v for v in pub["files"] if v["file"] == "consumers/process.json"]
    gate(doc, "root process and publication bind the same complete sharper native",
        rp["complete"] is True and rp["actual_returncode"] == 0
        and rp["mathematical_complete"] is True
        and str(rp["run_id"]) == str(pub["run_id"]) == "43594466882"
        and str(rp["run_attempt"]) == "1"
        and rp["mathematical_source_sha256"] == OLD_SOURCES["root_native"]
        and rp["manifest_sha256"] == OLD_MANIFESTS["root_process"]
        and rp["native_sha256"] == PINNED["root_native"]
        and passed_gates(rp,"mathematical_gates",13)
        and pub["complete"] is True and pub["actual_returncode"] == 0
        and len(pub_native) == len(pub_process) == 1
        and pub_native[0]["bytes"] == 30595
        and pub_native[0]["sha256"] == pub_native[0]["original_sha256"] == PINNED["root_native"]
        and pub_process[0]["bytes"] == 4120
        and pub_process[0]["sha256"] == pub_process[0]["original_sha256"] == PINNED["root_process"])
    p = pe["actual_scientific_receipt"]
    pcases = {c["exact_complex_radial_radius"]: c for c in p["cases"]}
    rootcase, terminalcase = pcases["9/1000000"], pcases["1/6000"]
    gate(doc, "potential actual success separates the root case from the full terminal case",
        pe["complete"] is True and pe["actual_returncode"] == 0
        and str(pe["run_id"]) == "43685624307" and str(pe["run_attempt"]) == "1"
        and p["complete"] is True and p["proved"] is True
        and p["actual_returncode"] == 0 and p["failure"] is None
        and p["source_sha256"] == OLD_SOURCES["potential_execution"]
        and p["input_manifest_sha256"] == OLD_MANIFESTS["potential_execution"]
        and p["runtime"] == OLD_RUNTIME and passed_gates(p,"gates",16)
        and all(c["complete"] is True and c["proved"] is True
            and c["failure"] is None and c["fixed_intrinsic_parameter"] == "eta_0"
            and c["exact_complex_delta_square_halfwidth"] == "1/100000000"
            and c["exact_complex_z_square_halfwidth"] == "1/9409"
            and c["all_integer_modes_abs_j_at_least"] == 97
            and c["both_carrier_signs_retained"] is True
            and c["physical_mean_is_not_z_zero_limit"] is True
            for c in (rootcase, terminalcase))
        and rootcase["reference_image"]["entire_original_physical_root_piece_covered"] is False
        and terminalcase["reference_image"]["entire_original_physical_root_piece_covered"] is True
        and up(terminalcase["complete_modulus_upper"]["V"]) < 276
        and lower(terminalcase["reference_image"]["complete_image_disk_radius_lower"]) > ex("1/2000"))
    g = ge["actual_scientific_receipt"]
    gr = g["reference_columns"]
    gate(doc, "genuine terminal Ai uses its original nonzero shear and both full columns",
        ge["complete"] is True and ge["actual_returncode"] == 0
        and str(ge["run_id"]) == "43688459733" and str(ge["run_attempt"]) == "1"
        and g["complete"] is True and g["proved"] is True
        and g["actual_returncode"] == 0 and g["failure"] is None
        and g["source_sha256"] == OLD_SOURCES["genuine_execution"]
        and g["input_manifest_sha256"] == OLD_MANIFESTS["genuine_execution"]
        and g["runtime"] == OLD_RUNTIME and passed_gates(g,"gates",16)
        and gr["exact_real_T_interval"] == ["-1/2000","1/2000"]
        and gr["complete_potential_modulus_used"] == 276
        and gr["all_abs_j_at_least"] == 97 and gr["physical_frequency"] == "n=4|j|"
        and gr["exact_root_relative_matrix"] == "[[1,0],[beta_n,1]]"
        and gr["both_independent_columns_retained"] is True
        and gr["both_carrier_signs_retained"] is True
        and gr["physical_mean_is_not_z_zero_limit"] is True
        and g["numerical_reference_column_samples_computed"] == 0
        and gr["numerical_reference_column_samples_computed"] == 0)
    gate(doc, "FA2 success preserves the complete original mixed-stage payload",
        fa["complete"] is True and fa["proved"] is True
        and fa["actual_returncode"] == 0 and fa["failure"] is None and fa["stage"] == "complete-new-free-Airy-strong-cut-scalars"
        and str(fa["run_id"]) == "43763658978" and str(fa["run_attempt"]) == "1"
        and fa["source_sha256"] == OLD_SOURCES["fa_science"]
        and fa["input_manifest_sha256"] == OLD_MANIFESTS["fa_science"]
        and fa["runtime"] == FA_RUNTIME and passed_gates(fa,"gates",24)
        and fa["original_complete_fold_payload_sha256"] == FOLD_PAYLOAD
        and fa["mathematical_parameters"]["exact_real_delta_radius"] == "1/100000000"
        and fa["mathematical_parameters"]["exact_coefficient_strip"] == "1/32"
        and fa["mathematical_parameters"]["exact_fold_radius"] == "3/8000"
        and fa["mathematical_parameters"]["exact_fold_strip"] == "3/128"
        and fa["mathematical_parameters"]["complete_physical_means_and_intermediate_projection_ranks_retained"] is True)
    gate(doc, "restored root native has its original complete ordinary L2 and left derivative identity",
        rn["kind"] == "complete_moving_current_root_scalarization_operator_budget"
        and rn["complete"] is True and rn["proved"] is True and rn["failure"] is None
        and rn["source_sha256"] == OLD_SOURCES["root_native"] and rn["runtime"] == ROOT_RUNTIME
        and str(rn["public_run_id"]) == "43594466882" and str(rn["public_run_attempt"]) == "1"
        and rn["gates"] == rp["mathematical_gates"]
        and rn["candidate_sha256"] == CANDIDATE
        and rn["background_definition_sha256"] == BASE
        and rn["explicit_direction_definition_sha256"] == DIRECTION
        and rn["inputs"]["root_germ"]["sha256"] == ROOT_GERM
        and rn["same_space_norms"] == ["complete_A_sigma","complete_H0_sigma","ordinary_L2"]
        and rn["angular_zero_mode_removed_only_in_A_inverse"] is True
        and rn["actual_independent_even_mean_preserved"] is True
        and rn["full_frequency_inverse_not_a_finite_section"] is True
        and rn["actual_nonlocal_operator_retained"] is True)
    payload = maj["payload"]
    gate(doc, "restored original 4501-byte stage has its complete no-LF payload identity",
        maj["complete"] is True
        and maj["stage"] == maj["name"] == "complete-original-reference-holomorphic-majorants"
        and maj["source_sha256"] == "f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
        and maj["algebra_sha256"] == "1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
        and maj["input_manifest_sha256"] == "76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
        and maj["runtime"] == OLD_RUNTIME
        and original_payload_sha(payload) == FOLD_PAYLOAD
        and all(payload["majorants"][k][1:] == ["3/8000","3/128"] for k in ("A","chi")))
    roots = PARAMETERS["exact_root_interval"]
    gate(doc, "all actual inputs restrict to the same real family and single root piece",
        h["exact_root_interval"] == a["exact_root_interval"] == rn["exact_root_interval"] == roots
        and fa["mathematical_parameters"]["exact_root_interval"] == roots
        and h["root_germ_sha256"] == a["root_germ_sha256"] == ROOT_GERM
        and h["object_sha256"] == a["object_sha256"] == OBJECT
        and h["exact_fixed_intrinsic_parameter"] == rn["exact_intrinsic_parameter"]
            == PARAMETERS["exact_intrinsic_parameter"]
        and a["exact_complex_delta_radius"] == rn["exact_complex_parameter_radius"] == "1/100000000"
        and a["original_polynomial_piece"] == rn["exact_candidate_and_response_piece"] == 2549
        and fa["mathematical_parameters"]["physical_root_piece"] == 2549
        and h["exact_original_physical_piece_interval"] == a["exact_original_piece_interval"] == rn["exact_piece_interval"]
        and a["background_definition_sha256"] == BASE
        and a["explicit_direction_definition_sha256"] == DIRECTION
        and a["original_root_budget_sha256"] == PINNED["root_native"]
        and rn["exact_outer_radial_radius"] == "1/100000"
        and rn["exact_moving_Wiener_strip"] == "1/1024")
    accepted = {
        "high_root": {"run_id":h["run_id"], "source_sha256":h["mathematical_source_sha256"],
            "manifest_sha256":h["manifest_sha256"], "gates":15,
            "runtime":copy.deepcopy(h["runtime"]), "fixed_intrinsic_parameter":"eta_0",
            "intrinsic_delta_independence_only_on_original_bump_zero_germ":True},
        "auxiliary": {"run_id":a["run_id"], "source_sha256":a["mathematical_source_sha256"],
            "manifest_sha256":a["manifest_sha256"], "gates":7,
            "global_complete":False,"global_returncode":1,"global_proved":False,
            "global_failure":copy.deepcopy(a["failure"]),
            "global_mathematical_failure":copy.deepcopy(a["mathematical_failure"]),
            "selected_exact_radius":"1/10000",
            "successful_domains":copy.deepcopy(a["successful_auxiliary_domains"]),
            "failed_domains":copy.deepcopy(a["failed_auxiliary_domains"])},
        "root": {"run_id":rp["run_id"], "source_sha256":rp["mathematical_source_sha256"],
            "manifest_sha256":rp["manifest_sha256"], "gates":13,
            "runtime":copy.deepcopy(rn["runtime"]), "original_arithmetic_bits":256,
            "native_sha256":rp["native_sha256"],
            "left_derivative_reason":"J=eta^-1 I(1+L eta^-1 I)^-1; partial_phi J=eta^-1(1+L eta^-1 I)^-1"},
        "potential": {"run_id":pe["run_id"], "source_sha256":p["source_sha256"],
            "manifest_sha256":p["input_manifest_sha256"], "gates":16,
            "runtime":copy.deepcopy(p["runtime"]), "root_radius":"9/1000000",
            "terminal_radius":"1/6000", "root_case_whole_piece":False},
        "genuine": {"run_id":ge["run_id"],"source_sha256":g["source_sha256"],
            "manifest_sha256":g["input_manifest_sha256"],"gates":16,
            "runtime":copy.deepcopy(g["runtime"]),"full_original_terminal_certificate_retained":True},
        "FA2": {"run_id":fa["run_id"],"source_sha256":fa["source_sha256"],
            "manifest_sha256":fa["input_manifest_sha256"],"gates":24,
            "runtime":copy.deepcopy(fa["runtime"]),"original_payload_sha256":FOLD_PAYLOAD},
        "majorants": {"source_sha256":maj["source_sha256"],
            "manifest_sha256":maj["input_manifest_sha256"],
            "algebra_sha256":maj["algebra_sha256"],"payload_sha256":FOLD_PAYLOAD,
            "runtime":copy.deepcopy(maj["runtime"])}}
    doc["accepted_old_inputs"] = accepted
    old_norm = small["full_family_norm_summary"]["1/32"]
    inverse_keys = ["inverse_same_space","inverse_followed_by_angular_derivative",
                    "L_derivative_commutator_bounds","integer_derivative_recursion"]
    def original_ball_record(value):
        if set(value) != {"ball","lower","upper","mid_float","radius_upper_float"}:
            raise ValueError("unexpected original root scalar record")
        return {"ball": copy.deepcopy(value["ball"])}
    root_inverse_records = {}
    for key in inverse_keys:
        value = rn[key]
        root_inverse_records[key] = ([original_ball_record(x) for x in value]
            if isinstance(value, list) else original_ball_record(value))
    copied = {
        "mixed": {k: copy.deepcopy(payload["coefficients"][k]) for k in ("U","V")},
        "intrinsic_K": copy.deepcopy(h["intrinsic_stage"]["ordinary_old_radial_jets"]["K"][:4]),
        "intrinsic_beta": copy.deepcopy(h["intrinsic_stage"]["ordinary_old_radial_jets"]["beta"][:4]),
        "eta_moduli": copy.deepcopy(small["complete_family"]["complete_eta_ordinary_jets_modulus_upper"]),
        "complete_mean_moduli": copy.deepcopy(small["complete_family"]["complete_mean_ordinary_jets_modulus_upper"]),
        "root_angular": {k:[original_ball_record(x) for x in rn["full_family_"+k+"_angular_norms"]] for k in ("U","V")},
        "aux_radial": {k:copy.deepcopy(old_norm[k+"_ordinary_radial_orders0to3"]) for k in ("U","V")},
        "root_drift": [original_ball_record(rn[k]) for k in
            ("moving_d_Astrip","moving_d_phi_Astrip","moving_d_phiphi_Astrip")],
        "aux_drift": copy.deepcopy(old_norm["full_drift_angular_bounds"]),
        "root_inverse": root_inverse_records,
        "root_record_projection": {
            "kind":"verbatim original ball string; unused display metadata referenced",
            "count":24, "original_native_sha256":PINNED["root_native"],
            "original_field_counts":{
                "full_family_U_angular_norms":5,"full_family_V_angular_norms":5,
                "moving_d_Astrip":1,"moving_d_phi_Astrip":1,"moving_d_phiphi_Astrip":1,
                "inverse_same_space":1,"inverse_followed_by_angular_derivative":1,
                "L_derivative_commutator_bounds":4,"integer_derivative_recursion":5},
            "unconsumed_record_fields":["lower","upper","mid_float","radius_upper_float"],
            "original_complete_native_records_unchanged":True},
        "root_potential": copy.deepcopy(rootcase),
        "terminal_potential_qualification": {
            "exact_complex_radial_radius":terminalcase["exact_complex_radial_radius"],
            "V":copy.deepcopy(terminalcase["complete_modulus_upper"]["V"]),
            "reference_image":copy.deepcopy(terminalcase["reference_image"])},
        "genuine_reference":copy.deepcopy(gr)}
    gate(doc, "every complete original mixed and angular row is finite with full means",
        all(len(copied["mixed"][k]) == 4
            and all(len(row)==5 for row in copied["mixed"][k]) for k in ("U","V"))
        and all(len(copied["root_angular"][k]) == 5 and len(copied["aux_radial"][k]) == 4
                for k in ("U","V"))
        and len(copied["eta_moduli"]) == len(copied["complete_mean_moduli"]) == 4
        and all(ball(x).is_finite()
            for k in ("U","V") for row in copied["mixed"][k] for x in row)
        and all(ball(x).is_finite()
            for k in ("U","V") for x in copied["root_angular"][k]+copied["aux_radial"][k])
        and all(ball(x).is_finite() for x in copied["eta_moduli"]+copied["intrinsic_K"]+copied["intrinsic_beta"]))
    doc["copied_old_inputs"] = copied
    doc["copied_old_inputs_sha256"] = sha(canonical(copied))
    return m, paths, copied


RETAINED_SCOPE = {"scientific_target":"one complete ordinary-L2 original-cutoff97 root stable scalar comparison","exact_real_parameter_family_only":True,"fixed_eta0_and_same_root_piece":True,"full_complex_square_result_claimed":False,"full_mean_of_v_and_every_radial_mean_retained":True,"independent_physical_mean_coordinates":2,"original_reflection_and_nonmean_inverse_domains_retained":True,"complete_two_reference_columns_and_two_carrier_signs_retained":True,"root_potential_small_case_does_not_replace_terminal_shear_case":True,"lambda_is_physical_root_kappa_not_frequency_Airy_scale":True,"positive_mean_rank_is_kept":True,"only_proved_diagonal_mean_subterm_vanishes":True,"full_IR0_uses_original_one_quarter":True,"input_diagonals_not_commuted_through_multipliers_or_J":True,"original_J1_is_complete_left_angular_derivative":True,"old_negative_Sobolev_norms_not_inferred_from_L2":True,"true_nonzero_beta_n_retained":True,"actual_PDE_solution_claimed":False,"full_incoming_inverse_claimed":False,"finite_Schur_inverse_claimed":False,"nonlinear_background_or_final_surface_claimed":False,"next_cutoff_or_scientific_rerun_triggered":False}
COUNTS = {"original_current_mathematical_texts":13,"original_historical_natives":2,"complete_old_mixed_entries":40,"selected_complete_mixed_entries":40,"original_auxiliary_successful_cases":2,"original_auxiliary_failed_cases_retained":2,"reciprocal_eta_derivatives":4,"alpha_ordinary_derivatives":4,"Q1_ordinary_derivatives":3,"delta3_positive_groups":5,"DeltaRD_positive_groups":9,"E0_positive_groups":4,"H0_positive_groups":4,"C1_positive_groups":7,"amplitude_positive_groups":2,"R0_positive_groups":8,"new_original_cutoff_comparisons":1,"old_successful_scientific_targets_recomputed":0,"old_scientific_modules_imported":0,"new_reference_or_potential_or_fold_solutions":0,"new_grid_or_array_outputs":0}
COMPLETE_FIELDS = ["kind","complete","proved","actual_returncode","failure","stage","source_sha256","input_manifest_sha256","public_repository","run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit","runtime","arithmetic_bits","parameters","input_sha256","verified_original_inputs","accepted_old_inputs","copied_old_inputs","copied_old_inputs_sha256","complete_mixed_norm_conclusion","complete_root_domain_conclusion","complete_real_radial_interval_conclusion","complete_root_drift_conclusion","complete_rational_quotient_conclusion","complete_correlated_coefficient_conclusion","complete_ordered_operator_conclusion","original_cutoff97_sufficient_gate_passed","retained_scope","counts","gates","actual_mathematical_wall_seconds"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every original root97 scientific result")
    ctx.prec = args.bits
    started = time.monotonic()
    doc = dict(kind=KIND, complete=False, proved=False, actual_returncode=None,
        failure=None, stage="identity",
        source_sha256=sha(Path(__file__).read_bytes()),
        input_manifest_sha256=sha(args.manifest.read_bytes()),
        public_repository=PUBLIC, run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        runtime={}, arithmetic_bits=args.bits, parameters=copy.deepcopy(PARAMETERS),
        retained_scope=copy.deepcopy(RETAINED_SCOPE), counts=copy.deepcopy(COUNTS),
        gates=[])
    try:
        m, paths, copied = checked_inputs(args, doc)
        doc["stage"] = "complete_old_inputs_read"
        persist(args.out, doc)
        mixed, mixed_audit = select_complete_mixed(copied)
        domain = scalar_domain(copied)
        doc["complete_mixed_norm_conclusion"] = encoded(mixed_audit)
        doc["complete_root_domain_conclusion"] = encoded(domain)
        gate(doc, "complete mixed selection and actual independent root gaps are finite",
            finite_tree(mixed) and finite_tree(domain)
            and domain["qgap"] > 0 and domain["eta_low"] > 0
            and domain["lambda_low"] > 0 and domain["K"][1].lower() > 0
            and len(mixed["U"]) == len(mixed["V"]) == 4)
        doc["stage"] = "complete_new_root_domain"
        persist(args.out, doc)
        radial = real_radial_intervals(domain, mixed)
        doc["complete_real_radial_interval_conclusion"] = encoded(radial)
        gate(doc, "complete real moments and neighborhood radial derivatives retain all mean terms",
            finite_tree(radial) and all(k in radial for k in
                ("Mr","Bmr","Emr","acp","qradp","tradp","bA","bC")))
        doc["stage"] = "complete_new_radial_intervals"
        persist(args.out, doc)
        drift, drift_audit = complete_root_drift(domain, mixed, copied)
        doc["complete_root_drift_conclusion"] = encoded(drift_audit)
        gate(doc, "complete mixed drift derivatives and every D squared p term are finite",
            finite_tree(drift_audit) and len(drift) == 10
            and len(drift_audit["D2p_four_complete_terms"]) == 4)
        doc["stage"] = "complete_new_root_drift"
        persist(args.out, doc)
        quotient, quotient_audit = complete_rational_quotient(domain, mixed, radial)
        doc["complete_rational_quotient_conclusion"] = encoded(quotient_audit)
        gate(doc, "complete rational quotient retains both gaps and all third ordinary derivatives",
            finite_tree(quotient_audit)
            and len(quotient_audit["reciprocal_eta_ordinary_0_3"]) == 4
            and len(quotient_audit["h_ordinary_0_3"]) == 4
            and len(quotient_audit["Q1_ordinary_0_2"]) == 3
            and list(map(len,quotient_audit["Q1_complete_positive_groups"])) == [2,5,8]
            and len(quotient_audit["C1_seven_groups_before_lambda_inverse_square"]) == 7)
        doc["stage"] = "complete_new_rational_quotient"
        persist(args.out, doc)
        coefficients, coefficient_audit = complete_correlated_coefficients(
            domain, mixed, radial, drift, quotient)
        doc["complete_correlated_coefficient_conclusion"] = encoded(coefficient_audit)
        gate(doc, "complete collected correlations preserve all nine derivative groups and the true mean",
            finite_tree(coefficient_audit)
            and len(coefficient_audit["delta3_five_complete_terms"]) == 5
            and len(coefficient_audit["DeltaRD_nine_complete_terms"]) == 9
            and len(coefficient_audit["E0_four_terms_before_lambda_inverse_square"]) == 4
            and len(coefficient_audit["H0_four_complete_terms"]) == 4)
        doc["stage"] = "complete_new_correlated_coefficients"
        persist(args.out, doc)
        result = complete_profile_and_error(domain, coefficients)
        doc["complete_ordered_operator_conclusion"] = encoded(result)
        doc["original_cutoff97_sufficient_gate_passed"] = result["original_cutoff97_sufficient_gate_passed"]
        gate(doc, "all ordered operator terms and genuine positive diagonal bounds are complete",
            finite_tree(result) and result["genuine_diagonal_lower"] > 0
            and result["complete_stable_error_upper"] >= 0
            and len(result["amplitude_two_terms"]) == 2
            and len(result["R0_eight_complete_terms"]) == 8
            and result["complete_positive_mean_rank"] == result["R0_eight_complete_terms"][-1])
        doc["stage"] = "complete_new_cutoff97_comparison"
        persist(args.out, doc)
        gate(doc, "the optional strict comparison has its exact narrow ordinary L2 scope",
            type(doc["original_cutoff97_sufficient_gate_passed"]) is bool
            and result["original_cutoff97_sufficient_gate_passed"] == bool(
                ball(doc["complete_ordered_operator_conclusion"]["complete_stable_error_upper"]).upper()
                < ball(doc["complete_ordered_operator_conclusion"]["genuine_diagonal_lower"]).lower())
            and result["cutoff_abs_j"] == 97 and result["physical_minimum_frequency"] == 388
            and result["negative_window_numerical_inverse_claimed"] is False
            and result["complete_incoming_inverse_claimed"] is False
            and result["finite_Schur_inverse_claimed"] is False
            and result["physical_independent_means_retained"] is True)
        gate(doc, "all original input bytes remain unchanged with zero old target calls",
            all(sha(path.read_bytes()) == PINNED[k] for k,path in paths.items())
            and all(len(path.read_bytes()) == PIN_SPECS[k]["bytes"] for k,path in paths.items())
            and doc["counts"]["old_successful_scientific_targets_recomputed"] == 0
            and doc["counts"]["old_scientific_modules_imported"] == 0
            and sha(canonical(doc["copied_old_inputs"])) == doc["copied_old_inputs_sha256"])
        doc["actual_mathematical_wall_seconds"] = time.monotonic()-started
        gate(doc, "complete scalar schema retains every conclusion whether the sufficient test passes or fails",
            len(doc["gates"]) == GATE_COUNT-1 and set(doc) == set(COMPLETE_FIELDS)
            and doc["parameters"] == PARAMETERS and doc["retained_scope"] == RETAINED_SCOPE
            and doc["counts"] == COUNTS)
        doc.update(complete=True, proved=True, actual_returncode=0, failure=None, stage="complete")
    except Exception as exc:
        doc["failure"] = {"type":type(exc).__name__, "message":str(exc)}
        doc["actual_returncode"] = 1
        doc["actual_mathematical_wall_seconds"] = time.monotonic()-started
        persist(args.out, doc)
        print_complete_document(doc)
        traceback.print_exc()
        raise
    raw = persist(args.out, doc)
    print_complete_document(doc)
    # This guard never overwrites or discards a preserved complete science.
    if len(raw) > COMPLETE_SCIENCE_MAX_BYTES:
        raise RuntimeError("complete science preserved before publication-size guard")


if __name__ == "__main__":
    main()

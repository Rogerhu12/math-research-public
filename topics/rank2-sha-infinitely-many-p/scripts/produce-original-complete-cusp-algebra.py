#!/usr/bin/env sage-python
"""Complete original 36-cusp algebra of X_0(867), without point omission.

All mathematics is executed only in this public repository's Actions.  The
complete S_4 is obtained from one persistent PARI rational cusp-form space,
saturated using all 409 faithful q coefficients, and extended to 817 on that
same basis.  S_8 is certified by actual S_4*M_4 products of full rank 696.
No coefficient or recomputable output file is written.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public repository Actions.")

import argparse
import hashlib
import importlib.util
import json
import time
from pathlib import Path
from sage.all import QQ, ZZ, GF, PowerSeriesRing, matrix, pari
from sage.env import SAGE_VERSION
from original_shadow_coordinate_tools import complete_product_recipes
from section_quotient_algebra import build_quotient, build_algebra
from finite_section_frobenius import inspect_frobenius, label_closed_components
import original_shadow_coordinate_tools
import section_quotient_algebra
import finite_section_frobenius

STARTED = time.monotonic()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def matrix_digest(M):
    return digest([[str(x) for x in row] for row in M.rows()])


def progress(stage, **kw):
    print("RANK2_CUSP_ALGEBRA_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)


def import_r917():
    path = Path(__file__).with_name("produce-r917-original-global-rr-q-lattice.py")
    spec = importlib.util.spec_from_file_location("rank2_original_r917_for_cusps", str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PariOriginalS4Basis:
    """One complete rational S_4(867) basis, never just newforms/eigenforms."""
    def __init__(self):
        self.seed = 20261120
        self.precision = 0
        self.columns = None
        progress("initialize complete exact rational PARI S4(867)")
        pari.allocatemem(268435456, 4294967296)
        pari.setrand(self.seed)
        self.mf = pari.mfinit([867, 4, 1], 1)
        parameters = list(pari.mfparams(self.mf))
        assert [int(t) for t in parameters[:4]] == [867, 4, 1, 1]
        assert int(pari.mfspace(self.mf)) == 1
        assert int(pari.mfdim(self.mf)) == 288
        self.basis = list(pari.mfbasis(self.mf))
        assert len(self.basis) == 288
        self.provenance = {
            "engine": "PARI mfinit([867,4,1],1), complete cuspidal space",
            "pari_version": str(pari.version()),
            "space": [867, 4, 1, 1],
            "dimension": 288,
            "coefficient_field": "QQ",
            "seed_immediately_before_mfinit": self.seed,
            "coefficient_method": "mfcoefs on the same complete space",
            "reference": "https://pari.math.u-bordeaux.fr/dochtml/html-stable/Modular_forms.html",
        }
        progress("complete rational S4 basis initialized", **self.provenance)

    def ensure_precision(self, precision):
        precision = int(precision)
        assert precision >= 1
        if precision <= self.precision:
            return
        progress("extend same exact rational S4 basis", precision=precision,
                 previous_precision=self.precision)
        coefficients = pari.mfcoefs(self.mf, precision-1)
        assert tuple(int(t) for t in coefficients.matsize()) == (precision, 288)
        # Exact QQ conversion rejects non-rational coefficient fields.
        columns = [[QQ(coefficients[i, j]) for i in range(precision)]
                   for j in range(288)]
        if self.columns is not None:
            assert all(columns[j][:self.precision] == self.columns[j]
                       for j in range(288))
        assert all(row[0] == 0 for row in columns)
        self.columns = columns
        self.precision = precision
        progress("same rational S4 expansion ready", precision=precision)


def series_rows(series, k, precision):
    return matrix(k, [[s[j] for j in range(precision)] for s in series])


def certified_s8_product_basis(s4, m4, k, precision):
    """Select true S_4*M_4 products and certify the complete S_8 dimension.

    Every considered column is a known global cusp form.  Reaching the full
    dimension 696 on 817 faithful jets proves equality with S_8; no inference
    from a shorter guessed prefix or from randomly selected cusp values occurs.
    """
    assert precision >= 817
    assert s4.nrows() == 288 and m4.nrows() == 324
    assert s4.ncols() == precision and m4.ncols() == precision
    ring = PowerSeriesRing(k, "Q_cusp_products", default_prec=precision)
    s4_series = [ring(list(r)).add_bigoh(precision) for r in s4.rows()]
    m4_series = [ring(list(r)).add_bigoh(precision) for r in m4.rows()]
    selected_recipes, selected_rows = [], []
    batches = []
    for i, cusp in enumerate(s4_series):
        new_rows = []
        new_recipes = []
        for j, form in enumerate(m4_series):
            product = (cusp*form).add_bigoh(817)
            new_rows.append([product[t] for t in range(817)])
            new_recipes.append((i, j))
        all_rows = selected_rows + new_rows
        all_recipes = selected_recipes + new_recipes
        independent = tuple(matrix(k, all_rows).transpose().pivots())
        selected_rows = [all_rows[j] for j in independent]
        selected_recipes = [all_recipes[j] for j in independent]
        rank = len(selected_recipes)
        assert rank <= 696
        batches.append({"s4_basis_row": i, "actual_product_rank": rank})
        progress("complete actual S4 times M4 product rank", batches=i+1,
                 actual_rank=rank, required_full_dimension=696)
        if rank == 696:
            break
    assert len(selected_recipes) == 696, "Actual S4*M4 products did not certify all S8."
    full_rows = []
    for i, j in selected_recipes:
        product = (s4_series[i]*m4_series[j]).add_bigoh(precision)
        full_rows.append([product[t] for t in range(precision)])
    s8 = matrix(k, full_rows)
    assert s8[:, :817] == matrix(k, selected_rows)
    assert s8[:, :817].rank() == 696
    assert all(s8[i, 0] == 0 for i in range(s8.nrows()))
    return s8, {
        "product": "actual complete S4 times complete M4",
        "expected_dimension": 696,
        "actual_full_rank": 696,
        "faithful_jet_coefficients": 817,
        "rank_batches": batches,
        "same_product_recipes_sha256": digest(selected_recipes),
        "complete_s8_jets_sha256": matrix_digest(s8),
    }


def build_original_cusp_algebra(prime=29, q_precision=817, decompose=True):
    prime, q_precision = int(prime), int(q_precision)
    assert prime in (29, 41) and q_precision >= 817
    r917 = import_r917()
    global_context, global_receipt = r917.build_original_global_rr_q_lattice(prime, q_precision)
    k = global_context["constants"]
    assert k == GF(prime)
    m2 = global_context["global_modular_form_jets"]
    assert m2.nrows() == 120 and m2.ncols() == q_precision
    # Use global modular forms themselves; the R917 RR rows divided by S are
    # deliberately not substituted for these two homogeneous section spaces.
    recipes, modular_series = complete_product_recipes(
        {"constants": k}, [list(row) for row in m2.rows()], 4, q_precision)
    m4 = series_rows(modular_series[2], k, q_precision)
    m8 = series_rows(modular_series[4], k, q_precision)
    assert m4.nrows() == 324 and m4[:, :409].rank() == 324
    assert m8.nrows() == 732 and m8[:, :817].rank() == 732

    cusp_owner = PariOriginalS4Basis()
    cusp_owner.ensure_precision(409)
    original_s4_409 = matrix(QQ, cusp_owner.columns)
    saturated, transform, reduced_s4_409, saturation = r917.saturate_original_rows(
        original_s4_409, prime)
    cusp_owner.ensure_precision(q_precision)
    original_s4_full = matrix(QQ, cusp_owner.columns)
    assert original_s4_full[:, :409] == original_s4_409
    saturated_full = transform*original_s4_full
    assert saturated_full[:, :409] == saturated
    r917.assert_integral_at(saturated_full, ZZ(prime))
    s4 = r917.reduce_at(saturated_full, k)
    assert s4[:, :409] == reduced_s4_409
    assert s4[:, :409].rank() == 288
    s8, s8_receipt = certified_s8_product_basis(s4, m4, k, q_precision)

    source = build_quotient(m4, s4, 409, "complete original M4/S4 at all 36 cusps", progress)
    target = build_quotient(m8, s8, 817, "complete original M8/S8 at all 36 cusps", progress)
    assert source["quotient_dimension"] == target["quotient_dimension"] == 36
    S = global_context["original_denominator_q_series"]
    h = (S*S).add_bigoh(q_precision)
    h_row = matrix(k, [[h[i] for i in range(q_precision)]]).row(0)
    algebra, algebra_receipt = build_algebra(source, target, h_row, progress)
    assert algebra["dimension"] == 36
    frobenius, frobenius_receipt = inspect_frobenius(
        algebra, expected="cusps", progress=progress, decompose=decompose)

    # h=S^2 trivializes L^2 on all cusps.  The SAME original f_i in M2 have
    # affine values f_i/S = (f_i*S)/h, retaining all 120 global coordinates.
    coordinate_jets = series_rows(
        [(form*S).add_bigoh(q_precision) for form in modular_series[1]],
        k, q_precision)
    original_coordinate_values = source["project"](coordinate_jets)
    assert original_coordinate_values.nrows() == 120
    assert original_coordinate_values.ncols() == 36
    point_labels, point_labels_receipt = None, None
    if decompose:
        component_values = [
            original_coordinate_values*component["projector_matrix"]
            for component in frobenius["decomposition"]["components"]]
        basis_id = section_quotient_algebra.matrix_digest(m2[:, :205])
        point_labels, point_labels_receipt = label_closed_components(
            algebra, frobenius, component_values, basis_id, progress)

    context = {
        "kind": "rank2_original_complete_cusp_algebra_context",
        "prime": prime,
        "constants": k,
        "all_geometric_cusps": 36,
        "global_modular_context": global_context,
        "complete_modular_product_recipes": recipes,
        "complete_modular_series": modular_series,
        "cusp_rational_owner": cusp_owner,
        "cusp_rational_basis_transform": transform,
        "complete_s4_jets": s4,
        "complete_s8_jets": s8,
        "source_quotient": source,
        "target_quotient": target,
        "algebra": algebra,
        "frobenius": frobenius,
        "original_M2_affine_coordinate_values": original_coordinate_values,
        "original_global_point_labels": point_labels,
        "q_precision": q_precision,
    }
    dependencies = {
        Path(module.__file__).name: hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
        for module in (r917, original_shadow_coordinate_tools,
                       section_quotient_algebra, finite_section_frobenius)
    }
    receipt = {
        "kind": "rank2_original_complete_cusp_algebra",
        "status": "certified_complete_original_36_cusp_algebra",
        "level": 867, "genus": 85, "prime": prime,
        "all_geometric_cusps": 36,
        "q_precision": q_precision,
        "original_denominator": "S=(3*E2(Q^3)-E2(Q))/2; S*dQ/Q=-dT/T",
        "normalizing_section": "the same h=S^2, verified invertible on the entire quotient",
        "all_modular_space_dimensions": {"M2":120, "M4":324, "M6":528, "M8":732},
        "all_cusp_space_dimensions": {"S4":288, "S8":696},
        "full_m4_jets_sha256": matrix_digest(m4),
        "full_m8_jets_sha256": matrix_digest(m8),
        "full_s4_jets_sha256": matrix_digest(s4),
        "complete_modular_product_recipes_sha256": digest(recipes),
        "r917_input": global_receipt,
        "rational_s4_source": cusp_owner.provenance,
        "s4_integral_saturation": saturation,
        "s8_complete_product_certificate": s8_receipt,
        "source_quotient": source["certificate"],
        "target_quotient": target["certificate"],
        "algebra": algebra_receipt,
        "frobenius": frobenius_receipt,
        "same_original_M2_affine_coordinates_sha256": matrix_digest(original_coordinate_values),
        "original_global_point_labels": point_labels_receipt,
        "source": os.environ.get("RANK2_SOURCE_SHA"),
        "run_id": os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt": os.environ.get("RANK2_RUN_ATTEMPT"),
        "sage_version": SAGE_VERSION,
        "image": os.environ.get("RANK2_IMAGE"),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256": dependencies,
        "readme_blobs": {
            "README.md": os.environ.get("RANK2_ROOT_README_SHA"),
            "topic": os.environ.get("RANK2_TOPIC_README_SHA")},
        "scope": ("Complete original cusp subscheme and its actual multiplication, Frobenius, "
                  "and closed-point degrees; no omitted cusp, reduced-support replacement, "
                  "map evaluation, or Selmer nonvanishing conclusion."),
        "elapsed_seconds": time.monotonic()-STARTED,
    }
    return context, receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=817)
    parser.add_argument("--no-decomposition", action="store_true")
    args = parser.parse_args()
    context, receipt = build_original_cusp_algebra(
        args.prime, args.q_precision, not args.no_decomposition)
    globals()["ORIGINAL_COMPLETE_CUSP_ALGEBRA_CONTEXT"] = context
    payload = canonical(receipt)
    print("RANK2_CUSP_ALGEBRA_RESULT " + payload, flush=True)
    print("RANK2_CUSP_ALGEBRA_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        progress("failed", exception_type=type(exc).__name__, message=str(exc))
        raise

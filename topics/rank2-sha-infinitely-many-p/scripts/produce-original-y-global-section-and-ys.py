#!/usr/bin/env sage-python
"""Complete original Y=X_0(3468) M2 lattice, three pullbacks, and original y_s.

All mathematics is confined to this public repository's Actions.  The complete
666-dimensional rational M2 space is saturated on all 1225 faithful jets and
extended on the same PARI basis.  The three global degeneracy maps retain their
logarithmic differential multipliers 1, 2, and 4.  The already identified y_s is
recovered on its original branch by the complete 0..1531 section kernel.
No large intersection divisor or Frobenius shadow is claimed.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public repository Actions.")

import argparse
import hashlib
import importlib.util
import time
from pathlib import Path
from sage.all import QQ, ZZ, GF, PowerSeriesRing, PolynomialRing, matrix, vector, identity_matrix, pari
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical, digest, matrix_digest
import section_quotient_algebra

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"


def progress(stage, **kw):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_Y_SECTION_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)


def import_file(filename, module_name):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class _OriginalYWeightTwoForm:
    def __init__(self, owner, index):
        self.owner, self.index = owner, int(index)

    def q_expansion(self, precision):
        precision = int(precision)
        self.owner.ensure_precision(precision)
        ring = PowerSeriesRing(QQ, "u", default_prec=precision)
        return ring(self.owner.columns[self.index][:precision]).add_bigoh(precision)


class PariOriginalYM2Basis:
    """One persistent complete QQ M2(3468) space, including all cusp forms."""
    def __init__(self):
        self.seed = 20261120
        self.precision = 0
        self.columns = None
        progress("initialize complete exact rational M2 of original Y", level=3468)
        pari.allocatemem(268435456, 4294967296)
        pari.setrand(self.seed)
        self.mf = pari.mfinit([3468, 2, 1], 4)
        parameters = list(pari.mfparams(self.mf))
        assert [int(t) for t in parameters[:4]] == [3468, 2, 1, 4]
        assert int(pari.mfspace(self.mf)) == 4
        assert int(pari.mfdim(self.mf)) == 666
        self.basis = list(pari.mfbasis(self.mf))
        assert len(self.basis) == 666
        self.forms = [_OriginalYWeightTwoForm(self, j) for j in range(666)]
        self.provenance = {
            "engine": "PARI full mfinit([3468,2,1],4), one fixed mfbasis",
            "pari_version": str(pari.version()),
            "seed_immediately_before_mfinit": self.seed,
            "space": [3468, 2, 1, 4],
            "dimension": 666,
            "coefficient_field": "QQ",
            "coefficient_method": "mfcoefs on the same complete space; exact whole-matrix rows",
            "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        }
        progress("complete rational Y M2 basis initialized", **self.provenance)

    def ensure_precision(self, precision):
        precision = int(precision)
        assert precision >= 1
        if precision <= self.precision:
            return
        progress("extend same complete original Y rational basis", precision=precision,
                 previous_precision=self.precision)
        coefficients = pari.mfcoefs(self.mf, precision-1)
        assert tuple(int(t) for t in coefficients.matsize()) == (precision, 666)
        # This exact conversion rejects any nonrational coefficient rather
        # than choosing an unrecorded field embedding.
        columns = [[QQ(coefficients[i, j]) for i in range(precision)]
                   for j in range(666)]
        if self.columns is not None:
            assert all(columns[j][:self.precision] == self.columns[j]
                       for j in range(666))
        self.columns, self.precision = columns, precision
        progress("same original Y rational expansion ready", precision=precision)


def complete_membership_reader(full_rows, faithful_length, label):
    """Exact coordinates with every retained nonpivot coefficient checked."""
    k = full_rows.base_ring()
    faithful_length = int(faithful_length)
    assert full_rows.ncols() >= faithful_length
    prefix = full_rows[:, :faithful_length]
    pivots = tuple(prefix.pivots())
    dimension = int(full_rows.nrows())
    assert len(pivots) == dimension
    inverse = prefix.matrix_from_columns(pivots).inverse()
    assert prefix.matrix_from_columns(pivots)*inverse == identity_matrix(k, dimension)
    nonpivots = tuple(i for i in range(full_rows.ncols()) if i not in set(pivots))
    reconstructed = inverse*full_rows.matrix_from_columns(nonpivots)

    def read(rows):
        assert rows.base_ring() == k and rows.ncols() == full_rows.ncols()
        entries = rows.matrix_from_columns(pivots)
        assert entries*reconstructed == rows.matrix_from_columns(nonpivots), (
            "Actual global section failed the complete retained membership test: " + label)
        return entries*inverse

    return read, {
        "label": label,
        "dimension": dimension,
        "faithful_jet_coefficients": faithful_length,
        "retained_jet_coefficients": int(full_rows.ncols()),
        "full_basis_rank": dimension,
        "fixed_pivot_columns_sha256": digest(list(pivots)),
        "pivot_inverse_sha256": matrix_digest(inverse),
        "all_retained_nonpivot_reconstruction_sha256": matrix_digest(reconstructed),
        "retained_nonpivot_count": len(nonpivots),
        "basis_rows_sha256": matrix_digest(full_rows),
    }


def pullback_weight_two_rows(rows, exponent, precision):
    """The original log-differential pullback j*f(u^j), in the SAME u."""
    exponent, precision = int(exponent), int(precision)
    assert exponent in (1, 2, 4)
    k = rows.base_ring()
    assert rows.ncols() >= (precision-1)//exponent+1
    return matrix(k, rows.nrows(), precision,
                  lambda i, n: (k(exponent)*rows[i, n//exponent]
                                if n % exponent == 0 else k.zero()))


def original_ys_branch(k, precision, eta_module):
    """Unique original z=u*y_s, z(0)=-1; integer eta input precedes reduction."""
    precision = int(precision)
    assert precision >= 1532
    ring = PowerSeriesRing(k, "u", default_prec=precision)
    u = ring.gen()
    eta_precision = (precision-1)//2+1
    integral_eta = eta_module.original_eta_unit(eta_precision)
    assert len(integral_eta) == eta_precision
    t = ring([k(integral_eta[i//2]) if i % 2 == 0 else k.zero()
              for i in range(precision)]).add_bigoh(precision)
    assert t[0] == 1
    z = ring(-1).add_bigoh(1)
    length = 1
    steps = []

    def equation(zz, tt, cap):
        return (zz**2*(zz**2-9*u**2)**2-tt*(zz**2-u**2)**2).add_bigoh(cap)

    while length < precision:
        next_length = min(2*length, precision)
        old = z
        zz = ring([z[i] for i in range(length)]).add_bigoh(next_length)
        tt = t.add_bigoh(next_length)
        residual = equation(zz, tt, next_length)
        derivative = (2*zz*(zz**2-9*u**2)**2
                      +4*zz**3*(zz**2-9*u**2)
                      -4*tt*zz*(zz**2-u**2)).add_bigoh(next_length)
        assert derivative[0] == k(-2) and derivative.valuation() == 0
        z = (zz-residual/derivative).add_bigoh(next_length)
        assert z[0] == -1 and (z-old).add_bigoh(length) == 0
        assert equation(z, tt, next_length) == 0
        steps.append({"old_precision": length, "new_precision": next_length})
        length = next_length
        progress("same original ys branch exact Hensel lift", precision=length,
                 branch_constant=-1, derivative_constant=int(k(-2)))
    assert z[0] == -1 and z[1] == 0
    assert all(z[i] == 0 for i in range(1, precision, 2))
    assert equation(z, t, precision) == 0
    receipt = {
        "original_global_function": "R882 y_s on the same Y=X0(3468)",
        "parameter": "u=q^3; central Q=u^2",
        "regular_variable": "z=u*y_s",
        "regular_equation": "z^2*(z^2-9*u^2)^2-t(u)*(z^2-u^2)^2=0",
        "t_series": "u^2*T3(u^2), from the exact original integer eta unit",
        "branch_constant": -1,
        "derivative_at_origin": -2,
        "full_regular_equation_checked_coefficients": precision,
        "all_previous_hensel_prefixes_preserved": True,
        "original_parity_verified": True,
        "integer_eta_unit_sha256": digest([str(c) for c in integral_eta]),
        "regular_t_jets_sha256": digest([int(t[i]) for i in range(precision)]),
        "original_z_jets_sha256": digest([int(z[i]) for i in range(precision)]),
        "hensel_steps": steps,
    }
    return ring, z, t, receipt


def recover_original_ys(rows, z, precision):
    """Full homogeneous section kernel; pole cap 1530 pays 0..1531."""
    k = rows.base_ring()
    assert rows.nrows() == 666 and rows.ncols() == precision
    length = 1532
    assert precision >= length
    ring = PolynomialRing(k, "u_polynomial")
    u = ring.gen()
    regular_z = ring([z[i] for i in range(length)])
    basis = [ring(list(row[:length])) for row in rows.rows()]
    equations = matrix(k, [
        [basis_i[n-1] if n else k.zero() for n in range(length)]
        for basis_i in basis] + [
        list((-(regular_z*basis_i).truncate(length)).padded_list(length))
        for basis_i in basis])
    assert equations.nrows() == 1332 and equations.ncols() == length
    progress("original ys full global section kernel start", unknowns=1332,
             complete_equations=length, complete_difference_pole_bound=1530)
    kernel = equations.left_kernel().basis_matrix()
    nullity = int(kernel.nrows())
    assert nullity >= 360
    assert nullity == 1332-int(equations.rank())
    assert kernel*equations == 0
    numerator_block = kernel[:, :666]
    denominator_block = kernel[:, 666:]
    # Both projections are injective on the entire kernel.  In particular no
    # fake vector with zero denominator can survive the full zero bound.
    assert numerator_block.rank() == denominator_block.rank() == nullity
    coefficients = kernel.row(0)
    first_denominator = next(j for j in range(666, 1332) if coefficients[j])
    coefficients = coefficients/coefficients[first_denominator]
    assert coefficients*equations == 0
    numerator_coordinates = vector(k, coefficients[:666])
    denominator_coordinates = vector(k, coefficients[666:])
    numerator_jets = numerator_coordinates*rows
    denominator_jets = denominator_coordinates*rows
    A, B = ring(list(numerator_jets)), ring(list(denominator_jets))
    assert A and B
    assert (u*A-regular_z*B).truncate(length) == 0
    assert int(B.valuation())-int(A.valuation()) == 1
    assert A[int(A.valuation())] == -B[int(B.valuation())]
    # The finite kernel identifies the already known global y_s by the full
    # degree-1530 bound.  The displayed regular branch equation is not itself
    # used as an existence claim for some new modular function.
    receipt = {
        "original_function": "the same R882 y_s on X0(3468)",
        "original_function_complete_pole_degree": 306,
        "same_numerator_denominator_space": "complete M2(3468), equivalently both divided by S_Y",
        "section_bundle_degree": 1224,
        "complete_difference_pole_bound": 1530,
        "shift_for_original_pole_at_infinity": 1,
        "checked_shifted_coefficients_inclusive": [0, 1531],
        "unknowns": 1332,
        "actual_equation_rank": 1332-nullity,
        "actual_full_kernel_dimension": nullity,
        "riemann_roch_kernel_dimension_lower_bound": 360,
        "entire_kernel_residual_verified": True,
        "both_full_kernel_coordinate_projections_injective": True,
        "same_original_branch_leading_coefficient": -1,
        "actual_numerator_infinity_order": int(A.valuation()),
        "actual_denominator_infinity_order": int(B.valuation()),
        "chosen_denominator_nonzero_global_section": True,
        "exact_original_global_identity_certified_by_full_pole_bound": True,
        "full_equation_matrix_sha256": matrix_digest(equations),
        "complete_kernel_sha256": matrix_digest(kernel),
        "complete_denominator_projection_sha256": matrix_digest(denominator_block),
        "chosen_coordinates_sha256": digest([int(c) for c in coefficients]),
        "actual_numerator_jets_sha256": digest([int(c) for c in numerator_jets]),
        "actual_denominator_jets_sha256": digest([int(c) for c in denominator_jets]),
    }
    progress("same original ys globally identified", kernel_dimension=nullity,
             numerator_order=int(A.valuation()), denominator_order=int(B.valuation()),
             complete_last_coefficient=1531)
    return {
        "numerator_coordinates": numerator_coordinates,
        "denominator_coordinates": denominator_coordinates,
        "numerator_jets": numerator_jets,
        "denominator_jets": denominator_jets,
        "full_kernel_coordinates": kernel,
        "certificate": receipt,
    }, receipt


def build_original_y_global_section_and_ys(prime=29, q_precision=1532):
    prime, q_precision = int(prime), int(q_precision)
    assert prime in (29, 41) and q_precision >= 1532
    r917 = import_file("produce-r917-original-global-rr-q-lattice.py", "original_y_r917_saturation")
    eta = import_file("produce-original-tuv-section-fractions.py", "original_y_exact_eta_source")
    k = GF(prime)
    owner = PariOriginalYM2Basis()
    owner.ensure_precision(1225)
    original_1225 = matrix(QQ, owner.columns)
    assert original_1225.nrows() == 666 and original_1225.ncols() == 1225
    progress("saturate complete original Y M2 on all faithful jets", prime=prime,
             complete_dimension=666, faithful_coefficients=1225)
    saturated, transform, reduced_1225, saturation = r917.saturate_original_rows(original_1225, prime)
    owner.ensure_precision(q_precision)
    original_full = matrix(QQ, owner.columns)
    assert original_full[:, :1225] == original_1225
    saturated_full = transform*original_full
    assert saturated_full[:, :1225] == saturated
    r917.assert_integral_at(saturated_full, ZZ(prime))
    rows = r917.reduce_at(saturated_full, k)
    assert rows[:, :1225] == reduced_1225 and rows[:, :1225].rank() == 666
    read_y, y_membership = complete_membership_reader(rows, 1225, "complete original Y M2")

    base, base_receipt = r917.build_original_global_rr_q_lattice(prime, q_precision)
    base_rows = base["global_modular_form_jets"]
    assert base_rows.nrows() == 120 and base_rows.ncols() == q_precision
    S = base["original_denominator_q_series"]
    S_row = matrix(k, [[S[i] for i in range(q_precision)]])
    read_base, base_membership = complete_membership_reader(base_rows, 205, "same original B M2")
    S_coordinates = read_base(S_row).row(0)
    pulls, pull_receipts, rho_series = {}, [], {}
    ring = PowerSeriesRing(k, "u", default_prec=q_precision)
    SY_row = pullback_weight_two_rows(S_row, 2, q_precision).row(0)
    SY = ring(list(SY_row)).add_bigoh(q_precision)
    assert SY[0] == k(2)
    SY_inverse = 1/SY
    rr_data = []
    for row in rows.rows():
        rr = (ring(list(row)).add_bigoh(q_precision)*SY_inverse).add_bigoh(q_precision)
        rr_data.append([rr[j] for j in range(q_precision)])
    rr_rows = matrix(k, rr_data)
    del rr_data
    assert rr_rows[:, :1225].rank() == 666
    for exponent, name in ((1, "pi1=q0"), (2, "pi2=q1"), (4, "pi4=q2")):
        pulled_rows = pullback_weight_two_rows(base_rows, exponent, q_precision)
        pulled_S = pullback_weight_two_rows(S_row, exponent, q_precision)
        assert S_coordinates*pulled_rows == pulled_S.row(0)
        coordinates = read_y(pulled_rows)
        S_y_coordinates = read_y(pulled_S).row(0)
        assert coordinates.rank() == 120
        assert S_coordinates*coordinates == S_y_coordinates
        rho = (ring(list(pulled_S.row(0))).add_bigoh(q_precision)*SY_inverse).add_bigoh(q_precision)
        if exponent == 2:
            assert rho == ring.one().add_bigoh(q_precision)
        rho_series[exponent] = rho
        pulls[exponent] = {
            "original_map": name,
            "differential_multiplier": exponent,
            "full_M2_pullback_jets": pulled_rows,
            "full_M2_pullback_coordinates": coordinates,
            "pulled_S_jets": pulled_S.row(0),
            "pulled_S_coordinates": S_y_coordinates,
            "rho_series": rho,
            "rr_pullback_formula": "pi_j^*(f_i/S)=(j*f_i(u^j)/S_Y)/rho_j",
        }
        pull_receipts.append({
            "original_map": name,
            "original_morphism_degree": 6,
            "base_parameter_substitution": "Q=u^%d" % exponent,
            "logarithmic_differential_multiplier": exponent,
            "all_original_basis_rows": 120,
            "actual_pullback_rank": 120,
            "faithful_Y_membership_coefficients": 1225,
            "all_retained_membership_coefficients": q_precision,
            "complete_coordinate_matrix_sha256": matrix_digest(coordinates),
            "complete_pullback_jets_sha256": matrix_digest(pulled_rows),
            "same_S_coordinate_return_verified": True,
            "pulled_S_coordinates_sha256": digest([int(c) for c in S_y_coordinates]),
            "rho_j_jets_sha256": digest([int(rho[j]) for j in range(q_precision)]),
            "rho_2_is_one": exponent == 2,
            "all_other_rho_factors_retained": True,
        })
        progress("original degeneracy complete membership certified", original_map=name,
                 differential_multiplier=exponent, full_rank=120,
                 all_retained_coefficients=q_precision)

    _, z, t, branch_receipt = original_ys_branch(k, q_precision, eta)
    ys, ys_receipt = recover_original_ys(rows, z, q_precision)
    context = {
        "kind": "rank2_original_Y_complete_global_M2_and_ys_context",
        "constants": k, "prime": prime, "level": 3468,
        "genus": 559, "all_geometric_cusps": 108,
        "line_bundle_degree": 1224, "q_parameter": "u=q^3",
        "rational_source_owner": owner,
        "rational_source_forms": owner.forms,
        "rational_basis_transform": transform,
        "global_modular_form_jets": rows,
        "original_SY_series": SY,
        "original_rr_jets": rr_rows,
        "original_base_context": base,
        "original_base_S_coordinates": S_coordinates,
        "degeneracy_maps": pulls,
        "original_z_series": z,
        "original_regular_central_T_series": t,
        "original_ys_fraction": ys,
        "q_precision": q_precision,
        "complete_membership_reader": read_y,
    }
    dependencies = [Path(r917.__file__), Path(eta.__file__),
                    HERE / "original_pari_m2_basis.py",
                    HERE / "original_shadow_coordinate_tools.py",
                    Path(section_quotient_algebra.__file__)]
    receipt = {
        "kind": "rank2_original_Y_global_section_and_ys_certificate",
        "status": "complete_original_Y_M2_three_degeneracies_and_ys_identified",
        "prime": prime, "level": 3468,
        "original_base_level": 867,
        "genus": 559, "all_geometric_cusps": 108,
        "modular_index": 7344, "line_bundle_degree": 1224,
        "complete_M2_dimension": 666,
        "faithful_M2_jet_coefficients": 1225,
        "retained_q_precision": q_precision,
        "original_parameter": "u=q^3; Q at the central pi2 is u^2",
        "original_denominator": "S_Y=2*S(u^2), with S=(3E2(Q^3)-E2(Q))/2",
        "original_SY_constant": 2,
        "original_divisor_degree": 1224,
        "rational_source_provenance": owner.provenance,
        "complete_integral_saturation": saturation,
        "complete_Y_membership_reader": y_membership,
        "same_base_membership_reader": base_membership,
        "same_original_base_M2_receipt": base_receipt,
        "complete_original_Y_M2_jets_sha256": matrix_digest(rows),
        "complete_original_Y_RR_jets_sha256": matrix_digest(rr_rows),
        "original_SY_jets_sha256": digest([int(SY[j]) for j in range(q_precision)]),
        "complete_original_degeneracy_maps": pull_receipts,
        "original_ys_branch": branch_receipt,
        "original_ys_global_fraction": ys_receipt,
        "higher_weight_complete_Y_spaces_claimed": False,
        "large_intersection_divisors_claimed": False,
        "original_shadow_computed": False,
        "full_Y_Atkin_Lehner_matrix_claimed": False,
        "source": os.environ.get("RANK2_SOURCE_SHA"),
        "run_id": os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt": os.environ.get("RANK2_RUN_ATTEMPT"),
        "sage_version": SAGE_VERSION,
        "image": os.environ.get("RANK2_IMAGE"),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256": {path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in dependencies},
        "readme_blobs": {"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
                         "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "scope": ("The complete original Y global M2 lattice, all three original logarithmic "
                  "degeneracy pullbacks, their actual rho factors, and the specified global ys "
                  "fraction.  No higher Y section space, complete intersection divisor, or "
                  "Frobenius shadow is inferred."),
        "elapsed_seconds": time.monotonic()-STARTED,
    }
    return context, receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=1532)
    args = parser.parse_args()
    context, receipt = build_original_y_global_section_and_ys(args.prime, args.q_precision)
    globals()["ORIGINAL_Y_GLOBAL_SECTION_AND_YS_CONTEXT"] = context
    payload = canonical(receipt)
    print("RANK2_Y_SECTION_RESULT " + payload, flush=True)
    print("RANK2_Y_SECTION_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise

#!/usr/bin/env sage-python
"""R926: original RF/Ri fractions and their complete global cube identities.

Only the SAME authenticated original M2 owner and saturation transform are
extended.  Full low kernels identify the already existing original roots;
the complete 6941/4287 coefficient identities are separate acceptance gates.
The exact original omega is used for all quadratic-field arithmetic.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public research Actions.")
if any(os.environ.get(key) for key in ("GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN")):
    raise SystemExit("Keep all repository tokens outside the Sage process.")

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from copy import copy
from pathlib import Path
from sage.all import QQ, ZZ, PolynomialRing, PowerSeriesRing, matrix, vector
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical, digest, matrix_digest
from original_shadow_coordinate_tools import certificate_weight
from original_shadow_receipt_tools import add_pinned_arguments, pinned_request, validate_envelope
import section_quotient_algebra

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"
LOW_INPUT = 2725
RF_LENGTH = 2313
RP_LENGTH = 1429
RF_IDENTITY_LENGTH = 6941
RP_IDENTITY_LENGTH = 4287


def progress(stage, **record):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_CUBE_SECTIONS_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **record)), flush=True)


def import_file(filename, name):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OriginalOmegaCoordinates:
    """Exact 1,omega coordinates in the caller's EXISTING quadratic field."""
    def __init__(self, fp, field, omega):
        self.fp, self.field, self.omega = fp, field, omega
        self.prime = int(fp.characteristic())
        assert int(fp.degree()) == 1 and int(field.degree()) == 2
        assert int(field.characteristic()) == self.prime
        assert omega.parent() is field and omega != 1 and omega**2+omega+1 == 0
        def native(value):
            coefficients = list(field(value).polynomial().list())
            assert len(coefficients) <= 2
            return vector(fp, coefficients+[fp.zero()]*(2-len(coefficients)))
        self.native = native
        self.basis = matrix(fp, [native(field.one()), native(omega)])
        assert self.basis.rank() == 2
        self.inverse = self.basis.inverse()
        assert native(field.one())*self.inverse == vector(fp, [1, 0])
        assert native(omega)*self.inverse == vector(fp, [0, 1])

    def split(self, value):
        value = self.field(value)
        answer = self.native(value)*self.inverse
        assert self.field(answer[0])+self.field(answer[1])*self.omega == value
        return self.fp(answer[0]), self.fp(answer[1])

    def prime_scalar(self, value):
        a, b = self.split(value)
        assert not b
        return a

    def coefficients(self, values):
        return [self.split(c) for c in values]

    def matrix_components(self, rows):
        first, second = [], []
        for row in rows.rows():
            pairs = self.coefficients(row)
            first.append([a for a, b in pairs])
            second.append([b for a, b in pairs])
        return matrix(self.fp, first), matrix(self.fp, second)

    def receipt(self):
        return {
            "exact_original_field_used":True,
            "original_omega_native_coordinates":[int(c) for c in self.native(self.omega)],
            "actual_one_omega_change_sha256":matrix_digest(self.basis),
            "actual_one_omega_inverse_sha256":matrix_digest(self.inverse),
            "every_converted_coefficient_returned_in_original_field":True,
            "quadratic_relation":"omega^2+omega+1=0",
        }


class PairPolynomials:
    """k[Q]/Q^N as two Fp polynomials in the actual basis 1,omega."""
    def __init__(self, codec, precision):
        self.codec, self.precision = codec, int(precision)
        self.fp, self.field = codec.fp, codec.field
        self.ring = PolynomialRing(self.fp, "Q_original_cube")
        self.Q = self.ring.gen()
        self.zero = (self.ring.zero(), self.ring.zero())
        self.one = (self.ring.one(), self.ring.zero())

    def truncate(self, value, precision=None):
        length = self.precision if precision is None else int(precision)
        assert 0 <= length <= self.precision
        return tuple(self.ring(p).truncate(length) for p in value)

    def scalar(self, value):
        a, b = self.codec.split(value)
        return self.ring(a), self.ring(b)

    def add(self, x, y):
        return self.truncate((x[0]+y[0], x[1]+y[1]))

    def sub(self, x, y):
        return self.truncate((x[0]-y[0], x[1]-y[1]))

    def mul(self, x, y):
        ac, bd = x[0]*y[0], x[1]*y[1]
        return self.truncate((ac-bd, x[0]*y[1]+x[1]*y[0]-bd))

    def power(self, value, exponent):
        exponent = int(exponent)
        assert exponent >= 0
        answer = self.one
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, value)
            exponent >>= 1
            if exponent:
                value = self.mul(value, value)
        return answer

    def shift(self, value, exponent):
        assert int(exponent) >= 0
        return self.truncate((self.Q**int(exponent)*value[0], self.Q**int(exponent)*value[1]))

    def from_series(self, value):
        assert value.valuation() >= 0 and value.precision_absolute() >= self.precision
        pairs = [self.codec.split(value[i]) for i in range(self.precision)]
        return (self.ring([a for a, b in pairs]), self.ring([b for a, b in pairs]))

    def to_series(self, value, field=None):
        field = self.field if field is None else field
        ring = PowerSeriesRing(field, "Q", default_prec=self.precision)
        if field is self.fp:
            assert not value[1]
            coefficients = [self.fp(value[0][i]) for i in range(self.precision)]
        else:
            assert field is self.field
            coefficients = [field(value[0][i])+field(value[1][i])*self.codec.omega
                            for i in range(self.precision)]
        return ring(coefficients).add_bigoh(self.precision)

    def constant_frobenius(self, value):
        c, d = self.codec.split(self.codec.omega**self.codec.prime)
        return self.truncate((value[0]+c*value[1], d*value[1]))

    def hash(self, value, precision=None):
        length = self.precision if precision is None else int(precision)
        assert length <= self.precision
        return matrix_digest(matrix(self.fp, [[value[s][i] for i in range(length)]
                                             for s in (0, 1)]))


class OriginalSectionEvaluator:
    """Only selected homogeneous sections are evaluated, by true recipe prefixes."""
    def __init__(self, rows, codec, precision):
        self.rows, self.codec, self.precision = rows, codec, int(precision)
        assert rows.nrows() == 120 and rows.ncols() >= self.precision
        self.arithmetic = PairPolynomials(codec, self.precision)
        self.ring = self.arithmetic.ring
        self.forms = tuple(self.ring(list(row[:self.precision])) for row in rows.rows())
        self.cache = {():self.ring.one()}
        self.cache.update({(i,):self.forms[i] for i in range(120)})

    def product(self, recipe):
        recipe = tuple(int(i) for i in recipe)
        assert all(0 <= i < 120 for i in recipe)
        if recipe not in self.cache:
            self.cache[recipe] = (self.product(recipe[:-1])*self.forms[recipe[-1]]).truncate(self.precision)
        return self.cache[recipe]

    def section(self, recipes, coefficients, power):
        recipes = tuple(tuple(int(i) for i in recipe) for recipe in recipes)
        assert len(recipes) == len(coefficients)
        assert all(len(recipe) == int(power) for recipe in recipes)
        groups = {}
        for recipe, coefficient in zip(recipes, coefficients):
            if not coefficient:
                continue
            assert recipe
            a, b = self.codec.split(coefficient)
            old = groups.get(recipe[:-1], self.arithmetic.zero)
            groups[recipe[:-1]] = (old[0]+a*self.forms[recipe[-1]],
                                  old[1]+b*self.forms[recipe[-1]])
        result = self.arithmetic.zero
        for prefix, linear in groups.items():
            product = self.product(prefix)
            result = self.arithmetic.add(result, (
                (product*linear[0]).truncate(self.precision),
                (product*linear[1]).truncate(self.precision)))
        return result

    def complete_basis(self, recipes, length):
        length = int(length)
        assert length <= self.precision
        return matrix(self.codec.fp, [[self.product(recipe)[i] for i in range(length)]
                                      for recipe in recipes])


def extend_same_rows(base, previous, precision, r917, fixed_transform):
    precision = int(precision)
    assert precision > previous.ncols()
    assert base["rational_basis_transform"] == fixed_transform
    owner = base["rational_source_owner"]
    old_rational = [list(row[:previous.ncols()]) for row in owner.columns]
    owner.ensure_precision(precision)
    assert all(owner.columns[i][:previous.ncols()] == old_rational[i] for i in range(120))
    rational = matrix(QQ, owner.columns)
    assert rational.nrows() == 120 and rational.ncols() == precision
    saturated = fixed_transform*rational
    r917.assert_integral_at(saturated, ZZ(base["prime"]))
    reduced = r917.reduce_at(saturated, base["constants"])
    assert reduced[:, :previous.ncols()] == previous
    assert reduced[:, :205].rank() == 120
    record = {
        "previous_precision":int(previous.ncols()), "new_precision":precision,
        "same_original_PARI_owner_and_basis":True,
        "same_exact_rational_saturation_transform":True,
        "all_previous_rational_coefficients_preserved":True,
        "all_previous_reduced_coefficients_preserved":True,
        "all_new_coefficients_integral_at_original_prime":True,
        "actual_original_basis_prefix_sha256":matrix_digest(reduced[:, :205]),
        "complete_extended_original_M2_sha256":matrix_digest(reduced),
        "fixed_rational_transform_sha256":digest([[str(c) for c in row] for row in fixed_transform.rows()]),
    }
    progress("same original full M2 lattice extended", **record)
    return reduced, record


def append_complete_R6(rows, old_recipes, codec):
    recipes = {int(m):[tuple(int(i) for i in recipe) for recipe in value]
               for m, value in old_recipes.items()}
    assert all(m in recipes for m in range(1, 6))
    assert recipes[1] == [(i,) for i in range(120)]
    for m in range(1, 6):
        assert len(recipes[m]) == 204*m-84
        assert all(len(recipe) == m for recipe in recipes[m])
    original_hash = digest({str(m):recipes[m] for m in range(1, 6)})
    evaluator = OriginalSectionEvaluator(rows, codec, 1225)
    selected, selected_rows, seen = [], [], set()
    for index in range(120):
        additions, jets = [], []
        for recipe in recipes[5]:
            candidate = tuple(sorted((index,)+recipe))
            if candidate in seen:
                continue
            seen.add(candidate)
            actual = evaluator.product(candidate)
            additions.append(candidate)
            jets.append([actual[i] for i in range(1225)])
        if not jets:
            continue
        all_recipes, all_rows = selected+additions, selected_rows+jets
        pivots = tuple(matrix(codec.fp, all_rows).transpose().pivots())
        selected, selected_rows = [all_recipes[i] for i in pivots], [all_rows[i] for i in pivots]
        progress("complete original R6 actual product rank", batch=index+1,
                 actual_rank=len(selected), expected=1140, full_coefficients=1225)
        if len(selected) == 1140:
            break
    assert len(selected) == 1140
    full = matrix(codec.fp, selected_rows)
    assert full.rank() == 1140 and full.ncols() == 1225
    recipes[6] = selected
    assert digest({str(m):recipes[m] for m in range(1, 6)}) == original_hash
    return recipes, {
        "previous_powers_1_through_5_recipes_unchanged":True,
        "previous_recipes_sha256":original_hash,
        "new_section_power":6, "actual_complete_dimension":1140,
        "complete_Sturm_coefficients":1225,
        "new_recipes_sha256":digest(selected),
        "complete_R6_Sturm_basis_sha256":matrix_digest(full),
        "same_genuine_original_M2_products":True,
    }


def original_tau(field, length, local_module):
    ring = PowerSeriesRing(field, "Q", default_prec=int(length))
    Q = ring.gen()
    euler = local_module.euler_series(ring, int(length))
    assert euler.precision_absolute() >= length and euler[0] == 1
    euler3 = ring([euler[i//3] if i % 3 == 0 else field.zero()
                  for i in range(length)]).add_bigoh(length)
    tau = ((euler/euler3)**12).add_bigoh(length)
    zeta = (tau+27*Q).add_bigoh(length)
    assert tau.precision_absolute() >= length and zeta.precision_absolute() >= length
    assert tau[0] == zeta[0] == 1
    return ring, tau, zeta


def original_cube_root(H, length, label):
    length = int(length)
    assert H.precision_absolute() >= length and H[0] == 1
    ring = H.parent()
    root = ring.one().add_bigoh(1)
    old_length, steps = 1, []
    while old_length < length:
        next_length = min(2*old_length, length)
        # Zero extension is ONLY a chosen Newton approximation.  H remains
        # the certified original input with its actual known precision.
        approximation = ring([root[i] for i in range(old_length)]).add_bigoh(next_length)
        target = H.add_bigoh(next_length)
        updated = ((2*approximation+target/approximation**2)/3).add_bigoh(next_length)
        assert updated.precision_absolute() >= next_length and updated[0] == 1
        assert (updated-root).add_bigoh(old_length) == 0
        assert (updated**3-target).add_bigoh(next_length) == 0
        root = updated
        steps.append({"old_precision":old_length,"new_precision":next_length})
        old_length = next_length
        progress("same original cube branch Newton identity", original_root=label,
                 all_checked_coefficients=next_length, original_leading_value=1)
    assert root.precision_absolute() >= length
    assert (root**3-H).add_bigoh(length) == 0
    return root, {"original_root":label,"complete_unit_coefficients":length,
                  "original_leading_value":1,"all_Newton_prefixes_preserved":True,
                  "every_step_entire_residual_verified":True,"Newton_steps":steps}


def fraction_kernel(basis, root, minimum, codec, label, supplied_kernel=None):
    """The full original low-window kernel, with exact Fp restriction of scalars."""
    fp, field = codec.fp, root.base_ring()
    dimension, length = int(basis.nrows()), int(basis.ncols())
    assert basis.base_ring() is fp and root.precision_absolute() >= length
    assert basis.rank() == dimension and root[0] == 1
    polynomials = PolynomialRing(fp, "Q_original_kernel")
    split_root = [codec.split(root[i]) for i in range(length)]
    R0 = polynomials([a for a, b in split_root])
    R1 = polynomials([b for a, b in split_root])
    products0, products1 = [], []
    for row in basis.rows():
        f = polynomials(list(row))
        p0, p1 = (R0*f).truncate(length), (R1*f).truncate(length)
        products0.append([-p0[i] for i in range(length)])
        products1.append([-p1[i] for i in range(length)])
    M0 = basis.stack(matrix(fp, products0))
    M1 = matrix(fp, dimension, length).stack(matrix(fp, products1))
    progress("complete original cube fraction kernel start", original_root=label,
             unknowns=2*dimension, full_coefficients=length,
             constant_degree=int(field.degree()))
    if supplied_kernel is None and field is fp:
        assert M1.is_zero()
        kernel = M0.left_kernel().basis_matrix()
        restriction_record = {"restriction_of_scalars_used":False,
                              "complete_equation_rank":int(M0.rank())}
        assert kernel.nrows() == 2*dimension-int(M0.rank())
    elif supplied_kernel is None:
        assert field is codec.field
        # (u+v*omega)(M0+M1*omega) has components
        # u*M0-v*M1, u*M1+v*M0-v*M1, in the SAME original 1,omega basis.
        block = M0.augment(M1).stack((-M1).augment(M0-M1))
        kernel_fp = block.left_kernel().basis_matrix()
        assert (kernel_fp*block).is_zero()
        block_rank = int(block.rank())
        assert kernel_fp.nrows() == 4*dimension-block_rank
        assert kernel_fp.nrows() % 2 == 0
        lifted = matrix(field, [[field(row[i])+field(row[2*dimension+i])*codec.omega
                                 for i in range(2*dimension)] for row in kernel_fp.rows()])
        kernel = lifted.row_space().basis_matrix()
        assert 2*kernel.nrows() == kernel_fp.nrows()
        restriction_record = {
            "restriction_of_scalars_used":True,
            "exact_original_1_omega_basis":True,
            "Fp_block_equation_shape":[int(block.nrows()),int(block.ncols())],
            "Fp_block_equation_rank":block_rank,
            "Fp_full_kernel_dimension":int(kernel_fp.nrows()),
            "actual_k_dimension_is_half_Fp_dimension":True,
            "Fp_block_equation_sha256":matrix_digest(block),
            "Fp_complete_kernel_sha256":matrix_digest(kernel_fp),
        }
    else:
        assert field is codec.field
        kernel = supplied_kernel
        assert kernel.base_ring() is field and kernel.ncols() == 2*dimension
        restriction_record = {
            "restriction_of_scalars_used":False,
            "source":"constant Frobenius of the entire original Ri1 kernel",
            "entire_kernel_returned_again_on_own_original_Ri2":True,
        }
    kernel_dimension = int(kernel.nrows())
    assert kernel_dimension >= int(minimum)
    assert kernel.ncols() == 2*dimension
    first, second = kernel[:, :dimension], kernel[:, dimension:]
    assert first.rank() == second.rank() == kernel_dimension
    K0, K1 = codec.matrix_components(kernel)
    assert (K0*M0-K1*M1).is_zero()
    assert (K0*M1+K1*M0-K1*M1).is_zero()
    chosen = kernel.row(0)
    first_denominator = next(i for i in range(dimension, 2*dimension) if chosen[i])
    chosen = chosen/chosen[first_denominator]
    numerator_coordinates = vector(field, chosen[:dimension])
    denominator_coordinates = vector(field, chosen[dimension:])
    ring = root.parent()
    numerator = ring(list(numerator_coordinates*basis.change_ring(field))).add_bigoh(length)
    denominator = ring(list(denominator_coordinates*basis.change_ring(field))).add_bigoh(length)
    assert numerator and denominator
    assert numerator.valuation() == denominator.valuation()
    order = int(numerator.valuation())
    assert numerator[order] == denominator[order]
    assert (numerator-root*denominator).add_bigoh(length) == 0
    record = {
        "original_root":label, "same_complete_section_dimension":dimension,
        "full_low_window_inclusive":[0,length-1],
        "complete_difference_pole_bound":length-1,
        "actual_complete_kernel_dimension":kernel_dimension,
        "proved_kernel_dimension_lower_bound":int(minimum),
        "both_entire_kernel_projections_injective":True,
        "all_original_equations_returned":True,
        "original_fraction_leading_value":1,
        "actual_common_cusp_order":order,
        "equation_real_component_sha256":matrix_digest(M0),
        "equation_omega_component_sha256":matrix_digest(M1),
        "entire_kernel_real_component_sha256":matrix_digest(K0),
        "entire_kernel_omega_component_sha256":matrix_digest(K1),
        "restriction_of_scalars":restriction_record,
        "numerator_coordinates_sha256":digest([[int(a),int(b)] for a,b in codec.coefficients(numerator_coordinates)]),
        "denominator_coordinates_sha256":digest([[int(a),int(b)] for a,b in codec.coefficients(denominator_coordinates)]),
    }
    progress("same original cube fraction completely identified", original_root=label,
             entire_kernel_dimension=kernel_dimension, full_coefficients=length)
    return {
        "numerator_coordinates":numerator_coordinates,
        "denominator_coordinates":denominator_coordinates,
        "full_kernel_coordinates":kernel,
        "low_numerator_series":numerator, "low_denominator_series":denominator,
        "original_root_series":root, "certificate":record,
    }, record


def build_original_cube_section_fractions(prime, first_cert, packet_cert):
    prime = int(prime)
    assert prime in (29, 41)
    assert certificate_weight(first_cert, "F") == 4
    assert certificate_weight(packet_cert, "P") == 6
    map_module = import_file("produce-original-map-section-fractions.py", "original_cube_map_source")
    r917 = import_file("produce-r917-original-global-rr-q-lattice.py", "original_cube_lattice_extension")
    local_module = import_file("produce-original-shadow-local-input.py", "original_cube_euler_source")
    maps, map_receipt = map_module.build_original_map_section_fractions(
        prime, first_cert, packet_cert, q_precision=1429)
    base = maps["original_r917_context"]
    fp, field = base["constants"], maps["constants"]
    assert maps["local_context"]["constants"] is field
    codec = OriginalOmegaCoordinates(fp, field, maps["original_omega"])
    fixed_transform = copy(base["rational_basis_transform"])
    low_rows, low_extension = extend_same_rows(
        base, base["global_modular_form_jets"], LOW_INPUT, r917, fixed_transform)
    recipes, recipe_receipt = append_complete_R6(low_rows, maps["complete_RR_product_recipes"], codec)
    low = OriginalSectionEvaluator(low_rows, codec, LOW_INPUT)
    arithmetic = low.arithmetic
    _, S_low = r917.original_denominator(fp, LOW_INPUT)
    S_pair = arithmetic.from_series(S_low)
    assert all(field(S_low[i]) == maps["original_S_series"][i] for i in range(1429))
    first = maps["F"]
    assert (int(first["numerator_power"]), int(first["denominator_recipe_power"]),
            int(first["denominator_S_power"])) == (5, 2, 3)
    F_A = low.section(recipes[5], first["numerator_coordinates"], 5)
    F_B = low.section(recipes[2], first["denominator_recipe_coordinates"], 2)
    F_D = arithmetic.mul(F_B, arithmetic.power(S_pair, 3))
    assert not F_A[1] and not F_B[1] and not F_D[1]
    for value, key in ((F_A,"numerator_modular_jets"),
                       (F_B,"denominator_recipe_modular_jets"),
                       (F_D,"same_degree_denominator_modular_jets")):
        assert all(field(value[0][i])+field(value[1][i])*codec.omega == first[key][i]
                   for i in range(1429))
    A_series, D_series = arithmetic.to_series(F_A, fp), arithmetic.to_series(F_D, fp)
    assert 0 <= D_series.valuation() <= 408
    assert A_series.valuation() == D_series.valuation()
    vF = A_series/D_series
    assert vF.valuation() == 0 and vF[0] == -1
    assert vF.precision_absolute() >= RF_LENGTH
    original_vF = maps["local_context"]["first"]["vF"]
    assert all(field(vF[i]) == original_vF[i] for i in range(min(len(original_vF), RF_LENGTH)))
    ring_F, tau_F, zeta_F = original_tau(fp, RF_LENGTH, local_module)
    Q_F = ring_F.gen()
    H_F = (ring_F(vF).add_bigoh(RF_LENGTH)**2*(zeta_F/tau_F)**3-17*Q_F/zeta_F).add_bigoh(RF_LENGTH)
    assert H_F.precision_absolute() >= RF_LENGTH and H_F[0] == 1
    RF_root, RF_newton = original_cube_root(H_F, RF_LENGTH, "RF")
    RF_basis = low.complete_basis(recipes[6], RF_LENGTH)
    assert RF_basis.nrows() == 1140
    RF, RF_kernel_receipt = fraction_kernel(RF_basis, RF_root, 52, codec, "RF")
    RF["section_power"] = 6
    RF["original_coordinate"] = "RF"
    RF_low_N = low.section(recipes[6], RF["numerator_coordinates"], 6)
    RF_low_E = low.section(recipes[6], RF["denominator_coordinates"], 6)
    assert arithmetic.to_series(RF_low_N, fp).add_bigoh(RF_LENGTH) == RF["low_numerator_series"]
    assert arithmetic.to_series(RF_low_E, fp).add_bigoh(RF_LENGTH) == RF["low_denominator_series"]

    P_basis = low.complete_basis(recipes[4], RP_LENGTH)
    assert P_basis.nrows() == 732
    RP, P_low_pairs, P_roots, P_newton, P_kernel_receipts = {}, {}, {}, [], []
    for index in (0, 1, 2):
        item, actual_local = maps["P"][index], maps["local_context"]["packet"][index]
        assert int(item["section_power"]) == 3
        for key in ("a17", "lambda", "v", "vnew"):
            assert item[key] == actual_local[key]
        target_field = fp if index == 0 else field
        A_pair = low.section(recipes[3], item["numerator_coordinates"], 3)
        B_pair = low.section(recipes[3], item["denominator_coordinates"], 3)
        for pair, key in ((A_pair,"numerator_modular_jets"),(B_pair,"denominator_modular_jets")):
            assert all(field(pair[0][i])+field(pair[1][i])*codec.omega == item[key][i]
                       for i in range(1429))
        A_series, B_series = arithmetic.to_series(A_pair, target_field), arithmetic.to_series(B_pair, target_field)
        assert 1 <= B_series.valuation() <= 612
        assert A_series.valuation()+1 == B_series.valuation()
        Q = A_series.parent().gen()
        QY = (Q*A_series)/B_series
        assert QY.valuation() == 0 and QY.precision_absolute() >= RP_LENGTH
        assert all(field(QY[i]) == actual_local["QY"][i] for i in range(len(actual_local["QY"])))
        ring_P, tau_P, zeta_P = original_tau(target_field, RP_LENGTH, local_module)
        vnew = codec.prime_scalar(item["vnew"]) if index == 0 else item["vnew"]
        qy = ring_P(QY).add_bigoh(RP_LENGTH)
        H = (qy*(qy+vnew*ring_P.gen())/zeta_P**2).add_bigoh(RP_LENGTH)
        assert H.precision_absolute() >= RP_LENGTH and H[0] == 1
        root, newton = original_cube_root(H, RP_LENGTH, "RP_%d" % index)
        supplied = None
        if index == 2:
            assert all(item[key] == maps["P"][1][key]**prime for key in ("a17", "lambda", "v", "vnew"))
            assert all(actual_local["QY"][i] == maps["local_context"]["packet"][1]["QY"][i]**prime
                       for i in range(len(actual_local["QY"])))
            for key in ("numerator_coordinates", "denominator_coordinates"):
                assert list(item[key]) == [c**prime for c in maps["P"][1][key]]
            assert all(root[i] == P_roots[1][i]**prime for i in range(RP_LENGTH))
            kernel1 = RP[1]["full_kernel_coordinates"]
            supplied = matrix(field, [[c**prime for c in row] for row in kernel1.rows()])
        result, record = fraction_kernel(P_basis, root, 120, codec, "RP_%d" % index, supplied)
        result["section_power"], result["original_coordinate"] = 4, "RP_%d" % index
        result["embedding"], result["vnew"] = index, item["vnew"]
        RP[index], P_roots[index] = result, root
        P_newton.append(newton)
        P_kernel_receipts.append(record)
        N_pair = low.section(recipes[4], result["numerator_coordinates"], 4)
        E_pair = low.section(recipes[4], result["denominator_coordinates"], 4)
        assert arithmetic.to_series(N_pair, target_field).add_bigoh(RP_LENGTH) == result["low_numerator_series"]
        assert arithmetic.to_series(E_pair, target_field).add_bigoh(RP_LENGTH) == result["low_denominator_series"]
        P_low_pairs[index] = {"A":A_pair,"B":B_pair,"N":N_pair,"E":E_pair}

    high_rows, high_extension = extend_same_rows(
        base, low_rows, RF_IDENTITY_LENGTH, r917, fixed_transform)
    high = OriginalSectionEvaluator(high_rows, codec, RF_IDENTITY_LENGTH)
    ar = high.arithmetic
    _, S_high = r917.original_denominator(fp, RF_IDENTITY_LENGTH)
    assert all(S_high[i] == S_low[i] for i in range(LOW_INPUT))
    S_high_pair = ar.from_series(S_high)
    selected = {
        "N":high.section(recipes[6], RF["numerator_coordinates"], 6),
        "E":high.section(recipes[6], RF["denominator_coordinates"], 6),
        "A":high.section(recipes[5], first["numerator_coordinates"], 5),
        "B":high.section(recipes[2], first["denominator_recipe_coordinates"], 2),
    }
    selected["D"] = ar.mul(selected["B"], ar.power(S_high_pair, 3))
    for name, old in (("N",RF_low_N),("E",RF_low_E),("A",F_A),("B",F_B),("D",F_D)):
        assert ar.truncate(selected[name], LOW_INPUT) == old
        assert not selected[name][1]
    _, tau, zeta = original_tau(fp, RF_IDENTITY_LENGTH, local_module)
    tau_pair, zeta_pair = ar.from_series(tau), ar.from_series(zeta)
    N3, E3 = ar.power(selected["N"],3), ar.power(selected["E"],3)
    D2, A2 = ar.power(selected["D"],2), ar.power(selected["A"],2)
    tau3, zeta4 = ar.power(tau_pair,3), ar.power(zeta_pair,4)
    first_term = ar.mul(ar.mul(N3,D2),ar.mul(tau3,zeta_pair))
    second_term = ar.mul(ar.mul(E3,A2),zeta4)
    third_term = ar.mul(ar.scalar(17),ar.shift(ar.mul(ar.mul(E3,D2),tau3),1))
    residual_F = ar.add(ar.sub(first_term,second_term),third_term)
    assert residual_F == ar.zero
    RF_identity = {
        "original_root":"RF", "same_section_total_power":28,
        "complete_global_zero_degree_bound":6936,
        "cusp_regularizing_shift":4,
        "full_checked_regular_coefficients_inclusive":[0,6940],
        "all_coefficients_zero":True,
        "original_global_identity_certified":True,
        "full_original_BF_S_cubed_retained":True,
        "equation":"N^3*D_F^2*tau^3*zeta-E^3*A_F^2*zeta^4+17*Q*E^3*D_F^2*tau^3",
        "all_selected_sections_preserve_old_2725_terms":True,
        "selected_high_section_hashes":{name:ar.hash(value) for name,value in selected.items()},
        "entire_residual_sha256":ar.hash(residual_F),
    }
    progress("complete original RF global cube identity passed", complete_coefficients=6941,
             global_zero_degree_bound=6936, regularizing_shift=4)
    P_identities, high_P = [], {}
    for index in (0, 1, 2):
        item, result = maps["P"][index], RP[index]
        actual = {
            "N":high.section(recipes[4],result["numerator_coordinates"],4),
            "E":high.section(recipes[4],result["denominator_coordinates"],4),
            "A":high.section(recipes[3],item["numerator_coordinates"],3),
            "B":high.section(recipes[3],item["denominator_coordinates"],3),
        }
        for name, value in actual.items():
            assert ar.truncate(value,LOW_INPUT) == P_low_pairs[index][name]
        pa = PairPolynomials(codec, RP_IDENTITY_LENGTH)
        N,E,A,B = [pa.truncate(actual[name]) for name in ("N","E","A","B")]
        zz = pa.truncate(zeta_pair)
        term1 = pa.mul(pa.mul(pa.power(N,3),pa.power(B,2)),pa.power(zz,2))
        term2 = pa.shift(pa.mul(pa.mul(pa.power(E,3),A),
                               pa.add(A,pa.mul(pa.scalar(item["vnew"]),B))),2)
        residual = pa.sub(term1,term2)
        assert residual == pa.zero
        record = {
            "original_root":"RP_%d" % index, "original_embedding":index,
            "same_section_total_power":18,
            "complete_global_zero_degree_bound":4284,
            "cusp_regularizing_shift":2,
            "full_checked_regular_coefficients_inclusive":[0,4286],
            "all_original_omega_components_zero":True,
            "original_global_identity_certified":True,
            "equation":"N^3*B_i^2*zeta^2-Q^2*E^3*A_i*(A_i+vnew_i*B_i)",
            "same_original_vnew_coordinates":[int(c) for c in codec.split(item["vnew"])],
            "all_selected_sections_preserve_old_2725_terms":True,
            "selected_high_section_hashes":{name:pa.hash(value) for name,value in actual.items()},
            "entire_residual_sha256":pa.hash(residual),
        }
        P_identities.append(record)
        high_P[index] = actual
        progress("complete original RP global cube identity passed", embedding=index,
                 complete_coefficients=4287, global_zero_degree_bound=4284,
                 regularizing_shift=2, both_original_omega_components=True)
    for name in ("N","E","A","B"):
        assert high_P[2][name] == ar.constant_frobenius(high_P[1][name])
    RF["complete_global_identity"] = RF_identity
    for index in (0,1,2):
        RP[index]["complete_global_identity"] = P_identities[index]
    context = {
        "kind":"rank2_original_cube_section_fractions_context",
        "prime":prime,"constants":field,"original_fp":fp,
        "original_omega":maps["original_omega"],"sigma_a_index":maps["sigma_a_index"],
        "map_context":maps,"original_map_sections_context":maps,
        "original_r917_context":base,
        "extended_original_M2_rows":high_rows,
        "extended_q_precision":RF_IDENTITY_LENGTH,
        "complete_product_recipes":recipes,"complete_RR_product_recipes":recipes,
        "RF":RF,"RP":RP,
        "original_S_high_series":S_high,
        "selected_RF_high_sections":selected,"selected_RP_high_sections":high_P,
        "original_omega_codec":codec,
    }
    dependencies = [Path(map_module.__file__),Path(r917.__file__),Path(local_module.__file__),
                    Path(section_quotient_algebra.__file__),
                    HERE/"original_pari_m2_basis.py",HERE/"original_shadow_coordinate_tools.py"]
    receipt = {
        "kind":"rank2_original_cube_section_fractions",
        "status":"same_original_RF_and_three_Ri_with_complete_global_cube_identities",
        "prime":prime,"level":867,
        "same_authenticated_F_and_P_source":map_receipt,
        "original_omega_coordinates":codec.receipt(),
        "same_original_lattice_extensions":[low_extension,high_extension],
        "complete_R6_source":recipe_receipt,
        "original_RF_unit_Newton":RF_newton,
        "original_RP_unit_Newton":P_newton,
        "original_RF_complete_low_kernel":RF_kernel_receipt,
        "original_RP_complete_low_kernels":P_kernel_receipts,
        "original_RF_full_global_cube_identity":RF_identity,
        "original_RP_full_global_cube_identities":P_identities,
        "original_RP2_own_QY_constants_and_all_high_identity_coefficients_verified":True,
        "RP2_constant_conjugation_distinct_from_original_Artin_permutation":True,
        "all_four_original_branches_have_leading_value_one":True,
        "complete_product_recipes_sha256":digest(recipes),
        "high_precision_full_R6_basis_matrix_constructed":False,
        "high_evaluation":"only selected genuine sections; grouped original product prefixes",
        "old_p_adic_germ_extended":False,
        "complete_divisors_computed":False,"original_shadow_computed":False,
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID",os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "sage_version":SAGE_VERSION,"image":os.environ.get("RANK2_IMAGE"),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
        "readme_blobs":{"root":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    return context, receipt


def main():
    parser = argparse.ArgumentParser()
    add_pinned_arguments(parser)
    args = parser.parse_args()
    request = pinned_request(args)
    incoming = sys.stdin.buffer.read(2*1024*1024+1)
    assert len(incoming) <= 2*1024*1024
    envelope = json.loads(incoming.decode("utf-8"))
    host_hash = hashlib.sha256((HERE/"read-original-shadow-pass-receipts.py").read_bytes()).hexdigest()
    first, packet = validate_envelope(envelope, request, host_hash)
    progress("both original complete PASS receipts authenticated",
             public_pass_envelope_sha256=envelope["envelope_sha256"])
    context, receipt = build_original_cube_section_fractions(args.prime,first,packet)
    globals()["ORIGINAL_CUBE_SECTION_FRACTIONS_CONTEXT"] = context
    receipt["public_pass_envelope_sha256"] = envelope["envelope_sha256"]
    receipt["authenticated_public_jobs"] = envelope["authentication"]
    payload = canonical(receipt)
    print("RANK2_CUBE_SECTIONS_RESULT "+payload,flush=True)
    print("RANK2_CUBE_SECTIONS_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed",failed_stage=failed,exception_type=type(exc).__name__,message=str(exc))
        raise

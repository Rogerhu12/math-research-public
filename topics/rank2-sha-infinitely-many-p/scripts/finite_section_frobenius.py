#!/usr/bin/env sage-python
"""Actual Frobenius and all closed components of original finite section algebras.

The input is an already authenticated complete global-section quotient algebra.
The expected geometry is used only as a gate after computing the full operator.
All idempotents are constructed in the same algebra, including every nilpotent
direction.  No coordinate output file is created.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public repository Actions.")

import hashlib
import json
from sage.all import ZZ, GF, matrix, vector, identity_matrix, PolynomialRing


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def matrix_digest(M):
    return digest([[int(x) for x in row] for row in M.rows()])


def vector_digest(v):
    return digest([int(x) for x in v])


def _default_progress(stage, **kw):
    print("RANK2_FINITE_FROBENIUS_STAGE " + canonical(dict(stage=stage, **kw)), flush=True)


def _coordinates(basis, rows):
    """Exact coordinates in an actual independent row basis, with full return."""
    assert basis.base_ring() == rows.base_ring()
    assert basis.ncols() == rows.ncols()
    pivots = tuple(basis.pivots())
    assert len(pivots) == basis.nrows()
    square = basis.matrix_from_columns(pivots)
    coefficients = rows.matrix_from_columns(pivots)*square.inverse()
    assert coefficients*basis == rows
    return coefficients


def _row_basis(M):
    B = M.row_space().basis_matrix()
    assert B.rank() == B.nrows()
    return B


def _split_fixed_algebra(algebra, frobenius, progress):
    """Split ker(F-1)=Fp^r by its actual multiplication operators.

    A row-basis element acts on this algebra with eigenvalues in Fp.  Projecting
    the current component identity into its exact eigenspaces produces genuine
    orthogonal idempotents.  Repeating on the fixed basis must distinguish all
    r components; no random primitive element or extension-field guess is used.
    """
    k, n = algebra["constants"], int(algebra["dimension"])
    p = int(k.characteristic())
    I = identity_matrix(k, n)
    fixed = (frobenius-I).left_kernel().basis_matrix()
    r = fixed.nrows()
    assert r > 0 and fixed*frobenius == fixed
    unit = algebra["unit"]
    unit_coords = _coordinates(fixed, matrix(k, [unit])).row(0)
    parts = [{"basis": identity_matrix(k, r), "unit": unit_coords}]
    splits = []

    for j, b in enumerate(fixed.rows()):
        if all(part["basis"].nrows() == 1 for part in parts):
            break
        M_b = algebra["multiplication_matrix"](b)
        C_b = _coordinates(fixed, fixed*M_b)
        new_parts = []
        for part in parts:
            W, one = part["basis"], part["unit"]
            d = W.nrows()
            if d == 1:
                new_parts.append(part)
                continue
            T_b = _coordinates(W, W*C_b)
            Id = identity_matrix(k, d)
            eigenspaces = []
            for c in range(p):
                E = (T_b-k(c)*Id).left_kernel().basis_matrix()
                if E.nrows():
                    eigenspaces.append((c, E))
            assert sum(E.nrows() for _, E in eigenspaces) == d
            stacked = matrix(k, [list(row) for _, E in eigenspaces for row in E.rows()])
            assert stacked.nrows() == d and stacked.rank() == d
            one_small = _coordinates(W, matrix(k, [one])).row(0)
            one_split = one_small*stacked.inverse()
            offset = 0
            for c, E in eigenspaces:
                count = E.nrows()
                coeff = vector(k, list(one_split[offset:offset+count]))
                child_one = (coeff*E)*W
                child_W = E*W
                assert not child_one.is_zero()
                new_parts.append({"basis": child_W, "unit": child_one})
                offset += count
            assert offset == d
        parts = new_parts
        assert sum(part["basis"].nrows() for part in parts) == r
        splits.append({"fixed_basis_row": j, "components_so_far": len(parts),
                       "remaining_fixed_dimensions": [int(part["basis"].nrows()) for part in parts]})
        progress("split actual Frobenius fixed algebra", fixed_basis_row=j,
                 closed_components=len(parts), required_components=r,
                 largest_unsplit_fixed_dimension=max(part["basis"].nrows() for part in parts))

    assert len(parts) == r and all(part["basis"].nrows() == 1 for part in parts)
    idempotents = matrix(k, [part["unit"]*fixed for part in parts])
    assert idempotents.rank() == r
    assert sum(idempotents.rows(), vector(k, n)) == unit
    assert idempotents*frobenius == idempotents
    matrices = []
    for j, e in enumerate(idempotents.rows()):
        M_e = algebra["multiplication_matrix"](e)
        observed = idempotents*M_e
        expected = matrix(k, r, n)
        expected.set_row(j, e)
        assert observed == expected, "The constructed idempotents must be pairwise orthogonal."
        assert M_e*M_e == M_e
        matrices.append(M_e)
    assert sum(matrices, matrix(k, n, n)) == I
    return fixed, idempotents, matrices, splits


def _closed_components(algebra, frobenius, mode, progress):
    k, n = algebra["constants"], int(algebra["dimension"])
    fixed, idempotents, projectors, splits = _split_fixed_algebra(algebra, frobenius, progress)
    P = PolynomialRing(k, "X_residue")
    X = P.gen()
    components, records = [], []
    zero = vector(k, n)
    total_nil_generator = vector(k, n)

    for i, (e, M_e) in enumerate(zip(idempotents.rows(), projectors)):
        ambient_dimension = int(M_e.rank())
        reduced_rows = _row_basis(M_e*frobenius)
        degree = int(reduced_rows.nrows())
        assert degree > 0
        # For the two admitted geometries im(F) is already the full reduced
        # algebra: F is bijective (cusps), or F^3=F (double divisor).
        if mode == "cusps":
            assert M_e*(frobenius**degree) == M_e
        assert reduced_rows*(frobenius**degree) == reduced_rows
        if degree == 1:
            alpha = zero
        else:
            proper = [degree//int(q) for q in ZZ(degree).prime_divisors()]
            alpha = None
            for candidate in reduced_rows.rows():
                if all(candidate*(frobenius**d) != candidate for d in proper):
                    alpha = candidate
                    break
            # The expected degrees 2 and 16 are prime powers.  Their proper
            # subfields lie in one maximal proper subfield, so one vector of
            # any full basis necessarily lies outside it.
            assert alpha is not None, "No primitive residue generator in the actual basis."
        M_alpha = algebra["multiplication_matrix"](alpha)
        powers = [e]
        for _ in range(1, degree+1):
            powers.append(powers[-1]*M_alpha)
        power_basis = matrix(k, powers[:degree])
        assert power_basis.rank() == degree
        relation = _coordinates(power_basis, matrix(k, [powers[degree]])).row(0)
        residue_polynomial = X**degree-sum((relation[j]*X**j for j in range(degree)), P.zero())
        assert residue_polynomial.degree() == degree
        assert residue_polynomial.is_irreducible()
        assert _coordinates(reduced_rows, power_basis).rank() == degree

        nil_dimension = ambient_dimension-degree
        nil_basis = matrix(k, 0, n)
        nil_generator = None
        if mode == "cusps":
            assert nil_dimension == 0
        else:
            assert mode == "ds" and degree == 2 and ambient_dimension == 4
            nil_basis = _row_basis(M_e-M_e*frobenius**2)
            assert nil_basis.nrows() == nil_dimension == degree
            assert nil_basis*frobenius == 0
            nil_generator = nil_basis.row(0)
            M_nil = algebra["multiplication_matrix"](nil_generator)
            assert (nil_generator*M_nil).is_zero()
            generated_nil = power_basis*M_nil
            assert generated_nil.rank() == degree
            assert _coordinates(nil_basis, generated_nil).rank() == degree
            # N=e*F_(p^2)*nu and nu^2=0 certify the entire local nilradical,
            # including all cross products; not just its reduced support.
            assert matrix(k, list(power_basis.rows())+list(generated_nil.rows())).rank() == ambient_dimension
            total_nil_generator = total_nil_generator+nil_generator

        components.append({
            "idempotent": e,
            "projector_matrix": M_e,
            "ambient_dimension": ambient_dimension,
            "residue_degree": degree,
            "residue_polynomial": residue_polynomial,
            "residue_generator": alpha,
            "residue_power_basis": power_basis,
            "nilradical_basis": nil_basis,
            "nilradical_generator": nil_generator,
        })
        records.append({
            "component_index": i,
            "ambient_dimension": ambient_dimension,
            "residue_degree": degree,
            "residue_polynomial_coefficients_ascending": [int(c) for c in residue_polynomial.list()],
            "residue_polynomial_irreducible": True,
            "idempotent_sha256": vector_digest(e),
            "actual_projector_rank": ambient_dimension,
            "reduced_generator_sha256": vector_digest(alpha),
            "reduced_power_basis_sha256": matrix_digest(power_basis),
            "nilradical_dimension": nil_dimension,
            "local_square_zero_generator_verified": mode == "ds",
            "nilradical_generator_sha256": (vector_digest(nil_generator) if nil_generator is not None else None),
        })
        progress("certified actual closed component", component=i,
                 total_components=idempotents.nrows(), residue_degree=degree,
                 ambient_dimension=ambient_dimension, nilradical_dimension=nil_dimension)

    assert sum(c["ambient_dimension"] for c in components) == n
    assert sum(c["residue_degree"] for c in components) == int(frobenius.rank())
    if mode == "cusps":
        assert sorted(c["residue_degree"] for c in components) == [1, 1, 1, 1, 16, 16]
    else:
        assert len(components) == 51
        assert all(c["residue_degree"] == 2 and c["ambient_dimension"] == 4 for c in components)
        assert (total_nil_generator*frobenius).is_zero()
        assert algebra["multiply"](total_nil_generator, total_nil_generator).is_zero()

    context = {
        "fixed_algebra_basis": fixed,
        "primitive_idempotents": idempotents,
        "components": components,
        "global_nilradical_generator": (total_nil_generator if mode == "ds" else None),
    }
    record = {
        "closed_component_count": len(components),
        "all_primitive_idempotents_constructed": True,
        "all_idempotents_mutually_orthogonal_and_sum_to_one": True,
        "fixed_algebra_basis_sha256": matrix_digest(fixed),
        "primitive_idempotents_sha256": matrix_digest(idempotents),
        "deterministic_fixed_algebra_splits": splits,
        "components": records,
        "full_nonreduced_components_retained": True,
        "global_nilradical_square_zero": mode == "ds",
    }
    return context, record


def inspect_frobenius(algebra, expected, progress=None, decompose=True):
    """Return the full Frobenius context and a compact independently gated receipt.

    expected='cusps': all 36 cusps, Fp^4 x F_(p^16)^2 at p=29 or 41.
    expected='ds': the complete degree-204 double divisor, 51 copies of
    F_(p^2)[epsilon]/epsilon^2, with every nilpotent coordinate retained.
    """
    progress = progress or _default_progress
    assert expected in ("cusps", "ds")
    k = algebra["constants"]
    n = int(algebra["dimension"])
    p = int(k.characteristic())
    assert int(k.cardinality()) == p and p in (29, 41)
    assert n == (36 if expected == "cusps" else 204)
    basis = identity_matrix(k, n)
    rows = []
    for i in range(n):
        rows.append(algebra["power"](basis.row(i), p))
        if i % 12 == 11 or i+1 == n:
            progress("compute actual Frobenius from every basis p-th power",
                     completed=i+1, total=n, prime=p, geometry=expected)
    F = matrix(k, rows)
    assert algebra["unit"]*F == algebra["unit"]
    rank = int(F.rank())
    polynomial = F.charpoly()
    X = polynomial.parent().gen()
    eig_plus = n-int((F-basis).rank())
    eig_minus = n-int((F+basis).rank())
    fixed_dimensions = []
    if expected == "cusps":
        assert rank == 36
        assert F**16 == basis
        expected_charpoly = (X-1)**4*(X**16-1)**2
        assert polynomial == expected_charpoly
        assert eig_plus == 6
        Fd = basis
        for d in range(1, 17):
            Fd = Fd*F
            observed = n-int((Fd-basis).rank())
            required = 4+2*int(ZZ(d).gcd(16))
            assert observed == required
            fixed_dimensions.append({"power": d, "actual_fixed_dimension": observed})
    else:
        assert rank == 102
        assert F**3 == F
        assert eig_plus == eig_minus == 51
        expected_charpoly = X**102*(X**2-1)**51
        assert polynomial == expected_charpoly
        assert (F**2)**2 == F**2 and (F**2).rank() == 102
        fixed_dimensions = [
            {"power": 1, "actual_fixed_dimension": eig_plus},
            {"power": 2, "actual_fixed_dimension": n-int((F**2-basis).rank())},
        ]
        assert fixed_dimensions[1]["actual_fixed_dimension"] == 102
    progress("full actual Frobenius operator passed geometric gates", geometry=expected,
             dimension=n, actual_rank=rank, plus_eigenspace=eig_plus,
             minus_eigenspace=eig_minus)

    # For the cusp algebra this small complete compatibility verification is
    # cheap.  For dimension 204, homomorphy follows from the already established
    # commutative associative section algebra and every actual p-th power above.
    compatibility_checked = False
    if expected == "cusps":
        for i, M_i in enumerate(algebra["multiplication_matrices"]):
            M_Fi = algebra["multiplication_matrix"](F.row(i))
            assert M_i*F == F*M_Fi
        compatibility_checked = True

    decomposition_context, decomposition_record = None, None
    if decompose:
        decomposition_context, decomposition_record = _closed_components(
            algebra, F, expected, progress)
    context = {
        "constants": k, "dimension": n, "frobenius_matrix": F,
        "nilradical_basis": F.left_kernel().basis_matrix(),
        "decomposition": decomposition_context,
    }
    receipt = {
        "geometry": expected,
        "prime": p, "complete_algebra_dimension": n,
        "full_frobenius_computed_from_all_basis_pth_powers": True,
        "frobenius_sha256": matrix_digest(F),
        "actual_frobenius_rank": rank,
        "actual_characteristic_polynomial_coefficients_ascending": [int(c) for c in polynomial.list()],
        "complete_expected_characteristic_polynomial_verified": True,
        "plus_one_eigenspace_dimension": eig_plus,
        "minus_one_eigenspace_dimension": eig_minus,
        "actual_fixed_dimensions": fixed_dimensions,
        "entire_algebra_etale": rank == n,
        "actual_nilradical_dimension": n-rank,
        "complete_frobenius_multiplication_matrix_compatibility_checked": compatibility_checked,
        "frobenius_homomorphy_basis": "p-th power in the authenticated associative commutative section algebra",
        "decomposition": decomposition_record,
    }
    return context, receipt


def _canonical_residue_field(k, degree):
    """Fixed explicit residue models shared by all original divisor cuts."""
    degree = int(degree)
    assert int(k.cardinality()) == int(k.characteristic())
    assert int(k.characteristic()) in (29, 41) and degree in (1, 2, 16)
    if degree == 1:
        return k, [0, 1]
    P = PolynomialRing(k, "X_canonical_residue")
    X = P.gen()
    if degree == 2:
        candidate = 2
        while k(candidate).is_square():
            candidate += 1
        modulus = X**2-k(candidate)
    else:
        assert degree == 16
        modulus = sum((X**i for i in range(17)), P.zero())
    assert modulus.is_irreducible()
    field = GF(int(k.characteristic())**degree, "z_residue_%d" % degree,
               modulus=modulus)
    return field, [int(c) for c in modulus.list()]


def _field_coordinates(value, degree):
    if degree == 1:
        return [int(value)]
    coefficients = [int(c) for c in value.polynomial().list()]
    assert len(coefficients) <= degree
    return coefficients+[0]*(degree-len(coefficients))


def label_closed_components(algebra, frobenius_context, component_coordinate_rows,
                            coordinate_basis_id, progress=None):
    """Label every closed point by the same original global projective embedding.

    Each item is a matrix of genuine global-section coordinate ratios in its
    full ambient component, not a guessed residue-field point.  Its nilpotent
    coordinates remain in the returned context.  Only the explicit closed-point
    label applies Frobenius to pass to the residue field.  Fixed degree-2 and
    degree-16 field models and a canonical full Frobenius orbit make the labels
    comparable between different cuts using the SAME original M2 basis.
    """
    progress = progress or _default_progress
    decomposition = frobenius_context["decomposition"]
    assert decomposition is not None
    components = decomposition["components"]
    assert len(component_coordinate_rows) == len(components)
    k, n = algebra["constants"], int(algebra["dimension"])
    p = int(k.characteristic())
    assert int(k.cardinality()) == p and p in (29, 41)
    F = frobenius_context["frobenius_matrix"]
    fields = {}
    contexts, records = [], []
    coordinate_count = None
    for i, (component, rows) in enumerate(zip(components, component_coordinate_rows)):
        assert rows.base_ring() == k and rows.ncols() == n
        assert rows*component["projector_matrix"] == rows
        if coordinate_count is None:
            coordinate_count = int(rows.nrows())
        assert rows.nrows() == coordinate_count
        degree = int(component["residue_degree"])
        reduced = rows*(F**degree)
        coordinates = _coordinates(component["residue_power_basis"], reduced)
        assert reduced*(F**degree) == reduced
        if degree not in fields:
            fields[degree] = _canonical_residue_field(k, degree)
        field, modulus_coefficients = fields[degree]
        polynomial = component["residue_polynomial"]
        if degree == 1:
            root = field(-polynomial[0]/polynomial[1])
        else:
            roots = polynomial.change_ring(field).roots(multiplicities=False)
            assert len(roots) == degree
            # A factorization backend may return the conjugate roots in a
            # different order.  The fixed polynomial model and coefficient
            # tuple make even this in-process embedding deterministic.  The
            # final full Frobenius orbit is independent of the chosen root.
            root = min(roots, key=lambda value: tuple(_field_coordinates(value, degree)))
        assert polynomial.change_ring(field)(root) == 0
        values = []
        for row in coordinates.rows():
            value = field.zero()
            for coefficient in reversed(row):
                value = value*root+field(coefficient)
            values.append(value)
        nonzero = [j for j, value in enumerate(values) if value]
        assert nonzero, "The original global sections must not all vanish at this point."
        first = nonzero[0]
        pivot = values[first]
        values = [value/pivot for value in values]
        assert values[first] == 1
        orbit = []
        for _ in range(degree):
            flat = tuple(c for value in values for c in _field_coordinates(value, degree))
            orbit.append(flat)
            values = [value**p for value in values]
        assert len(set(orbit)) == degree, "Global projective coordinates did not separate a whole closed point."
        canonical_orbit_representative = min(orbit)
        point_id = digest({
            "encoding": "original-M2-projective-Frobenius-orbit-v1",
            "prime": p, "residue_degree": degree,
            "coordinate_basis_id": coordinate_basis_id,
            "canonical_field_modulus": modulus_coefficients,
            "coordinates": canonical_orbit_representative,
        })
        contexts.append({
            "component_index": i,
            "full_component_coordinate_rows": rows,
            "reduced_coordinate_rows": reduced,
            "residue_power_coordinates": coordinates,
            "canonical_residue_field": field,
            "residue_generator_image": root,
            "canonical_projective_orbit_representative": canonical_orbit_representative,
            "point_id": point_id,
        })
        records.append({
            "component_index": i,
            "residue_degree": degree,
            "original_global_coordinate_count": coordinate_count,
            "first_nonzero_projective_coordinate": first,
            "canonical_field_modulus_coefficients_ascending": modulus_coefficients,
            "full_component_coordinate_rows_sha256": matrix_digest(rows),
            "reduced_residue_power_coordinates_sha256": matrix_digest(coordinates),
            "complete_projective_frobenius_orbit_length": len(set(orbit)),
            "original_curve_point_id_sha256": point_id,
        })
        progress("label actual closed point in original global embedding",
                 component=i, total_components=len(components), residue_degree=degree,
                 global_coordinates=coordinate_count, point_id_sha256=point_id)
    assert len({record["original_curve_point_id_sha256"] for record in records}) == len(records)
    return {"coordinate_basis_id": coordinate_basis_id, "components": contexts}, {
        "coordinate_basis_id": coordinate_basis_id,
        "fingerprint_base_field": "GF(%d)" % p,
        "fingerprint_frobenius_power": 1,
        "original_global_coordinate_count": coordinate_count,
        "every_closed_point_separated_by_same_global_embedding": True,
        "canonical_full_frobenius_orbits_used": True,
        "nonreduced_coordinate_rows_retained_in_process": True,
        "base_change_scope": (
            "These are full p-Frobenius closed points over Fp.  A later Fp^2 "
            "consumer must fix its original constant-field embedding and split "
            "the p^2-Frobenius orbits; it must not merge the resulting points."),
        "closed_point_labels": records,
    }

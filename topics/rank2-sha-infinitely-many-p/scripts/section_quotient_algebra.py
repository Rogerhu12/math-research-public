"""Exact finite divisor algebras from complete section spaces.

All coefficients, quotient bases and multiplication tables remain in process.
The caller supplies authenticated global section spaces for ONE divisor Z:
M_n = H0(L^n)/H0(L^n(-Z)) and M_2n at twice the degree.  A section h
whose multiplication M_n -> M_2n is invertible trivializes L^n on all Z,
including its nonreduced structure.  R924 proves that the transported
multiplication is precisely Gamma(Z, O_Z).

No geometric provenance or completeness is inferred from arbitrary q strings.
The caller must certify those inputs before invoking this helper.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public research Actions.")

import hashlib
import json
from sage.all import PowerSeriesRing, identity_matrix, matrix, vector


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def matrix_digest(value):
    """Streaming hash; never serialize a large coefficient array to output."""
    k = value.base_ring()
    assert k.cardinality() == k.characteristic()
    output = hashlib.sha256()
    output.update(canonical({"encoding":"prime-field-matrix-v1",
                             "prime":int(k.characteristic()),
                             "rows":int(value.nrows()),
                             "columns":int(value.ncols())}).encode())
    for row in value.rows():
        output.update(b"\n")
        output.update(",".join(str(int(c)) for c in row).encode())
    return output.hexdigest()


def vector_digest(value):
    return digest([int(c) for c in value])


def series_matrix(series, k, precision):
    return matrix(k, [[s[j] for j in range(precision)] for s in series])


def build_quotient(full_rows, ideal_rows, sturm, label, progress):
    """Build a full section quotient with exact projection and actual lifts.

    Rows are q coefficients of genuine global sections of the SAME bundle.
    ``sturm`` is an already proved injective jet length for that bundle.
    No ambient jet cokernel is confused with the quotient of global sections.
    """
    k = full_rows.base_ring()
    sturm = int(sturm)
    assert k.cardinality() == k.characteristic()
    assert ideal_rows.base_ring() == k
    assert ideal_rows.ncols() == full_rows.ncols()
    assert full_rows.ncols() >= sturm
    dimension = int(full_rows.nrows())
    ideal_dimension = int(ideal_rows.nrows())
    assert 0 < ideal_dimension < dimension <= sturm
    prefix = full_rows[:, :sturm]
    pivots = tuple(prefix.pivots())
    assert len(pivots) == dimension
    inverse = prefix.matrix_from_columns(pivots).inverse()
    assert prefix.matrix_from_columns(pivots)*inverse == identity_matrix(k, dimension)
    nonpivots = tuple(j for j in range(sturm) if j not in set(pivots))
    reconstruction = inverse*prefix.matrix_from_columns(nonpivots)

    def membership(jets):
        assert jets.base_ring() == k and jets.ncols() >= sturm
        entries = jets.matrix_from_columns(pivots)
        # Pivot columns hold identically by construction.  This equality
        # checks EVERY remaining coefficient through the full Sturm bound.
        assert entries*reconstruction == jets.matrix_from_columns(nonpivots), (
            "A proposed section is outside the authenticated full space: " + label)
        return entries

    ideal_entries = membership(ideal_rows)
    ideal_coordinates = ideal_entries*inverse
    assert ideal_coordinates*prefix == ideal_rows[:, :sturm]
    echelon = ideal_coordinates.echelon_form()
    ideal_pivots = tuple(echelon.pivots())
    assert len(ideal_pivots) == ideal_dimension
    assert echelon.nrows() == ideal_dimension
    assert echelon.matrix_from_columns(ideal_pivots) == identity_matrix(k, ideal_dimension)
    free = tuple(j for j in range(dimension) if j not in set(ideal_pivots))
    quotient_dimension = len(free)
    position = {column:i for i, column in enumerate(ideal_pivots)}
    quotient = matrix(k, dimension, quotient_dimension,
        lambda i, j: (-echelon[position[i], free[j]] if i in position
                      else k.one() if i == free[j] else k.zero()))
    assert (ideal_coordinates*quotient).is_zero()
    assert quotient.matrix_from_rows(free) == identity_matrix(k, quotient_dimension)
    projection = inverse*quotient

    def project(jets, verify=True):
        entries = membership(jets) if verify else jets.matrix_from_columns(pivots)
        return entries*projection

    lifts = full_rows.matrix_from_rows(free)
    assert project(lifts) == identity_matrix(k, quotient_dimension)
    assert project(ideal_rows).is_zero()
    certificate = {
        "label":label,
        "prime":int(k.characteristic()),
        "full_dimension":dimension,
        "ideal_dimension":ideal_dimension,
        "quotient_dimension":quotient_dimension,
        "complete_jet_coefficients":sturm,
        "retained_jet_precision":int(full_rows.ncols()),
        "full_space_rank":dimension,
        "full_ideal_rank":ideal_dimension,
        "ideal_full_sturm_membership_verified":True,
        "quotient_basis_lifts_verified":True,
        "quotient_kills_complete_ideal":True,
        "full_rows_sha256":matrix_digest(full_rows),
        "ideal_rows_sha256":matrix_digest(ideal_rows),
        "full_space_pivot_columns_sha256":digest(list(pivots)),
        "full_space_pivot_inverse_sha256":matrix_digest(inverse),
        "remaining_sturm_column_count":len(nonpivots),
        "remaining_sturm_columns_sha256":digest(list(nonpivots)),
        "membership_check":"pivot coordinates defined by the exact inverse; every remaining Sturm coefficient checked",
        "ideal_coordinates_sha256":matrix_digest(ideal_coordinates),
        "ideal_echelon_sha256":matrix_digest(echelon),
        "ideal_pivot_columns_sha256":digest(list(ideal_pivots)),
        "quotient_lift_indices_sha256":digest(list(free)),
        "quotient_projection_sha256":matrix_digest(projection),
        "quotient_lifts_sha256":matrix_digest(lifts),
    }
    progress("complete global section quotient certified", label=label,
             full_dimension=dimension, ideal_dimension=ideal_dimension,
             quotient_dimension=quotient_dimension, full_sturm=sturm)
    return {"constants":k, "full_dimension":dimension,
            "quotient_dimension":quotient_dimension, "sturm":sturm,
            "jet_precision":int(full_rows.ncols()), "lift_rows":lifts,
            "project":project, "certificate":certificate}


def multiplication_by_section(source, target, h_row, progress, batch_size=128):
    """Return the COMPLETE quotient matrix of multiplication by actual h."""
    k = source["constants"]
    assert target["constants"] == k
    n = source["quotient_dimension"]
    assert target["quotient_dimension"] == n
    precision = target["sturm"]
    assert source["jet_precision"] >= precision and len(h_row) >= precision
    batch_size = int(batch_size)
    assert batch_size > 0
    source["project"](matrix(k, [list(h_row)]))
    ring = PowerSeriesRing(k, "Q_section", default_prec=precision)
    h = ring(list(h_row[:precision])).add_bigoh(precision)
    lifts = [ring(list(row[:precision])).add_bigoh(precision)
             for row in source["lift_rows"].rows()]
    output = []
    for start in range(0, n, batch_size):
        products = [(a*h).add_bigoh(precision) for a in lifts[start:start+batch_size]]
        projected = target["project"](series_matrix(products, k, precision))
        output.extend(projected.rows())
    multiplier = matrix(k, output)
    assert multiplier.nrows() == multiplier.ncols() == n
    rank = int(multiplier.rank())
    record = {"source_dimension":n, "target_dimension":n,
              "rank":rank, "unit_on_complete_divisor":rank == n,
              "all_products_full_sturm_verified":True,
              "h_row_sha256":vector_digest(h_row),
              "matrix_sha256":matrix_digest(multiplier),
              "source_quotient_sha256":digest(source["certificate"]),
              "target_quotient_sha256":digest(target["certificate"])}
    progress("complete section multiplier rank", dimension=n, rank=rank,
             unit_on_complete_divisor=rank == n)
    return multiplier, record


def build_algebra(source, target, h_row, progress, batch_size=128,
                  precomputed_h=None):
    """Transport all products by the full invertible h multiplication map.

    Matrix convention: y*M_i = e_i*y for ROW coordinate vectors y.
    Associativity is the exact section-algebra transport in R924, not a
    claim based on testing only reduced points or a random set of triples.
    """
    k = source["constants"]
    assert target["constants"] == k
    n = source["quotient_dimension"]
    assert target["quotient_dimension"] == n
    precision = target["sturm"]
    assert source["jet_precision"] >= precision
    if precomputed_h is None:
        H, h_record = multiplication_by_section(source, target, h_row, progress,
                                               batch_size=batch_size)
    else:
        H, h_record = precomputed_h
        assert h_record["h_row_sha256"] == vector_digest(h_row)
        assert h_record["matrix_sha256"] == matrix_digest(H)
        assert h_record["source_quotient_sha256"] == digest(source["certificate"])
        assert h_record["target_quotient_sha256"] == digest(target["certificate"])
    assert H.nrows() == H.ncols() == n
    assert h_record["rank"] == n and h_record["unit_on_complete_divisor"]
    inverse = H.inverse()
    assert H*inverse == identity_matrix(k, n)
    unit = source["project"](matrix(k, [list(h_row)])).row(0)
    ring = PowerSeriesRing(k, "Q_section", default_prec=precision)
    lifts = [ring(list(row[:precision])).add_bigoh(precision)
             for row in source["lift_rows"].rows()]
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    tables = [[None]*n for _ in range(n)]
    batch_size = int(batch_size)
    assert batch_size > 0
    for start in range(0, len(pairs), batch_size):
        batch = pairs[start:start+batch_size]
        products = [(lifts[i]*lifts[j]).add_bigoh(precision) for i, j in batch]
        raw = target["project"](series_matrix(products, k, precision))
        returned = raw*inverse
        assert returned*H == raw
        for index, (i, j) in enumerate(batch):
            row = returned.row(index)
            tables[i][j] = row
            tables[j][i] = row
        completed = min(start+batch_size, len(pairs))
        if completed == len(pairs) or (start//batch_size) % 8 == 0:
            progress("complete section algebra products", completed=completed,
                     total=len(pairs), dimension=n, full_sturm=precision)
    matrices = tuple(matrix(k, rows) for rows in tables)
    del tables
    for i, M in enumerate(matrices):
        expected = vector(k, n)
        expected[i] = 1
        assert unit*M == expected
        for j in range(i, n):
            assert M.row(j) == matrices[j].row(i)

    def multiplication_matrix(x):
        x = vector(k, x)
        assert len(x) == n
        nonzero = [(i, c) for i, c in enumerate(x) if c]
        if not nonzero:
            return matrix(k, n, n)
        i, c = nonzero[0]
        answer = matrices[i] if c == 1 else c*matrices[i]
        for i, c in nonzero[1:]:
            answer = answer+c*matrices[i]
        return answer

    def multiply(x, y):
        y = vector(k, y)
        assert len(y) == n
        return y*multiplication_matrix(x)

    def power(x, exponent):
        exponent = int(exponent)
        assert exponent >= 0
        if exponent == 0:
            return vector(k, unit)
        M = multiplication_matrix(x)
        answer = vector(k, unit)
        if exponent <= 64:
            for _ in range(exponent):
                answer = answer*M
            return answer
        while exponent:
            if exponent & 1:
                answer = answer*M
            exponent >>= 1
            if exponent:
                M = M*M
        return answer

    hashes = [matrix_digest(M) for M in matrices]
    certificate = {
        "kind":"exact_section_quotient_finite_algebra",
        "prime":int(k.characteristic()), "dimension":n,
        "source_quotient":source["certificate"],
        "target_quotient":target["certificate"],
        "h_multiplier":h_record,
        "h_multiplier_inverse_sha256":matrix_digest(inverse),
        "complete_unordered_product_count":len(pairs),
        "all_basis_products_full_sturm_verified":True,
        "all_products_returned_by_same_h_inverse":True,
        "unit_verified_on_every_basis_vector":True,
        "commutativity_verified_on_every_basis_pair":True,
        "associativity_basis":"R924 exact transport of multiplication on the complete divisor scheme",
        "exhaustive_triple_associativity_test_claimed":False,
        "unit_coordinates_sha256":vector_digest(unit),
        "multiplication_table_sha256":digest(hashes),
        "nilradical_or_closed_point_decomposition_claimed":False,
        "all_bases_and_tables_kept_in_process_only":True,
        "helper_sha256":hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
    }
    progress("complete finite section algebra certified", dimension=n,
             unordered_products=len(pairs), full_unit_verified=True,
             multiplication_table_sha256=certificate["multiplication_table_sha256"])
    context = {"constants":k, "dimension":n, "unit":unit,
               "multiplication_matrices":matrices,
               "multiplication_matrix":multiplication_matrix,
               "multiply":multiply, "power":power,
               "source_quotient":source, "target_quotient":target,
               "h_row":h_row, "certificate":certificate}
    return context, certificate

#!/usr/bin/env sage-python
"""Translate only complete W4 and W8 sections into the original two polynomial charts."""
import os
if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Run only in the named public research Actions.")
import numpy as np
from sage.all import matrix, vector
from original_ys_divisor_ideal_tools import element_digest, polynomial_matrix_digest
from original_descended_pencil_sections import require, original_m2, normalized_level_sections, original_endpoint_germ, load_script
from original_descended_pencil_sections import coefficients, pack_polys, packed_hash
from original_descended_pencil_kernel import certify_g3, WholePencil


class PhysicalReturn:
    """Read every coefficient in the original faithful Laurent window."""
    def __init__(self, apery, finite, weight):
        self.finite = finite
        self.w = weight
        fp = apery["constants"]
        self.fp = fp
        self.table = apery["monomial_rows"][weight]
        self.recipes = apery["monomial_recipes"][weight]
        self.n = finite.dimension
        expected = self.n*weight+1
        require(self.table.ncols() == expected and self.table.nrows() == len(self.recipes),
                "Wrong complete physical jet window")
        source = load_script("produce-original-y-global-section-and-ys.py")
        self.read, self.receipt = source.complete_membership_reader(self.table, expected, "original W%d" % weight)

    def read_planes(self, jets, scales):
        f, r, length = jets.shape
        require(f == len(scales) and length == self.n*self.w+1 and self.finite.R.base_ring() is self.finite.k,
                "Incorrect source basis or returned coefficient planes")
        R = self.finite.R
        t = R.gen()
        input_jets = matrix(self.fp, [row.tolist() for plane in jets for row in plane])
        flat = self.read(input_jets)
        require(flat*self.table == input_jets, "A physical source did not return every ordinary coefficient")
        polys = []
        for j in range(r):
            row = vector(R, self.n)
            for a, scale in enumerate(scales):
                for coeff, (i, power) in zip(flat.row(a*r+j), self.recipes):
                    if coeff:
                        row[int(i)] += scale*self.finite.k(coeff)*t**int(power)
            row.set_immutable()
            polys.append(row)
        return polys


def reciprocal(row, finite, infinity, weights, grade):
    require(row.base_ring() is finite.R and finite.k is infinity.k and len(weights) == len(row),
            "Wrong original chart data for reciprocal transformation")
    s = infinity.R.gen()
    result = vector(infinity.R, len(row))
    for i, entry in enumerate(row):
        limit = grade - weights[i]
        require(not entry or entry.degree() <= limit, "A physical row exceeded the complete two-chart grade")
        for power, c in enumerate(entry.list()):
            if c:
                result[i] += c*s**(limit-power)
    other = finite.R.gen()
    for i, entry in enumerate(result):
        back = sum((c*other**(grade-weights[i]-j) for j, c in enumerate(entry.list()) if c), finite.R.zero())
        require(back == row[i], "A reciprocal coefficient was lost")
    result.set_immutable()
    return result


def selected_physical_sections(field, sections, pairs, lift8):
    """Use the canonical W2+uW2 recipe: each output costs only two scalar polynomials."""
    R = lift8.finite.R
    h2, h3 = len(sections["two"]), len(sections["three"])
    ids = sections["three_ids"]
    length = lift8.n*8+1
    require(sections["length"] >= length and all(row.shape == (field.f, 2*h3) for row in pairs),
            "Missing actual W8 coefficients or full selected pairs")
    # q^8 t^6 r=(q*t)^6(q^2 r), r in W2.
    factor = (sections["z"].truncate(length)**6).truncate(length)
    physical_two = pack_polys([(v.truncate(length)*factor).truncate(length) for v in sections["two"]], length)
    coeff = np.zeros((field.f, 4*len(pairs), h2), dtype=np.uint8)
    require(len(set(ids)) == h3 and all(0 <= i < 2*h2 for i in ids), "Corrupt scalar-pencil projection")
    for k, row in enumerate(pairs):
        for projection in range(2):
            for j, source in enumerate(ids):
                group, i = divmod(source, h2)
                coeff[:, 4*k+2*projection+group, i] = row[:, projection*h3+j]
    basis = np.zeros((field.f, h2, length), dtype=np.uint8)
    basis[0] = physical_two
    jets = field.product(coeff, basis).astype(np.uint8)
    subrows = lift8.read_planes(jets, field.basis)
    t = R.gen()
    t3u = (R.base_ring().one()/R.base_ring()(8))*(t**4 + 18*t**2 - 27)
    rows = []
    for k in range(len(pairs)):
        result = []
        for role in range(2):
            i = 4*k+2*role
            value = t**3*subrows[i]+t3u*subrows[i+1]
            value.set_immutable()
            result.append(value)
        rows.append(tuple(result))
    return rows, dict(full_physical_W8_receipt=lift8.receipt, actual_W8_inputs=len(subrows),
                      complete_normalized_W8_jets_sha256=packed_hash(jets),
                      complete_physical_W8_vectors=[element_digest(row) for row in subrows],
                      physical_finite_pairs=[[element_digest(row) for row in pair] for pair in rows])


class OriginalPencilSource:
    def __init__(self, six, engines):
        self.six, self.engines = six, engines
        finite = engines[False]
        model, affine = six["model"], six["original_affine_context"]
        apery = affine["original_apery_context"]
        require(six["kind"] == "rank2_original_Y_fraction_consumer_context" and set(engines) == {False,True} and
                model.affine is affine and model.embedding is six["embedding_context"] and
                model.operations is model.embedding["operations"] and int(six["prime"]) == int(model.prime) == 29 and
                int(apery["level"]) == 3468 and apery["q_precision"] >= 2453 and
                six["constants"] is model.k is model.embedding["constants"] is six["cube_context"]["constants"] and
                int(model.k.cardinality()) == 29**2, "Changed original fraction source, prime, or affine owner")
        self.weights = tuple(map(int, apery["apery_weights"]))
        require(self.weights == tuple(model.weights) == tuple(affine["basis_weights"]) and
                [self.weights.count(j) for j in range(5)] == [1,0,65,226,14] and len(self.weights) == 306 and
                sum(self.weights) == 864, "Changed full original integral basis weights")
        for flag, ring, name in ((False,model.P,"affine_polynomial_ring"),
                                (True,model.S,"infinity_polynomial_ring")):
            engine = engines[flag]
            chart = engine.chart
            require(engine.infinity_chart is flag and chart["infinity_chart"] is flag and
                    int(engine.dimension) == int(chart["dimension"]) == 306 and
                    engine.R is chart["polynomial_ring"] is ring is model.operations[name] and
                    engine.k is chart["constants"] is ring.base_ring() is model.k and
                    self.weights == tuple(map(int,chart["original_basis_weights"])) and
                    engine.unit == chart["unit"], "The original physical engine, ring, or weighted chart changed")
        length = 2449
        full, modular = original_m2(1156, 306, 180, 29, length)
        self.sections = normalized_level_sections(full, apery["original_z_series"], apery["J_over_u4"],
                                                  306, 127, length)
        lift4 = PhysicalReturn(apery, finite, 4)
        norm = (self.sections["z"].truncate(1225)**3).truncate(1225)
        jets = pack_polys([(norm*a.truncate(1225)).truncate(1225) for a in self.sections["one"]], 1225)
        w4 = lift4.read_planes(jets[None, :, :], [finite.k.one()])
        require(len(w4) == 180, "Incomplete original W1 to physical W4 return")
        self.cert = dict(actual_level_modular_source=modular,
                         graded_source=self.sections["certificate"], physical_W4=lift4.receipt,
                         all_180_returned_source_rows_sha256=polynomial_matrix_digest(matrix(finite.R, w4)))
        self.lift8 = PhysicalReturn(apery, finite, 8)

    def endpoint(self, index):
        function = self.six["A"][index]["y0"]
        qf, germ = original_endpoint_germ(self.six, index, 1483)
        field, K, graph = certify_g3(self.sections, qf, 306, 127, 564)
        pencil = WholePencil(field, self.sections, 306, 127, 564)
        pairs, selection = pencil.select(K)
        finite, infinity = self.engines[False], self.engines[True]
        first, lift = selected_physical_sections(field, self.sections, pairs, self.lift8)
        second = [tuple(reciprocal(row, finite, infinity, self.weights, 12) for row in pair) for pair in first]
        charts = {False:first, True:second}
        original = {}
        for flag, rows in charts.items():
            N, D = function.chart_pair(flag)
            engine = self.engines[flag]
            for h, x in rows:
                require(engine.multiply(N, h) == engine.multiply(D, x), "An actual original N,D row failed")
            original[str(flag)] = dict(original_N=element_digest(N), original_D=element_digest(D),
                                       source_pairs=[[element_digest(h), element_digest(x)] for h, x in rows])
        return charts, dict(source=self.cert, germ=germ, G3=graph, common_zero_check=selection, lift=lift,
                            actual_original_function_id=id(function), actual_original_endpoint=index,
                            original_two_chart_maps=original)

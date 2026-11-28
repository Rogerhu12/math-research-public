#!/usr/bin/env sage-python
"""The genuine level-1156 weight-two source and two ordered original A germs."""
import os
if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Run only in the named public research Actions.")
import hashlib
import importlib.util
from pathlib import Path
import numpy as np
from sage.all import GF, QQ, PolynomialRing, PowerSeriesRing, matrix, pari
from original_short_graph_kernel import prime_rref
from section_quotient_algebra import digest, matrix_digest

HERE = Path(__file__).resolve().parent


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def load_script(name):
    path = HERE / name
    spec = importlib.util.spec_from_file_location("descended_" + path.stem.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def original_m2(level, degree, dimension, p, precision):
    """Saturate the faithful window and extend the very same rational basis."""
    require((level, degree, dimension) in ((1156, 306, 180), (4, 1, 2)), "Unexpected modular source")
    faithful = degree + 1
    require(precision >= faithful and p == 29, "Insufficient source precision")
    owner = pari.mfinit([level, 2, 1], 4)
    require(list(map(int, list(pari.mfparams(owner))[:4])) == [level, 2, 1, 4] and
            int(pari.mfspace(owner)) == 4 and int(pari.mfdim(owner)) == dimension and
            len(list(pari.mfbasis(owner))) == dimension, "Incorrect full rational modular-form space")
    def coefficients(length):
        columns = pari.mfcoefs(owner, length - 1)
        require(tuple(map(int, columns.matsize())) == (length, dimension), "Wrong PARI expansion shape")
        return matrix(QQ, dimension, length, lambda i, j: QQ(columns[j, i]))
    saturation = load_script("produce-r917-original-global-rr-q-lattice.py")
    initial = coefficients(faithful)
    saturated, transform, reduced, cert = saturation.saturate_original_rows(initial, p)
    full = coefficients(precision)
    require(full[:, :faithful] == initial, "The modular-form owner changed its initial jets")
    transformed = transform * full
    require(transformed[:, :faithful] == saturated, "Changed saturated lattice")
    result = saturation.reduce_at(transformed, GF(p))
    require(result[:, :faithful] == reduced and reduced.rank() == dimension, "Incomplete reduced lattice")
    return result, dict(level=level, full_rational_dimension=dimension, faithful_jets=faithful,
                        high_jets=precision, complete_saturation=cert, high_rows_sha256=matrix_digest(result))


def coefficients(poly, n):
    limited = poly.truncate(n).list()
    data = np.zeros(n, dtype=np.uint8)
    if limited:
        data[:len(limited)] = np.fromiter((int(v) for v in limited), dtype=np.uint8, count=len(limited))
    return data


def pack_polys(polys, n):
    return np.stack([coefficients(poly, n) for poly in polys])


def packed_hash(array):
    data = np.ascontiguousarray(array, dtype=np.uint8)
    return digest(dict(shape=[int(i) for i in data.shape], raw_sha256=hashlib.sha256(data.tobytes()).hexdigest()))


def independent(p, rows):
    _, pivots = prime_rref(p, np.ascontiguousarray(rows.T))
    return list(pivots)


def normalized_level_sections(holomorphic, z, junit, degree, genus, length):
    """Construct q^m W_m at the common marked cusp with 1,u in the final pencil."""
    fp = holomorphic.base_ring()
    p = int(fp.characteristic())
    require(z.precision_absolute() >= length and junit.precision_absolute() >= length and
            holomorphic.ncols() >= length, "Missing genuine high weight-two coefficients")
    power = PowerSeriesRing(fp, "q", default_prec=length)
    zp = power([z[i] for i in range(length)]).add_bigoh(length)
    jp = power([junit[i] for i in range(length)]).add_bigoh(length)
    eta = -4*zp**3*jp
    require(zp[0] == -1 and jp[0] == 2 and eta[0] == 8, "Changed actual log differential frame")
    q = power.gen()
    qu = (zp**4 + 18*q**2*zp**2 - 27*q**4)/(8*zp**3)
    require(qu.precision_absolute() >= length and qu[0] == -fp.one()/8, "Wrong q*u")
    ring = PolynomialRing(fp, "qjet")
    Q = ring.gen()
    inv_eta = ring(list((1/eta).add_bigoh(length)))
    qu = ring(list(qu.add_bigoh(length)))
    one = [(ring(row.list()[:length])*inv_eta).truncate(length) for row in holomorphic.rows()]
    require(len(one) == degree + 1 - genus, "Incorrect W1 dimension")
    h2, h3 = 2*degree + 1 - genus, 3*degree + 1 - genus
    n2, n3 = 2*degree + 1, 3*degree + 1
    require(length >= n3, "Missing faithful product jets")
    selected = []
    rows = np.zeros((0, n2), dtype=np.uint8)
    for i in range(len(one)):
        indices = [(i, j) for j in range(i, len(one))]
        additions = pack_polys([(one[i].truncate(n2)*one[j].truncate(n2)).truncate(n2)
                                for _, j in indices], n2)
        candidates = selected + indices
        combined = np.concatenate((rows, additions), axis=0)
        keep = independent(p, combined)
        rows = combined[keep]
        selected = [candidates[k] for k in keep]
        if len(selected) == h2:
            break
    require(len(selected) == h2, "Actual W1 products did not span W2")
    two = [(one[i]*one[j]).truncate(length) for i, j in selected]
    require(np.array_equal(rows, pack_polys(two, n2)), "A selected quadratic product changed")
    all_three = [(Q*row).truncate(length) for row in two] + [(qu*row).truncate(length) for row in two]
    full = pack_polys(all_three, n3)
    ids = independent(p, full)
    require(len(ids) == h3, "W2+uW2 did not span W3")
    cert = dict(full_W1=len(one), full_W2=len(two), full_W3=len(ids),
                W2_recipes_sha256=digest([list(v) for v in selected]),
                W2_faithful_rows_sha256=packed_hash(rows), W3_scalar_recipes_sha256=digest(ids),
                W3_faithful_rows_sha256=packed_hash(full[ids]), actual_log_frame_scalar=-4)
    return dict(ring=ring, one=one, two=two, three=[all_three[i] for i in ids], three_ids=ids,
                two_recipes=selected, z=ring(list(zp)), qu=qu, length=length, certificate=cert)


def original_endpoint_germ(six, index, length):
    """Use real high A,B in physical Artin order, with every common q-zero."""
    require(index in (0, 1) and length == 1483, "Incorrect physical endpoint or G3 window")
    action = six["A"][index]
    constants = six["artin_constants"]["rows"][index]
    embedding = int(action["original_embedding"])
    require(int(constants["artin_index"]) == index == int(action["artin_index"]) and
            int(constants["embedding"]) == embedding == (0, 2)[index] and
            tuple(six["cube_context"]["sigma_a_index"]) == (2, 0, 1), "Changed Artin identity")
    cube = six["cube_context"]
    k = six["constants"]
    codec = cube["original_omega_codec"]
    require(codec.field is k and cube["constants"] is k and codec.omega == six["omega"] and
            int(cube["extended_q_precision"]) >= 2725, "Changed cube coefficient field or precision")
    pair = cube["selected_RP_high_sections"][embedding]
    vnew = constants["vnew"]
    require(vnew == cube["map_context"]["P"][embedding]["vnew"] and vnew == 2*constants["dnew"]**3 and vnew,
            "Changed endpoint scaling")
    power = PowerSeriesRing(k, "q", default_prec=length)
    def value(tag, j):
        a, b = pair[tag]
        return k(a[j]) + codec.omega*k(b[j])
    m = next((j for j in range(613) if value("B", j)), None)
    require(m is not None and m >= 1 and all(not value("A", j) for j in range(m-1)) and value("A", m-1),
            "Incorrect common zero in selected high sections")
    A = power([value("A", j+m-1) for j in range(length)]).add_bigoh(length)
    B = power([value("B", j+m) for j in range(length)]).add_bigoh(length)
    scaled = 2*A/vnew
    qf = (scaled/B + power.gen()).add_bigoh(length)
    require(qf[0] and ((qf-power.gen())*B-scaled).add_bigoh(length) == 0,
            "The selected high A,B do not reproduce the entire germ")
    return qf, dict(original_artin=index, original_embedding=embedding, actual_denominator_order=m,
                    actual_numerator_order=m-1, high_source_coefficients_used=m+length,
                    available_common_verified_prefix=2725, actual_normalized_germ_coefficients=length)

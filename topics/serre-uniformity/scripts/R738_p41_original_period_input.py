#!/usr/bin/env python3
"""Original p41 X_1 Manin cells, integral compact cycles, and intersection form.

All arithmetic is executed only in the public repository GitHub Actions.
No Hodge CM period, quotient rational function, beta, or height is claimed here.
"""
import argparse
from collections import deque
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

from flint import fmpz_mat

P, LEVEL = 41, 246
INDEX, GENUS = 4920, 400
I = (1, 0, 0, 1)
S = (0, -1, 1, 0)
T = (1, 1, 0, 1)
S2 = (0, 1, 1, 0)
T2 = (1, 1, 0, 1)
C2 = (0, 1, 1, 1)
CI2 = (1, 1, 1, 0)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if path.suffix == ".gz":
        data = gzip.compress(data, mtime=0)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)


def mm(a, b, n):
    return ((a[0]*b[0]+a[1]*b[2]) % n,
            (a[0]*b[1]+a[1]*b[3]) % n,
            (a[2]*b[0]+a[3]*b[2]) % n,
            (a[2]*b[1]+a[3]*b[3]) % n)


def mi(a, n):
    det = (a[0]*a[3]-a[1]*a[2]) % n
    inv = pow(det, -1, n)
    return tuple((inv*x) % n for x in (a[3], -a[1], -a[2], a[0]))


def theta_table():
    """The full Brau--Jones GL_2(F_3) -> GL_2(F_2) quotient, kernel Q8."""
    table = {I: I}
    todo = deque([I])
    while todo:
        a = todo.popleft()
        for g, image in ((S, I), (T, C2), ((1, 0, 0, -1), T2)):
            b, v = mm(a, g, 3), mm(table[a], image, 2)
            if b in table:
                assert table[b] == v
            else:
                table[b] = v
                todo.append(b)
    assert len(table) == 48
    assert sum((a[0]*a[3]-a[1]*a[2]) % 3 == 1 for a in table) == 24
    assert sum(v == I for v in table.values()) == 8
    for a in table:
        for b in table:
            assert table[mm(a, b, 3)] == mm(table[a], table[b], 2)
    return table


def conjugate(z):
    a, b = z
    return ((a-b) % P, (-b) % P)


def canon(z):
    z = (z[0] % P, z[1] % P)
    assert z[1]
    return min(z, conjugate(z))


def add(z, w):
    return ((z[0]+w[0]) % P, (z[1]+w[1]) % P)


def scalar(a, z):
    return ((a*z[0]) % P, (a*z[1]) % P)


def zmul(z, w):
    a, b = z
    c, d = w
    return ((a*c-b*d) % P, (a*d+b*c-b*d) % P)


def zinv(z):
    a, b = z
    norm = (a*a-a*b+b*b) % P
    assert norm
    return scalar(pow(norm, -1, P), conjugate(z))


def mobius(matrix, z):
    a, b, c, d = matrix
    return zmul(add(scalar(a, z), (b, 0)),
                zinv(add(scalar(c, z), (d, 0))))


def right_full_matrix(label, matrix, theta):
    a2 = tuple(x % 2 for x in matrix)
    a3 = tuple(x % 3 for x in matrix)
    ap = tuple(x % P for x in matrix)
    k, z = label
    k = mm(mm(mi(theta[a3], 2), k, 2), a2, 2)
    return k, canon(mobius(mi(ap, P), z))


def right_action(label, letter):
    k, z = label
    if letter == "S":
        return (mm(k, S2, 2), canon(scalar(-1, zinv(z))))
    assert letter == "T"
    return (mm(mm(CI2, k, 2), T2, 2), canon((z[0]-1, z[1])))


def label_of_matrix(a, theta):
    a2, a3 = tuple(x % 2 for x in a), tuple(x % 3 for x in a)
    k = mm(mi(theta[a3], 2), a2, 2)
    z = canon(mobius(mi(tuple(x % P for x in a), P), (0, 1)))
    return k, z


def cycles(perm):
    used, out = set(), []
    for start in range(len(perm)):
        if start in used:
            continue
        cyc = []
        cur = start
        while cur not in used:
            used.add(cur)
            cyc.append(cur)
            cur = perm[cur]
        assert cur == start
        out.append(cyc)
    return out


def cycle_lookup(parts, count):
    result = [-1]*count
    for j, part in enumerate(parts):
        for a in part:
            assert result[a] == -1
            result[a] = j
    assert min(result) >= 0
    return result


def iterate(perm, i, n):
    for _ in range(n):
        i = perm[i]
    return i


def egcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a//b, b, a % b
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0-q*y1
    return a, x0, y0


def integral_lift(a):
    """A bounded SL_2(Z) matrix in the same full LEVEL congruence class."""
    a0, b0, c0, d0 = a
    if a == I:
        return I
    c = c0 if c0 else LEVEL
    d = d0
    while math.gcd(c, d) != 1:
        d += LEVEL
    gcd, aa, minus_b = egcd(d, c)
    assert gcd == 1
    bb = -minus_b
    gcd, u, v = egcd(c, d)
    assert gcd == 1
    k = (u*(a0-aa)+v*(b0-bb)) % LEVEL
    if k > LEVEL//2:
        k -= LEVEL
    aa, bb = aa+k*c, bb+k*d
    result = (aa, bb, c, d)
    assert aa*d-bb*c == 1
    assert tuple(x % LEVEL for x in result) == a
    return result


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1]*n

    def root(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def join(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.p[y] = x
        self.size[x] += self.size[y]
        return True


def spanning_tree(vertices, oriented_edges):
    uf = UnionFind(vertices)
    tree = []
    for edge, u, v in oriented_edges:
        if uf.join(u, v):
            tree.append(edge)
    assert len(tree) == vertices-1
    return tree


def tree_path(adjacency, start, target):
    parent = {start: None}
    todo = deque([start])
    while target not in parent:
        u = todo.popleft()
        for v, edge, sign in adjacency[u]:
            if v not in parent:
                parent[v] = (u, edge, sign)
                todo.append(v)
    terms = []
    at = target
    while at != start:
        before, edge, sign = parent[at]
        terms.append((edge, sign))
        at = before
    terms.reverse()
    return terms


def compute(out):
    out.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    theta = theta_table()
    base = (I, canon((0, 1)))
    labels = [base]
    residues = [I]
    index = {base: 0}
    todo = deque([0])
    transitions = {}
    while todo:
        i = todo.popleft()
        for letter, matrix in (("S", S), ("T", T)):
            dest = right_action(labels[i], letter)
            residue = mm(residues[i], matrix, LEVEL)
            if dest not in index:
                index[dest] = len(labels)
                labels.append(dest)
                residues.append(residue)
                todo.append(index[dest])
            transitions[(i, letter)] = index[dest]
    assert len(labels) == INDEX
    assert all(label_of_matrix(a, theta) == label for a, label in zip(residues, labels))
    ss = [transitions[(i, "S")] for i in range(INDEX)]
    tt = [transitions[(i, "T")] for i in range(INDEX)]
    rr = [tt[ss[i]] for i in range(INDEX)]  # R=S*T, right cosets
    assert all(ss[ss[i]] == i for i in range(INDEX))
    assert all(rr[rr[rr[i]]] == i for i in range(INDEX))
    assert sorted(ss) == sorted(rr) == sorted(tt) == list(range(INDEX))
    s_orbits, r_orbits, cusps = cycles(ss), cycles(rr), cycles(tt)
    assert all(len(c) == 2 for c in s_orbits)
    assert sum(len(c) == 1 for c in r_orbits) == 3
    assert all(len(c) in (1, 3) for c in r_orbits)
    assert len(cusps) == 20 and all(len(c) == LEVEL for c in cusps)
    e2, e3 = 0, 3
    assert 12+INDEX-3*e2-4*e3-6*len(cusps) == 12*GENUS
    rv = cycle_lookup(r_orbits, INDEX)
    cv = cycle_lookup(cusps, INDEX)
    edges = []
    edge_of = [-1]*INDEX
    for part in s_orbits:
        positive, negative = min(part), max(part)
        edge = len(edges)
        edges.append((positive, negative))
        edge_of[positive] = edge_of[negative] = edge
    assert len(edges) == 2460 and len(r_orbits) == 1642
    lifts = [integral_lift(a) for a in residues]
    # Arithmetic real structure, with the same (zeta,1) period basis.
    # The reference coset I is NOT the original real point a=1.
    conjugation_matrix = (-1, -1, 0, 1)
    cc = [index[right_full_matrix(label, conjugation_matrix, theta)]
          for label in labels]
    assert all(cc[cc[i]] == i for i in range(INDEX))
    assert all(cc[rr[i]] == rr[rr[cc[i]]] for i in range(INDEX))
    real_fixed = [i for i in range(INDEX) if rr[i] == i and cc[i] == i]
    c1 = index[(C2, canon((0, 1)))]
    assert real_fixed == [c1]
    marked_c1_lift = (15130, 123, 123, 1)
    assert marked_c1_lift[0]*marked_c1_lift[3] - marked_c1_lift[1]*marked_c1_lift[2] == 1
    assert label_of_matrix(tuple(x % LEVEL for x in marked_c1_lift), theta) == labels[c1]
    assert rr[c1] == c1
    c0_label = (S2, canon((0, 1)))
    c0 = index[c0_label]
    c0_orbit = [c0, rr[c0], rr[rr[c0]]]
    assert len(set(c0_orbit)) == 3
    deck = [iterate(tt, i, 2*P) for i in range(INDEX)]
    assert all(deck[deck[deck[i]]] == i for i in range(INDEX))
    assert all(deck[ss[i]] == ss[deck[i]] and deck[tt[i]] == tt[deck[i]]
               for i in range(INDEX))
    assert all(cc[deck[i]] == deck[deck[cc[i]]] for i in range(INDEX))
    c1_deck = [c1, deck[c1], deck[deck[c1]]]
    assert len(set(c1_deck)) == 3
    assert all(rr[i] == i for i in c1_deck)
    assert set(c1_deck) == {c[0] for c in r_orbits if len(c) == 1}
    assert {deck[i] for i in c0_orbit} == set(c0_orbit)
    assert {cc[i] for i in c0_orbit} == set(c0_orbit)
    save(out/"original-cosets-and-markings.json.gz", {
        "p": P, "level": LEVEL, "index": INDEX, "genus": GENUS,
        "labels": [{"tame_k": k, "CM_pair_representative": z} for k, z in labels],
        "SL2_residues": residues,
        "SL2Z_lifts": [[str(x) for x in a] for a in lifts],
        "S": ss, "R": rr, "T": tt, "cusps": cusps,
        "tame_theta_GL2F3": [{"matrix": a, "image": v} for a, v in sorted(theta.items())],
        "c1": {"coset": c1, "elliptic_parameter": "tau=g_star(zeta)",
               "marked_SL2Z_representative": marked_c1_lift,
               "a": "1", "p_pair": [[0, 1], [40, 40]],
               "unique_real_R_fixed_point": True},
        "complex_conjugation": {"matrix": conjugation_matrix,
                               "period_basis": ["zeta", "1"],
                               "permutation_on_CM_cosets": cc},
        "c1_deck_orbit": [{"coset": a, "a": name}
                         for a, name in zip(c1_deck, ["1", "zeta", "zeta^2"])],
        "c0": {"cosets": c0_orbit, "a": "0", "ramification_at_j0": 3},
        "deck": {"matrix": [1, 2*P, 0, 1], "action": "a -> zeta*a",
                 "permutation": deck},
    })
    # Saturated Manin relations are the graph coboundaries of R-orbits.
    primal_tree = spanning_tree(len(r_orbits),
        [(e, rv[h], rv[k]) for e, (h, k) in enumerate(edges)])
    primal_set = set(primal_tree)
    relative_edges = [e for e in range(len(edges)) if e not in primal_set]
    assert len(relative_edges) == 819
    # Boundary of {g0,g infinity} is cusp(g)-cusp(gS).
    boundary_edges = [(e, cv[edges[e][1]], cv[edges[e][0]]) for e in relative_edges]
    dual_tree = spanning_tree(len(cusps), boundary_edges)
    dual_set = set(dual_tree)
    remaining = [e for e in relative_edges if e not in dual_set]
    assert len(remaining) == 2*GENUS
    adjacency = [[] for _ in cusps]
    for edge, u, v in boundary_edges:
        if edge in dual_set:
            adjacency[u].append((v, edge, 1))
            adjacency[v].append((u, edge, -1))
    compact = []
    for edge in remaining:
        h, k = edges[edge]
        u, v = cv[k], cv[h]
        terms = [(edge, 1)] + tree_path(adjacency, v, u)
        boundary = [0]*len(cusps)
        for e, coefficient in terms:
            a, b = edges[e]
            boundary[cv[a]] += coefficient
            boundary[cv[b]] -= coefficient
        assert not any(boundary)
        assert all(e in relative_edges for e, _ in terms)
        assert [(e, c) for e, c in terms if e in remaining] == [(edge, 1)]
        compact.append(terms)
    # Contract the primal tree and join the cusp faces along the dual tree.
    faces = {j: [h for h in part if edge_of[h] not in primal_set]
             for j, part in enumerate(cusps)}
    assert all(faces.values())
    for edge in dual_tree:
        h, k = edges[edge]
        fa = next(j for j, word in faces.items() if h in word)
        fb = next(j for j, word in faces.items() if k in word)
        assert fa != fb
        a, b = faces[fa], faces[fb]
        ia, ib = a.index(h), b.index(k)
        joined = a[ia+1:]+a[:ia]+b[ib+1:]+b[:ib]
        del faces[fa]
        del faces[fb]
        faces[min(fa, fb)] = joined
    assert len(faces) == 1
    word = next(iter(faces.values()))
    assert len(word) == 4*GENUS
    rem_index = {e: j for j, e in enumerate(remaining)}
    polygon = [(rem_index[edge_of[h]], 1 if h == edges[edge_of[h]][0] else -1)
               for h in word]
    assert all(sorted(sign for j, sign in polygon if j == i) == [-1, 1]
               for i in range(2*GENUS))
    # Antisymmetric polygon cup product, with positive cusp T orientation.
    rank = 2*GENUS
    twice = [[0]*rank for _ in range(rank)]
    prefix = [0]*rank
    for j, sign in polygon:
        for i, value in enumerate(prefix):
            if value:
                twice[i][j] += value*sign
                twice[j][i] -= value*sign
        prefix[j] += sign
    assert not any(prefix)
    assert all(v % 2 == 0 for row in twice for v in row)
    omega = [[v//2 for v in row] for row in twice]
    assert all(omega[i][j] == -omega[j][i] for i in range(rank) for j in range(rank))
    # Preserve the exact chain and matrix before the final determinant check.
    cycle_data = {
        "p": P, "level": LEVEL, "genus": GENUS,
        "edge_positive_negative_cosets": edges,
        "R_orbits": r_orbits, "primal_tree_edges": primal_tree,
        "relative_basis_edges": relative_edges, "dual_tree_edges": dual_tree,
        "compact_basis_leading_edges": remaining,
        "compact_cycles_in_oriented_Manin_edges": compact,
        "one_face_polygon": polygon,
        "intersection_matrix": omega,
        "intersection_determinant": None,
        "orientation": "positive cusp loop T; Manin edge {g0,g infinity}",
    }
    save(out/"integral-compact-Manin-cycles.json.gz", cycle_data)
    determinant = fmpz_mat(omega).det()
    cycle_data["intersection_determinant"] = str(determinant)
    save(out/"integral-compact-Manin-cycles.json.gz", cycle_data)
    assert determinant == 1
    files = [{"file": name, "bytes": (out/name).stat().st_size, "sha256": sha(out/name)}
             for name in ("original-cosets-and-markings.json.gz",
                          "integral-compact-Manin-cycles.json.gz")]
    cert = {
        "result": "R738-p41-original-period-input", "complete": True,
        "p": P, "level": LEVEL, "index": INDEX, "genus": GENUS,
        "elliptic_order2_fixed": e2, "elliptic_order3_fixed": e3,
        "cusps": len(cusps), "cusp_widths": [len(c) for c in cusps],
        "relative_rank": len(relative_edges), "compact_rank": len(compact),
        "intersection_determinant": str(determinant),
        "c1_coset": c1, "c0_cosets": c0_orbit, "c1_deck_cosets": c1_deck,
        "c0_a": "0", "c1_deck_a": ["1", "zeta", "zeta^2"],
        "theta_kernel_order": 8, "deck_translation": 82,
        "c1_unique_real_R_fixed": True, "marked_c1_SL2Z": marked_c1_lift,
        "complex_conjugation_matrix": conjugation_matrix,
        "c0_real_orbit": True,
        "all_SL2Z_lifts_verified": True, "all_compact_boundaries_zero": True,
        "Hodge_period_or_map_or_beta_computed": False,
        "source_sha256": sha(__file__), "files": files,
        "seconds": time.monotonic()-started,
    }
    save(out/"p41-original-period-input-certificate.json", cert)
    save(out/"core-receipt.json", {
        "result": cert["result"], "complete": True, "p": P,
        "certificate_sha256": sha(out/"p41-original-period-input-certificate.json"),
        "source_sha256": sha(__file__),
        "Hodge_period_or_map_or_beta_computed": False,
    })
    return cert


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Exact task computation is restricted to the public repository Actions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        result = compute(args.output)
        print(json.dumps({"complete": True, "p": P, "genus": GENUS,
                          "compact_rank": result["compact_rank"],
                          "seconds": result["seconds"]}), flush=True)
        return 0
    except BaseException as error:
        save(args.output/"core-receipt.json", {
            "result": "R738-p41-original-period-input", "complete": False,
            "p": P, "source_sha256": sha(__file__),
            "error": type(error).__name__ + ": " + str(error),
            "Hodge_period_or_map_or_beta_computed": False})
        raise


if __name__ == "__main__":
    sys.exit(main())

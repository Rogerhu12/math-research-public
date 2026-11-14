#!/usr/bin/env python3
"""Independent exact eight-row and quaternion-algebra audit; no surface data.

The author's rotation implementation is not imported. Axis centers are
constructed directly; general identities are checked as integer polynomials
using Hamilton multiplication. Coverage remains a proved universal lemma.
"""
import argparse
from fractions import Fraction as F
import hashlib
from itertools import permutations
import json
from pathlib import Path

T = Path(__file__).resolve().parent.parent
N = T / 'notes'
P = '2026-11-09-db6f-'
PINS = {
    N/(P+'prefix-euclidean-support-lower-bound.md'):
        'b6df2b1b46542d20ef0198293efe6b98389dc758a52cba9ed50dd6d3ca9780e6',
    N/(P+'prefix-euclidean-support-fixed-cap-scope.md'):
        '0496aa18c4c9b9fdceb014b57628db17c38e6965504b1bfe49ae748d641e4f86',
    T/'scripts/db6f-prefix-euclidean-support-toy-certificate.py':
        '8c0207a9974829fee227eada20ac4977824d52e50ef2779ec8470e10cd1e3305',
    N/(P+'prefix-euclidean-support-toy-certificate.json'):
        '5b5b3b8a6de37bde6c7132ea58791777c6275446884382f516b780b65c9e5793',
    N/(P+'prefix-euclidean-support-publication.json'):
        '7f2208cbaca10d5ca220c877b7c886c95806a956be882f4414aab37597b88d3e',
}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def item(p):
    p = Path(p).resolve()
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def det3(matrix):
    answer = F(0)
    for perm in permutations(range(3)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        answer += sign*matrix[0][perm[0]]*matrix[1][perm[1]]*matrix[2][perm[2]]
    return answer


# Eight-variable integer polynomial arithmetic, with exact zero cancellation.
Z = (0,)*8


def const(c):
    return {Z: c} if c else {}


def var(i):
    e = [0]*8
    e[i] = 1
    return {tuple(e): 1}


def add(*args):
    out = {}
    for a in args:
        for e, c in a.items():
            out[e] = out.get(e, 0)+c
    return {e: c for e, c in out.items() if c}


def scale(a, c):
    return {e: c*v for e, v in a.items() if c*v}


def mul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            ef = tuple(x+y for x, y in zip(e, f))
            out[ef] = out.get(ef, 0)+c*d
    return {e: c for e, c in out.items() if c}


def hamilton(a, b):
    return [
        add(mul(a[0], b[0]), *(scale(mul(a[i], b[i]), -1) for i in range(1,4))),
        add(mul(a[0], b[1]), mul(a[1], b[0]), mul(a[2], b[3]), scale(mul(a[3], b[2]), -1)),
        add(mul(a[0], b[2]), scale(mul(a[1], b[3]), -1), mul(a[2], b[0]), mul(a[3], b[1])),
        add(mul(a[0], b[3]), mul(a[1], b[2]), scale(mul(a[2], b[1]), -1), mul(a[3], b[0])),
    ]


def conj(q):
    return [q[0]]+[scale(a, -1) for a in q[1:]]


def norm(q):
    return add(*(mul(a, a) for a in q))


def action(q):
    columns = []
    for j in range(3):
        unit = [const(0)]+[const(int(i == j)) for i in range(3)]
        column = hamilton(hamilton(q, unit), conj(q))
        assert column[0] == {}
        columns.append(column[1:])
    return [[columns[j][i] for j in range(3)] for i in range(3)]


def pmul(a, b):
    return [[add(*(mul(a[i][k], b[k][j]) for k in range(3)))
             for j in range(3)] for i in range(3)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def exact_algebra():
    q = [var(i) for i in range(4)]
    p = [var(i+4) for i in range(4)]
    rq, rp = action(q), action(p)
    nq, np = norm(q), norm(p)
    checks = []

    def equal(a, b, label):
        assert a == b, label
        checks.append(label)

    # Each basis-vector Hamilton conjugation equals the manuscript formula.
    for i in range(3):
        for j in range(3):
            # v cross e_j, using the alternating determinant of standard axes.
            cross = {}
            for k in range(3):
                axes = (i, k, j)
                if len(set(axes)) == 3:
                    sign = (-1)**sum(axes[a] > axes[b] for a in range(3) for b in range(a+1,3))
                    cross = add(cross, scale(q[k+1], sign))
            form = add(scale(add(mul(q[0], q[0]), scale(add(*(mul(v,v) for v in q[1:])), -1)), int(i == j)),
                       scale(mul(q[i+1], q[j+1]), 2), scale(mul(q[0], cross), 2))
            equal(rq[i][j], form, f'action_formula_{i}{j}')
    gram = pmul(transpose(rq), rq)
    for i in range(3):
        for j in range(3):
            equal(gram[i][j], scale(mul(nq,nq), int(i == j)), f'orthogonality_{i}{j}')
    determinant = {}
    for perm in permutations(range(3)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(3) for j in range(i+1,3))
        determinant = add(determinant, scale(mul(mul(rq[0][perm[0]],rq[1][perm[1]]),rq[2][perm[2]]), sign))
    equal(determinant, mul(mul(nq,nq),nq), 'determinant_norm_cubed')
    pq = hamilton(p,q)
    equal(norm(pq), mul(np,nq), 'quaternion_norm_multiplicativity')
    composed, combined = pmul(rp,rq), action(pq)
    for i in range(3):
        for j in range(3):
            equal(composed[i][j],combined[i][j],f'composition_{i}{j}')
    relative = hamilton(conj(p),q)
    equal(relative[0],add(*(mul(p[i],q[i]) for i in range(4))), 'relative_scalar_dot')
    equal(add(*(rq[i][i] for i in range(3))), add(scale(mul(q[0],q[0]),4),scale(nq,-1)), 'trace_formula')
    conjugate_action = action(conj(q))
    for i in range(3):
        for j in range(3):
            equal(conjugate_action[i][j],rq[j][i],f'conjugate_transpose_{i}{j}')
    return checks


def run(replay):
    bound = {}

    def verify(p, expected=None):
        actual = item(p)
        if isinstance(expected, str):
            assert actual['sha256'] == expected
        elif expected is not None:
            assert actual == expected
        bound[actual['path']] = actual
        return actual

    for p,h in PINS.items():
        verify(p,h)
    publication=json.loads((N/(P+'prefix-euclidean-support-publication.json')).read_text())
    for b in publication['files']:
        verify(b['path'],b)
    verify(publication['earlier_inventory_preserved']['path'], publication['earlier_inventory_preserved'])
    ledger=json.loads((N/(P+'prefix-euclidean-support-lower-bound-sources.json')).read_text())
    for b in ledger['files']:
        verify(b['path'],b)
    source=N/(P+'prefix-euclidean-support-toy-certificate.json')
    report=json.loads(source.read_text())
    verify(replay,PINS[source])
    assert Path(replay).read_bytes() == source.read_bytes()
    for b in report['source_bindings']:
        verify(b['path'],b)

    decode_vector=lambda u: [F(x) for x in u]
    decode_matrix=lambda a: [decode_vector(row) for row in a]
    set0=[decode_vector(p) for p in report['sets']['S0']]
    set1=[decode_vector(p) for p in report['sets']['S1']]
    assert set(map(tuple,set0)) == {(F(-3),F(0),F(0)),(F(3),F(0),F(0))}
    assert set(map(tuple,set1)) == {(F(-1),F(0),F(0)),(F(1),F(0),F(0))}
    assert F(report['enclosing_radius_S1']) == 1
    assert all(dot(p,p) <= 1 for p in set1)
    assert F(report['coverage']['operator_distance_squared_upper']) == 3
    assert F(report['coverage']['declared_operator_radius_upper']) == F(7,4)
    assert F(3)<F(7,4)**2
    rows=report['rows'];assert len(rows)==8
    seen=set();summaries=[]
    for row in rows:
        j,branch=row['quaternion_axis_index'],row['branch']
        assert type(j) is int and 0<=j<4 and branch in ('proper','reflected')
        assert (j,branch) not in seen;seen.add((j,branch))
        # Derive these eight centers directly from rotations by pi about axes.
        diagonal=[F(1 if j==0 or j==i+1 else -1) for i in range(3)]
        if branch=='reflected':diagonal[0]*=-1
        matrix=[[diagonal[i] if i==k else F(0) for k in range(3)] for i in range(3)]
        assert decode_matrix(row['rotation_center'])==matrix
        assert det3(matrix)==(1 if branch=='proper' else -1)
        assert all(sum(matrix[k][i]*matrix[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
        u=[decode_vector(x) for x in row['directions']];w=decode_vector(row['weights'])
        assert len(u)==len(w)==2 and all(dot(x,x)==1 for x in u)
        assert sum(map(abs,w))==1 and all(sum(wi*x[k] for wi,x in zip(w,u))==0 for k in range(3))
        h0=[max(dot(x,d) for x in set0) for d in u]
        h1=[max(dot(x,[sum(matrix[i][k]*d[i] for i in range(3)) for k in range(3)]) for x in set1) for d in u]
        assert h0==decode_vector(row['support0_exact']) and h1==decode_vector(row['support1_exact'])
        L=sum(wi*(a-b) for wi,a,b in zip(w,h0,h1))
        rho,target=F(row['cell_radius_upper']),F(row['target'])
        lower=L-rho; margin=lower-target
        assert (L,rho,target,lower,margin)==(F(2),F(7,4),F(1,5),F(1,4),F(1,20))
        assert F(row['balanced_center_gap_lower'])==L
        assert F(row['whole_cell_distance_lower'])==lower
        assert F(row['strict_margin'])==margin
        summaries.append({'cell':j,'branch':branch,'lower':'1/4','margin':'1/20'})
    assert seen=={(j,b) for j in range(4) for b in ('proper','reflected')}
    tri=report['c3_fixed_orientation_witness']
    u=[decode_vector(v) for v in tri['directions']];w=decode_vector(tri['weights'])
    assert all(dot(v,v)==1 for v in u) and sum(map(abs,w))==1
    assert all(sum(wi*v[k] for wi,v in zip(w,u))==0 for k in range(3))
    coefficient=2*sum(wi*(4*v[0]**3-3*v[0]) for wi,v in zip(w,u))
    assert coefficient==F(32,25)==F(tri['support_gap_coefficient_multiplying_q'])
    assert tri['quotient_lower_bound_asserted'] is False
    assert F(report['certified_minimum_over_E3_lower'])==F(1,4)
    assert F(report['minimum_strict_margin'])==F(1,20)
    assert F(report['declared_target'])==F(1,5)
    assert F(report['analytic_exact_minimum_with_separate_identity_upper_bound'])==2

    algebra=exact_algebra()
    return {'status':'PASS_INDEPENDENT_EXACT_TOY_AND_QUATERNION_IDENTITIES',
            'script':item(Path(__file__)), 'verified_sources':[bound[k] for k in sorted(bound)],
            'bound_file_count':len(bound),'author_replay_byte_identical':True,
            'eight_distinct_cells_and_branches_checked':True,'row_checks':summaries,
            'integer_polynomial_identities':algebra,'polynomial_identity_count':len(algebra),
            'fixed_orientation_C3_coefficient':'32/25',
            'coverage_scope':'Universal sphere/grid and four-cell coverage is proved in the independent written review, not inferred from row sampling.',
            'actual_surface_files_read':False,'actual_support_optimization_calls':0,
            'root_RK_prefix_tail_solver_calls':0,
            'current_candidate_metric_or_source_changed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();report=run(args.replay)
    data=(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()
    assert len(data)<100000
    with args.out.open('xb') as f:f.write(data)
    args.out.chmod(0o444)
    print(json.dumps({'status':report['status'],'rows':8,'algebra_identities':report['polynomial_identity_count'],
                      'bound_files':report['bound_file_count'],'bytes':len(data),'sha256':sha(args.out),'solver_calls':0}))


if __name__=='__main__':main()

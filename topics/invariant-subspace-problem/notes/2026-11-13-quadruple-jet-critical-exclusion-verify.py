"""Exact original-kernel certificate for the quadruple-jet exclusion.

The two exact maximal minors have degree at most 40. Their integer factorizations
are established at 41 distinct integer points. A full-degree mod-103 Bezout
identity then proves that their residual factors are coprime over C.
Standard library only; the preceding published pencil certificate supplies K,
its exact inverse, the ten quadratic relations and finite-field arithmetic.
"""
from pathlib import Path
import json
import runpy

OLD = runpy.run_path(str(Path(__file__).with_name(
    '2026-11-13-four-jet-projected-quadric-pencil-verify.py')))
K, C, BASIS = OLD['K'], OLD['C'], OLD['basis']
P = 103
DATA = {'residuals': [[11986389602559590400, -57626861021712875520, 96938862963673006080, -34590467871008096256, -87905658834864046080, 94625238635941724160, 17008200640044728320, -65395673421512704000, 10813689891631923200, 26540659217665228800, -8900987020010127360, -7395497941685207040, 3163515536389816320, 1598841379326697472, -703899734216888320, -289711490181396480, 104213199947934720, 44207201908257280, -9588766021203200, -5271824808163200, 348546399180800, 430594738073600, 28838629716000, -18860286462000, -3828564970000, 89207382500, 115579306250, 16774634375, 1188650000, 48609375, 1125000], [453605240025907200, -1919792721376051200, 2623949420542033920, -159017422144143360, -2700469818393362432, 1711683677496279040, 851370681974128640, -1001732853145272320, -101194397649469440, 268196286683152384, 12859877088952320, -30425546241474560, -9102747666350080, -5245724627845120, 3013850888560640, 3336395779072000, -279499167129600, -787829677619200, -80379446732800, 98772459296000, 27122501584000, -4488661504000, -3043994160000, -327917700000, 89726450000, 32739575000, 4480125000, 300781250, 8203125]], 'bezout_u': [49, 102, 23, 76, 36, 101, 88, 13, 89, 77, 30, 63, 86, 90, 47, 14, 95, 4, 99, 29, 101, 83, 88, 0, 15, 4, 91, 49], 'bezout_v': [80, 30, 47, 68, 95, 30, 15, 73, 89, 102, 23, 20, 95, 97, 52, 35, 86, 13, 22, 20, 58, 31, 97, 86, 101, 42, 24, 88, 96, 18], 'null_vectors': [[0, 0, 0, 0, 11664, -5400, 1080, -1755, 135, 100], [80, -16, 20, 0, -36, 20, 0, 5, 0, 0]]}

def original_matrix(g):
    L = [list(g)+[0], [0]+list(g)]
    B = [[sum(C[i][j]*L[a][j] for j in range(6))
          for a in range(2)] for i in range(6)]
    return [[sum(A[i][j]*B[j][a] for j in range(6))
             for A in BASIS] for a in range(2) for i in range(6)]

def det_integer(A):
    A = [list(row) for row in A]
    n = len(A); sign = 1; previous = 1
    for k in range(n-1):
        pivot = next((i for i in range(k,n) if A[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        b = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = b*A[i][j] - A[i][k]*A[k][j]
                assert num % previous == 0
                A[i][j] = num // previous
            A[i][k] = 0
        previous = b
    return sign*A[-1][-1]

def value(a,x):
    v=0
    for c in reversed(a):
        v=v*x+c
    return v

def rank_mod(A):
    A=[[x%P for x in row] for row in A]
    rank=0
    for j in range(len(A[0])):
        k=next((i for i in range(rank,len(A)) if A[i][j]),None)
        if k is None:
            continue
        A[k],A[rank]=A[rank],A[k]
        b=pow(A[rank][j],-1,P)
        A[rank]=[b*x%P for x in A[rank]]
        for i in range(rank+1,len(A)):
            b=A[i][j]
            A[i]=[(x-b*y)%P for x,y in zip(A[i],A[rank])]
        rank+=1
    return rank

def verify():
    factors=DATA['residuals']
    assert [len(a)-1 for a in factors]==[30,28]
    assert [a[-1]%P for a in factors]==[34,102]
    constants=[67108864000000000,20971520000000000]
    powers=[7,6]
    omissions=[(10,11),(8,9)]
    # 41 exact evaluations certify the entire degree-at-most-40 identities.
    for s in range(41):
        M=original_matrix([s**4,-4*s**3,6*s*s,-4*s,1])
        for a,c,p,om in zip(factors,constants,powers,omissions):
            actual=det_integer([row for i,row in enumerate(M) if i not in om])
            assert actual == c*s**p*value(a,s)
    fm=[[x%P for x in a] for a in factors]
    total=OLD['add'](OLD['mul'](DATA['bezout_u'],fm[0]),
                     OLD['mul'](DATA['bezout_v'],fm[1]))
    assert total==[1]
    endpoint_ranks=[]
    for g,n in zip([[0,0,0,0,1],[1,0,0,0,0]],DATA['null_vectors']):
        M=original_matrix(g)
        assert all(sum(x*y for x,y in zip(row,n))==0 for row in M)
        endpoint_ranks.append(rank_mod(M))
    assert endpoint_ranks==[9,9]
    polars_zero=[K[j] for j in range(4)]
    polars_infinity=[list(reversed(K[5-j])) for j in range(4)]
    orders=[[next(i for i,c in enumerate(a) if c) for a in polar]
            for polar in [polars_zero,polars_infinity]]
    assert orders==[[4,3,2,1],[4,3,2,1]]
    assert polars_zero[3][1]==-32 and polars_infinity[3][1]==5
    return dict(all_pass=True,degree_bound=40,exact_integer_nodes=list(range(41)),
        omitted_zero_based_rows=omissions,scalar_factors=constants,
        removed_powers_of_s=powers,residual_coefficients_ascending=factors,
        residual_mod103_coefficients_ascending=fm,
        residual_degrees=[30,28],residual_leading_coefficients_mod103=[34,102],
        bezout_u=DATA['bezout_u'],bezout_v=DATA['bezout_v'],bezout_sum=[1],
        exact_endpoint_null_vectors=DATA['null_vectors'],endpoint_ranks=endpoint_ranks,
        physical_polars_at_zero_ascending=polars_zero,
        physical_polars_at_infinity_ascending=polars_infinity,contact_orders=orders,
        scope='The original quadruple-jet quadric locus consists exactly of 0 and infinity. Both are excluded from the full-H-rank, outer-mean, nonsecant, essential-three original complete cubic critical section. Other support multiplicities and rank-drop strata remain open.')

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))

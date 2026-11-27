#!/usr/bin/env python3
"""R1037: complete original degree378 CM decomposition after division by B12.

Run only in the named public Actions repository. Rebuilds only the necessary
two degree390 matrices before either source is used. No old source suite or
unrelated old kernel is rerun. No generated coefficient file
is read or written. All new CM operators use all 64 columns and 66 entire fibers.
The small rational point counts at 13,19,31 are identification diagnostics, not
a rank proof or a scan of the target prime p.
"""
from __future__ import annotations
import argparse
import concurrent.futures
from functools import lru_cache
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import multiprocessing
import os
from pathlib import Path
import sys
import time
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "topics/rank2-sha-infinitely-many-p/"
N, SIZE = 378, 64
START = time.monotonic()
H = None
D19 = None
FIXED_PINS = {
    "check-r480-actual-input-cm19.py":
        "3d4d9a05872cdde0f24ff756ec79407417afa943eabf6f71f4e48d32f91f9c45",
    "check-r466-fixed-two-division-source.py":
        "effd6f1526421cfcb9da3bd7769eed258374fa0addf337313d0315cb3ef08245",
    "check-r464-degree102-cm7-exact.py":
        "b3e11a9da1b28a7623d86acf944262ab23c2d1969b1f0183030a4d1c96b5f1ff",
}
SOURCE_DECLARATIONS = [
    ("F378_A_from_Psi35", 3, 5,
     "4485e52f18d5349f8158e0d2177d38b6ae5c5b5862089ea66ab6e4cf4546bcb0"),
    ("F378_B_from_Psi53", 5, 3,
     "dd354f3138dff257035c02561acef381470829b66fdb712801cb08455442fbe1"),
]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    sys.modules[name] = out
    spec.loader.exec_module(out)
    return out


def enc(x):
    return [str(x[0]), str(x[1])]


def pair(A):
    return A, Mat(A.nrows(), A.ncols())


def mh(A):
    return digest(H["serialize_matrix"](A))


def conjugate(A):
    return A[0], -A[1]


def real_rank(A):
    assert A[1] == Mat(A[0].nrows(), A[0].ncols())
    return A[0].rank()


def projector_rank(P):
    assert H["km"](P, P) == P
    assert P[1] == Mat(P[0].nrows(), P[0].ncols())
    tr = sum(P[0][i, i] for i in range(P[0].nrows()))
    rank = int(tr)
    assert tr == rank and 0 <= rank <= P[0].nrows()
    return rank


def powers(A, period):
    out = [H["identity"](A[0].nrows())]
    for _ in range(period):
        out.append(H["km"](out[-1], A))
    assert out[-1] == out[0]
    return out


def eig_project(pows, eigenvalue):
    period = len(pows)-1
    out = H["kzero"](pows[0][0].nrows(), pows[0][0].ncols())
    for j in range(period):
        out = H["ka"](out, H["ks"](pows[j], H["fp"](eigenvalue, -j)))
    out = H["ks"](out, H["fq"](Q(1, period)))
    assert H["km"](pows[1], out) == H["ks"](out, eigenvalue)
    projector_rank(out)
    return out


def scalar_identity(A):
    val = H["get_entry"](A, 0, 0)
    assert A == H["ks"](H["identity"](A[0].nrows()), val)
    return val


@lru_cache(None)
def sigma_division(norm):
    """Entire sigma quotient, determined in its proved finite divisor space."""
    fq, fa, fs, fm, fp = (H[k] for k in ("fq", "fa", "fs", "fm", "fp"))
    gamma = {7: fq(Q(5,2),Q(1,2)), 13: fq(Q(7,2),Q(1,2)),
             19: fq(4,1), 31: fq(Q(11,2),Q(1,2))}[norm]
    zero, one = fq(0), fq(1)
    degree = (norm-1)//2
    assert degree % 3 == 0
    length = degree//3+1
    W = [Q(1), Q(-1,7)]+[Q(0)]*max(0,length-2)
    W = W[:length]
    for n in range(2,length):
        W[n] = sum(W[i]*W[n-i] for i in range(1,n))/((6*n+1)*(n-1))
    logs = [zero]+[
        fm(fq(-W[k]/(6*k*(6*k-1))), fs(fp(gamma,6*k),fq(norm)))
        for k in range(1,length)]
    exponential = [one]
    for n in range(1,length):
        val = zero
        for k in range(1,n+1):
            val = fa(val, fm(fq(k),fm(logs[k],exponential[n-k])))
        exponential.append(fm(val,fq(Q(1,n))))
    B = Poly(W)
    c = [zero]*length
    for k in range(length):
        val = exponential[k]
        for j in range(k):
            val = fs(val, fm(c[j],fq((B**(degree-3*j))[k-j])))
        c[k] = val
    q = [zero]*(degree+1)
    for j in range(length):
        q[degree-3*j] = c[j]
    assert q[-1] == one
    if norm == 7:
        assert q == [fq(Q(-2,7),Q(6,7)),zero,zero,one]
    if norm == 13:
        assert q == [fq(Q(40,13),Q(24,13)),zero,zero,
                     fq(2,6),zero,zero,one]
    if norm == 19:
        assert (gamma,q) == H["q19_polynomial"]()
    numerator = H["qmap"](q,norm)
    assert len(numerator) == norm+1 and numerator[-1] == one
    assert all(v == zero for i,v in enumerate(numerator) if i%3 != 1)
    return gamma,q,numerator


def native_full_fiber(norm, degree, offset, target):
    """Original Q(delta) entire-fiber algorithm; no root or column omitted."""
    fq, fa, fn, fs, fm, fi, fp = (
        H[k] for k in ("fq","fa","fn","fs","fm","fi","fp"))
    pa, ps, pm, pd, ptrim = (H[k] for k in ("pa","ps","pm","pd","ptrim"))
    zero,one = fq(0),fq(1)
    J = (degree-2*offset)//6
    assert 2*offset+6*J == degree
    gamma,q,ng = sigma_division(norm)
    gb = (gamma[0],-gamma[1])
    qb = [(v[0],-v[1]) for v in q]
    nb = [(v[0],-v[1]) for v in ng]
    F = pa(ng,ps(pm(q,q),fm(fq(-target),fp(gamma,2))))
    assert len(F) == norm+1 and F[-1] == one
    def red(A):
        A = A[:]
        for i in range(len(A)-1,norm-1,-1):
            v = A[i]
            if v != zero:
                for j in range(norm):
                    A[i-norm+j] = fs(A[i-norm+j],fm(v,F[j]))
        return ptrim(A[:norm])
    def rm(A,B):
        return red(pm(A,B))
    def rp(A,n):
        out = [one]
        while n:
            if n&1:
                out = rm(out,A)
            A = rm(A,A)
            n //= 2
        return out
    def ri(A):
        r0,r1,s0,s1 = F,A,[zero],[one]
        while r1 != [zero]:
            quot,r2 = pd(r0,r1)
            r0,r1,s0,s1 = r1,r2,s1,pa(s0,ps(pm(quot,s1),fq(-1)))
        assert len(r0) == 1 and r0[0] != zero
        result = red(ps(s0,fi(r0[0])))
        assert rm(A,result) == [one]
        return result
    T = red(nb)
    V = ps(rp(qb,2),fp(gb,2))
    U,W = rp(T,3),rp(V,3)
    Up,Wp = [[one]],[[one]]
    for _ in range(J):
        Up.append(rm(Up[-1],U))
        Wp.append(rm(Wp[-1],W))
    frame = ps(rm(rp(ri(q),degree),rp(T,offset)),
               fm(fp(gamma,-degree-1),fq(Q(1,target**offset))))
    traces = [fq(norm)]
    for k in range(1,norm):
        val = fm(fq(k),F[norm-k])
        for j in range(1,k):
            val = fa(val,fm(F[norm-j],traces[k-j]))
        traces.append(fn(val))
    values = []
    for j in range(J+1):
        val = zero
        polynomial = rm(frame,rm(Up[j],Wp[J-j]))
        for k,coefficient in enumerate(polynomial):
            val = fa(val,fm(coefficient,traces[k]))
        values.append(val)
    return values


def rational_inverse(A, modulus):
    r0,r1,s0,s1 = modulus,A,Poly([0]),Poly([1])
    while r1 != 0:
        quotient,remainder = divmod(r0,r1)
        r0,r1,s0,s1 = r1,remainder,s1,s0-quotient*s1
    if r0.degree() != 0:
        return None
    result = divmod(s0/r0[0],modulus)[1]
    assert divmod(A*result,modulus)[1] == 1
    return result


def doubled_rational_full_fiber(norm, degree, offset, target):
    """Faithful whole 2*norm rational algebra; exact Q(delta) trace restored."""
    fq,fa,fm,fp = (H[k] for k in ("fq","fa","fm","fp"))
    gamma,q,ng = sigma_division(norm)
    gb = (gamma[0],-gamma[1])
    qb = [(v[0],-v[1]) for v in q]
    nb = [(v[0],-v[1]) for v in ng]
    F = H["pa"](ng,H["ps"](H["pm"](q,q),
                           fm(fq(-target),fp(gamma,2))))
    FR,FI = [Poly([v[k] for v in F]) for k in (0,1)]
    modulus = FR*FR+3*FI*FI
    assert modulus.degree() == 2*norm and modulus[2*norm] == 1
    invFI = rational_inverse(FI,modulus)
    if invFI is None:
        vals = native_full_fiber(norm,degree,offset,target)
        return vals, {"backend":"original_quadratic_entire_fiber",
                      "norm_fiber_sha256":digest([str(modulus[j]) for j in range(modulus.degree()+1)])}
    def red(A):
        return divmod(A,modulus)[1]
    delta = red(-FR*invFI)
    assert red(delta*delta+3) == 0
    assert red(FR+delta*FI) == 0
    def convert(A):
        return red(Poly([v[0] for v in A])+delta*Poly([v[1] for v in A]))
    def rm(A,B):
        return red(A*B)
    def rp(A,n):
        out = Poly([1])
        while n:
            if n&1:
                out = rm(out,A)
            A = rm(A,A)
            n //= 2
        return out
    q0 = convert(q)
    iq = rational_inverse(q0,modulus)
    assert iq is not None and rm(iq,q0) == 1
    T = convert(nb)
    V = rm(convert([fp(gb,2)]),rp(convert(qb),2))
    U,W = rp(T,3),rp(V,3)
    J = (degree-2*offset)//6
    assert 2*offset+6*J == degree
    Up,Wp = [Poly([1])],[Poly([1])]
    for _ in range(J):
        Up.append(rm(Up[-1],U))
        Wp.append(rm(Wp[-1],W))
    frame = rm(rm(rp(iq,degree),rp(T,offset)),
               convert([fm(fp(gamma,-degree-1),fq(Q(1,target**offset)))]))
    dimension = 2*norm
    traces = [Q(dimension)]
    for k in range(1,dimension):
        val = k*modulus[dimension-k]
        for j in range(1,k):
            val += modulus[dimension-j]*traces[k-j]
        traces.append(-val)
    def rational_trace(A):
        return sum(A[k]*traces[k] for k in range(A.degree()+1))
    assert rational_trace(Poly([1])) == 2*norm
    assert rational_trace(delta) == 0
    values = []
    for j in range(J+1):
        A = rm(frame,rm(Up[j],Wp[J-j]))
        val = (rational_trace(A)/2,-rational_trace(rm(delta,A))/6)
        values.append(val)
    return values, {
        "backend":"faithful_whole_doubled_rational_fiber",
        "rational_dimension":dimension,
        "delta_squared_minus_three_and_original_F_returned":True,
        "norm_fiber_sha256":digest([str(modulus[j]) for j in range(dimension+1)]),
        "whole_delta_embedding_sha256":digest(
            [str(delta[j]) for j in range(dimension)])}


def full_fiber(task):
    norm,degree,offset,target = task
    size = (degree-2*offset)//6+1
    values,receipt = doubled_rational_full_fiber(norm,degree,offset,target)
    assert len(values) == size
    print("R1037 degree{} norm{} entire fiber {}/{} elapsed {:.3f}s".format(
        degree,norm,target,size+2,time.monotonic()-START),file=sys.stderr,flush=True)
    return target,values,receipt


def complete_matrix(norm,workers,degree=N,offset=0):
    size = (degree-2*offset)//6+1
    targets = list(range(1,size+3))
    with concurrent.futures.ProcessPoolExecutor(
            max_workers=workers,mp_context=multiprocessing.get_context("fork")) as pool:
        rows = {a:(row,receipt) for a,row,receipt in
                pool.map(full_fiber,[(norm,degree,offset,a) for a in targets])}
    # One entire fiber is independently returned in the original K backend.
    assert rows[1][0] == native_full_fiber(norm,degree,offset,1)
    V = Mat([[Q(a**(3*j)) for j in range(size)]
             for a in targets[:size]])
    Vi = V.inv()
    A = tuple(Vi*Mat([[rows[a][0][j][k] for j in range(size)]
                      for a in targets[:size]]) for k in (0,1))
    for k in (0,1):
        assert V*A[k] == Mat([[rows[a][0][j][k] for j in range(size)]
                              for a in targets[:size]])
    for a in targets[size:]:
        ev = Mat([[Q(a**(3*j)) for j in range(size)]])
        for k in (0,1):
            assert ev*A[k] == Mat([[rows[a][0][j][k] for j in range(size)]])
    assert H["km"](A,conjugate(A)) == H["identity"](size)
    print("R1037 degree{} complete norm{} returned all{}, extra2, inverse".format(
        degree,norm,size),file=sys.stderr,flush=True)
    return A, {
        "norm":norm,"degree":degree,"all_columns":size,
        "entire_fiber_target_range":[1,size+2],
        "all_interpolation_rows_and_two_extra_fibers_returned":True,
        "one_full_fiber_independently_returned_in_original_quadratic_backend":True,
        "conjugate_inverse_returned":True,
        "complete_matrix_sha256":mh(A),
        "whole_fibers_sha256":digest([
            {"target":a,"row":[enc(v) for v in rows[a][0]],
             "certificate":rows[a][1]} for a in targets]),
        "fallback_targets":[a for a in targets if
            rows[a][1]["backend"] == "original_quadratic_entire_fiber"]}


def delta_pull_trace(up_degree):
    """Both full maps for D_delta:S_(N/3)->S_N and its unaveraged trace."""
    assert up_degree % 6 == 0
    M = up_degree//3
    offset = (M//2)%3
    J = (M-2*offset)//6
    upper_size = up_degree//6+1
    X = Poly([0,1])
    dM = Q((-3)**(M//2))
    ep = [dM*Q(-1,3)**(offset+3*j)*
          X**(2*(J-j))*(X+4)**(offset+3*j) for j in range(J+1)]
    E = pair(Mat([[p[i] for p in ep] for i in range(upper_size)]))
    positive = [Poly([3]),-3*X,9*X*X]
    maximum_positive = 3*(upper_size-1)-M
    for k in range(3,max(2,maximum_positive)+1):
        positive.append(-3*X*positive[k-1]-4*positive[k-3])
    negative = [Poly([3]),Poly([0]),-Q(3,2)*X]
    for k in range(3,M+1):
        negative.append(-Q(3,4)*X*negative[k-2]-Q(1,4)*negative[k-3])
    tp = []
    for j in range(upper_size):
        exponent = 3*j-M
        p = (positive[exponent] if exponent>=0 else negative[-exponent])/dM
        assert all(p[k] == 0 for k in range(p.degree()+1)
                   if k%3 != offset)
        assert p.degree() <= 3*J+offset
        tp.append(p)
    T = pair(Mat([[p[offset+3*i] for p in tp] for i in range(J+1)]))
    assert H["km"](T,E) == H["ks"](H["identity"](J+1),H["fq"](3))
    return E,T


def recover_two_original_sources(workers):
    A7,r7 = complete_matrix(7,workers,390)
    A19,r19 = complete_matrix(19,workers,390)
    assert H["km"](A7,A19) == H["km"](A19,A7)
    old_hash = digest({"N7":H["serialize_matrix"](A7),
                       "N19":H["serialize_matrix"](A19)})
    assert old_hash == "e80e5777735077da004012b5abe8dfd2ba246b9404fd53899502c453242d1fff"
    original_report = {
        "only_two_matrices_necessary_for_new_inputs_rebuilt":True,
        "old_construct_complete_source_not_called":True,
        "original_entire_matrix_sha256":old_hash,
        "original_job_without_full_coordinates":140158402506,
        "original_run":45892525657,
        "original_source_commit":"c3fc3c60605f4455fc57177367c89e56a9763f6a",
        "whole_operator_receipts":[r7,r19]}
    seq7,seq19 = powers(A7,12),powers(A19,12)
    zeta = H["fq"](Q(1,2),Q(-1,2))
    _,trace390 = delta_pull_trace(390)
    vectors,receipts,full_polynomials = [],[],[]
    for name,i,j,expected_hash in SOURCE_DECLARATIONS:
        P = H["km"](eig_project(seq7,H["fp"](zeta,i)),
                     eig_project(seq19,H["fp"](zeta,j)))
        assert projector_rank(P) == 1
        col = next(k for k in range(66) if
                   any(H["get_entry"](P,r,k) != H["fq"](0) for r in range(66)))
        v = H["column"](P,col)
        lead = max(r for r in range(66) if H["get_entry"](v,r) != H["fq"](0))
        assert lead == 64
        v = H["ks"](v,H["fi"](H["get_entry"](v,lead)))
        assert v[1] == Mat(66,1) and mh(v) == expected_hash
        assert H["km"](trace390,v) == H["kzero"](22,1)
        original = Poly([v[0][r,0] for r in range(66)])
        quotient,remainder = divmod(original,Poly([1,1]))
        assert remainder == 0 and quotient*Poly([1,1]) == original
        assert quotient.degree() == 63 and quotient[63] == 1
        w = H["kvec"]([quotient[r] for r in range(SIZE)])
        vectors.append(w)
        full_polynomials.append(original)
        print("R1037_COMPLETE_SOURCE_COORDINATES "+json.dumps({
            "name":name,"original390_whole_vector_sha256":mh(v),
            "original390_polynomial_X_ascending":[str(v[0][r,0]) for r in range(66)],
            "quotient378_whole_vector_sha256":mh(w),
            "quotient378_polynomial_X_ascending":[str(quotient[r]) for r in range(SIZE)]
        },sort_keys=True,separators=(",",":")),file=sys.stderr,flush=True)
        receipts.append({
            "name":name,"original390_entire_source_sha256":mh(v),
            "original390_entire_projector_sha256":mh(P),
            "original390_mass_zero_and_order_six":True,
            "original390_entire_delta_trace_zero":True,
            "whole_B12_division_back_multiplied":True,
            "new378_entire_vector_sha256":mh(w),
            "new378_mass":"1",
            "original_derivative_at_minus_one":str(
                sum(r*original[r]*Q(-1)**(r-1) for r in range(1,65)))})
    diff = H["ka"](vectors[0],H["ks"](vectors[1],H["fq"](-1)))
    assert H["get_entry"](diff,63) == H["fq"](0)
    assert diff != H["kzero"](SIZE,1)
    vectors.append(diff)
    return vectors,receipts,original_report,full_polynomials


def dyadic_operator():
    x = Poly([0,1])
    columns = [Q(-1)**j*(x+1)**(189-3*j)*(x-2)**(3*j)/Q(3)**94
               for j in range(SIZE)]
    D = pair(Mat([[p[3*i] for p in columns] for i in range(SIZE)]))
    I = H["identity"](SIZE)
    assert H["km"](D,D) == I
    return D


def seven_old_embeddings():
    gamma,q,ng = sigma_division(7)
    X = Poly([0,1])
    R = [H["fq"](0)]*2
    R[0],R[1] = q[0],q[3]
    A = [ng[1+3*j] for j in range(3)]
    outputs = []
    for isbar in (False,True):
        g = (gamma[0],-gamma[1]) if isbar else gamma
        rr = [(z[0],-z[1]) for z in R] if isbar else R
        aa = [(z[0],-z[1]) for z in A] if isbar else A
        def ppow(p,e):
            result = [H["fq"](1)]
            while e:
                if e&1:
                    result = H["pm"](result,p)
                p = H["pm"](p,p)
                e //= 2
            return result
        cols = []
        for j in range(10):
            p = H["pm"](ppow(rr,54-6*j),ppow(aa,3*j))
            p = [H["fq"](0)]*j+p
            p = H["ps"](p,H["fp"](g,54-6*j))
            p += [H["fq"](0)]*(SIZE-len(p))
            assert len(p) == SIZE
            cols.append(p)
        outputs.append(tuple(Mat([[cols[j][i][part] for j in range(10)]
                                  for i in range(SIZE)]) for part in (0,1)))
    combined = tuple(Mat([[outputs[0][part][i,j] for j in range(10)]+
                          [outputs[1][part][i,j] for j in range(10)]
                          for i in range(SIZE)]) for part in (0,1))
    assert H["rank"](combined) == 20
    return outputs,combined


def small_curve_trace_candidates():
    zeta = H["fq"](Q(1,2),Q(-1,2))
    roots = [H["fp"](zeta,j) for j in range(6)]
    lookup = {}
    for ell in (13,19,31):
        gamma,_,_ = sigma_division(ell)
        lookup[ell] = {}
        for j,root in enumerate(roots):
            value = H["fm"](gamma,root)
            trace = 2*value[0]
            assert trace == int(trace) and int(trace) not in lookup[ell]
            lookup[ell][int(trace)] = j
    result = []
    for a in range(6):
        for b in range(6):
            for c in range(6):
                d = 2**a*3**b*7**c
                exponents,traces = [],[]
                for ell in (13,19,31):
                    trace = 0
                    for x in range(ell):
                        val = (x*x*x+d)%ell
                        legendre = 0 if val==0 else (1 if pow(val,(ell-1)//2,ell)==1 else -1)
                        trace -= legendre
                    assert trace in lookup[ell]
                    traces.append(trace)
                    exponents.append(lookup[ell][trace])
                e13,e19,e31 = exponents
                cexp = (e19-2*e13)%6
                hexp = (cexp-e31)%6
                aexp = (e13-4*hexp-5*cexp)%6
                result.append({
                    "positive_sixth_power_representative":str(d),
                    "valuations_2_3_7":[a,b,c],
                    "exact_traces_at_13_19_31":traces,
                    "normalized_mu6_exponents_13_19_31":exponents,
                    "derived_A_C_H_exponents":[aexp,cexp,hexp],
                    "tame_two_candidate":a in (0,2) and (b+c)%2==0})
    return result


def complete_spectrum(ops,vectors,source_receipts,full_polynomials):
    km,ka,ks,fq,fp = (H[k] for k in ("km","ka","ks","fq","fp"))
    I = H["identity"](SIZE)
    zero = H["kzero"](SIZE,SIZE)
    zeta = fq(Q(1,2),Q(-1,2))
    for A in ops:
        assert km(A,conjugate(A)) == I
        powers(A,18)
    for i in range(3):
        for j in range(i):
            assert km(ops[i],ops[j]) == km(ops[j],ops[i])
    N13,N19,N31 = ops
    C = km(N19,H["kp"](conjugate(N13),2,I))
    HH = km(C,conjugate(N31))
    AA = km(km(N13,H["kp"](conjugate(HH),4,I)),
            H["kp"](conjugate(C),5,I))
    assert km(km(AA,H["kp"](HH,4,I)),H["kp"](C,5,I)) == N13
    assert km(C,H["kp"](N13,2,I)) == N19
    assert km(C,conjugate(HH)) == N31
    ap,cp,hp = powers(AA,6),powers(C,6),powers(HH,18)
    a3,h9 = scalar_identity(ap[3]),scalar_identity(hp[9])
    assert a3 == fq(-1) and h9 == fq(1)
    D2 = dyadic_operator()
    for op in ops:
        assert km(D2,op) == km(op,D2)
    two_proj = [ks(ka(I,ks(D2,fq(sign))),fq(Q(1,2))) for sign in (1,-1)]
    for P in two_proj:
        projector_rank(P)
    for i,source in enumerate(vectors[:2]):
        expected = sum(j*full_polynomials[i][j]*Q(-1)**(j-1)
                       for j in range(1,65))/Q(3)**94
        assert H["get_entry"](km(D2,source),63) == fq(expected)
        source_receipts[i]["complete_dyadic_masses"] = [
            enc(H["get_entry"](km(P,source),63)) for P in two_proj]

    E1,T1 = delta_pull_trace(378)
    E2,T2 = delta_pull_trace(126)
    E3,T3 = delta_pull_trace(42)
    Ei,Ti = E1,T1
    old = []
    for depth,(EE,TT,expected_rank) in enumerate(
            [(None,None,22),(E2,T2,8),(E3,T3,3)],start=1):
        if EE is not None:
            Ei,Ti = km(Ei,EE),km(TT,Ti)
        P = ks(km(Ei,Ti),fq(Q(1,3**depth)))
        assert projector_rank(P) == expected_rank
        for op in ops:
            assert km(P,op) == km(op,P)
        old.append(P)
    # R302 absolute phase anchor, pulled through the actual norm189 map.
    _,_,ng7 = sigma_division(7)
    theta7 = H["kvec"]([ng7[1+3*j][0] for j in range(3)])
    theta7 = (theta7[0],Mat([[ng7[1+3*j][1]] for j in range(3)]))
    theta378 = km(Ei,theta7)
    assert theta378 != H["kzero"](SIZE,1)
    assert H["get_entry"](theta378,63) == fq(1)
    theta_eigen = [fp(zeta,5),fq(1),fp(zeta,2)]
    for op,ev in zip(ops,theta_eigen):
        assert km(op,theta378) == ks(theta378,ev)
    assert km(AA,theta378) == ks(theta378,zeta)
    assert km(C,theta378) == ks(theta378,fp(zeta,2))
    assert km(HH,theta378) == theta378
    assert km(old[0],old[1]) == old[1]
    assert km(old[1],old[2]) == old[2]
    layers = [ka(I,ks(old[0],fq(-1))),
              ka(old[0],ks(old[1],fq(-1))),
              ka(old[1],ks(old[2],fq(-1))),old[2]]
    assert [projector_rank(P) for P in layers] == [42,14,5,3]
    e7,all7 = seven_old_embeddings()
    aproj = [(j,eig_project(ap,fp(zeta,j))) for j in range(6)]
    cproj = [(j,eig_project(cp,fp(zeta,j))) for j in range(6)]
    hproj = [("linear",j,eig_project(hp,fp(zeta,j))) for j in range(6)]
    h3powers = [hp[3*j] for j in range(7)]
    for j in (1,2,4,5):
        P = eig_project(h3powers,fp(zeta,j))
        assert km(hp[3],P) == ks(P,fp(zeta,j))
        hproj.append(("cubic",j,P))
    assert sum((P[0] for _,_,P in hproj),Mat(SIZE,SIZE)) == I[0]
    assert sum((P[1] for _,_,P in hproj),Mat(SIZE,SIZE)) == I[1]
    linear_total = zero
    for kind,_,P in hproj:
        if kind == "linear":
            linear_total = ka(linear_total,P)
    assert linear_total == old[0], (
        "Actual linear H part differs from the complete delta-old space")

    candidates = small_curve_trace_candidates()
    rows,total,zero_labels = [],zero,[]
    source_sums = [H["kzero"](SIZE,1) for _ in vectors]
    for ia,Pa in aproj:
        if projector_rank(Pa) == 0:
            continue
        for ic,Pc in cproj:
            Pac = km(Pa,Pc)
            if projector_rank(Pac) == 0:
                continue
            for kind,ih,Ph in hproj:
                P = km(Pac,Ph)
                rank = projector_rank(P)
                label = [ia,ic,kind,ih]
                if rank == 0:
                    zero_labels.append(label)
                    continue
                assert km(AA,P) == ks(P,fp(zeta,ia))
                assert km(C,P) == ks(P,fp(zeta,ic))
                assert km(hp[1 if kind=="linear" else 3],P) == ks(P,fp(zeta,ih))
                total = ka(total,P)
                layer_ranks = [projector_rank(km(P,Q0)) for Q0 in layers]
                assert sum(layer_ranks) == rank
                assert sum(r != 0 for r in layer_ranks) == 1
                dyadic_ranks = [projector_rank(km(P,Q0)) for Q0 in two_proj]
                assert sum(dyadic_ranks) == rank
                assert sum(r != 0 for r in dyadic_ranks) == 1
                old7rank = H["rank"](km(P,all7))
                assert old7rank in (0,rank)
                row = {
                    "label_A_C_H":label,"K_rank":rank,
                    "whole_projector_sha256":mh(P),
                    "delta_layers_new27_new9_new3_old1":layer_ranks,
                    "dyadic_plus_minus_ranks":dyadic_ranks,
                    "full_seven_old_image_rank":old7rank,
                    "whole_mass_row_nonzero":any(P[0][63,j] for j in range(SIZE)),
                    "whole_mass_row_sha256":digest([str(P[0][63,j]) for j in range(SIZE)]),
                    "inputs":[]}
                if kind == "linear":
                    e13 = (ia+4*ih+5*ic)%6
                    e19 = (ic+2*e13)%6
                    e31 = (ic-ih)%6
                    row["normalized_mu6_exponents_13_19_31"] = [e13,e19,e31]
                    row["sixth_twist_trace_matches_not_yet_rank_claims"] = [
                        c for c in candidates if
                        c["derived_A_C_H_exponents"] == [ia,ic,ih]]
                else:
                    row["genuine_ninth_character_not_Q_j0"] = True
                canonical = None
                if rank == 1:
                    col = next(j for j in range(SIZE)
                               if any(P[0][i,j] for i in range(SIZE)))
                    canonical = H["column"](P,col)
                    lead = max(i for i in range(SIZE) if canonical[0][i,0])
                    canonical = ks(canonical,fq(1/canonical[0][lead,0]))
                    assert canonical[1] == Mat(SIZE,1)
                    assert km(P,canonical) == canonical
                    denominator = math.lcm(*(
                        Fraction(str(canonical[0][i,0])).denominator for i in range(SIZE)))
                    row["canonical"] = {
                        "normalizing_column":lead,"origin_order":N-6*lead,
                        "mass":str(canonical[0][63,0]),
                        "whole_vector_sha256":mh(canonical),
                        "minimal_denominator":str(denominator)}
                    if lead != 63:
                        print("R1037_COMPLETE_MASS_ZERO_CANONICAL "+json.dumps({
                            "label_A_C_H":label,
                            "whole_vector_sha256":mh(canonical),
                            "full_polynomial_X_ascending":[
                                str(canonical[0][i,0]) for i in range(SIZE)]
                        },sort_keys=True,separators=(",",":")),file=sys.stderr,flush=True)
                for k,v in enumerate(vectors):
                    w = km(P,v)
                    source_sums[k] = ka(source_sums[k],w)
                    data = {"name":("A","B","A_minus_B")[k],
                            "zero":w == H["kzero"](SIZE,1),
                            "mass":enc(H["get_entry"](w,63)),
                            "whole_projected_vector_sha256":mh(w)}
                    if canonical is not None:
                        scalar = H["get_entry"](w,row["canonical"]["normalizing_column"])
                        assert w == ks(canonical,scalar)
                        data["scalar_on_whole_canonical_line"] = enc(scalar)
                    row["inputs"].append(data)
                rows.append(row)
                print("R1037 block "+json.dumps({
                    "label":label,"rank":rank,"layers":layer_ranks,
                    "dyadic":dyadic_ranks,"old7":old7rank,
                    "mass_row":row["whole_mass_row_nonzero"],
                    "input_nonzero":[not x["zero"] for x in row["inputs"]]
                },sort_keys=True),file=sys.stderr,flush=True)
    assert total == I and sum(row["K_rank"] for row in rows) == SIZE
    assert source_sums == vectors
    return {
        "all_three_entire_operators_commute":True,
        "all_three_entire_eighteenth_powers_identity":True,
        "derived_generators":{
            "C":"N19*N13^-2","H":"C*N31^-1","A":"N13*H^-4*C^-5",
            "A_cubed_scalar":enc(a3),"H_ninth_scalar":enc(h9),
            "C_sixth_identity":True,
            "all_inverse_substitutions_returned":True},
        "pulled_R302_Theta_anchor_all_three_operators_and_A_C_H_returned":True,
        "pulled_R302_Theta_anchor_sha256":mh(theta378),
        "complete_dyadic_operator_sha256":mh(D2),
        "complete_dyadic_projector_ranks":[projector_rank(P) for P in two_proj],
        "complete_delta_old_projector_ranks":[22,8,3],
        "complete_delta_old_projector_sha256":[mh(P) for P in old],
        "complete_delta_layer_ranks":[42,14,5,3],
        "linear_H_part_equals_entire_delta_old22":True,
        "both_complete_seven_old_embedding_sha256":[mh(E) for E in e7],
        "whole_seven_old_span_rank":20,
        "all_joint_projectors_sum_to_original_identity":True,
        "all_three_input_projections_sum_back_to_entire_inputs":True,
        "nonzero_joint_blocks":rows,
        "zero_joint_labels_after_complete_A_C":zero_labels,
        "all216_positive_2_3_7_sixth_twist_trace_candidates_sha256":digest(candidates),
        "no_arithmetic_rank_inferred_from_point_counts_or_mass_zero":True}


def compact_report(report):
    """Keep a bounded JSON result; the complete exact report stays in job logs."""
    print("R1037_COMPLETE_SPECTRUM_REPORT "+json.dumps(
        report,sort_keys=True,separators=(",",":")),file=sys.stderr,flush=True)
    spectrum = dict(report["spectrum"])
    detailed = spectrum.pop("nonzero_joint_blocks")
    spectrum.pop("zero_joint_labels_after_complete_A_C",None)
    columns = [
        "A_C_H_label","K_rank","delta_layer_0_to_3","dyadic_sign","seven_old_rank",
        "mass_row_nonzero","projector_sha256","mass_row_sha256",
        "canonical_lead_order_mass_hash_denominator","A_B_difference",
        "positive_twist_candidates_d_valuations_traces_tame2"]
    rows = []
    for row in detailed:
        canonical = row.get("canonical")
        canonical = None if canonical is None else [
            canonical["normalizing_column"],canonical["origin_order"],
            canonical["mass"],canonical["whole_vector_sha256"],
            canonical["minimal_denominator"]]
        inputs = [[x["zero"],x["mass"],x["whole_projected_vector_sha256"],
                   x.get("scalar_on_whole_canonical_line")] for x in row["inputs"]]
        candidates = [[x["positive_sixth_power_representative"],x["valuations_2_3_7"],
                       x["exact_traces_at_13_19_31"],x["tame_two_candidate"]]
                      for x in row.get("sixth_twist_trace_matches_not_yet_rank_claims",[])]
        rows.append([
            row["label_A_C_H"],row["K_rank"],
            next(i for i,r in enumerate(row["delta_layers_new27_new9_new3_old1"]) if r),
            1 if row["dyadic_plus_minus_ranks"][0] else -1,
            row["full_seven_old_image_rank"],row["whole_mass_row_nonzero"],
            row["whole_projector_sha256"],row["whole_mass_row_sha256"],
            canonical,inputs,candidates])
    spectrum["joint_block_columns"] = columns
    spectrum["all_nonzero_joint_blocks"] = rows
    spectrum["all_omitted_joint_labels_have_exactly_zero_projector"] = True
    out = dict(report)
    out["spectrum"] = spectrum
    out["schema"] = "rank2-original-degree378-complete-spectrum-result-v1"
    out["complete_exact_report_in_stderr_sha256"] = digest(report)
    out["complete_source_and_mass_zero_line_coordinates_in_stderr"] = True
    encoded = json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    if len(encoded) > 54000:
        # Every long rational remains in the complete authenticated log record.
        out["spectrum"]["joint_block_columns"] = columns[:8]+[
            "whole_canonical_vector_sha256","three_input_zero_flags",
            "three_whole_projected_vector_sha256","complete_block_receipt_sha256"]
        out["spectrum"]["all_nonzero_joint_blocks"] = [
            row[:8]+[
                None if original.get("canonical") is None else
                    original["canonical"]["whole_vector_sha256"],
                [x["zero"] for x in original["inputs"]],
                [x["whole_projected_vector_sha256"] for x in original["inputs"]],
                digest(original)]
            for row,original in zip(rows,detailed)]
        out["long_exact_scalars_retained_only_in_complete_stderr_record"] = True
    return out


def main():
    global H,D19
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers",type=int,default=4)
    parser.add_argument("--request",required=True)
    args = parser.parse_args()
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    request = json.loads(Path(args.request).read_text())
    assert request["schema"] == "rank2-original-degree378-complete-spectrum-v1"
    pins = dict(request["expected_source_pins"])
    for name,value in FIXED_PINS.items():
        assert pins[name] == value
    assert Path(__file__).name in pins
    actual = {}
    for name,expected in sorted(pins.items()):
        assert Path(name).name == name
        data = (HERE/name).read_bytes()
        sha = hashlib.sha256(data).hexdigest()
        assert sha == expected,(name,sha,expected)
        actual[name] = {"bytes":len(data),"sha256":sha}
    D19 = module("r1037_original_complete_CM19_backend",
                 HERE/"check-r480-actual-input-cm19.py")
    H = D19.H
    for norm in (7,13,19,31):
        sigma_division(norm)
    # R302 full Hecke/Schwartz phase anchor; no value is read from point counts.
    zeta = H["fq"](Q(1,2),Q(-1,2))
    for norm,exponent in ((13,5),(19,0),(31,2)):
        for target in (1,SIZE+2):
            row,_ = doubled_rational_full_fiber(norm,2,1,target)
            assert row == [H["fp"](zeta,exponent)]
    # Preserve both other old absolute normalizations, without rephasing norm31.
    for target in (1,SIZE+2):
        row,_ = doubled_rational_full_fiber(19,4,2,target)
        assert row == [H["fq"](-1)]
        row,_ = doubled_rational_full_fiber(13,34,2,target)
        coeff = [Q(-128,7),Q(-80,7),Q(-12,7),Q(-53,7),Q(1),Q(0)]
        value = H["fq"](0)
        for c,v in zip(coeff,row):
            value = H["fa"](value,H["fm"](H["fq"](c),v))
        expected = -sum(coeff[j]*Q(target)**(3*j) for j in range(6))
        assert value == H["fq"](expected)
    vectors,sources,original,polynomials = recover_two_original_sources(args.workers)
    ops,op_receipts = [],[]
    for norm in (13,19,31):
        A,receipt = complete_matrix(norm,args.workers)
        ops.append(A)
        op_receipts.append(receipt)
    spectrum = complete_spectrum(ops,vectors,sources,polynomials)
    report = {
        "status":"PASS","original_degree":390,"new_degree":378,
        "complete_basis":"sigma^378*(1,X,...,X^63), X=x^3",
        "normalization":"[gamma]_*[bar_gamma]^*/gamma, original entire sigma division",
        "original390_complete_source_report":original,
        "entire_B12_quotient_sources":sources,
        "new_norm_operators":op_receipts,
        "spectrum":spectrum,
        "source_manifest":actual,"source_manifest_sha256":digest(actual),
        "generated_coefficients_read_from_files":False,
        "generated_files_written":False,
        "elapsed_seconds":time.monotonic()-START}
    report = compact_report(report)
    encoded = json.dumps(report,sort_keys=True,separators=(",",":"))
    assert len(encoded.encode()) <= 58000, "Compact result must fit public request output cap"
    print(encoded,flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate all cyclic kernels of a chosen odd prime degree on a fixed SS curve.

Use the smallest x-coordinate field, a quadratic twist when Frobenius is -1,
two actual torsion generators, integral formal retraction, and exact descent
of every kernel polynomial to the quadratic unramified base.  Timing is not
part of the deterministic certificate.
"""
import argparse
import gzip
import hashlib
import json
import random
import time
from pathlib import Path
from p41_etale_torsion_lift47 import (curve_value, lift_ordinate, retract_torsion,
                                    jacobian_add, jacobian_double)
from p41_unramified_kernel_ring47 import (SparseUnramifiedRing, sparse_irreducible,
                                         nonsquare, square_root, square_root_minus_one,
                                         extract_quadratic)


def finite_add(P, Q, A, F):
    if P[2] == F.zero:
        return Q
    if Q[2] == F.zero:
        return P
    u1 = F.mul(P[0],F.power(Q[2],2))
    u2 = F.mul(Q[0],F.power(P[2],2))
    if u1 == u2:
        s1 = F.mul(P[1],F.power(Q[2],3))
        s2 = F.mul(Q[1],F.power(P[2],3))
        if s1 == s2:
            return jacobian_double(P,A,F)
        return F.one,F.one,F.zero
    return jacobian_add(P,Q,F)


def finite_multiply(P, n, A, F):
    out = F.one,F.one,F.zero
    for bit in bin(n)[2:]:
        if out[2] != F.zero:
            out = jacobian_double(out,A,F)
        if bit == '1':
            out = finite_add(out,P,A,F)
    return out


def affine(P, R):
    zi = R.inverse(P[2])
    z2 = R.mul(zi,zi)
    return R.mul(P[0],z2),R.mul(P[1],R.mul(zi,z2))


def batch_affine_x(points, R):
    prefix = [R.one]
    for P in points:
        assert R.is_unit(P[2])
        prefix.append(R.mul(prefix[-1],P[2]))
    inverse = R.inverse(prefix[-1])
    out = [None]*len(points)
    for k in range(len(points)-1,-1,-1):
        zi = R.mul(inverse,prefix[k])
        inverse = R.mul(inverse,points[k][2])
        out[k] = R.mul(points[k][0],R.mul(zi,zi))
    assert inverse == R.one
    return out


def short_multiples(P, count, A, R):
    out = [P]
    if count >= 2:
        out.append(jacobian_double(P,A,R))
    for _ in range(3,count+1):
        out.append(jacobian_add(out[-1],P,R))
    return out[:count]


def torsion_basis(ell, exponent, A, B, F, nonresidue, seed):
    rng = random.Random(seed)
    attempts = 0
    def sample():
        nonlocal attempts
        for _ in range(10000):
            attempts += 1
            x = tuple(rng.randrange(47) for _ in range(F.degree))
            y = square_root(curve_value(x,A,B,F),F,nonresidue)
            if y is None:
                continue
            P = finite_multiply((x,y,F.one),exponent//ell,A,F)
            if P[2] == F.zero:
                continue
            assert finite_multiply(P,ell,A,F)[2] == F.zero
            return affine(P,F)
        raise ArithmeticError('No nonzero torsion point found')
    P = sample()
    subgroup = set(batch_affine_x(short_multiples((P[0],P[1],F.one),(ell-1)//2,A,F),F))
    Q = sample()
    while Q[0] in subgroup:
        Q = sample()
    assert Q[0] not in subgroup
    return P,Q,attempts


def generate(ell, name, precision, field_polynomial=None):
    assert ell > 2 and ell != 47 and all(ell % d for d in range(2,int(ell**0.5)+1))
    av,bv = {'CM4':(-1,0),'source_j9':(1,32)}[name]
    # Count over F47, proving pi_47^2=[-47] for this actual source curve.
    cardinality = 1
    for x in range(47):
        rhs = (x*x*x+av*x+bv) % 47
        cardinality += 1 if rhs == 0 else (2 if pow(rhs,23,47)==1 else 0)
    assert cardinality == 48
    d = 1
    while pow(-47,d,ell) not in (1,ell-1):
        d += 1
    sign = 1 if pow(-47,d,ell)==1 else -1
    degree = 2*d
    polynomial = field_polynomial or sparse_irreducible(degree)
    assert len(polynomial)==degree+1
    F = SparseUnramifiedRing(polynomial,1)
    assert F.is_irreducible()
    R = SparseUnramifiedRing(polynomial,precision)
    R._residue = F
    nonresidue = nonsquare(F)
    nu = F.one if sign==1 else nonresidue
    Af = F.scale(F.power(nu,2),av)
    Bf = F.scale(F.power(nu,3),bv)
    A = R.scale(R.power(nu,2),av)
    B = R.scale(R.power(nu,3),bv)
    exponent = abs(sign*(-47)**d-1)
    assert exponent % ell == 0
    Pbar,Qbar,attempts = torsion_basis(ell,exponent,Af,Bf,F,nonresidue,470000+ell*10+(name=='CM4'))
    points = []
    for x0,y0 in [Pbar,Qbar]:
        y = lift_ordinate(x0,y0,A,B,R)
        P,t = retract_torsion((x0,y),ell,A,B,R)
        assert all(c % 47 == 0 for c in t)
        points.append(P)
    P,Q = [(x,y,R.one) for x,y in points]
    Qmult = short_multiples(Q,ell-1,A,R)
    generators = [P]+[jacobian_add(P,T,R) for T in Qmult]+[Q]
    assert len(generators)==ell+1
    h = (ell-1)//2
    full = []
    for G in generators:
        full.extend(short_multiples(G,h,A,R))
    xvalues = batch_affine_x(full,R)
    nuinv = R.inverse(nu)
    xvalues = [R.mul(x,nuinv) for x in xvalues]
    # This complete distinctness check also detects omitted or duplicate lines.
    residues = {tuple(c % 47 for c in x) for x in xvalues}
    assert len(residues)==(ell*ell-1)//2
    i = square_root_minus_one(R,nonresidue)
    Aorig,Borig = R.integer(av),R.integer(bv)
    kernels = []
    for k in range(ell+1):
        roots = xvalues[k*h:(k+1)*h]
        coefficients = [R.one]
        sumt,sumw = R.zero,R.zero
        for x in roots:
            out = [R.zero]*(len(coefficients)+1)
            for j,c in enumerate(coefficients):
                out[j] = R.sub(out[j],R.mul(x,c))
                out[j+1] = R.add(out[j+1],c)
            coefficients = out
            x2,x3 = R.power(x,2),R.power(x,3)
            sumt = R.add(sumt,R.add(R.scale(x2,3),Aorig))
            sumw = R.add(sumw,R.add(R.scale(x3,5),R.add(R.scale(R.mul(Aorig,x),3),R.scale(Borig,2))))
        descended = [extract_quadratic(c,i,R) for c in coefficients]
        assert descended[-1] == (1,0)
        At = R.sub(Aorig,R.scale(sumt,10))
        Bt = R.sub(Borig,R.scale(sumw,14))
        delta = R.add(R.scale(R.power(At,3),4),R.scale(R.power(Bt,2),27))
        assert R.is_unit(delta)
        jt = R.mul(R.scale(R.power(At,3),6912),R.inverse(delta))
        At2,Bt2,j2 = [extract_quadratic(v,i,R) for v in [At,Bt,jt]]
        assert j2[1] % 47 == 0 and j2[0] % 47 in (0,9,10,36,44)
        kernels.append({'line':k,'kernel_polynomial_ascending':descended,
                        'velu_A':At2,'velu_B':Bt2,'j':j2})
    source_paths = [Path(__file__),Path(__file__).with_name('p41_unramified_kernel_ring47.py'),
                    Path(__file__).with_name('p41_etale_torsion_lift47.py')]
    return {'curve':name,'ell':ell,'precision':precision,'modulus':R.modulus,
            'base_A':av,'base_B':bv,'cardinality_over_F47':cardinality,
            'minimal_x_degree_over_F47_squared':d,'absolute_field_degree':degree,
            'field_polynomial_ascending':polynomial,'R2_i_embedding':i,
            'quadratic_twist_used':sign==-1,'twist_parameter':nu,
            'group_exponent':str(exponent),'cofactor_used':str(exponent//ell),
            'sampling_attempts':attempts,'residue_torsion_basis':[Pbar,Qbar],
            'lifted_torsion_basis':points,'distinct_nonzero_torsion_x_count':len(residues),
            'all_kernel_polynomials_descend_to_R2':True,'kernels':kernels,
            'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths},
            'scope':'All cyclic kernels and normalized Velu short models for this stated curve and prime; no height evaluation.'}


if __name__=='__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--ell',type=int,required=True)
    ap.add_argument('--curve',choices=['CM4','source_j9'],default='CM4')
    ap.add_argument('--precision',type=int,choices=[4],default=4)
    ap.add_argument('--field-polynomial',type=Path)
    ap.add_argument('--output',type=Path,required=True)
    args = ap.parse_args()
    polynomial = json.loads(args.field_polynomial.read_text()) if args.field_polynomial else None
    started = time.monotonic()
    result = generate(args.ell,args.curve,args.precision,polynomial)
    raw = (json.dumps(result,separators=(',',':'))+'\n').encode()
    data = gzip.compress(raw,mtime=0) if args.output.suffix=='.gz' else raw
    args.output.write_bytes(data)
    print(json.dumps({'ell':args.ell,'curve':args.curve,'kernels':len(result['kernels']),
                      'field_degree':result['absolute_field_degree'],'twist':result['quadratic_twist_used'],
                      'elapsed_seconds':round(time.monotonic()-started,3),'sha256':hashlib.sha256(data).hexdigest()}))

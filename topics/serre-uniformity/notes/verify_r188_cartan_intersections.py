#!/usr/bin/env python3
"""Exact level-41 necklace weights and proper CM/Hecke intersections.

The arithmetic is over integers and F_41.  Only primes ell not dividing
2*41*n occur.  This is not a complete Neron height certificate.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from math import isqrt
from pathlib import Path

P = 41
SQRT_MINUS_ONE = 9
NONSQUARES = tuple(t for t in range(1, P) if pow(t, 20, P) == P-1)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n)+1))


def norm4(x, ell):
    a, b, c, d = x
    return a*a+b*b+ell*(c*c+d*d)


def in_order(x):
    a, b, c, d = x
    return (a-c) % 2 == 0 and (b-d) % 2 == 0


def multiply(x, y, ell):
    """Coordinates are (a+b*i+c*j+d*i*j)/2, j^2=-ell."""
    a,b,c,d = x
    e,f,g,h = y
    twice = (a*e-b*f-ell*(c*g+d*h),
             a*f+b*e+ell*(c*h-d*g),
             a*g-b*h+c*e+d*f,
             a*h+b*g-c*f+d*e)
    assert all(t % 2 == 0 for t in twice)
    z = tuple(t//2 for t in twice)
    assert in_order(z)
    assert norm4(z, ell)*4 == norm4(x, ell)*norm4(y, ell)
    return z


def all_of_norm(n, ell):
    bound = isqrt(4*n)
    jbound = isqrt(4*n//ell)
    result = []
    for c in range(-jbound, jbound+1):
        for d in range(-jbound, jbound+1):
            rest = 4*n-ell*(c*c+d*d)
            if rest < 0:
                continue
            for a in range(-isqrt(rest), isqrt(rest)+1):
                if (a-c) % 2:
                    continue
                b2 = rest-a*a
                b0 = isqrt(b2)
                if b0*b0 != b2:
                    continue
                for b in ({b0,-b0} if b0 else {0}):
                    x = (a,b,c,d)
                    if in_order(x):
                        assert max(map(abs,x)) <= bound < P
                        result.append(x)
    return sorted(result)


def gaussian_norm(n):
    result = []
    for a in range(-isqrt(n), isqrt(n)+1):
        b2 = n-a*a
        b = isqrt(b2)
        if b*b == b2:
            for bb in ({b,-b} if b else {0}):
                result.append((2*a,2*bb,0,0))
    return sorted(result)


def cyclic4(x):
    # A norm-4 endomorphism has noncyclic kernel iff it is divisible by [2].
    return not (all(t % 2 == 0 for t in x)
                and in_order(tuple(t//2 for t in x)))


def depth(x, ell):
    c,d = x[2:]
    assert c or d
    k = 1
    while c % ell == 0 and d % ell == 0:
        c //= ell
        d //= ell
        k += 1
    return k


def matching_necklaces(x, ell, n):
    a,b,c,d = x
    s = SQRT_MINUS_ONE
    A,B,C,D = ((a+s*b) % P, -ell*(c+s*d) % P,
               (c-s*d) % P, (a-s*b) % P)
    assert (A*D-B*C) % P == 4*n % P != 0
    # Both i and beta^{-1} i beta act as reflections of nu_t.
    actual = tuple(t for t in NONSQUARES if (B*D-t*A*C) % P == 0)
    Ap,Bp = (a*a+b*b) % P, ell*(c*c+d*d) % P
    if (a,b) == (0,0) or (c,d) == (0,0):
        expected = 20
    else:
        expected = int(pow((-Ap*Bp) % P, 20, P) == P-1)
    assert len(actual) == expected, (ell,n,x,actual,Ap,Bp)
    return actual


def compute(basis_path):
    basis_bytes = Path(basis_path).read_bytes()
    basis = json.loads(gzip.decompress(basis_bytes))
    assert basis['level'] == P and basis['dimension'] == 54
    labels = basis['new_correspondence_labels']
    assert len(labels) == 54 and all(x['index'] % P for x in labels)
    assert len(NONSQUARES) == 20 and SQRT_MINUS_ONE**2 % P == P-1
    rows = []
    positive = []
    checked = 0
    for label in labels:
        n = label['index']
        only_cyclic4 = label['kind'] == 'cyclic4'
        assert (n == 4) == only_cyclic4
        # All other indices in this particular basis are squarefree.
        assert only_cyclic4 or all(n % (d*d) for d in range(2,isqrt(n)+1))
        local = []
        for ell in range(3,4*n+1,4):
            if ell == P or n % ell == 0 or not prime(ell):
                continue
            units = all_of_norm(1,ell)
            assert len(units) == (12 if ell == 3 else 4)
            gaussians = gaussian_norm(n)
            # Remove the entire kernel class, including extra automorphisms
            # at 3.  A norm-4 Gaussian is divisible by 2, hence not cyclic.
            if only_cyclic4:
                gaussians = [x for x in gaussians if cyclic4(x)]
            cm_return = {multiply(u,a,ell) for u in units for a in gaussians}
            all_norm = all_of_norm(n,ell)
            assert cm_return.issubset(set(all_norm))
            hist = Counter()
            total = 0
            removed = 0
            noncyclic = 0
            entries = []
            for x in all_norm:
                if only_cyclic4 and not cyclic4(x):
                    noncyclic += 1
                    continue
                if x in cm_return:
                    removed += 1
                    continue
                assert x[2] or x[3]
                matched = matching_necklaces(x,ell,n)
                k = depth(x,ell)
                checked += 1
                hist[(k,len(matched))] += 1
                total += k*len(matched)
                if matched:
                    entries.append({'beta_twice':list(x),'depth':k,
                                    'necklaces':list(matched)})
            assert total % 2 == 0
            value = total//2
            record = {'ell':ell,'intersection':value,
                      'all_norm_n':len(all_norm),'removed_cm_kernel_class':removed,
                      'removed_noncyclic':noncyclic,
                      'proper_histogram':[
                          {'depth':k,'weight':w,'count':count}
                          for (k,w),count in sorted(hist.items())],
                      'positive_endomorphisms':entries}
            local.append(record)
            if value:
                positive.append([n,ell,value])
        rows.append({'correspondence':label,'local':local})
    lookup = {(r['correspondence']['index'],v['ell']):v
              for r in rows for v in r['local']}
    # Independent exact j-invariant check, including the extra-aut correction.
    j_difference = 287496-1728
    def valuation(n,ell):
        v=0
        while n % ell == 0:
            n//=ell;v+=1
        return v
    assert j_difference == 2**3*3**6*7**2
    assert lookup[2,3]['removed_cm_kernel_class'] == 12
    assert lookup[2,7]['removed_cm_kernel_class'] == 4
    assert lookup[2,3]['intersection'] == 2*valuation(j_difference,3) == 12
    assert lookup[2,7]['intersection'] == 2*valuation(j_difference,7) == 4
    return {'level':P,'basis_sha256':hashlib.sha256(basis_bytes).hexdigest(),
            'source_sha256':digest(__file__),
            'scope':'proper horizontal CM4/Hecke intersections only; ell does not divide 2*41*n; not a complete height',
            'bound':'ell <= 4*n; split ell contribute zero',
            'checked_proper_endomorphisms':checked,
            'positive_triples_n_ell_I':positive,'rows':rows,
            'independent_n2_j_check':{'j_CM16':287496,'j_CM4':1728,
                 'difference_factorization':[[2,3],[3,6],[7,2]],
                 'marked_intersections_Z4_C2proper':[[3,12],[7,4]]}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--basis',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    result=compute(args.basis)
    raw=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    if args.check:
        assert json.loads(gzip.decompress(args.output.read_bytes())) == result
    else:
        args.output.write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
    print('PASS: all 54 correspondences; %d marked endomorphisms; %d nonzero prime terms' %
          (result['checked_proper_endomorphisms'],len(result['positive_triples_n_ell_I'])))
    print('certificate_bytes=%d sha256=%s' % (args.output.stat().st_size,digest(args.output)))
    print('n=2 checks: I_3=12, I_7=4; full Neron correction remains open')


if __name__=='__main__':
    main()

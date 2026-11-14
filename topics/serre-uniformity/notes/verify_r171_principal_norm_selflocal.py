#!/usr/bin/env python3
"""Exact p=43 principal-norm, Robert-zero and self-local slope certificate.

Only the Python standard library and the repository's standard-library R161
arithmetic module are used. The input contains an ECPP chain with an elementary
Pratt base, exact polynomial maps, and all 44 roots in F_(q^2). No primality,
class-group, floating-point, or finite-field factorization oracle is needed.

The supplied gamma_2 class polynomial is the one returned by
  polclass(-16*43^2,5)
in PARI/GP 2.19.0. This one CM-polynomial input has a separate regeneration
command in R171. All subsequent polynomial identities and all reported finite
arithmetic are verified here exactly. Run --check to reproduce the certificate.
"""
import argparse
import hashlib
import importlib.util
import json
import sys
from math import comb, gcd, isqrt, lcm
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "r161_arithmetic", HERE / "verify_r161_adjoint_unit_residues.py")
r161 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r161)
TARGET = HERE / "r171_principal_norm_selflocal_certificate.json"


def trial_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def verify_pratt(cert):
    if isinstance(cert, int):
        assert cert < 1000 and trial_prime(cert)
        return cert
    n, a, factors = cert
    assert n >= 1000 and 1 < a < n
    product = 1
    seen = set()
    for prime, exponent, subcert in factors:
        assert prime not in seen and exponent > 0
        seen.add(prime)
        assert verify_pratt(subcert) == prime
        product *= prime**exponent
        assert gcd(pow(a, (n-1)//prime, n)-1, n) == 1
    assert product == n-1 and pow(a, n-1, n) == 1
    return n


def ec_add(n, a, p, q):
    if p is None:
        return q
    if q is None:
        return p
    x, y = p
    z, w = q
    if x == z and (y+w) % n == 0:
        return None
    if x == z:
        assert y == w
        denominator, numerator = 2*y % n, (3*x*x+a) % n
    else:
        denominator, numerator = (z-x) % n, (w-y) % n
    # A unit denominator makes every intermediate affine point valid modulo
    # every prime divisor of n, as required by the ECPP proof.
    assert gcd(denominator, n) == 1
    slope = numerator*pow(denominator, -1, n) % n
    xx = (slope*slope-x-z) % n
    return xx, (slope*(x-xx)-y) % n


def ec_mul(n, a, scalar, p):
    ans = None
    while scalar:
        if scalar & 1:
            ans = ec_add(n, a, ans, p)
        p = ec_add(n, a, p, p)
        scalar >>= 1
    return ans


def verify_ecpp(chain, base):
    next_prime = verify_pratt(base)
    for n, trace, cofactor, a, point in reversed(chain):
        assert n > next_prime and trace*trace < 4*n and cofactor > 0
        order = n+1-trace
        assert order == cofactor*next_prime
        # This integer bound is slightly stronger than the usual ECPP bound
        # next_prime > (n^(1/4)+1)^2 and avoids approximate roots.
        assert next_prime > (isqrt(isqrt(n))+2)**2
        x, y = point
        assert 0 <= x < n and 0 <= y < n
        a %= n
        b = (y*y-x*x*x-a*x) % n
        assert gcd(4*a*a*a+27*b*b, n) == 1
        assert ec_mul(n, a, order, (x,y)) is None
        assert ec_mul(n, a, cofactor, (x,y)) is not None
        next_prime = n
    return next_prime


def trim(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def reduce_poly(poly, modulus, characteristic=None):
    poly = poly[:]
    degree = len(modulus)-1
    assert modulus[-1] == 1
    for j in range(len(poly)-1, degree-1, -1):
        a = poly[j]
        if a:
            for k in range(degree):
                poly[j-degree+k] -= a*modulus[k]
                if characteristic is not None:
                    poly[j-degree+k] %= characteristic
    poly = poly[:degree]
    if characteristic is not None:
        poly = [x % characteristic for x in poly]
    return trim(poly)


def multiply_poly(a, b, modulus=None, characteristic=None):
    if not a or not b:
        return []
    c = [0]*(len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            c[j+k] += x*y
    if characteristic is not None:
        c = [x % characteristic for x in c]
    return reduce_poly(c, modulus, characteristic) if modulus else trim(c)


def power_poly(a, exponent, modulus, characteristic):
    ans = [1]
    while exponent:
        if exponent & 1:
            ans = multiply_poly(ans, a, modulus, characteristic)
        a = multiply_poly(a, a, modulus, characteristic)
        exponent >>= 1
    return ans


def gcd_poly(a, b, characteristic):
    a, b = trim(a[:]), trim(b[:])
    while b:
        b = [x*pow(b[-1], -1, characteristic) % characteristic for x in b]
        a, b = b, reduce_poly(a, b, characteristic)
    return [x*pow(a[-1], -1, characteristic) % characteristic for x in a]


def irreducible_degree44_mod5(descending):
    f = [x % 5 for x in reversed(descending)]
    assert len(f) == 45 and f[-1] == 1
    xx = [0,1]
    frob = xx
    for j in range(1,45):
        frob = power_poly(frob, 5, f, 5)
        if j in (4,22):
            difference = frob+[0]*max(0,2-len(frob))
            difference[1] = (difference[1]-1) % 5
            assert gcd_poly(f, trim(difference), 5) == [1]
    assert frob == xx


def verify_model(data):
    pd, wd, gd = data['P'], data['weber_polynomial'], data['gamma2_polynomial']
    assert len(pd) == len(wd) == len(gd) == 45
    assert pd[0] == wd[0] == gd[0] == 1
    assert all(pd[j] == 0 for j in range(1,45,2))
    irreducible_degree44_mod5(pd)
    irreducible_degree44_mod5(wd)
    pasc = list(reversed(pd))
    # Verify W(t(y))=0 in Q[y]/P(y), with one denominator and integer Horner
    # arithmetic. No numerical algebraic-number recognition is involved.
    rational_map = data['weber_map']
    denominator = lcm(*(c[1] for c in rational_map))
    numerator = [a*(denominator//b) for a,b in rational_map]
    value, d = [wd[0]], 1
    for coefficient in wd[1:]:
        value = multiply_poly(value, numerator, pasc)
        d *= denominator
        if not value:
            value = [0]
        value[0] += coefficient*d
        value = trim(value)
    assert value == []
    # W divides t^44 G((t^3+16)/t), exactly over Z.
    composite = [0]*133
    for index, coefficient in enumerate(gd):
        power = 44-index
        for j in range(power+1):
            composite[44-power+3*j] += coefficient*comb(power,j)*16**(power-j)
    assert reduce_poly(composite, list(reversed(wd))) == []
    b = data['b']
    norm = sum(c*b**j for j,c in enumerate(pd))
    assert norm == -data['q']
    return {'degree':44, 'irreducibility_prime':5,
            'norm_alpha':norm, 'gamma2_discriminant':-16*43**2}


class CertifiedField(r161.Fq2):
    def __init__(self, q):
        # Primality is proved by verify_ecpp before this is constructed.
        assert q % 172 == 171
        self.q = q
        self.zero, self.one, self.i = (0,0), (1,0), (0,1)


def polyval(field, descending, value):
    ans = field.zero
    for coefficient in descending:
        ans = field.add(field.mul(ans,value),(coefficient % field.q,0))
    return ans


def phi2(field, point):
    x, y = point
    s = field.sub(x,field.one)
    xx = field.add(x,field.div((2,0),s))
    yy = field.mul(y,field.sub(field.one,field.div((2,0),field.mul(s,s))))
    assert field.mul(yy,yy) == field.sub(
        field.sub(field.power(xx,3),field.scale(11,xx)),(14,0))
    return xx,yy


def quotient_delta(field, curve, generator):
    aa,bb,rt=(-11 % field.q,0),(-14 % field.q,0),(-2 % field.q,0)
    st,sw,sx=field.zero,field.zero,field.zero
    point=None
    for k in range(1,22):
        point=curve.add(point,generator)
        x,y=phi2(field,point)
        t=field.add(field.scale(3,field.mul(x,x)),aa)
        w=field.add(field.add(field.scale(5,field.power(x,3)),
            field.scale(3,field.mul(aa,x))),field.scale(2,bb))
        st,sw=field.add(st,field.scale(2,t)),field.add(sw,field.scale(2,w))
        xplus=field.sub(field.sub(field.div(field.mul(y,y),
            field.power(field.sub(x,rt),2)),x),rt)
        sx=field.add(sx,field.scale(2,field.sub(xplus,x)))
    a=field.sub(aa,field.scale(5,st))
    b=field.sub(bb,field.scale(7,sw))
    r=field.add(rt,sx)
    assert field.add(field.add(field.power(r,3),field.mul(a,r)),b)==field.zero
    discriminant=field.add(field.scale(4,field.power(a,3)),
                           field.scale(27,field.power(b,2)))
    assert discriminant!=field.zero
    j=field.div(field.scale(6912,field.power(a,3)),discriminant)
    a2,a4=field.scale(3,r),field.add(field.scale(3,field.mul(r,r)),a)
    delta=field.div(field.scale(16,field.sub(field.mul(a2,a2),field.scale(4,a4))),a4)
    assert j==field.div(field.power(field.add(delta,(16,0)),3),delta)
    return delta,j


def pairing(field, curve, p, r):
    def g(s,t,q):
        if s is None or t is None:
            return field.one
        st=curve.add(s,t)
        if st is None:
            return field.sub(q[0],s[0])
        if s==t:
            slope=field.div(field.sub(field.scale(3,field.mul(s[0],s[0])),field.one),field.scale(2,s[1]))
        else:
            slope=field.div(field.sub(t[1],s[1]),field.sub(t[0],s[0]))
        line=field.sub(field.sub(q[1],s[1]),field.mul(slope,field.sub(q[0],s[0])))
        return field.div(line,field.sub(q[0],st[0]))
    def miller(s,q):
        value,current=field.one,s
        for bit in bin(43)[3:]:
            value=field.mul(field.mul(value,value),g(current,current,q))
            current=curve.add(current,current)
            if bit=='1':
                value=field.mul(value,g(current,s,q));current=curve.add(current,s)
        assert current is None
        return value
    answer=field.neg(field.div(miller(p,r),miller(r,p)))
    assert answer!=field.one and field.power(answer,43)==field.one
    return answer


def robert_projection(field,curve,point,logs):
    p,q=43,field.q
    ip=curve.cm_i(point)
    p2=(field.i,(1,q-1))
    aa,bb=[None],[None]
    for k in range(1,p):
        aa.append(curve.add(aa[-1],point));bb.append(curve.add(bb[-1],ip))
    aa=[curve.add(p2,t) for t in aa]
    exponent=(q*q-1)//p
    sums=[0,0];records=bytearray();table={}
    for u in range(p):
        for v in range(p):
            if (u,v)==(0,0):
                continue
            here=curve.add(aa[u],bb[v])
            assert here is not None and curve.on_curve(here)
            psi=curve.division_values(here)
            value=psi(11)
            assert value!=field.zero
            ell=logs[field.power(value,exponent)]
            invnorm=pow((u*u+v*v)%p,-1,p)
            sums[0]=(sums[0]+ell*(u*u-v*v)*invnorm)%p
            sums[1]=(sums[1]+ell*2*u*v*invnorm)%p
            table[(u,v)]=ell;records.extend((u,v,ell))
            if (u,v) in ((0,1),(1,0),(1,1)):
                multiple=curve.mul(11,here)
                xx=field.sub(here[0],field.div(field.mul(psi(10),psi(12)),field.power(value,2)))
                assert multiple is not None and multiple[0]==xx
    assert len(table)==1848 and sums==[0,0]
    fp=r161.Fq2(43);independent=fp.zero
    for a,ell in table.items():
        assert table[(-a[1]%p,-a[0]%p)]==-ell%p
        independent=fp.add(independent,fp.scale(ell,fp.power(a,1-p)))
    assert independent==fp.zero
    return {'points':1848,'S':sums,
            'log_table_sha256':hashlib.sha256(records).hexdigest()}


def compute(data):
    model=verify_model(data)
    q=data['q'];p=43;b=data['b']
    assert verify_ecpp(data['ecpp'],data['pratt_base'])==q
    field,fp=CertifiedField(q),r161.Fq2(p)
    curve=r161.Curve(field)
    seed,point=r161.torsion_point(curve,p)
    zeta=pairing(field,curve,point,curve.cm_i(point))
    logs={};z=field.one
    for j in range(p):
        logs[z]=j;z=field.mul(z,zeta)
    assert len(logs)==p and z==field.one
    roots=[tuple(t) for t in data['roots_y']]
    assert len(roots)==44 and roots==sorted(set(roots))
    tcoeff=[a*pow(d,-1,q)%q for a,d in data['weber_map']]
    delta_map={}
    for index,y in enumerate(roots):
        assert polyval(field,data['P'],y)==field.zero
        t=polyval(field,list(reversed(tcoeff)),y)
        assert polyval(field,data['weber_polynomial'],t)==field.zero
        delta=field.power(t,3)
        assert delta not in delta_map
        delta_map[delta]=(index,y,t)
    beta,omega=(42,2),(8,25)
    assert fp.power(beta,1-p)==omega
    assert fp.power(omega,44)==fp.one
    assert fp.power(omega,22)!=fp.one and fp.power(omega,4)!=fp.one
    rows=[];current=point;rotation=fp.one
    for j in range(44):
        delta,jj=quotient_delta(field,curve,current)
        assert delta in delta_map
        index,y,t=delta_map[delta]
        rows.append((index,y,t,rotation,delta,jj))
        current=curve.add(curve.mul(-1,current),curve.mul(2,curve.cm_i(current)))
        rotation=fp.mul(rotation,omega)
    assert len({row[0] for row in rows})==44 and rotation==fp.one
    for j in range(44):
        for key in (1,2,4,5):
            assert rows[-j%44][key]==field.power(rows[j][key],q)
        assert rows[(j+22)%44][1]==field.neg(rows[j][1])
    constant=field.neg(field.scale(b,rows[0][1]))
    assert constant in (field.one,(-1%q,0))
    alpha_constant=1 if constant==field.one else -1
    unit_logs=[None];total=[0,0]
    for j in range(1,44):
        alpha=field.add(field.scale(b,rows[j][1]),constant)
        assert alpha!=field.zero
        ell=logs[field.power(alpha,(q*q-1)//p)]
        unit_logs.append(ell)
        for k in (0,1):
            total[k]=(total[k]+ell*rows[j][3][k])%p
    assert total[0]==0 and unit_logs[22]==0
    assert all((unit_logs[j]+unit_logs[44-j])%p==0 for j in range(1,22))
    slope=total[1]*pow(2,-1,p)%p
    assert slope==sum(rows[j][3][1]*unit_logs[j] for j in range(1,22))%p
    robert=robert_projection(field,curve,point,logs)
    v,quotient=0,q+1
    while quotient%p==0:
        v+=1;quotient//=p
    assert v==1 and slope==16 and (q+1)//p%p==11
    z=(q+1)//p*pow(2,-1,p)%p
    x=z*pow(slope,-1,p)%p
    assert x==p-1
    gaussian=field.power((-1%q,2),(q*q-1)//p)
    assert gaussian!=field.one
    def legendre(value):
        result=pow(value%p,(p-1)//2,p)
        assert result in (1,p-1)
        return 1 if result==1 else -1
    sign_e1=legendre(-2*x)
    sign_e3=legendre(-2*x*pow(3,-1,p))
    assert sign_e1==-1 and sign_e3==1
    return {'model':model,'ecpp_steps':len(data['ecpp']),'q_bits':q.bit_length(),
            'seed':seed,'P':point,'zeta_Weil':zeta,'beta':beta,'W_rotation':omega,
            'root_labels':[row[0] for row in rows], 'alpha_constant':alpha_constant,
            'unit_logs':unit_logs,'raw_W_sum':total,'lambda':slope,'robert':robert,
            'q_plus_one_p_valuation':v,'q_plus_one_div_p_mod_p':(q+1)//p%p,
            'forced_x':x,'gaussian5_symbol':gaussian,
            'Weil_multiplier_sign_for_e1':sign_e1,
            'Weil_multiplier_sign_for_e3':sign_e3}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--write-expected',action='store_true')
    args=parser.parse_args()
    data=json.loads(TARGET.read_text())
    result=json.loads(json.dumps(compute(data)))
    if args.write_expected:
        data['expected']=result
        TARGET.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    if args.check:
        assert data['expected']==result
    print('PASS: exact CM model; ECPP/Pratt primality; prime norm; 44 labelled CM roots; 1848 Robert values; lambda=16')
    print('certificate_sha256='+hashlib.sha256(TARGET.read_bytes()).hexdigest())


if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Exact restoration check in Q[a,zeta]/(a^3-4,zeta^2+zeta+1).
No torsion orbit modulo p, floating point, or previously lost p-adic run is used.
The common sqrt(3) factor is removed from all y/e coordinates.
"""
from fractions import Fraction as Q
import json, hashlib
from pathlib import Path
Z=(Q(0),)*6

def el(v):
    if isinstance(v,tuple):return v
    return (Q(v),)+Z[1:]
def add(a,b):return tuple(x+y for x,y in zip(el(a),el(b)))
def neg(a):return tuple(-x for x in el(a))
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    a,b=el(a),el(b);out=[Q(0)]*6
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            if not ai or not bj:continue
            u=i%3+j%3;v=i//3+j//3;c=ai*bj
            if u>=3:u-=3;c*=4
            if v==2:out[u]-=c;out[3+u]-=c
            else:out[3*v+u]+=c
    return tuple(out)
def scale(a,c):return mul(a,Q(c))
def power(a,n):
    out=el(1)
    while n:
        if n&1:out=mul(out,a)
        n//=2
        if n:a=mul(a,a)
    return out
A=tuple(map(Q,[0,1,0,0,0,0]));zet=tuple(map(Q,[0,0,0,1,0,0]));ONE=el(1)
def inv_a_minus_t(t):return scale(add(add(power(A,2),mul(A,t)),power(t,2)),Q(1,3))
def pmul(a,b):
    out=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=add(out[i+j],mul(x,y))
    return out

def serial(a):return [str(x) for x in a]
records=[]
for r in range(3):
    t=power(zet,r);di=inv_a_minus_t(t)
    assert mul(sub(A,t),di)==ONE
    X=sub(sub(scale(power(di,2),3),A),t)
    V=mul(sub(t,X),di) # y(Q)/sqrt(3), for delta=+1
    assert sub(power(X,3),scale(power(V,2),3))==ONE
    records.append((t,X,V,power(X,3)))
D=[ONE]
for _,_,_,a in records:D=pmul(D,[neg(a),ONE])
expectedD=list(map(el,[-64,48,-228,1]));assert D==expectedD
N0=[Z]*3;Nminus=[Z]*3
for i,(t,X,V,root) in enumerate(records):
    factor=[ONE]
    for j,(_,_,_,other) in enumerate(records):
        if j!=i:factor=pmul(factor,[neg(other),ONE])
    # H0/C0 = x * (-a/12) sum t*V*X/(s-X^3).
    # Hminus/C0 = x^2 * (-a/12) sum t^(-1)*V/(s-X^3).
    w0=scale(mul(mul(mul(A,t),V),X),Q(-1,12))
    wm=scale(mul(mul(A,power(t,2)),V),Q(-1,12))
    for k,f in enumerate(factor):N0[k]=add(N0[k],mul(w0,f));Nminus[k]=add(Nminus[k],mul(wm,f))
assert N0==list(map(el,[16,4,7]))
assert Nminus==list(map(el,[-8,34,1]))
# sum chi0(Q) e(Q)/sqrt(3) = 6 sum t^-1/(a-t) = 6a.
weighted=Z
for t,_,_,_ in records:weighted=add(weighted,scale(mul(power(t,2),inv_a_minus_t(t)),6))
assert weighted==scale(A,6)
# sum chi0^-1 e = 0: the i-orbit has sum 1+zeta+zeta^2.
assert add(add(ONE,zet),power(zet,2))==Z
out={'result':'R586 restored exact six-torsion kernels','field_basis':['1','a','a^2','zeta','a*zeta','a^2*zeta'],'relations':['a^3=4','zeta^2+zeta+1=0'],'sqrt3_removed':True,'Q_labels':'a mod3=delta*zeta^i; a mod2=zeta^j; Q=T3_delta_i+T2_j','chi0':'delta*zeta^(-i-j)','chi6':'delta*zeta^(j-i)','three_X_cubes_polynomial':[-64,48,-228,1],'H0_over_C0_numerator_in_x':'x*(7*x^6+4*x^3+16)','Hminus_over_C0_numerator_in_x':'x^2*(x^6+34*x^3-8)','common_denominator_in_x':'x^9-228*x^6+48*x^3-64','sum_chi0_e_over_sqrt3':serial(weighted),'records':[{'r':i,'X':serial(X),'y_over_sqrt3':serial(V),'X_cubed':serial(a)}for i,(_,X,V,a)in enumerate(records)],'all_exact_assertions_passed':True,'recovery_run':True,'p_adic_orbit_repeated':False}
source=Path(__file__).read_bytes();out['source_sha256']=hashlib.sha256(source).hexdigest()
target=Path(__file__).with_name('R586_six_torsion_kernel_certificate.recovered.json');target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','source_sha256':out['source_sha256'],'certificate':str(target),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}))

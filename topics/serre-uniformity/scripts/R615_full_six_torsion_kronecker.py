#!/usr/bin/env python3
"""Exact full diagonal Kronecker trace in Q[r]/(r^3-4).

One fixed weight is evaluated per invocation. This is not a prime scan.
The algebraic trace is proved by the finite ODE/series formula; its proposed
identification with the old C_k normalization is kept explicit in the output.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial
import json
from pathlib import Path
import time

ZERO = (F(0), F(0), F(0))
ONE = (F(1), F(0), F(0))

def add(a, b):
    return tuple(x+y for x,y in zip(a,b))

def scale(a, c):
    return tuple(x*c for x in a)

def mul(a, b):
    v = [F(0)]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            v[i+j] += x*y
    v[0] += 4*v[3]
    v[1] += 4*v[4]
    return tuple(v[:3])

def convolution(a, b, n):
    ans = ZERO
    for i in range(n+1):
        ans = add(ans,mul(a[i],b[n-i]))
    return ans

def Q(x):
    return str(x.numerator) if x.denominator==1 else str(x.numerator)+'/'+str(x.denominator)

def dump_element(a):
    return [Q(x) for x in a]

def shifted_sigma(N):
    # xi=beta*z, beta^2=3; these are x, y/beta and e_Q/beta.
    x = [(F(2),F(1),F(1))]
    y = [(F(-3),F(-2),F(-1))]
    e = [(F(1,3),F(1,3),F(1,6))]
    s = [ONE]
    for n in range(N):
        xx = convolution(x,x,n)
        es = convolution(e,s,n)
        x.append(scale(y[n],F(2,n+1)))
        y.append(scale(xx,F(1,n+1)))
        e.append(scale(x[n],F(-1,3*(n+1))))
        s.append(scale(es,F(1,n+1)))
    return x,y,e,s

def unshifted_inverse_sigma(H):
    # beta*sigma(xi/beta) has g2=0,g3=4/27.
    wp = [F(0)]*(H+1)
    if H:
        wp[1] = F(1,189)
    for n in range(2,H+1):
        wp[n] = sum((wp[i]*wp[n-i] for i in range(1,n)),F(0))/((n-1)*(6*n+1))
    logu = [F(0)]+[wp[n]/(6*n*(6*n-1)) for n in range(1,H+1)]
    u = [F(1)]
    for h in range(1,H+1):
        u.append(sum((i*logu[i]*u[h-i] for i in range(1,h+1)),F(0))/h)
    return wp,u

def run(k):
    assert k>=5 and k%6==5
    started = time.monotonic()
    m=k-1
    x,y,e,s = shifted_sigma(2*m+1)
    b=[ONE]
    for n in range(1,m+1):
        z=ZERO
        for j in range(1,n+1):
            z=add(z,mul(s[j],b[n-j]))
        b.append(scale(z,F(-1)))
    wp,u=unshifted_inverse_sigma((m+1)//6)
    blocks=[]
    cm=ZERO
    for h,uh in enumerate(u):
        ch=ZERO
        for j in range(m+1):
            n=2*m+1-j-6*h
            power=m-j
            if n<0 or n<power:
                continue
            ch=add(ch,scale(mul(b[j],s[n]),uh*comb(n,power)))
        cm=add(cm,ch)
        blocks.append(dict(inverse_sigma_power=6*h,inverse_sigma_coefficient=Q(uh),contribution=dump_element(ch)))
    # Tr(c_m/r)=3*[r]c_m in Q[r]/(r^3-4).
    trace=3*cm[1]
    hplus_over_cplus=F(3**m,6)*trace
    candidate_Ck=(-3)**m*factorial(m)*hplus_over_cplus
    # Exact finite series identities, not a second independent computation.
    assert mul(y[0],y[0])==scale(add(mul(mul(x[0],x[0]),x[0]),scale(ONE,-1)),F(1,3))
    for n in range(1,m+1):
        assert convolution(s,b,n)==ZERO
    return dict(
        result='R615-working',weight_parameter_k=k,diagonal_m=m,
        coefficient_algebra='Q[r]/(r^3-4)',coordinate='xi=sqrt(3)*z',
        tame_character='chi6(delta,i,j)=delta*zeta^(j-i), opposite to the R595 Hminus weight',
        initial_x=dump_element(x[0]),initial_y_over_sqrt3=dump_element(y[0]),
        initial_completed_zeta_over_sqrt3=dump_element(e[0]),
        full_Kronecker_expression='s(xi+eta)/(s(xi)*sigma_tilde(eta)), sigma_tilde=beta*sigma(eta/beta)',
        complete_inverse_sigma_blocks=blocks,
        diagonal_coefficient_in_1_r_r2=dump_element(cm),
        trace_diagonal_over_r=Q(trace),
        Hplus_m_over_Cplus=Q(hplus_over_cplus),
        normalization_candidate_Ck=Q(candidate_Ck),
        candidate_normalization_formula='(-3)^(k-1)*(k-1)!*Hplus_(k-1)/Cplus',
        proposed_Ck_identification_with_lost_R572_is_not_assumed=True,
        exact_series_identities_checked=True,
        runtime_seconds=round(time.monotonic()-started,6),
        source_sha256=sha256(Path(__file__).read_bytes()).hexdigest())

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--k',type=int,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    ans=run(args.k)
    args.output.write_text(json.dumps(ans,indent=2)+'\n')
    print(json.dumps({k:ans[k] for k in ['weight_parameter_k','diagonal_coefficient_in_1_r_r2','Hplus_m_over_Cplus','normalization_candidate_Ck','runtime_seconds']}))

if __name__=='__main__':
    main()

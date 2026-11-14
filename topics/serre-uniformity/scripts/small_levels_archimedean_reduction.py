#!/usr/bin/env python3
"""Certified first archimedean reduction for integral X_ns^+(p) points.

All finite data are exact.  Transcendental enclosures use python-flint Arb.
Only integer approximation witnesses are written; the separate verifier
reconstructs the cusp data by a different enumeration and checks them.
This does not classify integral points or certify the remaining intervals.
"""
from flint import arb, arb_mat, fmpq, ctx
from fractions import Fraction
from math import isqrt
import argparse, json, time
from pathlib import Path

LEVELS = (41, 47, 59, 83)
MARGIN_BITS = 64


def primitive_root(p):
    fac=[]; n=p-1
    for q in range(2,isqrt(n)+1):
        if n%q==0:
            fac.append(q)
            while n%q==0:n//=q
    if n>1:fac.append(n)
    return next(g for g in range(2,p) if all(pow(g,(p-1)//q,p)!=1 for q in fac))


def iupper(x):
    return int(x.upper().ceil().unique_fmpz())


def cf_convergents(x, bound):
    q=x.mid().fmpq(); a,b=int(q.p),int(q.q)
    hn2,hn1,kn2,kn1=0,1,1,0
    while b:
        t,a,b=a//b,b,a%b
        hn,kn=t*hn1+hn2,t*kn1+kn2
        if kn>bound:return
        yield hn,kn
        hn2,hn1,kn2,kn1=hn1,hn,kn1,kn


def exact_cusps(p):
    d=(p-1)//2; g=primitive_root(p)
    xi=next(a for a in range(2,p) if pow(a,d,p)==p-1)
    orbit=[(x,y) for x in range(p) for y in range(p) if (xi*x*x-y*y)%p in (1,p-1)]
    assert len(orbit)==2*(p+1)
    assert 2*len(orbit)%12==0
    assert all(sum(term(x,y) for x,y in orbit)%p==0 for term in (lambda x,y:x*x, lambda x,y:x*y, lambda x,y:y*y))
    lifts=[]
    for k in range(d):
        det=pow(g,k,p)
        a,b=next((a,b) for a in range(p) for b in range(p) if (a*a-xi*b*b)%p==det)
        lifts.append((a,xi*b%p,b,a))
    cusps=[]
    for s in range(1,d+1):
        u,v=next((u,v) for u in range(p) for v in range(p) if (u*u-xi*v*v)%p==s)
        if u:
            b,w=0,pow(u,-1,p)
        else:
            b,w=-pow(v,-1,p)%p,0
        assert (u*w-v*b)%p==1
        vs=[]; gamma=[]
        for a1,b1,c1,d1 in lifts:
            numerator=0; counts=[0]*p
            for x,y in orbit:
                xx=(x*a1+y*c1)%p; yy=(x*b1+y*d1)%p
                x2=(xx*u+yy*v)%p; y2=(xx*b+yy*w)%p
                numerator += 6*x2*x2-6*p*x2+p*p
                if x2==0: counts[y2]+=1
            vs.append(Fraction(-2*numerator,12*p*p))
            gamma.append(counts)
        assert sum(vs)==0
        assert all((vv*p).denominator==1 for vv in vs)
        cusps.append({'s':s,'matrix':[u,b,v,w], 'v':vs, 'gamma':gamma})
    return g,xi,cusps


def setup(p, precision):
    ctx.prec=precision; d=(p-1)//2; m=2
    g,xi,cusps=exact_cusps(p)
    logs={a:(2*arb.sin_pi_fmpq(fmpq(a,p))).log() for a in range(1,p)}
    E=arb_mat([[2*logs[pow(g,k,p)]]+[logs[(j*pow(g,k,p))%p]-logs[pow(g,k,p)] for j in range(2,d+1)] for k in range(d)])
    A=E.inv()
    assert (A*E-arb_mat([[int(i==j) for j in range(d)] for i in range(d)])).contains(arb_mat(d,d))
    kappa=max([sum(abs(A[i,j]) for j in range(d)).upper() for i in range(d)])
    kappa_num=iupper(kappa*2**MARGIN_BITS)
    kappa=arb(fmpq(kappa_num,2**MARGIN_BITS))
    Theta=kappa*m*p*2*(p+1)
    # Bajolet--Sha initial bound with the least divisor >=3.
    dd=next(q for q in range(3,d+1) if d%q==0)
    Omega=(arb(30)**(dd+5))*(arb(dd)**fmpq(-4*dd+9,2))*(arb(p)**(6*dd+5))*arb(p).log()**2
    S0=iupper(Omega+10000)
    for c in cusps:
        v=arb_mat([[arb(fmpq(vv.numerator,vv.denominator))] for vv in c['v']])
        w=arb_mat([[m*sum(n*logs[a] for a,n in enumerate(row) if n)] for row in c['gamma']])
        delta=A*v; theta=A*w
        assert delta[0,0].contains(0)
        assert theta[0,0].contains(m)
        c['delta']=[delta[i,0] for i in range(d)]
        c['theta']=[theta[i,0] for i in range(d)]
    return g,xi,cusps,kappa_num,Theta,S0


def reduce_cusp(p,c,Theta,S, max_rounds=6):
    ds,ts=c['delta'],c['theta']; d=len(ds)
    # Choose a rigorously nonzero slope. No division by delta_0.
    indices=sorted(range(1,d),key=lambda i:float(abs(ds[i]).mid()),reverse=True)
    i=indices[0]; assert abs(ds[i])>0
    record=[]
    for rnd in range(max_rounds):
        B=iupper(abs(ds[i])*S+abs(ts[i])+Theta)
        best=None
        for j in indices[1:]:
            delta=ds[j]/ds[i]; lam=delta*ts[i]-ts[j]
            for n,r in cf_convergents(delta, B*1000):
                rd=r*delta-n
                err=abs(rd)
                if err*B>=arb('0.5'):continue
                z=r*lam
                nearest=int((z.mid()+arb('0.5')).floor().unique_fmpz())
                zdist=abs(z-nearest)
                if not zdist<arb('0.5'):continue
                gap=zdist-B*err
                if not gap>0:continue
                gap_num=int((gap.lower()*2**MARGIN_BITS).floor().unique_fmpz())
                if gap_num<=0:continue
                certified_gap=arb(fmpq(gap_num,2**MARGIN_BITS))
                new=iupper(p*(r*(1+abs(delta))*Theta/certified_gap).log())
                if best is None or new<best['S_after']:
                    best={'i':i,'j':j,'B':str(B),'n':str(n),'r':str(r),'nearest_lambda':str(nearest),'gap_lower_numerator':gap_num,'S_after':new}
        if best is None or best['S_after']>=S:break
        best['S_before']=str(S)
        record.append(best)
        S=best['S_after']
        if rnd>0 and int(record[-1]['S_before'])-S<=1:break
    return S,record


def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--levels',default=','.join(map(str,LEVELS)))
    pa.add_argument('--precision',type=int,default=4096)
    pa.add_argument('--output',type=Path,default=Path(__file__).with_name('data')/'small_levels_archimedean_reduction.json')
    args=pa.parse_args()
    levels=tuple(map(int,args.levels.split(',')))
    assert levels and all(p in LEVELS for p in levels)
    assert args.precision>=4096
    output={'version':1,'precision_bits':args.precision,'margin_bits':MARGIN_BITS,
            'unit_exponent':2,'initial_bound':'Bajolet--Sha Theorem 1.1; additive j-series bound 10000',
            'scope':'first archimedean reduction only; remaining intervals not classified','levels':[]}
    for p in levels:
        t=time.time();g,xi,cusps,kappa_num,Theta,S0=setup(p,args.precision)
        level={'p':p,'g':g,'xi':xi,'kappa_upper_numerator':kappa_num,'S_initial':str(S0),'cusps':[]}
        for c in cusps:
            S,steps=reduce_cusp(p,c,Theta,S0)
            assert steps
            level['cusps'].append({'s':c['s'],'matrix':c['matrix'],
                'v':[[v.numerator,v.denominator] for v in c['v']],
                'gamma':[[[a,n] for a,n in enumerate(row) if n] for row in c['gamma']],
                'S_final':S,'steps':steps})
        level['S_uniform']=max(c['S_final'] for c in level['cusps'])
        output['levels'].append(level)
        print(f"p={p}: {len(cusps)} cusps, log|q|^-1 <= {level['S_uniform']}; {time.time()-t:.2f}s",flush=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,sort_keys=True,separators=(',',':'))+'\n')

if __name__=='__main__':main()

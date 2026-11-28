"""Frequency-holomorphic symbol and all-frequency original strong norm on the root collar."""
from fractions import Fraction as Q
from flint import arb,acb
import fourfold_codazzi_common_radial_potential_budget as P
import fourfold_codazzi_correlated_collar_reference as F
from fourfold_codazzi_collar_signed_geometry import joint
from fourfold_codazzi_true_phase_original_inputs import check

N=4*(2**20+1)
XI=Q(1,131072)
WIDTH=Q(1,512)


def zero_frequency_germ(c):
    """Exact z=0 analytic anchor. This is distinct from the physical state mean.

    theta=0, D=-2 beta(1+mean(u^2)-K mean(v^2)), and the finite limiting
    alpha still contributes -32 K eta alpha to W. The original signed
    background/Taylor data are read, not regenerated.
    """
    count=15
    sc={k:[v.scalar_value() for v in c[k][:count]] for k in ('K','eta','beta','k','a')}
    check(sc['K'][0]==0 and all(len(v)==count for v in sc.values()),'whole signed zero-frequency anchor')
    uu=[];vv=[];mix=[]
    for mode in range(97):
        u=[v.coefficient(mode) for v in c['u'][:count]];um=[v.coefficient(-mode) for v in c['u'][:count]]
        v=[v.coefficient(mode) for v in c['v'][:count]];vm=[v.coefficient(-mode) for v in c['v'][:count]]
        f=2 if mode else 1
        rr=P.jscale(P.jmul(u,um,count),f);ss=P.jscale(P.jmul(v,vm,count),f)
        tt=P.jscale(P.jmul(u,vm,count),mode)
        if mode:
            uu=P.jadd(uu,rr,count);vv=P.jadd(vv,ss,count);mix=P.jadd(mix,tt,count)
        else:uu,vv,mix=rr,ss,tt
    beta=sc['beta'];kk=sc['K'];eta=sc['eta'];k=sc['k'];a=sc['a']
    D=P.jscale(P.jmul(beta,P.jsub(P.jadd(P.jconst(1,count),uu,count),P.jmul(kk,vv,count),count),count),-2)
    alpha=P.jscale(P.jmul(beta,mix,count),acb(0,-1))
    abar=[z*P.ex(Q(3,2*j+3)) for j,z in enumerate(a)]
    rr=lambda x:[-v for v in P.jdr(x)]
    er,kr,ar=[P.jdiv(rr(v),v,count-1) for v in (eta,k,abar)]
    cc=[x/4-y/6-d/2 for x,y,d in zip(kr,ar,D)]
    ellq=[2*x+y/2-z/3+d for x,y,z,d in zip(er,kr,ar,D)]
    m=count-2;cross=P.jmul(cc,ellq,m);freq=P.jmul(kk,P.jmul(eta,alpha,m),m)
    W=[-y+cross[j]/2-32*freq[j] for j,y in enumerate(rr(cc))]
    kap=P.jmul(a,P.jpow(abar,Q(-1,3),m),m)
    pot=P.jdiv(W,P.jmul(kap,kap,m),m)
    bart=[acb(0)]+[-z for z in P.jpow(abar,Q(2,3),m-1)]
    return F.rho_to_t(pot,bart)


def full_frequency_potential(co,t):
    vals=F.potential_values(co,t)
    ratio=P.ex((388*XI)**2)
    # Cauchy in z on the original disk |z|<=1/9409.  Physical z=16*xi^2.
    cap=[arb(276),arb(26431),arb(276),arb(26431)/3,arb(3830956)/5]
    return [v+F.inflate(acb(0),b*ratio/(1-ratio)) for v,b in zip(vals,cap)]


def packet(geometry,co,save):
    # True complex disk is contained in this rectangle. Potential's separately
    # qualified disk error only needs to contain the same true disk values.
    v=P.ex(XI);xh=arb(0,v.upper());xi=acb(xh,xh)
    M=[arb(0),arb(0)];H=[arb(0),arb(0),arb(0)];allrows=0
    for sheet in (WIDTH,-WIDTH):
        for g in geometry[sheet]:
            t=g['T']/P.ex(F.R)
            vals=full_frequency_potential(co,t);V=vals[0]
            x,y,T=g['x'],g['y'],g['T']
            det=x*x+T*y*y-xi*xi*y*y*V
            check(abs(det).lower()>0,'true small complex-frequency and angular collar inverse gap')
            entries=(x/det,y*(T-xi*xi*V)/det,y/det)
            H=[max(old,abs(z).upper()) for old,z in zip(H,entries)]
            for eps in (1,-1):
                w=joint(g,xi,*vals,eps)
                M=[max(m,abs(z).upper()) for m,z in zip(M,w)]
                for z in (T,*vals,*entries,*w):save(z)
                allrows+=1
    h=max((H[0]+H[2]/128).upper(),(H[0]+128*H[1]).upper());norm=(M[0]+M[1]/128).upper()
    s=P.ex(WIDTH);n=arb(N);p=arb(4)/17
    k=(h*h+h*h*h/n*(2/s+8*p/(s*s))
       +P.ipow(h,4)/(n*n)*(4/(s*s)+54*p/P.ipow(s,3)+arb(256)/(17*P.ipow(s,4))))
    # Physical P at the final output gives |P Lambda^-2|<=1/17. All natural
    # modes and both signs remain inside the complete reference and B matrix.
    prof=arb(9)/5*arb(2).sqrt()/(1-1/(n*v))
    mix=(k.log()*P.ex(Q(5,6))).exp()
    weight=(-n.log()/6+P.ex(Q(2,3))*(1+1/(n*n)).log()).exp()
    val=prof*norm*weight*mix
    check(val.is_finite() and allrows==4*len(geometry[WIDTH]),'all infinite inputs and both true physical rows')
    return val.upper(),M,h,k.upper(),allrows

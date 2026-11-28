"""Exact one-sided 193-direction radial coefficients and full exterior free-wave sources."""
from math import comb
from fractions import Fraction as Q
from flint import arb,arb_series
from fourfold_codazzi_signed_density_transport_arithmetic import Jet,LP,exact,hull
from fourfold_codazzi_true_phase_original_inputs import CONTROL,DELTA,check
from fourfold_codazzi_true_phase_signed_speed import coordinate_polys,restricted
from fourfold_codazzi_genuine_strong_radial_inputs import take,inward
from fourfold_codazzi_genuine_signed_free_wave import Mixed,angle,advect,wave,radial_gauge,physical_geometry
from fourfold_codazzi_true_ratio_label_mesh import mesh

ORDER=5
BINS=32


def scalar(c):
    return Mixed([arb_series([p.scalar()],prec=ORDER+1-i) for i,p in enumerate(c.c)])


def circles(c):
    out=[[] for _ in range(BINS)]
    for d,p in enumerate(c.c):
        for row,j in zip(out,mesh(p,ORDER-d,cells=BINS)):row.append(arb_series(j,prec=len(j)))
    return [Mixed(row) for row in out]


def fields(inp,z,km,cell,l,r):
    _,_,k,i=cell;origin,models=inp.rows[i];x=hull(l-origin,r-origin);off=hull(l-inp.nodes[k],r-inp.nodes[k])
    base=inp.piece(k);sym=arb(0,exact(DELTA))
    direction=[coordinate_polys([arb(float(v)) for v in z[j,k]]) for j in (3,2,1,0)]
    def bg(which,repair):
        terms=[]
        for j in range(4):
            a=LP()
            for m in range(3,j-1,-1):
                coefficient=base[m][which]
                if j:coefficient+=direction[m][which]*sym
                a=a*off+coefficient*comb(m,j)
            terms.append(a if j else a+repair)
        return Jet(terms)
    def intrinsic(name):
        v=km[i] if name=='K' else models[name]
        return Jet([restricted(v,x,j) for j in range(4)])
    u=bg(0,inp.du);v=bg(1,inp.dv)+intrinsic('s')
    K=intrinsic('K');q=restricted(models['q'],x,0);gamma=intrinsic('gamma');beta=intrinsic('beta')
    check(q.lower()>0 and K.c[0].scalar().overlaps(-q*q),'original signed scalar on the whole exterior piece')
    K.c[0]=LP.const(K.c[0].scalar().intersection(-q*q))
    a,bb=CONTROL
    if a<=cell[0] and cell[1]<=bb:
        zt=Jet([hull((l-a)/(bb-a),(r-a)/(bb-a)),exact(1/(bb-a)),0,0,0])
        bump=4096*(zt*(1-zt))**6;w=take(bump,4)
        K=(-sym*w).exp()*(K+sym*intrinsic('T')*bump.derivative())
        gamma=gamma*(w*(sym/2)).exp()
    eta=-gamma*v.mean()
    q=(-K).sqrt();b=eta*q
    S=u*u+K*v*v;d=-beta*S.primitive();g=beta*S.mean()
    ell=-2*beta*u*v;e=-beta*(1+3*u*u+K*v*v);bloc=beta*(1-u*u-3*K*v*v)
    K2,eta2,d2,be2,u2,v2,ell2,e2,b0=[take(y,3) for y in (K,eta,d,beta,u,v,ell,e,bloc)]
    mlog=eta.derivative()/eta2;dp=d2.dphi();tq=dp+e2+mlog
    rq=ell.derivative()-d2*ell2.dphi()+e2.dphi()*eta2-2*be2*eta2*u2.dphi()*u2-ell2*(dp+mlog)
    v0=tq*b0-bloc.derivative()+d2*b0.dphi()-(ell2*ell2-4*be2*eta2*v2*u2.dphi())*K2
    th=rq/eta2-2*be2*K2*v2*v2.dphi()
    vals={k:scalar(inward(s)) for k,s in (('q',q),('b',b),('g',g))}
    vals.update({k:circles(inward(s)) for k,s in (('d',d),('T0',tq+b0),('V0',v0),('theta',th))})
    eta0=eta.c[0].scalar();up=u.c[0];vp=v.c[0]
    p=arb(17).sqrt()/(4*eta0.lower());U,U1=up.a(),up.a(1);V,V1,V2=vp.a(),vp.a(1),vp.a(2)
    lm=(2*abs(beta.c[0].scalar()).upper()*(U*V+U1*V+U*V1+(V1+V2)*(U+U1)/4)).upper()
    jj=p+p*p*lm*(1+exact(Q(7,5))*exact(Q(1855913,500000)))
    return vals,jj.upper()


def geom(rows,errors,tau,low):
    def evalpoly(v):
        p=LP()
        for z in reversed(v):p=p*tau+z
        return p
    plus,minus=rows
    x=evalpoly([(a+b)/2 for a,b in zip(plus,minus)]);w=evalpoly([(b-a)/2 for a,b in zip(plus,minus)])
    xd=[(a+b)/2 for a,b in zip(errors[0],errors[1])]
    sy=mesh(x,ORDER+1,xd,cells=BINS);sw=mesh(w,ORDER+1,errors[2],cells=BINS)
    br=[mesh(evalpoly(v),ORDER+1,e,cells=BINS) for v,e in zip(rows,errors[:2])]
    def pos(v,floor):
        check(v.upper()>=floor.lower(),'same complete positive pointwise lower')
        return max(v.lower(),floor.lower()).union(v.upper())
    def slope(v,identity):
        z=[k*t for k,t in enumerate(v) if k]
        if identity:z[0]=pos(1+z[0],exact(Q(1,27)))
        return arb_series(z,prec=len(z))
    out=[]
    for i,(xx,ww) in enumerate(zip(sy,sw)):
        xx=slope(xx,True);tt=slope(ww,False)
        pp,pm=[slope(v[i],True) for v in br]
        ww[0]=pos(ww[0],(exact(Q(2,3))*low*low.sqrt()).lower())
        xj=[xx[k].intersection((pp[k]+pm[k])/2) for k in range(ORDER+1)]
        tj=[tt[k].intersection((pm[k]-pp[k])/2) for k in range(ORDER+1)]
        out.append((arb_series(xj,prec=ORDER+1),arb_series(tj,prec=ORDER+1),
                    arb_series(ww[:ORDER+1],prec=ORDER+1),pp,pm))
    return out


def exterior_pair(geo,raw,i,ratio):
    xx,tt,om,pp,pm=geo;b=raw['b'];d=raw['d'][i];V0=raw['V0'][i];T0=raw['T0'][i];theta=raw['theta'][i]
    x,t,omega=physical_geometry(xx,tt,om,d,b)
    s=(omega*exact(Q(3,2))).power(Q(1,3));T=-s*s;Qf=b/s
    G=radial_gauge(2*raw['g'],3,ORDER+1)*(s/raw['q']).power(Q(1,2))
    a=G*(x*x+t*t);w=2*G*x*t/s
    def A0(z):return wave(z,d,b)+T0*advect(z,d)+V0*z
    fa=A0(a)-theta*Qf*T*w;fb=A0(w)+theta*Qf*a
    bk=(b.rho()-b*d.phi()).c[0];theta0=(theta*Qf).c[0]
    aa=bb=ga=gb=None
    for sign,p0,r in zip((1,-1),(pp,pm),ratio):
        p=x-sign*t
        arr=[p.c[0][j].intersection(p0[j]) for j in range(p.c[0].prec)]
        p=Mixed([arb_series(arr,prec=p.c[0].prec),*p.c[1:]])
        F=(-sign*fa+s*fb)/(2*b*G*p*p*p)
        f=F.c[0];opposite=advect(F,d-sign*b).c[0]
        rp=angle(r)
        def prod(z):
            zv=z.c[0];zm=advect(z,d-sign*b).c[0];zp=advect(z,d+sign*b).c[0]
            rz=A0(z).c[0]
            rf=rz*r+zv*(opposite-sign*bk*rp)+zm*f+zp*(f-2*sign*b.c[0]*rp)+T0.c[0]*zv*(f-sign*b.c[0]*rp)
            return zv*r,rf,sign*zv,sign*rz
        M=G*p*p/2
        av,af,ag,agf=prod(M);bv,bf,bg,bgf=prod(sign*M/s)
        z=(af+theta0*T.c[0]*bv,bf-theta0*av,agf+theta0*T.c[0]*bg,bgf-theta0*ag)
        if aa is None:aa,bb,ga,gb=z
        else:aa,bb,ga,gb=(a+b for a,b in zip((aa,bb,ga,gb),z))
    check(min(v.prec for v in (aa,bb,ga,gb))>=3,'complete signed output through second physical-angle derivative')
    return (aa,bb),(ga,gb),s.c[0]

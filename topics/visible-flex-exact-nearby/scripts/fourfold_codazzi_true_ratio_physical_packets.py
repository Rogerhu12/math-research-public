"""All signed real first-ratio inputs on a complete physical subcell."""
from math import factorial
from fractions import Fraction
from flint import arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact,hull
from fourfold_codazzi_true_phase_original_inputs import CONTROL,DELTA,check
from fourfold_codazzi_true_phase_signed_speed import restricted,scalar_model
from fourfold_codazzi_true_ratio_first_raw import first_raw
from fourfold_codazzi_true_damped_radial_moments import propagate,tightened,direct_first
from fourfold_codazzi_true_ratio_label_mesh import (
    M,CELLS,series,derivative,mesh,geometry,label_bins,label_jet)


def positive(v,bound):
    check(v.upper()>=bound.lower(),"authenticated lower and actual whole-bin enclosure")
    return max(v.lower(),bound.lower()).union(v.upper())


def positive_power(v,exponent):
    check(v[0].lower()>0,"qualified positive leading angular value")
    return (v.log()*exact(exponent)).exp()


def values(v,n=M+1):
    check(v.prec>=n,"all true physical angular derivatives")
    return [v[j] for j in range(n)]


def kth_second(inp,models,cell,l,r):
    _,_,_,i=cell;centre,row=inp.rows[i]
    x=hull(l-centre,r-centre);m=models[i]
    k,kr,krr=restricted(m,x,0),restricted(m,x,1),2*restricted(m,x,2)
    a,b=CONTROL
    if cell[0]>=a and cell[1]<=b:
        t=hull((l-a)/(b-a),(r-a)/(b-a));v=t*(1-t);w1=1-2*t
        # Polynomial powers are ordinary products, including when the
        # signed interval 1-2t is centered at zero.
        v2=v*v;v3=v2*v;v4=v2*v2;w12=w1*w1
        w=4096*v3*v3;wp=exact(Fraction(24576)/(b-a))*v4*v*w1
        wpp=exact(Fraction(24576)/(b-a)**2)*v4*(5*w12-2*v)
        wppp=exact(Fraction(24576)/(b-a)**3)*(20*v3*w12*w1-30*v4*w1)
        T,Tr,Trr=restricted(row["T"],x,0),restricted(row["T"],x,1),2*restricted(row["T"],x,2)
        z=arb(0,exact(DELTA))
        base=k+z*T*wp
        one=kr+z*(Tr*wp+T*wpp)
        two=krr+z*(Trr*wp+2*Tr*wpp+T*wppp)
        krr=(-z*w).exp()*(two-2*z*wp*one+(z*z*wp*wp-z*wpp)*base)
    return krr


def scalar_moment(previous,source,h,rho0):
    a=2;z=a*(1+h/rho0).log();w=(-z).exp()
    # Intersect two complete representations of the positive source mass.
    m=(1-w).intersection((z*(-z).exp()).lower().union(z.upper()))
    end=w*previous+m*source/2
    return previous.union(end),end


def signed_real_packet(x,v,xp,vp,s,sp,b,b_rho,dp,rho,B,Br,A,A1,Ap,k,k1,raw,p):
    # Divide R,U and their first-row complex weight by i*epsilon. The
    # negative real reflection and the other carrier sign are recovered
    # from the proved symmetry, including every true initial ratio.
    ix=b*vp-dp*x;iv=b*xp-dp*v;isb=b*x/(2*s*s)
    a=x*x+v*v;w=2*x*v/s
    ia=2*(x*ix+v*iv);aw=2*(ix*v+x*iv)/s-w*isb/s
    pa=2*(x*xp+v*vp);pw=2*(xp*v+x*vp)/s-w*sp/s
    lg=2*raw["beta_mean_S"]+A1/(6*A)-k1/(4*k)
    pg=Ap/(6*A);lt=lg+b*pg
    ad=ia+lg*a;wd=aw+lg*w
    ap=pa+pg*a;wp=pw+pg*w
    am=ad-b*ap;wm=wd-b*wp
    C=1/(2*b*p*p*p)
    c0=-C;c1=s*C
    corr=c0*am+c1*wm
    r0=3*dp-Br/B-1/(2*rho);r1=3*dp-Br/B+(A1+b*Ap)/(3*A)
    dr=b_rho-b*dp;theta=raw["theta"];T=-s*s
    fa=dr*ap+raw["T0"]*ad+raw["V0"]*a-theta*(b/s)*T*w
    fw=dr*wp+raw["T0"]*wd+raw["V0"]*w+theta*(b/s)*a
    rhs=c0*fa+c1*fw-c0*(r0-lt)*am-c1*(r1-lt)*wm
    return values(corr),values(rhs)


def prepare(inp,zsource,kmodels,cell,l,r,rhos,rows,errs,tau,previous):
    h=exact(r-l);rho0,rho=rhos
    raw=first_raw(inp,zsource,cell,l,r)
    xx,ww,plus=geometry(rows,errs,tau)
    d=mesh(raw["d"],M+1)
    tables={k:mesh(raw[k],M) for k in ("T0","V0","theta")}
    b=raw["b"];k=-raw["K"]/rho;B=b/rho.sqrt()
    k_direct=(raw["K_r"]-k)/rho
    if previous is None:
        k1=k_direct;k_end=k1
    else:
        ks,k_end=scalar_moment(previous["k1"],-kth_second(inp,kmodels,cell,l,r),h,rho0)
        check(ks.overlaps(k_direct),"direct k1 and its positive-weight moment agree")
        k1=ks.intersection(k_direct)
        # The direct whole-cell enclosure also contains the departure value.
        k_end=k_end.intersection(k_direct)
    Br=B*(-raw["eta_r"]/raw["eta"]+k1/(2*k))
    fields=[];forces=[];directs=[]
    lower=exact(Fraction(1,27))
    for j in range(CELLS):
        x=derivative(xx[j]);x[0]+=1
        v=derivative(ww[j]);omega=ww[j].copy()
        # Reuse the observed positive original cut omega and its exact common
        # positive source along L. A running lower improves deeper cells.
        gapfloor=exact(Fraction(4,10**8)) if previous is None else previous["omega_lower"]
        omega[0]=positive(omega[0],gapfloor)
        p=derivative(plus[j]);p[0]=positive(1+p[0],lower)
        x[0]=positive(x[0],lower)
        # The same exact p=x-v, and its complete derivative jets, are known
        # in two signed representations at the same physical angle.
        for t in range(len(p)):
            check(p[t].overlaps(x[t]-v[t]),"same genuine positive ray jet")
            p[t]=p[t].intersection(x[t]-v[t])
        A=[3*y/(2*rho*rho.sqrt()) for y in omega]
        ax=direct_first(A[:M+1],B,x[:M+1],rho)
        sx,sv=series(x),series(v);svphi=series(derivative(v));dp=series(derivative(d[j]))
        force=Br*sx+B*(b*svphi-dp*sx)
        forces.append(values(force));directs.append(ax)
        fields.append((x,v,p,A,omega,dp))
    if previous is None:
        a_whole=[max(abs(z[m]).upper() for z in directs) for m in range(M+1)]
        a_end=a_whole
    else:
        Ds=[max(abs(z[m]).upper() for z in d) for m in range(M+1)]
        F=[max(abs(z[m]).upper() for z in forces) for m in range(M+1)]
        a_whole,a_end=propagate(previous["A1"],F,Ds,Ds[1],h,rho0,Fraction(5,2),Fraction(3,2))
        a_end=[min(v,max(abs(z[m]).upper() for z in directs)).upper() for m,v in enumerate(a_end)]
    source=[];corr=[];pfields=[];images=[]
    for j,(x,v,p,A,omega,dp) in enumerate(fields):
        A1=series(tightened(directs[j],a_whole))
        s=positive_power(series(omega)*exact(Fraction(3,2)),Fraction(1,3))
        sp=series(v)/(2*s*s)
        data={n:series(t[j]) for n,t in tables.items()};data["beta_mean_S"]=raw["beta_mean_S"]
        co,fo=signed_real_packet(series(x),series(v),series(derivative(x)),series(derivative(v)),s,sp,
            b,raw["b_rho"],dp,rho,B,Br,series(A),A1,series(derivative(A)),k,k1,data,series(p))
        corr.append(co);source.append(label_jet(fo,p));pfields.append(p)
        images.append(label_bins(j,plus[j][0]))
    low=exact(Fraction(4,10**8)) if previous is None else previous["omega_lower"]
    minx=min(z[0][0].lower() for z in fields)
    nextstate={"k1":k_end,"A1":a_end,"omega_lower":(low+h.lower()*b.lower()*minx).lower()}
    return images,pfields,corr,source,fields,nextstate,{"k":k,"beta_mean_S":raw["beta_mean_S"],"K":raw["K"]}

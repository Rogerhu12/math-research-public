#!/usr/bin/env python3
"""Ordered mixed-jet majorants for the two genuine neighbors of the root piece.

Every entry is a uniform strip supremum or a separately declared joint Fourier
majorant. Jets are divided by p!q!. The two columns bound the reference and the
difference, never two unrelated absolute endpoints. No mathematics runs at import.
"""
from __future__ import annotations
import math
from fractions import Fraction as Q
from flint import arb,acb
import fourfold_codazzi_root_Laurent_Taylor_algebra as L

def ex(q):return L.ex(Q(q))
def up(v):return abs(v).upper()
def real_ball(v):
    if isinstance(v,str):return arb(v)
    if isinstance(v,dict) and "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    if isinstance(v,dict) and "ball" in v:return arb(v["ball"])
    raise ValueError("invalid original real interval record")
def ipow(x,n):
    if n<0:raise ValueError("negative integer power needs a paid positive gap")
    y=arb(1)
    for _ in range(n):y*=x
    return y
def power(x,p):
    if not x>0:raise ValueError("a real majorant power lost its positive input")
    return (x.log()*ex(p)).exp()
def keys(n,pmax):
    return [(p,q) for p in range(min(n,pmax)+1) for q in range(n-p+1)]
def zero(n=8,pmax=3):
    return J(n,pmax,{k:(arb(0),arb(0)) for k in keys(n,pmax)})
def scalar(value,n=8,pmax=3,delta=0):
    r=zero(n,pmax);r.a[0,0]=(up(value),up(delta));return r

class J:
    """Normalized mixed jets (reference, difference), with a complete simplex."""
    def __init__(self,n,pmax,a):
        self.n=int(n);self.pmax=min(int(pmax),self.n)
        self.a={k:(up(a[k][0]),up(a[k][1])) for k in keys(self.n,self.pmax)}
    def crop(self,n,pmax=None):
        pmax=self.pmax if pmax is None else pmax
        if n>self.n or min(n,pmax)>self.pmax:raise ValueError("unpaid mixed jet")
        return J(n,pmax,self.a)
    def get(self,p=0,q=0,which="bar",ordinary=True):
        b,d=self.a[p,q];v=b if which=="bar" else d if which=="delta" else b+d
        return (v*(math.factorial(p)*math.factorial(q) if ordinary else 1)).upper()
    def component(self,which):
        return J(self.n,self.pmax,{k:(self.get(*k,which,ordinary=False),arb(0)) for k in self.a})
    def with_difference(self,d):
        n=min(self.n,d.n);p=min(self.pmax,d.pmax)
        return J(n,p,{k:(self.a[k][0],d.a[k][0]) for k in keys(n,p)})
    def replace_bar(self,b):
        n=min(self.n,b.n);p=min(self.pmax,b.pmax)
        return J(n,p,{k:(min(self.a[k][0],b.a[k][0]).upper(),self.a[k][1]) for k in keys(n,p)})
    def scale(self,x):
        x=up(x);return J(self.n,self.pmax,{k:(x*b,x*d) for k,(b,d) in self.a.items()})
    def __add__(self,other):
        if not isinstance(other,J):other=scalar(other,self.n,self.pmax)
        n=min(self.n,other.n);p=min(self.pmax,other.pmax)
        return J(n,p,{k:(self.a[k][0]+other.a[k][0],self.a[k][1]+other.a[k][1]) for k in keys(n,p)})
    __radd__=__add__
    def __mul__(self,other):
        if not isinstance(other,J):return self.scale(other)
        n=min(self.n,other.n);pm=min(self.pmax,other.pmax);out={}
        for p,q in keys(n,pm):
            b=arb(0);d=arb(0)
            for i in range(p+1):
                for j in range(q+1):
                    a0,a1=self.a[i,j];b0,b1=other.a[p-i,q-j]
                    b+=a0*b0;d+=a1*b0+a0*b1+a1*b1
            out[p,q]=(b.upper(),d.upper())
        return J(n,pm,out)
    __rmul__=__mul__
    def deriv(self,p=0,q=0):
        n=self.n-p-q;pm=self.pmax-p
        if n<0 or pm<0:raise ValueError("an unproved mixed derivative was requested")
        out={}
        for i,j in keys(n,pm):
            f=math.factorial(i+p)//math.factorial(i)*math.factorial(j+q)//math.factorial(j)
            b,d=self.a[i+p,j+q];out[i,j]=(b*f,d*f)
        return J(n,pm,out)
    def fractional(self,p,gap_bar,gap_actual):
        """Finite Faà di Bruno with the same analytic power on the segment.

        The caller proves the whole connecting segment gap. Real powers have
        modulus |z|^p; no rounded upper endpoint is used in a denominator.
        """
        p=Q(p);b,d=self.a[0,0]
        if not (gap_bar>0 and gap_actual>0):raise ValueError("a complete homotopy gap was lost")
        bg=gap_bar.lower();ag=min(gap_bar,gap_actual).lower()
        bm=power(bg if p<0 else b,p).upper()
        exponent=p-1
        segment=max(b,b+d).upper() if exponent>=0 else ag
        dm=(abs(ex(p))*power(segment,exponent)*d).upper()
        inv0=scalar(1/bg,self.n,self.pmax,delta=(d/(bg*gap_actual.lower())).upper())
        nonzero=J(self.n,self.pmax,{k:((arb(0),arb(0)) if k==(0,0) else v) for k,v in self.a.items()})
        h=nonzero*inv0
        total=scalar(1,self.n,self.pmax);term=scalar(1,self.n,self.pmax);coefficient=Q(1)
        for k in range(1,self.n+1):
            term=term*h;coefficient*=Q(p-k+1,k)
            if coefficient:total=total+term.scale(abs(ex(coefficient)))
        return scalar(bm,self.n,self.pmax,dm)*total
    def exponential(self):
        """Entire exponential; used with exact zero reference logarithm."""
        b,d=self.a[0,0]
        bm=b.exp().upper();dm=(bm*(d.exp()-1)).upper()
        nonzero=J(self.n,self.pmax,{k:((arb(0),arb(0)) if k==(0,0) else v) for k,v in self.a.items()})
        total=scalar(1,self.n,self.pmax);term=scalar(1,self.n,self.pmax)
        for k in range(1,self.n+1):
            term=term*nonzero;total=total+term.scale(ex(Q(1,math.factorial(k))))
        return scalar(bm,self.n,self.pmax,dm)*total
    def record(self):
        return dict(normalization="partial_rho^p partial_phi^q / (p! q!)",
            total_order=self.n,radial_order=self.pmax,
            reference={str(p)+","+str(q):L.rec(v[0],80) for (p,q),v in self.a.items()},
            difference={str(p)+","+str(q):L.rec(v[1],80) for (p,q),v in self.a.items()})
    @classmethod
    def restore(cls,v):
        if v["normalization"]!="partial_rho^p partial_phi^q / (p! q!)":
            raise ValueError("changed mixed-jet normalization")
        n,pm=v["total_order"],v["radial_order"]
        return cls(n,pm,{k:(arb(v["reference"][str(k[0])+","+str(k[1])]),
            arb(v["difference"][str(k[0])+","+str(k[1])])) for k in keys(n,pm)})

def add_many(values):
    if not values:raise ValueError("empty ordered sum")
    out=values[0]
    for v in values[1:]:out=out+v
    return out

def radial_factor(h,H,power_value,n=8,pmax=3):
    """Absolute mixed jets of the same chosen power of strict-side rho."""
    if not (h>0 and H>=h):raise ValueError("strict radial factor needs the entire true-root gap")
    p=Q(power_value);out=zero(n,pmax);fall=Q(1)
    for j in range(min(n,pmax)+1):
        if j:fall*=p-j+1
        if not fall:continue
        e=p-j;base=H if e>=0 else h
        out.a[j,0]=((abs(ex(fall))*power(base,e)/math.factorial(j)).upper(),arb(0))
    return out

def mixed_sup_from_norms(norms,H,R,S,sigma,M,n=8,pmax=3):
    """Complete finite Fourier coefficients plus the full holomorphic tail.

    norms[d][q] is already sum_j sup_parameter |coefficient_j| (4|j|)^q
    exp(4|j|sigma). The radial sum is taken after each coefficient upper.
    """
    N=len(norms)-1
    if not (ex(H)<ex(R) and Q(sigma)<Q(S)):raise ValueError("nonpositive reference Taylor loss")
    x=ex(H)/ex(R);gap=ex(Q(S)-Q(sigma));out={}
    for p,q in keys(n,pmax):
        if p>N:raise ValueError("unpaid finite radial prefix")
        finite=sum((ex(math.comb(k,p))*norms[k][q]*ipow(ex(H),k-p)
            /math.factorial(q) for k in range(p,N+1)),arb(0))
        # sum_{k>=N+1} binom(k,p) x^(k-p). Differentiate x^(N+1)/(1-x).
        tail=arb(0)
        for j in range(p+1):
            if j>N+1:continue
            tail+=ex(math.comb(N+1,j))*ipow(x,N+1-j)/ipow(1-x,p-j+1)
        tail=M*tail/ipow(ex(R),p)/ipow(gap,q)
        out[p,q]=((finite+tail).upper(),arb(0))
    return J(n,pmax,out)

def angle_cauchy(value,loss,n=8,pmax=0):
    if not loss>0:raise ValueError("the actual-ray supremum needs a positive angle loss")
    out=zero(n,pmax)
    for q in range(n+1):out.a[0,q]=((value/ipow(loss,q)).upper(),arb(0))
    return out

def intrinsic_boxes(raw,third,interval,Rc,n=3):
    """Only old 0..15 root derivatives and old whole complex third derivatives."""
    a,b=map(Q,interval);rho=ex(a).union(ex(b));H=max(abs(a),abs(b));x=ex(H/Rc)
    if not (x<1 and n<=3):raise ValueError("intrinsic Taylor consumption left its original disk")
    result={}
    for key in ("K","beta","gamma","s"):
        if len(raw[key])!=16:raise ValueError("a complete original intrinsic degree is missing")
        coeff=[real_ball(v)*
            ex(Q((-1)**j,math.factorial(j))) for j,v in enumerate(raw[key])]
        if key=="K":
            if not coeff[0].contains(0):raise ValueError("the exact true-root identity is inconsistent")
            coeff[0]=arb(0)
        M=real_ball(third[key]).upper();jets=[]
        for p in range(n+1):
            finite=arb(0)
            for j in range(15,p-1,-1):
                finite=finite*rho+coeff[j]*(math.factorial(j)//math.factorial(j-p))
            den=(16*15*14,15*14,14,1)[p]
            tail=(M*ipow(ex(Rc),3-p)*ipow(x,16-p)/(den*(1-x))).upper()
            jets.append(finite+arb(0,tail))
        result[key]=jets
    coeff=[-real_ball(raw["K"][j+1])*ex(Q((-1)**(j+1),math.factorial(j+1))) for j in range(15)]
    M=real_ball(third["K"]).upper();kj=[]
    for p in range(4):
        finite=arb(0)
        for j in range(14,p-1,-1):
            finite=finite*rho+coeff[j]*(math.factorial(j)//math.factorial(j-p))
        tail=(M*ipow(ex(Rc),2)*ipow(x,15)/(14*15*16*(1-x)) if p==0 else
              M*ex(Rc)*ipow(x,14)/(14*16*(1-x)) if p==1 else
              M*ipow(x,13)/(16*(1-x)) if p==2 else
              M*ipow(x,12)/(ex(Rc)*(1-x)))
        kj.append(finite+arb(0,tail.upper()))
    if not kj[0].lower()>0:raise ValueError("the full divided curvature loses its real positive gap")
    result["k"]=kj
    for p in range(4):
        related=-rho*kj[p]-(p*kj[p-1] if p else 0)
        if not related.overlaps(result["K"][p]):raise ValueError("same intrinsic K and divided k jets are disjoint")
        result["K"][p]=result["K"][p].intersection(related)
    return result

def lp_derivative_product(a,b):
    count=min(len(a),len(b))
    return [sum((a[j]*b[p-j].scale(math.comb(p,j)) for j in range(p+1)),L.LP.zero())
        for p in range(count)]
def lp_add(a,b):return [x+y for x,y in zip(a,b)]
def lp_scale(a,s):return [v.scale(s) for v in a]
def lp_mean(a):return [L.LP.scalar(v.mean()) for v in a]
def lp_jet(values,width,n=8,pmax=3):
    pmax=min(pmax,len(values)-1);out={}
    for p,q in keys(n,pmax):
        out[p,q]=(values[p].norm(width,q)/(math.factorial(p)*math.factorial(q)),arb(0))
    return J(n,pmax,out)
def lp_scalar_jet(values,n=8):
    return lp_jet([L.LP.scalar(acb(v)) for v in values],Q(0),n,len(values)-1)

def evaluate_old_background(old_series,intrinsic,rho):
    """Reuse the saved complete cubic root prefix; only intrinsic s has a tail."""
    u=[];v=[]
    for p in range(4):
        uu=L.LP.zero();vv=L.LP.zero()
        for j in range(3,p-1,-1):
            uu=uu.scale(acb(rho))+old_series["u"][j].scale(math.factorial(j)//math.factorial(j-p))
            c=old_series["v"][j]-old_series["s"][j]
            vv=vv.scale(acb(rho))+c.scale(math.factorial(j)//math.factorial(j-p))
        u.append(uu);v.append(vv+L.LP.scalar(acb(intrinsic["s"][p])))
    return u,v

def background_pairs(ubar,vbar,du,dv,intrinsic,width,n=8):
    """Full signed old-circle products are formed before any Fourier upper sum."""
    K=[L.LP.scalar(acb(v)) for v in intrinsic["K"]]
    beta=[L.LP.scalar(acb(v)) for v in intrinsic["beta"]]
    gamma=[L.LP.scalar(acb(v)) for v in intrinsic["gamma"]]
    ubuv=lp_derivative_product(ubar,du);vbdv=lp_derivative_product(vbar,dv)
    ds=lp_add(lp_scale(ubuv,2),lp_derivative_product(du,du))
    ds=lp_add(ds,lp_derivative_product(K,lp_add(lp_scale(vbdv,2),lp_derivative_product(dv,dv))))
    sb=lp_add(lp_derivative_product(ubar,ubar),lp_derivative_product(K,lp_derivative_product(vbar,vbar)))
    db=lp_scale(lp_derivative_product(beta,[x.primitive() for x in sb]),-1)
    dd=lp_scale(lp_derivative_product(beta,[x.primitive() for x in ds]),-1)
    mb,dm=lp_mean(vbar),lp_mean(dv)
    eb=lp_scale(lp_derivative_product(gamma,mb),-1)
    de=lp_scale(lp_derivative_product(gamma,dm),-1)
    out={}
    for key,ref,diff in (("u",ubar,du),("v",vbar,dv),("S",sb,ds),("d",db,dd),
        ("eta",eb,de),("meanS",lp_mean(sb),lp_mean(ds)),("mean",mb,dm)):
        out[key]=lp_jet(ref,width,n).with_difference(lp_jet(diff,width,n))
    for key in ("K","beta","gamma","s","k"):
        out[key]=lp_scalar_jet(intrinsic[key],n)
    # eta is radial. Its full signed interval, not a Fourier norm, supplies the gap.
    eb0=eb[0].scalar_value();de0=de[0].scalar_value()
    bg=eb0.real.lower();ag=(eb0+de0).real.lower()
    if not (bg>0 and ag>0):raise ValueError("the same real radial eta loses its positive gap")
    out["eta_gap_bar"]=bg;out["eta_gap_actual"]=ag;out["k_gap"]=intrinsic["k"][0].lower()
    return out

def local_coefficients(c):
    u,v,K,b,eta,d=[c[k] for k in ("u","v","K","beta","eta","d")]
    ei=eta.fractional(-1,c["eta_gap_bar"],c["eta_gap_actual"])
    logeta=eta.deriv(1)*ei
    ell=(b*u*v).scale(2)
    epoly=b*(scalar(1,u.n,u.pmax)+u*u*3+K*v*v)
    bloc=b*(scalar(1,u.n,u.pmax)+u*u+K*v*v*3)
    tQ=logeta+d.deriv(0,1)+epoly
    T0=logeta+(b*c["meanS"])*4+d.deriv(0,1)*5
    def D(w):return w.deriv(1)+d*w.deriv(0,1)
    rq=D(ell)+eta*epoly.deriv(0,1)+(b*eta*u.deriv(0,1)*u)*2+ell*(logeta+d.deriv(0,1))
    vartheta=rq*ei+(b*K*v*v.deriv(0,1))*2
    V0=tQ*bloc+D(bloc)+K*(ell*ell+(b*eta*v*u.deriv(0,1))*4)
    c2=d*d+eta*eta*K
    c1=d.deriv(1)+d*d.deriv(0,1)+T0*d
    return dict(T0=T0,V0=V0,vartheta=vartheta,c2=c2,c1=c1,d=d,
        ell=ell,epoly=epoly,bloc=bloc,rQ=rq,tQ=tQ,
        signed_definitions_retained_by_ordered_absolute_difference=True)

def complete_local(w,c,Qphase,T):
    """Nraw=Lw, never the normalized L0w. Signs disappear only after differences."""
    result=[]
    for h in range(2):
        r=w[h].deriv(2)+(c["d"]*w[h].deriv(1,1))*2
        r=r+c["c2"]*w[h].deriv(0,2)+c["c1"]*w[h].deriv(0,1)
        r=r+c["T0"]*w[h].deriv(1)+c["V0"]*w[h]
        r=r+c["vartheta"]*Qphase*(T*w[1] if h==0 else w[0])
        result.append(r)
    return result

def common_reference_powers(ref,Amin,h,H):
    A=ref["A"];T=radial_factor(h,H,1,A.n,A.pmax)*A.fractional(Q(2,3),Amin,Amin)
    tau=radial_factor(h,H,Q(1,2),A.n,A.pmax)*A.fractional(Q(1,3),Amin,Amin)
    theta=ref["chi"]+(radial_factor(h,H,Q(3,2),A.n,A.pmax)*A).scale(ex(Q(2,3)))
    # The omitted nonperiodic phi is never used as a bounded function; only its derivatives enter.
    if (0,1) in theta.a:theta.a[0,1]=(theta.a[0,1][0]+1,arb(0))
    return T,tau,theta

def phase_comparison(c,ref,h,H,length,width_wide,width_flow,width_jet,Amin,side,
        local_coefficients=None,local_reference=None):
    """N.5--N.12 on the actual rays, including the principal radial-speed change."""
    if not Q(width_jet)<Q(width_flow)<Q(width_wide):raise ValueError("phase strip order changed")
    n=7;pm=3
    kroot=c["k"].fractional(Q(1,2),c["k_gap"],c["k_gap"])
    rootK=radial_factor(h,H,Q(1,2),n,pm)*kroot
    vel=(c["d"]+c["eta"]*rootK).crop(n,pm)
    speed=(c["eta"]*rootK).get(which="actual")
    D1=c["d"].get(0,1,"actual")
    path=(ex(width_flow)+(length*speed if side=="positive" else 0))*(D1*length).exp()
    if not path<ex(width_wide):raise ValueError("the complete actual principal characteristic leaves its paid strip")
    Tbar,taubar,thetabar=common_reference_powers(ref,Amin,h,H)
    source=(vel.get(which="delta")*thetabar.get(0,1)).upper()
    E=(length*source).upper();loss=ex(Q(width_flow)-Q(width_jet))
    if local_coefficients is not None:
        if local_reference is None:raise ValueError("the smaller strip needs both complete local data sets")
        c=local_coefficients;ref=local_reference
        kroot=c["k"].fractional(Q(1,2),c["k_gap"],c["k_gap"])
        rootK=radial_factor(h,H,Q(1,2),n,pm)*kroot
        vel=(c["d"]+c["eta"]*rootK).crop(n,pm)
        Tbar,taubar,thetabar=common_reference_powers(ref,Amin,h,H)
    e=angle_cauchy(E,loss,n,pm)
    vb=vel.component("actual");dv=vel.component("delta");tb=thetabar.deriv(0,1)
    for p in range(pm):
        rhs=vb*e.deriv(0,1)+dv*tb
        for q in range(n-p):
            if p+1+q<=n:e.a[p+1,q]=((rhs.a[p,q][0]/(p+1)).upper(),arb(0))
    X=ref["chi"].crop(n,pm).with_difference(e)
    if (0,1) in X.a:X.a[0,1]=(X.a[0,1][0]+1,X.a[0,1][1])
    da=(radial_factor(h,H,Q(-3,2),n,pm)*e).scale(ex(Q(3,2)))
    A=ref["A"].crop(n,pm).with_difference(da)
    actual_gap=(Amin-da.get()).lower()
    if not actual_gap>0:raise ValueError("actual and reference divided phases have no paid connecting-segment gap")
    T=radial_factor(h,H,1,n,pm)*A.fractional(Q(2,3),Amin,actual_gap)
    tau=radial_factor(h,H,Q(1,2),n,pm)*A.fractional(Q(1,3),Amin,actual_gap)
    Qphase=(c["eta"]*kroot*A.fractional(Q(-1,3),Amin,actual_gap)).crop(n,pm)
    # G/barG=(1+DeltaA/barA)^(1/6) exp(2 integral beta mean(DeltaS)).
    invA=ref["A"].fractional(-1,Amin,Amin)
    ratio_delta=da*invA
    ratio=scalar(1,n,pm).with_difference(ratio_delta)
    rgap=(1-ratio_delta.get()).lower()
    if not rgap>0:raise ValueError("the complete leading fractional-ratio segment gap failed")
    log=zero(n,pm);integrand=c["beta"].component("bar")*c["meanS"].component("delta")
    log.a[0,0]=(arb(0),(2*length*integrand.get()).upper())
    for p in range(1,pm+1):
        log.a[p,0]=(arb(0),(2*integrand.a[p-1,0][0]/p).upper())
    G=ref["G"]*ratio.fractional(Q(1,6),arb(1),rgap)*log.exponential()
    x=X.deriv(0,1);y=T.deriv(0,1)
    w0=[G*(x*x+T*y*y),(G*x*y)*2]
    w0=[w0[0].replace_bar(ref["a0"]),w0[1].replace_bar(ref["b0"])]
    mu=Qphase*Qphase*(x*x+T*y*y)
    return dict(X=X,A=A,T=T,tau=tau,Q=Qphase,G=G,x=x,y=y,w0=w0,mu=mu,
        velocity=vel,reference_theta=thetabar,phase_error=e,
        path_upper=path.upper(),phase_error_strip_sup=E,
        A_gap_bar=Amin,A_gap_actual=actual_gap,
        exact_common_nonzero_entry_trace_retained=True,
        only_comparison_entry_is_exactly_zero=True)

def matrix_product(a,b):
    return [[add_many([a[i][k]*b[k][j] for k in range(2)]) for j in range(2)] for i in range(2)]
def matrix_vector(a,v):
    return [add_many([a[i][k]*v[k] for k in range(2)]) for i in range(2)]
def matrix_component(a,which):return [[v.component(which) for v in row] for row in a]
def vector_component(a,which):return [v.component(which) for v in a]
def vector_add(*vectors):return [add_many([v[j] for v in vectors]) for j in range(2)]

def forcing_comparison(c,phase,reference,mu_gap,leading_Bi):
    """N.14--N.16, preserving correlated reference F and its true derivative."""
    op=local_coefficients(c)
    dn=[v.component("delta") for v in complete_local(phase["w0"],op,phase["Q"],phase["T"])]
    mu=phase["mu"];mgap=(mu_gap-mu.get(which="delta")).lower()
    if not mgap>0:raise ValueError("actual principal factor lost its complete difference gap")
    mui=mu.fractional(-1,mu_gap,mgap).component("actual")
    mf=mu.component("delta")
    # This exact product quotient also gives Delta F_rho with the ordered Leibniz rule.
    df=[mui*(dn[j]+mf*reference["F"][j]) for j in range(2)]
    F=[reference["F"][j].with_difference(df[j]) for j in range(2)]
    a0,b0=phase["w0"];T=phase["T"]
    det=a0*a0+T*b0*b0
    gapbar=(1/(leading_Bi*leading_Bi)).lower()
    gapactual=(gapbar-det.get(which="delta")).lower()
    if not gapactual>0:raise ValueError("the actual complete leading matrix loses its determinant gap")
    di=det.fractional(-1,gapbar,gapactual)
    inv=[[a0*di,T*b0*di],[b0*di,a0*di]]
    # Full inverse signs are retained in the identity; only each majorant is positive.
    raw=matrix_vector(inv,F)
    f=[raw[1].replace_bar(reference["f"][0]),raw[0].replace_bar(reference["f"][1])]
    return dict(operator=op,F=F,f=f,leading_matrix=[[a0,T*b0],[b0,a0]],
        leading_inverse=inv,mu_gap_actual=mgap,leading_det_gap_actual=gapactual,
        complete_unnormalized_leading_difference=dn)

def transport_matrices(c,phase):
    q,x,y,T=phase["Q"],phase["x"],phase["y"],phase["T"]
    amin,aa=phase["A_gap_bar"],phase["A_gap_actual"]
    # T inverse uses the same strict radial factor and never a sign-changing real power.
    h,H=phase["h"],phase["H"]
    ti=radial_factor(h,H,-1,T.n,T.pmax)*phase["A"].fractional(Q(-2,3),amin,aa)
    z=zero(q.n,q.pmax)
    C=[[c["d"],q*T],[q,c["d"]]]
    M=[[z,q*y*ex(Q(1,2))],[z,q*x*ti*ex(Q(1,2))]]
    N=[[q*x*ex(Q(1,2)),q*y*ex(Q(1,2))],
       [q*y*ex(Q(1,2)),q*x*ti*ex(Q(1,2))]]
    return C,M,N

def correction_comparison(c,phase,force,ref,bstar_norms,length,
        width_forcing,width_flow,width_jet):
    """Scalar actual-ray comparison, then ordered C/M/N radial differentiation."""
    if not Q(width_jet)<Q(width_flow)<Q(width_forcing):
        raise ValueError("the two true first-correction ray widths are unordered")
    h,H=phase["h"],phase["H"];vel=phase["velocity"]
    D1=c["d"].get(0,1,"actual")
    speed=(c["eta"]*radial_factor(h,H,Q(1,2))*c["k"].fractional(Q(1,2),c["k_gap"],c["k_gap"])).get(which="actual")
    path=(ex(width_flow)+(length*speed if phase["side"]=="positive" else 0))*(D1*length).exp()
    if not path<ex(width_forcing):raise ValueError("actual first-correction rays leave their complete forcing strip")
    tau=phase["tau"];T=phase["T"];q=phase["Q"];x=phase["x"];y=phase["y"]
    tau_min=(power(h,Q(1,2))*power(phase["A_gap_actual"],Q(1,3))).lower()
    bartau_min=(power(h,Q(1,2))*power(phase["A_gap_bar"],Q(1,3))).lower()
    T_min=(h*power(phase["A_gap_actual"],Q(2,3))).lower()
    barT_min=(h*power(phase["A_gap_bar"],Q(2,3))).lower()
    C=q*(x+tau*y)
    fb,fa=force["f"][1],force["f"][0]
    B0,B1,B2=[up(v) for v in bstar_norms[:3]]
    dx=phase["X"].get(which="delta")
    gbar=(fa.get()+2*T.get()*B1).upper()
    dg=(fa.get(which="delta")+2*T.get(which="delta")*B1+2*T.get()*B2*dx).upper()
    lbbar=((fb.get()+B0)/barT_min).upper()
    dlb=((fb.get(which="delta")+B1*dx+T.get(which="delta")*lbbar)/T_min).upper()
    dh=(C.get(which="delta")*(gbar+tau.get()*lbbar)
        +C.get(which="actual")*(dg+tau.get(which="delta")*lbbar+tau.get(which="actual")*dlb))/2
    ZA,ZB=ref["Z"]
    btilde=(ZB.get()+B0).upper()
    vphi=(ZA.get(0,1)+tau.get(0,1)*btilde
        +tau.get()*(ZB.get(0,1)+B1*x.get())).upper()
    E=(length*(vel.get(which="delta")*vphi+dh)).upper()
    dz0=[E,(E/tau_min+tau.get(which="delta")*btilde/tau_min+B1*dx).upper()]
    loss=ex(Q(width_flow)-Q(width_jet));n=5;pm=2
    delta=[angle_cauchy(v,loss,n,pm) for v in dz0]
    Cmat,Mmat,Nmat=transport_matrices(c,phase)
    Ca,Ma,Na=[matrix_component(v,"actual") for v in (Cmat,Mmat,Nmat)]
    Cd,Md,Nd=[matrix_component(v,"delta") for v in (Cmat,Mmat,Nmat)]
    fdelta=vector_component(force["f"],"delta")
    fbar=ref["f"];zbar=ref["Z"]
    for p in range(2):
        rhs=vector_add(matrix_vector(Ca,[v.deriv(0,1) for v in delta]),
            matrix_vector(Ma,delta),matrix_vector(Na,fdelta),
            matrix_vector(Cd,[v.deriv(0,1) for v in zbar]),
            matrix_vector(Md,zbar),matrix_vector(Nd,fbar))
        for j in range(2):
            for a in range(n-p):
                if p+1+a<=n:
                    delta[j].a[p+1,a]=((rhs[j].a[p,a][0]/(p+1)).upper(),arb(0))
    Z=[zbar[j].with_difference(delta[j]) for j in range(2)]
    w=matrix_vector(force["leading_matrix"],Z)
    w=[w[j].replace_bar(ref["w1"][j]) for j in range(2)]
    dN=[v.component("delta") for v in complete_local(w,force["operator"],phase["Q"],phase["T"])]
    return dict(w=w,Z=Z,dN=dN,
        scalar_transport_difference_sup=E,normalized_transport_difference_sup=dz0,
        complete_normalized_forcing_difference=[v.get(which="delta") for v in force["f"]],
        bstar_difference_terms=dict(ga=dg,Lb=dlb,H=dh,reference_V_phi=vphi),
        path_upper=path.upper(),complete_nonzero_original_entry_and_bstar_constant_retained=True,
        old_mean_projection_not_deleted=True)

def superscript_conversion(upper,source_width,target_width):
    """Uniform-in-r strip supremum -> joint sum_j sup_r coefficient upper."""
    loss=ex(Q(source_width)-Q(target_width))
    if not loss>0:raise ValueError("no positive strip loss for complete joint Fourier conversion")
    z=(-4*loss).exp()
    factor=((1+z)/(1-z)).upper()
    return (upper*factor).upper(),factor

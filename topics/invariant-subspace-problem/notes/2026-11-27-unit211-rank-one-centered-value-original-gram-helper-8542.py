#!/usr/bin/env python3
"""Reusable original rank-one centered-value chart, before imposing Phi=0.

Input comes from original zn=T*B3-A2^2=0 and D!=0. Interchange the two
singleton labels so h=1. Then A2,B3 are nonzero, c=A2^3/B3^2, k=1+B3/A2.
rho is the ORIGINAL (p-q)/2. All divisions below are in the base parameter
ring (lambda,rho), by A2,B3,rho,p,q or their rational constants.
This coordinate chart is already recorded in the original U-value atlas,
R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md,
section 2.2; its parameterization is not claimed as a new exclusion.
No ell-dependent parameter or algebraic norm is inverted here.
The caller supplies the named original inverse of b to the Gram builder.
"""
def original_rank_one_values(ell,lam,rho):
    A2=2*lam*lam-2*lam+1
    B3=4*lam**3-6*lam*lam+3*lam-1
    xi=B3/A2
    c=A2**3/(B3*B3)
    b=ell-c
    p,q=1+rho,1-rho
    Q=1-rho*rho
    u=p*ell-2*c*rho
    T=A2*A2/B3
    zeta=xi*p/(2*rho)
    v0,v1=xi/2,-xi/(2*rho)
    S=xi+3-2*lam
    w=lam-1-T
    V2=2*u-ell*Q
    T0=V2-2*u*u
    J=2*u*(1-u)+ell*Q
    Phi=T0+4*u-4+Q
    P02=(2-3*u)*V2-Q*u+2*u**3
    Pf=T0*(J-Q)
    G=lam*P02-(1-u)*T0
    Pc=Q*P02*(ell+T)-G*T0
    NF=(3-4*lam)*Q+S*(2*u*Q*v1+zeta*J)
    NT=b*c*Q*S*zeta
    R1=u*(3-2*lam+v0+v1)-ell*Q*v1
    NC=-G*S*zeta+S*Q*T0*v1/2+Q*w*R1
    determinant=Phi*NF-S*zeta*Pf
    return dict(ell=ell,lam=lam,rho=rho,A2=A2,B3=B3,xi=xi,
                a=1-ell,b=b,c=c,p=p,q=q,Q=Q,u=u,T=T,zeta=zeta,
                v0=v0,v1=v1,S=S,w=w,h=1,k=1+xi,
                V2=V2,T0=T0,J=J,Phi=Phi,P02=P02,Pf=Pf,G=G,Pc=Pc,
                NF=NF,NT=NT,NC=NC,determinant=determinant)

def original_rank_one_gram(v,f,t,inverse_b):
    """Original E0/N0 full Gram restoration; f,t retain their actual source.

    On Phi=0, Pf*f+Pc=0 and NF*f+NT*t+NC=0 restore them.
    On the general determinant-nonzero chart, the two full original lines
    give f=(S*zeta*Pc-Phi*NC)/determinant and
    t=(Pf*NC-Pc*NF)/(b*c*Q*determinant).
    This function never assumes either chart or divides by determinant.
    """
    a,b,c,p,q,Q,u=(v[k] for k in ("a","b","c","p","q","Q","u"))
    T0,P02,V2,lam=(v[k] for k in ("T0","P02","V2","lam"))
    assert b*inverse_b==1
    W1=T0/2+2*u*f
    W2=u*T0+lam*P02+(V2+2*u*u)*f-b*c*Q*t
    X=(q*W1-W2)*inverse_b*(1/(p*(q-p)))
    Y=(W2-p*W1)*(1/(c*q*(q-p)))
    rg=X-a*p-c*t
    sg=Y-a*q-b*t
    AA=2*f-2*b*X-2*c*Y+2*b*c*t
    zero=f*0
    rows=[[zero,zero,p,q],[zero,AA,rg,sg],
          [p,rg,zero,t],[q,sg,t,zero]]
    one=[1,0,1,1]
    def va(x,y):return [a+b for a,b in zip(x,y)]
    def vs(a,x):return [a*b for b in x]
    def vm(x,y):
        return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
    def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
    def DK(x):return [tau(vm(row,x)) for row in rows]
    d=DK(one)
    assert tau(d)==2*f
    F2=2*f
    def N4(x):
        tv=tau(x)
        return (2*tau(vm(d,vm(x,x)))-F2*tau(vm(x,x))
                -4*tv*tau(vm(d,x))+2*F2*tv**2+tau(vm(x,DK(x))))
    def P2(x):
        centered=va(x,vs(-tau(x),one))
        return tau(vm(vm(centered,centered),centered))
    def equations():
        Kd=DK(d)
        for j,name in ((1,"E1"),(2,"EB"),(3,"EC")):
            ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
            yield name,ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
        x,y=rows[0],rows[1]
        xc=va(x,vs(-tau(x),one));yc=va(y,vs(-tau(y),one))
        Pj=3*tau(vm(vm(xc,xc),yc))
        Nv=(4*tau(vm(d,vm(x,y)))-2*F2*tau(vm(x,y))
            -4*(tau(x)*tau(vm(d,y))+tau(y)*tau(vm(d,x)))
            +4*F2*tau(x)*tau(y)+tau(vm(x,DK(y)))+tau(vm(y,DK(x))))
        yield "N1",Nv-(4*lam/3)*Pj
        yield "NB",N4(rows[2])-2*lam*P02
        yield "PB",P2(rows[2])-P02
        yield "NC",N4(rows[3])-2*lam*P02*v["k"]**2
        yield "PC",P2(rows[3])-P02*v["k"]**3
    return dict(rows=rows,one=one,d=d,F2=F2,tau=tau,DK=DK,N4=N4,P2=P2,
                equations=equations,originalValues=[1,v["w"],1,v["k"]])


def original_rank_one_cleared_gram(v,fnum,tnum,weight_den):
    """Use f=fnum/weight_den, t=tnum/(b*weight_den), H=b*weight_den.

    The caller proves H!=0 from the original chart.  No H, b, or weight_den
    inverse is taken by this builder.  Every displayed row is H times the
    ORIGINAL Gram row.  Means are H^2 times original means; N/P rows H^3.
    """
    a,b,c,p,q,Q,u=(v[k] for k in ("a","b","c","p","q","Q","u"))
    T0,P02,V2,lam=(v[k] for k in ("T0","P02","V2","lam"))
    H=b*weight_den
    W1P=T0*weight_den/2+2*u*fnum
    W2P=(u*T0+lam*P02)*weight_den+(V2+2*u*u)*fnum-c*Q*tnum
    X0=(q*W1P-W2P)*(1/(p*(q-p)))
    Y0=(W2P-p*W1P)*(1/(c*q*(q-p)))
    rg0=X0-a*p*H-c*tnum
    sg0=Y0-a*q*weight_den-tnum
    AA0=2*fnum-2*X0-2*c*Y0+2*c*tnum
    zero=H*0
    rows=[[zero,zero,p*H,q*H],[zero,b*AA0,rg0,b*sg0],
          [p*H,rg0,zero,tnum],[q*H,b*sg0,tnum,zero]]
    one=[1,0,1,1]
    def va(x,y):return [a+b for a,b in zip(x,y)]
    def vs(a,x):return [a*b for b in x]
    def vm(x,y):
        return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
    def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
    def DKnum(x):return [tau(vm(row,x)) for row in rows]
    dN=DKnum(one);F2N=tau(dN)
    assert F2N==2*b*fnum
    def N4num(x):
        tv=tau(x)
        return (2*tau(vm(dN,vm(x,x)))-F2N*tau(vm(x,x))
                -4*tv*tau(vm(dN,x))+2*F2N*tv**2+tau(vm(x,DKnum(x))))
    def P2(x):
        centered=va(x,vs(-tau(x),one))
        return tau(vm(vm(centered,centered),centered))
    H3=H**3
    x,y=rows[0],rows[1]
    xc=va(x,vs(-tau(x),one));yc=va(y,vs(-tau(y),one))
    Pj=3*tau(vm(vm(xc,xc),yc))
    def equations():
        Kd=DKnum(dN)
        for j,name in ((1,"E1"),(2,"EB"),(3,"EC")):
            ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
            yield name,ee-2*Kd[j]-2*vm(dN,dN)[j]+2*F2N*dN[j]
        Nv=(4*tau(vm(dN,vm(x,y)))-2*F2N*tau(vm(x,y))
            -4*(tau(x)*tau(vm(dN,y))+tau(y)*tau(vm(dN,x)))
            +4*F2N*tau(x)*tau(y)+tau(vm(x,DKnum(y)))+tau(vm(y,DKnum(x))))
        yield "N1",Nv-(4*lam/3)*Pj
        yield "NB",N4num(rows[2])-2*lam*P02*H3
        yield "PB",P2(rows[2])-P02*H3
        yield "NC",N4num(rows[3])-2*lam*P02*v["k"]**2*H3
        yield "PC",P2(rows[3])-P02*v["k"]**3*H3
    return dict(rows=rows,one=one,dN=dN,F2N=F2N,H=H,tau=tau,DKnum=DKnum,
                N4num=N4num,P2=P2,Pj=Pj,
                P1Residual=Pj-3*v["w"]*P02*H3,
                equations=equations,originalValues=[1,v["w"],1,v["k"]])

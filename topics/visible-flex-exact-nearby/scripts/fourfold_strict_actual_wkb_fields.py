#!/usr/bin/env python3
"""True complete strict-core coefficient and WKB jets on closed cells.

The finite primitive is the same native scalar-germ Fourier-Taylor object.
It is differentiated before evaluating any radial interval. Infinite
primitive and complete finite Taylor errors are charged through radial
order five and angular order five; angular cell gaps are also charged.
The ordinary R46 potential Fcal and its first derivatives are evaluated from
the full operator, not from the reduced R106 density.

A completed report is a true field/energy input, not a full return inverse.
"""
from __future__ import annotations
import argparse, gzip, json, math, time
from collections import deque
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import acb, arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_beta_interval import primitive_fourier_budget,analytic_tail_derivative
from fourfold_phase_beta_bulk_box import (
    CBox,Box,zeros,cstack,arb_box,reduce_box,cdot,FastBulkTarget,complex_sincos)
from fourfold_phase_core_energy_fields import EnergyCoreTarget
from fourfold_phase_core_parameter_taylor import core_provenance
from fourfold_phase_core_low_coefficients import extend_half
from fourfold_phase_root_fourier_fit import read,save,sha
from fourfold_strict_high_energy_triangular import stirling_rows,power_tail

def record(value):
    x=arb(value)
    if not x.is_finite():raise ValueError("nonfinite directed field bound")
    return {"ball":x.str(50),"lower":x.lower().str(50),"upper":x.upper().str(50)}

def norm(z):return arb(float(np.max(z.magnitude_upper()))).upper()
def lo(z):return arb(float(np.min(z.real.lo))).lower()
def hi(z):return arb(float(np.max(z.real.hi))).upper()
def factbox(n):return CBox.from_acb(acb(math.factorial(n)))
def real(z):
    if np.any(z.imag.lo>0) or np.any(z.imag.hi<0):
        raise ValueError("an actual real jet lost the real axis")
    return CBox(z.real)

class Jet:
    """Rectangular normalized derivatives, without filling unknown jets."""
    __array_priority__=4000
    def __init__(self,rows):
        self.rows=[[CBox.coerce(z) for z in row] for row in rows]
        self.m=len(rows);self.n=len(rows[0])
        if not self.m or not self.n or any(len(r)!=self.n for r in rows):
            raise ValueError("invalid true jet rectangle")
    def __getitem__(self,key):return self.rows[key[0]][key[1]]
    def cut(self,m,n):
        if not 1<=m<=self.m or not 1<=n<=self.n:raise ValueError("unknown jet coefficient")
        return Jet([r[:n] for r in self.rows[:m]])
    def scalar(self,z):
        return Jet([[z if i==j==0 else 0 for j in range(self.n)] for i in range(self.m)])
    def coerce(self,z):return z if isinstance(z,Jet) else self.scalar(z)
    def __add__(self,z):
        z=self.coerce(z);m,n=min(self.m,z.m),min(self.n,z.n)
        return Jet([[self[i,j]+z[i,j] for j in range(n)] for i in range(m)])
    __radd__=__add__
    def __neg__(self):return Jet([[-z for z in r] for r in self.rows])
    def __sub__(self,z):return self+-self.coerce(z)
    def __rsub__(self,z):return self.coerce(z)+-self
    def __mul__(self,z):
        if not isinstance(z,Jet):
            return Jet([[v*z for v in r] for r in self.rows])
        m,n=min(self.m,z.m),min(self.n,z.n)
        return Jet([[sum((self[a,b]*z[i-a,j-b] for a in range(i+1)
                         for b in range(j+1)),CBox(0.))
                     for j in range(n)] for i in range(m)])
    __rmul__=__mul__
    def inv(self):
        rows=[[CBox(0.) for _ in range(self.n)] for _ in range(self.m)]
        g0=1/self[0,0];rows[0][0]=g0
        for i in range(self.m):
            for j in range(self.n):
                if i==j==0:continue
                rows[i][j]=-g0*sum((self[a,b]*rows[i-a][j-b]
                    for a in range(i+1) for b in range(j+1) if a or b),CBox(0.))
        return Jet(rows)
    def __truediv__(self,z):
        return self*z.inv() if isinstance(z,Jet) else self*(1/CBox.coerce(z))
    def __rtruediv__(self,z):return self.inv()*z
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        if n==0:return self.scalar(1)
        out=self
        for _ in range(n-1):out=out*self
        return out
    def dr(self):
        if self.m<2:raise ValueError("unknown radial derivative")
        return Jet([[(i+1)*self[i+1,j] for j in range(self.n)] for i in range(self.m-1)])
    def dt(self):
        if self.n<2:raise ValueError("unknown angular derivative")
        return Jet([[(j+1)*self[i,j+1] for j in range(self.n-1)] for i in range(self.m)])
    def radial_extend(self,n):
        if self.n!=1:raise ValueError("only an exactly radial jet can be extended")
        return Jet([[self[i,0] if j==0 else 0 for j in range(n)] for i in range(self.m)])

def dot(x,y):return sum((a*b for a,b in zip(x,y)),0)
def cross(x,y):return [x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]
def rot(x):return [-x[1],x[0],x[2]*0]
def angle_vector(x):return [a+b for a,b in zip([z.dt() for z in x],rot(x))]
def cut_vector(x,m,n):return [z.cut(m,n) for z in x]
def scalar_sqrt(f):
    if f.n!=1 or not lo(f[0,0])>0:raise ValueError("positive true radial square root required")
    root=CBox.from_acb(f[0,0].to_acb().sqrt(analytic=True))
    rows=[[root]]
    for i in range(1,f.m):
        rows.append([(f[i,0]-sum((rows[j][0]*rows[i-j][0]
                                  for j in range(1,i)),CBox(0.)))/(2*root)])
    return Jet(rows)

def jet_sincos(f):
    s0,c0=complex_sincos(f[0,0])
    ss=[[CBox(0.) for _ in range(f.n)] for _ in range(f.m)]
    cc=[[CBox(0.) for _ in range(f.n)] for _ in range(f.m)]
    ss[0][0],cc[0][0]=s0,c0
    for j in range(1,f.n):
        ss[0][j]=sum((l*f[0,l]*cc[0][j-l] for l in range(1,j+1)),CBox(0.))/j
        cc[0][j]=-sum((l*f[0,l]*ss[0][j-l] for l in range(1,j+1)),CBox(0.))/j
    for i in range(1,f.m):
        for j in range(f.n):
            ss[i][j]=sum((a*f[a,b]*cc[i-a][j-b] for a in range(1,i+1)
                          for b in range(j+1)),CBox(0.))/i
            cc[i][j]=-sum((a*f[a,b]*ss[i-a][j-b] for a in range(1,i+1)
                           for b in range(j+1)),CBox(0.))/i
    return Jet(ss),Jet(cc)

def position_angle_extension(radial_position,Y,n=6):
    """Exact rotating-frame ODE F_theta=Y-Jrot F at every actual point."""
    if any(f.n!=1 for f in radial_position):raise ValueError("radial position jet expected")
    m=min(f.m for f in radial_position)
    rows=[[[f[i,0]] for i in range(m)] for f in radial_position]
    for j in range(1,n):
        for i in range(m):
            previous=[rows[c][i][j-1] for c in range(3)]
            rotated=[-previous[1],previous[0],CBox(0.)]
            for c in range(3):rows[c][i].append((Y[c][i,j-1]-rotated[c])/j)
    return [Jet(r) for r in rows]

class StrictTarget(EnergyCoreTarget):
    def extended_primitive(self,radial):
        self.build_native_taylor()
        origin=acb(0) if self.cell[0]==0 else acb(self.anchor)
        delta=CBox.from_acb(radial-origin)
        jets=zeros((6,self.nodes,3))
        for i in range(self.native_order-1,-1,-1):
            jets=jets*delta+cstack([self.native_poly[i],*list(jets[:-1])])
        scalar_delta=CBox.from_acb(radial-acb(self.anchor))
        scalars=zeros((6,2*self.modes+2))
        for i in range(20,-1,-1):
            scalars=scalars*scalar_delta+cstack([self.scalar_poly[i],*list(scalars[:-1])])
        self.last_extended_scalars=scalars
        radius=Jet([[real(scalars[i,-2])] for i in range(6)])
        qjets=None
        if self.cell[0]==0:
            qjets=zeros((6,self.nodes))
            for i in range(self.native_order-1,0,-1):
                qjets=qjets*delta+cstack([self.native_poly[i,:,2],*list(qjets[:-1])])
        return jets,radius,qjets,origin

    def derivative_fees(self,radial,origin,sigma,quotient=False):
        extra=arb(1)/64
        widened=sigma+arb.pi()/self.angles+extra
        if not widened<self.tail_sigma:raise ValueError("primitive angular domain exceeded")
        infinite=FastBulkTarget.tail_errors(self,radial,widened)[0]
        budget=self.native_budget
        _,fm=primitive_fourier_budget(self.nodes,self.tail_sigma,widened,
                    self.native_radius,budget["radius_bound"],budget["height_bound"],
                    budget["tangent_bound"])
        distance=abs(radial-origin).upper()
        if not distance<self.native_radius:raise ValueError("native primitive radial disk exceeded")
        R=self.native_radius;degree=self.native_order
        if quotient:
            if self.cell[0]!=0:raise ValueError("quotient outside its exact waist germ")
            # Both the true and the finite vertical primitive vanish at zero.
            # The joint disk quotient maximum principle pays division by r.
            # Pay the quotient on an origin-centered disk first, then use
            # a whole tail_radius disk about every requested real point.
            if not abs(radial).upper()<self.tail_radius:
                raise ValueError("waist quotient real interval exceeds the paid origin disk")
            disk=acb(arb(0,2*self.tail_radius),arb(0,2*self.tail_radius))
            infinite=FastBulkTarget.tail_errors(self,disk,widened)[0]/(2*self.tail_radius)
            fm0=fm[0]/R;degree-=1
        else:fm0=fm[0]
        fees=[]
        for i in range(6):
            native=(arb(0) if distance==0 else
                    analytic_tail_derivative(fm0,R,distance,degree,i)/math.factorial(i))
            radial_fee=(infinite/self.tail_radius**i+native).upper()
            fees.append([(radial_fee/(extra/4)**j).upper() for j in range(6)])
        return fees

    def finite_angular_jets(self,cf,angular_order=5):
        freq=np.asarray(self.frequency)
        rows=[]
        for i in range(6):
            row=[]
            for j in range(angular_order+1):
                factor=CBox.from_acb(acb(0,1)**j/math.factorial(j))*CBox(freq**j)
                vals=cf[i]*factor.reshape(self.nodes,1) if cf.real.lo.ndim==3 else cf[i]*factor
                shape=(self.angles,3) if cf.real.lo.ndim==3 else (self.angles,)
                data=zeros(shape);data[(freq//4)%self.angles]=vals
                samples=(self.fast_fourier.fft(data,inverse=True)*self.angles)[:self.sample_count]
                row.append((real(samples),vals))
            rows.append(row)
        return rows

    def enclosed_jets(self,radial,cf,samples,origin,sigma,closed=True,quotient=False):
        fees=self.derivative_fees(radial,origin,sigma,quotient)
        normalized_gap=arb.pi()/self.angles if closed else arb(0)
        modes=np.abs(np.asarray(self.frequency)//4)
        variation=[]
        for k in modes:
            t=arb(int(k))*sigma
            variation.append(arb_box(t.exp()*arb(int(k))*normalized_gap+t.expm1()))
        variation=__import__("fourfold_phase_beta_bulk_box",fromlist=["stack"]).stack(variation)
        rows=[]
        n=len(samples[0])
        for i in range(6):
            row=[]
            for j in range(n):
                center,values=samples[i][j]
                vv=variation.reshape(self.nodes,1) if values.real.lo.ndim==2 else variation
                movement=reduce_box(Box(values.magnitude_upper())*vv).hi
                fee=movement+arb_box(fees[i][j]).hi
                row.append(center.pad(Box(fee),sigma==0))
            rows.append(row)
        if cf.real.lo.ndim==3:
            return [Jet([[rows[i][j][...,c] for j in range(n)] for i in range(6)])
                    for c in range(3)],fees
        return Jet(rows),fees

    def actual_tangent(self,sigma,radius,closed=True,order=6):
        scalar=self.last_extended_scalars
        ss,cc=self.angle_sines,self.angle_cosines
        gap=arb_box(arb.pi()/self.angles).hi if closed else 0.
        width=arb_box(sigma).hi
        shift=CBox(Box(-gap,gap),Box(-width,width))
        modes=CBox(np.arange(1,self.modes+1))
        ds,dc=complex_sincos(modes*shift)
        ds,dc=ds.reshape(-1,1),dc.reshape(-1,1)
        sine,cosine=ss*dc+cc*ds,cc*dc-ss*ds
        phase=[]
        for offset in (0,self.modes):
            rows=[]
            for i in range(order):
                row=[]
                for j in range(order):
                    trig=(sine,cosine,-sine,-cosine)[j%4]
                    weight=CBox((4*np.arange(1,self.modes+1))**j)/factbox(j)
                    row.append((scalar[i,offset:offset+self.modes].reshape(-1,1)
                                *weight.reshape(-1,1)*trig).sum())
                rows.append(row)
            phase.append(Jet(rows))
        sb,cb=jet_sincos(phase[0]);sg,cg=jet_sincos(phase[1])
        a=radius.cut(order,1).radial_extend(order)
        return [a*(-sb*cg),a*(cb*cg),a*sg]

    def curvature_jet(self,radial,cf,radius,origin):
        fees=self.derivative_fees(radial,origin,arb(0))
        Fr=[(i+1)*cf[i+1] for i in range(5)]
        ef=[(i+1)*fees[i+1][0] for i in range(5)]
        finite=[arb(float(np.max(reduce_box(Box(z.magnitude_upper())).hi))).upper() for z in Fr]
        rev=(-np.arange(self.nodes))%self.nodes
        E=[]
        for n in range(5):
            value=sum((cdot(Fr[i],Fr[n-i][rev]).sum() for i in range(n+1)),CBox(0.))
            error=sum((3*(finite[i]*ef[n-i]+finite[n-i]*ef[i]+ef[i]*ef[n-i])
                       for i in range(n+1)),arb(0)).upper()
            E.append([real(value).pad(arb_box(error),True)])
        E=Jet(E)
        if not lo(E[0,0])>0 or not lo(radius[0,0])>0:
            raise ValueError("true target E or radius not positive")
        K=(radius.dr()*E.dr()-2*radius.dr().dr()*E)/(2*radius*E**2)
        K=K.cut(4,1)
        if not hi(K[0,0])<0:raise ValueError("closed actual radial cell is not strictly negative")
        return K,{"E_lower":record(lo(E[0,0])),"target_K":record(K[0,0].to_acb().real)}

def actual_fields(F,K,waist=None,wkb=True,tangent=None):
    gsize=4 if wkb else 2
    psize=3 if wkb else 2
    X=[f.dr() for f in F];Y=angle_vector(F) if tangent is None else tangent
    Frr=[f.dr().dr() for f in F];Frt=[f.dr() for f in Y];Ftt=angle_vector(Y)
    C=cross(cut_vector(Y,gsize,gsize),cut_vector(X,gsize,gsize))
    G=dot(C,C);R=dot(cut_vector(F,gsize,gsize),cut_vector(F,gsize,gsize))
    H=dot(C,cut_vector(F,gsize,gsize))
    for value,name in ((G,"area squared"),(R,"radius squared"),(H,"support")):
        if not lo(value[0,0])>0:raise ValueError("true complex "+name+" not in right half-plane")
    C3=cut_vector(C,psize,psize)
    l,m,n=[dot(C3,cut_vector(z,psize,psize)) for z in (Frr,Frt,Ftt)]
    if not hi(n[0,0])<0:raise ValueError("true raw normal coefficient not negative")
    factor=R/H**2
    a,b,c0=-n*factor,m*factor,-l*factor
    kap=scalar_sqrt(-K).radial_extend(gsize)
    mu=kap*G*R/H**2
    c=(b*b-mu*mu)/a
    omega=c0-c
    FX=dot(cut_vector(F,psize,psize),cut_vector(X,psize,psize))
    FY=dot(cut_vector(F,psize,psize),cut_vector(Y,psize,psize))
    d0=(a*(dot(cut_vector(X,psize,psize),cut_vector(X,psize,psize))-FX*FX/R)
        +2*b*(dot(cut_vector(X,psize,psize),cut_vector(Y,psize,psize))-FX*FY/R)
        +c0*(dot(cut_vector(Y,psize,psize),cut_vector(Y,psize,psize))-FY*FY/R))/R
    if waist is None:
        if not lo(F[2][0,0])>0:raise ValueError("positive-side true height unresolved")
        ell=F[2].dt()/F[2]-FY/R
    else:
        if not lo(waist[0,0])>0:raise ValueError("true removable waist quotient unresolved")
        ell=waist.dt()/waist-FY/R
    tau=d0+omega*ell**2;sig=omega*ell
    d=(tau+sig.dt()).cut(2,2) if wkb else (tau+sig.dt()).cut(1,1)
    Krad=K.radial_extend(gsize)
    alpha=1/a;v=b/a;gamma=mu*mu/a;nu=mu/a
    if not wkb:
        return {"a":a,"b":b,"c":c,"tau":tau,"sigma":sig,"d":d,
                "alpha":alpha,"v":v,"gamma":gamma,"nu":nu,"mu":mu,
                "kappa":-Krad},{}
    Lr=(Krad.dr()/(2*Krad)+G.dr()/G+R.dr()/R-2*H.dr()/H).cut(3,3)
    Lt=(G.dt()/G+R.dt()/R-2*H.dt()/H).cut(3,3)
    Fcal=(d-((a.dr()+b.dt())*Lr+(b.dr()+c.dt())*Lt
              +a*Lr.dr()+2*b*Lr.dt()+c*Lt.dt())/2
             +(a*Lr**2+2*b*Lr*Lt+c*Lt**2)/4).cut(2,2)
    T=(a*Lr+b*Lt)/2
    Br=a.dr()+b.dt()-a*Lr-b*Lt
    out={"a":a,"b":b,"c":c,"tau":tau,"sigma":sig,"d":d,
         "alpha":alpha,"v":v,"gamma":gamma,"nu":nu,"mu":mu,
         "Lr":Lr,"Ltheta":Lt,"T":T,"Br":Br,"Fcal":Fcal,
         "Fcal_r":Fcal.dr(),"Fcal_theta":Fcal.dt(),"kappa":-Krad}
    km=lo(-K[0,0]);mulo=(km.sqrt()*lo(G[0,0])*lo(R[0,0])/norm(H[0,0])**2).lower()
    if not mulo>0:raise ValueError("true mu lower modulus unresolved")
    geom={"area2_real_lower":record(lo(G[0,0])),"radius2_real_lower":record(lo(R[0,0])),
          "support_real_lower":record(lo(H[0,0])),"mu_modulus_lower":record(mulo),
          "m_modulus_upper":record((1/mulo.sqrt()).upper())}
    return out,geom

def energy_data(fields):
    amin,amax=lo(fields["alpha"][0,0]),hi(fields["alpha"][0,0])
    gmin,gmax=lo(fields["gamma"][0,0]),hi(fields["gamma"][0,0])
    lmin,lmax=lo(fields["kappa"][0,0]),hi(fields["kappa"][0,0])
    if not min(amin,gmin,lmin)>0:raise ValueError("full real hyperbolic energy positivity failed")
    a=fields["alpha"][0,0];g=fields["gamma"][0,0];v=fields["v"][0,0];vt=fields["v"][0,1]
    ar=fields["alpha"][1,0];at=fields["alpha"][0,1]
    gr=fields["gamma"][1,0];gt=fields["gamma"][0,1]
    lam=fields["kappa"][0,0]+0*a;lr=fields["kappa"][1,0]+0*a;d=fields["d"][0,0]
    ma=(ar+v*at)/a;mg=(gr+v*gt)/g;ml=lr/lam
    trace=ma+ml;difference=ml-ma+2*vt
    fwd=[];back=[];cf=[];cb=[]
    nu_t=fields["nu"][0,1]
    count=a.real.lo.size
    for j in range(count):
        tr=trace[j].to_acb().real;df=difference[j].to_acb().real
        cross=(lam[j]-d[j]).to_acb().real*(a[j]/lam[j]).to_acb().real.sqrt()
        disc=(abs(df).upper()**2+4*abs(cross).upper()**2).sqrt()
        qr=(mg[j]-vt[j]).to_acb().real
        fwd.append(max(qr.upper(),((tr.upper()+disc)/2).upper()))
        back.append(max((-qr).upper(),((-tr.lower()+disc)/2).upper()))
        vtj=vt[j].to_acb().real;ntj=nu_t[j].to_acb().real
        cf.append(max(arb(0),(-vtj+abs(ntj).upper()).upper()))
        cb.append(max(arb(0),(vtj+abs(ntj).upper()).upper()))
    return dict(positive_ranges={name:[record(x),record(y)] for name,x,y in
            (("alpha",amin,amax),("gamma",gmin,gmax),("lambda",lmin,lmax))},
        base_energy_rate_forward=record(max(fwd)),base_energy_rate_backward=record(max(back)),
        first_characteristic_rate_forward=record(max(cf)),first_characteristic_rate_backward=record(max(cb)))

def high_moments(target,point,moduli,order,strip):
    names=("alpha","v","gamma","tau","sigma")
    odd={"v","sigma"}
    L=target.angles;K=L//2-1;q=(-strip).exp();st=stirling_rows(order)
    rows={};norms={}
    for name in names:
        value=point[name][0,0]
        transformed=target.fast_fourier.fft(extend_half(value,-1 if name in odd else 1))/L
        M=moduli[name]
        ck=[]
        for k in range(K+1):
            if name in odd and k==0:
                if not transformed[k].to_acb().contains(0):raise ValueError("true odd mean lost")
                ck.append(arb(0));continue
            alias=M*((-strip*(L-k)).exp()+(-strip*(L+k)).exp())/(1-(-strip*L).exp())
            ck.append(min(abs(transformed[k].to_acb()).upper()+alias,M*q**k).upper())
        vals=[]
        for j in range(order+1):
            finite=(ck[0] if j==0 else arb(0))+sum(
                (2*(4*k)**j*ck[k] for k in range(1,K+1)),arb(0))
            tail=2*M*4**j*power_tail(K+1,q,j,st)
            vals.append((finite+tail).upper())
        norms[name]=vals
        rows[name]=dict(true_complex_modulus=record(M),
            true_derivative_A_norms=[record(v) for v in vals],
            all_finite_fourier_modes_and_aliases_paid=True,retained_positive_modes=K)
    norms["d"]=[(norms["tau"][j]+norms["sigma"][j+1]).upper() for j in range(order)]
    rows["d"]=dict(exact_definition="tau+partial_theta sigma",
        true_derivative_A_norms=[record(v) for v in norms["d"]])
    return rows

def cell(target,left,right,strip,order,moment_strip,max_diagonal_integral):
    radial=acb(real_interval(left,right))
    cf,radius,qcf,origin=target.extended_primitive(radial)
    K,curv=target.curvature_jet(radial,cf,radius,origin)
    samples=target.finite_angular_jets(cf,angular_order=0)
    qsamples=None if qcf is None else target.finite_angular_jets(qcf)
    collected={};geoms={};fee_summary={}
    energy=None
    for tag,S,closed in (("real",arb(0),True),("complex",strip,True)):
        Fzero,fees=target.enclosed_jets(radial,cf,samples,origin,S,closed)
        jet_order=4 if tag=="real" else 6
        Fzero=cut_vector(Fzero,jet_order,1)
        Y=target.actual_tangent(S,radius,closed,jet_order)
        F=position_angle_extension(Fzero,Y,jet_order)
        Q=None
        if qcf is not None:Q,_=target.enclosed_jets(radial,qcf,qsamples,origin,S,closed,True)
        if tag=="real":
            F=cut_vector(F,4,4)
            Y=cut_vector(Y,4,4)
            if Q is not None:Q=Q.cut(4,4)
        values,geometry=actual_fields(F,K,Q,wkb=(tag=="complex"),tangent=Y)
        collected[tag]=values;geoms[tag]=geometry
        if tag=="real":
            energy=energy_data(values)
            base=max(arb(energy[k]["ball"]).upper() for k in
                     ("base_energy_rate_forward","base_energy_rate_backward"))/2
            first=max(arb(energy[k]["ball"]).upper() for k in
                      ("first_characteristic_rate_forward","first_characteristic_rate_backward"))
            if not exact_arb(right-left)*(max(arb(0),base)+order*first)<=max_diagonal_integral:
                raise ValueError("actual integrated diagonal energy rate requires subdivision")
        fee_summary[tag]={"primitive_component_Taylor_coefficient_errors":
                         [[record(z) for z in row] for row in fees]}
    oldcf,oldK,_,olderrors,_=target.complete_fast_data(radial)
    if not oldK.to_acb().real.overlaps(K[0,0].to_acb().real):
        raise ValueError("the independently expanded actual curvature enclosures disagree")
    node_values=target.coefficient_values(radial,oldcf,oldK,olderrors)
    collected["nodes"]={name:Jet([[value]]) for name,value in node_values.items()}
    broad=target.coefficient_moduli_bidisk(radial,oldcf,oldK,olderrors,moment_strip)
    moments=high_moments(target,collected["nodes"],broad,order+1,moment_strip)
    result=dict(left=str(left),right=str(right),whole_real_radial_interval=True,
        whole_complex_angle_strip=True,whole_parameter_interval=True,
        curvature=curv,geometry=geoms["complex"],
        complete_complex_field_moduli={name:record(norm(z[0,0])) for name,z in collected["complex"].items()},
        complete_complex_first_derivative_moduli={name:{
            "radial":record(norm(z[1,0])),"angular":record(norm(z[0,1]))}
            for name,z in collected["complex"].items() if z.m>=2 and z.n>=2},
        actual_angular_jets_from_exact_position_ODE=True,
        complete_primitive_derivative_errors=fee_summary,energy=energy,
        complete_high_angular_moments=moments,
        moment_normalized_angular_strip=record(moment_strip),
        moment_actual_geometry=target.last_geometric_domain,
        moment_actual_wiring=target.last_wiring_domain)
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--bulk-cover",type=Path,default=Path(
        "notes/2026-11-13-R106-current-full-complex-bulk-refined-native.json.gz"))
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    p.add_argument("--start-common",type=int,default=0)
    p.add_argument("--stop-common",type=int)
    p.add_argument("--left",type=Fraction)
    p.add_argument("--right",type=Fraction)
    p.add_argument("--physical-strip",type=Fraction,default=Fraction(1,640))
    p.add_argument("--moment-normalized-strip",type=Fraction,default=Fraction(1,16))
    p.add_argument("--use-refined-leaves",action="store_true")
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--angles",type=int,default=2048)
    p.add_argument("--native-order",type=int,default=40)
    p.add_argument("--native-radius",type=Fraction,default=Fraction(1,64))
    p.add_argument("--energy-order",type=int,default=10)
    p.add_argument("--max-diagonal-integral",type=Fraction,default=Fraction(3))
    p.add_argument("--bits",type=int,default=192)
    p.add_argument("--max-depth",type=int,default=12)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or a.out.suffix!=".gz":raise ValueError("new gzip output required")
    if not 0<a.half_width<=Fraction(1,10**9):raise ValueError("outside the current whole parameter family")
    ctx.prec,ctx.cap=a.bits,6;start=time.monotonic()
    target=StrictTarget(a.object,a.half_width,a.nodes,a.angles,
        arb(".003"),arb(".0025"),arb(".32"),native_order=a.native_order,native_radius=a.native_radius)
    if (a.left is None)!=(a.right is None):raise ValueError("both explicit interval endpoints required")
    if a.left is not None:
        if not 0<=a.left<a.right:raise ValueError("invalid positive strict interval")
        knots=[]
        for key,val in target.frozen.items():
            if key.endswith("_knots"):
                for v in val:
                    q=abs(Fraction(float(v)))
                    if a.left<q<a.right:knots.append(q)
        if knots:raise ValueError("explicit interval crosses a true scalar knot")
        groups=[(0,a.left,a.right,[(a.left,a.right)])]
        coverage_input=None
    else:
        cover=read(a.bulk_cover)
        if not cover.get("complete") or not cover.get("proved"):
            raise ValueError("incomplete original full radial partition")
        groups=[]
        for i in sorted({row["common_cell"] for row in cover["cells"]}):
            selected=[(Fraction(row["left"]),Fraction(row["right"]))
                      for row in cover["cells"] if row["common_cell"]==i]
            selected.sort()
            if i>=a.start_common and (a.stop_common is None or i<a.stop_common):
                leaves=selected if a.use_refined_leaves else [(selected[0][0],selected[-1][1])]
                groups.append((i,selected[0][0],selected[-1][1],leaves))
        if not groups:raise ValueError("empty strict cover selection")
        # R106 inserted a tiny waist integration cut inside the first actual
        # scalar germ. The exact Fz/r analytic germ must continue across it.
        if (len(groups)>=2 and groups[0][1]==0 and
                groups[0][2]==Fraction(1,1048576) and groups[1][1]==groups[0][2]):
            right=groups[1][2]
            for key,vals in target.frozen.items():
                if key.endswith("_knots") and any(0<abs(Fraction(float(v)))<right for v in vals):
                    raise ValueError("the merged waist interval crosses a true scalar knot")
            leaves=groups[0][3]+groups[1][3] if a.use_refined_leaves else [(Fraction(0),right)]
            groups=[(groups[0][0],Fraction(0),right,leaves),*groups[2:]]
        coverage_input={"path":str(a.bulk_cover),"sha256":sha(a.bulk_cover)}
    report=dict(kind="actual_strict_R46_complete_WKB_and_energy_fields",
        complete=False,proved=False,source_sha256=sha(__file__),
        identity=core_provenance(target,a.object),object_path=str(a.object),object_sha256=sha(a.object),
        coverage_input=coverage_input,settings={k:str(v) for k,v in vars(a).items()},
        physical_angle_strip=str(a.physical_strip),radial_derivative_order_paid=5,
        angular_jet_order_paid=5,energy_integer_order=a.energy_order,cells=[],failures=[],
        full_R46_strong_remainder_proved=False,full_return_inverse_proved=False,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            "fourfold_phase_core_energy_fields.py","fourfold_phase_core_parameter_taylor.py",
            "fourfold_phase_core_waist_taylor.py","fourfold_phase_core_radial_taylor.py",
            "fourfold_phase_beta_bulk_box.py","fourfold_phase_beta_interval.py",
            "fourfold_phase_beta_bulk_interval.py","fourfold_strict_high_energy_triangular.py")})
    def checkpoint():
        report["wall_seconds"]=time.monotonic()-start;save(a.out,report)
    checkpoint()
    for index,left,right,leaves in groups:
        target.set_cell(left,right)
        pending=deque([(l,r,0) for l,r in leaves])
        while pending:
            l,r,depth=pending.popleft()
            try:result=cell(target,l,r,4*exact_arb(a.physical_strip),a.energy_order,
                            exact_arb(a.moment_normalized_strip),exact_arb(a.max_diagonal_integral))
            except (ValueError,ZeroDivisionError,OverflowError) as exc:
                if depth>=a.max_depth:
                    report["failures"].append(dict(left=str(l),right=str(r),depth=depth,reason=str(exc)))
                    checkpoint();raise
                mid=(l+r)/2
                pending.appendleft((mid,r,depth+1));pending.appendleft((l,mid,depth+1))
                continue
            result.update(common_cell=index,subdivision_depth=depth)
            report["cells"].append(result);checkpoint()
            print(dict(common=index,cells=len(report["cells"]),r=float(r),
                Fcal=result["complete_complex_field_moduli"]["Fcal"]["ball"],
                base_forward=result["energy"]["base_energy_rate_forward"]["ball"],
                seconds=report["wall_seconds"]),flush=True)
    cursor=groups[0][1]
    for row in report["cells"]:
        if Fraction(row["left"])!=cursor:raise ValueError("actual strict cover has a gap")
        cursor=Fraction(row["right"])
    if cursor!=groups[-1][2]:raise ValueError("actual strict cover endpoint differs")
    report.update(complete=True,proved=True,exact_covered_positive_interval=[str(groups[0][1]),str(cursor)],
        full_selected_closed_interval_paid=True,mean_retained=True,
        full_operator_potential="Fcal=mu^(1/2) P(mu^(-1/2)); includes d=tau+sigma_theta",
        radial_knot_rule="Each exact scalar germ is treated separately; no derivative is silently taken across a knot.",
        scope="True scalar coefficients, ordinary WKB potential/first derivatives, complete high moments and constraint energy rates on the exact displayed positive strict interval. Negative side follows exact radial reflection with forward/backward orientation swapped. Root interfaces, full frame/composition and returned inverse remain separate.")
    checkpoint()
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),cells=len(report["cells"]),
               seconds=report["wall_seconds"]),flush=True)
if __name__=="__main__":main()


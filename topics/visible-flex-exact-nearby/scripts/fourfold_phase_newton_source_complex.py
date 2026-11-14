#!/usr/bin/env python3
"""Complex radial extension of the exact initial R117 source on one fixed germ.

Dot products are complex bilinear extensions. The fixed scalar polynomial
branch is continued across the selected disk solely for a Cauchy bound; the
real source is used only on its installed scalar germ. Every nonzero complex
denominator is checked for the entire supplied box and all angular cells.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_two_jet_newton_source import *
from fourfold_phase_correlated_curvature import Polynomial,component_upper
from fourfold_phase_beta_bulk_box import DirectedFFT,reduce_box,arb_box,square_box,cdot
from fourfold_phase_uniform_tail import up

def excludes_zero(v):
    v=CBox.coerce(v)
    return bool(np.all((square_box(v.real)+square_box(v.imag)).lo>0))

def complex_lower(v):
    v=CBox.coerce(v);q=square_box(v.real)+square_box(v.imag)
    return arb(float(np.min(q.lo))).sqrt().lower()

def analytic_square(v):return v*v

def trace2(a,inv):
    return sum((inv[i][j]*a[i][j] for i in range(2) for j in range(2)),CBox(0.))

def bilinear(a,x,y):
    return sum((a[k][l]*x[k]*y[l] for k in range(2) for l in range(2)),CBox(0.))

def inner2(a,b,inv):
    return sum((inv[i][k]*inv[j][l]*a[i][j]*b[k][l]
                for i in range(2) for j in range(2)
                for k in range(2) for l in range(2)),CBox(0.))

def inverse2(a,det):
    if not excludes_zero(det):raise ValueError('complex 2-metric determinant unresolved')
    return [[a[1][1]/det,-a[0][1]/det],[-a[1][0]/det,a[0][0]/det]]

def intersect(a,b,name):
    parts=[]
    for va,vb in ((a.real,b.real),(a.imag,b.imag)):
        lo=np.maximum(va.lo,vb.lo);hi=np.minimum(va.hi,vb.hi)
        if np.any(lo>hi):raise ValueError('inconsistent complex identity '+name)
        parts.append(Box(lo,hi))
    return CBox(*parts)

def nonmean(p,exact_zero_mean=False):
    if exact_zero_mean and not p.mean().contains(0):raise ValueError('structural complex zero mean lost')
    c=clone_coefficient(p.c);c[0]=0
    return ComplexPolynomial(c,p.error,p.degree,p.fft)

class ComplexPolynomial(Polynomial):
    def __init__(self,c,error,degree,fft):
        c=clone_coefficient(c);n=len(c.real.lo)
        modes=np.asarray([k if k<n//2 else k-n for k in range(n)])
        out=np.abs(modes)>degree
        if np.any(c.real.lo[out]>0) or np.any(c.real.hi[out]<0) or np.any(c.imag.lo[out]>0) or np.any(c.imag.hi[out]<0):raise ValueError('complex support gate')
        c[out]=0;const=c[0];mid=[];rad=[]
        for p in (c.real,c.imag):
            m=p.lo/2+p.hi/2;m=np.minimum(np.maximum(m,p.lo),p.hi)
            e=np.maximum(up(abs(m-p.lo)),up(abs(p.hi-m)));e[0]=0
            mid.append(m);rad.append(e)
        fee=arb(float(reduce_box(Box(up(rad[0]+rad[1]))).hi)).upper()
        c=CBox(Box(mid[0]),Box(mid[1]));c[0]=const
        super().__init__(c,arb(error)+fee,degree,fft)
    def coerce(self,v):
        if isinstance(v,Polynomial):
            if v.grid!=self.grid or v.fft is not self.fft:raise ValueError('different algebra')
            return v
        c=zeros((self.grid,));c[0]=CBox.from_acb(acb(v))
        return ComplexPolynomial(c,arb(0),0,self.fft)
    def __add__(self,v):
        v=self.coerce(v)
        return ComplexPolynomial(self.c+v.c,self.error+v.error,max(self.degree,v.degree),self.fft)
    __radd__=__add__
    def __neg__(self):return ComplexPolynomial(-self.c,self.error,self.degree,self.fft)
    def __mul__(self,v):
        v=self.coerce(v);degree=self.degree+v.degree
        if degree>=self.grid//2:raise ValueError('aliased product refused')
        a0,b0=self.c[0],v.c[0]
        if self.degree==0:c=v.c*a0
        elif v.degree==0:c=self.c*b0
        else:
            c=self.fft.fft(self.samples_without_constant()*v.samples_without_constant())/self.grid
            a,b=clone_coefficient(self.c),clone_coefficient(v.c);a[0]=0;b[0]=0
            c=c+a*b0+b*a0;c[0]=c[0]+a0*b0
        e=self.norm()*v.error+v.norm()*self.error+self.error*v.error
        return ComplexPolynomial(c,e,degree,self.fft)
    __rmul__=__mul__
    def mean(self):return self.c[0].to_acb()+acb(arb(0,self.error),arb(0,self.error))
    def angular_cells(self,angles):
        if angles<self.grid or angles&(angles-1):raise ValueError('angle grid')
        if angles==self.grid:c=self.c
        else:
            c=zeros((angles,));modes=np.asarray([k if k<self.grid//2 else k-self.grid for k in range(self.grid)])
            c[modes%angles]=self.c
        s=self.fft.fft(c,inverse=True)*angles
        fee=(self.error+arb.pi()/(4*angles)*self.norm(1)).upper()
        return s.pad(arb_box(fee))

class ComplexSource(TwoJetNewtonSource):
    def lift(self,finite,error):
        c=zeros((self.product_grid,));frequency=np.asarray(self.frequency)//4
        c[frequency%self.product_grid]=finite;c[(-self.nodes//2)%self.product_grid]=0
        return ComplexPolynomial(c,error,self.nodes//2-1,self.polynomial_fft)
    def complex_source(self,radial):
        cap_ground=False
        FF,YY,a,EF,EY,tail=self.first_two_jets(radial)
        F=[[self.lift(FF[j][:,k],EF[j][0]) for k in range(3)]
           for j in range(3)]
        Y=[[self.lift(YY[j][:,k],EY[j]) for k in range(3)]
           for j in range(2)]
        frequency=np.asarray(self.frequency)
        zz=YY[0]*CBox(0.,Box(frequency[:,None]))
        zz[:,0]=zz[:,0]-YY[0][:,1]
        zz[:,1]=zz[:,1]+YY[0][:,0]
        ezz=(EF[0][2]+2*EF[0][1]+EF[0][0]).upper()
        Z=[self.lift(zz[:,k],ezz) for k in range(3)]
        zero=F[0][0].coerce(0)
        first=[F[1],Y[0]]
        second=[[F[2],Y[1]],[Y[1],Z]]
        aa=[]
        for value in a[:3]:
            q=value.to_acb()
            aa.append(q)
        if aa[0].contains(0):raise ValueError("complex physical radius may vanish")
        a2=zero.coerce(aa[0]*aa[0])
        Epoly=dot(F[1],F[1]);E1poly=2*dot(F[1],F[2])
        # The scalar target mean is evaluated directly at Fourier index zero.
        # Its exact zero convolution avoids reusing the error of every other
        # coefficient as an independent uncertainty in the constant mode.
        rev=(-np.arange(self.nodes))%self.nodes
        M1=arb(float(np.max(reduce_box(Box(FF[1].magnitude_upper())).hi))).upper()
        M2=arb(float(np.max(reduce_box(Box(FF[2].magnitude_upper())).hi))).upper()
        ee=3*(2*M1*EF[1][0]+EF[1][0]*EF[1][0])
        ee1=6*(M1*EF[2][0]+M2*EF[1][0]+EF[1][0]*EF[2][0])
        E=cdot(FF[1],FF[1][rev]).sum().to_acb()+acb(arb(0,ee),arb(0,ee))
        E1=2*cdot(FF[1],FF[2][rev]).sum().to_acb()+acb(arb(0,ee1),arb(0,ee1))
        if E.contains(0):raise ValueError("complex target radial metric may vanish")
        K0=-aa[2]/(aa[0]*E)+aa[1]*E1/(2*aa[0]*E*E)
        mixed=dot(F[1],Y[0])
        # Exact R33 unit tangent identity: g_theta,theta = a^2.
        gp=[[Epoly,mixed],[mixed,a2]]
        fp=[[-nonmean(Epoly),-nonmean(mixed,True)],
            [-nonmean(mixed,True),zero]]
        # Derivative index comes first: df[k][i][j] = partial_k f_ij.
        dr_mix=dot(F[2],Y[0])+dot(F[1],Y[1])
        dt_mix=dot(Y[1],Y[0])+dot(F[1],Z)
        dfp=[
            [[-nonmean(E1poly),-nonmean(dr_mix,True)],
             [-nonmean(dr_mix,True),zero]],
            [[-nonmean(2*dot(F[1],Y[1]),True),-nonmean(dt_mix,True)],
             [-nonmean(dt_mix,True),zero]]]
        C=cross(Y[0],F[1])
        G=dot(C,C);T=dot(F[0],F[0]);S=dot(C,F[0])
        L=dot(C,F[2]);M=dot(C,Y[1]);N=dot(C,Z)
        Delta=L*N-M*M-G*G*K0
        # det(g0)-det(gamma) = a^2*f_rr + gamma_rtheta^2
        # follows from f_theta,theta=0 and f_rtheta=-gamma_rtheta.
        determinant_defect=a2*fp[0][0]+mixed*mixed
        Gmetric=Epoly*a2-mixed*mixed
        tp=[dot(F[0],first[i]) for i in range(2)]
        ff2=[[dot(F[0],second[i][j]) for j in range(2)] for i in range(2)]
        lower_conn=[[[dot(first[l],second[i][j]) for j in range(2)]
                     for i in range(2)] for l in range(2)]
        polys={"G":G,"G_metric":Gmetric,"T":T,"S":S,"L":L,"M":M,"N":N,
               "Delta":Delta,"determinant_defect":determinant_defect}
        for i in range(2):
            polys[f"t{i}"]=tp[i]
            for j in range(2):
                polys[f"g{i}{j}"]=gp[i][j]
                polys[f"f{i}{j}"]=fp[i][j]
                polys[f"FF2{i}{j}"]=ff2[i][j]
                for k in range(2):
                    polys[f"df{k}{i}{j}"]=dfp[k][i][j]
                    polys[f"conn{k}{i}{j}"]=lower_conn[k][i][j]
        if cap_ground:polys["F_z"]=F[0][2]
        boxes={key:value.angular_cells(self.curvature_angles)
               for key,value in polys.items()}
        gdet=intersect(boxes["G"],boxes["G_metric"],"cross-square = metric determinant")
        tt,ss=boxes["T"],boxes["S"]
        if not all(excludes_zero(v) for v in (gdet,tt,ss)):
            raise ValueError("complex immersion/radial-chart denominator unresolved")
        g=[[boxes[f"g{i}{j}"] for j in range(2)] for i in range(2)]
        f=[[boxes[f"f{i}{j}"] for j in range(2)] for i in range(2)]
        df=[[[boxes[f"df{k}{i}{j}"] for j in range(2)] for i in range(2)]
            for k in range(2)]
        t=[boxes[f"t{i}"] for i in range(2)]
        t2=[[g[i][j]+boxes[f"FF2{i}{j}"] for j in range(2)] for i in range(2)]
        gamma=inverse2(g,gdet)
        smetric=[[g[i][j]/tt-t[i]*t[j]/analytic_square(tt)
                  for j in range(2)] for i in range(2)]
        sdet=analytic_square(ss)/(analytic_square(tt)*tt)
        sinv=inverse2(smetric,sdet)
        # <U_l,U_ij> in inner products of F0,F1,F2; all large t_l*t_ij
        # terms have been cancelled algebraically before interval division.
        s_lower=[[[boxes[f"conn{l}{i}{j}"]/tt
                    -(g[l][i]*t[j]+g[l][j]*t[i]+t[l]*boxes[f"FF2{i}{j}"])/analytic_square(tt)
                    +2*t[l]*t[i]*t[j]/(analytic_square(tt)*tt)
                   for j in range(2)] for i in range(2)] for l in range(2)]
        cg=[[[sum((gamma[k][l]*boxes[f"conn{l}{i}{j}"] for l in range(2)),CBox(0.))
               for j in range(2)] for i in range(2)] for k in range(2)]
        cs=[[[sum((sinv[k][l]*s_lower[l][i][j] for l in range(2)),CBox(0.))
               for j in range(2)] for i in range(2)] for k in range(2)]
        bf=[[[cg[k][i][j]-cs[k][i][j] for j in range(2)] for i in range(2)]
            for k in range(2)]
        g0=[[CBox.from_acb(E),CBox(0.)],[CBox(0.),CBox.from_acb(aa[0]*aa[0])]]
        g0inv=[[CBox.from_acb(1/E),CBox(0.)],[CBox(0.),CBox.from_acb(1/(aa[0]*aa[0]))]]
        covg=[[[df[k][i][j]
                -sum((cg[m][k][i]*f[m][j]+cg[m][k][j]*f[i][m]
                      for m in range(2)),CBox(0.))
                 for j in range(2)] for i in range(2)] for k in range(2)]
        dconn=[[[sum((g0inv[k][l]*(covg[i][j][l]+covg[j][i][l]-covg[l][i][j])
                      for l in range(2)),CBox(0.))/2
                  for j in range(2)] for i in range(2)] for k in range(2)]
        tau=[trace2(bf[k],sinv) for k in range(2)]
        dtau=[trace2(dconn[k],sinv) for k in range(2)]
        q=bilinear(f,tau,tau)+2*bilinear(g0,tau,dtau)+bilinear(g0,dtau,dtau)
        for i in range(2):
            for j in range(2):
                for u in range(2):
                    for v in range(2):
                        bi=[bf[k][i][j] for k in range(2)]
                        bu=[bf[k][u][v] for k in range(2)]
                        di=[dconn[k][i][j] for k in range(2)]
                        du=[dconn[k][u][v] for k in range(2)]
                        q=q-sinv[i][u]*sinv[j][v]*(
                            bilinear(f,bi,bu)+2*bilinear(g0,bi,du)+bilinear(g0,di,du))
        zdiff=[]
        for i in range(2):
            z=sum((f[i][k]*tau[k]+g0[i][k]*dtau[k] for k in range(2)),CBox(0.))
            z=z-sum((sinv[j][l]*(f[k][l]*bf[k][i][j]+g0[k][l]*dconn[k][i][j])
                     for j in range(2) for l in range(2) for k in range(2)),CBox(0.))
            zdiff.append(z)
        # This whole expression is rational in T. Avoid a second independent
        # enclosure of rho^2 and rho*rho_i in the actual source.
        hf=[[8*t[i]*t[j]/(analytic_square(tt)*tt)-2*t2[i][j]/analytic_square(tt)
             +2*sum((cs[k][i][j]*t[k] for k in range(2)),CBox(0.))/analytic_square(tt)
             for j in range(2)] for i in range(2)]
        trf=trace2(f,sinv)
        curvature=2*(CBox.from_acb(K0)*boxes["determinant_defect"]-boxes["Delta"]/gdet)/sdet
        pieces={
            "connection_and_trace":(q-2*trf)/tt,
            "correlated_curvature":curvature/tt,
            "density_gradient":-4*bilinear(sinv,t,zdiff)/analytic_square(tt),
            "density_hessian":inner2(hf,f,sinv),
            "density_trace":-trace2(hf,sinv)*trf}
        compatibility=sum(pieces.values(),CBox(0.))
        source=-compatibility/2
        self.last_source_box=source
        return dict(source_modulus_upper=record(component_upper(source)),
                    chart_denominator_modulus_lower={k:record(complex_lower(v)) for k,v in [('G',gdet),('T',tt),('S',ss),('det_s',sdet)]},
                    target_radial_metric_modulus_lower=record(abs(E).lower()),
                    complete_primitive_A_sigma_error=record(tail),
                    correlated_Delta_A0_upper=record(Delta.norm()+Delta.error))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    p.add_argument('--left',type=Fraction,required=True);p.add_argument('--right',type=Fraction,required=True)
    p.add_argument('--radius-factor',type=Fraction,default=Fraction(4))
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--angles',type=int,default=4096)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=192;ctx.cap=4
    target=ComplexSource(args.object,args.half_width,args.nodes,args.angles);cuts=common_cells(target)
    center=(args.left+args.right)/2;half=(args.right-args.left)/2
    i=min(len(cuts)-2,bisect_right(cuts,center)-1)
    if not cuts[i]<=args.left<args.right<=cuts[i+1]:raise ValueError('crosses scalar germ')
    if not args.radius_factor>1:raise ValueError('outer radius must be strictly larger')
    target.set_cell(cuts[i],cuts[i+1]);R=half*args.radius_factor
    radial=acb(real_interval(center-R,center+R),arb(0,arb(R.numerator)/R.denominator))
    t=time.monotonic();out=target.complex_source(radial)
    out.update(kind='actual_R117_source_complex_radial_Cauchy_box',complete=True,
               exact_real_interval=list(map(str,(args.left,args.right))),exact_center=str(center),
               exact_radius=str(R),exact_half_width=str(args.half_width),
               source_sha256=sha(__file__),object_sha256=sha(args.object),
               scalar_germ=list(map(str,target.cell)),whole_real_angle_circle=True,
               scope='uniform complex square containing the closed radial disk; one fixed analytically continued scalar germ; no new real domain beyond installed germ',
               wall_seconds=time.monotonic()-t)
    save(args.out,out);print(json.dumps(out),flush=True)

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Actual finite-tilt latitude immersion design. Public Actions science only."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import qr, svd


def emit(kind, **data):
    print(json.dumps({"kind":kind,**data},sort_keys=True,allow_nan=False),flush=True)


def jy(v):
    return np.stack((v[...,2],np.zeros_like(v[...,0]),-v[...,0]),axis=-1)


def rz_frame(v,phi):
    """Rotate about y, broadcasting this meridian frame over azimuth."""
    c,s=np.cos(phi),np.sin(phi)
    return np.stack((c*v[...,0]+s*v[...,2],v[...,1],-s*v[...,0]+c*v[...,2]),axis=-1)


def dot(a,b):
    return np.einsum("...i,...i->...",a,b)


def primitive(x):
    """Zero-mean inverse d/dphi on this odd periodic grid."""
    n=x.shape[1]
    if n%2!=1:
        raise ValueError("The periodic primitive requires an odd grid.")
    coeff=np.fft.rfft(x,axis=1)
    coeff[:,0]=0
    coeff[:,1:]/=1j*np.arange(1,coeff.shape[1])[None,:,None]
    return np.fft.irfft(coeff,n=n,axis=1)


def mean_free(x):
    return x-x.mean(axis=1,keepdims=True)


class LatitudeSystem:
    def __init__(self, specification, count):
        self.spec=specification
        self.count=count
        self.a=float(specification["a"])
        self.b=float(specification["b"])
        self.ang=math.asin(float(specification["tilt_sine"]))
        self.nsp=int(specification["radial_spans"])
        self.K=int(specification["body_modes"])
        self.degree=5
        basic=np.linspace(self.a,self.b,self.nsp+1)
        self.knots=np.r_[[self.a]*self.degree,basic,[self.b]*self.degree]
        self.nb=len(self.knots)-self.degree-1
        self.spl=BSpline(self.knots,np.eye(self.nb),self.degree)
        self.na=self.nb-6
        self.nc=self.nb-4
        self.size=2*self.na*self.K+2*self.nc
        self.wpeak=float(specification["seed_slope_peak"])

    def split(self,x):
        z=self.na*self.K
        return x[:z].reshape(self.K,self.na),x[z:2*z].reshape(self.K,self.na),x[2*z:].reshape(2,self.nc)

    def seed(self):
        x=np.zeros(self.size)
        us,vs,_=self.split(x)
        greville=np.array([self.knots[i+1:i+1+self.degree].mean() for i in range(self.nb)])[3:-3]
        t=(greville-self.a)/(self.b-self.a)
        env=(4*t*(1-t))**4
        de=4*env*(1-2*t)/(t*(1-t))
        z=2*t-1
        wb=3*self.wpeak*z*(1-z*z)**2
        for j,nodes in self.spec["initial_pair_and_nodes"]:
            q=float(self.spec["seed_mode_height"])
            wave=np.cos(nodes*np.pi*t)
            f=q*env*wave
            fr=q*(de*wave-env*nodes*np.pi*np.sin(nodes*np.pi*t))/(self.b-self.a)
            # h'=-w, as in R628. Full solve subsequently frees every body column.
            us[j-1]=-wb*(j*f-greville*fr/j)/greville
            vs[j-1]=-j*f/greville
        return x

    def grid(self, order, azimuths, endpoints=False):
        xg,wg=np.polynomial.legendre.leggauss(order)
        spans=np.linspace(self.a,self.b,self.nsp+1)
        if endpoints:
            r=np.unique(np.r_[spans,*[(l+rgt)/2+(rgt-l)*xg/2 for l,rgt in zip(spans[:-1],spans[1:])]])
            weights=np.ones_like(r)/len(r)
        else:
            r=np.concatenate([(l+rgt)/2+(rgt-l)*xg/2 for l,rgt in zip(spans[:-1],spans[1:])])
            weights=np.tile(wg/(2*self.nsp),self.nsp)
        return self.at(r,azimuths,weights)

    def at(self,r,azimuths,weights=None):
        t=(r-self.a)/(self.b-self.a)
        span=self.b-self.a
        phi=2*np.pi*np.arange(azimuths)/azimuths
        j=np.arange(1,self.K+1)
        sn=np.sin(j[:,None]*phi)
        cs=np.cos(j[:,None]*phi)
        er=np.stack((np.cos(phi),np.sin(phi),np.zeros_like(phi)),axis=-1)[None,:,:]
        et=np.stack((-np.sin(phi),np.cos(phi),np.zeros_like(phi)),axis=-1)[None,:,:]
        mats=[self.spl(r,n) for n in range(3)]
        # chi=1-10t^3+15t^4-6t^5, with its two endpoint jets fixed.
        chi=1-10*t**3+15*t**4-6*t**5
        chix=-30*t*t*(1-t)**2/span
        chixx=-60*t*(1-t)*(1-2*t)/span**2
        z=2*t-1
        w=3*self.wpeak*z*(1-z*z)**2
        wx=6*self.wpeak*(1-z*z)*(1-5*z*z)/span
        return dict(r=r,t=t,phi=phi,sn=sn,cs=cs,j=j,er=er,et=et,ez=np.array([0.,0.,1.]),
                    A=[b[:,3:-3] for b in mats],C=[b[:,2:-2] for b in mats],
                    refw=w,refwx=wx,q=self.ang*chi,qx=self.ang*chix,qxx=self.ang*chixx,
                    weights=weights if weights is not None else np.ones_like(r)/len(r))

    def state(self,x,g,second=False):
        self.count["full_state_evaluations"]+=1
        ucoef,vcoef,cc=self.split(x)
        sn,cs=g["sn"],g["cs"]
        def field(co,k,table=sn):
            return g["A"][k]@co.T@table
        u,v=field(ucoef,0),field(vcoef,0)
        ur,vr=field(ucoef,1),field(vcoef,1)
        co,si=np.cos(u)[...,None],np.sin(u)[...,None]
        cv,sv=np.cos(v)[...,None],np.sin(v)[...,None]
        hor=si*g["er"]+co*g["et"]
        hop=co*g["er"]-si*g["et"]
        T=cv*hor+sv*g["ez"]
        Tu,Tv=cv*hop,-sv*hor+cv*g["ez"]
        Tuu,Tuv,Tvv=-cv*hor,-sv*hop,-T
        Tur=Tuu*ur[...,None]+Tuv*vr[...,None]
        Tvr=Tuv*ur[...,None]+Tvv*vr[...,None]
        Tr=Tu*ur[...,None]+Tv*vr[...,None]
        U,Ur=primitive(T),primitive(Tr)
        r=g["r"][:,None,None]
        q,qx=g["q"][:,None],g["qx"][:,None,None]
        Cp0=g["C"][0]@cc.T
        Cp=np.stack((Cp0[:,0],np.zeros(len(r)),Cp0[:,1]-g["refw"]),axis=-1)
        D=rz_frame(Cp[:,None,:],-q)+U+r*Ur+r*qx*jy(U)
        H=mean_free(T)
        E=dot(D,D).mean(axis=1)
        st=dict(T=T,Tu=Tu,Tv=Tv,Tur=Tur,Tvr=Tvr,Tr=Tr,U=U,Ur=Ur,D=D,H=H,E=E,Cp=Cp)
        if not second:
            return st
        urr,vrr=field(ucoef,2),field(vcoef,2)
        up,vp=field(ucoef,0,g["j"][:,None]*cs),field(vcoef,0,g["j"][:,None]*cs)
        Tp=Tu*up[...,None]+Tv*vp[...,None]+np.stack((-T[...,1],T[...,0],np.zeros_like(T[...,0])),axis=-1)
        Trr=(Tu*urr[...,None]+Tv*vrr[...,None]+Tur*ur[...,None]+Tvr*vr[...,None])
        Urr=primitive(Trr)
        Cpp0=g["C"][1]@cc.T
        Cpp=np.stack((Cpp0[:,0],np.zeros(len(r)),Cpp0[:,1]-g["refwx"]),axis=-1)
        Drr=(rz_frame(Cpp[:,None,:],-q)+2*Ur+r*Urr+2*qx*jy(U+r*Ur)
             +r*g["qxx"][:,None,None]*jy(U)+r*qx**2*jy(jy(U)))
        Drp=H+r*mean_free(Tr)+r*qx*jy(H)
        # The finite F uses the odd trigonometric interpolant of H. Its
        # exact second angular derivative on this grid uses the multiplier.
        kphi=np.arange(H.shape[1]//2+1)
        Tp_interpolant=np.fft.irfft(np.fft.rfft(H,axis=1)*(1j*kphi)[None,:,None],
                                    n=H.shape[1],axis=1)
        st.update(Drr=Drr,Drp=Drp,Dpp=r*Tp_interpolant,
                  sampled_tangent_derivative_alias=float(np.max(np.linalg.norm(Tp_interpolant-Tp,axis=-1))))
        return st

    def pack(self,rr,rt,tt,closure,g):
        # The residual keeps all rows; weights normalize each integral to unit mass.
        wr=np.sqrt(g["weights"])
        wt=wr[:,None]/math.sqrt(len(g["phi"]))
        return np.r_[(wt*rr).ravel(),(wt*rt).ravel(),(wt*tt).ravel(),wr*closure]

    def residual(self,x,g,fixed_E=None):
        self.count["residual_evaluations"]+=1
        st=self.state(x,g)
        D,H,E=st["D"],st["H"],st["E"]
        target=E if fixed_E is None else fixed_E
        scale=1+g["refw"]**2
        res=self.pack((dot(D,D)-target[:,None])/scale[:,None],dot(D,H)/np.sqrt(scale)[:,None],
                      dot(H,H)-1,st["T"][...,1].mean(axis=1),g)
        return res,st

    def jacobian(self,st,g,fixed=False):
        self.count["complete_dense_jacobians"]+=1
        D,H=st["D"],st["H"]
        r=g["r"][:,None,None]
        qx=g["qx"][:,None,None]
        ns=len(g["phi"])
        rows=3*len(r)*ns+len(r)
        jac=np.empty((rows,self.size),order="F")
        es=1+g["refw"]**2
        def raw(dD,dH,dc):
            rr=2*dot(D,dD)
            if not fixed:
                rr=mean_free(rr)
            return rr/es[:,None],(dot(H,dD)+dot(D,dH))/np.sqrt(es)[:,None],2*dot(H,dH),dc
        def fill(slot, B, channels, Br=None, rate=None):
            offset=0
            for i,channel in enumerate(channels):
                angular=ns if i<3 else 1
                w=np.sqrt(g["weights"]/angular)
                b=B*w[:,None]
                result=channel.reshape(len(r),angular,1)*b[:,None,:]
                if Br is not None:
                    result+=rate[i].reshape(len(r),angular,1)*(Br*w[:,None])[:,None,:]
                size=len(r)*angular
                jac[offset:offset+size,slot:slot+B.shape[1]]=result.reshape(size,B.shape[1])
                offset+=size
        for field,(deriv,derivr) in enumerate(((st["Tu"],st["Tur"]),(st["Tv"],st["Tvr"]))):
            for k,sine in enumerate(g["sn"]):
                dT=deriv*sine[None,:,None]
                dU=primitive(dT)
                dD=dU+r*(primitive(derivr*sine[None,:,None])+qx*jy(dU))
                dH=mean_free(dT)
                main=raw(dD,dH,dT[...,1].mean(axis=1))
                rate=raw(r*dU,np.zeros_like(dH),np.zeros(len(r)))
                slot=(field*self.K+k)*self.na
                fill(slot,g["A"][0],main,g["A"][1],rate)
        for k,coord in enumerate((0,2)):
            v=np.zeros_like(D)
            v[...,coord]=1
            v=rz_frame(v,-g["q"][:,None])
            fill(2*self.K*self.na+k*self.nc,g["C"][0],raw(v,np.zeros_like(H),np.zeros(len(r))))
        self.count["analytic_columns"]+=jac.shape[1]
        return jac

    def center(self,x,r):
        _,_,cc=self.split(x)
        antider=self.spl.antiderivative()
        ints=(antider(r)-antider(self.b))[:,2:-2]@cc.T
        t=(r-self.a)/(self.b-self.a)
        seed_height=16*self.wpeak*(self.b-self.a)*t**3*(1-t)**3
        return np.stack((ints[:,0],np.zeros(len(r)),ints[:,1]+seed_height),axis=-1)

    def readout(self,x,g,fixed_E=None):
        self.count["second_jet_readouts"]+=1
        st=self.state(x,g,second=True)
        D,H=st["D"],st["H"]
        r=g["r"][:,None]
        q=g["q"][:,None]
        F_r=rz_frame(D,q)
        F_p=r[...,None]*rz_frame(H,q)
        center=self.center(x,g["r"])
        F=center[:,None,:]+r[...,None]*rz_frame(st["U"],q)
        oriented=np.cross(D,r[...,None]*H)
        grams=dot(oriented,oriented)
        if np.min(grams)<=0 or not np.all(np.isfinite(grams)):
            raise ArithmeticError("Singular or nonfinite actual induced metric.")
        norm=oriented/np.sqrt(grams)[...,None]
        nlab=rz_frame(norm,q)
        e,f,gg=dot(D,D),r*dot(D,H),r*r*dot(H,H)
        L,M,N=dot(norm,st["Drr"]),dot(norm,st["Drp"]),dot(norm,st["Dpp"])
        mean=(L*gg-2*M*f+N*e)/(2*grams)
        gauss=(L*N-M*M)/grams
        kabs=abs(mean)+np.sqrt(np.maximum(0.,mean*mean-gauss))
        E=st["E"] if fixed_E is None else fixed_E
        rr,rt,tt=e/E[:,None]-1,f/(r*np.sqrt(E[:,None])),gg/(r*r)-1
        metric=abs((rr+tt)/2)+np.sqrt(((rr-tt)/2)**2+rt**2)
        ix,ixk=np.unravel_index(metric.argmax(),metric.shape),np.unravel_index(kabs.argmax(),kabs.shape)
        def loc(idx):
            return [float(g["r"][idx[0]]),float(g["phi"][idx[1]])]
        inner_center=self.center(x,np.array([self.a]))[0]
        pin=rz_frame(F-inner_center[None,None,:],-self.ang)[...,:2]
        nin=rz_frame(nlab,-self.ang)[...,:2]
        nd=dot(nin,nin)
        tmin=np.clip(-dot(pin,nin)/np.maximum(nd,1e-30),-.03,.03)
        imin=np.sqrt(dot(pin+tmin[...,None]*nin,pin+tmin[...,None]*nin))
        pout,nout=F[...,:2],nlab[...,:2]
        omax=np.maximum(np.linalg.norm(pout+.03*nout,axis=-1),np.linalg.norm(pout-.03*nout,axis=-1))
        def port():
            # Avoid division on either flat end. The complete measured inner
            # and outer heights are still read independently of this diagnostic.
            inside=(g["t"]>=.15)&(g["t"]<=.85)
            if inside.sum()<3 or np.min(E[inside])<=1+1e-12:
                return {"available":False,"reason":"positive radial slope unavailable on this compact interval"}
            xrad=g["r"][inside]
            w=np.sqrt(E[inside]-1)
            if fixed_E is not None:
                return {"available":False,"reason":"derivative of fixed reference read separately"}
            # Body-rotated Drr represents the actual physical second derivative.
            wx=dot(st["D"],st["Drr"]).mean(axis=1)[inside]/w
            phi=g["phi"]
            def first(v,angular):
                return 2*np.mean(v*angular[None,:],axis=1)[inside]
            vr=F_r-g["er"]
            vr=vr.copy()
            vr[...,2]+=np.sqrt(np.maximum(st["E"]-1,0))[:,None]
            vp=F_p-r[...,None]*g["et"]
            P=-first(dot(vr,vr),np.cos(phi))/2
            Q=-first(dot(vp,vp),np.cos(phi))/(2*xrad)
            S=-first(dot(vr,vp),np.sin(phi))
            pe=first(e-E[:,None],np.cos(phi))/2
            qe=first(gg-r*r,np.cos(phi))/(2*xrad)
            se=first(f,np.sin(phi))
            def integ(p,qv,sv):
                v=qv/(w*xrad)
                return float(v[-1]-v[0]+np.trapezoid(qv*wx/(w*w*xrad)-sv/(w*xrad*xrad)-p/(w*xrad),xrad))
            measured=first(F[...,2],np.cos(phi))/xrad
            uncorrected,correction=integ(P,Q,S),integ(pe,qe,se)
            return dict(available=True,interval=[float(xrad[0]),float(xrad[-1])],
                        sampled_measured_change=float(measured[-1]-measured[0]),
                        full_displacement_quadratic_port=uncorrected,
                        full_metric_defect_correction=correction,
                        sampled_quadrature_difference=float(measured[-1]-measured[0]-uncorrected-correction))
        minus_normal=np.array([-math.sin(self.ang),0.,-math.cos(self.ang)])
        observed_patch_support=max(float((F@minus_normal).max()),float(inner_center@minus_normal))
        sphere_support_low=(-(5/12)*math.sin(self.ang)+(.35+.045)*math.cos(self.ang)+.04499)
        intrinsic=None
        if fixed_E is None:
            value=dot(st["D"],st["Drr"]).mean(axis=1)/(g["r"]*E**2)
            jmax=int(np.argmax(abs(value)))
            intrinsic=dict(sampled_max_abs_G=float(abs(value[jmax])),
                           physical_radius=float(g["r"][jmax]),
                           sampled_ratio_to_reach_limit=float(.03**2*abs(value[jmax])))
        return dict(sampled_metric_max_relative=float(metric[ix]),metric_attainer=loc(ix),
                    sampled_design_intrinsic_Gaussian=intrinsic,
                    sampled_tangent_derivative_alias=st["sampled_tangent_derivative_alias"],
                    sampled_complete_meridian_length=float(np.trapezoid(np.sqrt(E),g["r"])),
                    necessary_meridian_from_actual_pose=math.sqrt(float(inner_center@inner_center)+
                        (self.b-self.a)**2+2*self.a*self.b*(1-math.cos(self.ang))),
                    exact_R655_spherical_support_difference=2*(5/12)*math.sin(self.ang),
                    sampled_R655_spherical_dominance_margin_min=sphere_support_low-observed_patch_support,
                    sampled_annulus_max_outer_horizontal_radius=float(np.linalg.norm(pout,axis=-1).max()),
                    sampled_max_principal_curvature=float(kabs[ixk]),curvature_attainer=loc(ixk),
                    sampled_gauss_abs_max=float(abs(gauss).max()),sampled_horizontal_jacobian_min=float(
                        np.cross(F_r,F_p)[...,2].min()),
                    sampled_E_range=[float(E.min()),float(E.max())],
                    ring_closure_max=float(abs(st["T"][...,1].mean(axis=1)).max()),
                    actual_inner_center=inner_center.tolist(),actual_tilt_sine=math.sin(self.ang),
                    physical_a=self.a,physical_b=self.b,
                    sampled_annulus_z_range=[float(F[...,2].min()),float(F[...,2].max())],
                    sampled_annular_inner_tube_cylinder_margin=float(imin.min()-self.a),
                    sampled_annular_outer_tube_cylinder_margin=float(self.b-omax.max()),
                    full_finite_tilt_port=port(),global_tube_verified=False)


def extend_exactly(old,x,new):
    """Degree-preserving midpoint insertion and zero-extension in Fourier order."""
    if new.K<old.K or new.nsp%old.nsp or new.spec["seed_slope_peak"]!=old.spec["seed_slope_peak"]:
        raise ValueError("Incompatible nested test spaces.")
    uq,vq,cq=old.split(x)
    result=np.zeros(new.size)
    un,vn,cn=new.split(result)
    newknots=np.linspace(old.a,old.b,new.nsp+1)[1:-1]
    insert=[k for k in newknots if not np.any(np.isclose(old.knots,k,rtol=0,atol=1e-14))]
    def refine(matrix,padding):
        shape=np.zeros((old.nb,len(matrix)))
        shape[padding:-padding]=matrix.T
        f=BSpline(old.knots,shape,old.degree)
        for knot in insert:
            f=f.insert_knot(float(knot))
        return f.c[padding:-padding].T
    un[:old.K]=refine(uq,3)
    vn[:old.K]=refine(vq,3)
    cn[:]=refine(cq,2)
    return result


def peg_readout(a,d,h,tilt):
    from scipy.integrate import cumulative_trapezoid, quad
    e=1/20
    rf=.032
    end=np.pi/2+e
    u=np.unique(np.r_[np.linspace(0,end,513),e,end-e])
    theta=np.where(u<e,u*u/(2*e),np.where(u>end-e,np.pi/2-(end-u)**2/(2*e),u-e/2))
    r1=a-rf*cumulative_trapezoid(np.cos(theta),u,initial=0)
    z1=rf*cumulative_trapezoid(np.sin(theta),u,initial=0)
    neck=r1[-1]
    k=quad(lambda z:math.sin(z*z/(2*e)),0,e)[0]+math.cos(e/2)
    rc=neck/k
    q=np.unique(np.r_[np.linspace(0,np.pi/2+e/2,513),e])
    turn=np.where(q<e,q*q/(2*e),q-e/2)
    r3=neck-rc*cumulative_trapezoid(np.sin(turn),q,initial=0)
    z3=z1[-1]+.201+rc*cumulative_trapezoid(np.cos(turn),q,initial=0)
    r3[-1]=0.
    rs=np.r_[r1,neck,r3]
    zz=np.r_[z1,z1[-1]+.201,z3]
    angle=np.r_[theta,np.pi/2,np.pi/2-turn]
    cs,ss=math.cos(tilt),math.sin(tilt)
    def xymax(rad,height):
        off=d+ss*height
        v=np.clip(off*cs/np.maximum(rad*ss*ss,1e-30),-1,1)
        return np.sqrt((off+cs*rad*v)**2+rad**2*(1-v*v))
    reach_proj=[]
    for t in (-.03,.03):
        reach_proj.append(float(xymax(rs+t*np.sin(angle),zz+t*np.cos(angle)).max()))
    return dict(physical_neck=float(neck),physical_pole_height=float(z3[-1]),fixed_open_hold_diameter_lower=.201,
                sampled_outer_horizontal_radius=float(xymax(rs,zz).max()),
                sampled_outer_tube_horizontal_radius=max(reach_proj),
                sampled_outer_z_range=[float(np.min(h+cs*zz-ss*rs)),float(np.max(h+cs*zz+ss*rs))])


def main():
    if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY","").lower()!="rogerhu12/math-research-public" or
        not os.environ.get("GITHUB_RUN_ID","").isdigit()):
        raise SystemExit("Scientific execution requires public math-research-public Actions.")
    p=argparse.ArgumentParser()
    p.add_argument("--geometry",required=True)
    p.add_argument("--max-seconds",type=float,default=1100.)
    args=p.parse_args()
    options=json.loads(Path(args.geometry).read_text())
    start=time.perf_counter()
    count=Counter()
    def elapsed():
        return time.perf_counter()-start
    if not 0<options["base"]["a"]<options["base"]["b"] or options["base"]["tilt_sine"]!=.36:
        raise ValueError("Incorrect fixed finite-tilt geometry.")
    emit("provenance",run_id=os.environ["GITHUB_RUN_ID"],
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         geometry_sha256=hashlib.sha256(Path(args.geometry).read_bytes()).hexdigest(),
         max_seconds=args.max_seconds,complete_original_columns=True,
         tilt_sine=options["base"]["tilt_sine"],old_R652_or_R657_transfer_replayed=False)
    current=None
    x=None
    frozen=None
    trust=float(options["initial_trust"])
    accepted=0
    timeline=[]
    final_detail=None
    final_refined=False
    def frozen_on(grid):
        if frozen is None:
            return None
        fs,fx=frozen
        return fs.state(fx,fs.at(grid["r"],options["frozen_reference_azimuths"]))["E"]
    def check(sys,params,order,nphi,with_peg=False):
        grid=sys.grid(order,nphi,endpoints=True)
        data=sys.readout(params,grid,frozen_on(grid))
        if frozen is not None:
            fs,fx=frozen
            independent=fs.state(fx,fs.at(grid["r"],options["frozen_check_azimuths"]))["E"]
            locked=frozen_on(grid)
            data["sampled_frozen_reference_relative_angular_difference"]=float(np.max(abs(independent/locked-1)))
        if with_peg:
            cx,_,cz=data["actual_inner_center"]
            peg=peg_readout(sys.a,cx,cz,sys.ang)
            data["peg_geometry"]=peg
            radius=max(data["sampled_annulus_max_outer_horizontal_radius"],peg["sampled_outer_horizontal_radius"])
            zmin=min(data["sampled_annulus_z_range"][0],peg["sampled_outer_z_range"][0])
            zmax=max(data["sampled_annulus_z_range"][1],peg["sampled_outer_z_range"][1])
            z0=.045
            far_disk=math.hypot(1/3+radius,max(abs(zmin+z0),abs(zmax+z0)))
            far_point=math.hypot(5/12+radius,max(abs(zmin+.35+z0),abs(zmax+.35+z0)))
            data["sampled_complete_D_budget_estimate"]=max(
                max(2/3,math.hypot(.75,.35))+2*.04501,
                max(far_disk,far_point)+.04501,math.hypot(2*radius,zmax-zmin))
            data["sampled_moving_disk_envelope"]=dict(horizontal_radius=radius,z_min=zmin,z_max=zmax)
        return data
    try:
        spaces=list(options["spaces"])
        for phase_i,phase in enumerate(spaces):
            if elapsed()>args.max_seconds-options["final_readout_seconds"]:
                break
            spec=dict(options["base"],radial_spans=phase["spans"],body_modes=phase["modes"])
            sys=LatitudeSystem(spec,count)
            if current is None:
                x=sys.seed()
            else:
                old=current
                oldx=x.copy()
                x=extend_exactly(old,oldx,sys)
                count["exact_spline_fourier_prolongations"]+=1
            current=sys
            work=sys.grid(phase["radial_order"],phase["azimuths"])
            reference_E=frozen_on(work)
            r,st=sys.residual(x,work,reference_E)
            before=float(np.linalg.norm(r))
            emit("space_started",space=phase_i,spans=sys.nsp,modes=sys.K,
                 original_columns=sys.size,all_residual_rows=len(r),objective_norm=before,
                 frozen_metric=frozen is not None,elapsed_seconds=elapsed())
            step_count=0
            emit("space_initial_candidate",space=phase_i,actual_complete_state=x.tolist(),
                 work_objective_norm=before)
            for iteration in range(phase["iterations"]):
                if elapsed()>args.max_seconds-options["final_readout_seconds"]:
                    break
                jac=sys.jacobian(st,work,fixed=frozen is not None)
                if iteration==0:
                    direction=np.sin(np.arange(1,sys.size+1)*.731)
                    direction/=np.linalg.norm(direction)
                    eps=2e-6
                    plus,_=sys.residual(x+eps*direction,work,reference_E)
                    minus,_=sys.residual(x-eps*direction,work,reference_E)
                    fd=(plus-minus)/(2*eps)
                    error=np.linalg.norm(jac@direction-fd)/max(np.linalg.norm(fd),1e-20)
                    emit("complete_J_contraction",space=phase_i,all_columns=sys.size,
                         central_difference_epsilon=eps,relative_difference=float(error))
                    if error>1e-5:
                        raise ArithmeticError("Finite difference disagrees with the actual complete Jacobian.")
                # FULL_COLUMN_QR/SVD: every original column is retained in
                # each damped least-squares direction, including tiny sigma.
                q,rb=qr(jac,mode="economic",check_finite=False,overwrite_a=True)
                rhs=q.T@r
                del q,jac
                uj,svals,vt=svd(rb,full_matrices=False,check_finite=False)
                count["complete_QR_SVD"]+=1
                transformed=-(uj.T@rhs)
                l2=float(r@r)
                accepted_here=False
                least_damp=max(1e-18,1e-13*float(svals[0])**2)
                for trial in range(12):
                    def amplitudes(mu):
                        return transformed*svals/(svals*svals+mu)
                    damp=least_damp
                    if np.linalg.norm(amplitudes(damp))>trust:
                        upper=damp
                        while np.linalg.norm(amplitudes(upper))>trust:
                            upper*=8
                        lower=damp
                        for _ in range(36):
                            mid=math.sqrt(lower*upper)
                            if np.linalg.norm(amplitudes(mid))>trust:
                                lower=mid
                            else:
                                upper=mid
                        damp=upper
                    al=amplitudes(damp)
                    dx=vt.T@al
                    predicted=2*float(transformed@(svals*al))-float((svals*al)@(svals*al))
                    newr,newst=sys.residual(x+dx,work,reference_E)
                    new_l2=float(newr@newr)
                    gain=(l2-new_l2)/predicted if predicted>0 else -math.inf
                    count["actual_full_metric_trials"]+=1
                    if new_l2<l2 and gain>.025:
                        x=x+dx
                        r,st=newr,newst
                        accepted+=1
                        step_count+=1
                        if gain>.75 and np.linalg.norm(dx)>.8*trust:
                            trust=min(2*trust,options["max_trust"])
                        elif gain<.20:
                            trust=max(.45*trust,1.e-11)
                        accepted_here=True
                        if accepted_here:
                            emit("accepted",actual_complete_state=x.tolist(),space=phase_i,iteration=iteration,accepted=accepted,
                                 objective_norm=math.sqrt(new_l2),trust=trust,damping=damp,
                                 smallest_retained_sigma=float(svals[-1]),largest_sigma=float(svals[0]),
                                 elapsed_seconds=elapsed())
                        break
                    trust*=.35
                    if trust<1e-11:
                        break
                if not accepted_here or np.linalg.norm(r)<options["work_l2_goal"]:
                    break
            detail=check(sys,x,phase["fine_radial_order"],phase["fine_azimuths"],True)
            final_detail=detail
            record=dict(space=phase_i,accepted=step_count,start_objective_norm=before,
                        last_work_objective_norm=float(np.linalg.norm(r)),fine=detail,
                        frozen_metric=frozen is not None,actual_complete_state=x.tolist(),elapsed_seconds=elapsed())
            timeline.append(record)
            emit("space_finished",**record,counts=dict(count))
            if frozen is not None and step_count>0:
                final_refined=True
            if frozen is None and detail["sampled_metric_max_relative"]<=options["freeze_fine_metric_gate"]:
                frozen=(sys,x.copy())
                if phase_i==len(spaces)-1:
                    spaces.append(options["last_fixed_space"])
                emit("metric_frozen",space=phase_i,retained_parameter_count=sys.size,
                     angular_reference_order=options["frozen_reference_azimuths"],
                     fine_metric=detail["sampled_metric_max_relative"])
            trust=max(trust,options["promoted_trust_floor"])
        if current is None:
            raise RuntimeError("No finite-angle state computed.")
        # Independent higher-resolution point readout; same representation
        # and, if the gate was met, exactly the same frozen E function.
        last_grid=spaces[len(timeline)-1]
        other_grids={}
        for name,radial,angle in (("refine_radius_only",options["final_radial_order"],last_grid["fine_azimuths"]),
                                  ("refine_angle_only",last_grid["fine_radial_order"],options["final_azimuths"])):
            other_grids[name]=dict(radial_order=radial,azimuths=angle,readout=check(current,x,radial,angle))
        final_detail=check(current,x,options["final_radial_order"],options["final_azimuths"],True)
        emit("terminal",completed_spaces=len(timeline),actual_finite_tilt_sine=math.sin(current.ang),
             accepted=accepted,trust=trust,actual_complete_state=x.tolist(),
             final_space_spec=current.spec,final_readout=final_detail,
             final_crossed_grid_readouts=other_grids,
             frozen_reference=None if frozen is None else
                 dict(space=frozen[0].spec,coefficients=frozen[1].tolist(),
                      azimuths=options["frozen_reference_azimuths"]),
             fixed_metric_refinement_attempted=any(rec["frozen_metric"] for rec in timeline),
             accepted_fixed_metric_parameter_refinement=final_refined,counts=dict(count),
             elapsed_seconds=elapsed(),certified_all_points=False,README_completion_claim=False)
    except Exception as exc:
        emit("incomplete",reason=str(exc),actual_complete_state=None if x is None else x.tolist(),
             active_spec=None if current is None else current.spec,trust=trust,counts=dict(count),
             last_readout=final_detail,elapsed_seconds=elapsed())
        raise


if __name__=="__main__":
    main()

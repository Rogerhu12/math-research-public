#!/usr/bin/env python3
"""One new positive-height allocation, with unchanged ports/rho/clock/frozen g."""
from __future__ import annotations
import hashlib,importlib.util,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
BASE=HERE/"6a65-geometry-nonfold-polar-connector.py"
EXPECTED_BASE="eef82a0e7522a70762a4e44a265b86bbf67f6e7d6f5d94d84842ba55d3390002"
if hashlib.sha256(BASE.read_bytes()).hexdigest()!=EXPECTED_BASE:
    raise ValueError("Frozen original full polar source changed")
spec=importlib.util.spec_from_file_location("polar_original_immutable",BASE)
base=importlib.util.module_from_spec(spec);sys.modules[spec.name]=base;spec.loader.exec_module(base)
mul,inv,bernstein=base.mul,base.inv,base.bernstein
geometry_statistics=base.geometry_statistics
check=base.check

class NonfoldPolarConnector(base.NonfoldPolarConnector):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.height_epsilon=.15
        self.identities.update(originalPolarSourceSHA256=EXPECTED_BASE,
            sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            heightAllocation=dict(epsilon=.15,lateralWeight="sin(theta)^8",
                positiveInternalWeights="1/(epsilon^2+rho_s(j/N,theta)^2)",
                unchangedEndpointControls=True,unchangedTotalHeightIntegral=True,
                unchangedRhoAndMaterialClock=True,sameFrozenTargetMetric=True))
    def connector(self,s,u):
        u=np.asarray(u,float).reshape(-1);t=(float(s)-self.b)/self.L
        if not -2e-15<=t<=1+2e-15:raise ValueError("Connector s outside its physical domain")
        t=float(np.clip(t,0,1));L=self.L
        left_clock,right_clock=self.endpoint_clocks(u)
        clock_data=np.concatenate([np.stack([x["phi"],x["phis"],x["phiss"]])
            for x in (left_clock,right_clock)],axis=0)
        clock=np.stack([np.einsum("i,ijk->jk",self.warm.ports.hermite_weights(t,L,j),clock_data)
            for j in range(3)])
        theta=clock[0,0]
        left,er0=self.inverse(0,theta);right,er1=self.inverse(1,theta)
        logrho_data=np.concatenate([left["logrho"],right["logrho"]],axis=0)
        Q=np.stack([np.einsum("i,ijk->jk",self.warm.ports.hermite_weights(t,L,j),logrho_data)
            for j in range(3)])
        R=np.exp(Q[0,0]);Rs=R*Q[1,0];Rt=R*Q[0,1]
        Rss=R*(Q[2,0]+Q[1,0]**2)
        Rst=R*(Q[1,1]+Q[1,0]*Q[0,1])
        Rtt=R*(Q[0,2]+Q[0,1]**2)
        n=self.degree;lz,rz=left["z"],right["z"]
        controls=np.empty((n+1,3,len(u)))
        controls[0]=lz[1];controls[1]=lz[1]+L*lz[2]/n
        controls[-1]=rz[1];controls[-2]=rz[1]-L*rz[2]/n
        inner=((n+1)*(rz[0]-lz[0])/L-
            controls[0]-controls[1]-controls[-2]-controls[-1])/(n-3)
        # Redistribute only the free positive control mass. Every endpoint
        # velocity/acceleration, total height increment, rho and Theta stay.
        mass=inner*(n-3)
        mass_taylor=np.stack((mass[0],mass[1],mass[2]/2))
        sine=np.stack((np.sin(theta),np.cos(theta),-np.sin(theta)/2))
        lateral=np.zeros_like(sine);lateral[0]=1
        for unused in range(8):lateral=mul(lateral,sine)
        one=np.zeros_like(lateral);one[0]=1
        inverse_speeds=[]
        for control_index in range(2,n-1):
            tj=control_index/n
            log_at=np.einsum("i,ijk->jk",self.warm.ports.hermite_weights(tj,L,0),logrho_data)
            logs_at=np.einsum("i,ijk->jk",self.warm.ports.hermite_weights(tj,L,1),logrho_data)
            rr=np.exp(log_at[0])
            rrj=np.stack((rr,rr*log_at[1],rr*(log_at[2]+log_at[1]**2)/2))
            rsj=mul(rrj,np.stack((logs_at[0],logs_at[1],logs_at[2]/2)))
            denominator=mul(rsj,rsj);denominator[0]+=self.height_epsilon**2
            inverse_speeds.append(inv(denominator))
        inverse_speeds=np.stack(inverse_speeds)
        sum_inverse=np.sum(inverse_speeds,axis=0)
        for j,weight in enumerate(inverse_speeds,start=2):
            normalized=mul(weight,inv(sum_inverse))
            blend=(one-lateral)/(n-3)+mul(lateral,normalized)
            bj=mul(mass_taylor,blend)
            controls[j]=np.stack((bj[0],bj[1],2*bj[2]))
        zcontrols=np.concatenate([lz[0][None],lz[0][None]+L/(n+1)*np.cumsum(controls,axis=0)],axis=0)
        z=np.einsum("i,ijk->jk",bernstein(t,n+1),zcontrols)
        zs=np.einsum("i,ijk->jk",bernstein(t,n),controls)
        zss=np.einsum("i,ijk->jk",bernstein(t,n-1),n/L*np.diff(controls,axis=0))
        er=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=1)
        et=np.stack((-np.sin(theta),np.cos(theta),np.zeros_like(theta)),axis=1)
        ez=np.asarray([0.,0.,1.])
        Y=R[:,None]*er+z[0,:,None]*ez
        Ys=Rs[:,None]*er+zs[0,:,None]*ez
        Yt=Rt[:,None]*er+R[:,None]*et+z[1,:,None]*ez
        Yss=Rss[:,None]*er+zss[0,:,None]*ez
        Yst=Rst[:,None]*er+Rs[:,None]*et+zs[1,:,None]*ez
        Ytt=(Rtt-R)[:,None]*er+2*Rt[:,None]*et+z[2,:,None]*ez
        ts,tu,tss,tsu,tuu=clock[1,0],clock[0,1],clock[2,0],clock[1,1],clock[0,2]
        out=dict(X=Y,Xs=Ys+Yt*ts[:,None],Xu=Yt*tu[:,None],
            Xss=Yss+2*Yst*ts[:,None]+Ytt*ts[:,None]**2+Yt*tss[:,None],
            Xsu=Yst*tu[:,None]+Ytt*(ts*tu)[:,None]+Yt*tsu[:,None],
            Xuu=Ytt*tu[:,None]**2+Yt*tuu[:,None])
        clock_controls=np.stack((left_clock["phi"][1],
            left_clock["phi"][1]+L*left_clock["phis"][1]/5,
            left_clock["phi"][1]+2*L*left_clock["phis"][1]/5+L*L*left_clock["phiss"][1]/20,
            right_clock["phi"][1]-2*L*right_clock["phis"][1]/5+L*L*right_clock["phiss"][1]/20,
            right_clock["phi"][1]-L*right_clock["phis"][1]/5,right_clock["phi"][1]))
        out.update(segment="new_polar_monotone_height_connector",
            minimumClockControl=float(np.min(clock_controls)),
            minimumHeightControl=float(np.min(controls[:,0])),
            minimumInteriorHeightControl=float(np.min(controls[2:-2,0])),
            minimumRho=float(np.min(R)),minimumThetaU=float(np.min(tu)),
            minimumFixedThetaZs=float(np.min(zs[0])),
            maximumInverseResidual=max(er0,er1),
            polarCrossSquared=tu**2*(R**2*zs[0]**2+(zs[0]*Rt-Rs*z[1])**2+R**2*Rs**2))
        return out


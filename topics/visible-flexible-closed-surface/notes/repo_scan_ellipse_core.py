#!/usr/bin/env python3
"""Arc-length planar ellipse/generalized-cylinder inlet for the full flow.

The central core F(x,theta)=gamma(theta)+x e_z has exactly
g=dx^2+a0^2 dtheta^2.  Spectral quadrature/inversion below are numerical
representations of that exact formula.  Optional even radial corrections
vanish at both principal-axis vertices and preserve their aspect ratio.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import json
import math
from pathlib import Path
import sys
import numpy as np
from scipy.special import ellipe


class PlanarEllipseCore:
    def __init__(self,aspect=2.,corrections=(),arc_nodes=4096):
        if aspect<1:
            raise ValueError('Aspect ratio must be at least one')
        self.aspect=float(aspect)
        self.corrections=tuple(corrections)
        A,B=1.,1./aspect
        coefficients={1:(A+B)/2,-1:(A-B)/2}
        def add(k,value):
            coefficients[k]=coefficients.get(k,0.)+value
        for j,c in enumerate(corrections,start=2):
            # c[cos(2j phi)-1] for even j; c[cos(2j phi)-cos(2phi)] for odd j.
            # Both corrections vanish at phi=0 and phi=pi/2.
            add(2*j+1,c/2);add(1-2*j,c/2)
            if j%2==0:
                add(1,-c)
            else:
                add(3,-c/2);add(-1,-c/2)
        self.frequencies=np.array(sorted(coefficients),dtype=int)
        self.coefficients=np.array([coefficients[k] for k in self.frequencies],dtype=float)
        phi=2*np.pi*np.arange(arc_nodes)/arc_nodes
        raw=self.curve(phi)
        self.raw_a0=float(np.mean(raw['speed']))
        self.coefficients/=self.raw_a0
        self.major_radius=1./self.raw_a0
        self.minor_radius=1./(aspect*self.raw_a0)
        sampled=self.curve(phi)
        if np.min(sampled['signed_kappa'])<=0:
            raise FloatingPointError('Planar inlet is not strictly convex')
        speed=sampled['speed']
        coef=np.fft.rfft(speed)/arc_nodes
        self.a0=float(coef[0].real)
        active=np.flatnonzero(abs(coef[1:-1])>2e-16)
        K=int(active[-1]+1) if len(active) else 0
        self.k=np.arange(1,K+1)
        self.arccoef=coef[1:K+1]/(1j*self.k)
        self.speed_omitted_l1=float(2*np.sum(abs(coef[K+1:-1]))+abs(coef[-1]))
        self.arc_omitted_l1=float(4*np.sum(abs(coef[K+1:-1])/np.arange(K+1,len(coef)-1))+
                                  2*abs(coef[-1])/(len(coef)-1))
        self.minimum_sampled_curvature=float(np.min(sampled['signed_kappa']))
        self.maximum_sampled_curvature=float(np.max(sampled['signed_kappa']))

    def curve(self,phi):
        phi=np.asarray(phi)
        exponent=np.exp(1j*phi[...,None]*self.frequencies)
        values=[]
        for j in range(3):
            z=np.sum(exponent*(1j*self.frequencies)**j*self.coefficients,axis=-1)
            values.append(np.stack((z.real,z.imag,np.zeros_like(z.real)),axis=-1))
        F,d1,d2=values
        speed=np.linalg.norm(d1,axis=-1)
        speed_phi=np.sum(d1*d2,axis=-1)/speed
        signed=(d1[...,0]*d2[...,1]-d1[...,1]*d2[...,0])/speed**3
        return dict(F=F,d1=d1,d2=d2,speed=speed,speed_phi=speed_phi,signed_kappa=signed)

    def arc(self,phi):
        phi=np.asarray(phi)
        flat=phi.ravel()
        out=self.a0*flat
        for j in range(0,len(flat),2048):
            e=np.exp(1j*flat[j:j+2048,None]*self.k[None,:])-1
            out[j:j+2048]+=2*np.real(e@self.arccoef)
        return out.reshape(phi.shape)

    def evaluate(self,theta):
        theta=np.asarray(theta,dtype=float)
        phi=theta.copy()
        lo=np.floor(theta/(2*np.pi))*2*np.pi
        hi=lo+2*np.pi
        for j in range(70):
            geom=self.curve(phi)
            residual=self.arc(phi)-self.a0*theta
            done=abs(residual)<4e-15
            if np.all(done):
                break
            lo=np.where((residual<0)&~done,phi,lo)
            hi=np.where((residual>0)&~done,phi,hi)
            nxt=phi-residual/geom['speed']
            nxt=np.where((nxt<lo)|(nxt>hi)|~np.isfinite(nxt),(lo+hi)/2,nxt)
            phi=np.where(done,phi,nxt)
        geom=self.curve(phi)
        speed=geom['speed']
        Ft=self.a0*geom['d1']/speed[...,None]
        Ftt=self.a0**2*(geom['d2']/speed[...,None]**2-
                       geom['d1']*geom['speed_phi'][...,None]/speed[...,None]**3)
        return dict(F=geom['F'],Ft=Ft,Ftt=Ftt,phi=phi,
                    kappa=geom['signed_kappa'],arc_residual=self.arc(phi)-self.a0*theta)

    def inlet(self,obj,angular=1024):
        theta=2*np.pi*np.arange(angular)/angular
        geom=self.evaluate(theta)
        B,B1,B2=obj.basis(angular)
        C=obj.project(geom['F'][None,:,:],B)[:,0]
        projection=obj.values(C[:,None],B)[0]
        derivative=obj.values(C[:,None],B1)[0]
        return C,dict(
            coordinate_projection_error=float(np.max(np.linalg.norm(projection-geom['F'],axis=1))),
            metric_projection_error=float(np.max(abs(np.sum(derivative**2,axis=1)-self.a0**2))),
            exact_arclength_metric_error=float(np.max(abs(np.sum(geom['Ft']**2,axis=1)-self.a0**2))),
            arc_inversion_residual=float(np.max(abs(geom['arc_residual']))),
            radial_fundamental=float(C[1]),vertical_coefficients_max=float(np.max(abs(C[obj.iz:]))),
            core_aspect=self.aspect,major_radius=self.major_radius,minor_radius=self.minor_radius,
            minimum_sampled_curvature=self.minimum_sampled_curvature,
            maximum_sampled_curvature=self.maximum_sampled_curvature,
            initial_speed_limit=self.a0*self.minimum_sampled_curvature,
            arc_speed_omitted_l1=self.speed_omitted_l1)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    sys.path.insert(0,str(args.source_root/'topics/large-amplitude-twist-flex/scripts'))
    from f6curve_inward_bvp import InwardPrefix
    rows=[]
    for aspect in [1.,1.2,1.5,2.,10./3]:
        core=PlanarEllipseCore(aspect)
        analytic_raw_a0=2*ellipe(1-aspect**-2)/np.pi
        for modes in [2,4,8,12,16]:
            obj=InwardPrefix(modes,.01,.3,.4,.7,.3,1,256,2,compute_stable=False)
            C,metrics=core.inlet(obj,2048)
            y=(C[:,None]-obj.base(np.array([0.])))/obj.q
            first=obj.q*obj.fun(np.array([0.]),y,np.zeros(obj.M))[:,0]
            rows.append(dict(aspect=aspect,modes=modes,**metrics,
                initial_projected_nonmean_velocity=float(np.max(abs(first))),
                perimeter_quadrature_difference=abs(core.raw_a0-analytic_raw_a0)))
    report=dict(scope=__doc__,rows=rows)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    for aspect in [1.,1.2,1.5,2.,10./3]:
        row=next(r for r in rows if r['aspect']==aspect and r['modes']==16)
        print(json.dumps(row),flush=True)


if __name__=='__main__':
    main()

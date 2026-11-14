#!/usr/bin/env python3
"""Reconstruct actual tail cut Cartesian two-jets and compare a saved prefix.

The planar projection metric is g-dZ^2. Its connection determines the
Cartesian second derivatives wherever the projection is nonsingular.
This is a finite quadrature audit, not a continuous seam or closure proof.
The tail height mean is aligned by a vertical translation; its first and
second derivatives are independently compared and cannot be translated away.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
HERE=Path(__file__).resolve().parent


def primitive(values,theta):
    """Fourier primitive with its mean retained, normalized to zero at 0."""
    N=len(theta);hat=np.fft.fft(values,axis=0)/N
    k=np.fft.fftfreq(N,1/N);denom=1j*k;denom[0]=1
    shape=(N,)+(1,)*(values.ndim-1)
    coeff=hat/denom.reshape(shape);coeff[0]=0
    periodic=np.fft.ifft(coeff*N,axis=0).real
    return periodic-periodic[0]+theta.reshape(shape)*hat[0].real


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','checkpoint','port','tail-response','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--angular',type=int,nargs='+',default=[512,1024])
    a=p.parse_args()
    spec=importlib.util.spec_from_file_location('root_seam_saved',HERE/'geometric-checkpoint-core-pullback.py')
    pb=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pb;spec.loader.exec_module(pb)
    saved,loader=pb.load_saved(a.checkpoint,a.source_topic,a.port,max(a.angular))
    raw=json.loads(gzip.decompress(a.tail_response.read_bytes()))
    response=raw['response'];jets=response['jets'];L=saved.flow.end
    H=np.asarray(jets['height']);slope=np.asarray(jets['slope']);second=np.asarray(jets['second'])
    if len(H)!=saved.M:raise ValueError('The complete tail and prefix spectra must coincide')
    sigma=saved.flow.bridge.sigma;cut=saved.rec['physical_tail_cut']
    E=float(cut['E']);Ep=float(cut['Ep']);radius=float(cut['radius'])
    r,r_s,r_ss=[float(np.ravel(x)[0])for x in saved.flow.profile(np.array([L]))]
    rows=[]
    for N in a.angular:
        theta=2*np.pi*np.arange(N)/N;n=saved.mode*np.arange(1,len(H)+1)
        co=np.cos(theta[:,None]*n);si=np.sin(theta[:,None]*n)
        height=saved.height_jets(np.array([L]),angular=N)
        old={key:value[0]for key,value in saved.jets(np.array([L]),theta[None,:],height).items()}
        z=sigma*(co@H);z+=old['pos'][0,2]-z[0]
        zt=-sigma*(si@(n*H));ztt=-sigma*(co@(n*n*H))
        zs=(jets['meanSlope']+co@slope)/np.sqrt(E)
        zst=-(si@(n*slope))/np.sqrt(E)
        zss=sigma*((jets['meanSecond']+co@second)/E-Ep*(jets['meanSlope']+co@slope)/(2*E*E))
        metric=np.empty((N,2,2));metric[:,0,0]=1-zs*zs
        metric[:,0,1]=metric[:,1,0]=-zs*zt;metric[:,1,1]=radius*radius-zt*zt
        determinant=np.linalg.det(metric);G=metric[:,1,1];A=np.sqrt(G)
        if np.min(determinant)<=0 or np.min(G)<=0:raise FloatingPointError('Tail cut planar projection is singular')
        U0=old['p1'][0,:2];V0=old['s1'][0,:2]
        orientation=np.sign(U0[0]*V0[1]-U0[1]*V0[0])
        if orientation==0:raise FloatingPointError('Prefix projection is singular at alignment point')
        # U=X_theta=A e(phi), V=X_s=b e(phi)+c e_perp(phi).
        angle_derivative=(-radius*r_s-radius*radius*zs*ztt/G)/(orientation*np.sqrt(determinant))
        angle=np.arctan2(U0[1],U0[0])+primitive(angle_derivative,theta)
        e=np.c_[np.cos(angle),np.sin(angle)];ep=np.c_[-e[:,1],e[:,0]]
        U=A[:,None]*e
        V=(metric[:,0,1]/A)[:,None]*e+(orientation*np.sqrt(determinant)/A)[:,None]*ep
        X=primitive(U,theta)+old['pos'][0,:2]
        # dg[point, derivative-coordinate, metric-row, metric-column].
        dg=np.empty((N,2,2,2))
        dg[:,0,0,0]=-2*zs*zss;dg[:,1,0,0]=-2*zs*zst
        dg[:,0,0,1]=dg[:,0,1,0]=-zss*zt-zs*zst
        dg[:,1,0,1]=dg[:,1,1,0]=-zst*zt-zs*ztt
        dg[:,0,1,1]=2*radius*r_s-2*zt*zst;dg[:,1,1,1]=-2*zt*ztt
        inverse=np.linalg.inv(metric);Gamma=np.zeros((N,2,2,2))
        for k in range(2):
            for i in range(2):
                for j in range(2):
                    for ell in range(2):
                        Gamma[:,k,i,j]+=.5*inverse[:,k,ell]*(dg[:,i,j,ell]+dg[:,j,i,ell]-dg[:,ell,i,j])
        def planar_second(i,j):return Gamma[:,0,i,j,None]*V+Gamma[:,1,i,j,None]*U
        new=dict(pos=np.c_[X,z],p1=np.c_[U,zt],s1=np.c_[V,zs],
            p2=np.c_[planar_second(1,1),ztt],sp=np.c_[planar_second(0,1),zst],
            s2=np.c_[planar_second(0,0),zss])
        errors={key:float(np.max(np.linalg.norm(new[key]-old[key],axis=1)))for key in new}
        chart=saved.angle(np.array([L]),theta[None,:])
        rows.append(dict(angular=N,cartesian_errors=errors,
            mean_first_error=float(height[1][0]-jets['meanSlope']/np.sqrt(E)),
            mean_second_error=float(height[2][0]-sigma*(jets['meanSecond']/E-Ep*jets['meanSlope']/(2*E*E))),
            angle_holonomy_error=float(2*np.pi*(np.mean(angle_derivative)-1)),
            planar_curve_closure_error=float(np.linalg.norm(2*np.pi*np.mean(U,axis=0))),
            projected_metric_determinant_min=float(np.min(determinant)),orientation=float(orientation),
            chart_identity_errors={key:float(np.max(abs(chart[key]-(1 if key=='rho'else 0))))
                for key in ('rho','theta_s','theta_ss','rho_s','rhop_s')},
            max_height_first=float(np.max(abs(zs))),max_height_second=float(np.max(abs(zss)))))
    data=dict(scope=__doc__,source_revision=loader.source_revision(a.source_topic),
        checkpoint=str(a.checkpoint),checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
        tail_response=str(a.tail_response),tail_response_sha256=hashlib.sha256(a.tail_response.read_bytes()).hexdigest(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        cut_radius_error=r-radius,cut_first_error=r_s-sigma/np.sqrt(E),
        cut_second_error=r_ss+Ep/(2*E*E),tail_residual=response['residual'],rows=rows)
    a.out.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data))


if __name__=='__main__':main()

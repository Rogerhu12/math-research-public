#!/usr/bin/env python3
"""Floating diagnostic of the actual fixed-target local waist correction.

No interval certification is claimed.  The source is the full R117 two-jet
expression for the updated geometry and the ORIGINAL target.  The initial
primitive is truncated, and the correction's angular derivatives are a
finite spectral differentiation.  The report names those omissions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np

from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_core_low_block import uniform_fields


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dot(a,b):return np.sum(a*b,axis=-1)
def trace(a,inv):return sum(inv[i][j]*a[i][j] for i in range(2) for j in range(2))
def bilinear(a,x,y):return sum(a[i][j]*x[i]*y[j] for i in range(2) for j in range(2))
def inner(a,b,inv):return sum(inv[i][k]*inv[j][l]*a[i][j]*b[k][l] for i in range(2) for j in range(2) for k in range(2) for l in range(2))
def inverse(a,d):return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]


def angular_derivative(v):
    """Physical theta derivative represented in the rotating frame."""
    freq=4*np.fft.fftfreq(len(v),1/len(v))
    out=np.fft.ifft(1j*freq[:,None]*np.fft.fft(v,axis=0),axis=0).real
    out[:,0]-=v[:,1];out[:,1]+=v[:,0]
    return out


def source_and_geometry(fields,target):
    F,X,Y,Frr,Frt,Ftt=fields
    first=[X,Y];second=[[Frr,Frt],[Frt,Ftt]]
    E,E1,a,a1,a2=[target[k] for k in ('E','E_x','a','a_x','a_xx')]
    K0=-a2/(a*E)+a1*E1/(2*a*E*E)
    g=[[dot(first[i],first[j]) for j in range(2)] for i in range(2)]
    g0=[[E,0.],[0.,a*a]];g0inv=[[1/E,0.],[0.,1/(a*a)]]
    f=[[g0[i][j]-g[i][j] for j in range(2)] for i in range(2)]
    dg0=[[[E1,0.],[0.,2*a*a1]],[[0.,0.],[0.,0.]]]
    df=[[[dg0[k][i][j]-dot(second[k][i],first[j])-dot(first[i],second[k][j]) for j in range(2)] for i in range(2)] for k in range(2)]
    C=np.cross(Y,X);G=dot(C,C);T=dot(F,F);S=dot(C,F)
    if min(np.min(G),np.min(T),np.min(S))<=0:raise ValueError('updated immersion/star shape failed')
    L,M,N=[dot(C,z) for z in (Frr,Frt,Ftt)]
    t=[dot(F,v) for v in first]
    ff2=[[dot(F,second[i][j]) for j in range(2)] for i in range(2)]
    t2=[[g[i][j]+ff2[i][j] for j in range(2)] for i in range(2)]
    lower=[[[dot(first[l],second[i][j]) for j in range(2)] for i in range(2)] for l in range(2)]
    gi=inverse(g,G)
    sm=[[g[i][j]/T-t[i]*t[j]/T**2 for j in range(2)] for i in range(2)]
    sd=S*S/T**3;si=inverse(sm,sd)
    slower=[[[lower[l][i][j]/T-(g[l][i]*t[j]+g[l][j]*t[i]+t[l]*ff2[i][j])/T**2+2*t[l]*t[i]*t[j]/T**3 for j in range(2)] for i in range(2)] for l in range(2)]
    cg=[[[sum(gi[k][l]*lower[l][i][j] for l in range(2)) for j in range(2)] for i in range(2)] for k in range(2)]
    cs=[[[sum(si[k][l]*slower[l][i][j] for l in range(2)) for j in range(2)] for i in range(2)] for k in range(2)]
    bf=[[[cg[k][i][j]-cs[k][i][j] for j in range(2)] for i in range(2)] for k in range(2)]
    covg=[[[df[k][i][j]-sum(cg[m][k][i]*f[m][j]+cg[m][k][j]*f[i][m] for m in range(2)) for j in range(2)] for i in range(2)] for k in range(2)]
    dc=[[[sum(g0inv[k][l]*(covg[i][j][l]+covg[j][i][l]-covg[l][i][j]) for l in range(2))/2 for j in range(2)] for i in range(2)] for k in range(2)]
    tau=[trace(bf[k],si) for k in range(2)];dtau=[trace(dc[k],si) for k in range(2)]
    q=bilinear(f,tau,tau)+2*bilinear(g0,tau,dtau)+bilinear(g0,dtau,dtau)
    for i in range(2):
        for j in range(2):
            for u in range(2):
                for v in range(2):
                    bi=[bf[k][i][j] for k in range(2)];bu=[bf[k][u][v] for k in range(2)]
                    di=[dc[k][i][j] for k in range(2)];du=[dc[k][u][v] for k in range(2)]
                    q-=si[i][u]*si[j][v]*(bilinear(f,bi,bu)+2*bilinear(g0,bi,du)+bilinear(g0,di,du))
    zd=[]
    for i in range(2):
        z=sum(f[i][k]*tau[k]+g0[i][k]*dtau[k] for k in range(2))
        z-=sum(si[j][l]*(f[k][l]*bf[k][i][j]+g0[k][l]*dc[k][i][j]) for j in range(2) for l in range(2) for k in range(2))
        zd.append(z)
    hf=[[8*t[i]*t[j]/T**3-2*t2[i][j]/T**2+2*sum(cs[k][i][j]*t[k] for k in range(2))/T**2 for j in range(2)] for i in range(2)]
    tf=trace(f,si)
    curvature=2*(K0*(E*a*a-G)-(L*N-M*M-K0*G*G)/G)/sd
    pieces=dict(connection=(q-2*tf)/T,curvature=curvature/T,
        density_gradient=-4*bilinear(si,t,zd)/T**2,
        density_hessian=inner(hf,f,si)-trace(hf,si)*tf)
    source=-sum(pieces.values())/2
    metricnorm=np.sqrt((f[0][0]/E)**2+2*(f[0][1]/(a*np.sqrt(E)))**2+(f[1][1]/a**2)**2)
    return dict(q=source,jq=S/T**1.5*source,metric_norm=metricnorm,
        metric=g,connection=cg,normal=C/np.sqrt(G)[:,None],
        actual_K=(L*N-M*M)/G**2,K0=K0,
        immersion=np.min(G),support=np.min(S/np.sqrt(G)),pieces=pieces)


def correction_norms(Vjet,old_geometry):
    V,Vr,Vt,Vrr,Vrt,Vtt=Vjet;first=[Vr,Vt];second=[[Vrr,Vrt],[Vrt,Vtt]]
    g=old_geometry['metric'];cg=old_geometry['connection']
    h=[[second[i][j]-sum(cg[k][i][j][:,None]*first[k] for k in range(2)) for j in range(2)] for i in range(2)]
    w=g[0][1]/g[0][0];res=g[1][1]-g[0][1]*w
    g1=Vr/np.sqrt(g[0][0])[:,None]
    g2=(Vt-w[:,None]*Vr)/np.sqrt(res)[:,None]
    H11=h[0][0]/g[0][0][:,None]
    H12=(h[0][1]-w[:,None]*h[0][0])/np.sqrt(g[0][0]*res)[:,None]
    H22=(h[1][1]-2*w[:,None]*h[0][1]+(w*w)[:,None]*h[0][0])/res[:,None]
    nu=old_geometry['normal'];normal=[dot(nu,x) for x in (H11,H12,H22)]
    return dict(C0=float(np.max(np.sqrt(dot(V,V)))),
        original_induced_C1=float(np.max(np.sqrt(dot(g1,g1)+dot(g2,g2)))),
        original_induced_H11=float(np.max(np.sqrt(dot(H11,H11)))),
        original_induced_H12=float(np.max(np.sqrt(dot(H12,H12)))),
        original_induced_H22=float(np.max(np.sqrt(dot(H22,H22)))),
        original_induced_Hessian_HS=float(np.max(np.sqrt(dot(H11,H11)+2*dot(H12,H12)+dot(H22,H22)))),
        old_normal_Hessian_HS=float(np.max(np.sqrt(normal[0]**2+2*normal[1]**2+normal[2]**2))))


def scalar_target(geometry,r):
    return {k:float(v[0]) for k,v in geometry.radial_target_metric([r]).items()}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--radii',default='0,0.0001,0.0005,0.001,0.002,0.005,0.01,0.015,0.02,0.03,0.05,0.075,0.1')
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();started=time.monotonic()
    geometry,definition=load_exact_object(args.object,args.nodes)
    waist=uniform_fields(geometry,0.,args.angles);F,X,Y,Frr,Frt,Ftt=waist
    t0=scalar_target(geometry,0.);newX=np.zeros_like(X);newX[:,2]=np.sqrt(t0['E'])
    newFrr=-t0['a']*t0['a_xx']*Ftt/dot(Ftt,Ftt)[:,None]
    V1=newX-X;V2=newFrr-Frr
    V1t=angular_derivative(V1);V2t=angular_derivative(V2)
    V1tt=angular_derivative(V1t);V2tt=angular_derivative(V2t)
    rows=[]
    for r in map(float,args.radii.split(',')):
        old=uniform_fields(geometry,r,args.angles);tgt=scalar_target(geometry,r)
        V=(r*V1+.5*r*r*V2,V1+r*V2,r*V1t+.5*r*r*V2t,V2,V1t+r*V2t,r*V1tt+.5*r*r*V2tt)
        new=tuple(x+v for x,v in zip(old,V))
        before=source_and_geometry(old,tgt);after=source_and_geometry(new,tgt)
        row=dict(r=r,original_source_C0=float(np.max(abs(before['q']))),
            updated_source_C0=float(np.max(abs(after['q']))),
            original_metric_defect_C0=float(np.max(before['metric_norm'])),
            updated_metric_defect_C0=float(np.max(after['metric_norm'])),
            updated_curvature_defect_C0=float(np.max(abs(after['actual_K']-after['K0']))),
            updated_support_min=float(after['support']),**correction_norms(V,before))
        rows.append(row);print(row,flush=True)
    freq=np.fft.fftfreq(args.angles,1/args.angles)
    coeff=np.fft.fft(V2,axis=0)/args.angles
    doc=dict(kind='floating_actual_local_waist_polynomial_correction',complete=True,certified=False,
        whole_real_angular_circle=False,whole_parameter_interval=False,whole_radial_domain=False,
        source_sha256=sha(__file__),object_sha256=sha(args.object),
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in ('fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py','fourfold_phase_core_low_block.py')},
        initial_target='original geometry E=<|F_r|^2>, a^2 frozen before the correction at every r',
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        angular_grid=args.angles,primitive_nodes=args.nodes,rows=rows,
        V2_finite_coefficient_l1_outside_physical_threshold={str(4*m):float(np.sum(abs(coeff[abs(freq)>m]))) for m in (8,16,32,64,128)},
        limitations=['No validated roundoff, angular aliasing or Fourier tails for the correction.',
            'Only the listed radial slices and the exact center parameter are sampled; no continuous cover is claimed.',
            'V=r V1+r^2 V2/2 is an actual local polynomial extension, not a global Newton solve; no cutoff is installed.',
            'Regular/mean matching, cap return and global boundary conditions are not imposed.'],
        wall_seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(doc,indent=2)+'\n')


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Scalar u,v,beta two-jets for the exact cosine-core orthonormal frame.

The beta lift is defined by an exact angle-derivative integral, with the
periodic even branch supplied by the cosine symmetry theorem. Its floating
evaluation uses fixed Gauss quadrature and is not a continuous certificate.
All material derivatives keep theta fixed and use genuine high core jets.
Positive and negative outward ports are handled without changing the core.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from cosine_rectifying_core import CosineRectifyingCore,identity_hash
from cosine_core_high_jets import material_frame_two_jets


def dot(a,b):return np.sum(a*b,axis=-1)


def cross2(a,b):return a[...,0]*b[...,1]-a[...,1]*b[...,0]


def scale(a,b):return np.asarray(a)[...,None]*b


class BetaLiftPrimitive:
    """The exact mathematical lift beta0+integral_0^phi beta_phi, evaluated.

    Cosine symmetry makes the lift even and 2*pi/3-periodic. Evaluating its
    representative on [0,pi/3] enforces those identities without unwrapping
    sampled atan2 values. Nonzero curvature throughout remains a hypothesis
    that an independent frozen-core certificate must provide for research.
    """
    def __init__(self,core,cells=256,quadrature=16):
        self.core=core;self.identity_sha256=core.identity_sha256
        self.cells=int(cells);self.quadrature=int(quadrature)
        if self.cells<8 or self.quadrature<4:
            raise ValueError('beta primitive needs at least eight cells and order four')
        self.period=2*np.pi/3;self.half_period=np.pi/3
        self.step=self.half_period/self.cells
        self.gauss_x,self.gauss_w=leggauss(self.quadrature)
        L,Q,_,_=self.components(np.asarray(0.))
        self.beta0=float(np.arctan2(Q,L))
        midpoint=(np.arange(self.cells)+.5)*self.step
        phi=midpoint[:,None]+self.step*self.gauss_x[None,:]/2
        integrals=self.step/2*(self.derivative(phi)@self.gauss_w)
        self.prefix=np.r_[0.,np.cumsum(integrals)]

    def components(self,phi):
        _,v1,v2,v3,_=self.core.raw_jets(phi)
        p=np.linalg.norm(v1[...,:2],axis=-1);speed=np.linalg.norm(v1,axis=-1)
        if np.any(p<=0) or np.any(speed<=0):
            raise ValueError('nonzero horizontal tangent and speed are required')
        pp=dot(v1[...,:2],v2[...,:2])/p
        ppp=(dot(v2[...,:2],v2[...,:2])+dot(v1[...,:2],v3[...,:2])-pp**2)/p
        speed_p=dot(v1,v2)/speed
        A=cross2(v1[...,:2],v2[...,:2]);Ap=cross2(v1[...,:2],v3[...,:2])
        L=p*v2[...,2]-pp*v1[...,2]
        Lp=p*v3[...,2]-ppp*v1[...,2]
        Q=-speed*A/p
        Qp=-(speed_p*A+speed*Ap)/p+speed*A*pp/p**2
        if np.any(L*L+Q*Q<=0):
            raise ValueError('nonzero Frenet curvature is required; no regularization is used')
        return L,Q,Lp,Qp

    def derivative(self,phi):
        L,Q,Lp,Qp=self.components(phi)
        return (L*Qp-Q*Lp)/(L*L+Q*Q)

    def value(self,phi):
        if identity_hash(self.core.identity)!=self.identity_sha256:
            raise ValueError('the primitive physical identity changed')
        phase=np.mod(np.asarray(phi,float),self.period)
        representative=np.minimum(phase,self.period-phase)
        index=np.minimum((representative/self.step).astype(int),self.cells-1)
        left=index*self.step;half=(representative-left)/2
        points=left[...,None]+half[...,None]*(1+self.gauss_x)
        tail=half*np.sum(self.derivative(points)*self.gauss_w,axis=-1)
        return self.beta0+self.prefix[index]+tail


def angle_two_jets(vector,jets):
    """Derivatives of a continuous arg(vector) from genuine Cartesian jets."""
    radius2=dot(vector,vector)
    if np.any(radius2<=0):raise ValueError('angle vector must be nonzero')
    first={key:cross2(vector,jets[key])/radius2 for key in ['s','theta']}
    result=dict(first)
    for key,i,j in [('ss','s','s'),('st','s','theta'),('tt','theta','theta')]:
        result[key]=(cross2(vector,jets[key])-first[i]*dot(vector,jets[j])-
                     first[j]*dot(vector,jets[i]))/radius2
    return result


def scalar_frame_two_jets(core,s,theta,beta_primitive=None,side=1):
    """Return scalar fields and derivatives in the OUTWARD radial variable.

    The physical input s is unchanged. For side sigma, the outward variable
    t satisfies ds/dt=sigma, and the target V is sigma*B. Dictionary fields
    's','ss','st' below mean t,t^2,t-theta derivatives in this convention;
    all theta derivatives keep the same material theta, not construction phi.
    """
    if side not in [-1,1]:raise ValueError('side must be +1 or -1')
    if beta_primitive is None:beta_primitive=BetaLiftPrimitive(core)
    if beta_primitive.identity_sha256!=core.identity_sha256:
        raise ValueError('beta primitive and core use different physical identities')
    frame=material_frame_two_jets(core,s,theta)
    T=frame['T'];V=side*frame['B']
    tj={'s':side*frame['Ts'],'theta':frame['Ttheta'],'ss':frame['Tss'],
        'st':side*frame['Tst'],'tt':frame['Ttt']}
    vj={'s':frame['Bs'],'theta':side*frame['Btheta'],'ss':side*frame['Bss'],
        'st':frame['Bst'],'tt':side*frame['Btt']}
    H=T[...,:2];hj={key:value[...,:2] for key,value in tj.items()}
    h=np.linalg.norm(H,axis=-1)
    psi_jets=angle_two_jets(H,hj)

    phi=frame['phi'];theta_local=np.mod(frame['theta'],2*np.pi)
    radius=1+core.a*np.cos(3*phi)+core.b*np.cos(6*phi)
    radius_p=-3*core.a*np.sin(3*phi)-6*core.b*np.sin(6*phi)
    if np.any(radius<=0):raise ValueError('positive radial graph is required for this exact psi branch')
    psi=phi-np.arctan(radius_p/radius)
    u=dict(value=psi-theta_local,**psi_jets)
    u['theta']=u['theta']-1

    hs={key:dot(H,hj[key])/h for key in ['s','theta']}
    hss={key:(dot(hj[i],hj[j])+dot(H,hj[key])-hs[i]*hs[j])/h
         for key,i,j in [('ss','s','s'),('st','s','theta'),('tt','theta','theta')]}
    slope=T[...,2]/h
    slope_first={key:(tj[key][...,2]-slope*hs[key])/h for key in ['s','theta']}
    slope_jets=dict(value=slope,**slope_first)
    for key,i,j in [('ss','s','s'),('st','s','theta'),('tt','theta','theta')]:
        slope_jets[key]=(tj[key][...,2]-slope*hss[key]-slope_first[i]*hs[j]-
                         slope_first[j]*hs[i])/h

    zero=np.zeros_like(psi)
    N0=np.stack((np.cos(psi),np.sin(psi),zero),axis=-1)
    horizontal_tangent=np.stack((-np.sin(psi),np.cos(psi),zero),axis=-1)
    nj={key:scale(psi_jets[key],horizontal_tangent) for key in ['s','theta']}
    for key,i,j in [('ss','s','s'),('st','s','theta'),('tt','theta','theta')]:
        nj[key]=scale(psi_jets[key],horizontal_tangent)-scale(psi_jets[i]*psi_jets[j],N0)
    M0=np.cross(T,N0)
    mj={key:np.cross(tj[key],N0)+np.cross(T,nj[key]) for key in ['s','theta']}
    for key,i,j in [('ss','s','s'),('st','s','theta'),('tt','theta','theta')]:
        mj[key]=(np.cross(tj[key],N0)+np.cross(tj[i],nj[j])+
                 np.cross(tj[j],nj[i])+np.cross(T,nj[key]))
    circle=np.stack((dot(V,N0),dot(V,M0)),axis=-1)
    circle_jets={}
    for key in ['s','theta']:
        circle_jets[key]=np.stack((dot(vj[key],N0)+dot(V,nj[key]),
                                  dot(vj[key],M0)+dot(V,mj[key])),axis=-1)
    for key,i,j in [('ss','s','s'),('st','s','theta'),('tt','theta','theta')]:
        circle_jets[key]=np.stack((dot(vj[key],N0)+dot(vj[i],nj[j])+dot(vj[j],nj[i])+dot(V,nj[key]),
                                  dot(vj[key],M0)+dot(vj[i],mj[j])+dot(vj[j],mj[i])+dot(V,mj[key])),axis=-1)
    beta=dict(value=beta_primitive.value(phi)+(np.pi if side<0 else 0),
              **angle_two_jets(circle,circle_jets))
    roundtrip=np.stack((np.cos(beta['value']),np.sin(beta['value'])),axis=-1)
    error=float(np.max(np.linalg.norm(roundtrip-circle/np.linalg.norm(circle,axis=-1)[...,None],axis=-1),initial=0.))
    return {'u':u,'v':slope_jets,'beta':beta,'physical_s':frame['s'],'material_theta':frame['theta'],
        'construction_phi':phi,'outward_side':side,'target_T':T,'target_V':V,
        'frame_jets':{'T':tj,'V':vj},
        'frozen_physical_identity':core.identity,'frozen_physical_identity_sha256':core.identity_sha256,
        'a0_numerical':core.a0,'material_equation_residual_max':frame['material_equation_residual_max'],
        'beta_lift_phase_roundtrip_error_max':error,
        'beta_lift_definition':'beta0 + exact integral of (L Qphi - Q Lphi)/(L^2+Q^2); periodic even branch',
        'beta_lift_initial_value_numerical':beta_primitive.beta0,
        'beta_lift_period_numerical':beta_primitive.period,
        'beta_quadrature_half_sector_cells':beta_primitive.cells,
        'beta_quadrature_order':beta_primitive.quadrature,
        'arclength_quadrature_cells':core.arc_cells,'arclength_quadrature_order':core.quadrature,
        'global_J_certificate_available':core.global_J_certificate_available,
        'beta_lift_requires_global_nonzero_curvature':True,
        'finite_quadrature_error_is_not_continuously_certified':True,
        'physical_core_extrapolated':False,'new_geometry_optimized':False}


def relative_error(actual,reference):
    return float(np.max(abs(np.asarray(actual)-np.asarray(reference)),initial=0.)/
                 max(1.,float(np.max(abs(np.asarray(reference)),initial=0.))))


def developer_check():
    def fixture(a,b,heights,width):
        return {'height_basis':'cosine','a':a,'b':b,'half_width':width,
                'height_coefficients':heights,'height_offset':'1/11'}
    circle=CosineRectifyingCore(fixture('0','0',['0'],'1/10'),arc_cells=32,quadrature=8)
    beta_circle=BetaLiftPrimitive(circle,16,8)
    theta=np.array([.17,.51,1.03,1.57,2.31,3.23,5.73])
    circle_rows=[]
    for side in [1,-1]:
        fields=scalar_frame_two_jets(circle,side*.031,theta,beta_circle,side)
        error=max(max(relative_error(v,0) for key,v in fields[name].items()) for name in ['u','v'])
        error=max(error,max(relative_error(v,0) for key,v in fields['beta'].items() if key!='value'))
        error=max(error,relative_error(fields['beta']['value'],side*(-np.pi/2)))
        circle_rows.append({'side':side,'scalar_jet_error':error})
    core=CosineRectifyingCore(fixture('1/20','1/200',['1/25','-1/100','1/1000'],'1/100'),
                             arc_cells=64,quadrature=16)
    beta=BetaLiftPrimitive(core,32,16)
    s=.0017;h=2e-6
    checks=[]
    for side in [1,-1]:
        center=scalar_frame_two_jets(core,side*s,theta,beta,side)
        sp=scalar_frame_two_jets(core,side*(s+h),theta,beta,side)
        sm=scalar_frame_two_jets(core,side*(s-h),theta,beta,side)
        tp=scalar_frame_two_jets(core,side*s,theta+h,beta,side)
        tm=scalar_frame_two_jets(core,side*s,theta-h,beta,side)
        errors={}
        for field in ['u','v','beta']:
            f=center[field]
            errors[field+'_s']=relative_error(f['s'],(sp[field]['value']-sm[field]['value'])/(2*h))
            errors[field+'_theta']=relative_error(f['theta'],(tp[field]['value']-tm[field]['value'])/(2*h))
            errors[field+'_ss']=relative_error(f['ss'],(sp[field]['s']-sm[field]['s'])/(2*h))
            errors[field+'_st_radial']=relative_error(f['st'],(sp[field]['theta']-sm[field]['theta'])/(2*h))
            errors[field+'_st_angle']=relative_error(f['st'],(tp[field]['s']-tm[field]['s'])/(2*h))
            errors[field+'_tt']=relative_error(f['tt'],(tp[field]['theta']-tm[field]['theta'])/(2*h))
        psi=theta+center['u']['value'];slope=center['v']['value'];beta_value=center['beta']['value']
        T=np.stack((-np.sin(psi),np.cos(psi),slope),axis=-1)/np.sqrt(1+slope*slope)[...,None]
        N0=np.stack((np.cos(psi),np.sin(psi),np.zeros_like(psi)),axis=-1);M0=np.cross(T,N0)
        V=scale(np.cos(beta_value),N0)+scale(np.sin(beta_value),M0)
        errors['T_value_reconstruction']=relative_error(T,center['target_T'])
        errors['V_value_reconstruction']=relative_error(V,center['target_V'])
        # Direct scalar form of the three R28 integrability equations, with a'=0.
        alpha=np.arctan(slope);alpha_s=center['v']['s']/(1+slope*slope)
        alpha_t=center['v']['theta']/(1+slope*slope)
        cp,spb=np.cos(beta_value),np.sin(beta_value);ca,sa=np.cos(alpha),np.sin(alpha)
        psi_s=center['u']['s'];psi_t=1+center['u']['theta']
        rT=cp*ca*psi_t+spb*alpha_t
        rV=core.a0*(cp*ca*psi_s+spb*alpha_s)
        rW=center['beta']['theta']+sa*psi_t-core.a0*(spb*ca*psi_s-cp*alpha_s)
        errors['exact_core_integrability_residual']=float(max(np.max(abs(rT)),np.max(abs(rV)),np.max(abs(rW))))
        checks.append({'side':side,'errors':errors,'material_equation_residual_max':center['material_equation_residual_max'],
                       'beta_phase_roundtrip_error_max':center['beta_lift_phase_roundtrip_error_max']})
    phi=np.array([.01,.23,.47,.81,1.013])
    periodic=relative_error(beta.value(phi+2*np.pi/3),beta.value(phi))
    even=relative_error(beta.value(-phi),beta.value(phi))
    boundary_checks=[]
    for side in [1,-1]:
        boundary=scalar_frame_two_jets(core,side*core.width,theta,beta,side)
        position=core.evaluate(side*core.width,theta)
        errors={'X_t':relative_error(boundary['target_V'],side*position['Xs']),
                'X_theta':relative_error(core.a0*boundary['target_T'],position['Xtheta']),
                'X_tt_outward':relative_error(boundary['frame_jets']['V']['s'],position['Xss']),
                'X_ttheta':relative_error(boundary['frame_jets']['V']['theta'],side*position['Xst']),
                'X_thetatheta':relative_error(core.a0*boundary['frame_jets']['T']['theta'],position['Xtt'])}
        boundary_checks.append({'side':side,'physical_s':side*core.width,'position_two_jet_errors':errors})
    passed=all(row['scalar_jet_error']<1e-12 for row in circle_rows)
    passed=passed and all(max(row['errors'].values())<2e-5 for row in checks)
    passed=passed and all(max(row['position_two_jet_errors'].values())<1e-12 for row in boundary_checks)
    passed=passed and periodic<1e-12 and even<1e-12
    return {'schema':'cosine-scalar-frame-port-development-v1','artificial_inputs_only':True,
        'research_geometry_evaluated':False,'optimization_performed':False,'circle':circle_rows,
        'checks':checks,'actual_two_boundary_ports':boundary_checks,
        'beta_periodicity_error':periodic,'beta_evenness_error':even,'passed':bool(passed)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-only',action='store_true',required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();result=developer_check()
    result['source_files_sha256']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ['cosine_scalar_frame_port.py','cosine_core_high_jets.py','cosine_rectifying_core.py']}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()

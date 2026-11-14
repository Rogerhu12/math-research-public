#!/usr/bin/env python3
"""Exactly closed psi-warped R44 saddle cores, with fixed-input geometry audits.

All parameter scans belong in the public repository's GitHub Actions. The local
--smoke-only path checks algebra and port differentiation at one artificial input.
No connector or closed surface is produced by this module.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np

from folded_reference_geometry import I, PI, DOWN, UP, sincos
from star_core_geometry import square, clipped, magnitude_lower


def closure_parameters(warp_v):
    aa=.5-1.5*warp_v
    eta=-2*aa/(3+np.sqrt(9-4*aa+4*aa*aa))
    return eta,np.sqrt(1-eta*eta)


def interval_parameters(warp_u,warp_v,scale):
    u,v,b=I(warp_u),I(warp_v),I(scale)
    if b.lo<=0 or not all(x.lo.is_finite() and x.hi.is_finite() for x in (u,v,b)):
        raise ValueError('Need finite warp parameters and positive scale')
    aa=I('.5')-I('1.5')*v
    eta=-2*aa/(3+(9-4*aa+4*square(aa)).sqrt())
    sigma=(1-square(eta)).sqrt()
    return u,v,b,eta,sigma


def vnorm(vector):
    total=sum((square(x) for x in vector),I(0))
    return I(max(D(0),total.lo),total.hi).sqrt()


def vcross(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]


def vdot(a,b):
    return sum((x*y for x,y in zip(a,b)),I(0))


def interval_direction_frame(theta,parameters,space=False):
    """All derivatives in the rotating (e_r(psi),e_theta(psi),e_z) frame."""
    u,v,b,eta,sigma=parameters
    # theta remains inside [0,2*pi]; the trig provider includes outward errors.
    s,c=sincos(3*theta-2*PI*int(float((3*(theta.lo+theta.hi)/2)/(2*PI.hi))))
    s,c=clipped(s),clipped(c)
    s2,c2=clipped(2*s*c),clipped(2*square(c)-1)
    pp=1+3*u*c+6*v*c2
    p1=-9*u*s-36*v*s2
    p2=-27*u*c-216*v*c2
    d0=[-s,eta*c,-sigma*c]
    d1=[-(3+eta*pp)*c,-(3*eta+pp)*s,3*sigma*s]
    d2=[-eta*p1*c+(9+6*eta*pp+square(pp))*s,
        -p1*s-(9*eta+6*pp+eta*square(pp))*c,9*sigma*c]
    d3=[(27+27*eta*pp+9*square(pp)+eta*pp**3-eta*p2)*c+3*(3*eta+pp)*p1*s,
        (27*eta+27*pp+9*eta*square(pp)+pp**3-p2)*s-3*(3+eta*pp)*p1*c,
        -27*sigma*s]
    speed=vnorm(d1)
    out={'d':[d0,d1,d2,d3],'speed':speed,'sin_chi':s,'cos_chi':c,
         'p':pp,'p1':p1,'p2':p2}
    if space:
        psi=theta+u*s+v*s2
        sp,cp=sincos(psi)
        cr=-sigma*pp*s*c
        ct=sigma*(3+eta*pp*square(c))
        cz=3*eta+pp*(square(s)+square(eta)*square(c))
        out['center_derivative']=[b*(cr*cp-ct*sp),b*(cr*sp+ct*cp),b*cz]
    return out


def interval_center_z(theta,parameters):
    u,v,b,eta,sigma=parameters
    reduced=3*theta-2*PI*int(float((3*(theta.lo+theta.hi)/2)/(2*PI.hi)))
    s,c=sincos(reduced)
    s,c=clipped(s),clipped(c)
    s2=clipped(2*s*c)
    s3=clipped(3*s-4*s**3)
    s4=clipped(2*s2*(2*square(c)-1))
    return b*(u*(1+3*square(eta))*s/4+
              (-square(sigma)/12+v*(1+square(eta))/2)*s2
              -u*square(sigma)*s3/12-v*square(sigma)*s4/8)


class WarpedRuledCore:
    def __init__(self,warp_u,warp_v=0.,scale=1.,arc_cells=192,quadrature=16):
        self.warp_u,self.warp_v,self.scale=map(float,(warp_u,warp_v,scale))
        if self.scale<=0 or arc_cells<6 or arc_cells%6:
            raise ValueError('Need positive scale and arc_cells a positive multiple of 6')
        self.eta,self.sigma=closure_parameters(self.warp_v)
        endpoint=3+self.eta*(1+6*self.warp_v+np.array([-3.,3.])*self.warp_u)
        if np.min(abs(endpoint))<1e-12:
            raise ValueError('The spherical direction curve is singular or numerically unresolved at a characteristic angle')
        self.arc_cells,self.quadrature=int(arc_cells),int(quadrature)
        self.gl,self.gw=np.polynomial.legendre.leggauss(quadrature)
        self.step=2*np.pi/arc_cells
        left=np.arange(arc_cells)*self.step
        grid=left[:,None]+self.step*(self.gl[None,:]+1)/2
        c1=self.center_derivatives(grid)[0]
        inc=self.step/2*np.einsum('ijk,j->ik',c1,self.gw)
        self.position_prefix=np.concatenate((np.zeros((1,3)),np.cumsum(inc,axis=0)))
        sector=self.position_prefix[arc_cells//3]
        candidate=(sector[0]+1j*sector[1])/(np.exp(2j*np.pi/3)-1)
        self.anchor=float(candidate.real)
        self.anchor_imaginary_error=float(abs(candidate.imag))
        self.center_derivative_closure=self.position_prefix[-1].copy()
        speed=np.linalg.norm(self.direction_jets(grid)[1],axis=-1)
        sinc=self.step/2*(speed@self.gw)
        self.arc_prefix=np.r_[0.,np.cumsum(sinc)]
        self.sphere_length=float(self.arc_prefix[-1])
        self.q=self.sphere_length/(2*np.pi)

    def direction_jets(self,phi):
        phi=np.asarray(phi,float)
        chi=3*phi;psi=phi+self.warp_u*np.sin(chi)+self.warp_v*np.sin(2*chi)
        s,c=np.sin(chi),np.cos(chi)
        pp=1+3*self.warp_u*c+6*self.warp_v*np.cos(2*chi)
        p1=-9*self.warp_u*s-36*self.warp_v*np.sin(2*chi)
        p2=-27*self.warp_u*c-216*self.warp_v*np.cos(2*chi)
        e=self.eta;sig=self.sigma
        values=[[-s,e*c,-sig*c],
                [-(3+e*pp)*c,-(3*e+pp)*s,3*sig*s],
                [-e*p1*c+(9+6*e*pp+pp*pp)*s,
                 -p1*s-(9*e+6*pp+e*pp*pp)*c,9*sig*c],
                [(27+27*e*pp+9*pp*pp+e*pp**3-e*p2)*c+3*(3*e+pp)*p1*s,
                 (27*e+27*pp+9*e*pp*pp+pp**3-p2)*s-3*(3+e*pp)*p1*c,-27*sig*s]]
        sp,cp=np.sin(psi),np.cos(psi)
        return [np.stack((rr*cp-tt*sp,rr*sp+tt*cp,zz),axis=-1) for rr,tt,zz in values]

    def center_derivatives(self,phi):
        d0,d1,d2,d3=self.direction_jets(phi)
        return [self.scale*np.cross(d0,d1),self.scale*np.cross(d0,d2),
                self.scale*(np.cross(d1,d2)+np.cross(d0,d3))]

    def vertical(self,phi,derivative=0):
        eta=self.eta;ss=self.sigma**2;u=self.warp_u;v=self.warp_v
        coefficients=np.array([u*(1+3*eta*eta)/4,-ss/12+v*(1+eta*eta)/2,-u*ss/12,-v*ss/8])
        phi=np.asarray(phi)
        return self.scale*sum(a*k**derivative*np.sin(k*phi+derivative*np.pi/2)
                              for a,k in zip(coefficients,[3,6,9,12]))

    def _cell_data(self,phi):
        phi=np.asarray(phi,float)
        turns=np.floor(phi/(2*np.pi))
        rem=phi-turns*2*np.pi
        index=np.minimum(np.floor(rem/self.step).astype(int),self.arc_cells-1)
        left=index*self.step;length=rem-left
        grid=left[...,None]+length[...,None]*(self.gl+1)/2
        return turns,index,length,grid

    def center(self,phi):
        _,index,length,grid=self._cell_data(phi)
        value=self.position_prefix[index]+length[...,None]/2*np.einsum('...jk,j->...k',self.center_derivatives(grid)[0],self.gw)
        value=value+np.array([self.anchor,0.,0.])
        value[...,2]=self.vertical(phi)
        return value

    def center_jets(self,phi):
        return [self.center(phi),*self.center_derivatives(phi)]

    def arclength(self,phi):
        turns,index,length,grid=self._cell_data(phi)
        speed=np.linalg.norm(self.direction_jets(grid)[1],axis=-1)
        return turns*self.sphere_length+self.arc_prefix[index]+length*(speed@self.gw)/2

    def phase(self,theta):
        theta=np.asarray(theta,float)
        turns=np.floor(theta/(2*np.pi))
        target=self.q*(theta-turns*2*np.pi)
        lo=np.zeros_like(target);hi=np.full_like(target,2*np.pi)
        phi=theta-turns*2*np.pi
        for _ in range(50):
            d=self.direction_jets(phi)
            speed=np.linalg.norm(d[1],axis=-1)
            residual=self.arclength(phi)-target
            active=abs(residual)>=3e-14
            if not np.any(active):
                break
            lo=np.where(residual<0,phi,lo);hi=np.where(residual>=0,phi,hi)
            candidate=phi-residual/speed
            update=np.where((candidate>lo)&(candidate<hi),candidate,(lo+hi)/2)
            phi=np.where(active,update,phi)
        error=float(np.max(abs(self.arclength(phi)-target)))
        if error>3e-11:
            raise RuntimeError('Material-angle inverse did not converge')
        d=self.direction_jets(phi)
        speed=np.linalg.norm(d[1],axis=-1)
        speed_prime=np.sum(d[1]*d[2],axis=-1)/speed
        return phi+turns*2*np.pi,self.q/speed,-self.q*self.q*speed_prime/speed**3,error

    def inlet(self,theta,s,derivative=0):
        phi,fp,fpp,error=self.phase(theta)
        cc=self.center_jets(phi);dd=self.direction_jets(phi)
        c=[cc[0],cc[1]*fp[...,None],cc[2]*fp[...,None]**2+cc[1]*fpp[...,None]]
        d=[dd[0],dd[1]*fp[...,None],dd[2]*fp[...,None]**2+dd[1]*fpp[...,None]]
        return np.stack((c[derivative]+s*d[derivative],d[derivative],np.zeros_like(d[derivative])))

    def metric(self,s):
        ss=np.asarray(s)
        rr=np.sqrt(self.scale**2+ss*ss)
        return self.q*rr,self.q*ss/rr,self.q*self.scale**2/rr**3


def certified_centerline(u_text,v_text,scale_text,nodes):
    """Directed center vertices and derivative bounds for projection consumers.

    Return API: vertices (N,3 float array), vertex_boxes (N lists of three I),
    vertex_error (Decimal Euclidean bound), position_cells / derivative_cells
    (same I format), second_derivative_upper (Decimal), and report (JSON-safe).
    The exact model uses decimal input strings, not their binary64 approximants.
    """
    if nodes<12 or nodes%6:
        raise ValueError('Continuous cells must be a multiple of 6, at least 12')
    params=interval_parameters(u_text,v_text,scale_text)
    u,v,b,eta,sigma=params
    if (2*PI+I(u.abs_upper())+I(v.abs_upper())).hi>=12:
        raise ValueError('This trig implementation requires 2*pi+|u|+|v| < 12')
    endpoint=[3+eta*(1+6*v+sign*3*u) for sign in (-1,1)]
    algebraic_regular=all(magnitude_lower(value)>0 for value in endpoint)
    step=2*PI/nodes
    frames=[];derivatives=[];midpoint_derivatives=[];midpoint_speeds=[]
    kmin=None;kmax=D(0);kappa_upper=D(0);kappa_peak_lower=D(0)
    c2max=D(0);c3max=D(0);sphere2max=D(0);sphere3max=D(0);unresolved=0
    height=D(0)
    for j in range(nodes):
        angle=I((2*PI*j/nodes).lo,(2*PI*(j+1)/nodes).hi)
        middle=PI*(2*j+1)/nodes
        value=interval_direction_frame(angle,params,True)
        mid=interval_direction_frame(middle,params,True)
        dd=value['d'];speed=value['speed']
        frames.append(value);derivatives.append(value['center_derivative'])
        midpoint_derivatives.append(mid['center_derivative'])
        midpoint_speeds.append(mid['speed'])
        kmin=speed.lo if kmin is None else min(kmin,speed.lo)
        kmax=max(kmax,speed.hi)
        if speed.lo<=0:
            unresolved+=1
        else:
            curvature=vdot(dd[0],vcross(dd[1],dd[2]))/(speed**3)
            kappa_upper=max(kappa_upper,curvature.abs_upper())
            kappa_peak_lower=max(kappa_peak_lower,magnitude_lower(curvature))
        c2=[b*x for x in vcross(dd[0],dd[2])]
        cross12,cross03=vcross(dd[1],dd[2]),vcross(dd[0],dd[3])
        c3=[b*(x+y) for x,y in zip(cross12,cross03)]
        c2max=max(c2max,vnorm(c2).hi);c3max=max(c3max,vnorm(c3).hi)
        sphere2max=max(sphere2max,vnorm(dd[2]).hi);sphere3max=max(sphere3max,vnorm(dd[3]).hi)
        height=max(height,interval_center_z(angle,params).abs_upper())
    integral_error=(I(c3max)*step**3/24).hi
    increments=[[step*x+I(-integral_error,integral_error) for x in mid[:2]] for mid in midpoint_derivatives]
    prefix=[[I(0),I(0)]]
    for row in increments:
        prefix.append([x+y for x,y in zip(prefix[-1],row)])
    sector=prefix[nodes//3]
    anchor=-sector[0]/2+I(3).sqrt()*sector[1]/6
    boxes=[];vertices=[];vertex_error=D(0)
    for j in range(nodes):
        x,y=anchor+prefix[j][0],prefix[j][1]
        z=interval_center_z(2*PI*j/nodes,params)
        xyz=np.array([float((t.lo+t.hi)/2) for t in (x,y,z)])
        error=vnorm([t-I(D.from_float(float(f))) for t,f in zip((x,y,z),xyz)]).hi
        vertex_error=max(vertex_error,error)
        vertices.append(xyz);boxes.append([x,y,z])
    chord_error=(I(c2max)*square(step)/8).hi
    position_cells=[]
    for j in range(nodes):
        nxt=(j+1)%nodes
        position_cells.append([I(DOWN.subtract(min(a.lo,c.lo),chord_error),
                                 UP.add(max(a.hi,c.hi),chord_error))
                               for a,c in zip(boxes[j],boxes[nxt])])
    sigma_length=None
    if unresolved==0:
        ksecond=(I(sphere2max)**2+I(kmax)*I(sphere3max))/I(kmin)+I(kmax)**2*I(sphere2max)**2/I(kmin)**3
        ke=(ksecond*step**3/24).hi
        sigma_length=sum((step*x+I(-ke,ke) for x in midpoint_speeds),I(0))
    principal=(I(kappa_upper)+(square(I(kappa_upper))+4).sqrt())/(2*b) if unresolved==0 else None
    principal_lower=(I(kappa_peak_lower)+(square(I(kappa_peak_lower))+4).sqrt())/(2*b) if unresolved==0 else None
    report={'exact_decimal_parameters':{'warp_u':u_text,'warp_v':v_text,'scale':scale_text},
            'eta':eta.json(),'sigma':sigma.json(),'regularity_endpoint_factors':[e.json() for e in endpoint],
            'continuous_direction_regular_by_endpoint_formula':algebraic_regular,
            'direction_speed_lower':str(kmin),'direction_speed_upper':str(kmax),'unresolved_speed_cells':unresolved,
            'sphere_geodesic_curvature_absolute_upper':str(kappa_upper) if unresolved==0 else None,
            'core_principal_curvature_upper':str(principal.hi) if principal else None,
            'core_max_principal_curvature_lower':str(principal_lower.lo) if principal_lower else None,
            'center_second_derivative_upper':str(c2max),'center_third_derivative_upper':str(c3max),
            'center_absolute_height_upper':str(height),'center_anchor_x':anchor.json(),
            'center_vertex_error_upper':str(vertex_error),'center_chord_error_upper':str(chord_error),
            'midpoint_integral_error_per_component_per_cell':str(integral_error),
            'spherical_length':sigma_length.json() if sigma_length else None,
            'nodes':nodes,'decimal_precision':50,
            'exact_center_closure_from_formula':True,'central_projection_embedded_certified':False,
            'core_embedding_certified':False,'whole_surface_reach_certified':False}
    return {'vertices':np.array(vertices),'vertex_boxes':boxes,'vertex_error':vertex_error,
            'position_cells':position_cells,'derivative_cells':derivatives,
            'second_derivative_upper':c2max,'report':report}


def sampled_geometry(core,width,angles=384):
    phi=np.arange(angles)*2*np.pi/angles
    cc=core.center(phi);d=core.direction_jets(phi)
    speed=np.linalg.norm(d[1],axis=-1)
    kg=np.sum(d[0]*np.cross(d[1],d[2]),axis=-1)/speed**3
    points=[];normals=[]
    for ss in (-width,0.,width):
        derivative=core.center_derivatives(phi)[0]+ss*d[1]
        a=np.sqrt(core.scale**2+ss*ss)*speed
        points.append(cc+ss*d[0]);normals.append(np.cross(d[0],derivative)/a[:,None])
    points=np.concatenate(points);normal=np.concatenate(normals)
    diameter=0.;normal_chord=np.inf
    for start in range(0,len(points),128):
        delta=points[None,:,:]-points[start:start+128,None,:]
        distance2=np.sum(delta*delta,axis=-1)
        denominator=2*np.abs(np.sum(delta*normal[start:start+128,None,:],axis=-1))
        ratio=np.divide(distance2,denominator,out=np.full_like(distance2,np.inf),
                        where=(distance2>1e-20)&(denominator>1e-18))
        normal_chord=min(normal_chord,float(np.min(ratio)))
        diameter=max(diameter,float(np.sqrt(np.max(distance2))))
    return {'angles':angles,'half_width':width,'q_numeric':core.q,
            'center_derivative_closure_numeric':core.center_derivative_closure.tolist(),
            'anchor_imaginary_numeric_error':core.anchor_imaginary_error,
            'center_coordinate_min':cc.min(axis=0).tolist(),'center_coordinate_max':cc.max(axis=0).tolist(),
            'core_diameter_sample':diameter,'normal_chord_radius_sample':normal_chord,
            'core_max_principal_curvature_sample':float(np.max((abs(kg)+np.sqrt(kg*kg+4))/(2*core.scale))),
            'samples_are_not_continuous_certificates':True}


def smoke_check():
    # Artificial nonzero u,v, no candidate selection or scan.
    core=WarpedRuledCore(.13,.02,1.,arc_cells=48,quadrature=12)
    phi=(np.arange(17)+.27)*2*np.pi/17
    dd=core.direction_jets(phi)
    theta=(np.arange(11)+.31)*2*np.pi/11
    eps=2e-5
    derivative_errors=[]
    for order in (0,1,2):
        fd=(core.direction_jets(phi-2*eps)[order]-8*core.direction_jets(phi-eps)[order]
            +8*core.direction_jets(phi+eps)[order]-core.direction_jets(phi+2*eps)[order])/(12*eps)
        derivative_errors.append(float(np.linalg.norm(fd-dd[order+1])/np.linalg.norm(dd[order+1])))
    cc=core.center_jets(phi)
    vertical_error=float(np.max(abs(cc[1][:,2]-core.vertical(phi,1))))
    cfd=(core.center(phi+eps)-core.center(phi-eps))/(2*eps)
    center_derivative_error=float(np.linalg.norm(cfd-cc[1])/np.linalg.norm(cc[1]))
    jets=[core.inlet(theta,.01,d) for d in range(3)]
    aa=core.metric(.01)[0]
    metric=max(float(np.max(abs(np.sum(jets[0][1]**2,axis=-1)-1))),
               float(np.max(abs(np.sum(jets[0][1]*jets[1][0],axis=-1)/aa))),
               float(np.max(abs(np.sum(jets[1][0]**2,axis=-1)/aa**2-1))))
    A=np.array([1.,-1.,-1.]);symmetry=0.
    for rd in range(3):
        for td in range(3-rd):
            lhs=core.inlet(-theta,0.,td)[rd]
            rhs=(-1)**(rd+td)*core.inlet(theta,0.,td)[rd]*A
            symmetry=max(symmetry,float(np.max(abs(lhs-rhs))))
    from ruled_core_geometry import RuledCore
    old=RuledCore(1.,np.pi/2);new=WarpedRuledCore(0.,0.,1.,48,12)
    baseline=max(float(np.max(abs(old.inlet(theta,.01,d)-new.inlet(theta,.01,d)))) for d in range(3))
    # One deliberately coarse artificial-input enclosure checks the API. These
    # floating evaluations only test implementation consistency, not rigor.
    certificate=certified_centerline('.13','.02','1',24)
    values=core.center(np.arange(24)*2*np.pi/24)
    box_miss=max(max(float(box[k].lo)-values[j,k],values[j,k]-float(box[k].hi))
                 for j,box in enumerate(certificate['vertex_boxes']) for k in range(3))
    result={'smoke_only':True,'research_scan_performed':False,
            'artificial_parameters':{'warp_u':.13,'warp_v':.02},
            'unit_norm_error':float(np.max(abs(np.sum(dd[0]**2,axis=-1)-1))),
            'direction_derivative_relative_errors':derivative_errors,
            'vertical_primitive_derivative_error':vertical_error,
            'center_derivative_relative_error':center_derivative_error,
            'metric_error':metric,'R6_complete_central_second_jet_error':symmetry,
            'zero_warp_matches_R44_all_port_jets_error':baseline,
            'center_closure_numeric':core.center_derivative_closure.tolist(),
            'interval_api_artificial_nodes':24,
            'interval_api_shape':list(certificate['vertices'].shape),
            'interval_vs_numeric_vertex_max_box_miss':float(box_miss),
            'interval_api_regularity_endpoint_formula':certificate['report']['continuous_direction_regular_by_endpoint_formula']}
    result['passed']=bool(max(derivative_errors)<1e-8 and vertical_error<1e-11 and
                          center_derivative_error<1e-7 and metric<1e-10 and symmetry<1e-9 and baseline<1e-9
                          and box_miss<2e-12)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--warp-u',default='.6,.8,1,1.2')
    parser.add_argument('--warp-v',default='0')
    parser.add_argument('--scale',default='1')
    parser.add_argument('--half-width',default='.05')
    parser.add_argument('--nodes',type=int,default=1536)
    parser.add_argument('--sample-angles',type=int,default=384)
    parser.add_argument('--smoke-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if float(args.half_width)<0:
        parser.error('--half-width must be nonnegative')
    if args.smoke_only:
        report=smoke_check()
    else:
        if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
            parser.error('Run geometry scans in this public repository GitHub Actions')
        dependencies=['warped_ruled_core.py','folded_reference_geometry.py','star_core_geometry.py',
                      'warped_ruled_projection.py']
        report={'schema':'warped-ruled-core-geometry-v1','task_complete':False,
                'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'dependency_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                     for name in dependencies if Path(__file__).with_name(name).exists()},
                'github_repository':os.environ.get('GITHUB_REPOSITORY'),
                'github_sha':os.environ.get('GITHUB_SHA'),
                'github_run_id':os.environ.get('GITHUB_RUN_ID'),'rows':[]}
        for u in args.warp_u.split(','):
            for v in args.warp_v.split(','):
                started=time.perf_counter()
                certificate=certified_centerline(u,v,args.scale,args.nodes)
                core=WarpedRuledCore(float(u),float(v),float(args.scale))
                row={'warp_u':u,'warp_v':v,'continuous':certificate['report'],
                     'sampled':sampled_geometry(core,float(args.half_width),args.sample_angles)}
                try:
                    from warped_ruled_projection import projection_audit
                    row['projection']=projection_audit(certificate,args.half_width)
                except ImportError:
                    row['projection']={'available':False,'filled_domain_witness_proved':False}
                row['elapsed_seconds']=time.perf_counter()-started
                report['rows'].append(row)
                args.out.parent.mkdir(parents=True,exist_ok=True)
                args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
                print(json.dumps(row),flush=True)
    report['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    if args.smoke_only:
        print(json.dumps(report),flush=True)
        if not report['passed']:
            raise SystemExit(1)


if __name__=='__main__':
    main()

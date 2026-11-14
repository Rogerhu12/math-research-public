#!/usr/bin/env python3
"""Floating non-circle-preserving tangential-gauge screen of an actual map.

This is NOT a repaired geometry or a continuous metric certificate. It reads
the actual Cartesian common prefix, its OWN frozen target, and optionally
its OWN integrated tail/collar and background packet. It samples metric
errors in physical angular coordinates and integrates the linear equations

 p_s=-B_ss/2,
 q_s=-(a*B_su+p_u)/a^2,
 corrected_B_uu=B_uu+2*a_s*p/a+2*q_u.

Here g=ds^2+a(s)^2 du^2, and the infinitesimal material displacement is
p*d_s+q*d_u. The radial component p depends on u: R109's circle-preserving
obstruction does not apply. The floating screen retains the remaining G
residual and the cuff boundary drift. No field is claimed to be C2, no
inverse map is constructed, and no holding/closed-surface condition is
inferred. No nonlinear solver or ODE shooting is called.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy import fft
from scipy.interpolate import CubicSpline

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
LD=np.longdouble
CD=np.clongdouble


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj


diff=module('fd2d_noncircle_difference',HERE/'fd2d-metric-prefix-c2-difference.py')
r105=module('fd2d_noncircle_r105',HERE/'78718-geometry-arclength-residual-screen.py')


def identity(path):return diff.identity(path)


def load_npz(path,expected):
    payload=Path(path).read_bytes()
    if hashlib.sha256(payload).hexdigest()!=expected:raise ValueError('Data hash mismatch')
    if payload[:2]==b'\x1f\x8b':payload=gzip.decompress(payload)
    with np.load(io.BytesIO(payload),allow_pickle=False) as raw:
        return {k:raw[k].copy() for k in raw.files}


def horner(c,x):
    v=np.zeros(c.shape[1:],dtype=LD)
    for a in c[::-1]:v=v*x+a
    return v


def angular(values,order=1):
    n=values.shape[-1]
    k=fft.fftfreq(n,d=1/n)
    if n%2==0:k[n//2]=0
    return fft.ifft(fft.fft(values,axis=-1)*(3j*k)**order,axis=-1).real


def primitive(values):
    n=len(values);k=fft.fftfreq(n,d=1/n)
    spectrum=fft.fft(values);spectrum[0]=0
    good=k!=0;spectrum[good]/=(3j*k[good])
    if n%2==0:spectrum[n//2]=0
    return fft.ifft(spectrum).real


def spectral_fields(coeff,modes,count):
    """R,T,Z and their full Cartesian psi derivatives in the moving frame."""
    c=np.zeros((3,count),dtype=CD)
    c[0,0]=coeff[0];c[2,0]=coeff[-1]
    for j in range(1,modes+1):
        c[0,j]=c[0,-j]=coeff[j]/2
        c[1,j]=-1j*coeff[modes+j]/2;c[1,-j]=1j*coeff[modes+j]/2
        c[2,j]=c[2,-j]=coeff[2*modes+j]/2
    k=fft.fftfreq(count,d=1/count).astype(LD)
    d=c*(3j*k)
    d[0]-=c[1];d[1]+=c[0]
    return fft.ifft(c,axis=-1,norm='forward').real,fft.ifft(d,axis=-1,norm='forward').real


class Prefix:
    def __init__(self,geometry,target,angular_count,psi_count):
        self.geometry_path=geometry;self.target_path=target
        self.geom,self.bindings=diff.load_geometry(geometry,'noncircle_reference')
        self.meta=json.loads(geometry.read_text())
        self.base_path=(r105.resolve(self.meta['base_geometry'],geometry.parent)
                        if self.meta.get('representation')=='exact-common-cut-prefix' else geometry)
        self.base_meta=json.loads(self.base_path.read_text())
        self.target=json.loads(target.read_text())
        if self.target['geometry_sha256']!=r105.sha(self.base_path):
            raise ValueError('Target is not the actual base map own frozen target')
        if self.target['frozen_profile']!=self.base_meta['frozen_profile']:
            raise ValueError('Frozen target profile changed')
        self.target_data=r105.resolve(self.target['data_file'],target.parent)
        self.raw=load_npz(self.target_data,self.target['data_sha256'])
        self.left=self.raw['left'];self.right=self.raw['right']
        if not (self.left[0]==self.geom.x[0] and self.right[-1]==self.geom.x[-1]
                and np.array_equal(self.right[:-1],self.left[1:])):
            raise ValueError('Own target does not partition the geometry')
        self.power=r105.midpoint(self.geom.power.lo,self.geom.power.hi)
        self.coefficient_radius=float(np.max((self.geom.power.hi.astype(LD)-self.geom.power.lo)/2))
        port_path=r105.resolve(self.base_meta['linear_port'],self.base_path.parent)
        if r105.sha(port_path)!=self.base_meta['port_sha256']:raise ValueError('Changed own port')
        supplier=module('fd2d_noncircle_supplier',HERE/'78718-prefix-metric-supplier-storage-v1.py')
        self.slope=r105.FrozenSlope(supplier,self.base_meta,self.target,json.loads(port_path.read_text()))
        self.n=angular_count;self.np=psi_count
        if psi_count<=4*self.geom.M or angular_count<16:raise ValueError('Insufficient angular grid')
        self.pi=LD(np.arccos(LD(-1)))
        self.psi=2*self.pi*np.arange(psi_count,dtype=LD)/(3*psi_count)
        self.u=np.asarray(2*self.pi*np.arange(angular_count,dtype=LD)/(3*angular_count),dtype=float)
        self.knots=np.unique(np.r_[self.geom.x,self.left,self.right]).astype(LD)
        self.target_uncertainty={k:0. for k in ('a','e','ep')}

    def point(self,s):
        p=min(max(int(np.searchsorted(self.left,s,side='right')-1),0),len(self.left)-1)
        tau=(s-LD(self.left[p]))/(LD(self.right[p])-LD(self.left[p]))
        target,unc=r105.target_point(self.raw,p,tau)
        for k in unc:self.target_uncertainty[k]=max(self.target_uncertainty[k],unc[k])
        a,e,ep=(target[k] for k in ('a','e','ep'))
        span=min(max(int(np.searchsorted(self.geom.x,s,side='right')-1),0),len(self.geom.x)-2)
        width=LD(self.geom.x[span+1])-LD(self.geom.x[span]);t=(s-LD(self.geom.x[span]))/width
        value=horner(self.power[span],t)
        radial=horner(self.power[span,1:]*np.arange(1,6,dtype=LD)[:,None],t)/width
        _,xt=spectral_fields(value,self.geom.M,self.np)
        xs,_=spectral_fields(radial,self.geom.M,self.np)
        rho=1-e*np.cos(3*self.psi);nu=-ep*np.sin(3*self.psi)/3
        if np.min(rho)<=0 or a<=0:raise ValueError('Sampled chart is not positive')
        Dss=np.sum(xs*xs,axis=0)-(1+a*a*nu*nu)
        Dsp=np.sum(xs*xt,axis=0)-a*a*nu*rho
        N=np.sum(xt*xt,axis=0)-a*a*rho*rho
        b=nu/rho
        errors=np.stack((Dss-2*b*Dsp+b*b*N,(Dsp-b*N)/(a*rho),N/(a*a*rho*rho)),axis=-1)
        theta=self.psi-e*np.sin(3*self.psi)/3
        # Interpolate SMALL residuals, not two nearly equal order-one metrics.
        theta=np.r_[theta,2*self.pi/3].astype(float)
        values=np.vstack((errors,errors[0])).astype(float)
        sampled=CubicSpline(theta,values,axis=0,bc_type='periodic')(self.u).T
        return dict(s=LD(s),a=float(a),ap=float(self.slope(float(s))),errors=sampled,
                    region='prefix',coordinate=float(s),minimum_rho=float(np.min(rho)))


class Tail:
    def __init__(self,manifest,packet,count):
        from db6f_tail_integrated import IntegratedTail
        self.path=manifest;self.reader=IntegratedTail(manifest);self.meta=self.reader.meta
        self.packet_path=packet;self.packet=json.loads(packet.read_text())
        if self.packet['finite_tail_manifest_sha256']!=r105.sha(manifest):raise ValueError('Wrong tail background')
        self.data_path=r105.resolve(self.packet['data_file'],packet.parent)
        self.raw=load_npz(self.data_path,self.packet['data_sha256'])
        indices=self.raw['span_index'];self.first={};self.last={}
        for j,k in enumerate(indices):
            k=int(k);self.first.setdefault(k,j);self.last[k]=j+1
        n=len(self.reader.L)
        if set(self.first)!=set(range(-1,n)):raise ValueError('Packet misses some actual tail/collar span')
        self.count=count;self.cuff=LD(self.meta['parameters']['rCuff'])
        self.length=self.reader.r[0]-self.cuff
        a0=self.reader.source_values[0].astype(LD);a1=self.reader.first[0].astype(LD);a2=self.reader.second[0].astype(LD)
        c3=10*a0-4*self.length*a1+self.length*self.length*a2/2
        c4=-15*a0+7*self.length*a1-self.length*self.length*a2
        c5=6*a0-3*self.length*a1+self.length*self.length*a2/2
        zero=np.zeros_like(a0)
        self.collar=np.stack((zero,zero,zero,c3,c4,c5))
        self.maximum_w_uncertainty=0.

    def background(self,span,t):
        first,last=self.first[span],self.last[span]
        j=first+min(max(int(np.searchsorted(self.raw['u_left'][first:last],t,side='right')-1),0),last-first-1)
        left,right=LD(self.raw['u_left'][j]),LD(self.raw['u_right'][j]);z=(LD(t)-left)/(right-left)
        lo,hi=self.raw['w_lo'][j].astype(LD),self.raw['w_hi'][j].astype(LD)
        w=horner((lo+hi)/2,z)
        uncertainty=horner((hi-lo)/2,abs(z))+LD(self.raw['w_remainder'][j])
        self.maximum_w_uncertainty=max(self.maximum_w_uncertainty,float(uncertainty))
        return w

    def point(self,span,t):
        t=LD(t);tail=self.reader
        if span==-1:
            value=horner(self.collar,t)
            first=horner(self.collar[1:]*np.arange(1,6,dtype=LD)[:,None],t)/self.length
            r=self.cuff+self.length*t
        else:
            value,first,_=tail.span_coefficients(span,t)
            r=tail.r[span]+tail.L[span]*t
        w=self.background(span,t)
        cp=np.zeros(self.count,dtype=CD);dp=cp.copy();cp_theta=cp.copy();cz=cp.copy();dz=cp.copy();cz_theta=cp.copy()
        for j,m in enumerate(tail.planar_modes):
            k=(int(m)-1)//3
            if 2*abs(k)>=self.count:raise ValueError('Planar angular grid aliases')
            cp[k%self.count]+=value[j];dp[k%self.count]+=first[j]
            cp_theta[k%self.count]+=1j*int(m)*value[j]
        for j,m in enumerate(tail.height_modes):
            k=int(m)//3
            if 2*k>=self.count:raise ValueError('Height angular grid aliases')
            if k==0:cz[0]+=value[tail.P+j];dz[0]+=first[tail.P+j]
            else:
                z=value[tail.P+j]/2;d=first[tail.P+j]/2
                cz[k]+=z;cz[-k]+=z;dz[k]+=d;dz[-k]+=d
                cz_theta[k]+=1j*int(m)*z;cz_theta[-k]-=1j*int(m)*z
        dr=fft.ifft(dp,norm='forward');dt=fft.ifft(cp_theta,norm='forward')
        zr=fft.ifft(dz,norm='forward').real;zt=fft.ifft(cz_theta,norm='forward').real
        E0=1+w*w;root=np.sqrt(E0);k=-1/root
        de=2*dr.real+2*w*zr+abs(dr)**2+zr*zr
        df=dt.real+r*dr.imag+w*zt+(np.conj(dr)*dt).real+zr*zt
        dg=2*r*dt.imag+abs(dt)**2+zt*zt
        return dict(a=float(r),ap=float(k),zeta=LD(root),errors=np.array((de/E0,k*df/r,dg/(r*r)),dtype=float),
                    region='collar' if span==-1 else 'tail',coordinate=float(r),span=int(span),tau=float(t))


def weights(h1,h2,until):
    """Exact formula, approximately evaluated, for three-node integration."""
    x=LD(until);a=LD(h1);b=LD(h2)
    return np.asarray((x-(a+b)*x*x/(2*a*b)+x*x*x/(3*a*b),
        (x*x*x/3-b*x*x/2)/(a*(a-b)),
        (x*x*x/3-a*x*x/2)/(b*(b-a))),dtype=float)


class Gauge:
    def __init__(self,start,record_every):
        self.old=start;self.p=np.zeros(start['errors'].shape[1]);self.q=primitive(-start['errors'][2]/2)
        self.rows=[];self.count=0;self.record_every=record_every
        self.maxima={k:0. for k in ('original_operator','remaining_G','radial_displacement','angular_displacement',
                                  'p_u','q_u','p_s','q_s')};self.worst={}
        self.initial_G_mean=float(np.mean(start['errors'][2]));self.observe(start,self.p,self.q)

    def observe(self,point,p,q):
        err=point['errors'];pu=angular(p);qu=angular(q)
        residual=err[2]+2*point['ap']*p/point['a']+2*qu
        ps=-err[0]/2;qs=-err[1]/point['a']-pu/(point['a']**2)
        op=r105.symmetric_norm(*err)
        values=dict(original_operator=float(np.max(op)),remaining_G=float(np.max(abs(residual))),
            radial_displacement=float(np.max(abs(p))),angular_displacement=float(np.max(abs(q))),
            p_u=float(np.max(abs(pu))),q_u=float(np.max(abs(qu))),p_s=float(np.max(abs(ps))),q_s=float(np.max(abs(qs))))
        location={k:point[k] for k in ('region','coordinate','span','tau') if k in point};location['s']=float(point['s'])
        for name,value in values.items():
            if value>self.maxima[name]:self.maxima[name]=value;self.worst[name]=location.copy()
        row={**location,**values,'G_mean':float(np.mean(residual)),'p_mean':float(np.mean(p))}
        if self.count%self.record_every==0:self.rows.append(row)
        self.last_row=row;self.count+=1

    def advance(self,middle,end):
        old=self.old;h1=middle['s']-old['s'];h2=end['s']-old['s']
        if not 0<h1<h2:raise ValueError('Radial integration coordinates are not increasing')
        wm,we=weights(h1,h2,h1),weights(h1,h2,h2)
        e=np.array((old['errors'][0],middle['errors'][0],end['errors'][0]))
        pm=self.p-np.dot(wm,e)/2;pe=self.p-np.dot(we,e)/2
        points=(old,middle,end);ps=(self.p,pm,pe)
        qder=np.array([-pt['errors'][1]/pt['a']-angular(p)/(pt['a']**2) for pt,p in zip(points,ps)])
        qm=self.q+np.dot(wm,qder);qe=self.q+np.dot(we,qder)
        self.observe(middle,pm,qm);self.observe(end,pe,qe)
        self.p,self.q,self.old=pe,qe,end


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--geometry',type=Path,required=True);ap.add_argument('--target',type=Path,required=True)
    ap.add_argument('--tail',type=Path);ap.add_argument('--tail-packet',type=Path)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--angular',type=int,default=512)
    ap.add_argument('--psi-angular',type=int,default=2048);ap.add_argument('--record-every',type=int,default=64)
    ap.add_argument('--prefix-subdivide',type=int,default=1);ap.add_argument('--tail-subdivide',type=int,default=1)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Select a new output')
    if (args.tail is None)!=(args.tail_packet is None):raise ValueError('Provide both own tail and own packet')
    if min(args.prefix_subdivide,args.tail_subdivide,args.record_every)<1:raise ValueError('Positive subdivision/count required')
    started=time.monotonic();prefix=Prefix(args.geometry,args.target,args.angular,args.psi_angular)
    gauge=Gauge(prefix.point(prefix.knots[0]),args.record_every)
    print(json.dumps(dict(stage='prefix_start',spans=len(prefix.knots)-1,seconds=time.monotonic()-started)),flush=True)
    for j,(left,right) in enumerate(zip(prefix.knots[:-1],prefix.knots[1:])):
        for part in range(args.prefix_subdivide):
            a=left+(right-left)*LD(part)/args.prefix_subdivide
            b=left+(right-left)*LD(part+1)/args.prefix_subdivide
            gauge.advance(prefix.point((a+b)/2),prefix.point(b))
        if (j+1)%1000==0:print(json.dumps(dict(stage='prefix',spans=j+1,seconds=time.monotonic()-started,
            maxima=gauge.maxima)),flush=True)
    prefix_maxima=gauge.maxima.copy();prefix_boundary=gauge.last_row.copy()
    tail=None
    if args.tail:
        if prefix.meta.get('tail_manifest_sha256')!=r105.sha(args.tail):raise ValueError('Tail is not the common prefix own tail')
        tail=Tail(args.tail,args.tail_packet,args.angular)
        endpoint=tail.point(len(tail.reader.L)-1,1)
        jump=float(np.max(abs(endpoint['errors']-gauge.old['errors'])))
        endpoint['s']=gauge.old['s'];gauge.old=endpoint
        print(json.dumps(dict(stage='tail_start',spans=len(tail.reader.L),junction_error_sample_difference=jump,
                             seconds=time.monotonic()-started)),flush=True)
        for done,span in enumerate(range(len(tail.reader.L)-1,-2,-1)):
            length=tail.length if span==-1 else tail.reader.L[span]
            for part in range(args.tail_subdivide):
                t0=LD(1)-LD(part)/args.tail_subdivide;t2=LD(1)-LD(part+1)/args.tail_subdivide;t1=(t0+t2)/2
                a,b,c=tail.point(span,t0),tail.point(span,t1),tail.point(span,t2)
                z=np.asarray([a['zeta'],b['zeta'],c['zeta']],dtype=LD);step=length*(t0-t2)
                d1=step*(LD(5)*z[0]+LD(8)*z[1]-z[2])/24
                d2=step*(z[0]+4*z[1]+z[2])/6
                b['s']=gauge.old['s']+d1;c['s']=gauge.old['s']+d2
                gauge.advance(b,c)
            if (done+1)%2000==0:print(json.dumps(dict(stage='tail',spans=done+1,seconds=time.monotonic()-started,
                                                   maxima=gauge.maxima)),flush=True)
        boundary_jump=jump
    else:boundary_jump=None
    if gauge.rows[-1]!=gauge.last_row:gauge.rows.append(gauge.last_row)
    report=dict(schema='fd2d-noncircle-linear-gauge-floating-screen-v1',status='SCREEN_ONLY__NO_REPAIRED_MAP',
        scope=__doc__,script=identity(__file__),geometry=identity(args.geometry),target=identity(args.target),
        target_data=identity(prefix.target_data),definition_bindings=prefix.bindings,
        coordinate_producer=identity(HERE/'fd2d-metric-prefix-c2-difference.py'),
        angular_samples=args.angular,psi_samples_for_material_interpolation=args.psi_angular,
        prefix_subdivisions=args.prefix_subdivide,tail_subdivisions=args.tail_subdivide,
        integration='Streaming three-node quadratic interpolation quadrature; no remainder certificate',
        prefix_target='Own frozen analytic target, radial zeta=1; exact bridge transfer not applied',
        prefix_target_point_uncertainty_max=prefix.target_uncertainty,
        prefix_common_coefficient_enclosure_radius_max=prefix.coefficient_radius,
        exact_bridge_transfer_applied=False,prefix_maxima=prefix_maxima,prefix_boundary=prefix_boundary,
        total_samples=gauge.count,maxima=gauge.maxima,worst_locations=gauge.worst,
        initial_G_material_mean=gauge.initial_G_mean,boundary=gauge.last_row,
        boundary_radial_displacement_samples=gauge.p.tolist(),boundary_angular_displacement_samples=gauge.q.tolist(),
        prefix_tail_sample_error_jump=boundary_jump,tail_covered_in_screen=tail is not None,
        caps_covered=False,holding_condition_verified=False,field_C2_verified=False,inverse_map_constructed=False,
        nonlinear_pullback_metric_evaluated=False,continuous_certificate=False,metric_bound_certified=False,
        complete_closed_surface=False,solver_calls=0,ODE_shooting_calls=0,rows=gauge.rows,
        limitations=['Floating sampling, interpolation, Fourier-tail and radial quadrature errors are not certified.',
            'The first-order gauge can leave a large G residual or a nonzero cuff displacement.',
            'Exact common target, globally C2 material diffeomorphism, fixed-cap jets and nonlinear pullback require later work.',
            'No R21 geometry theorem is transferred to a new map by this screen.'],
        seconds=time.monotonic()-started)
    if tail:
        report.update(tail=identity(args.tail),tail_packet=identity(args.tail_packet),tail_packet_data=identity(tail.data_path),
                      tail_background_w_point_uncertainty_max=tail.maximum_w_uncertainty)
    payload=(json.dumps(report,indent=2,allow_nan=False)+'\n').encode()
    if args.out.suffix=='.gz':payload=gzip.compress(payload,mtime=0)
    if len(payload)>=5_000_000 or (len(payload)>1_000_000 and args.out.suffix!='.gz'):
        raise ValueError('Use gzip or fewer summary rows under repository size limit')
    args.out.write_bytes(payload)
    print(json.dumps(dict(out=str(args.out),maxima=gauge.maxima,boundary=gauge.last_row,
        continuous_certificate=False,seconds=report['seconds']),allow_nan=False),flush=True)


if __name__=='__main__':main()

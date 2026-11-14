#!/usr/bin/env python3
"""Saved prefix -> general-core chart, preserving physical position before projection.

Supports the task's old frozen-spline-adaptive-v1 and new
general-support-core-blend-v1 metadata. Outputs projected state and two radial
jets, plus BOTH the original height mean and the new angular-mean correction.
This is an initial-guess conversion, never a new solved trajectory.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


charts=module('geometric_pullback_general_chart',HERE/'geometric-general-core-chart.py')


def load_saved(path,source_topic,port_path,angular=512):
    loader=module('geometric_pullback_mode2_loader',HERE/'numerical-m2-prefix.py')
    # Loading JSON metadata alone is not sufficient: coefficient chunks are
    # part of the saved mathematical finite trajectory.
    with (gzip.open(path,'rt')if str(path).endswith('.gz')else open(path))as f:meta=json.load(f)
    mode=int(meta['config'].get('base_mode',2))
    if mode==2:
        adaptive=loader.load(source_topic)
    elif mode==3:
        source_root=source_topic/'repro/source-root'
        sys.path[:0]=[str(source_topic/'notes'),str(source_root/'topics/large-amplitude-twist-flex/scripts')]
        adaptive=loader.source_module('geometric_pullback_mode3',source_topic/'scripts/950f-prefix-adaptive-chart-bvp-v2.py')
        patch=loader.source_module('geometric_pullback_mode3_flat',source_topic/'scripts/db6f-prefix-flat-profile.py')
        patch.install(adaptive);adaptive.old.install_source(source_root)
    else:raise ValueError('Current source adapter supports base modes 2 or 3')
    from curve_stable_prefix_bvp import load_checkpoint
    rec=load_checkpoint(path)
    port=json.loads(port_path.read_text())
    if rec['frozen_profile'].get('prefix_bridge'):
        short=module('geometric_pullback_short_bridge',HERE/'root_short_bridge.py');short.install()
        port['cut']={**port['cut'],'_prefix_bridge':rec['frozen_profile']['prefix_bridge']}
    if rec['frozen_profile'].get('ramp_law')=='hermite_boost_neck':
        neck=module('geometric_pullback_neck_provider',HERE/'alternative-neck-provider.py')
        neck.install();port=neck.tagged_port(port,rec['frozen_profile'])
    kind=rec['angular_chart']
    if kind=='frozen-spline-adaptive-v1':
        chart=rec['chart'];warp=rec['warp_reference_q']
    elif kind=='general-support-core-blend-v1':
        chart=dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.);warp=0.
    else:raise ValueError('Unknown saved angular_chart: '+kind)
    Flow,_=adaptive.build_classes(chart)
    flow=Flow(rec['frozen_profile'],port,rec['config']['modes'],rec['gauge_amplitude'],
              angular,mode,warp_q=warp)
    if hasattr(flow.bridge,'breakpoints'):
        flow.breaks=np.unique(np.r_[flow.breaks,flow.prefix_end+flow.bridge.breakpoints])
    if kind=='general-support-core-blend-v1':
        charts.attach_to_adaptive_flow(flow,rec['chart_reference_coefficients'],
                    rec['chart_reference_frequencies'],reference='core-blend',
                    transition_start=rec.get('chart_transition_start',0.),
                    transition_end=rec.get('chart_transition_end',1.))
    if abs(flow.end-float(rec['meridian_length']))>2e-12*max(1.,flow.end):
        raise ValueError('Reconstructed physical length differs from saved checkpoint')
    mesh=np.asarray(rec['mesh']);pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),mesh,extrapolate=True,axis=1)
    sol=SimpleNamespace(x=mesh,y=pp(mesh),p=np.asarray(rec['parameters']),sol=pp)
    return SavedPrefix(rec,flow,sol,kind,mode),loader


class SavedPrefix:
    def __init__(self,rec,flow,sol,kind,mode):
        self.rec,self.flow,self.sol,self.kind,self.mode=rec,flow,sol,kind,mode
        self.M=int(rec['config']['modes']);self.q=float(rec['gauge_amplitude'])
        self.frequencies=mode*np.arange(1,self.M+1)

    def weights(self,s):
        s=np.atleast_1d(np.asarray(s,float));f=self.flow
        if self.kind=='general-support-core-blend-v1':
            return f.general_core_chart.weight(s)
        x=s/f.end;h0=f.spline(x);h1=f.spline(x,1)/f.end;h2=f.spline(x,2)/f.end**2
        u=np.clip((x-.75)/.25,0.,1.);fac=1/(.25*f.end)
        c=1-u**3*(10-15*u+6*u*u);cp=-30*u*u*(1-u)**2*fac
        cpp=-60*u*(1-u)*(1-2*u)*fac**2
        return tuple(z[:,None] for z in (f.warp_e*h0*c,
                  f.warp_e*(h1*c+h0*cp),f.warp_e*(h2*c+2*h1*cp+h0*cpp)))

    def angle(self,s,eta):
        eta=np.asarray(eta,float);b,bp,bpp=self.weights(s)
        if self.kind=='general-support-core-blend-v1':
            c=self.flow.general_core_chart
            n=c.frequencies;q=c.coefficients
            arg=eta[:,:,None]*n[None,None,:]
            Q=np.sin(arg)@((1-n*n)*q/n)
            Qp=np.cos(arg)@((1-n*n)*q)
            Qpp=-np.sin(arg)@(n*(1-n*n)*q)
        else:
            m=self.mode;Q=-np.sin(m*eta)/m;Qp=-np.cos(m*eta);Qpp=m*np.sin(m*eta)
        return dict(theta=eta+b*Q,rho=1+b*Qp,rhop=b*Qpp,
                    theta_s=bp*Q,theta_ss=bpp*Q,rho_s=bp*Qp,rhop_s=bp*Qpp,
                    b=b,bp=bp,bpp=bpp)

    def inverse(self,s,target):
        target=np.asarray(target,float);eta=target.copy()
        lo=target-2*np.pi;hi=target+2*np.pi
        for iteration in range(60):
            g=self.angle(s,eta);res=g['theta']-target
            if np.min(g['rho'])<=0:raise FloatingPointError('Old saved angle map lost positive derivative')
            done=abs(res)<=5e-14*np.maximum(1.,abs(target))
            if np.all(done):break
            lo=np.where((res<0)&~done,eta,lo);hi=np.where((res>0)&~done,eta,hi)
            new=eta-res/g['rho'];bad=(new<=lo)|(new>=hi)|~np.isfinite(new)
            new=np.where(bad,(lo+hi)/2,new);eta=np.where(done,eta,new)
        residual=float(np.max(abs(self.angle(s,eta)['theta']-target)))
        if residual>2e-12:raise FloatingPointError('Old material-angle inversion failed: '+str(residual))
        return eta,residual,iteration+1

    def base(self,s,eta):
        g=self.angle(s,eta);z=charts.GeneralCoreChart._exponential_jets(g)
        if self.kind=='general-support-core-blend-v1':
            c=self.flow.general_core_chart;n=c.frequencies;q=c.coefficients
            arg=eta[:,:,None]*n[None,None,:];co=np.cos(arg);si=np.sin(arg)
            h=1+co@q;hp=-si@(n*q);rho=1+co@((1-n*n)*q);rp=-si@(n*(1-n*n)*q)
            er=np.exp(1j*eta);C=(h+1j*hp)*er;Cp=1j*rho*er;Cpp=(1j*rp-rho)*er
            b,bp,bpp=g['b'],g['bp'],g['bpp']
            z=dict(p0=(1-b)*z['p0']+b*C,p1=(1-b)*z['p1']+b*Cp,p2=(1-b)*z['p2']+b*Cpp,
                   s1=(1-b)*z['s1']+bp*(C-z['p0']),
                   s2=(1-b)*z['s2']-2*bp*z['s1']+bpp*(C-z['p0']),
                   sp=(1-b)*z['sp']+bp*(Cp-z['p1']),spp=(1-b)*z['spp']+bp*(Cpp-z['p2']))
        return charts.GeneralCoreChart._multiply_profile(z,self.flow.profile(s))

    def synth(self,coef,eta,derivative=0):
        """Cylindrical Fourier value at independently varying old angles."""
        n=self.frequencies;co=np.cos(eta[:,:,None]*n);si=np.sin(eta[:,:,None]*n)
        coef=np.asarray(coef).T
        R0=coef[:,0,None]+np.einsum('npk,nk->np',co,coef[:,1:self.M+1])
        T0=np.einsum('npk,nk->np',si,coef[:,self.M+1:2*self.M+1])
        Z0=np.einsum('npk,nk->np',co,coef[:,2*self.M+1:])
        if derivative==0:
            H=(R0+1j*T0)*np.exp(1j*eta);Z=Z0
        else:
            R1=-np.einsum('npk,nk->np',si,coef[:,1:self.M+1]*n)
            T1=np.einsum('npk,nk->np',co,coef[:,self.M+1:2*self.M+1]*n)
            Z1=-np.einsum('npk,nk->np',si,coef[:,2*self.M+1:]*n)
            if derivative==1:
                H=(R1-T0+1j*(T1+R0))*np.exp(1j*eta);Z=Z1
            elif derivative==2:
                R2=-np.einsum('npk,nk->np',co,coef[:,1:self.M+1]*n*n)
                T2=-np.einsum('npk,nk->np',si,coef[:,self.M+1:2*self.M+1]*n*n)
                Z2=-np.einsum('npk,nk->np',co,coef[:,2*self.M+1:]*n*n)
                H=(R2-2*T1-R0+1j*(T2+2*R1-T0))*np.exp(1j*eta);Z=Z2
            else:raise ValueError('Only angular derivatives 0,1,2 are implemented')
        return np.stack((H.real,H.imag,Z),axis=-1)

    def height_jets(self,s,angular=512,order=6):
        f=self.flow;H=f.height_integral(self.sol,s,angular,order)
        _,B1,B2=f.basis(angular);Hp=np.empty(len(s));Hpp=Hp.copy()
        for first in range(0,len(s),32):
            sl=slice(first,first+32);ss=s[sl]
            fr,_,dW=f.velocity_s(ss,self.sol.sol(ss),self.sol.sol(ss,1),B1,B2)
            Hp[sl]=np.mean(fr['V'][:,:,2],axis=1);Hpp[sl]=np.mean(dW[:,:,2],axis=1)
        return H,Hp,Hpp

    def jets(self,s,eta,height):
        b=self.base(s,eta);Y=self.sol.sol(s);Yp=self.sol.sol(s,1);Ypp=self.sol.sol(s,2)
        out=dict(pos=b['pos']+self.q*self.synth(Y,eta),
                 p1=b['p1']+self.q*self.synth(Y,eta,1),
                 p2=b['p2']+self.q*self.synth(Y,eta,2),
                 s1=b['s1']+self.q*self.synth(Yp,eta),
                 s2=b['s2']+self.q*self.synth(Ypp,eta),
                 sp=b['sp']+self.q*self.synth(Yp,eta,1))
        for key,H in zip(('pos','s1','s2'),height):out[key][:,:,2]+=H[:,None]
        return out


def basis_values(modes,mode,psi):
    n=mode*np.arange(1,modes+1);er=np.c_[np.cos(psi),np.sin(psi),np.zeros(len(psi))]
    et=np.c_[-np.sin(psi),np.cos(psi),np.zeros(len(psi))];ez=np.tile([0.,0.,1.],(len(psi),1))
    B=np.zeros((3*modes+1,len(psi),3));B1=B.copy();B2=B.copy()
    B[0]=er;B1[0]=et;B2[0]=-er
    for j,k in enumerate(n):
        co=np.cos(k*psi)[:,None];si=np.sin(k*psi)[:,None]
        R,T,Z=1+j,modes+1+j,2*modes+1+j
        B[R]=co*er;B1[R]=-k*si*er+co*et;B2[R]=-(k*k+1)*co*er-2*k*si*et
        B[T]=si*et;B1[T]=k*co*et-si*er;B2[T]=-(k*k+1)*si*et-2*k*co*er
        B[Z]=co*ez;B1[Z]=-k*si*ez;B2[Z]=-k*k*co*ez
    return B,B1,B2


def project(value,B):
    return np.einsum('npc,kpc->kn',value,B,optimize=True)/np.sum(B*B,axis=(1,2))[:,None]


def values(state,B):return np.einsum('kn,kpc->npc',state,B,optimize=True)


def convert(saved,new_chart,modes,gauge,s,angular=512,height_angular=512):
    """Return radial jet data for the SAME saved physical curve before projection.

    No rescaling of physical s or s-dependent vertical translation is permitted.
    Fourier projection errors are measured and reported, not declared zero.
    """
    if abs(new_chart.length-saved.flow.end)>2e-12*max(1.,new_chart.length):
        raise ValueError('Physical-preserving conversion requires the same meridian length')
    s=np.asarray(s,float);psi=2*np.pi*np.arange(angular)/angular
    B,B1,B2=basis_values(modes,saved.mode,psi)
    height=saved.height_jets(s,height_angular)
    arrays=dict(s=s,y=np.empty((3*modes+1,len(s))),ys=np.empty((3*modes+1,len(s))),yss=np.empty((3*modes+1,len(s))))
    for key in ('height_original','height_original_s','height_original_ss','height_correction','height_correction_s','height_correction_ss','height_new','height_new_s','height_new_ss'):
        arrays[key]=np.empty(len(s))
    errors=dict(position=0.,radial_first=0.,radial_second=0.,angular_first=0.,angular_second=0.,mixed=0.,angle_inverse=0.)
    maximum_iterations=0
    for first in range(0,len(s),24):
        sl=slice(first,first+24);ss=s[sl]
        ng=new_chart.geometry(ss,psi,saved.flow.profile)
        eta,res,it=saved.inverse(ss,ng['theta']);maximum_iterations=max(maximum_iterations,it)
        og=saved.angle(ss,eta);old=saved.jets(ss,eta,tuple(h[sl]for h in height))
        ep=ng['rho']/og['rho'];es=(ng['theta_s']-og['theta_s'])/og['rho']
        epp=(ng['rhop']-og['rhop']*ep*ep)/og['rho']
        esp=(ng['rho_s']-og['rho_s']*ep-og['rhop']*es*ep)/og['rho']
        ess=(ng['theta_ss']-og['theta_ss']-2*og['rho_s']*es-og['rhop']*es*es)/og['rho']
        v=lambda x:x[:,:,None]
        target=dict(pos=old['pos'],p1=old['p1']*v(ep),
                    p2=old['p2']*v(ep*ep)+old['p1']*v(epp),
                    s1=old['s1']+old['p1']*v(es),
                    s2=old['s2']+2*old['sp']*v(es)+old['p2']*v(es*es)+old['p1']*v(ess),
                    sp=old['sp']*v(ep)+old['p2']*v(es*ep)+old['p1']*v(esp))
        for order,key in enumerate(('pos','s1','s2')):
            residual=target[key]-ng[key]
            state=project(residual,B)/gauge
            statekey=('y','ys','yss')[order];arrays[statekey][:,sl]=state
            newmean=np.mean(residual[:,:,2],axis=1)
            suffix=('','_s','_ss')[order]
            arrays['height_original'+suffix][sl]=height[order][sl]
            arrays['height_new'+suffix][sl]=newmean
            arrays['height_correction'+suffix][sl]=newmean-height[order][sl]
            reconstructed=ng[key]+gauge*values(state,B)
            reconstructed[:,:,2]+=newmean[:,None]
            ekey=('position','radial_first','radial_second')[order]
            errors[ekey]=max(errors[ekey],float(np.max(np.linalg.norm(reconstructed-target[key],axis=-1))))
        for key,statekey,base in [('p1','y',B1),('p2','y',B2),('sp','ys',B1)]:
            reconstructed=ng[key]+gauge*values(arrays[statekey][:,sl],base)
            ekey={'p1':'angular_first','p2':'angular_second','sp':'mixed'}[key]
            errors[ekey]=max(errors[ekey],float(np.max(np.linalg.norm(reconstructed-target[key],axis=-1))))
        errors['angle_inverse']=max(errors['angle_inverse'],res)
    summary=dict(scope='Initial-guess representation conversion, not a new solution or changed physical curve before finite projection.',
                 old_angular_chart=saved.kind,new_angular_chart='general-support-core-blend-v1',
                 new_reference_coefficients=new_chart.coefficients.tolist(),new_reference_frequencies=new_chart.frequencies.tolist(),
                 physical_profile=saved.rec['frozen_profile'],physical_length=saved.flow.end,
                 old_modes=saved.M,new_modes=modes,old_gauge=saved.q,new_gauge=gauge,
                 radial_samples=len(s),angular_projection=angular,height_angular=height_angular,
                 height_quadrature_order=6,
                 height_definition='The source mean-height antiderivative is reconstructed with the stated angular quadrature and span-wise Gauss order; no interval integration certificate is asserted.',
                 maximum_inverse_iterations=maximum_iterations,sampled_projection_errors=errors,
                 mean_correction_max=[float(np.max(abs(arrays[k])))for k in ('height_correction','height_correction_s','height_correction_ss')],
                 new_inlet_state_max=float(np.max(abs(arrays['y'][:,0]))),
                 warning='The nonzero s-dependent height correction must be retained to represent the same saved image. No PDE solving occurred.')
    return arrays,summary


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','checkpoint','port','out-prefix'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--core-json',type=Path)
    p.add_argument('--amplitude',type=float,default=.2)
    p.add_argument('--modes',type=int,default=24)
    p.add_argument('--radial',type=int,default=151)
    p.add_argument('--angular',type=int,default=1024)
    p.add_argument('--height-angular',type=int,default=512)
    p.add_argument('--gauge',type=float)
    p.add_argument('--use-old-core',action='store_true',help='Use all saved actual core coefficients as the new reference')
    a=p.parse_args();saved,loader=load_saved(a.checkpoint,a.source_topic,a.port,a.height_angular)
    if a.use_old_core:
        core=saved.rec.get('core')or saved.rec.get('summary',{}).get('core')
        if not core:raise ValueError('Saved actual core coefficients missing')
        q=core['coefficients'];freq=core['frequencies']
    elif a.core_json:
        c=json.loads(a.core_json.read_text())
        q=c.get('coefficients',c.get('coefficients_float_initial_guess'))
        freq=c.get('frequencies',[2*j for j in range(1,len(q)+1)])
    else:q=[a.amplitude,-a.amplitude/(10*math.sqrt(2))];freq=[2,4]
    new=charts.GeneralCoreChart(q,freq,saved.flow.end)
    s=np.unique(np.r_[np.linspace(0,saved.flow.end,a.radial),saved.flow.breaks])
    arrays,summary=convert(saved,new,a.modes,a.gauge or a.amplitude,s,a.angular,a.height_angular)
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    data=a.out_prefix.with_suffix('.npz');np.savez_compressed(data,**arrays)
    if data.stat().st_size>1_000_000:
        compressed=data.with_suffix('.npz.gz')
        with data.open('rb')as src,gzip.open(compressed,'wb',compresslevel=9)as dst:
            for block in iter(lambda:src.read(1048576),b''):dst.write(block)
        data.unlink();data=compressed
    if data.stat().st_size>=5_000_000:raise ValueError('Warm data exceeds single-file limit; reduce radial samples')
    summary.update(checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
                   implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   data_file=data.name,data_sha256=hashlib.sha256(data.read_bytes()).hexdigest(),data_bytes=data.stat().st_size,
                   source_transforms=loader.TRANSFORMS)
    a.out_prefix.with_suffix('.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:summary[k]for k in ('old_angular_chart','old_modes','new_modes','sampled_projection_errors','mean_correction_max','new_inlet_state_max','data_bytes')}),flush=True)


if __name__=='__main__':main()

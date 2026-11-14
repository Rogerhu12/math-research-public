#!/usr/bin/env python3
"""Same frozen elliptic g with Fourier-coefficient ODE state and extended frames.

The ODE state and solve_ivp remain float64. Independent small Fourier modes do
not share O(1) Cartesian point-value additions. Geometry, FFT differentiation,
projection and actual E/F/G are evaluated in numpy.longdouble/scipy.fft.
This is a finite diagnostic, not a BVP or a continuous certificate.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,importlib.util
from pathlib import Path
import numpy as np
from scipy import fft as spfft
from scipy.signal import resample
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
def module(name,file):
    sp=importlib.util.spec_from_file_location(name,HERE/file)
    obj=importlib.util.module_from_spec(sp);sp.loader.exec_module(obj);return obj
ff=module('fd2d_fixed_spectral_base','fd2d_fixed_ellipse_flow.py')
fm=ff.fm


class SpectralMixin:
    def initial_coefficients(self):
        coeff=np.zeros((self.nodes//2+1,3),dtype=float)
        coeff[1,0]=self.A/2;coeff[1,1]=-self.B/2
        return coeff.ravel()

    def decode(self,coefficients):
        row=np.asarray(coefficients,dtype=np.longdouble).reshape(self.nodes//2+1,3)
        coeff=np.zeros(row.shape,dtype=np.clongdouble);kk=np.arange(len(row));odd=kk%2==1;even=~odd
        coeff[odd,0]=row[odd,0];coeff[odd,1]=1j*row[odd,1];coeff[even,2]=row[even,2]
        return spfft.irfft(coeff,n=self.nodes,axis=0,norm='forward')

    def encode(self,point_values):
        coeff=spfft.rfft(np.asarray(point_values,dtype=np.longdouble),axis=0,norm='forward')
        row=np.zeros(coeff.shape,dtype=np.longdouble);kk=np.arange(len(row));odd=kk%2==1;even=~odd
        row[odd,0]=coeff[odd,0].real;row[odd,1]=coeff[odd,1].imag;row[even,2]=coeff[even,2].real
        return np.asarray(row.ravel(),dtype=float)

    def derivative(self,x,order=1):
        xx=np.asarray(x,dtype=np.longdouble)
        return spfft.ifft(spfft.fft(xx,axis=0)*((1j*self.k)**order)[:,None],axis=0).real

    def project(self,x):
        coarse=resample(np.asarray(x,dtype=np.longdouble),self.nodes,axis=0)
        coeff=spfft.rfft(coarse,axis=0);kk=np.arange(len(coeff),dtype=np.longdouble)
        if self.filter_strength>0:
            coeff*=np.exp(-np.longdouble(self.filter_strength)*(kk/np.longdouble(self.nodes/2))**self.filter_order)[:,None]
        if self.symmetry:
            keep=np.zeros_like(coeff);odd=np.arange(len(coeff))%2==1;even=~odd
            keep[odd,0]=coeff[odd,0].real;keep[odd,1]=1j*coeff[odd,1].imag;keep[even,2]=coeff[even,2].real
            coeff=keep
        coarse=spfft.irfft(coeff,n=self.nodes,axis=0)
        return coarse,resample(coarse,self.work,axis=0)


class SpectralFixedFlow(SpectralMixin,ff.FixedFlow):
    def frame(self,s,y):
        return super().frame(s,self.decode(y).ravel())

    def rhs(self,s,y):
        self.calls+=1
        if self.calls>self.max_calls:raise RuntimeError('Finite spectral-state RHS-call limit')
        return self.encode(self.frame(s,y)['Vcoarse'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--nodes',type=int,default=512)
    p.add_argument('--oversample',type=int,default=2);p.add_argument('--max-calls',type=int,default=60000)
    p.add_argument('--stop-at',type=float);p.add_argument('--max-step',type=float,default=.001)
    args=p.parse_args();candidate=fm.Candidate(json.loads(args.candidate.read_text()))
    flow=SpectralFixedFlow(candidate,args.nodes,args.oversample,args.max_calls)
    y=flow.initial_coefficients();end=min(candidate.end,args.stop_at) if args.stop_at is not None else candidate.end
    def chart(s,y):return float(flow.frame(s,y)['chart'].min())-1e-4
    def metric(s,y):return 2e-5-flow.frame(s,y)['metric_error']
    def curvature(s,y):return 1/.136-float(flow.frame(s,y)['curvature'].max())
    def slab(s,y):return .75-float(abs(flow.frame(s,y)['X'][:,1]).max())
    def height(s,y):return 1.2886410585615193-float(abs(flow.frame(s,y)['X'][:,2]).max())
    events=[chart,metric,curvature,slab,height];names=['chart','metric','curvature','slab','height']
    for e in events:e.terminal=True;e.direction=-1
    initial=flow.frame(0.,y);decoded=flow.decode(y)
    report=dict(scope=__doc__,candidate=args.candidate.name,candidate_sha256=fm.digest(args.candidate),
        source_sha256=fm.digest(__file__),provider_sha256=fm.digest(HERE/'fd2d_frozen_ellipse_candidate.py'),
        base_flow_sha256=fm.digest(HERE/'fd2d_fixed_ellipse_flow.py'),nodes=args.nodes,geometry_grid=flow.work,
        dtypes=dict(initial_ode_state=str(y.dtype),decoded_geometry=str(decoded.dtype),
                    frame_X=str(initial['X'].dtype),frame_V=str(initial['V'].dtype),
                    fft=str(spfft.rfft(decoded,axis=0).dtype),
                    longdouble_mantissa_bits=int(np.finfo(np.longdouble).nmant)),
        metric_frozen=True,closed_surface=False,reaches_requested_endpoint=False,
        initial=flow.diagnostics(0.,y),rows=[])
    # Angular derivatives enter geometry: use a mode-dependent absolute error
    # weight, while retaining an ordinary float64 solve_ivp state.
    kk=np.arange(args.nodes//2+1);atol=np.repeat(2e-14/(1+kk)**2,3)
    last_s=0.
    try:
        for j,seg in enumerate(candidate.segments):
            if seg['s0']>=end-1e-14:break
            right=min(seg['s1'],end)
            sol=solve_ivp(flow.rhs,(seg['s0'],right),y,method='DOP853',rtol=2e-12,atol=atol,
                max_step=args.max_step,t_eval=np.linspace(seg['s0'],right,5),events=events)
            report['dtypes']['solve_ivp_output']=str(sol.y.dtype)
            rec=[flow.diagnostics(s,z) for s,z in zip(sol.t,sol.y.T)]
            last_s=float(sol.t[-1]);y=sol.y[:,-1]
            if sol.status==1:
                for ts,zs in zip(sol.t_events,sol.y_events):
                    if len(ts):last_s=float(ts[-1]);y=zs[-1];rec.append(flow.diagnostics(last_s,y))
            row=dict(index=j,segment_kind=seg['kind'],segment_label=seg.get('label'),status=sol.status,
                events={name:ts.tolist() for name,ts in zip(names,sol.t_events)},last=rec[-1],
                extrema={key:(min(r[key] for r in rec) if 'min' in key else max(r[key] for r in rec))
                    for key in ('minimum_chart','relative_metric_error','metric_angular_error','metric_E_error',
                        'metric_F_error','sampled_curvature_max','maximum_radius','maximum_abs_z','maximum_abs_y',
                        'held_witness_min_distance','velocity_projection_error')})
            report['rows'].append(row);args.out.write_text(json.dumps(report,indent=2)+'\n')
            np.savez_compressed(args.checkpoint,coefficients=y,s=last_s,
                candidate_sha256=report['candidate_sha256'],state_representation='rfft-forward-D2-real-imag-real',
                nodes=args.nodes)
            if sol.status!=0:print(json.dumps(row),flush=True);break
        report['reaches_requested_endpoint']=abs(last_s-end)<1e-12
    except Exception as exc:report['failure']=str(exc)
    report['rhs_calls']=flow.calls;report['last_s']=last_s
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report.get(k) for k in ('reaches_requested_endpoint','rhs_calls','last_s','failure')}),flush=True)


if __name__=='__main__':main()

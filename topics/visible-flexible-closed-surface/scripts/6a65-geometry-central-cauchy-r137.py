#!/usr/bin/env python3
"""New small negative-K ramp from the unchanged exact central cylinder.

Reuses the existing native-frame Gauss--Codazzi IVP. The metric is constant on
the central collar and only departs where f''>0. Its actual finite Cartesian
endpoint is compared against an explicitly new exact-form R137 inlet built
from that endpoint curve; endpoint discrepancies are never silently erased.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
def module(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
hybrid=module('new_ramp_existing_hybrid','fd2d-gc-ellipse-hybrid-flow.py')
ports=module('new_ramp_ports','6a65-geometry-r137-two-connectors.py')
core=ports.core


class Candidate:
    def __init__(self,A,B,length,v):
        ellipse=ports.ellipse_curve(A,B,0)
        self.ellipse=SimpleNamespace(A=A,B=B,a0=ellipse.a)
        self.length,self.v=length,v
    def profile(self,s):
        s=np.asarray(s);t=np.clip(s/self.length,0,1)
        S=126*t**5-420*t**6+540*t**7-315*t**8+70*t**9
        J=21*t**6-60*t**7+67.5*t**8-35*t**9+7*t**10
        f=self.ellipse.a0+self.v*self.length*J+self.v*np.maximum(0,s-self.length)
        fs=self.v*S;fss=self.v/self.length*630*t**4*(1-t)**4
        return f,fs,fss


def reset_arc(curve):
    lo=curve.cuts[:-1];length=np.diff(curve.cuts);theta=lo[:,None]+length[:,None]*curve.gx
    speed=np.linalg.norm(curve.derivative(theta.ravel(),1),axis=1).reshape(theta.shape)
    lengths=length*np.sum(speed*curve.gw,axis=1);curve.cumulative=np.r_[0,np.cumsum(lengths)]
    curve.perimeter=curve.cumulative[-1];curve.a=curve.perimeter/(2*np.pi)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('source_samples');ap.add_argument('output_prefix')
    ap.add_argument('--length',type=float,default=.02);ap.add_argument('--v',type=float,default=.003)
    ap.add_argument('--modes',type=int,default=95);ap.add_argument('--angles',type=int,default=1024)
    ap.add_argument('--coast-lengths',type=float,nargs='+',default=[.15,.35,.5]);args=ap.parse_args();start=time.time();prefix=Path(args.output_prefix)
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh prefix required')
    raw=json.loads(Path(args.source_samples).read_text());seed=raw['inheritedGapLengthDesign']['centralSeed']
    A,B=seed['actualCentralA'],seed['actualCentralB'];c=13/128
    candidate=Candidate(A,B,args.length,args.v);flow=hybrid.Hybrid(candidate,args.modes,2,30000)
    initial=flow.initial();other=initial[flow.shape_size:].reshape(flow.work,12);other[:,2]=c
    atol=2e-14/(1+flow.active_wave)**2
    sol=solve_ivp(flow.rhs,(0,args.length),initial,method='DOP853',rtol=2e-12,atol=atol,
                  max_step=args.length/128,t_eval=np.linspace(0,args.length,33))
    if sol.status!=0 or sol.t[-1]!=args.length:raise RuntimeError('Actual Cauchy process did not reach its stated endpoint')
    rows=[flow.diagnostics(float(s),state) for s,state in zip(sol.t,sol.y.T)]
    end=flow.frame(args.length,sol.y[:,-1]);native=np.asarray(end['values'],float);X=native[:,2:5]
    degree=flow.work//2-1;curve=core.Curve(X,degree)
    old_a=curve.a;target=float(candidate.profile([args.length])[0][0]);factor=target/old_a
    center=curve.coeff[curve.degree].copy();curve.coeff*=factor;curve.coeff[curve.degree]=center;reset_arc(curve)
    u=2*np.pi*np.arange(args.angles)/args.angles;data=curve.inlet(u,args.v);new=core.propagate(curve.a,args.v,0.,data)
    central=ports.ellipse_curve(A,B,0);theta=central.theta(u);modes=np.fft.fftfreq(flow.work,1/flow.work)
    coeff=np.fft.fft(native,axis=0)/flow.work
    def old_derivative(order=0):return (np.exp(1j*theta[:,None]*modes)@(coeff*(1j*modes[:,None])**order)).real
    old,old1,old2=old_derivative(),old_derivative(1),old_derivative(2)
    h=np.sqrt(A*A*np.sin(theta)**2+B*B*np.cos(theta)**2);theta_u=central.a/h
    theta_uu=-central.a**2*(A*A-B*B)*np.sin(theta)*np.cos(theta)/h**4
    old_jets={'X':old[:,2:5],'X_s':old[:,5:8],'X_ss':(old[:,1]**2/old[:,0])[:,None]*old[:,11:14],
              'X_u':old1[:,2:5]*theta_u[:,None],'X_su':old1[:,5:8]*theta_u[:,None],
              'X_uu':old2[:,2:5]*theta_u[:,None]**2+old1[:,2:5]*theta_uu[:,None]}
    mismatch={key:float(np.max(np.linalg.norm(new[key]-value,axis=1))) for key,value in old_jets.items()}
    n,m=data['n'],data['m'];k=m/n;ku=data['m_u']/n-m*data['n_u']/n**2;Bfield=args.v*(1+k*k)-ku
    negative=Bfield<0;Wfocus=np.where(negative,curve.a/np.maximum(-Bfield,1e-300),np.inf)
    focus=np.where(negative,np.hypot(curve.a/args.v+Wfocus,Wfocus*k)-curve.a/args.v,np.inf)
    coast=[];G=data['e1']-k[:,None]*data['e2'];marker=np.array([0,A,0])
    for length in args.coast_lengths:
        try:
            output=core.propagate(curve.a,args.v,length,data)
            at_u=core.at_material(curve.a,args.v,length,u,lambda t:curve.inlet(t,args.v))
        except (ValueError,RuntimeError) as exc:coast.append(dict(length=length,accepted=False,error=str(exc)));continue
        W=output['w'];D=output['D'];both=np.concatenate((data['X'],output['X']))
        wh=np.clip(-np.einsum('ij,ij->i',data['X']-marker,G)/np.einsum('ij,ij->i',G,G),0,W)
        nearest=data['X']+wh[:,None]*G
        coast.append(dict(length=length,accepted=True,minimumD=float(min(curve.a,np.min(D))),
            maximumRankOneCurvature=float(max(np.max(n*(1+k*k)),np.max(curve.a*n*(1+k*k)/D))),
            maximumCartesianMetric=float(np.max(at_u['metric'])),maximumOwnEndpointCurvature=float(np.max(at_u['actual_curvature'])),
            minimumMaterialDerivative=float(np.min(output['U_t'])),maximumRadius=float(np.max(np.linalg.norm(both,axis=1))),
            maximumAbsY=float(np.max(np.abs(both[:,1]))),maximumZ=float(np.max(both[:,2])),
            minimumHeld=float(np.min(np.linalg.norm(nearest-marker,axis=1)))))
        np.savez_compressed(str(prefix)+f'-coast-{length:g}-endpoint.npz',**{key:val for key,val in at_u.items() if isinstance(val,(np.ndarray,float,int,bool))})
    np.savez_compressed(str(prefix)+'-cauchy-state.npz',state=sol.y[:,-1],native=native,curve_modes=curve.modes,curve_coefficients=curve.coeff)
    report=dict(schema='6a65-existing-GC-real-central-negative-K-ramp-to-R137-v1',
        sourceSHA256=hashlib.sha256(Path(args.source_samples).read_bytes()).hexdigest(),
        scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        reusedHybridSHA256=hashlib.sha256((HERE/'fd2d-gc-ellipse-hybrid-flow.py').read_bytes()).hexdigest(),
        parameters=dict(centralA=A,centralB=B,centralLength=c,centralRadius=central.a,rampLength=args.length,v=args.v,
            fDefinition='a0+v*L*integral_0^(s/L)S9; f_s=v*S9; unchanged cylinder before ramp',
            fEnd=target,modes=args.modes,workAngles=flow.work,exactFormCurveDegree=degree,consumerAngles=args.angles),
        process=dict(status=sol.status,nfev=sol.nfev,rhsCalls=flow.calls,reachedEndpoint=True),
        cauchyWholeRecordedRamp=dict(maximumMetric=max(x['metric'] for x in rows),maximumOwnCurvature=max(x['actual_curvature'] for x in rows),
            minimumN=min(x['minimum_n'] for x in rows),maximumFrameDefect=max(x['curve_frame_defect'] for x in rows),
            maximumProjectionDefect=max(x['projection_defect'] for x in rows),maximumRadius=max(x['maximum_radius'] for x in rows),
            minimumHeld=min(x['held_distance'] for x in rows)),
        endpoint=rows[-1],curveRescale=dict(beforeRadius=old_a,targetRadius=target,numericalScale=factor,afterRadius=curve.a),
        completeNewInletTwoJetDifferenceFromActualCauchy=mismatch,
        newInlet=dict(minimumN=float(np.min(n)),maximumAbsM=float(np.max(np.abs(m))),maximumAbsKratio=float(np.max(np.abs(k))),
            maximumAbsKratioDerivative=float(np.max(np.abs(ku))),minimumB=float(np.min(Bfield)),minimumSampledFocus=float(np.min(focus)),
            maximumOwnCurvature=float(np.max(new['actual_curvature'])),maximumMetric=float(np.max(new['metric']))),
        coasts=coast,seconds=time.time()-start,finiteCauchyNotExactContinuumSolution=True,newExactFormCoastNotAutomaticallyGlued=True,
        wholeClosedSurface=False,continuousCertificate=False)
    Path(str(prefix)+'-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))


if __name__=='__main__':main()

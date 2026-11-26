#!/usr/bin/env python3
"""Actual full-angle GC attempt from a central cylinder toward the round cut.

The new f is C2 at ramp/coast/turn interfaces and reaches f=.8,f'=-1,f''=0
by definition. The Cartesian field must independently reach it, remain an
immersion, and match a developed-tail two-jet. The script never assumes those
claims from the scalar profile. Every saved state is an actually accepted
DOP853 state, including when a subsequent internal stage is rejected.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cauchy_tail_parent',HERE/'6a65-geometry-central-cauchy-r137.py')
parent=importlib.util.module_from_spec(spec);sys.modules[spec.name]=parent;spec.loader.exec_module(parent)
fixed_spec=importlib.util.spec_from_file_location('cauchy_tail_fixed_radius',HERE/'6a65-m12-r137-fixed-metric-adapter.py')
fixed_module=importlib.util.module_from_spec(fixed_spec);sys.modules[fixed_spec.name]=fixed_module;fixed_spec.loader.exec_module(fixed_module)


def SJ(t):
    t=np.asarray(t);S=126*t**5-420*t**6+540*t**7-315*t**8+70*t**9
    J=21*t**6-60*t**7+67.5*t**8-35*t**9+7*t**10
    dS=630*t**4*(1-t)**4;return S,J,dS


def material_from_theta(curve,theta):
    theta=np.asarray(theta,float);cell=np.minimum(curve.panels-1,np.floor(theta/(2*np.pi)*curve.panels).astype(int))
    lo=curve.cuts[cell];q=lo[:,None]+(theta-lo)[:,None]*curve.gx
    speed=np.linalg.norm(curve.derivative(q.ravel(),1),axis=1).reshape(q.shape)
    return (curve.cumulative[cell]+(theta-lo)*np.sum(speed*curve.gw,axis=1))/curve.a


def exact_coast(flow,candidate,state,prefix,curve_degree=None):
    source=np.asarray(flow.decode(state),float);degree=curve_degree or flow.work//2-1
    raw_curve=parent.core.Curve(source[:,2:5],degree)
    target=float(candidate.profile([candidate.length])[0][0]);curve=fixed_module.FixedRadiusCurve(raw_curve,target);scale=curve.normalization
    central=parent.ports.ellipse_curve(candidate.ellipse.A,candidate.ellipse.B,0)
    u=material_from_theta(central,np.asarray(flow.theta,float));inlet=curve.inlet(u,candidate.v)
    at0=parent.core.propagate(curve.a,candidate.v,0.,inlet)
    out=parent.core.at_material(curve.a,candidate.v,candidate.coast,u,lambda t:curve.inlet(t,candidate.v))
    values=np.column_stack((out['n'],out['m'],out['X'],out['e1'],out['e2'],out['N']))
    state_new=flow.encode(values);decoded=flow.decode(state_new)
    np.savez_compressed(str(prefix)+'-exact-coast-endpoint.npz',**{key:value for key,value in out.items() if isinstance(value,(np.ndarray,float,int,bool))})
    np.savez_compressed(str(prefix)+'-exact-coast-master.npz',curve_modes=raw_curve.modes,curve_coefficients=raw_curve.coeff,
        unnormalized_radius=raw_curve.a,exact_target_radius=target,v=candidate.v,length=candidate.coast,degree=degree)
    report=dict(exactFormCurveDegree=curve.degree,scaleToSameRampEndRadius=scale,
        actualInletPositionDifference=float(np.max(np.linalg.norm(at0['X']-source[:,2:5],axis=1))),
        actualInletXsDifference=float(np.max(np.linalg.norm(at0['X_s']-source[:,5:8],axis=1))),
        actualInletXssDifference=float(np.max(np.linalg.norm(at0['X_ss']-(source[:,1]**2/source[:,0])[:,None]*source[:,11:14],axis=1))),
        exactFormEndpointMetric=float(np.max(out['metric'])),exactFormEndpointCurvature=float(np.max(out['actual_curvature'])),
        minimumD=float(np.min(out['D'])),minimumMaterialDerivative=float(np.min(out['U_t'])),
        shapeInjectionDifference=float(np.max(np.abs(decoded[:,:2]-values[:,:2]))),
        exactEndpointNotAutomaticallyEqualToFiniteCauchy=True)
    return state_new,report


class Candidate(parent.Candidate):
    def __init__(self,A,B,ramp,v,coast,cut=.8):
        super().__init__(A,B,ramp,v);self.coast=coast;self.cut=cut
        self.turn_start=ramp+coast;self.turn_a=self.ellipse.a0+v*ramp/2+v*coast
        self.turn_length=2*(self.turn_a-cut)/(1-v)
        if self.turn_length<=0:raise ValueError('Invalid new scalar cut design')
        self.end=self.turn_start+self.turn_length
        self.segments=[(0.,ramp,'negative_K_ramp'),(ramp,self.turn_start,'affine_coast'),(self.turn_start,self.end,'positive_K_turn')]
    def profile(self,s):
        s=np.asarray(s);f,fs,fss=super().profile(s);mask=s>=self.turn_start
        t=np.clip((s-self.turn_start)/self.turn_length,0,1);S,J,dS=SJ(t)
        f=np.where(mask,self.turn_a+self.v*(s-self.turn_start)-(1+self.v)*self.turn_length*J,f)
        fs=np.where(mask,self.v-(1+self.v)*S,fs);fss=np.where(mask,-(1+self.v)/self.turn_length*dS,fss)
        return f,fs,fss


def main():
    ap=argparse.ArgumentParser();ap.add_argument('source_samples');ap.add_argument('output_prefix')
    ap.add_argument('--ramp',type=float,default=.18);ap.add_argument('--v',type=float,default=.15)
    ap.add_argument('--coast',type=float,default=.05);ap.add_argument('--modes',type=int,default=95)
    ap.add_argument('--exact-coast',action='store_true')
    ap.add_argument('--curve-degree',type=int)
    ap.add_argument('--max-step',type=float,default=.0005);args=ap.parse_args();prefix=Path(args.output_prefix);start=time.time()
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh prefix required')
    raw=json.loads(Path(args.source_samples).read_text());seed=raw['inheritedGapLengthDesign']['centralSeed']
    candidate=Candidate(seed['actualCentralA'],seed['actualCentralB'],args.ramp,args.v,args.coast)
    flow=parent.hybrid.Hybrid(candidate,args.modes,2,120000);state=flow.initial();state[flow.shape_size:].reshape(flow.work,12)[:,2]=13/128
    atol=2e-14/(1+flow.active_wave)**2;rows=[];failure=None;accepted=0;s=0.
    maxima=dict(metric=0.,actual_curvature=0.,maximum_radius=0.,maximum_abs_y=0.,maximum_abs_z=0.,projection_defect=0.,curve_frame_defect=0.)
    minima=dict(minimum_n=float('inf'),held_distance=float('inf'))
    last=flow.diagnostics(s,state);coast_bridge=None
    for left,right,kind in candidate.segments:
        if right<=left:continue
        if kind=='affine_coast' and args.exact_coast:
            try:state,coast_bridge=exact_coast(flow,candidate,state,prefix,args.curve_degree)
            except Exception as exc:failure=dict(segment=kind,type=type(exc).__name__,message=str(exc));break
            s=right;last=flow.diagnostics(s,state);rows.append(dict(segment='exact_R137_coast_injection',acceptedSteps=accepted,**last))
            for key in maxima:maxima[key]=max(maxima[key],last[key])
            for key in minima:minima[key]=min(minima[key],last[key])
            print(json.dumps(dict(segment='exact_R137_coast',s=s,metric=last['metric'],coastBridge=coast_bridge)),flush=True)
            np.savez_compressed(str(prefix)+'-coast-injected-state.npz',state=state,s=s,native=np.asarray(flow.decode(state),float),modes=args.modes)
            continue
        solver=DOP853(flow.rhs,left,state,right,max_step=args.max_step,rtol=2e-12,atol=atol)
        segment_accept=0
        while solver.status=='running':
            try:message=solver.step()
            except Exception as exc:failure=dict(segment=kind,type=type(exc).__name__,message=str(exc),failedInternalStageNotSaved=True);break
            if solver.status=='failed':failure=dict(segment=kind,type='DOP853_failed',message=message,failedInternalStageNotSaved=True);break
            s,state=float(solver.t),solver.y.copy();accepted+=1;segment_accept+=1;last=flow.diagnostics(s,state)
            for key in maxima:maxima[key]=max(maxima[key],last[key])
            for key in minima:minima[key]=min(minima[key],last[key])
            if segment_accept%20==0 or solver.status!='running':rows.append(dict(segment=kind,acceptedSteps=accepted,**last))
            if last['metric']>1e-5 or last['actual_curvature']>100 or last['minimum_n']<1e-5:
                failure=dict(segment=kind,type='explicit_actual_field_stop',metric=last['metric'],curvature=last['actual_curvature'],minimumN=last['minimum_n']);break
        print(json.dumps(dict(segment=kind,s=s,acceptedSteps=accepted,metric=last['metric'],curvature=last['actual_curvature'],minimumN=last['minimum_n'],failure=failure)),flush=True)
        np.savez_compressed(str(prefix)+'-'+kind+'-last-accepted.npz',state=state,s=s,native=np.asarray(flow.decode(state),float),modes=args.modes)
        if failure:break
    native=np.asarray(flow.frame(s,state)['values'],float)
    np.savez_compressed(str(prefix)+'-last-accepted.npz',state=state,s=s,native=native,modes=args.modes)
    report=dict(schema='6a65-new-actual-GC-central-ramp-coast-round-cut-attempt-v1',
        sourceSHA256=hashlib.sha256(Path(args.source_samples).read_bytes()).hexdigest(),scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        parameters=dict(A=candidate.ellipse.A,B=candidate.ellipse.B,a0=candidate.ellipse.a0,ramp=args.ramp,v=args.v,coast=args.coast,
            turnStart=candidate.turn_start,turnLength=candidate.turn_length,end=candidate.end,physicalCutCoordinate=13/128+candidate.end,
            intendedCutRadius=.8,intendedCutSlope=-1.,intendedCutSecondDerivative=0.,modes=args.modes,workAngles=flow.work),
        acceptedSteps=accepted,rhsCalls=flow.calls,lastAccepted=last,maximumOverAcceptedStates=maxima,minimumOverAcceptedStates=minima,
        rows=rows,failure=failure,exactCoastBridge=coast_bridge,reachedPhysicalCut=bool(abs(s-candidate.end)<1e-12),
        actualDevelopedTailTwoJetMatched=False,actualPeriodicPositionDefined=True,continuousCertificate=False,
        circleCutAndNZeroNotAssumed=True,seconds=time.time()-start)
    Path(str(prefix)+'-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({key:report[key] for key in ['parameters','acceptedSteps','rhsCalls','lastAccepted','maximumOverAcceptedStates','failure','reachedPhysicalCut','seconds']}))


if __name__=='__main__':main()

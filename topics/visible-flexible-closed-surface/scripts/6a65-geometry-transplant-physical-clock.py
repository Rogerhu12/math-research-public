#!/usr/bin/env python3
"""One exact physical-clock change of the complete earlier-.14 field.

The complete geometry is unchanged. The intended meridian coefficient is
reset to one in the new physical coordinate, so this is explicitly a new g.
No model is solved here and no accepted LM step is claimed. The auxiliary
base uses the existing short factory with a changed rightLength parameter.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
earlier=load('physical_clock_earlier',HERE/'6a65-geometry-transplant-earlier-inlet.py');w=earlier.w
lengths=earlier.p.short.lengths


class Clock:
    def __init__(self,parameters,delta):
        self.b=parameters['physicalCut']-parameters['rightLength'];self.L=parameters['rightLength'];self.delta=delta
        self.old_cut=parameters['physicalCut'];self.new_cut=self.old_cut+delta
        if not delta>=0:raise ValueError('This exact clock change requires nonnegative old compression')
    def jets(self,s):
        t=float(np.clip((s-self.b)/self.L,0,1));S=float(w.S9stable(t))
        d=630*t**4*(1-t)**4;dd=2520*t**3*(1-t)**3*(1-2*t)
        return s+self.delta*S,1+self.delta*d/self.L,self.delta*dd/self.L**2
    def inverse(self,sigma):
        if sigma<=self.b:return sigma
        if sigma>=self.new_cut:return sigma-self.delta
        lo=self.b;hi=self.old_cut;s=lo+(hi-lo)*(sigma-lo)/(self.new_cut-lo)
        for _ in range(32):
            value,first,_=self.jets(s);e=value-sigma
            if abs(e)<4e-15:return s
            if e>0:hi=s
            else:lo=s
            new=s-e/first;s=new if lo<new<hi else (lo+hi)/2
        raise RuntimeError('Monotone physical clock inverse failed')
    def transform(self,q,s):
        sigma,sp,spp=self.jets(s);alpha=1/sp;ap=-spp/sp**3;out=dict(q)
        for k0,k1,k2 in [('X','Xs','Xss'),('f','fs','fss')]:
            out[k1]=alpha*q[k1];out[k2]=alpha*alpha*q[k2]+ap*q[k1]
        out['Xsu']=alpha*q['Xsu']
        if 'Xssu' in q:out['Xssu']=alpha*alpha*q['Xssu']+ap*q['Xsu']
        if 'Xsuu' in q:out['Xsuu']=alpha*q['Xsuu']
        return out


def auxiliary_scalar(s,parameters):
    c=parameters['centralLength'];ramp=parameters['rampLength'];coast=parameters['coastLength'];L=parameters['rightLength'];v=parameters['v']
    a0=parameters['fCentral'];ramp_end=c+ramp;coast_end=ramp_end+coast;cut=coast_end+L
    if s<=c:return a0,0.,0.
    if s<=ramp_end:
        t=(s-c)/ramp;J=t**6*(21+t*(-60+t*(67.5+t*(-35+7*t))))
        return a0+v*ramp*J,v*float(w.S9stable(t)),v/ramp*630*t**4*(1-t)**4
    if s<=coast_end:return a0+v*ramp/2+v*(s-ramp_end),v,0.
    if s<=cut:return lengths.turn((s-coast_end)/L,L,a0+v*ramp/2+v*coast,v)
    return .8-(s-cut),-1.,0.


class ClockedEarlierMaster:
    """Arbitrary-coordinate full-jet consumer, including the true flat cuff."""
    def __init__(self,ramp_master,coast_master,source_report,parameters,delta):
        self.original=earlier.EarlierMaster(ramp_master,coast_master,source_report,old_start=.14)
        self.clock=Clock(parameters,delta)
    def normalized(self,sigma,u,quadrature=1024):
        s=self.clock.inverse(sigma);q=self.original.normalized(s,u,quadrature)
        return self.clock.transform(q,s)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('input_samples');ap.add_argument('input_report');ap.add_argument('output_prefix')
    ap.add_argument('--report-only',action='store_true');args=ap.parse_args();start=time.time();prefix=Path(args.output_prefix)
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh output required')
    data=np.load(args.input_samples);source=json.loads(Path(args.input_report).read_text())
    digest=hashlib.sha256(Path(args.input_samples).read_bytes()).hexdigest()
    if digest!=source['outputSHA256']:raise ValueError('Actual complete input identity mismatch')
    old=source['parameters'];delta=source['transplant']['clockDelta'];clock=Clock(old,delta)
    new={**old,'rightLength':old['rightLength']+delta,'physicalCut':old['physicalCut']+delta,
         'physicalFlatCuff':old['physicalFlatCuff']+delta}
    saved={k:[] for k in data.files if k not in ['s','u','targetRho','targetRhoFirst','targetRhoSecond']}
    new_s=[];rho=[];rhos=[];rhoss=[];rows=[];curvature_error=0.;area_error=0.;metric_identity_error=0.
    for i,s in enumerate(data['s']):
        s=float(s);sigma,sp,spp=clock.jets(s);q={key:data[key][i] for key in saved};value=clock.transform(q,s)
        for key in saved:saved[key].append(value[key])
        new_s.append(sigma);aux=auxiliary_scalar(sigma,new)
        rho.append(value['f']-aux[0]);rhos.append(value['fs']-aux[1]);rhoss.append(value['fss']-aux[2])
        diag=w.ports.diagnostics(value,new['centralA']);diag['minimumRelativeArea']=diag['minimumArea']/value['f']
        old_diag=source['rows'][i]['normalized'];curvature_error=max(curvature_error,abs(diag['maximumOwnCurvature']-old_diag['maximumOwnCurvature']))
        area_error=max(area_error,abs(diag['minimumArea']-old_diag['minimumArea']/sp))
        E=np.sum(q['Xs']**2,axis=1);F=np.sum(q['Xs']*q['Xu'],axis=1)/q['f']
        En=np.sum(value['Xs']**2,axis=1);Fn=np.sum(value['Xs']*value['Xu'],axis=1)/value['f']
        metric_identity_error=max(metric_identity_error,float(np.max(abs(En-E/sp**2))),float(np.max(abs(Fn-F/sp))))
        rows.append(dict(s=sigma,sourcePhysicalS=s,clockFirst=sp,clockSecond=spp,segment=source['rows'][i]['segment'],
            normalized=diag,inverseResidual=source['rows'][i]['inverseResidual'],
            discreteUnitTClosure=source['rows'][i]['discreteUnitTClosure']))
    output_path=Path(str(prefix)+'-samples.npz')
    if not args.report_only:
        if output_path.exists():raise ValueError('Fresh array output required')
        np.savez_compressed(output_path,s=np.asarray(new_s),u=data['u'],**{k:np.asarray(v) for k,v in saved.items()},
            targetRho=np.asarray(rho),targetRhoFirst=np.asarray(rhos),targetRhoSecond=np.asarray(rhoss))
    keys=['maximumRelativeMetric','maximumOwnCurvature','maximumAbsGError','maximumRadius','maximumAbsY','maximumZ','maximumAbsProfileSlope']
    extrema={k:max(row['normalized'][k] for row in rows) for k in keys}
    for k in ['minimumHeld','minimumArea','minimumRelativeArea']:extrema[k]=min(row['normalized'][k] for row in rows)
    power,beta,target=lengths.parameters(new['fCoastEnd'],new['v'],new['rightLength'])
    report=dict(schema='6a65-complete-earlier14-exact-physical-clock-new-g-v1',parameters=new,
        clock=dict(formula='sigma=s+Delta*S9((s-coastEnd)/oldRightLength), constant extensions',
            delta=delta,oldRightLength=old['rightLength'],oldCut=old['physicalCut'],newCut=new['physicalCut'],
            minimumFirst=1.,maximumFirst=1+delta/old['rightLength']*630/256,endpointFirst=1.,endpointSecond=0.,
            angleIndependent=True,positiveGlobalDiffeomorphism=True),
        auxiliaryRoundScalarTurn=dict(power=power,beta=beta,targetIntegral=target,
            Ip=str(lengths.INTEGRALS[power]),Ip1=str(lengths.INTEGRALS[power+1]),
            factory='6a65-geometry-short-cauchy-base.cjs createShortCauchyWarmBase',
            onlyFactoryParameterChange=dict(rightLength=new['rightLength']),notClaimedEqualToOldAuxiliaryClockComposition=True),
        actualMetricDefinition='d sigma^2 + old_actual_a(s(sigma))^2 du^2; this changes g',
        completeTwoJetTransform='Xs/sp; Xss/sp^2-spp*Xs/sp^3; Xsu/sp; fs/sp; fss/sp^2-spp*fs/sp^3',
        sourceArraysUnchanged=['X','Xu','Xuu','rawX','rawXu','mean','unitT'],
        exactCutAndFlatCuffTwoJetsPreserved=True,sameWholeGeometricImage=True,
        maximumRowCurvatureInvariantError=curvature_error,maximumAreaScalingIdentityError=area_error,
        maximumMetricTransformationIdentityError=metric_identity_error,
        maximumAbsoluteTargetRho=float(np.max(np.abs(rho))),normalizedExtrema=extrema,rows=rows,
        angles=source['angles'],quadrature=source['quadrature'],maximumDiscreteUnitTClosure=source['maximumDiscreteUnitTClosure'],
        sourceSamplesSHA256=digest,sourceReportSHA256=hashlib.sha256(Path(args.input_report).read_bytes()).hexdigest(),
        outputSHA256=None if args.report_only else hashlib.sha256(output_path.read_bytes()).hexdigest(),
        scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),acceptedOptimizationSteps=0,
        actualMetricRequiresCompleteRhoInitialization=True,newPhysicalMetricDesign=True,continuousCertificate=False,
        wholeClosedReachCertified=False,seconds=time.time()-start)
    Path(str(prefix)+'-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['parameters','clock','auxiliaryRoundScalarTurn','normalizedExtrema',
        'maximumRowCurvatureInvariantError','maximumAreaScalingIdentityError','maximumMetricTransformationIdentityError',
        'maximumAbsoluteTargetRho','outputSHA256','seconds']}),flush=True)


if __name__=='__main__':main()

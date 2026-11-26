#!/usr/bin/env python3
"""NEW g from the actual transplanted right curves' complete perimeters.

No radial homothety is used on the right. Full angular arclength reparameter-
ization preserves its geometric surface and true two-jet ports. The auxiliary
short round reference remains available; its difference from this actual g
must be fitted into all rho columns, not silently initialized to zero.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('perimeter_short_transplant',HERE/'6a65-geometry-short-cauchy-transplant.py')
short=importlib.util.module_from_spec(spec);sys.modules[spec.name]=short;spec.loader.exec_module(short)
w=short.w


class PerimeterMaster(short.ShortMaster):
    def normalized(self,s,u,quadrature=1024):
        if s<=self.coast_end or s>=self.cut-1e-13:return super().normalized(s,u,quadrature)
        u=np.asarray(u,float).reshape(-1);ug=2*np.pi*np.arange(quadrature)/quadrature;q=self.jet(s,ug)
        h=np.linalg.norm(q['Xu'],axis=1)
        if np.min(h)<=1e-6:raise ValueError('Actual angular curve is not regular')
        hs=np.einsum('ij,ij->i',q['Xu'],q['Xsu'])/h
        hss=(np.sum(q['Xsu']**2,axis=1)+np.einsum('ij,ij->i',q['Xu'],q['Xssu']))/h-hs**2/h
        a,as_,ass=np.mean(h),np.mean(hs),np.mean(hss)
        wave=np.fft.fftfreq(quadrature,1/quadrature);co=np.fft.fft(np.stack((h,hs,hss),axis=1),axis=0)/quadrature
        nz=wave!=0;weights=co[nz]/(1j*wave[nz,None]);mom=np.asarray([a,as_,ass])
        def primitive(v):return (v[:,None]*mom+(np.exp(1j*v[:,None]*wave[nz])-1)@weights).real
        v=u.copy()
        for iteration in range(9):
            I=primitive(v);raw=self.jet(s,v);hv=np.linalg.norm(raw['Xu'],axis=1);residual=I[:,0]-u*a
            if np.max(np.abs(residual))<5e-13:break
            v=np.clip(v-residual/hv,0,2*np.pi)
        else:raise RuntimeError('Actual perimeter angular inverse failed')
        X,S,U,SS,SU,UU=(raw[k] for k in ['X','Xs','Xu','Xss','Xsu','Xuu'])
        hsv=np.einsum('ij,ij->i',U,SU)/hv;hu=np.einsum('ij,ij->i',U,UU)/hv
        vs=(u*as_-I[:,1])/hv;vss=(u*ass-I[:,2]-2*hsv*vs-hu*vs**2)/hv
        vu=a/hv;vuu=-a*a*hu/hv**3;vsu=(as_-(hsv+hu*vs)*vu)/hv
        return dict(X=X,Xs=S+U*vs[:,None],Xss=SS+2*SU*vs[:,None]+UU*vs[:,None]**2+U*vss[:,None],
            Xu=U*vu[:,None],Xsu=(SU+UU*vs[:,None])*vu[:,None]+U*vsu[:,None],
            Xuu=UU*vu[:,None]**2+U*vuu[:,None],f=float(a),fs=float(as_),fss=float(ass),segment='right_perimeter_metric',
            normalizationScale=1.,rawAverageRadius=float(a),mean=np.mean(q['X']*h[:,None],axis=0)/a,
            materialInverseResidual=float(np.max(np.abs(residual))),exactPieceBypass=False,unitT=U/hv[:,None],
            auxiliaryRoundRadius=q['f'],auxiliaryRoundRadiusFirst=q['fs'],auxiliaryRoundRadiusSecond=q['fss'])


def main():
    ap=argparse.ArgumentParser();ap.add_argument('ramp_master');ap.add_argument('coast_master');ap.add_argument('old_report')
    ap.add_argument('short_samples');ap.add_argument('short_report');ap.add_argument('output_prefix');args=ap.parse_args();start=time.time()
    prefix=Path(args.output_prefix)
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh output required')
    previous=np.load(args.short_samples);report=json.loads(Path(args.short_report).read_text())
    if hashlib.sha256(Path(args.short_samples).read_bytes()).hexdigest()!=report['outputSHA256']:raise ValueError('Fixed-piece input identity mismatch')
    m=PerimeterMaster(args.ramp_master,args.coast_master,args.old_report);u=previous['u'];rows=[]
    saved={key:[] for key in previous.files if key not in ['s','u']};rho=[];rhos=[];rhoss=[]
    for j,s in enumerate(previous['s']):
        s=float(s)
        if s<=m.coast_end or s>=m.cut-1e-13:
            rows.append(report['rows'][j]);rho.append(0.);rhos.append(0.);rhoss.append(0.)
            for key in saved:saved[key].append(previous[key][j])
            continue
        raw=m.jet(s,u);norm=m.normalized(s,u,report['quadrature'])
        radius=m.scalar(s);rho.append(norm['f']-radius[0]);rhos.append(norm['fs']-radius[1]);rhoss.append(norm['fss']-radius[2])
        raw.update(f=norm['f'],fs=norm['fs'],fss=norm['fss'])
        rd=w.ports.diagnostics(raw,m.A);nd=w.ports.diagnostics(norm,m.A);nd['minimumRelativeArea']=nd['minimumArea']/norm['f']
        for key in saved:saved[key].append(raw['X'] if key=='rawX' else raw['Xu'] if key=='rawXu' else norm[key])
        rows.append(dict(s=s,segment=norm['segment'],raw=rd,normalized=nd,scale=1.,
            inverseResidual=norm['materialInverseResidual'],discreteUnitTClosure=float(np.linalg.norm(np.mean(norm['unitT'],axis=0)))))
        if j%10==0:print(json.dumps(dict(node=j,total=len(previous['s']),s=s,metric=nd['maximumRelativeMetric'],
            curvature=nd['maximumOwnCurvature'],relativeArea=nd['minimumRelativeArea'],rho=rho[-1])),flush=True)
    sample=Path(str(prefix)+'-samples.npz');np.savez_compressed(sample,s=previous['s'],u=u,**{key:np.asarray(value) for key,value in saved.items()},
        targetRho=np.asarray(rho),targetRhoFirst=np.asarray(rhos),targetRhoSecond=np.asarray(rhoss))
    keys=['maximumRelativeMetric','maximumOwnCurvature','maximumAbsGError','maximumRadius','maximumAbsY','maximumZ','maximumAbsProfileSlope']
    extrema={key:max(row['normalized'][key] for row in rows) for key in keys}
    for key in ['minimumHeld','minimumArea','minimumRelativeArea']:extrema[key]=min(row['normalized'][key] for row in rows)
    out=dict(schema='6a65-new-true-perimeter-metric-short-Cauchy-strong-transplant-v1',
        parameters=report['parameters'],auxiliaryRoundScalarTurn=report['scalarTurn'],transplant=report['transplant'],
        actualMetricDefinition='prefix original short profile; right a(s)=(2*pi)^(-1)*integral|raw X_u(s,u)|du; exact R205 tail',
        actualMetricRequiresCompleteRhoInitialization=True,rotationReferenceOnlyAuxiliary=True,
        maximumAbsoluteTargetRho=float(np.max(np.abs(rho))),maximumAbsoluteTargetRhoFirst=float(np.max(np.abs(rhos))),
        normalizedExtrema=extrema,rows=rows,angles=len(u),quadrature=report['quadrature'],
        maximumDiscreteUnitTClosure=max(row['discreteUnitTClosure'] for row in rows),
        outputSHA256=hashlib.sha256(sample.read_bytes()).hexdigest(),scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        shortSamplesSHA256=report['outputSHA256'],sourceReportSHA256=report['sourceReportSHA256'],
        newPhysicalMetricDesign=True,geometryOfRawRightMapUnchangedByReparameterization=True,
        acceptedOptimizationSteps=0,continuousCertificate=False,wholeClosedReachCertified=False,seconds=time.time()-start)
    Path(str(prefix)+'-report.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({key:out[key] for key in ['normalizedExtrema','maximumAbsoluteTargetRho','maximumAbsoluteTargetRhoFirst',
        'outputSHA256','seconds']}),flush=True)


if __name__=='__main__':main()

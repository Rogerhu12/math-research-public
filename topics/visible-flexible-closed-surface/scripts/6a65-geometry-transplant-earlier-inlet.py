#!/usr/bin/env python3
"""One declared earlier-inlet alternative, selected from actual two-jet probes.

The actual Cauchy prefix, tail amplitude, cuff height and auxiliary short base
stay fixed. The earlier old-source port, its monotone clock, height correction,
and the natural perimeter metric are rebuilt completely. No scan or LM occurs.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('earlier_inlet_perimeter',HERE/'6a65-geometry-transplant-perimeter-metric.py')
p=importlib.util.module_from_spec(spec);sys.modules[spec.name]=p;spec.loader.exec_module(p);w=p.w


class EarlierMaster(p.PerimeterMaster):
    def __init__(self,ramp_master,coast_master,old_report,*,old_start=.14):
        super().__init__(ramp_master,coast_master,old_report)
        if not self.old.s[0]<=old_start<self.old.end:raise ValueError('Earlier source port outside actual archive')
        self.old_start=old_start;self.clock_delta=self.old.end-old_start-self.L
        self.clock_min=1+min(0,self.clock_delta/self.L)*630/256
        if self.clock_min<=0:raise ValueError('New physical clock is not increasing')
        ug=2*np.pi*np.arange(1024)/1024
        self.dz=float(np.mean(self.coast_port(self.coast,ug)['P'][:,2])-np.mean(self.old.jet(old_start,ug)['X'][:,2]))
        self.correction_cache=None


def main():
    ap=argparse.ArgumentParser();ap.add_argument('ramp_master');ap.add_argument('coast_master');ap.add_argument('old_report')
    ap.add_argument('short_samples');ap.add_argument('short_report');ap.add_argument('output_prefix')
    ap.add_argument('--old-start',type=float,default=.14);args=ap.parse_args();start=time.time();prefix=Path(args.output_prefix)
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh output required')
    previous=np.load(args.short_samples);report=json.loads(Path(args.short_report).read_text())
    if hashlib.sha256(Path(args.short_samples).read_bytes()).hexdigest()!=report['outputSHA256']:raise ValueError('Fixed-piece identity mismatch')
    m=EarlierMaster(args.ramp_master,args.coast_master,args.old_report,old_start=args.old_start);u=previous['u'];rows=[]
    saved={key:[] for key in previous.files if key not in ['s','u']};rho=[];rhos=[];rhoss=[]
    for j,s in enumerate(previous['s']):
        s=float(s)
        if s<=m.coast_end or s>=m.cut-1e-13:
            rows.append(report['rows'][j]);rho.append(0.);rhos.append(0.);rhoss.append(0.)
            for key in saved:saved[key].append(previous[key][j])
            continue
        raw=m.jet(s,u);norm=m.normalized(s,u,report['quadrature']);radius=m.scalar(s)
        rho.append(norm['f']-radius[0]);rhos.append(norm['fs']-radius[1]);rhoss.append(norm['fss']-radius[2])
        raw.update(f=norm['f'],fs=norm['fs'],fss=norm['fss']);rd=w.ports.diagnostics(raw,m.A);nd=w.ports.diagnostics(norm,m.A)
        nd['minimumRelativeArea']=nd['minimumArea']/norm['f']
        for key in saved:saved[key].append(raw['X'] if key=='rawX' else raw['Xu'] if key=='rawXu' else norm[key])
        rows.append(dict(s=s,segment=norm['segment'],raw=rd,normalized=nd,scale=1.,
            inverseResidual=norm['materialInverseResidual'],discreteUnitTClosure=float(np.linalg.norm(np.mean(norm['unitT'],axis=0)))))
        if j%10==0:print(json.dumps(dict(node=j,s=s,metric=nd['maximumRelativeMetric'],curvature=nd['maximumOwnCurvature'],
            minRelativeArea=nd['minimumRelativeArea'],rho=rho[-1])),flush=True)
    sample=Path(str(prefix)+'-samples.npz');np.savez_compressed(sample,s=previous['s'],u=u,
        **{key:np.asarray(value) for key,value in saved.items()},targetRho=np.asarray(rho),targetRhoFirst=np.asarray(rhos),targetRhoSecond=np.asarray(rhoss))
    keys=['maximumRelativeMetric','maximumOwnCurvature','maximumAbsGError','maximumRadius','maximumAbsY','maximumZ','maximumAbsProfileSlope']
    extrema={key:max(row['normalized'][key] for row in rows) for key in keys}
    for key in ['minimumHeld','minimumArea','minimumRelativeArea']:extrema[key]=min(row['normalized'][key] for row in rows)
    correction=m.correction(u)[0];dc={key:float(np.max(np.linalg.norm(correction[key],axis=1))) for key in ['P','V','A','Pu','Vu','Puu']}
    out=dict(schema='6a65-one-actual-earlier-source-port-natural-metric-baseline-v1',parameters=report['parameters'],
        auxiliaryRoundScalarTurn=report['scalarTurn'],transplant=dict(oldStart=m.old_start,oldCut=m.old.end,blendLength=m.blend,
            meanHeightShift=m.dz,clockDelta=m.clock_delta,clockMinimumDerivative=m.clock_min,
            clockMaximumDerivative=1+max(0,m.clock_delta/m.L)*630/256,inletCorrectionTwoJets=dc),
        actualMetricDefinition='actual raw right perimeter; same fixed true short prefix and R205 tail',
        actualMetricRequiresCompleteRhoInitialization=True,maximumAbsoluteTargetRho=float(np.max(np.abs(rho))),
        normalizedExtrema=extrema,rows=rows,angles=len(u),quadrature=report['quadrature'],
        maximumDiscreteUnitTClosure=max(row['discreteUnitTClosure'] for row in rows),
        outputSHA256=hashlib.sha256(sample.read_bytes()).hexdigest(),scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        shortSamplesSHA256=report['outputSHA256'],sourceReportSHA256=hashlib.sha256(Path(args.old_report).read_bytes()).hexdigest(),
        newPositionAndMetricDesign=True,acceptedOptimizationSteps=0,continuousCertificate=False,wholeClosedReachCertified=False,seconds=time.time()-start)
    Path(str(prefix)+'-report.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({key:out[key] for key in ['transplant','normalizedExtrema','maximumAbsoluteTargetRho','outputSHA256','seconds']}),flush=True)


if __name__=='__main__':main()

#!/usr/bin/env python3
"""New short true Cauchy prefix with the complete retargeted R219 back half.

The new scalar metric is explicitly different: ramp .06, final slope .05,
coast .02, and a .75 turn paid by adjacent exact powers of S9. Old long-prefix
masters, factories, and samples are untouched. Collect and export are actual
computations; raw arrays are written only to caller-selected scratch paths.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
t=load('short_cauchy_transplant',HERE/'6a65-geometry-cauchy-strong-transplant.py');w=t.w
lengths=load('short_cauchy_scalar_turn',HERE/'6a65-geometry-cauchy-right-length-baselines.py')


class ShortMaster(t.TransplantMaster):
    def __init__(self,ramp_master,coast_master,old_report,**options):
        super().__init__(ramp_master,coast_master,old_report,coast_length=.02,old_start=.18,blend_length=.16,**options)
    def scalar(self,s):
        if self.coast_end<s<=self.cut:
            return *lengths.turn((s-self.coast_end)/self.L,self.L,self.curve.a+self.v*self.coast,self.v),'right_connector'
        return super().scalar(s)


def collect(source,prefix):
    start=time.time();ramp=.06;v=.05;coast=.02;degree=95
    path=w.collect_ramp(source,prefix,ramp=ramp,v=v,modes=191,nodes=17)
    d=np.load(path);co=d['coefficients'][-1,:,0,:];points=np.fft.ifft(co,axis=0).real*len(co)
    curve=w.core.Curve(points,degree);target=float(d['a0'])+v*ramp/2
    coastfile=Path(str(prefix)+'-coast-master.npz')
    if coastfile.exists():raise ValueError('Fresh coast output required')
    np.savez_compressed(coastfile,curve_modes=curve.modes,curve_coefficients=curve.coeff,
        unnormalized_radius=curve.a,exact_target_radius=target,v=v,length=coast,degree=degree)
    fixed=w.tail.fixed_module.FixedRadiusCurve(curve,target);u=2*np.pi*np.arange(512)/512
    out=w.core.at_material(target,v,coast,u,lambda x:fixed.inlet(x,v))
    report=dict(schema='6a65-new-short-real-Cauchy-ramp-and-explicit-R137-master-v1',
        rampLength=ramp,v=v,coastLength=coast,degree=degree,targetRadius=target,
        exactArcNormalizationScale=fixed.normalization,coastMinimumD=float(np.min(out['D'])),
        coastMinimumMaterialDerivative=float(np.min(out['U_t'])),coastMetricMaximum=float(np.max(out['metric'])),
        coastCurvatureMaximum=float(np.max(out['actual_curvature'])),
        rampMasterSHA256=hashlib.sha256(path.read_bytes()).hexdigest(),coastMasterSHA256=hashlib.sha256(coastfile.read_bytes()).hexdigest(),
        sourceSHA256=hashlib.sha256(Path(source).read_bytes()).hexdigest(),scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        CauchyToExactCoastTwoJetsRequireExplicitLastCellRepair=True,continuousCertificate=False,seconds=time.time()-start)
    Path(str(prefix)+'-collect-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report),flush=True)


def export(args):
    start=time.time();prefix=Path(args.output_prefix)
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh output prefix required')
    m=ShortMaster(args.ramp_master,args.coast_master,args.old_report)
    sx=np.unique(np.r_[np.linspace(0,m.c,5),m.c+m.sx,m.c+(m.sx[:-1]+m.sx[1:])/2,
        m.ramp_end+np.linspace(0,m.coast,5),m.coast_end+np.linspace(0,m.L,49),m.coast_end+m.blend,
        m.cut+np.array([0,.1,.2,.3,.4,.46,.48])])
    u=2*np.pi*np.arange(args.angles)/args.angles;rows=[]
    saved={k:[] for k in ['rawX','rawXu','X','Xs','Xu','Xss','Xsu','Xuu','unitT','mean','f','fs','fss']}
    for j,s in enumerate(sx):
        raw=m.jet(float(s),u);norm=m.normalized(float(s),u,args.quadrature)
        rd=w.ports.diagnostics(raw,m.A);nd=w.ports.diagnostics(norm,m.A)
        nd['minimumRelativeArea']=nd['minimumArea']/norm['f']
        for key in saved:saved[key].append(raw['X'] if key=='rawX' else raw['Xu'] if key=='rawXu' else norm[key])
        rows.append(dict(s=float(s),segment=norm['segment'],raw=rd,normalized=nd,scale=norm['normalizationScale'],
            inverseResidual=norm['materialInverseResidual'],discreteUnitTClosure=float(np.linalg.norm(np.mean(norm['unitT'],axis=0)))))
        if j%10==0 or j==len(sx)-1:print(json.dumps(dict(node=j,total=len(sx),s=float(s),segment=norm['segment'],
            metric=nd['maximumRelativeMetric'],curvature=nd['maximumOwnCurvature'],relativeArea=nd['minimumRelativeArea'],zmax=nd['maximumZ'])),flush=True)
    sample=Path(str(prefix)+'-samples.npz');np.savez_compressed(sample,s=sx,u=u,**{key:np.asarray(value) for key,value in saved.items()})
    keys=['maximumRelativeMetric','maximumOwnCurvature','maximumAbsGError','maximumRadius','maximumAbsY','maximumZ','maximumAbsProfileSlope']
    extrema={key:max(row['normalized'][key] for row in rows) for key in keys}
    for key in ['minimumHeld','minimumArea','minimumRelativeArea']:extrema[key]=min(row['normalized'][key] for row in rows)
    raw_ramp=m.ramp_port(len(m.sx)-1,u,repair=False);exact_ramp=m.coast_port(0.,u)
    repair={key:float(np.max(np.linalg.norm(raw_ramp[key]-exact_ramp[key],axis=1))) for key in ['P','V','A','Pu','Vu','Puu']}
    correction=m.correction(u)[0];dc={key:float(np.max(np.linalg.norm(correction[key],axis=1))) for key in ['P','V','A','Pu','Vu','Puu']}
    power,beta,target=lengths.parameters(m.curve.a+m.v*m.coast,m.v,m.L)
    report=dict(schema='6a65-new-short-Cauchy-accurate-prefix-to-strong-transplant-full-baseline-v1',
        parameters=dict(centralLength=m.c,rampLength=m.ramp,coastLength=m.coast,rightLength=m.L,v=m.v,
            physicalCut=m.cut,physicalFlatCuff=m.cuff,A=m.amplitude,Z=m.Z,centralA=m.A,centralB=m.B,
            fCentral=m.central.a,fRampEnd=m.curve.a,fCoastEnd=m.curve.a+m.v*m.coast,fCut=.8,fCuff=.32),
        scalarTurn=dict(power=power,beta=beta,targetIntegral=target,Ip=str(lengths.INTEGRALS[power]),Ip1=str(lengths.INTEGRALS[power+1]),
            formula="f'=v-(1+v)*((1-beta)*S9^power+beta*S9^(power+1)); integrate to fCut=.8",quadratureOrder=40),
        transplant=dict(oldStart=m.old_start,oldCut=m.old.end,blendLength=m.blend,meanHeightShift=m.dz,
            clockDelta=m.clock_delta,clockMinimumDerivative=m.clock_min,inletCorrectionTwoJets=dc),
        repairedLastRampCell=dict(length=float(m.sx[-1]-m.sx[-2]),oldToExactPortTwoJetDifference=repair),
        normalizedExtrema=extrema,rows=rows,angles=args.angles,quadrature=args.quadrature,
        maximumDiscreteUnitTClosure=max(row['discreteUnitTClosure'] for row in rows),
        outputSHA256=hashlib.sha256(sample.read_bytes()).hexdigest(),scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        sourceReportSHA256=hashlib.sha256(Path(args.old_report).read_bytes()).hexdigest(),
        rampMasterSHA256=hashlib.sha256(Path(args.ramp_master).read_bytes()).hexdigest(),coastMasterSHA256=hashlib.sha256(Path(args.coast_master).read_bytes()).hexdigest(),
        acceptedOptimizationSteps=0,newPhysicalMetricDesign=True,continuousCertificate=False,wholeClosedReachCertified=False,seconds=time.time()-start)
    Path(str(prefix)+'-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ['parameters','scalarTurn','transplant','repairedLastRampCell','normalizedExtrema','outputSHA256','seconds']}),flush=True)


def main():
    ap=argparse.ArgumentParser();sub=ap.add_subparsers(dest='command',required=True)
    col=sub.add_parser('collect');col.add_argument('source');col.add_argument('output_prefix')
    ex=sub.add_parser('export');ex.add_argument('ramp_master');ex.add_argument('coast_master');ex.add_argument('old_report');ex.add_argument('output_prefix')
    ex.add_argument('--angles',type=int,default=128);ex.add_argument('--quadrature',type=int,default=1024)
    args=ap.parse_args()
    if args.command=='collect':collect(args.source,args.output_prefix)
    else:export(args)


if __name__=='__main__':main()

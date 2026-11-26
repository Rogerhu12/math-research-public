#!/usr/bin/env python3
"""Three explicitly new right-connector designs; no nonlinear solve or old-g claim.

Keeps the actual Cauchy/R137 inlet, R205 cut/cuff, A and Z. Only the right
physical length and its explicit smooth slope profile change. Existing fixed
prefix/tail tables are reused because their functions are identically equal;
every new right segment is consumed with full normalized Cartesian jets.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
from fractions import Fraction
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('new_right_length_warm',HERE/'6a65-geometry-cauchy-unit-t-warm.py')
w=importlib.util.module_from_spec(spec);sys.modules[spec.name]=w;spec.loader.exec_module(w)

INTEGRALS={1:Fraction(1,2),2:Fraction(38251,92378),3:Fraction(17141,46189),
    4:Fraction(376009639,1094020070),5:Fraction(11451340856,35336848261),
    6:Fraction(3307149308705467,10702515099241394),
    7:Fraction(46079328383180761,155186468939000213),
    8:Fraction(3008062272705324698929883,10483830270076968893338822)}


def parameters(f0,v,L,fc=.8):
    target=(v-(fc-f0)/L)/(1+v)
    for power in range(1,8):
        upper,lower=float(INTEGRALS[power]),float(INTEGRALS[power+1])
        if lower<=target<=upper:return power,(target-upper)/(lower-upper),target
    raise ValueError('Specified new length has no declared adjacent-power mixture')


def turn(t,L,f0,v):
    power,beta,target=parameters(f0,v,L);t=float(np.clip(t,0,1));S=float(w.S9stable(t))
    q=(1-beta)*S**power+beta*S**(power+1)
    dq=((1-beta)*power*S**(power-1)+beta*(power+1)*S**power)*630*t**4*(1-t)**4
    gx,gw=np.polynomial.legendre.leggauss(40);gx=(gx+1)/2;gw=gw/2
    def complement(x):
        y=1-x;small=y**5*(126+y*(-420+y*(540+y*(-315+70*y))));z=1-small
        return small*((1-beta)*sum(z**j for j in range(power))+beta*sum(z**j for j in range(power+1)))
    if t<=.5:
        Sq=w.S9stable(t*gx);integ=t*np.sum(((1-beta)*Sq**power+beta*Sq**(power+1))*gw)
        f=f0+L*(v*t-(1+v)*integ);fs=v-(1+v)*q
    else:
        integ=(1-t)*np.sum(complement(t+(1-t)*gx)*gw)
        f=.8+L*(1-t)-L*(1+v)*integ;fs=-1+(1+v)*complement(t)
    return float(f),float(fs),float(-(1+v)/L*dq)


class LengthMaster(w.WarmMaster):
    def scalar(self,s):
        if self.coast_end<s<=self.cut:
            return *turn((s-self.coast_end)/self.L,self.L,self.curve.a+self.v*self.coast,self.v),'right_connector'
        return super().scalar(s)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('ramp_master');ap.add_argument('coast_master')
    ap.add_argument('old_full_samples');ap.add_argument('old_full_report');ap.add_argument('output_prefix')
    ap.add_argument('--lengths',nargs='+',type=float,default=[.8,.95,1.]);args=ap.parse_args();start=time.time()
    old=np.load(args.old_full_samples);old_report=json.loads(Path(args.old_full_report).read_text());op=old_report['parameters']
    if hashlib.sha256(Path(args.old_full_samples).read_bytes()).hexdigest()!=old_report['outputSHA256']:raise ValueError('Old complete fixed-piece identity mismatch')
    all_reports=[]
    for L in args.lengths:
        prefix=Path(args.output_prefix+f'-L{round(1000*L):04d}')
        if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh per-length outputs required')
        case_start=time.time();m=LengthMaster(args.ramp_master,args.coast_master,amplitude=op['A'],Z=op['Z'],right_length=L)
        power,beta,target=parameters(m.curve.a+m.v*m.coast,m.v,L)
        u=old['u'];rows=[];saved={key:[] for key in old.files if key not in ['s','u']};sx=[]
        for j,s in enumerate(old['s']):
            if s>=m.coast_end-1e-13:break
            sx.append(float(s));rows.append(old_report['rows'][j])
            for key in saved:saved[key].append(old[key][j])
        for j,s in enumerate(m.coast_end+L*np.linspace(0,1,33)):
            raw=m.jet(float(s),u);norm=m.normalized(float(s),u,old_report['quadrature'])
            rd=w.ports.diagnostics(raw,m.A);nd=w.ports.diagnostics(norm,m.A)
            for key in saved:saved[key].append(raw['X'] if key=='rawX' else raw['Xu'] if key=='rawXu' else norm[key])
            sx.append(float(s));rows.append(dict(s=float(s),segment=norm['segment'],raw=rd,normalized=nd,scale=norm['normalizationScale'],
                inverseResidual=norm['materialInverseResidual'],discreteUnitTClosure=float(np.linalg.norm(np.mean(norm['unitT'],axis=0)))))
            if j%8==0:print(json.dumps(dict(L=L,power=power,beta=beta,rightNode=j,s=float(s),metric=nd['maximumRelativeMetric'],curvature=nd['maximumOwnCurvature'],zmax=nd['maximumZ'])),flush=True)
        for j,s in enumerate(old['s']):
            if s<=op['physicalCut']+1e-13:continue
            news=float(s+L-op['rightLength']);sx.append(news);row=dict(old_report['rows'][j]);row['s']=news;rows.append(row)
            for key in saved:saved[key].append(old[key][j])
        sample_path=Path(str(prefix)+'-samples.npz');np.savez_compressed(sample_path,s=np.asarray(sx),u=u,**{key:np.asarray(value) for key,value in saved.items()})
        keys=['maximumRelativeMetric','maximumOwnCurvature','maximumAbsGError','maximumRadius','maximumAbsY','maximumZ','maximumAbsProfileSlope']
        extrema={key:max(row['normalized'][key] for row in rows) for key in keys}
        extrema['minimumHeld']=min(row['normalized']['minimumHeld'] for row in rows)
        extrema['minimumArea']=min(row['normalized']['minimumArea'] for row in rows)
        report=dict(schema='6a65-new-complete-right-length-normalized-baseline-v1',
            parameters={**op,'rightLength':L,'physicalCut':m.cut,'physicalFlatCuff':m.cuff},
            scalarTurn=dict(power=power,beta=beta,targetIntegral=target,Ip=str(INTEGRALS[power]),Ip1=str(INTEGRALS[power+1]),
                formula="f'=v-(1+v)*((1-beta)*S9^power+beta*S9^(power+1)); integrate to fCut=.8",quadratureOrder=40,
                allEndpointSlopeDerivativesThroughOrder4Zero=True),
            normalizedExtrema=extrema,rows=rows,angles=len(u),quadrature=old_report['quadrature'],
            inheritedFixedPieceSampleSHA256=old_report['outputSHA256'],fixedPrefixAndTailExactlyUnchanged=True,
            outputSHA256=hashlib.sha256(sample_path.read_bytes()).hexdigest(),scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            acceptedOptimizationSteps=0,newPhysicalMetricDesign=True,continuousCertificate=False,seconds=time.time()-case_start)
        Path(str(prefix)+'-report.json').write_text(json.dumps(report,indent=2)+'\n');all_reports.append({key:report[key] for key in ['parameters','scalarTurn','normalizedExtrema','outputSHA256','seconds']})
        print(json.dumps(all_reports[-1]),flush=True)
    Path(args.output_prefix+'-summary.json').write_text(json.dumps(dict(cases=all_reports,seconds=time.time()-start),indent=2)+'\n')


if __name__=='__main__':main()

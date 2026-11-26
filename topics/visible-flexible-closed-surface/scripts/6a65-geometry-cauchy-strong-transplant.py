#!/usr/bin/env python3
"""C2 source transplant: actual Cauchy/R137 prefix and a full old R219 back half.

The old field is explicitly retargeted in A/Z, sampled as Cartesian full jets,
then represented by one Fourier/quintic-Hermite map. An endpoint-flat monotone
physical clock and a C2 two-jet correction join the new exact-form coast.
The whole new raw map is normalized by the existing exact arclength definition
to the current L=.75 metric. No interpolation or quadrature certificate is
claimed. All arrays/reports go outside git; current warm02/base stay unchanged.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('strong_transplant_warm',HERE/'6a65-geometry-cauchy-unit-t-warm.py')
w=importlib.util.module_from_spec(spec);sys.modules[spec.name]=w;spec.loader.exec_module(w)


def smooth_twojet(t):
    if t<=0:return 0.,0.,0.
    if t>=1:return 1.,0.,0.
    return float(w.S9stable(t)),630*t**4*(1-t)**4,2520*t**3*(1-t)**3*(1-2*t)


class OldArchive:
    def __init__(self,report_file):
        self.report=json.loads(Path(report_file).read_text());r=self.report
        if hashlib.sha256(Path(r['dataFile']).read_bytes()).hexdigest()!=r['dataSHA256']:raise ValueError('Source data identity mismatch')
        raw=np.fromfile(r['dataFile'],dtype='<f8').reshape(r['shape'])
        self.s=np.asarray(r['nodes']);self.f=np.asarray([row['a'] for row in r['rows']]);self.count=r['count']
        self.coeff=np.fft.fft(raw[:,:,:3,:],axis=1)/self.count
        # A real finite Fourier curve uses no unpaired Nyquist mode.
        self.coeff[:,self.count//2]=0
        self.wave=np.fft.fftfreq(self.count,1/self.count)
        self.amplitude=r['sourceChange']['A'];self.Z=r['sourceChange']['Z'];self.end=r['baseEnd']
        self.phase_cache=None;self.cached_ports={}
        # Compare native derivative data against derivatives of the SAME curve.
        d1=np.fft.ifft(self.coeff*(1j*self.wave[None,:,None,None]),axis=1).real*self.count
        d2=np.fft.ifft(self.coeff*(-self.wave[None,:,None,None]**2),axis=1).real*self.count
        val=np.fft.ifft(self.coeff,axis=1).real*self.count
        self.projection={key:float(np.max(np.linalg.norm(a-b,axis=-1))) for key,a,b in [
            ('X',val[:,:,0],raw[:,:,0]),('Xs',val[:,:,1],raw[:,:,1]),('Xss',val[:,:,2],raw[:,:,2]),
            ('Xu',d1[:,:,0],raw[:,:,3]),('Xsu',d1[:,:,1],raw[:,:,4]),('Xuu',d2[:,:,0],raw[:,:,5])]}
    def phase(self,u):
        key=np.asarray(u).tobytes()
        if self.phase_cache is None or self.phase_cache[0]!=key:self.phase_cache=(key,np.exp(1j*np.asarray(u)[:,None]*self.wave))
        return self.phase_cache[1]
    def port(self,index,u,repair=True):
        if repair and index==len(self.s)-1:return w.developed_tail_port(self.amplitude,self.Z,u,.8)
        phase=self.phase(u);co=self.coeff[index]
        val=np.einsum('uk,kcj->ucj',phase,co).real
        du=np.einsum('uk,kcj->ucj',phase,co*(1j*self.wave[:,None,None])).real
        duu=np.einsum('uk,kcj->ucj',phase,co*(-self.wave[:,None,None]**2)).real
        return dict(P=val[:,0],V=val[:,1],A=val[:,2],Pu=du[:,0],Vu=du[:,1],Au=du[:,2],
            Puu=duu[:,0],Vuu=duu[:,1],Auu=duu[:,2],f=float(self.f[index]),fs=0.,fss=0.)
    def jet(self,s,u):
        if s<self.s[0]-1e-13 or s>self.s[-1]+1e-13:raise ValueError('Old source clock leaves archived field')
        if s>=self.s[-1]:return w.packet_from_port(self.port(len(self.s)-1,u))
        i=min(len(self.s)-2,max(0,np.searchsorted(self.s,s,side='right')-1));L=self.s[i+1]-self.s[i]
        return w.connector((s-self.s[i])/L,L,self.port(i,u),self.port(i+1,u))


class TransplantMaster(w.WarmMaster):
    def __init__(self,ramp_master,coast_master,old_report,*,old_start=.22,blend_length=.22,height_shift=True,**options):
        super().__init__(ramp_master,coast_master,**options);self.old=OldArchive(old_report)
        if self.amplitude!=self.old.amplitude or self.Z!=self.old.Z:raise ValueError('Actual same R205 A/Z required')
        self.old_start=old_start;self.blend=blend_length;self.clock_delta=self.old.end-old_start-self.L
        self.clock_min=1+min(0,self.clock_delta/self.L)*630/256
        if self.clock_min<=0 or old_start<self.old.s[0] or not 0<self.blend<=self.L:raise ValueError('Positive clock and interior blend required')
        ug=2*np.pi*np.arange(1024)/1024
        self.dz=float(np.mean(self.coast_port(self.coast,ug)['P'][:,2])-np.mean(self.old.jet(old_start,ug)['X'][:,2])) if height_shift else 0.
        self.correction_cache=None
    def clock(self,x):
        h,hp,hpp=smooth_twojet(x/self.L)
        return self.old_start+x+self.clock_delta*h,1+self.clock_delta*hp/self.L,self.clock_delta*hpp/self.L**2
    def old_clock_jet(self,x,u):
        tau,tp,tpp=self.clock(x);raw=self.old.jet(tau,u)
        out={**raw,'Xs':tp*raw['Xs'],'Xss':tp*tp*raw['Xss']+tpp*raw['Xs'],
             'Xsu':tp*raw['Xsu'],'Xssu':tp*tp*raw['Xssu']+tpp*raw['Xsu'],'Xsuu':tp*raw['Xsuu']}
        h,hp,hpp=smooth_twojet(x/self.L)
        for key,inc in [('X',self.dz*(1-h)),('Xs',-self.dz*hp/self.L),('Xss',-self.dz*hpp/self.L**2)]:
            out[key]=out[key].copy();out[key][:,2]+=inc
        return out
    def correction(self,u):
        key=np.asarray(u).tobytes()
        if self.correction_cache is not None and self.correction_cache[0]==key:return self.correction_cache[1]
        left=self.coast_port(self.coast,u);old=self.old_clock_jet(0.,u)
        dc={name:left[name]-old[k] for name,k in [('P','X'),('V','Xs'),('A','Xss'),('Pu','Xu'),('Vu','Xsu'),('Au','Xssu'),('Puu','Xuu'),('Vuu','Xsuu')]}
        # Xssuu enters only a nonessential higher jet; compute from the same
        # Fourier representation, never by differentiating independent data.
        i=min(len(self.old.s)-2,max(0,np.searchsorted(self.old.s,self.old_start,side='right')-1))
        L=self.old.s[i+1]-self.old.s[i];t=(self.old_start-self.old.s[i])/L
        p0=self.old.port(i,u);p1=self.old.port(i+1,u)
        seq=np.stack([p0['Puu'],p0['Vuu'],p0['Auu'],p1['Puu'],p1['Vuu'],p1['Auu']])
        dc['Auu']=left['Auu']-np.einsum('i,ijk->jk',w.ports.hermite_weights(t,L,2),seq)
        dc.update(f=0.,fs=0.,fss=0.)
        zero={k:np.zeros_like(v) if isinstance(v,np.ndarray) else 0. for k,v in dc.items()}
        self.correction_cache=(key,(dc,zero));return dc,zero
    def jet(self,s,u):
        u=np.asarray(u,float).reshape(-1)
        if s<=self.coast_end or s>self.cut:return super().jet(s,u)
        x=s-self.coast_end
        if abs(s-self.cut)<2e-14:
            out=w.packet_from_port(self.cut_port(u))
        else:
            out=self.old_clock_jet(x,u)
            if x<self.blend:
                left,right=self.correction(u);corr=w.connector(x/self.blend,self.blend,left,right)
                for key in ['X','Xs','Xss','Xu','Xsu','Xuu','Xssu','Xsuu']:out[key]=out[key]+corr[key]
        f,fs,fss,_=self.scalar(s);out.update(f=f,fs=fs,fss=fss,segment='right_transplant');return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('ramp_master');ap.add_argument('coast_master');ap.add_argument('old_report')
    ap.add_argument('old_full_samples');ap.add_argument('old_full_report');ap.add_argument('output_prefix')
    ap.add_argument('--old-start',type=float,default=.22);ap.add_argument('--blend',type=float,default=.22)
    ap.add_argument('--no-height-shift',action='store_true');ap.add_argument('--angles',type=int,default=128)
    ap.add_argument('--quadrature',type=int,default=1024);ap.add_argument('--right-nodes',type=int,default=49)
    args=ap.parse_args();start=time.time();prefix=Path(args.output_prefix)
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh output prefix required')
    old=np.load(args.old_full_samples);r=json.loads(Path(args.old_full_report).read_text());op=r['parameters']
    if hashlib.sha256(Path(args.old_full_samples).read_bytes()).hexdigest()!=r['outputSHA256']:raise ValueError('Fixed prefix/tail identity mismatch')
    if args.angles!=len(old['u']):raise ValueError('Copied fixed-piece angular grid must agree')
    m=TransplantMaster(args.ramp_master,args.coast_master,args.old_report,old_start=args.old_start,blend_length=args.blend,
        height_shift=not args.no_height_shift,amplitude=op['A'],Z=op['Z'],right_length=op['rightLength'])
    u=old['u'];rows=[];sx=[];saved={key:[] for key in old.files if key not in ['s','u']}
    for j,s in enumerate(old['s']):
        if s>=m.coast_end-1e-13:break
        sx.append(float(s));rows.append(r['rows'][j])
        for key in saved:saved[key].append(old[key][j])
    rights=np.unique(np.r_[m.coast_end+m.L*np.linspace(0,1,args.right_nodes),m.coast_end+m.blend])
    for j,s in enumerate(rights):
        raw=m.jet(float(s),u);norm=m.normalized(float(s),u,args.quadrature)
        rd=w.ports.diagnostics(raw,m.A);nd=w.ports.diagnostics(norm,m.A)
        for key in saved:saved[key].append(raw['X'] if key=='rawX' else raw['Xu'] if key=='rawXu' else norm[key])
        sx.append(float(s));rows.append(dict(s=float(s),segment=norm['segment'],raw=rd,normalized=nd,scale=norm['normalizationScale'],
            inverseResidual=norm['materialInverseResidual'],discreteUnitTClosure=float(np.linalg.norm(np.mean(norm['unitT'],axis=0)))))
        if j%8==0 or j==len(rights)-1:print(json.dumps(dict(rightNode=j,total=len(rights),s=float(s),metric=nd['maximumRelativeMetric'],
            curvature=nd['maximumOwnCurvature'],area=nd['minimumArea'],zmax=nd['maximumZ'])),flush=True)
    for j,s in enumerate(old['s']):
        if s<=op['physicalCut']+1e-13:continue
        sx.append(float(s));rows.append(r['rows'][j])
        for key in saved:saved[key].append(old[key][j])
    sample_path=Path(str(prefix)+'-samples.npz');np.savez_compressed(sample_path,s=np.asarray(sx),u=u,**{key:np.asarray(value) for key,value in saved.items()})
    keys=['maximumRelativeMetric','maximumOwnCurvature','maximumAbsGError','maximumRadius','maximumAbsY','maximumZ','maximumAbsProfileSlope']
    extrema={key:max(row['normalized'][key] for row in rows) for key in keys}
    extrema['minimumHeld']=min(row['normalized']['minimumHeld'] for row in rows);extrema['minimumArea']=min(row['normalized']['minimumArea'] for row in rows)
    dc=m.correction(u)[0];trace={k:float(np.max(np.linalg.norm(dc[k],axis=1))) for k in ['P','V','A','Pu','Vu','Puu']}
    truecut=m.cut_port(u);samplecut=m.old.port(len(m.old.s)-1,u,repair=False)
    tailrepair={k:float(np.max(np.linalg.norm(truecut[k]-samplecut[k],axis=1))) for k in ['P','V','A','Pu','Vu','Puu']}
    report=dict(schema='6a65-C2-real-Cauchy-to-complete-retargeted-R219-transplant-v1',parameters=op,
        transplant=dict(oldStart=m.old_start,oldCut=m.old.end,newCut=m.cut,blendLength=m.blend,meanHeightShift=m.dz,
            clockDelta=m.clock_delta,clockMinimumDerivative=m.clock_min,
            clock='oldStart+x+clockDelta*S9(x/L)',clockEndpointFirstJet=1.,clockEndpointSecondJet=0.,
            height='meanHeightShift*(1-S9(x/L)); zero two-jets at true cut',
            correction='complete left two-jet quintic Hermite correction, zero full two-jets at blend end',
            inletCorrectionTwoJets=trace,oldTailFourierRepairToExactR205=tailrepair),
        sourceFourierDerivativeDifferences=m.old.projection,sourceReportSHA256=hashlib.sha256(Path(args.old_report).read_bytes()).hexdigest(),
        sourceRetargeting=m.old.report['sourceChange'],oldSourceStateSHA256=m.old.report['sourceStateSHA256'],
        normalizedExtrema=extrema,rows=rows,angles=args.angles,quadrature=args.quadrature,
        maximumDiscreteUnitTClosure=max(row['discreteUnitTClosure'] for row in rows),
        inheritedFixedPieceSampleSHA256=r['outputSHA256'],fixedPrefixAndTailExactlyUnchanged=True,
        outputSHA256=hashlib.sha256(sample_path.read_bytes()).hexdigest(),scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        acceptedOptimizationSteps=0,newWholePositionField=True,newPositionNotSameMetricSolution=True,
        continuousCertificate=False,wholeClosedReachCertified=False,seconds=time.time()-start)
    Path(str(prefix)+'-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ['transplant','sourceFourierDerivativeDifferences','normalizedExtrema','outputSHA256','seconds']}),flush=True)


if __name__=='__main__':main()

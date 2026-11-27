#!/usr/bin/env python3
"""Sample actual A's C2 Hermite field after retaining its source background.

The baseline has h0'=w and h0''=wr from the unchanged metric source.
Only the nonround Cartesian perturbation is interpolated. Compare (i) old
full-height interpolation, (ii) preserving all old node means, and (iii)
subtracting the same RK12 background quadrature from each saved scalar mean
increment before adding the source primitive. These are numerical fields.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,gzip,hashlib,json,time
from pathlib import Path
import numpy as np


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def angular_jets(c,n):
    N=c.shape[1]
    if n<N or n%2: raise ValueError('Even angular grid at least as fine as input required')
    f=np.fft.rfft(np.asarray(c,dtype=float),axis=1)/N
    g=np.zeros((6,n//2+1,3),dtype=complex);g[:,:f.shape[1]]=f
    if n>N:g[:,N//2]*=.5
    k=np.arange(n//2+1)[None,:,None]
    return [np.fft.irfft(g*(1j*k)**d,n=n,axis=1)*n for d in range(3)]


def hermite(y0,y1,v0,v1,w0,w1,h):
    dy=y1-y0-h*v0;dv=h*(v1-v0);a=h*h*w0;b=h*h*w1
    return np.stack([y0,h*v0,a/2,10*dy-4*dv-1.5*a+.5*b,
                     -15*dy+7*dv+1.5*a-b,6*dy-3*dv-.5*a+.5*b])


def evaluate(c,u,h,d=0):
    weights=np.zeros(6,dtype=np.longdouble)
    for k in range(d,6):
        f=1
        for j in range(d):f*=k-j
        weights[k]=f*u**(k-d)/h**d
    return np.einsum('k,kjc->jc',weights,c)


def load_nodes(path):
    complete=json.loads(path.read_text());rows=complete['rows'];count=len(rows);N=complete['angular']
    y=np.empty((count,N,3),dtype=np.longdouble);v=y.copy();w=y.copy()
    r=np.array([q['geometry']['r']for q in rows],dtype=np.longdouble)
    if not np.all(r[:-1]>r[1:]):raise ValueError('Nodes must be outer to inner')
    for i,row in enumerate(rows):
        b=(path.parent/row['file']).read_bytes()
        if hashlib.sha256(b).hexdigest()!=row['sha256']:raise ValueError('Changed node bytes')
        raw=gzip.decompress(b)
        if hashlib.sha256(raw).hexdigest()!=row['rawSha256']:raise ValueError('Changed raw node bytes')
        z=np.frombuffer(raw,dtype='<f8').reshape(N,12)
        y[i]=z[:,:3];v[i]=z[:,3:6];w[i,:,2]=z[:,9]
    return complete,r,y,v,w


def assess(r,y,v,w,bg,angles,analytic_background):
    # Use one shared horizontal second derivative at every node.
    r=r[::-1].copy();y=y[::-1].copy();v=v[::-1].copy();w=w[::-1].copy();ns=len(r)-1
    for i in range(1,ns):
        hm=r[i]-r[i-1];hp=r[i+1]-r[i]
        w[i,:,:2]=(hp/(hm+hp)*(v[i,:,:2]-v[i-1,:,:2])/hm+
                   hm/(hm+hp)*(v[i+1,:,:2]-v[i,:,:2])/hp)
    w[0,:,:2]=(v[1,:,:2]-v[0,:,:2])/(r[1]-r[0]);w[-1,:,:2]=(v[-1,:,:2]-v[-2,:,:2])/(r[-1]-r[-2])
    theta=2*np.pi*np.arange(angles)/angles
    er=np.stack([np.cos(theta),np.sin(theta),np.zeros(angles)],axis=1)
    et=np.stack([-np.sin(theta),np.cos(theta),np.zeros(angles)],axis=1)
    maxima=dict(metric=0.,kappa=0.,minimum_metric_det=float('inf'));witnesses={};records=[]
    for si,stage in enumerate(bg['rows']):
        i=ns-1-si;h=r[i+1]-r[i]
        c=angular_jets(hermite(y[i],y[i+1],v[i],v[i+1],w[i],w[i+1],h),angles)
        sm=sk=0.
        for pt in stage['points']:
            radius=np.longdouble(pt['r']);u=(radius-r[i])/h
            if not(-1e-7<=u<=1+1e-7):raise ValueError(('Wrong radius',si,float(u)))
            u=min(np.longdouble(1),max(np.longdouble(0),u))
            fr=evaluate(c[0],u,h,1)+er;ft=evaluate(c[1],u,h)+radius*et
            frr=evaluate(c[0],u,h,2);frt=evaluate(c[1],u,h,1)+et;ftt=evaluate(c[2],u,h)-radius*er
            if analytic_background:
                fr[:,2]+=np.longdouble(pt['w']);frr[:,2]+=np.longdouble(pt['wr'])
            E=(fr*fr).sum(axis=1);F=(fr*ft).sum(axis=1);G=(ft*ft).sum(axis=1)
            Eg=np.longdouble(pt['E']);ga=(E-Eg)/Eg;gb=F/(np.sqrt(Eg)*radius);gc=G/(radius*radius)-1
            err=(np.abs(ga+gc)+np.sqrt((ga-gc)**2+4*gb*gb))/2
            j=int(np.argmax(err));value=float(err[j]);sm=max(sm,value)
            if value>maxima['metric']:
                maxima['metric']=value;witnesses['metric']=dict(stage=si,x=pt['x'],r=pt['r'],theta=float(theta[j]),components=[float(ga[j]),float(gb[j]),float(gc[j])])
            normal=np.cross(fr,ft);normal/=np.sqrt((normal*normal).sum(axis=1))[:,None]
            ee=(frr*normal).sum(axis=1);ff=(frt*normal).sum(axis=1);gg=(ftt*normal).sum(axis=1)
            det=E*G-F*F;tr=(ee*G+gg*E-2*ff*F)/det;prod=(ee*gg-ff*ff)/det
            kap=(np.abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*prod)))/2
            j=int(np.argmax(kap));value=float(kap[j]);sk=max(sk,value)
            if value>maxima['kappa']:
                maxima['kappa']=value;witnesses['kappa']=dict(stage=si,x=pt['x'],r=pt['r'],theta=float(theta[j]))
            maxima['minimum_metric_det']=min(maxima['minimum_metric_det'],float(det.min()))
        records.append(dict(stage=si,metric=sm,kappa=sk))
    return dict(maxima=maxima,witnesses=witnesses,stage_rows=records)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--complete',type=Path,required=True);p.add_argument('--background',type=Path,required=True)
    p.add_argument('--saved-stage-means',type=Path);p.add_argument('--angles',type=int,default=512)
    p.add_argument('--variants',default='old_full_height,preserve_node_means,correct_background_quadrature')
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();start=time.time();complete,r,osc,v,w=load_nodes(a.complete);bg=json.loads(a.background.read_text())
    rows=complete['rows'];ns=len(rows)-1
    if bg['stages']!=ns or len(bg['rows'])!=ns:raise ValueError('Stage count differs')
    nodeMean=np.array([q['meanHeightInnerAnchor']for q in rows],dtype=np.longdouble)
    nodeBG=np.asarray(bg['nodeHeightInnerAnchor'],dtype=np.longdouble)
    slope=np.array([q['geometry']['w']for q in rows],dtype=np.longdouble)
    second=np.array([q['geometry']['w']*q['geometry']['dlogwdx']/q['geometry']['drdx']for q in rows],dtype=np.longdouble)
    corrected=None;meanDefinition=None;sourceInputs={str(a.complete):sha(a.complete),str(a.background):sha(a.background)}
    if a.saved_stage_means:
        raw=gzip.decompress(a.saved_stage_means.read_bytes());data=np.frombuffer(raw,dtype='<f8').reshape(ns,-1)
        increments=np.asarray(data[:,-3],dtype=np.longdouble)-np.array([q['rk12HeightIncrement']for q in bg['rows']],dtype=np.longdouble)
        corrected=np.zeros(ns+1,dtype=np.longdouble)
        for i in range(ns-1,-1,-1):corrected[i]=corrected[i+1]+increments[i]
        sourceInputs[str(a.saved_stage_means)]=sha(a.saved_stage_means)
        meanDefinition='Replace each saved total mean increment I(ur) by I(ur)-RK12(w dr)+native_source_integral(w dr); one common inner anchor.'
    elif all('meanPerturbationInnerAnchor'in q for q in rows):
        corrected=np.array([q['meanPerturbationInnerAnchor']for q in rows],dtype=np.longdouble)
        meanDefinition='Use the separately accumulated engine perturbation mean supplied by the actual RK interior readout; the input total node mean already includes its source background primitive.'
    results={}
    for variant in a.variants.split(','):
        y=osc.copy();vv=v.copy();ww=w.copy()
        if variant=='old_full_height':y[:,:,2]+=nodeMean[:,None];analytic=False
        elif variant=='preserve_node_means':y[:,:,2]+=(nodeMean-nodeBG)[:,None];analytic=True
        elif variant=='correct_background_quadrature':
            if corrected is None:raise ValueError('Corrected mean inputs missing')
            y[:,:,2]+=corrected[:,None];analytic=True
        else:raise ValueError('Unknown variant '+variant)
        if analytic:vv[:,:,2]-=slope[:,None];ww[:,:,2]-=second[:,None]
        results[variant]=assess(r,y,vv,ww,bg,a.angles,analytic)
        print(json.dumps(dict(variant=variant,maxima=results[variant]['maxima'],seconds=time.time()-start)),flush=True)
    meanChange=None
    if corrected is not None:
        delta=corrected+nodeBG-nodeMean;j=int(np.argmax(np.abs(delta)))
        meanChange=dict(maximum_absolute=float(abs(delta).max()),worst_node=j,at_cut=float(delta[0]),
            correction_definition=meanDefinition,comparison_baseline='The total node means in this input complete.json, not necessarily the older accepted-A saved means.',
            corrected_perturbation_mean_at_cut=float(corrected[0]))
    out=dict(schema='accepted-A-background-preserving-Hermite-metric-v1',finished=True,
        definition=__doc__,source_sha256=sha(__file__),input_sha256=sourceInputs,
        original_profile_fingerprint=bg['original_profile_fingerprint'],
        nodes=len(rows),angular_evaluation=a.angles,radial_samples=sum(len(q['points'])for q in bg['rows']),
        variants=results,mean_correction=meanChange,seconds=time.time()-start,
        limitations=['Finite floating samples are not a continuous metric or curvature certificate.',
            'Shared horizontal second jets use the stated nonuniform difference rule.',
            'Correcting the separable background quadrature changes saved node means by the reported amount; no node change is hidden.',
            'No new BVP, infinite tail, closed surface, reach, or large-amplitude conclusion.'])
    with a.out.open('x')as f:json.dump(out,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(out=str(a.out),mean_correction=meanChange,seconds=out['seconds'])),flush=True)


if __name__=='__main__':main()

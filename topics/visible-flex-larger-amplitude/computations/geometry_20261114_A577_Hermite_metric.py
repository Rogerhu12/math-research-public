#!/usr/bin/env python3
"""Numerical metric/curvature evaluation of the precise R230 finite field.

Uses actual 577 node positions and r jets, shared nonuniform second r jets,
the full 512-point cardinal interpolant including Nyquist, and the original
frozen A metric at interior radial points. This is sampled evidence only.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[k]='1'
import argparse,gzip,hashlib,json,time
from pathlib import Path
import numpy as np

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def angular_jets(coeff, outN):
    N=coeff.shape[1]
    if outN<N or outN%2: raise ValueError('Need an even angular resolution >=512')
    f=np.fft.rfft(np.asarray(coeff,dtype=float),axis=1)/N
    g=np.zeros((coeff.shape[0],outN//2+1,3),dtype=complex)
    g[:,:f.shape[1],:]=f
    if outN>N:g[:,N//2,:]*=.5
    k=np.arange(outN//2+1)[None,:,None]
    return [np.fft.irfft(g*(1j*k)**d,n=outN,axis=1)*outN for d in range(3)]

def hermite_coeff(y0,y1,v0,v1,w0,w1,h):
    dy=y1-y0-h*v0;dv=h*(v1-v0);a=h*h*w0;b=h*h*w1
    return np.stack([y0,h*v0,a/2,10*dy-4*dv-1.5*a+.5*b,
                     -15*dy+7*dv+1.5*a-b,6*dy-3*dv-.5*a+.5*b])

def evaluate(c,u,h,order=0):
    weights=np.zeros(6,dtype=np.longdouble)
    for k in range(order,6):
        f=1
        for j in range(order):f*=k-j
        weights[k]=f*np.longdouble(u)**(k-order)/h**order
    return np.einsum('k,kjc->jc',weights,c)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--complete',type=Path,required=True)
    ap.add_argument('--background',type=Path,required=True)
    ap.add_argument('--angles',type=int,default=1024)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();start=time.time()
    report=json.loads(a.complete.read_text());bg=json.loads(a.background.read_text())
    assert report['completedNodes']==577 and report['whole_577_node_readout_complete']
    assert bg['stages']==576
    original=report['rows'];rr=np.array([r['geometry']['r']for r in original],dtype=np.longdouble)
    assert np.all(rr[:-1]>rr[1:])
    N=report['angular'];Y=np.empty((577,N,3),dtype=np.longdouble);V=Y.copy();W=Y.copy()
    for i,row in enumerate(original):
        p=a.complete.parent/row['file'];compressed=p.read_bytes()
        assert hashlib.sha256(compressed).hexdigest()==row['sha256']
        raw=gzip.decompress(compressed);assert hashlib.sha256(raw).hexdigest()==row['rawSha256']
        z=np.frombuffer(raw,dtype='<f8').reshape(N,12)
        Y[i]=z[:,:3];Y[i,:,2]+=np.longdouble(row['meanHeightInnerAnchor'])
        V[i]=z[:,3:6];W[i,:,2]=z[:,9]
    # Original nodes are outer-to-inner. The formula is equivalent after reversal.
    r=rr[::-1].copy();Y=Y[::-1].copy();V=V[::-1].copy();W=W[::-1].copy()
    for i in range(1,576):
        hm=r[i]-r[i-1];hp=r[i+1]-r[i]
        W[i,:,:2]=(hp/(hm+hp)*(V[i,:,:2]-V[i-1,:,:2])/hm+
                    hm/(hm+hp)*(V[i+1,:,:2]-V[i,:,:2])/hp)
    W[0,:,:2]=(V[1,:,:2]-V[0,:,:2])/(r[1]-r[0])
    W[576,:,:2]=(V[576,:,:2]-V[575,:,:2])/(r[576]-r[575])
    theta=2*np.pi*np.arange(a.angles)/a.angles
    er=np.stack([np.cos(theta),np.sin(theta),np.zeros(a.angles)],axis=1)
    et=np.stack([-np.sin(theta),np.cos(theta),np.zeros(a.angles)],axis=1)
    maxima=dict(metric=0.,kappa=0.,minimum_metric_det=float('inf'))
    witnesses={};stage_rows=[]
    for si,stage in enumerate(bg['rows']):
        assert stage['stage']==si
        i=575-si;h=r[i+1]-r[i]
        c=hermite_coeff(Y[i],Y[i+1],V[i],V[i+1],W[i],W[i+1],h)
        angular=angular_jets(c,a.angles);sm=0.;sk=0.
        for pt in stage['points']:
            radius=np.longdouble(pt['r']);u=(radius-r[i])/h
            if not(-1e-7<=u<=1+1e-7):raise ValueError(('wrong stage radius',si,float(u)))
            u=min(np.longdouble(1),max(np.longdouble(0),u))
            Fr=evaluate(angular[0],u,h,1)+er
            Ft=evaluate(angular[1],u,h,0)+radius*et
            Frr=evaluate(angular[0],u,h,2)
            Frt=evaluate(angular[1],u,h,1)+et
            Ftt=evaluate(angular[2],u,h,0)-radius*er
            E=np.sum(Fr*Fr,axis=1);F=np.sum(Fr*Ft,axis=1);G=np.sum(Ft*Ft,axis=1)
            Eg=np.longdouble(pt['E']);ga=(E-Eg)/Eg;gb=F/(np.sqrt(Eg)*radius);gc=G/(radius*radius)-1
            err=(np.abs(ga+gc)+np.sqrt((ga-gc)**2+4*gb*gb))/2
            j=int(np.argmax(err));value=float(err[j]);sm=max(sm,value)
            if value>maxima['metric']:
                maxima['metric']=value;witnesses['metric']=dict(stage=si,x=pt['x'],r=pt['r'],theta=float(theta[j]),
                    components=[float(ga[j]),float(gb[j]),float(gc[j])])
            normal=np.cross(Fr,Ft);normal/=np.sqrt(np.sum(normal*normal,axis=1))[:,None]
            ee=np.sum(Frr*normal,axis=1);ff=np.sum(Frt*normal,axis=1);gg=np.sum(Ftt*normal,axis=1)
            det=E*G-F*F;tr=(ee*G+gg*E-2*ff*F)/det;prod=(ee*gg-ff*ff)/det
            kap=(np.abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*prod)))/2
            j=int(np.argmax(kap));value=float(kap[j]);sk=max(sk,value)
            if value>maxima['kappa']:
                maxima['kappa']=value;witnesses['kappa']=dict(stage=si,x=pt['x'],r=pt['r'],theta=float(theta[j]))
            maxima['minimum_metric_det']=min(maxima['minimum_metric_det'],float(det.min()))
        stage_rows.append(dict(stage=si,metric=sm,kappa=sk))
        if(si+1)%96==0:print(json.dumps(dict(stages=si+1,maxima=maxima)),flush=True)
    out=dict(schema='actual-A-R230-finite-field-sampled-metric-v1',finished=True,
             definition='R230 unprojected finite cardinal/quintic Hermite field with horizontal W from (2.1)-(2.2); circular frame kept analytic.',
             complete_sha256=sha(a.complete),background_sha256=sha(a.background),source_sha256=sha(Path(__file__)),
             angular_evaluation=a.angles,radial_samples=576*bg['samples_per_stage'],
             maxima=maxima,witnesses=witnesses,stage_rows=stage_rows,seconds=time.time()-start,
             limitations=['Floating FFT and finite samples are not interval bounds.',
                          'Same finite node data; this angular evaluation refinement is not a new solution or the required fixed-g convergence chain.',
                          'No closed surface, global reach or large amplitude conclusion.'])
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),maxima=maxima,witnesses=witnesses,seconds=out['seconds'])),flush=True)

if __name__=='__main__':main()

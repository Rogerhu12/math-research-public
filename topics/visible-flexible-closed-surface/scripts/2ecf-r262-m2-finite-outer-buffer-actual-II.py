#!/usr/bin/env python3
"""Optimize a finite outer buffer only, retaining the actual oscillating R262 deep region up to its real flat-slope seam."""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
from scipy.stats import qmc
def design(v,a,b,w0):
    n=len(v);P=np.column_stack([np.full(n,w0),10**(-3-8*v[:,0]),.026+.075*v[:,1],10**(-2-4*v[:,2]),.028+.062*v[:,3],10**(-1.8-1.8*v[:,4]),.12+.28*v[:,5]])
    raw=.25+v[:,6:12];raw[:,-1]*=2.4;length=(b-a)*raw/raw.sum(axis=1)[:,None]
    return P,length
def calc(P,L,alpha,N):
    n=len(P);r=np.full(n,alpha['r']);Q=1/r**4;p=alpha['w']*r**4*(alpha['Hr']/alpha['H']-4/r);shape=np.full(n,alpha['innerShapePerUnitH']);baseK=np.zeros(n);height=np.zeros(n);kmer=np.zeros(n)
    for j in range(len(L[0])):
        w0=P[:,j];w1=P[:,j+1];ell=L[:,j];log=np.log(w1/w0);h=ell/N
        def geom(t):
            ss=t**3*(10+t*(-15+6*t));ds=30*t*t*(1-t)**2
            w=w0*np.exp(log*ss);wr=w*log*ds/ell
            return w,wr
        for k in range(N):
            t=k/N;c=np.sqrt(3)/6;w,wr=geom(t)
            E=1+w*w;H=r**4*Q;J=p/(r**4*w);hder=4*H/r+J;Hrr=-wr/w*J
            # Actual absolute linear II entries in true orthonormal material coordinates.
            dL=-Hrr/np.sqrt(E);dN=-np.sqrt(E)*J/r;dM=-6*H/(r*r)-2*J/r
            shape=np.maximum(shape,np.maximum(abs(dL)+abs(dM),abs(dN)+abs(dM)))
            baseK=np.maximum(baseK,np.maximum(abs(wr/E**1.5),w/(r*np.sqrt(E))))
            w1g,_=geom(t+(.5-c)/N);w2g,_=geom(t+(.5+c)/N)
            r1=r+h*(.5-c);r2=r+h*(.5+c)
            a1=h/(w1g*r1**8);a2=h/(w2g*r2**8);b1=12*h*w1g*r1**6;b2=12*h*w2g*r2**6
            A=(a1+a2)/2;B=(b1+b2)/2;d=-np.sqrt(3)/12*(a2*b1-a1*b2);r2=d*d-A*B
            tau=np.sqrt(abs(r2));sn=np.where(r2<=0,np.sin(tau),np.sinh(tau))/np.maximum(tau,1e-100);cs=np.where(r2<=0,np.cos(tau),np.cosh(tau))
            Q,p=(cs+sn*d)*Q+sn*A*p,-sn*B*Q+(cs-sn*d)*p
            height+=(w1g+w2g)*h/2;kmer+=(np.sqrt(1+w1g**2)+np.sqrt(1+w2g**2))*h/2;r+=h
    H=r**4*Q;J=p/(r**4*P[:,-1]);D=4/r+J/H
    return H,D,shape/abs(H),baseK,height,kmer
def main():
    p=argparse.ArgumentParser();p.add_argument('--source',required=True,type=Path);p.add_argument('--out',required=True,type=Path);p.add_argument('--power',type=int,default=14);p.add_argument('--seed',type=int,default=313473);p.add_argument('--radius',type=float,default=.25);p.add_argument('--cut',type=float,default=.6);a=p.parse_args()
    source=json.loads(a.source.read_bytes());seam=next(x for x in source['finite'][-1]['anchors'] if x['r']==a.radius)
    if seam['wr']!=0:raise ValueError('Choose an original constant-slope plateau for this buffer')
    seq=qmc.Sobol(12,scramble=True,seed=a.seed).random_base2(a.power);P,L=design(seq,a.radius,a.cut,seam['w'])
    H,D,sh,K,Z,S=calc(P,L,seam,32);idx=np.flatnonzero((K<10)&np.isfinite(D)&(abs(D)<180))
    if not len(idx):raise RuntimeError('No finite curvature-margin candidate')
    ids=idx[np.argsort(sh[idx])[:8]]
    vals=[]
    for i in ids:
        row=dict(levels=P[i].tolist(),lengths=L[i].tolist(),sourceInnerHeightGain=seam['innerShapePerUnitH'],grids=[])
        for n in [64,192,512]:
            H,D,sh,K,Z,S=calc(P[i:i+1],L[i:i+1],seam,n)
            row['grids'].append(dict(grid=n,outerHforUnitInner=float(H[0]),D=float(D[0]),shapeGain=float(sh[0]),baseK=float(K[0]),height=float(Z[0]),materialLength=float(S[0])))
        print('buf',i,row['grids'][-1],flush=True);vals.append(row)
    out=dict(schema='actual-R262-original-infinite-tail-to-inner-seam-new-C2-finite-m2-physical-buffer-v1',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),protectedInputSHA256=hashlib.sha256(a.source.read_bytes()).hexdigest(),sampled=a.power,seed=a.seed,innerRadius=a.radius,outerRadius=a.cut,originalSeam=seam,admissible=len(idx),choices=vals)
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
if __name__=='__main__':main()

#!/usr/bin/env python3
"""A new literal cubic tensor in physical polar charts, with the true infinite deep meridian and second mode at the cuff."""
import argparse,importlib.util,json,os
from fractions import Fraction
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.interpolate import PchipInterpolator
p=Path(__file__).with_name('2ecf-r289-material-polar-meridian-sections.py');sp=importlib.util.spec_from_file_location('r289_sections',p);sec=importlib.util.module_from_spec(sp);sp.loader.exec_module(sec)
DEN=25*2**34
def template(p):
    for k in ('scripts','meridian','buffer','tail-table','tail','state'):p.add_argument('--'+k,type=Path,required=True)
    return p
def load(a):return sec.Q.Field(a.scripts,a.meridian,a.buffer,a.tail_table,a.state,Fraction(json.loads(a.tail.read_bytes())['scale']))
def s5(t):return t**3*(10+t*(-15+6*t))
def clock(y,h):return y+h*(y-y**3)/2
def tensor(g,n,m,seam_den=32,bias=0.,prefilter=0.):
    assert n%seam_den==0
    end=n*(seam_den-1)//seam_den;y=np.arange(end+3)/n;rad=clock(y,bias);source,_=g.src.grid(max(600,2*n),12,True);th,V=sec.collect(g,source,m*2+1,True);unique=np.r_[True,np.diff(source[:,0])>1e-12];data=PchipInterpolator(source[unique,0]/g.T,V[unique,::2,:3],axis=0)(rad)
    xi=np.arange(m+1)/m;data[:,:,2]*=2/np.pi;data[:,0,2]=0;data[:,-1,2]=1
    if prefilter:
        left=data[:,1].copy();left[:,2]*=-1;right=data[:,-2].copy();right[:,2]=2-right[:,2]
        da=np.concatenate([left[:,None],data,right[:,None]],axis=1);data-=prefilter*np.diff(da,n=2,axis=1)/6
        left=data[1].copy();left[:,1]*=-1;right=2*data[-1]-data[-2]
        ds=np.concatenate([left[None],data,right[None]]);data-=prefilter*np.diff(ds,n=2,axis=0)/6
    Z=round(g.cutZ*DEN)/DEN;start,finish=(.885,.948) if seam_den==32 else (1-3.5/seam_den,1-1.7/seam_den);v=s5(np.clip((y-start)/(finish-start),0,1))[:,None]
    data[:,:,0]=(1-v)*data[:,:,0]+v*(.32+1.5*(1-rad[:,None])-1.5*bias*y[:,None]/(2*n*n))
    data[:,:,1]=(1-v)*data[:,:,1]+v*Z
    data[:,:,2]=(1-v)*data[:,:,2]+v*xi[None,:]
    core=np.rint(data*DEN).astype(np.int64)
    # Physical data are frozen as integer spline coefficients. Beyond 31/32 the round terminal
    # affine continuation joins the actual infinite rotating profile with a smooth cutoff.
    cp=np.empty((end+4,m+4,3),dtype=np.int64);cp[1:,1:m+2]=core;cp[0,1:m+2]=core[1];cp[0,1:m+2,1]*=-1
    cp[:,0]=cp[:,2];cp[:,0,2]*=-1;cp[:,m+2]=cp[:,m];cp[:,m+2,2]=2*DEN-cp[:,m+2,2];cp[:,m+3]=cp[:,m-1];cp[:,m+3,2]=2*DEN-cp[:,m+3,2]
    return cp,int(np.rint(Z*DEN))
def bernstein(cp):
    C=np.array([[1,4,1,0],[0,4,2,0],[0,2,4,0],[0,1,4,1]],np.int64)
    n,m=cp.shape[:2]
    raw=np.lib.stride_tricks.sliding_window_view(cp,(4,4),axis=(0,1)).transpose(0,1,3,4,2)
    return np.einsum('ij,nmjkc,lk->nmilc',C,raw,C,optimize=True)
def main():
    global DEN
    p=template(argparse.ArgumentParser());p.add_argument('--prefilter',type=float,default=0.);p.add_argument('--bias',type=float,default=0.);p.add_argument('--seam-den',type=int,default=32);p.add_argument('--out',type=Path,required=True);p.add_argument('--spans',type=int,default=256);p.add_argument('--ang',type=int,default=64);a=p.parse_args();DEN=int(np.lcm(DEN,a.ang));g=load(a);cp,Z=tensor(g,a.spans,a.ang,a.seam_den,a.bias,a.prefilter);b=bernstein(cp);A=int(b[0,0,0,0,0]);metadata=dict(cp=cp,den=DEN,N=a.spans,M=a.ang,Zint=Z,Aint=A)
    if a.seam_den!=32:metadata['seamDen']=a.seam_den
    if a.bias:metadata['clockBias']=a.bias
    np.savez_compressed(a.out,**metadata)
    print(dict(rows=cp.shape,scale=DEN,Z=Z/DEN,A=A/(36*DEN),targetPhysicalT=g.T,seamRadius=.32+1.5*(1-clock(1-1/a.seam_den,a.bias)),rangeR=[int(b[...,0].min())/(36*DEN),int(b[...,0].max())/(36*DEN)],input=g.m.base.sha(a.state),output=g.m.base.sha(a.out)),flush=True)
if __name__=='__main__':main()

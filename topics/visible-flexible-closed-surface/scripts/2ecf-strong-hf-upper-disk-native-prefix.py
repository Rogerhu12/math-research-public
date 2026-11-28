#!/usr/bin/env python3
"""Continuous central cylinder and all 64 native H65 physical Hermite elements."""
import argparse
import importlib.util
import json
import os
from fractions import Fraction as F
from pathlib import Path
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def main():
    ap=argparse.ArgumentParser()
    for n in ('scripts','master','potential','output'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--angles',type=int,default=1536)
    ap.add_argument('--central-partitions',type=int,default=48)
    args=ap.parse_args()
    here=Path(__file__).parent
    lib=load(here/'2ecf-strong-hf-upper-sector-check.py','native_sector')
    hf=load(here/'2ecf-strong-hf-interior-continuous-projection.py','native_fourier')
    edge=load(here/'2ecf-strong-hf-edge-continuous-projection.py','native_edge')
    K=load(args.scripts/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py','native_K');I=K.I
    if lib.digest(args.master)!='479dab51bd77a211f64a256bbb16d67b4382e150af0deee7fa6baf84d8e5464a':raise ValueError('The proved H65 master is required')
    with np.load(args.master) as r:
        a,b,c=[F(float(r[k])) for k in ('centralA','centralB','centralLength')]
        source=r['coefficients'];wave=list(map(int,r['wave']));s=list(map(F,r['sx']))
    pot=json.loads(args.potential.read_bytes());check=lib.SectorCheck(K,pot,I(a))
    maxwave=384;cut=64;H=hf.Harmonics(K,args.angles,cut)
    if set(wave)!=set(range(-384,384)):raise ValueError('Unexpected raw native Fourier modes')
    def port(node):
        # coeffs are Re of the complete two-sided Laurent series.
        data=source[node].transpose(1,0,2)
        if node==0:
            p=np.zeros((3,maxwave+1,3,2))
            p[0,1,0,0]=float(a);p[0,1,1,1]=-float(b);p[0,0,2,0]=float(c);p[1,0,2,0]=1
            return I(p)
        lookup={k:i for i,k in enumerate(wave)}
        pos=np.zeros((3,maxwave+1,3),dtype=complex);neg=pos.copy()
        pos[:,0]=data[:,lookup[0]].real
        for k in range(1,maxwave+1):
            if k in lookup:pos[:,k]=data[:,lookup[k]]
            neg[:,k]=data[:,lookup[-k]].conj()
        return I(np.stack((pos.real,pos.imag),axis=-1))+I(np.stack((neg.real,neg.imag),axis=-1))
    def trace(ctrl,order):
        q=H.boxes(ctrl[:,:cut+1],order)
        tail=ctrl[:,cut+1:]
        high=I(tail[:,:,:,0].abs_upper())+I(tail[:,:,:,1].abs_upper())
        error=(high*I(np.arange(cut+1,maxwave+1)[None,:,None])**order).sum(1)
        return q.widen(error[:,None,:])
    sn,cs=K.sincos(K.PI*I(2*np.arange(args.angles)+1)/args.angles)
    sn=sn.widen(K.PI/args.angles);cs=cs.widen(K.PI/args.angles)
    one=I(np.ones(args.angles));zero=I(np.zeros(args.angles))
    for j in range(args.central_partitions):
        z=I.bounds(c*j/args.central_partitions,c*(j+1)/args.central_partitions)*one
        check.cartesian([a*cs,b*sn,z],[zero,zero,one],[-a*sn,b*cs,zero],'central '+str(j))
    central=check.json();central['bounds']=dict(central['bounds']);central['worst']=dict(central['worst'])
    check=lib.SectorCheck(K,pot,I(a))
    # R233 records true final H65 trace differences in the SAME native angle,
    # and R261 preserves the old actual terminal P,V,A data bit for bit.
    defects={'right':{k:[float(F(v))*1.0000000001]*3 for k,v in {
        'P':'3.105e-14','U':'3.286e-12','V':'8.469e-12','SU':'6.336e-10','A':'3.682e-10','AU':'5.039e-8'}.items()}}
    p=port(0)
    for j,(l,r) in enumerate(zip(s,s[1:])):
        q=port(j+1);h=I(r-l);x,v,acc=p;xe,ve,ae=q
        ctrl=hf.parts(I,[x,x+h*v/5,x+2*h*v/5+h.square()*acc/20,
            xe-2*h*ve/5+h.square()*ae/20,xe-h*ve/5,xe])
        pack=[trace(ctrl,0),trace(5*(ctrl[1:]-ctrl[:-1])/h,0),trace(ctrl,1)]
        val=[I(np.min(i.lo,axis=0),np.max(i.hi,axis=0)) for i in pack]
        if j==len(s)-2:
            err=edge.hermite_error(K,'right',(l,r),l,r,defects)
            val=[i.widen(d) for i,d in zip(val,err)]
        check.cartesian(*[[v[:,k] for k in range(3)] for v in val],'H65 '+str(j))
        p=q
    out=dict(schema='upper-disk-potential-accurate-native-H65-and-central-v1',entrySHA256=lib.digest(Path(__file__)),
        sectorSourceSHA256=lib.digest(lib.__file__),potentialSHA256=lib.digest(args.potential),masterSHA256=lib.digest(args.master),angles=args.angles,
        central=central,completeH65=check.json(),physicalRampSegments=len(s)-1)
    with args.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('central',central['bounds'],'H65',check.limits,flush=True)


if __name__=='__main__':main()

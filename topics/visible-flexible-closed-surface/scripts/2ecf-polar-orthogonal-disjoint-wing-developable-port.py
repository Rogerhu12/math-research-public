#!/usr/bin/env python3
"""Independent long- and short-axis cylindrical wings on disjoint supports of the actual whole material disk."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from types import SimpleNamespace
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
here=Path(__file__).parent
base=module(here/'2ecf-polar-material-curve-coupled-spherical-design.py','orthogonal_material')
def curve(p,q,start,amp):
    n=q.shape[1];one=p.constant(1,n);sign=np.where(q[0]<0,-1.,1.)
    val=q[0]*sign;L=.8-start
    t=(q*sign-p.constant(start,n))/L;t[:,val<=start]=0.
    S=sum(c*p.power(t,k) for k,c in enumerate((126,-420,540,-315,70),start=5))
    sa,ca=p.sincos(amp*S);a1=amp*630*p.mul(p.power(t,4),p.power(one-t,4))/L
    cp=ca;hp=sa*sign;cpp=-p.mul(sa,a1)*sign;hpp=p.mul(ca,a1)
    length=np.maximum(val-start,0.);gx,gw=np.polynomial.legendre.leggauss(56)
    x=length[:,None]*(gx+1)/(2*L);a=amp*x**5*(126+x*(-420+x*(540+x*(-315+x*70))))
    C=sign*(np.minimum(val,start)+length*(np.cos(a)@(gw/2)))
    H=length*(np.sin(a)@(gw/2))
    return C,H,cp,hp,cpp,hpp
def wing_port(warm,Ax,Ay,u,r):
    if abs(Ax)>.35 or not 0<=Ay<=.85:raise ValueError('Two-wing amplitude rectangle required')
    p=warm.ports;U=p.constant(u,len(u));U[1]=1;su,cu=p.sincos(U)
    x,hx,cx,zx,cxx,zxx=curve(p,r*cu,.70,Ax)
    y,hy,cy,zy,cyy,zyy=curve(p,r*su,.56,Ay)
    Pu=np.stack([p.mul(cx,-r*su),p.mul(cy,r*cu),p.mul(zx,-r*su)+p.mul(zy,r*cu)],axis=-1)
    V=np.stack([-p.mul(cx,cu),-p.mul(cy,su),-p.mul(zx,cu)-p.mul(zy,su)],axis=-1)
    A=np.stack([p.mul(cxx,p.power(cu,2)),p.mul(cyy,p.power(su,2)),p.mul(zxx,p.power(cu,2))+p.mul(zyy,p.power(su,2))],axis=-1)
    return dict(P=np.stack([x,y,.415+hx+hy],axis=-1),Pu=Pu[0],Puu=Pu[1],Puuu=2*Pu[2],Puuuu=6*Pu[3],V=V[0],Vu=V[1],Vuu=2*V[2],Vuuu=6*V[3],A=A[0],Au=A[1],Auu=2*A[2])
class Ends:
    def __init__(self,scripts,ramp,coast,Ax,Ay,M):
        old=module(here/'2ecf-polar-raised-monotone-oblique-connector.py','two_wing_clock')
        tall=module(here/'2ecf-polar-raised-tail-tall-throat-source.py','two_wing_cap')
        self.warm=module(scripts/'6a65-geometry-cauchy-unit-t-warm.py','two_wing_warm')
        self.base=module(scripts/'6a65-geometry-nonfold-polar-connector.py','two_wing_trace')
        self.master=self.warm.WarmMaster(ramp,coast,coast_length=.02);self.master._ports=self.warm.ports;self.master._warm=self.warm
        self.raised=SimpleNamespace(raised_port=wing_port,tall_config=tall.tall_config);u=2*np.pi*np.arange(M)/M
        self.specs=[];self.clockMin=[]
        for p in (self.base.higher_coast_port(self.master,.02,u),wing_port(self.warm,Ax,Ay,u,.8)):
            d=self.base.endpoint_clock(p,u);r=self.base.polar_profiles(d);j=np.stack([d[k] for k in ('phi','phis','phiss')]);th=j[0,0].copy()
            self.clockMin.append(float(min(j[0,1])));j[0,0]-=u;j[0,1]-=1
            self.specs.append((old.periodic_spline(u,j),{k:old.periodic_spline(th,v) for k,v in r.items()}))
def plan(a):
    filename='2ecf-polar-raised-all-ray-geometric-design.py' if a.mode=='design' else '2ecf-polar-raised-physical-ray-field-observe.py'
    lib=module(here/filename,'orthogonal_wing_'+a.mode);loader=lib.load
    def supply(p,n):return sys.modules[__name__] if Path(p).name=='2ecf-polar-raised-monotone-oblique-connector.py' else loader(p,n)
    lib.load=supply;dest=a.output
    with TemporaryDirectory(dir=dest.parent) as temp:
        q=Path(temp)/'field.json';a.output=q;lib.run(a);data=base.read(q)
    if a.mode=='design':Ax,Ay=a.amplitude,a.flat
    else:
        d=base.read(a.design);Ax,Ay=d['amp'],d['flat'];assert d['orthogonalPortSHA256']==base.sha(__file__)
    data.update(orthogonalPortSHA256=base.sha(__file__),longAxisAmplitude=Ax,shortAxisAmplitude=Ay,physicalWingStarts=[.70,.56],actualEngineSHA256=base.sha(lib.__file__))
    base.stores(dest,data)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','field','output','prepared','independent','design'):a.add_argument('--'+k,type=Path)
    for k,v in [('spans',12),('angles',64),('h',64),('winding',0),('trace-nodes',1024)]:a.add_argument('--'+k,type=int,default=v)
    for k,v in [('b',.1815625),('end',.9772364498716914),('amplitude',.35),('flat',.85),('kappa',9.5),('penalty',3.),('geometry-weight',160000.)]:a.add_argument('--'+k,type=float,default=v)
    plan(a.parse_args())

#!/usr/bin/env python3
"""A complete developable port with independently specified interior bend and terminal tangent."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from types import SimpleNamespace
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import numpy as np

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj

def returning_port(warm,peak,terminal,u,r):
    if not 0<=peak<=.48 or not -.2<=terminal<=.2:
        raise ValueError('Outside returning-bend parameter rectangle')
    c=.52
    L=.8-c
    p=warm.ports
    U=p.constant(u,len(u))
    U[1]=1
    su,cu=p.sincos(U)
    y=r*su
    sign=np.where(y[0]<0,-1.,1.)
    ay=sign*y[0]
    on=ay>c
    one=p.constant(1,len(u))
    t=(y*sign[None,:]-p.constant(c,len(u)))/L
    t[:,~on]=0.
    m=one-t
    s9=sum(a*p.power(t,k) for k,a in enumerate((126,-420,540,-315,70),start=5))
    bump=1024*p.mul(p.power(t,5),p.power(m,5))
    alpha=peak*bump+terminal*s9
    sn,cs=p.sincos(alpha)
    factor=p.mul(p.power(t,4),p.power(m,4))
    prime=(peak*5120*p.mul(factor,one-2*t)+terminal*630*factor)/L
    cp=cs
    hp=sn*sign
    cpp=-p.mul(sn,prime)*sign
    hpp=p.mul(cs,prime)
    # C and H are independent Cartesian material primitives of (cos alpha,sin alpha).
    length=np.maximum(0,ay-c)
    gx,gw=np.polynomial.legendre.leggauss(64)
    x=length[:,None]*(gx[None,:]+1)/(2*L)
    ag=peak*(4*x*(1-x))**5+terminal*x**5*(126+x*(-420+x*(540+x*(-315+70*x))))
    C=sign*(np.minimum(ay,c)+length*(np.cos(ag)@(gw/2)))
    H=length*(np.sin(ag)@(gw/2))
    P=np.stack((r*cu[0],C,.415+H),axis=-1)
    pu=np.stack((-r*su,p.mul(cp,r*cu),p.mul(hp,r*cu)),axis=-1)
    v=np.stack((-cu,-p.mul(cp,su),-p.mul(hp,su)),axis=-1)
    k=np.stack((np.zeros_like(cu),p.mul(cpp,p.power(su,2)),p.mul(hpp,p.power(su,2))),axis=-1)
    return dict(P=P,Pu=pu[0],Puu=pu[1],Puuu=2*pu[2],Puuuu=6*pu[3],V=v[0],Vu=v[1],Vuu=2*v[2],Vuuu=6*v[3],A=k[0],Au=k[1],Auu=2*k[2])

class Ends:
    def __init__(self,scripts,ramp,coast,peak,terminal,angles):
        here=Path(__file__).parent
        old=module(here/'2ecf-polar-raised-monotone-oblique-connector.py','rb_old_trace_fit')
        tall=module(here/'2ecf-polar-raised-tail-tall-throat-source.py','rb_tall_cap')
        self.warm=module(scripts/'6a65-geometry-cauchy-unit-t-warm.py','rb_warm')
        self.base=module(scripts/'6a65-geometry-nonfold-polar-connector.py','rb_traces')
        self.master=self.warm.WarmMaster(ramp,coast,coast_length=.02)
        self.master._ports=self.warm.ports
        self.master._warm=self.warm
        self.raised=SimpleNamespace(raised_port=returning_port,tall_config=tall.tall_config)
        u=np.arange(angles)*2*np.pi/angles
        self.clockMin=[]
        self.specs=[]
        for data in (self.base.higher_coast_port(self.master,.02,u),returning_port(self.warm,peak,terminal,u,.8)):
            clock=self.base.endpoint_clock(data,u)
            profile=self.base.polar_profiles(clock)
            jets=np.stack([clock[k] for k in ('phi','phis','phiss')])
            polar=jets[0,0].copy()
            self.clockMin.append(float(np.min(jets[0,1])))
            jets[0,0]-=u
            jets[0,1]-=1
            self.specs.append((old.periodic_spline(u,jets),{k:old.periodic_spline(polar,v) for k,v in profile.items()}))

def run(args):
    here=Path(__file__).parent
    filename=('2ecf-polar-raised-all-ray-geometric-design.py' if args.mode=='design' else '2ecf-polar-raised-physical-ray-field-observe.py')
    engine=module(here/filename,'rb_'+args.mode)
    parent_load=engine.load
    def get_supplier(path,name):
        if Path(path).name=='2ecf-polar-raised-monotone-oblique-connector.py':
            return sys.modules[__name__]
        return parent_load(path,name)
    engine.load=get_supplier
    if args.mode=='observe':
        design=json.loads(args.design.read_text())
        assert design['returningPortSHA256']==sha(__file__) and design['profile']==dict(peak=design['amp'],terminal=design['flat'],flatStart=.52)
    actual=args.output
    if actual.exists():
        raise FileExistsError(actual)
    with TemporaryDirectory(dir=actual.parent) as work:
        args.output=Path(work)/'surface.json'
        engine.run(args)
        out=json.loads(args.output.read_text())
    out['schema']='returning-bend-actual-all-ray-'+args.mode+'-v1'
    out['returningPortSHA256']=sha(__file__)
    out['quadrantEngineSHA256']=sha(engine.__file__)
    out['profile']=dict(peak=args.amplitude,terminal=args.flat,flatStart=.52) if args.mode=='design' else design['profile']
    with actual.open('x') as f:
        json.dump(out,f,indent=2)
        f.write('\n')

if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--mode',choices=('design','observe'),required=True)
    for key in ('scripts','ramp','coast','field','output','prepared','independent','design'):
        a.add_argument('--'+key,type=Path)
    for key,value in [('spans',12),('angles',64),('h',64),('winding',0),('trace-nodes',1024)]:
        a.add_argument('--'+key,type=int,default=value)
    for key,value in [('b',.1815625),('end',.9772364498716914),('amplitude',.48),('flat',-.2),('kappa',9.5),('penalty',3.),('geometry-weight',120000.)]:
        a.add_argument('--'+key,type=float,default=value)
    run(a.parse_args())

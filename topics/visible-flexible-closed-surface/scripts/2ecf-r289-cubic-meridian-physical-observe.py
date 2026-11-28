#!/usr/bin/env python3
"""All six material jets of the literal finite cubic and the true infinite-tail splice, passed through the actual R289 maps."""
import argparse,importlib.util,json,math
from pathlib import Path
import numpy as np
p=Path(__file__).with_name('2ecf-r289-cubic-meridian-physical-source.py');sp=importlib.util.spec_from_file_location('r289_cubic',p);src=importlib.util.module_from_spec(sp);sp.loader.exec_module(src)
p=Path(__file__).with_name('2ecf-r291-injective-low-cuff-physical.py');sp=importlib.util.spec_from_file_location('r291_jet',p);G=importlib.util.module_from_spec(sp);sp.loader.exec_module(G)
def bern(k,x):
    return np.stack([math.comb(k,j)*x**j*(1-x)**(k-j) for j in range(k+1)],axis=-1)
def un(j,v,d,e):
    _,s,a,ss,sa,aa=j
    return np.stack([v,d*s,d*a,d*ss+e*s*s,d*sa+e*s*a,d*aa+e*a*a])
def cos(j):return un(j,np.cos(j[0]),-np.sin(j[0]),-np.cos(j[0]))
def sin(j):return un(j,np.sin(j[0]),np.cos(j[0]),-np.sin(j[0]))
def tanh(j):
    q=np.tanh(j[0]);v=1-q*q;return un(j,q,v,-2*q*v)
def materialized(P,U):
    A=np.stack(P,axis=-1);_,us,ua,uss,usa,uaa=U
    assert np.min(ua)>.05
    hs=-us/ua;hu=1/ua;hss=-(uss+2*usa*hs+uaa*hs*hs)/ua;hsu=-(usa+uaa*hs)*hu/ua;huu=-uaa*hu*hu/ua
    hs,hu,hss,hsu,huu=[q[...,None] for q in (hs,hu,hss,hsu,huu)]
    p,s,a,ss,sa,aa=A
    return np.stack([p,s+a*hs,a*hu,ss+2*sa*hs+aa*hs*hs+a*hss,sa*hu+aa*hs*hu+a*hsu,aa*hu*hu+a*huu]).transpose(1,0,2,3)
class Field:
    def __init__(self,g,archive):
        self.g=g
        with np.load(archive) as a:self.bias=float(a['clockBias']) if 'clockBias' in a.files else 0.;self.sd=int(a['seamDen']) if 'seamDen' in a.files else 32;self.N=int(a['N']);self.M=int(a['M']);self.Z=int(a['Zint'])/int(a['den']);self.A=int(a['Aint'])/(36*int(a['den']));self.B=src.bernstein(a['cp'])/(36*int(a['den']))
        self.B=self.B[:(self.sd-1)*self.N//self.sd,:self.M];G.F.install(self.A)
    def grid(self,rows,angles):
        # A material orbit quarter suffices by exact reflection symmetry. Angles below are true polar theta.
        s=rows[:,0];t=s/self.g.T;theta=np.zeros((6,len(s),len(angles)));theta[0]=angles;theta[2]=1;R,Z,U=np.zeros((3,6,len(s),len(angles)));tb=src.clock(1-1/self.sd,self.bias);finite=t<=tb+1e-14
        if np.any(finite):
            fy=t[finite].copy()
            for _ in range(10):fy-=(src.clock(fy,self.bias)-t[finite])/(1+self.bias*(1-3*fy**2)/2)
            y=fy*self.N;x=np.clip(angles*2/np.pi,0,1)*self.M;iy=np.minimum(y.astype(int),len(self.B)-1);ix=np.minimum(x.astype(int),self.M-1);Y=y-iy;X=x-ix;b=self.B[iy[:,None],ix[None,:]];J=[]
            for i,j in G.m.O:
                c=b
                if i:c=np.diff(c,n=i,axis=2)
                if j:c=np.diff(c,n=j,axis=3)
                v=np.einsum('nujlk,nj,ul->nuk',c,bern(3-i,Y),bern(3-j,X))
                v*=math.factorial(3)/math.factorial(3-i)*math.factorial(3)/math.factorial(3-j)*(self.N/self.g.T)**i*(2*self.M/np.pi)**j
                ps=(1+self.bias*(1-3*fy**2)/2)[:,None,None]
                if i:v/=ps**i
                if i==2:v-=J[1]*(-3*self.bias*fy)[:,None,None]/(self.g.T*ps**2)
                J.append(v)
            f=np.array(J);R[:,finite]=f[...,0];Z[:,finite]=f[...,1];U[:,finite]=f[...,2]*(np.pi/2)
        if np.any(~finite):
            rr=rows[~finite];tt=t[~finite];N=len(tt);shape=(6,N,len(angles))
            def lift(j):
                v=np.zeros(shape);v[0]=j[0][:,None];v[1]=j[1][:,None];v[3]=j[2][:,None];return v
            one=np.ones(N);nil=np.zeros(N);rad=lift(rr[:,(1,3,5)].T);z0=lift(rr[:,(2,4,6)].T);f=lift(rr[:,(7,9,11)].T);l=2/(1-tb)/self.g.T;w=(tt-tb)*(2/(1-tb))
            v=np.clip(w,0,1);active=(w>0)&(w<1)
            h=lift(np.array([1-src.s5(v),-l*30*v*v*(1-v)**2*active,-l*l*60*v*(1-v)*(1-2*v)*active]));o=lift(np.array([one,nil,nil]));oo=o-h;rflat=lift(np.array([.32+1.5*(1-tt),-1.5/self.g.T*one,nil]))
            R[:,~finite]=G.prod(h,rflat)+G.prod(oo,rad)
            ph=theta[:,~finite];amp=tanh(.34*G.prod(f,G.recip(rad)));osc=G.prod(amp,cos(2*ph))
            Z[:,~finite]=self.Z*o+G.prod(oo,z0-self.g.cutZ*o+.001*osc)
            U[:,~finite]=ph+.05*G.prod(oo,G.prod(amp,sin(2*ph)))
        P=[G.prod(R,cos(theta)),G.prod(R,sin(theta)),Z];J=materialized(P,U)
        return G.F.k.ball(G.F.k.slab(J)[0]),U[0]
def stats(f,rr,theta):
    outs=[]
    for i in range(0,len(rr),32):
        rows=rr[i:i+32];J,U=f.grid(rows,theta);z=G.metrics(J,rows,theta);j=np.argmin(abs(rows[:,0]-z['point'][0]));k=np.argmin(abs(theta-z['point'][1]));z['physicalPolarThetaAtPeak']=float(theta[k]);z['point'][1]=float(U[j,k]);outs.append(z)
    top=max(outs,key=lambda z:z['metric']).copy();top.pop('rms');top.update(curvature=max(z['curvature'] for z in outs),areaRatioMin=min(z['areaRatioMin'] for z in outs),heightRange=[min(z['heightRange'][0] for z in outs),max(z['heightRange'][1] for z in outs)],minimumUpperHeight=min(z['minimumUpperHeight'] for z in outs),maximumRadius=max(z['maximumRadius'] for z in outs),maxNorm=max(z['maxNorm'] for z in outs),maxAbsY=max(z['maxAbsY'] for z in outs));return top
def main():
    p=src.template(argparse.ArgumentParser())
    for k in ('source','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();g=src.load(a);f=Field(g,a.source);obs=[]
    for n,na,shift in [(521,145,False),(473,173,True)]:
        rr,_=g.src.grid(n,12,shift);theta=(np.arange(na)+.5)/(na)*np.pi/2 if shift else np.linspace(0,np.pi/2,na)
        q=stats(f,rr,theta);obs.append(dict(radial=len(rr),quarterAngular=len(theta),actual=q));print(obs[-1],flush=True)
    raw=g.src.original(np.flatnonzero(g.src.tail['r']<=g.src.rb[0]+1e-14));rr=np.unique(raw,axis=0);q=stats(f,rr,(np.arange(60)+.5)/60*np.pi/2);print('native',q,flush=True)
    result=dict(schema='r289-cubic-new-literal-material-differential-observation',entrySHA=g.m.base.sha(__file__),sourceSHA=g.m.base.sha(a.source),spans=[f.N,f.M],major=f.A,Z=f.Z,materialT=g.T,observers=obs,native=dict(rawRows=len(raw),distinct=len(rr),quarterAngles=60,actual=q))
    with a.out.open('x') as o:json.dump(result,o,indent=2);o.write('\n')
if __name__=='__main__':main()

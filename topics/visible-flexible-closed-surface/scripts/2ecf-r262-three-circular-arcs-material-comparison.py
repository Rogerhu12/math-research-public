#!/usr/bin/env python3
"""Compare the true R262 equal-perimeter inlet to the R299 successor with three genuine circular patches per orbit."""
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import betainc

P=2*np.pi/3
LOW=.04
L0=.915
L1=1.09
TAU=(P-L0-L1)/2
HIGH=(P-LOW*(L0+TAU))/(L1+TAU)

def target_angle(u,anchor=0.):
    w=np.asarray(u)+anchor
    j=np.floor((w+P/2)/P).astype(int)
    v=w-j*P
    x=np.clip((np.abs(v)-L0/2)/TAU,0,1)
    S=betainc(8,8,x)
    integral=x*S-.5*betainc(9,8,x)
    beta=LOW*np.abs(v)+(HIGH-LOW)*(TAU*integral+np.maximum(0,np.abs(v)-L0/2-TAU))
    return j*P+np.sign(v)*beta-anchor,LOW+(HIGH-LOW)*S

def native_coeff(row):
    M=(len(row)-2)//3
    assert len(row)==3*M+2 and np.count_nonzero(row[2*M+1:])==0
    ks=[1]
    cs=[row[0]]
    for i in range(1,M+1):
        ks.extend((1+3*i,1-3*i))
        cs.extend(((row[i]+row[M+i])/2,(row[i]-row[M+i])/2))
    return np.array(ks),np.array(cs)

def periodic_primitive(v):
    n=len(v)
    freq=np.fft.fftfreq(n,1/n)
    raw=np.fft.fft(v)
    raw[0]=0
    raw[1:]/=1j*freq[1:]
    return np.fft.ifft(raw)

class MaterialCenter:
    """One exact geometric definition, evaluated in float via smooth periodic arc inversion."""
    def __init__(self,row,n=16384):
        self.n=n
        self.u=np.arange(n)*2*np.pi/n
        self.k,self.c=native_coeff(row)
        z,v,a=self.native(self.u)
        speed=np.abs(v)
        self.mean=float(np.mean(speed))
        ac=periodic_primitive(speed/self.mean-1).real
        U=self.u+ac-ac[0]
        self.inv=CubicSpline(np.r_[U,2*np.pi],np.r_[self.u,2*np.pi])
        assert np.diff(U).min()>0
    def native(self,t):
        w=np.exp(1j*np.asarray(t)[:,None]*self.k[None,:])
        return [w@(self.c*(1j*self.k)**d) for d in range(3)]
    def original(self,u):
        v=np.asarray(u)%(2*np.pi)
        z,z1,z2=self.native(self.inv(v))
        speed=np.abs(z1)
        T=z1/speed
        N=-1j*T
        curvature=self.mean*np.imag(np.conj(z1)*z2)/speed**3
        return z/self.mean,T,N,curvature

def periodic_interp(v,t):
    n=len(v)
    grid=np.arange(n+1)*2*np.pi/n
    return CubicSpline(grid,np.r_[v,v[0]],bc_type='periodic')(np.asarray(t)%(2*np.pi))

class Transition:
    def __init__(self,center,anchor,lam):
        u=center.u
        z,T,N,k=center.original(u)
        b0=np.unwrap(np.angle(N))
        b0-=round(b0[0]/(2*np.pi))*2*np.pi
        b3,k3=target_angle(u,anchor)
        beta=(1-lam)*b0+lam*b3
        self.k=(1-lam)*k+lam*k3
        self.N=np.exp(1j*beta)
        self.T=1j*self.N
        self.z=periodic_primitive(self.T)
        self.velocity=periodic_primitive(-(b3-b0)*self.N)
    def at(self,u):
        return tuple(periodic_interp(v,u) for v in (self.z,self.T,self.N,self.k,self.velocity))

def measure(center):
    u=center.u
    original= center.original(u)
    rows=[]
    for anchor in (0.,np.pi/3):
        front=Transition(center,anchor,1.)
        levels=[]
        for lam in (0.,1/4096,1/256,1/32,1/4,1.):
            g=Transition(center,anchor,lam)
            dp=g.z-original[0]
            angle=np.angle(g.N*np.conj(original[2]))
            levels.append(dict(lam=lam,maxPosition=float(abs(dp).max()),rmsPosition=float(np.sqrt(np.mean(abs(dp)**2))),maxTangentAngle=float(abs(angle).max()),
                 curvatureRange=[float(g.k.min()),float(g.k.max())],maxCurvatureChange=float(abs(g.k-original[3]).max()),
                 maxPhysicalVelocity=float(abs(g.velocity).max()),axisRadii=[float(g.z[0].real),float(np.real(periodic_interp(g.z,[np.pi/3])[0]*np.exp(-1j*np.pi/3)))],
                 D3ClosureResidual=float(abs(np.mean(g.T))),unitSpeedError=float(abs(abs(g.T)-1).max())))
        rows.append(dict(anchor=anchor,levels=levels))
    # Allow independent rigid rotation only for this descriptive search. The two exact
    # reflection-compatible anchors above are the sources used by the continuation.
    opt=[]
    for shift in np.linspace(0,P,129)[:-1]:
        beta,k3=target_angle(u,shift)
        z=periodic_primitive(1j*np.exp(1j*beta))
        rot=np.angle(np.vdot(z,original[0]))
        d=np.abs(z*np.exp(1j*rot)-original[0])
        opt.append((float(np.sqrt(np.mean(d*d))),float(d.max()),float(shift),float(rot)))
    return dict(rawMeanArcSpeed=center.mean,sourceAxes=[float(original[0][0].real),float(np.real(periodic_interp(original[0],[np.pi/3])[0]*np.exp(-1j*np.pi/3)))],
                sourceCurvatureRange=[float(original[3].min()),float(original[3].max())],targetHigh=HIGH,targetLow=LOW,targetTransition=TAU,aligned=rows,
                bestRmsAfterDescriptiveRigidAngularSearch=min(opt))
def main():
    global LOW,HIGH
    p=argparse.ArgumentParser()
    group=p.add_mutually_exclusive_group(required=True)
    group.add_argument('--data',type=Path)
    group.add_argument('--coeff-json',type=Path)
    p.add_argument('--nodes',type=int,default=12288)
    p.add_argument('--low',type=float,nargs='+',default=[.04,.25,.35])
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.data:
        with gzip.open(a.data,'rb') as f:
            with np.load(f) as dd:row=dd['jets'][0,0].copy()
        src=hashlib.sha256(a.data.read_bytes()).hexdigest()
    else:
        old=json.loads(a.coeff_json.read_text())
        row=np.array([float.fromhex(t) for t in old['originalCentralNativeHex']])
        src=old['sourceDataSHA256']
    out=dict(schema='R262-D3-three-true-circular-plateau-unit-speed-material-comparison-v1',entrySHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),sourceDataSHA256=src,originalCentralNativeHex=[float(x).hex() for x in row],geometry=dict(period=P,lowLength=L0,highLength=L1,transition=TAU,operatingPhase=.41),observations=[])
    for n in (a.nodes,a.nodes*2):
        center=MaterialCenter(row,n)
        for low in a.low:
            LOW=low
            HIGH=(P-LOW*(L0+TAU))/(L1+TAU)
            data=measure(center)
            out['observations'].append(dict(uniformPhysicalAngles=n,**data))
            print('TRUE D3 INLET',n,low,data['sourceCurvatureRange'],[(r['anchor'],r['levels'][-1]['maxPosition'],r['levels'][-1]['maxTangentAngle']) for r in data['aligned']],flush=True)
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
if __name__=='__main__':main()

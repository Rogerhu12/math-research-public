#!/usr/bin/env python3
"""Independent cap/warp reconstruction and adaptive physical-height linear audit.
Consumes exported raw source coefficients, not the author's warped functions or
RK propagator. Numerical estimates only; no interval or nonlinear certificate.
"""
import argparse,gzip,hashlib,json,math
from pathlib import Path
import numpy as np
from scipy.integrate import quad_vec,solve_ivp
from scipy.optimize import brentq,minimize_scalar


def smooth(x):return x*x*x*(10+x*(-15+6*x))
def dsmooth(x):return 30*x*x*(1-x)*(1-x)
def capped(z,dz,C,L):
    if C<=0:return z,dz
    c=math.log(C)
    if z<=c-L:return z,dz
    if z>=c+L:return c,0.
    t=(z-c+L)/(2*L)
    def S(v):return v**4*(35-84*v+70*v*v-20*v**3)
    def J(v):return v**5*(7-14*v+10*v*v-2.5*v**3)
    if t<=.5:I=t-J(t);derivative=1-S(t)
    else:I=.5-J(1-t);derivative=S(1-t)
    return c-L+2*L*I,derivative*dz

class Entry:
    def __init__(self,tail,n,j,raw):
        self.tail=tail;self.n=n;self.j=j;self.raw=raw
        self.breaks=[]
        grid=np.linspace(0,1,257)
        functions=[lambda x:self.data(x)[1]]
        if tail.C>0:
            for lev in [math.log(tail.C)-tail.L,math.log(tail.C)+tail.L]:
                functions.append(lambda x,lev=lev:self.raw_data(x)[0]-lev)
        for f in functions:
            a=0.;fa=f(a)
            for b in grid[1:]:
                fb=f(float(b))
                if fa*fb<0:self.breaks.append(brentq(f,a,float(b),xtol=5e-15))
                a=float(b);fa=fb
        self.breaks=sorted(set(self.breaks))
        self.total=self.integral(0,1)
    def raw_data(self,x):
        q=self.raw;k=q['k'];r=q['r0']*math.exp(k*x)
        z=q['logw0']+q['logSmoothCoefficient']*smooth(x)-7*k*x
        dz=q['logSmoothCoefficient']*dsmooth(x)-7*k
        beta=self.tail.valleys[self.n] if self.n<len(self.tail.valleys) else 0.
        if self.j==3:z+=beta*smooth(x);dz+=beta*dsmooth(x)
        if self.j==4:z+=beta
        if self.j==5:z+=beta*(1-smooth(x));dz-=beta*dsmooth(x)
        return z,dz,r,k*r
    def data(self,x):
        z,dz,r,rx=self.raw_data(x);t=self.tail
        zc,dzc=capped(z,dz,t.C,t.L)
        last=len(t.rawcells[self.n]['profiles'])-1
        if self.n==0 and self.j==last:zc,dzc=z,dz
        elif self.n==0 and self.j==last-1:
            eta=1-smooth(x);de=-dsmooth(x)
            zc,dzc=z+eta*(zc-z),dz+eta*(dzc-dz)+de*(zc-z)
        chi=1.;j0=1.
        if self.n==t.N-1 and self.j==0:chi=smooth(x)
        if self.n==0 and self.j==last:
            chi=1-smooth(x);j0=1+(t.rCut/t.oldCut-1)*smooth(x)
        w=math.exp(zc);E=1+w*w
        v=abs(w*dzc)/(E**1.5)
        A=abs(rx)*j0*(1-chi)+chi*v/t.K
        B=chi*abs(rx)/E
        return zc,dzc,r,rx,A,B
    def integrand(self,x):
        z,dz,r,rx,A,B=self.data(x);w=math.exp(z);root=math.sqrt(1+w*w)
        return np.array([A,B,root*A,root*B,w*A,w*B])
    def integral(self,a,b):
        if a==b:return np.zeros(6)
        points=[p for p in self.breaks if a<p<b]
        val,err=quad_vec(self.integrand,a,b,epsabs=1e-35,epsrel=2e-12,points=points,limit=400,norm='max')
        return val
    def profile(self,x):
        z,dz,r,rx,A,B=self.data(x)
        if x==0:rr=self.start
        elif x==1:rr=self.end
        else:
            q=self.integral(0,x);rr=self.start+self.tail.sigma*(q[0]+self.tail.alpha*q[1])
        dr=self.tail.sigma*(A+self.tail.alpha*B)
        return rr,dr,z,dz

class Tail:
    def __init__(self,d):
        self.d=d;self.rawcells=d['source'];self.N=len(self.rawcells);p=d['parameters']
        self.rCut=p['rCut'];self.oldCut=p['oldCut'];self.C=p['slopeCap'];self.L=p['capTransition'];self.K=p['curvatureBound'];self.sigma=p['orientation'];self.valleys=p['valleyControls']
        self.entries=[];self.bykey={}
        for n in range(self.N-1,-1,-1):
            for j,raw in enumerate(self.rawcells[n]['profiles']):
                e=Entry(self,n,j,raw);self.entries.append(e);self.bykey[(n,j)]=e
        sums=np.sum([e.total for e in self.entries],axis=0)
        self.deep=self.rawcells[-1]['profiles'][0]['r0']
        target=self.sigma*(self.rCut-self.deep);self.alpha=(target-sums[0])/sums[1]
        if self.alpha<=0:raise ValueError('negative radial warp')
        accumulated=0.
        for e in self.entries:
            e.start=self.deep+self.sigma*accumulated
            accumulated+=e.total[0]+self.alpha*e.total[1]
            e.end=self.deep+self.sigma*accumulated
        self.stats={'alpha':self.alpha,'minimumWarpWidth':sums[0],'heightSpan':sums[4]+self.alpha*sums[5],'meridianLength':sums[2]+self.alpha*sums[3],'cutRadius':self.entries[-1].end,'rootStatDifferences':{}}
        for key in ['alpha','minimumWarpWidth','heightSpan','meridianLength']:
            self.stats['rootStatDifferences'][key]=self.stats[key]-d['rootStats'][key]
    def geometry_audit(self):
        errors={k:0. for k in ['r','drdx','logw','dlogwdx']}
        for s in self.d['samples']:
            vals=self.bykey[(s['n'],s['j'])].profile(s['x'])
            for k,v in zip(errors,vals):errors[k]=max(errors[k],abs(v-s[k]))
        joins={k:0. for k in ['r','w','w_r']}
        for a,b in zip(self.entries[:-1],self.entries[1:]):
            ga=a.profile(1);gb=b.profile(0)
            va=[ga[0],math.exp(ga[2]),math.exp(ga[2])*ga[3]/ga[1]]
            vb=[gb[0],math.exp(gb[2]),math.exp(gb[2])*gb[3]/gb[1]]
            for k,x,y in zip(joins,va,vb):joins[k]=max(joins[k],abs(x-y))
        cut=self.entries[-1].profile(1);deep=self.entries[0].profile(0)
        maxkr=0.;where=None;maxw=0.
        for e in self.entries:
            def kr(x):
                z,dz,r,rx,A,B=e.data(x);w=math.exp(z)
                return abs(w*dz)/((1+w*w)**1.5*(A+self.alpha*B))
            grid=np.unique(np.r_[np.linspace(0,1,129),e.breaks])
            vals=np.array([kr(float(x)) for x in grid])
            k=int(np.argmax(vals)); candidates=[(float(vals[k]),float(grid[k]))]
            if 0<k<len(grid)-1:
                sol=minimize_scalar(lambda x:-kr(x),bounds=(grid[k-1],grid[k+1]),method='bounded',options={'xatol':1e-13})
                candidates.append((-sol.fun,sol.x))
            kval,x=max(candidates)
            if kval>maxkr:maxkr=kval;where=[e.n,e.j,x]
            maxw=max(maxw,max(math.exp(e.data(float(x))[0]) for x in grid))
        return {'reconstructionMaxAbsoluteDifferences':errors,'maximumInterfaceJump':joins,
            'cut':{'r':cut[0],'w':math.exp(cut[2]),'w_r':math.exp(cut[2])*cut[3]/cut[1],
                   'expected_w_r':-7*self.d['parameters']['wCut']/self.rCut},
            'deep':{'r':deep[0],'w':math.exp(deep[2]),'drdx':deep[1]},
            'meridianCurvatureOptimizedEstimate':maxkr,'meridianCurvatureWhere':where,
            'slopeSampleMax':maxw,'azimuthalCurvatureUpperFromSampleW':maxw/(self.deep*math.sqrt(1+maxw*maxw))}
    def linear(self,mode,far,rtol=2e-11):
        p=self.d['parameters'];first=self.bykey[(far-1,0)];r=first.start;w=math.exp(first.data(0)[0]);cell=self.rawcells[far-1]
        if mode==2:z=0.
        else:
            R=p['R'];a=p['a'];nu=mode*mode*(mode*mode-1)/12;rho=2**a;c=1+1/R
            a00=1-c*nu*R;a10=(-nu*(1+R)+c*nu*nu*R)/rho;a11=(1-c*nu)/rho
            tr=a00+a11;lam=(tr-math.sqrt(tr*tr-4/rho))/2;z=a10/(lam-a11)
        slope=mode*mode/r+self.sigma*math.sqrt(12)*cell['mu']*z/(r**8*w)
        scale=mode*mode/self.rCut;initial=np.array([1.,slope/scale]);norm=np.linalg.norm(initial);y=initial/norm;ln=math.log(norm)
        records=[];radial_error=0.;nfev=0
        for n in range(far-1,-1,-1):
            for j in range(len(self.rawcells[n]['profiles'])):
                e=self.bykey[(n,j)]
                def rhs(x,Y):
                    z,dz,ro,rx,A,B=e.data(x);dr=self.sigma*(A+self.alpha*B)
                    return [dr,dr*scale*Y[2],-dz*(Y[2]-mode*mode*Y[1]/(Y[0]*scale))]
                sol=solve_ivp(rhs,(0,1),[e.start,*y],method='DOP853',rtol=rtol,atol=rtol*1e-3,dense_output=True,max_step=.125)
                if not sol.success:raise ValueError(sol.message)
                nfev+=sol.nfev
                radial_error=max(radial_error,abs(sol.y[0,-1]-e.end))
                if mode==2:records.append((e,sol.sol,ln))
                v=sol.y[1:,-1];norm=float(np.linalg.norm(v));y=v/norm;ln+=math.log(norm)
        outerlog=ln+math.log(abs(y[0]));outersign=math.copysign(1.,y[0]);out={'mode':mode,'far':far,'solver':'DOP853','rtol':rtol,'cutSlope':scale*y[1]/y[0],'logHeightGain':outerlog,'radialODESegmentError':radial_error,'nfev':nfev}
        if mode==2:
            best=(float('inf'),None);samplebest=(float('inf'),None);maxheight=0.;maxderivative=0.
            def evaluate(e,sol,l,x):
                Y=sol(x);rr=float(Y[0]);lw=e.data(float(x))[0];ww=math.exp(lw);E=1+ww*ww
                ff=float(Y[1])*outersign*math.exp(l-outerlog);fr=scale*float(Y[2])*outersign*math.exp(l-outerlog)
                base=rr*ww/E;lin=rr*fr/E-mode*mode*ff;crit=base/abs(lin) if lin else float('inf')
                row={'cell':e.n,'segment':e.j,'x':float(x),'r':rr,'w':ww,'f':ff,'fr':fr,'baseT':base,'linearT':lin}
                return crit,row
            for e,sol,l in records:
                # A dense output from adaptive integration, independent of the author's RK grid.
                grid=np.unique(np.r_[np.linspace(0,1,513),e.breaks]);vals=[]
                for x in grid:
                    c,row=evaluate(e,sol,l,float(x));vals.append(c)
                    maxheight=max(maxheight,abs(row['f']));maxderivative=max(maxderivative,abs(row['fr']))
                    if c<samplebest[0]:samplebest=(c,row)
                k=int(np.argmin(vals));c,row=evaluate(e,sol,l,float(grid[k]))
                if c<best[0]:best=(c,row)
                if 0<k<len(grid)-1 and c<10*samplebest[0]:
                    res=minimize_scalar(lambda x:evaluate(e,sol,l,x)[0],bounds=(grid[k-1],grid[k+1]),method='bounded',options={'xatol':2e-13})
                    c,row=evaluate(e,sol,l,res.x)
                    if c<best[0]:best=(c,row)
            out.update(linearTThresholdSample=samplebest[0],linearTThresholdOptimizedEstimate=best[0],thresholdLocation=best[1],normalizedHeightMaxSample=maxheight,normalizedDerivativeMaxSample=maxderivative)
        return out

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('input',type=Path);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--far',type=int,nargs='+',default=[24,32,48,80]);ap.add_argument('--modes',type=int,nargs='+',default=[2]);ap.add_argument('--rtol',type=float,default=2e-11);a=ap.parse_args()
    with gzip.open(a.input,'rt') as h:d=json.load(h)
    t=Tail(d);out={'scope':__doc__,'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),'audited_scripts_sha256':d['hashes'],'stats':t.stats,'geometry':t.geometry_audit(),'rows':[]}
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'stats':out['stats'],'geometry':out['geometry']}),flush=True)
    for mode in a.modes:
        for far in a.far:
            row=t.linear(mode,far,a.rtol);out['rows'].append(row);a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(row),flush=True)
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Independent nonsubtractive linear coordinates for the same frozen metric.
V=f/r^4, pi=sigma*r^4*w*(f_r-m^2*f/r)/(sqrt(12)*mu).
No author linear propagation code is invoked. No nonlinear claim.
"""
import argparse,gzip,json,math,hashlib
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar
from audit_cut_tail import Tail

def run(t,mode,far,rtol):
    p=t.d['parameters'];first=t.bykey[(far-1,0)];r=first.start;nu=mode*mode*(mode*mode-1)/12
    if mode==2:z=0.
    else:
        R=p['R'];rho=2**p['a'];alpha=1+1/R
        a00=1-alpha*nu*R;a10=(-nu*(1+R)+alpha*nu*nu*R)/rho;a11=(1-alpha*nu)/rho
        tr=a00+a11;lam=(tr-math.sqrt(tr*tr-4/rho))/2;z=a10/(lam-a11)
    yy=np.array([1/r**4,z/r**4]);norm=np.linalg.norm(yy);y=yy/norm;ln=math.log(norm)
    prev_mu=t.rawcells[far-1]['mu'];records=[];nfev=0;radial_error=0.
    for n in range(far-1,-1,-1):
        mu=t.rawcells[n]['mu'];y[1]*=prev_mu/mu
        norm=np.linalg.norm(y);y/=norm;ln+=math.log(norm);prev_mu=mu
        for j in range(len(t.rawcells[n]['profiles'])):
            e=t.bykey[(n,j)]
            def rhs(x,Y):
                lw,dlw,ro,rx,A,B=e.data(x);dr=t.sigma*(A+t.alpha*B);rr=Y[0]
                dtau=t.sigma*math.sqrt(12)*dr/rr;k=t.sigma*(mode*mode-4)/math.sqrt(12)
                P=math.exp(7*math.log(rr)+lw-math.log(mu))
                return [dr,dtau*k*Y[1]+(dtau/P)*Y[2],(-nu*dtau*P)*Y[1]-dtau*k*Y[2]]
            sol=solve_ivp(rhs,(0,1),[e.start,*y],method='DOP853',rtol=rtol,atol=rtol*1e-3,max_step=.125,dense_output=True)
            if not sol.success:raise RuntimeError(sol.message)
            nfev+=sol.nfev;radial_error=max(radial_error,abs(sol.y[0,-1]-e.end))
            if mode in (2,3):records.append((e,sol.sol,ln,mu))
            yy=sol.y[1:,-1];norm=np.linalg.norm(yy);y=yy/norm;ln+=math.log(norm)
    cut=t.entries[-1].profile(1);r=cut[0];w=math.exp(cut[2]);mu=t.rawcells[0]['mu']
    outerlog=ln+math.log(abs(r**4*y[0]));outersign=math.copysign(1.,y[0]);cutSlope=mode*mode/r+t.sigma*math.sqrt(12)*mu*y[1]/(r**8*w*y[0])
    out={'mode':mode,'far':far,'solver':'DOP853 in independently derived momentum variables','rtol':rtol,'cutSlope':cutSlope,'logHeightGain':outerlog,'radialODESegmentError':radial_error,'nfev':nfev}
    if mode in (2,3):
        best=(float('inf'),None);sample=(float('inf'),None);maxheight=0.;maxderivative=0.
        def point(e,sol,l,mu,x):
            Y=sol(x);rr=float(Y[0]);lw=e.data(float(x))[0];w=math.exp(lw);E=1+w*w
            fact=outersign*math.exp(l-outerlog)
            f=rr**4*float(Y[1])*fact
            fr=(mode*mode*rr**3*float(Y[1])+t.sigma*math.sqrt(12)*mu*float(Y[2])/(rr**4*w))*fact
            base=rr*w/E;lin=rr*fr/E-mode*mode*f;crit=base/abs(lin) if lin else float('inf')
            return crit,{'cell':e.n,'segment':e.j,'x':float(x),'r':rr,'w':w,'f':f,'fr':fr,'baseT':base,'linearT':lin}
        for e,sol,l,mu in records:
            grid=np.unique(np.r_[np.linspace(0,1,513),e.breaks]);vals=[]
            for x in grid:
                c,row=point(e,sol,l,mu,float(x));vals.append(c)
                maxheight=max(maxheight,abs(row['f']));maxderivative=max(maxderivative,abs(row['fr']))
                if c<sample[0]:sample=(c,row)
            k=int(np.argmin(vals));c,row=point(e,sol,l,mu,float(grid[k]))
            if c<best[0]:best=(c,row)
            if 0<k<len(grid)-1 and c<10*sample[0]:
                res=minimize_scalar(lambda x:point(e,sol,l,mu,x)[0],bounds=(grid[k-1],grid[k+1]),method='bounded',options={'xatol':2e-13})
                c,row=point(e,sol,l,mu,res.x)
                if c<best[0]:best=(c,row)
        out.update(linearTThresholdSample=sample[0],linearTThresholdOptimizedEstimate=best[0],thresholdLocation=best[1],normalizedHeightMaxSample=maxheight,normalizedDerivativeMaxSample=maxderivative)
    return out

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('input',type=Path);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--far',type=int,nargs='+',default=[24,32,48,80]);ap.add_argument('--modes',type=int,nargs='+',default=[2]);ap.add_argument('--rtol',type=float,default=2e-12);a=ap.parse_args()
    with gzip.open(a.input,'rt') as h:d=json.load(h)
    t=Tail(d);out={'scope':__doc__,'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),'audited_scripts_sha256':d['hashes'],'stats':t.stats,'rows':[]}
    for mode in a.modes:
        for far in a.far:
            row=run(t,mode,far,a.rtol);out['rows'].append(row);a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(row),flush=True)
if __name__=='__main__':main()

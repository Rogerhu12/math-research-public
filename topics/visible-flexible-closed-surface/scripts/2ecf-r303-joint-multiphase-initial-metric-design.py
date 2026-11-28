#!/usr/bin/env python3
"""Design one bendable initial induced metric jointly with multiple spatial phases, then freeze it."""
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[k]='1'
import numpy as np
from scipy.linalg import cho_factor,cho_solve
from scipy.spatial.transform import Rotation

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def displace(x,shape):
    return np.max(np.linalg.norm(x.reshape(shape),axis=0).sum(axis=-1))

def reset(grids,states,m):
    q=grids[0].jets(*states[0])
    target=m.CommonTarget(q)
    for p in grids:
        p.target=target

def observe(grids,states,m):
    reset(grids,states,m)
    return [p.report(*z) for p,z in zip(grids,states)]

def loss(grids,states,m,deltas):
    reset(grids,states,m)
    values=[]
    maximum=0.
    for j in range(1,len(grids)):
        e=grids[j].target.measure(grids[j].jets(*states[j]))[1]
        w=max(.01,deltas[j-1])
        values.append(np.mean((e/w)**6))
        maximum=max(maximum,float(e.max()/w))
    return np.mean(values)**(1/6)+.11*maximum

def blocks(grids,states,m,deltas,power):
    reset(grids,states,m)
    p0=grids[0]
    n=p0.nvar
    M0,_,_=p0.linear(*states[0],0.)
    M0=M0.reshape(3,-1,n+6)[:,:,:n]
    C=np.zeros((n,n))
    b=np.zeros(n)
    out=[]
    for j,p in enumerate(grids[1:],1):
        M,r,e=p.linear(*states[j],0.)
        G=p.target.measure(p.jets(*states[j]))[0]
        E=1+G[0].reshape(-1,1)
        F=G[1].reshape(-1,1)
        Z=1+G[2].reshape(-1,1)
        # Exact derivative of the reference-dependent Cholesky normalization.
        # M0 represents de/e, sqrt(2)(df-r de)/sqrt(eh), dh/h.
        raw=M.reshape(3,-1,n+6)
        shared=raw[:,:,:n].copy()
        shared[0]-=E*M0[0]
        shared[1]-=E*M0[1]+.5*F*(M0[0]+M0[2])
        shared[2]-=F*M0[1]+Z*M0[2]
        weight=np.maximum(.05,e/max(float(e.max()),1e-25))**power/max(deltas[j-1],.01)
        w=weight.ravel()[:,None]
        shared*=w[None,:,:]
        raw*=w[None,:,:]
        r=r.reshape(3,-1)*w[:,0]
        A=shared.reshape(-1,n)
        M=raw.reshape(-1,n+6)
        r=r.ravel()
        C+=A.T@A
        b+=A.T@r
        out.append((M.T@M,A.T@M,M.T@r))
    return C,b,out

def direction(C,b,groups,damp,x,shape,budget,trust):
    D=C.copy()
    c=b.copy()
    data=[]
    for H,B,v in groups:
        mat=H+np.diag(damp*np.maximum(1e-8,np.diag(H))+1e-13)
        ch=cho_factor(mat,lower=True)
        Z=cho_solve(ch,B.T)
        y=cho_solve(ch,v)
        D-=B@Z;c-=B@y
        data.append((Z,y))
    D=(D+D.T)/2
    D+=np.diag(damp*np.maximum(1.e-8,np.diag(C))+1e-12)
    z=cho_solve(cho_factor(D,lower=True),-c)
    change=displace(z,shape)
    if change>trust:
        z*=trust/change
    if displace(x+z,shape)>budget:
        lo=0.;hi=1.
        for _ in range(30):
            t=(lo+hi)/2
            if displace(x+t*z,shape)<=budget:lo=t
            else:hi=t
        z*=lo
    # After limiting the physical initial displacement, recompute the best
    # local phase steps conditional on this actual common step.
    return z,[-y-Z@z for Z,y in data]

def update(states,z,local,scale,n):
    out=[(states[0][0]+scale*z,np.eye(3),np.zeros(3))]
    for st,v in zip(states[1:],local):
        x,R,T=st
        out.append((x+scale*(z+v[:n]),Rotation.from_rotvec(scale*v[n:n+3]).as_matrix()@R,T+scale*v[n+3:]))
    return out

def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','solver','joint','field','out'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--deltas',nargs='+',type=float,default=[1/64,1/16,.25])
    p.add_argument('--seed-states',nargs='+',type=Path)
    p.add_argument('--base-budget',type=float,default=.018)
    p.add_argument('--base-trust',type=float,default=.0035)
    p.add_argument('--curvature-guide',type=float,default=8.82)
    p.add_argument('--freeze-initial',action='store_true')
    p.add_argument('--ramp-spans',type=int,default=3)
    p.add_argument('--phase-interior',type=int,default=1)
    for k,v in (('c',.78),('length',.58),('gate',.10),('cap-radius',.94),('cap-height',.32)):
        p.add_argument('--'+k,type=float,default=v)
    for k,v in (('spans',6),('modes',5),('angles',48),('radial',19),('independent',144),('test-radial',45),('steps',14)):
        p.add_argument('--'+k,type=int,default=v)
    a=p.parse_args()
    assert 0<min(a.deltas) and max(a.deltas)<=.5 and np.all(np.diff(a.deltas)>0)
    m=load(a.joint,'r303Joint')
    cl=load(a.solver,'r303Whole')
    ds=[0.]+a.deltas
    P=[m.PhaseGrid(cl,a,v,a.angles,a.radial,.347,True) for v in ds]
    Q=[m.PhaseGrid(cl,a,v,a.independent,a.test_radial,.629,False) for v in ds]
    n=P[0].nvar
    states=[(np.zeros(n),np.eye(3),np.zeros(3)) for d in ds]
    if a.seed_states:
        if len(a.seed_states)!=len(ds):raise ValueError('Need initial state and one state per listed phase')
        for j,file in enumerate(a.seed_states):
            with np.load(file) as zz:
                if abs(ds[j]-float(zz['delta']))>1e-15:raise ValueError('wrong saved phase')
                states[j]=(m.transfer(zz,P[j]),zz['rotation'].copy(),zz['translation'].copy())
        if not np.allclose(states[0][1],np.eye(3)) or np.linalg.norm(states[0][2])>1e-14:
            raise ValueError('This branch fixes the reference cap frame')
    baseline=observe(Q,states,m)
    hist=[]
    for step in range(a.steps):
        old=loss(P,states,m,a.deltas)
        C,b,B=blocks(P,states,m,a.deltas,.45 if step<5 else .95)
        best=None
        for damp in (2e-8,2e-6,1e-4,.003,.035):
            try:
                dz,dy=direction(C,b,B,damp,states[0][0],P[0].shape,a.base_budget,0. if a.freeze_initial else a.base_trust)
            except np.linalg.LinAlgError:
                continue
            for scale in (1.,.5,.25,.125,.0625):
                trial=update(states,dz,dy,scale,n)
                score=loss(P,trial,m,a.deltas)
                if score>=old or best is not None and score>=best[0]:continue
                values=observe(P,trial,m)
                if a.curvature_guide>0 and max(v['curvature'] for v in values)>a.curvature_guide:continue
                best=(score,trial,values,scale,damp)
        if best is None:break
        score,states,rr,scale,damp=best
        row=dict(step=step+1,scale=scale,damping=damp,normalizedObjective=score,basePhysicalL1UpperAtBinaryEvaluation=float(displace(states[0][0],P[0].shape)),phases=rr)
        hist.append(row)
        print(json.dumps(row),flush=True)
    final=observe(Q,states,m)
    between=[]
    for j in range(len(ds)-1):
        a0,x0,R0,T0=ds[j],*states[j]
        a1,x1,R1,T1=ds[j+1],*states[j+1]
        rotation=Rotation.from_matrix(R1@R0.T).as_rotvec()
        for frac in np.arange(1,a.phase_interior+1)/(a.phase_interior+1):
            d=a0+(a1-a0)*frac
            q=m.PhaseGrid(cl,a,d,a.independent,a.test_radial,.629,False)
            q.target=Q[0].target
            heat=q.report((1-frac)*x0+frac*x1,Rotation.from_rotvec(frac*rotation).as_matrix()@R0,(1-frac)*T0+frac*T1)
            between.append(dict(delta=float(d),data=heat))
    a.out.parent.mkdir(parents=True,exist_ok=True)
    saved=[]
    for j,(x,R,T) in enumerate(states):
        f=a.out.with_name(a.out.stem+'-phase'+str(j)+'.npz')
        with f.open('xb') as fd:
            np.savez_compressed(fd,delta=ds[j],coefficients=x,rotation=R,translation=T,knots=P[j].knots,modes=a.modes)
        saved.append(dict(filename=f.name,sha256=digest(f)))
    # Directed l1 bound on the actual stored float64 coefficients. sqrt is
    # enclosed by a rational fixedpoint ceiling for each vector.
    from fractions import Fraction as F
    import math
    unit=2**54
    coeff=states[0][0].reshape(P[0].shape)
    exactbudget=F(0)
    for k in range(coeff.shape[1]):
        line=F(0)
        for h in range(coeff.shape[2]):
            u=sum(F(float(co))**2 for co in coeff[:,k,h])
            q=math.isqrt(u.numerator*unit**2//u.denominator)
            line+=F(q if q*q*u.denominator==u.numerator*unit**2 else q+1,unit)
        exactbudget=max(exactbudget,line)
    report=dict(schema='R303-multiphase-new-initial-intrinsic-metric-joint-XYZ-v1',entrySHA256=digest(Path(__file__)),solverSHA256=digest(a.solver),jointSHA256=digest(a.joint),inputFieldSHA256=digest(a.field),parameters={k:v for k,v in vars(a).items() if k not in ('scripts','solver','joint','field','out','seed_states')},phases=ds,variables=n*(len(ds))+6*(len(ds)-1),initialFullObservations=baseline,accepted=hist,finalSameMetricObservations=final,genuineIntermediatePhases=between,states=saved,initialWNormRigorousUpper=str(exactbudget),
        frozenMetricDefinition='The actual first fundamental form of the final saved initial spatial state on all material points, including the native finite ramp, the closing strip, the initial C3 central components and fixed cap surfaces.',
        scope='The two nonzero phases and the interpolated phases use this one metric. A subsequent --freeze-initial run can refine the same metric by exact spline-space insertion. The full initial position change is bounded by the rowwise sum of exact Euclidean control-vector norms.')
    with a.out.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
    print('FINAL',json.dumps(dict(deltas=ds,initialW=str(exactbudget),peaks=[r['peak'] for r in final],interior=[r['data']['peak'] for r in between])),flush=True)
if __name__=='__main__':main()

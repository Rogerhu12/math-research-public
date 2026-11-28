#!/usr/bin/env python3
"""Banded Gram descent with supporting affine constraints from the actual second fundamental form."""
import numpy as np
from scipy.linalg import cho_solve_banded, cholesky_banded, eigh, LinAlgError
from scipy.optimize import minimize

def material_jets(G,X):
    J=G.base.copy()
    for i,(r,d) in enumerate(G.orders):
        J[:,i]+=G.forward_field(X,r,d)
    return J

def tangent_data(J):
    P,vs,vu,ss,su,uu=J
    I=np.array([[vs@vs,vs@vu],[vs@vu,vu@vu]])
    N=np.cross(vs,vu)
    N/=np.linalg.norm(N)
    II=np.array([[N@ss,N@su],[N@su,N@uu]])
    return I,II,N

def signed_wall(J,v,sgn,limit):
    # The signed form on v=(a,b) is sgn*II(v,v)-limit*I(v,v).
    # Its nonpositivity for both signs and all v is precisely the curvature bound.
    P,vs,vu,ss,su,uu=J
    I,II,N=tangent_data(J)
    v=v/np.sqrt(v@I@v);a,b=v
    t=a*vs+b*vu
    acc=a*a*ss+2*a*b*su+b*b*uu
    gamma=np.linalg.solve(I,[vs@acc,vu@acc])
    base=sgn*(N@acc)-limit*(t@t)
    coefficients=np.array([np.zeros(3),-sgn*gamma[0]*N-2*limit*a*t,
        -sgn*gamma[1]*N-2*limit*b*t,sgn*a*a*N,sgn*2*a*b*N,sgn*b*b*N])
    return coefficients,-base,v

def field_row(G,i,j,coefficients):
    R=np.zeros(G.shape)
    for h,(r,d) in enumerate(G.orders):
        R+=G.B[r][i,:,None]*(coefficients[h]@G.phi[d,:,:,j])[None,:]
    return R.ravel()

def max_sites(values,threshold,limit):
    ii,jj=np.where(values>threshold)
    if len(ii)==0:return []
    order=np.argsort(values[ii,jj])[::-1]
    chosen=[];blocked=set()
    for idx in order:
        i,j=int(ii[idx]),int(jj[idx])
        if (i,j) in blocked:continue
        chosen.append((i,j))
        if len(chosen)==limit:break
        blocked.update((i+di,j+dj) for di in (-1,0,1) for dj in (-1,0,1))
    return chosen

def collect_wall_rows(G,J,Y,curvature_limit,radius_limit,count):
    trial_K,_=G.micro.curvature(Y);current_K,_=G.micro.curvature(J)
    # Use old and proposed tangent directions. Old directions matter at a repeated eigenvalue.
    sites=max_sites(np.maximum(current_K,trial_K),.986*curvature_limit,count)
    normals=[];bounds=[]
    for i,j in sites:
        for local in (J[i,:,j],Y[i,:,j]):
            I,II,_=tangent_data(local)
            try:k,V=eigh(II,I)
            except LinAlgError:continue
            for ix in range(2):
                if abs(k[ix])<.982*curvature_limit:continue
                co,b,_=signed_wall(J[i,:,j],V[:,ix],np.sign(k[ix]),curvature_limit)
                normals.append(field_row(G,i,j,co));bounds.append(max(0.,b))
    yp=np.linalg.norm(Y[:,0],axis=-1);jp=np.linalg.norm(J[:,0],axis=-1)
    for i,j in max_sites(np.maximum(yp,jp),radius_limit-.008,max(6,count//3)):
        u=Y[i,0,j]/max(1e-15,yp[i,j])
        zero=np.zeros((6,3));zero[0]=u
        normals.append(field_row(G,i,j,zero));bounds.append(max(0.,radius_limit-u@J[i,0,j]))
    return normals,bounds

def project(chol,sc,d,rows,rhs):
    if not rows:return d,dict(rows=0,dualIterations=0)
    R=np.asarray(rows)*sc[None]
    V=cho_solve_banded((chol,True),R.T,check_finite=False)
    norm=np.sqrt(np.maximum(0.,np.einsum('ij,ji->i',R,V)))
    use=norm>1e-11
    if not np.any(use):return d,dict(rows=0,dualIterations=0)
    R=R[use]/norm[use,None];V=V[:,use]/norm[None,use];b=np.asarray(rhs)[use]/norm[use]
    C=R@V;C=(C+C.T)/2
    right=R@(d.ravel()/sc)-b
    if np.max(right)<=0:return d,dict(rows=len(C),dualIterations=0,maximumAffineViolation=0.)
    def dual(x):
        f=C@x-right
        return .5*(x@(f-right)),f
    fit=minimize(dual,np.zeros(len(C)),method='L-BFGS-B',jac=True,bounds=[(0,None)]*len(C),
                 options=dict(maxiter=450,ftol=1e-15,gtol=5e-11,maxcor=24))
    z=d.ravel()/sc-V@fit.x
    out=(z*sc).reshape(d.shape)
    return out,dict(rows=len(C),dualIterations=int(fit.nit),active=int(np.sum(fit.x>1e-11)),
                    maximumAffineViolation=float(np.max((R@z-b)*norm[use])))

def same_metric_step(G,T,X,direct,guide,radius=1.915):
    models=(G,T)
    base=[g.report(X) for g in models]
    J=[material_jets(g,X) for g in models]
    lim=[max(guide,r['curvature']+2e-8) for r in base]
    rad=[max(radius,float(np.max(np.linalg.norm(z[:,0],axis=-1)))+2e-10) for z in J]
    peak=max(v['peak'] for v in base);best=None;log=[]
    for power in (.72,1.9):
        ab,grad=direct.assemble(G,X,power)
        sc=1/np.sqrt(np.maximum(1e-25,ab[0]));n=len(sc)
        for k in range(min(n,len(ab))):ab[k,:n-k]*=sc[k:]*sc[:n-k]
        diag=ab[0].copy()
        for mu in (1e-9,1e-6,.0003):
            ab[0]=diag+mu
            try:chol=cholesky_banded(ab,lower=True,check_finite=False)
            except LinAlgError:continue
            d=(sc*cho_solve_banded((chol,True),-sc*grad,check_finite=False)).reshape(X.shape)
            grid=2.**(-np.arange(0,31)/2)
            def merit(h,x):return max(float(g.metrics(X+x*h)[3].max()) for g in models)
            alpha=min(grid,key=lambda t:merit(d,t))
            raw=d*alpha;direction=raw.copy()
            rows=[];bounds=[]
            for sweep in range(4):
                accepted_full=False
                options=sorted((merit(direction,t),float(t)) for t in grid)
                for score,t in options:
                    if score>=peak*(1-1e-11) or (best is not None and score>=best[0]):break
                    y=X+t*direction;stat=[g.report(y) for g in models]
                    if any(r['curvature']>L+2e-9 or r['minimumSupport']<min(.115,b['minimumSupport']) for r,b,L in zip(stat,base,lim)):continue
                    Rtests=[float(np.max(np.linalg.norm(g.base[:,0]+g.forward_field(y,0,0),axis=-1))) for g in models]
                    if any(r>L+1e-10 for r,L in zip(Rtests,rad)):continue
                    best=(score,y,dict(power=power,damping=mu,unconstrainedAlpha=float(alpha),projectedFraction=t,
                         contactSweep=sweep,radiusOnBothGrids=Rtests,training=stat[0],secondary=stat[1]))
                    accepted_full=(t==1)
                    break
                if sweep==3 or (sweep==0 and accepted_full):break
                for g,z,L,R in zip(models,J,lim,rad):
                    y=material_jets(g,X+direction)
                    nrm,bnd=collect_wall_rows(g,z,y,L,R,24)
                    rows.extend(nrm);bounds.extend(bnd)
                if not rows:break
                prior=direction;direction,stat=project(chol,sc,raw,rows,bounds)
                stat.update(power=power,damping=mu,sweep=sweep+1,normalStep=float(np.linalg.norm(direction-prior)))
                log.append(stat)
                if np.linalg.norm(direction-prior)<1e-9*max(np.linalg.norm(raw),1e-18):break
        if best is not None:break
    return best,log

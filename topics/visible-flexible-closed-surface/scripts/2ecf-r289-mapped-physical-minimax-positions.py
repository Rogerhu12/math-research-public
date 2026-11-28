#!/usr/bin/env python3
"""Sparse trust region for the actual R289 post-map metric eigenvalues and principal curvatures, retaining all true shape guarantees."""
import argparse,importlib.util,json,os
from pathlib import Path
for k in ('MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,csr_matrix,hstack,vstack
p=Path(__file__).with_name('2ecf-r289-true-cuff-closed-image-maps.py');s=importlib.util.spec_from_file_location('r289maps',p);f=importlib.util.module_from_spec(s);s.loader.exec_module(f);k,v,m=f.k,f.v,f.m;dot=f.dot

def select(A,model,maximum):
    # Keep each radial group's distinct angular maxima, then add large residuals in the quarter sector.
    keep=np.zeros_like(A,dtype=bool);inds=np.flatnonzero(model.t<=np.pi/2+1e-10);groups=np.array_split(inds,7)
    for ii in range(0,len(A),4):
        chunk=A[ii:ii+4]
        for js in groups:
            if not len(js):continue
            j,at=np.unravel_index(chunk[:,js].argmax(),(len(chunk),len(js)));idx=js[at]
            if A[ii+j,idx]>.43*maximum:keep[ii+j,idx]=True
    ij=np.argwhere(A[:,inds]>.82*maximum)
    if len(ij)>750:ij=ij[np.linspace(0,len(ij)-1,750,dtype=int)]
    keep[ij[:,0],inds[ij[:,1]]]=True;return keep

def packet(g,x,guide):
    raw=k.OldFit.field(g,x);J0,(d1,d2,d3)=k.slab(raw);J=k.ball(J0);P,V,U=J[:,0],J[:,1],J[:,2];rr=g.bb;E,F,G=dot(V,V)-1,dot(V,U)/rr,dot(U,U)/rr**2-1;mean=(E+G)/2;gap=np.hypot((E-G)/2,F);angle=np.arctan2(2*F,E-G)/2;K,dK=v.curve(J);data=[];cols=[];rows=[];bb=[];h=0;N=x.size;counts=[]
    for mode,values in enumerate([mean+gap,mean-gap,K]):
        selected=select(abs(values),g,max(.001,np.abs(values).max()) if mode<2 else max(guide,np.abs(values).max()));
        if mode==2:selected&=(abs(K)>guide-.5)
        counts.append(int(selected.sum()))
        for i in np.flatnonzero(selected.any(axis=1)):
            mask=selected[i];js=np.flatnonzero(mask);sg=np.where(values[i,mask]>=0,1.,-1.);cutmask=abs(g.B[0][i])+abs(g.B[1][i])+abs(g.B[2][i])>1e-15;ix=np.flatnonzero(cutmask);ids=(ix[:,None]*g.na+np.arange(g.na)).ravel();c=np.zeros((6,len(js),3));radius=rr[i,mask]
            if mode<2:
                th=angle[i,mask]+mode*np.pi/2;aa=np.cos(th)[:,None];b=(np.sin(th)/radius)[:,None];D=aa*V[i,mask]+b*U[i,mask];c[1]=2*aa*D;c[2]=2*b*D
            else:c[1:]=np.stack([t[i,mask] for t in dK]);
            c=k.radius_pull(c,J0[i][:,mask]);ys,yu,yss,ysu,yuu=raw[i,1:,:,1][:,mask];dx,d2x,d3x=d1[i,mask],d2[i,mask],d3[i,mask];y=c[:,:,1];p0,cs,cu,ss,su,uu=y.copy();y[0]=dx*p0+d2x*(cs*ys+cu*yu+ss*yss+su*ysu+uu*yuu)+d3x*(ss*ys**2+su*ys*yu+uu*yu**2);y[1]=dx*cs+d2x*(2*ss*ys+su*yu);y[2]=dx*cu+d2x*(su*ys+2*uu*yu);y[3:]*=dx
            local=sum(g.B[dr][i,ix][None,:,None]*np.einsum('uc,uac->ua',vv,g.ang[du,mask])[:,None,:] for vv,(dr,du) in zip(c,m.O)).reshape(len(js),len(ids));local*=sg[:,None]
            rows.extend(np.repeat(np.arange(h,h+len(js)),len(ids)));cols.extend(np.tile(ids,len(js)));data.extend(local.ravel());rows.extend(range(h,h+len(js)));cols.extend([N+int(mode==2)]*len(js));data.extend([-1.]*len(js));bb.extend((guide if mode==2 else 0)-abs(values[i,mask]));h+=len(js)
    return coo_matrix((data,(rows,cols)),shape=(h,N+2)).tocsr(),np.array(bb),counts

def proposal(g,x,guide,mu,trust):
    A,b,count=packet(g,x,guide);n=x.size;na=x.shape[1];rows=[];cols=[];data=[];rr=0;bound=[]
    for i in range(x.shape[0]-2):
        for j in range(na):
            for sg in (-1,1):
                rows.extend([rr]*3);cols.extend([i*na+j,(i+1)*na+j,(i+2)*na+j]);data.extend([sg,-2*sg,sg]);bound.append(trust*.17);rr+=1
    C=coo_matrix((data,(rows,cols)),shape=(rr,n+2)).tocsr();M=vstack([A,C],format='csr');angles=np.tile(np.arange(na//3)+1,3);w=np.tile(1/(1+.05*(angles-1)**1.5),x.shape[0]);bounds=[(-trust*t,trust*t) for t in w]+[(0,None),(0,None)];res=linprog(np.r_[np.zeros(n),1.,mu],A_ub=M,b_ub=np.r_[b,bound],bounds=bounds,method='highs-ipm',options={'time_limit':45.})
    if not res.success:return None,dict(status=res.status,message=res.message,rows=count)
    return res.x[:n].reshape(x.shape),dict(status=0,rows=count,predicted=res.x[-2:].tolist(),trust=trust)

def main():
    a=argparse.ArgumentParser()
    for key in ('meridian','buffer','tail-table','parent','out'):a.add_argument('--'+key,type=Path,required=True)
    a.add_argument('--steps',type=int,default=8);a.add_argument('--mu',type=float,default=.035);a.add_argument('--trust',type=float,default=.002);a.add_argument('--guide',type=float,default=9.4);a=a.parse_args();d=json.loads(a.parent.read_bytes());a.index=d['index'];src=m.Source(a);eps=d['epsilon'];n=d['stadiumPower'];mix=d['stadiumMix'];from math import comb
    cc=np.array([2*(-1)**j*comb(2*n,n-j)/comb(2*n,n)/(1-4*j*j) for j in range(1,n+1)]);A=src.R+eps*((1-mix)+mix*cc.sum()/cc[::2].sum());f.install(A);m.support=lambda R,e,u,power=n,blend=mix:v.stadium_center(R,e,u,power,blend);j0=m.jet
    def scaled(r,t,e,linear=True):
        q=r.copy();q[:,[7,9,11]]*=d['horizontalLinearScale'];q[:,[8,10,12]]*=d['verticalLinearScale'];return j0(q,t,e,linear)
    m.jet=scaled;sp,mo=d['spans'],d['modes'];x=np.array(d['xyz']);r,u=src.grid(202,96,False);ii,screen=v.screen(src,x,eps,sp,mo,a.guide);g=m.Fit(src,np.vstack([r,src.original(ii)]),u,eps,sp,mo);hist=[g.metrics(x)];details=[];merit=lambda z:z['metric']+a.mu*max(0,z['curvature']-a.guide);tr=a.trust;print('initial',hist[0],flush=True)
    for i in range(a.steps):
        dx,info=proposal(g,x,a.guide,a.mu,tr);print('linear',info,flush=True);ok=False
        if dx is not None:
            for st in [1,.5,.25,.125,.0625,.03125]:
                z=g.metrics(x+st*dx)
                if merit(z)<merit(hist[-1])*(1-1e-6):x+=st*dx;hist.append(z);details.append(dict(**info,scale=st));ok=True;tr=min(a.trust*2,tr*(1.15 if st>=.5 else .75));print('accepted',i,z,flush=True);checkpoint=a.out.with_suffix('.accepted.json');temp=checkpoint.with_suffix('.part');temp.write_text(json.dumps(dict(x=x.tolist(),history=hist,details=details)));temp.replace(checkpoint);break
        if not ok:
            tr*=.35;details.append(info)
            if tr<.00003:break
    obs=[]
    for n,na,shift in [(397,192,False),(381,225,True)]:
        g=m.Fit(src,*src.grid(n,na,shift),eps,sp,mo);q=g.metrics(x);P=g.field(x)[:,0];obs.append(dict(radial=len(g.z),angular=len(g.t),actual=q,sampledMaxNorm=float(np.linalg.norm(P,axis=-1).max()),sampledMaxAbsY=float(abs(P[...,1]).max())))
    inner=src.original(np.where(src.tail['r']<=src.rb[0]+1e-14)[0]);dv=[]
    for i in range(0,len(inner),48):
        g=m.Fit(src,inner[i:i+48],np.arange(120)*2*np.pi/120+np.pi/120,eps,sp,mo);dv.append(g.metrics(x))
    d.update(schema='R289-actual-closed-image-mapped-sparse-minimax-fixed-g',entrySHA256=m.base.sha(__file__),previousCompleteFieldSHA256=m.base.sha(a.parent),initialNativeScreen=screen,xyz=x.tolist(),steps=details,history=hist,observers=obs,deepObserver=dict(rawRadial=len(inner),angular=120,metric=max(q['metric'] for q in dv),curvature=max(q['curvature'] for q in dv)))
    with a.out.open('x') as o:json.dump(d,o,indent=2);o.write('\n')
    print('observed',obs[-1],d['deepObserver'],flush=True)
if __name__=='__main__':main()

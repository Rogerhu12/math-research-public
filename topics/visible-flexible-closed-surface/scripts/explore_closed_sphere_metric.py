#!/usr/bin/env python3
"""Closed-sphere exploratory metric search with an exact diameter witness.

F_i(p,t)=p_i*f_i(p_x^2,p_y^2,p_z^2,t), with spatial simplex Bernstein
polynomials and time Bernstein polynomials. Reflection symmetries are fixed.
All initial coefficients <=1 and the x-axis tip=1 give D0=2 exactly.
All final coefficients <=binary64(.9) and the x-axis tip at that value
give D1=2*binary64(.9) exactly (not exactly decimal 1.8).
Thus an embedded solution would have delta_E/D0 >=(1-binary64(.9))/2,
slightly below decimal .05, independent of rigid
registration. This script is a SEARCH, not a proof of isometry or reach.
In particular, the initial metric is allowed to change during the search.
"""
import argparse
import json
import math
from fractions import Fraction
import os
from pathlib import Path
import time
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse import csr_matrix, diags, hstack, vstack


def indices(k):
    return [(i,j,k-i-j) for i in range(k+1) for j in range(k-i+1)]


def bernstein_xyz(xyz,k,idx):
    X=xyz*xyz
    return np.stack([math.factorial(k)/(math.factorial(i)*math.factorial(j)*math.factorial(l))
                     *X[:,0]**i*X[:,1]**j*X[:,2]**l for i,j,l in idx],axis=1)


def sphere_grid(n,include_boundary=False):
    if include_boundary:
        angles=np.linspace(0,np.pi/2,n)
    else:
        a,_=np.polynomial.legendre.leggauss(n);angles=(a+1)*np.pi/4
    ph,th=np.meshgrid(angles,angles,indexing='ij');ph=ph.ravel();th=th.ravel()
    p=np.stack([np.sin(ph)*np.cos(th),np.sin(ph)*np.sin(th),np.cos(ph)],axis=1)
    u=np.stack([np.cos(ph)*np.cos(th),np.cos(ph)*np.sin(th),-np.sin(ph)],axis=1)
    v=np.stack([-np.sin(th),np.cos(th),np.zeros_like(th)],axis=1)
    return p,u,v


def spatial_operators(degree,n,include_boundary=False):
    p,u,v=sphere_grid(n,include_boundary)
    idx=indices(degree);nb=len(idx);B=bernstein_xyz(p,degree,idx)
    lowidx=indices(degree-1);low=bernstein_xyz(p,degree-1,lowidx);lowmap={q:i for i,q in enumerate(lowidx)}
    lo2idx=indices(degree-2);lo2=bernstein_xyz(p,degree-2,lo2idx);lo2map={q:i for i,q in enumerate(lo2idx)}
    B1=np.zeros((3,len(p),nb));B2=np.zeros((3,3,len(p),nb))
    for j,q in enumerate(idx):
        for a in range(3):
            qq=list(q);qq[a]-=1
            if qq[a]>=0:B1[a,:,j]=degree*low[:,lowmap[tuple(qq)]]
            for b in range(3):
                q2=qq.copy();q2[b]-=1
                if min(q2)>=0:B2[a,b,:,j]=degree*(degree-1)*lo2[:,lo2map[tuple(q2)]]
    def df(e):return sum((2*p[:,a]*e[:,a])[:,None]*B1[a] for a in range(3))
    def ddf(e,f):
        return sum((2*e[:,a]*f[:,a])[:,None]*B1[a] for a in range(3))+sum((4*p[:,a]*p[:,b]*e[:,a]*f[:,b])[:,None]*B2[a,b] for a in range(3) for b in range(3))
    U,V=df(u),df(v);UU,UV,VV=ddf(u,u),ddf(u,v),ddf(v,v)
    mats={key:[] for key in ['p','u','v','uu','uv','vv']}
    Z=csr_matrix((len(p),nb))
    for a in range(3):
        F=p[:,a,None]*B
        dd={'p':F,'u':u[:,a,None]*B+p[:,a,None]*U,'v':v[:,a,None]*B+p[:,a,None]*V,
            'uu':2*u[:,a,None]*U+p[:,a,None]*UU-(2*degree+1)*F,
            'uv':u[:,a,None]*V+v[:,a,None]*U+p[:,a,None]*UV,
            'vv':2*v[:,a,None]*V+p[:,a,None]*VV-(2*degree+1)*F}
        for key,A in dd.items():mats[key].append(hstack([csr_matrix(A) if b==a else Z for b in range(3)],format='csr'))
    return p,u,v,idx,mats


def eigmin2(a,b,c):
    rad=np.sqrt((a-c)**2+4*b*b)
    return (a+c-rad)/2


class Search:
    def __init__(self,degree=4,time_degree=4,grid=10,kappa=16.,dent=1.2):
        self.degree,self.time_degree,self.grid,self.kappa=degree,time_degree,grid,kappa
        self.p,self.u,self.v,self.idx,self.spatial=spatial_operators(degree,grid)
        self.nb=len(self.idx);self.ns=len(self.p);self.nt=time_degree+1;self.nfull=3*self.nb*self.nt
        self.times=np.linspace(0,1,2*time_degree+2)
        self.pin=np.zeros(self.nfull);fixed=[]
        for j in range(self.nt):
            for a,axis in enumerate([(degree,0,0),(0,degree,0),(0,0,degree)]):
                ii=j*3*self.nb+a*self.nb+self.idx.index(axis);fixed.append(ii)
                self.pin[ii]=[1-.1*j/time_degree,.85,.7][a]
        self.free=np.delete(np.arange(self.nfull),fixed)
        self.maps=[self.time_maps(t,self.spatial) for t in self.times]
        self.bases=[{key:np.stack([A@self.pin for A in mats],axis=1) for key,mats in mp.items()} for mp in self.maps]
        self.maps=[{key:[A[:,self.free] for A in mats] for key,mats in mp.items()} for mp in self.maps]
        c=np.zeros((self.nt,3,self.nb))
        for j in range(self.nt):
            for a in range(3):
                scale=[1-.1*j/time_degree,.85,.7][a]
                c[j,a]=[scale*(1-dent*(i*k+k*l+i*l)/(degree*(degree-1))) for i,k,l in self.idx]
        self.initial=c.ravel()[self.free]
        self.lower=np.full_like(self.initial,.2)
        maxfull=np.ones(self.nfull)*1.2;maxfull[:3*self.nb]=1.;maxfull[-3*self.nb:]=.9
        self.upper=maxfull[self.free]
        self.initial=np.maximum(self.lower+1e-9,np.minimum(self.upper-1e-9,self.initial))
        e=self.evaluate(self.initial,0);E,F,G=self.metric(e)
        self.scale=[1/np.maximum(E,.1),1/np.sqrt(np.maximum(E*G,.01)),1/np.maximum(G,.1)]
        self.calls=0

    def time_maps(self,t,spatial):
        b=[math.comb(self.time_degree,j)*t**j*(1-t)**(self.time_degree-j) for j in range(self.nt)]
        return {key:[hstack([bb*A for bb in b],format='csr') for A in mats] for key,mats in spatial.items()}

    def evaluate(self,x,index):
        return {key:self.bases[index][key]+np.stack([A@x for A in mats],axis=1) for key,mats in self.maps[index].items()}

    @staticmethod
    def metric(e):return [np.sum(e['u']*e['u'],axis=1),np.sum(e['u']*e['v'],axis=1),np.sum(e['v']*e['v'],axis=1)]

    @staticmethod
    def geometry(e):
        cross=np.cross(e['u'],e['v']);area=np.linalg.norm(cross,axis=1);N=cross/np.maximum(area,1e-14)[:,None]
        II=[np.sum(N*e[key],axis=1) for key in ['uu','uv','vv']]
        J=np.sum(e['p']*cross,axis=1)
        return N,area,II,J

    def residual(self,x):
        es=[self.evaluate(x,j) for j in range(len(self.times))]
        g0=self.metric(es[0]);out=[]
        for j,e in enumerate(es):
            g=self.metric(e)
            if j:out.extend([s*(a-b) for s,a,b in zip(self.scale,g,g0)])
            N,area,h,J=self.geometry(e)
            out.append(10*np.maximum(0,.08-J))
            out.append(10*np.maximum(0,.10-eigmin2(*g)))
            if self.kappa>0:
                for sign in [-1,1]:
                    M=[self.kappa*a+sign*b for a,b in zip(g,h)]
                    out.append((5/self.kappa)*np.maximum(0,-eigmin2(*M)))
        return np.concatenate(out)

    @staticmethod
    def min_eig_jac(a,b,c,jacs):
        rad=np.sqrt((a-c)**2+4*b*b);inv=np.divide(1.,rad,out=np.zeros_like(rad),where=rad>1e-14)
        return diags((1-(a-c)*inv)/2)@jacs[0]+diags(-2*b*inv)@jacs[1]+diags((1+(a-c)*inv)/2)@jacs[2]

    def jacobian(self,x):
        out=[];g0jac=None
        for j in range(len(self.times)):
            e=self.evaluate(x,j);mp=self.maps[j];g=self.metric(e)
            gj=[sum(diags(2*e['u'][:,i])@mp['u'][i] for i in range(3)),
                sum(diags(e['v'][:,i])@mp['u'][i]+diags(e['u'][:,i])@mp['v'][i] for i in range(3)),
                sum(diags(2*e['v'][:,i])@mp['v'][i] for i in range(3))]
            if j==0:g0jac=gj
            else:out.extend([diags(s)@(a-b) for s,a,b in zip(self.scale,gj,g0jac)])
            N,area,h,J=self.geometry(e)
            cp=np.cross(e['u'],e['v']);cu=np.cross(e['v'],e['p']);cv=np.cross(e['p'],e['u'])
            jj=sum(diags(cp[:,i])@mp['p'][i]+diags(cu[:,i])@mp['u'][i]+diags(cv[:,i])@mp['v'][i] for i in range(3))
            out.append(diags(-10*(J<.08))@jj)
            mine=eigmin2(*g);out.append(diags(-10*(mine<.1))@self.min_eig_jac(*g,gj))
            if self.kappa>0:
                hj=[]
                for key,hk in zip(['uu','uv','vv'],h):
                    a=(e[key]-hk[:,None]*N)/np.maximum(area,1e-14)[:,None]
                    bu=np.cross(e['v'],a);bv=np.cross(a,e['u'])
                    hj.append(sum(diags(N[:,i])@mp[key][i]+diags(bu[:,i])@mp['u'][i]+diags(bv[:,i])@mp['v'][i] for i in range(3)))
                for sign in [-1,1]:
                    M=[self.kappa*a+sign*b for a,b in zip(g,h)]
                    Mj=[self.kappa*a+sign*b for a,b in zip(gj,hj)]
                    low=eigmin2(*M)
                    out.append(diags((-5/self.kappa)*(low<0))@self.min_eig_jac(*M,Mj))
        return vstack(out,format='csr')

    def check_jacobian(self,x):
        rng=np.random.default_rng(90011);v=rng.normal(size=len(x));v/=np.linalg.norm(v)
        j=self.jacobian(x)@v
        return {str(h):float(np.linalg.norm((self.residual(x+h*v)-self.residual(x-h*v))/(2*h)-j)/max(np.linalg.norm(j),1e-14)) for h in [1e-5,1e-6,1e-7]}

    def diagnostic(self,x,n=24,nt=17):
        p,u,v,idx,spatial=spatial_operators(self.degree,n,True)
        full=self.pin.copy();full[self.free]=x
        metrics=[];Js=[];ks=[];normranges=[];max_norms=[]
        g0=None;err=0.;worst=None
        for t in np.linspace(0,1,nt):
            maps=self.time_maps(t,spatial)
            e={key:np.stack([A@full for A in mats],axis=1) for key,mats in maps.items()}
            E,F,G=self.metric(e);N,area,h,J=self.geometry(e);l,m,n2=h
            gram=np.stack([E,F,F,G],axis=1).reshape(-1,2,2)
            if g0 is None:
                g0=gram.copy();ev,V=np.linalg.eigh(g0);invs=np.einsum('...ij,...j,...kj->...ik',V,1/np.sqrt(np.maximum(ev,1e-14)),V)
            rel=invs@(gram-g0)@invs
            er=np.max(np.abs(np.linalg.eigvalsh(rel)),axis=1)
            if er.max()>err:err=float(er.max());worst={'t':float(t),'unit_sphere_point':p[int(er.argmax())].tolist()}
            det=E*G-F*F;HH=(G*l-2*F*m+E*n2)/(2*np.maximum(det,1e-14));KK=(l*n2-m*m)/np.maximum(det,1e-14)
            km=np.abs(HH)+np.sqrt(np.maximum(0,HH*HH-KK))
            Js.append(float(J.min()));ks.append(float(km.max()));metrics.append(float(eigmin2(E,F,G).min()))
            norms=np.linalg.norm(e['p'],axis=1);normranges.append([float(norms.min()),float(norms.max())]);max_norms.append(norms.max())
        return {'max_relative_metric_defect_sampled':err,'worst_metric_sample':worst,'min_radial_jacobian_sampled':min(Js),
                'max_abs_principal_curvature_sampled':max(ks),'min_gram_eigenvalue_sampled':min(metrics),
                'radial_norm_range_sampled':[min(a[0] for a in normranges),max(a[1] for a in normranges)],
                'initial_diameter_exact_if_regular':'2','final_diameter_exact_if_regular':str(2*Fraction.from_float(.9)),
                'rigid_quotient_delta_over_D_lower_if_embedded':str((1-Fraction.from_float(.9))/2),
                'closed_parameter_domain':'S2','C2_automatic':'polynomial restrictions',
                'embedded_certified':False,'reach_certified':False,'fixed_metric_refinement':False,
                'grid':[len(p),nt]}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--degree',type=int,default=4);ap.add_argument('--time-degree',type=int,default=4)
    ap.add_argument('--grid',type=int,default=10);ap.add_argument('--kappa',type=float,default=16.)
    ap.add_argument('--dent',type=float,default=1.2);ap.add_argument('--max-nfev',type=int,default=120)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    S=Search(args.degree,args.time_degree,args.grid,args.kappa,args.dent)
    checks=S.check_jacobian(S.initial);before=S.diagnostic(S.initial,16,9)
    start=time.monotonic()
    res=least_squares(S.residual,S.initial,jac=S.jacobian,bounds=(S.lower,S.upper),
                      method='trf',tr_solver='lsmr',tr_options={'atol':1e-10,'btol':1e-10,'maxiter':160},
                      max_nfev=args.max_nfev,ftol=1e-11,xtol=1e-11,gtol=1e-9,x_scale='jac')
    report={'status':'exploratory closed-sphere search; not an isometric solution',
            'arguments':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
            'unknowns':len(res.x),'residuals':len(res.fun),'jacobian_directional_checks':checks,
            'initial':before,'final':S.diagnostic(res.x),
            'solver':{'success':bool(res.success),'message':res.message,'nfev':res.nfev,'cost':float(res.cost),'optimality':float(res.optimality)},
            'elapsed_seconds':time.monotonic()-start}
    full=S.pin.copy();full[S.free]=res.x
    np.savez_compressed(args.out/'checkpoint.npz',coefficients=full,free_variables=res.x,indices=np.array(S.idx),times=S.times)
    (args.out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()

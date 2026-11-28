#!/usr/bin/env python3
"""Real full-core hypothesis testing of star rings and an injective meridian foliation."""
import argparse,importlib.util,json,os
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from fractions import Fraction
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
p=Path(__file__).with_name('2ecf-r289-physical-query.py')
sp=importlib.util.spec_from_file_location('r289_rays_query',p);Q=importlib.util.module_from_spec(sp);sp.loader.exec_module(Q)

def slopes(J):
    P,S,U=J[:,0],J[:,1],J[:,2];x,y,z=P.swapaxes(0,2).swapaxes(1,2);r=np.hypot(x,y)
    cross=lambda V:(x*V[...,1]-y*V[...,0])/r**2
    ts,tu=cross(S),cross(U);v=ts/tu
    rs=((x*S[...,0]+y*S[...,1])-v*(x*U[...,0]+y*U[...,1]))/r
    return r,z,np.arctan2(y,x),tu,rs,S[...,2]-v*U[...,2]

def certificate_test(r,z,theta,tu,dr,dz,s,u):
    # At each geometric angle and physical radius approximate a coefficient of -d rho;
    # a positive result suggests a potential z+H(r,theta).
    h=.5*np.arccos(np.cos(2*theta));rlo,rhi=r.min(),r.max()
    def grid(nr,na):
        tr=np.clip((r-rlo)/(rhi-rlo)*(nr-1),0,nr-1);ta=h/(np.pi/2)*(na-1);ii=np.minimum(tr.astype(int),nr-2);jj=np.minimum(ta.astype(int),na-2);p,q=tr-ii,ta-jj
        best=1e6*np.ones((nr,na));m=r.size
        rr=np.tile(np.arange(m),(5,1));cc=np.stack([(ii*na+jj).ravel(),(ii*na+jj+1).ravel(),((ii+1)*na+jj).ravel(),((ii+1)*na+jj+1).ravel(),np.full(m,nr*na)])
        w=np.stack([(dr*(1-p)*(1-q)).ravel(),(dr*(1-p)*q).ravel(),(dr*p*(1-q)).ravel(),(dr*p*q).ravel(),np.ones(m)]);A=coo_matrix((w.ravel(),(rr.ravel(),cc.ravel())),shape=(m,nr*na+1)).tocsr()
        opt=linprog(np.r_[np.zeros(nr*na),-1],A_ub=A,b_ub=dz.ravel(),bounds=[(-4,4)]*(nr*na)+[(None,None)],method='highs',options=dict(time_limit=50.))
        if not opt.success:return dict(ok=False,status=str(opt.message))
        return dict(ok=True,radial=nr,angular=na,minimum=opt.x[-1],weights=opt.x[:-1].reshape(nr,na).tolist(),radialRange=[float(rlo),float(rhi)])
    levels=[grid(2,2),grid(7,5),grid(20,12)]
    k=np.unravel_index(np.argmin(tu),tu.shape);m=np.unravel_index(np.argmin(dz),dz.shape);n=np.unravel_index(np.argmax(z),z.shape)
    return dict(radiusRange=[rlo,rhi],thetaUDomain=[tu.min(),tu.max()],worstStarMaterial=[s[k[0]],u[k[1]]],zRange=[z.min(),z.max()],zMaxMaterial=[s[n[0]],u[n[1]]],zThetaSlope=[dz.min(),dz.max()],worstSlopeMaterial=[s[m[0]],u[m[1]]],rThetaSlope=[dr.min(),dr.max()],coeffTests=levels)
def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','meridian','buffer','tail-table','tail','state','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--radial',type=int,default=321);p.add_argument('--angular',type=int,default=128);a=p.parse_args();g=Q.Field(a.scripts,a.meridian,a.buffer,a.tail_table,a.state,Fraction(json.loads(a.tail.read_bytes())['scale']));rows,u=g.src.grid(a.radial,a.angular,True);u=np.linspace(0,np.pi/2,a.angular//2+1);u=np.unique(np.r_[u,(u[:-1]+u[1:])/2]);r,z,th,tu,rs,zs=[],[],[],[],[],[];r1,z1,t1,tu1,rs1,zs1=[],[],[],[],[],[]
    for i in range(0,len(rows),28):
        f=g.m.Fit(g.src,rows[i:i+28],u,g.eps,g.d['spans'],g.d['modes']);raw=g.mod.k.OldFit.field(f,g.x)
        for container,jet in [((r,z,th,tu,rs,zs),raw),((r1,z1,t1,tu1,rs1,zs1),f.field(g.x))]:
            for x,v in zip(container,slopes(jet)):x.append(v)
    out=dict(schema='R289-real-meridian-potential-sampled-data',stateSHA256=g.m.base.sha(a.state),radial=len(rows),angular=len(u))
    for key,col in [('bare',(r,z,th,tu,rs,zs)),('final',(r1,z1,t1,tu1,rs1,zs1))]:
        out[key]=certificate_test(*[np.concatenate(x) for x in col],rows[:,0],u);d=out[key];print(key,d['thetaUDomain'],d['zRange'],d['zThetaSlope'],[s.get('minimum') for s in d['coeffTests']],flush=True)
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
if __name__=='__main__':main()

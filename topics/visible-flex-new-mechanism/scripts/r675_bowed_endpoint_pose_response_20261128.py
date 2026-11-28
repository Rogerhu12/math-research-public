#!/usr/bin/env python3
"""Physical Cartesian isometric-bending response of the fixed R673 endpoint."""
from __future__ import annotations
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import json
import math
import os
from pathlib import Path
import time
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import BSpline
from scipy.linalg import qr, svd


def emit(kind,**row):
    print(json.dumps(dict(kind=kind,**row),sort_keys=True,allow_nan=False),flush=True)


def dot(x,y):
    return np.einsum("...i,...i->...",x,y)


def jy(x):
    return np.stack((x[...,2],np.zeros_like(x[...,0]),-x[...,0]),axis=-1)


def rotate(x,q):
    c,s=np.cos(q),np.sin(q)
    return np.stack((c*x[...,0]+s*x[...,2],np.broadcast_to(x[...,1],(c*x[...,0]).shape),
                     -s*x[...,0]+c*x[...,2]),axis=-1)


class Endpoint:
    def __init__(self,opts,count):
        self.a,self.b=opts["radii"]
        self.l=self.a+opts["ramp"]
        self.u=self.b-opts["ramp"]
        self.A=opts["height"]
        self.theta=math.asin(opts["sine"])
        self.count=count
        self.M=self.theta/self.integral(self.a)

    def k(self,s):
        if s<self.l:
            t=(s-self.a)/(self.l-self.a)
            return t*t*(3-2*t),6*t*(1-t)/(self.l-self.a)
        if s>self.u:
            t=(self.b-s)/(self.b-self.u)
            return t*t*(3-2*t),-6*t*(1-t)/(self.b-self.u)
        return 1.,0.

    @lru_cache(maxsize=None)
    def integral(self,r):
        stops=[r]+[x for x in (self.l,self.u,self.b) if x>r]
        value=0.
        for lo,hi in zip(stops[:-1],stops[1:]):
            self.count["angle_profile_quadratures"]+=1
            value+=quad(lambda v:self.k(v)[0]/v,lo,hi,epsabs=4e-15,epsrel=4e-15)[0]
        return value

    def evaluate(self,r,phi):
        ang=self.M*np.array([self.integral(float(z)) for z in r])
        k,dk=np.array([self.k(z) for z in r]).T
        wr=-self.M*k/r
        wrr=self.M*(k/r**2-dk/r)
        shape=(r>=self.l)&(r<=self.u)
        L=self.u-self.l
        z=np.clip(2*(r-self.l)/L-1,-1,1)
        H=self.A*(1-z*z)**3
        Hr=-12*self.A*z*(1-z*z)**2/L
        Hrr=-24*self.A*(1-z*z)*(1-5*z*z)/L**2
        Hrr[~shape]=0
        er=np.stack((np.cos(phi),np.sin(phi),np.zeros_like(phi)),axis=-1)[None,:,:]
        et=np.stack((-np.sin(phi),np.cos(phi),np.zeros_like(phi)),axis=-1)[None,:,:]
        ez=np.array([0.,0.,1.])
        c,c1,c2=[x[:,None,None]/self.theta for x in (ang,wr,wrr)]
        rad=r[:,None,None]
        def state(increment):
            q=(ang[:,None]+increment*c[...,0])
            ar=wr[:,None,None]+increment*c1
            arr=wrr[:,None,None]+increment*c2
            R,P=rotate(er,q),rotate(et,q)
            J,JP=jy(R),jy(P)
            J2=jy(J)
            return [rad*R+H[:,None,None]*ez,
                    R+rad*ar*J+Hr[:,None,None]*ez,rad*P,
                    (2*ar+rad*arr)*J+rad*ar**2*J2+Hrr[:,None,None]*ez,
                    P+rad*ar*JP,-rad*R]
        raw=state(0.)
        R,P=rotate(er,ang[:,None]),rotate(et,ang[:,None])
        J,JP=jy(R),jy(P)
        J2,J2P=jy(J),jy(JP)
        J3=jy(J2)
        ar,arr=wr[:,None,None],wrr[:,None,None]
        # A unit increase of the actual inner angle, with both two-jets exact.
        pose=[rad*c*J,(c+rad*c1)*J+rad*c*ar*J2,rad*c*JP,
              (2*c1+rad*c2)*J+(2*(c+rad*c1)*ar+rad*c*arr)*J2+rad*c*ar**2*J3,
              (c+rad*c1)*JP+rad*c*ar*J2P,-rad*c*J]
        # Exactly the second parameter derivative of the same rigid angle lift.
        cc,cc1,cc2=c*c,2*c*c1,2*(c1*c1+c*c2)
        acc=[rad*cc*J2,(cc+rad*cc1)*J2+rad*cc*ar*J3,rad*cc*J2P,
             (2*cc1+rad*cc2)*J2+(2*(cc+rad*cc1)*ar+rad*cc*arr)*J3+rad*cc*ar**2*jy(J3),
             (cc+rad*cc1)*J2P+rad*cc*ar*jy(J2P),-rad*cc*J2]
        return dict(raw=raw,pose=pose,acc=acc,state=state,chi=[c[:,0,0],c1[:,0,0],c2[:,0,0]],
                    angle=ang,wr=wr,Hr=Hr,Hrr=Hrr)


class ResponseSpace:
    def __init__(self,end,bands,K):
        self.end=end
        self.bands=bands
        self.K=K
        ab=[end.a,end.l,end.u,end.b]
        self.edges=np.r_[end.a,*[np.linspace(lo,hi,n+1)[1:] for lo,hi,n in zip(ab[:-1],ab[1:],bands)]]
        knots=np.r_[[end.a]*5,self.edges,[end.b]*5]
        nb=len(knots)-6
        self.spl=BSpline(knots,np.eye(nb),5)
        self.nb=nb-6
        self.blocks=[(i,j) for i in range(3) for j in range(int(i==1),K+1)]
        self.size=self.nb*len(self.blocks)+2
        self.scale=end.b-end.a

    def grid(self,order,nphi,ends=False,phi=None):
        t,w=np.polynomial.legendre.leggauss(order)
        lo,hi=self.edges[:-1,None],self.edges[1:,None]
        r=((lo+hi+(hi-lo)*t)/2).ravel()
        weights=((hi-lo)*w/(2*self.scale)).ravel()
        if ends:
            r=np.unique(np.r_[r,self.edges])
            ds=np.diff(r)
            weights=(np.r_[0,ds]+np.r_[ds,0])/(2*self.scale)
        if phi is None:
            phi=2*np.pi*np.arange(nphi)/nphi
        g=self.end.evaluate(r,phi)
        g.update(r=r,phi=phi,weights=weights,b=[self.scale*self.spl(r,k)[:,3:-3] for k in range(3)])
        return g

    @staticmethod
    def angular(i,j,phi):
        if i==1:
            return np.sin(j*phi),j*np.cos(j*phi),-j*j*np.sin(j*phi)
        return np.cos(j*phi),-j*np.sin(j*phi),-j*j*np.cos(j*phi)

    def fields(self,x,g):
        out=[np.zeros_like(s) for s in g["raw"]]
        rad=g["b"]
        for k,(i,j) in enumerate(self.blocks):
            co=x[k*self.nb:(k+1)*self.nb]
            vals=[m@co for m in rad]
            f,df,ddf=self.angular(i,j,g["phi"])
            for outv,(idx,angular) in zip(out,((0,f),(1,f),(0,df),(2,f),(1,df),(0,ddf))):
                outv[...,i]+=vals[idx][:,None]*angular[None,:]
        for n,i in enumerate((0,2)):
            for pos,idx in ((0,0),(1,1),(3,2)):
                out[pos][...,i]+=self.scale*x[-2+n]*g["chi"][idx][:,None]
        return out

    def matrix(self,g):
        D,Y=g["raw"][1],g["raw"][2]/g["r"][:,None,None]
        r=g["r"][:,None,None]
        ns=len(g["phi"])
        rows=D.shape[0]*ns
        W=np.sqrt(g["weights"][:,None,None]/ns)
        matrix=np.empty((3*rows,self.size),order="F")
        def put(slot,i,B,Br,s,ds):
            R=Br[:,None,:]*s[None,:,None]
            P=B[:,None,:]*ds[None,:,None]/r
            for ix,val in enumerate((2*D[...,i,None]*R,
                              math.sqrt(2)*(Y[...,i,None]*R+D[...,i,None]*P),
                              2*Y[...,i,None]*P)):
                matrix[ix*rows:(ix+1)*rows,slot:slot+B.shape[1]]=(W*val).reshape(rows,B.shape[1])
        for k,(i,j) in enumerate(self.blocks):
            s,ds,_=self.angular(i,j,g["phi"])
            put(k*self.nb,i,*g["b"][:2],s,ds)
        for k,i in enumerate((0,2)):
            put(self.size-2+k,i,self.scale*g["chi"][0][:,None],self.scale*g["chi"][1][:,None],
                np.ones(ns),np.zeros(ns))
        return matrix


def strains(raw,v,r):
    D,Y=raw[1],raw[2]/r[:,None,None]
    dr,dp=v[1],v[2]/r[:,None,None]
    return [2*dot(D,dr),dot(D,dp)+dot(Y,dr),2*dot(Y,dp)]


def quadratic(v,r):
    dr,dp=v[1],v[2]/r[:,None,None]
    return [2*dot(dr,dr),2*dot(dr,dp),2*dot(dp,dp)]


def pack(vals,g):
    W=np.sqrt(g["weights"][:,None]/len(g["phi"]))
    return np.r_[(W*vals[0]).ravel(),(math.sqrt(2)*W*vals[1]).ravel(),(W*vals[2]).ravel()]


def plus(a,b):
    return [x+y for x,y in zip(a,b)]


def relative(raw,errs,r):
    D,Y=raw[1],raw[2]/r[:,None,None]
    e,f,gg=dot(D,D),dot(D,Y),dot(Y,Y)
    m=f/e
    h=np.sqrt(gg-m*f)
    x,y,z=errs
    aa,ab,bb=x/e,(y-m*x)/(np.sqrt(e)*h),(z-2*m*y+m*m*x)/(h*h)
    return abs((aa+bb)/2)+np.sqrt(((aa-bb)/2)**2+ab**2)


def bdelta(raw,v,r):
    D,Y=raw[1],raw[2]/r[:,None,None]
    dr,dp=v[1],v[2]/r[:,None,None]
    area=np.cross(D,Y)
    length=np.linalg.norm(area,axis=-1)
    n=area/length[...,None]
    da=np.cross(dr,Y)+np.cross(D,dp)
    dn=(da-n*dot(n,da)[...,None])/length[...,None]
    rr,pp=r[:,None],r[:,None]**2
    return [(dot(dn,raw[i])+dot(n,v[i]))/f for i,f in ((3,1.),(4,rr),(5,pp))]


def read(space,x,g,pose=True):
    correction=space.fields(x,g)
    v=plus(g["pose"],correction) if pose else correction
    eps=relative(g["raw"],strains(g["raw"],v,g["r"]),g["r"])
    idx=np.unravel_index(eps.argmax(),eps.shape)
    r=g["r"][:,None,None]
    cov=(v[3],v[4]/r-v[2]/r**2,v[5]/r**2+v[1]/r)
    bd=bdelta(g["raw"],v,g["r"])
    return dict(relative_strain_max=float(eps[idx]),attainer=[float(g["r"][idx[0]]),float(g["phi"][idx[1]])],
            residual_L2=float(np.linalg.norm(pack(strains(g["raw"],v,g["r"]),g))),
            displacement_max=float(np.linalg.norm(v[0],axis=-1).max()),
            first_gradient_column_max=float(max(np.linalg.norm(q,axis=-1).max() for q in (v[1],v[2]/r))),
            flat_polar_second_column_max=float(max(np.linalg.norm(q,axis=-1).max() for q in cov)),
            second_form_component_max=float(max(abs(q).max() for q in bd)),
            inner_translation=(space.scale*x[-2:]).tolist())


def central_moment(space,x,order):
    g=space.grid(order,1,phi=np.array([np.pi/2]))
    v=plus(g["pose"],space.fields(x,g))
    b=bdelta(g["raw"],v,g["r"])
    interior=(g["r"]>space.end.l)&(g["r"]<space.end.u)
    c=np.cos(g["angle"][interior])
    hr=g["Hr"][interior]
    val=c*(hr*b[0][interior,0]/g["r"][interior]+g["Hrr"][interior]*b[2][interior,0])
    val/=2*g["wr"][interior]*np.sqrt(1+(hr*c)**2)
    return float(space.scale*(g["weights"][interior]@val))


def main():
    if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY","").lower()!="rogerhu12/math-research-public" or
        not os.environ.get("GITHUB_RUN_ID","").isdigit()):
        raise SystemExit("Scientific execution requires public math-research-public Actions.")
    ap=argparse.ArgumentParser()
    ap.add_argument("--geometry",required=True)
    ap.add_argument("--max-seconds",type=float,required=True)
    args=ap.parse_args()
    opts=json.loads(Path(args.geometry).read_text())
    count=Counter()
    started=time.perf_counter()
    end=Endpoint(opts,count)
    elapsed=lambda:time.perf_counter()-started
    summary=[]
    last=None
    emit("provenance",run=os.environ["GITHUB_RUN_ID"],max_seconds=args.max_seconds,
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         fixed_bowed_metric=True,actual_pose_unit_radians=1.,positive_endpoint=end.theta,actual_M=end.M)
    try:
        for label,bands,K,order in opts["spaces"]:
            if elapsed()>args.max_seconds-opts["reserve_seconds"]:
                break
            sp=ResponseSpace(end,bands,K)
            g=sp.grid(order,2*K+5)
            fine=sp.grid(opts["fine_order"],max(opts["fine_angles"],4*K+9),True)
            J=sp.matrix(g)
            count["full_original_matrices"]+=1
            count["original_columns"]+=sp.size
            rhs=-pack(strains(g["raw"],g["pose"],g["r"]),g)
            direction=np.sin(np.arange(1,sp.size+1)*.693)
            direction/=np.linalg.norm(direction)
            check=pack(strains(g["raw"],sp.fields(direction,g),g["r"]),g)
            jerr=float(np.linalg.norm(J@direction-check)/max(np.linalg.norm(check),1e-18))
            if jerr>1e-10:
                raise ArithmeticError("Complete original Cartesian operator assembly failed.")
            Q,R=qr(J,mode="economic",overwrite_a=True,check_finite=False)
            projected=Q.T@rhs
            del J
            U,svals,vt=svd(R,full_matrices=False,check_finite=False)
            count["full_QR_SVD"]+=1
            def solve(reduced):
                y=U.T@reduced
                inv=np.divide(y,svals,out=np.zeros_like(y),where=svals!=0)
                return vt.T@inv
            x=solve(projected)
            work=read(sp,x,g)
            obs=read(sp,x,fine)
            independent_radius=read(sp,x,sp.grid(opts["fine_order"],2*K+5,True))
            independent_angle=read(sp,x,sp.grid(order,max(opts["fine_angles"],4*K+9)))
            complete_res=pack(strains(g["raw"],plus(g["pose"],sp.fields(x,g)),g["r"]),g)
            range_distance=float(np.linalg.norm(rhs-Q@projected))
            normal_difference=float(np.linalg.norm(R.T@(Q.T@complete_res)))
            moment=central_moment(sp,x,opts["moment_order"])
            weak=read(sp,vt[-1],fine,pose=False)
            second=None
            z=None
            if (obs["relative_strain_max"]<=opts["first_order_gate"]
                    and abs(moment+1)<=opts["moment_gate"]):
                vw=plus(g["pose"],sp.fields(x,g))
                second_rhs=-pack(plus(strains(g["raw"],g["acc"],g["r"]),quadratic(vw,g["r"])),g)
                z=solve(Q.T@second_rhs)
                vf=plus(fine["pose"],sp.fields(x,fine))
                zc=sp.fields(z,fine)
                za=plus(fine["acc"],zc)
                err2=plus(strains(fine["raw"],za,fine["r"]),quadratic(vf,fine["r"]))
                e2=relative(fine["raw"],err2,fine["r"])
                q=opts["predictor_angle_increment"]
                exact_pose=fine["state"](q)
                xc=sp.fields(x,fine)
                trial=[e+q*v+q*q*a/2 for e,v,a in zip(exact_pose,xc,zc)]
                D0,Y0=fine["raw"][1],fine["raw"][2]/fine["r"][:,None,None]
                D,Y=trial[1],trial[2]/fine["r"][:,None,None]
                defect=[dot(D,D)-dot(D0,D0),dot(D,Y)-dot(D0,Y0),dot(Y,Y)-dot(Y0,Y0)]
                second=dict(fine_second_strain_max=float(e2.max()),true_angle_increment=q,
                            true_fixed_metric_predictor_max=float(relative(fine["raw"],defect,fine["r"]).max()),
                            complete_acceleration_coefficients=z.tolist())
                count["second_order_full_solves"]+=1
            del Q
            row=dict(space=label,bands=bands,K=K,columns=sp.size,full_rows=len(rhs),
                     exact_angular_work_nodes=2*K+5,work=work,fine=obs,central_bending_moment=moment,
                     fine_radius_only=independent_radius["relative_strain_max"],
                     fine_angle_only=independent_angle["relative_strain_max"],
                     distance_to_complete_Q_column_range=range_distance,
                     full_normal_residual_norm=normal_difference,
                     exact_unit_pose_moment=-1.,smallest_right_direction_fine=weak,
                     minimum_sigma=float(svals[-1]),maximum_sigma=float(svals[0]),
                     exact_zero_float_singular_values=int(np.sum(svals==0)),complete_assembly_difference=jerr,
                     second_order_evaluated=second is not None,elapsed_seconds=elapsed())
            emit("space",**row,all_singular_values=svals.tolist(),complete_unit_pose_coefficients=x.tolist(),
                 complete_smallest_right_direction=vt[-1].tolist(),second=second)
            last=dict(row=row,complete_unit_pose_coefficients=x.tolist(),second=second)
            summary.append(row)
        emit("terminal",spaces=summary,last=last,counts=dict(count),elapsed_seconds=elapsed(),
             fixed_metric_change=False,nonlinear_path_solved=False,README_completion_claim=False)
    except Exception as exc:
        emit("incomplete",reason=str(exc),spaces=summary,last=last,counts=dict(count),elapsed_seconds=elapsed())
        raise


if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""Literal linear BVP diagnostics of a new fixed tail design.

Each material angular mode is solved independently with both endpoint rows, without
Cauchy shooting or a graph division.  Optional three bridge bubbles preserve
the shallow and bridge-end logw values and first derivatives.  Linear gains
do not certify a nonlinear field or its projection branch.
"""
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from parallel_20261117_dynamic_tail import Background


class BubbleBackground(Background):
    def __init__(self,path,beta=(0.,0.,0.),coordinate='source-index'):
        super().__init__(path,coordinate);self.beta=np.array(beta)
        self.lo=self.data['bridge']['r0'];self.h=self.data['bridge']['r1']-self.lo

    def bubble(self,r):
        t=(r-self.lo)/self.h;mask=(t>=0)&(t<=1);u=np.clip(t,0,1)
        base=16*u*u*(1-u)**2;derivative=32*u*(1-u)*(1-2*u)
        pol=np.array([np.ones_like(u),2*u-1,6*u*u-6*u+1])
        dp=np.array([np.zeros_like(u),2*np.ones_like(u),12*u-6])
        value=np.einsum('i,i...->...',self.beta,base*pol)*mask
        dr=np.einsum('i,i...->...',self.beta,derivative*pol+base*dp)*mask/self.h
        return value,dr

    def __call__(self,x):
        s,ell,z=super().__call__(x);r,rx=self.radial(x);b,br=self.bubble(r)
        return s,ell+br*rx,z*np.exp(2*b)


def solve_modes(bg,trace,modes,tol,max_nodes,unit_amplitude=1e-8):
    rows=[];solutions=[]
    for j in range(modes):
        m=2*(j+1);bp=bg.data['boundary'][j]['p'];bk=bg.data['boundary'][j]['k']
        def fun(x,y):
            s,ell,z=bg(x)
            return np.array([-(s+ell)*y[0]-m*s*y[1],-m*ell*y[0]-2*ell*y[1]])
        def jac(x,y):
            s,ell,z=bg(x);v=np.empty((2,2,len(x)));v[0,0]=-(s+ell);v[0,1]=-m*s;v[1,0]=-m*ell;v[1,1]=-2*ell
            return v
        def bc(ya,yb):return np.array([ya[0]-unit_amplitude,bp*yb[0]+bk*yb[1]])
        x=bg.x;y=np.zeros((2,len(x)));y[0]=unit_amplitude
        sol=solve_bvp(fun,bc,x,y,fun_jac=jac,bc_jac=lambda ya,yb:(np.array([[1.,0.],[0.,0.]]),np.array([[0.,0.],[bp,bk]])),tol=tol,bc_tol=unit_amplitude*1e-10,max_nodes=max_nodes)
        xx=np.ravel(sol.x[:-1,None]+np.diff(sol.x)[:,None]*np.linspace(0,1,5));yy=sol.sol(xx)/unit_amplitude
        target=trace['P_sin_coefficients'][j];expected=trace['K_cos_coefficients'][j]
        row=dict(frequency=m,success=bool(sol.success),nodes=len(sol.x),rms=float(max(sol.rms_residuals)),
                 cut_K_over_P=float(sol.y[1,0]/unit_amplitude),target_P=target,target_K=expected,
                 predicted_cut_K=float(sol.y[1,0]*target/unit_amplitude),cut_K_mismatch=float(sol.y[1,0]*target/unit_amplitude-expected),
                 P_gain=float(np.max(abs(yy[0]))),K_gain=float(np.max(abs(yy[1]))),
                 actual_trace_max_P=float(np.max(abs(yy[0]*target))),actual_trace_max_K=float(np.max(abs(yy[1]*target))))
        rows.append(row);solutions.append(sol)
    return rows,solutions


def main(a):
    started=time.perf_counter();trace=json.loads(a.trace.read_text());beta=[float(s) for s in a.beta.split(',')]
    bg=BubbleBackground(a.background,beta,a.coordinate);rows,_=solve_modes(bg,trace,a.modes,a.tol,a.max_nodes,a.unit_amplitude)
    x=bg.x;r,rx=bg.radial(x);_,ell,z=bg(x);w=np.sqrt(z)
    sampled=dict(max_w=float(np.max(w)),max_meridian_curvature=float(np.max(abs(w*ell/rx)/(1+z)**1.5)),max_angular_curvature=float(np.max(w/(r*np.sqrt(1+z)))))
    report=dict(scope=__doc__,background_sha256=bg.sha256,trace_sha256=hashlib.sha256(a.trace.read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),beta=beta,unit_amplitude=a.unit_amplitude,seconds=time.perf_counter()-started,rows=rows,sampled_background=sampled)
    a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--background',type=Path,required=True);p.add_argument('--trace',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--modes',type=int,default=8);p.add_argument('--beta',default='0,0,0')
    p.add_argument('--coordinate',choices=['source-index','physical-r'],default='source-index');p.add_argument('--tol',type=float,default=1e-6)
    p.add_argument('--max-nodes',type=int,default=16000);p.add_argument('--unit-amplitude',type=float,default=1e-8);main(p.parse_args())

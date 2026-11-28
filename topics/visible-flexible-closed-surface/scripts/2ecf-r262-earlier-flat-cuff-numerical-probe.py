#!/usr/bin/env python3
"""Read actual R262 two-jets at cached radii for a new enlarged-cuff design.

Finite numerical observations only.  No old full-tail certificate is rerun.
"""
import argparse, hashlib, importlib.util, json, os, time
from pathlib import Path
from fractions import Fraction as Q
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline

ORDERS=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module
def dot(a,b):return np.sum(a*b,axis=-1)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','data','grid','field','query-report','query-cache','output'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--radii',type=float,nargs='+',default=[.6,.5,.45,.4,.36,.34,.32,.30,.25,.20,.15])
    ap.add_argument('--angular',type=int,default=384)
    a=ap.parse_args();start=time.monotonic()
    assert not a.output.exists()
    assert sha(a.field)=='5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8'
    joint=load(a.scripts/'6a65-m12-global-common-cut-position-recovered.py','r280_joint')
    whole=load(a.scripts/'6a65-m12-entire-half-cartesian-bvp.py','r280_whole')
    bg=load(a.scripts/'6a65-m12-original-tail-background.py','r280_bg')
    a.background_tolerance=json.loads(a.grid.read_text())['background_tolerance']
    _,meta,bridge,_,_,chart=whole.definition(a,joint,bg)
    src=joint.CommonCutSource(a.data,meta,bridge,a.query_report,a.query_cache)
    _,coeff=joint.ad.exact_section(a.data,Q(0))
    central=joint.ad.NativeCurve(coeff,512,32)
    tail=whole.TailQueries(a.query_report,a.query_cache)
    load(a.scripts/'2ecf-m12-h2-cached-direct-lm-v2.py','r280_cache').cache_tail_apply(whole.TailQueries,[])
    pos=whole.WholePosition(src,central,chart,tail,joint)
    with np.load(a.field) as f:
        spl=BSpline(f['unit_knots'],np.pad(f['coefficients'],((3,3),(0,0))),5)
        pm=f['planar_modes'];hm=f['vertical_modes']
    N=a.angular;theta=np.arange(N)*2*np.pi/N
    u,rho,rhop=pos.angular(N);u=np.asarray(u,float);rho=np.asarray(rho,float);rhop=np.asarray(rhop,float)
    er=np.c_[np.cos(u),np.sin(u),np.zeros(N)]
    et=np.c_[-np.sin(u),np.cos(u),np.zeros(N)]
    ez=np.c_[np.zeros(N),np.zeros(N),np.ones(N)]
    candidates=[Q(k) for k in tail.lookup]
    T=float(chart.total);rows=[]
    for target in a.radii:
        rq=min(candidates,key=lambda x:abs(float(x)-target))
        r=whole.ld(rq);rf=float(r)
        J,bb=pos.tail_point(r,N)
        z=float(chart.inverse_radius(r))
        sc,scq=chart.scales(np.array([z]))
        v=[spl(np.array([z]),j) for j in range(3)]
        v[2]=v[2]/(T*sc[:,None])**2-v[1]*scq[:,None]/(T*sc[:,None]**3)
        v[1]/=T*sc[:,None]
        for l,(i,j) in enumerate(ORDERS):
            coef=v[i]
            plan=(coef[:,:len(pm)]*(1j*pm)**j)@np.exp(1j*pm[:,None]*theta)
            height=(coef[:,len(pm):]*(1j*hm)**j)@np.exp(1j*hm[:,None]*theta)
            J[l]+=np.stack([plan.real[0],plan.imag[0],height.real[0]],axis=-1)
        w,wr,drop,*_=map(float,chart.background.point(r))
        height=float(src.cut_height)+drop;rs=-1/np.sqrt(1+w*w);rss=-w*wr/(1+w*w)**2
        base=np.stack([rf*er+height*ez,rs*(er-w*ez),
                       rf*et*rho[:,None],-rs*rs*wr*ez+rss*(er-w*ez),
                       rs*et*rho[:,None],
                       -rf*er*rho[:,None]**2+rf*et*rhop[:,None]])
        d=J-base
        p,vv,uu,aa,ab,cc=J;E,F,G=dot(vv,vv),dot(vv,uu),dot(uu,uu)
        n=np.cross(vv,uu);ar=np.linalg.norm(n,axis=-1);n/=ar[:,None]
        ll,mm,nn=dot(n,aa),dot(n,ab),dot(n,cc)
        tr=(E*nn-2*F*mm+G*ll)/ar**2
        curv=abs(tr)/2+np.sqrt(np.maximum(0,tr**2/4-(ll*nn-mm**2)/ar**2))
        err=abs(E+G/bb**2-2)/2+np.hypot((E-G/bb**2)/2,F/bb)
        row=dict(requestedRadius=target,actualExactRadius=str(rq),actualRadius=rf,
                 q=float(chart.S+chart.c-r),unitCoordinate=z,
                 axisymmetricHeight=height,backgroundSlope=w,backgroundSlopeDerivative=wr,
                 deviationValueMax=float(np.linalg.norm(d[0],axis=-1).max()),
                 deviationRadialFirstMax=float(np.linalg.norm(d[1],axis=-1).max()),
                 deviationAngularUnitFirstMax=float((np.linalg.norm(d[2],axis=-1)/bb).max()),
                 deviationRadialSecondMax=float(np.linalg.norm(d[3],axis=-1).max()),
                 deviationMixedUnitMax=float((np.linalg.norm(d[4],axis=-1)/bb).max()),
                 deviationAngularUnitSecondMax=float((np.linalg.norm(d[5],axis=-1)/bb**2).max()),
                 actualMetricSampleMax=float(err.max()),actualCurvatureSampleMax=float(curv.max()),
                 heightRange=[float(p[:,2].min()),float(p[:,2].max())])
        rows.append(row);print(json.dumps(row),flush=True)
    packet=dict(schema='R262-actual-original-field-earlier-flat-cuff-design-probe-v1',
                sourceFieldSHA256=sha(a.field),gridSHA256=sha(a.grid),
                querySHA256=sha(a.query_cache),sourceSHA256=sha(__file__),
                prefixS=float(chart.S),actualT1=T,angular=N,rows=rows,
                numericalOnly=True,newCompleteFieldConstructed=False,
                continuousBoundsClaimed=False,seconds=time.monotonic()-start)
    a.output.write_text(json.dumps(packet,indent=2)+'\n')
if __name__=='__main__':main()

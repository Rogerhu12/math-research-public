#!/usr/bin/env python3
"""Directed complete material-pair cover of the actual R293 432-coordinate core.

Every material pair must be covered either by a previously proved complete
component, a chord of length at least 2*rho, or an explicit intrinsic path
shorter than 3.14/K. Combined with the actual global curvature certificate,
this proves embedding and excludes all shorter doubly critical chords.
No finite point cloud is used to decide a bound.
"""
import argparse
import bisect
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
from types import SimpleNamespace
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import numpy as np

GP=1<<30
MP=1<<20
MG=1<<20


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m)
    return m


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def flo(q,scale):q=Q(q);return q.numerator*scale//q.denominator
def cei(q,scale):return -flo(-Q(q),scale)


def angular_bounds(cert,n):
    I=cert.I;pi=cert.pi_interval();base=[]
    for j in range(n+1):
        t=I(Q(j,n));y=t/(1+(1+t.square()).sqrt())
        y2=y.square();power=y;v=I(0)
        for k in range(60):
            v+=((-1)**k)*power/Q(2*k+1);power*=y2
        base.append(4*(v+I(Q(-1,10**35),Q(1,10**35))))
    base[0]=I(0);base[-1]=pi/2
    allangles=[base[j]+q*pi/2 for q in range(4) for j in range(n)] + [2*pi]
    return base,allangles,pi


def central_boxes(cert,budget,A,B,base,pi,panels):
    """True arclength inverse of the exact central ellipse, with midpoint remainder."""
    I=cert.I;quarter=pi/2;step=quarter/panels
    pp=budget.perimeter_over_pi(A,B,32);a0=I(pp[0]/2,pp[1]/2)
    delta=A*A-B*B
    assert delta/B+delta*delta/(4*B**3)<16
    acc=I(0);als=[0];ahs=[0]
    for k in range(panels):
        sn,cs=cert.sincos(step*Q(2*k+1,2))
        acc+=step*(I(A*A)*sn.square()+I(B*B)*cs.square()).sqrt()
        error=I(16)*step.square()*(step*(k+1))/24
        als.append((acc-I.raw(error.hi,error.hi)).lo)
        ahs.append((acc+I.raw(error.hi,error.hi)).hi)
    boxes=[]
    def inverse_box(ul,uh):
        targetlo=(a0*ul).lo;targethi=(a0*uh).hi
        l=max(0,bisect.bisect_left(ahs,targetlo)-1)
        r=min(panels,bisect.bisect_right(als,targethi))
        assert l<=r
        sl,cl=cert.sincos(step*l);sr,cr=cert.sincos(step*r)
        xx=I(A)*I.raw(max(0,cr.lo),min(cert.SCALE,cl.hi))
        yy=I(B)*I.raw(max(0,sl.lo),min(cert.SCALE,sr.hi))
        return [xx,yy]
    n=len(base)-1
    for quadrant in range(4):
        for j in range(n):
            if quadrant%2:
                xy=inverse_box(quarter-base[j+1],quarter-base[j])
            else:xy=inverse_box(base[j],base[j+1])
            if quadrant in (1,2):xy[0]=-xy[0]
            if quadrant in (2,3):xy[1]=-xy[1]
            boxes.append([[float(v.lower()),float(v.upper())] for v in xy])
    out=np.asarray(boxes)
    out[:,:,0]=np.nextafter(out[:,:,0],-np.inf)
    out[:,:,1]=np.nextafter(out[:,:,1],np.inf)
    return out,a0.upper()


def build(a):
    started=time.monotonic()
    D=load(a.source/'2ecf-polar-released-directed-full-polynomial-curvature.py','pair_directed')
    K=load(a.scripts/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py','pair_x87')
    hf=load(a.scripts/'2ecf-strong-hf-interior-continuous-projection.py','pair_polynomial_sections')
    cert=load(a.scripts/'6a65-m12-r137-continuous-domain.py','pair_integer_trig')
    budget=load(a.scripts/'6a65-geometry-central-gap-held-budget.py','pair_ellipse_series')
    edge=json.loads(a.edge.read_text());state=json.loads(a.state.read_text());sol=json.loads(a.spatial.read_text())
    assert edge['closedPrimitiveTrue'] and edge['fieldSHA256']==sha(a.field)
    z=np.load(a.field);kn=list(map(Q,z['knots']));b,T=kn[0],kn[-1]
    S=Q(state['oldS']);pole=S+Q(4,5);flat_r=pole-T
    delta=Q(sol['raisedCuffDelta']);Z=Q(83,200)+delta
    assert sol['controls']==432 and sol['transition']==[0.,1.]
    errs=[[Q(x) for x in row] for row in edge['accurateMinusStoredPhysicalDerivativeMaxUpper']]
    hh=kn[1]-kn[0]
    ec=[[Q(1),0,0],[Q(1),hh/5,0],[Q(1),2*hh/5,hh*hh/20],[0,0,0],[0,0,0],[0,0,0]]
    error_controls=[ec,[[5*(ec[i+1][j]-ec[i][j])/hh for j in range(3)] for i in range(5)]]
    ph=D.Phase(a.quarter_angles,z['coeff'].shape[2])
    phg=D.Phase(a.gram_quarter_angles,z['coeff'].shape[2])
    material_angles,angle,pi=angular_bounds(cert,a.quarter_angles)
    angles=np.array([[flo(x.lower(),MP),cei(x.upper(),MP)] for x in angle],dtype=np.int64)
    ramp=np.load(a.ramp);A,B=Q(float(ramp['centralA'])),Q(float(ramp['centralB']));c=Q(float(ramp['centralLength']))
    eb,a0hi=central_boxes(cert,budget,A,B,material_angles,pi,a.ellipse_panels)
    rows=[];pboxes=[];grams=[];kinds=[]
    def append(l,r,lo,hi,gram,kind):
        rows.append((l,r));pboxes.append(np.stack([np.floor(lo*GP),np.ceil(hi*GP)],axis=2).astype(np.int64))
        grams.append(np.ceil(np.asarray(gram)*MG).astype(np.int64));kinds.append(kind)
    pref=sorted({Q(0),c,b,*[b*Q(j,a.prefix_rows) for j in range(1,a.prefix_rows)]})
    gprefix=[1.000001,float((a0hi+Q(9,4000))**2*Q(1000001,1000000)),1e-7]
    for l,r in zip(pref,pref[1:]):
        lo=np.empty((len(eb),3));hi=lo.copy()
        error=0. if r<=c else .0112
        lo[:,:2]=np.nextafter(eb[:,:,0]-error,-np.inf)
        hi[:,:2]=np.nextafter(eb[:,:,1]+error,np.inf)
        lo[:,2]=np.nextafter(float(l)-(0 if r<=c else .000782),-np.inf)
        hi[:,2]=np.nextafter(float(r)+2e-10,np.inf)
        append(l,r,lo,hi,gprefix,1)
    def split(pack,depth):
        if depth==0:return [pack]
        child=[D.left_right(p) for p in pack]
        return split([p[0] for p in child],depth-1)+split([p[1] for p in child],depth-1)
    args=SimpleNamespace(field=a.field,state=a.state,spatial=a.spatial,scripts=a.scripts,start_cell=0,end_cell=128)
    for cell,l,r,(P,Ps,Pss) in D.pieces(args,K,hf):
        pack=[ph.vals(P,0),phg.vals(Ps,0),phg.vals(P,1)]
        if cell==0:
            for index,(order,angular) in enumerate(((0,0),(1,0),(0,1))):
                err=np.array([np.nextafter(float(sum(abs(w)*errs[k][angular] for k,w in enumerate(v))),np.inf)
                              for v in error_controls[order]])[:,None,None]
                pack[index]=(np.nextafter(pack[index][0]-err,-np.inf),np.nextafter(pack[index][1]+err,np.inf))
        parts=split(pack,a.radial_depth);count=len(parts)
        for j,part in enumerate(parts):
            boxes=[(np.min(p[0],axis=0),np.max(p[1],axis=0)) for p in part]
            E=D.dot(boxes[1],boxes[1])[1];G=D.dot(boxes[2],boxes[2])[1];F=D.dot(boxes[1],boxes[2])
            gram=[np.max(E),np.max(G),np.max(np.maximum(abs(F[0]),abs(F[1])))]
            append(l+(r-l)*Q(j,count),l+(r-l)*Q(j+1,count),*boxes[0],gram,4)
        if cell%16==0:print('ENCLOSED',cell,len(rows),flush=True)
    # Exact rational unit-circle coordinate intervals on the same tan-half-angle boxes.
    circle=[]
    for q in range(4):
        for j in range(a.quarter_angles):
            t0,t1=Q(j,a.quarter_angles),Q(j+1,a.quarter_angles)
            co=(Q(1)-t1*t1)/(1+t1*t1),(Q(1)-t0*t0)/(1+t0*t0)
            sn=2*t0/(1+t0*t0),2*t1/(1+t1*t1)
            x,y=co,sn
            for _ in range(q):x,y=(-y[1],-y[0]),x
            circle.append((x,y))
    for j in range(a.flat_rows):
        l=T+(pole-T)*Q(j,a.flat_rows);r=T+(pole-T)*Q(j+1,a.flat_rows)
        lo=np.empty((len(circle),3));hi=lo.copy()
        for k,xy in enumerate(circle):
            for d in range(2):
                vals=[v*rr for v in xy[d] for rr in (pole-l,pole-r)]
                lo[k,d]=np.nextafter(float(min(vals)),-np.inf);hi[k,d]=np.nextafter(float(max(vals)),np.inf)
        lo[:,2]=np.nextafter(float(Z),-np.inf);hi[:,2]=np.nextafter(float(Z),np.inf)
        append(l,r,lo,hi,[1.,np.nextafter(float((pole-l)**2),np.inf),0.],2)
    upper=np.asarray(pboxes);nupper=len(rows)
    lower=upper[::-1].copy();lower[:,:,2,0]=-upper[::-1,:,2,1];lower[:,:,2,1]=-upper[::-1,:,2,0]
    boxes=np.concatenate((lower,upper),axis=0);del lower,upper,pboxes
    rows=[(-r,-l) for l,r in rows[::-1]]+rows
    grams=np.array(grams[::-1]+grams,dtype=np.int64)
    kind=np.array([3 if k==2 else k for k in kinds[::-1]]+kinds,dtype=np.int8)
    ns,nu=boxes.shape[:2]
    sgrid=np.array([[flo(l,MP),cei(r,MP)] for l,r in rows],dtype=np.int64)
    assert all(rows[i][1]==rows[i+1][0] for i in range(len(rows)-1))
    short_square=(Q(314,100)/a.curvature)**2
    header=np.array([0x52503239380001,ns,nu,cei(pi.upper(),MP),flo(2*pi.lower(),MP),
                     cei(2*pi.upper(),MP),cei((2*a.radius)**2,GP*GP),cei(2*a.radius,GP),
                     short_square.numerator,short_square.denominator,GP,MP,MG],dtype='<i8')
    arrays=[header,boxes,grams,sgrid,angles,kind.astype(np.int64)]
    digest=hashlib.sha256()
    with a.output.open('xb') as f:
        for arr in arrays:
            data=np.ascontiguousarray(arr,dtype='<i8').tobytes();digest.update(data);f.write(data)
    report=dict(schema='actual-complete-released-core-material-pair-boxes-v2',entrySHA256=sha(__file__),
        fieldSHA256=sha(a.field),stateSHA256=sha(a.state),spatialSHA256=sha(a.spatial),
        trueEndpointSHA256=sha(a.edge),directedSourceSHA256=sha(a.source/'2ecf-polar-released-directed-full-polynomial-curvature.py'),
        radius=str(a.radius),curvature=str(a.curvature),shortPathSquare=str(short_square),
        angularSectors=nu,gramAngularSectors=4*a.gram_quarter_angles,radialRows=ns,
        physicalClosedBoxes=ns*nu,radialDepth=a.radial_depth,prefixRows=a.prefix_rows,
        flatRows=a.flat_rows,ellipseMidpointPanels=a.ellipse_panels,
        completeBoxFileSHA256=digest.hexdigest(),completeBoxFileBytes=a.output.stat().st_size,
        requiresActualWholeCurvatureProof=True,consumesR267TruePrefix=True,
        firstExactCharacteristicTraceIncluded=True,exactCuffHeight=str(Z),
        exactFlatJoinRadius=str(flat_r),maximumUpperGram=(grams.max(axis=0)/MG).tolist(),
        seconds=time.monotonic()-started)
    a.output.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    for n in ('scripts','source','state','field','spatial','edge','ramp','output'):p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--radius',type=Q,default=Q(19,200));p.add_argument('--curvature',type=Q,default=Q(1041,100))
    p.add_argument('--quarter-angles',type=int,default=256);p.add_argument('--gram-quarter-angles',type=int,default=1024);p.add_argument('--radial-depth',type=int,default=2)
    p.add_argument('--prefix-rows',type=int,default=16);p.add_argument('--flat-rows',type=int,default=16)
    p.add_argument('--ellipse-panels',type=int,default=4096)
    build(p.parse_args())

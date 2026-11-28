#!/usr/bin/env python3
"""Impose both true held-support planes on every original G10 point with actual clamped position modes."""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy import sparse
from scipy.optimize import linprog


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp)
    sys.modules[name]=m;sp.loader.exec_module(m);return m


joint=load(Path(__file__).with_name("2ecf-strong-stadium-physical-guide-spectrum.py"),"true_stadium_physical_guide")
c=joint.c
def main(args):
    initial=time.monotonic()
    args.resume=None;args.guide_scale=.0025
    definition,basis,clock,physical,g11,_,mods,radius,meta,_=joint.actual_stadium(args)
    gs=json.loads(args.prior_guide.read_text())
    if gs["model"]["actualSameStadiumG"]!=meta["actualMetric"] or gs["model"]["fixedStadiumCompleteSource"]!=c.sha(args.fixed_stadium):
        raise ValueError("Actual same physical corrected field required")
    zg=np.asarray(gs["coefficients"]).reshape(basis.nb,basis.na)
    direct=joint.load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","linear_hold_independent").direct_packet
    groups=dict(**physical,independent=g11)
    for name,cache in groups.items():
        for j in range(0,len(cache.nodes),12):
            sl=slice(j,j+12);xx=cache.nodes[sl]
            cache.jets[sl]+=direct(basis,xx,zg,cache.u) if name=="independent" else basis.packet(basis.matrices(xx),zg,len(cache.u))
    x=physical["training"].nodes
    if not np.array_equal(x,physical["observer"].nodes):raise ValueError("Distinct original G10 labels")
    B,Bs,Bss=(a.toarray() for a in basis.matrices(x));n=basis.nb
    # At each angle use a genuine first harmonic in y and a genuine constant in z.
    cy=basis.channels.index((1,1,"sin"));cz=basis.channels.index((2,0,"cos"))
    A=float(definition["pointConfig"]["central_a"]);side=A-args.distance*np.sqrt(2.)
    actual_limit=A-.65*np.sqrt(2.)
    pre={};P=[];am=[]
    for name,obj in groups.items():
        xyz=obj.jets[:,0];h=np.abs(xyz[...,1])-xyz[...,2]-actual_limit
        idx=np.unravel_index(h.argmax(),h.shape);pre[name]=dict(plane=float(h[idx]),x=float(obj.nodes[idx[0]]),u=float(obj.u[idx[1]]))
        if name!="independent":
            P.append(xyz);am.append(np.sin(obj.u))
    Y=np.concatenate([p[...,1] for p in P],axis=1)
    Z=np.concatenate([p[...,2] for p in P],axis=1)
    sine=np.concatenate(am)
    if np.max(abs(Y[:1]))==0:raise ValueError("Degenerate actual sample")
    # Static support enclosures keep first and second derivatives from spiking between active rings.
    raw=copy=None
    ks=np.unique(basis.knots);knots=np.unique(np.r_[ks,(ks[:-1]+ks[1:])/2,(3*ks[:-1]+ks[1:])/4,(ks[:-1]+3*ks[1:])/4])
    _,d1,d2=(b.toarray() for b in basis.matrices(knots))
    active=[]
    for which in range(2):
        for M,bound in ((d1,args.first),(d2,args.second)):
            pad=np.zeros_like(M);D=np.column_stack((M,pad) if which==0 else (pad,M))
            active.append((D,np.full(len(D),bound)));active.append((-D,np.full(len(D),bound)))
    # Keep upper heights with the unchanged original allowance even during the lift.
    # The optional z cap is a fixed bound on the true zero-mode displacement.
    integ=(basis.knots[6:]-basis.knots[:-6])[3:-3]/6
    cost=np.r_[integ,args.height_cost*integ]
    coeff=np.zeros(2*n);history=[];seen=set()
    for i in range(24):
        beta=B@coeff[:n];gamma=B@coeff[n:]
        signed=np.stack((Y-beta[:,None]*sine-Z-gamma[:,None]-side,
            -Y+beta[:,None]*sine-Z-gamma[:,None]-side))
        mt=signed.max(axis=2);worst=float(mt.max())
        history.append(dict(iteration=i,maxG10=worst,activeRows=len(seen)))
        if worst<=2e-9:break
        ix,jx=np.where(mt>1e-9);lamp=signed[ix,jx].argmax(axis=1)
        fresh=[(int(i),int(j),int(k)) for i,j,k in zip(ix,jx,lamp) if (int(i),int(j),int(k)) not in seen]
        if not fresh:raise ArithmeticError(("Stalled separation",worst))
        seen.update(fresh);ii,jj,kk=np.array(fresh).T;sign=1.-2*ii
        M=np.column_stack((-sign[:,None]*sine[kk,None]*B[jj],-B[jj]))
        rhs=side-sign*Y[jj,kk]+Z[jj,kk]
        active.append((M,rhs))
        G=sparse.csr_matrix(np.vstack([a for a,_ in active]));u=np.concatenate([b for _,b in active])
        lp=linprog(cost,A_ub=G,b_ub=u,bounds=[(0,args.ymax)]*n+[(0,args.zmax)]*n,method="highs",
            options=dict(primal_feasibility_tolerance=1e-9,dual_feasibility_tolerance=1e-9))
        if not lp.success:
            data=dict(model=meta,prior=c.sha(args.prior_guide),initial=pre,history=history,status=lp.message,
                scope="Only the stated 152-variable amplitude and sampled derivative boxes")
            c.save(Path(str(args.prefix)+"-infeasible.json"),data)
            raise ArithmeticError(lp.message)
        coeff=lp.x
    else:raise ArithmeticError("Separation limit")
    z=np.zeros_like(zg);z[:,cy]=-coeff[:n];z[:,cz]=coeff[n:]
    for name,obj in groups.items():
        for j in range(0,len(obj.nodes),18):
            sl=slice(j,j+18);xx=obj.nodes[sl]
            obj.jets[sl]+=direct(basis,xx,z,obj.u) if name=="independent" else basis.packet(basis.matrices(xx),z,len(obj.u))
    saved=json.loads(args.prepared.read_text())
    actual=joint.hf.sample(groups,mods,saved,definition,clock,args)
    post={}
    for name,obj in groups.items():
        xyz=obj.jets[:,0]
        h=np.abs(xyz[...,1])-xyz[...,2]-actual_limit;idx=np.unravel_index(h.argmax(),h.shape)
        post[name]=dict(plane=float(h[idx]),x=float(obj.nodes[idx[0]]),u=float(obj.u[idx[1]]))
    result=dict(schema="actual-full-nonellipse-two-linear-held-support-plane-separation-v1",
        entry=c.sha(__file__),parent=c.sha(args.prior_guide),metric=meta["actualMetric"],actualSource=c.sha(args.fixed_stadium),
        held=0.65,projectionHeldMargin=args.distance,side=side,shapeDirections=["y -= sin(u) B beta","z += B gamma"],
        positionSpaceDimension=basis.dimension,restrictedProjectionColumns=2*n,geometryRings=len(x),geometryRows=2*len(x)*len(sine),
        allPhysicalG10Rows=4291840,originalG11Untouched=True,maximumAmplitudes=[args.ymax,args.zmax],sampledFirstSecond=[args.first,args.second],
        coefficientHex=[float(v).hex() for v in coeff],coefficients=z.ravel().tolist(),pre=pre,post=post,
        G10G11=actual,history=history,continuousGuideCertified=False,seconds=time.monotonic()-initial)
    sha=c.save(Path(str(args.prefix)+"-hold.json"),result)
    print(json.dumps(dict(event="real_all_G10_planes",SHA=sha,pre=pre,post=post,
        full={n:{k:v[k] for k in ("metric","curvature","held","guide")} for n,v in actual.items()},history=history)),flush=True)


if __name__=="__main__":
    ap=joint.slope.args_base()
    ap.add_argument("--fixed-stadium",type=Path,required=True);ap.add_argument("--prior-guide",type=Path,required=True)
    ap.add_argument("--distance",type=float,default=.651)
    ap.add_argument("--first",type=float,default=.35);ap.add_argument("--second",type=float,default=8.)
    ap.add_argument("--ymax",type=float,default=.14);ap.add_argument("--zmax",type=float,default=.08)
    ap.add_argument("--height-cost",type=float,default=2.5)
    main(ap.parse_args())

#!/usr/bin/env python3
"""Whole-image observer on a named true-arc R262 field, its original high flat caps, real tail, and both thick arms."""
import argparse
from fractions import Fraction
import gc
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import numpy as np
from scipy.spatial import ConvexHull, cKDTree
from scipy.spatial.distance import cdist


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()


def require(ok,message):
    if not ok:
        raise ValueError(message)


def tail_caps(src,n,steps,whole,cut,micro):
    chart=src.chart
    raw=src.pos.tail
    candidates=sorted(Fraction(k) for k in raw.lookup)
    radii=np.asarray([float(q) for q in candidates])
    indices=np.unique([int(np.argmin(abs(radii-v))) for v in np.linspace(float(chart.cuff),float(chart.c),steps+1)])[::-1]
    def long(q):
        return np.longdouble(q.numerator)/np.longdouble(q.denominator)
    actual=[long(candidates[i]) for i in indices]
    require(actual[0]==chart.c and actual[-1]==chart.cuff,"tail exact cut or cuff absent")
    theta=np.arange(n)*2*np.pi/n
    u=np.asarray(src.pos.angular(n)[0],np.longdouble)
    er=np.column_stack((np.cos(u),np.sin(u),np.zeros_like(u)))
    ep=np.exp(1j*theta[:,None]*src.pm)
    eh=np.cos(theta[:,None]*src.hm)
    pts=[]
    for r in actual:
        coef=raw.coefficient(r)
        p=raw.apply(coef[0],u,0)+r*er
        p[:,2]+=src.pos.src.cut_height+chart.background.point(r)[2]
        z=float(chart.inverse_radius(r))
        v=src.spline(z)
        xy=ep@v[:len(src.pm)]
        h=eh@v[len(src.pm):]
        point=np.asarray(p,float)+np.column_stack((xy.real,xy.imag,h))
        if whole is not None:
            coord=src.S if r==chart.c else (src.T if r==chart.cuff else z*src.T)
            kn,coeff,m,c,T=whole
            t=np.clip((coord-c)/(T-c),0.,1.)
            basis=cut.Bvals(np.array([t]),kn)[0]
            point+=micro.fft_forward(basis@coeff,m,n,0.,0)[0]
        pts.append(point)
    height=float(src.pos.src.cut_height+chart.background.point(chart.cuff)[2])
    cuff=np.asarray(chart.cuff*er,float)
    cuff[:,2]=height
    cuff_mismatch=float(np.linalg.norm(pts[-1]-cuff,axis=-1).max())
    require(cuff_mismatch<1e-7,"actual corrected W tail does not meet its flat disk")
    uv=np.stack(np.meshgrid(np.asarray(actual,float),theta,indexing="ij"),axis=-1)
    rows=[("tail",np.asarray(pts).reshape(-1,3),uv.reshape(-1,2))]
    radii=np.linspace(0,float(chart.cuff),max(9,steps//4))
    disk=np.asarray(radii[:,None,None]*er[None],float)
    disk[:,:,2]=height
    uv=np.stack(np.meshgrid(radii,theta,indexing="ij"),axis=-1)
    rows.append(("cap",disk.reshape(-1,3),uv.reshape(-1,2)))
    return rows,height,cuff_mismatch,pts[0],theta


def observe_ends(a,src,micro,definition,geo,arm,body):
    cut=module(a.cut,'adjacentActualCutEvaluator')
    cut.true_arc_position=definition.true_arc_position
    with np.load(a.state,allow_pickle=False) as state:
        known={"94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6","29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902","e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e","bc1836eb40110bb5fd9abfeeb8819ecf22b95ef334140109f6652dfcafb35917"}
        require(sha(a.definition) in known and
                str(state["cutSHA"])==sha(a.cut),"new normal curve or actual cut differs")
        frozen=module(a.scripts/"2ecf-r262-three-arcs-frozen-height-and-metric-refinement.py","r262_frozen_obs")
        a.physical_source=a.definition
        frozen.action_args(a,state)
        require((src.S,src.T)==(a.S,a.T),"different physical whole material chart")
        require(a.lam==1. and a.low==definition.LOW and a.full_sleeve==.350,"different central input")
        all_rings="heightDropEnd" in state.files
        a.modes=int(state["modes"])
        a.spans=int(state["spans"])
        require(not all_rings and "heatGain" not in state.files and "wholeTailXYZ" not in state.files,"expected actual ordinary or three-profile base cut")
        profiles=None
        if "physicalInletProfiles" in state.files:
            require(a.profile_source is not None and str(state["inletProfileSourceSHA"])==sha(a.profile_source),"different actual inlet profile")
            X=state["inletNativeXYZ"].copy()
            profiles=state["physicalInletProfiles"].copy()
        else:
            X=state["actualPhysicalXYZ"].copy()
        kn=state["knots"].copy()
        metric_kn=state["metricKnots"].copy() if "metricKnots" in state.files else kn
        aq=state["metricQ"].copy()
        aw=state["metricW"].copy()
    k617=definition.LOW==.617
    expected="73827ac7922cbb1580b5fddb8a9ff57155fd226eb8796af52a553b57567b9244" if k617 else "98cc2fcc1192195ac0615a4ce752e541665f1d64f775ff9cf92ee80e2e5957bc"
    whole=None
    if a.whole_state is not None:
        require(a.field_source is not None and sha(a.field_source)=="86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841","wrong full-half field generator")
        whole_api=module(a.field_source,"actualWholeHalfShape")
        with np.load(a.whole_state,allow_pickle=False) as state:
            known={"sourceSHA","fieldSHA","parentSHA","wholeTailXYZ","unitKnots","modes","c","actualCommonCut","actualCuffCoordinate"}
            require(set(state.files)-{"solverSHA","wallSHA"}==known,"unknown whole-half channels")
            require(str(state["parentSHA"])==sha(a.state) and str(state["fieldSHA"])==src.source_sha and str(state["sourceSHA"])==sha(a.field_source),"different whole-parent or original source")
            require((float(state["c"]),float(state["actualCommonCut"]),float(state["actualCuffCoordinate"]))==(a.full_sleeve,src.S,src.T),"different physical chart")
            wk=state["unitKnots"].copy();wc=state["wholeTailXYZ"].copy();wm=int(state["modes"])
            require(wc.shape==(len(wk)-12,3*wm+2) and np.isfinite(wc).all() and np.all(np.diff(wk)>=0) and np.all(wk[:6]==0) and np.all(wk[-6:]==1),"bad normalized spline")
            whole=wk,wc,wm,a.full_sleeve,src.T
    require(a.angles>2*max(a.modes,0 if whole is None else whole[2]),"use enough native angles to resolve all Cartesian modes")
    require(sha(a.belt)==expected,"the belt must implement its actual axial window")
    ports,_=body.setup(arm,definition,geo,a.low,a.anchor,a.full_sleeve)
    q,theta,J,rho,old,oldrho,unused,gate=cut.geometry(src,geo,None,a,a.radial,a.angles,False)
    del old,oldrho
    B=cut.Bvals(q,kn)
    require(X.shape==(B[0].shape[1],3*a.modes+2),"physical XYZ block has a different literal basis")
    Pextra=None
    if profiles is not None:
        require(profiles.shape==(X.shape[0],3),"wrong number of physical inlet channels")
        profile=module(a.profile_source,"actualClosedInletShape")
        Pextra=profile.angles_profile(definition,cut,src,geo,a,a.angles,False)[0]
    if whole is not None:
        wb=whole_api.field_basis(cut,whole[0],q,np.ones(len(q)),np.zeros(len(q)),a.full_sleeve,src.T)
    for i,(r,j) in enumerate(src.base.O):
        J[:,i]+=micro.fft_forward(B[r]@X,a.modes,a.angles,float(theta[0]),j)
        if Pextra is not None:
            amp=B[r]@profiles
            for d in range(3):J[:,i,:,d]+=amp@Pextra[j,d]
        if whole is not None:
            J[:,i]+=micro.fft_forward(wb[r]@whole[1],whole[2],a.angles,float(theta[0]),j)
    metric_basis=cut.Bvals(q,metric_kn)[0]
    Q=1+metric_basis@aq
    if hasattr(a,"drop"):
        velocity=a.full_sleeve*a.drop(q)[1]
        Q+=velocity**2
    W=1+metric_basis@aw
    error=micro.gram(J,Q[:,None],W[:,None],rho)[1]
    k,area=micro.curvature(J)
    # The lower mirror and both rigid pose mappings preserve these unsigned principal curvatures.
    normal=-np.cross(J[:,1],J[:,2])/np.sqrt(area)[:,:,None]
    keep=np.ones(len(q),dtype=bool) if all_rings else q>=a.full_sleeve
    position=J[keep,0].copy()
    support=np.sum(normal[keep]*position,axis=-1)
    min_index=lambda x,how:list(map(int,np.unravel_index(how(x),x.shape)))
    geo_report=dict(positionsInPrefix=int(position.size//3),positiveArea=float(area[keep].min()),
            observedPrefixMetricPeak=float(error[keep].max()),curvatureMax=float(k[keep].max()),
            supportMinimum=float(support.min()),exteriorHeightMinimum=float(position[:,:,2].min()),
            exteriorHeightMaximum=float(position[:,:,2].max()),
            supportIndex=min_index(support,np.argmin),curvatureIndex=min_index(k[keep],np.argmax),
            sourceRowsKept=[float(q[keep][0]),float(q[keep][-1])],
            radiusMaximum=float(np.linalg.norm(position[:,:,:2],axis=-1).max()))
    radial=np.linalg.norm(position[:,:,:2],axis=-1)
    height=np.abs(position[:,:,2])
    initial_limit,radius_limit,arm_rad=3.830,1.915,(2.197 if k617 else 2.194)
    mixed=(radial+arm_rad)**2+(height+.233)**2
    geo_report["observedPrefixShapeSufficientMargins"]={
        "planarRadius":float(radius_limit-radial.max()),
        "originRadius":float(initial_limit/2-np.linalg.norm(position,axis=-1).max()),
        "armMixedSquared":float(initial_limit**2-mixed.max()),
        "minimumExternalZForArmNormalBalls":float(position[:,:,2].min()-.348),
        "maximumMixedLocation":min_index(mixed,np.argmax)}
    matq=q[keep]+(a.full_sleeve if all_rings else 0.)
    uv=np.stack(np.meshgrid(matq,theta,indexing="ij"),axis=-1)
    rows=[("prefix",position.reshape(-1,3),uv.reshape(-1,2))]
    del J,normal,support,k,area,B,error
    gc.collect()
    ends,cap_z,cuff_diff,cutring,tail_theta=tail_caps(src,a.angles,a.tail_radii,whole,cut,micro)
    require(np.max(abs(tail_theta-theta))<1e-12,"angular grids do not agree across cut")
    cutoff=float(np.linalg.norm(position[-1]-cutring,axis=-1).max())
    require(cutoff<1e-7,"true old tail does not meet new field")
    check=cut.xyz(definition.true_arc_position(geo,np.asarray(src.center.arc(theta)),a.anchor))
    check[:,2]=a.full_sleeve
    seam=float(np.linalg.norm(position[0]-check,axis=-1).max())
    require(seam<1e-7,"new actual sleeve and actual material inlet differ")
    geo_report.update(originalCapHeight=cap_z,trueCuffPositionMismatch=cuff_diff,
                      trueCutPositionMismatch=cutoff,sleevePositionMismatch=seam,
                      numericOldTailRadii=ends[0][1].shape[0]//a.angles)
    rows.extend(ends)
    def pose(eta):
        parts=list(body.components(arm,definition,geo,a.low,a.anchor,a.full_sleeve,eta,
                                   a.belt_angles,a.belt_radial,a.bend,a.chi))
        for tag,pts,uv in rows:
            moved=arm.rotation(pts,eta)
            parts.append((tag+"+",moved,uv))
            lower=moved.copy()
            lower[:,2]*=-1
            parts.append((tag+"-",lower,uv))
        labels=[item[0] for item in parts]
        points=np.concatenate([p for name,p,v in parts])
        points=arm.holding_frame(points,ports[1],eta,initial=definition.PHASE)
        param=np.concatenate([v for name,p,v in parts])
        piece=np.repeat(np.arange(len(parts)),[len(v) for name,p,v in parts])
        require(np.all(np.isfinite(points)),"nonfinite physical curve")
        def witness(index):
            return dict(part=labels[piece[index]],parameter=param[index].tolist(),xyz=points[index].tolist())
        return points,piece,labels,witness
    return pose,geo_report


def diameter(points,ids,label,witness):
    # Face-interior points cannot increase diameter; the block cdist is exact for the supplied finite cloud.
    hull=ConvexHull(points).vertices
    best=-1.
    pair=None
    for begin in range(0,len(hull),192):
        batch=hull[begin:begin+192]
        dist=cdist(points[batch],points[hull],metric="sqeuclidean")
        i,j=np.unravel_index(np.argmax(dist),dist.shape)
        if dist[i,j]>best:
            best=dist[i,j]
            pair=batch[i],hull[j]
    return dict(value=float(np.sqrt(best)),points=int(len(points)),hull=int(len(hull)),
                pair=[witness(p) for p in pair])


def held(A,B,descA,descB):
    dist,idx=cKDTree(B).query(A,workers=1)
    i=int(np.argmax(dist))
    return dict(value=float(dist[i]),source=descA(i),nearest=descB(int(idx[i])))


def main(a):
    micro=module(a.scripts/"2ecf-r262-small-input-full-xyz-positive-metric-v2.py","R262obsmicro")
    body=module(a.belt,"R311obsbelt")
    arm=module(a.arms,"R302obsarms")
    definition=module(a.definition,"newPhysicalR262Definition")
    geo=definition.NormalCurve()
    if a.cut is None:a.cut=a.scripts/"2ecf-r262-three-arcs-shortened-prefix-v2.py"
    fielddir=a.work/"h2-c2-m48-g12-04r1"
    a.data=a.work/"m12-prefix-data.npz.gz"
    a.grid=fielddir/"grid.json"
    a.query_report=fielddir/"exact-tail-queries.json"
    a.query_cache=Path(str(a.query_report)+".npz")
    a.field=fielddir/"result.json.field.npz"
    src=micro.Source(a)
    pose,gr=observe_ends(a,src,micro,definition,geo,arm,body)
    gr["physicalInput"]=sha(a.definition)
    gr["hasPhysicalProfiles"]=a.profile_source is not None
    gr["wholeState"]=sha(a.whole_state) if a.whole_state is not None else None
    A,idA,labA,wa=pose(definition.PHASE)
    B,idB,labB,wb=pose(0.)
    da=diameter(A,idA,labA,wa)
    db=diameter(B,idB,labB,wb)
    ab,ba=held(A,B,wa,wb),held(B,A,wb,wa)
    report=dict(schema="R262-full-half-ordinary-or-physical-inlet-and-complete-tail-closed-shape-v2",
      sourceSHA256=sha(__file__),stateSHA256=sha(a.state),fieldSHA256=src.source_sha,
      wholeStateSHA256=sha(a.whole_state) if a.whole_state else None,profileSourceSHA256=sha(a.profile_source) if a.profile_source else None,
      definitionSHA256=sha(a.definition),beltSHA256=sha(a.belt),armSourceSHA256=sha(a.arms),
      cutSHA256=sha(a.cut),comparisonSHA256=sha(a.comparison),centralProfile=getattr(body,"PROFILE","R309-R311"),anchor=a.anchor,low=a.low,sleeve=a.full_sleeve,
      geometry=gr,initialPhase=definition.PHASE,otherPhase=0.,holdingArm=1,
      initialDiameter=da,otherDiameter=db,initialToOtherHeld=ab,otherToInitialHeld=ba,
      sampledHeldRatio=max(ab["value"],ba["value"])/da["value"],
      sampledHalfDiameterDifferenceRatio=abs(db["value"]-da["value"])/(2*da["value"]),
      sampledRequiredReach=.03*da["value"],
      materialKeys={"arm0/1":["meridian row index","chi"],"belt":["z","unit-speed material u"],
          "prefix+/-":["new physical meridian","native theta of the unrotated field"],
          "tail+/-":["actual original radius","native theta of unrotated field"],
          "cap+/-":["disk radius","native theta mapped to true physical angle"]},
      scope="Finite independent shape diagnostics on real parts of the same surface. Reach and continuous diameter, Hausdorff and full-domain metric inequalities require continuous arguments.")
    with a.out.open("x") as f:
        json.dump(report,f,indent=2,allow_nan=False)
        f.write("\n")
    print("HIGH_CAPS_ACTUAL",json.dumps({k:report[k] for k in ("low","sleeve","initialDiameter","otherDiameter",
          "sampledHeldRatio","sampledHalfDiameterDifferenceRatio","geometry")}),flush=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    for key in ("scripts","work","definition","comparison","state","belt","arms","out"):
        p.add_argument("--"+key,required=True,type=Path)
    for key in ("cut","whole-state","profile-source","field-source"):
        p.add_argument("--"+key,type=Path)
    for key,d in (("radial",84),("angles",144),("tail-radii",61),("belt-angles",240),("belt-radial",33),
                  ("bend",36),("chi",56)):
        p.add_argument("--"+key,type=int,default=d)
    main(p.parse_args())

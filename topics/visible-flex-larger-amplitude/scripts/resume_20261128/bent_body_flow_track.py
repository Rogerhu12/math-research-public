"""True finite-time pullback of the recorded Run39 material velocity on closed charts."""
import hashlib
import importlib
import json
import math
import os
from pathlib import Path
import sys
import time
import traceback

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.linalg import eigvalsh

import bent_body_ambient as ambient
import bent_body_killing as parent
from bent_body_flow_field import ClosedAtlas, Field


def norm(v):
    return float(np.linalg.norm(v))


def world(t):
    c,s=np.cos(t),np.sin(t)
    return np.array([[c,-s,0.],[s,c,0.],[0.,0.,1.]])


def address(tag,u,v):
    return {"chart":tag,"coordinate_1":float(u),"coordinate_2":float(v)}


def load_field(directory,r):
    file=directory/("stage-%02d.npz"%r["stage"])
    if file.stat().st_size!=r["npz_bytes"] or parent.filehash(file)!=r["npz_sha256"]:
        raise ValueError("replayed Run39 stage NPZ changed")
    with np.load(file,allow_pickle=False) as data:
        z,x=data["physical"].copy(),data["material"].copy()
    if (parent.digest(z),parent.digest(x),parent.digest(np.r_[z,x]))!=(
        r["physical_sha256"],r["material_sha256"],r["point_sha256"]):
        raise ValueError("actual replayed parent coordinates changed")
    return z,x


def seeds(field,r,p):
    a=field.a
    def disk(x,y,lo=False):
        u=a.m0+1+x
        return address("cylinder",a.period-u if lo else u,y)
    if a.d["geometry"]=="equal":marks=a.g.MARKS
    else:marks=a.g.disk.MARKERS
    mx,my,mr=marks[0]
    items=[("upper_grip",disk(.07,-.09)),("upper_marker_slope",disk(mx+.46*mr,my+.17*mr)),
           ("upper_bend",disk(.43,.28)),("lower_bend",disk(.48,-.29,True)),
           ("upper_y_rim",disk(.12,.996)),("lower_y_rim",disk(-.15,-.996,True)),
           ("right_meridian",address("cylinder",a.m0+2.+.10,1/1024))]
    for side in ("+","-"):
        direction=1 if side=="+" else -1
        items.extend([("head_"+side,address("end"+side,.17*a.period,.57*a.head.END_LENGTH)),
                      ("cap_center_"+side,address("cap-center"+side,a.center[0],a.center[2])),
                      ("cap_interior_"+side,address("cap"+side,.78*a.period,.54))])
        scores=[]
        for u in np.linspace(0.,a.period,p["seam_probe_angles"],endpoint=False):
            x,_=field.velocity("tube",[u,direction*(a.rim+.46*a.width)])
            scores.append((-direction*x[1],float(u)))
        for label,which in (("positive_outward",max),("negative_outward",min)):
            speed,u=which(scores)
            if label=="positive_outward":
                rec={"chart":"tube","coordinate_1":u,"coordinate_2":direction*(a.rim+.51*a.width)}
            else:
                pos=a.base("tube",[u,direction*(a.rim+.47*a.width)])[0][0]@a.frame.T+a.center
                rec={"chart":"cart"+side,"coordinate_1":float(pos[0]),"coordinate_2":float(pos[2])}
            rec["probe_initial_signed_outward_speed"]=speed
            items.append(("seam_"+side+label,rec))
    for key in ("max_Killing","max_material_chart_speed","max_abs_principal","min_support","max_fixed_gram"):
        if key in r["check"]:
            items.append(("actual_check_"+key,r["check"][key]))
    for key,part in r["check"]["parts"].items():
        items.append(("actual_part_"+key,part["Killing_arg"]))
    return items


def evaluate(field,target,seed,level,p,tag,partial):
    a=field.a
    if seed["chart"]=="tube" or seed["chart"].startswith("cart"):
        chart="tube" if seed["chart"]=="tube" else "cap"+seed["chart"][-1]
        q=np.array([seed["coordinate_1"],seed["coordinate_2"]])
    else:
        chart,q=a.seed(seed)
    hmark,dmark=a.marker(chart,q)
    marker_tan=np.outer([0.,0.,1.],dmark)
    r0,chi,x0=a.base(chart,q)
    target_f=r0+target.values(r0,chi)
    ref_tan=a.frame@target_f[1:3].T+marker_tan
    Gstar=ref_tan.T@ref_tan
    K0=field.physical.original_difference(r0,chi)
    A0=field.material.original_difference(r0,chi)
    _,ff,ex,xzero=field.jets(chart,q)
    X0,dX0=field.velocity(chart,q)
    Xcomparison=norm(X0-ambient.material_velocity(ff[None],ex[None],xzero[None])[0])
    t0=0.
    initial=chart,q.copy()
    partial.update(seed=tag,initial_regular_chart=chart,initial_regular_coordinates=q.tolist(),tolerance=level)
    state=np.r_[q,np.eye(2).ravel()]
    samples=sorted(set(float(t) for t in np.r_[np.linspace(0,np.pi,p["time_samples"]),p["phases"]]))
    data=[];seams=[];index=0;nfev=0
    partial.update(observations=data,seams=seams,accepted_through=0.,evaluations_entered=0)
    runtime_start=time.monotonic()
    def save(t,y,c):
        ref,f,extra,xzero=field.jets(c,y[:2])
        J=y[2:].reshape(2,2)
        rot=world(t)
        deriv=rot@a.frame@f[1:3].T@J+marker_tan
        pos=rot@(a.frame@f[0]+a.center)+[0.,0.,hmark]
        gram=deriv.T@deriv
        vals=eigvalsh(gram,Gstar)
        material=a.frame@ref[0]+a.center
        material_tan=a.frame@ref[1:3].T@J
        data.append(dict(t=t,chart=c,q=y[:2].tolist(),J=J.tolist(),marked_world=pos.tolist(),
            marked_tangent=deriv.tolist(),reference_world=material.tolist(),
            reference_tangent=material_tan.tolist(),relative_eigenvalues=vals.tolist(),
            error=float(np.max(abs(vals-1.))),chart_det_J=float(np.linalg.det(J))))
    save(0.,state,chart);index=1
    while t0<np.pi:
        def rhs(t,y):
            partial["evaluations_entered"]+=1
            partial["last_rhs_call"]={"t":float(t),"chart":chart,"state":y.tolist()}
            qq=y[:2]
            if chart=="tube" and abs(qq[1])>a.rim+.90*a.width:
                # A Runge-Kutta trial can jump past the overlap. The linear
                # extension lives beyond the stop surface only; no reported
                # trajectory point or derivative is taken from this extension.
                clamped=qq.copy()
                clamped[1]=np.copysign(a.rim+.90*a.width,qq[1])
                X,dX=field.velocity(chart,clamped)
                X=X+dX@(qq-clamped)
            else:
                X,dX=field.velocity(chart,qq)
            return np.r_[-X,(-dX@y[2:].reshape(2,2)).ravel()]
        def event(t,y):
            if chart=="tube":
                return a.rim+a.outer-abs(y[1])
            return a.ray(y[:2])[1]
        event.direction=-1;event.terminal=True
        sol=solve_ivp(rhs,(t0,np.pi),state,method="DOP853",rtol=level["rtol"],atol=level["atol"],
                      max_step=np.pi/level["max_step_divisions"],events=event,dense_output=True)
        nfev+=int(sol.nfev)
        end=float(sol.t[-1]);crossing=sol.status==1
        # Detect an observed exit and re-entry within an accepted step. The
        # near-rim test is evaluated on its true polar curve for any suspect
        # interior dense sample. Restart at the earliest actual event.
        for left,right in zip(sol.t[:-1],sol.t[1:]):
            found=False
            for t in np.linspace(left,right,level["inner_step_probes"]+2)[1:-1]:
                yy=sol.sol(t)
                near=(chart=="tube" or a.approximate_cap_margin(yy[:2])<.02)
                if near and event(t,yy)<0:
                    root=brentq(lambda tt:event(tt,sol.sol(tt)),left,t,xtol=4e-14,rtol=4e-14)
                    if root<end:
                        end=root;crossing=True;found=True
                    break
            if found:break
        while index<len(samples) and samples[index]<=end:
            save(samples[index],sol.sol(samples[index]),chart)
            index+=1
        partial["accepted_through"]=end
        partial["last_accepted_state"]=[chart,sol.sol(end).tolist()]
        if sol.status<0 and not crossing:
            raise ArithmeticError("DOP853 at phase %.17g: %s"%(end,sol.message))
        if not crossing:
            break
        if end<=t0:
            raise ArithmeticError("nonadvancing atlas event at phase %.17g"%end)
        state=sol.sol(end).copy()
        prev=chart
        chart,qq,B,pos_gap,tangent_gap=a.switch(chart,state[:2])
        v1,_=field.velocity(prev,state[:2]);v2,_=field.velocity(chart,qq)
        seams.append(dict(t=end,old=prev,new=chart,reference_position_gap=pos_gap,
                          reference_tangent_gap=tangent_gap,velocity_transition_gap=norm(B@v1-v2)))
        state=np.r_[qq,(B@state[2:].reshape(2,2)).ravel()]
        t0=end
    if len(data)!=len(samples) or data[-1]["t"]!=float(np.pi):
        raise ArithmeticError("finite trajectory did not cover all recorded phases")
    return dict(seed=tag,material_address=seed,initial_regular_chart=initial[0],
                initial_regular_coordinates=initial[1].tolist(),fixed_metric=Gstar.tolist(),
                parent_basis_physical_max_difference=K0,parent_basis_material_max_difference=A0,
                parent_velocity_max_difference=Xcomparison,nfev=nfev,seconds=time.monotonic()-runtime_start,
                seams=seams,observations=data)


def process_point(args):
    geometry,pp,p,r,z,x,rr,zt,tag,seed,out=args
    started=time.monotonic()
    sys.path.insert(0,str(Path(geometry).parent))
    src=importlib.import_module(Path(geometry).stem)
    a=ClosedAtlas(src,r["design"],pp)
    f=Field(a,r,z,x)
    from bent_body_flow_field import Polynomial
    target=Polynomial(rr["configuration"]["shape_degree"],True,pp["scale"],zt)
    outputs=[];errors=[];partials=[]
    for level in p["integrators"]:
        partial={}
        try:
            outputs.append(evaluate(f,target,seed,level,p,tag,partial))
            errors.append(None);partials.append(None)
        except Exception as exc:
            outputs.append(None);partials.append(partial)
            errors.append({"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()})
    detail={"stage":r["stage"],"point_sha256":r["point_sha256"],"seed":tag,"address":seed,
            "levels":outputs,"errors":errors,"partial_failed_levels":partials,"integration_seconds":time.monotonic()-started}
    path=Path(out)/("flow-%02d-%s.json"%(r["stage"],tag))
    parent.dump(path,detail)
    report={"seed":tag,"address":seed,"detail_bytes":path.stat().st_size,"detail_sha256":parent.filehash(path),
            "nfev":[v["nfev"] if v else None for v in outputs],"elapsed":detail["integration_seconds"]}
    if any(errors):
        report["errors"]=[e and [e["type"],e["message"][:320]] for e in errors]
        report["failed_level_observed_through"]=[v and v.get("accepted_through") for v in partials]
    if outputs[1]:
        fine=outputs[1]
        peak=max(fine["observations"],key=lambda row:row["error"])
        report.update(peak_error=peak["error"],peak_t=peak["t"],final_error=fine["observations"][-1]["error"],
                      crossings=len(fine["seams"]),
                      seam_position_max=max([s["reference_position_gap"] for s in fine["seams"]] or [0.]),
                      seam_tangent_max=max([s["reference_tangent_gap"] for s in fine["seams"]] or [0.]),
                      seam_velocity_max=max([s["velocity_transition_gap"] for s in fine["seams"]] or [0.]),
                      parent_basis_max=max(fine["parent_basis_material_max_difference"],
                                           fine["parent_basis_physical_max_difference"],
                                           fine["parent_velocity_max_difference"]))
    if all(outputs):
        discrepancies={k:0. for k in ("reference_world","reference_tangent","marked_world","marked_tangent","relative_eigenvalues")}
        for row1,row2 in zip(*(v["observations"] for v in outputs)):
            if row1["t"]!=row2["t"]:
                raise ValueError("two complete trajectory logs use different sample phases")
            for key in discrepancies:
                discrepancies[key]=max(discrepancies[key],norm(np.asarray(row1[key])-row2[key]))
        report["coarse_fine_max"]=discrepancies
    return report

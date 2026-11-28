#!/usr/bin/env python3
"""Audit the complete R751 published cap scans against their coordinate-invariant physical graph."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import numpy as np
import measure_r751_closed_mixed_atlas as measure
import r751_curvature_mixed_closed_two_jets as m


def matrix(z):
    return np.stack((z[...,0],z[...,1],z[...,1],z[...,2]),axis=-1).reshape(z.shape[:-1]+(2,2))


def working(j):
    g,b=measure.forms(j)
    den=g[...,0]*g[...,2]-g[...,1]**2
    tr=(g[...,2]*b[...,0]-2*g[...,1]*b[...,1]+g[...,0]*b[...,2])/den
    det=b[...,0]*b[...,2]-b[...,1]**2
    return (np.abs(tr)+np.sqrt(np.maximum(0.,tr**2-4*det/den)))/2


def cartesian(j,vr,phase,side):
    x,y,z=np.moveaxis(j,-1,0)
    a=m.J(x[...,0],s=1.)
    b=m.J(z[...,0],a=1.)
    f=m.axial.cap_displacement(a,b,(.75 if side==1 else .50)*np.sin(phase))
    hx,hz,hxx,hxz,hzz=(np.broadcast_to(side*v,x[...,0].shape) for v in f.parts()[1:])
    den=1+hx*hx+hz*hz
    trace=((1+hz*hz)*hxx-2*hx*hz*hxz+(1+hx*hx)*hzz)/den**1.5
    determinant=(hxx*hzz-hxz*hxz)/den**2
    curv=(np.abs(trace)+np.sqrt(np.maximum(0.,trace*trace-4*determinant)))/2
    signedheight=lambda i:hx*x[...,i]+hz*z[...,i]
    first=np.stack([y[...,i]-signedheight(i) for i in (1,2)],axis=-1)
    second=[]
    for i,k,l in ((3,1,1),(4,1,2),(5,2,2)):
        expected=(signedheight(i)+hxx*x[...,k]*x[...,l]+hxz*(x[...,k]*z[...,l]+z[...,k]*x[...,l])
                  +hzz*z[...,k]*z[...,l])
        second.append(y[...,i]-expected)
    second=np.stack(second,axis=-1)
    return curv,first,second


def run():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--report",required=True,type=Path)
    args=cli.parse_args()
    m.old.disk._public()
    rows=[];raw=sha256();nbytes=0
    for count,trans,order in ((48,12,16),(96,24,24),(192,48,32)):
        period,knots,m0,m1,top=m.offsets(order)
        ss=np.unique(np.r_[np.arange(count)*period/count,knots[:-1],
                    top+np.array([-m.BOOST_WIDTH,-m.PLATEAU,-m.PLATEAU/2,0.,m.PLATEAU,m.BOOST_WIDTH])])
        vv=np.unique(np.r_[np.linspace(1/trans,1,trans),1-np.array([0.,m.CAP_STRAIGHT,m.CAP_TURN,m.CAP_TURN+m.FLATTEN])])
        su,v=np.meshgrid(ss,vv,indexing="ij")
        for ph in [0.,.4,.8,.9,1.,1.2,np.pi/2]:
            for side,chart in ((1,"cap+"),(-1,"cap-")):
                j=m.chart_jet(chart,su,v,ph,order,rotate=False)
                world=m.chart_jet(chart,su,v,ph,order,rotate=True)
                wc=working(world)
                cc,first,second=cartesian(j,v,ph,side)
                flat=(1-v)>=m.CAP_TURN-5e-16
                winner=np.unravel_index(np.argmax(wc),wc.shape)
                flat_winner=np.unravel_index(np.argmax(np.where(flat,wc,-np.inf)),wc.shape)
                witnesses=[]
                for name,k in (("complete_published_max",winner),("planar_cap_working_max",flat_winner)):
                    if name=="planar_cap_working_max" and k==winner:
                        witnesses[0]["also_planar_working_max"]=True
                        continue
                    tang=world[k][1:3].T
                    normal=np.cross(tang[:,0],tang[:,1]);normal/=np.linalg.norm(normal)
                    _,sing,vt=np.linalg.svd(tang,full_matrices=False)
                    ii=np.array([[normal@world[k][3],normal@world[k][4]],
                                 [normal@world[k][4],normal@world[k][5]]])
                    qr=vt@ii@vt.T/(sing[:,None]*sing[None,:])
                    hp=m.axial.cap_displacement(m.J(j[k][0,0],s=1.),m.J(j[k][0,2],a=1.),
                        (.75 if side==1 else .50)*np.sin(ph))
                    graph_n=np.array([-hp.s,side,-hp.a]);graph_n/=np.linalg.norm(graph_n)
                    cos,si=np.cos(ph),np.sin(ph)
                    graph_world=[cos*graph_n[0]-si*graph_n[2],graph_n[1],si*graph_n[0]+cos*graph_n[2]]
                    witnesses.append({"kind":name,"s":float(su[k]),"v":float(v[k]),
                         "world_physical_two_jet":world[k].tolist(),
                         "gram_condition":float((sing[0]/sing[1])**2),"area":float(np.prod(sing)),
                         "cross_world_normal":normal.tolist(),"graph_world_normal":graph_world if flat[k] else None,
                         "cartesian_graph_gradient_hessian":[float(side*n) for n in hp.parts()[1:]] if flat[k] else None,
                         "pre_rotation_position":j[k][0].tolist(),"working_abs":float(wc[k]),
                         "tangent_singular_values":sing.tolist(),"svd_principal":np.linalg.eigvalsh(qr).tolist(),
                         "on_flat_graph":bool(flat[k]),"cartesian_abs":float(cc[k]) if flat[k] else None,
                         "graph_chain_first":first[k].tolist() if flat[k] else None,
                         "graph_chain_second":second[k].tolist() if flat[k] else None})
                for x in (wc,cc,first,second):
                    data=np.asarray(x,dtype="<f8").tobytes()
                    raw.update(data);nbytes+=len(data)
                rows.append({"level":[count,trans,order],"phase":float(ph),"side":side,"points":int(v.size),
                    "flat_points":int(np.count_nonzero(flat)),"working_max":float(np.max(wc)),
                    "flat_cartesian_abs_max":float(np.max(cc[flat])),
                    "flat_first_chain_max":float(np.max(np.abs(first[flat]))),
                    "flat_second_chain_max":float(np.max(np.abs(second[flat]))),
                    "witnesses":witnesses})
    repo="Rogerhu12/math-research-public"
    result={"schema":"R751-full-original-cap-coordinate-forensics-v1","run":os.environ["GITHUB_RUN_ID"],
            "attempt":os.environ["GITHUB_RUN_ATTEMPT"],"repository":repo,"trigger_commit":os.environ["GITHUB_SHA"],
            "source_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
            "rules_read_commit":os.environ["R751_RULES_COMMIT"],"original_run":"46150384106",
            "all_three_original_levels_both_complete_caps":rows,
            "raw_derived_identity":{"bytes":nbytes,"sha256":raw.hexdigest(),"uploaded":False}}
    b=(json.dumps(result,sort_keys=True,separators=(",",":"))+"\n").encode()
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_bytes(b)
    print("complete R751 cap comparison",len(b),flush=True)


if __name__=="__main__":
    run()

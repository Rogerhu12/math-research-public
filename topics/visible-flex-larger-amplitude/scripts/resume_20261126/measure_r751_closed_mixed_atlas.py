#!/usr/bin/env python3
"""Complete R751 prescribed phase/grid comparisons and actual narrow all-roll subarc."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import numpy as np
import r751_curvature_mixed_closed_two_jets as m


def forms(j):
    x,fu,fv,fuu,fuv,fvv=np.moveaxis(j,-2,0)
    cross=np.cross(fu,fv)
    area=np.linalg.norm(cross,axis=-1)
    n=cross/np.maximum(area,1e-300)[...,None]
    dot=lambda a,b:np.einsum("...i,...i->...",a,b)
    g=np.stack((dot(fu,fu),dot(fu,fv),dot(fv,fv)),axis=-1)
    b=np.stack((dot(n,fuu),dot(n,fuv),dot(n,fvv)),axis=-1)
    return g,b


def measure(sample,base):
    g,b=forms(sample)
    g0,_=forms(base)
    det=lambda a:a[...,0]*a[...,2]-a[...,1]**2
    d0,d=det(g0),det(g)
    valid=(d0>0)&(d>0)&np.isfinite(d)&np.isfinite(d0)
    if not np.any(valid):
        return {"points":int(d.size),"invalid":int(d.size),"relative_metric_max":None,"abs_principal_max":None}
    g0,g,b,d0,d=(x[valid] for x in (g0,g,b,d0,d))
    change=g-g0
    def op(z,mat,den):
        tr=(mat[...,2]*z[...,0]-2*mat[...,1]*z[...,1]+mat[...,0]*z[...,2])/den
        disc=np.maximum(0.,tr*tr-4*det(z)/den)
        return (np.abs(tr)+np.sqrt(disc))/2
    return {"points":int(valid.size),"invalid":int(np.count_nonzero(~valid)),
            "relative_metric_max":float(np.max(op(change,g0,d0))),
            "abs_principal_max":float(np.max(op(b,g,d)))}


def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--report",type=Path,required=True)
    cli.add_argument("--raw",type=Path,required=True)
    a=cli.parse_args()
    m.old.disk._public()
    phases=[0.,.4,.8,.9,1.,1.2,np.pi/2]
    levels=[(48,12,16),(96,24,24),(192,48,32)]
    all_rows=[]
    raw_sha=sha256()
    raw_bytes=0
    def hash_j(data,out):
        nonlocal raw_bytes
        blob=np.asarray(data,dtype="<f8").tobytes()
        raw_sha.update(blob)
        raw_bytes+=len(blob)
        out.write(blob)
    a.raw.parent.mkdir(parents=True,exist_ok=True)
    with a.raw.open("wb") as out:
        for count,trans,order in levels:
            period,knots,m0,m1,top=m.offsets(order)
            s=np.unique(np.r_[np.arange(count)*period/count,knots[:-1],
                              top+np.array([-m.BOOST_WIDTH,-m.PLATEAU,-m.PLATEAU/2,0.,m.PLATEAU,m.BOOST_WIDTH])])
            for ph in phases:
                rows={}
                for chart,sv,vv in (
                    ("cylinder",s,np.linspace(-1,1,trans+1)),
                    ("end+",s,np.linspace(0,m.old.END_LENGTH,trans+1)),
                    ("end-",s,np.linspace(0,m.old.END_LENGTH,trans+1)),
                    ("cap+",s,np.unique(np.r_[np.linspace(1/trans,1,trans),1-np.array([0.,m.CAP_STRAIGHT,m.CAP_TURN,m.CAP_TURN+m.FLATTEN])])),
                    ("cap-",s,np.unique(np.r_[np.linspace(1/trans,1,trans),1-np.array([0.,m.CAP_STRAIGHT,m.CAP_TURN,m.CAP_TURN+m.FLATTEN])])),
                    ("cap-normal+",s,np.linspace(0,m.CAP_TURN,trans+1)),
                    ("cap-normal-",s,np.linspace(0,m.CAP_TURN,trans+1)),
                    ("cap-cartesian+",np.asarray([m.old.CENTER_X]),np.asarray([0.])),
                    ("cap-cartesian-",np.asarray([m.old.CENTER_X]),np.asarray([0.]))):
                    su,ve=np.meshgrid(sv,vv,indexing="ij")
                    j=m.chart_jet(chart,su,ve,ph,order)
                    j0=m.chart_jet(chart,su,ve,0.,order)
                    hash_j(j,out)
                    rows[chart]=measure(j,j0)
                exact={}
                for side in ("+","-"):
                    for chart,terminal in (("end"+side,m.old.END_LENGTH),("cap-normal"+side,m.CAP_STRAIGHT)):
                        su,ve=np.meshgrid(np.linspace(top-m.PLATEAU,top,17),
                                          np.linspace(0,terminal,trans+1),indexing="ij")
                        j=m.chart_jet(chart,su,ve,ph,order)
                        j0=m.chart_jet(chart,su,ve,0.,order)
                        hash_j(j,out)
                        exact[chart]=measure(j,j0)
                s_top=m0+1.
                s_bot=period-(m0+1.-.65)
                p=m.chart_jet("cylinder",s_top,1.,ph,order)[0]
                q=m.chart_jet("cylinder",s_bot,1.,ph,order)[0]
                _,db=m.old.end_limits(order)
                height=2*(m.old.END_LENGTH+m.old.HEIGHT-db)
                dist_bound=float(np.hypot(.65,height))
                all_rows.append({"grid":[count,trans],"quadrature_order":order,"phase":float(ph),
                                 "charts":rows,"selected_fixed_material_subarc":exact,
                                 "closure_angle_knobs":m.settings(float(ph),order)[-1].tolist(),
                                 "diagonal_projected_end_distance":float(np.linalg.norm(p-q)),
                                 "initial_intrinsic_diagonal_upper":dist_bound})
    source=Path(__file__).read_bytes()
    generated=Path(m.__file__).read_bytes()
    rep={"schema":"R751-actual-full-closed-atlas-and-selected-exact-material-roll-v1",
         "run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
         "trigger_commit":os.environ["GITHUB_SHA"],"rules_read_commit":os.environ["R751_RULES_COMMIT"],
         "source_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
         "sources":{Path(__file__).name:[len(source),sha256(source).hexdigest()],
                    Path(m.__file__).name:[len(generated),sha256(generated).hexdigest()]},
         "rows":all_rows,"whole_raw":{"bytes":raw_bytes,"sha256":raw_sha.hexdigest(),"uploaded":False},
         "scope":"All prescribed phases, three grids and all nine closed atlas charts. Finite working values. Late-phase exact subarc is the true final .00015 right turn, reaching both actual caps through .0001 of inward original material."}
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(json.dumps(rep,sort_keys=True,separators=(",",":"))+"\n")
    print("R751 finished all levels",a.report.stat().st_size,flush=True)


if __name__=="__main__":
    main()

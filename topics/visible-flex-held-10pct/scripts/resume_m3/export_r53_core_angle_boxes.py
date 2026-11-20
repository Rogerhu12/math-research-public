#!/usr/bin/env python3
"""Export true R53 jets on new angle nodes and complete closed angle boxes.

Existing certificates and the 1168 mean-node cache are not changed or rerun.
This exports only the newly requested external angle grid. All interval
mathematical objects are identical to the validated true-core definition.
"""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import argparse,bisect,hashlib,importlib.util,json,sys,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
import mpmath as mp

def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s)
    sys.modules[name]=m;s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("source-run","physical","mean-kernel","interval-kernel","out","interval-output"):
        p.add_argument("--"+k,type=Path,required=True)
    p.add_argument("--support-dir",type=Path,default=Path(__file__).parent)
    p.add_argument("--nodes",type=int,default=2336)
    a=p.parse_args();start=time.monotonic()
    ad=module("_r53_export_model",a.support_dir/"actual_m3_metric_model.py")
    ld=module("_r53_export_physical",a.support_dir/"audit_full_relative_metric.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=ld.load_physical(a.physical)
    o.initial(z.p);f=o.flow(z.p[0]);core=f.exact_lift_core
    source=Path(__file__).with_name("r53_validated_material_core.py")
    oracle=module("_r53_export_oracle",source)
    progress=lambda x:print(json.dumps(x),flush=True)
    v=oracle.ValidatedMaterialCore(core,a.mean_kernel,a.interval_kernel,progress=progress)
    I=v.I;N=a.nodes;warp=I(f.warp_e)
    assert 0<=float(f.warp_e)<1
    psi=2*np.pi*np.arange(N)/N
    upper_period=float(v.from_mp(2*mp.iv.pi).x[1])
    psi_lo=psi.copy();psi_hi=np.r_[psi[1:],upper_period]
    assert np.all(psi_hi>psi_lo)
    # Exact dyadic cuts at both ends of every rigorous boundary enclosure.
    # Their central microscopic interval remains explicitly covered.
    cuts=[]
    for sector in range(-1,5):
        for boundary in v.pg:
            b=boundary+sector*v.T
            cuts.extend([float(b.x[0]),float(b.x[1])])
    cuts=sorted(set(cuts))
    fields=("F","Ft","Ftt","Fttt")
    point={k:np.empty((2,N,3)) for k in fields}
    boxes={k:np.empty((2,N,3)) for k in fields}
    theta_points=np.empty((2,N));theta_boxes=np.empty((2,N))
    max_parts=0;total_parts=0
    def theta_at(p):
        if float(p)==0:return I(0)
        x=I(float(p));s,_=v.sincos(3*x)
        return x-warp*s/3
    def jet_hull(theta):
        nonlocal max_parts,total_parts
        lo,hi=map(float,theta.x)
        inside=cuts[bisect.bisect_right(cuts,lo):bisect.bisect_left(cuts,hi)]
        grid=[lo]+inside+[hi]
        if lo==hi:grid=[lo,hi]
        vals=None;parts=0
        for left,right in zip(grid[:-1],grid[1:]):
            if right<left:raise ArithmeticError("reversed material interval")
            g=v.point(I(left,right));parts+=1
            if vals is None:vals={k:list(g[k]) for k in fields}
            else:
                vals={k:[v.hull(old,new) for old,new in zip(vals[k],g[k])] for k in fields}
        max_parts=max(max_parts,parts);total_parts+=parts
        return vals
    for j,(pl,pr) in enumerate(zip(psi_lo,psi_hi)):
        tl,tr=theta_at(pl),theta_at(pr)
        # theta_psi=1-warp*cos(3psi)>0, so endpoint evaluations enclose
        # the entire material image more tightly than a dependent interval formula.
        tb=I(float(tl.x[0]),float(tr.x[1]))
        theta_points[:,j]=[float(tl.x[0]),float(tl.x[1])]
        theta_boxes[:,j]=[float(tb.x[0]),float(tb.x[1])]
        gp=jet_hull(tl);gb=jet_hull(tb)
        for k in fields:
            for c in range(3):
                point[k][:,j,c]=[float(gp[k][c].x[0]),float(gp[k][c].x[1])]
                boxes[k][:,j,c]=[float(gb[k][c].x[0]),float(gb[k][c].x[1])]
        if (j+1)%128==0:
            progress({"stage":"new_external_angles","nodes_done":j+1,"nodes":N,
                      "material_parts":total_parts,"maximum_parts_per_query":max_parts,
                      "seconds":time.monotonic()-start})
    bindings={
        "source_run_sha256":sha(a.source_run),"physical_sha256":sha(a.physical),
        "oracle_source_sha256":sha(source),"exporter_source_sha256":sha(__file__),
        "mean_kernel_sha256":sha(a.mean_kernel),"interval_kernel_sha256":sha(a.interval_kernel),
        "nodes":N,"warp_e_exact":str(Q.from_float(float(f.warp_e))),
        "core_coefficients_exact":[str(x) for x in v.a],
        "lambda_exact":str(v.lam),"S_exact":str(v.S),"b_exact":str(v.width),"k_exact":str(v.k),
        "input_angles":"Literal original binary64 2*np.pi*np.arange(N)/N; true-sin map theta=psi-warp_e*sin(3psi)/3",
        "last_box":"Conservative binary upper endpoint strictly enclosing the true 2pi; the extra microscopic periodic interval is also covered",
        "endpoint_periodicity":"True R53 core is exactly 2pi-periodic; the point at true 2pi equals point zero",
        "jet_coordinates":"Cartesian F,Ft,Ftt,Fttt; derivatives are with respect to material theta",
        "array_axes":"Each jet array has shape (2,N,3), axis 0 is lower/upper",
        "box_definition":"box_k[:,j,:] encloses the true jet for every psi in [psi_lo[j],psi_hi[j]]",
        "splitting":"Both endpoints of every sector/window/integration-knot interval enclosure are inserted as exact dyadic cuts; all subboxes are covered and hulled",
        "mean_rule_changed":False,"old_1168_certificate_rerun":False}
    a.interval_output.parent.mkdir(parents=True,exist_ok=True)
    np.savez(a.interval_output,psi=psi,psi_lo=psi_lo,psi_hi=psi_hi,
        theta_point=theta_points,theta_box=theta_boxes,
        **{"point_"+k:x for k,x in point.items()},
        **{"box_"+k:x for k,x in boxes.items()},
        bindings_json=np.array(json.dumps(bindings)))
    report={"status":"new_external_angle_nodes_and_closed_boxes_certified",**bindings,
        "material_parts":total_parts,"maximum_parts_per_query":max_parts,
        "interval_output_sha256":sha(a.interval_output),"seconds":time.monotonic()-start,
        "point_width_maxima":{k:float(np.max(v.K.up(x[1]-x[0]))) for k,x in point.items()},
        "box_width_maxima":{k:float(np.max(v.K.up(x[1]-x[0]))) for k,x in boxes.items()},
        "scope":"Strict true-core node/box input, not a full prefix metric or closed-surface certificate"}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("status","nodes","material_parts","seconds","point_width_maxima","box_width_maxima","interval_output_sha256")}),flush=True)
if __name__=="__main__":main()

#!/usr/bin/env python3
"""Local C2 cylinder repair of the actual true-core M24 prefix.

Defines Fnew(s,theta)=F(s,theta)-sum_j A_j(s) Delta_j(theta), where Delta_j
are the true material inlet discrepancies from Gamma(theta)+s e_z.  The
quintic A_j have the identity inlet two-jet and zero outer two-jet.  The
original field, chart, profile, mean rule, and material g remain unchanged
outside [0,L].  Only this local interval is re-certified.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import numpy as np

H=[[Q(1),Q(0),Q(0),-Q(10),Q(15),-Q(6)],
   [Q(0),Q(1),Q(0),-Q(6),Q(8),-Q(3)],
   [Q(0),Q(0),Q(1,2),-Q(3,2),Q(3,2),-Q(1,2)]]

def module(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    z=importlib.util.module_from_spec(sp);sys.modules[name]=z;sp.loader.exec_module(z);return z
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))
def der(c):return [(i+1)*c[i+1] for i in range(len(c)-1)]
def value(c,x):
    v=Q(0)
    for a in c[::-1]:v=v*x+a
    return v
def bernstein_range(c,left,right):
    n=len(c)-1
    p=[sum((c[k]*comb(k,j)*left**(k-j)*(right-left)**j
            for k in range(j,n+1)),Q(0)) for j in range(n+1)]
    b=[sum((p[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)),Q(0))
       for i in range(n+1)]
    return min(b),max(b)
def coefficient_bounds(left,right,L):
    out=[]
    for j,p in enumerate(H):
        row=[];c=p
        for k in range(3):
            lo,hi=bernstein_range(c,left/L,right/L)
            row.append(max(abs(lo),abs(hi))*L**(j-k));c=der(c)
        out.append(row)
    return out

def apply_material_patch(base,inlet,s,length):
    """Reusable finite evaluator of the declared correction.

    `base` contains F,Fs,Ftheta,Fss,Fstheta,Fthetatheta in fixed material theta.
    `inlet[j][k]` is dtheta^k Delta_j at those same material angles; it must
    come from that complete original graph, including its fixed mean.
    This evaluator is not itself an outward interval oracle.
    """
    s,L=float(s),float(length)
    if s<0 or s>L: return dict(base)
    weights=[]
    for j,p in enumerate(H):
        row=[];c=p
        for k in range(3):
            row.append(float(value(c,Q.from_float(s/L)))*L**(j-k));c=der(c)
        weights.append(row)
    out=dict(base)
    for name,ds,dt in (("F",0,0),("Fs",1,0),("Ftheta",0,1),
                       ("Fss",2,0),("Fstheta",1,1),("Fthetatheta",0,2)):
        out[name]=np.asarray(base[name])-sum(weights[j][ds]*np.asarray(inlet[j][dt]) for j in range(3))
    return out

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ("source-run","physical","core-mean-intervals","core-mean-certificate",
                 "core-angle-intervals","core-angle-certificate","inlet-certificate",
                 "position-certificate","interval-kernel","support-dir","out"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--length",default="1/1000")
    ap.add_argument("--max-cells",type=int,default=20000)
    a=ap.parse_args();start=time.monotonic();L=Q(a.length)
    sys.path.insert(0,str(a.support_dir.resolve()))
    v=module("_local_cylinder_patch_metric",a.support_dir/"certify_prefix_metric_interval_taylor.py")
    v.m.K=v.m.module("_local_cylinder_patch_interval",a.interval_kernel)
    I,D=v.I,v.D
    ad=v.m.module("_local_cylinder_patch_model",a.support_dir/"actual_m3_metric_model.py")
    ld=v.m.module("_local_cylinder_patch_field",a.support_dir/"audit_full_relative_metric.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=ld.load_physical(a.physical)
    pieces=v.PrefixPieces(o,z);rh,ph=sha(a.source_run),sha(a.physical)
    ic=json.loads(a.inlet_certificate.read_text());pc=json.loads(a.position_certificate.read_text())
    assert ic["status"]=="true_material_inlet_jets_certified"
    assert pc["status"]=="continuous_prefix_position_and_support_certified"
    for rec in (ic,pc):
        assert rec["source_run_sha256"]==rh and rec["physical_sha256"]==ph
        assert rec["core_angle_intervals_sha256"]==sha(a.core_angle_intervals)
    for cert,arrays in ((a.core_mean_certificate,a.core_mean_intervals),
                        (a.core_angle_certificate,a.core_angle_intervals)):
        v.binding(json.loads(cert.read_text()),rh,ph,arrays)
    assert ic["metric_source_sha256"]==sha(a.support_dir/"certify_prefix_metric_interval_taylor.py")
    assert 0<L<pieces.profile_pieces[0]["right"]
    first=pieces.profile_pieces[0]
    alo,_=bernstein_range(first["coefficients_exact"],Q(0),L/first["length"])
    assert alo>=1
    for j,p in enumerate(H):
        c=p
        for k in range(3):
            assert value(c,Q(0))==(1 if k==j else 0)
            assert value(c,Q(1))==0
            c=der(c)
    with np.load(a.core_mean_intervals) as data:
        mt=v.AngleTable(data["psi"],data["psi"],pieces.f.even);mt.load_mean_lift(data)
    with np.load(a.core_angle_intervals) as data:
        pt=v.AngleTable(data["psi"],data["psi"],pieces.f.even)
        bt=v.AngleTable(data["psi_lo"],data["psi_hi"],pieces.f.even)
        pt.build_lift(data,pieces.f,"point",pieces.q)
        bt.build_lift(data,pieces.f,"box",pieces.q)
        step=float(np.max((I(bt.hi)-I(bt.lo)).x[1]))
    obj=v.PrefixMetric(pieces,mt,pt,bt,step)
    delta=[[I(t) for t in ic["Delta%d_material_derivatives_0_1_2_upper"%j]] for j in range(3)]
    old_radius=I(pc["radius_upper"]);old_support=I(pc["support_lower"])
    report={"status":"running","source_sha256":sha(__file__),
        "source_run_sha256":rh,"physical_sha256":ph,
        "inlet_certificate_sha256":sha(a.inlet_certificate),
        "position_certificate_sha256":sha(a.position_certificate),
        "core_angle_intervals_sha256":sha(a.core_angle_intervals),
        "metric_source_sha256":sha(a.support_dir/"certify_prefix_metric_interval_taylor.py"),
        "new_map_explicit":True,"patch_length_exact":str(L),"same_material_metric":True,
        "fixed_mean_nodes":mt.N,"angular_nodes":pt.N,
        "profile_lower_exact":str(alo),"accepted":0,"attempted":0,"splits":0,
        "metric_upper":0.,"local_old_metric_upper":0.,"principal_curvature_upper":0.,
        "position_change_upper":0.,"normalized_first_jet_change_upper":0.,
        "radius_upper":0.,"support_lower":None,"normal_difference_upper":0.,
        "whole_closed_surface":False,"old_graph_unchanged_for_s_at_least_L":True}
    def save():
        report["seconds"]=time.monotonic()-start
        a.out.parent.mkdir(parents=True,exist_ok=True)
        a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    def cert(left,right):
        eold,_=obj.enclose(left,right)
        wd,wm,au,av,velocity,rho=obj.last_context
        aa=wd[2].v
        A=[[I.rational(x) for x in row] for row in coefficient_bounds(left,right,L)]
        P=sum((A[j][0]*delta[j][0] for j in range(3)),I(0))
        B0=sum((A[j][1]*delta[j][0] for j in range(3)),I(0))
        B1=sum((A[j][0]*delta[j][1] for j in range(3)),I(0))/I.rational(alo)
        d=(B0.sq()+B1.sq()).sqrt()
        enew=I(eold)+2*(1+I(eold)).sqrt()*d+d.sq()
        if float(enew.x[1])>=1e-6:
            return False,{"reason":"local repaired metric exceeds target","metric":float(enew.x[1])}
        sec=[sum((A[j][2]*delta[j][0] for j in range(3)),I(0)),
             sum((A[j][1]*delta[j][1] for j in range(3)),I(0))/I.rational(alo),
             sum((A[j][0]*delta[j][2] for j in range(3)),I(0))/I.rational(alo).sq()]
        sym=lambda x:I(-float(x.x[1]),float(x.x[1]))
        u=[x.v+sym(B0) for x in au];w=[x.v+sym(B1) for x in av]
        cr=[u[1]*w[2]-u[2]*w[1],u[2]*w[0]-u[0]*w[2],u[0]*w[1]-u[1]*w[0]]
        ln=sum((x.sq() for x in cr),I(0)).sqrt()
        assert np.min(ln.x[0])>0
        n=[-x/ln for x in cr]
        _,ru,_,_,_=obj.metric(bt,wd,wm,"radial",True)
        h11=sum((n[k]*(ru[k].d-velocity.v*au[k].d+sym(sec[0])) for k in range(3)),I(0))
        h12=sum((n[k]*(au[k].d/(aa*rho.v)+sym(sec[1])) for k in range(3)),I(0))
        h22=sum((n[k]*(av[k].d/(aa*rho.v)+sym(sec[2])) for k in range(3)),I(0))
        curvature=I(float(np.max(v.op_upper([h11,h12,h22]))))/(1-enew)
        # Same orientation: tangent-column perturbation divided by the old
        # least singular value bounds sin(angle); sqrt(2)*eta bounds normals.
        eta=d/(1-I(eold)).sqrt();assert float(eta.x[1])<1
        dn=I(2).sqrt()*eta
        radius=old_radius+P;support=old_support-old_radius*dn-P
        stats={"metric":float(enew.x[1]),"old_metric":eold,"curvature":float(curvature.x[1]),
            "position_change":float(P.x[1]),"first_change":float(d.x[1]),
            "radius":float(radius.x[1]),"support":float(support.x[0]),
            "normal_difference":float(dn.x[1])}
        ok=(fq(stats["curvature"])<Q(123,10) and fq(stats["radius"])<Q(67,50)
            and fq(stats["support"])>Q(87,1000))
        if not ok:stats["reason"]="local geometry window unresolved"
        return ok,stats
    grid=sorted(set([Q(0),L]+[x for x in pieces.grid if 0<x<L]))
    todo=[(l,r,0) for l,r in zip(grid[:-1],grid[1:])][::-1]
    while todo:
        l,r,depth=todo.pop();report["attempted"]+=1
        try:good,stats=cert(l,r)
        except (ValueError,ArithmeticError,FloatingPointError) as exc:
            good=False;stats={"reason":str(exc)}
        if not good:
            if depth>=22 or report["accepted"]+len(todo)>=a.max_cells:
                report.update(status="local_cylinder_patch_not_certified",unresolved_s=[float(l),float(r)],
                    unresolved=stats,remaining=len(todo)+1);save();print(json.dumps(report),flush=True);return
            mid=(l+r)/2;todo.extend([(mid,r,depth+1),(l,mid,depth+1)]);report["splits"]+=1
        else:
            report["accepted"]+=1
            for output,key in (("metric_upper","metric"),("local_old_metric_upper","old_metric"),
                    ("principal_curvature_upper","curvature"),("position_change_upper","position_change"),
                    ("normalized_first_jet_change_upper","first_change"),("radius_upper","radius"),
                    ("normal_difference_upper","normal_difference")):
                report[output]=max(report[output],stats[key])
            report["support_lower"]=stats["support"] if report["support_lower"] is None else min(report["support_lower"],stats["support"])
        if report["attempted"]%10==0:
            save();print(json.dumps({k:report[k] for k in ("status","accepted","attempted","splits","metric_upper","principal_curvature_upper")}),flush=True)
    report.update(status="exact_C2_cylinder_patch_continuously_certified",
        cylinder_seam_exact=True,outer_two_jet_correction_exactly_zero=True,
        scope=["New explicitly defined map only on [0,L]; original source/field unchanged",
            "Exact true-core cylinder inlet in the unchanged material coordinate and g",
            "Local old metric re-evaluated and actual correction paid; no whole-prefix error was substituted",
            "This approximate patch does not prove an exact isometric solution or refinement convergence"])
    save();print(json.dumps(report),flush=True)
if __name__=="__main__":main()

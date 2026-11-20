#!/usr/bin/env python3
"""Actual material 0/1/2-jet mismatch of the declared C2 M24 inlet.

No boundary identity is inferred from the exact-lift label.  The cylinder is
Gamma(theta)+s e_z in the unchanged material metric ds^2+a(s)^2 dtheta^2.
All input coefficients are exact binary rationals; the true core uses the
already-computed interval files.  Only the previously unpaid inlet is tested.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse,hashlib,importlib.util,json,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod
    spec.loader.exec_module(mod);return mod
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("source-run","physical","core-mean-intervals","core-mean-certificate",
                 "core-angle-intervals","core-angle-certificate","interval-kernel",
                 "support-dir","out"):
        p.add_argument("--"+name,type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    sys.path.insert(0,str(a.support_dir.resolve()))
    v=module("_cylinder_inlet_metric",a.support_dir/"certify_prefix_metric_interval_taylor.py")
    v.m.K=v.m.module("_cylinder_inlet_interval",a.interval_kernel)
    I,D=v.I,v.D
    ad=v.m.module("_cylinder_inlet_model",a.support_dir/"actual_m3_metric_model.py")
    ld=v.m.module("_cylinder_inlet_physical",a.support_dir/"audit_full_relative_metric.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=ld.load_physical(a.physical)
    pieces=v.PrefixPieces(o,z);rh,ph=sha(a.source_run),sha(a.physical)
    for cert,arrays in ((a.core_mean_certificate,a.core_mean_intervals),
                        (a.core_angle_certificate,a.core_angle_intervals)):
        v.binding(json.loads(cert.read_text()),rh,ph,arrays)
    with np.load(a.core_mean_intervals) as data:
        mt=v.AngleTable(data["psi"],data["psi"],pieces.f.even);mt.load_mean_lift(data)
    assert mt.N==1168
    with np.load(a.core_angle_intervals) as data:
        pt=v.AngleTable(data["psi"],data["psi"],pieces.f.even)
        bt=v.AngleTable(data["psi_lo"],data["psi_hi"],pieces.f.even)
        pt.build_lift(data,pieces.f,"point",pieces.q)
        bt.build_lift(data,pieces.f,"box",pieces.q)
        if not np.array_equal(bt.hi[:-1],bt.lo[1:]) or bt.lo[0]!=0:
            raise ValueError("Uncovered angular interval")
        assert np.array_equal(pt.lo,bt.lo)
        v.mp.iv.dps=70
        assert bt.hi[-1]>=v.m.K.up(float((2*v.mp.iv.pi).b))
        step=float(np.max((I(bt.hi)-I(bt.lo)).x[1]))
    obj=v.PrefixMetric(pieces,mt,pt,bt,step)
    zero=obj.data(Q(0),Q(0),"radial")
    mean,root=obj.mean(zero)
    # Exact endpoint identities required by the trace formulas, checked as
    # rational polynomial identities (not inferred from interval closeness).
    prof=pieces.profile_pieces[0]["coefficients_exact"]
    assert prof[0]==1 and prof[1]==prof[2]==0
    ec=pieces.chart_coefficients_exact[0]
    assert ec[1]==0 and pieces.lift_lo>0
    e0,epp=ec[0],2*ec[2];warp=fq(pieces.f.warp_e)
    y=pieces.field_coefficients_exact[0]
    initial=[fq(t) for t in pieces.f.exact_lift_initial]
    trace=[[r[0]-t for r,t in zip(y,initial)],
           [r[1] for r in y],[2*r[2] for r in y]]
    M=pieces.M;q=pieces.q_exact;freq=list(map(int,pieces.frequencies))
    def fourier_l1(vals,order):
        # Cartesian rotating radial/tangential frequencies are m+/-1.
        total=abs(vals[0])
        for j,k in enumerate(freq):
            total+=(k+1)**order*(abs(vals[1+j])+abs(vals[M+1+j]))
            total+=k**order*abs(vals[2*M+1+j])
        return q*total
    rho=1-abs(e0);rp=3*abs(e0)
    assert rho>Q(1,2)
    def material_l1(vals):
        s=[fourier_l1(vals,j) for j in range(3)]
        return [s[0],s[1]/rho,s[2]/rho**2+rp*s[1]/rho**3]
    # True-core globally certified ||Gamma'||=1, ||Gamma''||<2,
    # ||Gamma'''||<5.3.  J=Gamma-circle thus has (2,3,6.3) bounds.
    core_record=json.loads(a.core_mean_certificate.read_text())
    # Source record schema is intentionally not used as a guessed key: the
    # bound is tied to its whole hash, and compared to its actual named field.
    bounds=core_record["continuous_all_angle_bounds"]
    assert fq(bounds["kappa"])<2 and fq(bounds["Gamma3"])<Q(53,10)
    de=abs(e0-warp)
    d0,d1,d2=de/3,de/rho,3*de/rho**3
    shift=[2*d0,3*d0+2*d1,Q(63,10)*d0+3*(2*d1+d1*d1)+2*d2]
    delta0=[a+b for a,b in zip(material_l1(trace[0]),shift)]
    delta1=[I.rational(x) for x in material_l1(trace[1])]
    mean0=mean.v-1
    mean0max=max(abs(float(mean0.x[0])),abs(float(mean0.x[1])))
    delta1[0]=delta1[0]+I(mean0max)
    def lift_trace(tab):
        yy=v.constant(zero[0].v)
        yss=v.constant(zero[1].d)
        G=tab.basis(yy,"radial",3)
        GG=tab.basis(yss,"radial",2)
        H=[tab.lift(j,"radial") for j in range(1,4)]
        pp=[[G[j+1][k].v+H[j][k].v for k in range(3)] for j in range(3)]
        sn,co=tab.sn3,tab.co3
        ee,ep2=I.rational(e0),I.rational(epp)
        rr=1-ee*co;rrp=3*ee*sn
        vs=-ep2*sn/(3*rr)
        vsp=-ep2*(co-ee)/rr.sq()
        vspp=3*ep2*sn*(1+ee*co-2*ee.sq())/(rr**3)
        vals=[]
        vals.append([GG[0][k].v-vs*pp[0][k]+(mean.d if k==2 else I(0)) for k in range(3)])
        vals.append([GG[1][k].v-vsp*pp[0][k]-vs*pp[1][k] for k in range(3)])
        vals.append([GG[2][k].v-vspp*pp[0][k]-2*vsp*pp[1][k]-vs*pp[2][k] for k in range(3)])
        return vals,rr,rrp
    def maxnorm(vec):
        value=sum((u.sq() for u in vec),I(0))
        # This is a sum of squares: roundoff below zero in its lower endpoint
        # is immaterial and may be intersected with the known [0,infinity).
        value=I(np.maximum(0.,value.x[0]),np.maximum(0.,value.x[1]))
        return float(np.max(value.sqrt().x[1]))
    pts,_,_=lift_trace(pt);boxes,br,brp=lift_trace(bt)
    point0=maxnorm(pts[0]);box2=maxnorm(boxes[2])
    # Linear interpolation of a vector has norm bounded by its endpoints.
    # The Green-function integral remainder is h^2/8 sup||dpsi^2 Delta2||.
    rem=(I(step).sq()/8*box2)
    delta20=I(point0)+rem
    delta21=maxnorm([x/br for x in boxes[1]])
    delta22=maxnorm([boxes[2][k]/br.sq()-brp*boxes[1][k]/(br**3) for k in range(3)])
    def interval(z):return [float(np.min(z.x[0])),float(np.max(z.x[1]))]
    report={"status":"true_material_inlet_jets_certified",
        "source_sha256":sha(__file__),"source_run_sha256":rh,"physical_sha256":ph,
        "core_mean_certificate_sha256":sha(a.core_mean_certificate),
        "core_angle_certificate_sha256":sha(a.core_angle_certificate),
        "core_angle_intervals_sha256":sha(a.core_angle_intervals),
        "metric_source_sha256":sha(a.support_dir/"certify_prefix_metric_interval_taylor.py"),
        "pieces_source_sha256":sha(a.support_dir/"explicit_m24_prefix_pieces.py"),
        "theta_target":"fixed original material theta; cylinder Gamma(theta)+s*ez",
        "angular_boxes":bt.N,"mean_nodes":mt.N,"fixed_mean_root_lower":root,
        "profile_initial_exact":["1","0","0"],"lift_initial_exact":["1","0","0"],
        "e0_exact":str(e0),"e0_minus_warp_exact":str(e0-warp),"ep0_exact":"0","epp0_exact":str(epp),
        "M0_interval":interval(mean.v),"Mprime0_interval":interval(mean.d),
        "qYs0_cartesian_l1_exact":str(fourier_l1(trace[1],0)),
        "qY0_minus_projection_l1_exact":str(fourier_l1(trace[0],0)),
        "qYss0_l1_exact":str(fourier_l1(trace[2],0)),
        "Delta0_material_derivatives_0_1_2_upper":[float(I.rational(x).x[1]) for x in delta0],
        "Delta1_material_derivatives_0_1_2_upper":[float(x.x[1]) for x in delta1],
        "Delta2_material_derivatives_0_1_2_upper":[float(delta20.x[1]),delta21,delta22],
        "Delta2_node_norm_upper":point0,"Delta2_psi2_box_norm_upper":box2,
        "Delta2_interpolation_remainder_upper":float(rem.x[1]),
        "entry_exact_cylinder_identity":False,"patch_created":False,
        "scope":"Trace certificate only; no new map or seam is silently substituted",
        "seconds":time.monotonic()-start}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps(report),flush=True)
if __name__=="__main__":main()

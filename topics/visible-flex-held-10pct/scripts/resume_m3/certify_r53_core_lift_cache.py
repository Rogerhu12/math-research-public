#!/usr/bin/env python3
"""Bind true R53 interval jets to the actual M24 inlet-angle cache.

This is a strict finite-node certificate for the named cached values and
exports a true-core oracle. Continuous all-angle curvature-jet bounds are
also computed; no finite metric or BVP result is promoted to a full theorem.
"""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np

def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s)
    sys.modules[name]=m;s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def scalar(i):return [float(i.x[0]),float(i.x[1])]
def gap_norm(v,literal,K):
    diff=K.sub(K.exact(np.asarray(literal,float)),K.stack([x.x for x in v],0))
    total=K.interval_sum_terms(K.square(diff),0)
    return float(K.sqrt((np.maximum(0,total[0]),total[1]))[1])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("source-run","physical","mean-kernel","interval-kernel","out"):
        p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--support-dir",type=Path,default=Path(__file__).parent)
    p.add_argument("--nodes",type=int,default=1168)
    p.add_argument("--interval-output",type=Path)
    a=p.parse_args();start=time.monotonic()
    ad=module("_r53_cache_model",a.support_dir/"actual_m3_metric_model.py")
    ld=module("_r53_cache_physical",a.support_dir/"audit_full_relative_metric.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=ld.load_physical(a.physical)
    o.initial(z.p);f=o.flow(z.p[0]);core=f.exact_lift_core
    oracle_module=module("_r53_cache_oracle",Path(__file__).with_name("r53_validated_material_core.py"))
    progress=lambda x:print(json.dumps(x),flush=True)
    v=oracle_module.ValidatedMaterialCore(core,a.mean_kernel,a.interval_kernel,progress=progress)
    I,K=v.I,v.K
    global_bounds=v.all_angle_curvature_bounds()
    progress({"stage":"global_curvature","seconds":time.monotonic()-start,"bounds":global_bounds})
    N=a.nodes;ang=f.angular(N);psi=np.asarray(ang[0],float)
    # The live cache is read only and compared to independent interval values.
    f.geo(np.array([0.]),N);cached=f.exact_lift_cache[N]
    initial=np.asarray(f.exact_lift_initial,float);q=I(o.q)
    freq=np.asarray(f.even,int);M=o.M
    maxima={key:0. for key in ("F","Ft","Ftt","Fttt","H","H1","H2")}
    widths={key:0. for key in ("F","Ft","Ftt","Fttt")}
    out={key:np.zeros((2,N,3)) for key in ("F","Ft","Ftt","Fttt","H","H1","H2")}
    gsource=core.evaluate(np.asarray(ang[1],float))
    source_nu=np.exp(1j*gsource["phi"])
    source_third=-(gsource["kappa_u"]+1j*gsource["kappa"]**2)*source_nu
    source_third=np.c_[source_third.real,source_third.imag,np.zeros(N)]
    for j,pj in enumerate(psi):
        pp=I(pj);s3,c3=v.sincos(3*pp);sp,cp=v.sincos(pp)
        if pj==0:s3=I(0);c3=I(1);sp=I(0);cp=I(1)
        theta=pp-I(f.warp_e)*s3/3
        rho=1-I(f.warp_e)*c3;rp=3*I(f.warp_e)*s3
        g=v.point(theta)
        for name in ("F","Ft","Ftt","Fttt"):
            literal=source_third[j] if name=="Fttt" else gsource[name][j]
            maxima[name]=max(maxima[name],gap_norm(g[name],literal,K))
            widths[name]=max(widths[name],max(float(K.up(x.x[1]-x.x[0])) for x in g[name]))
            for k,x in enumerate(g[name]):out[name][:,j,k]=scalar(x)
        # Exact Fourier projection constants are retained; no new projection
        # or zero-mean normalization is substituted.
        cs=[];sn=[]
        for m in freq:
            s,c=v.sincos(int(m)*pp);cs.append(c);sn.append(s)
        R0=q*I(initial[0]);R=[q*I(x) for x in initial[1:M+1]]
        T=[q*I(x) for x in initial[M+1:2*M+1]]
        Z=[q*I(x) for x in initial[2*M+1:]]
        Rv=R0+sum((r*c for r,c in zip(R,cs)),I(0))
        Tv=sum((t*s for t,s in zip(T,sn)),I(0))
        Zv=sum((zz*c for zz,c in zip(Z,cs)),I(0))
        R1=-sum((int(m)*r*s for m,r,s in zip(freq,R,sn)),I(0))
        T1=sum((int(m)*t*c for m,t,c in zip(freq,T,cs)),I(0))
        Z1=-sum((int(m)*zz*s for m,zz,s in zip(freq,Z,sn)),I(0))
        R2=-sum((int(m)**2*r*c for m,r,c in zip(freq,R,cs)),I(0))
        T2=-sum((int(m)**2*t*s for m,t,s in zip(freq,T,sn)),I(0))
        Z2=-sum((int(m)**2*zz*c for m,zz,c in zip(freq,Z,cs)),I(0))
        def cart(r,t,z):return [r*cp-t*sp,r*sp+t*cp,z]
        ini=cart(Rv,Tv,Zv);ini1=cart(R1-Tv,T1+Rv,Z1)
        ini2=cart(R2-2*T1-Rv,T2+2*R1-Tv,Z2)
        st,ct=v.sincos(theta)
        circle=[ct,st,I(0)];circle1=[-rho*st,rho*ct,I(0)]
        circle2=[-rho.sq()*ct-rp*st,-rho.sq()*st+rp*ct,I(0)]
        H=[g["F"][k]-circle[k]-ini[k] for k in range(3)]
        H1=[g["Ft"][k]*rho-circle1[k]-ini1[k] for k in range(3)]
        H2=[g["Ftt"][k]*rho.sq()+g["Ft"][k]*rp-circle2[k]-ini2[k] for k in range(3)]
        for name,vals,cache in (("H",H,cached[0]),("H1",H1,cached[1]),("H2",H2,cached[2])):
            maxima[name]=max(maxima[name],gap_norm(vals,cache[j],K))
            for k,x in enumerate(vals):out[name][:,j,k]=scalar(x)
        if (j+1)%128==0:progress({"stage":"nodes","completed":j+1,"nodes":N,"seconds":time.monotonic()-start,"maxima":maxima})
    result={"status":"true_R53_finite_node_and_continuous_curvature_certificate_completed",
        "source_run_sha256":sha(a.source_run),"physical_sha256":sha(a.physical),
        "source_sha256":sha(__file__),"oracle_source_sha256":sha(Path(__file__).with_name("r53_validated_material_core.py")),
        "mean_kernel_sha256":sha(a.mean_kernel),"interval_kernel_sha256":sha(a.interval_kernel),
        "nodes":N,"mean_node_contract":N==int(__import__("json").loads(a.source_run.read_text())["prefix_audit"]["samples_psi"]),
        "core_coefficients":[str(x) for x in v.a],"lambda":str(v.lam),"S":str(v.S),"b":str(v.width),"k":str(v.k),
        "strip_B_interval":scalar(v.strip_B),"complex_material_radius":str(v.R),
        "complex_inverse_radius":str(v.r),"complex_kappa_bound":str(v.complex_kappa_bound),
        "inverse_Taylor_degree":v.degree,"inverse_cells_per_unit":v.cells_per_unit,
        "inverse_seed_width_max":v.inverse_seed_max_width,"beta_interval":scalar(v.beta),
        "origin_real_interval":scalar(v.origin),"origin_imaginary_check":scalar(v.origin_imag_check),
        "gauss_node_gap_exact":str(v.gauss_node_gap),"gauss_weight_l1_exact":str(v.gauss_weight_l1),
        "continuous_all_angle_bounds":global_bounds,"true_core_interval_width_maxima":widths,
        "cached_value_distance_upper":maxima,"seconds":time.monotonic()-start,
        "scope":["True R53 core uses exact real 2pi/3 and exact frozen binary-rational coefficients and design parameters",
            "The mathematical arc inverse and weighted/position primitives are enclosed independently",
            "Cache comparisons include their actual floating evaluations; no blanket libm accuracy assumption is used",
            "The displayed cache distances are finite-node statements, not a uniform error theorem for the float function",
            "The callable oracle also accepts small angle intervals and returns true Gamma through its fourth material derivative",
            "No full prefix metric, profile endpoint, true-DN or closed-family condition is concluded here"]}
    if a.interval_output:
        a.interval_output.parent.mkdir(parents=True,exist_ok=True)
        np.savez(a.interval_output,psi=psi,**out)
        result["interval_output_sha256"]=sha(a.interval_output)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result),flush=True)
if __name__=="__main__":main()

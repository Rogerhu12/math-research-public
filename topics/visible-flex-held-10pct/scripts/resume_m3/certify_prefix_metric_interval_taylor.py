#!/usr/bin/env python3
"""Continuous metric of the explicitly shared-C2 lifted M24 prefix.

This directly uses the true R53 interval core, the endpoint-normalized profile,
shared Hermite field/chart, and the fixed original 1168-node mean. Radial
second-order Taylor bounds and angular linear-interpolation remainders cover
the entire prefix; no finite sample is promoted to a continuous claim.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[_key]="1"
import argparse,hashlib,json,math,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
import mpmath as mp
import certify_bridge_metric_fourier_taylor as b
from explicit_m24_prefix_pieces import PrefixPieces
I,D=b.I,b.D2
m=b.m


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def raw_interval(value):
    v=np.asarray(value,float)
    if v.shape[0]!=2 or not np.all(np.isfinite(v)) or np.any(v[0]>v[1]):
        raise ValueError("Invalid stored core interval")
    return I(v[0],v[1])


def stack_intervals(values):
    return I(np.stack([v.x[0] for v in values]),np.stack([v.x[1] for v in values]))

def constant(value):
    value=I(value)
    zeros=np.zeros_like(value.x[0])
    return D(value,I(zeros),I(zeros))


def dot(x,y):
    return sum((a*c for a,c in zip(x,y)),D(0))


def cross(x,y):
    return [x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]


def norm(x):
    return sum((a.sq() for a in x),D(0)).sqrt()


def scale(a,x):
    return [a*c for c in x]


def plus(*vectors):
    return [sum((v[k] for v in vectors),D(0)) for k in range(3)]


def op_upper(e):
    x,y,z=e
    trace=x+z
    tr=I(np.maximum(np.abs(trace.x[0]),np.abs(trace.x[1])))
    rad=(x-z).sq()+4*y.sq()
    rad=I(np.maximum(0.,rad.x[0]),rad.x[1]).sqrt()
    value=(tr+rad)/2
    if not value.finite():
        raise ArithmeticError("Nonfinite symmetric operator bound")
    return np.asarray(value.x[1])


class AngleTable:
    """True trigonometry and true-core lift intervals on fixed points or boxes."""
    def __init__(self,psi_lo,psi_hi,frequencies):
        self.lo=np.asarray(psi_lo,float)
        self.hi=np.asarray(psi_hi,float)
        if self.lo.shape!=self.hi.shape or np.any(self.lo>self.hi):
            raise ValueError("Invalid angular table")
        self.N=len(self.lo)
        self.frequencies=np.asarray(frequencies,int)
        mp.iv.dps=65
        cosines=[];sines=[]
        for k in [1,3]+self.frequencies.tolist():
            cl=[];ch=[];sl=[];sh=[]
            for l,h in zip(self.lo,self.hi):
                theta=mp.iv.mpf([float(l),float(h)])*int(k)
                c,s=mp.iv.cos(theta),mp.iv.sin(theta)
                cl.append(m.K.dn(float(c.a)));ch.append(m.K.up(float(c.b)))
                sl.append(m.K.dn(float(s.a)));sh.append(m.K.up(float(s.b)))
            cosines.append(I(np.array(cl),np.array(ch)))
            sines.append(I(np.array(sl),np.array(sh)))
        self.cp,self.co3=cosines[:2]
        self.sp,self.sn3=sines[:2]
        self.co=stack_intervals(cosines[2:])
        self.sn=stack_intervals(sines[2:])
        self.H=None

    def trig(self,axis):
        if axis=="radial":
            return tuple(constant(x) for x in (self.cp,self.sp,self.co3,self.sn3,self.co,self.sn))
        if axis!="angular":
            raise ValueError("Unknown derivative axis")
        fr=I(self.frequencies[:,None])
        return (D(self.cp,-self.sp,-self.cp),D(self.sp,self.cp,-self.sp),
                D(self.co3,-3*self.sn3,-9*self.co3),
                D(self.sn3,3*self.co3,-9*self.sn3),
                D(self.co,-fr*self.sn,-fr.sq()*self.co),
                D(self.sn,fr*self.co,-fr.sq()*self.sn))

    def basis(self,y,axis,max_order=2):
        cp,sp,_,_,co,sn=self.trig(axis)
        M=len(self.frequencies);fr=I(self.frequencies[:,None])
        rr=y.item(slice(1,M+1)).expand()
        tt=y.item(slice(M+1,2*M+1)).expand()
        zz=y.item(slice(2*M+1,None)).expand()
        R=[y.item(0)+(rr*co).sum()]
        T=[(tt*sn).sum()]
        Z=[(zz*co).sum()]
        pairs=[(R[0],T[0],Z[0])]
        if max_order>=1:
            R.append(-(rr*sn*fr).sum())
            T.append((tt*co*fr).sum())
            Z.append(-(zz*sn*fr).sum())
            pairs.append((R[1]-T[0],T[1]+R[0],Z[1]))
        if max_order>=2:
            R.append(-(rr*co*fr.sq()).sum())
            T.append(-(tt*sn*fr.sq()).sum())
            Z.append(-(zz*co*fr.sq()).sum())
            pairs.append((R[2]-2*T[1]-R[0],T[2]+2*R[1]-T[0],Z[2]))
        if max_order>=3:
            R.append((rr*sn*(fr**3)).sum())
            T.append(-(tt*co*(fr**3)).sum())
            Z.append((zz*sn*(fr**3)).sum())
            pairs.append((R[3]-3*T[2]-3*R[1]+T[0],
                          T[3]+3*R[2]-3*T[1]-R[0],Z[3]))
        return [[r*cp-t*sp,r*sp+t*cp,z] for r,t,z in pairs]

    def load_mean_lift(self,data):
        self.H=[]
        for name in ("H","H1","H2"):
            a=raw_interval(data[name])
            self.H.append([a.item((slice(None),k)) for k in range(3)])

    def build_lift(self,core_data,field,kind,q):
        # H is exactly Gamma(theta0)-circle(theta0)-the frozen projection.
        w=I(field.warp_e)
        rho=1-w*self.co3;rp=3*w*self.sn3;rpp=9*w*self.co3
        ds,dc=m.sincos_i(-w*self.sn3/3)
        ct=self.cp*dc-self.sp*ds;st=self.sp*dc+self.cp*ds
        er=[ct,st,I(0)];et=[-st,ct,I(0)]
        circle=[er,
                [rho*x for x in et],
                [rp*et[k]-rho.sq()*er[k] for k in range(3)],
                [(rpp-rho**3)*et[k]-3*rho*rp*er[k] for k in range(3)]]
        original=constant(I(q)*I(np.asarray(field.exact_lift_initial,float)))
        projection=self.basis(original,"radial",3)
        gs=[]
        for name in ("F","Ft","Ftt","Fttt"):
            val=raw_interval(core_data[kind+"_"+name])
            gs.append([val.item((slice(None),k)) for k in range(3)])
        composed=[gs[0],
                  [rho*x for x in gs[1]],
                  [rho.sq()*gs[2][k]+rp*gs[1][k] for k in range(3)],
                  [rho**3*gs[3][k]+3*rho*rp*gs[2][k]+rpp*gs[1][k]
                   for k in range(3)]]
        self.H=[[composed[j][k]-circle[j][k]-projection[j][k].v
                 for k in range(3)] for j in range(4)]

    def lift(self,order,axis):
        if self.H is None:
            raise ValueError("No bound true lift")
        if axis=="radial":
            return [constant(x) for x in self.H[order]]
        return [D(self.H[order][k],self.H[order+1][k],self.H[order+2][k])
                for k in range(3)]


class PrefixMetric:
    def __init__(self,pieces,mean_table,point_table,box_table,angular_step):
        self.p=pieces
        self.mt=mean_table;self.pt=point_table;self.bt=box_table
        self.angular_step=I(angular_step)

    def data(self,left,right,axis):
        p=self.p
        s=I(I.rational(left).x[0],I.rational(right).x[1])
        y=p.field(s,left,right)
        ys=p.field(s,left,right,1)
        aa,ap=p.profile(s,left,right)
        e,ep=p.chart(s,left,right)
        chi,chip=p.lift(s,left,right)
        if axis=="angular":
            return [constant(x.v) for x in (y,ys,aa,ap,e,ep,chi,chip)]
        return [y,ys,aa,ap,e,ep,chi,chip]

    def frame(self,table,data,axis):
        y,ys,aa,ap,e,ep,chi,chip=data
        cp,sp,c3,s3,_,_=table.trig(axis)
        delta=-e*s3/3
        sd,cd=b.trig(delta)
        er=[cp*cd-sp*sd,sp*cd+cp*sd,D(0)]
        et=[-er[1],er[0],D(0)]
        rho=1-e*c3;rp=3*e*s3
        velocity=-ep*s3/(3*rho)
        return er,et,rho,rp,velocity

    def mean(self,data):
        tab=self.mt
        y,ys,aa,ap,e,ep,chi,chip=data
        er,et,rho,rp,v=self.frame(tab,data,"radial")
        basis=tab.basis(y,"radial",2)
        h1=tab.lift(1,"radial");h2=tab.lift(2,"radial")
        d1=plus(basis[1],scale(aa*chi,h1))
        d2=plus(basis[2],scale(aa*chi,h2))
        U=plus(et,scale(1/(aa*rho),d1))
        V=plus(scale(-1,er),scale(1/(aa*rho*rho),d2),
               scale(-rp/(aa*rho*rho*rho),d1))
        un=norm(U);ka=norm(cross(U,V))/(un**3)
        tangent=scale(1/un,U)
        normal0=plus(V,scale(-dot(tangent,V),tangent))
        normal=scale(1/norm(normal0),normal0)
        binormal=cross(tangent,normal)
        alpha=-ap/ka
        root=1-alpha.sq()
        if np.any(root.v.x[0]<=0):
            raise ValueError("Fixed-node Frenet root not proved")
        mean=(alpha*normal[2]+root.sqrt()*binormal[2]+v*d1[2]).sum()/tab.N
        if not all(getattr(mean,k).finite() for k in ("v","d","d2")):
            raise ArithmeticError("Nonfinite mean interval")
        return mean,float(np.min(root.v.x[0]))

    def metric(self,table,data,mean,axis,details=False):
        y,ys,aa,ap,e,ep,chi,chip=data
        er,et,rho,rp,v=self.frame(table,data,axis)
        G=table.basis(y,axis,1)
        Gs=table.basis(ys,axis,0)[0]
        H0=table.lift(0,axis);H1=table.lift(1,axis)
        tangent_pert=plus(G[1],scale(aa*chi,H1))
        radial_pert=plus(Gs,scale(ap*chi+aa*chip,H0))
        u=plus(radial_pert,scale(-v,tangent_pert))
        w=scale(1/(aa*rho),tangent_pert)
        # Cancel the exact circle target BEFORE interval arithmetic/norms.
        U0=plus(scale(ap,er),[D(0),D(0),mean])
        e11=ap.sq()+mean.sq()-1+2*dot(U0,u)+dot(u,u)
        e12=ap*dot(er,w)+mean*w[2]+dot(et,u)+dot(u,w)
        e22=2*dot(et,w)+dot(w,w)
        residual=[e11,e12,e22]
        if details:
            return residual,plus(U0,u),plus(et,w),v,rho
        return residual

    def enclose(self,left,right):
        center=(left+right)/2
        pd=self.data(center,center,"radial")
        pm,point_root=self.mean(pd)
        pe=self.metric(self.pt,pd,pm,"radial")
        wd=self.data(left,right,"radial")
        wm,whole_root=self.mean(wd)
        we=self.metric(self.pt,wd,wm,"radial")
        ad=[constant(x.v) for x in wd]
        ae,au,av,velocity,rho=self.metric(self.bt,ad,constant(wm.v),"angular",True)
        point=op_upper([x.v for x in pe])
        first=op_upper([x.d for x in pe])
        second=op_upper([x.d2 for x in we])
        angular=op_upper([x.d2 for x in ae])
        h=I.rational((right-left)/2)
        radial=I(point)+h*I(first)+h*h/2*I(second)
        angular_max=float(np.max(angular))
        remainder=self.angular_step*self.angular_step/8*angular_max
        bound=I(float(np.max(radial.x[1])))+remainder
        self.last_context=(wd,wm,au,av,velocity,rho)
        return float(bound.x[1]),{
            "point_operator":float(np.max(point)),
            "radial_first":float(np.max(first)),
            "radial_second":float(np.max(second)),
            "angular_second":angular_max,
            "angular_interpolation_error":float(remainder.x[1]),
            "fixed_mean_root":min(point_root,whole_root)}

    def curvature(self,metric_bound):
        # Additional geometry of the same accepted radial box; the mean and
        # angular jets are reused, not solved or integrated a second time.
        wd,wm,au,av,velocity,rho=self.last_context
        _,ru,_,_,_=self.metric(self.bt,wd,wm,"radial",True)
        u=[constant(x.v) for x in au];v=[constant(x.v) for x in av]
        normal0=cross(u,v)
        length=norm(normal0)
        if np.any(length.v.x[0]<=0):
            raise ValueError("The geometric normal interval includes zero")
        normal=scale(1/length,normal0)
        n=[x.v for x in normal]
        aa=wd[2].v
        first=[x.d for x in au];second=[x.d for x in av]
        h11=sum((n[k]*(ru[k].d-velocity.v*first[k]) for k in range(3)),I(0))
        h12=sum((n[k]*first[k]/(aa*rho.v) for k in range(3)),I(0))
        h22=sum((n[k]*second[k]/(aa*rho.v) for k in range(3)),I(0))
        upper=float(np.max(op_upper([h11,h12,h22])))
        return float((I(upper)/(1-I(metric_bound))).x[1])


def binding(record,run_hash,physical_hash,arrays):
    if record.get("source_run_sha256",record.get("run_sha256"))!=run_hash:
        raise ValueError("Core certificate source-run mismatch")
    if record.get("physical_sha256")!=physical_hash:
        raise ValueError("Core certificate physical input mismatch")
    if record.get("interval_output_sha256")!=sha(arrays):
        raise ValueError("Core interval array mismatch")


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ("source-run","physical","core-mean-intervals","core-mean-certificate",
                "core-angle-intervals","core-angle-certificate","interval-kernel","out"):
        ap.add_argument("--"+key,type=Path,required=True)
    ap.add_argument("--target",type=float,default=9.7e-7)
    ap.add_argument("--max-cells",type=int,default=100000)
    ap.add_argument("--probe-only",action="store_true")
    args=ap.parse_args();started=time.monotonic()
    m.K=m.module("_lifted_prefix_interval_kernel",args.interval_kernel)
    support=Path(__file__).resolve().parent
    adapter=m.module("_lifted_prefix_model",support/"actual_m3_metric_model.py")
    loader=m.module("_lifted_prefix_physical",support/"audit_full_relative_metric.py")
    o=adapter.load_model({"source_run":str(args.source_run.resolve())})
    physical=loader.load_physical(args.physical)
    pieces=PrefixPieces(o,physical)
    rh,ph=sha(args.source_run),sha(args.physical)
    mc=json.loads(args.core_mean_certificate.read_text())
    ac=json.loads(args.core_angle_certificate.read_text())
    binding(mc,rh,ph,args.core_mean_intervals)
    binding(ac,rh,ph,args.core_angle_intervals)
    with np.load(args.core_mean_intervals) as z:
        mt=AngleTable(z["psi"],z["psi"],pieces.f.even)
        mt.load_mean_lift(z)
    assert mt.N==1168
    with np.load(args.core_angle_intervals) as z:
        pt=AngleTable(z["psi"],z["psi"],pieces.f.even)
        bt=AngleTable(z["psi_lo"],z["psi_hi"],pieces.f.even)
        pt.build_lift(z,pieces.f,"point",pieces.q)
        bt.build_lift(z,pieces.f,"box",pieces.q)
        psi=np.asarray(z["psi"],float)
        if len(psi)!=len(bt.lo) or psi[0]!=0 or np.any(np.diff(psi)<=0):
            raise ValueError("Angular ordering is not a complete cyclic grid")
        if not np.array_equal(bt.lo,psi) or not np.array_equal(bt.hi[:-1],psi[1:]):
            raise ValueError("Angular boxes do not match interpolation endpoints")
        mp.iv.dps=70
        pi_hi=m.K.up(float((2*mp.iv.pi).b))
        if bt.hi[-1]<pi_hi:
            raise ValueError("Last angular box does not cover the true period")
        step=float(np.max((I(bt.hi)-I(bt.lo)).x[1]))
    verifier=PrefixMetric(pieces,mt,pt,bt,step)
    report={"status":"running","target":args.target,"source_sha256":sha(__file__),
        "pieces_source_sha256":sha(support/"explicit_m24_prefix_pieces.py"),
        "derivative_kernel_sha256":sha(support/"certify_bridge_metric_fourier_taylor.py"),
        "interval_wrapper_sha256":sha(support/"certify_r59_fixed_mean_ranges.py"),
        "source_run_sha256":rh,"physical_sha256":ph,"mean_nodes":mt.N,
        "angular_nodes":pt.N,"angular_step_upper":step,
        "core_mean_certificate_sha256":sha(args.core_mean_certificate),
        "core_angle_certificate_sha256":sha(args.core_angle_certificate),
        "core_mean_intervals_sha256":sha(args.core_mean_intervals),
        "core_angle_intervals_sha256":sha(args.core_angle_intervals),
        "interval_kernel_sha256":sha(args.interval_kernel),
        "explicit_shared_C2_object":True,"true_R53_core_used":True,
        "endpoint_normalized_profile":True,"complete_surface":False,
        "accepted":0,"attempts":0,"splits":0,"peak":0.,
        "root_lower":None,"angular_second_upper":0.,
        "principal_curvature_upper":0.,"curvature_unresolved_cells":0}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report["seconds"]=time.monotonic()-started
        args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    if args.probe_only:
        probes=[]
        for index in np.linspace(0,len(pieces.grid)-2,9).astype(int):
            left,right=pieces.grid[index:index+2]
            c=(left+right)/2
            bound,meta=verifier.enclose(c,c)
            row={"s":float(c),"bound":bound,**meta}
            probes.append(row);print(json.dumps({"event":"point_probe",**row}),flush=True)
        report.update(status="point_probes_only",probes=probes)
        save();return
    todo=[(l,r,0) for l,r in zip(pieces.grid[:-1],pieces.grid[1:])][::-1]
    while todo:
        left,right,depth=todo.pop();report["attempts"]+=1
        try:
            bound,meta=verifier.enclose(left,right)
            reason="metric bound exceeds target"
        except (ValueError,ArithmeticError,FloatingPointError) as exc:
            bound=math.inf;meta=None;reason=str(exc)
        if bound<=args.target:
            report["accepted"]+=1
            try:
                curve=verifier.curvature(bound)
                if not math.isfinite(curve):
                    raise ArithmeticError("Nonfinite curvature")
                if curve>report["principal_curvature_upper"]:
                    report.update(principal_curvature_upper=curve,
                                  curvature_peak_interval=[float(left),float(right)])
            except (ValueError,ArithmeticError,FloatingPointError):
                report["curvature_unresolved_cells"]+=1
            if bound>report["peak"]:
                report.update(peak=bound,peak_interval=[float(left),float(right)],
                              peak_components=meta)
            root=meta["fixed_mean_root"]
            report["root_lower"]=root if report["root_lower"] is None else min(root,report["root_lower"])
            report["angular_second_upper"]=max(report["angular_second_upper"],meta["angular_second"])
        else:
            if depth>=28 or report["accepted"]+len(todo)>=args.max_cells:
                report.update(status="not_certified",unresolved_interval=[float(left),float(right)],
                    unresolved_reason=reason,last_bound=None if not math.isfinite(bound) else bound,
                    last_components=meta,remaining=len(todo)+1)
                save();print(json.dumps(report),flush=True);return
            middle=(left+right)/2
            todo.extend([(middle,right,depth+1),(left,middle,depth+1)])
            report["splits"]+=1
        if report["attempts"]%50==0:
            print(json.dumps({"event":"prefix_continuous_metric_progress",
                "accepted":report["accepted"],"attempts":report["attempts"],
                "splits":report["splits"],"remaining":len(todo),"s":float(right),
                "peak":report["peak"],"seconds":time.monotonic()-started}),flush=True)
    report.update(status="explicit_C2_prefix_continuous_metric_certified")
    save();print(json.dumps(report),flush=True)


if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""Full original finite-tilt continuation with actual principal-curvature constraints."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import time
import numpy as np
from scipy.linalg import qr, svd
from r659_finite_tilt_latitude_system_20261128 import (
    LatitudeSystem, dot, emit, extend_exactly, jy, mean_free, peg_readout,
    primitive, rz_frame)


def angular_derivative(value):
    n=value.shape[1]
    freq=np.arange(n//2+1)
    return np.fft.irfft(np.fft.rfft(value,axis=1)*(1j*freq)[None,:,None],n=n,axis=1)


class ReachSystem(LatitudeSystem):
    def shape(self,x,g,st,options,order_measure):
        D,H=st["D"],st["H"]
        r=g["r"][:,None,None]
        Y=r*H
        area=np.cross(D,Y)
        area_length=np.linalg.norm(area,axis=-1)
        if area_length.min()<=1e-12:
            raise FloatingPointError("singular actual finite-tilt frame")
        n=area/area_length[...,None]
        e,f,gg=dot(D,D),dot(D,Y),dot(Y,Y)
        m=f/e
        h=np.sqrt(gg-f*m)
        se=np.sqrt(e)
        L,M,N=[dot(n,st[key]) for key in ("Drr","Drp","Dpp")]
        aa,ab,bb=L/e,(M-m*L)/(se*h),(N-2*m*M+m*m*L)/(h*h)
        alpha=.5*np.arctan2(2*ab,aa-bb)
        ca,sa=np.cos(alpha),np.sin(alpha)
        eigen=[]
        for sign,v1,v2 in ((1,ca,sa),(-1,-sa,ca)):
            vr,vp=v1/se-v2*m/h,v2/h
            a,j,c=vr**2,2*vr*vp,vp**2
            curvature=a*L+j*M+c*N
            direction=vr[...,None]*D+vp[...,None]*Y
            second=a[...,None]*st["Drr"]+j[...,None]*st["Drp"]+c[...,None]*st["Dpp"]
            eigen.append((sign,curvature,vr,vp,direction,second))
        axis_o=np.stack((-np.sin(g["q"]),np.zeros(len(r)),np.cos(g["q"])),axis=-1)[:,None,:]
        axis_i=np.stack((np.sin(self.ang-g["q"]),np.zeros(len(r)),np.cos(self.ang-g["q"])),axis=-1)[:,None,:]
        constraints=[sign*options["T"]*curv-options["curvature_guard"]
                     for sign,curv,*_ in eigen]
        axes=(axis_o,axis_i)
        constraints.extend(options["normal_guard"]-dot(n,v) for v in axes)
        beta=np.linspace(-.25,.65,181)
        directions=np.array([np.cos(beta),np.sin(beta)]).T
        c=self.center(x,np.array([self.a]))[0][[0,2]]
        d0=np.array([self.b-self.a*math.cos(self.ang),self.a*math.sin(self.ang)])
        A,B=abs(beta+self.ang),abs(beta)
        turning=options["T"]*(A-np.sin(A)+B-np.sin(B))
        if (self.b-self.a)<options["T"]*max(A+B):
            raise ArithmeticError("overlap of directional endpoint tangent budgets")
        traces=np.stack((directions@(d0+c)+turning,directions@(d0-c)+turning))
        i,j=np.unravel_index(np.argmax(traces),traces.shape)
        cgrad=(1 if i==0 else -1)*directions[j]
        E=st["E"]
        length=(self.b-self.a)*float(order_measure@np.sqrt(E))
        excess=(traces[i,j]+options["length_guard"]-length)/(self.b-self.a)
        return dict(n=n,Y=Y,area_length=area_length,eigen=eigen,axes=axes,
                    constraints=constraints,excess=excess,cgrad=cgrad,
                    length=length,required=float(traces[i,j]),winning_angle=float(beta[j]),
                    directions=order_measure,actual_center=c,
                    max_abs_curvature=float(max(np.max(abs(item[1])) for item in eigen)),
                    min_outer_normal=float(np.min(dot(n,axis_o))),min_inner_normal=float(np.min(dot(n,axis_i))))

    def evaluate(self,x,g,options,fixed_E=None):
        self.count["augmented_residual_calls"]+=1
        st=self.state(x,g,second=True)
        D,H=st["D"],st["H"]
        scale=1+g["refw"]**2
        E=st["E"] if fixed_E is None else fixed_E
        metric=self.pack((dot(D,D)-E[:,None])/scale[:,None],dot(D,H)/np.sqrt(scale)[:,None],
                         dot(H,H)-1,st["T"][...,1].mean(axis=1),g)
        sh=self.shape(x,g,st,options,g["weights"])
        if fixed_E is not None:
            sh["length"]=(self.b-self.a)*float(g["weights"]@np.sqrt(fixed_E))
            sh["excess"]=(sh["required"]+options["length_guard"]-sh["length"])/(self.b-self.a)
        weight=np.sqrt(g["weights"][:,None]/len(g["phi"]))
        factors=[options["curvature_weight"]]*2+[options["normal_weight"]]*2
        blocks=[np.maximum(val,0)*weight*f for f,val in zip(factors,sh["constraints"])]
        peaks=[options["peak_weight"]*max(0.,float(val.max())) for val in sh["constraints"]]
        geom=np.r_[*[v.ravel() for v in blocks],options["length_weight"]*max(0.,sh["excess"]),peaks]
        return metric,geom,st,sh

    def full_jacobian(self,x,g,st,sh,options,fixed):
        base=self.jacobian(st,g,fixed)
        r=g["r"][:,None,None]
        qx=g["qx"][:,None,None]
        qxx=g["qxx"][:,None,None]
        D,Y,n=st["D"],sh["Y"],sh["n"]
        active=[z>0 for z in sh["constraints"]]
        active_last=sh["excess"]>0
        size=[int(mask.sum()) for mask in active]
        nrows=sum(size)+int(active_last)
        extra=np.empty((nrows,self.size),order="F")
        weights=np.sqrt(g["weights"][:,None]/len(g["phi"]))
        factors=[options["curvature_weight"]]*2+[options["normal_weight"]]*2
        def effects(dD,dY,rr,rp,pp):
            da=np.cross(dD,Y)+np.cross(D,dY)
            dn=(da-n*dot(n,da)[...,None])/sh["area_length"][...,None]
            out=[]
            for ii,(sign,curv,vr,vp,direction,second) in enumerate(sh["eigen"]):
                dv=vr[...,None]*dD+vp[...,None]*dY
                dd=vr[...,None]**2*rr+2*(vr*vp)[...,None]*rp+vp[...,None]**2*pp
                delta=dot(dn,second)+dot(n,dd)-2*curv*dot(direction,dv)
                out.append(sign*options["T"]*delta)
            out.extend(-dot(dn,axis) for axis in sh["axes"])
            length=np.zeros(len(r)) if fixed else dot(D,dD).mean(axis=1)/np.sqrt(st["E"])
            return out,length
        def add(slot,mats,derivatives,count_center=None):
            off=0
            cols=mats[0].shape[1]
            for ii,mask in enumerate(active):
                irows=np.nonzero(mask)[0]
                if len(irows):
                    chunk=np.zeros((len(irows),cols))
                    for mat,(channel,leng) in zip(mats,derivatives):
                        chunk+=(channel[ii]*weights*factors[ii])[mask,None]*mat[irows]
                    extra[off:off+len(irows),slot:slot+cols]=chunk
                off+=len(irows)
            if active_last:
                # divided by (b-a), so dS contribution has normalized Gauss weights
                row=-sum((g["weights"]*ls)@mat for mat,(_,ls) in zip(mats,derivatives))
                if count_center is not None:
                    row+=count_center/(self.b-self.a)
                extra[off,slot:slot+cols]=options["length_weight"]*row
        u,v,_=self.split(x)
        def field(co,k):
            return (g["A"][k]@co.T@g["sn"])[...,None]
        ur,vr,urr,vrr=field(u,1),field(v,1),field(u,2),field(v,2)
        a,b=field(u,0),field(v,0)
        hor=np.sin(a)*g["er"]+np.cos(a)*g["et"]
        hop=np.cos(a)*g["er"]-np.sin(a)*g["et"]
        T,Tu,Tv=st["T"],st["Tu"],st["Tv"]
        Tuu,Tuv,Tvv=-np.cos(b)*hor,-np.sin(b)*hop,-T
        Tuuv=np.sin(b)*hor
        Turr=(-Tu*ur**2+2*Tuuv*ur*vr-Tu*vr**2+Tuu*urr+Tuv*vrr)
        Tvrr=(Tuuv*ur**2-2*Tu*ur*vr-Tv*vr**2+Tuv*urr+Tvv*vrr)
        zero=np.zeros_like(D)
        for side,(tw,twr,twrr) in enumerate(((Tu,st["Tur"],Turr),(Tv,st["Tvr"],Tvrr))):
            for j,sine in enumerate(g["sn"]):
                w=sine[None,:,None]
                V,Vr,Vrr=tw*w,twr*w,twrr*w
                U,Ur,Urr=primitive(V),primitive(Vr),primitive(Vrr)
                H,Hr=mean_free(V),mean_free(Vr)
                first=effects(U+r*Ur+r*qx*jy(U),r*H,
                    2*Ur+r*Urr+2*qx*jy(U+r*Ur)+r*qxx*jy(U)+r*qx**2*jy(jy(U)),
                    H+r*Hr+r*qx*jy(H),r*angular_derivative(H))
                rate=effects(r*U,zero,2*U+2*r*Ur+2*r*qx*jy(U),r*H,zero)
                acceleration=effects(zero,zero,r*U,zero,zero)
                add((side*self.K+j)*self.na,g["A"],(first,rate,acceleration))
        anti=self.spl.antiderivative()
        cint=(anti(self.a)-anti(self.b))[2:-2]
        for i,coord in enumerate((0,2)):
            axis=np.zeros_like(D)
            axis[...,coord]=1
            axis=rz_frame(axis,-g["q"][:,None])
            add(2*self.K*self.na+i*self.nc,g["C"][:2],
                (effects(axis,zero,zero,zero,zero),effects(zero,zero,axis,zero,zero)),
                sh["cgrad"][i]*cint)
        self.count["all_geometry_columns"]+=self.size
        active_ids=np.r_[*[m.ravel() for m in active],active_last]
        peak_rows=[]
        peak_active=[]
        off=0
        for ii,mask in enumerate(active):
            peak_active.append(bool(mask.any()))
            if mask.any():
                values=sh["constraints"][ii]
                peak=np.unravel_index(np.argmax(values),values.shape)
                source_row=off+int(np.sum(mask.ravel()[:np.ravel_multi_index(peak,mask.shape)]))
                scale=options["peak_weight"]/(weights[peak[0],0]*factors[ii])
                peak_rows.append(extra[source_row]*scale)
            off+=size[ii]
        matrix=np.vstack((base,extra,*peak_rows))
        return np.asfortranarray(matrix),np.r_[active_ids,peak_active]


def observations(sys,x,order,angles,opts,frozen):
    g=sys.grid(order,angles,endpoints=True)
    Eref=None
    if frozen is not None:
        fs,fx=frozen
        Eref=fs.state(fx,fs.at(g["r"],opts["reference_azimuths"]))["E"]
    data=sys.readout(x,g,Eref)
    st=sys.state(x,g,second=True)
    intervals=np.diff(g["r"])
    trap=(np.r_[0,intervals]+np.r_[intervals,0])/(2*(sys.b-sys.a))
    sh=sys.shape(x,g,st,opts,trap)
    data.update(sampled_min_n_dot_outer=sh["min_outer_normal"],sampled_min_n_dot_inner=sh["min_inner_normal"],
                sampled_tangent_cost_with_actual_center=sh["required"],
                sampled_R665_length_margin=data["sampled_complete_meridian_length"]-sh["required"],
                sampled_worst_R665_direction_radians=sh["winning_angle"])
    if frozen is not None:
        fs,fx=frozen
        other=fs.state(fx,fs.at(g["r"],opts["check_reference_azimuths"]))["E"]
        data["sampled_frozen_angular_relative_difference"]=float(np.max(abs(other/Eref-1)))
    cx,_,cz=data["actual_inner_center"]
    peg=peg_readout(sys.a,cx,cz,sys.ang)
    data["peg"]=peg
    radius=max(data["sampled_annulus_max_outer_horizontal_radius"],peg["sampled_outer_horizontal_radius"])
    zmin=min(data["sampled_annulus_z_range"][0],peg["sampled_outer_z_range"][0])
    zmax=max(data["sampled_annulus_z_range"][1],peg["sampled_outer_z_range"][1])
    data["sampled_full_D_budget"]=max(
        max(2/3,math.hypot(.75,.35))+2*.04501,
        .04501+math.hypot(1/3+radius,max(abs(zmin+.045),abs(zmax+.045))),
        .04501+math.hypot(5/12+radius,max(abs(zmin+.395),abs(zmax+.395))),
        math.hypot(2*radius,zmax-zmin))
    return data


def geometry_gate(data):
    return (data["sampled_max_principal_curvature"]<=100/3
            and min(data["sampled_min_n_dot_outer"],data["sampled_min_n_dot_inner"])>.05
            and data["sampled_R665_length_margin"]>=0
            and data["sampled_full_D_budget"]<=1
            and -.08<=data["sampled_annulus_z_range"][0]
            and data["sampled_annulus_z_range"][1]<=.315
            and abs(data["actual_inner_center"][0])<=.028
            and -.05<=data["actual_inner_center"][2]<=.037)


def trust_step(sv,vt,force,trust,least):
    def amp(mu):
        return force*sv/(sv*sv+mu)
    mu=least
    if np.linalg.norm(amp(mu))>trust:
        hi=mu
        while np.linalg.norm(amp(hi))>trust:
            hi*=8
        lo=mu
        for _ in range(40):
            mid=math.sqrt(lo*hi)
            if np.linalg.norm(amp(mid))>trust:
                lo=mid
            else:
                hi=mid
        mu=hi
    v=amp(mu)
    pred=float(2*force@(sv*v)-(sv*v)@(sv*v))
    return vt.T@v,pred,mu


def main():
    if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY","").lower()!="rogerhu12/math-research-public" or
        not os.environ.get("GITHUB_RUN_ID","").isdigit()):
        raise SystemExit("Scientific execution requires public math-research-public Actions.")
    parser=argparse.ArgumentParser()
    parser.add_argument("--geometry",required=True)
    parser.add_argument("--max-seconds",type=float,required=True)
    args=parser.parse_args()
    opts=json.loads(Path(args.geometry).read_text())
    prior=json.loads(Path(opts["input_state"]).read_text())
    if (len(prior["continuous_parameters"])!=810 or prior["run"]!=46136199153
        or prior["last_accepted_trust"]!=.0010046531249999998):
        raise ValueError("Wrong physical source continuation.")
    t0=time.perf_counter()
    elapsed=lambda: time.perf_counter()-t0
    count=Counter()
    naccepted=0
    frozen=None
    stages=[]
    current=ReachSystem(prior["space"],count)
    x=np.array(prior["continuous_parameters"],dtype=float)
    trust=prior["last_accepted_trust"]
    report=None
    accepted_fixed=False
    emit("provenance",source_run=prior["run"],previous_objective=prior["last_work_norm"],
         preserved_costs=prior["previous_counts"],previous_scientific_seconds=prior["previous_scientific_seconds"],
         previous_terminal_trust=prior["next_space_promoted_trust"],resumed_same_space_trust=trust,
         complete_original_columns=True,true_pose_sine=math.sin(current.ang),
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    def frozen_at(sys,g):
        if frozen is None:
            return None
        fs,fx=frozen
        return fs.state(fx,fs.at(g["r"],opts["reference_azimuths"]))["E"]
    try:
        program=list(opts["stages"])
        for ix,phase in enumerate(program):
            if elapsed()>args.max_seconds-opts["reserve_seconds"]:
                break
            wopts=dict(opts,curvature_weight=phase["curvature_weight"])
            if phase["modes"]!=current.K or phase["spans"]!=current.nsp:
                old=current
                current=ReachSystem(dict(old.spec,body_modes=phase["modes"],radial_spans=phase["spans"]),count)
                x=extend_exactly(old,x,current)
                count["exact_prolongations"]+=1
                trust=max(trust,opts["promotion_trust"])
            g=current.grid(phase["work_order"],phase["work_angles"])
            Eref=frozen_at(current,g)
            def evaluate(params):
                return current.evaluate(params,g,wopts,Eref)
            mr,gr,st,sh=evaluate(x)
            def objective(a,b):
                return float(a@a+b@b)
            before=objective(mr,gr)
            accepted=0
            emit("stage_start",stage=ix,modes=current.K,spans=current.nsp,trust=trust,
                 residual_norm=math.sqrt(before),metric_norm=float(np.linalg.norm(mr)),
                 working_max_curvature=sh["max_abs_curvature"],working_R665_margin=sh["length"]-sh["required"],
                 frozen=frozen is not None,rows_including_inactive=len(mr)+len(gr),original_columns=current.size)
            for iteration in range(phase["iterations"]):
                if elapsed()>args.max_seconds-opts["reserve_seconds"]:
                    break
                jac,active=current.full_jacobian(x,g,st,sh,wopts,frozen is not None)
                r=np.r_[mr,gr[active]]
                if iteration==0:
                    direction=np.sin(np.arange(1,current.size+1)*.461)
                    direction/=np.linalg.norm(direction)
                    jv=jac@direction
                    differences=[]
                    for eps in (3e-7,7e-8):
                        pp,pg,_,_=evaluate(x+eps*direction)
                        mm,mg,_,_=evaluate(x-eps*direction)
                        fd=np.r_[pp-mm,(pg-mg)[active]]/(2*eps)
                        errors=[]
                        for sl in (slice(None,len(mr)),slice(len(mr),None),slice(None)):
                            err=np.linalg.norm(jv[sl]-fd[sl])/max(np.linalg.norm(fd[sl]),1e-9)
                            errors.append(float(err))
                        differences.append(errors)
                    emit("complete_J_direction",stage=ix,original_columns=current.size,
                         active_physical_rows=int(sum(active)),relative_metric_geometry_total=differences)
                    if min(d[2] for d in differences)>2e-4:
                        raise ArithmeticError("Complete physical Jacobian direction disagrees with finite difference.")
                Q,R=qr(jac,mode="economic",check_finite=False,overwrite_a=True)
                rhs=Q.T@r
                del Q,jac
                U,sv,vt=svd(R,full_matrices=False,check_finite=False)
                force=-(U.T@rhs)
                least=max(1e-18,1e-13*float(sv[0])**2)
                oldloss=objective(mr,gr)
                accepted_here=False
                count["complete_original_QR_SVD"]+=1
                for _ in range(14):
                    dx,pred,mu=trust_step(sv,vt,force,trust,least)
                    mn,gn,sn,hn=evaluate(x+dx)
                    loss=objective(mn,gn)
                    gain=(oldloss-loss)/pred if pred>0 else -math.inf
                    count["actual_augmented_trials"]+=1
                    if loss<oldloss and gain>.015:
                        x=x+dx
                        mr,gr,st,sh=mn,gn,sn,hn
                        accepted+=1
                        naccepted+=1
                        if gain>.70 and np.linalg.norm(dx)>.8*trust:
                            trust=min(1.65*trust,opts["max_trust"])
                        elif gain<.18:
                            trust=max(.6*trust,1e-10)
                        accepted_fixed|=frozen is not None
                        emit("accepted",stage=ix,iteration=iteration,accepted=naccepted,
                             objective_norm=math.sqrt(loss),metric_norm=float(np.linalg.norm(mr)),
                             geometry_norm=float(np.linalg.norm(gr)),working_max_curvature=sh["max_abs_curvature"],
                             working_min_axis_normals=[sh["min_outer_normal"],sh["min_inner_normal"]],
                             working_tangent_length_margin=sh["length"]-sh["required"],
                             all_original_singular_range=[float(sv[-1]),float(sv[0])],
                             trust=trust,damping=mu,actual_complete_state=x.tolist(),elapsed_seconds=elapsed())
                        accepted_here=True
                        break
                    trust*=.38
                    if trust<1e-10:
                        break
                if not accepted_here:
                    break
                if math.sqrt(loss)<opts["work_goal"]:
                    break
            report=observations(current,x,phase["fine_order"],phase["fine_angles"],wopts,frozen)
            stages.append(dict(stage=ix,accepted=accepted,metric_norm=float(np.linalg.norm(mr)),
                               total_norm=math.sqrt(objective(mr,gr)),fixed_E=frozen is not None))
            emit("stage_complete",**stages[-1],trust=trust,working_report=report,
                 actual_complete_state=x.tolist(),actual_space=current.spec,counts=dict(count),
                 elapsed_seconds=elapsed())
            if frozen is None and geometry_gate(report) and report["sampled_metric_max_relative"]<=opts["freeze_metric"]:
                frozen=(current,x.copy())
                emit("metric_frozen",source_space=current.spec,coefficients=x.tolist(),azimuths=opts["reference_azimuths"])
                if ix==len(program)-1:
                    program.append(opts["extra_fixed_stage"])
        if not stages:
            raise RuntimeError("No actual continuation was evaluated.")
        forder=program[len(stages)-1]["fine_order"]
        fangles=program[len(stages)-1]["fine_angles"]
        crossed={}
        for name,nrad,nphi in (("radial_only",opts["final_order"],fangles),
                               ("angle_only",forder,opts["final_angles"])):
            crossed[name]=observations(current,x,nrad,nphi,opts,frozen)
        report=observations(current,x,opts["final_order"],opts["final_angles"],opts,frozen)
        emit("terminal",source_run=prior["run"],stages=stages,
             original_columns=current.size,actual_complete_state=x.tolist(),actual_space=current.spec,
             actual_final_trust=trust,accepted=naccepted,counts=dict(count),final_report=report,
             independent_crossed_grids=crossed,finite_sample_geometry_gate=geometry_gate(report),
             frozen_reference=None if frozen is None else dict(space=frozen[0].spec,coefficients=frozen[1].tolist(),
                                                               angular_points=opts["reference_azimuths"]),
             accepted_fixed_metric_refinement=bool(accepted_fixed),elapsed_seconds=elapsed(),
             certified_all_points=False,README_completion_claim=False)
    except Exception as exc:
        emit("incomplete",reason=str(exc),actual_complete_state=x.tolist(),actual_space=current.spec,
             trust=trust,counts=dict(count),last_report=report,elapsed_seconds=elapsed())
        raise


if __name__=="__main__":
    main()

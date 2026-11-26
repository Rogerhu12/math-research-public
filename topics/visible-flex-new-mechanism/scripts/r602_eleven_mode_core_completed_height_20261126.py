#!/usr/bin/env python3
"""New 11-mode full weak height BVP with dependent R602 core completion.

Keep all paid coefficients and choose one fixed512 old-tanh radial mean.
Only modes18/20/22 get new true finite DtN mouths; all previous mouths are
reused. R602 is an actual added height
term with its full parameter and spatial jets, not removal of residual rows.
Science belongs only to the declared public Actions job.
"""
import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE=Path(__file__).resolve().parent
RESUME_FILE="r594_paid_weak_resume_20261126.py"
RESUME_SHA="bf1200c36779f06d8b54a21739509e467d8e32da76cd8e63867533e9ce25f5af"
HIGH_FILE="r600_factored_high_mode_jets_20261126.py"
HIGH_SHA="f6297e6e9a5272374273f5161a2010fc0e2eef9a4aa1b622102292d02267a5a9"
SCHEMA="r602-paid-height-eleven-weak-modes-and-full-dependent-core-v1"
SOURCE_RUN,SOURCE_JOB=45832877990,139953949524
SOURCE_COMMIT="92d43f4eec2abb934d781b941428d81fe136b38f"
SOURCE_RAW_SHA="0330b67723e0b99e457cb9f5516bacc37515e3987dbc96c928cfd20525fe7a4c"
SOURCE_FINAL_SHA="ebf6387feda9db2b5917126723391c882ab227a04f8880d1132e3ddcef1994c2"
SOURCE_Q_SHA="73e3fced9fabb88fd45c61e78befa192a1ad4439951fcd4ca0b7a80cd0e6dfd3"
MODES=np.arange(2,23,2,dtype=int)
CORE_MODES=np.arange(2,45,2,dtype=int)
CORE_QUADRATURE=512
CORE_LEFT,CORE_RIGHT=.65,.78
HARMONIC_MAX=96
COUNTS=defaultdict(int)
REJECTIONS={}

def bound_import(name,filename,digest):
    path=HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        raise RuntimeError("new complete-height source binding differs: "+filename)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

resume=bound_import("r602_paid_resume",RESUME_FILE,RESUME_SHA)
high=bound_import("r602_high_modes",HIGH_FILE,HIGH_SHA)
weak,base,paid,parent,knot=resume.weak,resume.base,resume.paid,resume.parent,resume.knot
emit=base.emit
check=weak.check


def reject(reason):
    COUNTS["rejected_steps"]+=1
    REJECTIONS[reason]=REJECTIONS.get(reason,0)+1


def input_state(args):
    raw=sys.stdin.buffer.read() if args.source_state_json=="@stdin" else args.source_state_json.encode()
    digest=hashlib.sha256(raw).hexdigest()
    if digest!=args.source_state_sha256:
        raise ValueError("new scope full input stdin identity differs")
    source=json.loads(raw)
    expected={"run_id":SOURCE_RUN,"job_id":SOURCE_JOB,"source_commit":SOURCE_COMMIT,
        "source_sha256":RESUME_SHA,"raw_stdout_bytes":1160033,"raw_stdout_sha256":SOURCE_RAW_SHA,
        "FINAL_JSON_bytes":36932,"FINAL_JSON_sha256":SOURCE_FINAL_SHA,
        "kind":"natural_next_sixty_iteration_limit_near_stationarity"}
    if source["origin"]!=expected:
        raise ValueError("actual paid terminal origin differs")
    qtext=source["actual_496q_JSON"]
    if len(qtext.encode())!=10880 or hashlib.sha256(qtext.encode()).hexdigest()!=SOURCE_Q_SHA:
        raise ValueError("actual paid 496-q JSON differs")
    q=np.asarray(json.loads(qtext),dtype=float)
    if q.shape!=(496,) or not np.all(np.isfinite(q)) or q[0]!=.5188892673274983:
        raise ValueError("invalid actual previous height state")
    if (source["amplitude"]!=1e-5 or source["global_accepted_iteration"]!=120
            or source["actual_next_damping"]!=1e-14
            or source["source_265q_sha256"]!=weak.SOURCE_Q_SHA
            or source["source_67knots_sha256"]!=weak.SOURCE_KNOT_SHA):
        raise ValueError("complete paid field, true iteration, or damping changed")
    if sorted(source["paid_modes_10_through_16"])!=["10","12","14","16"]:
        raise ValueError("all four already paid higher mouths must be reused")
    for j in (10,12,14,16):
        record=source["paid_modes_10_through_16"][str(j)]
        data=record["finite_inner_data"]
        if (data["mode"]!=j or data["M"]!=25 or data["terminal_peak_index"]!=26
                or record["terminal_index"]!=26 or len(data["outer_jets"])!=13):
            raise ValueError("a paid mouth's finite input identity is incomplete")
    return source,q,float(source["amplitude"]),float(source["actual_next_damping"]),digest


def expanded_paid_q(q,nb):
    """A literal index embedding, with no profile or seed evaluation."""
    if q.size!=1+7+8*nb:
        raise ValueError("old 496-q basis dimensions disagree")
    answer=np.zeros(1+(len(MODES)-1)+len(MODES)*nb)
    answer[0]=q[0]
    answer[1:8]=q[1:8]
    answer[len(MODES):len(MODES)+8*nb]=q[8:]
    recovered=np.r_[answer[0],answer[1:8],answer[len(MODES):len(MODES)+8*nb]]
    if not np.array_equal(q,recovered):
        raise ValueError("the original complete field was not embedded literally")
    return answer


class CompletedCoreHeight(weak.WeakHeight):
    def __init__(self,paid_model,modes,args,deadline):
        super().__init__(paid_model.old,paid_model.paidq,modes,args,deadline)
        self.nm=len(MODES)
        self.nq=1+(self.nm-1)+self.nm*self.nb
        self.column_modes=np.r_[MODES[1:],np.repeat(MODES,self.nb)]
        self.minimum=paid_model.minimum
        if any(m.flat.minimum_radius>self.minimum*(1+1e-14) for m in modes):
            raise ValueError("a new mode would discard a paid radial node")
        self.core_theta=np.arange(CORE_QUADRATURE)*2*np.pi/CORE_QUADRATURE
        self.core_co=np.cos(MODES[:,None]*self.core_theta)
        self.core_si=np.sin(MODES[:,None]*self.core_theta)
        self.core_all_co=np.cos(CORE_MODES[:,None]*self.core_theta)
        self.trace_key,self.trace_cached=None,None
        self.actual_checkpoint=None
        self.new_direction_observed=False
        self.canonical_mean_cache={}
        self.canonical_mean_observations={}

    def prepare(self,r,ntheta):
        check(self.deadline)
        r=np.asarray(r,dtype=float)
        key=(r.tobytes(),int(ntheta))
        if key in self.cache:
            return self.cache[key]
        data=dict(self.old.prepare(r,ntheta))
        fields=np.concatenate([data["fields"],
            np.stack([m.evaluate(r) for m in self.modes[4:]],axis=1)],axis=1)
        chi,chir,chirr=base.step2((r-weak.BULK_LEFT)/(weak.BULK_RIGHT-weak.BULK_LEFT))
        chir/=weak.BULK_RIGHT-weak.BULK_LEFT
        chirr/=(weak.BULK_RIGHT-weak.BULK_LEFT)**2
        delta,power=self.par.R-r,self.bulk_power
        v=chi*delta**power/self.bulk_scale
        vr=(chir*delta**power-chi*power*delta**(power-1))/self.bulk_scale
        vrr=(chirr*delta**power-2*chir*power*delta**(power-1)
             +chi*power*(power-1)*delta**(power-2))/self.bulk_scale
        B,Br,Brr=[self.bs(r,nu=k) for k in range(3)]
        bulk=np.stack([v[:,None]*B,vr[:,None]*B+v[:,None]*Br,
            vrr[:,None]*B+2*vr[:,None]*Br+v[:,None]*Brr],axis=2)
        data["new_columns"]=np.concatenate([fields[:,1:,:],
            np.tile(bulk,(1,self.nm,1))],axis=1)
        theta=data["theta"]
        data["column_cos"]=np.cos(self.column_modes[:,None]*theta)
        data["column_sin"]=np.sin(self.column_modes[:,None]*theta)
        data["weak_cos"]=np.cos(MODES[:,None]*theta)
        data["weak_sin"]=np.sin(MODES[:,None]*theta)
        data["core_all_cos"]=np.cos(CORE_MODES[:,None]*theta)
        data["core_all_sin"]=np.sin(CORE_MODES[:,None]*theta)
        dr=np.empty_like(r)
        dr[0],dr[-1]=(r[1]-r[0])/2,(r[-1]-r[-2])/2
        dr[1:-1]=(r[2:]-r[:-2])/2
        data["weak_row_units"]=np.sqrt(dr/dr.sum())[:,None]/MODES[None,:]**2
        cg,cgr,cgrr=base.step2((r-CORE_LEFT)/(CORE_RIGHT-CORE_LEFT))
        cgr/=CORE_RIGHT-CORE_LEFT
        cgrr/=(CORE_RIGHT-CORE_LEFT)**2
        unit=self.core_k*power
        data["core_radial"]=np.stack([
            cg*delta**power/unit,
            (cgr*delta**power-cg*power*delta**(power-1))/unit,
            (cgrr*delta**power-2*cgr*power*delta**(power-1)
             +cg*power*(power-1)*delta**(power-2))/unit],axis=1)
        data["paid_height_cache"]={}
        self.cache[key]=data
        return data

    def core_trace(self,q,amplitude):
        """R602 coefficients on one fixed512 quadrature, independent of r/theta grids."""
        key=(np.asarray(q).dtype.str,np.asarray(q).tobytes(),float(amplitude))
        if key==self.trace_key:
            return self.trace_cached
        COUNTS["core_completion_evaluations"]+=1
        coeff=np.zeros(self.nm,dtype=np.result_type(q,float))
        coeff[:4]=amplitude*np.r_[1.,self.paidq[1:4]]
        coeff[1:]+=amplitude*q[1:self.nm]
        pc=-(MODES**2-1)/self.par.R*coeff
        force_coefficient=amplitude**2*self.paidq[-1]
        pc[1]+=force_coefficient*(-15*self.old.forced.Acore/(self.par.R*self.old.forced.scale))
        P=pc@self.core_co
        Pt=-(pc*MODES)@self.core_si
        Ptt=-(pc*MODES**2)@self.core_co
        reference=float(np.max(np.real(-2*P)))
        left,right=0.,2.
        for _ in range(56):
            middle=(left+right)/2
            value=np.mean(1/np.sqrt(middle+reference+2*np.real(P)))
            if value>1:
                left=middle
            else:
                right=middle
        e=np.asarray((left+right)/2+reference,dtype=np.result_type(q,float)).item()
        for _ in range(3):
            u=np.sqrt(e+2*P)
            e+=2*(np.mean(1/u)-1)/np.mean(u**-3)
        u=np.sqrt(e+2*P)
        if not np.all(np.isfinite(u)) or np.min(np.real(u*u))<=1e-12:
            raise base.DomainError("dependent core turning root lost positivity")
        al=self.par.alpha/(1+self.par.alpha)
        bulk=q[self.nm:].reshape(self.nm,self.nb)@self.core_B
        prc=-al/self.par.R*MODES**2*pc
        prc+=amplitude*self.core_k*(self.par.alpha+2)/self.bulk_scale*bulk
        prc[1]+=force_coefficient*self.core_forced_source/self.par.R
        S=np.mean(Pt*Pt)
        target=(al*(e+2*P)*Ptt-Pt*Pt+(2*al+1)*S)/self.par.R
        target_coeff=2*(self.core_all_co@target)/CORE_QUADRATURE
        original=np.zeros(len(CORE_MODES),dtype=np.result_type(q,float))
        original[:self.nm]=prc
        cc=target_coeff-original
        result={"pc":pc,"prc":prc,"e":e,"P":P,"Pt":Pt,"Ptt":Ptt,"u":u,
            "S":S,"target_coeff":target_coeff,"cc":cc,
            "fixed_core_quadrature_turning_error":np.mean(1/u)-1,
            "projected_target_mean_error":np.mean(target),
            "expected_er":-2*(2*al+1)*S/self.par.R}
        self.trace_key,self.trace_cached=key,result
        return result

    def frozen_paid_canonical_height(self,amplitude,data):
        """Same paid pre-tanh coefficients; one fixed512 mean and its derivatives.

        Every radial field is already available in data. No ODE/seed/old
        geometry is called here. The force remains a separate post-tanh term.
        """
        COUNTS["paid_canonical_height_cache_builds"]+=1
        old_count=len(base.MODES)
        coefficient=amplitude*np.r_[1.,self.paidq[1:old_count]]
        bulk_coefficient=amplitude*self.paidq[old_count:self.old.original_nq].reshape(old_count,self.old.nb)
        radial=data["fields"]*coefficient[None,:,None]
        radial+=np.einsum("rbk,jb->rjk",data["bulk"],bulk_coefficient)
        key=(data["r"].tobytes(),float(amplitude))
        same_grid=(len(data["theta"])==CORE_QUADRATURE
            and np.array_equal(data["theta"],self.core_theta))

        def raw(co,si,angular):
            COUNTS["paid_frozen_tanh_grid_evaluations"]+=1
            COUNTS["paid_frozen_tanh_points"]+=int(len(data["r"])*co.shape[1])
            value=radial[:,:,0]@co
            vr,vrr=radial[:,:,1]@co,radial[:,:,2]@co
            scale=self.args.height_saturation
            th=np.tanh(value/scale)
            d1=1-th*th
            d2=-2*th*d1/scale
            answer=[scale*th,d1*vr,d1*vrr+d2*vr*vr]
            if angular:
                j=np.asarray(base.MODES)
                vt=-(radial[:,:,0]*j)@si
                vtt=-(radial[:,:,0]*j*j)@co
                vrt=-(radial[:,:,1]*j)@si
                answer.extend([d1*vt,d1*vtt+d2*vt*vt,d1*vrt+d2*vr*vt])
            return answer

        current=None
        if key not in self.canonical_mean_cache:
            canonical=raw(self.core_co[:old_count],self.core_si[:old_count],same_grid)
            means=np.stack([np.mean(v,axis=1) for v in canonical[:3]],axis=1)
            self.canonical_mean_cache[key]=means
            COUNTS["paid_canonical_mean_functions"]+=1
            COUNTS["paid_canonical_mean_points_subset_of_tanh_points"]+=int(len(data["r"])*CORE_QUADRATURE)
            if same_grid:
                current=canonical
        means=self.canonical_mean_cache[key]
        if current is None:
            current=raw(data["cos"],data["sin"],True)
        observed=np.stack([np.mean(v,axis=1) for v in current[:3]],axis=1)-means
        group=self.canonical_mean_observations.setdefault(str(len(data["theta"])),{
            "radial_array_evaluations":0,"radial_points":0,
            "new_minus_same_grid_mean_height_jet_maxima":[None,None,None]})
        group["radial_array_evaluations"]+=1
        group["radial_points"]+=int(len(data["r"]))
        for derivative in range(3):
            at=int(np.argmax(abs(observed[:,derivative])))
            previous=group["new_minus_same_grid_mean_height_jet_maxima"][derivative]
            value=float(observed[at,derivative])
            if previous is None or abs(value)>previous["absolute_value"]:
                group["new_minus_same_grid_mean_height_jet_maxima"][derivative]={
                    "radial_derivative_order":derivative,"absolute_value":abs(value),
                    "signed_value":value,"r":float(data["r"][at]),"amplitude":float(amplitude)}
            current[derivative]=current[derivative]-means[:,derivative,None]
        force=amplitude*amplitude*self.paidq[self.old.original_nq]
        G,Gr,Grr=data["forced_j4"].T
        co,si=data["forced_cos4"],data["forced_sin4"]
        addition=(G[:,None]*co,Gr[:,None]*co,Grr[:,None]*co,
            -4*G[:,None]*si,-16*G[:,None]*co,-4*Gr[:,None]*si)
        return tuple(a+force*b for a,b in zip(current,addition))

    def height_jets(self,q,amplitude,data):
        cache=data["paid_height_cache"]
        if float(amplitude) not in cache:
            cache[float(amplitude)]=self.frozen_paid_canonical_height(amplitude,data)
        plain=self.delta_jets(q,amplitude,data)
        trace=self.core_trace(q,amplitude)
        cc=trace["cc"]
        co,si,mm=data["core_all_cos"],data["core_all_sin"],CORE_MODES
        C=cc@co
        Ct=-(cc*mm)@si
        Ctt=-(cc*mm*mm)@co
        v,vr,vrr=data["core_radial"].T
        correction=(v[:,None]*C,vr[:,None]*C,vrr[:,None]*C,
            v[:,None]*Ct,v[:,None]*Ctt,vr[:,None]*Ct)
        return tuple(a+b+c for a,b,c in zip(cache[float(amplitude)],plain,correction))

    def correction_derivative(self,q,amplitude,dpc,dpr_bulk):
        """Derivative of the actual coefficient map, including the implicit core root."""
        trace=self.core_trace(q,amplitude)
        dP=self.core_co.T@dpc
        dPt=-self.core_si.T@(MODES[:,None]*dpc)
        dPtt=-self.core_co.T@(MODES[:,None]**2*dpc)
        de=-2*np.mean(dP/trace["u"][:,None]**3,axis=0)/np.mean(trace["u"]**-3)
        dS=2*np.mean(trace["Pt"][:,None]*dPt,axis=0)
        al=self.par.alpha/(1+self.par.alpha)
        dt=(al*((de[None,:]+2*dP)*trace["Ptt"][:,None]
                  +(trace["e"]+2*trace["P"])[:,None]*dPtt)
             -2*trace["Pt"][:,None]*dPt+(2*al+1)*dS[None,:])/self.par.R
        dcc=2*(self.core_all_co@dt)/CORE_QUADRATURE
        dpr_original=-al/self.par.R*MODES[:,None]**2*dpc+dpr_bulk
        dcc[:self.nm]-=dpr_original
        return dcc

    def core_state(self,q,amplitude,theta):
        COUNTS["core_full_residual_evaluations"]+=1
        trace=self.core_trace(q,amplitude)
        co,si=np.cos(MODES[:,None]*theta),np.sin(MODES[:,None]*theta)
        allco=np.cos(CORE_MODES[:,None]*theta)
        P=trace["pc"]@co
        Pt=-(trace["pc"]*MODES)@si
        Ptt=-(trace["pc"]*MODES**2)@co
        Pr=trace["prc"]@co+trace["cc"]@allco
        e=trace["e"];u=np.sqrt(e+2*P)
        if np.min(np.real(u*u))<=1e-12:
            raise base.DomainError("full core observation left its positive domain")
        al=self.par.alpha/(1+self.par.alpha)
        At=-self.par.R*Pr+al*(e+2*P)*Ptt-Pt*Pt
        er=-2*(np.mean(Pr/u**3)+np.mean(Ptt/u)/(self.par.R*(1+self.par.alpha)))/np.mean(u**-3)
        D=At-self.par.R*er/2
        return {"P":P,"Pt":Pt,"Ptt":Ptt,"Pr":Pr,"e":e,"u":u,"At":At,
            "er":er,"D":D,"weak":At@allco.T/(len(theta)*self.par.R),
            "pc":trace["pc"],"cc":trace["cc"],
            "turning_error":np.mean(1/u)-1,
            "expected_er":trace["expected_er"],
            "fixed_core_quadrature_turning_error":trace["fixed_core_quadrature_turning_error"],
            "projected_target_mean_error":trace["projected_target_mean_error"]}

    def evaluate(self,q,amplitude,data):
        check(self.deadline)
        COUNTS["weak_evaluations"]+=1
        g=self.geometry(q,amplitude,data,details=True)
        if np.min(np.real(g["Z"]))<=0:
            raise base.DomainError("reflected halves lost positive sampled height")
        r=data["r"][:,None]
        f,fr,frr,ft,ftt,frt=self.height_jets(q,amplitude,data)
        dh=q[0]-self.par.gain_height
        w=(data["w0"]+dh*data["gain_w"])[:,None]
        wr=(data["wr0"]+dh*data["gain_wr"])[:,None]
        E,e,p,b,N,u=[g[k] for k in ("E","e","p","b","N","u")]
        M=b**3*N/(r*r)
        B=frt-ft/r
        At=(-r*w*frr-r*wr*fr-e*wr*ftt+E*frr*ftt
            -w*wr*fr*ftt-E*B*B+r*fr*frr+w*wr*ft*ft/r)
        rows=(At/M)@data["weak_cos"].T/len(data["theta"])
        core=self.core_state(q,amplitude,data["theta"])
        vector=(rows*data["weak_row_units"]/amplitude).ravel()
        if not np.all(np.isfinite(vector)):
            raise base.DomainError("nonfinite complete eleven-mode weak residual")
        return {"q":q.copy(),"g":g,"f":f,"fr":fr,"frr":frr,"ft":ft,"ftt":ftt,"frt":frt,
            "w":w,"wr":wr,"M":M,"B":B,"At":At,"weak":rows,"core":core,"residual":vector}

    def jacobian(self,q,amplitude,data,state):
        check(self.deadline)
        COUNTS["analytic_jacobians"]+=1
        nr,nt=len(data["r"]),len(data["theta"])
        J=np.empty((nr*self.nm,self.nq))
        r=data["r"][:,None,None]
        g=state["g"]
        p,b,N,u,E,e=[g[k][:,:,None] for k in ("p","b","N","u","E","e")]
        w,wr,fr,frr,ft,ftt,B,M,At=[state[k][:,:,None] for k in
            ("w","wr","fr","frr","ft","ftt","B","M","At")]
        denominator=np.mean(N/u**3,axis=1,keepdims=True)
        co=data["weak_cos"]
        for first in range(0,self.nq,16):
            check(self.deadline)
            indices=np.arange(first,min(self.nq,first+16));nc=len(indices)
            jets=[np.zeros((nr,nt,nc)) for _ in range(6)]
            dw,dwr=np.zeros((nr,1,nc)),np.zeros((nr,1,nc))
            dpc,dpr_bulk=np.zeros((self.nm,nc)),np.zeros((self.nm,nc))
            for local,index in enumerate(indices):
                if index==0:
                    dw[:,0,local],dwr[:,0,local]=data["gain_w"],data["gain_wr"]
                    continue
                col=index-1
                fields=amplitude*data["new_columns"][:,col,:]
                c,s,j=data["column_cos"][col],data["column_sin"][col],self.column_modes[col]
                values=(fields[:,0,None]*c,fields[:,1,None]*c,fields[:,2,None]*c,
                    -j*fields[:,0,None]*s,-j*j*fields[:,0,None]*c,-j*fields[:,1,None]*s)
                for target,value in zip(jets,values):
                    target[:,:,local]=value
                if index<self.nm:
                    dpc[index,local]=-(MODES[index]**2-1)/self.par.R*amplitude
                else:
                    mode,bsindex=divmod(index-self.nm,self.nb)
                    dpr_bulk[mode,local]=amplitude*self.core_k*(self.par.alpha+2)/self.bulk_scale*self.core_B[bsindex]
            dcc=self.correction_derivative(q,amplitude,dpc,dpr_bulk)
            dC=data["core_all_cos"].T@dcc
            dCt=-data["core_all_sin"].T@(CORE_MODES[:,None]*dcc)
            dCtt=-data["core_all_cos"].T@(CORE_MODES[:,None]**2*dcc)
            v,vr,vrr=data["core_radial"].T
            extras=(v[:,None,None]*dC,vr[:,None,None]*dC,vrr[:,None,None]*dC,
                v[:,None,None]*dCt,v[:,None,None]*dCtt,vr[:,None,None]*dCt)
            for target,value in zip(jets,extras):
                target+=value
            _,dfr,dfrr,dft,dftt,dfrt=jets
            dp=-dw+dfr
            dN=(r*ft*dft/b**3+r*r*(ftt*dp+p*dftt)/b**3
                +3*r*r*p*ftt*ft*dft/b**5)
            dshift=(-2*dw*fr-2*w*dfr+2*fr*dfr
                +2*p*dp*ft*ft/b**2+2*p*p*ft*dft/b**2+2*p*p*ft**3*dft/b**4)
            de=(2*np.mean(dN/u,axis=1,keepdims=True)
                +np.mean(N*dshift/u**3,axis=1,keepdims=True))/denominator
            dE=2*w*dw+de
            dM=ftt*dp+p*dftt-2*ft*dft/r
            dB=dfrt-dft/r
            dAt=(-r*(dw*frr+w*dfrr)-r*(dwr*fr+wr*dfr)
                -de*wr*ftt-e*dwr*ftt-e*wr*dftt
                +dE*frr*ftt+E*dfrr*ftt+E*frr*dftt
                -(dw*wr+w*dwr)*fr*ftt-w*wr*dfr*ftt-w*wr*fr*dftt
                -dE*B*B-2*E*B*dB+r*(dfr*frr+fr*dfrr)
                +(dw*wr+w*dwr)*ft*ft/r+2*w*wr*ft*dft/r)
            dweak=np.einsum("rtp,jt->rjp",dAt/M-At*dM/M**2,co)/nt
            J[:,indices]=(dweak*data["weak_row_units"][:,:,None]/amplitude).reshape(-1,nc)
            COUNTS["analytic_columns"]+=nc
        if not np.all(np.isfinite(J)):
            raise ArithmeticError("nonfinite complete-height dependent-core Jacobian")
        return J


def mass_report(model,state,data):
    COUNTS["mass_eigenvalue_observations"] += 1
    r = data["r"][:,None]
    g = state["g"]
    aa = g["E"]*state["ftt"]+r*g["p"]
    coefficient = aa/state["M"]
    co = data["weak_cos"]
    mass = np.einsum("rt,it,jt->rij",coefficient,co,co)/len(data["theta"])
    eig = np.linalg.eigvalsh(mass)
    abs_eig = abs(eig)
    relative = np.min(abs_eig,axis=1)/np.maximum(np.max(abs_eig,axis=1),1e-300)
    where = np.unravel_index(int(np.argmax(aa)),aa.shape)
    worst = int(np.argmin(relative))
    return {"pointwise_a_min":float(np.min(aa)),"pointwise_a_max":float(np.max(aa)),
            "a_max_attainer":[float(data["r"][where[0]]),float(data["theta"][where[1]])],
            "nonnegative_a_node_count":int(np.sum(aa>=0)),
            "actual_weak_mass_smallest_relative_singular_value":float(relative[worst]),
            "weak_mass_worst_radius":float(data["r"][worst]),
            "weak_mass_worst_eigenvalues":eig[worst].tolist(),
            "sampled_weak_mass_rank_min_at_relative_1e_12":int(np.min(np.sum(
                abs_eig>1e-12*np.max(abs_eig,axis=1,keepdims=True),axis=1))),
            "pointwise_a_not_divided":True,"continuous_sign_or_rank_certificate":False}


def core_report(state,theta):
    c=state["core"]
    rows=[]
    for j in range(0,int(CORE_MODES[-1])+5,2):
        value=np.mean(c["D"]*np.cos(j*theta))*(1 if j==0 else 2)
        rows.append({"mode":j,"D_coefficient":float(value)})
    return {"P_cosine_coefficients":c["pc"].tolist(),
        "dependent_height_correction_coefficients":c["cc"].tolist(),
        "dependent_correction_modes":CORE_MODES.tolist(),
        "eR":float(c["e"]),"erR":float(c["er"]),"expected_R602_erR":float(c["expected_er"]),
        "erR_minus_R602_formula":float(c["er"]-c["expected_er"]),
        "uR_min":float(np.min(c["u"])),"complete_core_D_max":float(np.max(abs(c["D"]))),
        "complete_core_D_harmonics":rows,"core_weak_rows":c["weak"].tolist(),
        "turning_error":float(c["turning_error"]),
        "fixed512_turning_error":float(c["fixed_core_quadrature_turning_error"]),
        "target_polynomial_mean_roundoff_observation":float(c["projected_target_mean_error"]),
        "mean_weighted_D":float(np.mean(c["D"]/c["u"]**3)),
        "finite_core_formula_not_R_minus_epsilon":True,
        "complete_height_correction_used_in_body":True,
        "continuous_core_integral_or_roundoff_certificate":False}


def checkpoint(model,q,amp,data,state,iteration,damping,status):
    model.actual_checkpoint={"q":q.copy(),"amplitude":amp,"iteration":iteration,
        "damping":damping,"status":status,"new_scope_initial_not_old_qualification":iteration==120}
    report=knot.compact_report(q,amp,data,state["g"])
    report.update({"iteration":iteration,"actual_next_damping":damping,"status":status,
        "actual_correction_q":q.tolist(),"q_identity":weak.identity(q),
        "weak_merit":float(state["residual"]@state["residual"]/2),
        "body_weak_mode_order":MODES.tolist(),
        "body_weak_max_by_mode":np.max(abs(state["weak"]),axis=0).tolist(),
        "mass":mass_report(model,state,data),"core":core_report(state,data["theta"])})
    emit("CORE_COMPLETED_COMPLETE_STATE",report)
    return report


def new_chain_observation(model,q,amplitude,data,J):
    """One new derivative check of the newly added core/high-mode map, in this run."""
    direction=.001*np.cos(np.arange(model.nq)*.713)
    h=1e-25
    state=model.evaluate(q.astype(complex)+1j*h*direction,amplitude,data)
    actual=np.imag(state["residual"])/h
    predicted=J@direction
    relative=np.linalg.norm(actual-predicted)/max(1e-100,np.linalg.norm(actual))
    COUNTS["new_chain_direction_observations"]+=1
    emit("CORE_COMPLETED_NEW_CHAIN_DIRECTION",{
        "relative_l2_difference":float(relative),
        "absolute_max_difference":float(np.max(abs(actual-predicted))),
        "new_implicit_core_root_and_all_six_height_jets_included":True,
        "all_eleven_body_modes_and_existing_nonzero_residual_retained":True,
        "old_operator_direction_gate_replayed":False})
    if not relative<3e-5:
        raise ArithmeticError("new dependent-core/high-mode analytic derivative failed")
    model.new_direction_observed=True


def solve(model,q,amplitude,damping,data,args,deadline):
    q=q.copy()
    state=model.evaluate(q,amplitude,data)
    report=checkpoint(model,q,amplitude,data,state,120,damping,
                      "actual_new_scope_initial_with_dependent_core_height")
    status="declared_new_space_sixty_iteration_limit"
    for local_iteration in range(args.iterations):
        iteration=120+local_iteration
        check(deadline)
        if report["eta_max"]<=args.target_eta:
            status="active_metric_target_requires_complete_fine_readout"
            break
        residual=state["residual"]
        objective=.5*float(residual@residual)
        J=model.jacobian(q,amplitude,data,state)
        if not model.new_direction_observed:
            new_chain_observation(model,q,amplitude,data,J)
        column_norms=np.linalg.norm(J,axis=0)
        scales=np.maximum(column_norms,1e-12)
        Js=J/scales
        U,s,Vt=np.linalg.svd(Js,full_matrices=False)
        COUNTS["svd_factorizations"]+=1
        threshold=max(Js.shape)*np.finfo(float).eps*s[0]
        spectrum={"singular_max":float(s[0]),"singular_min":float(s[-1]),
            "reported_rank":int(np.sum(s>threshold)),"rank_threshold":float(threshold),
            "column_norm_min":float(np.min(column_norms)),
            "column_norm_max":float(np.max(column_norms)),
            "columns_below_scale_floor":int(np.sum(column_norms<1e-12)),
            "scaled_gradient_inf":float(np.max(abs(Js.T@residual))),
            "all_singular_directions_retained":True,"normal_equations_not_formed":True}
        ur=U.T@residual
        accepted=False
        for trial in range(8):
            check(deadline)
            lam=damping*10.**trial
            direction=-(Vt.T@(s/(s*s+lam)*ur))/scales
            COUNTS["model_directions"]+=1
            factor,measures=parent.function_trial_limit(model,q,direction,amplitude,data,state["g"])
            direction*=factor
            linear=J@direction
            for cut in range(9):
                check(deadline)
                fraction=2.**(-cut)
                predicted=objective-.5*float((residual+fraction*linear)@(residual+fraction*linear))
                COUNTS["line_search_trials"]+=1
                try:
                    candidate_q=q+fraction*direction
                    candidate=model.evaluate(candidate_q,amplitude,data)
                    actual=objective-.5*float(candidate["residual"]@candidate["residual"])
                    drop=max(32*np.finfo(float).eps*objective,1e-30)
                    ratio=actual/predicted if predicted>0 else -np.inf
                    okay=actual>drop and predicted>0 and ratio>.01
                    reason="no_resolvable_complete_new_weak_decrease"
                except base.DomainError as exc:
                    okay=False
                    reason="domain:"+str(exc)
                if okay:
                    q,state=candidate_q,candidate
                    old_damping=damping
                    damping=max(1e-14,lam/3)
                    COUNTS["accepted_steps"]+=1
                    emit("CORE_COMPLETED_ACCEPTANCE",{
                        "iteration":iteration,"amplitude":amplitude,"trial":trial,"fraction":fraction,
                        "function_factor":factor,"function_measures":measures,
                        "damping_before":old_damping,"lambda_used":lam,
                        "actual_next_damping":damping,"actual_decrease":float(actual),
                        "predicted_decrease":float(predicted),"actual_over_predicted":float(ratio),
                        "spectrum":spectrum})
                    report=checkpoint(model,q,amplitude,data,state,iteration+1,damping,
                                      "actual_accepted_complete_new_weak_decrease")
                    accepted=True
                    break
                reject(reason)
            if accepted:
                break
        if not accepted:
            status="no_resolvable_step_in_declared_eleven_mode_core_completed_space"
            emit("CORE_COMPLETED_STALL",{
                "iteration":iteration,"q_identity":weak.identity(q),
                "actual_retained_q":q.tolist(),"actual_next_damping":damping,"spectrum":spectrum})
            break
    return q,state,damping,{"status":status,"last_report":report}


def fine_readout(model,q,amplitude,args):
    r=knot.radial_grid(model,2)
    data=model.prepare(r,2*args.theta_nodes)
    state=model.evaluate(q,amplitude,data)
    report=knot.compact_report(q,amplitude,data,state["g"])
    report.update(mass=mass_report(model,state,data),core=core_report(state,data["theta"]),
        body_weak_mode_order=MODES.tolist(),
        body_weak_max_by_mode=np.max(abs(state["weak"]),axis=0).tolist())
    weight=r[:,None]**2/(state["g"]["u"]**3*state["g"]["b"]**3)
    D=state["g"]["R"]/weight
    harmonics=[]
    for j in range(0,HARMONIC_MAX+1,2):
        values=(1 if j==0 else 2)*np.mean(D*np.cos(j*data["theta"])[None,:],axis=1)
        i=int(np.argmax(abs(values)))
        harmonics.append({"mode":j,"maximum_absolute_D_coefficient":float(abs(values[i])),
            "signed_coefficient":float(values[i]),"radius":float(r[i])})
    report["complete_D_harmonics"]=harmonics
    direct=resume.stencil_position_geometry(model,q,amplitude,r,2*args.theta_nodes)
    half=resume.stencil_position_geometry(model,q,amplitude,r,2*args.theta_nodes,.5)
    okay=(report["eta_max"]<=args.target_eta and report["sampled_height_min"]>0
        and direct["direct_position_outward_ratio_min"]>0
        and half["direct_position_outward_ratio_min"]>0
        and direct["direct_reconstructed_metric_eta"]<=args.target_eta
        and half["direct_reconstructed_metric_eta"]<=args.target_eta)
    return {"same_actual_q":weak.identity(q),"fine":report,
        "direct_step":direct,"direct_half_step":half,
        "fine_metric_observation_passed":bool(okay),
        "complete_body_harmonics_through":HARMONIC_MAX,
        "continuous_tail_core_integral_or_reach_certificate":False}


def high_progress(attempts):
    result=[]
    for field in attempts:
        result.append({"mode":getattr(field,"mode",None),
            "status":getattr(field,"status","constructor_not_started"),
            "completed_inner_RHS":getattr(field,"completed_inner_RHS",0),
            "completed_outer_RHS":getattr(field,"completed_outer_RHS",0),
            "completed_inward_extension_RHS":getattr(field,"completed_inward_extension_RHS",0),
            "constructor_elapsed_seconds":(
                getattr(field,"finite_inner_data",{}).get("elapsed_seconds")
                if getattr(field,"status","")=="new_mode_dense_field_completed"
                else time.monotonic()-getattr(field,"started",time.monotonic())),
            "an_unfinished_integrator_scope_has_unknown_additional_RHS":
                getattr(field,"status","")!="new_mode_dense_field_completed"})
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json",required=True)
    parser.add_argument("--source-state-sha256",required=True)
    parser.add_argument("--maximum-seconds",type=float,default=2400.)
    parser.add_argument("--M",type=int,choices=[25],default=25)
    parser.add_argument("--rtol",type=float,default=2e-11)
    parser.add_argument("--atol",type=float,default=2e-13)
    parser.add_argument("--iterations",type=int,choices=[60],default=60)
    parser.add_argument("--theta-nodes",type=int,choices=[256],default=256)
    parser.add_argument("--target-eta",type=float,default=2e-9)
    parser.add_argument("--height-saturation",type=float,choices=[.15],default=.15)
    args=parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS")!="true" or
            os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("science executes only in the declared public Actions job")
    if not 60<args.maximum_seconds<=2400 or args.rtol!=2e-11 or args.atol!=2e-13:
        raise ValueError("declared actual input tolerances or clock changed")
    started=time.monotonic()
    deadline=started+args.maximum_seconds
    source,paidq,amplitude,damping,input_sha=input_state(args)
    q=expanded_paid_q(paidq,61)
    model,summary,readout=None,None,None
    high_attempts=[]
    status="new_input_before_necessary_reconstruction"
    emit("CORE_COMPLETED_DEFINITION",{
        "schema":SCHEMA,"source_state":source,"source_state_sha256":input_sha,
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "new_input_q":q.tolist(),"new_input_q_identity":weak.identity(q),
        "source_496q_identity":weak.identity(paidq),"initial_actual_damping":damping,
        "source_global_accepted_iteration":120,
        "body_weak_modes":MODES.tolist(),"new_true_flat_modes":list(high.DECLARED_NEW_MODES),
        "dependent_core_height_modes":CORE_MODES.tolist(),
        "fixed_core_quadrature_count":CORE_QUADRATURE,"core_correction_onset":[CORE_LEFT,CORE_RIGHT],
        "old_paid_base265q_and_all496q_coefficients_preserved":True,
        "old_pre_tanh_fields_retained_but_same_grid_mean_replaced_by_fixed512":True,
        "fixed512_mean_radial_derivatives_from_the_same_frozen_function":True,
        "old_grid_to_canonical_mean_changes_actual_radial_height_constant":True,
        "old_all67_knots_and_all_original_radial_points_preserved":True,
        "new_core_correction_changes_actual_height_and_full_Jacobian":True,
        "core_rows_not_merely_zeroed_or_removed_from_old_physics":True,
        "new_inner_modes_only_no_old_low_mode_Riccati_repeated":True,
        "necessary_dense_core_and_height_reconstruction_charged":True,
        "new_Jacobian_chain_observation_in_same_run_only":True,
        "old_operator_parity_or_direction_gate_replayed":False,
        "fixed_g_finite_solution_or_README_completion_claim":False})
    try:
        paid_model=resume.restore_model(source,args,deadline)
        if paid_model.nq!=496 or paid_model.nb!=61:
            raise ValueError("the complete paid height and basis did not reconstruct")
        modes=list(paid_model.modes)
        for j in high.DECLARED_NEW_MODES:
            check(deadline)
            flat=high.FactoredFlatSeed.__new__(high.FactoredFlatSeed)
            high_attempts.append(flat)
            flat.__init__(j,args,base,deadline,paid_model.minimum)
            before_connector=base.COUNTS["connector_RHS"]
            before_core=base.COUNTS["core_basis_RHS"]
            mode=base.AdmissibleMode(flat,paid_model.par,args)
            modes.append(mode)
            emit("CORE_COMPLETED_NEW_TRUE_MODE",{
                "mode":j,"finite_inner_data":flat.finite_inner_data,
                "core_and_explicit_match":mode.receipt(),
                "new_connector_RHS":base.COUNTS["connector_RHS"]-before_connector,
                "new_core_RHS":base.COUNTS["core_basis_RHS"]-before_core,
                "no_old_mode_inner_problem_repeated":True})
        model=CompletedCoreHeight(paid_model,modes,args,deadline)
        if model.nq!=682 or model.minimum!=paid_model.minimum:
            raise ValueError("new scope dimensions or paid common inner radius changed")
        model.actual_checkpoint={"q":q.copy(),"amplitude":amplitude,"iteration":120,
            "damping":damping,"status":"declared_new_input_before_first_evaluation",
            "new_scope_initial_not_old_qualification":True}
        r=knot.radial_grid(model,1)
        data=model.prepare(r,args.theta_nodes)
        q,state,damping,summary=solve(model,q,amplitude,damping,data,args,deadline)
        readout=fine_readout(model,q,amplitude,args)
        status=summary["status"]
        emit("CORE_COMPLETED_STAGE",{"amplitude":amplitude,"summary":summary,"readout":readout,
            "actual_correction_q":q.tolist(),"actual_q_identity":weak.identity(q),
            "actual_next_damping":damping})
    except (weak.ScientificBudget,paid.ScientificBudget,high.HighModeBudget) as exc:
        status="declared_scientific_budget_checkpoint"
        emit("CORE_COMPLETED_CLOCK",{"message":str(exc),"actual_retained_state_preserved":True})
    except (base.DomainError,ArithmeticError,ValueError,FloatingPointError,np.linalg.LinAlgError) as exc:
        status="declared_model_or_numerical_failure"
        emit("CORE_COMPLETED_FAILURE",{"type":type(exc).__name__,"message":str(exc)})
    actual_checkpoint=None
    if model is not None and model.actual_checkpoint is not None:
        keep=model.actual_checkpoint
        q=keep["q"].copy();amplitude=keep["amplitude"];damping=keep["damping"]
        actual_checkpoint={k:v for k,v in keep.items() if k!="q"}
    final={"schema":SCHEMA,"status":status,"elapsed_seconds":time.monotonic()-started,
        "actual_retained_amplitude":amplitude,"actual_retained_q":q.tolist(),
        "actual_retained_q_identity":weak.identity(q),"actual_next_damping":damping,
        "actual_complete_checkpoint":actual_checkpoint,"model_constructed":model is not None,
        "summary":summary,"readout":readout,"high_mode_attempts":high_progress(high_attempts),
        "canonical_paid_tanh_mean_observations":None if model is None else model.canonical_mean_observations,
        "canonical_mean_defines_one_radial_function_independent_of_observation_theta":True,
        "source_cost_not_counted_as_this_run":source["source_cost_ledger"],
        "earlier_source_cost_not_counted_as_this_run":source["prior_source_cost_ledger"],
        "new_counts":dict(COUNTS),"new_high_mode_counts":dict(high.COUNTS),
        "base_counts":base.COUNTS,"forced_counts":paid.NEW_COUNTS,
        "function_counts":parent.EXTRA,"gain_counts":base.gain.COUNTS,
        "paid_mouth_and_position_counts":resume.NEW,"old_weak_helper_counts":weak.COUNTS,
        "rejections":REJECTIONS,
        "new_counts_overlap_base_counts_do_not_sum_them_as_disjoint_work":True,
        "old_inner_H_shooting_or_old_direction_gate_repeated":False,
        "continuous_metric_curvature_reach_or_README_completion_claim":False,
        "raw_arrays_artifacts_releases_or_git_writes":False}
    raw=json.dumps(final,sort_keys=True,separators=(",",":"),allow_nan=False)
    print("CORE_COMPLETED_FINAL "+raw,flush=True)
    emit("CORE_COMPLETED_FINAL_IDENTITY",{"JSON_bytes":len(raw.encode()),
        "sha256":hashlib.sha256(raw.encode()).hexdigest()})


if __name__=="__main__":
    main()

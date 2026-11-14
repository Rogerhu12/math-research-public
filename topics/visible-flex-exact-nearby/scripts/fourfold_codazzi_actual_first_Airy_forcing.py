#!/usr/bin/env python3
"""Actual complete first Airy forcing from original intrinsic third jets.

Read only completed root rows, original complete cubic shards and six
completed body-jet parts. No target, ray or response solve is rerun.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction as Q
from functools import lru_cache
import gzip,hashlib,json,math,os,shutil,sys,time
from pathlib import Path
import numpy as np
import flint
from flint import arb,ctx
import fourfold_codazzi_piecewise_real_root_fold_resume_v2 as old

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby"
ROOT_SHA="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
ROOT_BYTES=5923431
ROOT_RUN="43616813816"
BODY_SOURCE="1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07"
DELTA=Q(1,100000000)
WIDTHS=(Q(1,16),Q(1,32))
ex,box,rec,up,power=old.ex,old.box,old.rec,old.up,old.power
read,save,sha=old.read,old.save,old.sha
ZERO=arb(0)

def upper(x):return arb(x).upper()
def maxup(values):return max((up(v) for v in values),default=arb(0)).upper()
def encode(d):return {str(k):([rec(x) for x in v] if isinstance(v,list) else rec(v)) for k,v in d.items()}
def weight(values,start,width,angular=0):
    return old.weighted(values,[4*j for j in range(start,start+len(values))],width,angular)

def restricted_jets(row,name,left,right):
    """True midpoint Taylor with the original whole ordinary third derivative."""
    a,b=map(Q,row["interval"]);mid=(a+b)/2
    if not a<=left<right<=b:raise ValueError("left the complete original intrinsic row")
    centre=row["intrinsic_midpoint_jets"];whole=row["intrinsic_whole_third_jets"]
    X=old.interval(left-mid,right-mid);result=[]
    for j in range(4):
        if j==3:
            result.append(box(whole[name+"3"]));continue
        value=sum((box(centre[name+(str(k) if k else "")])*X**(k-j)/math.factorial(k-j)
                   for k in range(j,3)),arb(0))
        value+=box(whole[name+"3"])*X**(3-j)/math.factorial(3-j)
        result.append(value)
    return result

def bell(n,k,values):
    @lru_cache(maxsize=None)
    def b(nn,kk):
        if nn==kk==0:return arb(1)
        if nn<=0 or kk<=0 or kk>nn:return arb(0)
        return sum((math.comb(nn-1,i-1)*values[i]*b(nn-i,kk-1)
                    for i in range(1,nn-kk+2)),arb(0))
    return upper(b(n,k))

KEY2=[(i,j) for i in range(3) for j in range(3-i)]
KEY3=[(i,j) for i in range(3) for j in range(4-i)]
def multiply(a,b,keys):
    return {(i,j):upper(sum((a.get((p,q),ZERO)*b.get((i-p,j-q),ZERO)
                    for p in range(i+1) for q in range(j+1)),arb(0))) for i,j in keys}
def normjet(d,keys=KEY2):
    return {key:upper(d.get(key,ZERO)/(math.factorial(key[0])*math.factorial(key[1]))) for key in keys}
def ordinary(d):
    return {key:upper(value*math.factorial(key[0])*math.factorial(key[1])) for key,value in d.items()}
def power_derivatives(A,p,amin,amax):
    da=normjet(A,KEY3);da[(0,0)]=ZERO
    powers={0:{(0,0):arb(1)}};out={(0,0):power(amax,p).upper()}
    coefficient=Q(1)
    for ell in range(1,4):
        powers[ell]=multiply(powers[ell-1],da,KEY3)
        coefficient*=Q(p-ell+1,ell)
        bound=ex(abs(coefficient))*power(amin if p-ell<0 else amax,p-ell)
        for key in KEY3:
            if key!=(0,0):out[key]=out.get(key,ZERO)+bound*powers[ell][key]
    return ordinary(out)

def full_leading_and_forcing(case,glob,seams,roots,check):
    """L.12--L.25: finite derivative calculus, including actual a_r seams."""
    values={k:box(v) for k,v in case["bounds"].items()}
    R=ex(Q(case["exact_radius"])+roots[1]-roots[0])
    am,ap=values["a_lower"],values["a_upper"]
    Am,Ap=values["A_lower"],values["A_upper"]
    km,kp=values["k_lower"],values["k_upper"]
    em,ep=values["eta_lower"],values["eta_upper"]
    G,Gi=values["leading_G"],values["leading_G_inverse"]
    D=glob["D"];Dr=glob["Dr"]
    E=(D[1]*R).exp().upper();j=(E-1).upper()
    h=(1-j).lower()
    check("all real leading rays fit the larger old-angle strip",
          E*(ex(Q(3,64))+values["positive_optical_integral"])<ex(Q(1,16)))
    check("the full forcing rays fit their actual smaller input strip",
          ex(Q(1,64))+values["whole_ray_displacement"]<ex(Q(5,128)))
    check("the full-family divided phase and root-frame gaps remain positive",
          Am>0 and km>0 and em>0 and h>0 and values["fold_noncharacteristic_gap"]>0)
    k1=glob["K_derivatives"][2]/2
    k2=glob["K_derivatives"][3]/3
    a1=(glob["eta_derivatives"][1]*kp.sqrt()+ep*k1/(2*km.sqrt())).upper()
    a2=(glob["eta_derivatives"][2]*kp.sqrt()
        +glob["eta_derivatives"][1]*k1/km.sqrt()
        +ep*(k2/(2*km.sqrt())+k1*k1/(4*power(km,Q(3,2))))).upper()
    C={1:E}
    for n in range(2,6):
        vals={1:E,**{t:R*C[t] for t in range(2,n)}}
        C[n]=(E*sum((D[k]*bell(n,k,vals) for k in range(2,n+1)),arb(0))).upper()
    X={1:E,**{n:(R*C[n]).upper() for n in range(2,6)}}
    ca={}
    for n in range(1,5):
        vals={1:E,**{t:R*C[t] for t in range(2,n+1)}}
        ca[n]=(ex(Q(3,5))*ap*sum((C[k+1]*bell(n,k,vals)
                                      for k in range(1,n+1)),arb(0))).upper()
    ag={0:Ap,**{n:(R*ca[n]).upper() for n in range(1,5)}}
    xr={}
    for n in range(1,4):
        xr[n]=(sum((math.comb(n,l)*D[l]*X[n-l+1] for l in range(n+1)),arb(0))
               +ex(Q(2,3))*ap*R*R*ag[n+1]).upper()
    xrr={}
    for n in (1,2):
        q=n+1
        rho2Ar=(R*R*sum((math.comb(q,l)*D[l]*ag[q-l+1] for l in range(q+1)),arb(0))
                 +ex(Q(3,2))*R*(ap*X[q+1]+ag[q])).upper()
        xrr[n]=(sum((math.comb(n,l)*(Dr[l]*X[n-l+1]+D[l]*xr[n-l+1])
                        for l in range(n+1)),arb(0))
                +ex(Q(2,3))*(a1*R*R*ag[n+1]+2*ap*R*ag[n+1]+ap*rho2Ar)).upper()
    P0=(D[0]*(1+E)).upper()
    P1=(2*D[1]*E+R*C[2]*D[0]).upper()
    P2=(D[2]*(E*E+E)+3*D[1]*R*C[2]+D[0]*R*C[3]).upper()
    P00=((1+E)*Dr[0]+D[1]*P0+D[0]*P1).upper()
    P11=(2*E*Dr[1]+D[2]*E*P0+2*D[1]*P1+D[0]*P2+R*C[2]*Dr[0]).upper()
    distances=[];meanjump=arb(0)
    for seam in seams:
        r=Q(seam["radial"])
        if r<roots[0]:distances.append(roots[0]-r)
        elif r>roots[1]:distances.append(r-roots[1])
        else:raise ValueError("a polynomial seam touches the genuine root enclosure")
        jump=seam["radial_derivatives"]["1"]
        meanjump+=ex(abs(Q(jump["base_even_mean_jump_exact"])))
        meanjump+=ex(DELTA*abs(Q(jump["direction_even_mean_jump_exact"])))
    hs=min(distances)
    Ja=(kp.sqrt()*glob["gamma_upper"]*meanjump).upper()
    seam20=(ex(Q(3,2))*E*Ja/ex(hs)).upper()
    seam21=(ex(Q(3,2))*C[2]*E*Ja).upper()
    check("all actual mean derivative seams have positive root distance",hs>0)
    A={(0,0):Ap,**{(0,n):ag[n] for n in (1,2,3)}}
    A[1,0]=(ex(Q(3,5))*a1*E+ex(Q(3,5))*ap*xr[1]+ap*X[2]*P0).upper()
    A[2,0]=(ex(Q(3,7))*a2*E+2*a1*(ex(Q(3,7))*xr[1]+ex(Q(3,5))*X[2]*P0)
        +ap*(ex(Q(3,7))*xrr[1]+ex(Q(6,5))*xr[2]*P0+X[3]*P0*P0+X[2]*P00)
        +seam20).upper()
    A[1,1]=(ex(Q(3,5))*a1*X[2]*E
        +ap*(ex(Q(3,5))*xr[2]*E+X[3]*P0*E+X[2]*P1)).upper()
    A[1,2]=(ex(Q(3,5))*a1*(X[3]*E*E+X[2]*R*C[2])
        +ap*(ex(Q(3,5))*xr[3]*E*E+X[4]*P0*E*E+2*X[3]*E*P1
             +ex(Q(3,5))*xr[2]*R*C[2]+X[3]*P0*R*C[2]+X[2]*P2)).upper()
    A[2,1]=(ex(Q(3,7))*a2*X[2]*E
        +2*a1*(ex(Q(3,7))*xr[2]*E+ex(Q(3,5))*X[3]*P0*E+ex(Q(3,5))*X[2]*P1)
        +ap*(ex(Q(3,7))*xrr[2]*E+ex(Q(6,5))*xr[3]*P0*E+X[4]*P0*P0*E
             +X[3]*P00*E+ex(Q(6,5))*xr[2]*P1+2*X[3]*P0*P1+X[2]*P11)
        +seam21).upper()
    log_r=(A[1,0]/(6*Am)+k1/(4*km)+glob["log_EG_r"]).upper()
    log_p=(A[0,1]/(6*Am)).upper()
    log_rr=((A[2,0]/Am+(A[1,0]/Am)**2)/6
            +(k2/km+(k1/km)**2)/4+glob["log_EG_rr"]).upper()
    log_rp=((A[1,1]/Am+A[1,0]*A[0,1]/Am**2)/6).upper()
    log_pp=((A[0,2]/Am+(A[0,1]/Am)**2)/6).upper()
    gd={(0,0):G,(1,0):G*log_r,(0,1):G*log_p,
        (2,0):G*(log_rr+log_r**2),(1,1):G*(log_rp+log_r*log_p),
        (0,2):G*(log_pp+log_p**2)}
    F=power_derivatives(A,Q(2,3),Am,Ap)
    td={(i,k):(R*F[i,k]+(i*F[i-1,k] if i else 0)).upper() for i,k in KEY2}
    tpd={(i,k):(R*F[i,k+1]+(i*F[i-1,k+1] if i else 0)).upper() for i,k in KEY2}
    xd={(0,0):X[1],(0,1):X[2],(0,2):X[3],
        (1,0):xr[1],(1,1):xr[2],(2,0):xrr[1]}
    gj,xj,tj,tpj=map(normjet,(gd,xd,td,tpd))
    xx=multiply(xj,xj,KEY2);tt=multiply(tj,multiply(tpj,tpj,KEY2),KEY2)
    a0=ordinary(multiply(gj,{k:xx[k]+tt[k] for k in KEY2},KEY2))
    b0=ordinary({k:2*v for k,v in multiply(gj,multiply(xj,tpj,KEY2),KEY2).items()})
    W={k:(a0[k]+b0[k]).upper() for k in KEY2}
    Tm=values["T_upper"];Tp=values["T_phi"];gap=values["fold_noncharacteristic_gap"]
    Hinv=((E+(1+Tm)*Tp)/gap).upper()
    DX=(ex(Q(2,3))*ap*R*R*ag[1]).upper()
    DT=(ap*power(Am,Q(-1,3))*E).upper()
    HD=(DX+(1+Tm)*DT).upper()
    force=((W[2,0]+2*D[0]*W[1,1]+(D[0]**2+ep**2*glob["K_derivatives"][0])*W[0,2]
        +(Dr[0]+D[0]*D[1])*W[0,1]
        +glob["T0"]*(W[1,0]+D[0]*W[0,1])
        +(glob["V0"]+glob["vartheta"]*Hinv*HD)*W[0,0])
        /values["principal_mu_abs_lower"]).upper()
    force1=(force/ex(Q(1,128))).upper()
    # F.7--F.16 with actual angular variational bounds, including final branches.
    cA1,cA2=ca[1],ca[2]
    cT1=(ex(Q(2,3))*power(Am,Q(-1,3))*cA1).upper()
    cT2=(ex(Q(2,3))*power(Am,Q(-1,3))*cA2
          +ex(Q(2,9))*power(Am,Q(-4,3))*cA1*cA1*R).upper()
    cY=(power(Ap,Q(1,3))*cT1).upper()
    cY1=(power(Ap,Q(1,3))*cT2+cT1*cT1*R/(2*power(Am,Q(1,3)))).upper()
    cH=(D[2]*(3*D[1]*R).exp()+cY1*power(R,Q(3,2))).upper()
    pstar=(ap*power(Am,Q(-1,3))*Gi/2).upper()
    K0=(pstar*E/h**2).upper()
    K1=(K0*(cA1/(2*Am)+3*cH/h)).upper()
    Kdiff=(2*pstar*cY*(3*E*E+cY*cY*R**5)/h**4).upper()
    B0=(G*E*E).upper();Bdiff=(4*G*E*cY).upper()
    M0=(K0*power(Am,Q(-1,3))).upper()
    M1=(power(Am,Q(-1,3))*K1+K0*power(Am,Q(-4,3))*cA1/3).upper()
    Mdiff=(power(Am,Q(-1,3))*Kdiff).upper()
    cchi=(ex(Q(4,3))*ap*E).upper()
    Aa=(B0*K0*R).upper()
    Ab0=((Bdiff*M0+B0*(Mdiff+M1*cchi)/6)*R**3).upper()
    Ab1=(ex(Q(3,4))*B0*M0*cchi*R**2).upper()
    Ba0=((Bdiff*K0+B0*(ex(Q(2,7))*Kdiff+ex(Q(3,14))*K1*cchi))
          *R**3/(2*power(Am,Q(1,3)))).upper()
    Ba1=(ex(Q(3,10))*B0*K0*cchi*R**2/power(Am,Q(1,3))).upper()
    Bb=(2*B0*K0*power(Am,Q(-2,3))).upper()
    aone=(Aa*force+Ab0*force+Ab1*force1).upper()
    bone=(Ba0*force+Ba1*force1+Bb*force).upper()
    check("the complete first forcing and both actual forced amplitudes are finite",
          all(v.is_finite() for v in (force,force1,aone,bone)))
    return dict(exact_radius=case["exact_radius"],exact_cover=case["exact_radial_cover"],
        exact_length_bound=str(Q(case["exact_radius"])+roots[1]-roots[0]),
        coefficient_strip="1/16",leading_strip="3/64",forcing_strip="5/128",output_strip="1/64",
        bound_type="analytic supremum, not same-width Wiener norm",
        leading_rays_imaginary_strip_upper=rec(E*(ex(Q(3,64))+values["positive_optical_integral"])),
        forcing_rays_old_angle_strip_upper=rec(ex(Q(1,64))+values["whole_ray_displacement"]),
        radial_a_derivatives=encode({"first":a1,"second":a2}),
        divided_curvature_derivatives=encode({"first":k1,"second":k2}),
        flow_variational_C=encode(C),A_angular_constants=encode(ca),
        A_mixed_derivative_bounds=encode({str(k):v for k,v in A.items()}),
        actual_original_mean_first_derivative_jump_sum=rec(meanjump),
        actual_minimum_seam_root_distance=str(hs),actual_a_first_derivative_jump_sum=rec(Ja),
        A_second_radial_seam_fee=rec(seam20),A_second_radial_first_angular_seam_fee=rec(seam21),
        leading_a0_derivative_bounds=encode({str(k):v for k,v in a0.items()}),
        leading_b0_derivative_bounds=encode({str(k):v for k,v in b0.items()}),
        matrix_H_inverse_l1=rec(Hinv),matrix_HD_l1=rec(HD),
        complete_actual_L0_v0_pair_sup=rec(force),complete_actual_L0_v0_pair_first_angular_sup=rec(force1),
        nonsingular_first_amplitude_coefficients=encode(dict(Aa=Aa,Ab0=Ab0,Ab1=Ab1,Ba0=Ba0,Ba1=Ba1,Bb=Bb)),
        actual_first_a_amplitude_sup=rec(aone),actual_first_b_amplitude_sup=rec(bone),
        common_next_root_trace="exactly zero",full_branch_factors_retained=True,
        first_forcing_is_the_complete_actual_degree_zero_operator=True,
        final_old_primitive_inverse_remainders_and_true_mean_still_required=True,
        actual_next_amplitude_state_seam_norms_evaluated=False,
        complete_strong_return_norm_evaluated=False,numerical_cutoff97_return_inverse_claimed=False)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--prepared",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--resume",type=Path)
    args=ap.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all scientific work must run in the actual public repository Actions")
    runtime={"python":".".join(map(str,sys.version_info[:3])),"numpy":np.__version__,"flint":flint.__version__}
    if runtime!={"python":"3.12.14","numpy":"2.3.5","flint":"0.9.0"}:
        raise RuntimeError("the exact directed runtime changed")
    if args.out.exists():raise FileExistsError("preserve every completed or failed first-forcing prefix")
    ctx.prec=256;started=time.monotonic();reused_complete=False
    report=dict(kind="actual_first_Airy_forcing_and_full_real_radial_inverse_jets_v1",
        complete=False,proved=False,failure=None,runtime=runtime,source_sha256=sha(__file__),
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        original_root_coefficients_and_target_rows_recomputed=0,
        full_original_193_direction_and_even_mean_retained=True,exact_real_delta_radius=str(DELTA),
        complete_strong_return_norm_evaluated=False,numerical_cutoff97_return_inverse_claimed=False,
        actual_PDE_branch_claimed=False,gates=[],rows=[],original_part_receipts=[])
    def check(name,truth):
        okay=bool(truth);report["gates"].append(dict(name=name,passed=okay))
        if not okay:raise ValueError("actual first-forcing gate failed: "+name)
    try:
        manifest=read(args.manifest)
        if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong authorized repository")
        paths={key:args.repo_root/rel for key,rel in manifest["input_paths"].items()}
        for entry in manifest["files"]:
            p=args.repo_root/entry["path"]
            if not p.is_file() or sha(p)!=entry["sha256"] or p.stat().st_size!=entry["bytes"]:
                raise ValueError("a pinned original file or scientific source changed: "+entry["path"])
        report["input_manifest_sha256"]=sha(args.manifest)
        shared=read(paths["intrinsic_parts"])
        if shared["original_source"]["sha256"]!=BODY_SOURCE:raise ValueError("wrong original jet producer")
        rootpath=args.prepared/"root"/"consumers"/"piecewise-real-root-fold-resumed-v2.json.gz"
        if sha(rootpath)!=ROOT_SHA or rootpath.stat().st_size!=ROOT_BYTES:
            raise ValueError("the complete original actual larger-root native differs")
        root=read(rootpath)
        check("the complete actual radius1over50 native and all1300 rows are reused",
            root["complete"] and root["proved"] and str(root["public_run_id"])==ROOT_RUN
            and root["source_sha256"]=="840d7ae96c023f0f1055516cfefe62f22a8f46a3f8a0ea2974553b32760eb112"
            and root["candidate_sha256"]==old.CANDIDATE and root["background_definition_sha256"]==old.BASE
            and root["explicit_direction_definition_sha256"]==old.ZDEF
            and root["selected"]["exact_radius"]=="1/50" and len(root["rows"])==1300
            and len(root["seams"])==1079 and all(g["passed"] for g in root["gates"]))
        roots=list(map(Q,root["exact_root_interval"]));left,right=map(Q,root["exact_cover"])
        check("the entire true explicit family lies outside compact intrinsic support",left>Q(9,50))
        original=[]
        for spec in shared["parts"]:
            p=args.prepared/spec["artifact"]/spec["inner_path"]
            if not p.is_file() or sha(p)!=spec["sha256"]:
                raise ValueError("an original whole body-jet part differs")
            doc=read(p)
            if (doc["kind"]!="actual_full_regular_joint_radial_polynomial_residual_rows_v1"
                or doc["complete"] is not False or doc["selected_cells_complete"] is not True
                or doc.get("failure") is not None or doc["identity"]!=shared["original_row_identity"]
                or doc["selected_indices"]!=spec["common_row_indices"] or len(doc["rows"])!=spec["rows"]):
                raise ValueError("an original row identity, whole eta box or completed range differs")
            if doc["rows"][0]["interval"][0]!=spec["exact_interval"][0] or doc["rows"][-1]["interval"][1]!=spec["exact_interval"][1]:
                raise ValueError("an original actual radial interval differs")
            for idx,row in enumerate(doc["rows"],spec["common_row_indices"][0]):
                if row["common_row"]!=idx:raise ValueError("original common-row order changed")
                a,b=map(Q,row["interval"])
                if a<right and b>left:original.append((a,b,row))
            report["original_part_receipts"].append(dict(artifact=spec["artifact"],inner_path=spec["inner_path"],
                sha256=spec["sha256"],actual_bytes=p.stat().st_size,complete_original_rows=len(doc["rows"])))
        original.sort(key=lambda x:x[0]);cursor=left
        for a,b,row in original:
            aa,bb=max(a,left),min(b,right)
            if aa!=cursor or not aa<bb:raise ValueError("the complete original intrinsic cover has a gap")
            cursor=bb
        check("all six original parts cover the exact real root interval without recomputation",cursor==right)
        previous=None
        if args.resume is not None:
            previous=read(args.resume)
            check("the saved first-forcing prefix has the identical source and all immutable inputs",
                previous.get("kind")==report["kind"]
                and previous.get("source_sha256")==sha(__file__)
                and previous.get("input_manifest_sha256")==sha(args.manifest)
                and previous.get("runtime")==runtime
                and previous.get("original_part_receipts")==report["original_part_receipts"]
                and previous.get("root_native_sha256")==ROOT_SHA
                and previous.get("prefix_global_accepted_rows")==len(previous.get("rows",[])))
            if previous.get("complete") and previous.get("proved") and previous.get("failure") is None:
                if not previous.get("gates") or not all(g["passed"] for g in previous["gates"]):
                    raise ValueError("a completed original first-forcing native has an unsuccessful gate")
                args.out.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(args.resume,args.out);reused_complete=True
                print(json.dumps(dict(complete_original_native_reused=True,new_closed_rows=0,
                    original_native_sha256=sha(args.resume))),flush=True)
                return
        report["root_native_sha256"]=ROOT_SHA
        report["original_completed_prefix_sha256"]=sha(args.resume) if args.resume else None
        report["original_completed_prefix_run_id"]=previous.get("public_run_id") if previous else None
        base=old.Shards(paths["candidate"],(1,2),65)
        response=old.Shards(paths["response"],(4,5,6),193)
        repair,direction=read(paths["repair"]),read(paths["direction"])
        eb=list(map(Q,repair["exact_cumulative_coefficient_suprema"]))
        ez=list(map(Q,direction["exact_complete_repair_coefficient_suprema"]))
        check("both exact repair identities and their open-piece radial rule remain",
            repair["derived_definition_sha256"]==old.BASE and direction["derived_direction_definition_sha256"]==old.ZDEF
            and repair["candidate_sha256"]==old.CANDIDATE and direction["original_trial_sha256"]==old.PINS["response"]
            and repair["corrected_value_and_all_angular_derivatives_continuous"]
            and repair["piecewise_radial_derivative_correction"]=="exactly zero on every open original cubic piece"
            and len(eb)==65 and len(ez)==193)
        alpha=Q(base.index["metadata"]["exact_float_amplitude"])
        if alpha!=Q(6890507429876859,9007199254740992):raise ValueError("the original alpha changed")
        oldrows=root["rows"];ostarts=[Q(r["interval"][0]) for r in oldrows]
        istarts=[r[0] for r in original]
        cuts={left,right}
        for r in oldrows:cuts.update(map(Q,r["interval"]))
        for a,b,_ in original:cuts.update((max(a,left),min(b,right)))
        cuts=sorted(cuts)
        scalar_keys=("gamma_upper","T0","V0","vartheta","log_EG_r","log_EG_rr")
        glob={key:arb(0) for key in scalar_keys}
        glob.update(D=[arb(0)]*6,Dr=[arb(0)]*3,K_derivatives=[arb(0)]*4,
                    eta_derivatives=[arb(0)]*4,J_radial=[arb(0)]*3)
        if previous is not None:
            saved=previous.get("rows",[])
            if len(saved)>len(cuts)-1:raise ValueError("the saved prefix exceeds the exact new common partition")
            restored=previous.get("global_coefficient_and_inverse_bounds")
            if saved and (not restored or set(restored)!=set(glob)):
                raise ValueError("a saved successful prefix lost its complete accumulated coefficient bounds")
            if saved:
                glob={k:([box(x) for x in v] if isinstance(v,list) else box(v)) for k,v in restored.items()}
                report["rows"]=list(saved)
        reused_count=len(report["rows"])
        report["original_closed_rows_reused"]=reused_count
        report["new_closed_rows"]=0
        report["global_coefficient_and_inverse_bounds"]=encode(glob)
        report["prefix_global_accepted_rows"]=reused_count
        for serial,(a,b) in enumerate(zip(cuts[:-1],cuts[1:])):
            oi=bisect_right(ostarts,a)-1;prev=oldrows[oi]
            ia,ib,ir=original[bisect_right(istarts,a)-1]
            if not (Q(prev["interval"][0])<=a<b<=Q(prev["interval"][1]) and ia<=a<b<=ib):
                raise ValueError("a new common cell crossed a true original source interval")
            piece=base.piece(a,b)
            if response.piece(a,b)!=piece or piece!=prev["candidate_and_response_piece"] or piece!=ir["pieces"]["background"]:
                raise ValueError("a common-row index was confused with an original polynomial piece")
            if serial<reused_count:
                saved=report["rows"][serial]
                if (saved.get("interval")!=[str(a),str(b)] or saved.get("original_root_row")!=oi
                    or saved.get("original_common_row")!=ir["common_row"]
                    or saved.get("original_piece")!=piece
                    or saved.get("original_intrinsic_interval")!=ir["interval"]
                    or saved.get("actual_scalar_germ")!=ir["actual_scalar_germ"]):
                    raise ValueError("a successful saved first-forcing common row changed its exact identity")
                continue
            jets={name:restricted_jets(ir,name,a,b) for name in ("gamma","beta","K","s")}
            if not jets["gamma"][0]>0:raise ValueError("true gamma interval lost its sign")
            raw=[base.values(piece,a,b,p) for p in range(4)]
            rz=[response.values(piece,a,b,p) for p in range(4)]
            uj=[];vj=[];mj=[]
            for p in range(4):
                ub=[ex(alpha)*v for v in raw[p][:32]]
                vb=[ex(alpha)*v for v in raw[p][32:]]
                if p==0:
                    ub=[v+arb(0,ex(e)) for v,e in zip(ub,eb[:32])]
                    vb=[v+arb(0,ex(e)) for v,e in zip(vb,eb[32:])]
                vb[0]+=jets["s"][p]
                zu=rz[p][:96];zv=rz[p][96:]
                if p==0:
                    zu=[v+arb(0,ex(e)) for v,e in zip(zu,ez[:96])]
                    zv=[v+arb(0,ex(e)) for v,e in zip(zv,ez[96:])]
                uf=[(ub[k] if k<32 else arb(0))+arb(0,ex(DELTA)*up(zu[k])) for k in range(96)]
                vf=[(vb[k] if k<=32 else arb(0))+arb(0,ex(DELTA)*up(zv[k])) for k in range(97)]
                uj.append(uf);vj.append(vf);mj.append(vf[0])
            etaj=[-sum((math.comb(p,l)*jets["gamma"][l]*mj[p-l]
                       for l in range(p+1)),arb(0)) for p in range(4)]
            if not etaj[0]>0:raise ValueError("the actual full-family mean lost its strict sign")
            rb={k:box(v) for k,v in prev["bounds"].items()}
            en,ep=rb["eta_lower"],rb["eta_upper"]
            bs=[up(v) for v in jets["beta"]];ks=[up(v) for v in jets["K"]]
            newstrips={}
            for width in WIDTHS:
                os0=prev["strips"][str(width)]
                U=[[box(v) for v in os0["U"]]]
                V=[[box(v) for v in os0["V"]]]
                for p in (1,2,3):
                    U.append([weight(uj[p],1,width,j) for j in range(2)])
                    V.append([weight(vj[p],0,width,j) for j in range(2)])
                nonmean=[weight(vj[p][1:],1,width,0) for p in (0,1)]
                mm=list(map(up,mj))
                Sn=(U[0][0]**2+ks[0]*(2*mm[0]*nonmean[0]+nonmean[0]**2)).upper()
                Srn=(2*U[0][0]*U[1][0]+ks[1]*(2*mm[0]*nonmean[0]+nonmean[0]**2)
                      +ks[0]*(2*mm[1]*nonmean[0]+2*mm[0]*nonmean[1]+2*nonmean[0]*nonmean[1])).upper()
                Sphi=2*(U[0][0]*U[0][1]+ks[0]*V[0][0]*V[0][1])
                Srphi=2*(U[1][0]*U[0][1]+U[0][0]*U[1][1])+2*ks[1]*V[0][0]*V[0][1]+2*ks[0]*(V[1][0]*V[0][1]+V[0][0]*V[1][1])
                dr=[(bs[1]*Sn+bs[0]*Srn).upper()/4,(bs[1]*Sn+bs[0]*Srn).upper(),
                    (bs[1]*Sphi+bs[0]*Srphi).upper()]
                ds=[box(os0["D"+str(k)]) for k in range(3)]
                for k in (3,4,5):
                    p=k-1
                    ds.append((bs[0]*sum((math.comb(p,l)*(U[0][l]*U[0][p-l]+ks[0]*V[0][l]*V[0][p-l])
                                           for l in range(p+1)),arb(0))).upper())
                lp=[]
                for p in range(4):
                    val=arb(0)
                    for i in range(p+1):
                        for j in range(p-i+1):
                            k=p-i-j;multi=math.factorial(p)//(math.factorial(i)*math.factorial(j)*math.factorial(k))
                            val+=multi*bs[i]*(2*U[j][0]*V[k][0]+V[j][1]*U[k][0]/2)
                    lp.append(val.upper())
                u0,u1,ur=U[0][0],U[0][1],U[1][0]
                v0,v1,vr=V[0][0],V[0][1],V[1][0]
                ell=2*bs[0]*u0*v0
                ellphi=2*bs[0]*(u1*v0+u0*v1)
                ellr=2*bs[1]*u0*v0+2*bs[0]*(ur*v0+u0*vr)
                ephi=2*bs[0]*(3*u0*u1+ks[0]*v0*v1)
                tQ=up(etaj[1])/en+ds[1]+bs[0]*(1+3*u0*u0+ks[0]*v0*v0)
                br0=bs[0]*(1+u0*u0+3*ks[0]*v0*v0)
                br0r=bs[1]*(1+u0*u0+3*ks[0]*v0*v0)+bs[0]*(2*u0*ur+3*ks[1]*v0*v0+6*ks[0]*v0*vr)
                br0phi=2*bs[0]*(u0*u1+3*ks[0]*v0*v1)
                RQ=(ellr+ds[0]*ellphi+ep*ephi+2*bs[0]*ep*u1*u0+ell*(up(etaj[1])/en+ds[1])).upper()
                vartheta=(RQ/en+2*bs[0]*ks[0]*v0*v1).upper()
                V0=(tQ*br0+br0r+ds[0]*br0phi+ks[0]*(4*bs[0]*ep*v0*u1+ell*ell)).upper()
                sm=box(os0["Smean"])
                smr=(2*u0*ur+ks[1]*v0*v0+2*ks[0]*v0*vr).upper()
                t0=(up(etaj[1])/en+4*bs[0]*sm+5*ds[1]).upper()
                item=dict(U_radial=[U[p] for p in (1,2,3)],V_radial=[V[p] for p in (1,2,3)],
                    D=ds,Dr=dr,L_radial=lp,rQ0=RQ,vartheta=vartheta,V0=V0,T0=t0,
                    log_EG_r=(2*bs[0]*sm).upper(),log_EG_rr=(2*bs[1]*sm+2*bs[0]*smr).upper())
                if width==Q(1,32):
                    J0,J1=box(os0["J0"]),box(os0["J1"])
                    M=[(up(etaj[p])*J1+lp[p]*J0).upper() for p in (1,2,3)]
                    jr=[(J0*M[0]).upper(),(J0*(2*M[0]**2+M[1])).upper(),
                        (J0*(6*M[0]**3+6*M[0]*M[1]+M[2])).upper()]
                    item["J0"]=J0;item["J1"]=J1;item["J_radial"]=jr
                    glob["J_radial"]=[maxup((x,y)) for x,y in zip(glob["J_radial"],jr)]
                if width==Q(1,16):
                    for key in ("D","Dr"):glob[key]=[maxup((x,y)) for x,y in zip(glob[key],item[key])]
                    for key in ("T0","V0","vartheta","log_EG_r","log_EG_rr"):
                        glob[key]=maxup((glob[key],item[key]))
                newstrips[str(width)]={k:([[rec(x) for x in z] for z in v] if k in ("U_radial","V_radial")
                                         else [rec(x) for x in v] if isinstance(v,list) else rec(v)) for k,v in item.items()}
            glob["gamma_upper"]=maxup((glob["gamma_upper"],jets["gamma"][0]))
            glob["K_derivatives"]=[maxup((x,y)) for x,y in zip(glob["K_derivatives"],ks)]
            glob["eta_derivatives"]=[maxup((x,y)) for x,y in zip(glob["eta_derivatives"],etaj)]
            report["rows"].append(dict(interval=[str(a),str(b)],original_root_row=oi,
                original_common_row=ir["common_row"],original_piece=piece,
                original_intrinsic_interval=ir["interval"],actual_scalar_germ=ir["actual_scalar_germ"],
                complete_intrinsic_ordinary_jets={k:[rec(v) for v in values] for k,values in jets.items()},
                full_actual_mean_derivatives=[rec(v) for v in mj],
                full_actual_eta_derivatives=[rec(v) for v in etaj],strips=newstrips))
            report["new_closed_rows"]+=1
            report["global_coefficient_and_inverse_bounds"]=encode(glob)
            report["prefix_global_accepted_rows"]=len(report["rows"])
            if serial%128==0:
                report["accepted_closed_rows"]=len(report["rows"]);report["seconds"]=time.monotonic()-started
                save(args.out,report)
                print(json.dumps(dict(accepted_closed_rows=len(report["rows"]),right=str(b),
                                      seconds=report["seconds"])),flush=True)
        check("every common cell retains its original true intrinsic and polynomial identities",
              len(report["rows"])==len(cuts)-1 and report["rows"][0]["interval"][0]==str(left)
              and report["rows"][-1]["interval"][1]==str(right)
              and all(a["interval"][1]==b["interval"][0] for a,b in zip(report["rows"],report["rows"][1:])))
        check("every completed same-source first-forcing prefix row was reused unchanged",
              previous is None or report["rows"][:reused_count]==previous.get("rows",[]))
        check("every original actual coefficient and seam record is consumed without target recomputation",
              len(oldrows)==1300 and len(root["seams"])==1079 and len(report["original_part_receipts"])==6)
        report["global_coefficient_and_inverse_bounds"]=encode(glob)
        report["actual_forcing"]=full_leading_and_forcing(root["selected"],glob,root["seams"],roots,check)
        report.update(complete=True,proved=True,accepted_closed_rows=len(report["rows"]),
            original_complete_root_rows=1300,original_complete_seams=1079,
            original_selected_intrinsic_rows=len(original),exact_cover=[str(left),str(right)],
            exact_root_interval=list(map(str,roots)),root_native_sha256=ROOT_SHA,
            original_root_native_bytes=ROOT_BYTES,original_root_native_public_run_id=ROOT_RUN)
    except BaseException as error:
        report["failure"]={"type":type(error).__name__,"message":str(error)};raise
    finally:
        if not reused_complete:
            report["seconds"]=time.monotonic()-started;save(args.out,report)
            print(json.dumps(dict(complete=report["complete"],failure=report["failure"],
                accepted_closed_rows=len(report["rows"]),seconds=report["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()

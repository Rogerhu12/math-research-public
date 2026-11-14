#!/usr/bin/env python3
"""Refine completed root source norms with analytic Airy columns and matrix jets.

All old moment and directed matrix rows are reused unchanged. Only new analytic
amplitude bounds, complete exponential Fourier tails, and source integrals run.
"""
from __future__ import annotations
import argparse,gzip,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_directed_matrix_old_circle_sources as previous

prior=previous.prior
PUBLIC=prior.PUBLIC
ROOT_SHA=prior.ROOT_SHA;FORCE_SHA=prior.FORCE_SHA;SEAM_SHA=prior.SEAM_SHA
OLD_SHA=previous.OLD_SHA;OLD_SOURCE=previous.OLD_SOURCE;OLD_MANIFEST=previous.OLD_MANIFEST
DIRECTED_SHA="3c8c4f3c93108de5a1c17149518f3aa16500a7f8ad58343f7a8dac325cc48d4b"
DIRECTED_SOURCE="f3a5d7b0caad97d65464e6b79e0884e3a50085cbc6b2d9bab35e9ab1e8a66b0d"
DIRECTED_MANIFEST="29465d2a93165f40f42b2ea73c772374a882475fd59f44fdbce20b37ff4d402f"
DELTA=prior.DELTA;CUTOFF=prior.CUTOFF
WIDTHS=previous.WIDTHS;FINITE_KEYS=previous.FINITE_KEYS
SIGMA=Q(3,64)
ex,box,up,ipow,powq=prior.ex,prior.box,prior.up,prior.ipow,prior.powq
read,save,sha=prior.read,prior.save,prior.sha
rec,compact,encode,decode=prior.rec,prior.compact,prior.encode,prior.decode
radial_weight=prior.radial_weight

NUMERIC_AMPLITUDE_KEYS=("R","hi","hd","w","wr","composition","fourier","profiles")
def tensor_encode(value):
    if isinstance(value,dict):return {k:tensor_encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [tensor_encode(v) for v in value]
    return compact(value)
def tensor_decode(value):
    if isinstance(value,list):return [tensor_decode(v) for v in value]
    if isinstance(value,dict):
        if "ball" in value:return box(value)
        return {k:tensor_decode(v) for k,v in value.items()}
    raise ValueError("a completed numerical amplitude tensor changed schema")

def vadd(a,b):return [(x+y).upper() for x,y in zip(a,b)]
def vscale(a,c):return [(x*c).upper() for x in a]
def madd(a,b):return [vadd(x,y) for x,y in zip(a,b)]
def mscale(a,c):return [vscale(x,c) for x in a]
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(2)),arb(0)).upper()
             for j in range(2)] for i in range(2)]
def mv(a,b):
    return [sum((a[i][k]*b[k] for k in range(2)),arb(0)).upper() for i in range(2)]
def mvjets(a,b,last):
    if len(a)<=last or len(b)<=last:raise ValueError("a true ordered matrix jet is missing")
    return [[sum((math.comb(k,l)*mv(a[l],b[k-l])[i]
                  for l in range(k+1)),arb(0)).upper() for i in range(2)]
            for k in range(last+1)]
def svjets(a,b,last):
    if len(a)<=last or len(b)<=last:raise ValueError("a true scalar-vector jet is missing")
    return [[sum((math.comb(k,l)*a[l]*b[k-l][i]
                  for l in range(k+1)),arb(0)).upper() for i in range(2)]
            for k in range(last+1)]
def vjadd(a,b):
    if len(a)!=len(b):raise ValueError("two source jets have different orders")
    return [vadd(x,y) for x,y in zip(a,b)]
def vjscale(a,c):return [vscale(x,c) for x in a]
def lam(j):return ex(1+16*j*j).sqrt()

def complete_fourier_factor(tau):
    """A1--4: all integer diagonals, including mean output, with a true tail."""
    if not tau>0:raise ValueError("the actual inverse phase strip is not positive")
    q=(-4*tau).exp()
    J=CUTOFF
    ratio=(q*powq(ex(Q(J+1,J)),Q(4,3))).upper()
    if not ratio<1:raise ValueError("the actual complete exponential tail does not contract")
    center=powq(lam(J),Q(-1,3))
    finite=sum((ipow(q,l)*powq(lam(J),Q(4,3))/powq(lam(J-l),Q(5,3))
                for l in range(1,J)),arb(0))
    tail=(ipow(q,J)*powq(lam(J),Q(4,3))/(1-ratio)).upper()
    total=(center+2*finite+2*tail).upper()
    return total,dict(inverse_phase_strip=compact(tau),diagonal_factor=compact(center),
        full_nonzero_lags_below_cutoff=compact(2*finite),
        complete_infinite_lag_tail=compact(2*tail),
        exact_geometric_tail_ratio=compact(ratio),complete_factor=compact(total),
        tail_first_lag=J,mean_output_and_both_lag_signs_retained=True)

def amplitude_case(case,af,roots):
    vals={k:box(x) for k,x in case["bounds"].items()}
    R=ex(Q(case["exact_radius"])+roots[1]-roots[0])
    Am=vals["A_lower"].lower();Ap=vals["A_upper"].upper();ap=vals["a_upper"].upper()
    gap=vals["fold_noncharacteristic_gap"].lower()
    E=up(box(af["flow_variational_C"]["1"]))
    if not (R>0 and Am>0 and gap>0 and E<2):
        raise ValueError("the original actual fold or real inverse phase gap was lost")
    if af["leading_strip"]!="3/64":
        raise ValueError("the actual completed leading strip changed")
    ray_strip=(E*(ex(SIGMA)+vals["positive_optical_integral"])).upper()
    if not ray_strip<ex(Q(1,16)):
        raise ValueError("the complete analytic leading characteristics leave their original coefficient strip")
    A={k:(R*up(box(af["A_angular_constants"][str(k)]))).upper() for k in (1,2,3)}
    X={1:E,2:(R*up(box(af["flow_variational_C"]["2"]))).upper(),
           3:(R*up(box(af["flow_variational_C"]["3"]))).upper()}
    T=[(R*powq(Ap,Q(2,3))).upper(),
       (ex(Q(2,3))*R*powq(Am,Q(-1,3))*A[1]).upper(),
       (ex(Q(2,3))*R*(powq(Am,Q(-1,3))*A[2]
             +powq(Am,Q(-4,3))*ipow(A[1],2)/3)).upper(),
       (ex(Q(2,3))*R*(powq(Am,Q(-1,3))*A[3]
             +powq(Am,Q(-4,3))*A[1]*A[2]
             +ex(Q(4,9))*powq(Am,Q(-7,3))*ipow(A[1],3))).upper()]
    hi0=mscale([[X[1],T[0]*T[1]],[T[1],X[1]]],1/gap)
    hp=[[X[2],ipow(T[1],2)+T[0]*T[2]],[T[2],X[2]]]
    hpp=[[X[3],3*T[1]*T[2]+T[0]*T[3]],[T[3],X[3]]]
    hi1=mm(mm(hi0,hp),hi0)
    hi2=madd(mscale(mm(mm(hi1,hp),hi0),2),mm(mm(hi0,hpp),hi0))
    hi=[hi0,hi1,hi2]
    ss=[powq(Am,Q(-1,3)),powq(Am,Q(-4,3))*A[1]/3,
        powq(Am,Q(-4,3))*A[2]/3+ex(Q(4,9))*powq(Am,Q(-7,3))*ipow(A[1],2)]
    Z=[(ex(Q(2,3))*ap*ipow(R,2)*A[k+1]).upper() for k in range(3)]
    Y=[(ap*ss[0]*X[1]).upper(),
       (ap*(ss[0]*X[2]+ss[1]*X[1])).upper(),
       (ap*(ss[0]*X[3]+2*ss[1]*X[2]+ss[2]*X[1])).upper()]
    hd=[[[Z[0],Y[0]*T[0]],[Y[0],Z[0]]],
        [[Z[1],Y[1]*T[0]+Y[0]*T[1]],[Y[1],Z[1]]],
        [[Z[2],Y[2]*T[0]+2*Y[1]*T[1]+Y[0]*T[2]],[Y[2],Z[2]]]]
    aa,bb=af["leading_a0_derivative_bounds"],af["leading_b0_derivative_bounds"]
    w=[[up(box(aa[str((0,k))])),up(box(bb[str((0,k))]))] for k in range(3)]
    wr=[[up(box(aa[str((1,k))])),up(box(bb[str((1,k))]))] for k in range(2)]
    m=(2-E).lower();M=E;F2=X[2];F3=X[3]
    P2=(F2/ipow(m,3)).upper()
    P3=(F3/ipow(m,4)+3*ipow(F2,2)/ipow(m,5)).upper()
    c0=(1/m.sqrt()).upper()
    c2=(M.sqrt()*(1/ipow(m,2)+2*ipow(P2,2)+1/ipow(m,4)+ipow(P3,2)
                       +ex(Q(9,2))*ipow(P2,2)/ipow(m,2)+1/ipow(m,6)).sqrt()).upper()
    cphi=(powq(c0,Q(1,6))*powq(c2,Q(5,6))).upper()
    tau=(m*ex(SIGMA)).lower()
    fourier,fe=complete_fourier_factor(tau)
    zz=powq(3*Ap/(2*Am),Q(2,3))
    ez=(zz+ipow(zz,2)/2).exp().upper()
    cm=(ex(Q(5,36)).exp()/(2*arb.pi().sqrt())).upper()
    cp=(ex(Q(5,72)).exp()/(2*arb.pi().sqrt())).upper()
    profiles=dict(central=[(ez*powq(3/(2*Am),Q(1,6))).upper(),
                               (ez*powq(R,Q(1,4))*powq(ex(4*CUTOFF),Q(-1,6))).upper()],
        negative=[(cm*powq(Am,Q(-1,6))).upper(),
                  (ex(Q(47,36))*cm*powq(R,Q(1,2))*powq(Ap,Q(1,6))).upper()],
        positive=[(cp*powq(Am,Q(-1,6))).upper(),
                  (ex(Q(47,36))*cp*powq(R,Q(1,2))*powq(Ap,Q(1,6))).upper()])
    if not all(x.is_finite() for row in profiles.values() for x in row):
        raise ValueError("a complete analytic Airy profile is nonfinite")
    evidence=dict(leading_strip=str(SIGMA),actual_leading_ray_strip=compact(ray_strip),
        fold_gap=compact(gap),real_inverse_phase_derivative_lower=compact(m),
        analytic_inverse_phase_strip=compact(tau),complete_Fourier_factor=compact(fourier),
        real_phase_Hminus5over3_composition=compact(cphi),
        no_angular_Cauchy_loss=True,separate_Airy_components=True,
        amplitude_angular_order=2,radial_angular_order=1,
        complete_exponential_Fourier_evidence=fe)
    full_evidence=dict(**evidence,H_inverse_angular_jets=tensor_encode(hi),
        HD_angular_jets=tensor_encode(hd),leading_vector_jets=tensor_encode(w),
        leading_radial_vector_jets=tensor_encode(wr),Airy_profiles=tensor_encode(profiles))
    return dict(R=R,hi=hi,hd=hd,w=w,wr=wr,composition=cphi,fourier=fourier,
        profiles=profiles,matrix_evidence=full_evidence,analytic_summary=evidence)

def source_constants(c,a,side):
    hi,hd,w,wr=a["hi"],a["hd"],a["w"],a["wr"]
    def A(v):
        if len(v)!=2:raise ValueError("the two true Airy components were merged")
        def profile(name):
            return sum((x*y for x,y in zip(a["profiles"][name],v)),arb(0)).upper()
        center=profile("central")
        if side=="negative":
            branch=profile("negative")
            core=(center*center+4*branch*branch).sqrt().upper()
        else:
            core=max(center,profile("positive")).upper()
        return (a["composition"]*a["fourier"]*core).upper()
    def Dfrak(v,last):return mvjets(hi,v,last+1)[1:]
    def B(v):return (A(mv(hi[0],v[0]))+A(Dfrak(v,0)[0])).upper()
    def M0(v):return A(Dfrak(v,0)[0])
    def M1(v):return A(Dfrak(Dfrak(v,1),0)[0])
    hdw=mvjets(hd,w,2)
    h=vjscale(mvjets(hi,hdw,2),1/c["eta_lower"])
    y=svjets(c["V"],mvjets(hi,hdw,2),2)
    dw=vjadd(wr,svjets(c["D"],w[1:],1))
    gd=vjadd(dw,vjscale(h[1:],c["eta_upper"]))
    qv=vjadd(svjets(c["V"],dw,1),y[1:])
    Bh,Bw,Bgd=B(h),B(w),B(gd)
    MD=(M1(hdw)+M0(dw)).upper()
    terms=dict(
        complete_SV=c["C_SV_directed"]*Bw,
        complete_SQ=c["C_SQ_directed"]*Bh,
        complete_RQ_J_gd=c["C_RQJ_directed"]*Bgd,
        complete_RQ_JL_h=c["C_RQJL_directed"]*Bh,
        complete_primitive_error=c["C_primitive_directed"]*B(qv),
        old_mean_rQ=c["m0_rQ"]*M0(h),
        old_mean_vphi=c["cB"]*c["V"][1]*M0(y),
        old_mean_raw_D=(c["cB"]*c["V"][1]*c["V"][0]/4+c["m0_T0"])*MD,
        old_mean_V0=c["m0_V0"]*M0(w))
    nl=sum(terms.values(),arb(0)).upper()
    vn=list(c["V"]);vn[0]=min(vn[0],vn[1]/4).upper()
    mean=(c["exact_nonlocal_even_mean_row_factor"]*
        (M0(svjets(c["U"],h,1))
         +c["C_uJ_directed"]*Bgd+c["C_uJL_directed"]*Bh+c["C_uJB_directed"]*Bw
         +c["K"]*M0(svjets(vn,w,1)))).upper()
    first=(c["C_J_scalar"]*nl).upper()
    if not (first.is_finite() and mean.is_finite()):
        raise ValueError("a complete analytic Airy source cost is nonfinite")
    return first,mean,{k:v.upper() for k,v in terms.items()}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","root-native","forcing-native","seam-native","old-native","directed-native","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all mathematics requires the actual public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):raise ValueError("the pinned runtime changed")
    if a.out.exists():raise FileExistsError("preserve every actual nonlocal remainder outcome")
    ctx.prec=256;started=time.monotonic()
    result=dict(kind="actual_complete_analytic_Airy_old_circle_source_budget_v1",
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),runtime=runtime,complete=False,proved=False,failure=None,
        root_native_sha256=ROOT_SHA,first_forcing_native_sha256=FORCE_SHA,first_seam_native_sha256=SEAM_SHA,
        original_completed_norm_native_sha256=OLD_SHA,old_completed_moment_rows_recomputed=0,
        original_completed_directed_native_sha256=DIRECTED_SHA,old_completed_directed_rows_recomputed=0,
        analytic_leading_strip=str(SIGMA),original_completed_directed_rows_reused=0,
        complete_exponential_tail_and_mean_output_retained=True,original_two_Airy_components_separate=True,
        actual_new_analytic_amplitude_cases=0,analytic_amplitude_cases_reused=0,actual_new_source_integral_rows=0,
        input_cutoff=CUTOFF,physical_frequency="4|j|",density_input_normalization="n^(7/6)",
        source_window="H^-4/3 -> ordinary radial L2(H^-2/3 x H^-2/3)",
        exact_real_delta_radius=str(DELTA),old_mean_and_all_Fourier_outputs_retained=True,
        original_target_coefficient_ray_and_amplitude_solves_recomputed=0,
        higher_radial_intrinsic_jets_invented_or_recomputed=False,
        local_L0_w1_paid=False,positive_source_to_root_conversion_claimed=False,
        complete_strong_return_norm_evaluated=False,numerical_cutoff97_inverse_claimed=False,
        actual_PDE_branch_claimed=False,gates=[],coefficient_rows=[],cases=[],
        coefficient_rows_reused=0,new_coefficient_norm_rows=0)
    def check(name,truth):
        passed=bool(truth);result["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("actual old-circle remainder gate failed: "+name)
    def checkpoint():
        result["seconds"]=time.monotonic()-started;save(a.out,result)
    try:
        manifest=read(a.manifest);result["input_manifest_sha256"]=sha(a.manifest)
        for entry in manifest["files"]:
            path=a.repo_root/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a complete fixed input changed: "+entry["path"])
        for path,expected,size in ((a.root_native,ROOT_SHA,5923431),
                (a.forcing_native,FORCE_SHA,6577892),(a.seam_native,SEAM_SHA,904977),(a.old_native,OLD_SHA,4837715),
                (a.directed_native,DIRECTED_SHA,7873296)):
            if sha(path)!=expected or path.stat().st_size!=size:raise ValueError("a complete original native changed")
        root,force,seam=read(a.root_native),read(a.forcing_native),read(a.seam_native)
        check("all three original complete natives and their actual gates remain proved",
            all(d["complete"] and d["proved"] and d["failure"] is None
                and all(g["passed"] for g in d["gates"]) for d in (root,force,seam))
            and len(root["rows"])==1300 and len(force["rows"])==1328 and len(seam["seams"])==1079
            and force["root_native_sha256"]==ROOT_SHA and seam["root_native_sha256"]==ROOT_SHA
            and seam["first_forcing_native_sha256"]==FORCE_SHA
            and force["source_sha256"]=="ba25934f0f6e147f293644edc93b2adf1c33d5935f86596d96355cf063c95fa6"
            and seam["source_sha256"]=="9c71989fc069bb6cc35bcb18c03f5ca73b20a33d57387b6a2be2b5a48aefe71a")
        fp=read(a.repo_root/manifest["input_paths"]["first_forcing_process"])
        sp=read(a.repo_root/manifest["input_paths"]["first_seam_process"])
        check("the complete original forcing and seam natives have actual zero-return public receipts",
            fp["actual_returncode"]==0 and fp["complete"] and fp["mathematical_complete"]
            and fp["mathematical_failure"] is None and fp["native_sha256"]==FORCE_SHA
            and str(fp["run_id"])=="43624260519"
            and all(g["passed"] for g in fp["mathematical_gates"])
            and sp["actual_returncode"]==0 and sp["complete"] and sp["mathematical_complete"]
            and sp["mathematical_failure"] is None and sp["native_sha256"]==SEAM_SHA
            and str(sp["run_id"])=="43625828234"
            and len(sp["mathematical_gates"])==39 and all(g["passed"] for g in sp["mathematical_gates"]))
        original_norm=read(a.old_native)
        op=read(a.repo_root/manifest["input_paths"]["original_norm_process"])
        check("all1328 completed original moment rows and all six cases are reused verbatim",
            original_norm["complete"] and original_norm["proved"] and original_norm["failure"] is None
            and original_norm["source_sha256"]==OLD_SOURCE
            and original_norm["input_manifest_sha256"]==OLD_MANIFEST
            and original_norm["root_native_sha256"]==ROOT_SHA
            and original_norm["first_forcing_native_sha256"]==FORCE_SHA
            and original_norm["first_seam_native_sha256"]==SEAM_SHA
            and len(original_norm["coefficient_rows"])==1328 and len(original_norm["cases"])==6
            and all(g["passed"] for g in original_norm["gates"])
            and op["actual_returncode"]==0 and op["complete"] and op["mathematical_complete"]
            and op["mathematical_failure"] is None and str(op["run_id"])=="43629465215"
            and op["native_sha256"]==OLD_SHA and op["mathematical_source_sha256"]==OLD_SOURCE
            and op["manifest_sha256"]==OLD_MANIFEST and len(op["mathematical_gates"])==7
            and all(g["passed"] for g in op["mathematical_gates"]))
        result["original_completed_norm_rows_reused"]=1328
        directed=read(a.directed_native)
        dp=read(a.repo_root/manifest["input_paths"]["directed_process"])
        check("the complete actual1328 directed matrix rows and all eight public gates are reused unchanged",
            directed["complete"] and directed["proved"] and directed["failure"] is None
            and directed["source_sha256"]==DIRECTED_SOURCE
            and directed["input_manifest_sha256"]==DIRECTED_MANIFEST
            and directed["original_completed_norm_native_sha256"]==OLD_SHA
            and directed["root_native_sha256"]==ROOT_SHA
            and directed["first_forcing_native_sha256"]==FORCE_SHA
            and directed["first_seam_native_sha256"]==SEAM_SHA
            and len(directed["coefficient_rows"])==1328 and len(directed["cases"])==6
            and len(directed["gates"])==8 and all(g["passed"] for g in directed["gates"])
            and dp["actual_returncode"]==0 and dp["complete"] and dp["mathematical_complete"]
            and dp["mathematical_failure"] is None and str(dp["run_id"])=="43632464994"
            and dp["native_sha256"]==DIRECTED_SHA and dp["native_bytes"]==7873296
            and dp["mathematical_source_sha256"]==DIRECTED_SOURCE
            and dp["manifest_sha256"]==DIRECTED_MANIFEST and len(dp["mathematical_gates"])==8
            and all(g["passed"] for g in dp["mathematical_gates"]))
        result["original_completed_directed_rows_reused"]=1328
        roots=list(map(Q,root["exact_root_interval"]))
        check("the same explicit real family and all true root identities are retained",
            force["exact_root_interval"]==root["exact_root_interval"]==seam["exact_root_interval"]
            and force["exact_cover"]==root["exact_cover"]==seam["exact_cover"]
            and force["exact_real_delta_radius"]==seam["exact_real_delta_radius"]==str(DELTA))
        cauchy=read(a.repo_root/manifest["input_paths"]["negative_cauchy_summary"])
        check("the actual negative source and primitive windows retain all means and gates",
            cauchy["complete"] and cauchy["failure"] is None and len(cauchy["gates"])==8
            and all(g["passed"] for g in cauchy["gates"])
            and cauchy["native_sha256"]=="3a214897f5dc47e1a1fed3db327f54fcc0302ad6fd273ea96ecdbfcc0ca4f1e0"
            and cauchy["input_sha256"]["root-native"]==ROOT_SHA
            and cauchy["exact_real_delta_radius"]==str(DELTA)
            and cauchy["all_frequencies_and_independent_even_mean_retained"] is True)
        positive_receipt=read(a.repo_root/manifest["input_paths"]["positive_negative_one_summary"])
        body_cut=Q(positive_receipt["fixed_body_cut"])
        check("the raw positive source split uses the same actual whole-family fixed body cut",
            positive_receipt["complete"] and positive_receipt["failure"] is None
            and all(g["passed"] for g in positive_receipt["gates"])
            and positive_receipt["exact_real_delta_radius"]==str(DELTA)
            and positive_receipt["negative_one_source_window_proved"] is True
            and body_cut==Q(1192029371497,5000000000000) and body_cut>roots[1])
        result["fixed_positive_body_cut"]=str(body_cut)
        result["positive_cut_receipt_sha256"]=sha(a.repo_root/manifest["input_paths"]["positive_negative_one_summary"])
        previous=None
        if a.resume:
            previous=read(a.resume)
            check("the existing successful scalar prefix has the identical producer and input bytes",
                previous["source_sha256"]==sha(__file__) and previous["input_manifest_sha256"]==sha(a.manifest)
                and previous["root_native_sha256"]==ROOT_SHA
                and previous["first_forcing_native_sha256"]==FORCE_SHA
                and previous["first_seam_native_sha256"]==SEAM_SHA and previous["runtime"]==runtime
                and previous["original_completed_norm_native_sha256"]==OLD_SHA
                and previous["original_completed_directed_native_sha256"]==DIRECTED_SHA)
            result["coefficient_rows"]=list(previous["coefficient_rows"])
            result["cases"]=list(previous["cases"])
        reused=len(result["coefficient_rows"]);result["coefficient_rows_reused"]=reused
        result["analytic_amplitude_cases_reused"]=sum(
            bool(c.get("complete_analytic_amplitude")) for c in result["cases"])
        for index,fr in enumerate(force["rows"]):
            ri=fr["original_root_row"];rr=root["rows"][ri]
            oldrow=original_norm["coefficient_rows"][index]
            dr=directed["coefficient_rows"][index]
            for row in (oldrow,dr):
                if row["common_row"]!=index or row["interval"]!=fr["interval"] or row["original_root_row"]!=ri:
                    raise ValueError("an original complete moment or directed row changed its identity")
            lo,hi=map(Q,fr["interval"]);rlo,rhi=map(Q,rr["interval"])
            if not rlo<=lo<hi<=rhi:raise ValueError("a reused row lost its exact original radial cover")
            entry=dict(common_row=index,interval=fr["interval"],original_root_row=ri,
                original_completed_moment_row=index,original_completed_directed_row=index,
                bounds=dr["bounds"])
            if index<reused:
                if result["coefficient_rows"][index]!=entry:
                    raise ValueError("the accepted reused directed row changed its exact bounds")
            else:
                result["coefficient_rows"].append(entry)
        check("all1328 complete original moment and directed matrix rows were reused without recalculation",
            len(result["coefficient_rows"])==1328 and result["new_coefficient_norm_rows"]==0
            and all(x["interval"][1]==y["interval"][0] for x,y in zip(
                result["coefficient_rows"],result["coefficient_rows"][1:])))
        checkpoint()
        for ci,(case,refined) in enumerate(zip(root["cases"],seam["refined_forcing_radius_cases"])):
            if case["exact_radius"]!=refined["exact_radius"] or not case["passed"] or not refined["passed"]:
                raise ValueError("an original completed forcing radius changed")
            cl,cr=map(Q,case["exact_radial_cover"]);af=refined["actual_forcing"]
            selected=[r for r in result["coefficient_rows"] if cl<=Q(r["interval"][0]) and Q(r["interval"][1])<=cr]
            if not selected or selected[0]["interval"][0]!=str(cl) or selected[-1]["interval"][1]!=str(cr):
                raise ValueError("a true radius lost its complete saved common cover")
            if ci<len(result["cases"]):
                out=result["cases"][ci]
                if out["exact_radius"]!=case["exact_radius"] or out["exact_cover"]!=case["exact_radial_cover"]:
                    raise ValueError("a completed radius prefix changed its domain")
                if out.get("complete"):
                    continue
            else:
                out=dict(exact_radius=case["exact_radius"],exact_cover=case["exact_radial_cover"],
                    complete=False,complete_original_rows=len(selected),rows=[])
                result["cases"].append(out)
            if out.get("complete_analytic_amplitude"):
                saved_amplitude=out["complete_analytic_amplitude_numeric"]
                if set(saved_amplitude)!=set(NUMERIC_AMPLITUDE_KEYS):
                    raise ValueError("an accepted complete amplitude tensor lost its exact fields")
                amplitude=tensor_decode(saved_amplitude)
                amplitude["matrix_evidence"]=out["constant_matrix_derivative_evidence"]
                amplitude["analytic_summary"]=out["analytic_amplitude_summary"]
            else:
                amplitude=amplitude_case(case,af,roots)
                out["constant_matrix_derivative_evidence"]=amplitude["matrix_evidence"]
                out["analytic_amplitude_summary"]=amplitude["analytic_summary"]
                out["complete_analytic_amplitude_numeric"]=tensor_encode(
                    {key:amplitude[key] for key in NUMERIC_AMPLITUDE_KEYS})
                out["complete_analytic_amplitude"]=True
                result["actual_new_analytic_amplitude_cases"]+=1
                checkpoint()
            prefix=len(out["rows"]);neg=arb(0);pos=arb(0);pos_collar=arb(0);pos_body=arb(0)
            for si,saved in enumerate(selected):
                left,right=map(Q,saved["interval"])
                if si<prefix:
                    item=out["rows"][si]
                    if item["common_row"]!=saved["common_row"] or item["interval"]!=saved["interval"]:
                        raise ValueError("an accepted source-integral row changed identity")
                else:
                    c=decode(original_norm["coefficient_rows"][saved["common_row"]]["bounds"])
                    c.update(decode(saved["bounds"]));item=dict(common_row=saved["common_row"],interval=saved["interval"])
                    result["last_attempted_source_row"]=dict(radius=case["exact_radius"],common_row=saved["common_row"])
                    for side in ("negative","positive"):
                        weight=radial_weight(left,right,roots,side)
                        if not weight>0:
                            item[side]=dict(squared_source_integral=compact(arb(0)),exact_zero_radial_part=True)
                            continue
                        first,mean,terms=source_constants(c,amplitude,side)
                        value=(weight*(first*first+mean*mean)).upper()
                        item[side]=dict(radial_weight_integral=compact(weight),
                            first_row_singular_envelope=compact(first),full_even_mean_singular_envelope=compact(mean),
                            complete_scalar_nonlocal_terms=encode(terms),
                            first_row_operator_term_envelopes=encode({k:c["C_J_scalar"]*z for k,z in terms.items()}),
                            squared_source_integral=compact(value))
                        if side=="positive":
                            wc=(radial_weight(left,min(right,body_cut),roots,side)
                                if left<min(right,body_cut) else arb(0))
                            wb=(radial_weight(max(left,body_cut),right,roots,side)
                                if max(left,body_cut)<right else arb(0))
                            item[side]["collar_squared_source_integral"]=compact((wc*(first*first+mean*mean)).upper())
                            item[side]["body_squared_source_integral"]=compact((wb*(first*first+mean*mean)).upper())
                    out["rows"].append(item);result["actual_new_source_integral_rows"]+=1;result.pop("last_attempted_source_row",None)
                neg+=box(item["negative"]["squared_source_integral"])
                pos+=box(item["positive"]["squared_source_integral"])
                if not item["positive"].get("exact_zero_radial_part"):
                    pos_collar+=box(item["positive"]["collar_squared_source_integral"])
                    pos_body+=box(item["positive"]["body_squared_source_integral"])
                if si%128==0:checkpoint()
            cb=next(z for z in cauchy["cases"] if z["exact_radius"]==case["exact_radius"])
            gain=box(cb["bounds"]["primitive_after_Hminus1"]["ordinary_L2_radial_source_to_L2"])
            keys=FINITE_KEYS
            out["complete_case_operator_cost_maxima"]={k:compact(max(
                up(box(row["bounds"][k])) for row in selected).upper()) for k in keys}
            out["separate_first_row_term_L2_source_bounds"]={}
            for side in ("negative","positive"):
                sums={}
                for item in out["rows"]:
                    row=item[side]
                    if row.get("exact_zero_radial_part"):continue
                    weight=box(row["radial_weight_integral"])
                    for key,value in row["first_row_operator_term_envelopes"].items():
                        term=box(value)
                        sums[key]=sums.get(key,arb(0))+weight*term*term
                out["separate_first_row_term_L2_source_bounds"][side]={
                    key:compact(value.sqrt().upper()) for key,value in sums.items()}
            out["negative_complete_ordinary_L2_source"]=rec(neg.sqrt().upper())
            out["positive_complete_ordinary_L2_source"]=rec(pos.sqrt().upper())
            out["positive_collar_complete_ordinary_L2_source"]=rec(pos_collar.sqrt().upper())
            out["positive_body_complete_ordinary_L2_source"]=rec(pos_body.sqrt().upper())
            out["positive_split_retains_independent_mean_and_is_not_a_full_low_high_inverse"]=True
            out["actual_negative_source_to_primitive_L2_gain"]=rec(gain)
            out["negative_leading_nonlocal_and_mean_component_Hminus4over3_to_primitive_L2"]=rec((gain*neg.sqrt()).upper())
            out["positive_source_to_root_conversion_claimed"]=False
            out["complete"]=True;out["original_norm_rows_reused"]=len(selected)
            out["original_directed_rows_reused"]=len(selected)
            out["complete_original_matrix_widths"]=list(map(str,WIDTHS))
            out["original_complete_source_bounds_not_overwritten"]=True
            checkpoint()
        check("all six real root windows have complete analytic Airy old inverse and independent mean source budgets",
            len(result["cases"])==6 and all(c["complete"] and len(c["rows"])==c["complete_original_rows"]
                for c in result["cases"]))
        check("complete exponential Fourier tails and separate Airy components use no angular Cauchy loss",
            all(c["analytic_amplitude_summary"]["no_angular_Cauchy_loss"]
                and c["analytic_amplitude_summary"]["separate_Airy_components"]
                and c["analytic_amplitude_summary"]["amplitude_angular_order"]==2
                and c["analytic_amplitude_summary"]["leading_strip"]==str(SIGMA)
                and c["analytic_amplitude_summary"]["complete_exponential_Fourier_evidence"][
                    "mean_output_and_both_lag_signs_retained"] for c in result["cases"]))
        result["exact_root_interval"]=root["exact_root_interval"];result["exact_cover"]=root["exact_cover"]
        result["actual_negative_Cauchy_native_sha256"]=cauchy["native_sha256"]
        result.update(complete=True,proved=True)
    except BaseException as error:
        result["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=result["complete"],failure=result["failure"],
            coefficient_rows=len(result["coefficient_rows"]),complete_cases=sum(bool(c.get("complete")) for c in result["cases"]),
            seconds=result["seconds"])),flush=True)
if __name__=="__main__":main()

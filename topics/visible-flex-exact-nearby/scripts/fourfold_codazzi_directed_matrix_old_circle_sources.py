#!/usr/bin/env python3
"""Consume completed rows with the complete directed analytic matrix algebra.

This changes only the new norm arithmetic. All original target, coefficient,
ray, forcing, seam and old moment rows remain fixed and are read verbatim.
"""
from __future__ import annotations
import argparse,gzip,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_leading_old_circle_remainder_sources as prior

PUBLIC=prior.PUBLIC
ROOT_SHA=prior.ROOT_SHA;FORCE_SHA=prior.FORCE_SHA;SEAM_SHA=prior.SEAM_SHA
OLD_SHA="7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c"
OLD_SOURCE="56b68983f36bb3d88e1427081ba9e60a8f6cf43dcd9578a0d925e1834292555d"
OLD_MANIFEST="7290cbb07293c15a239ffafb0e342e6c1b7ea812106f569e88bbe4d2502180df"
DELTA=prior.DELTA;CUTOFF=prior.CUTOFF
WIDTHS=(Q(1,16),Q(1,32),Q(1,64))
ex,box,up,ipow,powq=prior.ex,prior.box,prior.up,prior.ipow,prior.powq
read,save,sha=prior.read,prior.save,prior.sha
rec,compact,encode,decode=prior.rec,prior.compact,prior.encode,prior.decode
add,scale,mul=prior.add,prior.scale,prior.mul
amplitude_case,radial_weight=prior.amplitude_case,prior.radial_weight
FINITE_KEYS=("C_SV_directed","C_SQ_directed","C_RQJ_directed","C_RQJL_directed",
    "C_primitive_directed","C_uJ_directed","C_uJL_directed","C_uJB_directed")

class Budget:
    """z=M_sigma(K), d=M_sigma([partial,K]), g=M_sigma(K Lambda)."""
    def __init__(self,z,d=None,g=None):
        self.z=up(arb(z))
        self.d=None if d is None else up(arb(d))
        self.g=None if g is None else up(arb(g))
    def __add__(self,other):
        return Budget(self.z+other.z,
            None if self.d is None or other.d is None else self.d+other.d,
            None if self.g is None or other.g is None else self.g+other.g)
    def scaled(self,c):
        c=up(arb(c))
        return Budget(c*self.z,None if self.d is None else c*self.d,
            None if self.g is None else c*self.g)
    def __matmul__(self,other):
        choices=[]
        if other.g is not None:choices.append((self.z*other.g).upper())
        if self.g is not None and other.d is not None:
            choices.append((self.g*other.z+self.z*other.d).upper())
        return Budget(self.z*other.z,
            None if self.d is None or other.d is None else self.d*other.z+self.z*other.d,
            min(choices).upper() if choices else None)
    def record(self):
        return dict(z=compact(self.z),d=None if self.d is None else compact(self.d),
                    right_gain=None if self.g is None else compact(self.g))

def T(f):
    return Budget(f[0],f[1] if len(f)>1 else None)
def rank(f,g,CI):
    if len(f)<2 or len(g)<2 or f[1] is None or g[1] is None:
        raise ValueError("a complete old rank map lost its first coefficient derivatives")
    fp=min(f[0],f[1]/4).upper();gp=min(g[0],g[1]/4).upper()
    return Budget(fp*gp,f[1]*gp+fp*g[1],CI*fp*g[1])

def width_budget(fr,rr,width):
    """M12--15: exact operator words before any Sobolev conversion."""
    rt=rr["strips"][str(width)];st=fr["strips"]["1/16"]
    c=up(box(rt["c"]))
    evidence=dict(width=str(width),actual_original_contraction=compact(c),usable=bool(c<1))
    if not c<1:
        evidence["reason"]="the original full nonmean Neumann condition is not proved at this width"
        return None,evidence
    U=list(map(lambda x:up(box(x)),rt["U"]))
    V=list(map(lambda x:up(box(x)),rt["V"]))
    Ur=list(map(lambda x:up(box(x)),st["U_radial"][0]))
    Vr=list(map(lambda x:up(box(x)),st["V_radial"][0]))
    # The saved radial jets are complete on the larger width1/16;
    # their unchanged bounds are valid on each of the three chosen widths.
    D=[up(box(rt[k])) for k in ("D0","D1","D2")]
    jets=fr["complete_intrinsic_ordinary_jets"]
    b=up(box(jets["beta"][0]));br=up(box(jets["beta"][1]))
    K=up(box(jets["K"][0]));Kr=up(box(jets["K"][1]))
    eta=list(map(lambda x:up(box(x)),fr["full_actual_eta_derivatives"]))
    eta_min=box(rr["bounds"]["eta_lower"]).lower()
    if not eta_min>0:raise ValueError("the same actual full-family eta gap failed")
    cabs=2*b;cbabs=2*b*K;cr=2*br;cbr=2*(br*K+b*Kr)
    CI=ex(Q(17)).sqrt()/4
    primitive=Budget(ex(Q(1,4)),arb(0),CI)
    one=[arb(1),arb(0),arb(0)]
    uv=mul(U,V,2);uu=mul(U,U,2);vv=mul(V,V,2)
    ell=scale(uv,cabs)
    ee=scale(add(one,scale(uu,3),scale(vv,K)),b)
    bzero=scale(add(one,uu,scale(vv,3*K)),b)
    tq=[(eta[1]/eta_min+D[1]+ee[0]).upper(),(D[2]+ee[1]).upper()]
    rq=[up(box(st["rQ0"]))]
    def N(p,q):return T(p)@primitive@T(q)
    def C(p,q):
        # Signs are immaterial for this full triangle bound, but all five
        # projected products/rank terms from M13 are retained.
        dp=mul(D,p[1:],1);dq=mul(D,q[1:],1)
        return ((T(dp)+rank(p,D[1:],CI))@primitive@T(q)
            +T(p)@primitive@T(D[1:])@T(q)
            +T(p)@primitive@(T(dq)+rank(q,D[1:],CI)))
    NA=N(V[1:],U).scaled(cabs)
    NC=N(U[1:],V).scaled(cabs)
    NE=N(U[1:],U).scaled(cabs)
    NB=N(V[1:],V).scaled(cbabs)
    NAr=(N(V[1:],U).scaled(cr)+
         N(Vr[1:],U).scaled(cabs)+N(V[1:],Ur).scaled(cabs))
    NBr=(N(V[1:],V).scaled(cbr)+
         N(Vr[1:],V).scaled(cbabs)+N(V[1:],Vr).scaled(cbabs))
    L=T(ell)+NA;B=T(bzero)+NB
    originalL=list(map(lambda x:up(box(x)),rt["L"]))
    L.z=min(L.z,originalL[0]).upper()
    L.d=min(L.d,originalL[1]).upper()
    J0=up(box(rt["J0"]));Jright=(CI*up(box(rt["J1"]))).upper()
    JJ=Budget(J0,J0*J0*originalL[1],Jright)
    SAC=((rank(U[1:],V,CI)+N(U[2:],V)+rank(V[1:],U,CI)+N(V[1:],U[1:]))
            .scaled(cabs*eta[0])
         +rank(ell,ell,CI)+T(ell)@NC+NA@T(ell)+NA@NC)
    SQ=(NAr+C(V[1:],U).scaled(cabs)+rank(ell,D[1:],CI)
        +rank(U[1:],U,CI).scaled(cabs*eta[0])
        +N(U[2:],U).scaled(cabs*eta[0])
        +rank(ell,ee,CI)+rank(tq,ell,CI)
        +T(ell)@NE+NA@T(ee)+NA@NE+T(tq)@NA)
    RQ=T(rq)+SQ
    SV=(rank(tq,bzero,CI)+rank(bzero,D[1:],CI)+T(tq)@NB
        +RQ@JJ@B+NBr+C(V[1:],V).scaled(cbabs)+SAC.scaled(K))
    products=dict(SQ=SQ,SAC=SAC,RQ=RQ,SV=SV,L=L,B=B,J=JJ,
        RQJ=RQ@JJ,RQJL=RQ@JJ@L,
        primitive=(T(V[1:])@primitive).scaled(cbabs),
        # M_u is used here before the final mean, not the zero-mean T_u.
        # Its identical upper z,d bounds are a valid larger full matrix.
        uJ=T(U)@JJ,uJL=T(U)@JJ@L,uJB=T(U)@JJ@B)
    # The T(U) Budget is only a bound object: its scalar z,d are also the
    # bounds for M_u. No P is inserted in the actual Pi M_u functional.
    s=ex(Q(5,3));sigma=ex(width)
    kappa=(sigma.exp()*powq(s/(arb(1).exp()*sigma),Q(5,3))).upper()
    names=dict(C_SV_directed="SV",C_SQ_directed="SQ",C_RQJ_directed="RQJ",
        C_RQJL_directed="RQJL",C_primitive_directed="primitive",
        C_uJ_directed="uJ",C_uJL_directed="uJL",C_uJB_directed="uJB")
    costs={}
    for key,name in names.items():
        gain=products[name].g
        if gain is None or not gain.is_finite():raise ValueError("a complete exact operator word lost its right gain: "+name)
        costs[key]=(kappa*gain).upper()
    evidence.update(kappa_5over3=compact(kappa),operator_words={k:x.record() for k,x in products.items()},
        after_single_Sobolev_conversion=encode(costs),
        all_old_mean_ranks_and_radial_terms_retained=True,
        parity_reflection_inserted_in_exponential_algebra=False)
    return costs,evidence

def coefficient_row(fr,rr):
    alternatives=[];widths=[]
    for width in WIDTHS:
        costs,evidence=width_budget(fr,rr,width);widths.append(evidence)
        if costs is not None:alternatives.append(costs)
    if not alternatives:raise ValueError("no original paid angular width closes its true full inverse")
    minima={key:min(d[key] for d in alternatives).upper() for key in FINITE_KEYS}
    if not all(x.is_finite() and x.lower()>=0 for x in minima.values()):
        raise ValueError("a complete directed matrix cost is invalid")
    return minima,widths

def source_constants(c,a,side):
    hi,hd,w,wr=a["hi"],a["hd"],a["w"],a["wr"]
    def A(v):
        if len(v)<3:raise ValueError("the old complete Airy amplitude lost two derivatives")
        total=arb(0)
        for p,q in a[side]:
            big=[max(x,y).upper() for x,y in zip(p,q)]
            total+=prior.old.one_phase(mul(big,v,2),a["m"],a["M"],a["F2"],a["F3"])
        return total.upper()
    def Dfrak(v,last):return mul(hi,v,last+1)[1:]
    def B(v):return (A(mul(hi,v,2))+A(Dfrak(v,2))).upper()
    def M0(v):return A(Dfrak(v,2))
    def M1(v):return A(Dfrak(Dfrak(v,3),2))
    hdw=mul(hd,w,4)
    h=scale(mul(hi,hdw,4),1/c["eta_lower"])
    y=mul(c["V"],mul(hi,hdw,4),4)
    dw=add(wr[:4],mul(c["D"],w[1:],3))
    gd=add(dw,scale(h[1:],c["eta_upper"]))
    qv=add(mul(c["V"],dw,3),y[1:])
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
        (M0(mul(c["U"],h,4))
         +c["C_uJ_directed"]*Bgd+c["C_uJL_directed"]*Bh+c["C_uJB_directed"]*Bw
         +c["K"]*M0(mul(vn,w,4)))).upper()
    first=(c["C_J_scalar"]*nl).upper()
    if not (first.is_finite() and mean.is_finite()):
        raise ValueError("a complete directed source cost is nonfinite")
    return first,mean,{k:v.upper() for k,v in terms.items()}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","root-native","forcing-native","seam-native","old-native","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all mathematics requires the actual public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):raise ValueError("the pinned runtime changed")
    if a.out.exists():raise FileExistsError("preserve every actual nonlocal remainder outcome")
    ctx.prec=256;started=time.monotonic()
    result=dict(kind="actual_complete_directed_matrix_old_circle_source_budget_v1",
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),runtime=runtime,complete=False,proved=False,failure=None,
        root_native_sha256=ROOT_SHA,first_forcing_native_sha256=FORCE_SHA,first_seam_native_sha256=SEAM_SHA,
        original_completed_norm_native_sha256=OLD_SHA,old_completed_moment_rows_recomputed=0,
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
                (a.forcing_native,FORCE_SHA,6577892),(a.seam_native,SEAM_SHA,904977),(a.old_native,OLD_SHA,4837715)):
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
                and previous["original_completed_norm_native_sha256"]==OLD_SHA)
            result["coefficient_rows"]=list(previous["coefficient_rows"])
            result["cases"]=list(previous["cases"])
        reused=len(result["coefficient_rows"]);result["coefficient_rows_reused"]=reused
        for index,fr in enumerate(force["rows"]):
            ri=fr["original_root_row"];rr=root["rows"][ri]
            oldrow=original_norm["coefficient_rows"][index]
            if oldrow["common_row"]!=index or oldrow["interval"]!=fr["interval"] or oldrow["original_root_row"]!=ri:
                raise ValueError("an original completed moment row changed its exact identity")
            lo,hi=map(Q,fr["interval"]);rlo,rhi=map(Q,rr["interval"])
            if not rlo<=lo<hi<=rhi:raise ValueError("a completed forcing row lost its original root cover")
            if index<reused:
                saved=result["coefficient_rows"][index]
                if saved["common_row"]!=index or saved["interval"]!=fr["interval"] or saved["original_root_row"]!=ri:
                    raise ValueError("a completed coefficient norm row changed identity")
                continue
            result["last_attempted_coefficient_row"]=dict(common_row=index,interval=fr["interval"])
            bounds,widths=coefficient_row(fr,rr)
            result["coefficient_rows"].append(dict(common_row=index,interval=fr["interval"],
                original_root_row=ri,original_completed_moment_row=index,bounds=encode(bounds),
                complete_width_evidence=widths))
            result["new_coefficient_norm_rows"]+=1;result.pop("last_attempted_coefficient_row",None)
            if index%128==0:checkpoint()
        check("all1328 original completed rows receive complete new directed matrix costs without old recomputation",
            len(result["coefficient_rows"])==1328
            and all(x["interval"][1]==y["interval"][0] for x,y in zip(
                result["coefficient_rows"],result["coefficient_rows"][1:]))
            and result["coefficient_rows"][:reused]==(previous or {}).get("coefficient_rows",[]))
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
            amplitude=amplitude_case(case,af,roots)
            out["constant_matrix_derivative_evidence"]=amplitude["matrix_evidence"]
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
                    out["rows"].append(item);result.pop("last_attempted_source_row",None)
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
            out["complete_original_matrix_widths"]=list(map(str,WIDTHS))
            out["original_complete_source_bounds_not_overwritten"]=True
            checkpoint()
        check("all six real root windows have complete old inverse and independent mean source budgets",
            len(result["cases"])==6 and all(c["complete"] and len(c["rows"])==c["complete_original_rows"]
                for c in result["cases"]))
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

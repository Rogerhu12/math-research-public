#!/usr/bin/env python3
"""Complete leading old-circle inverse remainder and even-mean source budgets.

Only consume completed original root/forcing/seam natives. All new numerical
work is explicit scalar norm arithmetic on saved complete rows and intervals.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_actual_first_Airy_seam_operators as old

PUBLIC="Rogerhu12/math-research-public"
ROOT_SHA="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
FORCE_SHA="54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47"
SEAM_SHA="871aa54de8c4ee1caa47cdab39c8033bb9cd02e9d4d1f404b711ab8c28825642"
DELTA=Q(1,100000000)
SIGMA=Q(1,16);AMPLITUDE_SIGMA=Q(3,64);CUTOFF=97
ex,box,up,ipow,powq=old.ex,old.box,old.up,old.ipow,old.powq
read,save,sha=old.read,old.save,old.sha
def rec(v):return old.fullrec(arb(v))
def compact(v):return dict(ball=arb(v).str(48))
def encode(d):
    return {k:([compact(v) for v in x] if isinstance(x,list) else compact(x)) for k,x in d.items()}
def decode(d):return {k:([box(v) for v in x] if isinstance(x,list) else box(x)) for k,x in d.items()}
def add(*arrays):return [sum((a[k] for a in arrays),arb(0)).upper() for k in range(min(map(len,arrays)))]
def scale(a,c):return [(x*c).upper() for x in a]
def mul(a,b,n=None):
    n=min(len(a),len(b))-1 if n is None else n
    if n>=min(len(a),len(b)):raise ValueError("an ordinary angular jet is missing")
    return [sum((math.comb(k,j)*a[j]*b[k-j] for j in range(k+1)),arb(0)).upper()
            for k in range(n+1)]
def moment(a,start=0):
    if start+3>=len(a):raise ValueError("the complete third moment lacks derivatives")
    return sum((math.comb(3,k)*a[start+k] for k in range(4)),arb(0)).upper()
def finite_nonnegative(a):
    return a.is_finite() and a.lower()>=0

def real_jets(saved,last,mean=None):
    """B.1: every option is a bound for the entire old circle."""
    vals=list(map(lambda x:up(box(x)),saved));sigma=ex(SIGMA);decay=(-4*sigma).exp()
    out=[]
    for q in range(last+1):
        options=[]
        for p,value in enumerate(vals):
            if q==0 and p==0:
                options.append((decay*value if mean is not None and mean==0 else value).upper())
                continue
            k=q-p
            if k>0:factor=ipow(ex(k)/(arb(1).exp()*sigma),k)
            elif k==0:factor=decay
            else:factor=ex(Q(4)**k)*decay
            candidate=(factor*value).upper()
            if q==0 and p>0:
                if mean is None:continue
                candidate=(candidate+mean).upper()
            options.append(candidate)
        if not options:raise ValueError("no full derivative enclosure")
        out.append(min(options).upper())
    return out

def coefficient_row(fr,rr):
    st=fr["strips"]["1/16"];rt=rr["strips"]["1/16"]
    jets=fr["complete_intrinsic_ordinary_jets"]
    eta=list(map(lambda x:up(box(x)),fr["full_actual_eta_derivatives"]))
    en=box(rr["bounds"]["eta_lower"]).lower()
    if not en>0:raise ValueError("the actual old-circle eta gap failed")
    mean=list(map(lambda x:up(box(x)),fr["full_actual_mean_derivatives"]))
    U=real_jets(rt["U"],5,arb(0));V=real_jets(rt["V"],5,mean[0])
    Ur=real_jets(st["U_radial"][0],4,arb(0))
    Vr=real_jets(st["V_radial"][0],4,mean[1])
    D=real_jets(st["D"],5,arb(0))
    b=up(box(jets["beta"][0]));br=up(box(jets["beta"][1]))
    K=up(box(jets["K"][0]));Kr=up(box(jets["K"][1]))
    c=2*b;cr=2*br;cb=2*b*K;cbr=2*(br*K+b*Kr)
    one=[arb(1)]+[arb(0)]*4
    uu=mul(U,U,4);vv=mul(V,V,4);uv=mul(U,V,4)
    ell=scale(uv,c)
    ellr=add(scale(uv,cr),scale(add(mul(Ur,V,4),mul(U,Vr,4)),c))
    e=scale(add(one,scale(uu,3),scale(vv,K)),b)
    bzero=scale(add(one,uu,scale(vv,3*K)),b)
    bzeror=add(scale(add(one[:4],uu[:4],scale(vv[:4],3*K)),br),
        scale(mul(Ur,U,3),2*b),scale(vv[:4],3*b*Kr),
        scale(mul(Vr,V,3),6*b*K))
    eta_ratio=(eta[1]/en).upper()
    tq=add(D[1:5],e[:4],[eta_ratio,arb(0),arb(0),arb(0)])
    rq=add(ellr[:4],mul(D,ell[1:],3),scale(e[1:5],eta[0]),
        scale(mul(U[1:],U,3),c*eta[0]),
        mul(ell,add(D[1:5],[eta_ratio,arb(0),arb(0),arb(0)]),3))
    vac=add(mul(ell,ell,3),scale(mul(V,U[1:],3),4*b*eta[0]))
    vzero=add(mul(tq,bzero,3),bzeror,mul(D,bzero[1:],3),scale(vac,K))
    # Original analytic bounds remain available as independent full estimates.
    rq_cap=real_jets([st["rQ0"]],3)
    v_cap=real_jets([st["V0"]],3)
    rq=[min(x,y).upper() for x,y in zip(rq,rq_cap)]
    vzero=[min(x,y).upper() for x,y in zip(vzero,v_cap)]
    tzero=[up(box(st["T0"]))]+[5*D[k+1] for k in range(1,4)]
    mu,mv,mu1,mv1=moment(U),moment(V),moment(U,1),moment(V,1)
    mu2,mv2=moment(U,2),moment(V,2)
    mur,mvr,mur1,mvr1=moment(Ur),moment(Vr),moment(Ur,1),moment(Vr,1)
    md,md1=moment(D),moment(D,1)
    ml,me,mb,mt,mrq=moment(ell),moment(e),moment(bzero),moment(tq),moment(rq)
    CI=ex(Q(17)).sqrt()/4
    NA0=c*mv1*mu/4;NA1=c*CI*mv1*mu
    NC0=c*mu1*mv/4;NC1=c*CI*mu1*mv
    NE0=c*mu1*mu/4;NE1=c*CI*mu1*mu
    NB1=cb*CI*mv1*mv
    def comm(p,p1,q,q1):return CI*(md*(p1*q+p*q1)+3*p*md1*q)
    nar=CI*(cr*mv1*mu+c*(mvr1*mu+mv1*mur))
    nbr=CI*(cbr*mv1*mv+cb*(mvr1*mv+mv1*mvr))
    CQ=(nar+c*comm(mv1,mv2,mu,mu1)+ml*md1
        +c*eta[0]*mu1*mu+c*eta[0]*CI*mu2*mu
        +ml*me+mt*ml+ml*NE1+NA1*me+NA1*NE0+mt*NA1).upper()
    CAC=(c*eta[0]*(mu1*mv+CI*mu2*mv+mv1*mu+CI*mv1*mu1)
        +ml*ml+ml*NC1+NA1*ml+NA1*NC0).upper()
    hs=list(map(box,rr["strips"]["1/64"]["one_gain"]))
    CJ=(powq(hs[1],Q(1,3))*powq(hs[2],Q(2,3))).upper()
    CJminus=up(box(rr["strips"]["1/64"]["J_Hminus5over3_to_Hminus2over3"]))
    CR=(mrq+CQ).upper();CL=(ml+NA0).upper();CB=(mb+cb*mv1*mv/4).upper()
    CV=(mt*mb+mb*md1+mt*NB1+CR*CJ*CB+nbr
        +cb*comm(mv1,mv2,mv,mv1)+K*CAC).upper()
    out=dict(U=U,V=V,Ur=Ur,Vr=Vr,D=D,eta_lower=en,eta_upper=eta[0],mean_upper=mean[0],
        beta=b,K=K,cB=cb,C_I=CI,C_Q=CQ,C_AC=CAC,C_R=CR,C_L=CL,C_B=CB,C_V=CV,
        C_J_new=CJ,C_J_scalar=CJminus,m3_u=mu,m3_vphi=mv1,
        m0_rQ=rq[0],m0_T0=tzero[0],m0_V0=vzero[0],
        m3_rQ=mrq,m3_ell=ml,m3_tQ=mt,m3_b0=mb,
        exact_nonlocal_even_mean_row_factor=(2*b*mean[0]).upper())
    if any(not finite_nonnegative(x) for val in out.values() for x in (val if isinstance(val,list) else [val])):
        raise ValueError("a complete original coefficient norm is not finite and nonnegative")
    return out

def cauchy_jets(known,last=4):
    sigma=ex(AMPLITUDE_SIGMA)
    return [min((math.factorial(k-p)*v/ipow(sigma,k-p)).upper()
                for p,v in known.items() if p<=k).upper() for k in range(last+1)]

def amplitude_case(case,af,roots):
    v={k:box(x) for k,x in case["bounds"].items()}
    R=ex(Q(case["exact_radius"])+roots[1]-roots[0])
    Am=v["A_lower"].lower();Ap=v["A_upper"].upper();ap=v["a_upper"].upper()
    if not (R>0 and Am>0):raise ValueError("an actual amplitude window lost its root gaps")
    # D1 is the same actual whole-window coefficient used by the completed forcing.
    E=box(af["flow_variational_C"]["1"]).upper()
    j=(E-1).upper();Aphi=(R*box(af["A_angular_constants"]["1"])).upper()
    App=(R*box(af["A_angular_constants"]["2"])).upper()
    Y=(ex(Q(2,3))*R*powq(Am,Q(-1,3))*Aphi).upper()
    T=(R*powq(Ap,Q(2,3))).upper();maxT=max(arb(1),T)
    Hi=up(box(af["matrix_H_inverse_l1"]));HD=up(box(af["matrix_HD_l1"]))
    deltaH=(j+maxT*Y).upper()
    deltaA=(ap*j).upper()
    deltaT=(ex(Q(2,3))*R*powq(Am,Q(-1,3))*deltaA).upper()
    deltaDT=(ap*(powq(Am,Q(-1,3))*j+powq(Am,Q(-4,3))*deltaA/3)).upper()
    DX=(ex(Q(2,3))*ap*ipow(R,2)*Aphi).upper()
    deltaHD=(DX+maxT*deltaDT+ap*powq(Am,Q(-1,3))*deltaT).upper()
    hi=[Hi]+[(math.factorial(k)*Hi*min(arb(1),deltaH)/ipow(ex(AMPLITUDE_SIGMA),k)).upper() for k in range(1,5)]
    hd=[HD]+[(math.factorial(k)*min(HD,deltaHD)/ipow(ex(AMPLITUDE_SIGMA),k)).upper() for k in range(1,5)]
    aa=af["leading_a0_derivative_bounds"];bb=af["leading_b0_derivative_bounds"]
    w=cauchy_jets({k:up(box(aa[str((0,k))]))+up(box(bb[str((0,k))])) for k in range(3)})
    wr=cauchy_jets({k:up(box(aa[str((1,k))]))+up(box(bb[str((1,k))])) for k in range(2)})
    L1=(ex(Q(2,3))*Aphi/Am).upper()
    L2=(ex(Q(2,3))*(App/Am+ipow(Aphi/Am,2))).upper()
    m=(2-E).lower();M=E;F2=R*box(af["flow_variational_C"]["2"]);F3=R*box(af["flow_variational_C"]["3"])
    if not m>0:raise ValueError("the complete real circle map ceased to be invertible")
    H=powq(Am,Q(-1,6));N=powq(R,Q(1,4))*powq(4*CUTOFF,Q(-1,6))
    high=powq(R,Q(1,2))*powq(Ap,Q(1,6))
    def sc(a,l):return [(a*x).upper() for x in l]
    negative=[
      (sc(H,[16,94*L1,1208*ipow(L1,2)+94*L2]),sc(N,[8,51*L1,650*ipow(L1,2)+51*L2])),
      (sc(H,[3,16*L1,209*ipow(L1,2)+16*L2]),sc(high,[4,22*L1,290*ipow(L1,2)+22*L2])),
      (sc(H,[3,16*L1,209*ipow(L1,2)+16*L2]),sc(high,[4,22*L1,290*ipow(L1,2)+22*L2]))]
    positive=[(sc(H,[3,3*L1,5*ipow(L1,2)+3*L2]),sc(N,[3,3*L1,6*ipow(L1,2)+3*L2]))]
    return dict(R=R,hi=hi,hd=hd,w=w,wr=wr,m=m,M=M,F2=F2,F3=F3,
                negative=negative,positive=positive,
                matrix_evidence=encode(dict(H_inverse=Hi,H_inverse_oscillation=Hi*deltaH,
                    HD=HD,HD_oscillation=deltaHD,A_radial_reference_deviation=deltaA,
                    Xphi_deviation=j,Tphi=Y,T_bound=T)))

def source_constants(c,a,side):
    hi,hd,w,wr=a["hi"],a["hd"],a["w"],a["wr"]
    def A(v):
        if len(v)<3:raise ValueError("a complete Airy amplitude lost two angular derivatives")
        total=arb(0)
        for p,q in a[side]:
            big=[max(x,y).upper() for x,y in zip(p,q)]
            triple=mul(big,v,2)
            total+=old.one_phase(triple,a["m"],a["M"],a["F2"],a["F3"])
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
    Bh=B(h);Bw=B(w)
    ED=(B(gd)+c["C_L"]*Bh).upper()
    MD=(M1(hdw)+M0(dw)).upper()
    terms=dict(
        complete_SV=c["C_V"]*Bw,
        complete_SQ=c["C_Q"]*Bh,
        complete_RQ_J_error=c["C_R"]*c["C_J_new"]*ED,
        complete_primitive_error=c["cB"]*c["m3_vphi"]*c["C_I"]*B(qv),
        old_mean_rQ=c["m0_rQ"]*M0(h),
        old_mean_vphi=c["cB"]*c["V"][1]*M0(y),
        old_mean_raw_D=(c["cB"]*c["V"][1]*c["V"][0]/4+c["m0_T0"])*MD,
        old_mean_V0=c["m0_V0"]*M0(w))
    nl=sum(terms.values(),arb(0)).upper()
    vn=list(c["V"]);vn[0]=min(vn[0],vn[1]/4).upper()
    mean=(c["exact_nonlocal_even_mean_row_factor"]*
        (M0(mul(c["U"],h,4))
         +c["m3_u"]*c["C_J_new"]*(ED+c["C_B"]*Bw)
         +c["K"]*M0(mul(vn,w,4)))).upper()
    first=(c["C_J_scalar"]*nl).upper()
    if not (first.is_finite() and mean.is_finite()):raise ValueError("a complete source constant is not finite")
    return first,mean,{k:v.upper() for k,v in terms.items()}

def radial_weight(left,right,roots,side):
    lo,hi=roots
    if not left<right:raise ValueError("empty actual common row")
    if right<=lo:
        if side=="positive":return arb(0)
        return (2*(ex(lo-left).sqrt()-ex(lo-right).sqrt())).upper()
    if left>=hi:
        if side=="negative":return arb(0)
        return (2*(ex(right-hi).sqrt()-ex(left-hi).sqrt())).upper()
    if not lo<=left<right<=hi:raise ValueError("a saved common row crossed a true root endpoint")
    return (2*ex(right-left).sqrt()).upper()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","root-native","forcing-native","seam-native","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all mathematics requires the actual public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):raise ValueError("the pinned runtime changed")
    if a.out.exists():raise FileExistsError("preserve every actual nonlocal remainder outcome")
    ctx.prec=256;started=time.monotonic()
    result=dict(kind="actual_complete_leading_old_circle_remainder_source_budget_v1",
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),runtime=runtime,complete=False,proved=False,failure=None,
        root_native_sha256=ROOT_SHA,first_forcing_native_sha256=FORCE_SHA,first_seam_native_sha256=SEAM_SHA,
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
                (a.forcing_native,FORCE_SHA,6577892),(a.seam_native,SEAM_SHA,904977)):
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
                and previous["first_seam_native_sha256"]==SEAM_SHA and previous["runtime"]==runtime)
            result["coefficient_rows"]=list(previous["coefficient_rows"])
            result["cases"]=list(previous["cases"])
        reused=len(result["coefficient_rows"]);result["coefficient_rows_reused"]=reused
        for index,fr in enumerate(force["rows"]):
            ri=fr["original_root_row"];rr=root["rows"][ri]
            lo,hi=map(Q,fr["interval"]);rlo,rhi=map(Q,rr["interval"])
            if not rlo<=lo<hi<=rhi:raise ValueError("a completed forcing row lost its original root cover")
            if index<reused:
                saved=result["coefficient_rows"][index]
                if saved["common_row"]!=index or saved["interval"]!=fr["interval"] or saved["original_root_row"]!=ri:
                    raise ValueError("a completed coefficient norm row changed identity")
                continue
            result["last_attempted_coefficient_row"]=dict(common_row=index,interval=fr["interval"])
            bounds=coefficient_row(fr,rr)
            result["coefficient_rows"].append(dict(common_row=index,interval=fr["interval"],
                original_root_row=ri,bounds=encode(bounds)))
            result["new_coefficient_norm_rows"]+=1;result.pop("last_attempted_coefficient_row",None)
            if index%128==0:checkpoint()
        check("all1328 original closed rows receive their complete new moment and inverse-window costs",
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
                    c=decode(saved["bounds"]);item=dict(common_row=saved["common_row"],interval=saved["interval"])
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
            keys=("C_Q","C_AC","C_R","C_L","C_B","C_V","C_J_new","C_J_scalar",
                  "m3_rQ","m3_ell","m3_tQ","m3_b0")
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

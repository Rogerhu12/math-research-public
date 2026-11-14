#!/usr/bin/env python3
"""Complete actual first-amplitude seam operators, with all Fourier outputs.

Read two completed actual natives and their process receipts. Aggregate already
proved forcing rows on six original root windows and evaluate the first state
seam operators. No original target, coefficient, ray or amplitude solve is rerun.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,sys,time
from bisect import bisect_right
from fractions import Fraction as Q
from pathlib import Path
import flint
import numpy as np
from flint import arb,ctx
import fourfold_codazzi_actual_first_Airy_forcing as original_forcing

PUBLIC="Rogerhu12/math-research-public"
ROOT_SHA="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
ROOT_BYTES=5923431
ROOT_SOURCE="840d7ae96c023f0f1055516cfefe62f22a8f46a3f8a0ea2974553b32760eb112"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
DELTA=Q(1,100000000)
CUTOFF=97
SIGMA=Q(3,64)

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,separators=(",",":"),allow_nan=False)+"\n").encode()
    out=gzip.compress(raw,compresslevel=9,mtime=0) if p.suffix==".gz" else raw
    q=p.with_name(p.name+".partial");q.write_bytes(out);q.replace(p)
def ex(v):
    v=Q(v);return arb(v.numerator)/v.denominator
def box(d):
    if "lower" in d and "upper" in d:return arb(d["lower"]).lower().union(arb(d["upper"]).upper())
    return arb(d["ball"])
def up(v):return abs(v).upper()
def rec(v):return {"ball":arb(v).str(48)}
def fullrec(v):
    v=arb(v)
    return dict(ball=v.str(60),lower=v.lower().str(60),upper=v.upper().str(60))
def powq(v,p):return (arb(v).log()*ex(p)).exp()
def ipow(v,k):
    """Bounded products avoid the general-power zero-crossing runtime entry."""
    if k<0:return 1/ipow(v,-k)
    out=arb(1)
    for _ in range(k):out=out*v
    return out
def enc(d):return {str(k):([rec(x) for x in v] if isinstance(v,list) else rec(v)) for k,v in d.items()}
def pairproduct(p,a,q,b):
    return [sum((math.comb(k,l)*(p[l]*a[k-l]+q[l]*b[k-l])
                    for l in range(k+1)),arb(0)).upper() for k in range(3)]

def schur(B0,B2,J=CUTOFF):
    lam=(1+16*ipow(arb(J),2)).sqrt()
    return (powq(2,Q(5,3))*powq(lam,Q(-1,3))*(B0+ipow(arb.pi(),2)*B2/48)
        +8*B2*(powq(J,Q(-4,3))+3*powq(J,Q(-1,3))).sqrt()).upper()

def composition(m,M,F2,F3):
    P2=F2/ipow(m,3);P3=F3/ipow(m,4)+3*ipow(F2,2)/ipow(m,5)
    C0=1/m.sqrt()
    C2=(M*(ipow(m,-2)+2*ipow(P2,2)+ipow(m,-4)+ipow(P3,2)+ex(Q(9,2))*ipow(P2,2)/ipow(m,2)+ipow(m,-6))).sqrt()
    return powq(C0,Q(1,6))*powq(C2,Q(5,6))

def one_phase(triple,m,M,F2,F3):
    D0,D1,D2=triple
    transformed=(D2/ipow(m,2)+D1*F2/ipow(m,3)).upper()
    return (composition(m,M,F2,F3)*schur(D0,transformed)).upper()

def profile_triples(side,hmin,hmax,L1,L2):
    H=powq(hmin,Q(-1,4));N=powq(4*CUTOFF,Q(-1,6))
    def scaled(t,v):return [(t*x).upper() for x in v]
    if side=="positive":
        return [("central_X",scaled(H,[3,3*L1,5*ipow(L1,2)+3*L2]),
                 scaled(N,[3,3*L1,6*ipow(L1,2)+3*L2]))]
    high=powq(hmax,Q(1,4))
    return [
        ("central_X",scaled(H,[16,94*L1,1208*ipow(L1,2)+94*L2]),
         scaled(N,[8,51*L1,650*ipow(L1,2)+51*L2])),
        ("actual_root_ray_plus",scaled(H,[3,16*L1,209*ipow(L1,2)+16*L2]),
         scaled(high,[4,22*L1,290*ipow(L1,2)+22*L2])),
        ("actual_root_ray_minus",scaled(H,[3,16*L1,209*ipow(L1,2)+16*L2]),
         scaled(high,[4,22*L1,290*ipow(L1,2)+22*L2]))]

def aggregate_completed_forcing_rows(rows):
    """Only take maxima of already proved and saved actual row enclosures."""
    scalar=("gamma_upper","T0","V0","vartheta","log_EG_r","log_EG_rr")
    glob={k:arb(0) for k in scalar}
    glob.update(D=[arb(0)]*6,Dr=[arb(0)]*3,K_derivatives=[arb(0)]*4,
                eta_derivatives=[arb(0)]*4,J_radial=[arb(0)]*3)
    def maximum(x,y):return max(up(x),up(y)).upper()
    for row in rows:
        st=row["strips"]["1/16"]
        for key in ("D","Dr"):
            glob[key]=[maximum(x,box(y)) for x,y in zip(glob[key],st[key])]
        for key in ("T0","V0","vartheta","log_EG_r","log_EG_rr"):
            glob[key]=maximum(glob[key],box(st[key]))
        gj=row["complete_intrinsic_ordinary_jets"]
        glob["gamma_upper"]=maximum(glob["gamma_upper"],box(gj["gamma"][0]))
        glob["K_derivatives"]=[maximum(x,box(y)) for x,y in zip(glob["K_derivatives"],gj["K"])]
        glob["eta_derivatives"]=[maximum(x,box(y)) for x,y in zip(
            glob["eta_derivatives"],row["full_actual_eta_derivatives"])]
        glob["J_radial"]=[maximum(x,box(y)) for x,y in zip(
            glob["J_radial"],row["strips"]["1/32"]["J_radial"])]
    return glob

def decode_bounds(d):
    return {k:([box(x) for x in v] if isinstance(v,list) else box(v)) for k,v in d.items()}

def actual_seam(s,row,roots,glob,forcing,selected):
    r=Q(s["radial"])
    if r<roots[0]:
        side="negative";rmin=roots[0]-r;rmax=roots[1]-r
    elif r>roots[1]:
        side="positive";rmin=r-roots[1];rmax=r-roots[0]
    else:raise ValueError("an original seam meets the certified true root")
    rho=ex(rmax);distance=ex(rmin)
    rb={k:box(v) for k,v in row["bounds"].items()}
    st=row["strips"]["1/16"]
    U=box(st["U"][0]);V=box(st["V"][0]);b=rb["beta"]
    en=rb["eta_lower"].lower();km=rb["k_upper"].upper()
    kval=(km*rho).upper()
    values={k:box(v) for k,v in selected["bounds"].items()}
    Am=values["A_lower"].lower();Ap=values["A_upper"].upper()
    G=values["leading_G"].upper()
    gap=values["fold_noncharacteristic_gap"].lower()
    mu=values["principal_mu_abs_lower"].lower()
    amax=rb["a_upper"].upper()
    D0=box(glob["D"][0]);D1=box(glob["D"][1])
    C2=box(forcing["flow_variational_C"]["2"]);C3=box(forcing["flow_variational_C"]["3"])
    cA1=box(forcing["A_angular_constants"]["1"]);cA2=box(forcing["A_angular_constants"]["2"])
    E=(D1*rho).exp().upper()
    Aphi=(rho*cA1).upper();App=(rho*cA2).upper();Xpp=(rho*C2).upper()
    Tphi=(ex(Q(2,3))*rho*powq(Am,Q(-1,3))*Aphi).upper()
    Tupper=(rho*powq(Ap,Q(2,3))).upper()
    Tlower=(distance*powq(Am,Q(2,3))).lower()
    gamma=box(glob["gamma_upper"])
    first=s["radial_derivatives"]["1"]
    Jpair=box(first["full_complex_family_pair_angular_norms"]["1/16"]["0"])
    mean=ex(abs(Q(first["base_even_mean_jump_exact"]))+DELTA*abs(Q(first["direction_even_mean_jump_exact"])))
    deta=(gamma*mean).upper();da=(gamma*km.sqrt()*mean).upper()
    dS=(2*(U+kval*V)*Jpair).upper()
    dd=(b*dS/4).upper();ddp=(b*dS).upper()
    dell=(2*b*(U+V)*Jpair).upper()
    db0=(2*b*(U+3*kval*V)*Jpair).upper()
    ell=(2*b*U*V).upper();b0=(b*(1+U*U+3*kval*V*V)).upper()
    Arr=(dd*Aphi+ex(Q(3,2))*da*E/distance).upper()
    Aprr=(ddp*Aphi+dd*App+ex(Q(3,2))*da*Xpp/distance).upper()
    Xprr=(ddp*E+dd*Xpp+ex(Q(2,3))*da*ipow(rho,2)*App).upper()
    Trr=(ex(Q(2,3))*rho*powq(Am,Q(-1,3))*Arr).upper()
    Tprr=(ex(Q(2,3))*rho*(powq(Am,Q(-1,3))*Aprr
                 +powq(Am,Q(-4,3))*Aphi*Arr/3)).upper()
    Grr=(G*(Arr/(6*Am)+2*b*dS)).upper()
    a0rr=(Grr*(E*E+Tupper*Tphi*Tphi)
          +G*(2*E*Xprr+Trr*Tphi*Tphi+2*Tupper*Tphi*Tprr)).upper()
    b0rr=(2*(Grr*E*Tphi+G*(Xprr*Tphi+E*Tprr))).upper()
    a0={k:box(v) for k,v in forcing["leading_a0_derivative_bounds"].items()}
    ab0={k:box(v) for k,v in forcing["leading_b0_derivative_bounds"].items()}
    Wa,Wb=a0["(0, 0)"],ab0["(0, 0)"]
    Wpa,Wpb=a0["(0, 1)"],ab0["(0, 1)"]
    WDa=(a0["(1, 0)"]+D0*Wpa).upper()
    WDb=(ab0["(1, 0)"]+D0*Wpb).upper()
    DX=(ex(Q(2,3))*amax*ipow(rho,2)*Aphi).upper()
    DT=(amax*powq(Am,Q(-1,3))*E).upper()
    matrix_diag=((E*DX+Tupper*Tphi*DT)/gap).upper()
    matrix_off=((E*DT+Tphi*DX)/gap).upper()
    dT0=(deta/en).upper();dV=(dT0*b0+db0).upper()
    dvartheta=(dell/en+ell*deta/ipow(en,2)).upper()
    # The ordered pair is (F_b,F_a), not (F_a,F_b).
    Fb=((a0rr+dd*Wpa+dT0*WDa+dV*Wa
            +dvartheta*(matrix_diag*Wa+Tupper*matrix_off*Wb))/mu).upper()
    Fa=((b0rr+dd*Wpb+dT0*WDb+dV*Wb
            +dvartheta*(matrix_off*Wa+matrix_diag*Wb))/mu).upper()
    pref=(amax*powq(Am,Q(-1,3))/2).upper()
    ja=(pref*(E*Fa+Tphi*Fb)).upper()
    jb=(pref*(Tphi*Fa+E*Fb/Tlower)).upper()
    aj=[(math.factorial(k)*ja/ipow(ex(SIGMA),k)).upper() for k in range(3)]
    bj=[(math.factorial(k)*jb/ipow(ex(SIGMA),k)).upper() for k in range(3)]
    L1=(ex(Q(2,3))*Aphi/Am).upper()
    L2=(ex(Q(2,3))*(App/Am+ipow(Aphi/Am,2))).upper()
    hmin=Tlower;hmax=Tupper
    # X is a real circle map on both sides; only negative rays are real maps.
    m=(2-E).lower();M=E
    F2=(rho*C2).upper();F3=(rho*C3).upper()
    if not (m>0 and en>0 and Am>0 and Tlower>0 and gap>0 and mu>0):
        raise ValueError("an actual seam lost a true denominator or real circle-map gap")
    phases=[];airy=arb(0)
    for name,p,q in profile_triples(side,hmin,hmax,L1,L2):
        triple=pairproduct(p,aj,q,bj)
        value=one_phase(triple,m,M,F2,F3)
        airy+=value
        phases.append(dict(phase=name,full_symbol_derivatives=list(map(rec,triple)),
                           complete_Hminus4over3_to_Hminus5over3=rec(value)))
    js=box(row["strips"]["1/64"]["J_Hminus5over3_to_Hminus2over3"])
    fee=(js*airy).upper()
    if not fee.is_finite():raise ValueError("the complete actual seam operator is not finite")
    return dict(radial=s["radial"],side=side,left_piece=s["left_piece"],right_piece=s["right_piece"],
        exact_minimum_root_distance=str(rmin),exact_maximum_root_distance=str(rmax),
        original_first_derivative_component_jump_sha256=first["complete_exact_component_jump_sha256"],
        original_first_derivative_pair_norm=rec(Jpair),exact_mean_jump_absolute_bound=str(
            abs(Q(first["base_even_mean_jump_exact"]))+DELTA*abs(Q(first["direction_even_mean_jump_exact"]))),
        full_degree_zero_forcing_jump=enc(dict(F_b=Fb,F_a=Fa)),
        first_amplitude_radial_jumps=enc(dict(a=ja,b=jb)),
        exact_Hinverse_HD_entry_bounds=enc(dict(diagonal=matrix_diag,off_diagonal=matrix_off)),
        real_circle_map_bounds=enc(dict(lower=m,upper=M,second=F2,third=F3)),
        logarithmic_T_angular_bounds=enc(dict(first=L1,second=L2)),
        full_Airy_profile_phases=phases,complete_old_J_one_gain=rec(js),
        complete_first_state_jump_Hminus4over3_to_Hminus2over3_times_Hminus1=rec(fee),
        exact_second_state_row_jump="0",old_mean_and_parity_projections_retained=True,
        positive_weighted_affine_port_conversion_claimed=False)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--root-native",type=Path,required=True)
    ap.add_argument("--forcing-native",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--resume",type=Path)
    a=ap.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all mathematics requires the actual public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):raise ValueError("the directed runtime changed")
    if a.out.exists():raise FileExistsError("preserve every actual seam prefix")
    ctx.prec=256;started=time.monotonic()
    result=dict(kind="actual_complete_first_Airy_seam_operator_in_mixed_source_window_v1",
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),runtime=runtime,complete=False,proved=False,failure=None,
        input_cutoff=CUTOFF,physical_frequency="4|j|",exact_real_delta_radius=str(DELTA),
        actual_coefficient_or_target_rows_recomputed=0,actual_amplitude_or_ray_solves_recomputed=0,
        source_window="H^-4/3 -> H^-2/3 x H^-1",density_input_normalization="n^(7/6)",
        old_mean_full_output_and_head_rows_retained=True,
        positive_weighted_affine_port_conversion_claimed=False,
        complete_strong_return_norm_evaluated=False,numerical_cutoff97_inverse_claimed=False,
        actual_PDE_branch_claimed=False,gates=[],seams=[],refined_forcing_radius_cases=[])
    def check(name,truth):
        okay=bool(truth);result["gates"].append(dict(name=name,passed=okay))
        if not okay:raise ValueError("actual seam gate failed: "+name)
    try:
        manifest=read(a.manifest);result["input_manifest_sha256"]=sha(a.manifest)
        for item in manifest["files"]:
            p=a.repo_root/item["path"]
            if not p.is_file() or sha(p)!=item["sha256"] or p.stat().st_size!=item["bytes"]:
                raise ValueError("an original actual input or exact source changed: "+item["path"])
        check("the exact original complete root native has all1300 closed rows",
            sha(a.root_native)==ROOT_SHA and a.root_native.stat().st_size==ROOT_BYTES)
        root=read(a.root_native)
        check("the actual repaired full real family and every root gate remain complete",
            root["complete"] and root["proved"] and root["failure"] is None
            and root["source_sha256"]==ROOT_SOURCE and str(root["public_run_id"])=="43616813816"
            and root["background_definition_sha256"]==BASE and root["explicit_direction_definition_sha256"]==ZDEF
            and len(root["rows"])==1300 and len(root["seams"])==1079
            and all(g["passed"] for g in root["gates"]) and root["selected"]["exact_radius"]=="1/50")
        fp=a.repo_root/manifest["input_paths"]["forcing_process"]
        forcing_process=read(fp);fid=manifest["forcing_identity"]
        check("the complete actual first forcing and all true source gates were proved",
            forcing_process["actual_returncode"]==0 and forcing_process["complete"]
            and forcing_process["mathematical_complete"] and forcing_process["mathematical_failure"] is None
            and str(forcing_process["run_id"])==str(fid["run_id"])
            and forcing_process["mathematical_source_sha256"]==fid["source_sha256"]
            and forcing_process["native_sha256"]==fid["native_sha256"]
            and forcing_process["manifest_sha256"]==fid["manifest_sha256"]
            and all(g["passed"] for g in forcing_process["mathematical_gates"])
            and forcing_process["exact_real_delta_radius"]==str(DELTA))
        cauchy=read(a.repo_root/manifest["input_paths"]["negative_cauchy_summary"])
        cauchy_process=read(a.repo_root/manifest["input_paths"]["negative_cauchy_process"])
        check("the actual same-family large-root negative propagation passed all eight gates",
            cauchy["complete"] and cauchy["failure"] is None and len(cauchy["gates"])==8
            and all(g["passed"] for g in cauchy["gates"])
            and cauchy["native_sha256"]=="3a214897f5dc47e1a1fed3db327f54fcc0302ad6fd273ea96ecdbfcc0ca4f1e0"
            and cauchy["source_sha256"]=="9acc1e8187663b91845347878034a384f5ff25b939e7faa0a1ab72f7f8738de9"
            and cauchy["input_sha256"]["root-native"]==ROOT_SHA
            and cauchy["background_definition_sha256"]==BASE
            and cauchy["explicit_direction_definition_sha256"]==ZDEF
            and cauchy["exact_real_delta_radius"]==str(DELTA)
            and cauchy["exact_root_interval"]==root["exact_root_interval"]
            and cauchy["source_windows"]["Hminus1"]["root_and_jumps"]==["Hminus2/3","Hminus1"]
            and cauchy["all_frequencies_and_independent_even_mean_retained"] is True
            and cauchy_process["complete"] and str(cauchy_process["run_id"])=="43621934843"
            and cauchy_process["complete_native_sha256"]==cauchy["native_sha256"]
            and len(cauchy_process["children"])==1
            and cauchy_process["children"][0]["actual_returncode"]==0)
        if sha(a.forcing_native)!=fid["native_sha256"] or a.forcing_native.stat().st_size!=fid["native_bytes"]:
            raise ValueError("the completed original first-forcing native differs")
        forcing_native=read(a.forcing_native)
        check("the completed first-forcing rows are reused without polynomial or target reevaluation",
            forcing_native["complete"] and forcing_native["proved"] and forcing_native["failure"] is None
            and forcing_native["source_sha256"]==fid["source_sha256"]
            and forcing_native["input_manifest_sha256"]==fid["manifest_sha256"]
            and forcing_native["root_native_sha256"]==ROOT_SHA
            and forcing_native["exact_root_interval"]==root["exact_root_interval"]
            and len(forcing_native["rows"])==forcing_native["accepted_closed_rows"]
            and forcing_native["prefix_global_accepted_rows"]==len(forcing_native["rows"])
            and forcing_native["exact_cover"]==root["exact_cover"]
            and all(g["passed"] for g in forcing_native["gates"]))
        f=forcing_process["actual_forcing"];glob=forcing_process["global_coefficient_and_inverse_bounds"]
        check("the actual first-forcing coefficient and leading domains contain the full seam strip",
            f["first_forcing_is_the_complete_actual_degree_zero_operator"] is True
            and Q(f["exact_radius"])==Q(1,50) and Q(f["leading_strip"])>=SIGMA
            and f["full_branch_factors_retained"] is True)
        Ai0=1/(powq(3,Q(2,3))*ex(Q(2,3)).gamma())
        Aip0=-1/(powq(3,Q(1,3))*ex(Q(1,3)).gamma())
        check("the exact real Airy initial sum satisfies the elementary energy hypothesis",abs(Ai0)+abs(Aip0)<1)
        check("the elementary Airy energy and central-argument constants hold",
            arb(1).exp()<3 and arb(2).exp()<8 and 25*ex(Q(5,18)).exp()<36)
        roots=list(map(Q,root["exact_root_interval"]))
        starts=[Q(x["interval"][0]) for x in root["rows"]]
        previous=None
        if a.resume:
            previous=read(a.resume)
            check("the actual saved seam prefix has the same source and all input bytes",
                previous.get("source_sha256")==sha(__file__)
                and previous.get("input_manifest_sha256")==sha(a.manifest)
                and previous.get("root_native_sha256")==ROOT_SHA
                and previous.get("first_forcing_native_sha256")==fid["native_sha256"]
                and previous.get("runtime")==runtime)
            result["seams"]=list(previous.get("seams",[]))
            result["refined_forcing_radius_cases"]=list(previous.get("refined_forcing_radius_cases",[]))
        reused=len(result["seams"]);result["completed_seams_reused"]=reused
        result["new_seams_evaluated"]=0
        result["root_native_sha256"]=ROOT_SHA
        result["first_forcing_native_sha256"]=fid["native_sha256"]
        result["first_forcing_process_sha256"]=sha(fp)
        refined=[]
        for ci,case in enumerate(root["cases"]):
            if not case["passed"]:raise ValueError("a complete original root radius is not proved")
            cl,cr=map(Q,case["exact_radial_cover"])
            oldrows=[z for z in forcing_native["rows"] if cl<=Q(z["interval"][0]) and Q(z["interval"][1])<=cr]
            selected_seams=[z for z in root["seams"] if cl<Q(z["radial"])<cr]
            if not oldrows or oldrows[0]["interval"][0]!=str(cl) or oldrows[-1]["interval"][1]!=str(cr):
                raise ValueError("an actual smaller radius lost its complete saved forcing cover")
            if ci<len(result["refined_forcing_radius_cases"]):
                entry=result["refined_forcing_radius_cases"][ci]
                if (entry["exact_radius"]!=case["exact_radius"]
                    or entry["exact_cover"]!=case["exact_radial_cover"]
                    or entry["complete_original_forcing_rows"]!=len(oldrows)
                    or entry["complete_original_seams"]!=len(selected_seams)
                    or not entry["passed"] or not all(g["passed"] for g in entry["gates"])):
                    raise ValueError("a completed smaller-radius first-forcing refinement changed")
                smaller=decode_bounds(entry["complete_coefficient_bounds"])
                af=entry["actual_forcing"]
            else:
                localgates=[]
                def localcheck(name,truth):
                    passed=bool(truth);localgates.append(dict(name=name,passed=passed))
                    check("radius"+case["exact_radius"]+": "+name,passed)
                smaller=aggregate_completed_forcing_rows(oldrows)
                af=original_forcing.full_leading_and_forcing(case,smaller,selected_seams,roots,localcheck)
                entry=dict(exact_radius=case["exact_radius"],exact_cover=case["exact_radial_cover"],
                    complete_original_forcing_rows=len(oldrows),complete_original_seams=len(selected_seams),
                    complete_coefficient_bounds=enc(smaller),actual_forcing=af,gates=localgates,passed=True)
                result["refined_forcing_radius_cases"].append(entry)
                result["seconds"]=time.monotonic()-started;save(a.out,result)
            refined.append((cl,cr,case,entry["complete_coefficient_bounds"],af))
        negative=arb(0);positive=arb(0)
        for index,s in enumerate(root["seams"]):
            r=Q(s["radial"]);ri=bisect_right(starts,r)-1;row=root["rows"][ri]
            if not Q(row["interval"][0])<=r<=Q(row["interval"][1]):
                raise ValueError("an original seam has no full closed coefficient row")
            if index<reused:
                item=result["seams"][index]
                if (item["radial"]!=s["radial"] or item["left_piece"]!=s["left_piece"]
                    or item["right_piece"]!=s["right_piece"]
                    or item["original_first_derivative_component_jump_sha256"]!=
                       s["radial_derivatives"]["1"]["complete_exact_component_jump_sha256"]):
                    raise ValueError("an accepted original seam identity changed")
            else:
                result["last_attempted_seam"]=dict(index=index,radial=s["radial"],original_root_row=ri)
                chosen=min((z for z in refined if z[0]<=r<=z[1]),key=lambda z:Q(z[2]["exact_radius"]))
                item=actual_seam(s,row,roots,chosen[3],chosen[4],chosen[2])
                item["actual_forcing_bound_radius"]=chosen[2]["exact_radius"]
                item["original_root_row"]=ri
                result["seams"].append(item);result["new_seams_evaluated"]+=1
                result.pop("last_attempted_seam",None)
            fee=box(item["complete_first_state_jump_Hminus4over3_to_Hminus2over3_times_Hminus1"])
            if item["side"]=="negative":negative+=fee
            else:positive+=fee
            if index%128==0:
                result["seconds"]=time.monotonic()-started;save(a.out,result)
                print(json.dumps(dict(completed_seams=len(result["seams"]),last_radial=s["radial"])),flush=True)
        check("all1079 original seams and every old full component jump remain accounted for",
            len(result["seams"])==1079 and result["seams"][:reused]==(previous or {}).get("seams",[]))
        result["complete_unpropagated_seam_operator_sums"]={
            "negative_mixed_source":fullrec(negative.upper()),
            "positive_raw_mixed_source_only":fullrec(positive.upper()),
            "all_raw_mixed_sources":fullrec((negative+positive).upper())}
        result["actual_negative_first_seam_contributions"]=[]
        for case in cauchy["cases"]:
            if not case["passed"]:raise ValueError("a previously complete negative radius failed")
            left,right=map(Q,case["exact_enclosing_negative_interval"])
            chosen=[z for z in result["seams"] if z["side"]=="negative" and left<=Q(z["radial"])<=right]
            total=sum((box(z["complete_first_state_jump_Hminus4over3_to_Hminus2over3_times_Hminus1"])
                       for z in chosen),arb(0)).upper()
            gain=box(case["bounds"]["primitive_after_Hminus1"]["full_root_bracket_to_L2"])
            result["actual_negative_first_seam_contributions"].append(dict(
                exact_radius=case["exact_radius"],exact_enclosing_interval=case["exact_enclosing_negative_interval"],
                complete_actual_seams=len(chosen),mixed_source_operator_sum=fullrec(total),
                actual_full_mean_Cauchy_and_primitive_gain=fullrec(gain),
                first_seam_contribution_Hminus4over3_to_primitive_L2_pair=fullrec((gain*total).upper()),
                zero_root_and_other_sources_for_this_linear_component=True,
                no_radial_length_factor_applied_to_any_affine_jump=True,
                complete_return_remainder_claimed=False))
        result["actual_negative_Cauchy_native_sha256"]=cauchy["native_sha256"]
        result["negative_first_seam_component_has_complete_strong_4over3_window"]=True
        result["negative_seam_count"]=sum(s["side"]=="negative" for s in result["seams"])
        result["positive_seam_count"]=sum(s["side"]=="positive" for s in result["seams"])
        result["exact_root_interval"]=list(map(str,roots))
        result["exact_cover"]=root["exact_cover"]
        result.update(complete=True,proved=True)
    except BaseException as error:
        result["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        result["seconds"]=time.monotonic()-started;save(a.out,result)
        print(json.dumps(dict(complete=result["complete"],failure=result["failure"],
            completed_seams=len(result["seams"]),seconds=result["seconds"])),flush=True)
if __name__=="__main__":main()

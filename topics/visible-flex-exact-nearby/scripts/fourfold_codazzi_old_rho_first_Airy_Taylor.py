#!/usr/bin/env python3
"""Complete old-radial first Airy Taylor coefficients from the paid root jets.

All new mathematics runs in the one public Actions repository.  Original target,
FFT, intrinsic error, auxiliary-domain and point stages are never re-evaluated.
Every completed finite algebra stage is saved separately with its full support.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,io,json,math,os,shutil,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
import flint
from flint import acb,arb,ctx
import fourfold_codazzi_root_Laurent_Taylor_algebra as L

PUBLIC="Rogerhu12/math-research-public"
ROOT="397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
RB="10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"
HIGH="38a8ba8d2998a75ddb863fe9b486defd756a22488e1c3a96ed8bf54581877e8f"
HPROC="3b06c881b8b00f8bb830653b3eb290b09687b0a2576320b605ba758e2e706abe"
HSOURCE="c3bb77f96f05ceedd05a0fc4cda39d591065d4ee2203fd7b05be79169d04709d"
FOLD="84e2bd1b7637299e94428b22cc19aba290d0b661f9dbe18dae918bf752f10077"
FPROC="855730f8bf86d04c6cc7622e1881f9fc29a2af754694dfaf5dad16012b98544e"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
RESPONSE="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
DELTA=Q(1,10**8)
COUNT=9
ORDER=6
RHO=Q(1,6000)
SIGMA=Q(1,128)
HREAL=Q(9,10**6)
WIDTHS=(Q(0),Q(1,1024),Q(1,512))
I=acb(0,1)

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,separators=(",",":"),allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,compresslevel=6,mtime=0)
    tmp=path.with_name(path.name+".partial");tmp.write_bytes(raw);tmp.replace(path)
def ex(q):return L.ex(q)
def up(v):return abs(v).upper()
def rb(v):
    if isinstance(v,str):return arb(v)
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def cb(v):return acb(rb(v["real"]),rb(v["imag"]))
def record(v):return dict(ball=L.rec(v,90))
def encode(value):
    if isinstance(value,dict):return {k:encode(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [encode(v) for v in value]
    return record(value)
def decode(value):
    if isinstance(value,dict):
        if "ball" in value:return rb(value)
        return {k:decode(v) for k,v in value.items()}
    if isinstance(value,list):return [decode(v) for v in value]
    return value
def interval(a,b):return ex(a).union(ex(b))
def dyadic(x):return Q.from_float(float(x))
def sqr(x):return x*x
def ipow(x,n):
    if n<0:raise ValueError("negative integer exponent must use a paid denominator")
    y=arb(1)
    for _ in range(n):y=y*x
    return y
def cubic(c,x):
    a=[acb(ex(dyadic(z))) for z in c]
    return [((a[0]*x+a[1])*x+a[2])*x+a[3],
        (3*a[0]*x+2*a[1])*x+a[2],6*a[0]*x+2*a[1],6*a[0]]
def series(payload):return {k:L.unpack_series(v) for k,v in payload.items()}
def pack(values):return {k:L.pack_series(v) for k,v in values.items()}
def cprod(a,b,n):
    """A triangular product: an unpaid coefficient is allowed only against exact zero."""
    if n<0:return L.LP.zero()
    out=L.LP.zero()
    for j in range(n+1):
        k=n-j
        if j<len(a) and k<len(b):out+=a[j]*b[k]
        elif j<len(a) and a[j].is_zero():continue
        elif k<len(b) and b[k].is_zero():continue
        else:raise ValueError("triangular recurrence requested an unpaid nonzero factor")
    return out
def D(a,d,count):
    L.require(a,count+1);L.require(d,count)
    return L.sub(L.scale(L.dr(a),-1,count),L.mul(d,L.theta(a),count),count)
def local_coefficients(c):
    n=ORDER+1;u,v,K,beta,eta,d=[c[k] for k in ("u","v","K","beta","eta","d")]
    uu,vv=L.mul(u,u,COUNT),L.mul(v,v,COUNT)
    kvv=L.mul(K,vv,COUNT)
    ell=L.scale(L.mul(beta,L.mul(u,v,COUNT),COUNT),-2)
    epoly=L.scale(L.mul(beta,L.add(L.constant(1,COUNT),L.add(L.scale(uu,3),kvv,COUNT),COUNT),COUNT),-1)
    bloc=L.mul(beta,L.sub(L.constant(1,COUNT),L.add(uu,L.scale(kvv,3),COUNT),COUNT),COUNT)
    etainv=L.inverse(eta,COUNT)
    logeta=L.mul(L.dr(eta),etainv,n)
    tQ=L.add(L.add(L.scale(logeta,-1),L.theta(d),n),epoly,n)
    T0=L.add(L.sub(L.scale(logeta,-1),L.scale(L.mul(beta,L.mean(c["S"]),n),4),n),
        L.scale(L.theta(d),5),n)
    rq=L.sub(L.add(D(ell,d,n),L.mul(eta,L.theta(epoly),n),n),
        L.scale(L.mul(L.mul(beta,eta,n),L.mul(L.theta(u),u,n),n),2),n)
    rq=L.sub(rq,L.mul(ell,L.add(L.scale(logeta,-1),L.theta(d),n),n),n)
    vartheta=L.sub(L.mul(rq,etainv,n),
        L.scale(L.mul(L.mul(beta,K,n),L.mul(v,L.theta(v),n),n),2),n)
    inner=L.sub(L.mul(ell,ell,n),
        L.scale(L.mul(L.mul(beta,eta,n),L.mul(v,L.theta(u),n),n),4),n)
    V0=L.sub(L.sub(L.mul(tQ,bloc,n),D(bloc,d,n),n),L.mul(K,inner,n),n)
    crossd=L.add(L.dr(d),L.mul(d,L.theta(d),n),n)
    angular2=L.add(L.mul(d,d,n),L.mul(L.mul(eta,eta,n),K,n),n)
    return dict(T0=T0,V0=V0,vartheta=vartheta,crossd=crossd,angular2=angular2,
        ell=L.take(ell,n),epoly=L.take(epoly,n),bloc=L.take(bloc,n),rQ=rq,tQ=tQ)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("repo-root","manifest","out"):p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new root Taylor mathematics runs only in the authorized public Actions repository")
    import scipy
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise RuntimeError("the reviewed exact runtime changed")
    if a.out.exists():raise FileExistsError("preserve every original complete or failed native")
    ctx.prec=320;ctx.cap=4
    start=time.monotonic()
    doc=dict(kind="actual_complete_old_rho_first_Airy_Taylor_Fourier_coefficients",
        complete=False,proved=False,failure=None,gates=[],stages={},
        source_sha256=sha(__file__),algebra_sha256=sha(L.__file__),
        input_manifest_sha256=sha(a.manifest),runtime=runtime,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        root_germ_sha256=ROOT,root_budget_sha256=RB,complete_high_root_native_sha256=HIGH,
        complete_high_root_process_sha256=HPROC,complete_larger_fold_native_sha256=FOLD,
        background_definition_sha256=BASE,explicit_direction_definition_sha256=ZDEF,
        actual_intrinsic_parameter="eta_0",exact_complex_delta_radius=str(DELTA),
        leading_Taylor_order=COUNT-1,forcing_Taylor_order=ORDER,first_correction_Taylor_order=ORDER,
        complete_non_circular_Fourier_algebra=True,physical_angle_frequency_multiplier=4,
        principal_mu_uses_B_plus_and_leading_a0_uses_B_minus=True,
        original_target_FFT_or_high_root_stages_recomputed=0,
        original_auxiliary_fold_forcing_or_domain_stages_recomputed=0,
        new_cubic_true_root_component_rows=0,reused_cubic_true_root_component_rows=0,
        new_finite_algebra_stages=0,reused_finite_algebra_stages=0,
        exact_structural_views=[],branch_epsilon_computed=1,
        negative_branch_reused_by_exact_same_complex_parameter_symmetry=True,
        old_circle_I_J_or_independent_even_mean_budget_paid=False,
        complete_strong_return_or_cutoff97_inverse_claimed=False,
        all_original_physical_seams_and_independent_mean_equations_retained=True,
        physical_background_outside_original_piece_replaced=False)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(a.out,doc)
    def gate(name,truth):
        okay=bool(truth);doc["gates"].append(dict(name=name,passed=okay))
        if not okay:raise ValueError("complete root Taylor gate failed: "+name)
    def stage(name,build):
        if name in doc["stages"]:
            r=doc["stages"][name];path=a.out.parent/r["file"]
            if not path.is_file() or sha(path)!=r["sha256"] or path.stat().st_size!=r["bytes"]:
                raise ValueError("a complete finite algebra prefix changed bytes: "+name)
            s=read(path)
            if (s["stage"]!=name or s["source_sha256"]!=doc["source_sha256"]
                or s["algebra_sha256"]!=doc["algebra_sha256"]
                or s["input_manifest_sha256"]!=doc["input_manifest_sha256"] or not s["complete"]):
                raise ValueError("a complete finite algebra stage changed mathematical identity")
            doc["reused_finite_algebra_stages"]+=1
            return s["payload"]
        payload=build()
        path=a.out.parent/"stages"/(name+".json.gz")
        if path.exists():raise FileExistsError("do not replace an unindexed mathematical stage")
        s=dict(stage=name,complete=True,source_sha256=doc["source_sha256"],
            algebra_sha256=doc["algebra_sha256"],input_manifest_sha256=doc["input_manifest_sha256"],
            complete_high_root_native_sha256=HIGH,runtime=runtime,payload=payload)
        save(path,s)
        if path.stat().st_size>=5_000_000:
            raise ValueError("one natural complete algebra stage exceeds the reviewable publication size")
        doc["stages"][name]=dict(file=str(path.relative_to(a.out.parent)),
            sha256=sha(path),bytes=path.stat().st_size)
        doc["new_finite_algebra_stages"]+=1;checkpoint()
        return payload
    def exactzero(v,identity):
        out=L.known_zero_view(v,identity)
        doc["exact_structural_views"].append(identity);return out
    def exactscalar(v,z,identity):
        out=L.known_scalar_view(v,z,identity)
        doc["exact_structural_views"].append(identity);return out
    try:
        manifest=read(a.manifest)
        gate("the exact manifest belongs to this public complete Fourier consumer",
            manifest["public_repository"]==PUBLIC and manifest["mathematical_parameters"]["Taylor_order"]==ORDER)
        for f in manifest["files"]:
            path=a.repo_root/f["path"]
            if not path.is_file() or sha(path)!=f["sha256"] or path.stat().st_size!=f["bytes"]:
                raise ValueError("a pinned mathematical input changed: "+f["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        germ,budget,high,hproc,fold,fproc,cp,zp=[read(paths[k]) for k in
            ("root_germ","root_budget","high_root_native","high_root_process",
             "fold_native","fold_process","candidate_index","response_index")]
        gate("the complete high-root and larger-fold results are the actual successful originals",
            sha(paths["root_germ"])==ROOT and sha(paths["root_budget"])==RB
            and sha(paths["high_root_native"])==HIGH and sha(paths["high_root_process"])==HPROC
            and sha(paths["fold_native"])==FOLD and sha(paths["fold_process"])==FPROC
            and high["complete"] and high["proved"] and high["failure"] is None
            and high["source_sha256"]==HSOURCE and hproc["native_sha256"]==HIGH
            and hproc["actual_returncode"]==0 and all(g["passed"] for g in high["gates"])
            and fold["complete"] and fold["proved"] and fold["failure"] is None
            and fproc["native_sha256"]==FOLD and fproc["actual_returncode"]==0)
        gate("the same repaired background full direction and fixed intrinsic parameter are retained",
            germ["complete"] and germ["proved"] and germ["failure"] is None
            and budget["complete"] and budget["proved"] and budget["failure"] is None
            and budget["background_definition_sha256"]==fold["background_definition_sha256"]==BASE
            and budget["explicit_direction_definition_sha256"]==fold["explicit_direction_definition_sha256"]==ZDEF
            and budget["actual_intrinsic_parameter"]==high["actual_intrinsic_parameter"]==fold["actual_intrinsic_parameter"]=="eta_0"
            and Q(budget["exact_complex_parameter_radius"])==Q(fold["exact_complex_delta_radius"])==DELTA
            and germ["compact_bump_identically_zero_on_entire_actual_germ"]
            and germ["actual_candidate_piece"]==budget["exact_candidate_and_response_piece"]==2549)
        roots=list(map(Q,germ["root_interval"]));cell=list(map(Q,germ["exact_candidate_piece_interval"]))
        gate("all true-root and physical-piece endpoints agree",
            list(map(Q,high["exact_root_interval"]))==list(map(Q,fold["exact_root_interval"]))==roots
            and list(map(Q,high["exact_original_physical_piece_interval"]))==cell
            and list(map(Q,fold["exact_original_piece_interval"]))==cell
            and cell[0]<roots[0]<=roots[1]<cell[1])
        gate("the original full 65 and 193 component indices and actual amplitude are unchanged",
            sha(paths["candidate_index"])==CANDIDATE and sha(paths["response_index"])==RESPONSE
            and cp["coefficient_shape"]==[4,6144,65] and zp["coefficient_shape"]==[4,6144,193]
            and zp["metadata"]["finite_head_mean_was_not_removed_from_the_solve"])
        alpha=Q(cp["metadata"]["exact_float_amplitude"])
        offsets=list(map(Q,budget["exact_background_root_offsets"]))
        gate("all exact value repairs and the same candidate amplitude are retained",
            alpha==Q(germ["exact_amplitude"]) and len(offsets)==65
            and len(budget["response_raw_complete_coefficient_upper"])==193
            and len(budget["response_repaired_complete_coefficient_upper"])==193
            and budget["exact_intrinsic_parameter"]==germ["exact_center_parameter"])
        doc.update(exact_root_interval=list(map(str,roots)),exact_original_physical_piece_interval=list(map(str,cell)),
            exact_fixed_intrinsic_parameter=germ["exact_center_parameter"],
            original_completed_point_payload_sha256=high["original_finite_point_payload_sha256"],
            old_failed_high_root_source_and_point_retained=True)
        if a.resume:
            prev=read(a.resume)
            gate("accepted finite prefixes have exactly the same source algebra manifest runtime and originals",
                prev["source_sha256"]==doc["source_sha256"] and prev["algebra_sha256"]==doc["algebra_sha256"]
                and prev["input_manifest_sha256"]==doc["input_manifest_sha256"] and prev["runtime"]==runtime
                and prev["complete_high_root_native_sha256"]==HIGH
                and prev["complete_larger_fold_native_sha256"]==FOLD
                and prev["exact_root_interval"]==doc["exact_root_interval"])
            doc["cubic_point_rows"]=copy.deepcopy(prev.get("cubic_point_rows",{"candidate":[],"response":[]}))
            doc["original_prefix_audit"]=dict(native_sha256=sha(a.resume),native_bytes=a.resume.stat().st_size,
                run_id=prev["run_id"],complete=prev["complete"],proved=prev["proved"],
                failure=prev["failure"],gates=prev["gates"],stage_count=len(prev["stages"]))
            for name,r in prev["stages"].items():
                if not name.replace("-","").replace("_","").isalnum():
                    raise ValueError("unsafe finite stage name")
                relative=Path(r["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="stages":
                    raise ValueError("a saved finite stage left its natural stage directory")
                src=a.resume.parent/relative;dst=a.out.parent/relative
                if sha(src)!=r["sha256"] or src.stat().st_size!=r["bytes"]:
                    raise ValueError("an original complete finite stage changed bytes")
                dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
                doc["stages"][name]=copy.deepcopy(r)
            checkpoint()
        rawjets=high["intrinsic_stage"]["ordinary_old_radial_jets"]
        gate("the paid complete intrinsic prefix has all ten ordinary derivatives without zero padding",
            high["intrinsic_stage"]["complete_primitive_and_product_errors_included"]
            and high["intrinsic_stage"]["missing_series_coefficients_padded_with_zero"] is False
            and set(rawjets)=={"K","beta","gamma","s"} and all(len(v)==10 for v in rawjets.values())
            and high["at_the_certified_true_root"]["exact_K0"]=="0"
            and high["at_the_certified_true_root"]["fixed_intrinsic_parameter"]=="eta_0")
        case=fold["cases"][1]
        gate("the paid larger auxiliary case supplies its full complex old product and canonical amplitudes",
            case["complete"] and case["proved"] and case["failure"] is None
            and Q(case["exact_fold_radius"])==Q(3,8000)
            and all(g["passed"] for g in case["gates"]))
        coeff_bounds=decode(case["characteristic_refinement_evidence"]["complete_refined_coefficient_majorants"])
        f_bounds=decode(case["fold_evidence"]["complete_fold_and_leading_bounds"])
        forced=case["first_forcing_evidence"]
        original_amp=decode(forced["separated_first_amplitudes"])
        rt,sv=Q(forced["exact_forcing_T_radius"]),Q(forced["exact_amplitude_X_width"])
        hcover=HREAL+roots[1]-roots[0]
        gate("the new old-product circle is mapped inside the already paid canonical amplitude rectangle",
            RHO<Q(case["exact_fold_radius"]) and SIGMA<Q(case["exact_old_leading_width"])
            and ex(RHO)*(f_bounds["Ap"].log()*ex(Q(2,3))).exp()<ex(rt)
            and ex(SIGMA)+ex(RHO)*f_bounds["Xr"]<ex(sv))
        gate("the original physical inner cover and true-root bracket fit the new old-product circle",
            hcover<RHO and cell[0]<roots[0]-HREAL and roots[1]+HREAL<cell[1]
            and roots[0]-HREAL>Q(germ["original_scalar_germ"][0])
            and roots[1]+HREAL<Q(germ["original_scalar_germ"][1]))
        doc["old_product_domain"]=dict(exact_rho_radius=str(RHO),exact_phi_width=str(SIGMA),
            exact_physical_inner_radius=str(HREAL),exact_physical_rho_cover_radius=str(hcover),
            exact_physical_interval=[str(roots[0]-HREAL),str(roots[1]+HREAL)],
            original_canonical_T_radius=str(rt),original_amplitude_X_width=str(sv),
            image_T_upper=record((ex(RHO)*(f_bounds["Ap"].log()*ex(Q(2,3))).exp()).upper()),
            image_X_width_upper=record((ex(SIGMA)+ex(RHO)*f_bounds["Xr"]).upper()),
            full_canonical_a1_sup=record(original_amp["a1"]),full_canonical_b1_sup=record(original_amp["b1"]),
            same_original_piece_identity_only=True)
        checkpoint()

        # These are NEW values of the original two cubics at the true root.
        # They are not evaluations of any previously completed auxiliary domain.
        doc.setdefault("cubic_point_rows",{"candidate":[],"response":[]})
        if a.resume:
            previous_rows=prev.get("cubic_point_rows",{"candidate":[],"response":[]})
            doc["cubic_point_rows"]=copy.deepcopy(previous_rows)
        for name,index,first,end,count,psha in (
            ("candidate",cp,1346,2692,65,"3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106"),
            ("response",zp,2265,2718,193,"ce29c19c81e77cb2f2ea9b70edc59af96a869116fa96e2e5375ffa4d61927917")):
            part=next(v for v in index["parts"] if v["first_interval"]<=2549<v["last_interval_exclusive"])
            path=paths[name+"_shard"];local=2549-first
            gate("the full original "+name+" shard and piece are unchanged",
                part["first_interval"]==first and part["last_interval_exclusive"]==end
                and part["sha256"]==sha(path)==psha and part["bytes"]==path.stat().st_size
                and part["file"]==path.name)
            accepted=doc["cubic_point_rows"][name]
            if len(accepted)>count or any(x["component"]!=j for j,x in enumerate(accepted)):
                raise ValueError("a completed original cubic component prefix changed")
            doc["reused_cubic_true_root_component_rows"]+=len(accepted)
            if len(accepted)==count:continue
            with np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False) as z:
                nodes=z["radial_nodes"].copy();coeff=z["piece_coefficients"].copy()
            gate("the "+name+" arrays retain all original components and exact radial nodes",
                nodes.shape==(end-first+1,) and coeff.shape==(4,end-first,count)
                and np.isfinite(nodes).all() and np.isfinite(coeff).all() and (np.diff(nodes)>0).all()
                and [dyadic(nodes[local]),dyadic(nodes[local+1])]==cell)
            x=acb(interval(*roots)-ex(cell[0]))
            for j in range(len(accepted),count):
                values=cubic(coeff[:,local,j],x)
                if name=="candidate":values=[ex(alpha)*z for z in values]
                accepted.append(dict(component=j,ordinary_r_derivatives=[L.cpack(z) for z in values]))
                doc["new_cubic_true_root_component_rows"]+=1;checkpoint()
        def make_coefficients():
            raw=[[L.cunpack(row["ordinary_r_derivatives"][p])
                for row in doc["cubic_point_rows"]["candidate"]] for p in range(4)]
            zraw=[[L.cunpack(row["ordinary_r_derivatives"][p])
                for row in doc["cubic_point_rows"]["response"]] for p in range(4)]
            fees=[(arb(b["upper"]).upper()-arb(x["lower"]).lower()).upper()
                for x,b in zip(budget["response_raw_complete_coefficient_upper"],
                    budget["response_repaired_complete_coefficient_upper"])]
            if not all(f.is_finite() and f>=0 for f in fees):
                raise ValueError("a complete exact constant direction repair fee is invalid")
            for j,q in enumerate(offsets):raw[0][j]+=ex(q)
            for j,fee in enumerate(fees):zraw[0][j]+=acb(arb(0,fee))
            delta=acb(arb(0,ex(DELTA)),arb(0,ex(DELTA)))
            intr={key:[L.LP.scalar(acb(rb(v))*ex(Q((-1)**p,math.factorial(p))))
                for p,v in enumerate(values)] for key,values in rawjets.items()}
            rawK0=intr["K"][0]
            intr["K"][0]=exactzero(rawK0,"certified true-root curvature K(0)=0 at fixed eta_0")
            u=[];v=[]
            for p in range(COUNT):
                uf=[acb(0) for _ in range(193)]
                vf=[acb(0) for _ in range(193)]
                vf[96]=intr["s"][p].scalar_value()
                if p<4:
                    scale=ex(Q((-1)**p,math.factorial(p)))
                    vf[96]+=(raw[p][32]+delta*zraw[p][96])*scale
                    for j in range(1,97):
                        us=(raw[p][j-1] if j<=32 else acb(0))+delta*zraw[p][j-1]
                        vs=(raw[p][32+j] if j<=32 else acb(0))+delta*zraw[p][96+j]
                        uf[96+j]=us*scale/(2*I);uf[96-j]=-us*scale/(2*I)
                        vf[96+j]=vs*scale/2;vf[96-j]=vs*scale/2
                u.append(L.LP(-96,uf));v.append(L.LP(-96,vf))
            K=L.take(intr["K"],COUNT);beta=L.take(intr["beta"],COUNT)
            gamma=L.take(intr["gamma"],COUNT);s=L.take(intr["s"],COUNT)
            k=[L.LP.scalar(acb(rb(rawjets["K"][p+1]))*ex(Q((-1)**p,math.factorial(p+1))))
                for p in range(COUNT)]
            eta=L.scale(L.mul(gamma,L.mean(v),COUNT),-1)
            achar=L.mul(eta,L.power(k,Q(1,2),COUNT),COUNT)
            if not (k[0].scalar_value().real>0 and eta[0].scalar_value().real>0
                and achar[0].scalar_value().real>0):
                raise ValueError("the same true-root characteristic branch is unresolved")
            S=L.add(L.mul(u,u,COUNT),L.mul(K,L.mul(v,v,COUNT),COUNT),COUNT)
            d=L.scale(L.mul(beta,L.primitive(S),COUNT),-1)
            return dict(series=pack(dict(u=u,v=v,K=K,beta=beta,gamma=gamma,s=s,k=k,
                eta=eta,a=achar,S=S,d=d,e_d=L.scale(d,-1))),
                raw_complete_K0=L.pack_series([rawK0]),
                complete_constant_direction_repair_fees=[record(x) for x in fees],
                zero_bump_germ_and_fixed_eta0=True,positive_order_value_repair_derivatives_exactly_zero=True,
                original_65_and_193_rows_retained=True,complete_mean_at_all_orders_retained=True)
        c=series(stage("complete-background-root-series",make_coefficients)["series"])
        gate("the complete original Fourier input and high intrinsic mean have been retained",
            len(c["v"])==COUNT and all(q.degree<=96 for q in c["u"]+c["v"])
            and all(q.degree<=192 for q in c["S"]+c["d"])
            and all(q.scalar_value().is_finite() for q in c["eta"]+c["a"]))
        chi=[];A=[]
        for degree in range(COUNT):
            def build_fold(degree=degree):
                if degree==0:
                    x=L.LP.zero();v=c["a"][0]
                else:
                    xp=L.theta(chi);xp[0]+=1
                    x=(cprod(c["e_d"],xp,degree-1)
                        +cprod(c["a"],L.theta(A),degree-3).scale(ex(Q(2,3)))).divide_scalar(degree)
                    xpnew=L.theta(chi+[x]);xpnew[0]+=1
                    v=(cprod(c["e_d"],L.theta(A),degree-1).scale(2)
                        +cprod(c["a"],xpnew,degree).scale(3)).divide_scalar(2*degree+3)
                if x.degree>192*degree or v.degree>192*degree:
                    raise ValueError("a complete fold coefficient exceeds its proved exact Fourier support")
                return dict(degree=degree,chi=x.record(),A=v.record(),
                    full_non_circular_support=True)
            row=stage("fold-degree-"+str(degree).zfill(3),build_fold)
            if row["degree"]!=degree:raise ValueError("a completed fold degree changed")
            chi.append(L.LP.restore(row["chi"]));A.append(L.LP.restore(row["A"]))
        gate("all nine complete fold degrees and the exact radial anchor are present",
            len(A)==COUNT and len(chi)==COUNT and chi[0].is_zero()
            and A[0].scalar_value().real>0)
        leading={}
        builders={
            "Xp":lambda:L.add(L.constant(1,COUNT),L.theta(chi),COUNT),
            "T":lambda:L.scale(L.shift(L.power(A,Q(2,3),COUNT),1,COUNT),-1),
            "Q":lambda:L.mul(c["a"],L.power(A,Q(-1,3),COUNT),COUNT),
            "EG":lambda:L.exp_integral(L.scale(L.mul(c["beta"],L.mean(c["S"]),COUNT),2),COUNT),
            "G":lambda:L.mul(L.mul(L.power(A,Q(1,6),COUNT,normalized=True),
                L.power(c["k"],Q(-1,4),COUNT,normalized=True),COUNT),leading["EG"],COUNT),
            "B_minus":lambda:L.sub(L.mul(leading["Xp"],leading["Xp"],COUNT),
                L.mul(leading["T"],L.mul(L.theta(leading["T"]),L.theta(leading["T"]),COUNT),COUNT),COUNT),
            "B_plus":lambda:L.add(L.mul(leading["Xp"],leading["Xp"],COUNT),
                L.mul(leading["T"],L.mul(L.theta(leading["T"]),L.theta(leading["T"]),COUNT),COUNT),COUNT),
            "mu":lambda:L.mul(L.mul(leading["Q"],leading["Q"],COUNT),leading["B_plus"],COUNT),
            "a0":lambda:L.mul(leading["G"],leading["B_minus"],COUNT),
            "b0":lambda:L.scale(L.mul(L.mul(leading["G"],leading["Xp"],COUNT),
                L.theta(leading["T"]),COUNT),-2*I),
            "mu_inverse":lambda:L.inverse(leading["mu"],COUNT)}
        for key,build in builders.items():
            payload=stage("leading-complete-"+key,lambda key=key,build=build:
                dict(name=key,coefficients=L.pack_series(build())))
            if payload["name"]!=key:raise ValueError("a leading series changed its identity")
            leading[key]=L.unpack_series(payload["coefficients"])
        gate("the exact normalized leading constants and order-two odd amplitude are preserved",
            leading["G"][0].scalar_value()==1 and leading["a0"][0].scalar_value()==1
            and leading["b0"][0].is_zero() and leading["b0"][1].is_zero()
            and leading["T"][0].is_zero() and leading["Xp"][0].scalar_value()==1)
        op=series(stage("complete-local-operator-series",lambda:pack(local_coefficients(c))))
        T,Xp,Qc,a0,b0=[leading[k] for k in ("T","Xp","Q","a0","b0")]
        wr=[L.dr(a0),L.dr(b0)]
        wrr=[L.dr(wr[0]),L.dr(wr[1])]
        wphi=[L.theta(a0),L.theta(b0)]
        wrphi=[L.theta(wr[0]),L.theta(wr[1])]
        wphiphi=[L.theta(a0,2),L.theta(b0,2)]
        w=[a0,b0]
        nums=[[],[]];F=[[],[]]
        vq=L.mul(op["vartheta"],Qc,ORDER+1)
        for degree in range(ORDER+1):
            def build_forcing(degree=degree):
                nb=[]
                for h in range(2):
                    value=wrr[h][degree]+cprod(c["d"],wrphi[h],degree).scale(2)
                    value+=cprod(op["crossd"],wphi[h],degree)
                    value+=cprod(op["angular2"],wphiphi[h],degree)
                    value+=cprod(op["T0"],wr[h],degree)
                    value+=cprod(L.mul(op["T0"],c["d"],degree+1),wphi[h],degree)
                    value+=cprod(op["V0"],w[h],degree)
                    cross=cprod(vq,L.mul(T,b0,degree+1) if h==0 else a0,degree).scale(I)
                    nb.append(value+cross)
                force=[-cprod(leading["mu_inverse"],nums[h]+[nb[h]],degree) for h in range(2)]
                if any(v.degree>192*(degree+2) for v in force):
                    raise ValueError("a full degree-zero forcing coefficient exceeds its proved support")
                return dict(degree=degree,numerator_b=nb[0].record(),numerator_a=nb[1].record(),
                    Fb=force[0].record(),Fa=force[1].record(),
                    full_radial_and_angular_terms_and_cross_couplings_retained=True)
            row=stage("forcing-degree-"+str(degree).zfill(3),build_forcing)
            if row["degree"]!=degree:raise ValueError("a completed forcing degree changed")
            nums[0].append(L.LP.restore(row["numerator_b"]));nums[1].append(L.LP.restore(row["numerator_a"]))
            F[0].append(L.LP.restore(row["Fb"]));F[1].append(L.LP.restore(row["Fa"]))
        def build_transport_coefficients():
            n=ORDER+1
            determinant=L.sub(L.mul(a0,a0,n),L.mul(T,L.mul(b0,b0,n),n),n)
            determinant[0]=exactscalar(determinant[0],1,"the true leading determinant has constant one")
            di=L.inverse(determinant,n)
            J=L.sub(L.mul(L.dr(T),Xp,n),L.mul(L.theta(T),L.dr(chi),n),n)
            Jstar=T[1].scalar_value()
            J[0]=exactscalar(J[0],Jstar,"the old-radial Jacobian at the root equals T_rho(0)")
            Xm=L.take(Xp,n);Xm[0]=exactzero(Xm[0]-1,"X_phi(0)-1 is exactly zero")
            excess=L.mul(T,Xp,n)
            excess[0]=exactzero(excess[0],"T X_phi has zero constant")
            excess[1]=exactzero(excess[1]-Jstar,"T X_phi-J_star rho has zero linear coefficient")
            Jm=L.take(J,n);Jm[0]=exactzero(Jm[0]-Jstar,"J-J_star has zero constant")
            return pack(dict(inv00=L.mul(a0,di,n),
                inv01=L.scale(L.mul(L.mul(T,b0,n),di,n),-1),
                inv10=L.scale(L.mul(b0,di,n),-1),
                J=J,Xm=Xm,T_excess=excess,Jm=Jm,TTphi=L.mul(T,L.theta(T),n),
                TTrho=L.mul(T,L.dr(T),n),TXrho=L.mul(T,L.dr(chi),n),
                Xrho=L.take(L.dr(chi),n)))
        tr=series(stage("complete-normalized-transport-coefficients",build_transport_coefficients))
        fb=[];fa=[]
        for degree in range(ORDER+1):
            def build_normalized(degree=degree):
                vb=cprod(tr["inv00"],F[0],degree)+cprod(tr["inv01"],F[1],degree)
                va=cprod(tr["inv10"],F[0],degree)+cprod(tr["inv00"],F[1],degree)
                return dict(degree=degree,fb=vb.record(),fa=va.record())
            row=stage("normalized-forcing-degree-"+str(degree).zfill(3),build_normalized)
            if row["degree"]!=degree:raise ValueError("a normalized forcing degree changed")
            fb.append(L.LP.restore(row["fb"]));fa.append(L.LP.restore(row["fa"]))
        An=[];Bn=[]
        for degree in range(ORDER+1):
            def build_transport(degree=degree):
                if degree==0:an=L.LP.zero();bn=fb[0]
                else:
                    n=degree-1
                    rhs=cprod(tr["J"],fa,n)
                    rhs+=cprod(tr["Xrho"],L.theta(An),n).scale(2)
                    rhs-=cprod(tr["Xm"],L.dr(An),n).scale(2)
                    rhs+=cprod(tr["TTphi"],L.dr(Bn),n).scale(2*I)
                    rhs-=cprod(tr["TTrho"],L.theta(Bn),n).scale(2*I)
                    an=rhs.divide_scalar(2*degree)
                    knownA=An+[an]
                    rhs=cprod(tr["J"],fb,degree)
                    rhs+=cprod(tr["TXrho"],L.theta(Bn),degree).scale(2)
                    rhs-=cprod(tr["T_excess"],L.dr(Bn),degree).scale(2)
                    rhs-=cprod(tr["Jm"],Bn,degree)
                    rhs+=cprod(tr["TTphi"],L.dr(knownA),degree).scale(2*I)
                    rhs-=cprod(tr["TTrho"],L.theta(knownA),degree).scale(2*I)
                    bn=rhs.divide_scalar(T[1].scalar_value()*(2*degree+1))
                return dict(degree=degree,A=an.record(),B=bn.record(),
                    actual_same_canonical_Fuchsian_solution=True,unpaid_current_coefficients_discarded=False)
            row=stage("transport-degree-"+str(degree).zfill(3),build_transport)
            if row["degree"]!=degree:raise ValueError("a transport degree changed")
            An.append(L.LP.restore(row["A"]));Bn.append(L.LP.restore(row["B"]))
        a1=[];b1=[]
        for degree in range(ORDER+1):
            def build_reconstructed(degree=degree):
                av=cprod(a0,An,degree)+cprod(L.mul(T,b0,degree+1),Bn,degree)
                bv=cprod(b0,An,degree)+cprod(a0,Bn,degree)
                if av.degree>192*(degree+1) or bv.degree>192*(degree+2):
                    raise ValueError("a complete first-correction coefficient exceeds its proved support")
                return dict(degree=degree,a1=av.record(),b1=bv.record(),
                    a1_exact_support_upper=192*(degree+1),b1_exact_support_upper=192*(degree+2),
                    no_incomplete_high_Fourier_output_removed=True)
            row=stage("first-correction-degree-"+str(degree).zfill(3),build_reconstructed)
            if row["degree"]!=degree:raise ValueError("a first-correction degree changed")
            a1.append(L.LP.restore(row["a1"]));b1.append(L.LP.restore(row["b1"]))
        gate("all seven complete first-correction Fourier coefficients and both branch identities are present",
            len(a1)==len(b1)==ORDER+1 and a1[0].is_zero()
            and all(a1[p].degree<=192*(p+1) and b1[p].degree<=192*(p+2) for p in range(ORDER+1)))
        doc["complete_branch_identity"]=dict(same_complex_delta_without_conjugation=True,
            leading_a0_minus="a0_plus",leading_b0_minus="-b0_plus",
            Fb_minus="Fb_plus",Fa_minus="-Fa_plus",
            normalized_A_minus="-A_plus",normalized_B_minus="B_plus",
            first_correction_a1_minus="-a1_plus",first_correction_b1_minus="b1_plus",
            both_original_Airy_carrier_branches_retained=True)
        checkpoint()

        def tail_factor(x,radial_order):
            den=1-x
            if not den>0:raise ValueError("the actual Taylor inner radius reaches its Cauchy circle")
            if radial_order==0:return ipow(x,ORDER+1)/den
            if radial_order==1:return (ORDER+1)*ipow(x,ORDER)/den+ipow(x,ORDER+1)/sqr(den)
            if radial_order==2:return (ORDER*(ORDER+1)*ipow(x,ORDER-1)/den
                +2*(ORDER+1)*ipow(x,ORDER)/sqr(den)+2*ipow(x,ORDER+1)/(den*den*den))
            raise ValueError("unpaid radial derivative order")
        summaries=[]
        for width in WIDTHS:
            norm_rows=[]
            for degree in range(ORDER+1):
                def build_norm(degree=degree,width=width):
                    return dict(degree=degree,exact_width=str(width),
                        a1=[record(a1[degree].norm(width,q)) for q in range(4)],
                        b1=[record(b1[degree].norm(width,q)) for q in range(4)],
                        a1_actual_Fourier_range=[a1[degree].lo,a1[degree].hi],
                        b1_actual_Fourier_range=[b1[degree].lo,b1[degree].hi],
                        complete_mean_retained_in_angular_order_zero=True)
                tag=str(width.numerator)+"_"+str(width.denominator)
                row=stage("full-Fourier-norm-"+tag+"-degree-"+str(degree).zfill(3),build_norm)
                if row["degree"]!=degree or Q(row["exact_width"])!=width:
                    raise ValueError("a completed Fourier norm changed width or degree")
                norm_rows.append(row)
            def build_budget(width=width,norm_rows=norm_rows):
                delta=ex(SIGMA-width);z=(-4*delta).exp();one=1-z
                if not (delta>0 and one>0):raise ValueError("the angular tail loses its positive width")
                sums=[(1+z)/one,8*z/sqr(one),32*z*(1+z)/(one*one*one),
                      128*z*(1+4*z+z*z)/ipow(one,4)]
                x=ex(hcover)/ex(RHO)
                tables={}
                for name in ("a1","b1"):
                    values=[[rb(row[name][q]).upper() for q in range(4)] for row in norm_rows]
                    M=up(original_amp[name]);sup={};wiener={};parts={}
                    for p in range(3):
                        for q in range(4):
                            finite=sum((math.factorial(k)//math.factorial(k-p)
                                *values[k][q]*ipow(ex(hcover),k-p) for k in range(p,ORDER+1)),arb(0)).upper()
                            common=M*tail_factor(x,p)/ipow(ex(RHO),p)
                            st=(common*math.factorial(q)/ipow(delta,q)).upper()
                            wt=(common*sums[q]).upper()
                            key=str(p)+","+str(q)
                            sup[key]=(finite+st).upper();wiener[key]=(finite+wt).upper()
                            parts[key]=dict(complete_finite_Fourier_prefix=finite,
                                complete_strip_sup_tail=st,complete_Wiener_tail=wt)
                    tables[name]=dict(strip_sup=sup,Wiener=wiener,parts=parts)
                def local(v):
                    d,dr=coeff_bounds["D"],coeff_bounds["Dr"]
                    return dict(radial_second=v["2,0"],
                        radial_angular=2*d[0]*v["1,1"],
                        angular_second=(d[0]*d[0]+sqr(coeff_bounds["ep"])*coeff_bounds["K"])*v["0,2"],
                        drift_derivative=(dr[0]+d[0]*d[1])*v["0,1"],
                        first_transport=coeff_bounds["T0"]*(v["1,0"]+d[0]*v["0,1"]),
                        scalar_potential=coeff_bounds["V0"]*v["0,0"])
                va,vb=tables["a1"]["strip_sup"],tables["b1"]["strip_sup"]
                pa,pb=local(va),local(vb)
                pa["exact_QK_cross"]=coeff_bounds["vartheta"]*f_bounds["Q"]*f_bounds["TM"]*vb["0,0"]
                pb["exact_QK_cross"]=coeff_bounds["vartheta"]*f_bounds["Q"]*va["0,0"]
                if not f_bounds["mu"]>0:raise ValueError("the paid complete principal factor loses its gap")
                raw=[sum(v.values(),arb(0)).upper() for v in (pa,pb)]
                normalized=[(v/f_bounds["mu"]).upper() for v in raw]
                return dict(exact_output_phi_width=str(width),
                    exact_old_rho_Cauchy_radius=str(RHO),exact_old_phi_Cauchy_width=str(SIGMA),
                    exact_physical_rho_cover_radius=str(hcover),
                    complete_geometric_Fourier_sums=encode(sums),first_amplitude_budgets=encode(tables),
                    unnormalized_local_operator_sup_bounds=encode(dict(first=raw[0],second=raw[1])),
                    complete_normalized_local_L0_w1_sup_bounds=encode(dict(first=normalized[0],second=normalized[1])),
                    unnormalized_local_operator_sup_parts=encode([pa,pb]),
                    complete_normalized_local_L0_w1_sup_parts=encode([
                        {k:(v/f_bounds["mu"]).upper() for k,v in row.items()} for row in (pa,pb)]),
                    local_operator_output_space="strip supremum on the declared old physical angle strip",
                    amplitude_Wiener_and_sup_spaces_separately_labelled=True,
                    old_circle_I_J_and_independent_mean_budget_paid=False,
                    canonical_to_old_second_derivative_Cauchy_chain_used=False)
            tag=str(width.numerator)+"_"+str(width.denominator)
            result=stage("complete-old-derivative-budget-"+tag,build_budget)
            summaries.append(result)
        doc["first_correction_derivative_budgets"]=summaries
        doc["complete_Fourier_coefficient_support"]=[
            dict(degree=p,a1_range=[a1[p].lo,a1[p].hi],b1_range=[b1[p].lo,b1[p].hi],
                a1_proved_bound=192*(p+1),b1_proved_bound=192*(p+2)) for p in range(ORDER+1)]
        gate("all complete old-radial derivative budgets retain positive angular and radial Cauchy losses",
            len(summaries)==len(WIDTHS)
            and all(Q(v["exact_output_phi_width"])<SIGMA for v in summaries))
        gate("all original no-recomputation and scope limits remain exact",
            doc["original_target_FFT_or_high_root_stages_recomputed"]==0
            and doc["original_auxiliary_fold_forcing_or_domain_stages_recomputed"]==0
            and not doc["old_circle_I_J_or_independent_even_mean_budget_paid"]
            and not doc["complete_strong_return_or_cutoff97_inverse_claimed"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            new_cubic_true_root_component_rows=doc["new_cubic_true_root_component_rows"],
            new_finite_algebra_stages=doc["new_finite_algebra_stages"],
            reused_finite_algebra_stages=doc["reused_finite_algebra_stages"],
            native_sha256=sha(a.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()

#!/usr/bin/env python3
"""Evaluate new auxiliary domains of the identical original root-piece germ.

Six complete primitive jets pay complex intrinsic derivatives through order3.
All65/193 original cubic components and the complete mean are retained.
The extension is auxiliary; no physical polynomial seam is crossed by a claim.
"""
from __future__ import annotations
import argparse,gzip,hashlib,io,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
import flint
from flint import acb,arb,ctx
from fourfold_codazzi_cubic_target_jets import CubicCodazziTarget
from fourfold_phase_beta_bulk_box import Box,cdot,reduce_box

PUBLIC="Rogerhu12/math-research-public"
ROOT_SHA="397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
BUDGET_SHA="10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
DIRECTION_INDEX="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
DELTA=Q(1,10**8)
RADII=(Q(1,10000),Q(1,2000),Q(1,1000),Q(1,500))
WIDTHS=(Q(1,64),Q(1,32),Q(1,16))

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,separators=(",",":"),allow_nan=False)+"\n").encode()
    if p.suffix==".gz":raw=gzip.compress(raw,compresslevel=9,mtime=0)
    tmp=p.with_name(p.name+".partial");tmp.write_bytes(raw);tmp.replace(p)
def ex(x):
    x=Q(x);return arb(x.numerator)/x.denominator
def dyadic(x):return Q.from_float(float(x))
def up(x):return abs(x).upper()
def rec(x):
    x=arb(x)
    if not x.is_finite():raise ValueError("nonfinite auxiliary complex bound")
    return dict(ball=x.str(48),lower=x.lower().str(48),upper=x.upper().str(48))
def compact(x):return dict(ball=arb(x).str(48))
def crecord(z):
    z=acb(z)
    if not z.is_finite():raise ValueError("nonfinite auxiliary complex jet")
    return dict(real=rec(z.real),imag=rec(z.imag),modulus_upper=rec(up(z)))
def box(d):
    if "lower" in d and "upper" in d:return arb(d["lower"]).lower().union(arb(d["upper"]).upper())
    return arb(d["ball"])
def cb(d):return acb(box(d["real"]),box(d["imag"]))
def interval(a,b):return ex(a).union(ex(b))
def square(radius):
    r=arb(radius).upper();return acb(arb(0,r),arb(0,r))
def ipow(x,n):
    if n<0:raise ValueError("only bounded nonnegative powers are used")
    y=1
    for _ in range(n):y=y*x
    return y
def encode(v):
    if isinstance(v,dict):return {k:encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    return compact(v)
def mul(a,b,count=None):
    count=min(len(a),len(b)) if count is None else count
    return [sum((a[j]*b[i-j] for j in range(i+1)
        if j<len(a) and i-j<len(b)),acb(0)) for i in range(count)]
def inv(a):
    b=[1/a[0]]
    for i in range(1,len(a)):
        b.append(-b[0]*sum((a[j]*b[i-j] for j in range(1,i+1)),acb(0)))
    return b
def sqrt_series(a):
    b=[a[0].sqrt()]
    for i in range(1,len(a)):
        b.append((a[i]-sum((b[j]*b[i-j] for j in range(1,i)),acb(0)))/(2*b[0]))
    return b
def diff(a):return [(j+1)*a[j+1] for j in range(len(a)-1)]
def complex_intrinsic(target,radial):
    """E4--E7: complete bilinear zero convolution, before complex division."""
    F,_,a,EF,_,tail=target.scalar_jets_and_fourier(radial)
    if len(F)!=6 or len(EF)!=6 or len(a.real.lo)!=6:
        raise ValueError("the full six original primitive jets were not returned")
    aa=[a[j].to_acb() for j in range(6)]
    reverse=(-np.arange(target.nodes))%target.nodes
    norms=[arb(float(np.max(reduce_box(Box(f.magnitude_upper())).hi))).upper() for f in F]
    means={};fees={}
    def mean(i,j):
        key=str(min(i,j))+","+str(max(i,j))
        if key not in means:
            finite=cdot(F[i],F[j][reverse]).sum().to_acb()
            fee=(3*(norms[i]*EF[j][0]+norms[j]*EF[i][0]+EF[i][0]*EF[j][0])).upper()
            means[key]=finite+square(fee);fees[key]=fee
        return means[key]
    Ej=[sum((math.comb(k,j)*mean(j+1,k-j+1) for j in range(k+1)),acb(0))
        for k in range(5)]
    ar=[aa[j]/math.factorial(j) for j in range(6)]
    er=[Ej[j]/math.factorial(j) for j in range(5)]
    gap0=Ej[0]-aa[1]*aa[1]
    evidence=dict(original_scalar_polynomial_degree_at_most=20,
        exact_bilinear_zero_convolution_without_conjugation=True,
        original_complete_primitive_nodes=target.nodes,
        full_primitive_tail=rec(tail),
        complete_primitive_radial_errors=[rec(e[0]) for e in EF],
        complete_finite_field_component_Wiener_bounds=[rec(x) for x in norms],
        full_product_mean_error_fees={k:rec(v) for k,v in fees.items()},
        physical_radius_ordinary_jets=[crecord(z) for z in aa],
        radial_metric_ordinary_jets=[crecord(z) for z in Ej],
        denominator_gaps={k:rec(z.real.lower()) for k,z in
            (("radius_real",aa[0]),("E_real",Ej[0]),("rotational_gap_real",gap0))})
    if not (aa[0].real>0 and Ej[0].real>0 and gap0.real>0):
        return None,evidence,"a complete auxiliary intrinsic denominator leaves the right half-plane"
    ia,ie=inv(ar),inv(er)
    first=mul(mul(diff(diff(ar)),ia),ie)
    second=mul(mul(mul(mul(diff(ar),diff(er)),ia),ie),ie)
    curvature=[-first[j]+second[j]/2 for j in range(4)]
    beta=mul(diff(ar),ia)[:4]
    gamma=mul(sqrt_series(er),ia)[:4]
    slope=diff(ar)
    sq=mul(slope,slope,4)
    gap=[er[j]-sq[j] for j in range(4)]
    rotation=[-z for z in mul(ar,sqrt_series(mul(er[:4],inv(gap))))[:4]]
    jets={name:[math.factorial(j)*v[j] for j in range(4)]
        for name,v in (("K",curvature),("beta",beta),("gamma",gamma),("s",rotation))}
    evidence["ordinary_intrinsic_jets"]={k:[crecord(z) for z in v] for k,v in jets.items()}
    evidence["root_slope_real_lower"]=rec(jets["K"][1].real.lower())
    evidence["minus_rotational_real_lower"]=rec((-jets["s"][0].real).lower())
    evidence["gamma_real_lower"]=rec(jets["gamma"][0].real.lower())
    if not (jets["K"][1].real>0 and jets["s"][0].real<0 and jets["gamma"][0].real>0):
        return None,evidence,"the complete auxiliary root slope or rotational branch gap is unresolved"
    return jets,evidence,None

def cubic_component(coeff,x):
    c=[acb(ex(dyadic(v))) for v in coeff]
    return [((c[0]*x+c[1])*x+c[2])*x+c[3],
        (3*c[0]*x+2*c[1])*x+c[2],6*c[0]*x+2*c[1],6*c[0]]
def norms(values,start,width,order):
    return sum((v*ex((4*j)**order)*(ex(4*j)*ex(width)).exp()
        for j,v in enumerate(values,start) if order==0 or j),arb(0)).upper()

def family_budget(jets,base_rows,z_rows,offsets,repair_fee):
    base=[[cb(row["ordinary_derivatives"][p]) for row in base_rows] for p in range(4)]
    z=[[up(cb(row["ordinary_derivatives"][p]))+
        (repair_fee[i] if p==0 else arb(0)) for i,row in enumerate(z_rows)] for p in range(4)]
    for i,value in enumerate(offsets):base[0][i]+=acb(ex(value))
    for p in range(4):base[p][32]+=jets["s"][p]
    means=[base[p][32]+square(ex(DELTA)*z[p][96]) for p in range(4)]
    eta=[-sum((math.comb(p,j)*jets["gamma"][j]*means[p-j] for j in range(p+1)),acb(0))
        for p in range(4)]
    whole=dict(complete_mean_ordinary_jets=[crecord(v) for v in means],
        complete_eta_ordinary_jets=[crecord(v) for v in eta],
        complex_parameter_enclosed_by_full_component_disks=True,
        exact_background_value_offsets_retained=True,
        every_positive_order_value_repair_derivative_zero=True)
    if not (means[0].real<0 and eta[0].real>0):
        return whole,False,"the complete auxiliary mean or eta branch is unresolved"
    kbox=jets["K"][1]
    achar=eta[0]*kbox.sqrt()
    whole["complex_divided_curvature_enclosure"]=crecord(kbox)
    whole["complex_root_characteristic_enclosure"]=crecord(achar)
    whole["root_characteristic_real_lower"]=rec(achar.real.lower())
    whole["divided_curvature_radial_derivative_bounds"]=[
        rec(up(jets["K"][2])/2),rec(up(jets["K"][3])/3)]
    strips={}
    for width in WIDTHS:
        U=[];V=[];Vnon=[]
        for p in range(4):
            ub=[up(base[p][j])+ex(DELTA)*z[p][j] for j in range(32)]
            ub.extend(ex(DELTA)*z[p][j] for j in range(32,96))
            vb=[up(base[p][32+j])+ex(DELTA)*z[p][96+j] for j in range(1,33)]
            vb.extend(ex(DELTA)*z[p][96+j] for j in range(33,97))
            U.append([norms(ub,1,width,q) for q in range(5)])
            Vnon.append([norms(vb,1,width,q) for q in range(5)])
            V.append([(Vnon[-1][q]+(up(means[p]) if q==0 else arb(0))).upper()
                for q in range(5)])
        b,K=up(jets["beta"][0]),up(jets["K"][0])
        m=up(means[0]);vn=Vnon[0][0]
        nonmean_S=(U[0][0]*U[0][0]+K*(2*m*vn+vn*vn)).upper()
        d0=(b*nonmean_S/4).upper();d1=(b*nonmean_S).upper()
        d2=(2*b*(U[0][0]*U[0][1]+K*V[0][0]*V[0][1])).upper()
        strips[str(width)]=dict(full_family_U_ordinary_radial_angular_jets=encode(U),
            full_family_V_ordinary_radial_angular_jets=encode(V),
            full_family_V_nonmean_ordinary_radial_angular_jets=encode(Vnon),
            full_drift_angular_bounds=encode([d0,d1,d2]),
            scalar_mean_abs_upper=rec(m),nonmean_S_bound=rec(nonmean_S))
    whole["strips"]=strips
    return whole,bool(achar.real>0),None if achar.real>0 else "the auxiliary characteristic coefficient real-part gap is unresolved"

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","out"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path)
    args=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new auxiliary-domain mathematics runs only in public repository Actions")
    import scipy
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
        numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0"):
        raise RuntimeError("the exact numerical environment changed")
    if args.out.exists():raise FileExistsError("preserve every completed auxiliary domain and failed prefix")
    ctx.prec=320;ctx.cap=4;started=time.monotonic()
    doc=dict(kind="actual_auxiliary_same_root_piece_complete_complex_third_jets_v1",
        complete=False,proved=False,failure=None,gates=[],source_sha256=sha(__file__),runtime=runtime,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        candidate_sha256=CANDIDATE,background_definition_sha256=BASE,explicit_direction_definition_sha256=ZDEF,
        object_sha256=OBJECT,root_germ_sha256=ROOT_SHA,original_root_budget_sha256=BUDGET_SHA,
        actual_intrinsic_parameter="eta_0",exact_complex_delta_radius=str(DELTA),cases=[],
        original_completed_small_domain_results_recomputed=0,new_intrinsic_domains=0,
        reused_intrinsic_domains=0,new_original_cubic_component_jet_rows=0,reused_original_cubic_component_jet_rows=0,
        auxiliary_extension_only=True,physical_background_identity_outside_original_piece_claimed=False,
        every_original_global_seam_and_full_mean_retained=True,
        enlarged_fold_or_first_amplitude_budget_paid=False,full_strong_return_or_cutoff97_inverse_claimed=False)
    def checkpoint():
        doc["seconds"]=time.monotonic()-started;save(args.out,doc)
    def gate(name,truth):
        truth=bool(truth);doc["gates"].append(dict(name=name,passed=truth))
        if not truth:raise ValueError("auxiliary-root input gate failed: "+name)
    try:
        manifest=read(args.manifest);doc["input_manifest_sha256"]=sha(args.manifest)
        for entry in manifest["files"]:
            f=args.repo_root/entry["path"]
            if not f.is_file() or sha(f)!=entry["sha256"] or f.stat().st_size!=entry["bytes"]:
                raise ValueError("an exact original input changed: "+entry["path"])
        paths={k:args.repo_root/v for k,v in manifest["input_paths"].items()}
        germ,rb,cp,zp=[read(paths[k]) for k in ("root_germ","root_budget","candidate_index","response_index")]
        gate("the original complete root, physical background and full direction identities are unchanged",
            sha(paths["root_germ"])==ROOT_SHA and sha(paths["root_budget"])==BUDGET_SHA
            and sha(paths["object"])==OBJECT and sha(paths["candidate_index"])==CANDIDATE
            and sha(paths["response_index"])==DIRECTION_INDEX
            and germ["complete"] and germ["proved"] and germ["failure"] is None
            and rb["complete"] and rb["proved"] and rb["failure"] is None
            and rb["background_definition_sha256"]==BASE and rb["explicit_direction_definition_sha256"]==ZDEF
            and rb["actual_intrinsic_parameter"]=="eta_0" and germ["object_sha256"]==OBJECT)
        roots=list(map(Q,germ["root_interval"]));cell=list(map(Q,germ["exact_candidate_piece_interval"]))
        scalarcell=list(map(Q,germ["original_scalar_germ"]))
        offsets=list(map(Q,rb["exact_background_root_offsets"]))
        alpha=Q(cp["metadata"]["exact_float_amplitude"])
        raw=rb["response_raw_complete_coefficient_upper"];repaired=rb["response_repaired_complete_coefficient_upper"]
        repair_fee=[(arb(b["upper"]).upper()-arb(a["lower"]).lower()).upper() for a,b in zip(raw,repaired)]
        gate("the identical original scalar and polynomial germs contain the root and retain every repair",
            germ["actual_candidate_piece"]==rb["exact_candidate_and_response_piece"]==2549
            and list(map(Q,rb["exact_piece_interval"]))==cell and len(offsets)==65 and len(repair_fee)==193
            and all(e>=0 and e.is_finite() for e in repair_fee)
            and cell[0]<roots[0]<=roots[1]<cell[1] and scalarcell[0]<roots[0]<=roots[1]<scalarcell[1]
            and germ["compact_bump_identically_zero_on_entire_actual_germ"]
            and roots[0]-max(RADII)>Q(9,50)
            and Q(rb["exact_complex_parameter_radius"])==DELTA
            and cp["coefficient_shape"]==[4,6144,65] and zp["coefficient_shape"]==[4,6144,193]
            and zp["metadata"]["finite_head_mean_was_not_removed_from_the_solve"]
            and alpha==Q(germ["exact_amplitude"])
            and rb["exact_intrinsic_parameter"]==germ["exact_center_parameter"])
        doc.update(exact_root_interval=list(map(str,roots)),original_scalar_germ=list(map(str,scalarcell)),
            original_polynomial_piece=2549,exact_original_piece_interval=list(map(str,cell)),
            exact_physical_candidate_amplitude=str(alpha),exact_intrinsic_affine_center=germ["exact_center_parameter"],
            exact_intrinsic_affine_half_width=germ["exact_parameter_half_width"],
            complete_constant_direction_repair_fees=[rec(v) for v in repair_fee])
        shards={}
        for name,index,first,end,count,psha in (
            ("candidate",cp,1346,2692,65,"3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106"),
            ("response",zp,2265,2718,193,"ce29c19c81e77cb2f2ea9b70edc59af96a869116fa96e2e5375ffa4d61927917")):
            part=next(e for e in index["parts"] if e["first_interval"]<=2549<e["last_interval_exclusive"])
            path=paths[name+"_shard"];local=2549-first
            gate("the_original_"+name+"_shard_is_unchanged_and_complete",
                part["first_interval"]==first and part["last_interval_exclusive"]==end
                and part["sha256"]==sha(path)==psha and part["bytes"]==path.stat().st_size
                and part["file"]==path.name)
            with np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False) as z:
                nodes=z["radial_nodes"].copy();coeff=z["piece_coefficients"].copy()
            gate("the_original_"+name+"_array_has_its_true_piece_and_all_components",
                nodes.shape==(end-first+1,) and coeff.shape==(4,end-first,count)
                and np.isfinite(nodes).all() and np.isfinite(coeff).all() and (np.diff(nodes)>0).all()
                and [dyadic(nodes[local]),dyadic(nodes[local+1])]==cell)
            shards[name]=coeff[:,local,:].copy()
        if args.resume:
            previous=read(args.resume)
            gate("all accepted auxiliary domain prefixes have identical source runtime and exact inputs",
                previous["source_sha256"]==sha(__file__) and previous["input_manifest_sha256"]==sha(args.manifest)
                and previous["runtime"]==runtime and previous["root_germ_sha256"]==ROOT_SHA
                and previous["original_root_budget_sha256"]==BUDGET_SHA)
            doc["cases"]=previous["cases"]
        target=CubicCodazziTarget(paths["object"],Q(germ["exact_parameter_half_width"]),512,4096)
        target.set_cell(*scalarcell)
        gate("the original polynomial anchor and whole affine parameter box remain fixed",
            tuple(target.cell)==tuple(scalarcell) and target.nodes==512
            and target.metric_half_width==Q(germ["exact_parameter_half_width"]))
        for ci,radius in enumerate(RADII):
            left,right=roots[0]-radius,roots[1]+radius
            if ci<len(doc["cases"]):
                case=doc["cases"][ci]
                if case["exact_auxiliary_radius"]!=str(radius) or case["exact_complex_rectangle"]!=dict(
                    real_interval=[str(left),str(right)],imaginary_half_width=str(radius)):
                    raise ValueError("an accepted new auxiliary domain changed its exact rectangle")
                if case.get("complete"):
                    doc["reused_intrinsic_domains"]+=int(case.get("intrinsic_evaluation_complete",False))
                    doc["reused_original_cubic_component_jet_rows"]+=sum(len(v) for v in case.get("polynomial_component_jets",{}).values())
                    continue
            else:
                case=dict(exact_auxiliary_radius=str(radius),
                    exact_complex_rectangle=dict(real_interval=[str(left),str(right)],imaginary_half_width=str(radius)),
                    complete=False,proved=False,failure=None,polynomial_component_jets={"candidate":[],"response":[]})
                doc["cases"].append(case)
            doc["last_attempted_domain"]=ci;checkpoint()
            radial=acb(interval(left,right),arb(0,ex(radius)))
            if case.get("intrinsic_evaluation_complete"):
                evidence=case["complete_complex_intrinsic_evidence"]
                jets={k:[cb(v) for v in vs] for k,vs in evidence.get("ordinary_intrinsic_jets",{}).items()}
                error=case.get("intrinsic_domain_failure")
                doc["reused_intrinsic_domains"]+=1
            else:
                jets,evidence,error=complex_intrinsic(target,radial)
                case["complete_complex_intrinsic_evidence"]=evidence
                case["intrinsic_domain_failure"]=error;case["intrinsic_evaluation_complete"]=True
                doc["new_intrinsic_domains"]+=1;checkpoint()
            if error is not None:
                case.update(complete=True,proved=False,failure=error);checkpoint();continue
            x=radial-acb(ex(cell[0]))
            for name,count in (("candidate",65),("response",193)):
                accepted=case["polynomial_component_jets"][name]
                if len(accepted)>count:raise ValueError("an accepted polynomial prefix gained a component")
                doc["reused_original_cubic_component_jet_rows"]+=len(accepted)
                for j in range(count):
                    if j<len(accepted):
                        if accepted[j]["component"]!=j:raise ValueError("an accepted cubic prefix changed component")
                        continue
                    values=cubic_component(shards[name][:,j],x)
                    if name=="candidate":values=[ex(alpha)*v for v in values]
                    accepted.append(dict(component=j,ordinary_derivatives=[crecord(v) for v in values]))
                    doc["new_original_cubic_component_jet_rows"]+=1
                    if j%32==0:checkpoint()
                checkpoint()
            budget,okay,error=family_budget(jets,case["polynomial_component_jets"]["candidate"],
                case["polynomial_component_jets"]["response"],offsets,repair_fee)
            case["complete_family_budget"]=budget
            case.update(complete=True,proved=okay,failure=error,
                exact_identity_with_original_family_only_on_original_germ_intersection=True,
                auxiliary_continuation_does_not_replace_neighboring_physical_pieces=True)
            checkpoint()
        doc["all_requested_domains_attempted"]=len(doc["cases"])==len(RADII) and all(x["complete"] for x in doc["cases"])
        doc["successful_auxiliary_domains"]=[x["exact_auxiliary_radius"] for x in doc["cases"] if x["proved"]]
        doc["failed_auxiliary_domains"]=[dict(radius=x["exact_auxiliary_radius"],failure=x["failure"])
            for x in doc["cases"] if not x["proved"]]
        doc["complete"]=doc["all_requested_domains_attempted"]
        doc["proved"]=doc["complete"] and not doc["failed_auxiliary_domains"]
        doc.pop("last_attempted_domain",None)
        if not doc["proved"]:raise RuntimeError("one or more actual auxiliary-domain gaps failed; all successful prefixes are retained")
        gate("all four new auxiliary domains retain complete third jets every finite component and the full mean",
            len(doc["successful_auxiliary_domains"])==4
            and all(len(x["polynomial_component_jets"]["candidate"])==65
                and len(x["polynomial_component_jets"]["response"])==193 for x in doc["cases"]))
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            attempted=len(doc["cases"]),successful=doc.get("successful_auxiliary_domains",[]),
            native_sha256=sha(args.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()

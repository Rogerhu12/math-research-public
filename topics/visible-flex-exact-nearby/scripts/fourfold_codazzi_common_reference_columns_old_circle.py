#!/usr/bin/env python3
"""Genuine common-radial column constants and complete old-circle inverse gates.

Only public Actions evaluates these new scalar consequences. The original
potential, complete fold and every accepted target/FFT/Taylor coefficient are
read unchanged. Only small actual conclusions and execution metadata persist.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
POTENTIAL_EXECUTION="d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9"
POTENTIAL_SOURCE="042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7"
POTENTIAL_MANIFEST="44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437"
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
COLUMNS_PROOF="0e56cf640b5c5f46c917699396e0ef6e5cce1fd5276cbddfc56ee1ed58d89c49"
INVERSE_PROOF="edede2b11d5f798ebb98012dde34e92dc92fbbf4eed0511db396b8e94ac88015"
FOLD_PROOF="63e76681a33b5dd319e7de0c14a6812a3d6ec5aede641fe066af25f28bf06d10"
RG=Q(3,8000);SG=Q(3,128);H=Q(1,20000)
SIGMA=Q(1,64);NARROW=Q(1,128);L=Q(1,2000);M=276
N0=388;CUTOFF=97;DELTA=Q(1,10**8)
ROOT_COVER=Q(893368603925465506687,21990232555520000000000000)
PARAMETERS=dict(arb_precision_bits=320,fixed_intrinsic_parameter="eta_0",
    minimum_absolute_fourfold_mode=97,minimum_physical_frequency=388,
    exact_real_reference_T_radius="1/2000",reference_potential_modulus=276,
    exact_old_rho_radius="1/20000",exact_original_fold_radius="3/8000",
    exact_original_fold_phi_strip="3/128",exact_inverse_phi_strip="1/64",
    exact_Wiener_phi_strip="1/128",exact_complex_delta_square_halfwidth="1/100000000",
    independent_even_mean_retained=True,both_carrier_signs_retained=True)

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def phash(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def save(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(v,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    if p.suffix==".gz":raw=gzip.compress(raw,compresslevel=6,mtime=0)
    tmp=p.with_name(p.name+".partial");tmp.write_bytes(raw);tmp.replace(p)
def ex(q):
    q=Q(q);return arb(q.numerator)/arb(q.denominator)
def rb(v):
    if isinstance(v,(str,int)):return arb(v)
    if isinstance(v,Q):return ex(v)
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def up(v):
    if isinstance(v,(int,Q)):v=ex(v)
    return abs(v).upper()
def lo(v):return arb(v).lower()
def positive(v,name):
    v=arb(v)
    if not v.is_finite() or not v.lower()>0:
        raise ValueError("strict positive complete denominator required: "+name)
    return v
def power(v,p):
    # Keep the complete directed ball; never insert an upper positive power
    # into a denominator. Every eventual modulus is taken after the expression.
    return (positive(v,"power base").log()*ex(p)).exp()
def rec(v):
    v=arb(v)
    if not v.is_finite():raise ValueError("nonfinite final scalar conclusion")
    return dict(ball=v.str(64))
def pack(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):pack(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [pack(x) for x in v]
    if isinstance(v,(bool,str,int,float)) or v is None:return v
    raise TypeError("unrecorded scalar conclusion "+type(v).__name__)
def unpack(v):
    if isinstance(v,dict):
        if set(v)=={"ball"}:return arb(v["ball"])
        return {k:unpack(x) for k,x in v.items()}
    if isinstance(v,list):return [unpack(x) for x in v]
    return v
def maximum(a,b):return max(up(a),up(b)).upper()
def minimum(a,b):return min(up(a),up(b)).upper()

def column_budget(gate):
    lam=power(ex(N0),Q(2,3))
    taup=(8*ex(M)*ex(L)/lam).upper()
    ep=taup.exp().upper()
    aerr=(4*ex(M)*ex(L)/lam*ep).upper()
    agap=lo(1-aerr);positive(agap,"root a coefficient")
    shear_coefficient=(arb.pi()*ex(M)*ep/(9*agap)).upper()
    # This complete coefficient multiplies n^(-4/3).
    shear_uniform=(shear_coefficient/power(ex(N0),Q(4,3))).upper()
    pos=(ep/agap).upper()
    taun=(8*arb.pi()*ex(M)*ex(L)/lam).upper()
    en=taun.exp().upper()
    root=(1+shear_uniform).upper()
    neg=(en*root).upper()
    gate("the complete real reference interval fits the paid rational Volterra thresholds",
        lam.lower()>52 and taup<ex(Q(1,40)) and taun<ex(Q(1,10)))
    gate("the complete root normalization is nonzero and retains its full n to minus four thirds shear",
        aerr<ex(Q(1,78)) and agap>ex(Q(77,78))
        and shear_coefficient<ex(Q(M,2)) and shear_uniform<ex(Q(1,19)))
    gate("both positive weighted columns and both negative relative directions obey their complete bounds",
        pos<ex(Q(21,20)) and ep<ex(Q(21,20))
        and neg<ex(Q(6,5)) and en<ex(Q(10,9)))
    return dict(exact_real_T_interval=[str(-L),str(L)],complete_potential_modulus_used=M,
        all_abs_j_at_least=CUTOFF,physical_frequency="n=4|j|",
        lambda_at_minimum_frequency_lower=rec(lam.lower()),
        positive_Volterra_exponent_upper=rec(taup),
        negative_Volterra_exponent_upper=rec(taun),
        root_a_distance_from_one_upper=rec(aerr),root_a_modulus_lower=rec(agap),
        root_shear_coefficient_of_n_to_minus_four_thirds_upper=rec(shear_coefficient),
        root_shear_uniform_modulus_upper=rec(shear_uniform),
        exact_root_relative_matrix="[[1,0],[beta_n,1]]",
        exact_Wronskian="n^(2/3)/pi",
        complete_positive_Ai_weighted_height_and_derivative_factor=rec(pos),
        complete_positive_Bi_weighted_height_and_derivative_factor=rec(ep),
        negative_relative_basis_and_inverse_factor=rec(neg),
        negative_complete_relative_propagator_and_inverse_factor=rec(en),
        both_independent_columns_retained=True,both_carrier_signs_retained=True,
        ordinary_two_source_rows_retained=True,ordinary_g2_radial_derivative_used=False,
        physical_positive_boundary_row_selected_by_Ai_terminal_data=False,
        complex_T_uniform_column_bound_claimed=False,
        physical_mean_is_not_z_zero_limit=True,
        numerical_reference_column_samples_computed=0)

def inverse_budget(f,c,potential,gate):
    d1=up(c["D"][1]);ap=up(f["Ap"]);bt=up(f["BT"])
    if not all(v.is_finite() and v.lower()>=0 for v in (d1,ap,bt)):
        raise ValueError("original complete majorants must be finite nonnegative enclosures")
    e=(d1*ex(H)).exp().upper();d=(e-1).upper()
    t=(ex(H)*power(ap,Q(2,3))).upper()
    y=(bt*ex(H/RG)*ex(H/RG)).upper()
    image=rb(potential["reference_image"]["complete_image_disk_radius_lower"]).lower()
    oldcover=Q(potential["reference_image"]["exact_whole_physical_root_cover_radius"])
    gate("the smaller product covers the whole physical root piece and keeps both positive angular margins",
        oldcover==ROOT_COVER and H>=oldcover and H<RG and 0<NARROW<SIGMA<SG)
    gate("the actual old fold image lies inside both the real reference interval radius and the full complex potential disk",
        t<ex(L) and ex(L)<image)
    v=[up(rb(potential["complete_modulus_upper"][k])) for k in ("V","V_T","V_TT")]
    gate("the previously proved complete potential value and both derivatives are consumed without recomputation",
        v[0]<M and all(x.is_finite() and x.lower()>=0 for x in v))
    n2=ex(N0*N0);g=lo(1-2*d-d*d-t*y*y);positive(g,"complete free Bplus gap")
    theta=(y*y*v[0]/g/n2).upper()
    gv=lo(g-y*y*v[0]/n2);positive(gv,"complete deformed determinant gap")
    gate("the full complex old-circle determinant keeps the genuine Bplus factor and all high input modes",
        g>0 and theta<1 and gv>0)
    hfree=(e+maximum(t*y,y)).upper();bfree=(hfree/g).upper()
    h0=(e+maximum(y*(t+v[0]/n2),y)).upper()
    inv0=minimum(h0/gv,bfree+y*v[0]*bfree*bfree/(n2*positive(1-theta,"Sherman Morrison gap")))
    margin=ex(SG-SIGMA);x=[e,(d/margin).upper(),(2*d/(margin*margin)).upper()]
    yy=[y,(y/margin).upper(),(2*y/(margin*margin)).upper()]
    vv=[v[0],(v[1]*yy[0]).upper(),(v[2]*yy[0]*yy[0]+v[1]*yy[1]).upper()]
    aa=[(t+vv[0]/n2).upper(),(yy[0]+vv[1]/n2).upper(),(yy[1]+vv[2]/n2).upper()]
    u=[(yy[0]*aa[0]).upper(),(yy[1]*aa[0]+yy[0]*aa[1]).upper(),
       (yy[2]*aa[0]+2*yy[1]*aa[1]+yy[0]*aa[2]).upper()]
    hh=[(x[q]+maximum(u[q],yy[q])).upper() for q in range(3)]
    bb=[inv0,(inv0*inv0*hh[1]).upper(),
        (2*inv0*inv0*inv0*hh[1]*hh[1]+inv0*inv0*hh[2]).upper()]
    gate("the full ordered inverse and both angular derivatives are finite on the same complex product",
        all(a.is_finite() and a.lower()>=0 for a in bb+hh+vv))
    delta=ex(SIGMA-NARROW)
    cf=(1+2/positive((4*delta).exp()-1,"positive strip to Wiener margin")).upper()
    error0=(d+maximum(y*(t+v[0]/n2),y)).upper()
    w0=minimum(cf*bb[0],1+cf*bb[0]*error0)
    ww=[w0,(cf*bb[1]).upper(),(cf*bb[2]).upper()]
    gate("the narrower complete Wiener bounds include both output signs and the true zero mode",
        cf>1 and all(a.is_finite() and a.lower()>=0 for a in ww))
    return dict(exact_old_rho_radius=str(H),exact_original_fold_radius=str(RG),
        exact_original_fold_phi_strip=str(SG),exact_inverse_phi_strip=str(SIGMA),
        exact_Wiener_phi_strip=str(NARROW),exact_full_physical_root_cover=str(ROOT_COVER),
        old_fold_image_modulus_upper=rec(t),
        actual_common_potential_image_radius_lower=rec(image),
        full_physical_root_piece_covered=True,
        physical_other_cubic_identity_claimed=False,
        complete_free_Bplus_modulus_lower=rec(g),
        complete_deformed_determinant_modulus_lower=rec(gv),
        full_zeta_modulus_upper=rec(theta),
        complete_HV_angular_derivative_bounds=[rec(a) for a in hh],
        complete_inverse_HV_angular_derivative_bounds=[rec(a) for a in bb],
        complete_composed_V_angular_derivative_bounds=[rec(a) for a in vv],
        exact_positive_conversion_margin=str(SIGMA-NARROW),
        complete_two_signed_Fourier_conversion_factor=rec(cf),
        inverse_constant_subtraction="-i epsilon times identity, retained exactly",
        complete_inverse_Wiener_angular_derivative_bounds=[rec(a) for a in ww],
        same_strip_sup_called_Wiener=False,only_two_angular_derivatives_paid=True,
        full_mean_output_retained=True,physical_primitive_projection_retained=True,
        full_J_inverse_or_parity_domain_extended=False,
        actual_reference_seam_jumps_retained=True,
        old_original_fold_majorants_recomputed=0,
        final_complex_old_circle_inverse_matrix_paid=True,
        full_complex_angle_reference_column_norm_paid=False,
        full_strong_return_or_high_BVP_inverse_paid=False)

def render(doc,manifest_path):
    lines=["# Genuine common-radial columns and old-circle inverse: actual result","",
        "**Scope:** the same fixed intrinsic eta_0 and complete complex explicit family; all |j| >= 97 and both signs.","",
        "- Public repository: "+PUBLIC,
        "- Actual run: "+str(doc["run_id"])+"/"+str(doc["run_attempt"]),
        "- Scientific source: "+TOPIC+"scripts/fourfold_codazzi_common_reference_columns_old_circle.py",
        "- Source SHA256: "+doc["source_sha256"],
        "- Manifest: "+str(manifest_path),
        "- Manifest SHA256: "+doc["input_manifest_sha256"],
        "- Command: --repo IMMUTABLE --manifest MANIFEST --manifest-sha SHA --out-dir TEMPORARY",
        "- Actual return code: "+str(doc["actual_returncode"]),
        "- Complete/proved: "+str(doc["complete"])+"/"+str(doc["proved"]),
        "- Old target, FFT, phase, potential, accepted derivative or old norm recomputations: 0.",
        "- New reference column samples: 0; only the new proved scalar constants and inverse gates are evaluated.",
        "- New reproducible data retained in repository, Release, or artifact: none.",""]
    for heading,key in (("Actual real-axis two-column bounds","reference_columns"),
                        ("Actual complex old-circle inverse bounds","old_circle_inverse")):
        lines+=["## "+heading,""]
        v=doc.get(key)
        if v is None:lines+=["This stage did not complete.",""];continue
        for k,x in v.items():
            if isinstance(x,dict) and set(x)=={"ball"}:s=x["ball"]
            elif isinstance(x,list):s=json.dumps(x,separators=(",",":"))
            else:s=str(x)
            lines.append("- "+k+": "+s)
        lines.append("")
    lines+=["## Actual gates",""]
    for g in doc["gates"]:lines.append("- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"])
    lines+=["","## Remaining scope","",
        "The new reference keeps both real-axis columns and both ordinary physical source rows. The physical positive boundary row and independent mean are still explicit. A positive growing column is not discarded.",
        "The complex old-circle matrix inverse does not itself prove a complex-angle column norm, a full primitive/inverse remainder, a physical positive Schur denominator, or the global low/high return inverse. True physical seam and moving projection terms remain.",
        "The auxiliary radial identity with the physical background is limited to original piece2549. The true root remains fixed; no realized nonlinear parameter or final family is claimed.",""]
    if doc["failure"] is not None:lines+=["## Actual failure","",json.dumps(doc["failure"],ensure_ascii=False),""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","manifest","out-dir"):p.add_argument("--"+k,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics runs only in the authorized public Actions repository")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,
                 numpy=np.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the reviewed complete runtime changed")
    ctx.prec=320;ctx.cap=4;a.out_dir.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    doc=dict(kind="actual_genuine_common_reference_columns_and_old_circle_inverse",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,
        complete=False,proved=False,actual_returncode=None,failure=None,gates=[],
        original_target_FFT_intrinsic_or_point_derivatives_recomputed=0,
        original_saved_characteristic_or_Fourier_coefficients_recomputed=0,
        original_complete_potential_or_fold_bounds_recomputed=0,original_reproducible_inputs_modified=0,
        numerical_reference_column_samples_computed=0,
        real_reference_columns_proved=False,complex_old_circle_inverse_matrix_proved=False,
        original_mean_and_reference_interface_conditions_retained=True,
        full_complex_angle_column_norm_proved=False,full_high_inverse_claimed=False,
        reproducible_data_published_to_repository=False,reproducible_data_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False)
    def gate(name,condition):
        passed=bool(condition);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError(name)
    def checkpoint():
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-start
        save(a.out_dir/"temporary-common-reference-columns-old-circle.json.gz",doc)
    try:
        m=read(a.manifest);pins={v["path"]:v for v in m["files"]}
        paths={k:a.repo/v for k,v in m["input_paths"].items()}
        gate("the new complete scalar consumer and manifest have their exact independently reviewed identities",
            sha(a.manifest)==a.manifest_sha and m["public_repository"]==PUBLIC
            and m["runtime"]==runtime and m["mathematical_parameters"]==PARAMETERS
            and sha(__file__)==pins[m["scientific_source"]]["sha256"])
        for rel,e in pins.items():
            path=Path(rel)
            if path.is_absolute() or ".." in path.parts or not rel.startswith(TOPIC):
                raise ValueError("a pinned input left the authorized topic")
            actual=a.repo/path
            if not actual.is_file() or actual.stat().st_size!=e["bytes"] or sha(actual)!=e["sha256"]:
                raise ValueError("a complete original or current input differs: "+rel)
        gate("all exact input bytes and both new complete analytic contracts were verified",
            sha(paths["columns_contract"])==COLUMNS_PROOF and sha(paths["contract"])==INVERSE_PROOF
            and sha(paths["fold_contract"])==FOLD_PROOF
            and sha(paths["potential_execution"])==POTENTIAL_EXECUTION
            and sha(paths["old_fold_majorants_stage"])==MAJORANTS
            and sha(paths["adjacent_process"])==APROC and sha(paths["adjacent_publication"])==APUB)
        pe=read(paths["potential_execution"]);pp=pe["actual_scientific_receipt"]
        gate("the original complete potential run actually succeeded with every true gate and no old recomputation",
            pe["repository"]==PUBLIC and pe["run_id"]=="43685624307" and pe["run_attempt"]=="1"
            and pe["complete"] is True and pe["actual_returncode"]==0
            and pe["source_budget_source_sha256"]==POTENTIAL_SOURCE
            and pe["input_manifest_sha256"]==POTENTIAL_MANIFEST
            and pp["complete"] is True and pp["proved"] is True and pp["actual_returncode"]==0
            and pp["failure"] is None and pp["source_sha256"]==POTENTIAL_SOURCE
            and pp["input_manifest_sha256"]==POTENTIAL_MANIFEST and pp["runtime"]==runtime
            and len(pp["gates"])==16 and all(g["passed"] for g in pp["gates"])
            and pp["original_target_FFT_intrinsic_or_point_derivatives_recomputed"]==0
            and pp["original_saved_characteristic_or_Fourier_coefficients_recomputed"]==0)
        pc=next(x for x in pp["cases"] if Q(x["exact_complex_radial_radius"])==Q(1,6000))
        gate("the complete potential case retains eta0, all high modes, both signs and the whole complex explicit box",
            pc["complete"] is True and pc["proved"] is True and pc["failure"] is None
            and pc["fixed_intrinsic_parameter"]=="eta_0"
            and Q(pc["exact_complex_delta_square_halfwidth"])==DELTA
            and Q(pc["exact_complex_z_square_halfwidth"])==Q(1,CUTOFF*CUTOFF)
            and pc["all_integer_modes_abs_j_at_least"]==CUTOFF
            and pc["physical_angular_frequency"]=="4j" and pc["both_carrier_signs_retained"] is True
            and pc["physical_mean_is_not_z_zero_limit"] is True
            and pc["whole_complex_bilinear_family"] is True
            and pc["reference_image"]["entire_original_physical_root_piece_covered"] is True)
        gate("the actual complete potential modulus and disk pay the chosen entire real reference interval",
            up(rb(pc["complete_modulus_upper"]["V"]))<M
            and rb(pc["reference_image"]["complete_image_disk_radius_lower"]).lower()>ex(L))
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        mr=next(x for x in au["files"] if x["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz")
        gate("the original full fold is reused with its unique unchanged accepted stage lineage",
            ms["complete"] is True and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
            and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==runtime
            and ms["payload_sha256"]==phash(ms["payload"])
            and mr["bytes"]==paths["old_fold_majorants_stage"].stat().st_size and mr["sha256"]==MAJORANTS
            and ap["actual_returncode"]==0 and ap["mathematical_complete"] and ap["mathematical_proved"]
            and ap["mathematical_failure"] is None and au["complete"]
            and ms["payload"]["majorants"]["A"][1:]==[str(RG),str(SG)])
        original=unpack(ms["payload"])
        doc["reference_columns"]=column_budget(gate);doc["real_reference_columns_proved"]=True;checkpoint()
        doc["old_circle_inverse"]=inverse_budget(original["fold"],original["coefficients"],pc,gate)
        doc["complex_old_circle_inverse_matrix_proved"]=True;checkpoint()
        gate("all old-circle projections, physical positive ports, true seams and the independent mean remain in scope",
            doc["original_mean_and_reference_interface_conditions_retained"] is True
            and doc["full_complex_angle_column_norm_proved"] is False
            and doc["full_high_inverse_claimed"] is False)
        doc["complete"]=doc["proved"]=True;doc["actual_returncode"]=0
    except BaseException as err:
        doc["actual_returncode"]=1;doc["failure"]=dict(type=type(err).__name__,message=str(err))
    finally:
        checkpoint();native=a.out_dir/"temporary-common-reference-columns-old-circle.json.gz"
        process=dict(doc)
        process.update(temporary_native_sha256=sha(native),temporary_native_bytes=native.stat().st_size,
                       temporary_native_is_not_published=True)
        raw=(json.dumps(process,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
        conclusion=render(doc,m["manifest_path"] if "m" in locals() else str(a.manifest))
        # Only necessary final scalar conclusions and identity/gate metadata
        # are in process. The original fold and potential arrays are not copied.
        if len(raw)>60000 or len(conclusion.encode())>60000:
            small={k:v for k,v in process.items() if k not in ("reference_columns","old_circle_inverse")}
            small["formatting_failure"]="the required small result exceeded60000 bytes"
            small["actual_scientific_returncode"]=doc["actual_returncode"]
            small["complete"]=small["proved"]=False;small["actual_returncode"]=1
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Common reference: incomplete formatter\n\nThe actual scientific return code is preserved in process.json. No certificate arrays were published.\n")
            raise SystemExit(1)
        (a.out_dir/"process.json").write_bytes(raw)
        (a.out_dir/"conclusion.md").write_text(conclusion)
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],
            actual_returncode=doc["actual_returncode"],gates=len(doc["gates"]),
            new_scalar_reference_and_inverse_stages=int(doc["real_reference_columns_proved"])+int(doc["complex_old_circle_inverse_matrix_proved"]),
            old_mathematical_enclosures_recomputed=0,full_high_inverse_claimed=False)),flush=True)
    if doc["actual_returncode"]:raise SystemExit(doc["actual_returncode"])
if __name__=="__main__":main()

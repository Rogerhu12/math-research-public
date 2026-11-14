#!/usr/bin/env python3
"""Exact full193 right trace of the existing continuous explicit direction.

Only the original final NPZ shard is read. Every endpoint coefficient is
evaluated over Fraction, then the original exact continuous offset is added.
No background, target, response solve, prior endpoint certificate or outer
graph is recomputed. This is a new endpoint norm diagnostic, not an inverse.
"""
from __future__ import annotations
import argparse,gzip,hashlib,io,json,os,sys,time
from fractions import Fraction
from pathlib import Path
import numpy as np
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
PINS={
 "trial_index":"ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6",
 "trial_shard":"4a863085ec89c7d7104b4fdf566f9ae380d22eb7b4e4f8b2146cd190c3b4b037",
 "direction":"87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88",
 "outer_summary":"1f8a0eb70945c15b25f94361fcee9e39730afbcfeed39917485139687c55dba6"}
OUTER_NATIVE="75e7c0e1447306a97971ee05dcb68b8d357cb4fffa5c1a37335a6fc29a473424"

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)

def exact(x):
    x=Fraction(x);return arb(x.numerator)/x.denominator

def interval(x):return arb(x["lower"]).lower().union(arb(x["upper"]).upper())

def record(x):
    x=arb(x)
    if not x.is_finite():raise ArithmeticError("nonfinite exact endpoint budget")
    return dict(ball=x.str(80),lower=x.lower().str(80),upper=x.upper().str(80))

def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,ensure_ascii=False,separators=(",",":"),allow_nan=False)+"\n").encode()
    if p.suffix==".gz":raw=gzip.compress(raw,mtime=0)
    temporary=p.with_name(p.name+".partial");temporary.write_bytes(raw);temporary.replace(p)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in PINS:p.add_argument("--"+key.replace("_","-"),type=Path,required=True)
    p.add_argument("--out",type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError("preserve every actual exact endpoint diagnostic")
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("only the actual public repository Actions may compute this diagnostic")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),numpy=np.__version__,python_flint=flint.__version__)
    if runtime!=dict(python="3.12.14",numpy="2.3.5",python_flint="0.9.0"):
        raise RuntimeError("the pinned endpoint arithmetic environment changed")
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    d=dict(kind="actual_full193_exact_right_endpoint_of_continuous_Z_v1",
        complete=False,failure=None,gates=[],runtime=runtime,source_sha256=sha(__file__),
        public_repository=PUBLIC,public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        candidate_sha256=CANDIDATE,background_definition_sha256=BASE,
        explicit_direction_definition_sha256=ZDEF,exact_right_radius="25/8",
        original_response_shards_consumed=[13],original_response_solves_recomputed=0,
        original_target_calls=0,original_endpoint_certificates_recomputed=0,
        complete_mean_retained=True,physical_direction_unscaled_by_alpha=True,
        full_delta_outer_graph_proved=False,full_delta_positive_body_proved=False,
        true_PDE_response_or_parameter_Schur_proved=False,inputs={})
    def gate(name,ok):
        d["gates"].append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError("exact right endpoint gate failed: "+name)
    try:
        for key,pin in PINS.items():
            path=getattr(a,key)
            gate("exact_original_bytes_"+key,sha(path)==pin)
            d["inputs"][key]=dict(sha256=pin,bytes=path.stat().st_size)
        index,Z,outer=(read(x) for x in (a.trial_index,a.direction,a.outer_summary))
        md=index["metadata"];definition=Z["derived_direction_definition"]
        gate("same_complete_physical193_trial_and_independent_mean",
            index["kind"]=="complete_lossless_radial_cubic_shards_v1"
            and index["coefficient_shape"]==[4,6144,193] and index["radial_nodes_count"]==6145
            and index["polynomial_order"]=="numpy/scipy PPoly descending local powers"
            and md["role"]=="response_full" and md["modes"]==96 and md["physical_frequency_factor"]==4
            and md["background_candidate_sha256"]==CANDIDATE
            and md["finite_head_mean_was_not_removed_from_the_solve"]
            and md["original_fourth_Robin_row_retained"]
            and md["coordinates"]=="physical unnormalized moving variation; h1 sine(4j phi), h2 cosine(4j phi) including its true mean")
        gate("same_exact_continuous_direction_and_all6143_original_seams",
            Z.get("complete") and Z["candidate_sha256"]==CANDIDATE
            and Z["background_definition_sha256"]==BASE and Z["derived_direction_definition_sha256"]==ZDEF
            and Z["original_trial_sha256"]==PINS["trial_index"]
            and Z["actual_affine_parameter"]=="eta_0" and Z["exact_affine_offset"]=="0"
            and Z["exact_interface_count"]==6143 and Z["exact_component_interface_count"]==6143*193
            and len(Z["gates"])==7 and all(x["passed"] for x in Z["gates"])
            and definition["exact_interval"]==["0","25/8"]
            and definition["all193_states_and_mean_retained"])
        part=index["parts"][-1]
        gate("one_original_final_shard_has_its_complete_declared_byte_identity",
            len(index["parts"])==14 and part["first_interval"]==5889
            and part["last_interval_exclusive"]==6144 and part["file"]==a.trial_shard.name
            and part["sha256"]==PINS["trial_shard"] and part["bytes"]==a.trial_shard.stat().st_size)
        with np.load(io.BytesIO(gzip.decompress(a.trial_shard.read_bytes())),allow_pickle=False) as data:
            nodes=data["radial_nodes"].copy();coeff=data["piece_coefficients"].copy()
        gate("all255_original_cubics_and_the_true_right_endpoint_are_present",
            nodes.shape==(256,) and coeff.shape==(4,255,193)
            and nodes.dtype==np.float64 and coeff.dtype==np.float64
            and np.isfinite(nodes).all() and np.isfinite(coeff).all()
            and np.all(nodes[1:]>nodes[:-1])
            and Fraction(float(nodes[0]))==Fraction(float(part["radial_left"]))
            and Fraction(float(nodes[-1]))==Fraction(25,8))
        offsets=list(map(Fraction,Z["exact_right_physical_direction_offset"]))
        gate("complete_exact_right_offset_retains_the_independent_mean",
            len(offsets)==193 and offsets[96]==Fraction(Z["exact_right_mean_offset"]))
        h=Fraction(float(nodes[-1]))-Fraction(float(nodes[-2]))
        raw=[]
        for k in range(193):
            v=Fraction(0)
            for j in range(4):v=v*h+Fraction(float(coeff[j,-1,k]))
            raw.append(v)
        values=[x+y for x,y in zip(raw,offsets)]
        gate("all193_exact_dyadic_horner_traces_have_the_same_physical_normalization",
            len(values)==193 and h>0 and all((v-x)==o for v,x,o in zip(values,raw,offsets)))
        gate("same_actual_complete_repaired_outer_summary_and_all25_gates",
            outer.get("complete") and not outer.get("failure") and outer["native_sha256"]==OUTER_NATIVE
            and outer["original_candidate_sha256"]==CANDIDATE and outer["derived_definition_sha256"]==BASE
            and outer["exact_affine_parameter_offset"]=="0"
            and len(outer["gates"])==25 and all(x["passed"] for x in outer["gates"])
            and outer["full_Hone_sixth_Riccati_graph_proved"]
            and outer["independent_even_mean_and_all_head_and_affine_outer_columns_retained"])
        frequencies=list(range(4,385,4))+[0]+list(range(4,385,4))
        groups={"u":range(96),"v_nonmean":range(97,193),"v_including_mean":range(96,193),"full_pair":range(193)}
        norms={}
        for width in (Fraction(0),Fraction(1,128),Fraction(1,64),Fraction(1,32),Fraction(1,16),Fraction(1,8)):
            weights=[(exact(width)*k).exp().upper() for k in frequencies]
            row={}
            for order in range(5):
                row[str(order)]={name:record(sum((exact(abs(values[k]))*weights[k]*frequencies[k]**order
                    for k in ids),arb(0)).upper()) for name,ids in groups.items()}
            norms[str(width)]=row
        mean=exact(abs(values[96]))
        old=outer["bounds"]
        m0lo=interval(old["corrected_endpoint_mean_absolute_lower"]).lower()
        m0hi=interval(old["corrected_endpoint_mean_absolute_upper"]).upper()
        U0=interval(old["corrected_moving_U_Aone_eighth"]).upper()
        V0=interval(old["corrected_moving_Vnonmean_Aone_eighth"]).upper()
        P0=interval(old["corrected_angle_displacement_Aone_eighth"]).upper()
        rows=[]
        for radius in (Fraction(1,10**8),Fraction(1,10**10)):
            r=exact(radius);mlo=(m0lo-r*mean).lower();mhi=(m0hi+r*mean).upper()
            gate("true_independent_mean_terminal_invariant_on_radius_"+str(radius),
                mlo>exact("5.8") and (1-exact(Fraction(1,2*800000**2)))/mhi>exact(Fraction(1,8))
                and 1/mlo<exact(Fraction(1,5)))
            widths={}
            for width in norms:
                nu=interval(norms[width]["0"]["u"]).upper()
                nv=interval(norms[width]["0"]["v_nonmean"]).upper()
                eu=(r*nu).upper();ev=(r*nv).upper();em=(r*mean).upper()
                psi=((ev+em*V0/m0lo)/(4*mlo)).upper()
                widths[width]=dict(delta_u_A0=record(eu),delta_v_nonmean_A0=record(ev),
                    delta_mean_abs=record(em),delta_angle_A0=record(psi),
                    updated_moving_u_A0=record(U0+eu),updated_moving_v_nonmean_A0=record(V0+ev),
                    updated_angle_A0=record(P0+psi),
                    old_Aone_eighth_bounds_restricted_to_this_width=True)
            rows.append(dict(exact_parameter_radius=str(radius),
                true_mean_abs_lower=record(mlo),true_mean_abs_upper=record(mhi),
                pstar_lower=record((1-exact(Fraction(1,2*800000**2)))/mhi),
                pstar_upper=record(1/mlo),width_budgets=widths,
                complete_outer_graph_permission=False))
        gate("all_six_complete_strip_norms_and_orders_zero_through_four_are_finite",
            len(norms)==6 and all(len(x)==5 for x in norms.values()))
        d.update(complete=True,exact_last_piece=6143,exact_last_piece_width=str(h),
            original_raw_right_full193=list(map(str,raw)),
            original_exact_right_offset_full193=list(map(str,offsets)),
            continuous_Z_exact_right_full193=list(map(str,values)),
            exact_independent_mean=str(values[96]),norms=norms,
            complete_parameter_radius_diagnostics=rows,
            original_complete_outer_native_sha256=OUTER_NATIVE,
            outer_true_physical_infinite_Fourier_change_not_yet_paid=True,
            new_background_real_delta_norms_do_not_grant_nonlinear_outer_inverse=True)
    except BaseException as e:
        d["failure"]=dict(type=type(e).__name__,message=str(e));raise
    finally:
        d["seconds"]=time.monotonic()-started;save(a.out,d)
    print(json.dumps(dict(complete=d["complete"],gates=len(d["gates"]),
        seconds=d["seconds"],norms=norms,parameter_radii=rows),allow_nan=False),flush=True)

if __name__=="__main__":main()

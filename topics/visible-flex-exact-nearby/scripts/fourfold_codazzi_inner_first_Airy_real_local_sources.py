#!/usr/bin/env python3
"""New real-angular local source bound; reuse the complete accepted inner result."""
from __future__ import annotations
import argparse,copy,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx
import fourfold_codazzi_inner_first_Airy_complete_sources as O

PUBLIC=O.PUBLIC
INNER="6b5e6c646f02b48d82f25e12a41b329e7ab71d649b39d29c1608ef03a1fd847e"
IPROC="e54c7505255182567a65d7b93af18726dced7cedc8b2284841e268582402946b"
ISOURCE="0b0dc7b3b5c747dd8935f77c75554c60f2b08fd40a6cf5dd27c7c81f5c945fbf"
IMANIFEST="76faab17f11d84dd47e5f4e71695393deba10d6a962ac648ce0b8f3b5a91786b"
PAYLOADS={
 "new-inner-Airy-profile-and-exact-PQ-jets":
 "9809a086152cbf69649dea0a0fcc90710411897caa02863992294530ca2f87b2",
 "all-inner-amplitudes-and-complete-Airy-operators":
 "1f46b066ae07b7d06cf9678040aa4bab0a04232b80f24a899819cef7eea3a0a8"}
SIGMA=Q(1,512)
COEFF_WIDTH=Q(1,32)
sha=O.sha
read=O.read
save=O.save
box=O.box
up=O.up
ex=O.ex
ipow=O.ipow
record=O.record
encode=O.encode
decode=O.decode

def scalar_product(a,b,last=2):
    if min(len(a),len(b))<=last:raise ValueError("an unpaid scalar angular jet")
    return [sum((math.comb(q,l)*a[l]*b[q-l] for l in range(q+1)),arb(0)).upper()
            for q in range(last+1)]

def complete_local_jets(tay,p):
    tables={Q(x["exact_output_phi_width"]):x for x in tay["first_correction_derivative_budgets"]}
    if Q(0) not in tables or SIGMA not in tables:raise ValueError("missing actual Taylor widths")
    if not all(v["amplitude_Wiener_and_sup_spaces_separately_labelled"] for v in tables.values()):
        raise ValueError("the complete sup and Wiener tables were confused")
    real=decode(tables[Q(0)]["first_amplitude_budgets"])
    strip=decode(tables[SIGMA]["first_amplitude_budgets"])
    names=("a1","b1")
    W=[[up(real[k]["strip_sup"]["0,"+str(q)]) for k in names] for q in range(4)]
    Wr=[[up(real[k]["strip_sup"]["1,"+str(q)]) for k in names] for q in range(4)]
    Wrr=[[up(real[k]["strip_sup"]["2,"+str(q)]) for k in names] for q in range(3)]
    missing={}
    fourth=[]
    for k in names:
        candidates=[(math.factorial(4-q)*up(strip[k]["strip_sup"]["0,"+str(q)])
                    /ipow(ex(SIGMA),4-q)).upper() for q in range(4)]
        chosen=min(candidates).upper()
        missing[k]=dict(exact_paid_width=str(SIGMA),candidates=encode(candidates),
                        chosen=record(chosen),original_derivative_orders=list(range(4)))
        fourth.append(chosen)
    W.append(fourth)
    c=p["c"];D=[up(x) for x in c["D"]];Dr=[up(x) for x in c["Dr"]]
    if len(D)<4 or len(Dr)<3:raise ValueError("missing original complete drift derivatives")
    aa=scalar_product(D,D)
    aa[0]=(aa[0]+c["ep"]*c["ep"]*c["K"]).upper()
    bb=scalar_product(D,D[1:])
    bb=[(bb[q]+Dr[q]).upper() for q in range(3)]
    def cauchy(name):
        return [(math.factorial(q)*up(c[name])/ipow(ex(COEFF_WIDTH),q)).upper()
                for q in range(3)]
    tj,vj,theta=[cauchy(k) for k in ("T0","V0","vartheta")]
    parts=dict(
        radial_second=Wrr,
        radial_angular=[O.vscale(x,arb(2)) for x in O.svjets(D,Wr[1:],2)],
        drift_derivative=O.svjets(bb,W[1:],2),
        angular_second=O.svjets(aa,W[2:],2),
        first_transport=O.svjets(tj,O.vjadd(Wr[:3],O.svjets(D,W[1:],2)),2),
        scalar_potential=O.svjets(vj,W,2),
        exact_QK_cross=O.svjets(theta,O.mvjets(p["PQ"],W,2),2))
    jets=O.vjadd(*parts.values())
    if not O.ensure_nonnegative(jets):raise ValueError("nonfinite or negative complete local majorant")
    return dict(complete_real_raw_local_jets=encode(jets),complete_product_parts=encode(parts),
        paid_missing_W04=missing,coefficient_angular_jets=encode(dict(
            angular_second=aa,drift_derivative=bb,T0=tj,V0=vj,vartheta=theta)),
        coefficient_sup_width=str(COEFF_WIDTH),old_real_tables_recomputed=False,
        old_positive_strip_tables_recomputed=False,original_PQ_jets_recomputed=False,
        raw_numerator_is_mu_L0_w1=True,division_by_mu_not_inserted=True,
        exact_same_parameter_branch_identity_retained=True,all_product_terms_retained=True)

def complete_real_Airy(jets,p,old):
    answer={}
    for side in ("negative","positive"):
        pieces=[];total=arb(0)
        for pa,pb in p["real_"+side]:
            symbol=[sum((math.comb(q,l)*(pa[l]*jets[q-l][0]+pb[l]*jets[q-l][1])
                     for l in range(q+1)),arb(0)).upper() for q in range(3)]
            b2=(symbol[2]/ipow(p["m"],2)+symbol[1]*p["F2"]/ipow(p["m"],3)).upper()
            value=(p["composition"]*(p["near"]*(symbol[0]+arb.pi()*arb.pi()*b2/48)
                                     +p["far"]*b2)).upper()
            pieces.append(dict(symbol=encode(symbol),inverse_phase_second=record(b2),
                               complete_profile_bound=record(value)))
            total+=value
        total=total.upper()
        previous=copy.deepcopy(old["complete_Airy_source_bounds"][side]["local_numerator"])
        old_bound=up(box(previous["bound"]))
        selected=min(total,old_bound).upper()
        answer[side]=dict(bound=record(selected),new_real_two_derivative_complete=record(total),
            original_complete_local_Airy=previous,
            choice="real_two_derivative" if total<old_bound else "original_complete_analytic",
            new_real_profiles=pieces,all_output_frequencies_and_mean_retained=True,
            original_analytic_Airy_recomputed=False)
    return answer

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for k in ("repo-root","manifest","out"):parser.add_argument("--"+k,type=Path,required=True)
    parser.add_argument("--resume",type=Path)
    a=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new interval arithmetic requires this public repository Actions")
    if a.out.exists():raise FileExistsError("preserve every complete or failed actual native")
    ctx.prec=320;ctx.cap=4
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):
        raise ValueError("the exact reviewed runtime changed")
    start=time.monotonic()
    doc=dict(kind="actual_complete_real_angular_inner_first_Airy_local_source",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,
        complete=False,proved=False,failure=None,gates=[],stages={},rows=[],
        original_inner_native_sha256=INNER,original_inner_process_sha256=IPROC,
        original_Taylor_native_sha256=O.TAYLOR,original_Taylor_process_sha256=O.TPROC,
        original_auxiliary_native_sha256=O.AUX,original_inner_mathematical_source_sha256=ISOURCE,
        original_inner_manifest_sha256=IMANIFEST,
        new_stages=0,reused_stages=0,new_changed_local_integral_rows=0,reused_changed_local_integral_rows=0,
        old_target_FFT_Taylor_profile_matrix_nonlocal_or_mean_recomputations=0,
        original_physical_seams_retained=True,fixed_inner_interval_introduces_no_artificial_source=True,
        positive_raw_source_only=True,positive_weighted_port_conversion_claimed=False,
        complete_strong_return_or_cutoff97_inverse_claimed=False,actual_PDE_branch_claimed=False)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(a.out,doc)
    def check(name,truth):
        good=bool(truth);doc["gates"].append(dict(name=name,passed=good))
        if not good:raise ValueError("complete real-local gate failed: "+name)
    def stage(name,build):
        if name in doc["stages"]:
            v=doc["stages"][name]
            if not v["complete"] or O.payload_sha(v["payload"])!=v["payload_sha256"]:
                raise ValueError("an accepted complete new stage changed its exact payload")
            doc["reused_stages"]+=1;return v["payload"]
        payload=build()
        doc["stages"][name]=dict(complete=True,payload=payload,payload_sha256=O.payload_sha(payload))
        doc["new_stages"]+=1;checkpoint();return payload
    try:
        m=read(a.manifest)
        check("the complete exact manifest and every original64 pin belong to this public consumer",
            m["public_repository"]==PUBLIC
            and m["kind"]=="complete_inner_real_local_first_Airy_exact_public_inputs"
            and all((a.repo_root/f["path"]).is_file() and sha(a.repo_root/f["path"])==f["sha256"]
                    and (a.repo_root/f["path"]).stat().st_size==f["bytes"] for f in m["files"]))
        paths={k:a.repo_root/v for k,v in m["input_paths"].items()}
        fixed=[("inner_native",INNER,25724),("inner_process",IPROC,20208),
               ("original_inner_manifest",IMANIFEST,25258),
               ("Taylor_native",O.TAYLOR,52843),("Taylor_process",O.TPROC,48844),
               ("auxiliary_native",O.AUX,20319),("auxiliary_process",O.APROC,46443)]
        check("all original complete natives and receipts retain exact bytes",
            all(sha(paths[k])==h and paths[k].stat().st_size==n for k,h,n in fixed)
            and sha(O.__file__)==ISOURCE)
        previous_manifest=read(paths["original_inner_manifest"])
        pins={f["path"]:f for f in m["files"]}
        check("all64 original input pins remain unchanged without a schema exception",
            len(previous_manifest["files"])==64
            and all(f==pins.get(f["path"]) for f in previous_manifest["files"]))
        old,proc,tay,tp,aux,ap=[read(paths[k]) for k in (
            "inner_native","inner_process","Taylor_native","Taylor_process","auxiliary_native","auxiliary_process")]
        check("the actual complete inner result has all17 original gates and actual child0",
            old["complete"] and old["proved"] and old["failure"] is None
            and len(old["gates"])==17 and all(x["passed"] for x in old["gates"])
            and old["source_sha256"]==ISOURCE and old["input_manifest_sha256"]==IMANIFEST
            and proc["actual_returncode"]==0 and proc["complete"]
            and str(proc["run_id"])=="43657933806" and proc["native_sha256"]==INNER
            and proc["mathematical_gates"]==old["gates"])
        check("the complete original Taylor20 gates corrected mu and same complex branch are retained",
            tay["complete"] and tay["proved"] and tay["failure"] is None
            and len(tay["gates"])==20 and all(x["passed"] for x in tay["gates"])
            and tay["source_sha256"]==O.TSOURCE and tay["input_manifest_sha256"]==O.TMANIFEST
            and tay["principal_mu_uses_B_plus_and_leading_a0_uses_B_minus"]
            and tay["complete_branch_identity"]["same_complex_delta_without_conjugation"]
            and tp["actual_returncode"]==0 and tp["native_sha256"]==O.TAYLOR)
        small=aux["cases"][0]
        check("the original small complete coefficient and fold domain includes the same fixed inner interval",
            aux["complete"] and aux["proved"] and aux["failure"] is None
            and small["complete"] and small["proved"] and small["failure"] is None
            and len(small["gates"])==13 and all(x["passed"] for x in small["gates"])
            and Q(small["exact_fold_radius"])==Q(3,40000)
            and Q(small["exact_coefficient_width"])==COEFF_WIDTH
            and Q(old["exact_physical_rho_cover"])<Q(small["exact_fold_radius"])
            and old["original_auxiliary_native_sha256"]==O.AUX
            and ap["actual_returncode"]==0 and ap["native_sha256"]==O.AUX)
        check("both complete old successful stage payloads are identical and are not recomputed",
            set(old["stages"])==set(PAYLOADS)
            and all(old["stages"][k]["complete"] and old["stages"][k]["payload_sha256"]==h
                    and O.payload_sha(old["stages"][k]["payload"])==h for k,h in PAYLOADS.items()))
        profile=old["stages"]["new-inner-Airy-profile-and-exact-PQ-jets"]["payload"]
        p=decode(profile["numeric"])
        check("the profile coefficient table is exactly the paid full complex strip table",
            profile["original_smaller_auxiliary_payload_sha256"]==O.payload_sha(small)
            and set(profile["numeric"]["c"])==set(small["coefficient_evidence"]["complete_coefficient_majorants"])
            and profile["all_old_auxiliary_values_reused"] is True)
        rows=old["rows"]
        check("the four accepted original rows and complete matrix conversions cover the same physical interval",
            len(rows)==4 and len(old["matrix_conversions"])==4
            and old["complete_inner_integral_rows"]==4
            and rows[0]["interval"][0]==old["exact_physical_inner_interval"][0]
            and rows[-1]["interval"][1]==old["exact_physical_inner_interval"][1]
            and all(x["interval"][1]==y["interval"][0] for x,y in zip(rows,rows[1:]))
            and old["exact_root_interval"]==tay["exact_root_interval"]
            and Q(old["exact_real_delta_radius"])==Q(1,10**8)
            and old["fixed_intrinsic_parameter"]=="eta_0")
        for key in ("exact_real_delta_radius","fixed_intrinsic_parameter","input_cutoff","physical_frequency",
                    "actual_first_correction_density","source_window","exact_root_interval",
                    "exact_physical_inner_interval","exact_physical_rho_cover","exact_original_physical_piece_interval"):
            doc[key]=copy.deepcopy(old[key])
        doc["original_complete_stage_payloads"]=copy.deepcopy(PAYLOADS)
        doc["original_complete_matrix_conversions_payload_sha256"]=O.payload_sha(old["matrix_conversions"])
        doc["original_complete_rows_payload_sha256"]=O.payload_sha(rows)
        if a.resume:
            prev=read(a.resume)
            identity=("source_sha256","input_manifest_sha256","runtime","original_inner_native_sha256",
                      "original_inner_process_sha256","original_Taylor_native_sha256",
                      "original_auxiliary_native_sha256","exact_physical_inner_interval")
            check("every accepted new prefix retains identical source runtime and all original input identities",
                all(prev.get(k)==doc.get(k) for k in identity))
            doc["stages"]=copy.deepcopy(prev["stages"]);doc["rows"]=copy.deepcopy(prev["rows"])
            doc["original_prefix_audit"]=dict(native_sha256=sha(a.resume),
                complete=prev["complete"],proved=prev["proved"],failure=prev["failure"],
                completed_stages=len(prev["stages"]),completed_rows=len(prev["rows"]))
        jets=stage("complete-real-raw-local-angular-jets",lambda:complete_local_jets(tay,p))
        bounds=stage("complete-real-local-Airy-bounds",
            lambda:complete_real_Airy(decode(jets["complete_real_raw_local_jets"]),p,old))
        doc["complete_real_raw_local_jets"]=copy.deepcopy(jets["complete_real_raw_local_jets"])
        doc["complete_local_Airy_bounds"]=copy.deepcopy(bounds)
        prefix=len(doc["rows"])
        if prefix>len(rows):raise ValueError("accepted prefix exceeds the exact original four rows")
        for index,previous in enumerate(rows):
            if index<prefix:
                item=doc["rows"][index]
                if item["original_complete_row_payload_sha256"]!=O.payload_sha(previous):
                    raise ValueError("a completed changed-local row no longer has its original source")
                doc["reused_changed_local_integral_rows"]+=1;continue
            item=copy.deepcopy(previous)
            item["original_complete_row_payload_sha256"]=O.payload_sha(previous)
            for side in ("negative","positive"):
                oldside=previous[side]
                if oldside.get("exact_zero_radial_part"):continue
                out=item[side]
                jj=up(box(oldside["original_final_J_window"]))
                raw=(jj*up(box(bounds[side]["bound"]))).upper()
                local=min(raw,up(box(oldside["first_local_singular_envelope"]))).upper()
                nonlocal_bound=up(box(oldside["first_nonlocal_singular_envelope"]))
                mean=up(box(oldside["independent_even_mean_singular_envelope"]))
                weight=up(box(oldside["radial_weight_integral"]))
                square=((nonlocal_bound+local)*(nonlocal_bound+local)+mean*mean).upper()
                out["original_first_local_singular_envelope"]=copy.deepcopy(oldside["first_local_singular_envelope"])
                out["new_real_local_candidate"]=record(raw)
                out["first_local_singular_envelope"]=record(local)
                out["complete_squared_vector_envelope"]=record(square)
                out["squared_source_integral"]=record((weight*square).upper())
                out["separate_squared_source_integrals"]["first_local_singular_envelope"]=record((weight*local*local).upper())
                out["old_nonlocal_mean_and_weight_reused_exactly"]=True
            doc["rows"].append(item);doc["new_changed_local_integral_rows"]+=1;checkpoint()
        preserved=("complete_nine_nonlocal_terms","complete_five_even_mean_terms",
                   "first_nonlocal_singular_envelope","independent_even_mean_singular_envelope",
                   "original_final_J_window","original_even_mean_factor","radial_weight_integral")
        check("every complete nonlocal term independent mean weight and zero radial part is unchanged",
            len(doc["rows"])==4 and all(
                (new[side]==previous[side] if previous[side].get("exact_zero_radial_part")
                 else all(new[side][k]==previous[side][k] for k in preserved))
                for new,previous in zip(doc["rows"],rows) for side in ("negative","positive")))
        totals={}
        for side in ("negative","positive"):
            total=sum((up(box(x[side]["squared_source_integral"])) for x in doc["rows"]),arb(0)).upper()
            loc=sum((up(box(x[side]["separate_squared_source_integrals"]["first_local_singular_envelope"]))
                     for x in doc["rows"] if not x[side].get("exact_zero_radial_part")),arb(0)).upper()
            separate=copy.deepcopy(old["complete_inner_source_totals"][side]["separate_component_L2_bounds"])
            separate["first_local_singular_envelope"]=record(loc.sqrt().upper())
            totals[side]=dict(complete_first_correction_ordinary_L2_source=record(total.sqrt().upper()),
                complete_squared_source_integral=record(total),separate_component_L2_bounds=separate,
                original_complete_total=copy.deepcopy(old["complete_inner_source_totals"][side]))
        doc["complete_inner_source_totals"]=totals
        check("all new real local bounds are finite with complete original scope and zero old recomputations",
            O.ensure_nonnegative(decode(jets["complete_real_raw_local_jets"]))
            and all(box(v["bound"]).is_finite() and box(v["bound"]).lower()>=0 for v in bounds.values())
            and doc["old_target_FFT_Taylor_profile_matrix_nonlocal_or_mean_recomputations"]==0
            and not doc["complete_strong_return_or_cutoff97_inverse_claimed"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],
            failure=doc["failure"],new_stages=doc["new_stages"],
            new_changed_local_integral_rows=doc["new_changed_local_integral_rows"],
            native_sha256=sha(a.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()

#!/usr/bin/env python3
"""R114 constrained static fourth quotient, consuming the public original DAG.

No lower-field, W, local-density or old fourth forcing compiler is called.
The old producer remains byte-bound. Complete reports are gzip files; the
small main always keeps source/run/completion and exact file identities.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import tempfile
import time

import literature_local_fourth_quotient as old
import literature_full_m8_tail_response_projection as publication_helper

colored=old.colored
exact=old.exact
local=old.local
formal=old.formal
blocks=old.blocks
dual=old.dual
SCHEMA="visible-flex-R114-constrained-static-fourth-v1"
REPOSITORY="Rogerhu12/math-research-public"
PRODUCER_SHA="9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0"
PUBLICATION_HELPER_SHA="e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345"
SOURCE_RUN="43645177423"
SOURCE_COMMIT="2f1b809c0b0abb7a26303d36940edc203815f872"
REPORT_SHA="19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a"
PUBLICATION_SHA="c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba"
EXPORT_SHA="ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace"
TOTAL_BYTES=4800000
MAX_INPUT_BYTES=4800000
MAX_RAW_BYTES=40000000
MODES=(-4,-2)
DEFAULT_DIR=Path(__file__).resolve().parents[1]/"notes"/"actions-43645177423-1-local_fourth_quotient"
# h=1, d in (0,1,-1,2), k=0,1. omega=d+k is carried as an endpoint state.
BASIS_STATES=tuple((F(1),F(k),F(d+k)) for d in (0,1,-1,2) for k in (0,1))

def sha(data):
    return hashlib.sha256(data).hexdigest()

def json_bytes(value,pretty=False):
    return (json.dumps(value,sort_keys=True,indent=2 if pretty else None,
        separators=None if pretty else (",",":"),allow_nan=False)+"\n").encode()

def identity(path):
    p=Path(path)
    data=p.read_bytes()
    return {"filename":p.name,"bytes":len(data),"sha256":sha(data)}

def checked_bytes(path,maximum):
    p=Path(path)
    if p.stat().st_size>maximum:
        raise ValueError("bounded input exceeded")
    data=p.read_bytes()
    if len(data)>maximum:
        raise ValueError("bounded input changed while reading")
    return data

def current_sources():
    original=old.dependencies()
    if original["driver"]["sha256"]!=PRODUCER_SHA:
        raise ValueError("do not mutate the original local producer; explicitly rebind a new source")
    helper=identity(publication_helper.__file__)
    if helper["sha256"]!=PUBLICATION_HELPER_SHA:
        raise ValueError("publication identity helper changed; explicitly rebind it")
    return {"driver":identity(__file__),"original_producer_dependencies":original,
        "publication_identity_helper":helper}

def geometry_value(key,state):
    """Exact evaluation at the eight h=1 rational states, never a curve."""
    if len(key)!=8 or old.jet_weight(key):
        raise ValueError("this consumer accepts static geometry coefficients only")
    h,k,o=state
    if h!=1 or key[local.LH]<0 or key[local.K]<0 or key[local.O]<0:
        raise ValueError("rational h=1 basis requires polynomial k,omega,logh")
    if key[local.LH]:
        return F(0)  # log(1)=0, including every positive power
    return k**key[local.K]*o**key[local.O]

def evaluate_scalar(terms,state):
    return sum((value*geometry_value(key,state) for key,value in terms.items()),F(0))

def inverse(matrix):
    n=len(matrix)
    if any(len(row)!=n for row in matrix):
        raise ValueError("square exact matrix required")
    rows=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for col in range(n):
        pivot=next((i for i in range(col,n) if rows[i][col]),None)
        if pivot is None:
            raise ValueError("R114 rational reference matrix is singular")
        rows[col],rows[pivot]=rows[pivot],rows[col]
        scale=rows[col][col]
        rows[col]=[x/scale for x in rows[col]]
        for i in range(n):
            if i!=col and rows[i][col]:
                amount=rows[i][col]
                rows[i]=[x-amount*y for x,y in zip(rows[i],rows[col])]
    result=[row[n:] for row in rows]
    for i in range(n):
        for j in range(n):
            if sum((F(matrix[i][k])*result[k][j] for k in range(n)),F(0))!=F(i==j):
                raise AssertionError("exact inverse multiplication")
    return result

def reference_coordinates():
    matrix=old.pointwise_matrix()
    static=[{key:value for key,value in x.terms.items() if old.jet_weight(key)==0} for x in matrix]
    # columns are the eight actual reference states, rows the eight matrix coordinates
    reference=[[evaluate_scalar(static[row],state) for state in BASIS_STATES] for row in range(8)]
    inv=inverse(reference)
    coefficients=[]
    for i in range(8):
        terms={}
        for j in range(8):
            for key,value in static[j].items():
                terms[key]=terms.get(key,F(0))+inv[i][j]*value
        terms={key:value for key,value in terms.items() if value}
        coefficients.append(terms)
        for j,state in enumerate(BASIS_STATES):
            if evaluate_scalar(terms,state)!=F(i==j):
                raise AssertionError("reference coordinate Kronecker identity")
    info={"coordinate_order":list(exact.PARAMETERS),
        "basis_states_h_k_omega":[[str(x) for x in state] for state in BASIS_STATES],
        "matrix_columns_are_reference_states":[[str(x) for x in row] for row in reference],
        "inverse":[[str(x) for x in row] for row in inv],
        "exact_inverse_verified":True,"exact_reference_Kronecker_verified":True,
        "all_h_equal_one":True,"complete_real_paths_claimed_constant_h":False}
    return coefficients,info

def evaluate_profile_geometry(ring,terms,state):
    result=ring.number(0)
    for key,value in terms.items():
        scalar=geometry_value(key,state)
        if scalar:
            result=result+scalar*value
    return result

def normalize_static(ring,target,coordinates):
    """L(S)-sum_i a_i(S)L(S_i), with exact geometry coordinates and original profiles."""
    result={}
    details={}
    for mode in MODES:
        original=target[mode].terms
        values=[evaluate_profile_geometry(ring,original,state) for state in BASIS_STATES]
        out=dict(original)
        for coefficients,value in zip(coordinates,values):
            if not value.terms:
                continue
            for key,amount in coefficients.items():
                out[key]=out.get(key,ring.number(0))-amount*value
        normalized=local.GExpr(ring,out)
        for state in BASIS_STATES:
            if evaluate_profile_geometry(ring,normalized.terms,state).terms:
                raise AssertionError("normalized original density does not vanish at a reference state")
        result[mode]=normalized
        details[str(mode)]={"input_geometry_coefficients":len(original),
            "normalized_geometry_coefficients":len(normalized.terms),
            "reference_profile_sha256":[ring.digest(value) for value in values],
            "normalized_original_root_sha256":[
                {"geometry_key":list(key),"sha256":ring.digest(value)}
                for key,value in sorted(normalized.terms.items())],
            "all_eight_reference_evaluations_exactly_zero":True}
    return result,details

def load_bound_input(args,ring,report):
    raw_main=checked_bytes(args.source_report,100000)
    if sha(raw_main)!=args.source_report_sha256:
        raise ValueError("published source report bytes changed")
    manifest=json.loads(raw_main)
    if manifest.get("schema")!=old.SCHEMA:
        raise ValueError("wrong original local density manifest")
    original_dependencies=report["source_hashes"]["original_producer_dependencies"]
    if manifest.get("source_hashes")!=original_dependencies:
        raise ValueError("the complete original semantic source set changed")
    metadata=manifest.get("portable_original_expression_export")
    if not metadata or metadata.get("content_scope")!="W-and-local-static-density":
        raise ValueError("the complete local density export is required, not W-only")
    raw_publication=checked_bytes(args.publication_receipt,100000)
    if sha(raw_publication)!=args.publication_receipt_sha256:
        raise ValueError("publication receipt bytes changed")
    publication=json.loads(raw_publication)
    binding=publication_helper.verify_publication_binding(publication,
        source_run=args.source_run,source_commit=args.source_commit,
        report_name=args.source_report.name,report_bytes=len(raw_main),
        report_sha=sha(raw_main),export_record=metadata,
        driver_identity=manifest["source_hashes"]["driver"])
    observed_run=manifest.get("github_run_id")
    observed_commit=manifest.get("github_sha")
    if observed_run is None and observed_commit is None:
        observed_run,observed_commit=binding["source_run"],binding["source_commit"]
    if str(observed_run)!=args.source_run or observed_commit!=args.source_commit:
        raise ValueError("producer source/run mismatch")
    packed=checked_bytes(args.input_export,MAX_INPUT_BYTES)
    if (len(packed),sha(packed))!=(metadata["stored_bytes"],metadata["stored_sha256"]):
        raise ValueError("original local export packed bytes changed")
    if sha(packed)!=args.export_sha256:
        raise ValueError("explicit original local export SHA mismatch")
    with gzip.open(args.input_export,"rb") as stream:
        raw=stream.read(MAX_RAW_BYTES+1)
    if (len(raw)>MAX_RAW_BYTES or len(raw)!=metadata["raw_bytes"]
        or sha(raw)!=metadata["raw_sha256"]):
        raise ValueError("original local export raw bytes changed")
    # Use the already published decoder and all original-hash checks unchanged.
    receipt=dual.read_receipt(args.third_receipt)
    legacy={"source_hashes":original_dependencies}
    templates,target=old.load_export(args.input_export,args.export_sha256,ring,legacy,receipt)
    report["input"]={"producer_run":args.source_run,"producer_source":args.source_commit,
        "producer_completion":manifest.get("completion"),
        "producer_report":{"filename":args.source_report.name,"bytes":len(raw_main),"sha256":sha(raw_main)},
        "publication_receipt":{"filename":args.publication_receipt.name,
            "bytes":len(raw_publication),"sha256":sha(raw_publication),"binding":binding},
        "original_export":metadata,"bound_W":legacy["bound_W"],
        "raw_export_hash_verified":True,"all_original_roots_hash_verified":True,
        "old_forcing_compiled":False,"W_compiled":False,"local_density_compiled":False}
    return templates,target

def mode_weight_target(ring,target,weight,grade):
    return {mode:local.GExpr(ring,{key:grade.project(value,weight)
        for key,value in geo.terms.items()}) for mode,geo in target.items()}

def store_complete_block(path,data,maximum,already_published,main_reserve):
    raw=json_bytes(data,pretty=True)
    packed=gzip.compress(raw,mtime=0)
    if len(packed)>maximum or already_published+len(packed)+main_reserve>TOTAL_BYTES:
        raise formal.CompilationBudgetExceeded("complete compressed block output budget")
    path.parent.mkdir(parents=True,exist_ok=True)
    gzpath=path.with_suffix(path.suffix+".gz");gzpath.write_bytes(packed)
    added=len(packed)
    info={"filename":gzpath.name,"stored_bytes":len(packed),"stored_sha256":sha(packed),
        "raw_bytes":len(raw),"raw_sha256":sha(raw)}
    # Preserve a small directly readable block as well when bounded.
    if len(raw)<=main_reserve and already_published+added+len(raw)+main_reserve<=TOTAL_BYTES:
        path.write_bytes(raw);added+=len(raw)
        info["readable_json"]={"filename":path.name,"bytes":len(raw),"sha256":sha(raw)}
    return info,added

def publish_report(path,report,main_max,full_max,already_published=0):
    """Persist the complete report before writing a bounded main; never drop source identity."""
    raw=json_bytes(report,pretty=True)
    packed=gzip.compress(raw,mtime=0)
    fullpath=path.with_name(path.stem+"-complete-report.json.gz")
    path.parent.mkdir(parents=True,exist_ok=True)
    info={"filename":fullpath.name,"stored_bytes":len(packed),"stored_sha256":sha(packed),
        "raw_bytes":len(raw),"raw_sha256":sha(raw)}
    fits=len(packed)<=full_max and already_published+len(packed)+main_max<=TOTAL_BYTES
    if fits:
        fullpath.write_bytes(packed)
    main={key:report.get(key) for key in (
        "schema","completion","phase","scope","github_repository","github_run_id","github_sha",
        "source_hashes","limits","input","reference_matrix",
        "completed_blocks","checkpoint","coefficient_checkpoint","toy","elapsed_seconds","peak_rss_mib","error",
        "all_derivative_weights_computed","complete_U4_equals_R8_proved",
        "U4_quotient_nonzero_proved","P0_or_ruling_paid","finite_isometric_family_constructed")}
    main["complete_report_file"]={**info,"persisted":fits}
    main["complete_report_raw_exceeds_main_limit"]=len(raw)>main_max
    if not fits:
        main["computation_completion"]=report.get("completion")
        main["completion"]="output_limit"
        main["error"]="complete compressed report exceeded the explicitly reserved output budget"
    data=json_bytes(main,pretty=True)
    if len(data)>main_max:
        main["reference_matrix"]={"details_in_complete_report":True}
        main["input"]={"details_in_complete_report":True,
            "producer_run":(report.get("input") or {}).get("producer_run"),
            "producer_source":(report.get("input") or {}).get("producer_source")}
        data=json_bytes(main,pretty=True)
    if len(data)>main_max:
        main["source_hashes"]={"full_mapping_in_complete_report":True,
            "mapping_sha256":sha(json_bytes(report.get("source_hashes"))),
            "driver":report.get("source_hashes",{}).get("driver")}
        data=json_bytes(main,pretty=True)
    if len(data)>main_max:
        raise ValueError("small semantic main report exceeded bound")
    path.write_bytes(data)
    return {"completion":main["completion"],"bytes":len(data),"sha256":sha(data),
        "complete_report_file":main["complete_report_file"]}

def small_toy():
    coordinates,reference=reference_coordinates()
    limits=exact.Limits(seconds=30,nodes=10000,atoms=3000,terms=5000,rewrites=10000,memory_mib=256)
    ring=colored.ColoredRing(limits)
    q=ring.color("artificial_q");q4=q*q*q*q
    matrix=old.pointwise_matrix()
    target={mode:{} for mode in MODES}
    for i,coordinate in enumerate(matrix):
        template=exact.Expr(ring,{(i,()):F(1)})*q4
        for key,value in coordinate.terms.items():
            if old.jet_weight(key)==0:
                target[-4][key]=target[-4].get(key,ring.number(0))+value*template
                target[-2][key]=target[-2].get(key,ring.number(0))-2*value*template
    normalized,_=normalize_static(ring,{mode:local.GExpr(ring,terms) for mode,terms in target.items()},coordinates)
    if any(x.terms for x in normalized.values()):
        raise AssertionError("artificial exact matrix-linear density was not removed")
    key=[0]*8;key[local.H]=1;key[local.K]=3
    artificial={-4:local.GExpr(ring,{tuple(key):q4}),-2:local.GExpr(ring,{})}
    normalized,_=normalize_static(ring,artificial,coordinates)
    low=key[:];low[local.K]=1
    expected=local.GExpr(ring,{tuple(key):q4,tuple(low):-q4})
    if (normalized[-4]-expected).terms or normalized[-2].terms:
        raise AssertionError("artificial hk^3 normalization must be h(k^3-k)")
    toy={"schema":SCHEMA,"completion":"toy_passed","phase":"artificial_report_roundtrip",
        "scope":"artificial only","source_hashes":{},
        "github_repository":REPOSITORY,"github_run_id":"artificial","github_sha":"artificial",
        "completed_blocks":[],"large_artificial_diagnostic":"abcd"*50000}
    with tempfile.TemporaryDirectory(prefix="R114-report-toy-") as folder:
        path=Path(folder)/"toy.json"
        out=publish_report(path,toy,20000,300000)
        main=json.loads(path.read_bytes())
        full=gzip.decompress((path.parent/out["complete_report_file"]["filename"]).read_bytes())
        if (sha(full)!=out["complete_report_file"]["raw_sha256"]
            or json.loads(full)!=toy or main["github_sha"]!="artificial"
            or main["github_run_id"]!="artificial" or main["completion"]!="toy_passed"):
            raise AssertionError("complete compressed report/source identity round trip")
    return {"R114_exact_reference_matrix_inverse":True,
        "R114_exact_Kronecker_coordinates":True,
        "artificial_matrix_linear_density_zero":True,
        "artificial_hk_cubed_residual_hk_times_k_squared_minus_one":True,
        "complete_large_artificial_report_gzip_roundtrip":True,
        "main_source_run_and_actual_completion_retained":True,
        "true_profile_or_geometry_evaluated":False,
        "public_original_DAG_consumed":False,"research_compiler_called":False}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--source-report",type=Path,default=DEFAULT_DIR/"local-fourth-quotient.json")
    parser.add_argument("--source-report-sha256",default=REPORT_SHA)
    parser.add_argument("--source-run",default=SOURCE_RUN)
    parser.add_argument("--source-commit",default=SOURCE_COMMIT)
    parser.add_argument("--publication-receipt",type=Path,default=DEFAULT_DIR/"receipt.json")
    parser.add_argument("--publication-receipt-sha256",default=PUBLICATION_SHA)
    parser.add_argument("--input-export",type=Path,default=DEFAULT_DIR/"local-fourth-quotient-original-expressions.json.gz")
    parser.add_argument("--export-sha256",default=EXPORT_SHA)
    parser.add_argument("--third-receipt",type=Path,default=dual.DEFAULT_RECEIPT)
    parser.add_argument("--weights",default="1")
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--max-seconds",type=float,default=180)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-main-bytes",type=int,default=90000)
    parser.add_argument("--max-full-report-bytes",type=int,default=2500000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.max_main_bytes,args.max_full_report_bytes)<=0:
        parser.error("positive resource limits required")
    if args.max_main_bytes<10000 or args.max_main_bytes>=100000:
        parser.error("small main must reserve 10000..99999 bytes")
    if args.max_full_report_bytes+args.max_main_bytes>TOTAL_BYTES:
        parser.error("reserve main inside total published output budget")
    weights=[int(x) for x in args.weights.split(",")]
    if len(weights)>11 or len(set(weights))!=len(weights) or any(x<-8 or x>2 for x in weights):
        parser.error("distinct affine weights within [-8,2]")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY):
        parser.error("research consumes the public original DAG only in this repository Actions")
    started=time.monotonic();published=0;code=0
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "scope":"R114 normalized static density modulo all complete E8 x W36 fourth responses",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{},"completed_blocks":[],
        "all_derivative_weights_computed":False,"complete_U4_equals_R8_proved":False,
        "U4_quotient_nonzero_proved":False,"P0_or_ruling_paid":False,
        "finite_isometric_family_constructed":False,
        "limits":{"seconds":args.max_seconds,"memory_polling_mib":args.memory_mib,
            "nodes":400000,"atoms":100000,"terms":150000,"rewrite_calls":1000000,
            "rational_bits_during_elimination":8192,"main_bytes":args.max_main_bytes,
            "complete_compressed_report_bytes":args.max_full_report_bytes,"total_output_bytes":TOTAL_BYTES}}
    try:
        report["source_hashes"]=current_sources()
        if args.toy_only:
            report["phase"]="artificial_interface_and_reporting_checks"
            report["toy"]=small_toy();report["completion"]="toy_passed"
        else:
            limits=exact.Limits(args.max_seconds,400000,100000,150000,1000000,args.memory_mib,8192)
            ring=colored.ColoredRing(limits)
            report["phase"]="consume_bound_original_W_and_local_density"
            templates,target=load_bound_input(args,ring,report)
            coordinates,reference=reference_coordinates()
            report["reference_matrix"]=reference
            grade=blocks.ScalingGrading(ring)
            for weight in weights:
                report["phase"]="R114_normalized_static_weight_"+str(weight)
                projected=mode_weight_target(ring,target,weight,grade)
                normalized,details=normalize_static(ring,projected,coordinates)
                report["checkpoint"]={"weight":weight,"original_DAG_consumed":True,
                    "geometric_normalization_complete":True,
                    "normalized_geometry_coefficients":{
                        str(mode):len(value.terms) for mode,value in normalized.items()}}
                block=old.run_weight_block(ring,templates,normalized,weight,report)
                block["target_is_R114_normalized_density"]=True
                block["original_unconstrained_target_repeated"]=False
                block["normalization_checks"]=details
                block["new_scope"]="coefficient identities of L0(S)-sum a_i(S)L0(S_i), not independent raw geometric costs"
                block["true_static_balanced_nonzero_proved"]=False
                data={"schema":SCHEMA+"-block","github_sha":report["github_sha"],
                    "github_run_id":report["github_run_id"],"source_hashes":report["source_hashes"],
                    "input":report["input"],"reference_matrix":reference,**block}
                path=args.output.with_name(args.output.stem+f"-weight-{weight:+d}.json")
                file_info,added=store_complete_block(path,data,args.max_full_report_bytes,
                    published,args.max_main_bytes)
                published+=added
                report["completed_blocks"].append({"weight":weight,
                    "outcome":block["outcome"],"paid":len(block["paid_geometry_coefficients"]),
                    "unresolved":len(block["unresolved_geometry_coefficients"]),
                    "true_response_dimension_upper_bound":block["true_response_dimension_upper_bound"],
                    "complete_block_file":file_info})
                print(json.dumps({"phase":"complete_constrained_static_block","weight":weight,
                    "outcome":block["outcome"],"seconds":time.monotonic()-started}),flush=True)
                if block["unresolved_geometry_coefficients"]:
                    report["stopped_after_first_unresolved_block"]=True
                    break
            report["compiler_inventory"]={"coefficient_nodes":len(ring.algebra.c.nodes),
                "profile_atoms":len(ring.p.atoms),"history_states":len(ring.algebra.c.state_rhs),
                "actual_forcing_compiled":False}
            report["completion"]="complete"
    except formal.CompilationBudgetExceeded as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    written=publish_report(args.output,report,args.max_main_bytes,args.max_full_report_bytes,published)
    if written["completion"]=="output_limit":
        code=2
    print(json.dumps({"output":str(args.output),**written}),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())

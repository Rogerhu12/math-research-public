#!/usr/bin/env python3
"""Read the exact selected 96-row waist source; never rerun an old producer."""
from __future__ import annotations
import argparse,gzip,hashlib,io,json,math,os,platform,time,traceback
from fractions import Fraction
from pathlib import Path
import numpy as np
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
SOURCE=REL+"scripts/fourfold_codazzi_exact_selected_waist_data.py"
KIND="actual_exact_selected_waist_data_in_original96_rows_v1"
CONTRACT="6b8142abbb303930e952e0f1f8015f2798b6148515fc8fbd06fd8f0cda18fdb9"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
FIRST_PART="5dae124eef0b3004bfea08334c2f2546ade3edc5cb926c665591e42b842babc4"
RECONSTRUCTION="0e87af02cc2d499bb52de886a2b457307a02b298e16a7859fa91e2a8d2bf918f"
TRIAL="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
DIRECTION_SOURCE="9c08e253d2b4cdd951392a31aafc190b2341793a162c46aaadd914780894bf5c"
DIRECTION_PROOF="2b7d6080dc7fdac0bd5c557b71f3e7ec1eb5436a14d45a5a762e1b548a9e20f1"
REPAIR_SOURCE="51a3f7968991ed85211b74c23befae7021bb192796daf0ae2d12ec5a1d45329b"
DIRECTION_DEFINITION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
BACKGROUND_DEFINITION="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ALPHA="6890507429876859/9007199254740992"
RADII=("0","1/10000000000","1/100000000","1/100000")

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(v):return (json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
def save(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_name(p.name+".partial")
    tmp.write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+"\n");tmp.replace(p)
def read(p):return json.loads(Path(p).read_text())
def gate(doc,name,ok):
    ok=bool(ok);doc["gates"].append(dict(name=name,passed=ok))
    if not ok:raise ArithmeticError("complete waist identity gate failed: "+name)
def exact(x):
    x=Fraction(x)
    return arb(x.numerator)/arb(x.denominator)
def rec(x):
    x=arb(x)
    if not x.is_finite():raise ArithmeticError("a new complete waist scalar is not finite")
    return dict(ball=x.str(60,radius=True))
def dyadic(x):
    if type(x) not in (int,float) or not math.isfinite(x):
        raise ValueError("every complete initial coefficient must be a finite binary64 value")
    return Fraction.from_float(float(x))
def safe_relative(p):
    p=Path(p)
    if p.is_absolute() or ".." in p.parts or not str(p).startswith(REL):
        raise ValueError("a complete input left the authorized topic")
    return p

class Inputs:
    def __init__(self,root,manifest,doc):
        self.root=root;self.manifest=manifest;self.m=read(manifest);self.doc=doc
        gate(doc,"public runtime and exact320-bit arithmetic",
            os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
            and platform.python_version()=="3.12.14"
            and flint.__version__=="0.9.0" and np.__version__=="2.3.5"
            and ctx.prec==320)
        entries=self.m["files"];paths=[e["path"] for e in entries]
        ok=(self.m.get("public_repository")==PUBLIC and len(paths)==len(set(paths))
            and self.m.get("old_successful_scientific_calls_allowed") is False
            and self.m.get("expected_scientific_gates")==13)
        for entry in entries:
            p=root/safe_relative(entry["path"])
            ok=ok and p.is_file() and p.stat().st_size==entry["bytes"] and sha(p)==entry["sha256"]
        self.paths={k:root/safe_relative(v) for k,v in self.m["input_paths"].items()}
        fixed={"candidate_index":CANDIDATE,"candidate_first_part":FIRST_PART,
            "response_reconstruction":RECONSTRUCTION,"direction_source":DIRECTION_SOURCE,
            "direction_proof":DIRECTION_PROOF,"repair_source":REPAIR_SOURCE,"new_contract":CONTRACT}
        ok=ok and all(sha(self.paths[k])==h for k,h in fixed.items())
        ok=ok and self.paths["new_source"]==root/SOURCE and sha(root/SOURCE)==doc["source_sha256"]
        gate(doc,"complete pinned closure and unchanged primary identities",ok)
        self.base=read(self.paths["candidate_index"]);b=self.base;bm=b["metadata"]
        gate(doc,"complete same background index and physical frequency",
            b["kind"]=="complete_lossless_radial_cubic_shards_v1"
            and b["polynomial_order"]=="numpy/scipy PPoly descending local powers"
            and b["coefficient_shape"]==[4,6144,65] and b["radial_nodes_count"]==6145
            and len(b["initial_state"])==65 and bm["modes"]==32
            and bm["physical_frequency_factor"]==4 and bm["exact_float_amplitude"]==ALPHA
            and bm["normalized_state_order"]=="moving phi: U sine modes 1..M; V cosine modes 0..M, frequency 4m")
        e=b["parts"][0];part=self.paths["candidate_first_part"]
        with np.load(io.BytesIO(gzip.decompress(part.read_bytes())),allow_pickle=False) as z:
            nodes=z["radial_nodes"];coeff=z["piece_coefficients"]
            shape_ok=(set(z.files)=={"radial_nodes","piece_coefficients"}
                and nodes.dtype==np.dtype("float64") and coeff.dtype==np.dtype("float64")
                and nodes.shape==(1347,) and coeff.shape==(4,1346,65)
                and np.all(np.isfinite(nodes)) and np.all(np.isfinite(coeff))
                and np.all(np.diff(nodes)>0) and nodes[0].view(np.uint64)==np.float64(0).view(np.uint64)
                and e["first_interval"]==0 and e["last_interval_exclusive"]==1346
                and e["bytes"]==2738500 and e["sha256"]==FIRST_PART
                and part.name==e["file"] and nodes[-1]==float(e["radial_right"]))
            gate(doc,"complete original first shard shape bytes and zero radial start",shape_ok)
            initial=np.asarray(b["initial_state"],dtype=np.float64)
            gate(doc,"new exact bitwise base first trace in all65 entries",
                initial.shape==(65,) and np.all(np.isfinite(initial))
                and np.array_equal(initial.view(np.uint64),coeff[3,0,:].view(np.uint64)))
        reconstruction=read(self.paths["response_reconstruction"]);r=reconstruction["roles"]["response"]
        full=r["output_identity"]["full_trial"];self.trial=full["reconstructible_complete_document"]
        reconstructed=(json.dumps(self.trial,indent=2,allow_nan=False)+"\n").encode()
        gate(doc,"complete original response index reconstructed byte identity and old success",
            reconstruction["complete"] is True and reconstruction["base_candidate_sha256"]==CANDIDATE
            and full["sha256"]==TRIAL and hashlib.sha256(reconstructed).hexdigest()==TRIAL
            and r["actual_process_complete"] is True
            and len(r["recorded_child_return_codes"])>0 and all(c==0 for c in r["recorded_child_return_codes"]))
        t=self.trial;tm=t["metadata"]
        gate(doc,"same full193 physical direction including its original fourth row and mean",
            t["kind"]=="complete_lossless_radial_cubic_shards_v1" and t["coefficient_shape"]==[4,6144,193]
            and t["radial_nodes_count"]==6145 and tm["role"]=="response_full"
            and tm["background_candidate_sha256"]==CANDIDATE and tm["modes"]==96
            and tm["physical_frequency_factor"]==4 and tm["original_fourth_Robin_row_retained"] is True
            and tm["finite_head_mean_was_not_removed_from_the_solve"] is True
            and tm["coordinates"]=="physical unnormalized moving variation; h1 sine(4j phi), h2 cosine(4j phi) including its true mean")
        self.base_initial=[dyadic(x) for x in b["initial_state"]]
        self.response_initial=[dyadic(x) for x in t["initial_state"]]
        gate(doc,"all65 and193 saved initial values retained as exact binary64 rationals",
            len(self.base_initial)==65 and len(self.response_initial)==193)
        source=self.paths["direction_source"].read_text();proof=self.paths["direction_proof"].read_text()
        repair=self.paths["repair_source"].read_text()
        gate(doc,"reuse proved direction firsttrace and both zero-left repair definitions",
            "trial['initial_state'].view(np.uint64)" in source
            and "trial['piece_coefficients'][3,0,:].view(np.uint64)" in source
            and "if piece==0:zero_left=all(x==0 for x in offset)" in source
            and DIRECTION_DEFINITION in proof and BACKGROUND_DEFINITION in source
            and "offset=[Fraction(0) for _ in range(n)]" in repair and "yield 0,tuple(offset),None" in repair
            and "seven gates" in proof and "Its waist value is exactly unchanged" in proof)
        nf=self.paths["NF_contract"].read_text();sr=self.paths["SR_contract"].read_text()
        gate(doc,"same original96 waist coordinates and independent fifth-source contract",
            r"\tag{NF.21}" in nf and r"\tag{NF.24}" in nf
            and r"\tag{SR.20}" in sr and r"\tag{SR.21}" in sr)
        doc["complete_input_identity_conclusion"]=dict(
            candidate_index_sha256=CANDIDATE,candidate_first_part_sha256=FIRST_PART,
            candidate_first_shard_shape=[4,1346,65],new_base_bitwise_entries_checked=65,
            original_response_index_sha256=TRIAL,response_reconstruction_sha256=RECONSTRUCTION,
            original_direction_source_sha256=DIRECTION_SOURCE,original_direction_proof_sha256=DIRECTION_PROOF,
            original_background_repair_source_sha256=REPAIR_SOURCE,
            background_definition_sha256=BACKGROUND_DEFINITION,direction_definition_sha256=DIRECTION_DEFINITION,
            exact_alpha=ALPHA,original_full_state_sizes=[65,193],physical_frequency_factor=4,
            orthonormal_waist_conversion="raw sine amplitude divided by sqrt(2)",
            background_only_multiplied_by_alpha=True,response_not_multiplied_by_alpha=True,
            both_exact_continuous_repair_offsets_at_waist_are_zero=True,
            old_direction_firsttrace_and_zero_left_identity_reused_without_reexecution=True,
            original_even_mean_retained_in_input_identity=True,
            no_even_mean_constraint_or_high_waist_condition_removed=True,
            exact_initial_vectors_canonical_sha256=hashlib.sha256(canonical(dict(
                base=list(map(str,self.base_initial)),response=list(map(str,self.response_initial))))).hexdigest())

def exact_quadratic(inp,doc):
    alpha=Fraction(ALPHA);a=inp.base_initial[:32]+[Fraction(0)]*64;z=inp.response_initial[:96]
    A=alpha*alpha*sum((v*v for v in a),Fraction(0))/2
    B=alpha*sum((v*w for v,w in zip(a,z)),Fraction(0))
    D=sum((w*w for w in z),Fraction(0))/2
    gate(doc,"complete signed96-term rational quadratic and positive semidefinite consistency",
        len(a)==len(z)==96 and A>=0 and D>=0 and B*B<=4*A*D)
    doc["complete_exact_waist_quadratic_conclusion"]=dict(
        exact_A=str(A),exact_B=str(B),exact_D=str(D),
        norm_squared_formula="A+B*delta+D*delta^2",
        exact_components_formula="-(alpha*a_j+delta*z_j)/sqrt(2), j=1..96",
        complete_original_odd96_terms_retained=True,base_zero_extension_modes=[33,96],
        cross_coefficient_is_signed=True,exact_for_every_real_delta_as_an_algebraic_identity=True,
        A_ball=rec(exact(A)),B_ball=rec(exact(B)),D_ball=rec(exact(D)),
        identically_zero_for_all_delta=bool(A==0 and D==0),
        base_waist_exactly_zero=bool(A==0),direction_waist_exactly_zero=bool(D==0))
    doc["new_exact_rational_dot_products"]=3
    return A,B,D

def uniform_bounds(A,B,D,doc):
    rows=[]
    for radius in RADII:
        d=Fraction(radius);left=A-B*d+D*d*d;right=A+B*d+D*d*d
        maximum=A+d*abs(B)+d*d*D
        if not (left>=0 and right>=0 and maximum==max(left,right)):
            raise ArithmeticError("the exact uniform endpoint identity failed")
        upper=exact(maximum).upper()
        if not (upper.is_finite() and upper>=0):
            raise ArithmeticError("the exact nonnegative squared waist maximum has no finite upper bound")
        bound=upper.sqrt().upper()
        if not bound.is_finite():raise ArithmeticError("the complete uniform waist norm is not finite")
        rows.append(dict(exact_parameter_half_width=radius,
            exact_left_endpoint_squared_norm=str(left),exact_right_endpoint_squared_norm=str(right),
            exact_uniform_squared_norm=str(maximum),uniform_squared_norm=rec(exact(maximum)),
            uniform_original96_Euclidean_waist_norm_upper=rec(bound),
            normalized_circle_odd_L2=True,no_parameter_sampling=True,
            no_extension_of_PDE_phase_cap_or_metric_domain=True))
    doc["complete_uniform_waist_conclusion"]=rows;doc["new_uniform_parameter_intervals"]=len(rows)
    gate(doc,"all four exact endpoint maxima and complete directed square roots",
        len(rows)==4 and tuple(x["exact_parameter_half_width"] for x in rows)==RADII)

def render(doc):
    lines=["# Actual exact selected waist data in the original96 rows","",
        "Public run: "+doc["run_id"]+"/"+doc["run_attempt"]+".",
        "Complete scalar conclusion: "+str(doc["complete"])+".",
        "Scientific child return code: "+str(doc["actual_returncode"])+".","",
        "Scientific SHA256: "+doc["source_sha256"],
        "Manifest SHA256: "+doc["input_manifest_sha256"],""]
    q=doc.get("complete_exact_waist_quadratic_conclusion")
    if q:
        lines+=["## Exact signed rational polynomial","",
            "The complete original96 squared norm is A+B*delta+D*delta^2.","",
            "- A = "+q["exact_A"],"- B = "+q["exact_B"],"- D = "+q["exact_D"],"",
            "Only the base is multiplied by alpha; physical direction Z is not scaled.",
            "All96 sine amplitudes use the original 1/sqrt(2) normalization.",""]
    rows=doc.get("complete_uniform_waist_conclusion",[])
    if rows:
        lines+=["## Complete uniform bounds","",
            "| Exact half width | Original96 Euclidean waist norm upper |",
            "|---|---|"]
        lines += ["| "+r["exact_parameter_half_width"]+" | "+r["uniform_original96_Euclidean_waist_norm_upper"]["ball"]+" |" for r in rows]
        lines+=[""]
    lines+=["## Exact scope","",
        "The new base firsttrace check retains all65 entries; the complete original193 response identity and the proved zero-left repair are reused.",
        "No old response, repair sequence, Green product, source integral or numerical enclosure was recomputed.",
        "The even mean and high waist conditions remain independent. No fifth-column norm, ell0, actual PDE, cut inverse, full high inverse or final surface is claimed.",""]
    if doc.get("failure"):lines+=["Actual failure: "+json.dumps(doc["failure"],ensure_ascii=False),""]
    return "\n".join(lines)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root",type=Path,required=True);ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--workdir",type=Path,required=True);ap.add_argument("--process",type=Path,required=True)
    ap.add_argument("--conclusion",type=Path,required=True);ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320
    if args.process.exists() or args.out.exists():raise FileExistsError("preserve every actual waist evaluation")
    args.workdir.mkdir(parents=True,exist_ok=True)
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID",""),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT",""),
        workflow_event_commit=os.environ.get("GITHUB_SHA",""),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT",""),
        source_sha256=sha(__file__),input_manifest_sha256=sha(args.manifest),
        runtime=dict(Python=platform.python_version(),python_flint=flint.__version__,numpy=np.__version__),
        arithmetic_bits=320,mathematical_parameters=dict(exact_alpha=ALPHA,
            exact_parameter_half_widths=list(RADII),odd_rows=96,physical_frequency_factor=4),
        new_exact_rational_dot_products=0,new_uniform_parameter_intervals=0,
        old_numerical_enclosures_recomputed=0,old_response_or_repair_producers_called=0,
        old_Green_or_Poisson_products_recomputed=0,old_scientific_source_imports=0,
        original_input_bytes_modified=False,new_recomputable_arrays_persisted=False,
        fifth_column_or_ell0_evaluated=False,full_high_inverse_claimed=False,
        actual_PDE_solution_claimed=False,final_surface_claimed=False,
        scope="only exact selected family waist data; all mean high matching and domain obligations retained")
    try:
        inp=Inputs(args.repo_root,args.manifest,doc);save(args.process,doc)
        A,B,D=exact_quadratic(inp,doc);save(args.process,doc)
        uniform_bounds(A,B,D,doc)
        gate(doc,"only the new waist scalars were computed and no old successful producer was called",
            doc["new_exact_rational_dot_products"]==3 and doc["new_uniform_parameter_intervals"]==4
            and doc["old_numerical_enclosures_recomputed"]==doc["old_response_or_repair_producers_called"]==0
            and doc["old_Green_or_Poisson_products_recomputed"]==doc["old_scientific_source_imports"]==0)
        if len(doc["gates"])!=13:raise ArithmeticError("the complete waist gate count changed")
        doc.update(complete=True,proved=True,actual_returncode=0)
    except Exception as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
    # Persist the entire small scientific conclusion before rendering or wrapper publication.
    save(args.process,doc)
    raw=canonical(doc)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with gzip.GzipFile(filename=str(args.out),mode="wb",mtime=0) as f:f.write(raw)
    args.conclusion.parent.mkdir(parents=True,exist_ok=True);args.conclusion.write_text(render(doc))
    print(json.dumps(dict(complete=doc["complete"],actual_returncode=doc["actual_returncode"],
        scientific_conclusion_bytes=len(raw),scientific_conclusion_sha256=hashlib.sha256(raw).hexdigest(),
        complete_gates=len(doc["gates"]),old_numerical_enclosures_recomputed=0),sort_keys=True),flush=True)
    if not doc["complete"]:raise SystemExit(1)
if __name__=="__main__":main()

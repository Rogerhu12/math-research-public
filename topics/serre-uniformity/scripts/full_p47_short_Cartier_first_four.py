#!/usr/bin/env python3
"""Four previously unfinished values, using the unchanged R1118 algorithm.

This separate v2 request/entry deliberately leaves every successful v1 file
and guard unchanged.  The only mathematical engines are the pinned v1 RR,
support and Gaussian frame functions.  Existing twelve values are excluded.
"""
import argparse
import hashlib
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
REPO="Rogerhu12/math-research-public"
REQUEST=ROOT/(PRE+"notes/full-p47-short-Cartier-first-four-request.json")
ENTRY=PRE+"scripts/full_p47_short_Cartier_first_four.py"
METHOD=PRE+"notes/2026-11-27-full-p47-short-Cartier-first-four-method.md"
CORE=PRE+"scripts/full_p47_short_Cartier_third_kind.py"
SUPPORT=PRE+"scripts/full_p47_Cartier_support.py"
GRADED=PRE+"scripts/full_p47_graded_RR_source.py"
GAUSSIAN=PRE+"scripts/full_p47_Gaussian_CM_log.py"
RR_REQUEST=PRE+"notes/full-p47-graded-RR-source-request.json"
FIRST_FOUR=["0-ZA","0-ZB","141-ZA","141-ZB"]
DONE_TWELVE=["100-ZA","100-ZB","108-ZA","108-ZB","196-ZA","196-ZB",
              "220-ZA","220-ZB","76-ZA","76-ZB","77-ZA","77-ZB"]
IDS=[0,76,77,100,108,141,196,220]
P,Q=47,4513
START=time.monotonic()
DEADLINE=None
SOURCE=None
REQUEST_HASH=None
STAGE="preflight"
COMPLETED=[]
PREPARED=[]
FAILURES=[]
ENGINE=None

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()

def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,Cartier_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

def stop(signum,frame):
    raise TimeoutError("The declared first-four Cartier reserve was reached.")

def check():
    if DEADLINE is not None and time.monotonic()>=DEADLINE:
        raise TimeoutError("The declared first-four Cartier reserve was reached.")

def read_request(path):
    global REQUEST_HASH
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Only this original public Actions request may run mathematics.")
    raw=Path(path).read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("The separate first-four request pin changed.")
    req=json.loads(raw)
    if (req["execution_id"]!="full-p47-short-Cartier-first-four-v2" or
        req["prime"]!=P or req["coefficient_prime"]!=Q or
        req["sage_version"]!="10.6" or req["python_flint_version"]!="0.9.0" or
        req["jet_length"]!=836 or req["local_length"]!=Q or
        req["cases"]!=FIRST_FOUR or req["already_completed_case_ids"]!=DONE_TWELVE or
        req["maximum_workers"] not in (1,2,3,4)):
        raise RuntimeError("The v2 request is not the four new original cases.")
    overlap=req["concurrent_independent_algorithm"]
    if (overlap["algorithm"]!="bounded_Miller" or overlap["run"]!=45973334832 or
        overlap["job"]!=140418866621 or
        overlap["source"]!="4fc63ab4df03123599b1b1ad06560a071f464d58" or
        overlap["case_ids"]!=FIRST_FOUR or overlap["completed_case_ids_observed_at_request"] or
        overlap["relationship"]!="independent_algorithm_for_not_yet_completed_values" or
        overlap["later_Miller_completion"]!="consume_existing_run_only_no_rerun"):
        raise RuntimeError("The explicitly authorized independent concurrent source changed.")
    old=req["consumed_short_Cartier"]
    if (old["run"]!=45994669183 or old["job"]!=140490956495 or
        old["source"]!="1340d243733c1693ac57aa04043b7b9194fd14ed" or
        old["request_sha256"]!="20db24c6c8857df91109713833b47fcd2db5fd0930e45b4703f7017befb49f84" or
        old["result_sha256"]!="895d06ff05fab216225b5a6794295b3fb731d4ea5d1982935db365a4ebddcc09" or
        old["completed_case_ids"]!=DONE_TWELVE):
        raise RuntimeError("The twelve prior values are not the exact consumed receipt.")
    gate=req["certified_common_Cartier_input"]
    exact={
        "Cartier_column_matrix_sha256":"21fc43c13f58e974adb58804e3480f80d3268104546e31e40ca5370806bbb58f",
        "Cartier_row_matrix_sha256":"deda5ed6dbe8122f243c46bb60245cf8facc00b6040a8f34958c9ca4241d855d",
        "Hodge_evaluation_sha256":"8c5073af02da9d9731f7cbff7ab5fa1e061e590fe965355c9a2e79ff463795bb",
        "Hodge_evaluation_determinant":3058,
        "selected_frames_sha256":"ac2b0b2dc168977fe758cbf9b6f9a2eeb5b187d6da566f0940f824c9f375c67f",
        "selected95_values_sha256":"2c8159a9a6d8e5f6c6bf54d4e312cd5a9b062f9a8c61f7fa250300f96f5402a9",
        "grid_sha256":"627e076ae64de06332324f1bdf0a82e2888b493f4799af3b7211c6d7524d7c50",
        "dimension":73,"one_minus_C_determinant":551,"KS_constant":809}
    if gate!=exact or req["certified_Gaussian_grid_sha256"]!=exact["grid_sha256"]:
        raise RuntimeError("The exact already-certified common input changed.")
    for filename,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("A pinned original dependency changed: "+filename)
    required={ENTRY,METHOD,CORE,SUPPORT,GRADED,GAUSSIAN,RR_REQUEST,
        PRE+"scripts/full_p47_Miller_support.py",
        PRE+"scripts/full_p47_eight_CM_tangents.py",
        PRE+"scripts/full_p47_weight_one_Hodge_certificate.py",
        PRE+"scripts/original_p47_ell4513_cuspidal_transfer.py",
        PRE+"scripts/original_p47_cuspidal_disks.py",
        PRE+"notes/full-p47-CM-height-move-request.json",
        PRE+"notes/original-p47-ell4513-cuspidal-transfer-request.json",
        PRE+"notes/full-p47-short-Cartier-third-kind-request.json",
        PRE+"notes/2026-11-27-full-p47-short-Cartier-third-kind-method.md",
        PRE+"results/R1118-original-short-Cartier-reading-for-CM-third-kind-values.md",
        PRE+"results/R1121-certified-original-twelve-short-Cartier-values.md",
        "README.md",PRE+"README.md"}
    if not required.issubset(req["source_sha256"]):
        raise RuntimeError("A v2 execution dependency lacks its source pin.")
    total,reserve=int(req["total_seconds"]),int(req["reserve_seconds"])
    if not 900<=total<=3600 or not 30<=reserve<total or not 1<=int(req["field_worker_seconds"])<=1800:
        raise RuntimeError("The explicit v2 finite budget changed.")
    return req

def first_four_cases(self,data,req):
    """The original cleared divisor formulas, with the strict NEW v2 scope.

    No v1 guard or request is modified.  This new scope explicitly records
    the already running different algorithm and excludes all twelve results.
    """
    if req["cases"]!=FIRST_FOUR or req["already_completed_case_ids"]!=DONE_TWELVE:
        raise RuntimeError("The constructor was given another case scope.")
    def image(cm,c):
        rows=data["angle_images"]["%d:%d"%(cm,c)]
        out={str(pid):int(m) for pid,m in rows}
        if len(out)!=len(rows) or any(m<=0 for m in out.values()):
            raise ArithmeticError("An original angle cycle is invalid.")
        if sum(self.points[pid]["degree"]*m for pid,m in out.items())!=(24 if c==0 else 48):
            raise ArithmeticError("An original raw angle degree changed.")
        return out
    def combine(terms):
        result={}
        for c,divisor in terms:
            for pid,m in divisor.items():
                result[pid]=result.get(pid,0)+c*m
        return {pid:m for pid,m in result.items() if m}
    cusp={"cusp_%d"%b:1 for b in range(23)}
    result=[]
    for cm in (0,141):
        za=combine([(39,image(141,20)),(12,image(141,5)),(52,image(0,4)),
                    (48,cusp),(-156,image(cm,0)),(-48,image(cm,2))])
        zb=combine([(-21,image(141,20)),(8,image(0,12)),(-28,image(0,4)),
                    (48,cusp),(-24,image(cm,4)),(84,image(cm,0))])
        for angle,weights in (("ZA",za),("ZB",zb)):
            if sum(self.points[pid]["degree"]*m for pid,m in weights.items()):
                raise ArithmeticError("The original cleared divisor has nonzero degree.")
            if any(weights.get("cusp_%d"%b)!=48 for b in range(23)):
                raise ArithmeticError("An original cusp coefficient was lost.")
            result.append({"id":"%d-%s"%(cm,angle),"candidate_id":cm,
                "angle":angle,"weights":weights,"clearing_denominator":6})
    if [r["id"] for r in result]!=FIRST_FOUR:
        raise RuntimeError("The v2 constructor produced an unrequested divisor.")
    return result

def field_worker(req,output,seconds):
    if any(n=="sage" or n.startswith("sage.") for n in sys.modules):
        raise RuntimeError("The original field input requires a fresh process.")
    if not 1<=seconds<=int(req["field_worker_seconds"]):
        raise RuntimeError("The field worker exceeded its declared budget.")
    support=load("unchanged_R1118_support_v2",SUPPORT)
    # Call the existing mathematical worker, not the v1 command-line reader.
    support.worker(req,Path(output),seconds)

def one_frame(index):
    return ENGINE.frame_worker(index)

def main(req):
    global SOURCE,DEADLINE,STAGE,ENGINE
    DEADLINE=START+int(req["total_seconds"])-int(req["reserve_seconds"])
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    head=load("original_v2_checkout",PRE+"scripts/full_p47_weight_one_Hodge_certificate.py")
    SOURCE=head.source_head()
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,cases=FIRST_FOUR,
         consumed_short_Cartier=req["consumed_short_Cartier"],
         concurrent_independent_algorithm=req["concurrent_independent_algorithm"],
         scope="Only four unfinished values; necessary common input is regenerated and pinned.")
    scratch=Path(os.environ.get("RUNNER_TEMP","/tmp"))/(
        "original-p47-Cartier-four-"+os.environ.get("GITHUB_RUN_ID","unknown"))
    scratch.mkdir(parents=True,exist_ok=True)
    support_path=scratch/"actual-Cartier-support.json"
    STAGE="fresh_original_support_input"
    command=[sys.executable,str(ROOT/ENTRY),"--field-worker","--request",str(REQUEST),
             "--output",str(support_path),"--seconds",
             str(min(int(req["field_worker_seconds"]),max(1,int(DEADLINE-time.monotonic()))))]
    completed=subprocess.run(command,check=False,timeout=max(1,DEADLINE-time.monotonic()))
    if completed.returncode:
        raise RuntimeError("The fresh original support input failed.")
    data=json.loads(support_path.read_text())
    from sage.all import matrix,vector,PolynomialRing,identity_matrix,proof
    from sage.env import SAGE_VERSION
    if SAGE_VERSION!="10.6":
        raise RuntimeError("Wrong pinned Sage version.")
    proof.all(True)
    ENGINE=load("unchanged_R1118_engine_v2",CORE)
    ENGINE.DEADLINE=DEADLINE
    rr=load("original_graded_input_v2",GRADED)
    rr.DEADLINE=DEADLINE
    STAGE="consume_original_RR_and_probe_inputs"
    graded=rr.build_graded_source(json.loads((ROOT/RR_REQUEST).read_text()),
                                 expected_certificate=req["graded_certificate"])
    class FourRR(ENGINE.ResidueRR):
        build_cases=first_four_cases
    arithmetic=FourRR(graded,data,req)
    gate=req["certified_common_Cartier_input"]
    for key in ("Hodge_evaluation_sha256","Hodge_evaluation_determinant",
                "selected_frames_sha256","selected95_values_sha256","KS_constant"):
        if arithmetic.probe_receipt[key]!=gate[key]:
            raise ArithmeticError("The original shared probe input changed: "+key)
    emit("consumed_original_Cartier_probe_input",
         probe_receipt=arithmetic.probe_receipt,input_receipt=arithmetic.input_receipt)
    STAGE="new_four_meromorphic_RR_cases"
    for case in arithmetic.cases:
        try:
            PREPARED.append(arithmetic.prepare_case(case))
        except TimeoutError:
            raise
        except Exception as exc:
            row={"id":case["id"],"stage":STAGE,
                 "exception_type":type(exc).__name__,"message":str(exc)}
            FAILURES.append(row)
            emit("incomplete_meromorphic_case",**row)
            traceback.print_exc()
    if not PREPARED:
        raise ArithmeticError("None of the four new divisors reached its exact RR space.")
    STAGE="consume_original_shared_Gaussian_grid"
    gaussian=load("original_Gaussian_grid_v2",GAUSSIAN)
    gaussian.DEADLINE=DEADLINE
    pp,qq,ii=gaussian.original_base()
    if pp!=(653,525) or qq!=(3860,232) or ii!=95:
        raise ArithmeticError("The physical Gaussian basis changed.")
    ring=PolynomialRing(arithmetic.K,"B")
    S,grid=gaussian.torsion_eisenstein_grid(ring,pp,qq,ii)
    grid_receipt=gaussian.COMPLETED["original_grid"]
    if (grid_receipt["points"]!=2208 or grid_receipt["precision"]!=Q or
        grid_receipt["weil_root"]!=2 or grid_receipt["grid_sha256"]!=gate["grid_sha256"]):
        raise ArithmeticError("The exact consumed Gaussian grid changed.")
    KS=-3*343*S.inv(ring(4*343**3+27*S.z*S.z))
    if KS[0]!=arithmetic.k0:
        raise ArithmeticError("The actual KS scale changed.")
    ENGINE.SHARED={"series":S,"grid":grid,"KS":KS,
        "descriptors":arithmetic.descriptors,"probes":arithmetic.probes,
        "kernel":arithmetic.kernel,"pairs":arithmetic.pairs,"prepared":PREPARED}
    STAGE="new_four_values_on_consumed_73_charts"
    frame_results={}
    if int(req["maximum_workers"])==1:
        for index in range(73):
            frame_results[index]=one_frame(index)
    else:
        context=multiprocessing.get_context("fork")
        with context.Pool(processes=int(req["maximum_workers"])) as pool:
            for row in pool.imap_unordered(one_frame,range(73),chunksize=1):
                index=int(row["index"])
                if index in frame_results:
                    raise ArithmeticError("An actual frame was repeated.")
                frame_results[index]=row
                emit("first_four_Cartier_progress",complete_frames=len(frame_results))
    if sorted(frame_results)!=list(range(73)):
        raise ArithmeticError("The common chart input did not finish.")
    ordered=[frame_results[i] for i in range(73)]
    EC=matrix(arithmetic.K,[row["Hodge_Cartier_values"] for row in ordered])
    C=arithmetic.E_inverse*EC
    I=identity_matrix(arithmetic.K,73)
    if (ENGINE.row_hash(C)!=gate["Cartier_column_matrix_sha256"] or
        ENGINE.row_hash(C.transpose())!=gate["Cartier_row_matrix_sha256"] or
        int((I-C).det())!=gate["one_minus_C_determinant"]):
        raise ArithmeticError("The regenerated common Cartier input changed its prior certificate.")
    inverse=(I-C).inverse()
    cartier_receipt={"dimension":73,"convention":"columns; original Hecke row is transpose",
        "Cartier_column_matrix_sha256":ENGINE.row_hash(C),
        "Cartier_row_matrix_sha256":ENGINE.row_hash(C.transpose()),
        "Cartier_characteristic_polynomial":[int(x) for x in C.charpoly().list()],
        "one_minus_C_determinant":int((I-C).det()),
        "all73_frame_values_sha256":digest(ordered),
        "probe_receipt":arithmetic.probe_receipt,"consumed_Gaussian_grid":grid_receipt}
    emit("actual_Cartier_matrix_certificate",**cartier_receipt,
         certificate_role="necessary_reconstruction_of_previously_certified_common_input")
    STAGE="new_four_original_third_kind_values"
    for prepared in PREPARED:
        case=prepared["case"]
        values=[]
        for row in ordered:
            selected=[v for v in row["cases"] if v["id"]==case["id"]]
            if len(selected)!=1:
                raise ArithmeticError("A probe omitted one new original case.")
            values.append(selected[0]["Cartier_difference_value"])
        delta=arithmetic.E_inverse*vector(arithmetic.K,values)
        correction=inverse*delta
        if (C-I)*correction+delta:
            raise ArithmeticError("The actual Cartier-fixed correction sign changed.")
        alpha=(vector(arithmetic.K,prepared["target_rho"])+
               arithmetic.target_Hodge*correction)/arithmetic.K(6)
        target=arithmetic.center_ids.index(case["candidate_id"])
        result={"id":case["id"],"candidate_id":case["candidate_id"],"angle":case["angle"],
            "coarse_parameter":"j-j_CM","alpha":int(alpha[target]),
            "all_eight_log_derivatives":[int(x) for x in alpha],
            "clearing_denominator":6,"order_mod_q":551,"method":"R1118-short-Cartier",
            "exact_initial_divisor_sha256":digest(case["weights"]),
            "meromorphic_RR_certificate":prepared["certificate"],
            "Cartier_difference_coordinates_sha256":digest([int(x) for x in delta]),
            "holomorphic_correction_sha256":digest([int(x) for x in correction]),
            "Cartier_matrix_certificate_sha256":digest(cartier_receipt)}
        COMPLETED.append(result)
        emit("actual_third_kind_value",**result)
    signal.setitimer(signal.ITIMER_REAL,0)
    complete=not FAILURES and {r["id"] for r in COMPLETED}==set(FIRST_FOUR)
    STAGE="completed" if complete else "partially_completed"
    ordered_values=sorted(COMPLETED,key=lambda row:row["id"])
    emit("receipt",status="complete" if complete else "incomplete",source=SOURCE,
         run=os.environ.get("GITHUB_RUN_ID"),request_sha256=REQUEST_HASH,
         execution_id=req["execution_id"],completed=ordered_values,failed_cases=FAILURES,
         result_sha256=digest(ordered_values),Cartier_matrix_certificate=cartier_receipt,
         consumed_common_Cartier=req["consumed_short_Cartier"],
         scope="Four new values only; no repeat of the prior twelve or new certification of common inputs.")
    support_path.unlink(missing_ok=True)
    if not complete:
        sys.exit(1)

if __name__=="__main__":
    try:
        parser=argparse.ArgumentParser()
        parser.add_argument("--field-worker",action="store_true")
        parser.add_argument("--request",default=str(REQUEST))
        parser.add_argument("--output")
        parser.add_argument("--seconds",type=int)
        args=parser.parse_args()
        if Path(args.request).resolve()!=REQUEST.resolve():
            raise RuntimeError("Only the separate pinned v2 request path is accepted.")
        request=read_request(args.request)
        if args.field_worker:
            if not args.output or args.seconds is None:
                raise RuntimeError("The fresh field stage is incomplete.")
            field_worker(request,args.output,args.seconds)
        else:
            if args.output is not None or args.seconds is not None:
                raise RuntimeError("Worker-only parameters were passed to the main entry.")
            main(request)
    except BaseException as exc:
        if isinstance(exc,SystemExit) and exc.code==1 and STAGE=="partially_completed":
            raise
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
             request_sha256=REQUEST_HASH,stage=STAGE,completed=COMPLETED,
             failed_cases=FAILURES,prepared_cases=[v["case"]["id"] for v in PREPARED],
             exception_type=type(exc).__name__,message=str(exc))
        traceback.print_exc()
        sys.exit(1)

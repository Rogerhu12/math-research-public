#!/usr/bin/env python3
"""Cross-check completed original CM q^-1 logs in the same Hodge frame.

Read the fixed completed q^2 job, rebuild only the certified finite Hodge/
T2,T3,T5 input, and compare against the old Gaussian log and Jacobi ratios.
No CM chain, CM torsion grid, high moment, Jacobi path or height is rerun.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
THIS=PRE+"scripts/full_p47_CM_log_crosscheck.py"
METHOD=PRE+"notes/2026-11-27-full-p47-CM-log-crosscheck-method.md"
REQUEST=ROOT/(PRE+"notes/full-p47-CM-log-crosscheck-request.json")
HODGE=PRE+"scripts/full_p47_weight_one_Hodge_certificate.py"
HEIGHT=PRE+"notes/full-p47-CM-height-move-request.json"
QCINPUT=PRE+"notes/full-p47-QC-first-rows-request.json"
REPO="Rogerhu12/math-research-public"
Q=4513
IDS=(0,141,76,108)
START=time.monotonic()
SOURCE=None
REQUEST_HASH=None
STAGE="preflight"
COMPLETED={}
Q2_SOURCE={
    "source":"ccad9f4ad40466d9a3387e70b42a77c75a2d75b9",
    "run":45977769585,
    "job":140433713916,
    "request_sha256":"5bf66b6ddb303f71e2c255badc61942d0faf6694612a9ebdf74adde9b5dc49dc",
    "result_sha256":"5a084d55b4df85ab0a4eb38e8e5032292960ff83a81b6babfd3c54235d5ea734",
}
LOG_HASHES={
    141:"5e33d5638db673d62465a2c48415558e239adb07e50a411582c833be4bd2ccb3",
    0:"c5292bd60325292f2b006fc7e1330508f0d6e9e1d812aedcc629d28064bba44b",
    76:"ea56dbbe7450aa404c5301e6fb23115a2c0afa1f79dba1b5cda08f395bb63807",
    108:"dadb68c6004ffaafcf0f15ba67a7957cc291258c6c49654ddca07e02c6e2e1e7",
}
OLD_LOG_HASH="489ab09b0e7bedae211e478938e687b51cd3d477438d9d47605d2cac0a4929dd"
KERNEL_HASH="a1631dfbb9f6db6f796fe17e634869d57fe9486f276bcedc200a10c4ebfac86d"
N_HASH="cd5db67aa8fa60ef764bb773a9a694878698cba5663f6bfe2cfd2f2b3d863e41"
JACOBI_HASH="b9f610583ea037e18d5e948341af5b09b78c8426a16f7643a6f44bd2949b882e"
JACOBI_CERT_HASH="4a4895f692c0eaeab0fa76eed9987af0ebaefa524d03d23fcb00425c2df45ed8"


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,
                                    separators=(",",":")).encode()).hexdigest()


def rows(M):
    return [[int(a) for a in row] for row in M.rows()]


def emit(kind,**data):
    print(json.dumps(dict(kind=kind,elapsed_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)


def stop(signum,frame):
    raise TimeoutError("The declared completed-input cross-check budget was reached.")


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


def read_request():
    global REQUEST_HASH
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Arithmetic is restricted to the original public Actions.")
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("The exact cross-check request hash changed.")
    req=json.loads(raw)
    if (req["execution_id"]!="full-p47-CM-log-crosscheck-v1" or
            req["prime"]!=47 or req["coefficient_prime"]!=Q or
            req["sage_version"]!="10.6" or req["total_seconds"]!=600 or
            req["reserve_seconds"]!=30 or req["consumed_modq2_source"]!=Q2_SOURCE):
        raise RuntimeError("Unexpected fixed completed-input request.")
    needed={THIS,METHOD,HODGE,HEIGHT,QCINPUT}
    if not needed.issubset(req["source_sha256"]):
        raise RuntimeError("The completed-input source pins are incomplete.")
    for path,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Source pin mismatch: "+path)
    return req


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None


class PublicHTTPSRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        parts=urllib.parse.urlsplit(newurl)
        if parts.scheme!="https" or not parts.hostname or parts.username or parts.password:
            raise RuntimeError("The public log redirect was not HTTPS.")
        answer=super().redirect_request(req,fp,code,msg,headers,newurl)
        if answer is not None:
            answer.remove_header("Authorization")
        return answer


def download_fixed_job_log():
    """Token only reaches api.github.com; signed storage receives no token."""
    token=os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError("The workflow's read-only Actions token is absent.")
    url="https://api.github.com/repos/"+REPO+"/actions/jobs/140433713916/logs"
    request=urllib.request.Request(url,headers={
        "Authorization":"Bearer "+token,
        "Accept":"application/vnd.github+json",
        "X-GitHub-Api-Version":"2022-11-28",
        "User-Agent":"original-full47-completed-CM-log-crosscheck",
    })
    location=None
    opener=urllib.request.build_opener(NoRedirect())
    try:
        response=opener.open(request,timeout=30)
        response.close()
        raise RuntimeError("The fixed job-log API did not return its documented redirect.")
    except urllib.error.HTTPError as exc:
        try:
            if exc.code!=302:
                raise RuntimeError("The fixed job-log API returned HTTP "+str(exc.code)) from None
            location=exc.headers.get("Location")
        finally:
            exc.close()
    except urllib.error.URLError:
        raise RuntimeError("The fixed GitHub job-log API could not be read.") from None
    parts=urllib.parse.urlsplit(location or "")
    if parts.scheme!="https" or not parts.hostname or parts.username or parts.password:
        raise RuntimeError("The fixed job did not supply a valid HTTPS storage URL.")
    # A fresh opener and a fresh request: Authorization is not forwarded.
    public_request=urllib.request.Request(location,headers={
        "User-Agent":"original-full47-completed-CM-log-crosscheck"})
    public_opener=urllib.request.build_opener(PublicHTTPSRedirect())
    try:
        with public_opener.open(public_request,timeout=30) as response:
            raw=response.read(8*1024*1024+1)
    except urllib.error.HTTPError as exc:
        code=exc.code
        exc.close()
        raise RuntimeError("The unauthenticated job-log download returned HTTP "+str(code)) from None
    except urllib.error.URLError:
        raise RuntimeError("The unauthenticated job-log storage could not be read.") from None
    if len(raw)>8*1024*1024:
        raise RuntimeError("The fixed job log exceeded the declared input bound.")
    return raw.decode("utf-8-sig")


def consume_completed_logs():
    log=download_fixed_job_log()
    receipts=[]
    for line in log.splitlines():
        first=line.find("{")
        if first<0:
            continue
        try:
            obj=json.loads(line[first:])
        except json.JSONDecodeError:
            continue
        if isinstance(obj,dict) and obj.get("kind")=="receipt":
            receipts.append(obj)
    selected=[r for r in receipts if r.get("status")=="complete" and
              r.get("source")==Q2_SOURCE["source"] and
              str(r.get("run"))==str(Q2_SOURCE["run"]) and
              r.get("request_sha256")==Q2_SOURCE["request_sha256"]]
    if len(selected)!=1:
        raise RuntimeError("The fixed job lacks its unique complete original receipt.")
    receipt=selected[0]
    if (receipt.get("result_sha256")!=Q2_SOURCE["result_sha256"] or
            digest(receipt["completed"])!=Q2_SOURCE["result_sha256"]):
        raise ArithmeticError("The complete q^2 receipt canonical hash changed.")
    records=receipt["completed"]["CM_logs"]
    if len(records)!=4 or sorted(r.get("candidate_id") for r in records)!=sorted(IDS):
        raise ArithmeticError("The completed job did not contain exactly the four original CM classes.")
    result={}
    for record in records:
        cm=record["candidate_id"]
        values=record["lambda73"]
        terminal=record["terminal"]
        algebra=record["residue_algebra"]
        if (record["exact_divisor"]!="23*y-C_infty" or
                record["coefficient_prime"]!=Q or record["modulus"]!=20367169 or
                record["N_mod_q"]!=551 or record["N_sha256"]!=N_HASH or
                terminal["terminal_reduction_is_actual_D0"] is not True or
                terminal["formula"]!="lambda_D=Tr_A(delta*r)/(epsilon*N)" or
                terminal["signed_multiplier"]!=-1 or
                algebra["Hodge_kernel_sha256"]!=KERNEL_HASH or
                algebra["finite_etale"] is not True or
                algebra["all_geometric_conjugates_included"] is not True):
            raise ArithmeticError("The actual q^2 divisor, frame or signed terminal formula changed.")
        if (len(values)!=73 or any(type(a) is not int or not 0<=a<Q for a in values) or
                record["lambda73_sha256"]!=LOG_HASHES[cm] or digest(values)!=LOG_HASHES[cm]):
            raise ArithmeticError("A completed original CM log vector failed its full hash.")
        result[cm]=values
    certificate={"source":Q2_SOURCE,
                 "lambda73_sha256":{str(cm):LOG_HASHES[cm] for cm in IDS},
                 "Hodge_kernel_sha256":KERNEL_HASH,
                 "exact_divisor":"23*y-C_infty",
                 "terminal_signed_multiplier":-1,
                 "N_mod_q":551,"N_sha256":N_HASH,
                 "complete_records_sha256":digest(records)}
    COMPLETED["completed_modq2_input"]=certificate
    emit("completed_modq2_input",certificate=certificate)
    return result


def evaluate_matrix(polynomial,H,identity):
    answer=0*identity
    for coefficient in reversed(polynomial.list()):
        answer=answer*H+coefficient*identity
    return answer


def evaluate_column(polynomial,H,column):
    answer=0*column
    for coefficient in reversed(polynomial.list()):
        answer=H*answer+coefficient*column
    return answer


def compare_columns(actual,predicted):
    difference=actual-predicted
    bad=[i for i,a in enumerate(difference) if a]
    return {"match":not bad,
            "actual_sha256":digest(list(map(int,actual))),
            "predicted_sha256":digest(list(map(int,predicted))),
            "difference_sha256":digest(list(map(int,difference))),
            "mismatch_count":len(bad),
            "first_mismatches":[[i,int(actual[i]),int(predicted[i])] for i in bad[:8]]}


def main():
    global SOURCE,STAGE
    req=read_request()
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,START+570-time.monotonic()))
    hodge=module("original_CM_log_crosscheck_Hodge",HODGE)
    SOURCE=hodge.source_head()
    from sage.env import SAGE_VERSION
    from sage.all import PolynomialRing,identity_matrix,vector,proof
    if SAGE_VERSION!="10.6":
        raise RuntimeError("The actual Sage version changed.")
    proof.all(True)
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,consumed_modq2_source=Q2_SOURCE)
    STAGE="read_completed_original_CM_vectors"
    values=consume_completed_logs()
    old=json.loads((ROOT/HEIGHT).read_text())
    qc=json.loads((ROOT/QCINPUT).read_text())
    old_generator=qc["consumed_Gaussian_log"]
    if old_generator!={"run":45947023569,"job":140333947037,"lambda73_sha256":OLD_LOG_HASH}:
        raise RuntimeError("The old Gaussian generator certificate changed.")
    jacobi=qc["consumed_CM_Hecke_coordinates"]
    cert=qc["consumed_CM_Hecke_certificate"]
    cartier=qc["consumed_Cartier_matrix_certificate"]
    if (digest(jacobi)!=JACOBI_HASH or
            qc["consumed_CM_Hecke_coordinates_sha256"]!=JACOBI_HASH or
            digest(cert)!=JACOBI_CERT_HASH or
            qc["consumed_CM_Hecke_certificate_sha256"]!=JACOBI_CERT_HASH or
            digest(cartier)!=qc["consumed_Cartier_matrix_certificate_sha256"] or
            cert["actual_Hodge_row_checks"]!=[2,3,5] or
            cert["common_reference_rank"]!=73 or
            cert["all_needed_denominators_q_units"] is not True or
            cert["exact_rational_path_relations"] is not True):
        raise ArithmeticError("The already certified full Jacobi/Cartier input changed.")
    STAGE="rebuild_fixed_original_Hodge_and_three_Hecke_matrices"
    source=hodge.build_source(descriptors=old["Hodge_descriptors"],
                              expected_certificate=old["Hodge_certificate"])
    if source["certificate"]["kernel_coordinates_sha256"]!=KERNEL_HASH:
        raise ArithmeticError("The two methods do not use the same ordered Hodge basis.")
    bridge=hodge.hecke_bridge(source)
    for n in (2,3,5):
        if digest(rows(bridge["operators"][n]))!=old["original_Hecke_hashes"][str(n)]:
            raise ArithmeticError("The original Hecke row-action matrix changed.")
    if bridge["H2_sha256"]!=old["original_Hecke_hashes"]["H2"]:
        raise ArithmeticError("The old H2 row-action matrix changed.")
    K=source["K"]
    H=bridge["operators"][3]+bridge["operators"][5]
    identity=identity_matrix(K,73)
    PR=PolynomialRing(K,"X")
    P=PR(H.charpoly("X"))
    hhash=digest(rows(H))
    phash=digest([int(a) for a in P.list()])
    for previous in (cert,qc["consumed_basis_certificate"]):
        if (hhash!=previous["Hodd_matrix_sha256"] or
                phash!=previous["Hodd_characteristic_polynomial_sha256"]):
            raise ArithmeticError("The original Hodd embedding changed.")
    if P.degree()!=73 or P.gcd(P.derivative()).degree()!=0:
        raise ArithmeticError("The consumed full Hodd algebra is not the original etale algebra.")
    bp=PR(cert["Bq_coefficients"])
    if (len(cert["Bq_coefficients"])!=73 or
            digest(cert["Bq_coefficients"])!=cert["Bq_coefficients_sha256"] or
            bp.gcd(P).degree()!=0):
        raise ArithmeticError("The original Bq polynomial changed or ceased to be a unit.")
    B=evaluate_matrix(bp,H,identity)
    if int(B.det())!=551 or cert["Bq_determinant_mod_q"]!=551:
        raise ArithmeticError("The original Bq determinant changed.")
    Tq=identity-B
    if (cartier["convention"]!="columns; original Hecke row is transpose" or
            cartier["one_minus_C_determinant"]!=551 or
            digest(rows(Tq))!=cartier["Cartier_row_matrix_sha256"] or
            digest(rows(Tq.transpose()))!=cartier["Cartier_column_matrix_sha256"]):
        raise ArithmeticError("The full actual Cartier-row/Hecke bridge failed.")
    hcert={"Hodge_kernel_sha256":KERNEL_HASH,
           "Hodd_matrix_sha256":hhash,"Hodd_characteristic_polynomial_sha256":phash,
           "Bq_coefficients_sha256":cert["Bq_coefficients_sha256"],
           "Bq_matrix_sha256":digest(rows(B)),"Bq_determinant_mod_q":551,
           "Tq_row_matrix_sha256":digest(rows(Tq)),
           "Cartier_column_matrix_sha256":digest(rows(Tq.transpose())),
           "convention":"T_n omega_i=sum_j M_n[i,j] omega_j; log columns transform by M_n"}
    COMPLETED["original_frame_and_Hecke_bridge"]=hcert
    emit("original_frame_and_Hecke_bridge",certificate=hcert)
    STAGE="compare_original_Gaussian_anchor"
    logs={cm:vector(K,values[cm]) for cm in IDS}
    recovered=B*logs[141]
    recovered_hash=digest(list(map(int,recovered)))
    anchor={"new_divisor":"23*y_141-C_infty",
            "old_divisor":"Bq*(23*y_141-C_infty)",
            "old_q_inverse_log_sha256":OLD_LOG_HASH,
            "Bq_times_new_log_sha256":recovered_hash,
            "match":recovered_hash==OLD_LOG_HASH,
            "additional_sign_or_scale_applied":False}
    COMPLETED["Gaussian_anchor"]=anchor
    emit("Gaussian_anchor_crosscheck",**anchor)
    STAGE="compare_all_four_signed_Jacobi_ratios"
    D={141:-4,0:-3,76:-7,108:-8}
    W={141:2,0:3,76:1,108:1}
    reports=[]
    for record in jacobi:
        cm=record["candidate_id"]
        if (cm not in IDS or record["method"]!="R1119" or
                record["fundamental_discriminant"]!=D[cm] or
                record["reverse_incidence_multiplicity"]!=W[cm] or
                record["source_coarse_weight"]!=1 or
                record["exact_divisor"]!="23*y_%d-C_infty"%cm or
                record["weighted_Jacobi_pair"]!=[2209*D[cm],0 if D[cm]%2==0 else 2209] or
                record["Hodd_characteristic_polynomial_sha256"]!=phash or
                record["Bq_coefficients_sha256"]!=cert["Bq_coefficients_sha256"]):
            raise ArithmeticError("The actual CM class or signed Jacobi convention changed.")
        rho_list=record["ratio_to_u4_coefficients"]
        c_list=record["coordinate_relative_Bq_u4_coefficients"]
        if (len(rho_list)!=73 or len(c_list)!=73 or
                digest(rho_list)!=record["ratio_to_u4_sha256"] or
                digest(c_list)!=record["coordinate_relative_Bq_u4_sha256"]):
            raise ArithmeticError("A full Jacobi polynomial failed its old hash.")
        rho,c=PR(rho_list),PR(c_list)
        if (c*bp-rho)%P!=0 or (cm==141 and rho!=PR.one()):
            raise ArithmeticError("The original Bq*c_D=rho_D polynomial identity failed.")
        relative=compare_columns(logs[cm],evaluate_column(rho,H,logs[141]))
        qc_relative=compare_columns(logs[cm],evaluate_column(c,H,recovered))
        moved=compare_columns(B*logs[cm],evaluate_column(rho,H,recovered))
        report={"candidate_id":cm,"fundamental_discriminant":D[cm],
                "raw_log_sha256":LOG_HASHES[cm],
                "rho_D_sha256":record["ratio_to_u4_sha256"],
                "c_D_sha256":record["coordinate_relative_Bq_u4_sha256"],
                "lambda_D_equals_rho_D_lambda_141":relative,
                "lambda_D_equals_c_D_recovered_Bq_log":qc_relative,
                "Bq_lambda_D_equals_rho_D_recovered_Bq_log":moved}
        reports.append(report)
        emit("signed_CM_log_crosscheck",**report)
    if sorted(r["candidate_id"] for r in reports)!=sorted(IDS):
        raise ArithmeticError("The comparison lost a completed CM class.")
    COMPLETED["signed_CM_comparisons"]=reports
    STAGE="compare_the_original_sixteen_linear_readings"
    H2=bridge["H2"]
    linear=[]
    old_rows=old["original_CM_linear_rows"]
    if len(old_rows)!=16:
        raise ArithmeticError("The original sixteen linear readings were not retained.")
    for record in old_rows:
        eigenvalue=K(record["H2_eigenvalue"])
        eigen=(H2.transpose()-eigenvalue*identity).right_kernel().basis_matrix()
        if eigen.nrows()!=1:
            raise ArithmeticError("An original degree-one eigenspace changed.")
        e=eigen.row(0)
        pivot=next(i for i,a in enumerate(e) if a)
        e=e/e[pivot]
        if (digest(list(map(int,e)))!=record["eigenform_coordinates_sha256"] or
                record["normalization"]!="first nonzero actual73-Hodge coordinate is one"):
            raise ArithmeticError("An original normalized eigenform changed.")
        actual=int(e.dot_product(recovered))
        expected=record["q_inverse_log_Bq_u1728"]
        report={"H2_eigenvalue":int(eigenvalue),"actual":actual,"expected":expected,
                "match":actual==expected,
                "eigenform_coordinates_sha256":record["eigenform_coordinates_sha256"]}
        linear.append(report)
        emit("original_linear_reading_crosscheck",**report)
    COMPLETED["sixteen_linear_comparisons"]=linear
    passed=(anchor["match"] and all(r["match"] for r in linear) and
            all(r[name]["match"] for r in reports for name in (
                "lambda_D_equals_rho_D_lambda_141",
                "lambda_D_equals_c_D_recovered_Bq_log",
                "Bq_lambda_D_equals_rho_D_recovered_Bq_log")))
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="complete"
    emit("receipt",status="complete",comparison_status="match" if passed else "mismatch",
         comparisons_pass=passed,source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=COMPLETED,
         result_sha256=digest(COMPLETED),
         scope="Only the independently completed four q^-1 CM logs versus the already certified Gaussian anchor and signed Jacobi coordinates, in the fixed original73 Hodge basis. No new CM chain, high moment, Jacobi path, height or QC computation.")
    return 0 if passed else 2


if __name__=="__main__":
    try:
        if sys.argv[1:]:
            raise RuntimeError("Unexpected command-line arguments.")
        exit_code=main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
             request_sha256=REQUEST_HASH,stage=STAGE,completed=COMPLETED,
             exception_type=type(exc).__name__,message=str(exc),
             scope="Only fully printed comparisons survive; no unperformed agreement is claimed.")
        traceback.print_exc()
        exit_code=1
    sys.exit(exit_code)

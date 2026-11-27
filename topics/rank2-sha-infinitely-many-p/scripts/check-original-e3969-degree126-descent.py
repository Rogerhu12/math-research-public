#!/usr/bin/env python3
"""Live R1037 receipt -> entire degree126 source; no spectrum is repeated."""
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from fractions import Fraction
from math import gcd
from pathlib import Path

if os.environ.get("GITHUB_ACTIONS") != "true" or \
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Mathematical execution requires the named public GitHub Actions repository.")

from flint import fmpq, fmpq_mat, fmpq_poly

ORIGINAL = {
    "run":45973650826, "job":140419911466,
    "source":"22ac87ec033d658aa19b32d417c493f5748aa122",
    "request_id":"2026-11-27-original-degree378-complete-spectrum",
    "request_sha256":"be7284acf6e2e66b718e5ee2b2ae249292687693576460235eb23392c2be9c9b",
    "script":"topics/rank2-sha-infinitely-many-p/scripts/check-original-degree378-complete-spectrum.py",
    "script_sha256":"e5dc7114c455695349bc263061e3b8e6247a258c5c82469402b0934c64f0f2f2",
    "host_sha256":"1a6b2f908affe6989ae302622ac11ef4741487d66bc308791a63c17f03793898",
    "workflow_sha256":"70e970500ad9bff262b874e1fc664d08b192f70d8ce310314b6f36ac2feb4867",
    "source_manifest_sha256":"c29c75656945cc0db6b7965cf9777e29c3f4d147adfde6a03ca6be8e28f93c85",
    "full_report_sha256":"a4b054e6fc2ad28f26fc1be3552dd54ae0ceeb90adfa19dc39bc04411f4bb17e",
    "full_report_bytes":43787,
    "canonical_payload_sha256":"ecc330553cbabc891884eafe463db0a71f403e4a0b9b75394a86755a6a357b48",
    "canonical_payload_bytes":2892,
    "canonical_vector_sha256":"5d578c544bb1e01467c49837f1c579c172a014376e969fcc868ea458409c2b7b",
    "label":[5,4,"linear",2],
}
DEPS = {
    "check-r480-actual-input-cm19.py":"3d4d9a05872cdde0f24ff756ec79407417afa943eabf6f71f4e48d32f91f9c45",
    "check-r466-fixed-two-division-source.py":"effd6f1526421cfcb9da3bd7769eed258374fa0addf337313d0315cb3ef08245",
    "check-r464-degree102-cm7-exact.py":"b3e11a9da1b28a7623d86acf944262ab23c2d1969b1f0183030a4d1c96b5f1ff",
}

class ReceiptReadError(Exception):
    pass

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()

def digest(value):
    return hashlib.sha256(canonical_bytes(value)).hexdigest()

def api_get(path, redirect=False):
    headers = {"Accept":"application/vnd.github+json",
               "X-GitHub-Api-Version":"2022-11-28",
               "User-Agent":"rank2-original-e3969-degree126-reader",
               "Accept-Encoding":"identity"}
    token = os.environ.get("RANK2_ACTIONS_READ_TOKEN", "")
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(
        "https://api.github.com/repos/Rogerhu12/math-research-public"+path,
        headers=headers, method="GET")
    try:
        response = urllib.request.build_opener(NoRedirect()).open(req, timeout=30)
    except urllib.error.HTTPError as exc:
        status, location = exc.code, exc.headers.get("Location")
        exc.close()
        if status == 302 and redirect and location and location.startswith("https://"):
            return location
        raise ReceiptReadError("Original public API returned HTTP "+str(status))
    if redirect:
        response.close()
        raise ReceiptReadError("Original log endpoint did not issue its HTTPS redirect.")
    with response:
        data = response.read(2000001)
    if len(data)>2000000:
        raise ReceiptReadError("Original metadata exceeds bound.")
    return json.loads(data)

def live_original():
    run = api_get("/actions/runs/"+str(ORIGINAL["run"]))
    job = api_get("/actions/jobs/"+str(ORIGINAL["job"]))
    if run.get("id") != ORIGINAL["run"] or job.get("id") != ORIGINAL["job"] or \
            job.get("run_id") != ORIGINAL["run"]:
        raise ReceiptReadError("Original run/job mismatch.")
    for entry in (run,job):
        if entry.get("head_sha") != ORIGINAL["source"] or \
                entry.get("status") != "completed" or entry.get("conclusion") != "success":
            raise ReceiptReadError("Original source/completion mismatch.")
    url = api_get("/actions/jobs/"+str(ORIGINAL["job"])+"/logs", redirect=True)
    # The signed storage request is new and has NO Authorization header.
    req = urllib.request.Request(url,headers={
        "User-Agent":"rank2-original-e3969-degree126-reader",
        "Accept-Encoding":"identity"},method="GET")
    with urllib.request.urlopen(req,timeout=30) as response:
        raw = response.read(4000001)
    if len(raw)>4000000:
        raise ReceiptReadError("Original job log exceeds bound.")
    tags = ("RANK2_DEGREE378_HOST", "RANK2_DEGREE378_HOST_RESULT",
            "RANK2_DEGREE378_SUMMARY", "R1037_COMPLETE_SPECTRUM_REPORT",
            "R1037_COMPLETE_MASS_ZERO_CANONICAL")
    records = {tag:[] for tag in tags}
    pattern = re.compile(rb"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z ([A-Z0-9_]+) (.*)$")
    for line in raw.splitlines():
        match = pattern.fullmatch(line)
        if match is None:
            continue
        tag, payload = match.group(1).decode(), match.group(2)
        if tag in records:
            value = json.loads(payload)
            if canonical_bytes(value) != payload:
                raise ReceiptReadError("Original record is not its exact canonical JSON.")
            records[tag].append((value,payload))
    if any(len(records[tag]) != 1 for tag in tags):
        raise ReceiptReadError("A required original record is missing or ambiguous.")
    host = records[tags[0]][0][0]
    complete = records[tags[1]][0][0]
    summary = records[tags[2]][0][0]
    report, report_raw = records[tags[3]][0]
    canonical, canonical_raw = records[tags[4]][0]
    for entry in (host,complete):
        for key in ("request_id","request_sha256","workflow_sha256"):
            if entry.get(key) != ORIGINAL[key]:
                raise ReceiptReadError("Original host binding differs: "+key)
        if entry.get("run_id") != ORIGINAL["run"] or \
                entry.get("source_commit") != ORIGINAL["source"]:
            raise ReceiptReadError("Original host run/source differs.")
    if complete.get("status") != "COMPLETE_ORIGINAL_SPECTRUM" or \
            complete.get("exit_code") != 0 or complete.get("timed_out") is not False or \
            complete.get("full_report_hash_matches_summary") is not True:
        raise ReceiptReadError("Original host did not finish the whole exact spectrum.")
    for key in ("script","script_sha256","host_sha256"):
        if complete.get(key) != ORIGINAL[key]:
            raise ReceiptReadError("Original complete host source pin differs: "+key)
    manifest = host.get("source_manifest",{})
    for name,sha in dict(DEPS,**{
            "check-original-degree378-complete-spectrum.py":ORIGINAL["script_sha256"],
            "launch-original-degree378-complete-spectrum.py":ORIGINAL["host_sha256"]}).items():
        if manifest.get(name,{}).get("sha256") != sha:
            raise ReceiptReadError("An original complete input source pin differs.")
    for raw_value,sha,size,tag in (
            (report_raw,ORIGINAL["full_report_sha256"],ORIGINAL["full_report_bytes"],tags[3]),
            (canonical_raw,ORIGINAL["canonical_payload_sha256"],ORIGINAL["canonical_payload_bytes"],tags[4])):
        if len(raw_value) != size or hashlib.sha256(raw_value).hexdigest() != sha:
            raise ReceiptReadError("Original complete payload hash differs: "+tag)
        identities = complete.get("complete_record_identities",{}).get(tag,[])
        if len(identities) != 1 or identities[0].get("payload_bytes") != size or \
                identities[0].get("payload_sha256") != sha:
            raise ReceiptReadError("Original host does not bind complete payload: "+tag)
    if summary.get("complete_exact_report_in_stderr_sha256") != ORIGINAL["full_report_sha256"] or \
            report.get("status") != "PASS" or report.get("new_degree") != 378 or \
            report.get("source_manifest_sha256") != ORIGINAL["source_manifest_sha256"]:
        raise ReceiptReadError("Original summary/report does not give the complete PASS.")
    spectrum = report["spectrum"]
    for key in ("all_joint_projectors_sum_to_original_identity",
                "all_three_entire_eighteenth_powers_identity",
                "all_three_entire_operators_commute",
                "all_three_input_projections_sum_back_to_entire_inputs",
                "linear_H_part_equals_entire_delta_old22",
                "pulled_R302_Theta_anchor_all_three_operators_and_A_C_H_returned"):
        if spectrum.get(key) is not True:
            raise ReceiptReadError("An original whole-spectrum gate is absent: "+key)
    blocks = [b for b in spectrum["nonzero_joint_blocks"] if b["label_A_C_H"] == ORIGINAL["label"]]
    if len(blocks) != 1:
        raise ReceiptReadError("Original complete canonical block is not unique.")
    block = blocks[0]
    if block.get("K_rank") != 1 or block.get("whole_mass_row_nonzero") is not False or \
            block.get("delta_layers_new27_new9_new3_old1") != [0,1,0,0] or \
            block.get("dyadic_plus_minus_ranks") != [0,1] or \
            block.get("full_seven_old_image_rank") != 0 or \
            block["canonical"].get("whole_vector_sha256") != ORIGINAL["canonical_vector_sha256"]:
        raise ReceiptReadError("Original arithmetic candidate block has changed.")
    if canonical.get("label_A_C_H") != ORIGINAL["label"] or \
            canonical.get("whole_vector_sha256") != ORIGINAL["canonical_vector_sha256"] or \
            len(canonical.get("full_polynomial_X_ascending",[])) != 64:
        raise ReceiptReadError("Original full64 canonical coordinates are not supplied.")
    values = canonical["full_polynomial_X_ascending"]
    serialization = {"real":[[v] for v in values],"delta":[["0"] for _ in values]}
    if digest(serialization) != ORIGINAL["canonical_vector_sha256"]:
        raise ReceiptReadError("Original full64 vector does not match its complete matrix hash.")
    os.environ.pop("RANK2_ACTIONS_READ_TOKEN",None)
    return values,block

def coefficients(poly, length=None):
    return [str(poly[i]) for i in range(poly.degree()+1 if length is None else length)]

def valuation(poly, factor):
    if poly.is_zero():
        raise ArithmeticError("A requested source polynomial is zero.")
    order = 0
    while True:
        quotient,remainder = divmod(poly,factor)
        if not remainder.is_zero():
            return order,poly
        poly = quotient
        order += 1

def denominator(poly):
    out=1
    for coefficient in coefficients(poly):
        den=Fraction(coefficient).denominator
        out=out*den//gcd(out,den)
    return out

def factor_receipt(poly):
    content,factors = poly.factor()
    returned = fmpq_poly([content])
    entries=[]
    for factor,exponent in factors:
        returned *= factor**exponent
        entries.append({"coefficients_ascending":coefficients(factor),"exponent":exponent})
    if returned != poly:
        raise ArithmeticError("Full rational polynomial factorization did not multiply back.")
    return {"content":str(content),"factors":entries,"whole_product_returned":True}

def run(request=None):
    started=time.monotonic()
    if request is not None and request.get("schema") != "rank2-e3969-degree126-live-descent-v1":
        raise ValueError("Wrong exact reader request schema.")
    values,block=live_original()
    X=fmpq_poly([0,1])
    original=fmpq_poly([fmpq(v) for v in values])
    # Phi378 = delta^-6 Phi126(delta*z), delta^-6 = -1/27.
    columns=[fmpq(-1,27)*((-3)**(63-3*j))*X**(42-2*j)*(X+4)**(3*j)
             for j in range(22)]
    matrix=fmpq_mat([[columns[j][r] for j in range(22)] for r in range(64)])
    top=fmpq_mat([[columns[j][42+i] for j in range(22)] for i in range(22)])
    target=fmpq_mat([[original[42+i]] for i in range(22)])
    if matrix.rank()!=22 or top.rank()!=22:
        raise ArithmeticError("The complete original22 delta pull is not injective.")
    vector=top.solve(target)
    returned=matrix*vector
    if any(returned[r,0]!=original[r] for r in range(64)):
        raise ArithmeticError("The exact126 source did not return all original64 coordinates.")
    P=fmpq_poly([vector[j,0] for j in range(22)])
    if P.degree()!=20 or P[20]!=1:
        raise ArithmeticError("The actual minimal source is not normalized at order six.")
    angle=fmpq_poly([0])
    for j in range(22):
        angle += P[j]*(-X)**(21-j)
    if angle[1] != -1 or angle[0] != 0:
        raise ArithmeticError("The actual angle source does not preserve the original first six-jet.")
    h7=7+4*X+16*X**2
    X_h7=16-4*X+7*X**2
    endpoints={}
    for label,value in (("zero",fmpq(0)),("one",fmpq(1)),
                        ("minus_one_eighth",fmpq(-1,8)),("one_quarter",fmpq(1,4))):
        order,_=valuation(angle,X-value)
        endpoints[label]={"point":str(value),"order":order,"value":str(angle(value))}
    h_order,h_quot=valuation(angle,h7)
    h_rem=angle % h7
    pulled=fmpq_poly([0])
    for k in range(angle.degree()+1):
        pulled += angle[k]*(-27*X)**k*(1-4*X)**(63-3*k)
    pulled_endpoints={}
    for label,value in (("zero",fmpq(0)),("one",fmpq(1)),
                        ("minus_one_eighth",fmpq(-1,8)),("one_quarter",fmpq(1,4))):
        order,_=valuation(pulled,X-value)
        pulled_endpoints[label]={"point":str(value),"order":order,"value":str(pulled(value))}
    P_factor=factor_receipt(P)
    angle_factor=factor_receipt(angle)
    result={
        "status":"PASS_COMPLETE_E3969_DEGREE126_DESCENT",
        "original_binding":dict(ORIGINAL,consumed_live=True,spectrum_repeated=False),
        "actual_block":block,
        "full_original22_delta_columns_rank":22,
        "all_original64_coordinates_returned":True,
        "delta_pull_normalization":"Phi378(z)=-Phi126(delta*z)/27",
        "degree126_basis":"sigma^126*(1,X,...,X^21); X=x^3",
        "degree126_polynomial_X_ascending":coefficients(P,22),
        "degree126_polynomial_sha256":digest(coefficients(P,22)),
        "degree126_minimal_denominator":str(denominator(P)),
        "degree126_origin_order":126-6*P.degree(),
        "degree126_P_at_zero":str(P(0)),
        "degree126_P_at_minus_one":str(P(-1)),
        "degree126_P_at_eight":str(P(8)),
        "degree126_P_at_minus_four":str(P(-4)),
        "degree126_P_factorization":P_factor,
        "degree126_gcd_with_X_and_E2_and_norm7":
            coefficients(P.gcd(X*(X+1)*X_h7)),
        "angle_definition":"Phi126=Theta^63*f(t), t=-1/X",
        "angle_polynomial_t_ascending":coefficients(angle),
        "angle_degree":angle.degree(),
        "angle_factorization":angle_factor,
        "angle_endpoints":endpoints,
        "angle_h7_order":h_order,
        "angle_h7_full_remainder":coefficients(h_rem,2),
        "angle_h7_full_resultant":str(angle.resultant(h7)),
        "angle_infinity_pole_order":angle.degree(),
        "actual_cubic_angle_pull":{
            "definition":"(1-4u)^63*f(-27u/(1-4u)^3)",
            "full_polynomial_u_ascending":coefficients(pulled),
            "full_polynomial_sha256":digest(coefficients(pulled)),
            "degree":pulled.degree(),
            "all_five_boundary_orders":dict(pulled_endpoints,
                infinity={"pole_order":pulled.degree()}),
        },
        "no_arithmetic_rank_inferred_from_new_factorization":True,
        "no_central_zero_propagated_to_source_products":True,
        "generated_output_files_written":False,
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds":time.monotonic()-started,
    }
    if len(canonical_bytes(result))>60000:
        raise RuntimeError("Complete necessary new coordinates exceed small-runner output bound.")
    return result

if __name__=="__main__":
    try:
        print(canonical_bytes(run()).decode())
    except Exception as exc:
        print(json.dumps({"status":"EXECUTION_ERROR","error_type":type(exc).__name__,
                          "message":str(exc)},sort_keys=True,separators=(",",":")),file=sys.stderr)
        raise

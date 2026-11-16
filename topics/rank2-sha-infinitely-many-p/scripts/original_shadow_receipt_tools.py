#!/usr/bin/env python3
"""Pure, network-free validation of the original shadow's two pinned receipts."""
import hashlib
import json
import re

SCHEMA="rank2-original-public-pass-pipeline/v1"

def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=True)

def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()

def add_pinned_arguments(parser):
    parser.add_argument("--prime",type=int,choices=(29,41),default=29)
    for stem in ("first","packet"):
        parser.add_argument("--"+stem+"-job",type=int,required=True)
        parser.add_argument("--"+stem+"-run",type=int,required=True)
        parser.add_argument("--"+stem+"-run-head",required=True)
        parser.add_argument("--"+stem+"-source",required=True)
        parser.add_argument("--"+stem+"-result-sha256",required=True)

def pinned_request(args):
    result={"prime":int(args.prime)}
    for stem in ("first","packet"):
        for suffix in ("job","run","run_head","source","result_sha256"):
            name=stem+"_"+suffix
            result[name]=getattr(args,name)
        if not re.fullmatch(r"[0-9a-f]{40}",result[stem+"_run_head"]):
            raise ValueError("Pin the complete original workflow head SHA.")
        if not re.fullmatch(r"[0-9a-f]{40}",result[stem+"_source"]):
            raise ValueError("Pin the complete original mathematical source SHA.")
        if not re.fullmatch(r"[0-9a-f]{64}",result[stem+"_result_sha256"]):
            raise ValueError("Pin the published complete mathematical result SHA256.")
    return result

def validate_original_receipt(kind,result,request):
    if kind=="F":
        stem,flag,status,weights=("first","certified_original_first_factor",
                                "certified_original_first_factor",(2,4))
        expected_kind="rank2_original_first_factor_level867_coordinates"
    else:
        assert kind=="P"
        stem,flag,status,weights=("packet","certified_original_map",
                                "certified_original_rational_hecke_hom",(4,6))
        expected_kind="rank2_original_rational_hecke_map"
    assert result["kind"]==expected_kind and result.get(flag) is True
    assert result["source"]==request[stem+"_source"]
    assert int(result["run_id"])==request[stem+"_run"]
    assert digest(result)==request[stem+"_result_sha256"]
    cases=[x for x in result["cases"] if x.get("status")==status]
    assert len(cases)==1
    case=cases[0]
    weight=int(case["weight"])
    assert weight in weights
    certificate=case["last_exact_certificate"]
    assert certificate.get("full_0_through_bound_identity") is True
    if kind=="F":
        assert result["original_curve"]==[0,0,0,0,17]
        assert result["source_level"]==10404 and result["base_level"]==867
        assert int(certificate["sturm_bound"])==612*(weight+6)
        assert certificate["V_constant"]=="-1" and certificate["V_Q_coefficient"]=="5"
        assert case["no_assumed_manin_constant"] is True
    else:
        assert result["selected_original_u"]==["915/55569","1097/55569","2962/55569"]
        assert int(certificate["bound"])==612*(weight+1)
        assert case["full_original_artin_source_preserved"] is True
        assert int(case["certified_original_integer_return"])==17
    return weight

def validate_envelope(envelope,request,host_script_sha256):
    supplied_hash=envelope.get("envelope_sha256")
    body={k:v for k,v in envelope.items() if k!="envelope_sha256"}
    assert supplied_hash==digest(body)
    assert body["schema"]==SCHEMA and body["request"]==request
    assert body["host_script_sha256"]==host_script_sha256
    assert body["repository"]=="Rogerhu12/math-research-public"
    for kind,stem in (("F","first"),("P","packet")):
        auth=body["authentication"][kind]
        assert auth["job_id"]==request[stem+"_job"]
        assert auth["run_id"]==request[stem+"_run"]
        assert auth["job_status"]==auth["run_status"]=="completed"
        assert auth["job_conclusion"]==auth["run_conclusion"]=="success"
        assert auth["run_head_sha"]==request[stem+"_run_head"]
        assert auth["job_head_sha"]==request[stem+"_run_head"]
        assert auth["result_sha256"]==request[stem+"_result_sha256"]
        assert auth["mathematical_source"]==request[stem+"_source"]
        assert re.fullmatch(r"[0-9a-f]{64}",auth["complete_job_log_sha256"])
        validate_original_receipt(kind,body["certificates"][kind],request)
    return body["certificates"]["F"],body["certificates"]["P"]

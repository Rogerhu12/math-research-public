#!/usr/bin/env python3
"""R885 success: standard-library Range retrieval of completed certificates, never mathematics."""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import tarfile

S=Path(__file__).resolve().parent
TOPIC=S.parent
REPO=TOPIC.parent.parent
RESULT="R885-original-polynomial-one-row-adjugate"
FINAL="p41-original-polynomial-one-row-adjugate-certificate.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
RANGE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p)
    with (gzip.open if p.suffix==".gz" else open)(p,"rt",encoding="utf-8") as f:
        return json.load(f)
def write(p,x):
    Path(p).write_text(json.dumps(x,sort_keys=True,separators=(",",":"))+"\n")
def plain(x):
    return {k:x[k] for k in ("file","bytes","sha256")}
def spec(p):
    p=Path(p)
    return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p)}
def fingerprint(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def main():
    sys.set_int_max_str_digits(0)
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    parser=argparse.ArgumentParser()
    parser.add_argument("--request",required=True)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    request=read(args.request)
    assert sha(__file__)==request["script_sha256"]
    assert sha(REPO/"README.md")==request["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==request["readme_sha256"]["topic"]
    assert sha(S/RANGE)==RANGE_SHA
    definition=importlib.util.spec_from_file_location("R885_IO_Range",S/RANGE)
    module=importlib.util.module_from_spec(definition);definition.loader.exec_module(module)
    out=Path(args.output);folder=out/"original";folder.mkdir(parents=True,exist_ok=True)
    source=request["source"]
    archive=module.Archive(source,out/"range",whole=False)
    try:
        members=archive.by_name[REFERENCE]
        assert len(members)==1 and members[0].file_size<4096
        raw=archive.zip.read(members[0]);(folder/REFERENCE).write_bytes(raw)
        reference=read(folder/REFERENCE)
        assert reference["result"]==RESULT and reference["file"]==MANIFEST
        archive.extract_bound(MANIFEST,reference["sha256"],folder/MANIFEST,reference["bytes"])
        manifest=read(folder/MANIFEST)
        assert manifest["result"]==RESULT and manifest["source_commit"]==source["source_commit"]
        assert str(manifest["workflow_run_id"])==str(source["run_id"])
        entries={x["file"]:plain(x) for x in manifest["files"]}
        assert len(entries)==len(manifest["files"])
        for name,row in entries.items():
            assert Path(name).name==name
            assert len(archive.by_name[name])==1 and archive.by_name[name][0].file_size==row["bytes"]
        selected={"public-actions-input.json","run-receipt.json","core-receipt.json",FINAL}
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in sorted(selected)])
        public,run,core=[read(folder/n) for n in ("public-actions-input.json","run-receipt.json","core-receipt.json")]
        assert public["result"]==run["result"]==core["result"]==RESULT
        assert public["source_commit"]==run["source_commit"]==source["source_commit"]
        assert str(run["workflow_run_id"])==str(source["run_id"])
        assert public["core_sha256"]==core["source_sha256"]==source["core_sha256"]
        assert public["wrapper_sha256"]==source["wrapper_sha256"]
        assert run["complete"] is True and core["complete"] is True and run["process_exit_code"]==0
        assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
        assert core["certificate_sha256"]==request["certificate_sha256"]==entries[FINAL]["sha256"]
        cert=read(folder/FINAL);tag=cert["configuration"]
        assert cert["complete"] is True and cert["result"]==RESULT
        assert tag==core["configuration"] and fingerprint(tag)==public["mathematical_configuration_sha256"]
        for key in ("source_audit","characteristic_relation","one_row_adjugate","stage_manifest"):
            row=plain(cert[key]);assert entries[row["file"]]==row
            selected.add(row["file"])
        selected.update(("R885-original-source-inventory.json","R885-retained-inputs-receipt.json",
                         "R885-adjugate-row-level-000.json.gz","R885-adjugate-row-level-272.json.gz"))
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in sorted(selected)])
        stages=read(folder/cert["stage_manifest"]["file"])
        assert stages["complete"] is True and stages["configuration"]==tag
        assert len(stages["files"])==549
        for row in stages["files"]:
            assert plain(row)==entries[row["file"]]
        audit=read(folder/cert["source_audit"]["file"])
        characteristic=read(folder/cert["characteristic_relation"]["file"])
        adj=read(folder/cert["one_row_adjugate"]["file"])
        for value in (audit,characteristic,adj):
            assert value["complete"] is True and value["configuration"]==tag
        assert len(characteristic["source_node_stages"])==273
        assert characteristic["exact_original_modular_characteristic_polynomial_certified"] is True
        assert characteristic["all273_nodes_for_all273_T_coefficients_verified"] is True
        assert adj["r_is_exactly_original_e0_transpose_adjugate"] is True
        assert adj["all272_polynomial_components_of_terminal_row_zero"] is True
        assert len(adj["adjugate_row_T_terms"])==272
        row_sources=[plain(x["source"]) for x in adj["adjugate_row_T_terms"]]
        for row in row_sources:
            assert row==entries[row["file"]]
        assert plain(adj["terminal_Cayley_Hamilton_row"])==entries["R885-adjugate-row-level-272.json.gz"]
        terminal=read(folder/"R885-adjugate-row-level-272.json.gz")
        assert terminal["terminal_complete_polynomial_row_zero"] is True and terminal["row_level"]==272
        assert all(x==0 for row in terminal["coefficient_rows_ascending_z"] for x in row)
        inventory=read(folder/"R885-original-source-inventory.json")
        receipt=read(folder/"R885-retained-inputs-receipt.json")
        assert receipt["source_inventory"]==entries["R885-original-source-inventory.json"]
        assert receipt["source_bundle"]==entries["R885-retained-R827-inputs.tar.gz"]
        assert fingerprint(inventory["source_R827"]["files"])==tag["source_R827"]["selected_files_sha256"]
        assert len(inventory["source_R827"]["files"])==15
        summary={
            "result":RESULT,"actual_source":source,"source_manifest":spec(folder/MANIFEST),
            "source_manifest_file_count":len(entries),"source_reference":spec(folder/REFERENCE),
            "configuration_sha256":fingerprint(tag),"core_seconds":core["seconds"],
            "actual_certificate":entries[FINAL],"actual_stage_manifest":plain(cert["stage_manifest"]),
            "characteristic_relation":plain(cert["characteristic_relation"]),
            "one_row_adjugate":plain(cert["one_row_adjugate"]),"source_audit":plain(cert["source_audit"]),
            "source_inventory":entries["R885-original-source-inventory.json"],
            "retained_inputs_receipt":entries["R885-retained-inputs-receipt.json"],
            "retained_original_R827_bundle":entries["R885-retained-R827-inputs.tar.gz"],
            "core_receipt":entries["core-receipt.json"],
            "complete":True,"actual_complete_stage_count":549,"actual_node_count":273,
            "actual_row_level_count":273,"old_cyclic_nodes":audit["old_completed_cyclic_nodes"],
            "full_row_source_count":len(row_sources),
            "full_row_source_compressed_bytes":sum(x["bytes"] for x in row_sources),
            "actual_complete_polynomial_adjugate_row_certified":True,
            "actual_full_terminal_row_zero":True,
            "whole_adjugate_matrix_materialized":False,
            "target_Artin_coordinates_nine_norms_Picard_support_or_height_computed":False,
            "selected_original_files":{n:entries[n] for n in sorted(selected)},
            "old_carrier_or_full_row_payload_downloaded":False,"new_mathematics_executed":False,
            "range_transport":archive.receipt()}
        write(out/"R885-ended-small-IO-summary.json",summary)
        with tarfile.open(out/"R885-ended-selected-original-small.tar.gz","w:gz") as tar:
            for path in sorted(folder.iterdir()):
                tar.add(path,arcname="original/"+path.name,recursive=False)
        print("R885_ENDED_SMALL_IO="+json.dumps(summary,sort_keys=True),flush=True)
    finally:
        archive.close()
if __name__=="__main__":
    main()

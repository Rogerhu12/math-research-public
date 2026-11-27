#!/usr/bin/env python3
"""Reproduce the complete actual18 method-source binding repair from frozen Git.

This only reads complete Git source objects, applies exact UTF-8 changes and
writes complete source files. No scientific module or Python AST is imported.
The three former files may already be replaced in the current checkout:
all original bytes come from the explicit fixed historical commit below.
This optional constructor is not an admission gate or scientific fixture.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

DATA = json.loads("{\"schema\":\"complete-meridian-actual18-method-source-binding-repair-text-reproduction-v1\",\"fixed_parent_commit\":\"36fb3539d71ac8826645df636359d34769f786e9\",\"original_executed_scientific_commit\":\"7936ae753065d6e47c1c02848551020acf5a7b2a\",\"sources\":[{\"parent\":{\"name\":\"fixed_fejer_meridian_analytic_normal_frame.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_analytic_normal_frame.py\",\"bytes\":47244,\"sha256\":\"ab282ea02ce774b6f2aa044c700389369d05d1ff6105cdc9a0dbdae33a4db544\",\"git_blob_sha\":\"abfa338ddea26f149a337a14882121505ba1af96\"},\"output\":{\"role\":\"analytic_frame\",\"name\":\"fixed_fejer_meridian_analytic_normal_frame.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_analytic_normal_frame.py\",\"bytes\":47431,\"sha256\":\"d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd\",\"git_blob_sha\":\"9c24a81d34171155f6bb4e19592bfe54a2fb7b40\"},\"patches\":[{\"label\":\"Append the complete current meridian-data source to the existing strict override dictionary\",\"before\":\"\\\"}\\n\\n\\ndef complete_method_ast():\",\"after\":\"\\\", \\\"_meridian_data\\\": \\\"    def _meridian_data(self, x, query, phi, curvature, query_label):\\\\n        return self.detached_meridian_values.meridian_data(x,query,phi,curvature,query_label)\\\\n\\\"}\\n\\n\\ndef complete_method_ast():\",\"count\":1}]},{\"parent\":{\"name\":\"fixed_fejer_detached_meridian_normal_lift.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py\",\"bytes\":96276,\"sha256\":\"388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4\",\"git_blob_sha\":\"8a22b31dcc36d3160d4c968f9645600961a22abc\"},\"output\":{\"role\":\"endpoint\",\"name\":\"fixed_fejer_detached_meridian_normal_lift.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py\",\"bytes\":96276,\"sha256\":\"33c269f3cd04c9435ccb5144984124c8a0b6ae348f95c8bd71ac92a334c51cf4\",\"git_blob_sha\":\"8af8a63ac394bc3f0f4a3fa1b30ff5eb8fd5cdef\"},\"patches\":[{\"label\":\"Pin the complete corrected analytic-frame source\",\"before\":\"ab282ea02ce774b6f2aa044c700389369d05d1ff6105cdc9a0dbdae33a4db544\",\"after\":\"d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd\",\"count\":1}]},{\"parent\":{\"name\":\"fixed_fejer_meridian_root_packets.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_root_packets.py\",\"bytes\":73723,\"sha256\":\"910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15\",\"git_blob_sha\":\"e347b156b0b4bec87871fc07809a40a3bbda4ddd\"},\"output\":{\"role\":\"root_packets\",\"name\":\"fixed_fejer_meridian_root_packets.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_root_packets.py\",\"bytes\":73723,\"sha256\":\"45dd618adaa5262002bfb9d1979b6f555fe5233a57ec0f75abcec2ab7633a5be\",\"git_blob_sha\":\"8a578530490cfed771974ff0095b82d8814ef8d8\"},\"patches\":[{\"label\":\"Register the actual corrected normal whole source\",\"before\":\"388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4\",\"after\":\"33c269f3cd04c9435ccb5144984124c8a0b6ae348f95c8bd71ac92a334c51cf4\",\"count\":1},{\"label\":\"Register its corrected analytic-frame whole source\",\"before\":\"ab282ea02ce774b6f2aa044c700389369d05d1ff6105cdc9a0dbdae33a4db544\",\"after\":\"d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd\",\"count\":1}]}],\"required_complete_wrapper\":{\"parent_name\":\"fixed_fejer_detached_meridian_normal_lift.py\",\"source\":\"    def _meridian_data(self, x, query, phi, curvature, query_label):\\n        return self.detached_meridian_values.meridian_data(x,query,phi,curvature,query_label)\\n\"}}")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def frozen_source(repo, record):
    raw = subprocess.check_output(
        ["git", "show", "--no-textconv",
         DATA["fixed_parent_commit"]+":"+record["path"]], cwd=repo)
    git_digest = hashlib.sha1(
        b"blob "+str(len(raw)).encode("ascii")+b"\0"+raw).hexdigest()
    if (len(raw)!=record["bytes"] or digest(raw)!=record["sha256"]
            or git_digest!=record["git_blob_sha"]):
        raise ValueError("The complete frozen original Git source differs: "+record["path"])
    return raw


def replace_exact(text, before, after, count, label):
    if not before or text.count(before)!=count:
        raise ValueError("A complete source replacement has a different count: "+label)
    return text.replace(before, after)


def write_complete(outdir, record, raw):
    if len(raw)!=record["bytes"] or digest(raw)!=record["sha256"]:
        raise ValueError("The complete repaired source differs: "+record["name"])
    path=outdir/record["name"]
    if path.exists():
        if path.read_bytes()!=raw:
            raise ValueError("Refuse to overwrite a different complete source: "+str(path))
    else:
        with path.open("xb") as stream:
            stream.write(raw)
    if path.read_bytes()!=raw:
        raise ValueError("A full repaired source changed while writing")
    return dict(path=str(path.resolve()),bytes=len(raw),sha256=digest(raw))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--outdir",type=Path,required=True)
    args=parser.parse_args()
    repo=args.repo.resolve()
    outdir=args.outdir.resolve()
    if outdir==repo or repo in outdir.parents or outdir in repo.parents:
        raise ValueError("Use a separate source-only scratch directory outside the checkout")
    originals={}
    prepared=[]
    for item in DATA["sources"]:
        raw=frozen_source(repo,item["parent"])
        originals[item["parent"]["name"]]=raw
        text=raw.decode("utf-8")
        for patch in item["patches"]:
            text=replace_exact(text,patch["before"],patch["after"],
                patch["count"],patch["label"])
        result=text.encode("utf-8")
        restored=text
        for patch in reversed(item["patches"]):
            restored=replace_exact(restored,patch["after"],patch["before"],
                patch["count"],"inverse "+patch["label"])
        if restored.encode("utf-8")!=raw:
            raise ValueError("The complete inverse failed to recover every original byte")
        if len(result)!=item["output"]["bytes"] or digest(result)!=item["output"]["sha256"]:
            raise ValueError("The complete repaired source identity changed")
        prepared.append((item["output"],result))
    wrapper=DATA["required_complete_wrapper"]
    if originals[wrapper["parent_name"]].decode("utf-8").count(wrapper["source"])!=1:
        raise ValueError("The actual failed normal source has a different complete wrapper")
    outdir.mkdir(parents=True,exist_ok=True)
    outputs=[write_complete(outdir,record,raw) for record,raw in prepared]
    for item in DATA["sources"]:
        if frozen_source(repo,item["parent"])!=originals[item["parent"]["name"]]:
            raise ValueError("A complete frozen parent changed during construction")
    print(json.dumps(dict(schema=DATA["schema"],complete=True,outputs=outputs,
        fixed_parent_commit=DATA["fixed_parent_commit"],
        original_execution_commit=DATA["original_executed_scientific_commit"],
        original_bytes_read_from_current_checkout=False,
        every_complete_parent_restored_by_exact_inverse=True,
        original_guard_and_mathematical_functions_replaced=False,
        source_byte_reproduction_only=True,Python_AST_or_compile_executed=False,
        scientific_module_import_F_J_root_or_fixture_execution=False,
        new_scientific_admission_gate=False),sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())

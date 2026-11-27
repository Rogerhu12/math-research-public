#!/usr/bin/env python3
"""Reproduce the complete actual18 static/bound callable-source repair.

Read exact frozen Git source bytes and write complete new source files only.
No scientific module, numerical array, Python AST, compiler, fixture or solver
is loaded. This optional text constructor is not a scientific admission gate.
The current checkout may already contain the repaired same-named sources.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

DATA = json.loads("{\"schema\":\"complete-meridian-actual18-callable-source-binding-repair-text-reproduction-v1\",\"fixed_parent_commit\":\"bf863c8796a36e99c175117688e692fd5009a89e\",\"original_executed_scientific_commit\":\"5a8dcd127ecb1120418b258f43fad7ada5080560\",\"base_source\":{\"name\":\"fixed_fejer_supported_so3_meridian_operator.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py\",\"bytes\":40840,\"sha256\":\"552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3\",\"git_blob_sha\":\"1d9e435bb68374b71c3d7361771c28f47838d59e\"},\"sources\":[{\"parent\":{\"name\":\"fixed_fejer_detached_meridian_values.py\",\"bytes\":41030,\"sha256\":\"7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd\",\"git_blob_sha\":\"6ab29473b0d549539de69a064efb19af4227a867\",\"parent\":null,\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_values.py\"},\"output\":{\"role\":\"detached_meridian\",\"name\":\"fixed_fejer_detached_meridian_values.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_values.py\",\"bytes\":41126,\"sha256\":\"eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de\",\"git_blob_sha\":\"2b547c08dcaeb55701f5c68ba56d405f595f5b9e\"},\"patches\":[{\"before\":\"            function=getattr(q.base,name).__func__\\n\",\"after\":\"            bound=getattr(q.base,name)\\n            function=getattr(bound,'__func__',bound)\\n\",\"count\":1,\"label\":\"Unwrap the actual instance or static base callable before the unchanged complete-source hash guard\"},{\"before\":\"                or any(getattr(q.base,name).__func__ is not fn for name,fn in self.methods.items())\\n\",\"after\":\"                or any(getattr(getattr(q.base,name),'__func__',getattr(q.base,name)) is not fn\\n                       for name,fn in self.methods.items())\\n\",\"count\":1,\"label\":\"Revalidate the same actual unwrapped callable identity on every request\"}]},{\"parent\":{\"role\":\"endpoint\",\"name\":\"fixed_fejer_detached_meridian_normal_lift.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py\",\"bytes\":96276,\"sha256\":\"33c269f3cd04c9435ccb5144984124c8a0b6ae348f95c8bd71ac92a334c51cf4\",\"git_blob_sha\":\"8af8a63ac394bc3f0f4a3fa1b30ff5eb8fd5cdef\"},\"output\":{\"role\":\"endpoint\",\"name\":\"fixed_fejer_detached_meridian_normal_lift.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py\",\"bytes\":96276,\"sha256\":\"76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d\",\"git_blob_sha\":\"fc51c16b6dbd53abf04fe9175e5421f77e25c49c\"},\"patches\":[{\"before\":\"7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd\",\"after\":\"eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de\",\"count\":1,\"label\":\"Propagate the exact changed whole-source identity\"}]},{\"parent\":{\"role\":\"root_packets\",\"name\":\"fixed_fejer_meridian_root_packets.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_root_packets.py\",\"bytes\":73723,\"sha256\":\"45dd618adaa5262002bfb9d1979b6f555fe5233a57ec0f75abcec2ab7633a5be\",\"git_blob_sha\":\"8a578530490cfed771974ff0095b82d8814ef8d8\"},\"output\":{\"role\":\"root_packets\",\"name\":\"fixed_fejer_meridian_root_packets.py\",\"path\":\"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_root_packets.py\",\"bytes\":73723,\"sha256\":\"c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4\",\"git_blob_sha\":\"2b294ce46cf51c24c90b6e71c26d0d9c4269d28f\"},\"patches\":[{\"before\":\"33c269f3cd04c9435ccb5144984124c8a0b6ae348f95c8bd71ac92a334c51cf4\",\"after\":\"76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d\",\"count\":1,\"label\":\"Propagate the exact changed whole-source identity\"}]}]}")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def frozen_source(repo, record):
    raw=subprocess.check_output(
        ["git","show","--no-textconv",DATA["fixed_parent_commit"]+":"+record["path"]],
        cwd=repo)
    git_digest=hashlib.sha1(b"blob "+str(len(raw)).encode("ascii")+b"\0"+raw).hexdigest()
    if (len(raw)!=record["bytes"] or digest(raw)!=record["sha256"]
            or git_digest!=record["git_blob_sha"]):
        raise ValueError("The complete frozen Git source differs: "+record["path"])
    return raw


def replace_exact(text, before, after, count, label):
    if not before or text.count(before)!=count:
        raise ValueError("A complete source replacement count differs: "+label)
    return text.replace(before,after)


def write_complete(outdir, record, raw):
    if len(raw)!=record["bytes"] or digest(raw)!=record["sha256"]:
        raise ValueError("The complete repaired source differs: "+record["name"])
    path=outdir/record["name"]
    if path.exists():
        if path.read_bytes()!=raw:
            raise ValueError("Refuse to overwrite another source: "+str(path))
    else:
        with path.open("xb") as stream:
            stream.write(raw)
    if path.read_bytes()!=raw:
        raise ValueError("A complete repaired source changed while writing")
    return dict(path=str(path.resolve()),bytes=len(raw),sha256=digest(raw))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--outdir",type=Path,required=True)
    args=parser.parse_args()
    repo=args.repo.resolve()
    outdir=args.outdir.resolve()
    if outdir==repo or repo in outdir.parents or outdir in repo.parents:
        raise ValueError("Use source-only scratch outside the checkout")
    base=frozen_source(repo,DATA["base_source"])
    originals={}
    prepared=[]
    for item in DATA["sources"]:
        raw=frozen_source(repo,item["parent"])
        originals[item["parent"]["name"]]=raw
        text=raw.decode("utf-8")
        for patch in item["patches"]:
            text=replace_exact(text,patch["before"],patch["after"],
                patch["count"],patch["label"])
        restored=text
        for patch in reversed(item["patches"]):
            restored=replace_exact(restored,patch["after"],patch["before"],
                patch["count"],"inverse "+patch["label"])
        if restored.encode("utf-8")!=raw:
            raise ValueError("The inverse did not recover every complete original byte")
        result=text.encode("utf-8")
        if len(result)!=item["output"]["bytes"] or digest(result)!=item["output"]["sha256"]:
            raise ValueError("The complete repaired source identity differs")
        prepared.append((item["output"],result))
    outdir.mkdir(parents=True,exist_ok=True)
    outputs=[write_complete(outdir,record,raw) for record,raw in prepared]
    if frozen_source(repo,DATA["base_source"])!=base:
        raise ValueError("The complete frozen base source changed")
    for item in DATA["sources"]:
        if frozen_source(repo,item["parent"])!=originals[item["parent"]["name"]]:
            raise ValueError("A complete frozen parent changed")
    print(json.dumps(dict(schema=DATA["schema"],complete=True,outputs=outputs,
        fixed_parent_commit=DATA["fixed_parent_commit"],
        original_execution_commit=DATA["original_executed_scientific_commit"],
        original_bytes_read_from_current_checkout=False,
        every_complete_parent_restored_by_exact_inverse=True,
        original_codefile_and_callable_identity_guards_retained=True,
        only_callable_extraction_and_downstream_identity_changed=True,
        scientific_formulas_changed=False,
        source_byte_reproduction_only=True,Python_AST_or_compile_executed=False,
        scientific_module_import_F_J_root_or_fixture_execution=False,
        new_scientific_admission_gate=False),sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())

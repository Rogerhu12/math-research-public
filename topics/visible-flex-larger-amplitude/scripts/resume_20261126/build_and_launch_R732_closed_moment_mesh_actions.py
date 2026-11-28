#!/usr/bin/env python3
"""Build all complete R732 source dependencies, then run the unchanged full target argv."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import traceback

BUILDERS = {
  "science": {
    "source": {
      "role": "complete_source_builder",
      "name": "reproduce_r732_R729_complete_sources.mjs",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_r732_R729_complete_sources.mjs",
      "bytes": 53259,
      "sha256": "f250982e3abe4b01e9e6c49211fb3d7bf066b8d84df91a7f5e5fb32b57782da3",
      "git_blob_sha": "7148f6aba2456e391a94b7cf0ccb3f2c0f929a77"
    },
    "schema": "actual-complete-R732-R729-source-materialization-v1",
    "count_key": "complete_source_file_count",
    "count": 17
  },
  "accurate": {
    "source": {
      "role": "normal build reproducer of four complete original-source-guarded runtimes from four current main R722 parents with all exact reversible replacements",
      "name": "reproduce_R732_accurate_normal_geometry_sources.mjs",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_R732_accurate_normal_geometry_sources.mjs",
      "bytes": 69694,
      "sha256": "f001de2154b6efae895c2eec744958762a9f6f44a4b36ed15e89c2afbd238c3c",
      "git_blob_sha": "d4fa267ddaf6e2667e68c423a6644dc42afc81f8"
    },
    "schema": "complete-R732-accurate-source-text-reconstruction-v1",
    "count_key": "complete_source_count",
    "roles": [
      "normal",
      "leaf",
      "geometry",
      "bridge"
    ]
  },
  "closed_moment": {
    "source": {
      "role": "normal complete source reconstruction from checked-in R722/R723 closure and flux parents, each replacement fully reversible",
      "name": "reproduce_R732_closed_and_moment_sources.mjs",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_R732_closed_and_moment_sources.mjs",
      "bytes": 68970,
      "sha256": "1b03dc841bd5a352e8a10f8ed34e6358fbdc80abf598b2f7b2e650663bd75534",
      "git_blob_sha": "8c79d6fcdb5043d82b21d492f7f488bc675acdc0"
    },
    "schema": "complete-R732-closed-and-moment-source-reconstruction-v1",
    "count_key": "complete_source_count",
    "roles": [
      "closed_base",
      "directional",
      "flux",
      "moment"
    ]
  },
  "mesh": {
    "source": {
      "role": "complete reversible source build from three published complete R723 field, mesh and pure reader sources",
      "name": "reproduce_R732_complete_same_field_mesh_sources.mjs",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_R732_complete_same_field_mesh_sources.mjs",
      "bytes": 38841,
      "sha256": "27498c163d0ac924e988be7a9c8e5a8d425212bc006629b83f1c52adf74a2af9",
      "git_blob_sha": "5cab1f8adbc71b7584714c6637dacab5e44ff106"
    },
    "schema": "complete-R732-mesh-source-text-reconstruction-v1",
    "count_key": "complete_source_count",
    "roles": [
      "meshinput",
      "mesh",
      "meshread"
    ]
  }
}
ENTRIES = {
  "closed": {
    "role": "complete original R723 directional flow/reach and all-phase marked/unmarked source for the actual R732 whole field",
    "name": "fixed_fejer_R732_R723_directional_closed_phase_grip_evidence.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R732_R723_directional_closed_phase_grip_evidence.py",
    "bytes": 87597,
    "sha256": "524c65ae8b34439ad8a746528442fa201ebd9fae835d4b7b064df3e308280a61",
    "git_blob_sha": "dd75f954d8af9ce49be6173f6fb2730265490e12"
  },
  "flux": {
    "role": "full R716 twelve flux channels, all original blocks and source-specific half-turn stage pairing using the complete accurate R732 leaf reader",
    "name": "fixed_fejer_R732_complete_closed_surface_moment_integrals.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R732_complete_closed_surface_moment_integrals.py",
    "bytes": 33236,
    "sha256": "dc0310f65768a10b761217cfc091a16f02fb14bfec952254bf553c7c5a2b9c6a",
    "git_blob_sha": "db7dee05ef76ecd3ab436be50a53b60b79209996"
  },
  "moment": {
    "role": "complete R716 centred quotient with all original R650 or strict R723 main/sidecar, same-field twelve channels and signed half-turn evidence",
    "name": "fixed_fejer_R732_R723_compatible_r716_centred_volume_moment.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R732_R723_compatible_r716_centred_volume_moment.py",
    "bytes": 61926,
    "sha256": "0d57a0f6b081e7d4166d262b6497dbb560b1ca02fcff0947c0bc2204879809a8",
    "git_blob_sha": "7e4c697ff068b836c1406ed0f843caca455ac9da"
  },
  "mesh": {
    "role": "complete R732 working phase meshes with free-point held evidence, all public raw six-jets and complete original domain refinement",
    "name": "fixed_fejer_R732_R723_same_field_phase_meshes.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R732_R723_same_field_phase_meshes.py",
    "bytes": 55092,
    "sha256": "33863e6427077490c38c9f7624ee6ed09c6fd143990360a216784e64f9eb1444",
    "git_blob_sha": "aab415a8699b6e9ea8b0383d5af6148dd979d8be"
  },
  "mesh_read": {
    "role": "complete pure mesh/point/immutable reference and optional closed same-field evidence reader",
    "name": "read_fixed_fejer_R732_R723_same_field_phase_meshes.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_R732_R723_same_field_phase_meshes.py",
    "bytes": 25905,
    "sha256": "f3586af539f1941b8b6903a8678d80cb2c087edaf07d0b19d429d1da77b12278",
    "git_blob_sha": "1b46ad05ef7082408f85c02d4db91ea70bf982bf"
  }
}


def file_record(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
        git_blob_sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest())


def whole_file(path, expected):
    actual = file_record(path)
    if any(actual[key] != expected[key] for key in ('bytes', 'sha256', 'git_blob_sha')):
        raise ValueError('Complete source differs: '+str(path))
    return actual


def save(path, value):
    temporary = path.with_name(path.name+'.writing-'+str(os.getpid()))
    with temporary.open('x', encoding='utf-8', newline='\n') as handle:
        json.dump(value, handle, indent=2, allow_nan=False)
        handle.write('\n')
    os.replace(temporary, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", choices=sorted(ENTRIES), required=True)
    parser.add_argument("--build-record", type=Path, required=True)
    parser.add_argument("original_arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    original = list(args.original_arguments)
    if original[:1] == ["--"]:
        original = original[1:]
    if original.count("--repo") != 1:
        raise ValueError("The complete original entry must carry its repository argument")
    repo = Path(original[original.index("--repo")+1]).resolve(strict=True)
    target = ENTRIES[args.entry]
    command = [sys.executable, "-u", str(repo/target["path"]), *original]
    record = args.build_record.resolve()
    if repo == record or repo in record.parents:
        raise ValueError("Source build records belong in the runner work directory")
    record.parent.mkdir(parents=True, exist_ok=True)
    bundle = ["science","accurate","closed_moment"]
    if args.entry in ("mesh","mesh_read"):
        bundle.append("mesh")
    records = {key:record.with_name(record.name+"."+key+".json") for key in bundle}
    if record.exists() or any(path.exists() for path in records.values()):
        raise FileExistsError("Each invocation preserves its own full build and child-return records")
    node = shutil.which("node")
    if node is None:
        raise RuntimeError("Node.js is required for this complete text source build")
    value = dict(schema="complete-R732-closed-moment-mesh-normal-build-and-entry-v1",
        complete=False, phase="source-materialization", wrapper_source=file_record(__file__),
        wrapper_argv=list(sys.argv), python_version=sys.version, node_executable=node,
        source_commit=subprocess.check_output(["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip(),
        workflow_trigger_commit=os.environ.get("GITHUB_SHA"), github_run_id=os.environ.get("GITHUB_RUN_ID"),
        github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"), complete_builds={},
        entry=args.entry, target=target, complete_target_argv=command, original_target_words=original,
        original_direct_entry=True, scientific_role_count=139, complete_scientific_runtime_count=24,
        extra_scientific_preflight_or_execution=False, extra_child_budget=None,
        child_started=False, child_returncode=None, mathematical_success_or_certificate_claimed=False)
    save(record,value)
    try:
        for key in bundle:
            spec = BUILDERS[key]
            script = repo/spec["source"]["path"]
            expected = whole_file(script,spec["source"])
            build = [node,str(script),"--source-repository",str(repo),
                "--output-repository",str(repo),"--record",str(records[key])]
            build_info = dict(source=expected, argv=build, returncode=None)
            value["complete_builds"][key] = build_info
            save(record,value)
            built = subprocess.run(build,cwd=repo,check=False)
            build_info["returncode"] = built.returncode
            if built.returncode:
                raise RuntimeError("Complete source build returned "+str(built.returncode)+" for "+key)
            result = json.loads(records[key].read_text(encoding="utf-8"))
            count = spec.get("count",len(spec.get("roles",[])))
            if (result.get("complete") is not True or result.get("direction")!="forward"
                    or result.get("schema")!=spec["schema"] or result.get(spec["count_key"])!=count):
                raise ValueError("The complete source build is missing its recorded whole outputs for "+key)
            if "roles" in spec and [row["role"] for row in result["complete_sources"]]!=spec["roles"]:
                raise ValueError("The complete source build changed role order for "+key)
            build_info.update(record=file_record(records[key]),complete_materialization=result)
        value["actual_target"] = whole_file(repo/target["path"],target)
        value.update(phase="original-entry-start",child_started=True)
        save(record,value)
        child = subprocess.run(command,cwd=repo,check=False)
        value.update(phase="original-entry-returned",complete=True,child_returncode=child.returncode,
            successful_process_return=child.returncode==0)
        save(record,value)
        return child.returncode if child.returncode>=0 else 128-child.returncode
    except Exception as error:
        value.update(phase="source-build-or-entry-error",
            error=dict(type=type(error).__name__,message=str(error)))
        save(record,value)
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

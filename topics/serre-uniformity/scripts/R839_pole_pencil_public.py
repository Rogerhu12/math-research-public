#!/usr/bin/env python3
"""Standard-library source/carrier runner for the original D pole pencil."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R839-pole-pencil-public-request.json"
RESULT = "R839-original-D-pencil-and-eight-generator-pole-ideal"
FINAL = "p41-original-D-pencil-and-pole-ideal-certificate.json"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R839-pole-pencil-retained-original-inputs.tar.gz"
INVENTORY = "R839-pole-pencil-original-source-inventory.json"
INPUT_RECEIPT = "R839-pole-pencil-retained-inputs-receipt.json"
MATH_INVENTORY = "R839-pole-pencil-stage-manifest.json.gz"
LEGACY_NAME = "R839_original_short_RR_spaces.py"
LEGACY_SHA = "0a027c2dd83cfab37181e6386cfd8b22baf176421b727d81a7584d7b351d0c36"
RANGE_NAME = "R824_public_original_global_polar_generators.py"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "configuration_sha256")
LABELS = ("R842", "R827", "R787", "R786", "R775", "R809", "R837")
META = (MANIFEST, "run-receipt.json", "core-receipt.json", "public-actions-input.json")
EPS = [0]+[1]*144+[2]*127
NODES = list(range(5))
FLAGS = ("complete_original_D_pencil_certified", "complete_original_Ey_ideal_certified")
SCOPE = {
    "auxiliary_prime": 1000000753, "original_branch": 0,
    "normal_basis_rank": 272, "normal_basis_degrees": EPS,
    "original_V3_dimension": 690, "original_D_RR_dimension": 295,
    "normal_conversion_rhs_count": 690, "normal_conversion_batch_size": 30,
    "old_S5_prefix_shape": [1380, 1234], "normal_V3_coordinate_count": 690,
    "old_fiber_nodes": NODES, "fiber_evaluation_matrix_shape": [1360, 1380],
    "required_pencil_rank": 1111,
    "fixed_a_original_D_basis_column": 0,
    "b_candidate_family": "sum_{j=0}^{294} integer_parameter^j original_D_basis_column_j",
    "candidate_parameter_start": 1,
    "all_690_tau_squared_V3_products_are_original_V5_same_index_aliases": True,
    "old_S5_inverse_or_Krylov_inverse_or_Fourier_products_recomputed": False,
    "rank_certificate_only_requires_evaluation_lower_bound": True,
    "five_fibers_not_assumed_to_avoid_D": True,
    "candidate_pole_ideal_generators": 8,
    "original_pole_divisor_identity": "E_y = fixed_21_branch_points + 3*original_D",
    "char0_sections_remain_original_unit_solve_expressions": True,
    "budget_maximum_trials_and_absolute_directories_excluded_from_mathematical_identity": True,
}
H64 = re.compile(r"[0-9a-f]{64}")
IO = None


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            value.update(block)
    return value.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    temporary.write_text(json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n", encoding="utf-8")
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name, str) and Path(name).name == name and name not in (".", "..") and "\\" not in name
    return name


def plain(value):
    out = {key: value[key] for key in ("file", "bytes", "sha256")}
    safe_name(out["file"])
    assert isinstance(out["bytes"], int) and out["bytes"] >= 0 and H64.fullmatch(out["sha256"])
    return out


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(folder, entry):
    entry = plain(entry)
    path = Path(folder)/entry["file"]
    assert file_spec(path) == entry, ("Changed source bytes", str(path))
    return path


def topic_path(name):
    relative = PurePosixPath(name)
    assert not relative.is_absolute() and ".." not in relative.parts
    path = (TOPIC/str(relative)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def identity(item):
    return {key: item[key] for key in BASE_KEYS}


def load_helper(item, helper_dir=None):
    global IO
    path = (S if helper_dir is None else Path(helper_dir))/RANGE_NAME
    assert item["io_helper_sha256"] == RANGE_SHA and sha(path) == RANGE_SHA
    loader = importlib.util.spec_from_file_location("R839_pole_stdlib_range_IO", path)
    IO = importlib.util.module_from_spec(loader)
    loader.loader.exec_module(IO)


def guard(item, path):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert path.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
    assert item["core"] == "R839_original_pole_pencil.py"
    assert item["wrapper"] == "R839_pole_pencil_public.py"
    assert item["legacy_core"] == LEGACY_NAME and item["legacy_core_sha256"] == LEGACY_SHA
    assert sha(S/item["core"]) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
    assert sha(S/LEGACY_NAME) == LEGACY_SHA
    assert 0 < item["budget_minutes"] <= 300 and int(item["maximum_trials"]) >= 1
    for key in ("proof", "method"):
        assert sha(topic_path(item[key])) == item[key+"_sha256"]
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert set(item["sources"]) == set(LABELS)
    for label, source in item["sources"].items():
        for key in ("core_sha256", "manifest_sha256", "configuration_sha256", "selected_files_sha256"):
            assert H64.fullmatch(source[key])
        assert isinstance(source["selected_file_count"], int) and source["selected_file_count"] >= 4
    load_helper(item)


def starting_names(label, source):
    names = set(META)
    if source.get("certificate_name"):
        names.add(source["certificate_name"])
    fixed = {
        "R842": ["R839-original-D-unit-kernel-basis.json.gz", "R839-original-S5-fixed-place-matrix.json.gz"],
        "R827": ["R827-prime-1000000753-S5-fixed-minor-inverse.json.gz", "R827-eight-original-unit-cyclic-nodes.json.gz"]+
                ["R827-prime-1000000753-z-"+str(c)+"-Krylov.json.gz" for c in NODES],
        "R787": ["R787-real-power5-row-"+str(i).zfill(4)+".json.gz" for i in range(690)],
        "R786": ["R786-exact-power5-basis-index.json.gz"],
        "R775": ["R775-basis-power-4.json.gz", "R775-basis-power-5.json.gz"],
        "R809": ["R809-S5-basis-index.json.gz"],
        "R837": [],
    }
    names.update(fixed[label])
    if source.get("configuration_stage"):
        names.add(safe_name(source["configuration_stage"]))
    return names


def extend_names(label, source, folder, names):
    folder = Path(folder)
    names = set(names)
    certname = source.get("certificate_name")
    cert = read(folder/certname) if certname and (folder/certname).exists() else None
    if label == "R842" and cert is not None:
        names.update(plain(cert[key])["file"] for key in ("D_kernel_basis", "source_audit", "stage_manifest"))
        kernel_path = folder/cert["D_kernel_basis"]["file"]
        if kernel_path.exists():
            names.add(plain(read(kernel_path)["source_original_D_matrix"])["file"])
    elif label == "R809":
        path = folder/"R809-S5-basis-index.json.gz"
        if path.exists():
            index = read(path)
            assert len(index["basis_rows"]) == 1234
            names.update(plain(row["source"])["file"] for row in index["basis_rows"])
    elif label == "R837" and cert is not None:
        names.update(plain(cert[key])["file"] for key in
                     ("pencil_certificate", "fixed_branch_space", "original_P0_evaluation", "stage_manifest"))
        pencil_path = folder/cert["pencil_certificate"]["file"]
        if pencil_path.exists():
            pencil = read(pencil_path)
            names.update(plain(pencil[key])["file"] for key in ("first_anchor", "second_anchor"))
    return names


def source_names(label, source, folder):
    names = starting_names(label, source)
    for _ in range(6):
        larger = extend_names(label, source, folder, names)
        if larger == names:
            return sorted(names)
        names = larger
    raise AssertionError("Unexpected cyclic source selection")


def review_source(label, source, folder):
    folder = Path(folder)
    assert file_spec(folder/MANIFEST) == {"file": MANIFEST, "bytes": source["manifest_bytes"], "sha256": source["manifest_sha256"]}
    manifest = read(folder/MANIFEST)
    assert manifest["result"] == source["result"]
    entries = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    entries[MANIFEST] = file_spec(folder/MANIFEST)
    names = source_names(label, source, folder)
    selected = {name: entries[name] for name in names}
    assert len(selected) == source["selected_file_count"]
    assert fingerprint([selected[name] for name in sorted(selected)]) == source["selected_files_sha256"]
    for row in selected.values():
        bound(folder, row)
    run, core, initial = (read(folder/name) for name in META[1:])
    assert run["result"] == core["result"] == initial["result"] == source["result"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert run["source_commit"] == initial["source_commit"] == source["source_commit"]
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["core_sha256"] == core["source_sha256"] == source["core_sha256"]
    assert initial["job"]["core_sha256"] == source["core_sha256"]
    if source.get("wrapper_sha256"):
        assert initial["driver_sha256"] == source["wrapper_sha256"]
    assert run["core_receipt_sha256"] == selected["core-receipt.json"]["sha256"]
    assert run["process_exit_code"] in source["accepted_process_exit_codes"]
    assert run.get("error") is None
    certname = source.get("certificate_name")
    cert = read(folder/certname) if certname else None
    if source["expected_conclusion"] == "success":
        assert run["complete"] is True and core["complete"] is True and run["process_exit_code"] == 0
        assert cert is not None and cert["complete"] is True
        assert core["certificate_sha256"] == selected[certname]["sha256"]
    else:
        assert label in ("R827", "R787")
        assert source["expected_conclusion"] == "failure" and run["complete"] is False and core["complete"] is False
        assert run["process_exit_code"] != 0
    if cert is not None:
        assert cert["result"] == source["result"]
        tag = cert["configuration"]
    else:
        tag = read(folder/source["configuration_stage"])["configuration"]
    assert tag["result"] == source["result"] and tag["source_sha256"] == source["core_sha256"]
    assert tag["python_flint"] == "0.9.0" and fingerprint(tag) == source["configuration_sha256"]
    for name in names:
        if name.endswith(".json.gz"):
            value = read(folder/name)
            assert value["complete"] is True and value["configuration"] == tag
            if "result" in value:
                assert value["result"] == source["result"]
    if label == "R842":
        assert cert["exact_original_D_RR_space_as_unit_chart_expression_certified"] is True
        assert [cert[key] for key in ("actual_T11_rank", "actual_T5_rank", "actual_D_kernel_rank", "actual_D_RR_dimension")] == [2451, 415, 395, 295]
        assert cert["prime"] == 1000000753 and cert["original_branch"] == 0
    if label == "R837":
        assert cert["fixed_branch_pencil_certified"] is True and cert["actual_pencil_rank"] == 1213
    return {**identity(source), "certificate_name": certname, "files": selected}


def review_all(item, retained):
    retained = Path(retained)
    reviewed = {label: review_source(label, item["sources"][label], retained/label) for label in LABELS}
    assert sum(len(value["files"]) for value in reviewed.values()) == item["selected_original_file_count"]
    assert fingerprint(reviewed) == item["expanded_sources_sha256"]
    return reviewed


def fetch_sources(item, retained):
    retained = Path(retained)
    transport = {}
    for label in LABELS:
        source = item["sources"][label]
        folder = retained/label
        folder.mkdir(parents=True, exist_ok=True)
        archive = IO.Archive(source, retained.parent/("download-pole-source-"+label), whole=False)
        try:
            archive.extract_bound(MANIFEST, source["manifest_sha256"], folder/MANIFEST, source["manifest_bytes"])
            manifest = read(folder/MANIFEST)
            entries = {row["file"]: plain(row) for row in manifest["files"]}
            assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
            names = starting_names(label, source)
            for _ in range(6):
                archive.extract_many([(name, entries[name]["sha256"], folder/name, entries[name]["bytes"])
                                      for name in sorted(names) if name != MANIFEST])
                larger = extend_names(label, source, folder, names)
                if larger == names:
                    break
                names = larger
            else:
                raise AssertionError("Source selection did not close")
            review_source(label, source, folder)
            transport[label] = archive.receipt()
        finally:
            archive.close()
    return review_all(item, retained), transport


def pack_sources(retained, sources, target):
    retained, target = Path(retained), Path(target)
    temporary = target.with_name(target.name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, filename="") as compressed:
            with tarfile.open(fileobj=compressed, mode="w|") as archive:
                for label in LABELS:
                    for name, row in sorted(sources[label]["files"].items()):
                        path = bound(retained/label, row)
                        info = archive.gettarinfo(str(path), arcname=label+"/"+name)
                        info.uid = info.gid = info.mtime = 0
                        info.uname = info.gname = ""
                        with path.open("rb") as stream:
                            archive.addfile(info, stream)
    temporary.replace(target)


def unpack_sources(bundle, retained, sources):
    retained = Path(retained)
    wanted = {(label, name): row for label in LABELS for name, row in sources[label]["files"].items()}
    seen = set()
    with tarfile.open(bundle, "r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            relative = PurePosixPath(member.name)
            assert not relative.is_absolute() and ".." not in relative.parts and "\\" not in member.name
            assert member.isfile() and len(relative.parts) == 2
            key = tuple(relative.parts)
            assert key in wanted and key not in seen
            seen.add(key)
            row = wanted[key]
            assert member.size == row["bytes"]
            target = retained/key[0]/key[1]
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(target.name+".download")
            digest, count = hashlib.sha256(), 0
            with archive.extractfile(member) as stream, temporary.open("wb") as destination:
                for block in iter(lambda: stream.read(4*1024*1024), b""):
                    destination.write(block)
                    digest.update(block)
                    count += len(block)
            assert count == row["bytes"] and digest.hexdigest() == row["sha256"]
            if target.exists():
                bound(target.parent, row)
                temporary.unlink()
            else:
                temporary.replace(target)
    assert seen == set(wanted)
    return len(seen)


def expected_tag(item, reviewed):
    return {"result": RESULT, "source_sha256": item["core_sha256"], "python_flint": "0.9.0", "p": 41,
            "legacy_R839_core_sha256": LEGACY_SHA,
            "pole_pencil_proof_sha256": item["proof_sha256"],
            "pole_pencil_method_sha256": item["method_sha256"], "sources": reviewed, **SCOPE}


def prepare_sources(item, out, allow_download=True):
    out = Path(out)
    retained = out.parent/"retained-original-pole-pencil"
    retained.mkdir(parents=True, exist_ok=True)
    if all((out/name).exists() for name in (INPUT_RECEIPT, INVENTORY, BUNDLE)):
        receipt, inventory = read(out/INPUT_RECEIPT), read(out/INVENTORY)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is True and inventory["complete"] is True
        assert receipt["source_requests"] == item["sources"]
        assert receipt["expanded_sources_sha256"] == item["expanded_sources_sha256"]
        bound(out, receipt["source_inventory"])
        bound(out, receipt["source_bundle"])
        count = unpack_sources(out/BUNDLE, retained, inventory["sources"])
        reviewed = review_all(item, retained)
        assert reviewed == inventory["sources"]
        assert count == receipt["minimal_bundle_member_count"] == item["selected_original_file_count"]
        return retained, receipt, reviewed
    assert allow_download, "Continuation must preserve its complete original source carrier."
    reviewed, transport = fetch_sources(item, retained)
    save(out/INVENTORY, {"result": RESULT, "complete": True, "sources": reviewed,
                        "all_members_are_unchanged_original_producer_bytes": True})
    pack_sources(retained, reviewed, out/BUNDLE)
    receipt = {"result": RESULT, "complete": True, "source_requests": item["sources"],
               "expanded_sources_sha256": item["expanded_sources_sha256"],
               "source_inventory": file_spec(out/INVENTORY), "source_bundle": file_spec(out/BUNDLE),
               "minimal_bundle_member_count": item["selected_original_file_count"], "range_transport": transport,
               "old_S5_inverse_Krylov_inverse_or_real_Fourier_conversions_recomputed": False}
    save(out/INPUT_RECEIPT, receipt)
    print("POLE_PENCIL_SOURCE_IO="+json.dumps({"source_inventory": receipt["source_inventory"],
          "source_bundle": receipt["source_bundle"], "selected_original_files": item["selected_original_file_count"],
          "new_mathematics_executed": False}, sort_keys=True), flush=True)
    return retained, receipt, reviewed


def output_manifest(out):
    out = Path(out)
    entries = [dict(file_spec(path), included_in_git=False) for path in sorted(out.iterdir())
               if path.is_file() and path.name not in (MANIFEST, REFERENCE)
               and not path.name.endswith((".tmp", ".download", ".partial"))]
    save(out/MANIFEST, {"result": RESULT, "files": entries,
                       "temporary_active_checkpoint_retention_days": 1,
                       "reproducible_data_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": MANIFEST, "manifest_sha256": sha(out/MANIFEST),
                        "manifest_bytes": (out/MANIFEST).stat().st_size, "file_count": len(entries)})


def stable_job(item):
    return {key: value for key, value in item.items()
            if key not in ("resume", "budget_minutes", "maximum_trials", "readme_sha256", "rules_last_read_commit")}


def restore(item, out):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    out, meta = Path(out), Path(out).parent/"resume-pole-pencil-metadata"
    meta.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(resume, out.parent/"download-pole-pencil-resume", whole=False)
    try:
        archive.extract_bound(MANIFEST, resume["manifest_sha256"], meta/MANIFEST, resume["manifest_bytes"])
        manifest = read(meta/MANIFEST)
        assert manifest["result"] == RESULT
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == resume["manifest_file_count"]
        names = ["run-receipt.json", "public-actions-input.json", "core-receipt.json", INPUT_RECEIPT, INVENTORY, BUNDLE]
        for name in names:
            if name == "core-receipt.json" and name not in entries:
                continue
            row = entries[name]
            destination = out/name if name in (INPUT_RECEIPT, INVENTORY, BUNDLE) else meta/name
            archive.extract_bound(name, row["sha256"], destination, row["bytes"])
        run, initial = read(meta/"run-receipt.json"), read(meta/"public-actions-input.json")
        assert run["result"] == initial["result"] == RESULT
        assert str(run["workflow_run_id"]) == str(resume["run_id"])
        assert run["source_commit"] == initial["source_commit"] == resume["source_commit"]
        assert initial["core_sha256"] == item["core_sha256"]
        assert stable_job(initial["job"]) == stable_job(item)
        assert run["process_exit_code"] in resume["accepted_process_exit_codes"]
        core = None
        if (meta/"core-receipt.json").exists():
            core = read(meta/"core-receipt.json")
            assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
            assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        else:
            assert run.get("core_receipt_sha256") is None and run["complete"] is False
        _, _, reviewed = prepare_sources(item, out, allow_download=False)
        tag = expected_tag(item, reviewed)
        math_names = sorted(name for name in entries if name.startswith("R839-pole-") and name.endswith(".json.gz"))
        archive.extract_many([(name, entries[name]["sha256"], out/name, entries[name]["bytes"]) for name in math_names])
        for name in math_names:
            value = read(out/name)
            assert value["complete"] is True and value["configuration"] == tag and value["result"] == RESULT
        restored_final = False
        if FINAL in entries:
            row = entries[FINAL]
            archive.extract_bound(FINAL, row["sha256"], meta/FINAL, row["bytes"])
            final = read(meta/FINAL)
            assert final["configuration"] == tag and final["result"] == RESULT
            if final["complete"] is True:
                assert run["complete"] is True and run["process_exit_code"] == 0
                assert core is not None and core["complete"] is True and core["certificate_sha256"] == row["sha256"]
                assert all(final[key] is True for key in FLAGS) and final["actual_pencil_rank"] == 1111
                shutil.copyfile(meta/FINAL, out/FINAL)
                restored_final = True
        save(out/"resume-inheritance-receipt.json", {
            "result": RESULT, "complete": True, "source_resume": resume,
            "original_manifest": file_spec(meta/MANIFEST), "range_transport": archive.receipt(),
            "all_restored_complete_stages": [entries[name] for name in math_names],
            "restored_successful_final": restored_final,
            "old_complete_source_bound_stages_not_recomputed": True,
            "incomplete_final_not_used_to_override_newer_completed_stages": True})
    finally:
        archive.close()


def compute(item, out, request_path):
    out.mkdir(parents=True, exist_ok=True)
    process, exitcode, error, outer_timeout = None, 1, None, False
    try:
        restore(item, out)
        retained, receipt, reviewed = prepare_sources(item, out)
        expanded = dict(item)
        expanded["sources"] = {label: {**reviewed[label], "directory": str((retained/label).resolve())}
                               for label in LABELS}
        for key in ("proof", "method"):
            expanded[key] = str(topic_path(item[key]))
        save(out/"public-actions-expanded-job.json", expanded)
        initial = {"result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
                   "source_commit": os.environ["GITHUB_SHA"], "job": item,
                   "request_sha256": sha(request_path), "driver_sha256": sha(__file__),
                   "core_sha256": item["core_sha256"], "legacy_core_sha256": LEGACY_SHA,
                   "proof_sha256": item["proof_sha256"], "method_sha256": item["method_sha256"],
                   "io_helper_sha256": RANGE_SHA, "workflow_sha256": sha(REPO/item["workflow"]),
                   "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
                   "source_inventory": receipt["source_inventory"],
                   "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                   "all_new_mathematics_runs_only_in_separate_public_Actions_core": True}
        save(out/"public-actions-input.json", initial)
        command = [sys.executable, str(S/item["core"]), "--config", str(out/"public-actions-expanded-job.json"),
                   "--out", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w", encoding="utf-8") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                exitcode = process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                exitcode = 124
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
        if process is not None and process.poll() is None:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
        exitcode = 1
    finally:
        core_path = out/"core-receipt.json"
        core = read(core_path) if core_path.exists() else None
        final = read(out/FINAL) if (out/FINAL).exists() else None
        complete = exitcode == 0 and core is not None and core.get("complete") is True and \
            final is not None and final.get("complete") is True and all(final.get(key) is True for key in FLAGS)
        run = {"result": RESULT, "p": 41, "complete": complete, "process_exit_code": exitcode, "error": error,
               "core_receipt_sha256": sha(core_path) if core_path.exists() else None,
               "source_commit": os.environ.get("GITHUB_SHA"), "workflow_run_id": os.environ.get("GITHUB_RUN_ID"),
               "workflow_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
               "execution_environment": "public-repository-github-actions", "outer_timeout": outer_timeout,
               "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
        save(out/"run-receipt.json", run)
        output_manifest(out)
        print("POLE_PENCIL_RUN_RECEIPT="+json.dumps(run, sort_keys=True), flush=True)
    return exitcode


def verify(item, out, request_path):
    manifest = read(out/MANIFEST)
    assert manifest["result"] == RESULT
    entries = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    for row in entries.values():
        bound(out, row)
    reference = read(out/REFERENCE)
    assert reference["result"] == RESULT and reference["manifest_sha256"] == sha(out/MANIFEST)
    assert reference["manifest_bytes"] == (out/MANIFEST).stat().st_size and reference["file_count"] == len(entries)
    run = read(out/"run-receipt.json")
    if not run.get("complete"):
        print("POLE_PENCIL_INCOMPLETE_IO_REVIEW="+json.dumps({"complete": False, "run": run,
              "manifest_files": len(entries), "no_failed_modular_trial_claimed_as_original_pencil": True}, sort_keys=True), flush=True)
        return 2
    _, receipt, reviewed = prepare_sources(item, out, allow_download=False)
    initial, core, final = (read(out/name) for name in ("public-actions-input.json", "core-receipt.json", FINAL))
    assert initial["job"] == item and initial["request_sha256"] == sha(request_path)
    assert initial["source_commit"] == run["source_commit"]
    assert initial["driver_sha256"] == sha(__file__) and initial["core_sha256"] == item["core_sha256"]
    assert core["result"] == final["result"] == RESULT and core["complete"] is True and final["complete"] is True
    assert run["process_exit_code"] == 0 and core["source_sha256"] == item["core_sha256"]
    assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
    assert core["certificate_sha256"] == entries[FINAL]["sha256"]
    tag = expected_tag(item, reviewed)
    assert final["configuration"] == tag
    assert all(final[key] is True and core[key] is True for key in FLAGS)
    assert final["actual_pencil_rank"] == core["actual_pencil_rank"] == 1111
    parameter = final["accepted_integer_parameter"]
    assert parameter == core["accepted_integer_parameter"] and isinstance(parameter, int) and parameter >= 1
    for key in ("expanded_characteristic_zero_coordinates_computed", "Jacobian_standard_representative_computed", "actual_eta_or_height_computed"):
        assert final[key] is False
    assert final["old_Fourier_products_S5_inverse_and_Krylov_inverses_recomputed"] is False
    inventory = read(bound(out, final["stage_manifest"]))
    assert inventory["complete"] is True and inventory["configuration"] == tag and inventory["result"] == RESULT
    stages = {row["file"]: plain(row) for row in inventory["files"]}
    assert len(stages) == len(inventory["files"]) == final["complete_math_stage_count"]
    assert set(stages) == {name for name in entries if name.startswith("R839-pole-") and name.endswith(".json.gz") and name != MATH_INVENTORY}
    for name, row in stages.items():
        assert row == entries[name]
        value = read(bound(out, row))
        assert value["complete"] is True and value["configuration"] == tag and value["result"] == RESULT

    def stage(row):
        assert plain(row) == stages[row["file"]]
        return read(bound(out, row))

    def original(row):
        label = row["producer"]
        assert plain(row) == reviewed[label]["files"][row["file"]]

    audit = stage(final["source_audit"])
    assert audit["prime"] == 1000000753 and audit["all_690_original_tau_squared_product_recipes_verified"] is True
    assert audit["original_power3_and_power5_indices_identical"] is True
    assert audit["old_S5_and_Krylov_inverse_arithmetic_repeated"] is False
    for key in ("source_complete_original_D_basis", "source_original_S5_matrix", "source_original_S5_basis_index",
                "source_completed_same_prime_S5_inverse", "source_original_power5_basis_index",
                "source_original_power4_recipe", "source_original_power5_recipe", "source_original_unit_grid",
                "source_original_pencil"):
        original(audit[key])
    for row in audit["source_original_fixed_anchors"].values():
        original(row)
    normal = stage(final["V3_normal_index"])
    assert normal["dimension"] == 690 and normal["normal_basis_rank"] == 272
    assert normal["all690_rhs_and_all1380_equations_and_weighted_support_verified"] is True
    assert normal["same_prime_S5_inverse_recomputed"] is False
    assert len(normal["blocks"]) == 23
    for batch, row in enumerate(normal["blocks"]):
        value = stage(row)
        first, stop = 30*batch, min(690, 30*(batch+1))
        assert value["original_V3_indices"] == [first, stop]
        assert value["all1380_original_equations_verified"] is True and value["all_extra_weight5_coordinates_zero"] is True
        assert value["original_tau_squared_products_or_phase_conversion_recomputed"] is False
        assert value["source_original_alias_audit"] == final["source_audit"]
        assert value["original_source_integer_scale"] == "13744803133596058624"
        assert len(value["normal_coefficients_mod_prime"]) == 690
        assert all(len(line) == stop-first for line in value["normal_coefficients_mod_prime"])
        assert len(value["source_original_real_V5_rows"]) == stop-first
        for source in value["source_original_real_V5_rows"]:
            original(source)
    dag = stage(final["pole_ideal_DAG"])
    assert dag["integer_parameter"] == parameter
    assert dag["complete_original_D_ideal_certified"] is True and dag["complete_original_Ey_ideal_certified"] is True
    assert dag["both_original_affine_chart_trivializations_preserved"] is True
    assert dag["canonical_ideal_embedding_not_only_Picard_class"] is True
    assert dag["eight_source_bound_generators_supplied"] is True
    assert dag["unknown_scalar_or_new_cube_root_introduced"] is False
    assert dag["original_D_degree"] == 395 and dag["original_fixed_branch_degree"] == 21 and dag["original_Ey_degree"] == 1206
    assert dag["Ey_chart_denominator_degrees"] == {"tau": 11, "sigma": 11}
    expected_products = [{"fixed_anchor": anchor, "a_exponent": 3-j, "b_exponent": j, "homogeneous_degree": 11}
                         for anchor in ("u", "v") for j in range(4)]
    assert dag["Ey_homogeneous_generators"] == expected_products
    assert dag["accurate_ideal_identity"] == "I_Ey=I_fixed_branch*I_original_D^3"
    assert dag["D_chart_transition"] == "both generators multiply by t^3"
    assert dag["Ey_chart_transition"] == "all eight generators multiply by t^11"
    assert dag["existing_followup_identity"] == "I_EyR=(original_y^2-original_b)*I_Ey^3; requires the original global y DAG"
    for key in ("expanded_V11_generator_coordinates_computed", "real_descent_pole_ideal_expression_supplied",
                "original_y_global_function_supplied_by_this_consumer", "Jacobian_standard_representative_computed", "actual_eta_or_height_computed"):
        assert dag[key] is False
    candidate = stage(dag["source_candidate_sections"])
    assert candidate["integer_parameter"] == parameter and candidate["a_exact_D_basis_column"] == 0
    assert candidate["all_original_free_coordinates_verified"] is True and candidate["extra_rescaling_or_reconstruction_used"] is False
    assert len(candidate["a_original_V3_coordinates_mod_prime"]) == len(candidate["b_original_V3_coordinates_mod_prime"]) == 690
    rank = stage(dag["source_actual_pencil_rank"])
    assert rank["actual_rank"] == rank["required_rank"] == 1111 and rank["original_D_pencil_certified"] is True
    assert rank["integer_parameter"] == parameter and rank["source_candidate_sections"] == dag["source_candidate_sections"]
    assert rank["matrix_shape"] == [1360, 1380] and rank["actual_minor_determinant_mod_prime"] != 0
    assert len(set(rank["selected_original_fiber_rows"])) == 1111
    assert len(set(rank["selected_original_V3_pair_columns"])) == 1111
    assert rank["additional_common_zero_divisor_degree"] == 0
    assert rank["image_is_exactly_H0_6H_minus_original_D"] is True
    assert rank["no_injectivity_of_fiber_evaluation_or_disjointness_from_D_assumed"] is True
    assert len(rank["source_fiber_products"]) == 5
    for node, pair in zip(NODES, rank["source_fiber_products"]):
        assert pair["z0"] == node
        for which in ("a", "b"):
            product = stage(pair[which])
            assert product["which"] == which and product["z0"] == node and product["matrix_shape"] == [272, 690]
            assert product["old_Krylov_inverse_or_global_multiplication_table_recomputed"] is False
            assert product["fixed_a_product_independent_of_candidate_parameter"] is (which == "a")
            if which == "b":
                assert product["integer_parameter"] == parameter
                assert product["source_candidate_sections"] == dag["source_candidate_sections"]
            else:
                assert product["integer_parameter"] is None and product["a_exact_D_basis_column"] == 0
            original(product["source_original_Krylov_point"])
            evaluation = stage(product["source_original_fiber_evaluation"])
            assert evaluation["z0"] == node and evaluation["matrix_shape"] == [272, 690]
            assert evaluation["source_original_V3_normal_index"] == final["V3_normal_index"]
            assert evaluation["old_inverse_recomputed"] is False and evaluation["fiber_not_assumed_reduced_or_disjoint_from_D"] is True
    print("POLE_PENCIL_SUCCESS_IO_REVIEW="+json.dumps({
        "complete": True, "certificate": file_spec(out/FINAL), "stage_manifest": final["stage_manifest"],
        "actual_pencil_rank": 1111, "accepted_integer_parameter": parameter,
        "actual_minor_determinant_mod_prime": rank["actual_minor_determinant_mod_prime"],
        "complete_original_Ey_ideal_certified": True, "pole_ideal_DAG": final["pole_ideal_DAG"],
        "complete_math_stages": len(stages), "selected_original_files": item["selected_original_file_count"],
        "source_bundle": receipt["source_bundle"], "seconds": final["seconds"],
        "actual_eta_or_height_computed": False, "new_mathematics_executed_by_verifier": False}, sort_keys=True), flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("compute", "verify"))
    parser.add_argument("--request", type=Path, default=REQUEST)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    item = read(args.request)
    guard(item, args.request)
    if args.mode == "compute":
        return compute(item, args.out, args.request)
    return verify(item, args.out, args.request)


if __name__ == "__main__":
    raise SystemExit(main())

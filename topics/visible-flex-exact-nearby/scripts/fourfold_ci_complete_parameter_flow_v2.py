#!/usr/bin/env python3
"""Restore immutable completed blocks and execute the full true parameter flow.

This is orchestration only. No missing zero-order or parameter density is
sampled here. Original reports, primitive files, source SHAs and exact time
partitions are checked before the unchanged arithmetic validators are called.
The complete center and hybrid accumulators run sequentially and retain every
cross-segment Fourier term. The endpoint may reject the actual KAM gates;
that rejection and all completed preceding results remain in the artifact.

The first artifact request is authenticated to api.github.com. Its signed
redirect is fetched with a fresh request containing NO Authorization header.
"""
from __future__ import annotations

import argparse
import ast
from fractions import Fraction
import gc
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import time
import traceback
from types import SimpleNamespace
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import Request, build_opener, HTTPRedirectHandler, urlopen
import zipfile

REPOSITORY = "Rogerhu12/math-research"
BASE = Path("data/phase_ring_continuation")
DESCRIPTOR = BASE/"step5_retargeted_reference/descriptor.json"
COVER = BASE/"type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_forward.json.gz"
BLOCKS = BASE/"step5_ci_forward_blocks"
PREFIX = BASE/"step5_forward_density_prefix_checks/prefix0110/index.json"
PREFIX_SHA = "d08e5286abb48e84918d76f145e6e3f16da941675e3d65846e996ef9736b54eb"
DESCRIPTOR_SHA = "097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052"
COVER_SHA = "5cf017df6f91a1e5d29a6464a9c3fcf8b82586fda10f9c28fcbd14d218ca6271"
DELTA = Fraction(-7789843107295549, 4611686018427387904)
DENSITY_RUN = 43275872327
PARAMETER_RUN = 43290967141
ARTIFACTS = [
    (DENSITY_RUN, 55, 110, 13974148929, 51839953, "09cf877cfa1f5807b26d3eda06aa0b9cb02065b8ca231fd011aaf9e7826e2e9c"),
    (DENSITY_RUN, 110, 165, 13975492929, 46457442, "53a5c8bb55166b8a5d0aaae14243fb582146a25f47b3978db1eea3026e368d4a"),
    (DENSITY_RUN, 165, 220, 13973193003, 48542556, "3b623b2e006c84f85e05d2197fa8b763eaf510885779be64b5360ed5a8fb387f"),
    (DENSITY_RUN, 220, 275, 13973194259, 51902760, "9f5602379909801481090b32e74bd895e1bfed02e48c32400c45e1af1e3c3ce6"),
    (DENSITY_RUN, 275, 330, 13975781771, 60945927, "3c7ab872a25ba437d2d847b99a99c7cf91871e69b638f4103f2fa1ac37035757"),
    (DENSITY_RUN, 330, 385, 13976862226, 50793514, "ed8f4db5e9c6ea5523a11395b9a006bcb0d74d18ac7919bb03c33b6a08d3b1b0"),
    (DENSITY_RUN, 385, 440, 13976217276, 48416145, "adbbb0594ac663c95e54ca62bf15e926c8b4061b95357332b86e3a9ea60e2eff"),
    (DENSITY_RUN, 440, 495, 13975839366, 55724613, "45a118b1100c4c2bff2b33a5bb67014ded4d90defa5b5ed69aefdcf4f35fcd72"),
    (DENSITY_RUN, 495, 550, 13975398325, 45524063, "dd0373dc1f8364c9a07e47610bd8b8024669e068a49a9a78193984abbf13be42"),
    (PARAMETER_RUN, 32, 37, 13977077508, 3226322, "4fa981887e0fd401ee51b4f7cdb687a825513e466cf94662a1ef77b058fb3fb4"),
    (PARAMETER_RUN, 37, 42, 13976664693, 3196327, "5ca59dcbdab675ec7a22ff53fdd3c2b6b6b2435075cc082cac3944e594aa3a7a"),
    (PARAMETER_RUN, 42, 47, 13977865639, 3037405, "32b52b1925264a4b58af2bb29c39b66162a117f4be0f29a7e35ec3e417d56c69"),
    (PARAMETER_RUN, 47, 51, 13976144917, 2631010, "8ead697da84c732be258ba847cf0cd5f7d8bdad176e9304f49e92bdcd6fd5a74"),
    (PARAMETER_RUN, 51, 55, 13976894032, 2479352, "73cc733bbb96b5f11731d1a805837557dec6c00760d3b0ab37ec040155ecb25b"),
]
SOURCE_SHAS = {
    "fourfold_forward_density_cover_v9.py": "1451d5d434ef8fb4d7e0214e051afd185537ad75d882ddde6a82bf92d6a35ee1",
    "fourfold_forward_density_cover_v10.py": "cce56487c244a0f5823edc85835cbe9124c9df0f04afc1fa4117531f3db7c1ff",
    "fourfold_forward_density_pipeline_composition_v9.py": "42185f8a6d132593e9e930ceb6496af0e591750f7219a42767e5120a3b465a7b",
    "fourfold_parameter_density_pipeline_efficient_v5.py": "bee932df5c1d63860a900898cf0b9f288c49462361d08fbf0545bd900ff340fb",
    "fourfold_parameter_density_accumulate_v2.py": "2c8f3799bfb41b7cb8d5f44364bbf72ed44dc1fd8eb7e5d58f710c627f635f17",
    "fourfold_parameter_hybrid_accumulate_v3.py": "207f50be8fd05ab68715f617db2332908601a3312f913c4187028e381b5ff00a",
    "fourfold_actual_parameter_endpoint_kam_v2.py": "4d67186bc891279b668dd898baa3cb58d92e80342e995911e49416b4b6ca8c32",
}
ORIGINAL_INDEX = {
    "center": (BASE/"step5_parameter_session_unavailable_1849/center_index.json",
               "d9d93c2b9354aedc25a50956fc2c0351ae81dad8d9dd544b9a95122ed95ec693"),
    "uniform": (BASE/"step5_parameter_session_unavailable_1849/uniform_index.json",
                "089571e1d3ae43be95441ba74acbd26bee9dbc49c8395d9202fd1c99b8b8a6c5"),
}
NINE = Path("notes/2026-11-12-parameter-new-nine-leaves-ready-manifest.json")
NINE_SHA = "db1701d9547b87bf667019ab2da0c4eb01b7e128b6591740ac923196e9f6fe46"


def sha(path):
    with Path(path).open("rb") as stream:
        h = hashlib.sha256()
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, indent=2)+"\n").encode()
    if path.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    elif len(raw) > 1_000_000:
        raise ValueError("large report requires gzip: "+str(path))
    if len(raw) >= 5_000_000:
        raise ValueError("report exceeds the repository single-file limit: "+str(path))
    temporary = path.with_name(path.name+".tmp")
    temporary.write_bytes(raw)
    temporary.replace(path)


def checked(path, digest, size=None):
    path = Path(path)
    if not path.is_file() or sha(path) != digest:
        raise ValueError("saved file missing or SHA differs: "+str(path))
    if size is not None and path.stat().st_size != size:
        raise ValueError("saved file size differs: "+str(path))
    return path


def portable(value):
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or "\\" in value or "\n" in value:
        raise ValueError("nonportable artifact path")
    return path


def immutable_write(path, raw):
    path = Path(path)
    if path.exists():
        if path.read_bytes() != raw:
            raise ValueError("refuse to overwrite different saved bytes: "+str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".intake-tmp")
    temporary.write_bytes(raw)
    temporary.replace(path)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        return None


def download_artifact(artifact_id, expected_size, expected_sha, directory):
    destination = directory/("artifact-%d.zip" % artifact_id)
    if destination.exists():
        checked(destination, expected_sha, expected_size)
        return destination
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("the read-only Actions token is absent")
    endpoint = "https://api.github.com/repos/%s/actions/artifacts/%d/zip" % (REPOSITORY, artifact_id)
    request = Request(endpoint, headers={
        "Authorization": "Bearer "+token, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "visible-flex-complete-flow"})
    try:
        response = build_opener(NoRedirect).open(request, timeout=60)
    except HTTPError as exc:
        if exc.code not in (301, 302, 303, 307, 308):
            raise RuntimeError("GitHub artifact request failed with status %s" % exc.code) from None
        location = exc.headers.get("Location")
        if not location or urlparse(location).scheme != "https":
            raise ValueError("artifact redirect is absent or not HTTPS")
        # This request is intentionally new and has NO Authorization header.
        response = urlopen(Request(location, headers={"User-Agent": "visible-flex-complete-flow"}), timeout=180)
    temporary = destination.with_suffix(".zip.part")
    h = hashlib.sha256()
    size = 0
    with response, temporary.open("wb") as stream:
        for block in iter(lambda: response.read(1024*1024), b""):
            stream.write(block); h.update(block); size += len(block)
    if size != expected_size or h.hexdigest() != expected_sha:
        raise ValueError("downloaded artifact size or SHA differs; partial file retained")
    temporary.replace(destination)
    return destination




def existing_block_intake(spec, directory):
    """Reuse only a complete byte-checked repository closure, without a download.

    This does not claim to have rechecked the transport ZIP digest. The saved
    scientific files and original run/head/source identities are rechecked.
    The unchanged mathematical validators still run after this storage gate.
    """
    run, start, stop, artifact_id, size, digest = spec
    parameter = run == PARAMETER_RUN
    tag = ("ci_parameter_" if parameter else "ci_")+str(run)
    canonical = BLOCKS/tag/("block_%04d_%04d" % (start, stop))
    mp, ip = canonical/"block-manifest.json", canonical/"files.json"
    if not mp.is_file() or not ip.is_file():
        return None
    block, inventory = read(mp), read(ip)
    expected_head = ("2b9d63a5491082877bed47c4a28defe529630d69" if parameter
                     else "ebd02784509fd71b7bb041537a52fc30663d4411")
    if (not block.get("complete") or not block.get("complete_requested_g0_block")
        or not block.get("complete_center_and_uniform_g2_block")
        or block.get("requested_segment_interval") != [start, stop]
        or block.get("run_tag") != tag or block.get("source_commit") != expected_head
        or block.get("descriptor_sha256") != DESCRIPTOR_SHA
        or block.get("field_cover_sha256") != COVER_SHA
        or block.get("actual_R31_accepted") or block.get("full_forward_leg_claimed")
        or inventory.get("block_manifest_sha256") != sha(mp)):
        raise ValueError("saved block has a different complete source/run identity")
    worker_sources = {sha(p) for p in Path("scripts").glob("fourfold_ci_density_block*.py")}
    if block["source_sha256"] not in worker_sources:
        raise ValueError("saved completed worker source is absent")
    for label in ("g0", "parameter"):
        checked(block[label+"_pipeline_path"], block[label+"_pipeline_sha256"])
    seen, external, count = set(), 0, 0
    missing = []
    for row in inventory["files"]:
        path = Path(portable(row["path"]))
        if str(path) in seen:
            raise ValueError("saved block inventory duplicates a path")
        seen.add(str(path))
        try:
            path.relative_to(canonical)
        except ValueError:
            if not parameter or not inventory.get("external_read_only_inputs_preserve_original_paths"):
                raise ValueError("unexpected external saved block input")
            external += 1
        if not path.is_file():
            missing.append(str(path))
            continue
        checked(path, row["sha256"], row["bytes"])
        count += 1
    if missing:
        print("SAVED_BLOCK_MISSING_FILES", start, stop, len(missing), flush=True)
        return None
    evidence = dict(run=run, artifact_id=artifact_id,
        original_transport_artifact_sha256=digest, original_transport_artifact_bytes=size,
        transport_zip_not_downloaded=True, transport_zip_digest_not_rechecked=True,
        reused_checked_repository_closure=True, block_manifest_path=str(mp),
        block_manifest_sha256=sha(mp), inventory_path=str(ip),
        inventory_sha256=sha(ip), local_files=count-external,
        external_read_only_files=external, all_inventory_bytes_checked=True,
        original_paths_preserved=True, existing_mathematical_validator_still_required=True)
    save(directory/("artifact-%d-intake.json" % artifact_id), evidence)
    print("REUSED_CHECKED_BLOCK", run, start, stop, count, flush=True)
    return evidence

def intake(spec, directory):
    run, start, stop, artifact_id, size, digest = spec
    parameter = run == PARAMETER_RUN
    tag = ("ci_parameter_" if parameter else "ci_")+str(run)
    block_name = "block_%04d_%04d" % (start, stop)
    canonical = BLOCKS/tag/block_name
    existing = existing_block_intake(spec, directory)
    if existing is not None:
        return existing
    archive_path = None
    for attempt in range(12):
        try:
            archive_path = download_artifact(artifact_id, size, digest, directory)
            break
        except HTTPError as exc:
            # Respect ordinary retry/backoff; no alternate host or quota bypass.
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 11:
                raise
            retry_header = exc.headers.get("Retry-After", "")
            try:
                delay = max(15, min(60, int(retry_header)))
            except ValueError:
                delay = min(60, 15*(attempt+1))
            save(directory/("artifact-%d-retry-%02d.json" % (artifact_id, attempt+1)),
                dict(artifact_id=artifact_id, attempt=attempt+1,
                     http_status=exc.code, reason=str(exc.reason),
                     retry_after_seconds=delay, no_signed_url_or_token_recorded=True))
            print("ARTIFACT_BACKOFF", artifact_id, exc.code, delay, flush=True)
            time.sleep(delay)
    if archive_path is None:
        raise RuntimeError("artifact download exhausted bounded retries")
    with zipfile.ZipFile(archive_path) as archive:
        names = {}
        for item in archive.infolist():
            portable(item.filename)
            mode = (item.external_attr >> 16) & 0xFFFF
            if stat.S_ISLNK(mode):
                raise ValueError("artifact contains a symbolic link")
            if not item.is_dir():
                if item.filename in names:
                    raise ValueError("artifact duplicates a path")
                names[item.filename] = item
        manifests = [name for name in names if name.endswith(block_name+"/block-manifest.json")]
        if len(manifests) != 1:
            raise ValueError("artifact has no unique requested block manifest")
        member_manifest = PurePosixPath(manifests[0])
        prefix = member_manifest.parent
        member_files = str(prefix/"files.json")
        if member_files not in names:
            raise ValueError("completed block file inventory is absent")
        raw_manifest = archive.read(manifests[0])
        raw_inventory = archive.read(member_files)
        manifest, inventory = json.loads(raw_manifest), json.loads(raw_inventory)
        manifest_sha = hashlib.sha256(raw_manifest).hexdigest()
        expected_head = ("2b9d63a5491082877bed47c4a28defe529630d69" if parameter
                         else "ebd02784509fd71b7bb041537a52fc30663d4411")
        if (not manifest.get("complete") or not manifest.get("complete_requested_g0_block")
            or not manifest.get("complete_center_and_uniform_g2_block")
            or manifest.get("requested_segment_interval") != [start, stop]
            or manifest.get("run_tag") != tag
            or manifest.get("source_commit") != expected_head
            or manifest.get("descriptor_sha256") != DESCRIPTOR_SHA
            or manifest.get("field_cover_sha256") != COVER_SHA
            or manifest.get("actual_R31_accepted") or manifest.get("full_forward_leg_claimed")):
            raise ValueError("artifact is not the requested complete same-object partial block")
        if inventory.get("block_manifest_sha256") != manifest_sha:
            raise ValueError("artifact inventory binds another manifest")
        worker_sources = {sha(p) for p in Path("scripts").glob("fourfold_ci_density_block*.py")}
        if manifest["source_sha256"] not in worker_sources:
            raise ValueError("the original completed block worker source is absent")
        for label in ("g0", "parameter"):
            checked(manifest[label+"_pipeline_path"], manifest[label+"_pipeline_sha256"])
        seen, external, local = set(), [], []
        for row in inventory["files"]:
            target = portable(row["path"])
            if str(target) in seen:
                raise ValueError("artifact inventory duplicates a file")
            seen.add(str(target))
            try:
                relative = target.relative_to(PurePosixPath(str(canonical)))
            except ValueError:
                if not parameter or not inventory.get("external_read_only_inputs_preserve_original_paths"):
                    raise ValueError("unexpected external artifact inventory path")
                checked(target, row["sha256"], row["bytes"])
                external.append(row)
                continue
            member = str(prefix/relative)
            if member not in names:
                raise ValueError("an inventoried block file is missing from its artifact")
            raw = archive.read(member)
            if len(raw) != row["bytes"] or hashlib.sha256(raw).hexdigest() != row["sha256"]:
                raise ValueError("artifact file bytes differ from inventory")
            immutable_write(target, raw)
            local.append(row)
        immutable_write(canonical/"block-manifest.json", raw_manifest)
        # Its visibility is the commit point for read-only dynamic seed discovery.
        immutable_write(canonical/"files.json", raw_inventory)
        if parameter:
            proof_names = [name for name in names if name.endswith("ci-output/parameter-inputs-proof.json")]
            if len(proof_names) != 1:
                raise ValueError("selected parameter input proof is absent")
            proof_raw = archive.read(proof_names[0])
            proof = json.loads(proof_raw)
            if (not proof.get("complete") or proof.get("input_manifest_sha256")
                    != "05d303da37e984e003102390a1203fcc8f9512cb12d5bfb7e8165a95d44b9aa2"):
                raise ValueError("selected input proof names different immutable input")
            immutable_write(directory/("artifact-%d-input-proof.json" % artifact_id), proof_raw)
    evidence = dict(run=run, artifact_id=artifact_id, artifact_sha256=digest,
        artifact_bytes=size, block_manifest_path=str(canonical/"block-manifest.json"),
        block_manifest_sha256=manifest_sha, inventory_path=str(canonical/"files.json"),
        inventory_sha256=sha(canonical/"files.json"), local_files=len(local),
        external_read_only_files=len(external), all_inventory_bytes_checked=True,
        signed_download_had_no_authorization=True, original_paths_preserved=True)
    save(directory/("artifact-%d-intake.json" % artifact_id), evidence)
    # Only this now fully verified duplicate transport archive is removed.
    archive_path.unlink()
    print("INTAKEN", run, start, stop, len(local), len(external), flush=True)
    return evidence


def verify_sources():
    for name, digest in SOURCE_SHAS.items():
        checked(Path("scripts")/name, digest)
    v9 = ast.parse(Path("scripts/fourfold_forward_density_cover_v9.py").read_text())
    v10 = ast.parse(Path("scripts/fourfold_forward_density_cover_v10.py").read_text())
    def outside_main(tree):
        return [ast.dump(node, include_attributes=False) for node in tree.body
                if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) or node.name != "main"]
    if outside_main(v9) != outside_main(v10):
        raise ValueError("v10 changed a non-main arithmetic/source function")
    checked(DESCRIPTOR, DESCRIPTOR_SHA)
    checked(COVER, COVER_SHA)
    checked(PREFIX, PREFIX_SHA)
    for path, digest in ORIGINAL_INDEX.values():
        checked(path, digest)
    checked(NINE, NINE_SHA)


def run_child(command, log):
    log.parent.mkdir(parents=True, exist_ok=True)
    if log.exists():
        raise ValueError("refuse to replace an earlier execution log")
    print("RUN", command, flush=True)
    began = time.monotonic()
    with log.open("w") as stream:
        child = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1"))
        while child.poll() is None:
            time.sleep(20)
            print("CHILD_PROGRESS", log.name, int(time.monotonic()-began),
                  log.stat().st_size, flush=True)
    code = child.returncode
    print("CHILD_FINISHED", log.name, code, int(time.monotonic()-began), flush=True)
    if code:
        print(log.read_text(errors="replace")[-8000:], flush=True)
    return code


def key(row):
    return (int(row["segment"]), *map(Fraction, row["normalized_subspan"]))


def build_indices(out):
    from flint import ctx
    from fourfold_parameter_density_cover_efficient_v4 import validate_parameter_report
    from fourfold_phase_domain_cover_verify import Time
    from fourfold_completed_block_seeds import complete_inventory
    ctx.prec = 320
    g0_path = out/"g0/index.json.gz"
    g0 = read(g0_path)
    if (not g0.get("complete") or not g0.get("whole_forward_leg")
        or g0.get("completed_segments") != 550 or g0["descriptor_sha256"] != DESCRIPTOR_SHA):
        raise ValueError("only the complete same-object g0 selection may feed parameter accumulation")
    selected = {}
    for row in g0["leaves"]:
        k = key(row)
        if k in selected:
            raise ValueError("duplicate full zero-order selected leaf")
        checked(row["path"], row["sha256"])
        selected[k] = row
    descriptor = read(DESCRIPTOR)
    if Fraction(descriptor["target_exact_delta_fraction"]) != DELTA:
        raise ValueError("the exact target parameter differs")
    grid_meta = descriptor["old_forward_reference"]
    checked(grid_meta["path"], grid_meta["sha256"])
    grid = read(grid_meta["path"])
    if grid["segment_count"] != 550:
        raise ValueError("the full exact finite reference grid is absent")
    original = {scope: read(item[0]) for scope, item in ORIGINAL_INDEX.items()}
    old = {scope: {key(row): row for row in doc["leaves"] if int(row["segment"]) < 32}
           for scope, doc in original.items()}
    for item in read(NINE)["checks"]:
        if item["segment"] >= 32:
            continue
        report_path = checked(item["report"], item["sha256"])
        ref = read(report_path)["identity"]["reference"]
        k = key(ref)
        if k in old[item["scope"]]:
            raise ValueError("the immutable original prefix choice is duplicated")
        zero = selected[k]
        if zero["sha256"] != item["selected_g0_sha256"]:
            raise ValueError("the recovered parameter prefix uses another selected zero-order leaf")
        old[item["scope"]][k] = dict(path=str(report_path), sha256=item["sha256"],
            segment=k[0], normalized_subspan=list(map(str, k[1:])),
            g0_report_path=zero["path"], g0_report_sha256=zero["sha256"])
    manifests = [BLOCKS/"local_actual55/block_0055_0056/block-manifest.json"]
    for run, start, stop, *_ in ARTIFACTS:
        tag = ("ci_parameter_" if run == PARAMETER_RUN else "ci_")+str(run)
        manifests.append(BLOCKS/tag/("block_%04d_%04d" % (start, stop))/"block-manifest.json")
    blocks = []
    for path in manifests:
        doc = read(path)
        if (not doc.get("complete") or not doc.get("complete_requested_g0_block")
            or not doc.get("complete_center_and_uniform_g2_block")
            or doc["descriptor_sha256"] != DESCRIPTOR_SHA or doc["field_cover_sha256"] != COVER_SHA):
            raise ValueError("a selected parameter block is incomplete or has another object")
        inventory_path, entries = complete_inventory(path, sha(path))
        blocks.append((path, doc, sha(inventory_path), entries))
    versions = {}
    for path in Path("scripts").glob("fourfold_parameter_density_pipeline*.py"):
        versions[sha(path)] = path
    for scope, doc in original.items():
        for name, digest in doc["pipeline_sources"].items():
            # Only source paths are relocated; their original bytes are mandatory.
            checked(Path("scripts")/Path(name).name, digest)
    reports = {}
    for scope in ("center", "uniform"):
        eta = Fraction(0) if scope == "center" else Fraction(1, 10**9)
        args = SimpleNamespace(source_versions=versions, descriptor=DESCRIPTOR,
            uniform_half_width=eta, label_strip="1/256", inner_strip="3/1024",
            spatial_strip=Fraction(7, 2048))
        rows, provenance = [], []
        last = Time(Fraction(0), Fraction(-1, 2))
        for segment in range(550):
            keys = sorted(k for k in selected if k[0] == segment)
            if not keys or keys[0][1] != 0 or keys[-1][2] != 1:
                raise ValueError("the full zero-order partition has a gap")
            if any(a[2] != b[1] for a, b in zip(keys, keys[1:])):
                raise ValueError("the selected subspans do not meet")
            for k in keys:
                zero = selected[k]
                if segment < 32:
                    item = old[scope].get(k)
                    if item is None:
                        raise ValueError("a selected original parameter prefix leaf is absent")
                    path, digest = Path(item["path"]), item["sha256"]
                    evidence = dict(selection="original_pre32_parameter_choice",
                        source_index_path=str(ORIGINAL_INDEX[scope][0]),
                        source_index_sha256=ORIGINAL_INDEX[scope][1])
                else:
                    wanted_tag = ("ci_parameter_"+str(PARAMETER_RUN) if segment < 55
                                  else "local_actual55" if segment == 55
                                  else "ci_"+str(DENSITY_RUN))
                    matches = []
                    for manifest_path, block, invsha, inventory in blocks:
                        if block["run_tag"] != wanted_tag:
                            continue
                        for item in block["leaves"]:
                            if key(item) == k and item["g0_report_sha256"] == zero["sha256"]:
                                matches.append((manifest_path, block, invsha, inventory, item))
                    if len(matches) != 1:
                        raise ValueError("no unique completed same-g0 parameter leaf: "+str((scope, k)))
                    manifest_path, block, invsha, inventory, item = matches[0]
                    path, digest = Path(item[scope+"_report_path"]), item[scope+"_report_sha256"]
                    if inventory.get(str(path)) != digest:
                        raise ValueError("parameter report is absent from the completed inventory")
                    evidence = dict(selection=wanted_tag,
                        block_manifest_path=str(manifest_path),
                        block_manifest_sha256=sha(manifest_path),
                        file_inventory_sha256=invsha)
                checked(path, digest)
                report, zero_report = validate_parameter_report(path, Path(zero["path"]), args, k)
                for name, wanted in report["dependency_sha256"].items():
                    checked(Path("scripts")/Path(name).name, wanted)
                begin, end = map(Time.parse, grid["exact_time_endpoints"][segment:segment+2])
                ta, tb = begin+(end-begin).scale(k[1]), begin+(end-begin).scale(k[2])
                if ta != last:
                    raise ValueError("the actual parameter chronology has a time gap")
                last = tb
                rows.append(dict(path=str(path), sha256=digest, bytes=path.stat().st_size,
                    segment=segment, normalized_subspan=list(map(str, k[1:])),
                    g0_report_path=zero["path"], g0_report_sha256=zero["sha256"],
                    immutable_selection=evidence))
                if len(rows) % 40 == 0:
                    print("VALIDATED_PARAMETER_INPUTS", scope, len(rows), flush=True)
        if last != Time(Fraction(0), Fraction(1, 2)) or len(rows) != len(selected):
            raise ValueError("the actual parameter sources are not a complete forward leg")
        doc = dict(kind="actual_complete_forward_parameter_density_inputs", complete=True,
            source_sha256=sha(__file__), descriptor_sha256=DESCRIPTOR_SHA,
            g0_index_path=str(g0_path), g0_index_sha256=sha(g0_path),
            pipeline_sources={str(path): digest for digest, path in versions.items()},
            required_parameter_orders=[1, 2] if scope == "center" else [2],
            exact_target_delta_fraction=str(DELTA), uniform_parameter_half_width=str(eta),
            whole_real_parameter_tube=bool(eta), label_strip="1/256",
            inner_strip="3/1024", spatial_strip="7/2048", completed_segments=550,
            whole_forward_leg=True, exact_begin=dict(rational="0", pi_coefficient="-1/2"),
            exact_final_time=dict(rational="0", pi_coefficient="1/2"), leaves=rows,
            original_mathematical_validator_applied_to_every_leaf=True,
            zero_order_resampled=False, parameter_sources_resampled=False,
            g0_g1_uniform_control_requires_hybrid_center_mean_value_transfer=bool(eta),
            no_chronological_or_endpoint_conclusion_from_index_alone=True)
        report_path = out/(scope+"_index.json.gz")
        save(report_path, doc)
        reports[scope] = dict(path=str(report_path), sha256=sha(report_path),
                              completed_segments=550, completed_leaves=len(rows))
        del rows
        gc.collect()
    save(out/"parameter-input-selection.json", dict(complete=True, reports=reports,
        source_sha256=sha(__file__), g0_index_sha256=sha(g0_path)))


def full(out, downloads):
    verify_sources()
    out.mkdir(parents=True, exist_ok=True)
    downloads.mkdir(parents=True, exist_ok=True)
    state = dict(kind="actual_complete_parameter_flow_execution", complete=False,
        source_sha256=sha(__file__), source_commit=os.environ.get("GITHUB_SHA"),
        descriptor_sha256=DESCRIPTOR_SHA, exact_target_delta_fraction=str(DELTA),
        actual_R31_accepted=False, zero_order_resampled=False,
        parameter_sources_resampled=False, stages=[], artifact_intakes=[])
    state_path = out/"execution.json"
    save(state_path, state)
    try:
        for spec in ARTIFACTS:
            state["artifact_intakes"].append(intake(spec, downloads))
            save(state_path, state)
        g0dir = out/"g0"
        g0dir.mkdir(exist_ok=True)
        immutable_write(g0dir/"index.json", PREFIX.read_bytes())
        commands = [
            ("g0", [sys.executable, "-u", "scripts/fourfold_forward_density_cover_v10.py",
                "--out-directory", str(g0dir), "--primitive-nodes", "640",
                "--root-nodes", "1024", "--turn-primitive-nodes", "512",
                "--turn-root-nodes", "512", "--seed-only-from", "110", "--follow"]),
            ("parameter-input-selection", [sys.executable, "-u", __file__,
                "--stage", "indices", "--out-directory", str(out)]),
            ("center-chronological", [sys.executable, "-u",
                "scripts/fourfold_parameter_density_accumulate_v2.py",
                "--index", str(out/"center_index.json.gz"),
                "--directory", str(out/"center_chronological")]),
            ("hybrid-chronological", [sys.executable, "-u",
                "scripts/fourfold_parameter_hybrid_accumulate_v3.py",
                "--center-index", str(out/"center_index.json.gz"),
                "--uniform-index", str(out/"uniform_index.json.gz"),
                "--directory", str(out/"hybrid_chronological")]),
            ("actual-endpoint", [sys.executable, "-u",
                "scripts/fourfold_actual_parameter_endpoint_kam_v2.py",
                "--center", str(out/"center_chronological/report.json.gz"),
                "--uniform", str(out/"hybrid_chronological/report.json.gz"),
                "--half-outer-width", "5/2048", "--half-derivative-width", "9/4096",
                "--full-width", "1/512", "--kam-start-width", "3/2048",
                "--kam-width-step", "1/4096", "--inverse-radius", "1/1000",
                "--bits", "320", "--out", str(out/"actual_endpoint.json.gz")]),
        ]
        for stage, command in commands:
            state["current_stage"] = stage
            save(state_path, state)
            code = run_child(command, out/"logs"/(stage+".log"))
            state["stages"].append(dict(stage=stage, command=command, returncode=code))
            save(state_path, state)
            if code:
                raise RuntimeError("actual stage rejected or failed: "+stage)
        endpoint = read(out/"actual_endpoint.json.gz")
        state["actual_R31_accepted"] = bool(endpoint.get("actual_R31_accepted"))
        state["complete"] = True
        state["endpoint_path"] = str(out/"actual_endpoint.json.gz")
        state["endpoint_sha256"] = sha(out/"actual_endpoint.json.gz")
    except Exception as exc:
        state["failure"] = type(exc).__name__+": "+str(exc)
        state["traceback"] = traceback.format_exc()
        print(state["failure"], flush=True)
        print(state["traceback"], flush=True)
    save(state_path, state)
    rows = [dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)
            for path in sorted(out.rglob("*")) if path.is_file() and path.name != "files.json.gz"]
    save(out/"files.json.gz", dict(kind="complete_or_failed_flow_output_inventory",
        execution_sha256=sha(state_path), files=rows,
        imported_input_artifacts_remain_available_by_recorded_run_and_SHA=True))
    return 0 if state["actual_R31_accepted"] else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=("full", "indices"), default="full")
    parser.add_argument("--out-directory", type=Path, required=True)
    parser.add_argument("--download-directory", type=Path, default=Path("ci-output/complete-flow-intake"))
    args = parser.parse_args()
    if args.stage == "indices":
        verify_sources()
        build_indices(args.out_directory)
        return 0
    return full(args.out_directory, args.download_directory)


if __name__ == "__main__":
    raise SystemExit(main())

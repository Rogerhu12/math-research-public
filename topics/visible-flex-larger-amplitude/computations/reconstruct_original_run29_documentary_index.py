#!/usr/bin/env python3
"""Regenerate both immutable documentary Markdown files for original run 46110194444/1.
From a partial repository checkout, pass an empty scratch directory as argv[1].
The original renderer was public_actions_controller_parallel29_geometry_locations.py
at 259814e67c1435016353a70bb9e9b7d7b2a8c7e7, 19995 bytes, SHA-256
0ab835efc215f21291c10d1cec24a29460419d0f9e71e1b9db69e2a05ee3df01.
This metadata reconstruction does not rerun the scientific input or read any raw log.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

TOPIC = "topics/visible-flex-larger-amplitude"
FIXED = "409235e12cb7b77b526ab6e34c864b63297b3684"
TRIGGER = "259814e67c1435016353a70bb9e9b7d7b2a8c7e7"
STAGE = "prepare-complete-fixed-fejer-r690-inputs-20261127"


def original(commit, path, size, digest):
    data = subprocess.check_output(["git", "show", commit+":"+TOPIC+"/"+path])
    if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
        raise RuntimeError("historical documentary source differs: "+path)
    return data.decode("utf-8")


def save(out, name, text, size, digest):
    data = text.encode("utf-8")
    if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
        raise RuntimeError("complete Markdown regeneration differs: "+name)
    with (out/name).open("xb") as stream:
        stream.write(data)


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    request = original(TRIGGER, "computations/resume-20261128-actions-request-29.json",
                       40193, "473b5ff5c7af82fa6ef3611c7134b9255bc03f443c518ae76594a0b3830479c2")
    own = original(FIXED, "notes/2026-11-28-run29-complete-r726-spherical-launch-and-continuation.md",
                   73361, "637477bc6a46a87c55344221d9a8a2ed784c10077428ec4da507416cb0a78d20")
    blocks = [json.loads(m) for m in re.findall(r"(?ms)^```json\n(.*?)^```$", own)]
    records = next(b["complete_original_events"] for b in blocks
                   if isinstance(b,dict) and "complete_original_events" in b)
    event = next(r["complete_original_event"] for r in records
                 if r["complete_original_event"].get("event") == "followup_returned"
                 and r["complete_original_event"].get("step_id") == STAGE)
    # Only the seven fields absent from the existing returned event are literal.
    residual = json.loads(r'''{"name":"followup:prepare-complete-fixed-fejer-r690-inputs-20261127","scope":"Necessary complete deterministic new mathematical input. Restore the exact accepted099 scalar-parameter source; extract the whole e640 projection; construct the fixed seven-mode RN-even Fejer chart, all 923 exact affine nodes and complete FullHold node/radius error ledger. No warm/BVP/pulse field, old core, old final, F/J/normal root or geometric certificate is used. This is a new fixed target; original branches and old literal-address provenance are retained explicitly.","input_files":[{"role":"source","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py","commit":"14fa94bbaac9dafaa6b7be3d06a32d940a8c1f04","sha256":"89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"},{"role":"followup_queue","path":"topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-29.json","path_commit":"259814e67c1435016353a70bb9e9b7d7b2a8c7e7","checkout_commit":"14fa94bbaac9dafaa6b7be3d06a32d940a8c1f04","sha256":"e16b8d782febeb5e0b70840b925003fdc6524ee6595f29b3fb1e9807a5dd717a"}],"command":["/opt/hostedtoolcache/Python/3.12.14/x64/bin/python","-u","/home/runner/work/_temp/visible-larger-research-46110194444-1/followup-sources/0001-167d7c1a5813-14fa94bbaac9/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py","--repo","/home/runner/work/_temp/visible-larger-research-46110194444-1/followup-sources/0001-167d7c1a5813-14fa94bbaac9","--outdir","/home/runner/work/_temp/visible-larger-research-46110194444-1/research/fixed-fejer-r690-inputs","--panels","128"],"cleanup_generated":{"deleted":{"record_count":0,"recorded_bytes":0,"records_with_bytes":0,"listed_file_count":0,"records_with_file_lists":0,"canonical_metadata_bytes":2,"canonical_metadata_sha256":"4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945","canonicalization":"UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False","detail_scope":"Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"},"skipped":{"record_count":0,"recorded_bytes":0,"records_with_bytes":0,"listed_file_count":0,"records_with_file_lists":0,"canonical_metadata_bytes":2,"canonical_metadata_sha256":"4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945","canonicalization":"UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False","detail_scope":"Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"},"scope":"Only explicit patterns, newly generated regular caches and an already returned child; never parent/input/output files"},"summary_errors":[],"missing_outputs":[]}''')
    order = ["name","state","returncode","seconds","scope","metrics","outputs","input_files","source_commit","source_sha256","command","cleanup_generated","step_id","summary_errors","missing_outputs"]
    stage = {k:residual[k] if k in residual else event[k] for k in order}
    part = "# 公开Actions 46110194444/1：实际阶段 1–1\n\n[运行](https://github.com/Rogerhu12/math-research-public/actions/runs/46110194444)；[总索引](2026-11-28-public-actions-46110194444-1.md)。\n\n本卷完整保留这些实际阶段的紧凑输入/源码/参数/输出身份，不存科学数组或逐点报告。\n\n## 1. followup:prepare-complete-fixed-fejer-r690-inputs-20261127\n\n```json\n" + json.dumps(stage, ensure_ascii=False, indent=2) + "\n" + "```\n\n"
    index = "# 公开Actions实际运行 46110194444/1\n\n状态记录时间：2026-11-28 05:02:35 UTC。本记录由分卷控制器在真实公开Actions生成。\n\n- 运行：[GitHub Actions 46110194444](https://github.com/Rogerhu12/math-research-public/actions/runs/46110194444)。\n- 请求：`visible-larger-resume-20261128-29`；请求文件SHA256 `473b5ff5c7af82fa6ef3611c7134b9255bc03f443c518ae76594a0b3830479c2`。\n- 初始执行源码提交：`259814e67c1435016353a70bb9e9b7d7b2a8c7e7`；控制器实际加载SHA256 `0ab835efc215f21291c10d1cec24a29460419d0f9e71e1b9db69e2a05ee3df01`。\n- 当前阶段：`followup:prepare-complete-fixed-fejer-r690-inputs-20261127`；阶段状态：`completed`。\n- 实际子进程退出码：`0`。\n\n每项实际输入、完整命令、源码与输出SHA及紧凑数值完整保存在下列分卷。所有科学数组、逐点/逐胞报告和完整日志只留runner；输入重建不重复宣告旧科学结论。\n\n## 已实际返回的阶段与分卷\n\n- [第1卷：阶段1–1](2026-11-28-public-actions-46110194444-1-part-001.md)。\n\n| 阶段 | 实际状态 | 退出码 |\n|---|---|---|\n| 1. followup:prepare-complete-fixed-fejer-r690-inputs-20261127 | completed | 0 |\n\n## 完整可复现请求\n\n```json\n" + request + "```\n\n科学完成标准仍是本题README的全域度量、全t几何和固定参数实际精化；单步或本job退出不构成研究完成。\n"
    save(out, "2026-11-28-public-actions-46110194444-1-part-001.md", part, 5751, "f3da5281438902016474d99afa41ba496ba8f779b769f8159e926f12fa49f61a")
    save(out, "2026-11-28-public-actions-46110194444-1.md", index, 41570, "2f20ac1c148fa255ad17c303e70de0a36eb870ea3fec68ad0d8736ddfad13b12")


if __name__ == "__main__":
    main(Path(sys.argv[1]))

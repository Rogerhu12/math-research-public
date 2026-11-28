#!/usr/bin/env python3
"""Freeze one already returned original R87 design stage as a small note.

This reads the genuine raw/physical files and applies the unchanged original
acceptance checks. It never runs a BVP, a predictor, or a Jacobian. No numerical
array is copied to the repository. A live outer journal is represented by its
one actual command line, never by a purported final whole-journal digest.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--controller-out", type=Path, required=True)
    p.add_argument("--stage", required=True)
    p.add_argument("--label", required=True)
    p.add_argument("--expect", choices=("accepted", "metric-only"), required=True)
    a = p.parse_args()
    if not a.stage.startswith("attempt-") or "/" in a.stage or "/" in a.label:
        raise ValueError("Require one explicit local stage and note label")
    topic = a.repo.resolve()/"topics/visible-flex-held-10pct"
    sys.path.insert(0, str(topic/"scripts/resume_20261126"))
    from material_design_secant_predictor import accepted_original
    from material_design_continue import original_finite_checks, complete_initializer
    out = a.controller_out.resolve()
    run = out/a.stage/"run.json"
    r = json.loads(run.read_text())
    checks = original_finite_checks(r)
    complete = complete_initializer(run, r)
    metric = r.get("prefix_audit", {}).get("metric_l1")
    if a.expect == "accepted":
        r, _ = accepted_original(run, a.repo)
    elif not (checks["solver_and_boundary_pass"] and complete and
              isinstance(metric, (int,float)) and metric > 1e-6):
        raise ValueError("This is not a true original metric-only return")
    for group in ("source_hashes", "inputs"):
        for file, expected in r[group].items():
            if sha(file) != expected:
                raise ValueError("A real source/input changed: "+file)
    current = json.loads((out/"summary.json").read_text())
    row, = [x for x in current["stages"] if x["name"] == a.stage]
    accepted = a.expect == "accepted"
    if (row["run_sha256"] != sha(run) or row["returncode"] != 0 or
            row["accepted"] is not accepted):
        raise ValueError("The genuine joined stage and requested classification differ")
    trace = out.with_name(out.name+"-dispatch-execution.jsonl")
    commands = []
    for line in trace.read_bytes().splitlines(keepends=True):
        item = json.loads(line)
        command = item.get("executed", [])
        if (item.get("event") == "subprocess" and "--outdir" in command and
                Path(command[command.index("--outdir")+1]).resolve() == run.parent):
            commands.append(dict(trace_path=str(trace), actual_record=item,
                exact_line_including_newline_sha256=hashlib.sha256(line).hexdigest()))
    if len(commands) != 1:
        raise ValueError("Require the one original executed command")
    qr = out/(a.stage+"-block-qr.jsonl")
    qrrows = [json.loads(x) for x in qr.read_text().splitlines()]
    if qrrows[-1]["event"] != "driver_return_or_exception":
        raise ValueError("The complete original QR wrapper has not returned")
    transfers = {}
    for kind in ("transfer", "secant", "cross-mode-secant"):
        directory = out/(a.stage+"-"+kind)
        if directory.is_dir():
            for name in ("transfer.json", "predictor.json"):
                file = directory/name
                if file.is_file():
                    transfers[kind] = dict(path=str(file), sha256=sha(file),
                                            record=json.loads(file.read_text()))
    record = dict(kind="actual_original_R87_single_gentle_finite_stage",
        classification=a.expect, accepted=accepted,
        serializer_source_sha256=sha(__file__),
        accepted_original_validator_passed=accepted,
        validator_source_sha256=sha(topic/"scripts/resume_20261126/material_design_secant_predictor.py"),
        run=str(run), run_sha256=sha(run), actual_executed_command=commands[0],
        original_stage_row=row, original_sources=r["source_hashes"],
        original_inputs=r["inputs"], original_finite_checks=checks,
        complete_saved_initializer=complete, physical_profile=r["physical_profile"],
        frozen_profile=r["frozen_profile"], core_settings=r["core_settings"],
        modes=r["modes"], angular=r["angular"], gauge_q=r["gauge_q"],
        warp_reference=r["warp_reference"], original_gates=r["gates"],
        raw_return=r["raw_return"], physical_sha256=r["physical_sha256"],
        prefix_audit=r["prefix_audit"], original_mean_floor=16*(3*r["modes"]+1),
        domain_newton_stats=r["domain_newton_stats"],
        domain_error_counts=r["domain_error_counts"], seconds=r["seconds"],
        complete_QR=dict(trace=str(qr), sha256=sha(qr),
            factors=sum(x["event"] == "factor_return" for x in qrrows),
            last_return=qrrows[-1]),
        actual_initializer_records=transfers,
        all_original_raw_physical_source_input_gates_retained=True,
        full_nonlinear_DN_paid=False, same_g_refinement=False,
        source_parameters_at_lambda_one=(r["core_settings"]["homotopy"] == 1),
        rigorous_geometry=False, complete_surface=False)
    name = "2026-11-28-design-single-gentle-"+a.label+"-"+(
        "actual" if accepted else "metric")
    js = topic/"notes"/(name+".json")
    md = js.with_suffix(".md")
    if js.exists() or md.exists():
        raise FileExistsError("A previously frozen note will never be overwritten")
    audit, raw, stats = r["prefix_audit"], r["raw_return"], r["domain_newton_stats"]
    title = "原完整有限门接受" if accepted else "仅原 metric 门未过"
    finding = ("通过未修改的 accepted_original：完整来源、raw/physical SHA、所有状态和参数形状、"
        "cubic、原 RMS/BC/metric 及实际 mean 均核过。"
        if accepted else "原 solver、RMS、物理 BC 及完整文件门通过，metric 大于1e−6，未接受；不是数学不存在。")
    text = f"""# R87 新剖面 λ={r['core_settings']['homotopy']} / M={r['modes']}：{title}

2026-11-28，/root/design_continuation。{finding}

| 原量 | 实际值 |
|---|---:|
| 模态 / 求解角点 | {r['modes']} / {r['angular']} |
| 节点 | {raw['nodes']} |
| RMS | {raw['rms']:.17g} |
| metric L1 | {audit['metric_l1']:.17g} |
| physical BC | {audit['physical_bc_max']:.17g} |
| 实际 audit mean / 原下限 | {audit['samples_psi']} / {16*(3*r['modes']+1)} |
| 实际 δ | {r['frozen_profile']['delta']:.17g} |
| 原 BVP 加 audit 秒 | {r['seconds']:.17g} |
| 完整 QR 次数 | {record['complete_QR']['factors']} |
| 原接受步 / merit拒 / 域拒 | {stats['accepted_steps']} / {stats['rejected_merit_trials']} / {stats['rejected_domain_trials']} |
| QR driver 核计最大 RSS KiB | {qrrows[-1]['maximum_rss_kib']} |

q=warp=.012，仍是同一新单级温和剖面。原门为 RMS≤1e−6、metric≤1e−6、
physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000，全部状态、支撑列、δ列及
原域、线搜索和 mesh 规则均保留。预测或升模所得完整场都只是未接受初猜。

实际目录：{run.parent}。

| 输出 | SHA-256 |
|---|---|
| run.json | {sha(run)} |
| 完整 raw | {raw['sha256']} |
| physical.npz | {r['physical_sha256']} |

[同名实际 JSON]({js.name})记录来源、实际命令单行字节 SHA、所有原门、实际初猜
来源及完整 QR 小摘要。仍在增长的外层日志没有被冒称冻结，数组未入 Git。

本条是有限线性-port 数值返回。实际非线性 DN、同一最终 g 的精化、连续全域
几何、闭合和 README 完成标准尚未由本条支付；控制器继续后继实际计算。
"""
    js.write_text(json.dumps(record, indent=2, allow_nan=False)+"\n")
    md.write_text(text.rstrip()+"\n")
    print(json.dumps(dict(json=str(js),json_sha256=sha(js),json_bytes=js.stat().st_size,
        md=str(md),md_sha256=sha(md),classification=a.expect,
        lambda_value=r["core_settings"]["homotopy"],modes=r["modes"],
        metric=audit["metric_l1"],RMS=raw["rms"],physical_BC=audit["physical_bc_max"],
        seconds=r["seconds"],peakRSS_KiB=qrrows[-1]["maximum_rss_kib"]),
        allow_nan=False))


if __name__ == "__main__":
    main()

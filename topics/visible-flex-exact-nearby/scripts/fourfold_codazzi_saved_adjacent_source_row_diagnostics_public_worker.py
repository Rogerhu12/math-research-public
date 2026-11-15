#!/usr/bin/env python3
"""Public saved-row diagnosis with only provenance and conclusions persisted."""
from __future__ import annotations
import argparse,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_saved_adjacent_source_row_diagnostics.py"
REPORTS=TOPIC/"notes/saved_adjacent_source_row_diagnostics_ci"
SUMMARY="complete-correlated-adjacent-source-row-diagnostics-summary.json"
DETAIL="smallest-radius-dominant-source-rows.json"
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def save(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".partial")
    t.write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+"\n");t.replace(p)
def checked(p,size,digest):
    p=Path(p)
    if not p.is_file() or p.stat().st_size!=size or sha(p)!=digest:
        raise ValueError("a complete pinned input differs: "+str(p))
def read(p):return json.loads(Path(p).read_text())
def relpath(p):
    p=Path(p)
    if p.is_absolute() or ".." in p.parts or not str(p).startswith(str(TOPIC)+"/"):
        raise ValueError("an input left the authorized topic")
    return p
def rec(p,base):
    p=Path(p);return dict(file=str(p.relative_to(base)),bytes=p.stat().st_size,sha256=sha(p))
def ball(v):
    if isinstance(v,dict):
        if isinstance(v.get("ball"),str):return v["ball"]
        if "upper" in v:return str(v["upper"])
        return json.dumps(v,ensure_ascii=False,separators=(",",":"))
    return str(v)
def cell(v):return str(v).replace("|","\\|").replace("\n"," ")

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mode",choices=("hydrate","run"),required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--pipeline-sha",required=True)
    p.add_argument("--rules",type=Path,required=True)
    p.add_argument("--rules-sha",required=True)
    p.add_argument("--work",type=Path);p.add_argument("--prepared",type=Path);p.add_argument("--out-dir",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("only the public repository Actions may consume the scientific inputs")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:raise ValueError("separate execution pins changed")
    m=read(a.manifest);rules=read(a.rules)
    if m["public_repository"]!=PUBLIC or rules["repository"]!=PUBLIC:raise ValueError("wrong public repository")
    for k in ("reproducible_data_persisted_in_repository","reproducible_data_persisted_in_Releases","new_reproducible_Actions_output_uploads"):
        if rules["large_data_policy"].get(k) is not False:raise ValueError("latest no-data rule15 is required")
    rm=a.manifest.relative_to(root);rr=a.rules.relative_to(root);rw=Path(__file__).resolve().relative_to(root)
    gb=["git","-c","safe.directory="+str(root)]
    if a.mode=="hydrate":
        paths={str(PIPELINE),str(rw),str(rm),str(rr),str(REPORTS)+"/"}|set(rules["readme_sha256"])
        subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
            input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
        print("Hydrated scripts, parameters, reviewed READMEs and small earlier conclusions only.",flush=True);return
    if a.work is None or a.prepared is None or a.out_dir is None:raise ValueError("temporary work paths are required")
    work=a.work.resolve();out=a.out_dir.resolve();prepared=a.prepared.resolve()
    if work.exists() or out.exists():raise FileExistsError("preserve an existing actual execution")
    if any(v.is_relative_to(root) for v in (work,out,prepared)):raise ValueError("reproducible data must stay outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True);ws=sha(__file__)
    state=dict(kind="actual_public_saved_source_row_diagnostic_execution",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        diagnostic_source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_diagnostic_processes=0,old_numerical_enclosures_recomputed=0,
        reproducible_data_published_to_repository=False,reproducible_data_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False,new_operator_norm_claimed=False,final_topic_complete=False)
    env=os.environ.copy();token=env.pop("GITHUB_TOKEN")
    env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="1",
        GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
        GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+token).encode()).decode())
    def git(*args,check=True,stdout=None):
        r=subprocess.run(gb+list(args),cwd=root,env=env,text=stdout is None,
            stdout=subprocess.PIPE if stdout is None else stdout,stderr=subprocess.PIPE,timeout=900)
        if check and r.returncode:
            e=r.stderr if isinstance(r.stderr,str) else r.stderr.decode("utf-8","replace")
            raise RuntimeError("public Git "+str(args[0])+" failed: "+e[:1200])
        return r
    def sync():
        before=git("rev-parse","HEAD").stdout.strip();git("pull","--rebase","origin","main")
        after=git("rev-parse","origin/main").stdout.strip()
        diff=git("diff",before,after,"--",*rules["readme_sha256"]).stdout
        state["readme_checks"].append(dict(time=utc(),before=before,after=after,actual_diff=diff,
            explicitly_reviewed_commit=rules["read_commit"]))
        save(out/"worker-process.json",state)
        for path,digest in rules["readme_sha256"].items():
            if sha(root/path)!=digest:
                print(diff,flush=True);raise RuntimeError("read and apply the newly changed README diff")
        if sha(a.rules)!=a.rules_sha or sha(a.manifest)!=a.manifest_sha or sha(root/PIPELINE)!=a.pipeline_sha:
            raise ValueError("the separately pinned execution contract changed during pull")
        if sha(root/rw)!=ws:raise ValueError("the running wrapper changed during pull")
    git("config","user.name","github-actions[bot]")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com");sync()
    for old in sorted((root/REPORTS).glob("*/execution.json")):
        v=read(old)
        if v.get("complete") is True and v.get("input_manifest_sha256")==a.manifest_sha and v.get("diagnostic_source_sha256")==a.pipeline_sha:
            print(json.dumps(dict(reused_existing_complete_conclusion=str(old.relative_to(root)),
                original_run_id=v["run_id"],new_diagnostic_processes=0,new_numerical_enclosures=0)),flush=True);return
    hist=m["historical_input_commit"]
    if len(hist)!=40 or any(c not in "0123456789abcdef" for c in hist):raise ValueError("the input commit is not immutable")
    git("fetch","--filter=blob:none","--no-tags","origin",hist)
    state["historical_input_commit"]=hist;state["input_receipts"]=[]
    external={v["path"]:v for v in m["external_original_inputs"]}
    for e in m["files"]:
        rel=relpath(e["path"]);dst=work/rel;dst.parent.mkdir(parents=True,exist_ok=True)
        if str(rel) in external:
            spec=external[str(rel)];src=prepared/spec["artifact_relative_path"]
            checked(src,e["bytes"],e["sha256"]);shutil.copyfile(src,dst)
            origin=dict(kind="original_complete_Actions_artifact",run_id=spec["artifact_run_id"],
                artifact_id=spec["artifact_id"],artifact_relative_path=spec["artifact_relative_path"])
        elif (root/rel).is_file():
            checked(root/rel,e["bytes"],e["sha256"]);shutil.copyfile(root/rel,dst)
            origin=dict(kind="exact_current_text_input")
        else:
            with dst.open("wb") as stream:git("show",hist+":"+str(rel),stdout=stream)
            origin=dict(kind="exact_public_historical_blob",commit=hist)
        checked(dst,e["bytes"],e["sha256"])
        state["input_receipts"].append(dict(path=str(rel),bytes=e["bytes"],sha256=e["sha256"],origin=origin))
    tm=work/rm;tm.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.manifest,tm)
    checked(work/PIPELINE,next(e["bytes"] for e in m["files"] if e["path"]==str(PIPELINE)),a.pipeline_sha)
    cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),"--manifest",str(tm),
        "--manifest-sha",a.manifest_sha,"--out-dir",str(out/"consumers")]
    state["command"]=cmd;state["actual_scientific_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
    state["actual_diagnostic_processes"]=1;save(out/"worker-process.json",state)
    ce=os.environ.copy();ce.pop("GITHUB_TOKEN",None);ce["VISIBLE_PHASE_SCIENCE_COMMIT"]=state["actual_scientific_checkout_commit"]
    started=time.monotonic()
    with (out/"diagnostic.stdout.log").open("wb") as log:
        child=subprocess.Popen(cmd,cwd=work,env=ce,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        try:child.wait(timeout=3000)
        except subprocess.TimeoutExpired:
            state["timeout_seconds"]=3000;os.killpg(child.pid,signal.SIGTERM)
            try:child.wait(timeout=10)
            except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
        state["actual_returncode"]=child.returncode
    state["diagnostic_child_wall_seconds"]=time.monotonic()-started
    c=out/"consumers";proc=read(c/"process.json") if (c/"process.json").is_file() else None
    state["complete"]=bool(child.returncode==0 and proc and proc.get("complete") is True and proc.get("actual_returncode")==0)
    state["actual_failure"]=None if proc is None else proc.get("failure")
    state["output_hashes"]=[rec(p,out) for p in sorted(out.rglob("*")) if p.is_file() and not p.name.endswith(".partial") and p.name!="worker-process.json"]
    if proc is not None:
        state["actual_diagnostic_receipt"]={k:proc.get(k) for k in
            ("actual_diagnostic_processes","old_numerical_enclosures_recomputed","new_operator_norms_or_interval_integrals_evaluated",
             "diagnostic_wall_seconds","original_mathematical_run_id","original_mathematical_native_sha256",
             "new_complete_diagnostic_case_stages","reused_complete_diagnostic_case_stages","gates","complete_cases","diagnostic_native")}
    save(out/"worker-process.json",state)
    # One bounded50-minute child, followed by an actual README-checked pull.
    sync();report=root/REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"]);report.mkdir(parents=True,exist_ok=True)
    def conclusion():
        lines=["# 原完整六案例源行诊断：实际结论","",
            "这里只排列已经保存的有理上端；不是实际残差的下界，也不构成新源包络、强返回或cutoff97逆。","",
            "- 实际仓库："+PUBLIC,"- 实际 run："+state["run_id"]+"/"+state["run_attempt"],
            "- 脚本："+str(PIPELINE),"- 脚本 SHA256："+a.pipeline_sha,
            "- 参数清单："+str(rm),"- 清单 SHA256："+a.manifest_sha,
            "- 输入历史提交："+hist,"- 原完整数学 run：43676926141/1；原78成功阶段全部只读。",
            "- CLI：--repo <immutable-science> --manifest "+str(rm)+" --manifest-sha "+a.manifest_sha+" --out-dir <runner-temporary-output>",
            "- 实际子进程退出码："+str(state["actual_returncode"]),
            "- 原 numerical enclosures 重算：0；新增诊断消费进程："+str(state["actual_diagnostic_processes"]),
            "- 大输入和可重算输出仅在runner临时目录，不提交数据、不上传artifact或Release。",""]
        if not state["complete"]:
            lines+=["实际诊断未完成。原输入与已成数学未改变。",
                "实际错误："+json.dumps(state["actual_failure"],ensure_ascii=False),""]
            return "\n".join(lines)
        s=read(c/SUMMARY);d=read(c/DETAIL)
        lines+=["## 完整案例中的主导已存上界","",
            "每行保原piece/common-row及完整径向加权平方积分。四个通道分别保留，不相减旧上界。","",
            "| 半径 | 侧 | 通道 | 原piece | common-row | 原行角色 | 已存平方积分 |",
            "| --- | --- | --- | ---: | ---: | --- | --- |"]
        for case in s["cases"]:
            for side,channels in case["leading_saved_squared_integral_rows"].items():
                for channel,rows in channels.items():
                    for row in rows:
                        vals=(case["exact_radius"],side,channel,row["physical_piece"],row["common_row"],row["selected_row_role"],ball(row["saved_squared_source_integral"]))
                        lines.append("| "+" | ".join(cell(v) for v in vals)+" |")
        lines+=["","## 最小原半径的真实主导行","",
            "费用从原成功行读取，保原九非局部词和五独立偶mean。排序仅比较已存上界。"]
        for row in d["rows"]:
            lines+=["","### piece "+str(row["original_piece"])+" / common-row "+str(row["common_row"])+" / "+row["side"],"",
                "- 原 serial："+str(row["serial"])+"；原 root-row："+str(row["original_root_row"]),
                "- 原物理区间："+json.dumps(row["interval"],ensure_ascii=False),
                "- 真实径向权积分："+ball(row["radial_weight_integral"]),
                "- 完整源平方积分："+ball(row["complete_squared_source_integral"]),
                "- 原完整行payload SHA256："+row["complete_original_row_payload_sha256"],"",
                "| 原完整源词 | 已存上界 |","| --- | --- |"]
            src=row["source_bounds"]
            for key in row["nonlocal_word_order_by_saved_envelope"]:
                lines.append("| "+cell(key)+" | "+cell(ball(src["complete_nine_nonlocal_terms"][key]))+" |")
            for key in row["independent_mean_word_order_by_saved_envelope"]:
                lines.append("| "+cell(key)+" | "+cell(ball(src["complete_five_independent_even_mean_terms"][key]))+" |")
            for key,value in row["saved_complete_amplitude_operator_bounds"].items():
                lines.append("| "+cell("原振幅算子 "+key)+" | "+cell(ball(value))+" |")
        lines+=["","## 保存范围","",
            "完整新诊断只在临时目录产生；输出SHA256、实际脚本、参数和run见同目录execution.json。"
            "原1079物理seam、653 normalized ledger、九词、五mean与78原科学阶段身份均由脚本检查。"
            "未证明修正seam算子、strong-return、全高频逆、参数Schur或最终PDE族。",""]
        return "\n".join(lines)
    def snapshot():
        text=conclusion();raw=(json.dumps(state,indent=2,ensure_ascii=False,allow_nan=False)+"\n").encode()
        if len(text.encode())>=100000 or len(raw)>60000:raise ValueError("small conclusion or provenance exceeds its size limit")
        (report/"actual-result.md").write_text(text);(report/"execution.json").write_bytes(raw)
        # Never copy any native, stage, numerical array or original case into Git.
    snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
    git("commit","-m","visible-exact: record saved-row diagnostic conclusions under no-data rule15")
    while True:
        r=git("push","origin","HEAD:refs/heads/main",check=False)
        if r.returncode==0:break
        if not any(v in r.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
            raise RuntimeError("conclusion push failed outside concurrent-main rebase")
        sync();snapshot();git("add","--sparse","--",owned);git("commit","--amend","--no-edit")
    print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
        report=owned,old_numerical_enclosures_recomputed=0,new_diagnostic_processes=1,
        reproducible_output_files_persisted=0,output_hash_count=len(state["output_hashes"]),
        original_inputs_unchanged=True),ensure_ascii=False),flush=True)
    if not state["complete"]:raise SystemExit(1)
if __name__=="__main__":main()

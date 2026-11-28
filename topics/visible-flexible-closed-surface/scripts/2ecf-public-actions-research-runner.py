#!/usr/bin/env python3
"""Run the visible-flex calculations after loss of the interactive executor.
Only sources, scalar research notes, parameters, run identity and output digests
are committed. Arrays remain in RUNNER_TEMP. No credential is written to a file.
"""
import argparse, datetime, hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path

ROOT=Path.cwd()
TOPIC=Path("topics/visible-flexible-closed-surface")
WORK=Path(os.environ["RUNNER_TEMP"])/("2ecf-visible-flex-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"])
WORK.mkdir(exist_ok=True)
RUN=os.environ["GITHUB_RUN_ID"]
ATTEMPT=os.environ["GITHUB_RUN_ATTEMPT"]
SOURCE=WORK/"source"
CHECKS=[]
LAST=0.
PRIVATE=None

def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

def auth_env(private=False):
    e=dict(os.environ)
    token=e.get("MR_TOKEN") if private else e.get("M12_RECOVERY_TOKEN")
    if token:
        e["RESEARCH_GIT_TOKEN"]=token
        e.update(GIT_CONFIG_COUNT="2",GIT_CONFIG_KEY_0="credential.helper",GIT_CONFIG_VALUE_0="",
                 GIT_CONFIG_KEY_1="credential.helper",
                 GIT_CONFIG_VALUE_1='!f() { printf "username=x-access-token\\npassword=%s\\n" "$RESEARCH_GIT_TOKEN"; }; f')
    e["GIT_TERMINAL_PROMPT"]="0"
    return e

def git(*args,cwd=ROOT,private=False,capture=False,check=True):
    p=subprocess.run(["git",*map(str,args)],cwd=cwd,env=auth_env(private),
                     text=True,stdout=subprocess.PIPE if capture else None,
                     stderr=subprocess.PIPE if capture else None)
    if check and p.returncode:
        if capture:
            print(p.stdout or "",p.stderr or "",flush=True)
        raise RuntimeError("git "+str(args[0])+" failed")
    return (p.stdout or "").strip() if capture else p.returncode

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):
            h.update(b)
    return h.hexdigest()

def rule_diff(before,after,cwd=ROOT,private=False):
    paths=["README.md"] if private else ["README.md",str(TOPIC/"README.md")]
    diff=git("diff",before,after,"--",*paths,cwd=cwd,private=private,capture=True)
    CHECKS.append(dict(time=now(),repository="math-research" if private else "math-research-public",
                       commit=after,changed=bool(diff)))
    print("README_CHECK",json.dumps(CHECKS[-1]),flush=True)
    if diff:
        print(diff,flush=True)
        raise RuntimeError("README changed: the supervising root must read and apply this exact diff")

def pull_one(cwd=ROOT,private=False):
    before=git("rev-parse","origin/main",cwd=cwd,private=private,capture=True)
    code=git("pull","--rebase","origin","main",cwd=cwd,private=private,check=False)
    after=git("rev-parse","origin/main",cwd=cwd,private=private,capture=True)
    rule_diff(before,after,cwd,private)
    return code,after

def check_rules():
    global LAST
    code,_=pull_one()
    if code:
        raise RuntimeError("Unexpected public rebase conflict during a read-only periodic pull")
    if PRIVATE is not None:
        code,_=pull_one(PRIVATE,True)
        if code:
            raise RuntimeError("Unexpected private queue/rules pull conflict")
    LAST=time.monotonic()

def marker_text():
    public=[r for r in CHECKS if r["repository"]=="math-research-public"][-1]
    private=[r for r in CHECKS if r["repository"]=="math-research"]
    s="<!-- 2ecf-actions-rules --> Actions run "+RUN+"/"+ATTEMPT+"：真实 pull/rebase "+public["time"]+"；公开已读 "+public["commit"]+"，根/课题 README 无变化。"
    if private:
        s+=" 私库真实 pull "+private[-1]["time"]+"、已读 "+private[-1]["commit"]+"，私根无变化。"
    return s+"\n"

def set_marker():
    p=ROOT/TOPIC/"HANDOFF.md"
    h=p.read_text()
    lines=[x for x in h.splitlines(keepends=True) if not x.startswith("<!-- 2ecf-actions-rules -->")]
    if lines and not lines[-1].endswith("\n"):
        lines[-1]+="\n"
    lines.append(marker_text())
    raw="".join(lines)
    if len(raw.encode())>10240:
        raise RuntimeError("HANDOFF exceeds 10 KB; root must compact the actual text")
    p.write_text(raw)

def publish(label,body,files=()):
    stamp=now()
    name="2026-11-28-2ecf-actions-"+RUN+"-"+ATTEMPT+"-"+label+".md"
    path=ROOT/TOPIC/"notes"/name
    entries=[]
    for p in files:
        p=Path(p)
        if p.exists() and p.is_file():
            entries.append("- "+p.name+": SHA-256 \u0060"+sha(p)+"\u0060 ("+str(p.stat().st_size)+" bytes).")
    text=("# "+label+"\n\n**数值记录。** "+stamp+"；会话 Astra-visible-flex-2ecfcd69-20261128。\n\n"
          "公开 Actions run ["+RUN+"](https://github.com/Rogerhu12/math-research-public/actions/runs/"+RUN+"), attempt "+ATTEMPT+
          "；计算源码提交 \u0060"+SOURCE_HEAD+"\u0060。命令与参数由本提交中的 \u00602ecf-public-actions-research-runner.py\u0060 明列。\n\n"+
          body+"\n\n## 可重算输出的身份\n\n"+"\n".join(entries)+
          "\n\n数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。\n")
    path.write_text(text)
    logline=stamp+" — Astra-visible-flex-2ecfcd69-20261128：Actions "+RUN+"/"+ATTEMPT+" "+label+"；小结见 notes/"+name+"，继续强比例下的完整度量与厚度。\n"
    logpath=ROOT/TOPIC/"log.md"
    logpath.write_text(logpath.read_text()+"\n"+logline)
    subject="visible-flex: "+label+" from Actions "+RUN+" attempt "+ATTEMPT
    git("add","--",path,logpath)
    git("commit","-m",subject)
    while True:
        code,_=pull_one()
        if code:
            conflicts=git("diff","--name-only","--diff-filter=U",capture=True).splitlines()
            allowed={str(TOPIC/"HANDOFF.md"),str(TOPIC/"log.md")}
            if not conflicts or not set(conflicts)<=allowed:
                raise RuntimeError("Rebase conflict outside this publication's own state lines")
            for f in conflicts:
                upstream=git("show",":2:"+f,capture=True)+"\n"
                if f==str(TOPIC/"log.md") and logline not in upstream:
                    upstream+="\n"+logline
                (ROOT/f).write_text(upstream)
                git("add","--",f)
            e=auth_env()
            e["GIT_EDITOR"]="true"
            subprocess.run(["git","rebase","--continue"],cwd=ROOT,env=e,check=True)
        set_marker()
        git("add","--",TOPIC/"HANDOFF.md")
        if git("diff","--cached","--quiet",check=False):
            if git("log","-1","--format=%s",capture=True)!=subject:
                raise RuntimeError("Refusing to amend another publication")
            git("commit","--amend","--no-edit")
        if git("push","origin","HEAD:main",check=False)==0:
            break
    print("PUBLISHED",label,git("rev-parse","HEAD",capture=True),flush=True)

def execute(args,allow_failure=False):
    print("RESEARCH_COMMAND",json.dumps(list(map(str,args))),flush=True)
    child=subprocess.Popen(list(map(str,args)),cwd=ROOT,env=os.environ.copy())
    try:
        while child.poll() is None:
            if time.monotonic()-LAST>45*60:
                check_rules()
                publish("rules-read-"+datetime.datetime.now(datetime.timezone.utc).strftime("%H%M%S"),"计算继续进行；本项只登记两库真实 pull 与逐差规则读取，没有新增数学结论。")
            time.sleep(5)
    except BaseException:
        child.terminate()
        child.wait(timeout=30)
        raise
    if child.returncode and not allow_failure:
        raise RuntimeError("Research child exited "+str(child.returncode))
    return child.returncode

def py(name,*args,**kw):
    return execute([sys.executable,SOURCE/"scripts"/name,*args],**kw)

def obj(path):
    return json.loads(Path(path).read_text())

def compact(x):
    return "\n\n\u0060\u0060\u0060json\n"+json.dumps(x,ensure_ascii=False,indent=2)+"\n\u0060\u0060\u0060\n"

def r299():
    S=SOURCE/"scripts"
    W=WORK/"r299"
    W.mkdir()
    ports=W/"r302-c2-port-and-clearances.json"
    py("2ecf-r299-actual-thick-arms-and-tapered-central-belt-v2.py","--output",W/"thick-arms.json")
    py("2ecf-strong-moving-rigid-arm-true-cylindrical-ports-v2.py","--output",ports)
    py("2ecf-r302-c2-high-arm-rational-holding-witness.py","--ports",ports,"--output",W/"held-witness.json")
    py("2ecf-r302-wide-c3-rational-holding-fingers.py","--ports",ports,"--output",W/"C3-fingers.json")
    covers=[]
    for label,extra in (("C2-original",["--pair","C2"]),("C3-wider",["--pair","C3","--length",".58","--cap-radius",".94","--cap-height",".32"])):
        p=W/("C2-"+label+"-continuous.json")
        code=py("2ecf-r303-thick-pair-whole-image-integer-cover.py","--out",p,*extra,allow_failure=True)
        if code==0:
            covers.append((label,p))
            publish("C2-"+label+"-whole-image-bounds","未校正的真实完整 C2 厚臂族；中央原函数、真实端口修正、全部关闭段及双帽都进入连续覆盖。该覆盖不适用于后继非零 XYZ 场。"+
                    compact(obj(p)["readable"]),[p,ports,W/"held-witness.json"])
        else:
            publish("C2-"+label+"-cover-exit","本次覆盖器退出 "+str(code)+"，未登记新的连续几何结论。",[ports])
    field=W/"r299-arc-m383-h65-field.json"
    py("2ecf-r299-short-phase-positive-curvature-arc-cauchy.py","--scripts",S,"--modes","383","--nodes","65","--length",".06","--speed",".006","--out",field)
    for label,extra in (("originalg",[]),("widerg",["--c",".78","--length",".58","--cap-radius",".94","--cap-height",".32","--spans","14","--modes","8","--steps","24"])):
        fit=W/("r303-closure-v2-"+label+".json")
        code=py("2ecf-r303-reconstructed-full-closure-xyz.py","--scripts",S,"--field",field.with_suffix(".npz"),"--out",fit,*extra,allow_failure=True)
        if code or not fit.exists():
            publish("closure-"+label+"-exit","真实闭合段求解退出 "+str(code)+"；没有完成的末态报告。",[field,field.with_suffix(".npz")])
            continue
        geo=[]
        for stateflag,flag in (("unmodified",["--unmodified"]),("actual",[])):
            out=W/(label+"-"+stateflag+"-whole.json")
            gc=py("2ecf-r303-complete-closed-thick-holding-explicit-pair-v2.py","--scripts",S,
                "--solver",S/"2ecf-r303-reconstructed-full-closure-xyz.py",
                "--arms",S/"2ecf-r299-actual-thick-arms-and-tapered-central-belt-v3.py",
                "--pair","C2" if label=="originalg" else "C3",
                "--field",field.with_suffix(".npz"),"--fit",fit,"--state",fit.with_suffix(".npz"),
                "--out",out,*flag,allow_failure=True)
            if gc==0:
                q=obj(out)
                geo.append(dict(state=stateflag,metric=q["activeMetricAndCurvature"],
                                initialDiameter=q["initialHalfPhaseDiameter"]["distance"],
                                finalDiameter=q["finalZeroPhaseDiameter"]["distance"],
                                diameterQuotient=q["diameterVariationQuotientRatio"],
                                held=[r["sampledRatio"] for r in q["allThreeHoldingFrames"]]))
        p=obj(fit)
        body=("每个分支冻结自己的径向目标 g，真实 XYZ 系数同时改动整个闭合段。两端全部二 jets 不变，完整 ramp 另行观察；三种 holding frame 对整个空间像同时作刚体变换。几何表为有限点云，不能直接当作连续 reach 或 Hausdorff 下界。"+
              compact(dict(parameters=p["parameters"],variables=p["variables"],accepted=len(p["accepted"]),
                           initial=p["initialIndependent"],final=p["finalIndependent"],
                           ramp=p["independentUnchangedWholeRamp"],whole=geo)))
        publish("closure-"+label+"-actual-XYZ",body,[field,field.with_suffix(".npz"),fit,fit.with_suffix(".npz"),*W.glob(label+"-*-whole.json")])

    for label,extra in (("phase-original",[]),("phase-wider",["--length",".58","--cap-radius",".94","--cap-height",".32"]),
                        ("phase-wider-finer",["--length",".58","--cap-radius",".94","--cap-height",".32","--spans","12","--modes","10","--angles","96","--radial","40","--deltas",".0009765625"])):
        p=W/(label+".json")
        code=py("2ecf-r303-phase-specific-xyz-and-rigid-cap-continuation.py","--scripts",S,
                "--solver",S/"2ecf-r303-reconstructed-full-closure-xyz.py","--field",field.with_suffix(".npz"),"--out",p,*extra,allow_failure=True)
        if code or not p.exists():
            publish(label+"-exit","新逐相位同初相真实 g 求解退出 "+str(code)+"，未登记未完成末态。",[field])
            continue
        report=obj(p)
        rows=[{k:v for k,v in q.items() if k!="accepted"}|{"acceptedSteps":len(q["accepted"])} for q in report["results"]]
        publish(label+"-induced-g-actual-XYZ","固定紧初相真实诱导度量，后相位完整独立 XYZ 与上帽 SE(3) 自由；这允许非轴对称 g。高臂仍为点点固定 H，首端真实相位和所有两 jets 均保留。有限观察不代全时连续存在。"+
                compact(dict(parameters=report["parameters"],results=rows)),[p,*W.glob(label+"-phase*.npz")])

def r262():
    W=WORK/"original-r262"
    code=py("2ecf-r262-four-field-reconstruction.py","--scripts",SOURCE/"scripts","--directory",W,allow_failure=True)
    receipt=W/"regenerated-fields.json"
    if code:
        publish("R262-reconstruction-exit","原实际输入再生退出 "+str(code)+"。已写出的阶段回执列在下方；没有把未恢复的原字节当作可用。"+compact(obj(receipt) if receipt.exists() else []),[receipt])
        return
    rows=obj(receipt)
    publish("R262-original-input-reconstructed","这是既有 R262 输入的独立再生，不重复登记为新数学结论。各阶段原始 SHA 是否一致如下；未匹配时只使用新场身份。"+compact(rows),[receipt])
    check_rules()
    path=TOPIC/"scripts/2ecf-r262-small-input-full-xyz-positive-metric-v2.py"
    if not (ROOT/path).exists():
        publish("R262-followup-source-missing","原输入已生成，但本轮预定新小输入求解源码尚未进入 main；不宣称该分支已执行。",[])
        return
    target=SOURCE/"scripts"/path.name
    shutil.copy2(ROOT/path,target)
    py(path.name,"--scripts",SOURCE/"scripts","--work",W,"--out",WORK/"r262-small-input-v2.json")
    p=WORK/"r262-small-input-v2.json"
    report=obj(p)
    publish("R262-new-small-input-actual-XYZ","真正改变中央输入后，对完整原前缀及正径向目标执行真实 XYZ 更新；原尾及帽保持各自定义。结果："+compact(report.get("summary",report)),[p,p.with_suffix(".npz")])

def r299_joint():
    S=SOURCE/"scripts"
    W=WORK/"joint"
    W.mkdir()
    field=W/"r299-m383-h65.json"
    py("2ecf-r299-short-phase-positive-curvature-arc-cauchy.py","--scripts",S,"--modes","383","--nodes","65","--length",".06","--speed",".006","--out",field)
    proof=W/"true-ramp-second-jets.json"
    code=py("2ecf-r299-whole-ramp-second-jets-and-true-central-simpson.py","--field",field.with_suffix(".npz"),"--quarter","2048","--out",proof,allow_failure=True)
    geom=W/"C3-true-wide-closing-and-cap.json"
    if not code:
        code=execute(["node",S/"2ecf-r303-wide-closing-and-cap-directed.cjs","--ramp",proof,"--out",geom],allow_failure=True)
    if not code and geom.exists():
        g=obj(geom)
        publish("C3-actual-whole-local-curvature","真实本次 H65 的全部径格、准确中央、末端三迹及两阶角导直接进入宽关闭段/完整帽的定向矩阵。新 field 身份只来自本次数据；是否同时满足已有整像覆盖的空间垫量如表。闭核的非局部法球由正文解析论证另行合成。"+
                compact({k:g[k] for k in ("fieldSHA256","allLocalPiecesCertified","bindsPublishedShapeCover","shapeCoverEnvelope","rampPrincipalAbsoluteUpper","curvatureUpper","gate","remainder","cap","closedReachRadius")}),
                [field,field.with_suffix(".npz"),proof,geom])
    else:
        publish("C3-actual-local-curvature-exit","本次真实入口/关闭段合成退出 "+str(code)+"；未登记未通过的全闭 reach。",[field,field.with_suffix(".npz"),proof,geom])
    common=["--scripts",S,"--solver",S/"2ecf-r303-reconstructed-full-closure-xyz.py","--field",field.with_suffix(".npz"),
            "--length",".58","--cap-radius",".94","--cap-height",".32"]
    coarse=W/"C3-joint-phases.json"
    code=py("2ecf-r303-joint-active-material-phase-xyz.py",*common,"--out",coarse,
            "--deltas",".0009765625",".00390625",".015625",".0625",".125",".25",".375",".5",allow_failure=True)
    if not code:
        q=obj(coarse)
        rows=[{k:v for k,v in t.items() if k!="accepted"}|{"acceptedSteps":len(t["accepted"])} for t in q["results"]]
        publish("C3-true-whole-active-phase-XYZ","一次样条跨过整个真 .06 ramp 出口，使全部真实中间端迹参与空间求解；中央及帽端的两 jets 保持。固定同一初相真实诱导 g，所有实际相位与插值相位均单独观察。"+
                compact(dict(parameters=q["parameters"],results=rows,definedFamily=q["definedFamily"])),[coarse,*W.glob("C3-joint-phases-phase*.npz")])
        seed=W/"C3-joint-phases-phase1.npz"
        fine=W/"C3-joint-finer.json"
        fine_code=py("2ecf-r303-joint-active-material-phase-xyz.py",*common,"--out",fine,"--deltas",".0009765625",
                    "--spans","16","--ramp-spans","8","--modes","12","--angles","128","--radial","50",
                    "--steps","24","--seed-state",seed,allow_failure=True)
        if not fine_code:
            p=obj(fine)
            publish("C3-same-input-true-joint-refinement","实际旧小相位系数经准确 Boehm 和零角频补入更大空间；同一连续初相度量及全部物理参数保持。"+
                    compact(dict(results=[{k:v for k,v in t.items() if k!="accepted"}|{"acceptedSteps":len(t["accepted"])} for t in p["results"]],definedFamily=p["definedFamily"])),
                    [fine,*W.glob("C3-joint-finer-phase*.npz")])
        else:
            publish("C3-joint-finer-exit","同输入真精化退出 "+str(fine_code)+"；没有未完成的精度结论。",[coarse])
    else:
        publish("C3-joint-phases-exit","全活动段实际相位求解退出 "+str(code)+"。",[coarse])
    design=W/"C3-multiphase-design.json"
    code=py("2ecf-r303-joint-multiphase-initial-metric-design.py",*common,
            "--joint",S/"2ecf-r303-joint-active-material-phase-xyz.py","--out",design,
            "--deltas",".03125",".125",".25",".5","--curvature-guide","8.65","--steps","20",allow_failure=True)
    if not code:
        p=obj(design)
        publish("C3-true-initial-and-multiphase-metric-design","该项真实改变初相和各相位共同寻找同一诱导度量，和前两项固定旧初相 g 区分。初相全域空间位移的准确有理控制界来自真实已存系数；有限曲率导引和相位观察不代全时 reach 或精确等距。"+
                compact({k:p[k] for k in ("parameters","phases","variables","initialFullObservations","finalSameMetricObservations","genuineIntermediatePhases","initialWNormRigorousUpper")}|{"acceptedSteps":len(p["accepted"])}),
                [design,*W.glob("C3-multiphase-design-phase*.npz")])
    else:
        publish("C3-multiphase-design-exit","共同新度量/初相设计退出 "+str(code)+"；未登记未完成状态。",[design])

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--task",choices=("r299","r262","r299_joint"),required=True)
    a=p.parse_args()
    git("config","user.name","Astra-visible-flex-2ecfcd69-20261128")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    if os.environ.get("MR_TOKEN"):
        PRIVATE=WORK/"private-queue"
        subprocess.run(["git","clone","--filter=blob:none","--sparse","--single-branch",
                        "https://github.com/Rogerhu12/math-research.git",str(PRIVATE)],env=auth_env(True),check=True)
        git("sparse-checkout","set","--no-cone","/README.md","/QUEUE.md",cwd=PRIVATE,private=True)
    check_rules()
    SOURCE_HEAD=git("rev-parse","HEAD",capture=True)
    shutil.copytree(ROOT/TOPIC,SOURCE)
    print("SOURCE_HEAD",SOURCE_HEAD,flush=True)
    try:
        globals()[a.task]()
    except Exception as error:
        print(type(error).__name__,str(error),flush=True)
        raise

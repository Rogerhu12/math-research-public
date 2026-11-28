#!/usr/bin/env python3
"""Keep regenerated mathematical input in one public Actions job.
Only source/parameters and short scalar conclusions are published. Each command
uses actual files in RUNNER_TEMP; there is no data artifact or persistent cache.
"""
import datetime, importlib.util, json, os, shutil, subprocess, sys, time
from pathlib import Path

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj

ROOT=Path.cwd()
TOPIC=Path("topics/visible-flexible-closed-surface")
pub=module(ROOT/TOPIC/"scripts/2ecf-public-actions-research-runner.py","actual_r262_live_publisher")
S=pub.SOURCE/"scripts"
W=pub.WORK
ORDERS=ROOT/TOPIC/"scripts/2ecf-r262-live-work-orders.json"
PROTECTED={
 "2ecf-r262-three-arcs-shortened-prefix-v2.py",
 "2ecf-r262-three-circular-arcs-material-comparison.py",
 "2ecf-r262-small-input-full-xyz-positive-metric-v2.py",
 "2ecf-r262-minkowski-physical-continuation.py",
 "2ecf-r262-all-original-rings-affine-height-design.py",
}

def subst(value):
    return str(value).replace("{S}",str(S)).replace("{W}",str(W))

def inside(path,base):
    path=Path(path).resolve()
    if not path.is_relative_to(Path(base).resolve()):
        raise ValueError("Research output must stay in its temporary working directory")
    return path

def selected(report,fields):
    out={}
    for field in fields:
        value=report
        for name in field.split("."):
            if not isinstance(value,dict) or name not in value:
                value=None
                break
            value=value[name]
        if value is not None:
            if field in ("accepted","history"):
                value={"actualCompletedSteps":len(value)}
            out[field]=value
    return out

def perform(order):
    key=order["id"]
    pub.SOURCE_HEAD=pub.git("rev-parse","HEAD",capture=True)
    copied=[]
    for name in order.get("sources",[]):
        if Path(name).name!=name:
            raise ValueError("Source name must be a single script filename")
        source=ROOT/TOPIC/"scripts"/name
        dest=S/name
        if name in PROTECTED and dest.exists() and pub.sha(dest)!=pub.sha(source):
            raise ValueError("Parent physical definition changed; use a new explicitly defined branch")
        shutil.copy2(source,dest)
        copied.append(dest)
    script=S/order["script"]
    if not script.is_file():
        raise FileNotFoundError(script)
    interpreter={"python":sys.executable,"node":"node"}[order.get("interpreter","python")]
    args=[interpreter,str(script),*map(subst,order.get("args",[]))]
    paths=[inside(subst(v),W) for v in order.get("outputs",[])]
    for path in paths:
        path.parent.mkdir(parents=True,exist_ok=True)
    before=pub.now()
    code=pub.execute(args,allow_failure=True)
    body=order["description"]+"\n\n"
    body+="本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 "+key+"；实际源码逐文件摘要列于下方。开始 "+before+"，结束 "+pub.now()+"。退出码 "+str(code)+"。"
    if code:
        body+=" 本次退出不登记任何未完成数值或连续结论；后续其他输入继续。"
    else:
        report_path=Path(subst(order.get("report","")))
        if order.get("report") and report_path.is_file():
            data=json.loads(report_path.read_text())
            body+=pub.compact(selected(data,order.get("fields",[])))
        body+=" "+order.get("scope","数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。")
    files=[script,ORDERS,*copied,*paths]
    for path in paths:
        if path.suffix==".json" and path.with_suffix(".npz").is_file():
            files.append(path.with_suffix(".npz"))
    pub.publish(key+("-exit" if code else ""),body,files)
    return code==0

def main():
    start=time.monotonic()
    pub.git("config","user.name","Astra-visible-flex-2ecfcd69-20261128")
    pub.git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    if os.environ.get("MR_TOKEN"):
        pub.PRIVATE=W/"private-queue"
        subprocess.run(["git","clone","--filter=blob:none","--sparse","--single-branch",
                        "https://github.com/Rogerhu12/math-research.git",str(pub.PRIVATE)],
                       env=pub.auth_env(True),check=True)
        pub.git("sparse-checkout","set","--no-cone","/README.md","/QUEUE.md",cwd=pub.PRIVATE,private=True)
    pub.check_rules()
    pub.SOURCE_HEAD=pub.git("rev-parse","HEAD",capture=True)
    shutil.copytree(ROOT/TOPIC,pub.SOURCE)
    pub.publish("R262-live-input-recovery-start",
      "原运行已自然结束，其临时数组按规矩不保存。此公开任务只重建后续计算必需的原输入；既有结论不重复计算登记。此后同一任务保留实际数组，按已提交的具体科学参数继续；每个完成项独立 pull/rebase 推送。两库每45分钟真实pull，读取规则差；数组不进入Git/Release/artifact。")
    code=pub.py("2ecf-r262-four-field-reconstruction.py","--scripts",S,
                "--directory",W/"original-r262",allow_failure=True)
    receipt=W/"original-r262/regenerated-fields.json"
    if code:
        pub.publish("R262-live-input-recovery-exit","必要输入重建退出 "+str(code)+"，没有新数学结论。",[receipt])
        raise RuntimeError("Original physical input reconstruction failed")
    pub.publish("R262-live-input-recovered",
       "这一步恢复后继研究所需的实际原输入，不重登记原结论。若SHA与上次不同，只使用本次新身份。"+
       pub.compact(pub.obj(receipt)),[receipt])
    done=set()
    passed=set()
    while time.monotonic()-start<325*60:
        pub.check_rules()
        if not ORDERS.is_file():
            raise FileNotFoundError("The concrete research work orders must exist")
        orders=json.loads(ORDERS.read_text())
        if orders.get("schema")!="visible-flex-actual-r262-work-orders-v1":
            raise ValueError("Unknown work order schema")
        progress=False
        for order in orders["orders"]:
            key=order["id"]
            if key in done:
                continue
            if not set(order.get("after",[]))<=passed:
                continue
            if not all(Path(subst(v)).is_file() for v in order.get("requires",[])):
                continue
            ok=perform(order)
            done.add(key)
            if ok:
                passed.add(key)
            progress=True
            # Incorporate newly committed mathematical directions after each
            # real result instead of taking one immutable list for the whole job.
            break
        if not progress:
            time.sleep(45)
    pub.publish("R262-live-platform-time-window",
       "本公开任务到达预设平台运行窗口；已完成的科学项目逐项登记。课题仍继续，临时可重生数据不转存到Git或artifact。")

if __name__=="__main__":
    main()

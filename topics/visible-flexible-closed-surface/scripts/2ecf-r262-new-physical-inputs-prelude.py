#!/usr/bin/env python3
"""Consume the already regenerated original R262 data for new full-amplitude inputs.
This driver keeps every array inside RUNNER_TEMP and publishes each finished
numerical conclusion separately through the ordinary pull/rebase loop.
"""
import argparse, importlib.util, json, os, shutil, sys
from pathlib import Path

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s)
    sys.modules[name]=m
    s.loader.exec_module(m)
    return m

def scalar_report(q):
    omitted={"physicalVelocitySpline","recordedMeanSpline","metricDefinition","frozenMetric"}
    return {k:({"acceptedSteps":len(v)} if k=="accepted" else v)
            for k,v in q.items() if k not in omitted}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--scripts",type=Path,required=True)
    p.add_argument("--work",type=Path,required=True)
    a=p.parse_args()
    root=Path.cwd()
    scripts=root/"topics/visible-flexible-closed-surface/scripts"
    pub=load(scripts/"2ecf-public-actions-research-runner.py","r262_actual_publisher")
    private=pub.WORK/"private-queue"
    if private.exists():
        pub.PRIVATE=private
    pub.check_rules()
    pub.SOURCE_HEAD=pub.git("rev-parse","HEAD",capture=True)
    # This live job has just regenerated the original fields. Copy only the
    # newly committed mathematical sources; do not regenerate the old solve.
    names=("2ecf-r262-three-circular-arcs-material-comparison.py",
           "2ecf-r262-physical-axial-shortening.py",
           "2ecf-r262-three-arcs-shortened-prefix-v2.py",
           "2ecf-r262-three-arcs-fixed-metric-refinement.py",
           "2ecf-r262-all-original-rings-three-arcs-sleeve.py",
           "2ecf-r262-all-original-rings-affine-height-design.py",
           "2ecf-r262-three-arcs-frozen-height-and-metric-refinement.py")
    for name in names:
        src=scripts/name
        if not src.exists():
            raise FileNotFoundError("Missing published new input "+name)
        target=a.scripts/name
        if src.resolve()!=target.resolve():
            shutil.copy2(src,target)
    pub.SOURCE=a.scripts.parent
    out=pub.WORK/"r262-full-inputs"
    out.mkdir()
    axial=out/"axial-reduction016.json"
    code=pub.py("2ecf-r262-physical-axial-shortening.py","--scripts",a.scripts,
                "--work",a.work,"--reduction",".16","--out",axial,allow_failure=True)
    if code:
        pub.publish("R262-physical-axial-shortening-exit","真实原场轴向压短退出 "+str(code)+"；没有借原场的几何证书。",[axial])
    else:
        q=pub.obj(axial)
        pub.publish("R262-actual-physical-axial-shortening","真实空间 z-H(q) 的全六 jet 与新正径向目标，保留原无限尾的完整导数；九个设计及独立物理网均用本次实际原场。这里只登记有限新输入观察。"+
                    pub.compact(scalar_report(q)),[axial])
    successful=[]
    for low in (".25",".35"):
        target=out/("three-arcs-low"+low[1:]+".json")
        code=pub.py("2ecf-r262-three-arcs-shortened-prefix-v2.py",
                    "--scripts",a.scripts,"--comparison",a.scripts/names[0],
                    "--work",a.work,"--low",low,"--out",target,allow_failure=True)
        if code:
            pub.publish("R262-true-full-three-arcs-low"+low[1:]+"-exit",
                        "真整幅圆弧前缀退出 "+str(code)+"；未登记完整求解结果。",[target,target.with_suffix(".npz")])
            continue
        q=pub.obj(target)
        pub.publish("R262-true-full-three-arcs-low"+low[1:],
                    "中央完整三重真圆弧及两个真正刚口取 lambda=1，使用原已有高度替换首段，随后接回原实际无限尾。正目标在本次设计后固定；原 H65 或旧 R262 几何不转移到新位置。"+
                    pub.compact(scalar_report(q)),[target,target.with_suffix(".npz")])
        successful.append((float(q["finalIndependent"]["peak"]),target))
    if successful:
        _,parent=min(successful)
        target=out/(parent.stem+"-fixed-h1.json")
        code=pub.py("2ecf-r262-three-arcs-fixed-metric-refinement.py",
                    "--scripts",a.scripts,"--comparison",a.scripts/names[0],
                    "--physical-source",a.scripts/"2ecf-r262-three-arcs-shortened-prefix-v2.py",
                    "--work",a.work,"--parent",parent.with_suffix(".npz"),"--out",target,allow_failure=True)
        if code:
            pub.publish("R262-true-three-arcs-frozen-refinement-exit",
                        "新真圆弧输入固定连续两径向因子的实际加密退出 "+str(code)+"。",[parent,target])
        else:
            q=pub.obj(target)
            pub.publish("R262-true-three-arcs-frozen-physical-refinement",
                        "选择两次已公布完整设计中独立谱峰较小者，保留两条整连续正目标；对每个真实物理单元插入中点，角模式18到30，实际Boehm包含后只更新空间。"+
                        pub.compact(scalar_report(q)),[parent,parent.with_suffix(".npz"),target,target.with_suffix(".npz")])

    # A second physical construction retains every original radial ring and
    # redistributes the added sleeve height inside the original prefix.
    for low in (".25",".35"):
        target=out/("all-original-rings-low"+low[1:]+".json")
        code=pub.py("2ecf-r262-all-original-rings-three-arcs-sleeve.py",
                    "--scripts",a.scripts,"--comparison",a.scripts/names[0],
                    "--work",a.work,"--low",low,"--steps","0","--out",target,allow_failure=True)
        if code:
            pub.publish("R262-all-original-rings-low"+low[1:]+"-exit",
                        "保全每一原圈并重新分配中央柱高度的新物理源退出 "+str(code)+"。",[target])
        else:
            q=pub.obj(target)
            pub.publish("R262-all-original-rings-true-sleeve-low"+low[1:],
                        "这一独立输入保全每个原截圈，前置真 .78 圆弧柱，在原前缀内用两侧平坦的速度分配收回高度；原无限尾及平盘物理位置保持。完整六 jet、未拟目标和所选正目标下的实际空间步分别列出，不与前一切除构造合并接受计数。"+
                        pub.compact(scalar_report(q)),[target,target.with_suffix(".npz")])

    chosen=[]
    for sleeve,low in ((".78",".25"),(".66",".25"),(".66",".35")):
        key="c"+sleeve[1:]+"-low"+low[1:]
        target=out/("affine-height-"+key+".json")
        code=pub.py("2ecf-r262-all-original-rings-affine-height-design.py",
                    "--scripts",a.scripts,"--comparison",a.scripts/names[0],
                    "--work",a.work,"--full-sleeve",sleeve,"--low",low,"--out",target,allow_failure=True)
        if code:
            pub.publish("R262-true-full-affine-height-"+key+"-exit",
                        "真实全原圈高度/径向目标联合线性设计退出 "+str(code)+"；没有完整结果。",[target])
            continue
        q=pub.obj(target)
        pub.publish("R262-true-full-affine-height-"+key,
                    "所有原圈保留，真实两导和全部材料角进入带固定总高度的有符号Rayleigh线性设计；之后对该实际空间重算完整Gram并执行XYZ/正目标步。c=.66 的新中央使用R310的.350至.650锥缩窗定义，外部几何各自仍待连续证明。"+
                    pub.compact(scalar_report(q)),[target,target.with_suffix(".npz")])
        k=float(q["finalIndependent"]["curvature"])
        score=float(q["finalIndependent"]["peak"])+.02*max(0.,k-8.69)
        chosen.append((score,target))
    if chosen:
        _,parent=min(chosen)
        target=out/(parent.stem+"-fixed-h1.json")
        code=pub.py("2ecf-r262-three-arcs-frozen-height-and-metric-refinement.py",
                    "--scripts",a.scripts,"--comparison",a.scripts/names[0],
                    "--physical-source",a.scripts/"2ecf-r262-all-original-rings-affine-height-design.py",
                    "--work",a.work,"--parent",parent.with_suffix(".npz"),"--out",target,allow_failure=True)
        if code:
            pub.publish("R262-affine-height-frozen-refinement-exit",
                        "真实高度和两径向目标均固定的空间加密退出 "+str(code)+"。",[parent,target])
        else:
            q=pub.obj(target)
            pub.publish("R262-affine-height-and-metric-true-frozen-refinement",
                        "父态按已声明的独立误差与有限曲率代价选择；整高度分配、两条g和完整中央幅度均保留，只作真实Boehm/角频空间细化。"+
                        pub.compact(scalar_report(q)),[parent,parent.with_suffix(".npz"),target,target.with_suffix(".npz")])

if __name__=="__main__":
    main()

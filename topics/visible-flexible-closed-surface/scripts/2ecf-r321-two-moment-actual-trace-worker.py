#!/usr/bin/env python3
"""Compare a new actual low-port input with the full original material trace."""
import importlib.util,os,shutil,subprocess,sys
from pathlib import Path

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m

root=Path.cwd()
topic=Path("topics/visible-flexible-closed-surface")
pub=load(root/topic/"scripts/2ecf-public-actions-research-runner.py","actual_low_port_comparison")
pub.git("config","user.name","Astra-visible-flex-2ecfcd69-20261128")
pub.git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
if os.environ.get("MR_TOKEN"):
    pub.PRIVATE=pub.WORK/"private-queue"
    subprocess.run(["git","clone","--filter=blob:none","--sparse","--single-branch",
                    "https://github.com/Rogerhu12/math-research.git",str(pub.PRIVATE)],
                   env=pub.auth_env(True),check=True)
    pub.git("sparse-checkout","set","--no-cone","/README.md","/QUEUE.md",cwd=pub.PRIVATE,private=True)
pub.check_rules()
pub.SOURCE_HEAD=pub.git("rev-parse","HEAD",capture=True)
shutil.copytree(root/topic,pub.SOURCE)
S=pub.SOURCE/"scripts"
W=pub.WORK/"actual-low-port-trace"
W.mkdir()
recovery=load(S/"2ecf-r262-four-field-reconstruction.py","actual_trace_recovery")
recovery.fetch_blob(recovery.PREFIX_BLOB,3112330,recovery.PREFIX_SHA,W/"m12-prefix-data.npz.gz")
out=W/"actual-low-port-comparison.json"
code=pub.py("2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py","--scripts",S,"--work",W,
            "--compare-only","--out",out,allow_failure=True)
if code:
    pub.publish("R321-actual-original-two-moment-comparison-exit",
      "新相邻低口与完整原材料trace比较退出 "+str(code)+"；不登记未完成数值。",[out])
else:
    q=pub.obj(out)
    selected={k:q[k] for k in ("inputSHA","entrySHA","comparisonSHA","cutSHA","normalPlateau","normalTransition","k","phase","anchor","momentAdjustments","R317SourceSHA","axisRadii","planarMouthWidth","materialCenters","heldRelativeTranslation","gridComparisons")}
    pub.publish("R321-actual-original-two-moment-comparison",
      "只恢复已有完整原中央数据，以原74项与真实U0比较R321宽.040两矩输入。两个准确矩保持R317真实圆心及周长；本次新位置/切向/曲率数据不是先前R317或R21比较的重复登记。全角有限观察与R321严格中央/两导结论分开。"+
      pub.compact(selected),[S/"2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py",out])

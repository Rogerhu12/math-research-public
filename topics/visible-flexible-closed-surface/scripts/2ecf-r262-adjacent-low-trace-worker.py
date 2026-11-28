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
code=pub.py("2ecf-r262-adjacent-low-ports-support-physical-cut.py","--scripts",S,"--work",W,
            "--compare-only","--out",out,allow_failure=True)
if code:
    pub.publish("R317-actual-original-low-port-comparison-exit",
      "新相邻低口与完整原材料trace比较退出 "+str(code)+"；不登记未完成数值。",[out])
else:
    q=pub.obj(out)
    selected={k:q[k] for k in ("inputSHA","entrySHA","comparisonSHA","cutSHA","normalPlateau","normalTransition","k","phase","anchor","exteriorRadiusScale","axisRadii","planarMouthWidth","materialCenters","heldRelativeTranslation","gridComparisons")}
    pub.publish("R317-actual-original-low-port-comparison",
      "只恢复已有原中央数据，直接以完整原74项及真实U0比较R317的新圆口曲线；不是M12支撑参考的代理比较。此任务不恢复旧四场或重复旧结论。新的全角位置/切向/曲率比较为有限网格观察；全连续中央/臂证明已另在R317。"+
      pub.compact(selected),[S/"2ecf-r262-adjacent-low-ports-support-physical-cut.py",out])

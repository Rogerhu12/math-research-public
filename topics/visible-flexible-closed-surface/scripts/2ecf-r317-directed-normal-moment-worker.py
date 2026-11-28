#!/usr/bin/env python3
"""Compute strict moment enclosures for the actual adjacent-port curve."""
import importlib.util,os,shutil,subprocess,sys
from pathlib import Path
def module(path,name):
    q=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(q);sys.modules[name]=m;q.loader.exec_module(m);return m
root=Path.cwd()
topic=Path("topics/visible-flexible-closed-surface")
pub=module(root/topic/"scripts/2ecf-public-actions-research-runner.py","r317_directed_moment_publisher")
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
out=pub.WORK/"strict-normal-angle-moments.json"
script=S/"2ecf-r317-directed-normal-angle-moments-and-inlet-jets.py"
physical=S/"2ecf-r262-adjacent-low-ports-support-physical-cut.py"
code=pub.py(script.name,"--scripts",S,"--physical-source",physical,"--out",out,allow_failure=True)
if code:
    pub.publish("R317-direct-normal-moments-exit",
      "真实支撑半径的多项式乘指数矩以及实际材料二jet入口退出 "+str(code)+"；未登记未完成包围。源码与实际错误见本run。",[script,physical,out])
else:
    q=pub.obj(out)
    pub.publish("R317-direct-normal-moments",
      "针对R317/R319准确母线的新精密连续求值：12谐波短窗的24阶解析矩含严格余项，外半扇使用有限谐波原函数。物理归一化、两对称轴及实际法角反解含界；96个整角测试盒只是本项明列覆盖，不替代后继全外核Gram或reach。"+
      pub.compact(q),[script,physical,out])

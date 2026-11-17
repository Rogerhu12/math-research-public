# 927f LM 执行中断与原预算恢复

这不是算法失败或新科学预算。旧 executor session `91073` 在恢复读取时返回 `Unknown process id`；当前可见进程中没有旧命令，日志停在 `2026-11-17 18:24:37 UTC`，没有终态 report/field。未观察到退出码或信号，不推测具体终止原因。

已完整完成 direction0、direction1，共2个方向、2次接受。最后接受态 raw SSE `1.9976501293934307e−5`，node max `4.1205043470e−4`、mid max `8.5893150752e−4`，原 BC max `1.5265566589e−16`；8192 node/mid 正分支门通过，实际 cubic Gram `1.1068715579e−3`。这些仍是代数迭代态，不是物理接受父。

正在执行的是 direction2，damp=.25；最后日志记录已完成至少64次 Jv 和64次 Jᵀv。其后的未记录工作量未知。没有 `direction-002.npz`，也没有任何 direction2 的完成返回、候选或接受记录。不得把它计成一个已完成方向，也不得称24方向预算已经用尽。

根会话授权从最后接受态继续同一有限预算：准确复用已完成 history0/1、S、两个 Q、原 g/mesh/全部580328行/BC/容差；仅从零重新执行未完成 direction2 的原128次 LSMR，damp仍为.25。总逻辑预算仍为24方向/20接受，不刷新；此前丢失的至少64次 Krylov工作作为额外执行开销明确保留，不能隐去或并称原方向只执行了128次。

## 恢复身份

- 原算法源 `parallel-implicit-lm-budget.py`：`927f403f984c88471dedaf14988b6cd25ebd44b5ce3d0a1e6a0bcc57ea20cc0d`。
- checkpoint `parallel-implicit-lm-budget-once.checkpoint.json.gz`：`84b1f854dabfbacca654be5b91a46cf4946b2198c9b5c3bc859d3a6a8319e821`。
- 原日志 `parallel-implicit-lm-budget-once.log`：`16940942748d446f68fa9b8823e88a14f96959b413eee444cbd1ccee7aae06a1`。
- 原 `parallel-implicit-lm-budget-work/accepted-002.npz`：`6198aa6e3b1fe8f4c86bd443882912c279eef692bd69a4f013e9cd1488b929b5`。
- 原完成方向 `direction-001.npz`：`d78630ecbb241335efcf60f405c131a0ad787e89550aa56280240687b5543fd7`，不重算。
- 最小恢复生成器 `parallel-implicit-lm-resume.py`，5951 B，SHA256 `6a172b2d8e32fb265e7e169da93c2465d43ef013925297b89969b2ba49a5a72a`。
- 由原源准确启动补丁生成的 `parallel-implicit-lm-budget-resumed.py`：`8fa6dc6d441b5345ead444d2c01baf6d89d8229f45ecd1684a469917af0af399`。无需重复入库该派生全文。

生成器核原源 SHA 后，只替换启动状态/计数/恢复日志及输入身份。它不改任何循环、方向公式、接受门、阻尼更新、预算或终态读出；还要求恢复后的 policy 与 checkpoint 字典完全相同，checkpoint Y/U 与 accepted002 逐位相同，完整 residual summary 一致。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-implicit-lm-resume.py \
 --base-source parallel-implicit-lm-budget.py \
 --emit-source parallel-implicit-lm-budget-resumed.py \
 --topic math-research-public/topics/visible-flex-larger-amplitude \
 --problem-source parallel-model-implicit-frenet-newton.py \
 --warm parallel-hold-m160-short-bvp-warm.json.gz \
 --polynomial-source parallel-root-implicit-frenet-probe.py \
 --matrix-source parallel-root-implicit-matrix-free.py \
 --prepared parallel-implicit-lm-direction-once.prepared.npz \
 --preparation-report parallel-implicit-lm-direction-once.preparation.json \
 --first-direction parallel-implicit-lm-direction-once.direction.npz \
 --first-report parallel-implicit-lm-direction-once.json \
 --first-physical parallel-implicit-lm-fullstep-physical.json \
 --resume-checkpoint parallel-implicit-lm-budget-once.checkpoint.json.gz \
 --interruption-log parallel-implicit-lm-budget-once.log \
 --work parallel-implicit-lm-resumed-work \
 --out parallel-implicit-lm-resumed-once.json
```

所有旧文件保持原字节。新输出与 work 使用独占路径；恢复原因、丢失部分工作下界、原 source 和 checkpoint SHA 会写入新 checkpoint/终态。此恢复定义冻结时尚未产生新求解结论，后续终态单独登记。

正式保留的恢复源为 `scripts/parallel_20261117_implicit_lm_resume.py`，原算法源为 `scripts/parallel_20261117_implicit_lm_budget.py`；上述命令在 WORK 原输入目录运行，scratch 同名源码与正式源逐字相同。派生源/原输入和状态按既有完整配方保留于仓库外。

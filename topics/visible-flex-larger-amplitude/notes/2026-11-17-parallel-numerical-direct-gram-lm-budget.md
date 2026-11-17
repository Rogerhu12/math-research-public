# R647：完整 Gram–T LM 预算准备

## 新模型与唯一缓存方向

这是一项与仍在执行的 `0f269…` Pr 预算独立的新任务。保留原 `1662…` 的同一 Hold g、602 节点、M160/N2048、全部 580328 个 Y/U 自由变量及可逆 T 坐标；初始化仅采用 `85c726…` 已明示的 `U0=ez`。原 Y 和其余 U 不改，不消费旧 Pr 未达标终态。

每个节点和实际 cubic 中点完整保留

\[
p_0=V\cdot d/a,\qquad
p_1=|d|^2/a^2-\rho(Y_0)^2,\qquad
p_2=|V|^2-1
\]

的全部二次 Fourier 系数，共 962 行。总物理行数 `1157286`，加原位置 BC 482 行和新 `U0-ez` 482 行，合计 **1158250 行**。全域共享 rho 的核心链式导数和列平方和交叉项由冻结 `85c726…`/`5b5ebf…` 源提供，固定复用完整 `70c6a7…` prepared，不重算 moments。

第 0 方向直接消费 `513aa782…` 的已完成 damp=1/max256 方向 `11550c74…` 和报告 `81c8d131…`。真实试点的 full Gram SSE=`6.191013184119097e-10`、ratio=`.9999999646425087`、8192 全部 node/mid 正分支已付，实际 cubic Gram=`4.980386907216856e-6`。新源仅核原始数组/输入/完整残差身份，不重跑该 LSMR 或物理审计。它记为本预算的首次代数接受，下一方向索引 1、damp=.5，仍不是物理合格父。

## 固定预算与新终门

最多 24 个逻辑方向（含缓存 0），最多 20 次接受；其余每个 LSMR 固定 maxiter512，atol=btol=`1e-8`、conlim=`1e6`。全部普通停止码、真实方向、显式坐标 normal 残差照存，不把 `istop=7` 叫线性收敛。目标为

\[
\min_z\|r+Jd_0+JTS\Pi z\|_2^2+\mu^2\|z\|_2^2,
\qquad\delta x=d_0+TS\Pi z.
\]

仿射修复和投影采用完整 CoreBoundary，包含原位置 BC 与全部 U0 行，不能混用旧 Pr 的482行边界器。只评价满步 alpha=1；pred 使用全部1158250行。仅当有限、pred>0、实际 SSE 严降、ratio≥`1e-4`、原位置BC≤`1e-11`、U0字面等于ez，才调用原8192角 node/mid分支审计；rho/Q/W/H/正法速度都正方可接受。接受ratio>.75则µ除2，<.25则乘2；其余不变。拒绝留原点并µ乘2，均计入原方向总额。

**本模型的固定终门**同时要求：

1. 全部节点和中点的 full Gram 系数 max≤`1e-10`；
2. 原位置 BC max≤`1e-11`，并且 U0 字面为 ez；
3. 同一已接受 Y/U 的完整8192角 node/mid实际相对Gram≤`5e-7`，正分支门保持。

这些是新模型门，不冒称旧 Pr 的 `1e-8` 门。中间不要求Gram单调，终门不以低SSE代替。旧物理读者仍附带 Pr 点残差等诊断字段，它们不进入这个新目标或收敛判定；实际 full Gram 数组另外完整保存。

## 恢复与输出

沿用 `0f269…` 的完整 durable 流程：每个完成方向（含拒绝）原子提交checkpoint；已完成LSMR由ready+真实dY/dU/z恢复，已完成评价由evaluation恢复；不重算完成的方向或8192审计。active每16次乘积保存阶段/base/damp/计数，未完成调用可用同源、同索引、同µ的 `--resume` 续原预算，其partial成本明确登记。总方向/接受上限不刷新。

终态保存真实mesh/Y/U、全部node/mid full Gram系数、964边界残差、历史、已付physical审计及核心字面偏差。**不调用旧 Pr 的 C_U 逆生成共同加速度**，不提供伪造A。当前cached0核心Z的160个非零槽约`2.46e-32`不在此算法中抹掉；未来镜像及共同C²定义另作真实几何步骤。本预算即使终门通过，也不自动给全连续域、闭合、reach或精确同g收敛证书。

## 冻结身份与复现

算法 `parallel-direct-gram-integrated-budget.py` SHA256：
`efe92eb460c73719b1db067df7bb32383732ab46140ab13dc98ee5bceffcf460`。
仅准备报告 `parallel-direct-gram-integrated-budget-preflight.preparation.json` SHA：
`0acdccf5f39907978bbd26c70942efa5a557701e7de33d75a4dca5565a1ba301`。
完整初始prepared SHA：`70c6a7cb4f8886d96daba9dacda11d7c82d08342ef4d0283cf3a93c795a58390`。
其准备报告SHA：`b1c03602bd19049361e5268a3cfa39eb0d23fce30805cab814965e45c7c79ea4`。
所有源与缓存依赖的完整SHA在preflight报告。preflight已通过，未启动新预算方向。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-direct-gram-integrated-budget.py \
 --topic math-research-public/topics/visible-flex-larger-amplitude \
 --problem-source parallel-model-implicit-frenet-newton.py \
 --warm parallel-hold-m160-short-bvp-warm.json.gz \
 --polynomial-source parallel-root-implicit-frenet-probe.py \
 --matrix-source parallel-root-implicit-matrix-free.py \
 --coordinate-source parallel-root-integrated-coordinate-preparation.py \
 --gram-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_direct_gram_matrix_free.py \
 --preparation-source parallel-root-direct-gram-integrated-preparation.py \
 --prepared parallel-root-direct-gram-integrated-preparation.prepared.npz \
 --preparation-report parallel-root-direct-gram-integrated-preparation.json \
 --first-direction parallel-root-direct-gram-integrated-direction-once.direction.npz \
 --first-report parallel-root-direct-gram-integrated-direction-once.json \
 --work parallel-direct-gram-integrated-budget-work \
 --out parallel-direct-gram-integrated-budget-once.json
```

仅准备命令用单独的 `--out parallel-direct-gram-integrated-budget-preflight.json --prepare-only`，保留原preflight字节。恢复在原实际CLI追加 `--resume`，不更换前缀刷新预算。实际启动与终态独立登记。

## 真实启动登记

root完整审读efe92后已按上述CLI真实启动session1878。启动报告SHA `d0547198059d9d7536ebd80b12268012bb442b7fcb1121036ac594446ff6564d`；cached0记1方向/1接受，Y/U仍3ddd76cc原身份，SSE6.191013184119097e−10，下一方向1/µ=.5。原preflight0ac以另名完整保存。没有重做缓存LSMR、8192审计或1203点moments。后续真实终态由numerical唯一读取；本条不预报通过门。旧Pr0f在99082执行器中断后用同--resume恢复为97062，≥432对未完乘积成本保留，详见单独recovery1；其原目标、预算与门完全不改。

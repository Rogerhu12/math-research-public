# 原 1662 的 T 坐标单方向：执行前冻结

本条是准备，不是已执行数值结论。源 `parallel-implicit-integrated-direction.py`，9205 B，SHA256 `2754dbcb63a21fc58789b27d756ec9433e748ef12a14a25bc4000d2c54c1b7cc`。已作语法编译检查，未运行准备入口、LSMR 或物理审计；原 927f/8fa6 LM 预算不受影响。

保持原 `1662`、602节点、M160/N2048、全部580328个Pr/BC行、原完整变量和325/157边界；唯一变化是使用已登记的可逆积分坐标T及其完整列尺度。所有梯形兼容缺陷 D 继续作为变量，不替换原公共三次场。直接复用 `ef81` 的 `IntegratedCoordinates/IntegratedBoundary` 与 `7aff` prepared 的 S，不重算 moments 或列范数。

计算一次

\[
 \min_z\|r+Jd_0+JT S\Pi z\|_2^2+\|z\|_2^2,
 \qquad \delta x=d_0+TS\Pi z,
\]

固定 `damp=1,maxiter=128,atol=btol=1e-8,conlim=1e6`，只一个原始全步 alpha=1。普通 damping 施于新 z，**改变了步范数**，不冒称只做了数值等价预条件。raw residual 权重、Pr/BC方程和g均不改。

保存完整原物理 `dY,dU`、新坐标 z、基点身份和方向 SHA；报告完整线性模型残差、坐标正则 normal residual、真实 raw SSE 与预测下降率。为避免只在不同坐标内比较 normal residual，另报告同一原物理 Y/U 系数中的 `Jᵀr` 和 `Jᵀ(r+Jδ)` 的L2/最大范数，及相对初始范数。它们的两倍是raw SSE梯度；这些未投影向量含边界约束法向分量，不单独当作约束问题的stationarity证书。

旧 S-only µ1 方向仅从已保存5629数组读取，使用同一当前J重算可比物理 `Jᵀ(r+Jδ_old)`，不重做旧LSMR、trial或物理审计。该读取不是第二个新求解。

新alpha1试点只调用一次原8192全节点/实际三次中点物理审计，报告rho/Q/W/H/normal、Gram和全部未保留二次谱。仅在实际raw merit及原BC门通过、该指定审计的正分支门也通过后，报告有限试点可行；始终 `accepted_parent=false`。此外R647 ray只核这一个alpha1，不另作半步或参数扫描。未执行非线性后继预算。

## 冻结输入

- 原 Problem源5b965及warm1662，matrix-free源 `ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4`。
- T源 `ef81da0b0de7200501d34d6702f92ae0131a953e9038ad8302d2e1edb61cd3d8`。
- T prepared数组 `7affbce1eac7e61b94a03ca8b463c35ea1c4e28dfc3f02e74f1847670923965e`。
- T preparation report `c69c2325a979af1757904ff37ba7ad7a3e7ef4f1e2f1f003d63cf985e875ec8f`。
- R647 ray源 `e67f7d1bf021fd88646e1a77057b4557418ff77ebd5032461d8a46dd7f6498fc`。
- 旧S-only方向 `5629db05e0cc7b014c6eb4375badb35ea1d408f40d8cdbccef88122e6150798e`。

原完整LM真正终态后接下列已定单次方向，原运行不被替换：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-implicit-integrated-direction.py \
 --topic math-research-public/topics/visible-flex-larger-amplitude \
 --problem-source parallel-model-implicit-frenet-newton.py \
 --warm parallel-hold-m160-short-bvp-warm.json.gz \
 --polynomial-source parallel-root-implicit-frenet-probe.py \
 --matrix-source parallel-root-implicit-matrix-free.py \
 --coordinate-source parallel-root-integrated-coordinate-preparation.py \
 --prepared parallel-root-integrated-coordinate-preparation.prepared.npz \
 --preparation-report parallel-root-integrated-coordinate-preparation.json \
 --ray-source parallel-implicit-quadratic-ray.py \
 --baseline-direction parallel-implicit-lm-direction-once.direction.npz \
 --out parallel-implicit-integrated-direction-once.json --execute-direction
```

默认不带 `--execute-direction` 时只读入冻结准备并输出身份/规则，不运行线性或非线性求解。所有原始数组/报告保留scratch，后续真实数值另记。

正式源为 `scripts/parallel_20261117_implicit_integrated_direction.py`；上述WORK内同名源码与正式源逐字相同，依赖源均已刊入同topic/scripts，原数组/报告按对应原配方在仓库外保留。

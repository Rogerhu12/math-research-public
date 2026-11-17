# 向内 .997 / M128：fast125 Schur 有限族精化未接受

日期：2026-11-17。维护：`parallel-geometry-amplification`。

**状态：真实运行失败记录。`success=false`，没有新的可接续父；没有把失败
迭代的节点几何当作接受场，也没有运行要求成功输入的共同 quintic 读者。**

## 1. 固定比较对象

warm 是已真接受的
[`M112 Schur 场`](2026-11-17-parallel-geometry-schur-m112-accepted.md)，
SHA `dd566c28b0f3a51c1d052bd22d9644c707570afdb0dfcc927849568eb4f082dd`。
reference 仍为原真 .995 M112 场，
SHA `d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f`。

两者零补到 M128，固定 N2048、向内 scalar、原 .995 参照、`duration=0`。
在新有限维数下重新计算完整 RHS、实际移动框架和连接，取最快 `M−3=125`
个实 Schur 维数；目标仍为原参照的二阶 Taylor 目标。浅端保留原规则的
261 行，ODE 为全部 386 维。该固定标量比较依赖既有材料规范；计算角 φ 中
`rho` 随可调高 core 系数而变，不能据此宣称已经完成公共材料坐标的精化对齐。

谱准备成功：所选阈值 `2.4971541657033427`，完整实维数 125，
分界间隙 `4.352306229597014`，最小所选实部 `4.673307280503485`。
原系数行条件数 `1.00569523534`，子空间 `sep` 估计 `.0165893821`。
没有硬切复共轭块或删行来强行达到维数。

## 2. 原求解策略的实际终态

设 `tol=1e−8`、`max_nodes=2000`，原 domain-safe Newton 与 separated QR
完整保留。首网格 510 节点，初始根矩阵条件估计 `95371.51`。
部分 Newton 步真接受，但步长曾缩到 `1/8192`，末次全部试步无下降时按原
策略保留旧可行点。

| 网格阶段 | 实际节点 | 最大 RMS | 边界残差 | 原策略结果 |
|---|---:|---:|---:|---|
| 第一阶段 | 510 | 约 2.49e−4 | 约 2.87e−9 | 自动增加 913 节点 |
| 第二阶段 | 1423 | 3.59247613343e−4 | 2.87358700723e−9 | 再请求增加 2610 节点，超过上限 |

最终 `status=1`，报告 `The maximum number of mesh nodes is exceeded.`。
最后阶段也出现 fresh-Jacobian 后全部 trial 无下降，保留旧点。
总计 222 次批量函数调用、436 次分块 Jacobian 调用。

这次运行没有得到可与 M112 实际 Gram 做成功场比较的 M128 场。
它只说明本次明确的 finite-family 精化与初猜/求解参数未接受；不证明所有
M128 解不存在，也不证明更高 M 的其他边界或初猜无法达到目标。

## 3. 冻结来源与复现

新 wrapper：
[`2026-11-17-parallel-geometry-schur-refine-bvp.py`](2026-11-17-parallel-geometry-schur-refine-bvp.py)。
SHA256：`a33ad582a81c859d30aab7651065e64a9a0319ba40fb0c8c0ed55bb6fea97b33`。
它调用已冻结 M112 driver 的 `main`，显式传新 M；原 driver 和 Schur helper
未改。输出分别保存 wrapper / base driver / helper 的 SHA 和谱选择诊断。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  notes/2026-11-17-parallel-geometry-schur-refine-bvp.py \
  --input "$SCRATCH/parallel-inward0997-m112-schur.json.gz" \
  --boundary-input "$SCRATCH/parallel-continue0995-m112.json.gz" \
  --out "$SCRATCH/parallel-inward0997-m128-schur.json.gz" \
  --modes 128 --angles 2048 --tol 1e-8 --max-nodes 2000
```

失败 raw SHA256：
`58b685e7252e5f4c7a6caa5f6286f3a0a92adf9b5c80c15669becfc2258488f6`。
完整 log SHA256：
`3949042e680310da9d8d4e0a7b21adc308c12b28f947b92dd902363a82e498ea`。
原始状态和完整 log 保存在 scratch，不入库、不作为接受父。

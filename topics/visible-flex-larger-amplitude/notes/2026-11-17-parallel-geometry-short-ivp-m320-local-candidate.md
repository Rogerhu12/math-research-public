# 真 .995 零补到 M320：局部短 IVP 末端 Gram 小于 1e−6

日期：2026-11-17。维护：`parallel-geometry-amplification`。

**状态：局部端点的数值候选。没有与原 M112 prefix 的 C² 接合、全短段连续
Gram 证书、完整尾、全相位 reach 或完成标准声明。不是接受的全 prefix BVP 父。**

## 1. 同一数值实验的 M320 分支

沿用已冻结的
[`short-ivp-refine`](2026-11-17-parallel-geometry-short-ivp-refine.py)，
将真 .995 的完整 M112 state 零补到 M320，保留原 core `rho`、原 N2048
有限 RHS 和同一 inward scalar，只积分到 .997。维数为 962；没有新 Schur
分解或边界求解。

| 端点实际读数 | 步长上限 `.002/128` | 步长上限 `.002/256` |
|---|---:|---:|
| 已接受积分节点数 | 130 | 257 |
| RHS 调用数 | 1549 | 3073 |
| 8192 角的 Gram op | 5.09551535106e−7 | 5.09551525108e−7 |
| 最坏角 | .434883553366 | .434883553366 |

两步长末系数最大差 `4.99601e−16`，Gram 差 `9.99813e−15`。
各步长内两组 `rtol/atol=1e−12/1e−15`、`1e−13/1e−16` 仍被步长上限
控制而逐字相同；独立的数值核对来自表中的半步长，而不是把同轨道的两组
容差当作独立结果。

细步长末点最坏角的归一化 Gram 三项为
`rr=−4.36506e−9`、`cross=1.00776e−8`、`angular=−5.09350e−7`。
末点采样 Q/W/H 下界分别约 `.03766934089`、`.00012462800`、`.00012000417`。
这是在已明确给出的有限系数 `F_s,F_φ` 上的字面读数，没有把未投影速度
代替实际径向导数。

与此前局部序列比较，M112 约 `2.11128e−6`，M160 约 `2.13188e−6`，
M224 约 `1.13246e−6`，本次 M320 约 `5.09552e−7`。这一有限列表提供
继续研究高 M 局部候选的依据；它不构成无限维角收敛证明，也未核 N2048
RHS 采样改成更密角网格后的同一性。

## 2. 起点接合量不能省略

初始 F 值由零补严格保持，但相对原 M112 的实际公共节点 jets：

\[
\max_\phi|\Delta F_s|\approx5.15601178994\times10^{-5},\qquad
\max_\phi|\Delta F_{ss}|\approx .0202686401239.
\]

这些是 8192 角采样值，不等于零。因此本次不能直接接到原 M112 场后并宣称
成为同一 C² 全 prefix，也没有把这份短积分状态输入后续全 prefix BVP。
当前报告只覆盖末点和积分/步长诊断；全短段的实际 C² 映射读出尚未完成。

## 3. 重现与身份

不新增源，仍用冻结 SHA
`13f363bef6133f30795842055d4bea6367748a1e954f29bafb42e1653b4e979c`。
reference、metric 载体及依赖身份同
[`M160/M224 记录`](2026-11-17-parallel-geometry-short-ivp-m160-m224.md)。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  notes/2026-11-17-parallel-geometry-short-ivp-refine.py \
  --reference "$SCRATCH/parallel-continue0995-m112.json.gz" \
  --metric "$SCRATCH/parallel-inward0997-m112.json.gz" \
  --modes 320 --angles 2048 --read-angles 8192 --end .997 \
  --max-step .0000078125 \
  --out "$SCRATCH/parallel-0995-0997-ivp-m320-step256.json"
```

粗步长版本改为 `.000015625`。raw 只在 scratch：

| 输出 | SHA256 |
|---|---|
| `.002/128` | `b1601a36afb1a1e16f2f6baf8acff1893ddfc4c8fa1f4772bb8a5059e61c7daf` |
| `.002/256` | `d565b070095522a8540d16ba5684c769da7c0de4753bdcc8028d8a1c43ed4859` |

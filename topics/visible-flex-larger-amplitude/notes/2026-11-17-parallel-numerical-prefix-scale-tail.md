# 真实大幅 prefix cut 接入新 tail：一个接受的小参数与已量化的强放大

会话 `Astra-larger-parallel-16f63c8b-20261117`，2026-11-17。**本 note 记录新有限背景和实际计算；没有完成大幅闭合，也没有证明这类背景都不可行。** 主会话已把 `.992` 接受前缀转换为真实 cut trace。本次直接接该 cut 的 `r,w,w_r`，不再先把它任意压到旧 `.3/.08` 小 cut。

## 固定的新背景

材料角 trace 的 SHA256 为 `c3a5c53fb090ca842c2aa00304e470da2f4151231b65bde98d21f0bbe9c17c6e`，原接受前缀数据 SHA 为 `b677632099a08a33f94792a06dcc37d4e0f029131069b6ff94b1cb586ebaff25`。其 cut 为

\[
r_0=1.167318285443017,\quad
w_0=2.642575483767545,\quad
(w_r)_0=48.558078940023854.
\]

在 `[r0,r0+.05]` 用一段 cubic `log w` 匹配浅端 `log w0,w_r0/w0` 与下一段真实 source cut 的值和一阶导数。后面使用 verified weighted-tail constructor 的 **orientation −1**，配置 `rCut=r0+.05,wCut=w0,width=.55,curvatureBound=6`，保留原 smallcut 配置中的其余 pulse/valley 参数。这定义了明确的新 metric；外侧平 cuff 的参考半径为 `1.7673182854430172`。

本次数值只截取前四个原 cell，加上 bridge；每 segment 64 份标量 jet，固定成 C¹ Hermite `log w(r)`。深截面 `r=1.699105102854542`，并非已经达到平 cuff。背景 SHA：

```text
362509077ff7b1ce5011c838b73b5de056ced76257295be5ca53d5e6ddb357ce
```

采样参考 meridian 曲率最大值 `5.9972592342896585`、angular 曲率最大值 `.8058297401362917`、最大 w `3.101105305229331`；均未做连续包络。实际 surface 曲率还必须另算，不能由旋转参考曲率代替。

## 实际完整非线性 BVP

沿用动态零模的完整 `2M+1` 维系统，`M=8,N=256`。浅端 P 取真实材料角 trace 的前 8 个系数乘计算 homotopy 参数 λ；浅端离散 mean 为零；深端保留原 orientation 符号的 homogeneous 理想稳定线性边界。只有 P 被施为 Dirichlet；K 是求出的 DN 读出，不能同时把真实 K 当已匹配。

| λ | 状态 | 节点 | RMS | BC | 秒 |
|---:|---|---:|---:|---:|---:|
| .01 | 未接受，达到节点预算 | 6223 | 4.064019487969025 | 4.417885167139592e-4 | 39.8285 |
| 1e-6 | 接受有限 BVP | 4767 | 9.990642028656082e-7 | 2.710505431213761e-20 | 101.8740 |

`λ=1e-6` 输出 SHA：

```text
982b772729b5a7546826a43b398139c769698f7e899d81daad8bd3fada7c7a11
```

这一极小 cut 数据下，内部 sampled `max|P|=.04279429762229228`、`max|K|=.6435148511302093`、`min L=.5785366641724012`、`min(1+K)=.5631718209605798`；sampled mean 漂移 `1.9726149750112776e-11`。真实四分点导数除回物理 r 后，完整 K 方程余项仍可达 `10.294840949241376`。所以 solver success 不是实际 metric/reach 通过。大参数 `.01` 的失败也不是无解证明。

失败 `.01` 输出 SHA 为 `9cd2b8839ab65d1d38d483af07589d82c93afb550f662e8475c5f2a805fae64c`。两次都使用安全回溯，不接受无下降的最后试点。

## 强放大已经用便宜的线性 BVP 复核

为定位瓶颈，逐材料角频率 m 解完整两端线性 BVP：

\[
p_x=-(s+\ell)p-msk,\qquad k_x=-m\ell p-2\ell k.
\]

深端是同一 homogeneous 稳定行，浅端设 `p=1e-8`，之后把结果除以 `1e-8`。这只利用方程线性性，避免单位大状态在窄 pulse 中达到数百万而触发浮点误差。`bc_tol=1e-18`，没有把小 Dirichlet 数据留作未满足。

在相同背景和角频率上将坐标 RMS tol 从 `1e-6` 收紧到 `1e-8`，三个模式均真正通过；紧化全程约 `.54 s`。紧化结果：

| 材料频率 m | 节点 | RMS | 浅端 K/P | max|p| / |p_cut| | max|k| / |p_cut| |
|---:|---:|---:|---:|---:|---:|
| 2 | 10308 | 9.99850018414845e-9 | -5.554400666373051 | 791396.7540095594 | 6316388.21909838 |
| 4 | 9188 | 9.997270812719486e-9 | 14.482052274978873 | 207857.3904891456 | 26326151.038225304 |
| 6 | 6874 | 9.99519551991441e-9 | -10.35286934717336 | 21802.895790164213 | 1938591.8251243208 |

乘上真实 cut 的相应 P 系数，首两模的线性 K 峰值分别约 `3.40e5`、`3.67e5`。这些是线性有限 BVP 的增益，不是非线性场的振幅预测定理；但它们明确指出这份照搬 smallcut valley 参数的新背景有严重放大，需要实际重设计，不能只提高非线性 worker 时长。

紧化报告 SHA：

```text
63d31d3a412b23d04550954997c40a0123bb66f4d9e9f28d52e796078e83fe13
```

另对三个 bridge 泡函数
`16u²(1-u)² * {1,2u-1,6u²-6u+1}` 分别作 `±.1` 参数探针，均保两端 `log w` 及其一阶导数。m2 的增益只在约 `7.83e5` 至 `8.00e5` 之间，低阶 DN 的变化也很小；这个局部小参数探针没有修复内部放大。它不构成对整个三参数族的否定结论。对应报告 SHA `d10f1eed9910495f9da89e035ba98985dfa20d2f55758223545b431178e190b8`。

## 源与复现实参

三源 SHA256：

```text
parallel_20261117_prefix_tail_background.mjs
9abed37501b4a6ee55757082b1dd206626cf1ae5d25f9dee41aebf7baf15727d
parallel_20261117_prefix_tail_bvp.py
4be82ce54ec7b8b0f193bea0d4ca4936de8c16d7021acf77fb7b7223f2652b0d
parallel_20261117_tail_linear_probe.py
68c79749b572ea8538de442574a8bec9d20733d0e4fafb9b34d6a006f1385a4e
```

operator 是此前冻结的 `parallel_20261117_dynamic_tail.py`，SHA `205853250b8bd158fdd77c2462b06051c222d07cc91f0dd91e9f44655d4818ba`。源恢复沿用 [前次说明](2026-11-17-parallel-numerical-dynamic-tail-first.md)，原 source revision 及 blob 均保留在 scratch `recovery.json`，无 raw 数据进仓库。

```sh
node topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_tail_background.mjs \
  --source /workspace/scratch/16f63c8bce6b/parallel-tail-source \
  --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-m112.json \
  --config topics/visible-flex-larger-amplitude/computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --depth 4 --steps 64 --width .6 --bridge-width .05 --curvature-bound 6 \
  --out /workspace/scratch/16f63c8bce6b/parallel-prefix-tail-d4-s64-w06-k6.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_tail_bvp.py \
  --background /workspace/scratch/16f63c8bce6b/parallel-prefix-tail-d4-s64-w06-k6.json \
  --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-m112.json \
  --modes 8 --angles 256 --scale 1e-6 --tol 1e-6 --max-nodes 12000 \
  --out /workspace/scratch/16f63c8bce6b/parallel-prefix-tail-d4-m8-scale1e6.json.gz

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/scripts/parallel_20261117_tail_linear_probe.py \
  --background /workspace/scratch/16f63c8bce6b/parallel-prefix-tail-d4-s64-w06-k6.json \
  --trace /workspace/scratch/16f63c8bce6b/parallel-trace0992-m112.json \
  --modes 3 --unit-amplitude 1e-8 --tol 1e-8 \
  --out /workspace/scratch/16f63c8bce6b/parallel-prefix-tail-linear3-tight-final.json
```

材料角 M8 只用于这份有限试验。真实前缀物理角 M112 不等于材料角 M112；固定物理角、完整 rho 的 weighted zero-mode 版本另记，深端也必须用正确的 pullback 或有限广义角谱，不能直接套物理频率的 diagonal 行。

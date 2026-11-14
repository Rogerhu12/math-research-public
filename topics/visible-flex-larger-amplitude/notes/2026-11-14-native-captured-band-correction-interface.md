# actual28 保存系统的完整带状重解入口

2026-11-14。此入口消费 actual28 的原完整 J、残差、边界、scale 和原 delta，只改变该已保存有限线性系统的求解算法。它不调用 native worker、ODE/RK、initializer 或任何非线性 trial。首次选择原保存 $\sigma$ 的行列尺度，全部模式、节点、cut/far 方程及原归一化完整保留。

科学动因与 actual28 的真实浮点读数见 [actual28 记录](2026-11-14-actual-request28-native-linear-defect.md)；数组代数与普通浮点缺陷的区别见 [R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md)。本文件是已完成源码的接口，不声称新方向已经算出或通过原 native。

## 1. 源与唯一实际输入

新源为 `computations/geometry_20261114_native_captured_band_correction.py`，36,867 B，SHA256：

```text
b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390
```

只完成 Python AST 检查，没有在本地 import/运行数值函数。LAPACK 调用沿用仓库已有 `geometry_20261114_banded_collocation.py` 的 `dgbtrf/dgbtrs` 实际接口；该参考源 SHA 为 `0780dcc4e331f6cde64141b0fa9ebdd1325eec2af87d94fc455e72405a0524f1`，此新入口不修改或导入其 collocation 对象。

固定输入来自公开 [run 43611175099](https://github.com/Rogerhu12/math-research-public/actions/runs/43611175099)，source `6bd52b446241be53e8842d4db5a24f9c2069e6e5`，artifact `14120548264`（`visible-mainline-nativecorrection-43611175099-1`）。完整 artifact 的 ZIP 为 235,561,097 B，SHA256 `0ff8e6f597af60f19243b5457c28e8638096c775551b6f3d044dc2d2f1fabeee`。

解压后输入目录为 `native-correction-capture`。必须保留其完整内容，尤其 `large-arrays/`；这些大阵在原 artifact 中，Git 中的 publication manifest 不能替代原数组。

| 身份 | 固定 SHA256 |
| --- | --- |
| `result.json` | `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7` |
| `capture-summary.json` | `48d8c012aa0e266bd9c39d1ce6342a97ef54c7d01a6dcfb37997da6ede4b22c1` |
| `capture-manifest.json` | `3ed8c1bf3458f2f5852c5e74ebaec77292233a6b940b494c73e4289bbdf95ae3` |
| 全部原 J 的串联 Float64LE 字节 | `394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19` |
| 原 delta 的完整 Float64LE 字节 | `d3734cf4587acbddbc32c80e49223fc6db4e8077190c8c875c22f218219031f2` |

源同时绑定 capture launcher/hook、原 diagonal-far core、原 seed/H/scales/far 的既有 SHA。运行前逐件核 result 的 22 件小输出、29 个完整数组、所有 116 个 chunks 的大小/行段/字节 SHA 和各完整数组串联 SHA，并核完整 chunk ledger。每次读 J chunk 时再核该块 SHA。不会将重新生成或近似的 J 混入这个系统。

## 2. Actions CLI

将本仓上述 artifact 解压到 `$CAPTURE28` 后，在本仓 Actions 执行：

```bash
python "$VISIBLE_COMPUTATIONS/geometry_20261114_native_captured_band_correction.py" \
  --capture-directory "$CAPTURE28/native-correction-capture" \
  --capture-result-sha256 ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7 \
  --scaling original-sigma \
  --out "$VISIBLE_OUT/captured-native-band-correction"
```

`--scaling original-sigma` 是本次已选择且源码默认的选项；另提供显式 `none`，便于有因的同系统对照，不在一次运行中自动扩展多个实验。没有额外 row/column equilibration。实际形成矩阵每一行、每一列的最大绝对条目会保全，以便判断下一步是否确需另一种可逆缩放；不以这些数值冒充条件数。

输出目录必须为空且独立于输入。输入 artifact 由 workflow 取回；此入口本身不联网、不下载、不改分支、不改任何输入文件。

## 3. 完整行列布局与实际存储

实际 $M=112$、$K=2M=224$、$D=576$，未知量为 577 个完整节点的 $(Q,\Pi)$，总维数 129,248。方程行顺序为：cut 的 112 行、576 个 stage 各 224 行、far 的 112 行。原 stage 方程是

$$
-\delta_n+J_n\delta_{n+1}=-r_n.
$$

cut 用原 $r_c=y_{0,Q}-\mathrm{target}$；far 用原 $r_D=\Pi_D-G_DQ_D$。新源锁定已捕获的原 core SHA 和完整 $M$ 维 far 向量，确认该原 far 为对角结构，才使用本带宽；没有把未知 dense far 偷当成对角矩阵。

stage 行 $M+nK+i$ 的 $-I$ 位于列 $nK+i$，行列差为 $M$。完整 J 位于列 $(n+1)K+j$，行列差在 $[-(3M-1),M-1]$ 内。cut 和对角 far 没有扩大这个范围，故下带宽 $kl=112$、上带宽 $ku=335$。使用 LAPACK 存储

$$
\mathrm{AB}[kl+ku+\mathrm{row}-\mathrm{column},\mathrm{column}]
   =A_{\mathrm{row},\mathrm{column}}.
$$

原始 J 按块流读，直接装入 Fortran 顺序带阵。为 pivot fill 预留 $kl$ 行，实际形状为 $560\times129248$，占 579,031,040 B。完整 J 不再整体复制到内存，不另存可重生成的巨大 LU；保存 LU 字节 SHA、完整 pivot 向量、原来源和全部新方向，使线性计算可在相同输入下复现。

## 4. 原 sigma 行列尺度与原坐标复核

选择 `original-sigma` 时，定义 $\delta_n=\sigma_n v_n$，每个 stage 方程行除原 $\sigma_n$。于是该块为

$$
-v_n+\frac{\sigma_{n+1}}{\sigma_n}J_n v_{n+1}
   =-\frac{r_n}{\sigma_n}.
$$

cut/far 的同节点比例抵消。所有 $\sigma$ 直接来自 actual28 完整原数组，不用初猜器的 private graphs/gains 替换。实际比例、乘法、RHS 和恢复均为明确 binary64 运算；因此源码同时记录形成时非零舍入为零的个数、比例 bits 和恢复误差所需的完整 $v$、$\sigma$、$\delta$。这种浮点形成不是自动精确的实数组变换，按 R266 单列。

分解调用 `dgbtrf(...,overwrite_ab=1)`，回代调用 `dgbtrs(...,overwrite_b=1)`，保留全部原 pivot。参数错误、零 pivot 或非有限输入/方向均如实失败并保全实际信息；没有截断 SVD、伪逆、删行或换边界的隐藏后备。

恢复完整原坐标后，再次流读原 J，并同时对原 delta 与新 delta 逐行计算：

$$
e_n=(J_n\delta_{n+1}-\delta_n)+r_n,
\qquad
e_c=\delta_{0,Q}+r_c,
\qquad
e_D=(\delta_{D,\Pi}-G_D\delta_{D,Q})+r_D.
$$

矩阵乘法使用逐列分离的 binary64 乘、加，以原 `matrixVector` 的列顺序累加。全部 raw/scaled stage/cut/far 行均保全，每个节点方向的最大分量及其原 scale 比值也保全。原方向的六组 raw/scaled 缺陷会与 capture 中的完整数组逐字节对照；结果如实记录，若不同不伪称同一浮点求值。两次读出都只是普通浮点诊断，不把计算得小误差直接升格为严格全系统上界。

## 5. Actions 内的精确最坏行见证

在任何带阵分解之前，先对 actual28 已观察到的最坏行（stage 43、row 221、Pi mode 110）作精确 `Fraction` 运算。所有 finite binary64 操作数按其精确实数值解释，完整 224 项点积、减当前 delta、加原 residual，再除原 sigma，均用有理数完成。即使后面的 factor/solve 失败，这份独立见证也已落盘。

见证保全完整 J 行、下一节点完整 delta 的 Float64LE hex、其余标量 bits、精确 numerator/denominator 和仅供阅读的十进制显示；另给原浮点报告与精确行值之差。它可以给同一保存数组模型的全缺陷一个**严格下界**，从而区分浮点点积消减与实际 binary-array 校正缺陷。

若新方向算出，还会对其全浮点报告选中的最坏行作同样的精确核验。**一个精确行见证不是完整系统的严格上界，也不是原非线性 flow 的精确导数证书。**本次没有增加这样的完成门；它是直接回答 actual28 已暴露问题的有因检查。

## 6. 产物与退出语义

小报告包括 `input-binding.json`、`assembled-model.json`、`factorization.json`、两份 `exact-*.json`、`output-array-manifest.json` 与 `result.json`。完整新方向另存 `direction-checkpoint.json.gz`，包含 577×224 全值、负零 sidecar、完整字节 SHA、原输入绑定及明确的 `native_accepted=false`。

原坐标/缩放坐标方向、全部缺陷、RHS、pivot 及实际矩阵条目尺度向量集中在新输出 `large-arrays/`，延用 artifact 保全与 Git manifest 分流。原 28 大阵不复制进新输出，不重复发布几百 MB 的输入。

exit 0 只表示该离线方向与完整诊断已算完，不因诊断缺陷大小自动称 native 接受。原 native 请求数、新 J 次数和 nonlinear trial 次数均为 0。新方向是否有资格进入后续原 nonlinear 验证，按真实结果另作判断；本入口不运行那些试步、不改变原容差或研究完成标准。

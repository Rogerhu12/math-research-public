# 六模冻结候选的锐化连续验证接口（2026-11-14）

## 冻结对象与独立脚本

`scripts/space_star_frozen_lift_verify.py` 读取已公开 Actions 43592270686 的六模高度设计 JSON，直接使用其保存的准确 numerator/denominator。它不调用优化器、不重新拟合、也不重新选择系数；默认读取 `selected_frozen_candidate`。另可用明确的原始 `initial_lift` 标签选择一条已保存候选，但这只是指定输入，验证过程中不会自动切换。

主输入为 a=.65,b=.12 的 `.10` 起点冻结候选（其最终 H1 约 .70334）；备用为 a=.60,b=.09 的 `.30` 起点冻结候选。两者保持原报告的半宽 **w=.02**。原始选定候选身份、求解器 success 原值、准确物理参数哈希、原 JSON 哈希和平面证书哈希均写入输出。

脚本准确重算尖谷线性消元等式，验证全部六个有理高度与保存的四个自由有理数一致；还要求平面证书 SHA 与原设计输入完全相同。它不会从文档中的截短小数重建模型。

## 1. 二阶高度误差包围

对准确冻结高度

\[
 z(\phi)=\sum_j H_j\sin(3j\phi)
\]

取准确有理数

\[
 M_{z,2}=\sum_j(3j)^2|H_j|\ge\sup|z''|.
\]

均匀顶点 \(\phi_i=2\pi i/N\) 的每个高度都以定向区间计算。若其绝对值上界的最大值为 \(H_V\)，则

\[
 \sup|z|\le H_V+M_{z,2}(2\pi/N)^2/8.
\]

理由是高度到相邻端点线性插值的误差不超过二阶弦余项，而线性插值的绝对值不大于两端点绝对值的最大值。该界只改善证明，不改变任何高度系数。

输出保留全单元区间的旧高度上界、顶点上界、准确 M2、弦余项、新上界和相对于允许高度的余量，避免将新的证明方法误报为新的几何设计。

## 2. 同一旋转正交架中的物理导数

设 \(e_r=(\cos\phi,\sin\phi,0)\)、\(e_\phi=(-\sin\phi,\cos\phi,0)\)。下列向量是实际 Cartesian 导数在同一个 \((e_r,e_\phi,e_z)\) 架中的分量：

\[
 v_1=(r',r,z'),\quad
 v_2=(r''-r,2r',z''),
\]

\[
 v_3=(r'''-3r',3r''-r,z'''),\quad
 v_4=(r''''-6r''+r,4r'''-4r',z'''').
\]

它们不是把上一行的分量直接求导后所得的向量；旋转基的所有导数已经包含在这些公式中。因此同一角度上的范数、点积、叉积范数和标量三重积可直接在此架计算，与先乘上整体旋转矩阵完全相同。省略整体旋转可减少区间依赖。

令 \(v=|v_1|\)、\(W=|v_1\times v_2|\)、\(D=\det(v_1,v_2,v_3)\)，则

\[
 \kappa=W/v^3,\quad \tau=D/W^2,\quad
 D'=\det(v_1,v_2,v_4),
\]

\[
 v'=v_1\cdot v_2/v,\qquad
 W'=(v_1\times v_2)\cdot(v_1\times v_3)/W,
\]

\[
 q_\ell=\frac1v\left(
 \frac{D'v^3}{W^3}+\frac{3Dv^2v'}{W^3}
 -\frac{3Dv^3W'}{W^4}\right).
\]

这些是与原 Cartesian 实现相同的物理不变量。在每个完整角单元上，脚本直接界

\[
 J\ge1-w\sup|q_\ell|,\qquad
 \lambda\le\frac{\lambda_0}{1-w|q_\ell|},\quad
 \lambda_0=\kappa+\tau^2/\kappa.
\]

最后才对单元取最大值；没有将不同角度的全局最坏分子、分母混合。如果某个框架或 J 单元未认证，则不输出全宽主曲率上界，也不宣告材料映射合格。

## 3. 最小 Actions 命令

首轮选择 32768 单元，因为原 4096 的 J 界宽足以使其下界显著为负；单元宽缩小八倍，加上共同旋转架可以直接检验剩余依赖是否已够小。不预报结果，不在本地运行这些命令。

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_frozen_lift_verify.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43592270686-1-star_lift/space-star-lift-design-a65-b12.json \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --trial selected --nodes 32768 --samples 384 \
  --out "$VISIBLE_OUT/space-star-six-mode-a65-b12-N32768.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_frozen_lift_verify.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43592270686-1-star_lift/space-star-lift-design-a60-b09.json \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --trial selected --nodes 32768 --samples 384 \
  --out "$VISIBLE_OUT/space-star-six-mode-a60-b09-N32768.json"
```

需要的输入 sparse 路径为原 `actions-43592270686-1-star_lift/` 和 `actions-43590239302-1-star_core/`；代码依赖本新模块、`space_star_lift_design.py`、`space_star_flat_core.py`、`star_core_geometry.py`、`folded_reference_geometry.py`。输出是小型证书摘要，不保存大网格。

全宽 J 连续认证为正后才附加同一冻结候选的有限正常弦诊断，明确标为样本，不作为 reach 下界。即使局部曲率和条件幅度同时通过，仍保留全局嵌入、reach、真实过渡带与帽包络为未证明。

## 4. 已完成的开发检查

`notes/space-star-frozen-lift-verifier-check-20261114.json` 只使用人工输入：三个角点上的 Cartesian 与共同旋转架不变量区间相交；准确单位圆/圆柱通过完整证书接口，得到 J≈1、唯一非零主曲率≈1、高度零，并正确拒绝零旋转距离的幅度门。没有读入或计算真实六模研究候选，没有优化或参数扫描。

本脚本独立于已排队的其他验证器；现有两模 mix=.187 的认证结果继续保留，不因更宽六模验证而重算或替换。

# 多高度模的全角曲率设计，随后冻结准确系数

日期：2026-11-14。独立新脚本 `scripts/space_star_lift_design.py`，不修改已经排入 Actions 的两高度模脚本。准确平核公式仍是 `results/R9-rectifying-flat-core.md`。本地只做解析导数与有理消元核对；没有运行研究优化。

## 1. 为什么改为优化整圈

两高度模的廉价实现检查已经显示：$(a,b,h,c)=(.60,.09,.2,.20)$ 虽将谷点主曲率降到约 $4.705$，全圈粗样本却出现约 $30.22$ 的峰。只改善谷或尖，不能说明整圈或有宽度的准确核曲率改善。

新高度函数为

\[
z(\varphi)=\sum_{j=1}^{m}H_j\sin(3j\varphi),\qquad m\ge4.
\]

它保留三重转动及完整半转对称。不同 $H_j$ 会改变空间曲线周长和 $a_0$；整个优化阶段是准确局部核的**几何设计**，不是共同固定度量的精化。挑定系数以后才冻结该候选的准确度量与全部入口 jets。

## 2. 以有理线性代数精确消去两项

记

\[
r_v=1-a+b,\quad t_v=28a-109b-1,\qquad
r_t=1+a+b,\quad t_t=-1-28a-109b.
\]

尖点和谷点的挠率分子都是高度系数的线性式；其准确零条件为

\[
\sum_{j=1}^{m}j(9j^2r_t+t_t)H_j=0,
\quad
\sum_{j=1}^{m}(-1)^j j(9j^2r_v+t_v)H_j=0.
\tag{1}
\]

程序把 $a,b$ 的十进制输入解释为准确有理数，用 `Fraction` 消去 $H_2,H_3$，保留 $H_1,H_4,\ldots,H_m$。每个自由基都逐项验证 (1) 恰为有理数零。因此这两项没有软惩罚残差，也没有把 `.220` 之类小数当作消挠率恒等式。

在最终冻结时，优化所得自由浮点值先转为可往返的十进制字符串，解释成准确有理数，再用同一准确消元矩阵重算全部 $H_j$。报告保存每一项的分子和分母；连续区间验证使用这些准确有理系数。后续调用不能把另一组舍入后的系数默认为相同准确候选。

## 3. 全角、有宽度的真实主曲率目标

对每个极角，使用四阶位置导数计算

\[
\kappa=\frac{|\gamma'\times\gamma''|}{|\gamma'|^3},\quad
\tau=\frac{\det(\gamma',\gamma'',\gamma''')}{|\gamma'\times\gamma''|^2},
\quad q=\tau/\kappa,\quad q_\ell=\frac{dq/d\varphi}{|\gamma'|}.
\]

指定半带宽 $w$ 后，R9 的材料映射余量和全径向最坏主曲率是

\[
J_{\min}(\varphi)=1-w|q_\ell(\varphi)|,\qquad
\lambda_{\rm band}(\varphi)=
\frac{\lambda_0(\varphi)}{J_{\min}(\varphi)},
\quad \lambda_0=\kappa+\tau^2/\kappa.
\tag{2}
\]

引入标量上界 $T$，SLSQP 直接最小化 $T$，并在完整角网格上施加

\[
T(1-w|q_\ell|)-\lambda_0\ge0,\quad
1-w|q_\ell|\ge J_{\rm floor},\quad
\kappa\ge\kappa_{\rm floor}.
\tag{3}
\]

默认 $J_{\rm floor}=.15$、$\kappa_{\rm floor}=.04$。这些是设计时避免退化的约束；没有在负 $J$ 时裁剪分母再声称得到小曲率。完整目标和约束的自由系数 Jacobian 由一阶前向解析微分给出，包含 $q_\ell$ 中的全部四阶位置导数影响。

为避免优化器试步在真正奇点上产生未定义数值，内部极小交叉积范数有显式计算保护。报告标记一切触发该保护的场；它们不能成为通过的准确候选。最终连续认证不使用这个保护替代 $\kappa>0$。

## 4. 真实高度与宏观幅度预算

输入平面数据来自公开 Actions `43590239302` 的 4096 段证书。记它的距离下界为 $d$，全平面直径上界为 $D_{xy}$。由于准确平核投影 padding 至多 $w$，保留 $.3$ 见证的完整直径预算是 $(d-w)/.3$。由此得到中央高度绝对值的充分预算

\[
H_*=
\frac12\sqrt{\left(\frac{d-w}{.3}\right)^2-(D_{xy}+2w)^2}-w.
\tag{4}
\]

优化不仅约束角节点上的高度。对于等距极角网格步长 $\Delta\varphi$，全局标量插值余项满足

\[
\epsilon_z\le\frac{\Delta\varphi^2}{8}
                  \sum_j(3j)^2|H_j|.
\]

每个节点同时要求 $|z_i|+\epsilon_z\le H_*$，由此控制节点之间的真实高度。优化使用浮点实现，最终由连续区间重新核对高度、padding 和完整三维直径；不会只看离散最高点。

预算只覆盖准确局部核。未来过渡和帽必须另外证明同一投影外扩与总高度条件，才能传给闭曲面；当前没有构造这些对象。

## 5. 冻结后的独立复核

每个起点的优化结果先固定准确有理系数，再在独立加密角网格审计。按真实宽度曲率样本及正则性选择候选后，使用完整极角区间作连续认证：

- 验证所有区间的空间曲率正下界及 $J>0$；遇到无法决定的格子就标记未认证。
- 在每个小区间使用其自己的 $\lambda_0$ 和 $q_\ell$ 包络求 (2) 上界，避免把不在同一位置的全局最大值不必要地相乘。
- 累加准确系数所定义曲线的周长包络，保存冻结 $a_0$ 的区间。
- 重新证明真实高度和条件见证比值；记录实际主曲率下界所给 reach 的必要上界。
- 仅当正则条件通过时，另列准确核位置公式上的法线弦样本。它们仍不是 reach 下界。

因此 `solver_success=true`、小的优化目标、好的密采样和连续认证是四个不同字段；任何一个都不会自动置课题完成。

## 6. 已完成的廉价实现检查

仅以 32 角做合成自由系数检查，不运行 SLSQP 或全曲线研究扫描。4 和 6 高度模均验证两个有理线性约束恰为零；完整约束 Jacobian 的随机方向中心差分相对差分别为

\[
8.05\times10^{-10},\qquad1.03\times10^{-8}.
\]

小记录为 `notes/space-star-lift-design-check4-20261114.json`、`notes/space-star-lift-design-check6-20261114.json`。当前没有获得这一多模优化的实际结果。

## 7. Actions 命令

先在两组宏观核心上以 6 高度模、三个起点运行。若需要较小对照，改 `--height-modes 4`，其余物理输入保持相同；它改变有限设计空间，不是更换候选的准确参数。

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_lift_design.py \
  --a .60 --b .09 --height-modes 6 --half-width .02 \
  --angles 384 --dense-angles 3072 --initial-lifts .10,.20,.30 \
  --higher-coefficient-bound .08 --j-floor .15 --kappa-floor .04 \
  --max-iterations 200 --certificate-nodes 4096 \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --out "$VISIBLE_OUT/space-star-lift-design-a60-b09.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_lift_design.py \
  --a .65 --b .12 --height-modes 6 --half-width .02 \
  --angles 384 --dense-angles 3072 --initial-lifts .10,.20,.30 \
  --higher-coefficient-bound .08 --j-floor .15 --kappa-floor .04 \
  --max-iterations 200 --certificate-nodes 4096 \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --out "$VISIBLE_OUT/space-star-lift-design-a65-b12.json"
```

sparse 路径需要本新脚本，以及稳定依赖 `space_star_flat_core.py`、`star_core_geometry.py`、`folded_reference_geometry.py` 和原 `actions-43590239302-1-star_core` 目录。Python 依赖为 numpy、scipy；不新增外部服务或私有来源。

# 偶 cosine 核的新准确端点分支：q_ell 归零与尖端转向预算

日期：2026-11-14。状态：准确线性参数化和导数已推导，独立新脚本及人工开发检查已完成；尚未运行此分支的真实研究 solve。本分支是新的几何设计，不是对已严格排除固定点继续加密。

## 1. 实际失败点说明应改变什么

[公开 run 43597247312](actions-43597247312-1-cosine_core/receipt.json) 的首个自由六模 cosine 候选具有零 framing，且连续验证证明曲率不为零、全宽 J 为正。但其已认证主曲率最大值下界为 16.2794705330，对完整曲面给出的必要 reach/D 上界为 .01956718606，严格小于 .03。因此这个冻结点不应再安排嵌入证书或闭合连接优化。

失败不来自尖端/谷底挠率没有归零：偶对称确实使两处 τ=0。实际谷底 q_ell≈35，使 J≈.3，谷底全宽曲率约 16.312；独立全角下界也确认厚度失败。原 H2≈−.12 触及指定物理系数边界。

新设计直接消去尖端、谷底的 q_ell，并显式放宽导出的 H2/H3 物理系数箱至 ±.5。它没有沿用旧 sine 高度的挠率消元公式。

## 2. 准确的两个线性条件

取 r=1+a cos(3φ)+b cos(6φ)，z=z0+Σ Hj cos(3jφ)。在尖端、谷底分别令 σ=1、−1。记

\[
R_\sigma=r''-r=-1-10\sigma a-37b,\qquad
U_\sigma=r''''-6r''+r=1+136\sigma a+1513b.
\]

在这些对称点，Z=z''=−9Σσ^j j²Hj、V=z''''=81Σσ^j j⁴Hj，并有

\[
q_\ell=\frac{ZU-RV}{(R^2+Z^2)^{3/2}}.
\]

因此只需准确施加

\[
\boxed{\sum_{j=1}^m \sigma^j j^2(U_\sigma+9j^2R_\sigma)H_j=0,
\qquad \sigma=1,-1.}
\tag{1}
\]

这两式使 q_ell 准确为零；相应两条完整材料径线上的 J=1、全宽主曲率等于中央 κ。在其他角度，q_ell、J 和 λ 仍需完整约束及独立连续验证。

## 3. 有理参数化与真正冻结的模型

令两行分别为 t_j、v_j。以 H2、H3 为导出变量，设 Δ=t2 v3−t3 v2。对于每个自由 Hj，其对导出两变量的系数是

\[
H_2:\ \frac{-t_jv_3+t_3v_j}{\Delta},\qquad
H_3:\ \frac{-t_2v_j+t_jv_2}{\Delta}.
\]

`EndpointElimination` 全部使用 `fractions.Fraction`，逐列断言两行乘积严格为零。六模时自由高度是 H1、H4、H5、H6，加上 offset 与 epigraph T，共 6 个未知量；固定 offset 时为 5 个。

冻结时先把优化器实际 binary64 的四个自由高度用 `Fraction.from_float` 精确存为有理数，再经这个**预先定义的准确有理矩阵**生成全部六个 H。不能把浮点矩阵乘法舍入后的 H2/H3 又各自视作准确输入，否则 (1) 只会近似成立。

这不是求解后重新拟合两个物理参数：准确线性图从设计一开始就是模型定义，浮点优化只是它的数值求值。最终 dense audit 使用准确有理图生成 H 后的浮点求值，并记录与优化浮点矩阵乘法的差。通用独立 cosine verifier 直接消费所得完整 `frozen_physical_identity`，不需改变其数学公式。

## 4. 把尖端转向的真实几何门也放进设计

尖端在准确 core 上有 q=τ=0，故整条材料径线准确为 γ(0)+s B(0)。令尖端 Zt=z''(0)、Rt=r''(0)−r(0)。两侧中至少一侧具有向外的单位径向速度

\[
\eta=\frac{|Z_t|}{\sqrt{R_t^2+Z_t^2}}.
\]

如果完整曲面 reach 至少 τ，且其投影只允许相对原尖端向外扩张 p，那么必要转向距离给

\[
w\eta+\tau(1-\sqrt{1-\eta^2})\le p.
\]

当前 p=w。令 e=w/τ、s0=1+√(2e)，可化成对 Zt 的两条线性不等式

\[
\boxed{|Z_t|\le |R_t|\,\frac{s_0-s_0^{-1}}2,
\qquad Z_t=-9\sum j^2H_j.}
\tag{2}
\]

脚本记录两种 τ：

- `necessary`：τ0=.03×公开水平直径连续下界。违反由上端计算的 (2) 可严格排除；这是任何完整候选必须支付的最低厚度。
- `planned`：τtarget=.03×本次完整直径预算上界。它是更保守的设计约束；其失败不能当作一般不存在证明。默认使用这一种。

两种 (2) 都用区间算术包围。设计采用上界函数的**下端**，再将 binary64 常数向下取一 representable step。严格必要失败采用上端判断；输入函数保留 |Rt| 的整个区间，没有把其 abs_upper 当成准确值。

这一尖端条件只是一条必要/保守设计门，没有替代整个连接带的投影审计或 reach 证书。

## 5. 目标、边界箱和保存策略

新脚本 `scripts/space_star_cosine_endpoint_design.py` 仍最小化 T，并对每个角度约束

\[
T(1-w|q_\ell|)-\lambda_0\ge0,\quad
1-w|q_\ell|\ge .3,\quad \kappa\ge .1.
\]

高度含 offset 和二阶导数插值余项；默认预留完整允许中央高度的绝对余量 .02。默认自由 H1∈[−.6,.6]、H4..H6∈[−.12,.12]，导出 H2/H3∈[−.5,.5]。这些是明确的新设计箱，不能称作旧固定参数细化。

自由 offset 默认以当前初值高度最小/最大值的中点自动居中，再作为变量优化；固定 offset 模式不执行这个初值调整。每个 case 独立一个 solve、一个完整小 JSON 和 checkpoint。第一评价、每 10 评价或 60 秒保存当前采样可行的最小 epigraph 候选；若未有可行点则保存最小违反点。最后还保留 raw final 的完整冻结身份和 dense audit。

## 6. 已实际完成的开发检查

`notes/cosine-endpoint-design-check-20261114.json` 只用一个人工 a=.07、b=.005 的六模样本，没有进行研究参数优化。结果：

- 自由 offset 模式的完整约束 Jacobian 方向差分相对误差 4.41×10^−9；
- 固定 offset 模式 7.43×10^−9；
- tip、valley 的两个准确有理线性分子均严格为零；
- 有理定义图冻结后的完整 H 与浮点矩阵求值的最大差为 3.26×10^−19；
- 两个对称点的数值 q_ell 为浮点零量级，完整公式与独立对称式一致。

`repo_sources` 独立静态审核了两行、H2/H3 消元符号、尖端预算的必要/计划方向及定向取值；并指出一般非终止有理 Rt 的 abs 区间细节，已修正后重跑同一个开发检查。没有把这些实现检查当成真实几何可行性。

## 7. 可直接运行的单 case Actions

```bash
OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_cosine_endpoint_design.py \
  --check-only --out "$RUN_DIR/cosine-endpoint-check.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_cosine_endpoint_design.py \
  --a .65 --b .12 --height-modes 6 --half-width .02 \
  --initial-lift .15 --angles 768 --dense-angles 6144 \
  --j-floor .3 --kappa-floor .1 --height-reserve .02 --tip-budget planned \
  --derived-coefficient-bound .5 --max-iterations 400 \
  --checkpoint-every 10 --checkpoint-seconds 60 \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --out "$RUN_DIR/cosine-endpoint-a65-b12-h15.json"

OPENBLAS_NUM_THREADS=1 python topics/visible-flex-new-mechanism/scripts/space_star_cosine_verify.py \
  --input "$RUN_DIR/cosine-endpoint-a65-b12-h15.json" --nodes 32768 \
  --planar-report topics/visible-flex-new-mechanism/notes/actions-43590239302-1-star_core/star-core-geometry-grid.json \
  --out "$RUN_DIR/cosine-endpoint-a65-b12-h15-N32768.json"
```

这里每个研究 case 仍独立保存。下一步只有新冻结点真正通过全宽局部曲率与高度预算后，才接准确 core 全宽单射验证和双侧连接；零 framing 与两个端点的 q_ell=0 都不是连接 PDE 的充分条件。

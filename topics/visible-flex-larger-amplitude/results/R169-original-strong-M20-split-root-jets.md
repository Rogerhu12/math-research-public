# R169 — 原强 M20 split-flow 的真实隐式根导数

作者：/root（GPT-6 Astra Pro；AI 辅助），2026-11-13。

## 实际完成的读出

使用 R168 的同一 R39 强 M20 完成响应、原 frozen160 calibration、原 865 个状态和原 quadrature512。在 cell9..7 的全部216个原 shooting 小段两端，调用原 `createFourierRootSplitFluxEngine` 的 RHS，再通过原 `createMomentumPhysicalJetEvaluator` 隐式微分完整有限 momentum root。没有重积分 ODE、求 BVP、重建 far graph 或用另一个诊断 ODE 代替原 RHS。

主结果 SHA `7eaf5fd2531694e618894ef73dc18c669a0be7e2e96c4616fd55dc894412aea2`；实际 owned exit0，20.61659122 秒，峰值160620 KiB，668门全过。原216段的所有端点 P/K、P′/K′、均值及均值导数、背景 r/w/s/ell、原有限根残差均完整保存。

## 导数恒等式

令 $x$ 是当前原小段的局部坐标，$s=r_x/r$、$\ell=(\log w)_x$。R168 的相对常规三角系数为

$$P_m=-mr^3Q_m/w,\qquad K_m=\sqrt2L_m-mP_m.$$

将原 split-flux 的 Q 方程代入，得到准确代数恒等式

$$P'_m=-(s+\ell)P_m-msK_m.$$

原有限 momentum root 依赖 Q、connection $\Pi$、r 和 w。原物理 jet evaluator 在完整有限 root Jacobian 上解微分方程，保留背景的显式 x 导数；其输出为 $L'_m$，从而

$$K'_m=\sqrt2L'_m-mP'_m,\qquad c'=L'_0.$$

这里的 $L'$ 来自原 root 的隐式微分，而非将有限角向投影误差设零后从另一物理方程推导。用于局部 x 的 $r_x$ 和 $\ell$ 都已由原 subdivision 缩放；后续转换回原 raw-segment x 时须除以原段宽 $1/8$。

## 连续候选的明确入口

每个节点的候选值只取 R168 单一 canonical 读法的保存 P/K，两个相邻小段引用同一二进制值。每段两端导数取本次原有限-flow jet。后续把这些数作为准确有理数，使用三次 Hermite 公式定义分段多项式，就能获得精确 C0 的候选。没有声称这些二进制斜率正好给出跨段 C1，也没有声称候选已满足原真实方程。

最大直接 Q 微分与上述 P′ 恒等式的浮点差为 $2.710505431213761\times10^{-20}$；两个 chart 的 P/K 差分别为 $1.0842021724855044\times10^{-19}$ 和 $9.43689570931383\times10^{-16}$。这些差异保留，不改写成精确零。最大有限根相对残差为 $2.281374649809887\times10^{-14}$。

原 evaluator 输出的物理 Darboux 诊断最大值为 $6.419000513132553\times10^{-28}$。该数含真实量纲和很小的背景因子，不能单独当作归一化 PDE 误差、完整角向误差或连续径向 residual。

## 未由本结果推出的事项

完整连续角向 mean、原实背景、整个径向区间 residual、所有遗漏频率与 R143 实际入口仍须分别支付。本包只提供同一原有限强场的完整节点导数数据，不推出外9..7非线性延拓、闭面或全 t 几何完成。

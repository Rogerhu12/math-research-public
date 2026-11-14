# R45 单 P 的独立有限参数实例接口

日期：2026-11-14。源码开发说明；尚无本脚本的真实设计计算。计算只在 `Rogerhu12/math-research-public` 的 GitHub Actions 执行。

## 1. 为什么是新目标

脚本 `scripts/literature_single_P_instance.py` 复用已公开的 `literature_zero_operator_instance.py` 中平滑标量控制、框架桥、准确整圈、矩阵密度和绝对步长 Jacobian 工具，不读取旧实例的最优参数或输出。

旧实例拟合的是 Klein 八块总矩阵。当前准确目标是 [R45](../results/R45-reversal-four-block-third-period-cancellation.md) 的单条 P：frame 从 I 到 $D=\operatorname{diag}(-1,1,-1)$，标量端芽相同，且 $M_P=0$。其归一目标改为

$$\frac{M_P}{N}=F_{\rm bulk}(p)+\frac{G_{\rm common}(p)+G_D(p)}N.$$

只编译终点 D 所需的桥，不拟合 g1 桥。八个参数每次均从零初值重新求解，冻结预条件矩阵仍来自 R37 准确八维 bulk 导数。

## 2. 倒行的控制定义与自然闭合

P 的完整原始控制按顺序保存在输出中。反向控制通过逆转 segment 顺序和各 segment 的时间得到，u 与 xi 均不翻号。

对 ramp

$$k=k_0+(k_1-k_0)S,\quad
b=b_0(1-S)+b_1S+\eta S(1-S),\quad h=1/(2b),$$

反向 ramp 交换 $k_0,k_1$ 和 $b_0,b_1$，保留 eta、时长，将起点 omega 取为原 ramp 的真实公式终值。因为 $S(1-t)=1-S(t)$，这给 $k^R,h^R,\omega^R$ 的同号反向路径，且 $\omega_s^R=k_s^R/(2h^R)$。小型 Fraction toy 只核其三次原函数身份，没有评价候选几何。

验证时另行积分反向的冻结控制。若实际 P 的末框架为 A、位移为 v，则对任意 A 都有准确关系

$$A_R=DA^{-1}D,\qquad v_R=-DA^{-1}v.$$

脚本报告实际倒行结果与这两个公式的差，而不强行设 $A=D$ 或 $v_R=-v$。只有准确 $A=D$ 时才简化为 R45 的目标公式。

随后自然传播 `P,P,P_reverse,P_reverse` 的实际 frame 和位移，记录全四块位置、frame 及 omega 的真实闭合残差。没有把精确群元 D 用作数值接缝重置。

omega 沿四块连续携带；若浮点评价的 P 末 omega 有微小偏差，第二 P 和反向段的相应偏移全部报告，并用准确 xi 平移共轭公式记录对矩阵的影响。段内 omega 缓存的浮点接缝误差也保留，未认证其为数学零。

## 3. 冻结与加密

一组固定 N、八参数、全部桥控制、正 h、物理 xi 区间和归一化形成一个身份 SHA。设计使用绝对中心差分，列步长为 $2\cdot10^{-5}\max(1,|p_j|)$，并做独立方向差分。

选定之后，按同一控制的 $64/128/256$ 阶 Gauss 积分及每 ramp $96/192/384$ 个 frame 步加密，整个验证中不重新拟合端点、不改参数、不改 N、不改物理区间。

报告包含单 P 及完整四块的所有矩阵项、trace、自然闭合、倒行身份误差、未修正标量接缝、物理 gap 与 u 范围。所有“准确零算子、准确闭合、嵌入、reach”证书仍明确为 false；小残差不替代 R45 的存在证明。

默认命令：

```sh
python topics/visible-flex-new-mechanism/scripts/literature_single_P_instance.py \
  --turns 16384 --quadrature-n 64 --frame-n 96 \
  --validation-multipliers 1 2 4 --max-nfev 32 --design-seconds 300 \
  --out topics/visible-flex-new-mechanism/notes/single-P-instance.json
```

N 改变是新实体设计，不是同一几何的验证加密。这里的长整圈仍只是算子实验输入，不是本题厚度合格的闭面候选。

## 4. 如何接完整第四编译

公开 Actions 43615655870 已完成准确形式编译，实际需要 732 个实 s 历史、profile 四阶导数，以及 h、k 的三阶导数。该编译没有提供任何真实 P。当前脚本恰补一个**定义正确、残差如实保留**的 P 数据接口，仍不评价 profile 或第四 range。

未来的数值 P 只是近似零算子时，不得在每块重置二阶历史，也不得直接将四倍单 P 当成已认证完整周期；应同时检查完整四块真实累计结果。第四周期的准确单 P 约简以 R45 的准确条件为前提，数值缺陷必须单独保留。

本脚本的输出尚不能支持任何第四周期结论。下一步须冻结同一 profile、目标度量及输入 SHA，再评价完整编译的 period 与 ruling，并在同一参数下加密。

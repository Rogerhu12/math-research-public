# Phi 原最高 D2=0 整支：四原二次式的完整一元来源

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

状态：以下几何缩约已成；具体 QQ(u)[s] 来源尚未执行。新输入固定 60 秒 / 1 GiB，不重放原头、最高 Gaussian、P6/P9、范数或旧模块。

## 1. 原图与真正新的输入

只在完整 H1 排除后的当前 Phi=0、原物理 D≠0 图工作。原第一二次头已付，原 u、u−1、Q、delta=1−Q、ell、M 及原 f 的权分母已付。完整原三均值及 N1 使用
notes/2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py
中的 Rbar、W4、Obar、N1；保持全部低次原定义，取其最高部分时不换成数值替代式。

将 lambda、T、z 同赋次数 1。原三均值的 T²,Tz,z² 系数矩阵可逆，所以共同的非零无穷方向不能有 lambda 方向坐标为零：否则三个平方单项式皆零，从而 T=z=0。因此可在最高齐次式中规范 lambda=1，记 t=T/lambda、s=z/lambda。这个 projective 规范不在原仿射方程环中倒置物理 lambda。

[原最高 NV/F6 和严格 lift](../results/R150-appendix-unit211-Phi-zero-whole-first-head-highest-original-NV-F6-filtered-lift-and-twenty-one-generators.md)给
$$
D_2=2\ell-t^2,\qquad K_3=4\ell^2-6\ell t+2t^3,\qquad
\overline F_6=MK_3^2-4m^2D_2^3 .
$$
这里的 D2 是原 D 的最高部分；原 D≠0 **不**排除 D2=0 的无穷方向。

## 2. 整 D2=0 方向的严格几何缩约

在最高原共同零点上，若 D2=0，则已付 M 及 F6 给 K3=0。由 t²=2ell，
$$
K_3=2\ell(2\ell-t).
$$
ell 已付，故 t=2ell；再代 t²=2ell，得到
$$
\boxed{\ell=\tfrac12,\qquad t=1.}
$$
原 Phi 恒等式
$$
\ell=1-\frac{2(u-1)(u-2)}Q
$$
随即给整权曲线
$$
\boxed{Q=4(u-1)(u-2).}
$$
没有选择某个代数权点，也没有因原 D 单位删去该方向。原最高 NV 在此方向为零，因而本输入直接返回其余四个原二次条件，而不把 NV 的零返回作为新约束。

在整曲线上仍有
$$
M=-2(u-1)^2,\qquad \delta=1-4(u-1)(u-2).
$$
u−2 也成为已付单位，因为 Q=4(u−1)(u−2)，且 Q、u−1 已付。除此以外，不添加任何 u 因子的逆。

## 3. 四个真正原最高多项式

对四个原多项式 F_i，定义
$$
h_i(u,s)=[\lambda^2]\,
F_i\bigl(u,4(u-1)(u-2),\lambda,T=\lambda,z=\lambda s\bigr),
\qquad F_i=(Rbar,W4,Obar,N1).
$$
每个 h_i 对 s 至多二次。源码逐单项式构成完整 0、1、2 次分解，核回同一原式的最高部分；分母逐项剥已付 u、u−1、u−2、delta 后必须为非零有理常数。原定义只执行到构造 quads 之前，既不求逆原二次头，也不构造原三列矩阵或旧 cofactor。

新算术目标是在 QQ(u)[s] 中按上述四原式的固定顺序做完整 Euclid。每次准确除法均返回原乘积，四条 Bezout 来源一路保留，并实际核回
$$
g(u,s)=\sum_i a_i(u,s)h_i(u,s).
$$
若 g 仍有正 s 次数，只记录真实泛型方向及全部未决支，不宣判空。

## 4. 最后分母清回与完整例外支持

若 g=1，取所有最终 a_i 系数分母的最小公倍式 C(u)，并定义 beta_i=C a_i。源码必须逐系数返回
$$
\boxed{C(u)=\sum_i\beta_i(u,s)h_i(u,s).}
$$
这是完整原最高式的身份，在已付原权环中有效，包含中间 Euclid 主元的全部零面。随后仅剥第 2 节已经支付的因子，写 C=U C_*；C_* 完整 QQ 分解及乘回。

只有当 C_* 为非零常数时，才排除整 D2=0 的最高原共同零支。若 C_* 非常数，则保留其全部复根及每个完整 s 纤维；不同候选 u 值数至多为其不同不可约因子次数之和。这个数不被解释为原仿射点数、lambda 次数或整个 Phi 的解数。

完整 Phi、其它最高方向、C*/H19 权交集、原个别 N/P 和 D0 碰撞图均不因本次而自动关闭。

## 5. 固定源与唯一依赖

源文件：
notes/2026-11-28-unit211-Phi-zero-whole-D2-zero-infinity-original-four-quadratics-8542.py

最终 blob：321647e9cd06500e769bb0b6b8119659e4bd95fd。

8110 字节，SHA256：
baf684e40df5e447c6dfcb9f5eb3eef8173d28d6ae1a37e152c4475ff342b03c。

唯一依赖：
2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py，
SHA256 100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf。

前缀以唯一的 quads 构造行为边界；执行时输出前缀准确字节数与 SHA，只保存源、定义、次数和实际小回执。无历史系数 JSON、编码、分片或大输出。旧草稿 fd2d1e5839964cd7a770cd661b12bda42cd6bae9 从未执行；首次前仅将多项式单轴 degree 调用统一为已在依赖使用的 degrees 元组接口。

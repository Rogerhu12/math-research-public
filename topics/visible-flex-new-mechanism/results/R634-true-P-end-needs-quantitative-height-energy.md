# R634：真 P 端零迫使定量高度能量与 Volterra 范数超过阈值

2026-11-28；会话 `Astra-new-mechanism-8cdb3418-20261128`。
**已证明：R612 的任一非零真 P 端根必须满足下面的 B(h)>1，进而有
U>(h_min/h_max)²；在原物理盒内，四偶共同根必有 U>16/225。**
这把已知非恒高条件强化为定量必要条件；不声称后三端或完整 ruling 已解。

## 1. 原 P 的同一归一化与完整积分身份

沿用 [R612](R612-exact-physical-length-elimination-and-three-true-end-integrals.md)
的实际 h,k∈C²([0,1])、h>0、k(0)=0，物理时间 s=Lx，并保持

$$
\eta(x)=\int_0^x\frac{k_y}{2h}\,dy,\qquad d=h\eta-k,
\qquad K=\int_0^1 k^2,\quad U=\int_0^1(h_x/h)^2,
$$
$$
\boxed{P=-\int_0^1kd=\frac{A_{p_1}(L)}L.}
\tag{1}
$$

分部积分没有端余项，因为 k(0)=0：

$$
2\eta(x)=\frac{k(x)}{h(x)}+
\int_0^x\frac{h_y(y)k(y)}{h(y)^2}\,dy.
$$

在实 Hilbert 空间 L²(0,1) 上定义完整 Volterra 算子

$$
(T_hf)(x)=h(x)\int_0^x\frac{h_y(y)}{h(y)^2}f(y)\,dy.
\tag{2}
$$

于是

$$
\boxed{d=\frac{T_hk-k}{2},\qquad
P=\frac12\bigl(\|k\|_2^2-\langle k,T_hk\rangle\bigr).}
\tag{3}
$$

这里没有把 eta 当作独立变量，也没有用到 h 或 k 的单调性、同号性或有限
模态假设。h 变化处于相对较小的范围，不意味着其导数能量一定小。

## 2. 完整 Hilbert–Schmidt 阈值及严格性

令 m=min h>0、M=max h。核
`h(x)h_y(y)/h(y)^2` 乘 `1_{y<x}` 是平方可积的，因此 T_h 为紧的
Hilbert–Schmidt 算子，且其完整范数为

$$
\boxed{B(h)^2=\|T_h\|_{HS}^2
=\int_0^1\frac{h_y(y)^2}{h(y)^4}
\left(\int_y^1h(x)^2\,dx\right)dy.}
\tag{4}
$$

Cauchy–Schwarz 和算子范数界直接给，对所有 k，

$$
\boxed{P\ge\frac12(1-\|T_h\|)K
\ge\frac12(1-B(h))K.}
\tag{5}
$$

若 h 非常数，则 h_y 在某个开区间不为零。取该区间内先后分离的两个小区间
I₁、I₂，并分别取支撑其中的光滑 f₁、f₂，使
`∫ h_y f_j/h²` 非零；例如取非负非零 cutoff 乘 h_y。
在 I₁ 与 I₂ 之间，T_h f₁ 非零而 T_h f₂ 为零；在 I₂ 之后后者非零。
故两像线性无关，rank T_h≥2。紧 Hilbert–Schmidt 算子因此至少有两个非零
奇异值，最大奇异值严格小于全部奇异值平方和的平方根：

$$\|T_h\|<\|T_h\|_{HS}=B(h).\tag{6}$$

现在设 k 非零且 P=0。若 h 恒定，(3) 给 P=K/2>0，矛盾；所以 h 非常数。
由 (3) 还有 `〈k,T_hk〉=K`，故 `1≤‖T_h‖`。联同 (6) 得

$$\boxed{P=0,\ K>0\quad\Longrightarrow\quad B(h)>1.}\tag{7}$$

特别 B(h)≤1 时，任何非零 k 都不可能支付这个真端；在 B=1 的边界也不能
以 (5) 的非严格下界零冒称已经有零方向。B>1 仍只是必要条件：T_h 的最大
实二次型由 `(T_h+T_h^*)/2` 决定，可能仍小于 1。

## 3. 不依赖具体曲率的高度能量下界

记 `u=h_x/h`。式 (4) 给

$$
B(h)^2\le\left(\frac M m\right)^2
\int_0^1(1-y)u(y)^2\,dy
\le\left(\frac M m\right)^2U.
\tag{8}
$$

第一步只是逐点使用 `h(x)²/h(y)²≤(M/m)²`，没有删除有符号交叉项。
从 (7)(8) 可得更强的加权版本及其推论：

$$
\boxed{\int_0^1(1-y)(h_y/h)^2\,dy>
\left(\frac mM\right)^2,
\qquad U>\left(\frac mM\right)^2.}
\tag{9}
$$

在本题原盒 `.8<h<3` 内，m/M>4/15，故任意真 P=0、K>0 的曲线都满足

$$\boxed{U>16/225.}\tag{10}$$

若同时是 R612 的四偶共同根，其动能身份还给 `K−1=U/L²`。
原长度上界 L≤7.9 因而进一步推出

$$
\boxed{K>1+\frac{64}{56169}.}
\tag{11}
$$

这是对真共同根的必要定量空隙，不能反过来当成其余端或 ruling 的充分条件。

## 4. 对 R632 输入和恢复方向的实际含义

固定同一 h，把基础曲率 κ 乘任意非零实常数 a，会同时把 eta、d 乘 a，
所以 `P(h,aκ)=a²P(h,κ)`。因此
[R632](R632-true-kinetic-amplitude-chart-with-negative-center-branch.md) 的正动能
幅值 α 以及由 L 改变而导致的正 α，均不能改变基础 P 的符号或零性质。
它准确支付动能端，却不自动跨过 (7) 的真 P 障碍。

对任意常数 b>0，整体高度缩放 h↦bh 给 eta↦eta/b、d 不变，且
`T_{bh}=T_h`、`B(bh)=B(h)`、`U(bh)=U(h)`。所以整体 h 同质收缩可以修复
高度上盒和创造迭代空间，但它本身不改善 P；必须改变**相对高度形状**。

新 R632 求解保留所有实际 h 节点及导数自由度，正可在真实端梯度中改变这一
形状。本文不修改已冻结的首个计算范围，也不加入重复审计或额外机械门。
若用有限求积值观察 U 或 B，必须保留其数值误差性质：仅凭 sampled 高低值
或未经积分误差控制的近似 U，不能声称严格排除了某条实际曲线。
需要换输入时，(3) 给出构造真 P 零的明确二次型目标，而不是继续把 stored
端设零或只改变 κ 的幅值。

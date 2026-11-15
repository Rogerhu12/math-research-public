# 单调交换漂移的真实算子界与平滑后二次删除源的完整 MP 预算

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 结论

继续使用[加权交换二阶 commutator 和真 jet 两带稿](R271-appendix-weighted-exchange-second-commutator-two-jet-bands-and-heat-flag-decay.md)的原连续尾
$$
D=D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad
\mathcal L=\sum_{i\ge x}(I-V_i),\qquad
\mathcal T=e^{-x\mathcal L/4},
$$
以及实际交换形式
$\mathfrak e(v)=\sum_{i\ge x}\|P_i^-v\|^2$。

本文用硬核 occupation 的真实望远镜，证明
$$
\boxed{
\|(\mathcal L-\mathcal L^*)v\|
\le\frac8{\sqrt x}\mathfrak e(v)^{1/2}
+\frac4x\|v\|.
}
\tag{0.1}
$$
这是算子向量范数界，不只是 numerical-range 估计；常数与孔数、jet 长度及窗口均无关。因而
$$
\operatorname{Dom}\mathcal L=\operatorname{Dom}\mathcal L^*,\qquad
\|\mathcal L^*v\|\le2\|\mathcal Lv\|+\frac{20}{x}\|v\|,
\tag{0.2}
$$
反向同式亦成立。特别，
$$
\boxed{\|\mathcal L^*\mathcal T\|<90/x.}
\tag{0.3}
$$

对任意固定孔层的真正 primitive $f\in\ker D$，记
$$
\mathcal C_1=[D,\mathcal L^*],\qquad
\mathcal C_2=[D,[D,\mathcal L^*]].
$$
则同一个真实可行向量 $y=\mathcal L^*\mathcal Tf$ 同时给
$$
Dy=\mathcal C_1\mathcal Tf,\qquad
D^2y=\mathcal C_2\mathcal Tf,\qquad D^3y=0.
$$
所以完整真 MP 预算为
$$
\boxed{
D^\dagger\mathcal C_1\mathcal Tf
=P_{(\ker D)^\perp}\mathcal L^*\mathcal Tf,
\qquad
(D^2)^\dagger\mathcal C_2\mathcal Tf
=P_{(\ker D^2)^\perp}\mathcal L^*\mathcal Tf,
}
\tag{0.4}
$$
两列范数都小于 $90\|f\|/x$。这里保留完整最小化；第二列不是顺次 $D^\dagger D^\dagger$。

## 1. 反自伴漂移的配置行

置
$$
s_i=\sinh(2\theta_i),\qquad
\theta_i=\log\frac{i+2}{i+1}.
$$
$s_i>0$ 单调下降且趋零。真实局部矩阵给
$$
\mathcal A:=\mathcal L-\mathcal L^*
=-2\sum_{i\ge x}s_iH_iU_i,\qquad H_i=n_{i+1}-n_i.
\tag{1.1}
$$
先在固定孔层的有限支撑核心上计算。用有限物理子集 $I$ 标记配置，$I^i$ 是交换 $i,i+1$ 后的配置，$n_j(I)\in\{0,1\}$。则
$$
\begin{aligned}
(\mathcal Av)(I)
={}&-2\sum_{i\ge x}s_i\bigl(n_{i+1}(I)-n_i(I)\bigr)
\bigl(v(I^i)-v(I)\bigr)\\
&+m(I)v(I),
\end{aligned}
\tag{1.2}
$$
其中
$$
\begin{aligned}
m(I)
&=-2\sum_{i\ge x}s_i\bigl(n_{i+1}(I)-n_i(I)\bigr)\\
&=2s_xn_x(I)
-2\sum_{j\ge x+1}(s_{j-1}-s_j)n_j(I).
\end{aligned}
\tag{1.3}
$$
每个配置只有有限多个占据，故上述望远镜准确成立。由于 $0\le n_j(I)\le1$ 且 $s_{j-1}-s_j\ge0$，
$$
|m(I)|\le2s_x\le4/x.
\tag{1.4}
$$
此处保留了全部双占据的抵消；没有把逐位下降梯度误当成交换梯度。

记 (1.2) 的第一行为 $\mathcal Bv$。每个配置行上的 Cauchy--Schwarz 给
$$
|(\mathcal Bv)(I)|^2
\le4\left(\sum_{i\ge x}s_i^2\right)
\sum_{i\ge x}|v(I^i)-v(I)|^2.
$$
对 $I$ 求和，用
$\sum_i\|(U_i-I)v\|^2=4\mathfrak e(v)$，
得到
$$
\|\mathcal Bv\|^2
\le16\left(\sum_i s_i^2\right)\mathfrak e(v)
\le\frac{64}{x}\mathfrak e(v).
\tag{1.5}
$$
结合 (1.4) 即为 (0.1)。有限孔层延拓及自然闭形式极限给全部陈述域。

## 2. 两个闭发生器具有同一自然域

原实部界
$$
\operatorname{Re}\langle\mathcal Lv,v\rangle
\ge2\mathfrak e(v)-\frac2x\|v\|^2
$$
给
$$
\mathfrak e(v)^{1/2}
\le2^{-1/2}\|\mathcal Lv\|^{1/2}\|v\|^{1/2}
+x^{-1/2}\|v\|.
$$
代入 (0.1)，再用
$$
\frac{4\sqrt2}{\sqrt x}
\|\mathcal Lv\|^{1/2}\|v\|^{1/2}
\le\|\mathcal Lv\|+\frac8x\|v\|,
$$
得到
$$
\|(\mathcal L-\mathcal L^*)v\|
\le\|\mathcal Lv\|+\frac{20}{x}\|v\|.
$$
故 (0.2) 成立。由于 $\operatorname{Re}\mathcal L^*=\operatorname{Re}\mathcal L$，同一证明可将 $\mathcal L,\mathcal L^*$ 互换。

先在每个固定孔层使用这些共同常数，再对孔层作平方和，可严格得到闭直和的两个域相同。这里未假设 $\mathcal L$ 在全空间有界。

## 3. 同一个热算子的正向和反向发生器预算

已付热平滑稿给
$$
\|\mathcal T\|\le e^{1/2},\qquad
\|\mathcal L\mathcal T\|\le8e^{3/2}/x,\qquad
\mathfrak e(\mathcal Tv)\le(4e^2+e)x^{-1}\|v\|^2.
$$
由 (0.1)，
$$
\|\mathcal L^*\mathcal Tv\|
\le\frac{8e^{3/2}+8\sqrt{4e^2+e}+4e^{1/2}}{x}\|v\|
<\frac{90}{x}\|v\|.
\tag{3.1}
$$
例如 $e<11/4$ 使分子小于
$13\sqrt{11}+8\sqrt{33}<90$，故常数无需数值实验。

更一般，令 $c_k=e^{3/2}k!8^k$，则 (0.2) 和全阶热界给
$$
\|\mathcal L^*\mathcal L^k\mathcal T\|
\le (2c_{k+1}+20c_k)x^{-k-1}.
\tag{3.2}
$$
这也是同一个热算子的混合顺序估计；不交换 $\mathcal L$ 与 $\mathcal L^*$。

## 4. 原 primitive 上同一二次删除源的真最小预像

固定远孔层 $p$，取 $f\in\ker D_p$。由于 $\mathcal T$ 与原 $D$ 对易，$g=\mathcal Tf$ 仍为同层 primitive。令 $y=\mathcal L^*g$。由真实 commutator 恒等式
$$
Dy=\mathcal C_1g,\qquad D^2y=\mathcal C_2g,
$$
且 $\operatorname{ad}_D^3(\mathcal L^*)=0$ 给 $D^3y=0$。其中二次源完全显式：
$$
\mathcal C_2
=2\sum_{i\ge x}
\frac{(b_i^2-b_{i+1}^2)^2}{b_ib_{i+1}}E_iE_{i+1}.
\tag{4.1}
$$
该源本身与 $D$ 对易，因此 $\mathcal C_2g$ 是 $p-2$ 层 primitive（$p<2$ 时为零）。

对实际固定层的完整算子 $D$ 或 $D^2$，合法预像 $y$ 的最小范数部分正是其正交核补投影。因此 (0.4) 是准确恒等式，结合 (3.1) 得
$$
\|D^\dagger\mathcal C_1\mathcal Tf\|^2
\le8100x^{-2}\|f\|^2,
$$
$$
\|(D^2)^\dagger\mathcal C_2\mathcal Tf\|^2
\le8100x^{-2}\|f\|^2.
\tag{4.2}
$$
完整两个分量还由同一个 $y\in\ker D^3$ 正交拆分：
$$
D^\dagger\mathcal C_1\mathcal Tf
=F_2y+F_3y,\qquad
(D^2)^\dagger\mathcal C_2\mathcal Tf=F_3y.
\tag{4.3}
$$
所以这些费用没有独立换源或先压缩后求逆。

## 5. 尚未跨越的原返回接口

(4.2) 只给明确的联合源 $\mathcal C_1\mathcal Tf,\mathcal C_2\mathcal Tf$。它不把 $\mathcal C_2$ 换成原三次删除 $D_3=\sum b_i^3E_i$，不把完整 $(D^2)^\dagger$ 换成顺次 $D^\dagger D^\dagger$，也不证明原 $\mathscr A_n\mathcal T$ 的完整费用。

该区别是必要的：真实 $F_3y$ 已由 (4.3) 支付，但顺次预像可能另有 $F_2$ 返回。后续必须继续保这个同源返回及 actual $u_Q$ 的两端 partial，而不能把原全谱 inverse 障碍误当成本文这两条特定源列的障碍。

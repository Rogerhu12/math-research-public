# 将旋转背景曲率界扩展到整个 cell 0

2026-11-09，`/root/independent_geometry`。完整推导，待未参与者独审。本文只处理同一个精确解析旋转背景；不把它与保存的非轴对称显式尾混同。

## 1. 已支付输入

采用 `2026-11-09-db6f-audit-positive-radial-alpha.md` 中冻结的有限 source 几何和精确径向宽度归一参数。其 Fraction 账本已给严格 $\alpha>7$；该正性证明已由 tail_theory 独审及独立复跑。

背景高度粗界 `2026-11-09-db6f-tail-background-height-bound.md` 给全尾 $w\le16/15$，cell 0 最后 raw 平段还满足 $w<5/9$。所有半径 $r>a_c>7/50$。固定参数还给 $r_{cut}>59/100$、$r_{old}<4/25$，所以

$$r_{cut}/r_{old}>59/16.$$

R15 已给 cell $n\ge1$ 及未修改无限源的实际主曲率绝对值不超过 6。现在只需处理 cell 0。

## 2. cell 0 除最后 raw port 外

这些段的 $\chi=1$，包括 cut-preserving 的恢复过渡段。固定正权重 $\omega>0$，因此

$$v_r=\frac{|w_x|}{6E^{3/2}}+\alpha\frac{r'_o\omega}{E},\qquad E=1+w^2,$$

直接给

$$|\kappa_r|=\frac{|w_x|}{v_r E^{3/2}}\le6.$$

这一点不依赖 cap 的大小，也不依赖恢复段的导数是否单调。

## 3. 最后的 raw port

写 $t=S(x)\in[0,1]$。源实现给

$$\chi=1-t,\qquad j_0=1+(r_{cut}/r_{old}-1)t,\qquad\omega=1.$$

原 source 在这段的 $w r_o^7$ 为常数，故

$$w_{r_o}=-7w/r_o.$$

定义无量纲量

$$q=\frac{|w_x|}{6E^{3/2}r'_o}
=\frac{7w}{6r_o(1+w^2)^{3/2}}.$$

函数 $w/(1+w^2)^{3/2}$ 的全局最大值为 $2/(3\sqrt3)<2/5$，再用 $r_o>a_c>7/50$，得到 $q<10/3$。

另一方面，$w<5/9$ 给 $E<106/81<4/3$，于是 $\alpha/E>21/4$。因此

$$\begin{aligned}
\frac{v_r-|w_x|/(6E^{3/2})}{r'_o}
&=t(j_0-q)+(1-t)\alpha/E\\
&>\frac{21}{4}-\frac{91}{12}t+\frac{43}{16}t^2.
\end{aligned}$$

右侧在 $[0,1]$ 严格递减，因为导数至多 $-53/24<0$；在 $t=1$ 的值为 $17/48>0$。因此整个最后 port 都有

$$v_r>|w_x|/(6E^{3/2}),\qquad |\kappa_r|<6.$$

这同时覆盖 $\chi\to0$ 的 cut 端；不需要错误地假设旧 source 的曲率本来小于 6。

## 4. 全尾的角向曲率

旋转图的另一主曲率满足

$$|\kappa_\theta|=\frac{w}{r\sqrt{1+w^2}}.$$

由 $w\le16/15<4/3$ 及单调性，有 $w/\sqrt{1+w^2}<4/5$。于是

$$|\kappa_\theta|<\frac{4/5}{7/50}=40/7<6.$$

综上，**同一个精确解析背景的整个尾，包括 cell 0、保护端及无限原 source，均满足 $|\kappa_i|\le6$**。已有 C² 接合论证不变：正 free term 保证径向速度不退化，$w_x/v_r$ 在 cusp 连续，深端 $w,w_r\to0$。

这条背景界可作为实际非轴对称有限尾的 perturbation 认证输入，但实际 $F=F_{rot}+V$ 的曲率、共同 metric 与完整曲面仍需独立控制，不能直接继承背景的数值 6。

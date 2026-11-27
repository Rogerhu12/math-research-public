# 六位出生一 half：完整精度的六次 companion 新输入

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f / stable_kernel_return。

**状态：以下来源映射、完整特征系数目标与判据是纸面恒等式；所附新源码尚未实际运行，六位 half 尚未证明。** 本输入使用原六位整个矩阵，不重算或假设旧满支持 $M_6$ 的正性。

## 1. 原物理来源

令 $b_i>0$（$1\le i\le6$），$z_i=b_i^2$，$b=(b_i)$，$K=b^\perp$。在物理一孔层令 $T_0=\operatorname{diag}z_i$、$Q_0=bb^*$，并写 $S=e_1(z)$、$Z=e_2(z)$、$W=e_3(z)$。已刊完整出生一精度式给
$$
F_1=SI-2T_0+Q_0,\qquad
F_2=ZI-2ST_0+3T_0^2+SQ_0-T_0Q_0-Q_0T_0,
$$
$$
C_2=F_1-\frac{(S-T_0)Q_0(S-T_0)}{Z},
$$
$$
C_3=F_2-\frac{(Z-ST_0+T_0^2)Q_0(Z-ST_0+T_0^2)}{W}.
$$
它们分别是完整 $\Gamma_{1,1}^{-1}$、$\Gamma_{2,1}^{-1}$ 在 $\mathbb Cb$ 上的零延拓。下标沿此前 half 稿，避免与 R275 上源 $C_1,C_2$ 混淆。

所需六位 half 等价于
$$
H=C_2^2-2C_3\succ0\quad\hbox{在 }K\hbox{ 上}.
$$
确实，对 $\Gamma_1\Gamma_2^{-1}\Gamma_1\prec I/2$ 作同一 $\Gamma_1^{-1}$ 的同余即得此式。令
$$
J=Z^2W\,H.
$$
$Z^2W>0$，所以 $J|_K$ 与目标符号完全一致。

## 2. 完整相似后才除去真零线

先经物理去权坐标，$T_0$ 的算子坐标为 $\operatorname{diag}z_i$，$Q_0$ 为 $\mathbf1(z_1,\ldots,z_6)$；内积为 $\operatorname{diag}z_i$。在互异 $z_i$ 上再用六点求值基 $1,x,\ldots,x^5$。乘 $x$ 的完整伴随矩阵 $\mathcal T$ 具有最后一列
$$
(-e_6,e_5,-e_4,e_3,-e_2,e_1)^{\mathsf t},
$$
及五个下副对角的 $1$。$\mathcal Q$ 只有第一行非零，为
$(p_1,\ldots,p_6)$，其中 $p_j=\sum_i z_i^j$ 按 Newton 身份写成 elementary 多项式。这是真正相似，未把普通转置当物理伴随。

将上节全部公式中的 $T_0,Q_0$ 替换为 $\mathcal T,\mathcal Q$。令
$$
\mathcal A=Z F_1-(S-\mathcal T)\mathcal Q(S-\mathcal T),
\quad
\mathcal G=Z-S\mathcal T+\mathcal T^2,
$$
则完整无分母矩阵恰为
$$
\boxed{J=W\mathcal A^2-2Z^2W F_2+2Z^2\mathcal G\mathcal Q\mathcal G.}
$$
$J$ 的第一列恒零，正是已付的 $C_2b=C_3b=0$。只有形成这个完整矩阵并核实该恒等式以后，才取右下 $5\times5$ 块 $\widehat J$，即商掉这个实际不变零线。因此
$$
\det(tI_6+J)=t\det(tI_5+\widehat J).
$$
五个商特征值就是物理 $J|_K$ 的实特征值；没有先删源再取 MP。

## 3. 新原计算与完整判据

新源码按 Faddeev–LeVerrier 计算
$$
\det(tI_5+\widehat J)
=t^5+c_1t^4+c_2t^3+c_3t^2+c_4t+c_5.
$$
每个 $c_k$ 的 elementary 加权次数为 $9k$。每一步立即保存全部整数系数，仅除去明确正整数内容和 elementary 单项式因子；这两项都在正权上严格正。源码还保留：

- 每次精确整数除法和全部加权次数；
- 六位等权时的同一物理身份 $c_k=\binom5k18000^k$；
- 最后完整五维 Cayley–Hamilton 余矩阵为零；
- 每阶完整系数和 SHA256，部分完成不会被标作全部正性。

若全部五个 $c_k(z)>0$ 对所有正权成立，则 $J|_K$ 的实谱不能有负特征值：否则 $t=-\lambda>0$ 使上述全部正系数多项式为零，矛盾；$c_5>0$ 又排零特征值。因此六位 half 严格成立。若 elementary 系数有负项，只表示该充分系数检验未闭，必须接同一保存多项式的真实正权正性，不能当作矩阵反例。

资源界固定为内层 180 秒、地址空间 4 GiB。这个新输入不复跑旧六位满支持流，也不重算已经闭合的五位 S2。当前不声称六位 half、七位来源或普通 ISP 已完成。

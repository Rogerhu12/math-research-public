# R154：原 cell7 非零中心的完整复均值域

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-13。

**已证明（实际 Arb 证书，原 1247 个整叶全部覆盖）。** 本文核销原 R75 的完整均值根及完整角分母的域，中心是此前已实际传播的同一个有符号线性参考场 $L_R$。不把齐次参考场称作非线性解，也不宣称尚未支付的非线性修正已经留在下述域内。

## 1. 固定对象和范数

原 cell7 的度量、全部九段 source、真实半径、真实 $w$、原 node10 高度和原线性系数全部不变。原 256-bit / Taylor order 24 / remainder 100 / root 160 的成功传播未重算。输入固定为原 cell7 primary `90f6ef97…` 与 cell8 primary `062a9ed7…`，后者提供真实进入 cell7 的同一 projective 列。

在任一原闭叶 $I$ 上记

$$
\|f\|_{j,\sigma,I}=\sum_{m\in2\mathbb Z}(1+|m|)^j e^{\sigma|m|}\sup_{x\in I}|f_m(x)|,
\qquad \sigma=1/64.
$$

强 tube 为

$$
\|\delta P\|_{1,\sigma,I}+\|\delta\bar K\|_{1,\sigma,I}\le\eta=1/16.
\tag{1}
$$

扰动可以含全部无限非零偶频，且可以为复数；$P$ odd、$\bar K$ even，均无零模。中心是有限的真实 $L_R$，不是选取保存区间的浮点中点。式 (1) 可同时用于所有原叶，形成分区 block-max Banach 范数；全胞元 radial-first 强范数不超过 $\eta$ 当然也满足它。

各材料源界是逐叶的 radial-first 弱范数。对各叶取最大仅给 block-max 范数，**不**等于全胞元先取径向 sup 再求所有频率之和的同一常数。下游强迫须逐叶消费保存的正预算，或另付合法的全胞元汇总。

## 2. 仅收紧真实物理读出，不重做传播

原每叶已保存完整 $\ell=(\log w)_x$ 区间 $[\ell_-,\ell_+]$，原叶长为 $\Delta$，并有原闭式在两端的真实 $w_l,w_r$。故对整个叶都成立

$$
w(x)\in w_l\exp([0,\Delta][\ell_-,\ell_+]),
\qquad
w(x)\in w_r\exp([-\Delta,0][\ell_-,\ell_+]).
\tag{2}
$$

两者与旧整叶 $w$ 包取交仍包围同一个真 $w$，不依赖 $\ell$ 的符号，也不丢掉原转折小叶。源值在准确有理端点直接包围；没有新的径向积分。

从原 cell8 出口 projective 列出发，按原有顺序乘每个已保存的 signed endpoint 矩阵。叶内部分矩阵仍为原 $I+[0,M]$ 加原 balanced 尾 $q^2/(1-q)$。所有 $r,r_x,\ell$ 和尾门照旧；只将读出分母 $\sqrt{rw^3}$ 换成 (2) 的更紧真包，然后与旧整叶中心包取交。每段末与原保存的 endpoint 列逐项相交，再恢复该原列继续。这是同一连续 $L_R$ 的有效区间限制和放宽，不是更换中心或消掉误差。

实际读出的中心弱 $K$ 范数在所有叶上小于 $0.067552895$，相关量 $\bar K+E P_\theta$ 的弱 $\sigma$ 范数小于 $0.069647245$。旧 coarse 读出中出现的约 $0.85166$ 弱帽及 $2.6682$ 全胞元强帽因此不能被当成实际场的幅度下界。

## 3. 完整均值的无消去恒等式

沿用 R64、R75，$z=w^2$，$E=1+z$，$K=c+\bar K$，$T=P_\theta$，并置

$$
A=2K+K^2+EP^2,\quad S=1-zP^2,\quad D=1-zA,\quad L=1+K+ET,
$$

$$
C(u)=(1-u)^{-1/2},\qquad C_1(u)=\frac{C(u)-1}{u},\quad C_1(0)=1/2.
$$

完整 mean 算子准确为

$$
\mathcal M(c)=\left\langle A C_1(zA)+\frac{(1+K)T}{S}C(zA)\right\rangle
=c+\frac{c^2}{2}+q_0+\mathcal R(c),
\tag{3}
$$

$$
q_0=\left\langle\frac{\bar K^2+EP^2}{2}+\bar K T\right\rangle.
$$

零 Fourier 系数由完整二次卷积的准确公式支付。对中心 $P=\sum p_m\sin m\theta,\bar K=\sum k_m\cos m\theta$，实际使用

$$q_{0,c}=\frac14\sum_m(k_m^2+Ep_m^2)+\frac12\sum_m m k_mp_m,$$

保留原 signed 区间及其相消。没有有限角采样，亦没有把 $\langle\Omega\rangle-1$ 除以浮点极小 $z$。

## 4. 全复扰动和完整无穷余项

设 $p,k,t$ 为中心的弱 $P,\bar K,P_\theta$ 帽。对式 (1) 的全频扰动，写 $R_P+R_K\le\eta$。非零偶频给弱 $P,K$ 费用各不超过对应 $R/3$，而 $\|\delta P_\theta\|_0\le R_P$。于是

$$
|q_0-q_{0,c}|
\le\eta\max\left\{\frac{Ep}{3}+k,\frac{k+t}{3}\right\}+\frac{\eta^2}{8}.
\tag{4}
$$

其中二次部分先按
$E R_P^2/18+R_K^2/18+R_PR_K/3$ 支付。在 $E\le5/4$ 下，该粗式的最大值为 $31\eta^2/270<\eta^2/8$。式 (4) 无额外 pair 因子。

取 $|c|\le d=1/8$，令 $p_*,k_*,t_*$ 包含 tube 误差，

$$
A_* =2(k_*+d)+(k_*+d)^2+Ep_*^2,\quad
U=zA_*,\quad V=zp_*^2,\quad Y=(1+d+k_*)t_*.
$$

R64 的无相减正函数

$$
f(q)=\frac{q(2+\sqrt{1-q})}{2\sqrt{1-q}(1+\sqrt{1-q})^2},\qquad
 g(q)=\frac{q}{\sqrt{1-q}(1+\sqrt{1-q})}
$$

给整个复圆盘上的完整余项

$$
|\mathcal R(c)|\le A_*f(U)+Y\frac{g(U)+V}{1-V}.
\tag{5}
$$

所有叶实际核过 $U,V<1$，同样核过完整角宽 $\sigma$ 上的 $U_\sigma,V_\sigma<1$。因此 (3) 在整个 $c$ 圆盘及全复 tube 上全纯，完整平方根和逆都保留。

## 5. 唯一简单根、全实分支与角逆

每个原叶都严格满足

$$
|q_{0,c}|+\text{式 (4) 的费用}+d^2/2+\text{式 (5) 的费用}<d.
\tag{6}
$$

实际最坏左端小于 $0.013618684$，而 $d=0.125$。Rouché 定理说明完整 $\mathcal M$ 在圆盘内有且仅有一个零点，计重数为一；所以它简单，随复非均值场全纯变化。实输入由共轭唯一性给同一个实根。进一步

$$
|c|\le\frac{|q_0|+|\mathcal R|}{1-d/2}<0.006193263.
$$

各叶公共端点的根由同一圆盘中的唯一性一致。对于具有相应径向连续性及导数的输入，隐函数定理给原完整 mean 的连续性及导数。

实际另逐叶核销 R75 的全部实门，而不把 Rouché 当成这些门的替代：

$$
S>0.9999999996,\quad D>0.9999997573,\quad
 y>0.7866137,\quad L>0.7450307,\quad N>0.9999999445.
$$

完整实导数 $\mathcal M_c=\langle L/D^{3/2}\rangle>0.7450307$。这些十进制界仅作向外展示，原 dyadic 下界随实际包保存。

角向逆采用弱 Wiener 代数。相关完整系数 $k_m+Em p_m$ 先合成，再取绝对帽。实际

$$
1-d-\|\bar K_c+E(P_c)_\theta\|_{0,\sigma,I}-E\eta
>0.7428527.
$$

因此整个 tube 的 $L^{-1}$ 在同一正角宽上有完整 Wiener 逆，没有把只有实角的正性冒作复条带分母门。

## 6. 两材料完整非线性接口

记 $U_f=K_\theta-P$，原相对物理 source-x 方程的完整源为

$$
\mathcal N=\Pi_\perp\frac{EsU_f^2+
\ell[(K+T)^2+z(2KT+T^2-P^2)]}{L}.
\tag{7}
$$

它可按 $s$ 和 $\ell$ 两材料分别消费。每叶保存完整弱 $\sigma$ 源帽 $N_s,N_\ell$；其 block-max 分别小于 $0.056090511$ 和 $0.104481695$。这些是式 (7) 的**相对 source-x**材料系数；若换为物理 $\kappa$ 源必须按原方程另乘真实 $w$。它们没有额外 $r_x$，也不是旧内侧 $V'^2/(rw)$ 材料的无条件替换。

均值取式 (3) 的完整根，零模只在最后由 $\Pi_\perp$ 投影。式 (7) 的平方根/逆间接费用、完整无限扰动及全部均值依赖均已在前面的域门支付。源帽保持两材料分开，未将两个不相关径向上界的最大值冒成共同频谱帽。

这给出了下一次非线性强迫和线性化所需的实际合法域。仍须另证真实非线性解的强迫积分及误差留在 tube 内；原外侧全部 $0,\ldots,9$ 延拓、无限高传播、闭面和全 $t$ 结论均未由本证书获得。

## 7. 实际数据和可复现性

原 9 段共 1247 个成功叶全部消费。77,060 个输入、覆盖、有限、同列、完整 mean 和实/复正域门通过，实际正式退出 0；主程序 120.222 秒，wait4 总计 126.085 秒，峰值 50,704 KiB。原所有 ODE、Taylor 阶数、remainder、root 精度和旧成功包保持原值。

primary `d9c11913…` 保存每个叶的完整根、分支、逆和两材料源预算；78 个可约两分钟重建的 refined signed profile 分片共 2,193,958 字节留在 scratch，原 SHA 和再生算法全部保存。稳定 manifest 绑定 source、primary、正式资源和本证明。独立几何代理已核过式 (2) 的同对象交集/重放以及式 (4)–(6) 的均值论证，没有要求改变任何数值门。

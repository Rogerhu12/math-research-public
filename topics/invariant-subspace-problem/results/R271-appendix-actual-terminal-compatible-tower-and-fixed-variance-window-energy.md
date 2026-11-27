# 原实际终列的逐高度 Bernoulli 预算与同一 forcing 的固定方差窗真核费用

日期：2026-11-27（Asia/Taipei）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：本文完整支付原相容塔一直到真实终列 $L=h-1$ 的逐高度范数，并把同一实际 forcing 的有限孔真核误差控制为同一头上的一个固定对数方差窗能量。它不要求短核投影或头相似条件数。尚未证明该 moving-head 能量窗趋零，也没有把模型真核运输成原全局 $N=\overline{B\ker T}$。**

继续使用[同一 Bernoulli 条件池精确塔](R271-appendix-compatible-bernoulli-vacuum-towers-and-same-test-exact-kernel-approximation.md)和[固定基数负相关稿](R271-appendix-fixed-cardinality-negative-correlation-near-optimal-compatible-vacuum-towers.md)的原对象。旧的近最优短窗结论保持不变；本条不声称高终列近最优，改为逐高度的固定指数费用，并在同一来源上准确付清它。

## 1. 原完整尾、同一个条件事件与本条参数

取整数 $x\ge4$，
$$
D_x=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad
z_i=b_i^2,\quad S=S_x=\sum_{i\ge x}z_i,\quad t=z_x.
$$
沿用原独立 Bernoulli 池 $\mathcal P$：
$$
p_i=z_i/t,\qquad N=|\mathcal P|,\qquad
\lambda=\mathbb EN=S/t.
$$
$N$ 几乎处处有限，且 $p_x=1$。令 $P_k=\Pr(N\ge k)$，
约定 $P_0=1$。全部 $P_k>0$。

本条取
$$
x\le L\le2x,\qquad
\mathcal A=2^{22}.                                    \tag{1.1}
$$
所有高度 $0\le r\le L$ 仍对同一个事件 $N\ge L$ 条件化：
$$
v_r=\mathbb E\left[
 \frac1{(N)_{\underline r}}
 \sum_{\substack{J\subset\mathcal P\\|J|=r}}b_J^{-1}e_J
 \ \middle|\ N\ge L\right].                            \tag{1.2}
$$
零阶 $v_0=\Omega$。旧逐坐标计数给
$$
D_xv_r=v_{r-1},\qquad
\langle v_r,\omega_r\rangle=1,\quad
\omega_r=(D_x^*)^r\Omega,\quad
\sigma_r^2=\|\omega_r\|^2=(r!)^2e_r(z).                 \tag{1.3}
$$
下节重新给本参数中的实际 Hilbert 范数预算，不要求先有条件随机向量的 Bochner 可积性。

## 2. 稀有条件事件的逐步尾概率比

**引理。** 在 (1.1) 的整个区间，原同一池满足
$$
\boxed{\frac{P_{k-1}}{P_k}\le626\qquad(1\le k\le L).}   \tag{2.1}
$$

取固定块
$$
F=\{x+1,\ldots,x+2L\},\qquad |F|=2L.
$$
这些位均有 $0<p_i<1$，并且
$$
p_i\ge\left(\frac{x+1}{x+2L+1}\right)^4
\ge\frac1{625}.                                      \tag{2.2}
$$
先在包含 F 的有限 Bernoulli 系统中计数；$p_x=1$ 的确定坐标原样保留。
对每个基数为 $k-1$ 的状态，在 F 中至少有 $2L-k+1$ 个空位。
加入其中一个位 i 时，状态概率乘以
$p_i/(1-p_i)\ge1/625$。
每个基数为 k 的输出状态最多被 k 个前态计数。因此
$$
k\Pr(N=k)\ge
\frac{2L-k+1}{625}\Pr(N=k-1).
$$
当 $k\le L$ 时，
$$
\Pr(N=k-1)\le625\Pr(N=k)\le625P_k.
$$
于是 $P_{k-1}=P_k+\Pr(N=k-1)\le626P_k$。
有限系统扩大到原可数池时，N 单调趋于有限的原基数，所有涉及的固定基数及尾概率收敛，故 (2.1) 保持。确定的第 x 位没有被加入或除以 $1-p_x$，所以不存在该位的除零问题。

迭代同一原尾概率比得到
$$
\boxed{P_{L-r}/P_L\le626^r\qquad(0\le r\le L).}        \tag{2.3}
$$
这正是保逐高度费用的步骤；不再把统一的 $P_L^{-1}$ 费用付到所有低层。

## 3. 真实终列中每一层的固定指数预算

对 $|J|=r\ge1$，原准确系数为
$$
(v_r)_J=
\frac{b_J}{t^rP_L}
\mathbb E\left[
 \frac{\mathbf1_{\{N_{J^c}+r\ge L\}}}
 {(N_{J^c}+r)_{\underline r}}\right].
$$
在该事件上分母至少为 $(L)_{\underline r}$，而
$\Pr(N_{J^c}\ge L-r)\le P_{L-r}$。由 (2.3)，
$$
0\le(v_r)_J\le
\frac{626^r b_J}{t^r(L)_{\underline r}}.                \tag{3.1}
$$
又
$$
e_r(z)\le S^r/r!,\qquad
(L)_{\underline r}\ge(L/e)^r.                         \tag{3.2}
$$
第二式可由递减序列 $\log L,\ldots,\log1$ 的前 r 项平均不小于全部 L 项平均，
再用 $\log L!\ge L\log L-L$ 得到，包含 $r=L$。

原积分界给
$$
\lambda=\frac{S}{t}
\le\frac{(x+1)^4}{3x^3}\le x\le L
\qquad(x\ge4).
$$
于是 (3.1)--(3.2) 给
$$
\|v_r\|^2
\le\frac{(626e\,\lambda/L)^{2r}}{r!S^r}
\le\frac{(626e)^{2r}}{r!S^r}.
$$
用 $e<3$ 及 $9\cdot626^2<2^{22}$，得到整个原终列的明确预算
$$
\boxed{
\|v_r\|^2\le\frac{\mathcal A^r}{r!S^r}
\qquad(0\le r\le L),\qquad\mathcal A=2^{22}.}           \tag{3.3}
$$
零阶直接为等号。这里先按非负坐标求和证明 Hilbert 收敛，再由原有限池计数、非负 Tonelli 及 $D_x$ 有界性得到 (1.3) 的实际 Hilbert 等式。

特别 $1\le\sigma_r\|v_r\|\le\mathcal A^{r/2}$。
本文不把右边称作近一估计；实际碰撞范数 $\sigma_r$ 没有从交叉 Gram 身份中删去。

## 4. 同一个完整有限头：真终列的三个 Gram

令原有限头 $C$ 满足 $C^h=0$，取真正的
$$
L=h-1,\qquad x\le h-1\le2x.
$$
定义
$$
\mathscr R a=\sum_{r=0}^L(-C)^ra\otimes\frac{\omega_r}{\sigma_r^2},
\qquad
\mathscr T a=\sum_{r=0}^L(-C)^ra\otimes v_r,
$$
$$
H_{\rm coh}=\mathscr R^*\mathscr R,\qquad
H_{\rm tow}=\mathscr T^*\mathscr T,\qquad
H_C(v)=\sum_{r=0}^L\frac{(C^*)^rC^r}{r!v^r}.           \tag{4.1}
$$
相容性与真实末端 $C^{L+1}=0$ 给
$$
\boxed{(C+D_x)\mathscr T a=0\quad\text{对全部原头来源 }a.} \tag{4.2}
$$
此处没有再投到一个短 $\ker C^{r+1}$。

由 (1.3)，
$$
\mathscr R^*\mathscr T=H_{\rm coh}.
$$
同层 Cauchy–Schwarz 及 $\langle v_r,\omega_r\rangle=1$ 给
$\|v_r\|^2\ge\sigma_r^{-2}$。结合
$\sigma_r^2\le r!S^r$ 和 (3.3)，得到全部完整原物理 Gram 的有序链
$$
\boxed{
I\preceq H_C(S)\preceq H_{\rm coh}
\preceq H_{\rm tow}\preceq H_C(S/\mathcal A).}           \tag{4.3}
$$
每个逆都在同一个完整物理头上求；没有把压缩逆与逆压缩交换。

## 5. 同一个 forcing 的真核投影与准确正差

固定同一 $F=g\otimes\Omega$，定义真正交投影
$$
f_{\rm coh}=\mathscr R H_{\rm coh}^{-1}g,\qquad
k_{\rm tow}=\mathscr T H_{\rm tow}^{-1}g.
$$
$\mathscr R,\mathscr T$ 的零行都是恒等，所以其像闭，以上正是向各自完整像的交投影。置
$$
q_C(v)=\langle H_C(v)^{-1}g,g\rangle,\quad
q_{\rm coh}=\|f_{\rm coh}\|^2,\quad
q_{\rm tow}=\|k_{\rm tow}\|^2.
$$
(4.3) 的逆序给
$$
q_C(S)\ge q_{\rm coh}\ge q_{\rm tow}\ge q_C(S/\mathcal A).
                                                               \tag{5.1}
$$
原交叉 Gram 还给准确配对
$\langle f_{\rm coh},k_{\rm tow}\rangle=q_{\rm tow}$，所以
$$
\boxed{
\|f_{\rm coh}-k_{\rm tow}\|^2
=q_{\rm coh}-q_{\rm tow}
\le q_C(S)-q_C(S/\mathcal A).}                         \tag{5.2}
$$
这已经是同一个 forcing 的完整重新最小化，$k_{\rm tow}$ 是 (4.2) 中的真核。式中没有短核距离 $\delta_L$、未付的 terminal MP 或头相似条件数。

也可保留一个显式但未重新最小化的同 forcing 真核：
$$
a=H_C(S/\mathcal A)^{-1}g,\qquad k=\mathscr T a.
$$
则
$$
\langle F,k\rangle=q_C(S/\mathcal A),\qquad
\|k\|^2\le q_C(S/\mathcal A),
$$
$$
\|k-a\otimes\Omega\|^2
\le\sum_{r=1}^L\frac{\|C^ra\|^2}{r!(S/\mathcal A)^r}.  \tag{5.3}
$$
(5.3) 明确改用了缩小方差后的原最小来源；不能把旧方差 S 的来源直接代进去。

## 6. 返回原模型的实际 u 与固定方差窗能量

现在取原 N 或 Y 有限头模型
$$
d=2^m,\quad R=x-m,\quad C=A_m+D_{[m,x)},\quad
h=d+R,\quad L=h-1.
$$
沿用原模型和母窗的全部条件，并取 $m\ge10$、$x\ge m+d$；于是
$$
x\le L=x+d-m-1<2x,
$$
正好满足本稿参数。$A_m$ 的全部原 carry 和物理内积始终保留。

令 $V_{m,Q},K_{m,Q}$ 为旧同一模型的实际可行空间与真核，
$g=g_{\rm old}\otimes\Omega_{[m,x)}$，仍取同一个
$F=g\otimes\Omega_{\ge x}$。在原母窗内另保
$$
Q\ge R+L.                                             \tag{6.1}
$$
原相干低行身份给
$P_Vf_{\rm coh}=P_VF$、$P_Kf_{\rm coh}=P_KF$。
(4.2) 的强孔至多 R、远孔至多 L，故
$k_{\rm tow}\in K_{m,Q}\subset V_{m,Q}$。
因此原实际向量 $u_g=(P_V-P_K)F$ 满足
$$
\boxed{
\|u_g\|^2\le
q_C(S_x)-q_C(S_x/\mathcal A).}                         \tag{6.2}
$$
例如 $x=m+d$ 时 $R=d,L=2d-1$，只需 $Q\ge3d-1$，
所以在其余原母窗条件同时满足时，既有的 $Q=4d$ 已覆盖这个真实终列；没有为塔增大 x 到
$\exp(O(d^4))$。其它原母窗限制仍须保留。

对同一个固定 C 和同一个 g，令
$$
a_C(v)=H_C(v)^{-1}g,\qquad
\mu_C(v)=\sum_{r=1}^L
 \frac{r\|C^ra_C(v)\|^2}{r!v^r}.
$$
有限级数微分及逆导数准确给
$dq_C/d\log v=\mu_C(v)$。所以本条最终费用也可写成
$$
\boxed{
\|u_g\|^2\le
\int_{S_x/\mathcal A}^{S_x}\mu_C(v)\,\frac{dv}{v},
\qquad \log\mathcal A=22\log2.}                       \tag{6.3}
$$
这是同一个原头及同一个 forcing 的固定长度对数方差窗，没有逐高度换源。
(5.2) 的真核候选差也由同一积分控制。

## 7. 仍须支付的同源端点

(6.3) 是真实全终列的已付预算，但不是已知趋零量。moving m、x 时，
$C=A_m+D_{[m,x)}$ 本身在变化；不能只因每个固定算子的全对数能量有限，就断言这些移动窗口积分趋零。

已有 actual-variance 源极限在其明确的 $s\in[S_x,2S_x]$ 范围内使用。
本稿不把它延长为 $S_x/\mathcal A$，也不把这里的 $\mu_C$ 免费替成原全 T 的 $\mu_T$。若能对同一 forcing 证明
$q_C(S_x)-q_C(S_x/\mathcal A)\to0$，(5.2)、(6.2) 就给原合法母窗中的终列真核逼近；此后仍须完成原模型核到全局稳定范围的实际 carry / lift 运输。

因此原近最优短窗、Chebyshev 条件结果仍保原范围；这里提供的是另一条已经完整付清的终列来源接口，而非把它们的尚未支付输入改称已闭。原 $N=M$ 与普通 Hilbert ISP 均未由本文完成。

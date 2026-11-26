# R271 附录：真空源的全新增位矩、真实物理运输与完整加权 inverse

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下完整源矩改进、两实际物理列的比较及完整 inverse 孔权界已证明。**
本稿改进[全部新增强位的绝对完整源定理](R271-appendix-all-strong-bit-extension-weighted-complete-source.md)：
不再用新增删除的整个算子范数估计实际真空 forcing 的伴随差。
全部新增位一次硬化，头最小者也同时重新最小化。
另给旧、新两个原物理代表的准确翻译，二者分别保持同一个原 $u$。

所用辅助方差仍为 $s\ge2^{24}/y$，不声称它是原物理方差 $S_x$。
没有把全空间 inverse 改称真 $F_0$ 上的压缩 inverse，
也没有把最终有界 Gram 正则化列改称真物理核列。

## 1. 同一 forcing、完整列与旧高度能量

沿依赖稿的记号，令 $C^h=0$ 为完整旧头，
$D=\sum_{i\in I}b_iE_i$ 为全部新增真实 Boolean 位，$C$ 与 $D$ 交换。
对任意固定有限 $J\ge0$ 和 $s>0$，用
$$
\mathcal R_{X,J}(s)v
=\sum_{l=0}^J\frac{(-X)^lv}{\sqrt{l!s^l}}\otimes e_l,
\qquad H_{X,J}(s)=\mathcal R_{X,J}^*\mathcal R_{X,J}.
$$
原同一个 forcing 为 $f=g\otimes\Omega_I\otimes e_0$。
记
$$
a_0=H_{C,J}(s)^{-1}g,\qquad
k_0=\mathcal R_{C,J}(s)a_0\otimes\Omega_I,
$$
$$
a_1=H_{C+D,J}(s)^{-1}(g\otimes\Omega_I),\qquad
k_1=\mathcal R_{C+D,J}(s)a_1.
$$
旧列至多有 $H=\min(J,h-1)$ 个辅助孔。定义它的原实际层能量
$$
E_l=\frac{\|C^la_0\|^2}{l!s^l},\qquad
\varepsilon_0=\sum_{l=1}^{H}E_l,\qquad
\mu_1=\sum_{l=1}^{H}lE_l.
\tag{1.1}
$$
这些都来自同一个未加权完整最小者。

记 $a_{\rm aux}$ 为标准辅助 annihilation，
$$
M=\exp(-Da_{\rm aux}^*/\sqrt s),\qquad
B=P_{\{N_a\le J\}}M|_{\mathscr E_0},\qquad
\mathscr E_0=\operatorname{Ran}\mathcal R_{C,J}\otimes\mathcal H_I,
\quad K=B^*B.
$$
依赖稿已证准确截断卷积、满射和原投影公式
$$
B\mathcal R_{C,J}=\mathcal R_{C+D,J},\qquad
Bk_0=k_0,\qquad k_1=BK^{-1}k_0.
\tag{1.2}
$$
本稿继续使用这个原 $K^{-1}$，不改为加权最小化。

## 2. 实际真空 forcing 的准确平方和

令 $0<\gamma\le1$，$\Gamma=\gamma^{-N_I}$，并置
$$
\alpha=\|D\|/\sqrt s,\qquad
\theta_h(u)=u\sqrt h+u^2/2,
$$
$$
\theta_+=\theta_h(\gamma\alpha),\quad
\theta_-=\theta_h(\gamma^{-1}\alpha),\quad
\Theta=\theta_++\theta_-<\log2.
$$
依赖稿的准确两向共轭和 Neumann 界为
$$
\Gamma_0K\Gamma_0^{-1}=B_-^*B_+,
\quad
\|\Gamma_0K^{-1}\Gamma_0^{-1}\|
\le(2-e^\Theta)^{-1},
\quad \|B_+\|\le e^{\theta_+}.
\tag{2.1}
$$
这里 $P_{\mathscr E_0}$ 与 $\Gamma$ 交换；并未对新核投影提出相同假设。

令 $S_I=\sum_{i\in I}b_i^2$，$e_j(b_I^2)$ 为原平方权的第 $j$ 个初等对称式。
由于旧列在所有新增位上是真空，且 $D^*$ 每次精确增加一个新增孔，
不同 $j$ 的项正交。准确有
$$
\begin{aligned}
\mathfrak d_\gamma^2
&:=\left\|
\left[\exp(-\gamma^{-1}D^*a_{\rm aux}/\sqrt s)-I\right]k_0
\right\|^2\\
&=\sum_{j=1}^{H}\frac{\gamma^{-2j}e_j(b_I^2)}{s^j}
\|a_{\rm aux}^{\,j}k_0\|^2\\
&=\sum_{l=1}^{H}E_l
\sum_{j=1}^{l}(l)_j\frac{\gamma^{-2j}e_j(b_I^2)}{s^j}.
\end{aligned}
\tag{2.2}
$$
这里 $(l)_j=l!/(l-j)!$。归一化来自
$\|(D^*)^j\Omega_I\|^2=(j!)^2e_j(b_I^2)$，
正好消掉 exponential 中的 $(j!)^2$；不同旧辅助 $l$ 在每个固定 $j$ 后也仍正交。
这保留所有实际碰撞，不把平方自由塔改成 bosonic 等号。

设 $\eta=\gamma^{-2}S_I/s$。
由 $e_j(b_I^2)\le S_I^j/j!$，得到
$$
\boxed{
\mathfrak d_\gamma^2
\le\sum_{l=1}^{H}\bigl[(1+\eta)^l-1\bigr]E_l
\le\eta e^{\eta H}\mu_1
\le\bigl(e^{\eta H}-1\bigr)\varepsilon_0.}
\tag{2.3}
$$
中间一步使用 $(1+\eta)^l-1\le l\eta e^{l\eta}$。

在 (1.2) 中，因 $B_+k_0=k_0$，完整差的强迫为
$(I-B_-^*)k_0$。
它是 (2.2) 中向量到旧完整列空间的正交投影，故其范数至多 $\mathfrak d_\gamma$。
由 (2.1) 得到真实重新最小化后的来源界
$$
\boxed{
\|\Gamma(k_1-k_0)\|
\le\frac{e^{\theta_+}}{2-e^\Theta}\mathfrak d_\gamma.}
\tag{2.4}
$$
其第零辅助分量 $a_1-a_0\otimes\Omega_I$ 满足同一上界。

旧真空列子空间 $\operatorname{Ran}\mathcal R_{C,J}\otimes\Omega_I$
是新列空间的子空间，因为 $D\Omega_I=0$。
因此另有准确的同源勾股身份
$$
\langle g\otimes\Omega_I,a_1\rangle-\langle g,a_0\rangle
=\|k_1-k_0\|^2\ge0.
\tag{2.5}
$$
本式固定辅助方差 $s$；不能把它移到删位后同时更换物理方差的另一比较。

## 3. 两个原物理代表之间的准确翻译

现在令旧头位于 $[0,y)$，新增真实位为 $I=[y,x)$，实际远尾从 $x$ 开始。
记
$$
D_y^*=D_{[y,x)}^*+D_x^*,\qquad
\omega_{y,l}=(D_y^*)^l\Omega,\qquad
\omega_{x,l}=(D_x^*)^l\Omega.
$$
两头的原物理阻尼代表分别为
$$
f_y^{\rm phys}
=\sum_{l=0}^J\frac{(-C_y)^la_0\otimes\omega_{y,l}}{l!s^l},
\qquad
f_x^{\rm phys}
=\sum_{l=0}^J\frac{(-C_x)^la_1\otimes\omega_{x,l}}{l!s^l}.
\tag{3.1}
$$
它们各自使用自己的原完整 inverse，forcing 则是同一个物理向量。

令 $T_x$ 为把辅助 $e_j$ 送到
$\omega_{x,j}/\sqrt{j!s^j}$ 的逐层物理映射。
当 $s\ge S_x$ 时，$T_x$ 收缩，且与新增孔权 $\Gamma$ 交换。
将二项式展开的每个 $D_{[y,x)}^*$ 项保留，得到精确身份
$$
\boxed{
f_x^{\rm phys}=T_xk_1,\qquad
f_y^{\rm phys}
=T_x\exp(+D_{[y,x)}^*a_{\rm aux}/\sqrt s)\,k_0.}
\tag{3.2}
$$
第二式的正号不能换成 $M^*$ 的负号。
具体地，旧第 $l$ 层贡献中取 $j$ 个新增孔，翻译后的系数正好是
$$
\frac{(-C_y)^la_0\,(D_{[y,x)}^*)^j\omega_{x,l-j}}
{j!(l-j)!s^l},
$$
与 $\omega_{y,l}$ 的二项式完全相同。辅助 annihilation 仅降次数，故没有截断外漏项。

把 (2.2) 的负号改成正号不改变平方和，因为不同新增孔层仍正交。
因此 (2.4)、(3.2) 给两个真正物理列的比较
$$
\boxed{
\|\Gamma(f_x^{\rm phys}-f_y^{\rm phys})\|
\le\left(1+\frac{e^{\theta_+}}{2-e^\Theta}\right)
\mathfrak d_\gamma.}
\tag{3.3}
$$
这里没有把同一个辅助列未经翻译地当作两个不同远尾 cut 的物理列。

## 4. 原连续尾的 $1/y$ 来源预算及一次公共方差选择

取原 N/Y 模型，$m\ge10$、$d=2^m$、$y\ge m+d$，并令
$$
C_y=A_m+D_{[m,y)},\qquad h=d+y-m\le2y,
\qquad \gamma=1/32,
\qquad s\ge K/y,\quad K\ge2^{24}.
$$
对任意 $x\ge y$，
$$
\|D_{[y,x)}\|\le1/y,\qquad
S_{[y,x)}\le1/(3y^3).
$$
因此依赖稿的 $\Theta<1/32$、$e^{\theta_+}/(2-e^\Theta)\le16/15$ 仍适用。
同时
$$
\eta\le\frac{1024}{3Ky^2},\qquad
\eta H\le\frac{2048}{3Ky}<\frac1{32}.
$$
结合 (2.3) 得到便于使用的明确常数
$$
\boxed{
\|32^{N_{[y,x)}}(k_x-k_y)\|
\le\frac{64}{\sqrt{3K}\,y}\sqrt{\mu_1},}
\tag{4.1}
$$
$$
\boxed{
\|32^{N_{[y,x)}}(f_x^{\rm phys}-f_y^{\rm phys})\|
\le\frac{96}{\sqrt{3K}\,y}\sqrt{\mu_1}.}
\tag{4.2}
$$
例如 $e^{\eta H/2}\le\sqrt{32/31}$，
$(16/15)\sqrt{32/31}<2$、$(31/15)\sqrt{32/31}<3$，给上述常数。
仅用 $\mu_1\le2y\varepsilon_y$ 也比旧全算子差界多得到 $y^{-1/2}$。

还可用已有的完整对数方差导数，只选择一次方差。
固定 $C_y,J,g$，记 $q_y(s)=\langle g,H_{C_y,J}(s)^{-1}g\rangle$。
直接求导给
$$
\frac{d q_y(s)}{d\log s}=\mu_1(s).
$$
在 $[K/y,2K/y]$ 上，存在同一个 $s_*$ 使
$$
\mu_1(s_*)
\le\frac{q_y(2K/y)-q_y(K/y)}{\log2}
\le\frac{\|g\|^2-q_y(K/y)}{\log2}.
\tag{4.3}
$$
该选择只依赖旧头、同一 forcing 和指定 $J$，不依赖后续 $x,Q$。
若同时取所有 $J\ge h-1$，旧 Gram 已稳定，因而也可使用同一次选择；
不声称一个选择同时支付任意未稳定的全部较小 $J$。

设原 $u_{g,Q}=(P_{V_Q}-P_{K_Q})i_0g$、
$\Delta_{g,Q}^2=\|g\|^2-\|u_{g,Q}\|^2$。
在 $Q\ge(x-m)+J$ 下，两条 (3.1) 分别满足原逐列低方程，故
$$
P_{V_Q}f_x^{\rm phys}=P_{V_Q}f_y^{\rm phys}=P_{V_Q}i_0g,
\quad
P_{K_Q}f_x^{\rm phys}=P_{K_Q}f_y^{\rm phys}=P_{K_Q}i_0g.
\tag{4.4}
$$
这里 $g$ 在新增位和原远尾上均按同一个真空嵌入。
旧物理列范数平方至多 $q_y(K/y)$，所以
$q_y(K/y)\ge\|u_{g,Q}\|^2$。由 (4.2)–(4.3)，对所有合法 $x,Q$ 同时有
$$
\boxed{
\|32^{N_{[y,x)}}(f_x^{\rm phys}(s_*)-f_y^{\rm phys}(s_*))\|
\le\frac{96}{\sqrt{3K\log2}\,y}\Delta_{g,Q}.}
\tag{4.5}
$$
全部原内部顶部和两端 partial 仍由 (4.4) 的同一个 $u_{g,Q}$ 产生。
如另需 c26 母提升，可照原范围取
$x+1\le e^{26d^3}/4$、$J\le d+x-m-1$、$Q\ge(x-m)+J$；
这样 $Q$ 可选在原上限内。额外 joined/full 帽条件仍单独保留。

## 5. 同一 Neumann 证明给完整 inverse 的算子界

此节不要求 forcing 在新增位为真空。
记 $i_0$ 为插入辅助真空，$P_0=i_0^*$。
$M$ 只增加辅助次数，所以在全部旧列空间上 $P_0B=P_0$，且
$B^*i_0=P_{\mathscr E_0}i_0$。完整投影公式给准确的原 inverse
$$
\boxed{
H_{C+D,J}(s)^{-1}
=P_0K^{-1}P_{\mathscr E_0}i_0.}
\tag{5.1}
$$
两端都是原 Hilbert 范数的收缩，并与相应新增孔权交织。
因此 (2.1) 给
$$
\boxed{
\|\Gamma H_{C+D,J}(s)^{-1}\Gamma^{-1}\|
\le\frac1{2-e^\Theta}.}
\tag{5.2}
$$
完整列同样满足
$$
\boxed{
\|\Gamma\mathcal R_{C+D,J}(s)
H_{C+D,J}(s)^{-1}\Gamma^{-1}\|
\le\frac{e^{\theta_+}}{2-e^\Theta}.}
\tag{5.3}
$$
特别在 §4 的原窗中，常数分别不超过 $31/30$ 和 $16/15$。
这控制原未加权 inverse 的共轭，不是另一个加权 Gram 的逆。

## 6. 原无限物理尾和全级数 Gram

固定 $m,y,s$ 满足 §4，令原有界物理算子
$$
L_m=A_m+D_{\ge m}=C_y+D_{\ge y},
\qquad \Gamma_y=32^{N_{\ge y}}.
$$
先对任意固定有限 $J$ 取 $x\to\infty$。
$C_x\to L_m$ 于算子范数，故 $H_{C_x,J}(s)\to H_{L_m,J}(s)$ 于算子范数，
其 inverse 也范数收敛，因每个 Gram 都至少为恒等。
(5.2) 对递增有限孔权成立；先固定任意有限位置 cut，再取 $x$ 极限，
最后对位置 cut 单调收敛，得到
$$
\boxed{
H_{L_m,J}(s)^{-1}\operatorname{Dom}\Gamma_y
\subseteq\operatorname{Dom}\Gamma_y,
\qquad
\|\Gamma_yH_{L_m,J}(s)^{-1}v\|
\le\frac{31}{30}\|\Gamma_yv\|.}
\tag{6.1}
$$
一般 $v\in\operatorname{Dom}\Gamma_y$ 由有限孔/有限位置向量在其图范数中稠密、
以及 $\Gamma_y$ 闭性得到；没有把无界孔权作为处处有界算子使用。

因为 $L_m$ 有界，完整级数
$$
\mathcal H_{L_m}(s)=\sum_{j=0}^{\infty}
\frac{(L_m^*)^jL_m^j}{j!s^j}
$$
在算子范数中收敛且至少为恒等。
再令 $J\to\infty$，同一闭图论证给 (6.1) 对
$\mathcal H_{L_m}(s)^{-1}$ 仍成立。

对于旧真空 forcing $g$，还有更精确的实际源界。
固定有限 $J$，新物理列满足
$$
\|f_x^{\rm phys}-a_x\|
\le\sqrt{S_x/s}\,\|g\|\to0,
$$
所以 $f_x^{\rm phys}\to H_{L_m,J}(s)^{-1}i_0g$。
对 (4.2) 先固定有限位置孔权再取极限，得到
$$
\boxed{
\|\Gamma_y[H_{L_m,J}(s)^{-1}i_0g-f_y^{\rm phys}]\|
\le\frac{96}{\sqrt{3K}\,y}\sqrt{\mu_1}.}
\tag{6.2}
$$
当 $J\ge h-1$ 时，旧列、旧物理代表和 $\mu_1$ 均不再变化。
因此 (6.2) 也可令 $J\to\infty$，以相同右端比较
$\mathcal H_{L_m}(s)^{-1}i_0g$ 和原旧物理列。

该极限是原无限物理 $L_m$ 的完整 Gram 正则化源，
通常不在 $\ker L_m$。式 (4.4) 的有限 $Q$ 身份依赖 $Q\ge x-m+J$，
所以不能把 $x\to\infty$ 时增长的 $Q$ 偷换成一个固定有限 cut。

## 7. 本条实际推进与剩余返回

本稿把新增真空的全部 factorial 矩用于原完整重新最小化，
并通过 (3.2) 将两个不同硬化头的辅助列准确接到两个各自同源的物理列。
由此得到一次公共方差选择下的真实 $1/y$ 来源预算，以及完整未加权 inverse 的孔权算子界。

这些结论均在大辅助方差范围。它们不删除原 $s\to S_x$ 的重新最小化，
不把无限物理 Gram 正则化源当作真物理核，不支付真 $F_0$ 的绝对
$\mathcal Z_{1/32}(S_x)$、全部 MP 自然返回或完整帽逆费用。

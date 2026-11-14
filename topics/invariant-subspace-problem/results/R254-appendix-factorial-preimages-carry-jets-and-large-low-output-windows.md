# R254 第十二附录：阶乘多次原像、真实进位的指数导数范数与大孔窗口

日期：2026-11-13（UTC）。作者：boundary；Astra-ISP-1cf8c51d 复核。状态：已证明的实际中间结论。

本稿强化 [R254 第十附录](../results/R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md) 的相容多次原像，保留每次递推真实支付的阶乘。随后以原位号支付全部跨头 carry 的指数导数范数，并给实际平方核到低输出方程空间的巨大窗口近似。最后一步仍只是低方程近似；现有实际稳定像提升尚不能在该窗口支付，本文不登记新的 $N=M$ 或正则饱和范围。

## 1. 多次双和的真实阶乘

沿用第十附录固定的共同辅助头。输入次数上界为 $q$，最大原像阶为 $2d$，并记
$$
L=512\sqrt{q+2d+1}(m+q+2d+2)^{3/2}.
$$
相容原像为
$$
R_tf=\sum_{k+l\le q}
 C^{k+l+t}F^{(t)}_{kl}(H)D^kD_1^lf,\qquad
DR_t=R_{t-1},\quad R_0=I.
$$
这里 $D$ 是纯高尾删除，$C$ 是辅助有限头的倒系数创建，$D_1$ 是该辅助头之后的纯删除。全部算子、源层分母及精确恒等式已经在第十附录支付。

令 $A^{(t)}_{kl}$ 为 $(-1)^kF^{(t)}_{kl}$ 的正倒数乘积展开中全部系数之和。原递推为
$$
A^{(t)}_{kl}
\le\frac{
A^{(t-1)}_{kl}+A^{(t)}_{k-1,l}
+2(k+2l+t-2)A^{(t)}_{k,l-1}
}{k+l+t}.
\tag{1.1}
$$
对
$\widehat A^{(t)}_{kl}=(k+t)!A^{(t)}_{kl}$
使用 (1.1)：前两个方向各出现
$(k+t)/(k+l+t)\le1$，第三个方向仍至多付 $4$。所以同一三方向 Pascal 归纳给
$$
\boxed{
A^{(t)}_{kl}
\le
\frac{(k+l+t-1)!}{k!\,l!\,(t-1)!}
\frac{4^l}{(k+t)!}.
}
\tag{1.2}
$$
$t=1,k=l=0$ 的初值为 $1$；其余边界与第十附录一致。

源层上的分母数仍为 $k+2l+t$，最大极点仍为 $2(k+l)+t-1$。因此，在第十附录的同一个 $l$ 求和中，保留 $\|D^kf\|$，得到
$$
\|R_tf\|
\le\sum_{k=0}^{q}
\frac{\binom{k+t-1}{k}}{(k+t)!}
 L^{k+t}\|D^kf\|.
$$
准确的系数关系是
$$
\frac{\binom{k+t-1}{k}}{(k+t)!}
=\frac{t}{k+t}\frac1{k!\,t!}
\le\frac1{k!\,t!}.
$$
故对任意 $R\ge L$，
$$
\boxed{
\|R_tf\|
\le\frac{R^t}{t!}\,\mathcal U_R(f),
\qquad
\mathcal U_R(f):=\sum_{k=0}^\infty
 \frac{R^k}{k!}\|D^kf\|.
}
\tag{1.3}
$$
有限孔输入时和准确有限；一般 Hilbert 向量也总有
$\mathcal U_R(f)\le e^{R\|D\|}\|f\|<\infty$。

相容性还给
$D^kR_tf=R_{t-k}f$ 当 $k<t$，
以及 $D^kR_tf=D^{k-t}f$ 当 $k\ge t$。
分别使用 (1.3) 和 $(l+t)!\ge l!\,t!$，得到
$$
\boxed{
\mathcal U_R(R_tf)
\le\frac{(2R)^t}{t!}\mathcal U_R(f).
}
\tag{1.4}
$$
这两条界没有把多次原像当作与 $D$ 交换的算子。

## 2. 指数导数范数与完整纯尾源层

在本稿固定的纯尾 $D=D_m^{\rm p}$ 下，定义
$$
\|X\|_{\delta,R}
=\sum_{k=0}^\infty
 \frac{R^k}{k!}\|\operatorname{ad}_D^kX\|.
\tag{2.1}
$$
$D$ 有界，所以所有 $X\in B(H)$ 的该范数均有限，至多为
$e^{2R\|D\|}\|X\|$。真实 Leibniz 公式给
$$
\|XY\|_{\delta,R}\le
\|X\|_{\delta,R}\|Y\|_{\delta,R}.
\tag{2.2}
$$
把 $D^kX$ 正规排列到 $X$ 的导数与右侧 $D$ 幂，也得到
$$
\boxed{
\mathcal U_R(Xf)
\le\|X\|_{\delta,R}\mathcal U_R(f).
}
\tag{2.3}
$$
这是有界算子的实际范数等式与估计，不涉及形式伴随原像。

任何孔截断都满足
$$
D^kP_{\le a}=P_{\le a-k}D^k,\qquad
D^kP_{>a}=P_{>a-k}D^k.
$$
因此这些截断在 $\mathcal U_R$ 中均为收缩。该事实只利用严格次数，不把截断当成与 $D$ 交换。

若 $K_\ell$ 只作用前 $\ell+1$ 个图尾位，$\ell\ge m$，则只有 $j=m,\ldots,\ell$ 参与其与 $D$ 的交换子。因为 $E_j^2=0$，
$$
\operatorname{ad}_{E_j}^3K_\ell=0,\quad
\|\operatorname{ad}_{E_j}K_\ell\|\le2\|K_\ell\|,\quad
\frac12\|\operatorname{ad}_{E_j}^2K_\ell\|\le\|K_\ell\|.
$$
不同 $j$ 的导子相互交换。逐项展开有限指数并对系数取绝对值，得到
$$
\boxed{
\|K_\ell\|_{\delta,R}
\le\|K_\ell\|
 \prod_{j=m}^{\ell}(1+Rb_j)^2,
\qquad b_j=(j+2)^{-2}.
}
\tag{2.4}
$$
特别，最高非零交换子阶至多为 $2(\ell-m+1)$。这保留了原物理尾长度，而不是使用整个头长度 $\ell+1$。

同一个有限 Leibniz 公式还给真实核阶运输：
$$
\boxed{
K_\ell(\ker D^s)
\subseteq\ker D^{s+2(\ell-m+1)}.
}
\tag{2.5}
$$
确实，展开 $D^{s+2(\ell-m+1)}K_\ell f$，超过最高导数阶的项为零，其余各项右侧至少有 $D^s f$。对有限和 $K_{\ell,r}Y_r$，只要全部 $Y_r$ 与 $D$ 交换，同一结论也成立。

## 3. 真实跨头 carry 的全部导数预算

记实际慢尾为 $\mathcal A$，混合截断为
$$
\mathcal A^{[\ell]}=\mathcal A_\ell+\sum_{j\ge\ell}b_jE_j.
$$
R254 第三附录的真实界为
$$
\|\mathcal A-\mathcal A^{[\ell]}\|\le26\eta_\ell,
\qquad
\|C-C_\ell\|\le\eta_\ell.
$$
两相邻混合截断的差
$\Delta\mathcal A_\ell=\mathcal A^{[\ell+1]}-\mathcal A^{[\ell]}$
只作用前 $\ell+1$ 位：更高纯尾准确消去。因此
$$
\|\Delta\mathcal A_\ell\|\le52\eta_\ell.
$$
同样 $\Delta C_\ell=C_{\ell+1}-C_\ell$ 只作用前 $\ell+1$ 位，且
$\|\Delta C_\ell\|\le2\eta_\ell$。这些是实际有限头矩阵差，不是将无限实际尾替换为纯尾。

令
$$
S_m(R)=
\sum_{\ell=m}^\infty
\eta_\ell\prod_{j=m}^{\ell}(1+Rb_j)^2.
\tag{3.1}
$$
其级数对每个有限 $R$ 收敛。由 (2.4) 及真实范数极限，
$$
\|\mathcal A-\mathcal A^{[m]}\|_{\delta,R}\le52S_m(R),
\qquad
\|C-C_m\|_{\delta,R}\le2S_m(R).
\tag{3.2}
$$
$\mathcal A^{[m]}$ 与 $C_m$ 都与 $D$ 交换，故其导数范数就是普通范数，分别小于 $2/3$ 和至多 $1$。

两种实际平方符号仍为
$$
P=\mathcal A^2-\eta C\quad(N),\qquad
P=\mathcal A^2-\eta C(I+\mathcal A)^2\quad(Y),
$$
而 $P_m$ 以 $\mathcal A^{[m]},C_m$ 代入同一多项式，$\eta=e^{-1070}$。置
$$
E_m=P_m-P.
$$
由 (2.2)--(3.2)，当 $S=S_m(R)\le1/104$ 时，两型统一有
$$
\begin{aligned}
\|E_m\|_{\delta,R}
\le{}&52S(4/3+52S)\\
&+\eta\left[
2S(5/3+52S)^2+52S(10/3+52S)
\right]
<128S.
\end{aligned}
\tag{3.3}
$$
这个上界也包含较小的 $N$ 型误差；乘积差按原次序展开，不假设不同混合层的头相互交换。

仍令 $d=2^m$，$m\ge4$。若
$$
x:=\log(2+R)\le d^3,
\tag{3.4}
$$
粗但真实的 $\eta_\ell\le e^{-77016^\ell}$ 给
$$
S_m(R)
\le\sum_{r\ge0}
\exp[-770d^4\,16^r+2(r+1)d^3]
\le2e^{-769d^4}.
$$
首项的 $2d^3\le d^4/8$；其余相邻项比具有远大于所需的负指数。于是 $S\le1/104$，并有
$$
\boxed{
\epsilon_m(R):=\|E_m\|_{\delta,R}
\le e^{-760d^4}.
}
\tag{3.5}
$$
原物理位号和全部真实 carry 已进入该界。

## 4. 实际平方核的纯尾指数导数控制

设 $u\in K=\ker P$。由于
$$
D^2u=-Q_mu+E_mu,\qquad [D,Q_m]=0,\qquad Q_m^d=0,
$$
对所有 $j\ge1$ 都有有限递推
$$
D^{2j}u=(-Q_m)^ju+
\sum_{\ell=0}^{j-1}
(-Q_m)^\ell D^{2(j-1-\ell)}E_mu.
\tag{4.1}
$$
不要求 $E_m$ 与 $D$ 交换。奇阶式再左乘一次 $D$。

置
$$
A_m(R)=\sum_{\ell=0}^{d-1}
 \frac{R^{2\ell}}{(2\ell)!}\|Q_m^\ell\|.
\tag{4.2}
$$
将 (4.1) 及奇阶式乘对应的阶乘权再求和；用 $\|D\|\le\sum_{j\ge m}(j+2)^{-2}<1$ 控制奇阶首项，并利用
$(r+s)!\ge r!s!$，得到
$$
\mathcal U_R(u)
\le(1+R)A_m(R)\|u\|
+R^2A_m(R)\mathcal U_R(E_mu).
$$
由 (2.3)，
$$
\mathcal U_R(u)
\le(1+R)A_m(R)\|u\|
+R^2A_m(R)\epsilon_m(R)\mathcal U_R(u).
\tag{4.3}
$$
$\mathcal U_R(u)$ 本来有限，所以吸收不是形式运算。

在 (3.4) 下，用 $\|Q_m^\ell\|\le1$ 即有
$$
A_m(R)\le d(1+R)^{2d},
\qquad \log A_m(R)\le3d^4.
$$
因此 $R^2A_m(R)\epsilon_m(R)<1/2$，(4.3) 给
$$
\boxed{
\mathcal U_R(u)
\le2(1+R)A_m(R)\|u\|
\le e^{4d^4}\|u\|,
\quad \log(2+R)\le d^3.
}
\tag{4.4}
$$
它是真实核上的估计；没有将环境全空间的纯尾幂直接改成头四次衰减。

## 5. 无有限阶核前提的低输出修复

第十附录的相容右逆
$$
\widetilde{\mathcal G}_{m,q}
=\sum_{\ell<d}(-1)^\ell Q_m^\ell R_{2\ell+2}
$$
在全部有限孔输入上满足
$P_m\widetilde{\mathcal G}_{m,q}=I$，输出最低增加两孔、最高增加 $2d$ 孔。由 (1.3)，对每个 $f\in\mathcal H_{\le q}$，
$$
\boxed{
\|\widetilde{\mathcal G}_{m,q}f\|
\le R^2A_m(R)\mathcal U_R(f),
\qquad R\ge L.
}
\tag{5.1}
$$
这里没有假设 $f\in\ker D^s$。这正是阶乘范数的用途。(1.4) 同样给有限输入范围内的导数范数界
$$
\mathcal U_R(\widetilde{\mathcal G}_{m,q}f)
\le4R^2 A_m(2R)\mathcal U_R(f).
\tag{5.1a}
$$
所有这些右逆都保留固定的有限孔输入范围。

现假设 $R=L$ 并满足 (3.4)。对实际 $u\in K$，置
$$
r=P_{\le q-2}P_mP_{\le q}u.
$$
$P_m$ 最多降低两孔，所以原 $P_{>q}u$ 不能进入此输出窗口。又 $P_mu=E_mu$，故
$$
r=P_{\le q-2}E_mu.
$$
由第 2 节的截断收缩性及 (2.3)，
$$
\mathcal U_R(r)\le\epsilon_m(R)\mathcal U_R(u).
$$
令 $z=\widetilde{\mathcal G}_{m,q}r$。由 (3.5)、(4.4)、(5.1)，
$$
\|z\|\le
R^2A_m(R)\epsilon_m(R)\mathcal U_R(u)
\le e^{-700d^4}\|u\|.
\tag{5.2}
$$
于是
$$
P_{\le q}u-P_{\le q}z
$$
属于闭空间
$$
\mathcal L_{m,q}
=\{v\in\mathcal H_{\le q}:P_{\le q-2}P_mv=0\}.
$$
因为 $P_mP_{>q}z$ 的最低输出为 $q-1$，这里的截断修复准确成立。

令 $v_{m,q}$ 为 $P_{\le q}u$ 到 $\mathcal L_{m,q}$ 的正交投影。最小距离性质给
$$
\boxed{
\|v_{m,q}\|\le\|u\|,\qquad
\|P_{\le q}u-v_{m,q}\|\le e^{-700d^4}\|u\|.
}
\tag{5.3}
$$
低方程的真实带宽恒等式
$$
D^{2j}v_{m,q}=P_{\le q-2j}(-Q_m)^jv_{m,q}
$$
在 $j=d$ 还给
$$
v_{m,q}\in\ker D^{2d}.
\tag{5.4}
$$
因而有限阶纯核归属是构造的结论，不是对 $r$ 未经证明的输入假设。

## 6. 一个远大于四次尺度的明确窗口

取
$$
q_m=\left\lfloor e^{d^3/4}\right\rfloor,\qquad d=2^m,\quad m\ge4.
$$
此时 $q_m\ge3d+m+2$，故
$$
L\le2048q_m^2,\qquad
\log(2+L)\le9+2\log q_m\le d^3.
$$
第 5 节于是给实际低方程正交投影
$$
\boxed{
\|P_{\le q_m}u-v_{m,q_m}\|
\le e^{-700d^4}\|u\|,\qquad
v_{m,q_m}\to u,
}
\tag{6.1}
$$
且每个 $v_{m,q_m}$ 满足 (5.4) 及准确低输出方程。
高尾截断余项仍只付原向量的普通总孔尾；强收敛不要求任何给定尾速率。

## 7. 明确保留的实际提升障碍

(6.1) 是到混合低方程空间的近似。它不是到 $\ker P_m$、原实际核或 $N$ 的距离估计。

即使随后按已证公式准确修掉顶两层，现有 R239 实际正则提升仍含
$$
\delta_{m,Q}
=130C_G\sqrt{(2m+5)(Q+m+2)}
 e^{7(Q+2m+3)}\eta_m.
$$
当 $Q$ 达到本稿 $q_m$ 时，$7Q$ 远大于 $-\log\eta_m=O(d^4)$；旧提升没有可用的小误差。不能把第 6 节直接接成新的对数权饱和或 $N=M$。

另一个必须保留的限制是：对固定有限 $R$，$\mathcal U_R$ 与 Hilbert 范数等价。因此不能把 (5.1a) 自动延为整个 Hilbert 空间上的有界右逆；有界准幂零的 $P_m$ 不可能因这套有限孔公式而满射。共同辅助头的正分母只在已声明的有限源层范围成立。无限次校正必须另外控制源次数、核阶和辅助头的改变。

本稿独立交付的是：真实阶乘多次原像、指数导数的乘积和局部 carry 预算、实际核上的可吸收 jet 估计，以及无预设有限核阶的大窗口低方程修复。后续需要新的实际稳定像提升或缺陷专属能量来利用该窗口。普通 ISP 仍未完成。

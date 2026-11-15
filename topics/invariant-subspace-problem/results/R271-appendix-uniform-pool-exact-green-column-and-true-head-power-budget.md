# 等权长池的完整伴随 Green 列与原头幂预算

日期：2026-11-15。作者：literature_audit / 789f。

**状态：已证明的完整列公式及上界。** 本文保留原头的物理内积、全部头坐标和完整核投影。对一个等权池，先准确写出 $(C^*)^\dagger(f\otimes\Omega)$，再由同一核投影的能量付其三角卷积。得到的预算只用真实头幂，不使用头的 Jordan 相似条件数。

特别地，若 $A=A_m$ 是原 $N/Y$ 头，所得列费用由已付的真实四次头幂控制。此结论没有把其余强位删除；若把其余强位并入头，公式仍成立，但其中所有幂和完整 $H^{-1}$ 都必须随之改为该扩头的真实对象。本文没有支付原连续尾完整强块的固定 Green 列，也没有完成 $N=M$。

## 1. 完整物理对象

设 $\mathcal H$ 是有限维 Hilbert 空间，$A$ 是其真实物理算子，并有
$$
A^d=0,\qquad d\ge2.
$$
$d$ 是一个合法幂零指数，不要求 $A$ 只有一个 Jordan 块。另取 $L$ 个等权物理 Boolean 位，权为 $t>0$，并假设
$$
L\ge2d,\qquad S=Lt^2.
\tag{1.1}
$$
在完整 $\mathcal H\otimes(\mathbb C^2)^{\otimes L}$ 上记
$$
D=t\sum_{i=1}^{L}E_i,\qquad C=A\otimes I+I\otimes D.
$$
取任意 $f\in\mathcal H$；原 forcing 是 $f\otimes\Omega$，其中 $\Omega$ 是该池的物理真空。所求列为
$$
g_f=(C^*)^\dagger(f\otimes\Omega).
\tag{1.2}
$$
这是完整 Moore–Penrose 列，因而它解的方程是
$$
C^*g_f=(I-P_{\ker C})(f\otimes\Omega),
\qquad g_f\perp\ker C^*.
\tag{1.3}
$$
不能把右侧提前改成仅含真空坐标的向量。

池的置换对称空间对 $D,D^*$ 同时约化。其正交基为
$$
u_j=\binom Lj^{-1/2}\sum_{|I|=j}e_I,\qquad 0\le j\le L.
$$
有
$$
Du_j=a_j u_{j-1},\qquad
a_j=t\sqrt{j(L-j+1)},\qquad
p_0=1,\quad p_j=\prod_{\nu=1}^{j}a_\nu.
\tag{1.4}
$$
因为 forcing 的池坐标为 $u_0$，完整核投影与完整 Moore–Penrose 列都留在这个约化空间。其他池的表示类型没有被非正交地删去。

## 2. 同一 forcing 的完整核投影

在上述约化空间中，把向量写成 $(v_0,\ldots,v_L)$。方程 $Cv=0$ 是
$$
Av_j+a_{j+1}v_{j+1}=0\quad(0\le j<L),\qquad Av_L=0.
$$
由于 $L\ge d-1$，其全部解准确为
$$
\mathcal R h=
\sum_{j=0}^{d-1}\frac{(-A)^jh}{p_j}\otimes u_j,\qquad h\in\mathcal H.
\tag{2.1}
$$
特别没有先把 $h$ 限制到若干低头坐标。置
$$
H=\mathcal R^*\mathcal R
=\sum_{j=0}^{d-1}\frac{(A^*)^jA^j}{p_j^2}\succeq I,
\qquad h=H^{-1}f.
\tag{2.2}
$$
由 $\mathcal R^*(f\otimes u_0)=f$，完整正交投影是
$$
P_{\ker C}(f\otimes\Omega)=\mathcal R H^{-1}f.
\tag{2.3}
$$
因此 (1.3) 的全部坐标为
$$
r_0=f-h,\qquad
r_j=(-1)^{j+1}\frac{A^jh}{p_j}\quad(1\le j<d),
\qquad r_j=0\quad(j\ge d).
\tag{2.4}
$$
同一投影还给出后文使用的真实能量：
$$
\sum_{j=0}^{d-1}\left\|\frac{A^jh}{p_j}\right\|^2
=\langle Hh,h\rangle
=\langle H^{-1}f,f\rangle
\le\|f\|^2.
\tag{2.5}
$$
这里保留了 $H^{-1}$，没有将它移过 $A$ 或将 $H^{-1}f$ 换成 $f$。

## 3. 完整最小列的有限公式

定义 $g_j=0$ 对所有 $j\ge d-1$，并对 $1\le j\le d-1$ 置
$$
\boxed{
g_{j-1}
=(-1)^{j+1}p_{j-1}
\sum_{k=j}^{d-1}
\frac{(A^*)^{k-j}A^kh}{p_k^2}.
}
\tag{3.1}
$$
则
$$
\boxed{g_f=\sum_{j=0}^{d-2}g_j\otimes u_j.}
\tag{3.2}
$$

先核全部方程。对 $1\le j\le d-2$，
$A^*g_j+a_jg_{j-1}$ 中 $k\ge j+1$ 的项逐项抵消，只剩
$(-1)^{j+1}A^jh/p_j=r_j$。在 $j=d-1$，同式只剩
$a_{d-1}g_{d-2}=r_{d-1}$。底行是
$$
A^*g_0
=\sum_{k=1}^{d-1}\frac{(A^*)^kA^kh}{p_k^2}
=(H-I)h=f-h=r_0.
$$
所有更高行都为零，所以 $C^*g=r$。

还须核最小性，而不把一个可行提升直接称为 Moore–Penrose 列。
$\ker C^*$ 的池对称部分由从顶部反向求解得到，其全部向量只支撑在
$$
L-d+1,\ldots,L
$$
这些池占据层。因为 $L\ge2d$，它与 (3.2) 的层
$0,\ldots,d-2$ 物理正交。其余池类型也与 (3.2) 正交。因此
$g\perp\ker C^*$，证明 (3.2) 是完整最小列。

事实上，公式的最小性只需 $L\ge2d-2$；本文采用较方便的
$L\ge2d$，以统一后续每一项的分母下界。

## 4. 保完整核能量的三角卷积预算

由 (1.1)，对 $1\le\nu\le d-1$，
$$
a_\nu^2
=S\nu\left(1-\frac{\nu-1}{L}\right)
\ge\frac S2\,\nu.
\tag{4.1}
$$
令 $v_k=A^kh/p_k$。把 (3.1) 中 $k=j+\ell$ 的项写成
$$
(A^*)^\ell v_{j+\ell}\,\frac{p_{j-1}}{p_{j+\ell}}.
$$
其算子系数满足
$$
\begin{aligned}
\|(A^*)^\ell\|\frac{p_{j-1}}{p_{j+\ell}}
&\le
\|A^\ell\|
\left(\frac2S\right)^{(\ell+1)/2}
\sqrt{\frac{(j-1)!}{(j+\ell)!}}\\
&\le
\sqrt{\frac2S}\,
\frac{\|A^\ell\|(2/S)^{\ell/2}}{\sqrt{(\ell+1)!}}.
\end{aligned}
\tag{4.2}
$$
将各向后移位的有限序列视为零延拓的 $\ell^2(\mathcal H)$ 向量，
三角不等式给离散卷积的 $\ell^1$–$\ell^2$ 界。再用 (2.5)，得到
$$
\boxed{
\|g_f\|
\le
\sqrt{\frac2S}
\left[
\sum_{\ell=0}^{d-2}
\frac{\|A^\ell\|(2/S)^{\ell/2}}{\sqrt{(\ell+1)!}}
\right]
\langle H^{-1}f,f\rangle^{1/2}.
}
\tag{4.3}
$$
右端可进一步用 $\|f\|$，但 (4.3) 保留了同一真实核投影的费用。

定义与
[完整 bosonic 核预算](../notes/2026-11-14-full-boolean-kernel-bosonic-zero-occupation-and-head-only-budget-789f-next.md)
相同的真实头幂和
$$
\mathfrak C(A,\sigma)
=\sum_{\ell=0}^{d-1}
\frac{\|A^\ell\|^2}{\sigma^\ell\ell!}.
\tag{4.4}
$$
Cauchy–Schwarz 和 $\sum_{\ell\ge0}2^{-\ell}=2$ 给
$$
\left[
\sum_{\ell=0}^{d-2}
\frac{\|A^\ell\|(2/S)^{\ell/2}}{\sqrt{(\ell+1)!}}
\right]^2
\le
2\sum_{\ell=0}^{d-2}
\frac{\|A^\ell\|^2(4/S)^\ell}{(\ell+1)!}
\le2\mathfrak C(A,S/4).
$$
于是
$$
\boxed{
\|(C^*)^\dagger(f\otimes\Omega)\|^2
\le
\frac4S\,\mathfrak C(A,S/4)
\,\langle H^{-1}f,f\rangle
\le
\frac4S\,\mathfrak C(A,S/4)\|f\|^2.
}
\tag{4.5}
$$
这是一条完整 Green 列界。它没有用 $C$ 的全最小奇异值，也没有用
$\exp(2\|A\|^2/S)$ 替代真实幂和。

## 5. 原 $N/Y$ 头的显式费用

现取原物理 $A=A_m$、$d=2^m$。令
$$
k_0=\max(2m,16),\qquad \gamma=\frac{770}{16^4}>\frac1{100}.
$$
[R234 真四次头幂](R234-appendix-quartic-head-powers-and-super-four-thirds-hole-weights.md)
及前述 bosonic 核稿 §4 给
$$
\|A_m^\ell\|\le6^\ell,\qquad
\|A_m^\ell\|\le6^\ell e^{-\gamma\ell^4}\quad(\ell\ge k_0).
\tag{5.1}
$$
这些是原内积中的幂界。其实际 carry 理由是：
$N_i^2=\eta_iN_{i+1}$、$\eta_i\le e^{-770\,16^i}$；
$\ell\ge k_0$ 时进位总数至少 $\ell/4$，加权进位能量至少
$(\ell/16)^4$。原系数绝对和小于 $2$，$Y$ 型共同 Cayley 逆最多再付
$3^\ell$，遂得 (5.1)。没有使用头相似变换。

置
$$
T=\max\!\left(0,\log\frac{144}{S}\right).
$$
低阶部分至多 $k_0e^{k_0T}$。高阶使用
$$
Tx-\gamma x^4
\le\frac{3}{4^{4/3}\gamma^{1/3}}T^{4/3}
\le3T^{4/3}
$$
及剩余 $e^{-\gamma\ell^4}/\ell!$ 的和至多 $e$，得到
$$
\mathfrak C(A_m,S/4)
\le(k_0+e)\exp\!\left(k_0T+3T^{4/3}\right).
\tag{5.2}
$$
所以全部原头向量统一满足
$$
\boxed{
\|(C^*)^\dagger(f\otimes\Omega)\|^2
\le
\frac{4(k_0+e)}{S}
\exp\!\left(k_0T+3T^{4/3}\right)
\langle H^{-1}f,f\rangle.
}
\tag{5.3}
$$
保留 $\langle H^{-1}f,f\rangle$ 或将它放大为 $\|f\|^2$ 均合法。

例如固定 $M>0$，若 $S\ge d^{-M}$，则
$$
\log\!\left(S\,\|(C^*)^\dagger(f\otimes\Omega)\|^2/\|f\|^2\right)
=O_M(m^2)
\tag{5.4}
$$
作为上界成立，常数不依赖等权池长度 $L\ge2d$。
若 $S\ge c(m+1)^{-M}$，同一上界改为
$O_{c,M}(m\log(m+1))$。
这些量级属于所述完整等权池模型，不代表原慢尾拥有一个同强度、同容量的真实等权约化池。

## 6. 真实强位块的应用边界

若一个实际模型包含某个等权池，并将其余全部强位并入
$$
A_{\mathrm{rest}}=A_m+D_{\mathrm{early}},
$$
则 §§1–4 可原样应用，只须使用其真实合法幂零指数
$h_0=d+R_{\mathrm{early}}$，并要求 $L\ge2h_0$。
此时必须使用
$$
H_{\mathrm{rest}}
=\sum_{j<h_0}\frac{(A_{\mathrm{rest}}^*)^jA_{\mathrm{rest}}^j}{p_j^2},
\qquad
\mathfrak C(A_{\mathrm{rest}},S/4).
$$
不能将这些量换回 $A_m$ 的量；(5.1) 不是
$A_m+D_{\mathrm{early}}$ 的四次幂界。

同样，即使 $f=e_a$ 是固定低头，$H^{-1}e_a$ 一般也不保持其低头支持。
故 (3.1)、(4.3) 以及 (5.3) 中的幂阶仍达到真实指数 $d-1$，
不能仅因 $A_m^{a+1}e_a=0$ 就截断到 $a$。

原连续正权池的置换对称空间通常不对 $D,D^*$ 同时约化。
已有完整核投影或对称源 Schur 比较，也不能自动替换本文的完整
$C^*$ Green 列。要用于原固定测试，仍需把其余强位、实际权差及全部
零源反馈放回同一个 Green 问题，并支付其费用。本文不跳过这一步。

# 可数共同域附录：每个无限乘积正则子的强主理想单位与全部不变子商

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整加强。

本附录接续《可数个实际一阶乘子的共同自然域与不变限制上的同时图逼近》
（源 blob cdf1e129ea55a58d06853e81b7e72466222615eb）。
原稿没有把无限乘积的单射性或稠密像列入结论；这里用该特定对角构造的尾乘积和真实预解式比率补齐，并进一步得到每个固定正则子的全子商性质。

## 1. 原构造及尾乘积趋于单位

沿用原稿的最大增生正分量 $Y_i$、收缩预解式
$$
R_i(t)=(I+tY_i)^{-1}\in\mathfrak C=\{A\}',\qquad t>0,
$$
以及稠密测试族 $(h_j)$、参数 $t_{n,k}>0$：
$$
\|(R_{i_k}(t_{n,k})-I)h_j\|\le2^{-n-k}
\qquad(1\le j\le n+k).
\tag{1.1}
$$
每个正分量指标 $i$ 在 $(i_k)$ 中出现无穷多次。所有有界因子在同一个交换代数 $\mathfrak C$ 中。

固定 $n$，置
$$
P_K=\prod_{k=1}^K R_{i_k}(t_{n,k}),\qquad
S_n=\underset{K\to\infty}{\operatorname{SOT-lim}}P_K.
$$
省去前 $K$ 个因子的尾乘积
$$
Q_K=\underset{L\to\infty}{\operatorname{SOT-lim}}
\prod_{k=K+1}^L R_{i_k}(t_{n,k})
$$
由同一望远镜估计存在，并为收缩。对于 $K$ 充分大而满足 $n+K\ge j$，
$$
\boxed{\|(Q_K-I)h_j\|\le\sum_{k>K}2^{-n-k}=2^{-n-K}.}
\tag{1.2}
$$
收缩的一致范数界和测试族稠密性给
$$
\boxed{Q_K\longrightarrow I\quad{\rm SOT}.}
\tag{1.3}
$$
而有限因子剥离给准确恒等式
$$
\boxed{S_n=P_KQ_K=Q_KP_K.}
\tag{1.4}
$$

每个 $P_K$ 单射，因为每个 $R_i(t)$ 都是闭算子 $I+tY_i$ 的单值逆。
因此若 $S_nx=0$，(1.4) 迫 $Q_Kx=0$ 对每个 $K$ 成立；
(1.3) 再给 $x=0$。所以
$$
\boxed{\ker S_n=\{0\}.}
\tag{1.5}
$$
这里使用了尾乘积趋单位，不是从“每个有限乘积单射”直接传给其强极限。

## 2. 有限前缀的实际有界除法

对同一最大增生 $Y$ 及 $s,t>0$，定义
$$
U(t,s)=\frac ts I+\left(1-\frac ts\right)(I+sY)^{-1}.
\tag{2.1}
$$
它是有界交换子。由于 $(I+sY)^{-1}H\subseteq\operatorname{Dom}Y$，
真实预解式恒等式给
$$
U(t,s)=(I+tY)(I+sY)^{-1}
$$
作为全空间上的有界算子，并且
$$
\boxed{(I+tY)^{-1}U(t,s)=(I+sY)^{-1}.}
\tag{2.2}
$$
这里没有把两个无界算子相除；右侧 (2.1) 已给出全域有界公式。
交换 $s,t$ 得 $U(t,s)^{-1}=U(s,t)$，但后续只需要 (2.2)。

固定 $K$，把有限前缀的各参数同时换为 $s>0$，置
$$
F_K(s)=\prod_{k=1}^K R_{i_k}(s),\qquad
U_K(s)=\prod_{k=1}^K
\left[
\frac{t_{n,k}}s I+
\left(1-\frac{t_{n,k}}s\right)R_{i_k}(s)
\right].
\tag{2.3}
$$
它们属于 $\mathfrak C$，而
$$
\boxed{P_KU_K(s)=F_K(s),\qquad \|F_K(s)\|\le1.}
\tag{2.4}
$$
对每个固定 $K$，有限乘积的强收敛给 $F_K(s)\to I$ 当 $s\downarrow0$。

可选 $s_K>0$，使
$$
\|(F_K(s_K)-I)h_j\|\le2^{-K}\qquad(1\le j\le K).
\tag{2.5}
$$
记 $U_K=U_K(s_K)$、$F_K=F_K(s_K)$。于是由 (1.4)、(2.4) 和交换性，
$$
\boxed{S_nU_K=Q_KF_K,\qquad \|S_nU_K\|\le1.}
\tag{2.6}
$$
对每个固定测试向量 $h_j$，充分大 $K$ 时
$$
\begin{aligned}
\|(S_nU_K-I)h_j\|
&\le\|Q_K(F_K-I)h_j\|+\|(Q_K-I)h_j\|\\
&\le2^{-K}+2^{-n-K}.
\end{aligned}
$$
再用 (2.6) 的一致范数界，得到
$$
\boxed{S_nU_K\longrightarrow I\quad{\rm SOT}.}
\tag{2.7}
$$

因此每个固定 $S_n$ 都有一个范数至多 $1$ 的强主理想单位逼近。
$U_K$ 自身的范数可随 $K$ 很大；证明没有要求它们一致有界。

由于 $\mathfrak C=\operatorname{SOT\!-\!cl}\mathbb C[A]$，固定左乘 $S_n$
对 SOT 连续，(2.7) 也说明
$$
I\in\operatorname{SOT\!-\!cl}\bigl(S_n\mathbb C[A]\bigr).
\tag{2.8}
$$
这里只对 (2.7) 中的真实有界除法因子断言一致收缩界；
没有另行断言某条多项式逼近序列也自动具有同一范数界。

## 3. 所有有限放大不变子商都单射且像稠密

固定有限放大，并把 $S_n,U_K$ 换成相应对角放大。
它们仍交换、保持全部闭 $A$ 放大不变子空间，且 (2.6)—(2.7) 仍成立。

设 $\mathcal N\subseteq\mathcal M$ 为两个这样的闭不变空间，考虑商
$\mathcal Q=\mathcal M/\mathcal N$。若 $x\in\mathcal M$ 且 $S_nx\in\mathcal N$，
则交换性及 $U_K\mathcal N\subseteq\mathcal N$ 给
$$
S_nU_Kx=U_KS_nx\in\mathcal N.
$$
由 (2.7) 和 $\mathcal N$ 闭，$x\in\mathcal N$。
所以 $(S_n)_{\mathcal Q}$ 单射。

另一方面，对每个 $x\in\mathcal M$，
$U_Kx\in\mathcal M$ 且 $S_nU_Kx\to x$。
故 $(S_n)_{\mathcal Q}$ 的像稠密。于是
$$
\boxed{
(S_n)_{\mathcal Q}\text{ 在每个非零有限放大不变子商上均为 quasiaffinity}.
}
\tag{3.1}
$$
特别 $S_n|_{\mathcal M}$ 的像在 $\mathcal M$ 中稠密。

以上只用同一组全空间有界算子和真实强收敛，没有从全空间稠密像直接推限制稠密像。

## 4. 准确的循环子空间保持

取任意 $x\in H$，令 $\mathcal M_x=\operatorname{cyc}_A(x)$。
由于 $S_n$ 与 $A$ 交换，
$$
\operatorname{cyc}_A(S_nx)
=\overline{S_n\mathcal M_x}.
$$
由第3节，
$$
\boxed{\operatorname{cyc}_A(S_nx)=\operatorname{cyc}_A(x).}
\tag{4.1}
$$
于是每个非零向量在保持其整个闭循环子空间的情况下，都可经每个 $S_n$
送入原稿的可数共同自然 word 域；原稿还给 $S_nx\to x$。

这不意味着每个 $wS_n$ 都具有全子商稠密像。
一般一阶 $X_\nu$ 的限制像问题仍需另证，不能把 (3.1) 直接传给一个含无界 word 的乘积。

## 5. 加强范围与边界模型

原稿关于全部有限 mixed words 的真实域、$wS_n$ 的有界性、联合图逼近，
以及 R186 已有闭最大多项式的图核心结论均保持不变。
本附录只把原先保留的单射/稠密像问题，用这个特定构造实际闭合。

如果列表含有一个非 $\ell^1$ 的一阶系数列，原稿已证明 $S_n$ 不在 UHF 中。
因此本附录没有把 $S_n$ 送入负整数边界表示的理由；
也不能把这里的全 Haar 子商正则化移作 R200 中 $M=\ker T_N$ 或 $\ker T_Y$
的边界右移域稠密性证明。

## 6. 不能把“可数族”升级为全部 $\ell^2$ 系数

记不含常数项的闭一阶为
$$
X_a=\overline{\sum_{j\ge0}a_jV_j},\qquad a\in\ell^2,
$$
闭实现与核心均按 R125。令
$$
\mathscr D_{\rm all}=\bigcap_{a\in\ell^2}\operatorname{Dom}X_a.
$$
下面的反面完全使用原 Haar 表示。

**命题。** 设 $0\ne M\subseteq H$ 为闭 $A$ 不变空间。
若有界交织 $K:M\to H$ 满足
$$
KA|_M=AK,\qquad K(M)\subseteq\mathscr D_{\rm all},
\tag{6.1}
$$
则 $K=0$。

先付清参数方向的闭图。固定 $f\in\mathscr D_{\rm all}$。
在有限柱 $z$ 上，纯创建、删除、次数三块以及有界 carry 给
$$
\|X_a^*z-X_b^*z\|\le C_z\|a-b\|_2.
\tag{6.2}
$$
例如当 $z$ 的 Walsh 次数至多 $p$ 时，可用有限常数
$C_z=(4\sqrt{p+1}+8\|\eta\|_2)\|z\|$，增大该常数也不影响证明。
有限柱是每个 $X_a^*$ 的图核心。

若 $a_l\to a$ 于 $\ell^2$，且 $X_{a_l}f\to y$ 于 $H$，则由 (6.2)
$$
\langle y,z\rangle
=\lim_l\langle f,X_{a_l}^*z\rangle
=\langle f,X_a^*z\rangle.
$$
伴随核心识别给 $f\in\operatorname{Dom}X_a$ 且 $X_af=y$。
同一核心配对还证明
$a\mapsto X_af$ 在整个 $\ell^2$ 上线性。因此这个全域线性映射闭，
由闭图定理存在 $C_f<\infty$，使
$$
\|X_af\|\le C_f\|a\|_2.
\tag{6.3}
$$

在 (6.1) 下，对每个固定 $a$，
$X_aK$ 为从 Banach 空间 $M$ 到 $H$ 的全域闭算子，
故 $X_aK$ 有界。另一方面，把 (6.3) 用于每个固定 $f=Kx$，得到
$$
\sup_{\|a\|_2\le1}\|X_aKx\|<\infty
\qquad(x\in M).
$$
现在对有界算子族 $\{X_aK:\|a\|_2\le1\}$ 使用一致有界原理：
$$
\boxed{\sup_{\|a\|_2\le1}\|X_aK\|=C_K<\infty.}
\tag{6.4}
$$
次序是先在参数 $a$ 上闭图，再对每个 $a$ 在输入 $x$ 上闭图，
最后才使用一致有界原理；没有预设一个联合有界的无界乘子映射。

取固定 $x\in M$，令 $h=Kx$。固定整数 $r\ge1$，对高位 $r$ 元集合 $F$ 置
$$
N_F=\prod_{j\in F}N_j,\qquad
a_j^F=r^{-1/2}{\bf1}_{j\in F}.
$$
则 $\|a^F\|_2=1$。有限多项式交织给
$N_Fx\in M$ 及 $KN_Fx=N_Fh$。

实际恒等式
$$
(V_j-I)N_j=-2N_j^2(I+N_j)^{-1}
$$
和 $\|N_j^2\|\le\eta_j$、$\|(I+N_j)^{-1}\|\le3$ 给
$$
\boxed{
\|X_{a^F}N_F-\sqrt r\,N_F\|
\le \frac6{\sqrt r}\sum_{j\in F}\eta_j.
}
\tag{6.5}
$$
对每个固定向量 $v\in H$，固定 $r$ 后令 $\min F\to\infty$，
有限柱逼近及 $\|N_F-E_F\|\le\sum_{j\in F}\eta_j$ 给
$$
\|N_Fv\|\longrightarrow2^{-r/2}\|v\|.
\tag{6.6}
$$
这里 $E_F$ 作用在固定有限柱头之外时其平方范数恰乘 $2^{-r}$；
实际乘积与纯乘积的误差已由 (6.5)—(6.6) 支付。

由 (6.4)，
$$
\|X_{a^F}N_Fh\|
=\|X_{a^F}K N_Fx\|
\le C_K\|N_Fx\|.
$$
先固定 $r$，再用 (6.5)—(6.6) 令高位移走，得到
$$
\sqrt r\,2^{-r/2}\|Kx\|
\le C_K\,2^{-r/2}\|x\|.
$$
约去正数 $2^{-r/2}$ 后令 $r\to\infty$，迫 $Kx=0$。
$x$ 任意，故 $K=0$。

逐分量的同一闭图配对和高位范数极限，也给任意固定有限放大上的
$K:M\subseteq H^d\to H^e$ 版本。此处未把命题外推至任意子商。

这个反面不与前文冲突：每个指定的可数族有共同正则子，
但若要求其范围同时落在全部不可数 $\ell^2$ 参数的自然域中，
闭图与一致有界原理就会强制 (6.4)，而真实高位乘积排除了这个一致界。

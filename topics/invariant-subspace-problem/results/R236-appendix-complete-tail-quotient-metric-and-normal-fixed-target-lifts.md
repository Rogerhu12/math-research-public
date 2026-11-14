# R236 附录：完整尾商的逐位完全有界费用、实际图度量及固定目标的远尾提升

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的定量接口。** 本文把 $h/k$ 商修正的费用直接等同于逐位尾商逆映射的费用，并给实际有限放大图延拓的近最优度量。它不声称该费用一致有界；正常性下的固定远尾目标另有明确发散下界。

依赖：[完整正常尾商](R236-appendix-normal-tail-ideal-closure-and-finite-amplification.md)、[实际翻转分支及 h/k 源](R236-appendix-dyadic-flip-ideals-and-branch-lifting-cost.md)、[同一正常表示与未来尾](R236-appendix-fixed-normal-tail-representation-and-tail-preserving-unit-lifting-cost.md)。

## 1. 完整一次尾商逆的完全有界范数

使用原实际物理分块
$$
N=\begin{pmatrix}0&t\\I&0\end{pmatrix},\quad
t=\eta N_{\rm next},\quad \|N\|=1,
$$
$$
\mathcal C=\mathcal B\oplus N\mathcal B,
\qquad S=D(N+G),\quad Z=E+NF,
\qquad h=G^2-t,\quad k=E-GF.
$$
$\mathcal B$ 是完整下一尾交换子。取任一范数闭尾理想 $K\ni h,k$，
并置
$$
J=\{a+Nb:a-Gb\in K\}.
$$
原完整两生成元范数闭理想和超弱闭理想都属于这一范围。
假设 $K\ne\mathcal B$，记
$$
Q_1=\mathcal B/K,\qquad Q_0=\mathcal C/J,
\qquad m=\operatorname{dist}_{\mathcal B}(G,K).
$$

尾包含给含单位、完全契约的代数双射
$$
\iota:Q_1\longrightarrow Q_0,
$$
其逆是准确余式
$$
\Theta([a+Nb])=a-Gb+K.
\tag{1.1}
$$
乘法性使用 $G^2-t\in K$，满射性使用 $N+G\in J$。
在原商算子空间矩阵范数下，有
$$
\boxed{
\max\{1,m\}\le\|\Theta\|\le\|\Theta\|_{cb}
\le\sqrt{1+m^2}.
}
\tag{1.2}
$$

**证明。** 单位给下界 $1$。
$\Theta([N])=-G+K$ 且 $\|[N]\|_{Q_0}\le1$，故另有下界 $m$。

对任意 $\epsilon>0$，取 $H\in K$ 使
$\widetilde G=G-H$ 的原范数不超过 $m+\epsilon$。
任意矩阵级的 $R=a+Nb$ 的实际首物理列为 $\operatorname{col}(a,b)$，所以
$$
\|\operatorname{col}(a,b)\|\le\|R\|.
$$
同一商余式可以写成 $a-\widetilde G b$，因此
$$
\|a-\widetilde G b\|
\le\|(I,-\widetilde G)\|\,
\|\operatorname{col}(a,b)\|
\le\sqrt{1+(m+\epsilon)^2}\,\|R\|.
$$
这是逐个矩阵级同一常数的界；对 $R$ 的近最小商代表再取下确界，
然后令 $\epsilon\downarrow0$，即得 (1.2)。证毕。

若 $J,K$ 超弱闭，$\iota$ 和 $\Theta$ 也都正常：包含正常，
而实际两个块压缩及固定 $G$ 乘法均正常。
所以每一位都确有正常完全有界逆，且其费用准确被 (1.2) 夹住。
这并没有给不同位之间的一致逆常数。

特别，$h/k$ 修正若把 $m_l$ 降到有界子列，便也把这些逐位逆的完全有界范数降到有界子列；
反过来，逐位逆的统一完全有界估计已经包含所需的 $G_l$ 商上界。
该问题不能靠把“有逆”改写为“完全有界有逆”来省略费用。

## 2. 实际有限放大中的图延拓与近最优费用

现在设
$$
\pi:\mathcal B\to B(\mathscr Q)
$$
是原 $\mathscr H_{\rm next}^{\oplus d}$ 中的正常、含单位、完全契约半不变压缩，
且 $\pi(K)=0$。令
$$
g=\pi(G),\qquad \tau=\pi(t),\qquad g^2=\tau.
$$
条目级应用 $\pi$ 给原当前尾的正常完全契约表示
$$
\Pi(a+Nb)=
\begin{pmatrix}\pi(a)&\tau\pi(b)\\\pi(b)&\pi(a)\end{pmatrix}
\quad\text{于 }\mathscr Q\oplus\mathscr Q.
\tag{2.1}
$$
其不变图空间
$$
\mathscr L_g=\{(-gx,x):x\in\mathscr Q\}
\tag{2.2}
$$
被 $\Pi(S)$、$\Pi(Z)$ 同时杀掉。
这由 $g^2=\tau$ 和 $\pi(E)-g\pi(F)=0$ 直接逐块核对。

写 $X=(I+g^*g)^{1/2}$。等距参数化
$$
Vx=(-gX^{-1}x,X^{-1}x)
$$
把图限制在原 $\mathscr Q$ 上表示成
$$
\sigma(a)=X\pi(a)X^{-1},\qquad
\sigma(N)=-XgX^{-1}.
\tag{2.3}
$$
$\sigma$ 对整个当前尾完全契约，并杀掉 $J$。

这里图确实仍是原有限放大的半不变子商。
若 $\mathscr Q=M_0\ominus N_0$ 是原尾旗，先取
$\widetilde M=\mathbb C^2\otimes M_0$、
$\widetilde N=\mathbb C^2\otimes N_0$。
由 (2.1)，图在该商内不变，故
$$
M'=\widetilde N\oplus\mathscr L_g
$$
是 $\widetilde M$ 内的闭不变空间，且
$M'\ominus\widetilde N=\mathscr L_g$。
放大次数仍为 $d$；只恢复了原当前物理位，没有引入无限放大。

因为 $G$ 拟幂零，$g$ 也拟幂零。
拟幂零算子不可能有严格正的下模量：若 $\|gx\|\ge c\|x\|$，
则 $\|g^n\|\ge c^n$，矛盾。因此
$$
\|X\|=\sqrt{1+\|g\|^2},\qquad \|X^{-1}\|=1.
$$
图延拓的实际相似费用准确为
$$
\boxed{\kappa(X)=\sqrt{1+\|g\|^2}.}
\tag{2.4}
$$

该界距所有可能的同一尾表示相似延拓的最优费用至多一个 $\sqrt2$ 因子。
具体地，若某有界可逆 $Y$ 使 $Y\pi(\cdot)Y^{-1}$ 延为一个杀掉 $S$ 的当前尾完全契约表示，
则其 $N$ 像必为 $-YgY^{-1}$，从而
$$
\boxed{\kappa(Y)\ge\max\{1,\|g\|\}.}
\tag{2.5}
$$
当 $\|g\|\to\infty$，(2.4) 与 (2.5) 的比趋于一。
所以这里的大图度量费用不只是所选图参数化的粗糙上界。

对单位向量 $v\in\mathscr Q$，原实际图向量 $(-gv,v)$ 的范数平方是
$1+\|gv\|^2$。它归一化后给新的正正常图状态，单位锚为一；
未归一化的锚和费用必须按这个准确因子保留。
这一般改变原尾状态，并不保持原 $\rho$ 的全部配对。
本文没有把这个新的正态与此前的同一 $\rho$ 右测试混用。

## 3. 固定非标量目标向无限远尾提升的费用必发散

这一结论只用原物理尾与正常性，可以用于固定的同一 $\pi$。
固定某起点 $s$，设
$$
\pi:\mathcal C_s\to B(\mathscr Q)
$$
是原 $\mathscr H_s^{\oplus d}$ 中的正常含单位半不变压缩。
给定一个非标量 $T\in B(\mathscr Q)$，假设
$T\in\pi(\mathcal C_l)$ 对所有 $l\ge s$ 成立，记
$$
c_l(T)=\inf\{\|R\|:R\in\mathcal C_l,\ \pi(R)=T\}.
\tag{3.1}
$$
则 $c_l(T)$ 非减，并且
$$
\boxed{c_l(T)\longrightarrow\infty.}
\tag{3.2}
$$

先给不含速度假设的紧性证明。
若沿某无限子列有统一有界代表 $R_l\in\mathcal C_l$，
从原算子球取超弱聚点 $R$。每个固定 $n$ 后，该子列最终全属于
$I_{[s,n)}\otimes B(\mathscr H_n)$，故
$$
R\in\bigcap_n\bigl(I_{[s,n)}\otimes B(\mathscr H_n)\bigr)=\mathbb C I.
$$
最后的交等式是原有限头矩阵代数的不可约性。
正常性给 $\pi(R)=T$，迫 $T$ 标量，矛盾。
没有用代数像相等推出统一提升。

在实际有限放大中，还有一个固定正常配对的显式下界。
因为 $T$ 非标量，可选同一对单位向量 $v,w\in\mathscr Q$，使
$$
\langle v,w\rangle=0,\qquad
b=|\langle Tv,w\rangle|>0.
$$
令 $P_l$ 为原前 $l-s$ 位张量尾真空的正交投影，并在 $d$ 重放大上使用同一记号。
记
$$
\epsilon_l(v)=\|(I-P_l)v\|,\qquad
\epsilon_l(w)=\|(I-P_l)w\|.
$$
二者都趋零。对任意原尾 $R\in\mathcal C_l$，分解两个向量并用
$$
\langle R P_lv,P_lw\rangle
=\langle R\Omega_l,\Omega_l\rangle\,
  \langle P_lv,P_lw\rangle,
$$
以及 $\langle P_lv,P_lw\rangle=-\langle(I-P_l)v,(I-P_l)w\rangle$，得
$$
|\langle\pi(R)v,w\rangle|
\le \|R\|\,[\epsilon_l(v)+\epsilon_l(w)+\epsilon_l(v)\epsilon_l(w)].
$$
因此
$$
\boxed{
c_l(T)\ge
\frac{b}{\epsilon_l(v)+\epsilon_l(w)+\epsilon_l(v)\epsilon_l(w)}.
}
\tag{3.3}
$$
配对 $v,w$、非零锚 $b$ 和物理放大都固定；没有逐层换测试。
若分母在某层为零，则该层根本不存在 $T$ 的尾代表，与本节假设矛盾。

原固定表示中的所有未来像代数相等时，(3.2) 可具体取
$T=\pi(N_s)$。这个 $T$ 不可能为零：若为零，则后续所有
$\pi(N_l)$ 都为零，与正常弱极限 $\pi(N_l)\to I/2$ 矛盾。
而 $\pi(N_s)$ 拟幂零，故也不可能是非零标量。
所以这确实给一个固定实际算子目标，除此前随层变化的 $U_l$ 外，
其向远尾提升的原范数也必发散。

## 4. 对当前 $h/k$ 主目标的用途与范围

(1.2) 把完整两生成元代表费用直接量化为逐位正常完全有界逆的费用。
(2.4)–(2.5) 给实际有限放大中可执行且近最优的图度量，没有更换原物理范数。
(3.3) 则说明即使所有未来像代数在同一个表示中相等，
固定非标量目标也不能被一致有界地推到无限远尾。

这些结论没有证明不同 $l$ 的 $m_l$ 有界，也没有构造足够便宜的实际 $h/k$ 修正。
它们将“商代表”“逐位完全有界逆”和“恢复前一物理位的相似度量”放到同一费用表中；
真正要解决的仍是原特殊两行能否把其中的 $m_l$ 降下来，或给另一种保同一正常锚的目标。

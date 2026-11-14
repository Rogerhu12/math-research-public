# R237 附录：渐近收缩有限柱逼近与主理想同范数强密度

日期：2026-11-12（UTC）。独占作者：normal_next。

状态：以下初等算子扩张、真正条件期望的渐近双模性、主理想同范数强逼近及 R253 真空测试等价式均有完整证明。它不证明 R253 的 $q_m$ 统一正下界，不把 $A'$ 中的非 UHF 算子自动纳入相对乘法结论，也不声称普通 ISP 完成。

## 1. 结论及记号

沿用 [R88](../results/R88-riesz-basis-bounded-multipliers-strong-closure.md)：
$$
\mathcal U=C^*(I,A),\quad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\quad
\mathscr C=\{A\}',\quad
\mathscr E=\{E_j:j\ge0\}'.
$$
$\mathcal U$ 为原表示中的 UHF 范数代数。设
$$
H=H_{<n}\otimes H_{\ge n},\qquad
J_n:H_{<n}\to H,\quad J_nh=h\otimes\Omega_{\ge n}.
$$
本文的真正有限头条件期望是
$$
\boxed{\mathbb E_n(T)=(J_n^*TJ_n)\otimes I_{\ge n}\qquad(T\in B(H)).}
\tag{1.1}
$$
这是 $B(H)$ 到有限头矩阵代数张量尾恒等的收缩正映射。它不是有限秩正交投影 $\Pi_n=J_nJ_n^*$；(1.1) 的输出算子仍作用于全 $H$。

R88 的有限柱乘子逼近记为
$$
\Psi_n(F)=X_{\,\Pi_nF1}\in\mathcal A
\qquad(F\in\mathscr C).
\tag{1.2}
$$

**主定理。** 存在与 $F$ 无关的 $\varepsilon_n\downarrow0$（把原误差换成其尾上确界即可），使
$$
\boxed{\|\Psi_n(F)-\mathbb E_n(F)\|\le\varepsilon_n\|F\|,
\qquad
\|\Psi_n(F)\|\le(1+\varepsilon_n)\|F\|.}
\tag{1.3}
$$
此外 $\Psi_n(F)\to F$ 于 SOT 及 SOT$^*$。

对每个固定 $Q\in\mathcal A$，还存在 $\kappa_n(Q)\to0$，使
$$
\boxed{\|\Psi_n(QF)-Q\Psi_n(F)\|
\le\kappa_n(Q)\|F\|\qquad(F\in\mathscr C).}
\tag{1.4}
$$
特别，对每个固定 $F\in\mathscr C$，存在 $T_n\in Q\mathcal A$ 满足
$$
\boxed{\|T_n\|\le\|QF\|,\qquad T_n\longrightarrow QF
\quad\text{SOT 和 SOT}^*.}
\tag{1.5}
$$
所有实际 carry 均通过 R88 的真实 Riesz 变换保留。这里没有把 R88 的线性对应误作代数同构。

## 2. 真正条件期望的两个性质

首先，若 $g$ 只依赖前 $r$ 位，则对 $n\ge r$，
$$
\mathbb E_n(T)g=\Pi_nTg.
$$
因此 $\mathbb E_n(T)g\to Tg$。有限柱稠密，且 $\|\mathbb E_n(T)\|\le\|T\|$，所以
$$
\mathbb E_n(T)\to T\quad\text{SOT}.
\tag{2.1}
$$
又 $\mathbb E_n(T)^*=\mathbb E_n(T^*)$，同一论证给 SOT$^*$ 收敛。

其次，若 $L,R$ 都只作用于前 $r$ 位，则 $n\ge r$ 时有准确双模等式
$$
\mathbb E_n(LTR)=L\mathbb E_n(T)R
\qquad(T\in B(H)).
\tag{2.2}
$$
这可以直接从 (1.1) 的张量矩阵元核验。

若只知道 $L,R\in\mathcal U$，以有限局部矩阵在范数中逼近它们。利用 $\|\mathbb E_n\|\le1$，从 (2.2) 得到
$$
\boxed{
\sup_{\|T\|\le1}
\|\mathbb E_n(LTR)-L\mathbb E_n(T)R\|
\longrightarrow0.
}
\tag{2.3}
$$
例如将 $L,R$ 替换为局部 $L_0,R_0$，两边的替换误差之和至多
$$
2\|L-L_0\|\|R\|+2\|L_0\|\|R-R_0\|.
$$
先选局部逼近，再取 $n$ 大于其支撑，即得 (2.3)。

同理，对固定 $Q\in\mathcal U$，记
$$
\mu_n(Q)=\sup_{\|T\|\le1}
\|\mathbb E_n(QT)-Q\mathbb E_n(T)\|.
$$
则
$$
\boxed{\mu_n(Q)\to0.}
\tag{2.4}
$$
这个结论依赖 $Q\in\mathcal U$；不对任意 $Q\in B(H)$ 声称它成立。

## 3. R88 对应在全部 B(H) 上的初等算子扩张

为避免与实际 Cayley 因子混淆，本节沿用 R88 的两个生成元但将纯者改记为 $D_j$：
$$
U_j=I-2N_j,\qquad D_j=I-2E_j.
$$
于是
$$
\|U_j\|,\|D_j\|\le3,\qquad
\|U_j-D_j\|\le2\eta_j,\qquad
\eta_j\le e^{-770\,16^j}.
\tag{3.1}
$$
R88 给出可逆 $W\in\mathcal U$，
$$
W\chi_F=U_F1,\qquad \|W-I\|\le\rho<1,
$$
以及有界线性双射
$$
\Phi:\mathscr E\longrightarrow\mathscr C,\qquad
\Phi(P)1=P1,\qquad
\|\Phi^{-1}(F)\|\le(1+\rho)^2\|F\|.
\tag{3.2}
$$

对 $K\subset[0,j)$，令 $Q_{j,K}$ 为 R88 的局部秩一头算子张量尾恒等：
$$
Q_{j,K}\Big(\sum_Fc_F\chi_F\Big)
=\sum_{L\subset(j,\infty)}c_{K\cup\{j\}\cup L}\chi_L.
$$
它属于 $\mathcal U$ 且范数为 1。R88 §4 的完整排序式给
$$
\Phi(P)=
\left[
P+\sum_{j\ge0}\sum_{K\subset[0,j)}
U_K(U_j-D_j)P Q_{j,K}
\right]W^{-1}
\qquad(P\in\mathscr E).
\tag{3.3}
$$

关键是这不只在 $\mathscr E$ 上有界。因为
$$
\begin{aligned}
&\sum_{j\ge0}\sum_{K\subset[0,j)}
\|U_K(U_j-D_j)\|\,\|Q_{j,K}W^{-1}\|\\
&\qquad\le
2\|W^{-1}\|\sum_{j\ge0}\eta_j
\sum_{K\subset[0,j)}3^{|K|}
=
2\|W^{-1}\|\sum_{j\ge0}\eta_j4^j<\infty,
\end{aligned}
\tag{3.4}
$$
右侧 (3.3) 对任意 $P\in B(H)$ 都按初等算子范数绝对收敛。
记所得有界线性扩张为 $\widetilde\Phi:B(H)\to B(H)$。

这个扩张的每一项形如 $P\mapsto LPR$，而其左右系数均在 $\mathcal U$：
$U_K,U_j,D_j,Q_{j,K},W^{-1}$ 全部属于原 UHF 代数。
由 (2.3)，每个固定项与 $\mathbb E_n$ 渐近交换，且对 $\|P\|\le1$ 一致。
再用 (3.4) 截断绝对收敛的算子级数，得到
$$
\boxed{
d_n:=
\|\mathbb E_n\widetilde\Phi-\widetilde\Phi\mathbb E_n\|_{B(B(H))}
\longrightarrow0.
}
\tag{3.5}
$$
尾项的交换误差至多是其初等算子范数尾的两倍，所以此处没有把仅逐向量收敛提升为算子范数收敛。

## 4. 有限柱逼近成为渐近收缩

若 $P\in\mathscr E$，R88 §7 给
$$
\mathbb E_n(P)\in\mathscr E,\qquad
\mathbb E_n(P)1=\Pi_nP1.
$$
所以对 $F\in\mathscr C$，取 $P=\Phi^{-1}(F)$，由有限柱乘子的唯一性，
$$
\boxed{\Psi_n(F)=\Phi(\mathbb E_n(P))
=\widetilde\Phi(\mathbb E_n(P)).}
\tag{4.1}
$$
另一方面 $F=\widetilde\Phi(P)$。故由 (3.5) 和 (3.2)，
$$
\begin{aligned}
\|\Psi_n(F)-\mathbb E_n(F)\|
&=\|(\widetilde\Phi\mathbb E_n-\mathbb E_n\widetilde\Phi)(P)\|\\
&\le d_n(1+\rho)^2\|F\|.
\end{aligned}
\tag{4.2}
$$
取 $\varepsilon_n=(1+\rho)^2\sup_{k\ge n}d_k$，即得 (1.3)。
(2.1) 及 (4.2) 同时给 SOT、SOT$^*$ 收敛。

特别，$\mathcal A$ 的单位球在 $\mathscr C$ 的单位球中强且强$^*$稠密。
准确地，给定 $F\ne0$，令
$$
c_n=\max\left(1,\frac{\|\Psi_n(F)\|}{\|F\|}\right)\to1,
\qquad A_n=c_n^{-1}\Psi_n(F).
$$
则 $A_n\in\mathcal A$、$\|A_n\|\le\|F\|$，且 $A_n\to F$ 强、强$^*$。
对 $F=0$ 取 $A_n=0$。
这里缩放的是有限柱乘子；无需声称原 $\Psi_n$ 每一步已经恰为收缩映射。

## 5. 固定范数代数左因子的相对乘法误差

固定 $Q\in\mathcal A\subset\mathcal U$。将差分成三项：
$$
\begin{aligned}
\Psi_n(QF)-Q\Psi_n(F)
&=[\Psi_n(QF)-\mathbb E_n(QF)]\\
&\quad+[\mathbb E_n(QF)-Q\mathbb E_n(F)]\\
&\quad+Q[\mathbb E_n(F)-\Psi_n(F)].
\end{aligned}
$$
由于 $QF\in\mathscr C$，两端误差均可用 (1.3)，中间误差用 (2.4)，故
$$
\boxed{
\|\Psi_n(QF)-Q\Psi_n(F)\|
\le\bigl(2\varepsilon_n\|Q\|+\mu_n(Q)\bigr)\|F\|.
}
\tag{5.1}
$$
这证明 (1.4)，而且对 $\|F\|\le1$ 一致。

特别，若 $F$ 固定，记 $B_n=Q\Psi_n(F)\in Q\mathcal A$。
它强、强$^*$趋于 $QF$，并且由 (5.1) 和 (1.3)，
$$
\limsup_n\|B_n\|\le\|QF\|.
\tag{5.2}
$$
若 $QF\ne0$，取
$$
s_n=\max\left(1,\frac{\|B_n\|}{\|QF\|}\right)\to1,
\qquad T_n=s_n^{-1}B_n.
$$
即得 (1.5)。若 $QF=0$，直接取 $T_n=0$ 即可。

(5.1) 没有在未知输入上除以 $Q$，也没有要求 $Q$ 单射或可逆。
它同样没有给出
$\|\Psi_n(QF)-Q\Psi_n(F)\|\le o(1)\|QF\|$
这种更强的相对界：当前右边仍为 $o(1)\|F\|$。
因此若 $F$ 随 $n$ 无界增长，不能免费使用该误差。

## 6. 正常泛函的主理想测试范数不因扩右因子而改变

对固定 $Q\in\mathcal A$，令
$$
\mathcal J_Q=\overline{Q\mathcal A}^{\|\cdot\|}.
$$
若 $\varphi$ 是任意正常迹类泛函，则
$$
\boxed{
\|\varphi|_{\mathcal J_Q}\|
=
\sup_{\substack{F\in\mathscr C\\\|QF\|\le1}}
|\varphi(QF)|.
}
\tag{6.1}
$$

右边不小于左边：先对 $Q\mathcal A$ 的元素取上确界，再用范数闭包和必要的标量缩放。
反过来，对每个固定 $\|QF\|\le1$，(1.5) 给 $T_n\in Q\mathcal A$、$\|T_n\|\le1$ 和 $T_n\to QF$ 强。正常泛函在一致有界强收敛序列上连续，故
$$
|\varphi(QF)|=\lim_n|\varphi(T_n)|
\le\|\varphi|_{\mathcal J_Q}\|.
$$
最后取上确界即得 (6.1)。

所用正常连续性可以由迹类密度的有限秩范数逼近直接证明：
有限秩部分对强收敛连续，迹范数尾乘统一算子范数控制。
不把它推广到无界强逼近网。

## 7. R253 全部尾理想的准确等价式

对 [R253](../results/R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md) 的每个固定尾空间 $H_m$，
记
$$
\mathcal B_m=\overline{\mathbb C[I,\widehat N_m]}^{\|\cdot\|},
\qquad
\mathfrak C_m=\{\widehat N_m\}'.
$$
该尾具有同样的真实局部递归，误差行只是 $\eta_{m+j}$；R88 的 Riesz 构造与本稿 §2–6 在该尾逐字适用。具体地可取统一包络
$
\bar\rho=2\sum_{j\ge0}e^{-770\,16^j}10^{j/2}<1,
\qquad
\rho^{(m)}=2\sum_{j\ge0}\eta_{m+j}10^{j/2}\le\bar\rho.
$
所以 $\|\Phi_m^{-1}\|\le(1+\bar\rho)^2$，初等扩张的绝对和也由
$2(1-\bar\rho)^{-1}\sum_j e^{-770\,16^j}4^j$ 统一控制。
本稿只需每个固定 $m$ 的条件期望指标趋于无穷，没有额外声称两个指标任意联动时的统一误差率。
这些都是同一个实际尾算子，未把不同 $m$ 的权算子互相等同。

令 $Q_m\in\mathcal B_m$ 为 R253 的非零相位消元符号，
$\mathcal J_m=\overline{Q_m\mathcal B_m}^{\|\cdot\|}$，
$\omega_m(T)=\langle T\Omega_m,\Omega_m\rangle$。
于是
$$
\boxed{
q_m=\|\omega_m|_{\mathcal J_m}\|
=
\sup_{\substack{F\in\mathfrak C_m\\\|Q_mF\|\le1}}
|\omega_m(Q_mF)|.
}
\tag{7.1}
$$
因此可以在完整尾交换子中寻找有界右因子来估计 $q_m$，不会改变 R253 原先范数理想的测试量。

一个精确的条件应用是：若对某个固定 $m$ 能找到收缩 $P$ 和有界 $G\in\mathfrak C_m$，
使 $P=Q_mG$，且存在 $F_n\in\mathfrak C_m$ 满足
$\|PF_n\|\le1$、$PF_n\to I$ 强，
则 (7.1) 给 $q_m=1$。
若还有 R253 的正尾湮灭态，它由有界强逼近将湮灭条件延到
$Q_m\mathfrak C_m$，再对 $PF_n=Q_m(GF_n)$ 取极限便与正迹矛盾。
非负一阶预解式无穷乘积在总行平方可和时已经提供后一种强单位，
但本稿**没有构造前面的有界因式 $P=Q_mG$**。

## 8. 量词边界

新增的是有限柱逼近与真正条件期望的统一范数接近，固定 $Q\in\mathcal A$ 的渐近乘法性质，以及原主理想的同范数强逼近。
它加强了 R88 的固定常数范数界，并使 R253 的完整交换子右因子测试合法化。

尚未给 $q_m$ 的非消失统一下界，未给 $Q_m^{-1}P$ 有界性，也未给 R244 指定输入配对域。
相对乘法结论必须保留 $Q\in\mathcal A\subset\mathcal U$：
对位于 $\mathfrak C\setminus\mathcal U$ 的无穷预解式极限，本文不由 (5.1) 推出
其原范数代数主理想中存在同一收缩强近似单位。
源证明中的 $o(1)\|F\|$ 也不允许随着 $n$ 任意选择范数失控的右因子。

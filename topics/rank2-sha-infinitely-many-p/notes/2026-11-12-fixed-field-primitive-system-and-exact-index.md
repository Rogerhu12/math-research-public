# 固定十六域上的原始完整类群族与准确指数

日期：2026-11-12。**已证明。** 本篇将 R144 的准确长度结论
用于 R150、R153 的同一批实际点。完整 Hilbert 类群和保留；
不要求负扭曲秩一，也不删除其未知 Sha 的素因子。结论仍不证明
原点的指数 $a\le1$。

## 1. 固定对象与结论

固定
$$
 E=389\mathrm a1:\quad y^2+y=x^3+x^2-2x.
$$
令 $\mathcal D$ 为 R153 的十六个判别式，即 R150 表中用
$-532$ 替换 $-19$ 后的列表。对每个 $F=\mathbb Q(\sqrt D)$，
都有 $389$ 分裂、$\mathcal O_F^\times=\{\pm1\}$，且类群由
R150、R153 指定的分歧素理想基生成，阶 $h_F\in\{1,2,4\}$。

取充分大的普通素数 $p$，满足 $p\nmid389D$、
$a_p(E)\not\equiv\pm1\pmod p$，且 $G_F$ 在 $T_pE$ 上满像。
所有固定例外可以对有限个域一次合并；R150、R153 的联合
输入已满足这些条件。令
$$
 \ell\text{ 在 }F\text{ 惰性},\qquad
 \ell+1=pu,\qquad p\nmid u a_\ell(E),
 \tag{1}
$$
并保持 $\ell$ 素于固定模型及分歧理想基。设 $L/F$ 是
$F[\ell]/F$ 的唯一次数 $p$ 子扩张，
$\Gamma=\langle\tau\rangle$。使用 R150 的固定扭点乘数 $t_0$，
并删去整除它的有限多个 $p$。原整数点为
$$
 Q=[t_0]\operatorname{Tr}_{F[\ell]/L}P[\ell],\qquad
 N_{L/F}Q=0.
 \tag{2}
$$
假定这个指定的 $Q$ 非扭。此条件已由 R150、R153 对联合
筛得到的同一批输入支付。

置
$$
 \begin{gathered}
 A=\ker\bigl(N:\operatorname{Res}_{L/F}E\longrightarrow E\bigr),
 \qquad \mathcal O=\mathbb Z_p[\zeta_p],\\
 \delta=\tau^{(p-1)/2}(\tau-1),\qquad
 A(F)\otimes\mathbb Z_p=\mathcal O w,\\
 Q=\delta^a\varepsilon w,\quad \varepsilon\in\mathcal O^\times,
 \qquad S=\Sha(A/F)[p^\infty].
 \end{gathered}
 \tag{3}
$$
格的秩一及 $S$ 有限由 R146 §1 的实际完整迹与 Nekovář
定理给出。

**定理。** 同一个原整数 Heegner 诱导族在模 $\delta$ 后
原始，并且
$$
 \boxed{\quad
 S\simeq M\oplus M,\qquad
 \operatorname{length}_{\mathcal O}M=a+1.
 \quad}
 \tag{4}
$$
尤其 R150 的 $\operatorname{length}_{\mathcal O}S\le2(a+1)$
在这些输入上准确等于 $2(a+1)$。

令
$$
 s_+=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/F)^+,
 \qquad
 s_-=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/F)^-.
$$
实际模 $\delta$ 类族的最小非零辅助素因子数为
$$
 \boxed{\qquad \nu=\max(s_+,s_-)-1.\qquad}
 \tag{5}
$$
若 $r_+=\operatorname{rank}E(\mathbb Q)$、
$r_-=\operatorname{rank}E^F(\mathbb Q)$，则
$s_\pm=r_\pm+\dim_{\mathbb F_p}\Sha(E^{\pm}/\mathbb Q)[p]$，
其中 $E^+=E$、$E^-=E^F$。这里不把负号维数擅自设为一。

## 2. 原曲线原始性定理逐域适用

Zhang（2014）Theorem 1.1 的条件是：普通 $p\ge5$、
$p\nmid D_FN$、$(D_F,N)=1$、剩余表示满像、广义 Heegner
条件及 Hypothesis $\spadesuit$。其发表版印页 194–195
明确允许一般基本判别式；没有 $D_F$ 为奇数的附加条件。

在这里 $N=389$，每个域都有 $N^+=389,N^-=1$。
R136 的模型给分裂乘法约化 $I_1$，
$v_{389}(\Delta_E)=1$。因此 $p$ 不整除 Tate 参数的估值，
$E[p]$ 在 $389$ 的惯性作用非平凡，正好满足
Hypothesis $\spadesuit$ 的全部要求。平方自由导子没有其
非平方自由分支的额外条件。

故对原 $E/F$ 的**完整类群** Heegner 族存在
$$
                    c_n^{E,\mathrm{raw}}\bmod p\ne0.
 \tag{6}
$$
Zhang 的首项本来就是 $\operatorname{Tr}_{F[1]/F}P[1]$
的 Kummer 类；其一般节点也保留全部类群 coset。
所以 (6) 不是对某个单独 Hilbert 类群角色的断言。
Howard（2004）Theorem 1.7.5 的原曲线节点修正可逆，故
这里可以按 R144 的 raw 规范使用 (6)。固定参数化与文献
规范之间的固定同源或整数倍只再排除有限多个素数。

R147 的满像论证也对这个有限域集统一适用：固定非 CM
$E$ 的大 $p$ 像为 $\mathrm{GL}_2(\mathbb Z_p)$；它的唯一
二次行列式子域在 $p$ 分歧，而 $p\nmid D_F$。故限制到
$G_F$ 仍满像。这里不以未证明的负扭曲 Sha 有限性提供
任何原始性输入。

## 3. 完整类群求和后的准确剩余比较

对辅助平方自由 $n$，令
$$
 Y_n^0=\operatorname{Tr}_{F[\ell n]/LF[n]}P[\ell n]
                  \in E(LF[n]).
$$
$L$ 在 $\ell$ 全分歧，而 $F[n]/F$ 在 $\ell$ 不分歧，故
$L\cap F[n]=F$。原 Heegner 范数关系给真正整数点恒等式
$$
                      N_\Gamma Y_n^0=a_\ell P[n].
 \tag{7}
$$

R150 的选定分歧理想基在每个 $F[n]$、$F[\ell n]$ 中
给相容的阶 $h_F$ 补群。先对 $Y_n^0$ 作辅助导数，再按
这些实际类群代表求全部 coset 和；乘 $t_0$ 并经
$\operatorname{Res}_{L/F}E\to A$ 取像。范数、辅助导数、
类群和及差分 $\tau-1$ 都互相交换。尤其在 $n=1$，
对 $Y_1^0$ 的全部 $h_F$ 项求和之后才得到
$\operatorname{Tr}_{F[\ell]/L}P[\ell]$。
没有在整数点上除以 $h_F$，也没有额外乘一个 $h_F$。

使用实际对角同构 $A[\delta]\simeq E[p]$，由 R144 §3.1
的 Kummer 图逐个类群标签相加，得到
$$
 \boxed{\quad
 \overline c_n^A
       =-t_0a_\ell\,\overline c_n^{E,\mathrm{raw}}.
 \quad}
 \tag{8}
$$
为核定反号，给定 $Y\in\operatorname{Res}_{L/F}E$，取
$pV=NY$。差分除点 $Y-\operatorname{diag}V\in A$ 的
Galois 误差在对角核上是
$-\operatorname{diag}(\sigma V-V)$；平衡 $\delta$ 附带的
$\tau$ 幂在对角核上为一。该图对求和与域范数自然，
所以 (7) 给 (8)。全局 $H^0(E[p])=0$ 保证类的下降唯一。

这里 $t_0a_\ell$ 为 $p$ 单位。由 (6)、(8)，实际
$A$ 类族的某个模 $\delta$ 节点非零。类群和并未被当作
一个自动保非零的算子；保非零的输入是 Zhang 已经对
**同一个完整类群原族**给出的 (6)。

首项正是 $(\tau-1)Q$ 的 Kummer 类，在 (3) 的自由格中
指数为 $a+1$。这是原始性与首项指数之间不可删去的一层。

## 4. 局部条件及弱刚性没有新增类群成本

R146 §§2–3 已对这里的完整族证明
$$
                 \operatorname{Sel}_\delta(A/F)
                       \simeq\operatorname{Sel}_p(E/F).
 \tag{9}
$$
其输入均不涉及负扭曲的秩或 Sha：在 $\ell$ 处
$H^i(F_\lambda,E[p])=0$，因为
$(\ell+1)^2-a_\ell^2$ 为 $p$ 单位；在其余好位包括 $p$
处用不分歧范数满射，在 $389$ 处用 Tate 参数估值一。
它们给真实 Kummer 条件及所有所需精度的 Cartesian 比较。

任何不分歧于 $L$、在 $F$ 惰性的辅助有理素数 $q$，在
$\operatorname{Gal}(L/\mathbb Q)$ 中的 Frobenius 为反射，
故 $F$ 上的 $q$ 位自动在 $L/F$ 分裂。又
$L\cap F(E[p^\infty])=F$，可直接由 $\ell$ 处的分歧区别
看出。于是 R144 §4.1 的高精度 Chebotarev 选择仍适用，
可避开全部固定类群代表和模型坏位。

在每个类群标签上，真实有限／奇异比较仍为
$$
 -q\varphi_q^{-1}\otimes1,
 \qquad
 a_q-(q+1)\varphi_q
       =-q\varphi_q^{-1}(\varphi_q^2-1).
 \tag{10}
$$
对全部标签求和和乘 $t_0$ 与 (10) 交换。所以原族满足
R144 §4 已完整证明的弱刚性引理：任意精度 $k$、任意节点
$n$，存在与 $n,k$ 无关的深度 $d\ge0$（或无穷），使
$$
                 \mathcal O c_n^{(k)}
                         =\delta^d\mathcal S_k(n),
 \tag{11}
$$
其中 $\mathcal S_k(n)$ 是真实局部条件给出的循环 stub。
该引理只用全精度局部零性、四角长度公式、core 图连通性
和唯一的高精度下降，并未要求给 $A$ 族另造一个全局修正。
上述逐项核对已支付它在新域上的所有输入。

由 (8) 的实际非零节点，(11) 迫使 $d=0$。在 $n=1$
取任意大 $k$，已知有限的 $S$ 给
$H_k(1)=\mathcal O/\delta^k\oplus M\oplus M$。
首项自由格指数为 $a+1$，而其 stub 深度为
$\operatorname{length}_{\mathcal O}M$。因此两者相等，证明 (4)。

最后，(8) 在每个节点准确保持零性。Zhang（2014）
Lemma 8.4 对原完整族的公式遂直接给 (5)。若要求任意高
辅助精度，在其逐步选择中使用 R144 §4.1 即可；类群和
并不改变剩余正负局部维数。

## 5. 同一无穷联合输入上的结论和剩余目标

R149–R150 的联合筛、R153 的源校准和固定有限域鸽巢给
一个固定 $F_*$，以及无穷多个普通、非异常、在 $F_*$
分裂的 $p$，使其实际 $Q$ 同时满足
$$
 \begin{gathered}
 u\ll p^{333/667},\qquad
 0<\widehat h(Q)\ll p^{666/667}\log p=o(p),\\
 0\le a\le(p-3)/2,\qquad
 \boxed{\ \operatorname{length}_{\mathcal O}\Sha(A/F_*)[p^\infty]
                                      =2(a+1).\ }
 \end{gathered}
 \tag{12}
$$
这里没有重新相交两个未知分布的无穷素数集合；(4) 对
R150、R153 已构造的每个合法输入成立，仅删除固定有限例外。

R146 的原始层配对对两个符号分别给
$$
 a+1\ge
 \max\bigl(s_+-\mathbf1_{\{a\text{ 偶}\}},
           s_--\mathbf1_{\{a\text{ 奇}\}}\bigr).
 \tag{13}
$$
确实，Kummer 像的符号为 $(-1)^a$；从相应 Selmer 符号
维数减去这条线后，奇长块正负成对、偶长块至少长二，
分别得到 $\operatorname{length}S\ge2\dim S[\delta]^\pm$。
结合 (4) 即得 (13)。

准确长度与原始性均未把 $a+1$ 改成 $a$。原目标仍可由
同一个 $Q$ 的 $a\le1$ 解决（R146），而 (12) 尚允许
$a\ge2$。这一步必须来自指定首项或指定 CM 纤维的额外
非零性，不能再由原族某个辅助节点非零替代。

## 来源与依赖

- W. Zhang, *Selmer groups and the indivisibility of Heegner points*,
  Cambridge J. Math. **2** (2014), 191–253；Theorem 1.1、
  Hypothesis $\spadesuit$（印页 194–195），Lemma 8.4
  （印页 236–239）。
  [正式发表全文](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2014/0002/0002/CJM-2014-0002-0002-a002.pdf)。
- B. Howard, *The Heegner point Kolyvagin system*, Compositio Math.
  **140** (2004), 1439–1472；§§1.5–1.7，特别是
  Theorem 1.7.5。
  [正式发表全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF8414258216C1575963BBDA814CB2F/S0010437X04000569a.pdf/the-heegner-point-kolyvagin-system.pdf)。
- [R144 的原族和弱刚性完整证明](2026-11-12-noncm-primitive-induced-system-and-exact-length.md)
  给本篇使用的引理及原符号约定；本篇 §§2–4 逐项验证
  迁移，未直接套用一个只针对反圆分 $p$ 塔角色的定理。
- [R146 的完整类群及通常局部条件](2026-11-12-noncm-two-step-criterion-with-varying-heegner-field.md)
  给 (3)、(9) 和正号两步判据。
- [R150](2026-11-12-sixteen-fixed-fields-and-complete-class-st-jets.md)、
  [R153](2026-11-12-sixteen-unramified-cm-sources-and-square-frobenius.md)
  给固定原对象、统一有限例外及 (12) 的同一输入集合。

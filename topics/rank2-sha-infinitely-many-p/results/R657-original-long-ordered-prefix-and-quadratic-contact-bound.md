# R657 — 原连续长前缀的完整单射、Smith 上界与二次接触界

日期：2026-11-15。**状态：已证明。**

本篇把 R646 的分歧合流证明落实到原普通 Taylor 次数排序的一个**连续前缀**。所需长度准确可取
$$
k_*=1+\max_{0\le u<s,\ C_u>0}\{u+s(C_u-1)\}\le sC_0.
$$
在这个前缀上，原完整来源的评价已经全列单射，并保持 R646 的全部 Smith 指数上界。由此对固定、未去 Gaussian 的原特征零空间 $G_0\mathcal W_D$ 得到
$$
\sup_{0\ne F\in G_0\mathcal W_D}\operatorname{ord}_{w=0}F
\le\left(\frac{99}{40}+o(1)\right)D^2.
$$

这里的连续前缀属于 R646 的同一个完整目标 $\mathcal C_p$。它不等于旧三块 $M$，也不支付任意更短前缀的饱和分类。R644 的五来源辅助空间含额外的原 $z/H$ 方向，不能由本篇自动包含；其 jet 界须另证。

## 1. 原来源、原目标和有序截断

保持
$$
p=6s-1>101,\qquad f_D=\lfloor9D/2\rfloor+4<p.
\tag{1}
$$
原来源及全部十九角条件仍是
$$
\mathcal W_D
=\bigoplus_{n=0}^{D}Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\qquad
h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\left\lfloor\frac{n+1}{4}\right\rfloor,\quad
B_n=\left\lfloor\frac{n+1}{3}\right\rfloor,\quad
C_n=\left\lfloor\frac n2\right\rfloor,
$$
$$
f_n=\lfloor9n/2\rfloor+4,\quad
e_{n+1}=f_n-3A_n-B_n+C_n,\quad b_n=A_n+e_{n+1}.
\tag{2}
$$
原标准列为 $C_{n,k}=Y^nq_n(t)t^k$，$0\le k\le e_{n+1}$；记列数为
$$
N_D=\sum_{n=0}^{D}(e_{n+1}+1).
$$

评价完整保持原 $P_{134}/U_0$、$w^{13}$ 和共同 charge 四十：
$$
\Phi(P)=c_*w^{13}U_0(w)e^{40a\epsilon}
P(t(w),g(w)e^{a\epsilon}).
\tag{3}
$$
其中 $a,c_*,U_0(0)$、$t'(0)$ 都是原单位。目标为
$$
\mathcal C_p=
\mathcal O[w,\epsilon,\Upsilon]/
(w^s-p\epsilon,\epsilon^6-w\Upsilon,
 w^{s-1}\epsilon^5-p\Upsilon,\Upsilon^s).
\tag{4}
$$
R607/R646 的同一个原整基按普通 $w$ 次数排序后是
$$
\gamma_m=p^{-\lfloor6m/p\rfloor}w^m,
\qquad0\le m<ps.
\tag{5}
$$
它只是原标准单项式基的重排，不是额外允许除以 $p$。

对于 $1\le k\le ps$，令 $M_{<k}$ 为 (3) 的原整矩阵只保留
$$
\gamma_0,\gamma_1,\ldots,\gamma_{k-1}
\tag{6}
$$
这些行。等价地，目标是按普通次数 $\ge k$ 的原格直和因子取商。该截断有理化后恰为普通 Taylor 截断模 $w^k$。所以 (6) 是连续有序前缀，包含其中全部低行及原零行；不是把一个非连续子式重新编号。

## 2. 实际合流列及所需行号

对原列定义
$$
r_{n,k}=13+A_n+k.
$$
取辅助完全分歧扩张 $\pi^s=p$，并令 $w=\pi z$。R646 的全高尾证明给
$$
\widetilde F_{n,k}(z)=
\pi^{-r_{n,k}}\Phi(C_{n,k})(\pi z)
\in\mathcal O'[z]/z^{ps},
$$
$$
\overline{\widetilde F}_{n,k}
=\lambda_{n,k}z^{r_{n,k}}
e^{\bar a(n+40)z^s},\qquad\lambda_{n,k}\in k^\times.
\tag{7}
$$
这里 $g,t/w,U_0$ 和原 $q_n$ 的所有高尾仍在第一行。具体由 R618，
$$
v_p(h_l)\ge-\lfloor6l\tau_2\rfloor,\qquad
\tau_2=\frac{2p-1}{p(p^2-1)},
$$
从而
$$
v_\pi(\pi^lh_l)\ge l-s\lfloor6l\tau_2\rfloor>0
\quad(l\ge1).
\tag{8}
$$
故它们只在 (7) 的模 $\pi$ 约化中消失。第一 Gaussian 则准确化为 $e^{az^s}$；次数 $<ps$ 只使用阶乘 $0!,\ldots,(p-1)!$，没有使用不整的指数高项。

写 $r_{n,k}=u+js$，$0\le u<s$。在固定余类 $u$，实际列就是
$$
X^j e^{\bar a(n+40)X},\qquad X=z^s,
\quad13+A_n\le u+js\le13+b_n.
\tag{9}
$$
定义
$$
J_n(u)=\left\lfloor\frac{b_n+13-u}{s}\right\rfloor,
\qquad
C_u=\sum_{n=0}^{D}(J_n(u)+1)_+.
\tag{10}
$$
R646 已证明整个 (1) 范围内
$$
C_u\le C_0\le p.
\tag{11}
$$
在固定 $u$，仅为证明独立性，把同节点的缺失低 $j$ 补到
$j=0,\ldots,J_n(u)$。这个完整合流族用
$$
[X^0],\ldots,[X^{C_u-1}]
\tag{12}
$$
便有单位行列式：不同节点的差为 $\bar a(n'-n)\ne0$，且所需阶乘次数小于 $p$。原列是补齐族的子族，因此已经在 (12) 上独立。

补齐列只用于这次独立性证明，始终没有加入 $\mathcal W_D$，也没有修改任何原角帽。高尾的处理在 (8)，不是假设各普通余类在特征零中互相独立。

## 3. 连续前缀定理与同一 Smith 上界

定义
$$
\boxed{
k_*=1+\max_{\substack{0\le u<s\\ C_u>0}}
\{u+s(C_u-1)\}.}
\tag{13}
$$
因 $u\le s-1$，有
$$
1+s(C_0-1)\le k_*\le sC_0\le sp.
\tag{14}
$$

**定理 1。** 对所有满足 (1) 的原参数，以及所有
$k_*\le k\le ps$，原有序矩阵 $M_{<k}$ 全列单射。其 $N_D$ 个 Smith 因子全部非零，若一个因子为 $p^e$，则
$$
\boxed{
e\le B_D:=\left\lceil\frac{b_D+13}{s}\right\rceil.}
\tag{15}
$$
其余核自由秩为 $k-N_D$；torsion 被 $p^{B_D}$ 杀掉。特别 $B_D\le7$，且 $p\ge137$ 时 $B_D\le6$，与 R646 同界。

**证明。** (12) 对应的普通 $z$ 行恰为
$$
m=u+hs,\qquad0\le h<C_u.
$$
全部这些行都小于 $k_*$。因此把 (7) 限制到连续前缀 $m<k$ 后，约化矩阵仍全列独立；它有一个单位列满秩子式及整左逆。

为把这个事实送回**原**格，按 (5) 定义
$$
\omega_m=m-s\lfloor6m/p\rfloor.
$$
R646 的准确行权界在每个 $m<ps$ 都成立：
$$
1-s\le\omega_m\le s-1.
\tag{16}
$$
前缀归一矩阵正是
$$
\mathsf A_{<k}
=\operatorname{diag}_{m<k}(\pi^{\omega_m})
 M_{<k}
 \operatorname{diag}_{n,k}(\pi^{-r_{n,k}}).
\tag{17}
$$
它有整左逆 $\mathsf L_{<k}$。注意 (17) 不是原格上的整等价；负权和来源的 $\pi^{-r_{n,k}}$ 都只用于辅助证明。

若 $P$ 是对应某个 Smith 指数 $e$ 的原 primitive 向量，则
$M_{<k}P\in p^e\mathcal O^k$。由左逆，
$$
\operatorname{diag}(\pi^{r_{n,k}})P
=\mathsf L_{<k}\operatorname{diag}(\pi^{\omega_m})M_{<k}P
\in\pi^{se+1-s}\mathcal O'^{N_D}.
$$
$P$ 有一个单位坐标，而每个 $r_{n,k}\le b_D+13$，故
$$
se+1-s\le b_D+13.
$$
取整得到
$$
e\le\left\lfloor\frac{b_D+13+s-1}{s}\right\rfloor
=\left\lceil\frac{b_D+13}{s}\right\rceil.
$$
非零因子和自由秩由全列单射立即得到。统一数值界沿用 R646 已付的十二余类帽估计。证毕。

这里“同界”指 (15)，不声称 $M_{<k}$ 与完整 $M_{\mathcal C}$ 的各个 Smith 指数逐个相同，也不声称 (13) 是最短的满列秩前缀。

## 4. 固定特征零空间与一个辅助惰性素数

令 $\mathfrak F_D$ 为原**未正规化**的固定特征零空间
$$
\mathfrak F_D=G_0\mathcal W_D
=\{G_0(w)P(t(w),\mathscr R(w)):P\in\mathcal W_D\otimes\mathbf Q\},
\tag{18}
$$
并允许把标量扩张到任意特征零域。这里 $G_0$、$\mathscr R$ 是原来源，而不是另选的 $p$ 依赖规范。对任一好惰性 $p$，(3) 正是 (18) 的准确 Gaussian 分解：
$$
\mathscr R=g\,e^{a w^s/p},\qquad
G_0=c_*w^{13}U_0e^{40a w^s/p}.
\tag{19}
$$
因此改变辅助素数只改变 (19) 的分解，不改变 (18) 的特征零系数矩阵。原 $w^{13}$ 与 $G_0$ 全部保持。

对任一个满足 (1) 的辅助素数，定理 1 说明 (18) 的普通系数矩阵在行 $0,\ldots,k_*-1$ 已全列秩。确实 (5) 只把普通系数行乘一个非零有理数，而 (17) 的分歧域仍是域扩张。因此某个原有理系数子式非零。域扩张不改变这个秩，得到
$$
\boxed{
0\ne F\in\mathfrak F_D
\quad\Longrightarrow\quad
\operatorname{ord}_{w=0}F<k_*.
}
\tag{20}
$$
无需要求 $F$ 的来源坐标在该辅助素数处 primitive，也无需把每个 $F$ 分别选一个素数：同一个 $p$ 和同一个有限矩阵已经证明整个固定空间的 (20)。

## 5. 明确的二次主常数

选 $p_D$ 为大于 $\max(101,f_D)$ 的最小素数
$p_D\equiv5\pmod6$。固定模数的算术级数素数定理给
$$
p_D=\left(\frac92+o(1)\right)D,\qquad
s_D=\frac{p_D+1}{6}
=\left(\frac34+o(1)\right)D.
\tag{21}
$$
这里只用固定模数六，没有令模数随 $D$ 增长。

为了把所用外部输入的量词写清，素数定理是
$$
\pi(x;6,5)\sim\frac{x}{2\log x}.
$$
因此对任意固定 $\varepsilon>0$，当 $x$ 充分大时区间
$(x,(1+\varepsilon)x]$ 中有素数 $5\bmod6$。令 $x=f_D$，
再让固定 $\varepsilon$ 任意小，即得 (21)。该定理的原作者讲义来源可见 K. S. Kedlaya，*Notes on analytic number theory*，§4.4，Theorem 4.12：
[Primes in arithmetic progressions](https://kskedlaya.org/ant/chap-primes-in-ap.html)。
本篇只使用该定理及上面的直接推论，不使用未说明的短区间定量界。

原十二余类公式给一致估计
$$
b_n=\frac{25}{6}n+O(1).
\tag{22}
$$
将 (10) 在 $u=0$ 改写为真实整数计数：
$$
C_0=\sum_{j\ge0}
\#\{0\le n\le D:b_n+13\ge j s_D\}.
\tag{23}
$$
由 (21)–(22)，当 $D$ 充分大时仅有 $j=0,\ldots,5$。
对每个这样的固定 $j$，
$$
\frac1D\#\{0\le n\le D:b_n+13\ge j s_D\}
\longrightarrow1-\frac{9j}{50}.
$$
边界的固定整数误差只有 $O(1)$，而 (21) 的 $o(D)$ 只产生 $o(D)$ 计数误差。故
$$
\boxed{
\frac{C_0}{D}\longrightarrow
\sum_{j=0}^{5}\left(1-\frac{9j}{50}\right)
=\frac{33}{10}.
}
\tag{24}
$$
由 (14)，$k_*=s_DC_0+O(s_D)$，所以
$$
\boxed{
k_*=\left(\frac{99}{40}+o(1)\right)D^2.
}
\tag{25}
$$
结合 (20) 得：

**定理 2。** 固定原未正规空间 $G_0\mathcal W_D$ 的最大原点接触满足
$$
\boxed{
J_D^{\rm old}:=
\sup_{0\ne F\in G_0\mathcal W_D}
\operatorname{ord}_{w=0}F
\le\left(\frac{99}{40}+o(1)\right)D^2.
}
\tag{26}
$$
一个不含渐近符号的可计算上界是：取上述具体 $p_D$，按 (10)、(13) 求 $k_*(D,p_D)$，则 $J_D^{\rm old}\le k_*-1$。

## 6. 已付范围与仍须支付的原接口

(13)–(17) 是完整原格中一个真实**长**连续前缀的结论。它不把 R648 的列权旗标换成所有长度的普通 Taylor 旗标。若 $k<k_*$，截取后在固定普通余类的行数可能不足以容纳整个合流族；原 $q_n/g/U_0$ 的高尾于是可能决定新的 Padé 子式，不能由本篇删掉。

同样，(26) 只证明固定特征零空间的接触上界。辅助素数处的单位子式不控制该有理子式在其他素数处的分子估值。因此它没有给“所有 $p>C D^\theta$”的无例外整性 cutoff，也没有直接改善全局真饱和 jet 的 $p$ 进主成本。

旧 $M$ 仍只读取原两长块、一短块和两组十三行。其指定 $P+pR+p^2T$ 的同一个 $R$、完整第二 forcing 和实际像均须在旧截止内处理。本篇不由长前缀单射认定旧 $d_2$ 非零，也不增加任何原算术中央条件。

R644 的辅助空间使用 $u^{66D}x^a y^b h^m$，包含本篇未覆盖的 $z/H$ 方向；不能把 (26) 的系数或长度直接套到那一空间。该辅助空间的真实 Gaussian 块若另行付清，可独立给它的 jet 界。

## 依赖

- [R646](R646-original-full-target-ramified-confluent-block-and-smith-bound.md)：原完整目标、全部高尾、合流补齐与行权界。
- [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：原第二盘 regular 系数估值。
- [R620](R620-full-original-weighted-hilbert-function-and-thirteen-row-smith-window.md)：真实来源、全部角帽及完整目标整性。
- [R648](R648-original-weight-flag-and-complete-smith-classification.md)：列权旗标的范围；本篇的连续长前缀是其外另付的结论。
- K. S. Kedlaya，*Notes on analytic number theory*，§4.4，Theorem 4.12，[作者正文](https://kskedlaya.org/ant/chap-primes-in-ap.html)：固定算术级数的素数定理。

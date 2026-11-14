# R224A：快参数加强与 Bell 对快分式域超越

日期：2026-11-12（UTC）。作者：kernel；有限头延拓由 boundary 完整构造。状态：以下命题已证明。

这是 [准确第二因子及单 Bell 公共像障碍](R224-exact-gauge-second-factors-and-common-image-obstruction.md) 的加强。规范系数仍为

$$
a_*=0,\quad a_j=(-1)^j(j+1)^{-\sigma},\quad 1/2<\sigma\le1,
\qquad B=\sum_j a_j^2(I-V_j^2).
$$

本稿把可排除的全空间公共像从 $\mathbb C\{A,B\}$ 的有界解析分式扩大到整个 $\mathbb K(B)$、$\mathbb K=\operatorname{Frac}\mathcal G$，以及有限个快参数与 $B$ 的全纯演算。一般快元素的边界核不必有限；证明使用整个新边界核上的表示忠实性，不把未知单向量强行移出其核。

## 1. 新边界核有有控的全部有限头延拓

记 $\pi$ 为负整数边界表示，$A_-=\pi A$。对任意真解析 $r$ 且 $r(0)=0$，置

$$
M_r=\ker\pi(B-r(A)),\qquad D_r=A_-|_{M_r}.
$$

[boundary 的 Bell 核完整稿 §8A](R223-bell-minus-arbitrary-analytic-germ-boundary-kernels.md) 给：对每个 $m\ge1$，有线性算子

$$
J_m:\mathcal F_m\longrightarrow M_r,
\quad P_mJ_m=I_{\mathcal F_m},
\quad \|J_m\|\le C_r\exp(K_r m2^m).
\tag{1.1}
$$

$C_r,K_r$ 可以依固定解析头 $r$，但不依 $m$。该输入由真实空白间隔误差及有限维右逆得到：初次不要求 $Sv$ 小的有限模型纠错，归一化后已经进入下一真实头尺度的小残量预算；归一化只用于估计，实际每一步线性，因此得到 (1.1)。

给定整数 $n\ge1$，取 $m=\lceil\log_2(n+1)\rceil$，令 $g_n=J_me_n$。由 $\langle g_n,e_n\rangle=1$ 及边界权移位恒等式

$$
(A_-^*)^ne_0=W_ne_n,
$$

得到

$$
\frac{W_n}{C_r e^{K_r m2^m}}
\le\|D_r^n\|\le W_n.
\tag{1.2}
$$

因为 $m2^m=O(n\log(n+1))$，对每个固定整数 $q\ge1$，实际二进位权公式给

$$
\boxed{\tau_4(D_r^q)=\frac{100}{15}q^4.}
\tag{1.3}
$$

每个 $\pi E$、$E\in\mathcal A$，保持 $M_r$，因为它与 $\pi(B-r(A))$ 交换。故在 $M_r$ 上得到真正收缩代数表示。
若 $f(z)=z^q u(z)$ 为非零真解析芽、$u(0)\ne0$，则 $u(A)$ 与其逆在该表示中仍为互逆单位，(1.3) 蕴含

$$
\tau_4(f(D_r))=\frac{100}{15}q^4.
\tag{1.4}
$$

$q=0$ 时为单位，型为零。

## 2. 全部非零快元素在 M_r 上不消失

**命题 2.1。** 对每个 $0\ne G\in\mathcal G$，有

$$
\boxed{\pi(G)|_{M_r}\ne0.}
\tag{2.1}
$$

**证明。** 令 $q=\operatorname{ord}\iota(G)$。$q=0$ 时 $G$ 是单位，结论直接成立。
若 $q\ge1$，R151 给真正解析逼近

$$
G=f_k(A)+E_k,
\quad\|E_k\|\to0,
\quad\tau_4(E_k)\to\infty,
$$

并由精确有限 jet 稳定，可使每个充分大的 $f_k$ 首阶恰为 $q$。若 $\pi(G)|_{M_r}=0$，则

$$
f_k(D_r)=-\pi(E_k)|_{M_r}.
$$

左边由 (1.4) 型恰为 $100q^4/15$；右边因表示收缩，型至少 $\tau_4(E_k)$，对大 $k$ 严格更大，矛盾。证毕。

这只是“不消失”的表示忠实性。它没有声称每个快算子在 $M_r$ 上单射，或在这个边界限制上像稠密；$A_-$ 自己便有真空核。

## 3. 任意有界交换商迫快系数多项式在 r 上为零

取 $P(w)=\sum_{k=0}^d G_kw^k\in\mathcal G[w]$，并假定有 $C\in\{A\}'$ 有界使

$$
P(B)=(B-r(A))C.
\tag{3.1}
$$

因 $C$ 与 $B-r(A)$ 交换，

$$
P(B)^*P(B)\le\|C\|^2(B-r(A))^*(B-r(A)).
$$

不等式两端都属于 UHF，故由忠实 Haar 表示传到负整数边界。这说明 $\pi(P(B))$ 杀掉**整个** $M_r$。在该核上 $\pi B=r(D_r)$，因此

$$
\pi(P(r(A)))|_{M_r}=0.
$$

由于 $P(r(A))\in\mathcal G$，(2.1) 迫

$$
\boxed{P(r(A))=0\quad\text{于实际快代数中}.}
\tag{3.2}
$$

这里不能只选 (1.1) 中某一个边界向量；一般 $G$ 可能有较大的边界核。正序给整个 $M_r$ 被杀，才允许使用命题 2.1。

同一结论对 $P(B)\in\overline{(B-r(A))\mathcal A}$ 成立：连续边界表示先杀整个 $M_r$，后续相同。

### 3.1 Bell 对快分式域超越

若某个 $P\in\mathcal G[w]$ 满足 $P(B)=0$，则对任意 $r(z)=cz$（$c\in\mathbb C$），在 $M_r$ 上代入同样得 $P(cA)=0$。$\mathbb K=\operatorname{Frac}\mathcal G$ 是域，其中 $cA$ 随 $c$ 取无限多个不同值。因此有限次数域多项式 $P$ 必为零。

清有限个快分母后得到

$$
\boxed{B\text{ 超越于 }\mathbb K.}
\tag{3.3}
$$

所以 $\mathcal G[B]$ 的求值忠实，R152 的快系数多项式定理使其每个实际非零成员在原 $H$ 上单射稠密。R152 的闭分式附录因此准确实现 $\mathbb K(B)$。这里仍不声称这些慢多项式在任意 Haar 限制上像稠密。

## 4. 整个 K(B) 中没有非零全空间公共像

使用主稿的解析芽 $r_\zeta$。其有限 jet 已证明：有无限多个不同 $r_\zeta(A)\in\mathcal G\subset\mathbb K$。

假设有一个有界 $R\in\{A\}'$，可由 $\mathbb K(B)$ 的分式表示。清有限个快系数分母后，准确有界图方程可写成

$$
Q(B)R=P(B),\qquad P,Q\in\mathcal G[w],\quad Q\ne0.
\tag{4.1}
$$

由 (3.3) 及 R152，$Q(B)$ 单射。
再假设

$$
\operatorname{Ran}R\subseteq\operatorname{Ran}S_\zeta,
\qquad S_\zeta=B-r_\zeta(A)
\tag{4.2}
$$

对全部相关 $\zeta$ 成立。$S_\zeta$ 是单射有界算子，所以最大闭商 $C_\zeta=S_\zeta^{-1}R$ 全域定义且有界；取消 $S_\zeta$ 验证 $C_\zeta\in\{A\}'$。由 (4.1)，

$$
P(B)=S_\zeta[Q(B)C_\zeta].
$$

§3 迫 $P(r_\zeta(A))=0$。有限次数 $P$ 在域 $\mathbb K$ 中有无限多个不同根，因此 $P=0$；最后由 $Q(B)$ 单射，$R=0$。即

$$
\boxed{
\mathbb K(B)\text{ 的有界实现中不存在满足 (4.2) 的非零元素。}
}
\tag{4.3}
$$

相同证明对每个 $\zeta$ 的范数闭主理想条件成立：如果 $R\in\bigcap_\zeta\overline{S_\zeta\mathcal A}$，则其分子 $P(B)=Q(B)R$ 也在每个闭理想中，由 §3 再得 $R=0$。

## 5. 任意有限快参数全纯演算的加强

令

$$
\mathscr H_{\mathcal G,B}
=\{F(G_1,\ldots,G_d,B):G_i\in\mathcal G,
\ F\text{ 在联合字符点附近全纯},\ d<\infty\}.
$$

R151 的有限变量全纯封闭附录保证：对每个真解析零常数 $r$，

$$
F(G_1,\ldots,G_d,r(A))\in\mathcal G.
\tag{5.1}
$$

因此 §3 的全核正序论证仍成立：若实际

$$
R=F(G_1,\ldots,G_d,B)=S_\zeta C_\zeta,
$$

则

$$
F(G_1,\ldots,G_d,r_\zeta(A))=0.
\tag{5.2}
$$

这里 $F$ 不必在慢变量方向正规，也不先假定 $R$ 单射。

下面证明 (5.2) 已迫 $R=0$，使用明确有限 jet 而不用未经证明的快系数 Weierstrass 准备。
先把 $G_i$ 的字符平移到零。令

$$
g_i(z)=\iota(G_i)(z),\qquad
\widehat F(z,w)=F(g_1(z),\ldots,g_d(z),w)
\in\mathbb C[[z,w]].
$$

形式代入合法，因为所有参数的常数项为零。
主稿 §5 给一个正整数 $k$、一个固定零常数多项式 $p(z)$（次数小于 $k$），以及取无限多个不同复值的 $c_\zeta$，使

$$
r_\zeta(z)=p(z)+c_\zeta z^k+O(z^{k+1}).
\tag{5.3}
$$

具体地，若前两个非零系数为 $a,b$、$b\ne a$，则 $k=(2^{j_1-j_0}-1)h$，变化系数是一个非零常数乘 $H_{2^{j_1-j_0}}(\zeta^h)$ 加固定常数。

如果 $\widehat F\ne0$，作合法替换

$$
\widehat F(z,p(z)+z^k v)=\sum_{N\ge0}z^N P_N(v),
\qquad P_N\in\mathbb C[v].
\tag{5.4}
$$

每个 $z^N$ 系数只涉及有限多个原单项式，故确为有限多项式。此替换单射：先用 $w\mapsto p(z)+w$ 的形式自同构，再用 $w\mapsto z^kv$，后者不会使一个非零的 $w^m$ 系数变零。
取最小的 $N_0$ 使 $P_{N_0}\ne0$。由 (5.2)、(5.3) 的形式像，代入 $v=c_\zeta+O(z)$ 后的最低系数为

$$
P_{N_0}(c_\zeta)=0
\quad\text{对全部相关 }\zeta.
$$

非零有限多项式不能在无限多个不同复数处为零，矛盾。因此 $\widehat F=0$。最后

$$
\iota(R)=\widehat F(z,\iota(B)(z))=0,
$$

由 $\mathcal A$ 的形式忠实性得 $R=0$。

综上，任意 $R\in\mathscr H_{\mathcal G,B}$ 若满足 (4.2)，必为零；同样排除它属于全部 $\overline{S_\zeta\mathcal A}$。

### 5.1 有真实单射分母的全纯商

更一般，设有界 $R\in\{A\}'$ 满足

$$
Q R=P,\qquad P,Q\in\mathscr H_{\mathcal G,B},
\quad Q\text{ 在全 }H\text{ 单射}.
$$

若 (4.2) 成立，则 $P=S_\zeta(QC_\zeta)$，上一证明使 $P=0$，从而 $R=0$。
这里特意保留 $Q$ 的实际单射假设；一般非正规快参数混合芽的全空间单射性不是本稿的结论。对 §4 的 $\mathbb K(B)$ 分母，该假设已经由 R152 付清。

## 6. 边界

本稿只处理全空间 range inclusion 或 UHF 范数闭主理想。若只知

$$
RM\subseteq S_\zeta M
$$

于原危险 Haar 核 $M$ 上成立，尚不能把相应正序送到负整数边界；本稿没有排这种 $M$ 特有的公共像。
也没有排除 $\mathscr H_{\mathcal G,B}$ 及上述有实际单射分母的商之外的有界交换子。

输入：boundary 的完整 Bell 核稿及 §8A；R32 的忠实形式系数；R151 与其有限变量全纯封闭附录；R152 的快系数多项式与闭分式；R195 的指定模块型比较方法；主稿 §5 的准确 gauge 有限 jet。

# R195：具体慢边界模块的精确四次型与非标准理想对快分式的分离

日期：2026-11-12（UTC）。作者：l2_moments。根代理预留 R195。

状态：完整证明。只研究 R185、R188 构造出的两个具体慢核、它们的固定稠密像部分及指定的一维商。它们保留全部非零 $\mathcal G$ 符号的精确四次型，但本稿不把这一结论外推到任意边界不变子商，也不从型的非消失推出所有未知核或闭像的消失。

## 1. 两个具体理想与边界模块

取
$$
a_j=(j+1)^{-2},\qquad
S_N=\sum_{j\ge0}a_jN_j,\qquad
S_Y=\sum_{j\ge0}a_jN_j(I+N_j)^{-1}.
$$
以下分别对 $S=S_N$、$S=S_Y$ 使用相同记号：
$$
J=\overline{S\mathcal A}^{\|\cdot\|},\qquad
\mathcal Q=\mathcal A/J,\qquad q:\mathcal A\to\mathcal Q.
\tag{1.1}
$$
设 $\pi_-$ 是 R174 的负整数边界表示，
$$
B=\pi_-(A),\qquad
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1}.
$$
置
$$
T=\pi_-(S),\qquad
M=\ker T,\qquad N=\overline{BM}.
\tag{1.2}
$$

R185、R188、R187 及其附录给：

1. $M,N$ 都无限维，且
   $$
   M\cap\ker B^k=\mathbb C e_0\quad(k\ge1).
   $$
2. $e_0\in N$，$\overline{B^kM}=N$ 对每个 $k\ge1$，
   且 $\overline{BN}=N$。
3. 在
   $$
   \mathscr K=N/\mathbb C e_0
   $$
   上诱导的算子 $C$ 单射、稠密像、拟幂零。
4. 对
   $$
   \mathscr F_m=\operatorname{span}\{e_n:0\le n<2^m\},
   $$
   存在一次固定的有界线性延拓
   $$
   J_m:\mathscr F_m\to M,\qquad P_mJ_m=I,
   \qquad
   \|J_m\|\le2e^{8m2^m}\quad(m\ge2).
   \tag{1.3}
   $$
   两种慢算子共用同一纯块右逆。Cayley 情形只把有限头范数上界取为6、
   实际空 gap 误差取为 $26\eta$，这些常数已经包含在 (1.3) 中。

记
$$
c_*=\frac{100}{15},\qquad
\tau_4(R)=\liminf_{n\to\infty}
 \frac{-\log\|R^n\|}{n^4},
$$
并约定零算子的型为 $+\infty$。

本稿证明：

- 三个指定表示 $B_M=B|_M$、$B_N=B|_N$、$C$ 都满足
  $$
  \tau_4(D^r)=c_*r^4\quad(r\ge0).
  $$
- 对每个 $0\ne g\in\mathcal G$，令 $r=\operatorname{ord}\iota(g)$，
  则它在上述三个表示及 Banach 商 $\mathcal Q$ 中的实际像均不为零，
  且精确型都等于 $c_*r^4$。
- 因而
  $$
  \boxed{J\cap\mathcal G=\{0\}.}
  \tag{1.4}
  $$
  更强，$J$ 不含任何非零、全域有界的 $\operatorname{Frac}\mathcal G$
  实际实现。
- 对较小的 R179 快尾子代数 $\mathcal T$，标准范数闭主理想另外给出准确核与闭像；
  对一般 $\mathcal G$ 不越过这一额外缺口。

## 2. 有限头延拓给每个幂的实际范数下界

边界的实际权积满足
$$
(B^*)^ne_0=W_ne_n,
$$
所以对任意 $x$，
$$
\langle B^nx,e_0\rangle=W_n\langle x,e_n\rangle.
\tag{2.1}
$$

给定 $n\ge1$，取
$$
m=m(n)=\max\left(2,\left\lceil\log_2(n+1)\right\rceil\right).
$$
则 $e_n\in\mathscr F_m$。
由 (1.3)，向量
$$
g_n=J_me_n\in M
$$
在第 $n$ 个坐标等于1，而
$\|g_n\|\le2e^{8m2^m}$。
(2.1) 精确给
$$
|\langle B^ng_n,e_0\rangle|=W_n.
$$
于是
$$
\boxed{
\frac{W_n}{2e^{8m(n)2^{m(n)}}}
\le\|B_M^n\|\le W_n.
}
\tag{2.2}
$$
上界是实际不变限制的范数界。

因为 $m(n)2^{m(n)}=O(n\log(n+1))$，
(2.2) 给
$$
-\log\|B_M^n\|
=-\log W_n+O(n\log(n+1)).
\tag{2.3}
$$
这里每个 $n$ 都有一个明确核内测试向量；
没有把整个边界的坐标向量未经修改放进 $M$。

对固定 $r\ge1$，将 $n$ 换成 $rn$。
实际二进制权公式给
$$
\liminf_{n\to\infty}\frac{-\log W_{rn}}{n^4}=c_*r^4.
\tag{2.4}
$$
该常数可由
$-\log W_k=100D_4(k)+O(k^3+k\log(k+1))$、
$k^4\le15D_4(k)$，
以及
$rn_j=2^j-t_j$、$1\le t_j\le r$
的补位子列得到；见 R191 §2 的直接核对。
所以
$$
\boxed{\tau_4(B_M^r)=c_*r^4.}
\tag{2.5}
$$
$r=0$ 为恒等算子，型为0。

## 3. 固定稠密像部分与一维商保留精确型

这一步只用真实范数夹逼，不调用未知限制的同型定理。

### 3.1 从 M 到 N

因 $B_M^rM\subseteq N$，对每个固定 $r\ge1$，
$$
\|B_M^{r(n+1)}\|
\le\|B_N^{rn}\|\,\|B_M^r\|,
\qquad
\|B_N^{rn}\|\le\|B_M^{rn}\|.
\tag{3.1}
$$
固定算子的一个有限幂移位不改变四次 liminf：
$$
\liminf_n\frac{-\log\|R^{n+1}\|}{n^4}
=\tau_4(R).
$$
分母从 $n^4$ 换成 $(n+1)^4$ 只差趋于1的比例。
用 (3.1) 和 (2.5)，得到
$$
\boxed{\tau_4(B_N^r)=c_*r^4.}
\tag{3.2}
$$

### 3.2 从 N 到 K

令 $\rho:N\to\mathscr K=N/\mathbb C e_0$ 为 Hilbert 商映射。
对固定 $r\ge1$，$B_N^r$ 杀掉 $\mathbb C e_0$，
所以有真正有界因子
$$
V_r:\mathscr K\to N,\qquad
V_r(x+\mathbb C e_0)=B_N^rx,\qquad
\|V_r\|\le\|B_N^r\|.
$$
商与幂的交织给
$$
B_N^{r(n+1)}=V_r C^{rn}\rho.
$$
同时商范数给 $\|C^{rn}\|\le\|B_N^{rn}\|$。
故
$$
\|B_N^{r(n+1)}\|
\le\|B_N^r\|\,\|C^{rn}\|,
\qquad
\|C^{rn}\|\le\|B_N^{rn}\|.
\tag{3.3}
$$
再次取型，得到
$$
\boxed{\tau_4(C^r)=c_*r^4.}
\tag{3.4}
$$

这两个夹逼只适用于已指定的 $N$ 与 $\mathscr K$。
没有证明任意更小不变子空间或任意后续商都保留精确型。

## 4. 真解析头在三个表示上的精确型

统一用 $D$ 表示 $B_M$、$B_N$、$C$ 之一。
每个 $\pi_-(\mathcal A)$ 元素保持 $M$、$N$ 和 $\mathbb C e_0$，
所以这些空间都承载真正连续的 $\mathcal A$ 表示。

取非零解析芽
$$
F(z)=z^rU(z),\qquad U(0)\ne0.
$$
$U(A)$ 及其逆属于 $\mathcal A$。
其在上述表示中的像仍相互为逆，并与 $D$ 交换。
于是
$$
F(D)=D^rU(D).
$$
对每个固定幂 $n$，
乘 $U(D)^n$ 及其逆最多增加 $O(n)$ 的对数范数。
由 §3，
$$
\boxed{\tau_4(F(D))=c_*r^4.}
\tag{4.1}
$$
$r=0$ 时这是一个有界单位，型为0。

该论证使用的单位是每个固定解析头自己的实际有界单位，
不要求不同逼近头的逆范数一致。

## 5. 全部非零 G 符号都保留精确型

取 $0\ne g\in\mathcal G$，记
$$
r=\operatorname{ord}\iota(g).
$$
用 R151 的定义与精确 jet 稳定选真正解析逼近
$$
g=F_\ell(A)+E_\ell,\qquad
\|E_\ell\|\to0,\qquad
\tau_4(E_\ell)\to+\infty,
$$
使充分大 $\ell$ 时
$$
F_\ell(z)=z^rU_\ell(z),\qquad U_\ell(0)\ne0.
\tag{5.1}
$$

在上述任一表示中记实际像为 $g_D$、$(E_\ell)_D$。
表示收缩，故
$$
\tau_4((E_\ell)_D)\ge\tau_4(E_\ell)\longrightarrow+\infty.
\tag{5.2}
$$
各项有界且交换。
使用交换和的四次谐和下界
$$
\tau_4(P+Q)\ge
\left(\tau_4(P)^{-1/3}+\tau_4(Q)^{-1/3}\right)^{-3}
\tag{5.3}
$$
时，可先取严格较小的正下界，再取极限；
无穷型按逆三次方根为零理解。

先设 $r\ge1$，令 $a=c_*r^4>0$。
由
$$
g_D=F_\ell(D)+(E_\ell)_D
$$
和 (4.1)—(5.3)，令 $\ell\to\infty$ 得
$\tau_4(g_D)\ge a$。

反过来，
$$
F_\ell(D)=g_D-(E_\ell)_D.
$$
若 $\tau_4(g_D)>a$，包括假设它为零算子的无穷型情形，
可取一个固定有限 $\beta>a$ 且 $\beta<\tau_4(g_D)$。
令 $\ell$ 足够大，使
$$
\left(\beta^{-1/3}
+\tau_4((E_\ell)_D)^{-1/3}\right)^{-3}>a.
$$
(5.3) 将迫使 $\tau_4(F_\ell(D))>a$，
与 (4.1) 矛盾。
所以
$$
\boxed{\tau_4(g_D)=c_*r^4\quad(r\ge1).}
\tag{5.4}
$$

若 $r=0$，$g$ 的字符非零，故 $g$ 是 $\mathcal A$ 中的单位。
其在三个表示中的像也为单位，型直接为0。

综上，
$$
\boxed{
0\ne g\in\mathcal G
\ \Longrightarrow\
g_D\ne0,\qquad
\tau_4(g_D)=c_*\,\operatorname{ord}\iota(g)^4.
}
\tag{5.5}
$$
这同时处理 $S_N$ 与 $S_Y$ 构造出的全部六个指定边界空间。

## 6. 非标准理想与整个快代数的交为零

$J$ 在 $M$ 上的边界作用为零：
若 $F=S H\in S\mathcal A$，则
$$
\pi_-(F)x=\pi_-(H)Tx=0\qquad(x\in M),
$$
再用范数闭包即可。

如果 $0\ne g\in J\cap\mathcal G$，
它在 $M$ 上的像为零，
与 (5.5) 的有限精确型矛盾。
因此
$$
\boxed{
J_N\cap\mathcal G=J_Y\cap\mathcal G=\{0\}.
}
\tag{6.1}
$$
这里 $J_N,J_Y$ 分别表示两个闭主理想。
这严格加强了先前只对较小 $\mathcal T$ 类的零交结论。

更强，设某个非零 $Z\in J$ 同时是快分式 $a/b$ 的全域有界实际实现，
其中 $a,b\in\mathcal G$、$b\ne0$。
最大分式定义给真实有界恒等式
$$
bZ=a.
$$
因为 $J$ 是 $\mathcal A$ 理想，$bZ\in J$。
又非零 $b$ 单射，$Z\ne0$ 保证 $a\ne0$。
于是 $0\ne a\in J\cap\mathcal G$，矛盾。

所以
$$
\boxed{
J\text{ 不含任何非零的有界快分式实现。}
}
\tag{6.2}
$$
其中 $Z\in J$ 本身保证 $Z\in\mathcal A$；
没有把任意有界快分式先假设属于 $\mathcal A$。

特别两个生成元 $S_N,S_Y$ 都不属于快分式域的有界实现。
更一般，若 $q$ 为非恒定解析芽，则
$$
q(S)-q(0)I=S^kU\in J\setminus\{0\}
$$
对某个 $k\ge1$ 和实际解析单位 $U$ 成立，
所以 $q(S)$ 也不属于快分式域。
这是 R191 非成员结论的另一条实际闭理想证明。
R191 的原全空间混合型是独立的定量信息，不被这一理想论证替代。

## 7. Banach 商中仍保留全部快符号的精确型

边界核上的表示经 $\mathcal Q=\mathcal A/J$ 分解，
而且是收缩表示。
因此对任意 $g\in\mathcal A$ 及整数 $n$，
$$
\|(\pi_-(g)|_M)^n\|
\le\|q(g)^n\|_{\mathcal Q}
\le\|g^n\|.
\tag{7.1}
$$

若 $0\ne g\in\mathcal G$，R151 给原空间精确型
$c_*r^4$，§5 给左侧同样的精确型。
取 (7.1) 的对数 liminf，得到
$$
\boxed{
q(g)\ne0,\qquad
\tau_4(q(g))=c_*r^4,\qquad
r=\operatorname{ord}\iota(g).
}
\tag{7.2}
$$

于是 $\mathcal G$ 到 $\mathcal Q$ 的代数映射忠实，
并保留每个非零快元素的四次型。
这不是等距嵌入结论，也没有把原来的每个形式系数泛函下降到商中。

R187 同时给
$$
\operatorname{rad}\mathcal Q=\overline{b^n\mathcal Q}
\quad(n\ge1),\qquad b=q(A),
$$
且所有连续有限维表示都只有字符。
(7.2) 说明：这些有限维表示看不见的商范数结构，
仍容纳整个忠实快代数及其原来的精确幂型。

## 8. 已能确定的核与闭像，以及一般 G 的剩余点

### 8.1. 较小快尾子代数的准确结论

R179 对 $0\ne g\in\mathcal T$、
$r=\operatorname{ord}\iota(g)$ 给标准范数闭主理想
$$
\overline{g\mathcal A}=I_r
=\overline{A^r\mathcal A}.
\tag{8.1}
$$
把两向范数逼近送入任何本稿的连续表示，
即可同时识别核与像的闭包：
$$
\ker g_D=\ker D^r,\qquad
\overline{g_D(\text{空间})}
=\overline{D^r(\text{空间})}.
\tag{8.2}
$$

因此当 $r\ge1$ 时：

| 指定空间 | 核 | 值域闭包 |
|---|---|---|
| $M$ | $\mathbb C e_0$ | $N$ |
| $N$ | $\mathbb C e_0$ | $N$ |
| $\mathscr K=N/\mathbb C e_0$ | $0$ | $\mathscr K$ |

$r=0$ 时三种像均为有界单位。
这里对 $\mathscr K$ 的单射稠密结论确有额外的范数主理想输入。

### 8.2. 一般 G 不能只凭精确型升级

对一般 $0\ne g\in\mathcal G$ 且 $r\ge1$，
$\pi_-(g)e_0=0$，故其在 $M,N$ 上都至少有真空核。
又 $g\in I_1=\overline{A\mathcal A}$，所以
$$
g_M M\subseteq N.
$$
若 $g_M$ 或 $g_N$ 的核有限维，则只能是 $\mathbb C e_0$：
其核为 $B$ 不变空间，R187 的有限维分类适用。

在 $\mathscr K$ 上，$C$ 单射且像稠密，拟幂零。
所以它没有非零有限维不变子空间，也没有非零有限维连续不变商：
前者由有限维拟幂零与单射性矛盾；
后者由稠密像传到有限维商变成满射，再与拟幂零性矛盾。
因此一般 $g_C$ 若有非零核，该核必须无限维；
若其闭像为真子空间，对应缺陷商也必须无限维。

这些是准确的结构限制，尚未排除这些无限维可能。
§5 的型结论针对整个 $M,N,\mathscr K$，
没有给其任意未知子空间或后续商的同一下界，
所以不能套用“每个非零子商不消失”来自动排核或证明稠密像。

## 9. 与 Haar 传输和 N=M 问题的关系

R187 证明
$$
C^{2^j}/d_j\longrightarrow0\quad\text{强},
$$
而每个非零原 Haar 不变子商的对应归一化幂弱趋于 $I/2$。
因此两种表示之间的非零有界交织仍不存在。

本稿进一步说明，即使这些指定边界表示在全部快符号上保留精确四次型，
这种型信息也不会消除上述强弱极限差别。
不把它误作一个把边界核传回原 $H$ 的表示同一性。

具体未知问题仍是
$$
N=\overline{BM}\overset?=M.
$$
等价地，forward 子模
$$
\mathcal I=M^\perp
=\overline{\operatorname{span}\{(B^*)^nT^*e_0:n\ge0\}}
$$
是否满足
$$
(B^*)^{-1}\mathcal I=\mathcal I.
$$
有限头线性延拓、精确型及零交结论均未替代这个真实除法饱和问题。

原 Haar 表示中的一般慢限制值域与完整不变子空间问题仍未解决。

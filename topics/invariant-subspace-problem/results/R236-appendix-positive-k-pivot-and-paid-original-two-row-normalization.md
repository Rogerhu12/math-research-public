# R236 附录：实际双线性行的正 k 枢轴、三位正规化与双向源费用

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的实际有限层构造。** 本稿先给真正保留 carry 的两二次生成元正规化，再从原两条 $N_j$ 线性行列出全部原双源。第二生成元使指定三位链的费用只含较早的 $\eta_n^{-2}$；同时付出保存完整两生成元理想的反向源。没有据此声称固定原理想的所有未来层都保持这一改进，也没有把一般 gauge 的 $Q_j/H_\zeta$ 双行替换为本文的线性行。

原失联恢复稿保[完整笔记](../notes/2026-11-13-actual-two-row-k-correction-1856-recovery.md)。root 已全文核正分母、实际双源、反向单位和量词；所有结论仍按下述指定范围。

## 1. 一个实际的双二次 k 正规化

在某个真实尾 $\mathcal C_l$ 写
$$
N=N_l,\qquad N^2=t=\eta_lN_{l+1}.
$$
设 $U,V\in\mathcal B_l$ 有准确物理分块
$$
U=\alpha N+u,\qquad V=\beta N+v,
\quad u,v\in\mathcal B_{l+1},\quad\chi(u)=\chi(v)=0,
$$
其中 $\alpha\in\mathbb R\setminus\{0\}$、$\beta>0$ 是标量。
取 $\varepsilon,\delta>0$，并定义两条实际行
$$
H=V^2-\delta N,\qquad K=U^2+\varepsilon V.
\tag{1.1}
$$
令
$$
c=\frac{\varepsilon\beta}{2\alpha},\qquad
q_0=\frac{\varepsilon^2\beta^2}{4\alpha^2}
       +\frac{\varepsilon\delta}{2\beta}>0,
\qquad q=q_0I+\alpha^2t.
\tag{1.2}
$$
用 $u,v$ 写出四个真实块：
$$
C_H=v^2+\beta^2t,\qquad D_H=2\beta v-\delta I,
$$
$$
C_K=u^2+\alpha^2t+\varepsilon v,
\qquad D_K=2\alpha u+\varepsilon\beta I.
\tag{1.3}
$$
于是 $H=C_H+ND_H$、$K=C_K+ND_K$，并且
$$
\boxed{
C_K-\frac{u-c}{2\alpha}D_K
       -\frac{\varepsilon}{2\beta}D_H=q.
}
\tag{1.4}
$$
这里正项 $\varepsilon\delta/(2\beta)$ 与 $\varepsilon^2\beta^2/(4\alpha^2)$ 相加；没有取消一个可能为零的标量分母。

$q$ 是真实下一尾单位。定义当前尾中的两个原右源
$$
A=-\frac{\varepsilon}{2\beta}q^{-1},\qquad
B=\left[N-\frac{u-c}{2\alpha}\right]q^{-1},
\tag{1.5}
$$
以及下一尾算子
$$
\boxed{
R=\left[
 tD_K-\frac{u-c}{2\alpha}C_K
       -\frac{\varepsilon}{2\beta}C_H
 \right]q^{-1}.
}
\tag{1.6}
$$
则完整实际算子身份为
$$
\boxed{P:=N+R=HA+KB.}
\tag{1.7}
$$
证明是按 $I,N$ 展开：奇块系数由 (1.4) 恰为 $I$，偶块系数恰为 (1.6)。全部 $N^2=t$ 项均保留。
$R$ 的常数字符为零，因为 (1.6) 的每项均含 $t,u,v$ 中至少一项。

### 1.1 所用逆与双向完整理想身份

若
$$
\theta:=\frac{\alpha^2\eta_l}{q_0}\le\frac12,
\tag{1.8}
$$
则
$$
q^{-1}=q_0^{-1}\sum_{r\ge0}(-\alpha^2t/q_0)^r,
\qquad \|q^{-1}\|\le2/q_0.
\tag{1.9}
$$
这是真实算子范数的 Neumann 预算。

更重要的是，(1.5) 的第一个源 $A$ 是便宜的实际单位：
$$
\boxed{A^{-1}=-\frac{2\beta}{\varepsilon}q.}
\tag{1.10}
$$
因此
$$
\boxed{(H,K)=(P,K)}
\tag{1.11}
$$
作为 $\mathcal C_l$ 中的代数、范数闭或超弱闭生成理想，均准确成立。
反向身份明确为
$$
\boxed{
H=-\frac{2\beta}{\varepsilon}qP
 +\frac{2\beta}{\varepsilon}
       \left[N-\frac{u-c}{2\alpha}\right]K.
}
\tag{1.12}
$$
本稿没有使用 $B^{-1}$，也没有把某个未知商逆的范数省掉。

下一物理位的完整尾交由通常余式给出
$$
(P,K)\cap\mathcal C_{l+1}
=(R^2-t,\ C_K-RD_K).
\tag{1.13}
$$
范数及超弱闭版本同样由原正常余式证明。
(1.13) 保留全部第二生成元；它没有声称后者再次具有 (1.1) 的同一简单形式。

## 2. 从两条原 N 线性行得到 (1.1)

取固定起点 $n\ge0$，并固定两条实际范数收敛线性行
$$
S=\sum_{j\ge n}a_jN_j,\qquad
Z=\sum_{j\ge n}c_jN_j,
\quad a_n,a_{n+1}>0,
\tag{2.1}
$$
其中 $a,c\in\ell^1(\mathbb R)$。
置 $m=n+1$、$l=n+2$，以及
$$
r_n=c_n/a_n,\qquad
b_j=r_na_j-c_j\quad(j\ge m),\qquad b_m\ne0.
$$
令
$$
P_m=\frac{r_nS-Z}{b_m}=N_m+V,
\qquad
V=\sum_{j\ge l}\frac{b_j}{b_m}N_j,
$$
$$
F=\sum_{j\ge m}a_jN_j,
\qquad
U=\sum_{j\ge l}a_jN_j-a_mV.
\tag{2.2}
$$
因此准确有 $F=a_mP_m+U$。
写
$$
\varepsilon=\eta_na_n^2>0,\qquad
\delta=\eta_m,
$$
$$
H=V^2-\eta_mN_l,
\qquad K=U^2+\varepsilon V.
\tag{2.3}
$$
这正是 (1.1)。其物理系数为
$$
\boxed{
\beta=b_l/b_m,
\qquad\alpha=a_l-a_m\beta,
}
\tag{2.4}
$$
以及从 (2.2) 删除第 $l$ 项得到的 $u,v$。
只要 $\beta>0$、$\alpha\ne0$，§1 的正分母结论适用。
例如 $a_j>0$ 且 $r_j=c_j/a_j$ 严格单调时，
$$
\beta=\frac{a_l(r_n-r_l)}{a_m(r_n-r_m)}>0,
\qquad
\alpha=\frac{a_l(r_l-r_m)}{r_n-r_m}\ne0.
$$
这里 $\alpha$ 可以为负；$q_0$ 只使用 $\alpha^2$。

### 2.1 全部原双源

以下身份给出实际 $S,Z$ 源，没有只引用抽象理想成员性。
由 $N_n^2=\eta_nN_m$，
$$
Q=(F-a_nN_n)S=F^2-\varepsilon N_m.
\tag{2.5}
$$
又令
$$
E=a_m^2P_m+2a_mU-\varepsilon I.
\tag{2.6}
$$
代入 $F=a_mP_m+U$、$N_m=P_m-V$ 得
$$
Q=K+P_mE.
$$
所以
$$
\boxed{
H=(V-N_m)\frac{r_nS-Z}{b_m},
}
$$
$$
\boxed{
K=(F-a_nN_n)S-\frac{r_nS-Z}{b_m}E.
}
\tag{2.7}
$$
把 (2.7) 代入 (1.7)，就得到所求全部原双源：
$$
\boxed{P=S\mathcal U+Z\mathcal V,}
\tag{2.8}
$$
$$
\mathcal U=
\frac{r_n}{b_m}(V-N_m)A
 +\left[F-a_nN_n-\frac{r_n}{b_m}E\right]B,
$$
$$
\mathcal V=
-\frac{V-N_m}{b_m}A+\frac{E}{b_m}B.
\tag{2.9}
$$
所有因子属于原 $\mathcal A$；只有明确列出的非零标量与 §1 的 $q$ 被求逆。

### 2.2 这是完整两次尾交

原第 $n$ 位的首奇系数为非零标量 $a_n$。
完整尾交定理给
$$
(S,Z)\cap\mathcal C_m=(Q,P_m).
$$
(2.5)–(2.7) 又给 $(Q,P_m)=(K,P_m)$，因为 $K\in\mathcal C_l$。
对 $P_m=N_m+V$ 再用实际余式，得到
$$
\boxed{(S,Z)\cap\mathcal C_l=(H,K)=(P,K).}
\tag{2.10}
$$
对原理想先作范数或超弱闭再取尾交，等式由原余式映射逐次给出；
没有一般性地交换“闭包”和“取交”。
反向各因子为 $a_n^{-1},b_m^{-1}$、(2.6)，以及 (1.12)；全部已明确。

## 3. 一个明确的迟首正系数族及全部 carry 预算

现在取实际两条固定行
$$
a_j=(j+1)^{-2}\quad(j\ge n),\qquad
c_n=0,\quad c_j=a_j^2=(j+1)^{-4}\quad(j>n).
\tag{3.1}
$$
这是一个迟首辅助行实例。它本身不包含任意 $H_\zeta$ 或 Cayley 快补项。
记 $x=n+1\ge1$。
此时 $r_n=0$、$b_m=-c_m$，且
$$
P_m=Z/c_m,
\qquad
V=\sum_{j\ge l}\frac{a_j^2}{a_m^2}N_j,
\qquad
U=\sum_{j\ge l}a_j(1-a_j/a_m)N_j.
\tag{3.2}
$$
两条真实尾的系数均非负。
准确下一位标量为
$$
\boxed{
\alpha=\frac{2x+3}{(x+2)^4},\qquad
\beta=\frac{(x+1)^4}{(x+2)^4},\qquad
\varepsilon=\frac{\eta_n}{x^4},\quad\delta=\eta_{n+1}.
}
\tag{3.3}
$$
尤其 $\alpha,\beta>0$。
积分估计及正系数绝对和给
$$
\|V\|\le\frac{x+1}{3}\le x,
\qquad \|U\|\le\frac1{x+1}\le\frac1x,
\qquad \|v\|\le x,\quad\|u\|\le1/x.
\tag{3.4}
$$
最后两式也直接由实际物理块压缩得到。
还可用简单的统一界
$$
\frac1{81x^3}\le\alpha\le\frac5{x^3},
\qquad \frac16\le\beta\le1.
\tag{3.5}
$$

原 carry 的精确式是
$$
u_j=-\log\eta_j
=1400\,16^j-630\,8^j+300\,2^j,
\quad770\,16^j\le u_j\le1400\,16^j.
\tag{3.6}
$$
由 (3.3)–(3.5)，
$$
q_0\ge\frac{\eta_n^2}{3600x^2},
$$
$$
\frac{\alpha^2\eta_{n+2}}{q_0}
\le90000\,\frac{\eta_{n+2}}{\eta_n^2}
\le90000e^{-194320\,16^n}<\frac12.
\tag{3.7}
$$
所以每个指定起点 $n$ 的真逆都有已付上界
$$
\boxed{\|q^{-1}\|\le7200x^2\eta_n^{-2}.}
\tag{3.8}
$$
注意这里支付的是较早的 $\eta_n^{-2}$，不是 $\eta_{n+1}^{-2}$。

### 3.1 目标、原双源及反向源的明确范数

记 $J=-(u-c)/(2\alpha)$。
由 $\eta_n\le e^{-1070}$、(3.4)–(3.5)，
$$
|c|\le41\eta_n/x<1/x,
\quad\|J\|\le81x^2,
\quad\|C_H\|\le2x^2,
$$
$$
\|C_K\|\le2/x^2,
\quad\|D_K\|\le11/x^4.
\tag{3.9}
$$
例如 $\|C_K\|\le x^{-2}+25\eta_{n+2}x^{-6}+\eta_nx^{-3}$。
(1.6) 的分子范数小于 $164$，所以
$$
\boxed{
\|R\|\le1.2\cdot10^6x^2\eta_n^{-2},
\quad\|B\|\le6\cdot10^5x^4\eta_n^{-2},
\quad\|A\|\le22000x^{-2}\eta_n^{-1}.
}
\tag{3.10}
$$

对原双源，迟首 $r_n=0$ 把 (2.9) 简化为
$$
\boxed{
\mathcal U=(F-a_nN_n)B,
\qquad
\mathcal V=\frac{V-N_m}{c_m}A-\frac{E}{c_m}B.
}
\tag{3.11}
$$
这里 $c_m=(x+1)^{-4}$，且
$$
\|F-a_nN_n\|\le2/x,\qquad
\|E\|\le5/x^3,
$$
$$
\|(V-N_m)/c_m\|\le32x^5,
\qquad \|E/c_m\|\le80x.
$$
因此，例如
$$
\boxed{
\|\mathcal U\|\le1.2\cdot10^6x^3\eta_n^{-2},
\qquad
\|\mathcal V\|\le5\cdot10^7x^5\eta_n^{-2}.
}
\tag{3.12}
$$
这些常数不作最优性主张。

反向也保留实际预算。由 (1.2)、(3.5)，
$$
q_0\le1644\eta_n^2/x^2,
\qquad\|q\|\le2466\eta_n^2/x^2.
$$
故 (1.12) 的两个反向源满足
$$
\boxed{
\left\|\frac{2\beta}{\varepsilon}q\right\|
\le5000x^2\eta_n,
\qquad
\left\|\frac{2\beta}{\varepsilon}(N+J)\right\|
\le164x^6\eta_n^{-1}.
}
\tag{3.13}
$$
这次完整两生成元等价不含任何未预算的反向单位。

## 4. 与旧完整尾商及同一正常锚的连接

对固定原理想 $S\mathcal A'+Z\mathcal A'$，(2.8) 给真正位于第 $l=n+2$ 尾的
$P=N_l+R$，且原双源为 (2.9) 或 (3.11)。
若旧规范 $G_l^{\rm old}$ 来自 $S_l=D_l(N_l+G_l^{\rm old})$，
原余式 $\mathfrak r_l(a+N_lb)=a-G_l^{\rm old}b$ 给
$$
R-G_l^{\rm old}\in\mathcal J_{l+1}'(S,Z).
$$
所以 (3.10) 是完整联合商中 $G_l^{\rm old}$ 的一个实际代表上界。
并非 raw 商范数下界，也不依赖正常表示的像范数倒推提升范数。

设同一个原正正常密度 $0\ne\rho\ge0$ 湮灭 $S\mathcal A'+Z\mathcal A'$。
定义
$$
\Theta=2P(I+N_l)^{-2}
 =S[2\mathcal U(I+N_l)^{-2}]
  +Z[2\mathcal V(I+N_l)^{-2}].
\tag{4.1}
$$
在第 $l$ 位取 $e=\Omega_+\otimes I$。
原二乘二 carry 身份准确给
$$
\boxed{e^*\Theta e=I,\qquad\omega_l(\Theta)=1.}
\tag{4.2}
$$
实际目标与两个原源的费用分别为
$$
\|\Theta\|\le\frac{8(1+\|R\|)}{(1-\eta_l)^2},
$$
$$
\|2\mathcal U(I+N_l)^{-2}\|
\le\frac8{(1-\eta_l)^2}\|\mathcal U\|,
\quad
\|2\mathcal V(I+N_l)^{-2}\|
\le\frac8{(1-\eta_l)^2}\|\mathcal V\|.
\tag{4.3}
$$
对 (3.1) 可取
$$
\|\Theta\|\le2\cdot10^7x^2\eta_n^{-2},
\qquad
\frac{|\omega_l(\Theta)|}{\|\Theta\|}
\ge\frac{\eta_n^2}{2\cdot10^7x^2}.
\tag{4.4}
$$
同一个 $\rho$ 湮灭 (4.1)，未换纯态或作新的正化。
(4.4) 是明确但会变小的锚，没有统一正下界。

## 5. 费用改善的准确量词和可继续范围

### 5.1 对指定三位链的真实改善

(3.10)、(3.12) 的对数预算为
$$
2u_n+O(\log(n+2)).
$$
在 $l=n+2$ 的尺度上，这一指定构造满足
$$
\limsup_{n\to\infty}16^{-(n+2)}
\log\max\{1,\|R\|,\|\mathcal U\|,\|\mathcal V\|\}
\le\frac{175}{16}.
\tag{5.1}
$$
这里极限比较的是 (3.1) 中**以 $n$ 为起点的实际两行族**。
对一个固定起点的原正常湮灭者，本文只直接给该起点后的 $l=n+2$ 层。
不能从原 $S,Z$ 的湮灭自动删去前 $n$ 项，继而把 (5.1) 误称为同一原理想的全层渐近 type。

例如 $n=0$ 时，当前目标的主要对数费用为 $2u_0=2140$；
同一行只用此前单行 h 修正到第2位的预算为
$8u_0+2u_1+5\log8=44480+5\log8$。
这是对指定已付上界的改善，不是二者最小成本之比的下界。

### 5.2 可以立即继续的原来源递推

从固定 (2.8) 出发，下一步可对 $P=N_l+R$ 使用
[carry 稳定的单行 h 修正](R236-appendix-carry-stable-recursive-h-corrections-and-actual-sources.md)。
若该稿给 $P_{l+1}=(R-N_l)P A_l$，则两个原源同时乘同一个已付右因子：
$$
\mathcal U_{l+1}=\mathcal U(R-N_l)A_l,
\qquad
\mathcal V_{l+1}=\mathcal V(R-N_l)A_l.
\tag{5.2}
$$
因此整个未来构造仍属于**同一个**原 $S,Z$ 理想，并由同一个原 $\rho$ 湮灭。
(3.10)、(3.12) 的全部初值都小于 $\exp(240\,16^l)$，
所以该稿的全层 Neumann 归纳直接支付后续每一步的实际 carry 和双源。
但只使用单行修正时，其长期主上界回到 $700/3$；不能把 (5.1) 的有限链改善声称为已保持。

若保留完整第二生成元，准确下一接口是 (1.13)：
$$
h_{l+1}=R^2-\eta_lN_{l+1},\qquad
k_{l+1}=u^2+\alpha^2\eta_lN_{l+1}+\varepsilon v
             -R(2\alpha u+\varepsilon\beta I).
\tag{5.3}
$$
它们具有明确实际来源，且完整尾交已由 (1.10)–(1.13) 支付。
不过 $k_{l+1}$ 一般为 $u,v$ 的较高次有理式；不能重命名后把它当作新的两条纯线性行。
继续利用 (5.3) 的特殊系数降低未来成本仍是实际下一问题。

## 6. 与原二次见证的边界

本稿的所有源、逆和锚都在原 Haar 算子及其真实 $N_j$ 上，不是纯 nilpotent 模型。
但 (2.1) 明确要求两个初始生成元都是实际 $N_j$ 线性和。
原迟首二次核通常给的是同一 gauge 的 $S=X+H_\zeta$ 与
$Z=Y-B_0+H_\zeta^2$；其中 $Q_j$ 或 $H_\zeta$ 未被本稿删除。
因此不能直接把一般这对 $S,Z$ 代进 (3.1)。

例如在 **N 版本** 的二次式
$$
T_N=X^2-\sum_{j\ge n}a_j^2N_j^2+Y,
\quad X=\sum_{j\ge n}a_jN_j,\quad
Y=\sum_{j>n}c_jN_j,
$$
若已合法选定只翻转第 $n$ 位的 gauge，准确一次因子为
$S=X-a_nN_n$。对应同一正常见证的第二行是
$$
Z=Y-\sum_{j>n}a_j^2N_j^2
=c_{n+1}N_{n+1}
 +\sum_{j\ge n+2}(c_j-a_{j-1}^2\eta_{j-1})N_j.
\tag{6.1}
$$
因此 **在该特定 gauge 已产生非零见证的前提下**，(2.1) 的一般线性行版本可从 $n+1$ 开始检查：
原主系数为 $a_j$，辅助系数必须使用 (6.1) 的精确 carry 修正。
未证明这个 gauge 总能选到，未把它替代由一般存在性得到的另一个 $\zeta$，也未未经计算就将 (3.3) 套给修正后系数。

本稿新增的是明确双源、正分母、保完整理想的廉价反向和有限层费用改善。
同一固定原理想的全层统一正常锚与一般实际两行的进一步低费消元仍未关闭。

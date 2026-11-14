# R472 — 同预算法向导数真像与最高次数立方范围

日期：2026-11-14。**状态：已证明。** 本篇直接计算 R459 式 (13d) 使用的同一个实际仿射修正格的一部分真像。利用原连续电荷列的准确角次数，得到法向导数 jet 的明确满射界；没有扩大 $D$、没有加入自由角多项式，也没有用试验矩形替换原来源。在 $D=3b_F$、源维数至少为原三块长度、立方接触取最小允许阶的整段范围内，R459 的单独单位 $5$ 法向导数条件必可由原格实现。

这付清的是该必要条件的真实像，而非整个首次提升：当 R459 的另一条单位 $-2$ 分支值也可读时，两条必须用同一个修正联立；原三个块、两条十三行 carry 和完整第二障碍仍保留。新增第三原中央不改变本篇无条件满射，也不因此付出全局预算。

## 1. 原有限格与待求的真实映射

固定 $p=6s-1>83$，$f_D=\lfloor9D/2\rfloor+4<p$，所以 $D<p$。取整个原单部分
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},\qquad Y=\mathscr R,
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\qquad
A_n=\lfloor(n+1)/4\rfloor,\quad B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
d=1+8t,\quad h_7=7+4t+16t^2,\quad
e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+\lceil2m/3\rceil-2.
$$
记
$$
f_n=\deg q_n+e_{n+1}=\lfloor9n/2\rfloor+4,\qquad
M_n=f_n+C_n=5n+4-(n\bmod2).
\tag{1}
$$
以下 $k$ 是剩余域，必要时先作代数闭包；满射是矩阵秩条件，故最终按原系数域下降。

设 $F(t,Y)=\sum_{i=0}^b f_i(t)Y^i\in k[t,Y]$ 不可约，
$$
F(0,1)=0,\qquad F_Y(0,1)\ne0,\qquad 1\le b\le D.
$$
其唯一正规分支为 $Y=\psi(t)$。定义准确的斜次数
$$
\boxed{u(F)=\max_i\{\deg_t f_i-4i\}.}
\tag{2}
$$
不可约 $F$ 不是 $Y$，故 $f_0\ne0$，从而 $u(F)\ge0$。
这里用每个真实系数的次数，未以 $\deg_tF$ 的矩形上界替代。

R459 需要的同一线性映射是
$$
\overline{\mathcal W}_D\longrightarrow k[[t]]/(t^{H+1}),
\qquad R\longmapsto(\mathcal ER)(t,\psi(t)),\qquad
\mathcal E=Y\partial_Y.
\tag{3}
$$
乘 R461 的共同角单位 $d^{C_D}$ 后仍是同一个满射问题，因为 $\mathcal E$ 不作用于角单位，且 $d(0)=1$。$t=-w+\cdots$ 也保完整 jet 长度及像；所以 (3) 可直接用于原 $w$ 坐标中的指定首项。

## 2. 连续 b 个真实 charge 内的斜三角子格

令
$$
n_0=D-b+1\ge1,\qquad
K=M_{n_0}-3A_D-B_D,
$$
$$
\mathcal H_D(t)=(th_7)^{A_D}(t-1)^{B_D}d^{-C_{n_0}}.
\tag{4}
$$
对 $n_0\le n\le D$，商
$$
\frac{\mathcal H_D}{q_n}
=(th_7)^{A_D-A_n}(t-1)^{B_D-B_n}d^{C_n-C_{n_0}}
\tag{5}
$$
是实际整多项式，次数为
$3(A_D-A_n)+(B_D-B_n)+C_n-C_{n_0}$。因此该列仍允许的多项式次数准确为
$$
e_{n+1}-\deg(\mathcal H_D/q_n)
=f_n-3A_D-B_D+C_{n_0}.
$$
若 $n=n_0+i$，则
$$
f_{n_0+i}-f_{n_0}
=4i+\lfloor(n_0+i)/2\rfloor-\lfloor n_0/2\rfloor\ge4i.
$$
故有真正的、未扩预算的包含
$$
\boxed{\mathcal H_DY^{n_0}
\left\{\sum_{i=0}^{b-1}Y^iP_i(t):\deg P_i\le K+4i\right\}
\subset\overline{\mathcal W}_D.}
\tag{6}
$$
负的次数上界表示该系数为零。因所有 $n_0+i$ 均处于 $1,\ldots,D<p$，逐列除以其 charge 是整可逆的。因此 (6) 同时包含于
$\mathcal E\overline{\mathcal W}_D$ 的来源表示中；这里没有用一个含 $p$ 分母的 Euler 逆。

在 $Y=\psi$ 上，$\mathcal H_D\psi^{n_0}$ 的阶恰为 $A_D$，其余因子都是单位。于是它将一个完整长度 $j$ 的多项式 jet 送为 $t^{A_D}$ 后的完整长度 $j$ jet。

## 3. 斜三角空间在真实代数分支上的完整限制

这一节给 (6) 的完整几何证明，并保可能的全局奇点。取 Hirzebruch 曲面 $\mathbb F_4$，负截面记为 $S_0$、纤维记为 $F_0$，则
$$
S_0^2=-4,\quad S_0F_0=1,\quad F_0^2=0,
\qquad K_{\mathbb F_4}=-2S_0-6F_0.
$$
在原仿射 $(t,Y)$ 图中，完整空间
$$
\sum_{i=0}^mY^i k[t]_{\le K+4i}
$$
恰是
$H^0(\mathbb F_4,\mathcal O(mS_0+(K+4m)F_0))$。这由两张底图的变换直接读出，等价于其沿 $\mathbf P^1$ 的推前
$\bigoplus_{i=0}^m\mathcal O(K+4i)$；没有取一组非完整截面。

设 $C$ 为 $F=0$ 的整闭包。由 (2) 的精确最大次数和 $\deg_YF=b$，其除子类为
$$
C\sim bS_0+(u+4b)F_0.
\tag{7}
$$
原点 $P=(0,1)$ 为光滑点，且 $t$ 是该点的正规参数。全局 $C$ 可以奇异；作为光滑曲面中的整 Cartier 曲线，它是 Gorenstein，必须使用其算术亏格而非未经证明的光滑模型亏格。

取
$$
L=\mathcal O_C((b-1)S_0+(K+4b-4)F_0).
$$
曲面限制序列的核是
$$
\mathcal O_{\mathbb F_4}(-S_0+(K-u-4)F_0).
$$
它在每个纤维都是 $\mathcal O_{\mathbf P^1}(-1)$，推前及高推前都为零。因此该核的所有上同调为零，准确得到
$$
\boxed{H^0(C,L)=
\left\{\sum_{i=0}^{b-1}Y^iP_i(t):\deg P_i\le K+4i\right\}.}
\tag{8}
$$
这是 R459 所需的实际分支限制，并未只用两个空间维数相同来认定。

伴随公式给
$$
\omega_C=L\otimes
\mathcal O_C(-S_0+(u-K-2)F_0),
$$
所以
$$
\boxed{\deg(\omega_C\otimes L^{-1})
=(b-1)u-bK-2b.}
\tag{9}
$$
也可直接核算
$p_a(C)=(b-1)(2b-1+u)$；当 $K\ge0$ 时 (8) 的维数是
$b(K+1)+2b(b-1)$，与 (9) 的 Riemann–Roch 值相合。

对长度 $j\ge1$ 的实际 $P$-jet，若
$$
j\le bK-(b-1)u+2b-1,
\tag{10}
$$
则 $\omega_C\otimes L^{-1}(jP)$ 的度严格为负，因 $C$ 整而没有非零截面。Gorenstein Serre 对偶遂给
$H^1(C,L(-jP))=0$，因此
$$
H^0(C,L)\twoheadrightarrow L|_{jP}
$$
是真满射。这一步同时处理所有分支曲线的全局奇点；没有假设 $P$ 是一般点或使用数值意义上的 Padé 正常性。

所用标准上同调事实可核于 Stacks Project 的
[projective-space cohomology](https://stacks.math.columbia.edu/tag/01XS)、
[Gorenstein Riemann–Roch/duality](https://stacks.math.columbia.edu/tag/0BS6) 及
[negative degree line bundles](https://stacks.math.columbia.edu/tag/0B40)。本题的完整来源包含、曲面类和次数 (5)–(10) 已在此逐项给出。

## 4. 同一个原导数像的满射界

还须填入 (6) 未触及的最初 $A_D$ 行，而不能免费除 $t^{A_D}$。对
$0\le r<A_D$，取真实 charge $n=r+1$ 的原列
$$
Y^{r+1}q_{r+1}(t)t^{r-A_{r+1}}.
\tag{11}
$$
有 $A_{r+1}\le r$ 且所显示多项式次数不超过 $e_{r+2}$。其在分支上的首阶恰为 $r$，施加 $\mathcal E$ 后首系数另乘 $r+1$，仍为单位。按 $r$ 递增作三角消元，(11) 完整支付这些低行；产生的所有高尾随后由 (6)、(10) 同时修正。

**定理 1。** 置
$$
\boxed{H_D(F)=A_D+bK-(b-1)u(F)+2b-2.}
\tag{12}
$$
只要 $H\le H_D(F)$，映射 (3) 满射。低于 $A_D$ 的部分由 (11) 单独满射；若 (10) 的右端非正，则 (12) 不额外给出高行。

特别，对任意真实仿射修正空间
$\bar R_{\rm base}+\overline{\mathcal W}_D$，其法向导数 jet 也充满同一目标。这不需要选取一个保 $F$ 或保 $F^2$ 的修正。若 R459 的 $h+k\le H_D(F)$，其式 (13d) 的指定非零单位 $5$ jet 总能由同一实际仿射格实现；单独这条必要条件不能排除候选。

此结论没有断言同一个修正已满足 $R_0,R_1,R_2$ 的全部物理行，或满足另一条分支值。满射属于准确的 (3)，不能扩大成全 $\beta_J$ 满射。

## 5. 真立方首核给更强斜次数约束

现在真正使用 R459 的实际来源条件：
$$
d^{C_D}\bar P=t^rF^3Q,\qquad r\ge1,\quad Q(0,1)\ne0,
\quad\bar P\in\overline{\mathcal W}_D.
\tag{13}
$$
赋多项式权 $\operatorname{wt}(t)=1$、$\operatorname{wt}(Y)=-4$。
原第 $n$ 个系数乘 $d^{C_D}$ 后次数不超过 $f_n+C_D$，所以整个真实来源满足
$$
\operatorname{wt}(d^{C_D}\bar P)
\le C_D+4+\max_{n\le D}\lfloor n/2\rfloor
=2C_D+4.
\tag{14}
$$
加权最高次初形式的乘积非零，故这个权对乘法准确相加，即使某些元素的权为负也成立。

设 $m$ 为 $Q$ 的最低 $Y$ 次数，则
$\operatorname{wt}(Q)\ge-4m$，而 $m+3b\le D$。因此 (13)–(14) 给
$$
r+3u-4(D-3b)\le2C_D+4,
$$
即
$$
\boxed{u(F)\le\left\lfloor\frac{M_D-r}{3}\right\rfloor-4b.}
\tag{15}
$$
这里保留了 $Q$ 可以含 $Y^m$ 的情况；不能因为 $Q(0,1)$ 为单位，就把它误认成对负权非负。

式 (15) 是整个原格强迫的斜次数界，比只用 $3\deg_tF+r\le M_D$ 更适合 (12)。右侧为负时，该真实因子形状本身不可能，因为 $u(F)\ge0$。

## 6. 最高径向次数和最小接触：单位 5 条件全部可实现

令
$$
\mathsf N_D=\dim\overline{\mathcal W}_D
=\sum_{n=0}^D(e_{n+1}+1).
$$
在真实 (13) 的基础上，假定
$$
D=3b,\qquad 2s+\ell\le\mathsf N_D,
\qquad h=\left\lceil\frac{s-r}{2}\right\rceil\ge1,
\qquad k=2h+r-s\in\{0,1\}.
\tag{16}
$$
当应用 R459 时仍需其完整可读窗
$k<\min(s-h,\ell,h)$；本节不删除这项条件。

**定理 2。** 整个 (16) 范围内都有
$$
\boxed{h+k\le H_D(F).}
\tag{17}
$$
因此 R459 单独的法向导数必要值在这一最高径向次数的整段原预算中，必可由真实仿射修正格实现。

**证明。** 此时 $n_0=2b+1$，令 $A=\lfloor(3b+1)/4\rfloor$。式 (4)、(15) 给
$$
K=9b+8-3A,\qquad
u\le u_b:=\begin{cases}b+1,&b\text{ 偶},\\b,&b\text{ 奇}.\end{cases}
$$
所以只需用
$$
H_b=A+b(9b+8-3A)-(b-1)u_b+2b-2
\le H_D(F).
\tag{18}
$$
另一方面，由 $r\ge1,\ell\ge1$ 和 (16)，
$$
h+k\le s/2+1\le(\mathsf N_{3b}+3)/4.
\tag{19}
$$
完整 floor/ceiling 成本必须核清。原维数的十二项块为
$$
(e_{n+1}+1)_{0\le n<12}=(5,9,14,15,21,24,30,31,36,40,46,46),
$$
其和 $317$，且每移十二项恰增加 $47$。令 $b=4m+j$，则直接求和得
$$
\begin{array}{c|c}
j&4H_b-\mathsf N_{3b}-3\\\hline
0&86m^2+90m-12\quad(m\ge1),\\
1&86m^2+137m+14,\\
2&86m^2+200m+63,\\
3&86m^2+247m+120.
\end{array}
\tag{20}
$$
每个允许值都严格为正。与 (18)–(19) 合并即得 (17)。这是所有整数预算的闭式比较，不是扫描目标素数后作外推。$\square$

这给出了 R467 留下的高径向次数区内一个准确的真像结论。它没有假定已经找到该范围的深立方首核，也没有把一个试验代数分支标为原 $g$；定理 1 对每个给定代数分支都计算同一个真实来源像，定理 2 说明任何符合原条件的候选在这一个必要测试上都不能被排除。

## 7. 与第三原中央及完整原 M 的关系

R468 新增了合法的第三角中央条件，但 (6)、(11)、(12) 只使用固定 canonical 来源、$F$ 的实际分支和可逆 charge；它们不把 $g$ 的三个高轴当作可调源系数。故三个中央同时失败也不破坏定理 2 的法向导数满射。若另外添入第三来源列，像只会增大，不能使已实现的 jet 重新成为缺口。

剩下的实际条件仍有两层：当 $r>2k$ 时，R459 还强迫同一个 $R$ 的分支值有单位 $-2$ 首项；其余情况下也始终保留原全部 $J$ 行及真实 $\pi\beta_J$。本篇的单导数满射没有证明这些联立条件可解，亦没有证明它们不可解。

恢复整个原矩阵时继续使用
$$
M=c_*U_0m_{13}J,\qquad
K_2^{\rm red}(M)=\ker(\pi\beta_J),\qquad
G_2=C_2(J)/\overline H.
$$
$P_{134}/U_0$、十三自由行、两条十三行 carry 和原第三位保持 R449/R468 的准确运输。没有在来源上除去 $t^{A_D}$ 或 $t^r$，也没有由法向导数的同格满射宣称物理像饱和。主目标与 R418 的全量词严格预算仍未完成。

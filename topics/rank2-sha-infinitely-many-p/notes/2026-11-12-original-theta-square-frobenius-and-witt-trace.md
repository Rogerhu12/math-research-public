# 原两变量 theta 的真实平方 Frobenius、参考因子与全轨道 Witt 交叉项

日期：2026-11-12。状态：本文的完整 theta Frobenius 方程、
公共参考因子的整性、所有迭代层及原 $256$ 项求和的 Witt 公式均已证明。
它们给原中央对角的实际约束，尚未给其无穷素数非消失。

本篇不把轨道和换成对数范数。
它接续[原 theta 的固定同源覆盖](2026-11-12-translated-kummer-units-and-original-theta-cover.md)，
保留同一个二挠点参考以及每个标签的指数化。

## 1. 固定曲线、真实 Frobenius lift 和原 theta

始终取
\[
E:y^2=x^3-17x,\quad \omega=dx/(2y),\quad
N=68,\quad T=(0,0),\quad F=K(E[f]),\quad f=34(1+i).
\]
$\mathcal S$ 是原 $256$ 点 $F/K$ 轨道。
取惰性素数 $p\ge7$，所以 $p\ne17$，并在相应未分歧整环
$\mathcal O$ 中实现全部原 $N$ 级标签。
记 $\sigma$ 为算术 Witt Frobenius，置
\[
q=p^2,\qquad a_r=(-p)^r,\qquad Q_r=a_r^2=p^{2r}.
\]

$p\equiv3\pmod4$ 时，点数公式中 $x$ 与 $-x$ 的二次字符项相消，
给 $a_p(E)=0$。故约化上的 $p$ 次幂 Frobenius $\pi_p$ 满足
\[
\pi_p^2=[-p].
\]
prime-to-$p$ torsion 的约化单射，于是
\[
\sigma^{2r}(P)=[a_r]P,\qquad P\in E[N].
\tag{1}
\]
因此本篇使用的源曲面映射
\[
\Phi=[-p]\times[-p]:E\times E\longrightarrow E\times E
\tag{2}
\]
是真正约化为 $p^2$ 次幂 Frobenius 的全局同源，
不是在一个局部参数上任意写 $Z\mapsto Z^{p^2}$。
它和 $[N]\times[N]$ 准确交换。

在原加法均匀化变量中，沿用
\[
F_P(z)=e^{-\eta_Pz}\frac{\sigma(z_P+z)}{\sigma(z_P)},\qquad
\Theta_P(z,w)=\frac{F_P(z+w)}{F_P(z)\sigma(w)},
\]
\[
Z=-x/y,\qquad
U_P(z,w)=Z(w)\Theta_P(z,w).
\tag{3}
\]
$U_P$ 是在 $w=0$ 为一的正式单位。
这里不预先断言它在惰性处系数整。
其系数属于原 $F$，且
\[
U_P^{\sigma^{2r}}=U_{a_rP}
\tag{4}
\]
由已证明的原 torsion 初值与 sigma 系数的 Galois 相容性得到。

下文的整性均指两个整形式群参数
$Z_1=Z(z),Z_2=Z(w)$，不是把加法对数变量误当整参数。

## 2. 不丢公共因子的完整乘法公式

对于任意与 $N$ 互素的非零整数 $a$，sigma 除法函数满足
\[
\sigma(az)=\Psi_a(z)\sigma(z)^{a^2},\qquad
\Psi_a(z)=a z^{1-a^2}+\cdots.
\tag{5}
\]
选择 $aP$ 的代表为 $az_P$，并用 $\eta_{aP}=a\eta_P$。
换代表的周期因子在 $F_P$ 中相消，所以准确有
\[
F_{aP}(az)=F_P(z)^{a^2}
              \frac{\Psi_a(P+z)}{\Psi_a(P)}.
\tag{6}
\]
将 (6) 分别用于 $z+w,z$，再使用 (5)，得到
\[
\Theta_{aP}(az,aw)
=\Theta_P(z,w)^{a^2}
 \frac{\Psi_a(P+z+w)}
      {\Psi_a(P+z)\Psi_a(w)}.
\tag{7}
\]
这是原 theta 的公式，不是其对数或某个系数的类比。

定义
\[
J_a(w)=\frac{Z([a]w)}{Z(w)^{a^2}\Psi_a(w)},\qquad
D_{a,P}(z,w)=
J_a(w)\frac{\Psi_a(P+z+w)}{\Psi_a(P+z)}.
\tag{8}
\]
两者在原点的可去值均为一。(3)、(7) 给出
\[
\boxed{\quad
U_{aP}(az,aw)=U_P(z,w)^{a^2}D_{a,P}(z,w).
\quad}
\tag{9}
\]
尤其由 (1)、(4)，
\[
\boxed{\quad
U_P^{\sigma^{2r}}\circ\Phi^r
       =U_P^{Q_r}D_{a_r,P}
\qquad(r\ge1).
\quad}
\tag{10}
\]
$D_{a,P}$ 是 $E\times E$ 上的真实有理函数；
(10) 保留完整原点 germ 的所有混合系数。

## 3. 公共参考 J_a 的整性必须单独证明

这里只取 $a=a_r=(-p)^r$，并写 $Q=a^2$。
尽管 (8) 的分子和 $\Psi_a$ 各自首项都含 $a$，
它们的比值并非仅因常数为一就自动整。
下面使用完整除子消去全部 $p$-primary kernel。

### 3.1 在非零二挠点处核定 division 常数

原曲线的奇数 division function 在 $T=(0,0)$ 满足
\[
\boxed{\qquad
\Psi_n(T)=(-1)^{(n-1)/2}17^{(n^2-1)/4}
\quad(n>0\text{ 为奇数}).
\qquad}
\tag{11}
\]
负奇数由 $\Psi_{-n}=-\Psi_n$ 延拓；符号等于 $\chi_{-4}(n)$。

为完整核定 (11)，可在标准 division recurrence 中直接代入 $T$。
偶数 division functions 在 $T$ 为零，奇数初值为
\[
\Psi_1(T)=1,\qquad \Psi_3(T)=-17^2 .
\]
对 $n=2m+1\ge5$，只有一个乘积非零：
\[
\Psi_{2m+1}(T)=
\begin{cases}
-\Psi_{m-1}(T)\Psi_{m+1}(T)^3,&m\text{ 偶},\\
 \Psi_{m+2}(T)\Psi_m(T)^3,&m\text{ 奇}.
\end{cases}
\]
代入归纳式，指数两种情况均为 $m(m+1)$；
符号分别为 $+1,-1$，正好等于 $(-1)^m$。
这证明 (11)，不需要猜 resultant 的符号。

$a=(-p)^r\equiv1\pmod4$，而
$(p^{2r}-1)/4$ 是 $p-1$ 的倍数。因此
\[
\Psi_a(T)=17^{(Q-1)/4}\equiv1\pmod p.
\tag{12}
\]
另一方面，[a] 在特殊纤维等于纯不可分的
$p^{2r}$ 次幂 Frobenius，其全部 geometric kernel 只有 $O$。
整数 division 函数的水平零点全部约化到 $O$。
(12) 保证没有一个整体竖直 $p$ 因子；
约化函数的除子因而为
$Q(O)-Q(O)=0$。所以
\[
\boxed{\qquad \overline{\Psi_a}=1
                    \quad\text{作为 }\overline E\text{ 上的有理函数}.\qquad}
\tag{13}
\]

### 3.2 公共比值的所有 kernel 点恰好相消

在原模型记非零二挠点为 $T_0=T,T_+,T_-$。有
\[
\operatorname{div}Z=(O)+(T_0)-(T_+)-(T_-),\qquad
\operatorname{div}\Psi_a=[a]^*(O)-Q(O).
\]
故 (8) 的准确除子是
\[
\boxed{\quad
\operatorname{div}J_a
 =[a]^*\big((T_0)-(T_+)-(T_-)\big)
        -Q\big((T_0)-(T_+)-(T_-)\big).
\quad}
\tag{14}
\]
全部 $[a]$-kernel 已从 (14) 消失；
没有把这些深处的形式挠点极点留在一个分母里。

(14) 的剩余支撑约化到非零二挠点，因而都远离形式原点。
在光滑 proper 整模型上，一个有理函数的除子由这些水平闭包
及可能的特殊纤维整数倍组成。特殊纤维不可约，
而水平支撑不遇到零截面；$J_a(O)=1$ 因而迫使该竖直倍数为零。
所以
\[
J_a\in\mathbb Z_p[[Z_2]]^\times.
\tag{15}
\]
这一步同时排除了隐藏的 $1/p$ 系数；单独的 $J_a(O)=1$
没有被用作充分理由。

现在 (2)、(13) 给
\[
\overline{Z([a]w)}=Z(w)^Q,\qquad
\boxed{\quad J_a\equiv1\pmod p.\quad}
\tag{16}
\]
对原 $P$ 及参考 $T$，$\Psi_a(P+z)$ 在形式邻域为单位且模 $p$ 为一，
因为 $P$ 约化不为 $O$。因此
\[
\boxed{\quad
D_{a,P},D_{a,T}\in1+p\mathcal O[[Z_1,Z_2]],
\qquad D_{a,P}(Z_1,0)=D_{a,T}(Z_1,0)=1 .
\quad}
\tag{17}
\]
特别，公共参考 $D_{a,T}$ 已单独付清整性；
证明没有假设 $U_T$ 在 supersingular 处整。

## 4. 同一个真实 Frobenius 的全部层

对任意正式函数定义
\[
\mathcal F(f)=f^{\sigma^2}\circ\Phi .
\]
$\Phi$ 定义于 $\mathbb Q_p$，所以与系数 $\sigma^2$ 交换。
由 (10)，令
\[
D_{r,P}=D_{a_r,P},
\]
便有
\[
\mathcal F^r(U_P)=U_P^{q^r}D_{r,P},
\]
\[
\boxed{\quad
D_{r,P}
=\prod_{j=0}^{r-1}
      \mathcal F^j(D_{1,P})^{q^{\,r-1-j}},
\qquad
\log D_{r,P}
=\sum_{j=0}^{r-1}
      q^{\,r-1-j}\mathcal F^j(\log D_{1,P}).
\quad}
\tag{18}
\]
$D_{1,P}(Z_1,0)=1$，故这里是常数为零的正式对数；
由 (17)，它也属于 $p\mathcal O[[Z_1,Z_2]]$。

(18) 的另一种完全显式表达就是 (8) 取 $a=(-p)^r$。
两种表达的相等来自真实 multiplication composition，
而不是把一个逐 $p$ 的模 $p$ 恒等式迭代到未核精度。

虽然各层都属于 $1+p\mathcal O[[Z_1,Z_2]]$，
(18) 不自动给 $D_{r,P}\in1+p^r\mathcal O[[Z_1,Z_2]]$：
末项 $\mathcal F^{r-1}(D_{1,P})$ 的幂为一。
若需要更高精度，必须同时使用具体 jet 阶与 $\Phi^{r-1}$ 的收缩，
不能凭层数补上额外的 $p$ 因子。

### 4.1 完整正式解的歧义准确只有二次项

固定同一个包含原 $F$ 的局部未分歧系数域，以及同一个保持
$p$-赋值的 $\sigma$。设 $U,\widetilde U$ 是常数为一的两个正式解，
满足同一个完整方程
$\mathcal F(U)=U^qD_{1,P}$。令 $V=\widetilde U/U$。
在加法参数中 $[-p](z,w)=(-pz,-pw)$，故
\[
V^{\sigma^2}(-pz,-pw)=V(z,w)^{p^2}.
\]
写 $\log V=\sum_{i+j>0}c_{ij}z^iw^j$，逐系数给
\[
(-p)^{i+j}\sigma^2(c_{ij})=p^2c_{ij}.
\]
若 $c_{ij}\ne0$，因为 $\sigma$ 保持赋值，两侧赋值迫使 $i+j=2$；
此时等式又准确成为 $\sigma^2(c_{ij})=c_{ij}$。
因此全部可能的歧义恰为
\[
\boxed{\quad
V(z,w)=\exp(c_{20}z^2+c_{11}zw+c_{02}w^2),
\qquad \sigma^2(c_{ij})=c_{ij}.
\quad}
\tag{18a}
\]
这使用的是正式对数，不需要先假设两个解在整个单位双盘收敛。
反之，(18a) 中每个因子都满足齐次方程，所以此分类是双向的。

原 $U_P(z,0)=1$ 的规范杀掉 $c_{20}$。
而原曲线的 $Z(w)/\sigma(w)=1+O(w^4)$，以及
$H_P=\log F_P$ 的 $H_P''(0)=-x(P)$，准确给
\[
\big[\log U_P\big]_{\text{总次数 }2}
      =-x(P)\left(zw+\frac{w^2}{2}\right).
\tag{18b}
\]
因此再固定这个真实二阶 jet，$c_{11},c_{02}$ 也都为零，
完整正式解即唯一。对参考 $T=(0,0)$，(18b) 为零，
所以已证的 $D_{1,T}$、$U_T(z,0)=1$ 和二阶 jet 为零
唯一重建原公共参考的全部正式系数。

这是同一实际 Frobenius 方程的严格唯一性，
没有用一个可任意更改的局部模型代替原 theta。
但 $D_{1,P}$ 含 $\Psi_{-p}$，随 $p$ 改变；
有限的解歧义本身不等于指定中央行已经由一个固定维线性
Frobenius 矩阵算出，也没有给该行的非零性。

## 5. 固定有理覆盖上的整比值

置
\[
\mathcal R_P=U_P/U_T=\Theta_P/\Theta_T.
\tag{19}
\]
前篇已证
\[
\mathcal R_P(z,w)
=\left(\frac{B_P(z+w)}{B_P(z)}\right)^{1/N}
\in\mathcal O[[Z_1,Z_2]]^\times,\qquad
\mathcal R_P(Z_1,0)=1.
\]
其共同 $[N]\times[N]$ 拉回为
\[
\mathcal R_P(Nz,Nw)=\frac{A_P(z+w)}{A_P(z)}
\in F(E\times E).
\tag{20}
\]
这个固定覆盖在所有目标 $p$ 都 étale，且与真实 $\Phi$ 交换。

将 (10) 除以 $T$ 的同一式，得到
\[
\boxed{\quad
\mathcal F^r(\mathcal R_P)
=\mathcal R_P^{q^r}C_{r,P},\qquad
C_{r,P}=
\frac{D_{r,P}}{D_{r,T}}
=\frac{\Psi_{a_r}(P+z+w)\Psi_{a_r}(T+z)}
       {\Psi_{a_r}(P+z)\Psi_{a_r}(T+z+w)}.
\quad}
\tag{21}
\]
特别
\[
C_{r,P}\in1+p\mathcal O[[Z_1,Z_2]] .
\]
公共 $J_{a_r}$ 在 (21) 准确相消；
但恢复原 theta 时仍须保留已单独控制的 $D_{r,T}$。
(21) 本身是固定有理 cover 上所有标签的完整乘法 Frobenius 约束，
不是仅有 first vertical jet 的关系。

## 6. 原 256 项相加后的准确 Witt 交叉项

令
\[
\mathcal A(z,w)=\sum_{P\in\mathcal S}\mathcal R_P(z,w),\qquad
\mathcal A(Z_1,0)=256.
\tag{22}
\]
由于 $\sigma^{2r}$ 固定 $K$ 并置换原 $\mathcal S$，
\[
\mathcal F^r(\mathcal A)=\mathcal A\circ\Phi^r .
\]
把每一项 (21) 相加。写
\[
E_{r,P}=(C_{r,P}-1)/p\in\mathcal O[[Z_1,Z_2]].
\]
对任意 $p$ 幂 $Q$ 定义整数多项式
\[
\mathfrak C_Q(X_1,\ldots,X_{256})
=\frac{(X_1+\cdots+X_{256})^Q-\sum_jX_j^Q}{p}
       \in\mathbb Z[X_1,\ldots,X_{256}].
\tag{23}
\]
其整性来自特征 $p$ 的 $p$ 次幂可加性。
那么原轨道的完整等式是
\[
\boxed{\quad
\frac{\mathcal A\circ\Phi^r-\mathcal A^{q^r}}p
=\sum_{P\in\mathcal S}\mathcal R_P^{q^r}E_{r,P}
 -\mathfrak C_{q^r}\big((\mathcal R_P)_{P\in\mathcal S}\big).
\quad}
\tag{24}
\]
这里所有项都在同一个整正式环中；
经固定 $[N]\times[N]$ 拉回后，还都是由同一固定有理
$\mathcal A$ 和准确 division corrections 给出的恒等式。

(24) 是原和的公式，不能把最后一项删掉或改成
$\sum\log\mathcal R_P$。
它包括原 $256$ 个标签的所有非线性交叉数据。

### 6.1 第一层和第二层的差别可以准确量化

设 $S_1=\sum X_j$、$S_p=\sum X_j^p$，
并记 $\mathfrak C_p=(S_1^p-S_p)/p$。
直接展开 $(S_p+p\mathfrak C_p)^p$ 给
\[
\boxed{\quad
\mathfrak C_{p^2}(X)
\equiv
\mathfrak C_p(X_1^p,\ldots,X_{256}^p)
 +p S_p^{p-1}\mathfrak C_p(X)
              \pmod{p^2}.
\quad}
\tag{25}
\]
证明：一次项是 $pS_p^{p-1}\mathfrak C_p$；
其余二次至 $p$ 次项的系数在除过一次 $p$ 后仍被 $p^2$ 整除，
这里 $p\ge3$ 足够。

特别
\[
\mathfrak C_{p^2}(X)\equiv\mathfrak C_p(X)^p\pmod p.
\]
一般由同样归纳得到
\[
\boxed{\quad
\mathfrak C_{p^{2r}}(X)
 \equiv\mathfrak C_p(X)^{p^{2r-1}}\pmod p.
\quad}
\tag{26}
\]
因此在整形式群参数中，交叉项第一层的非零单项式指数
都是 $p^{2r-1}$ 的倍数。
这可以合法消去某些第一层 mixed coefficient；
但 (25) 显示第二层已有
$pS_p^{p-1}\mathfrak C_p(X)$，没有同样的指数限制。
而 $\mathfrak C_p(X_1^p,\ldots)$ 自身在模 $p^2$ 下
也不能简单换成 $\mathfrak C_p(X)^p$。

这正是应保留的 Witt carry，不是一个可忽略的常数。
例如其在所有 $X_j=1$ 的值已经包含
$(256^{p^{2r}}-256)/p$；
不过这个值在 (24) 两侧的常数项准确相消，
不能独立当成原中央非消失的来源。

## 7. 保留参考后，完整原对角的接口是什么

原 theta 和准确恢复为
\[
\sum_{P\in\mathcal S}U_P=U_T\mathcal A.
\]
所以所有层都满足
\[
\boxed{\quad
\left(\sum_PU_P\right)\circ\Phi^r
 =U_T^{q^r}D_{r,T}
    \left\{\mathcal A^{q^r}
      +p\sum_P\mathcal R_P^{q^r}E_{r,P}
      -p\,\mathfrak C_{q^r}((\mathcal R_P)_P)\right\}.
\quad}
\tag{27}
\]
左侧的系数 Frobenius可省略，是因原和在 $K$ 上且
$\sigma^{2r}$ 固定 $K$；单个 $U_P$ 仍必须使用 (10) 的 $\sigma^{2r}$。

再用完全准确的
\[
\sum_P U_P(z,w)
=Z(w)\left(\frac{256}{w}+\mathscr K(z,w)\right)
\tag{28}
\]
及 $d_m=[z^mw^m]\mathscr K$，便得到原中央对角的所有系数约束。
如果使用前篇的固定 rational cover，
则同一式的目标系数是
\[
N^{2m+1}d_m
=[z^mw^m]\left\{
N\Theta_T(Nz,Nw)\sum_P\frac{A_P(z+w)}{A_P(z)}
      -\frac{256}{w}\right\}.
\tag{29}
\]
从整 $Z_1,Z_2$ 坐标转回加法 $z,w$ 的形式对数及其分母必须保留，
不能仅凭 (26) 的整坐标指数限制就宣布 (29) 的第二层为零或非零。

(10)、(18)、(21)、(24)、(27) 给出的都是完整形式关系。
它们没有停在一个投影或一个模 $p$ first jet 上；
公共参考、有限角色、逐标签幂及原和的交叉项都已具体确定。
但其中 $\Psi_{(-p)^r}$ 的程度及目标 jet 阶随 $p,r$ 增长，
而 (27) 不是一个可直接引用的固定维线性 Frobenius 矩阵。

目前还没有从这些准确约束推出原中央导数的无穷次非零。
可继续研究的具体量是：
原参考 $D_{r,T}$ 与 (25) 的第二层 carry，
是否在 (29) 的真实对角和既定中央零阶下还有可计算的非零余项。
不能用固定 norm 常数的非零对数替代这个比较。

## 8. 证明来源与范围

- 原 $F_P,\Theta_P,d_m$ 和 torsion Galois 相容性：
  [固定原 theta 对角](2026-11-12-anticyclotomic-theta-diagonal.md)，
  §§1–3；Bannai–Kobayashi (2010)，
  *Algebraic theta functions and the p-adic interpolation of
  Eisenstein–Kronecker numbers*，Example1.9、§1.3 式(15)、Theorem1.17，
  [作者原文](https://arxiv.org/pdf/math/0610163)。
- 同一个 $[N]$ cover、原 $B_P,A_P$、所有好位整根：
  [前篇完整证明](2026-11-12-translated-kummer-units-and-original-theta-cover.md)。
- 真实 $[-p]$ 与 $\sigma^2$ 在 prime-to-$p$ torsion 上的规范：
  [全部同源 norm](2026-11-12-all-isogeny-neighbors-kummer-norms.md)，§5；
  本文 §1 又以点数和特征多项式核定。
- (6)–(29) 的 sigma、除子、整模型和整数多项式计算均在本文给出。
  特别没有援用仅对 ordinary primes 成立的 theta 整性命题，
  没有把 $U_T$ 本身写成已知整单位，也没有省略真实形式群坐标的换元。

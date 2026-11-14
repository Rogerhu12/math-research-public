# R275 — 原十七核的三阶 CM jets、十六维 Hermite 投影与真实加权伴随成本

日期：2026-11-13。**状态：以下完整局部 jets、整 Hermite 投影、原三来源的真实 theta 部分式及固定阶伴随所需的 Frobenius 零因子均已证明。尚未把这些固定挠点投影等同于原完整中央导数。**

沿用 R270/R274 的普通 $p=4r+1\ge13$、$p\ne17$、
$\pi b_0=p$、$R(U)=\sigma(\pi z)/\sigma(z)^p$；
固定 $\beta=4-i$、$K=K_\beta$，其中
$$
K(U)=\beta U^4+(-12+20i)U^3+(28+10i)U^2+(-20-12i)U-i.
\tag{1}
$$

## 1. 完整 CM 互反的局部正规化

对非零 $P\in E_0[\beta]$，置
$$
c_P=r_\beta'(P),\qquad
H_P(w)=\log\left(\frac{r_\beta(P+w)}{c_Pw}\right),\qquad
s(w)=\log\frac{\sigma(w)}w.
\tag{2}
$$
$H_P$ 为常数零的形式级数，所有系数为固定代数数。
记 $h_{P,k}=H_P^{(k)}(0)$。$c_P$ 是 R270 的固定十七单位；
在当前素位是单位。此处形式 $\log$ 只作用于常数一的级数，不选择新的 $p$ 次根。

R270 的完整有理恒等式
$$
r_\beta(z)^p r_\pi(\beta z)
=r_\pi(z)^{17}r_\beta(\pi z)
$$
在 $z=P+w$ 除以常数、零极首项后，准确给
$$
\boxed{
17\bigl(\log r_\pi(P+w)-\log r_\pi(P)\bigr)
=pH_P(w)-H_{[\pi]P}(\pi w)
 +s(\pi\beta w)-p\,s(\beta w).
}
\tag{3}
$$
其中差的对数可等价写为
$\log(r_\pi(P+w)/r_\pi(P))$；右边没有未定常数或自动因子。

**证明。** 用
$$
r_\beta(P+w)=c_Pw\,e^{H_P(w)},\qquad
r_\pi(q)=\pi q^{1-p}e^{s(\pi q)-ps(q)}
$$
逐项代入，再用 R270(31) 的准确常数
$r_\pi(P)^{17}=\beta^{1-p}c_P^p/c_{[\pi]P}$ 消去首项，即得 (3)。
这些指数只是常数一形式级数恒等式。$\square$

因此，对所有 $k\ge1$ 有全 jet 公式
$$
\boxed{
17(\log r_\pi)^{(k)}(P)
=ph_{P,k}-\pi^kh_{[\pi]P,k}
 +\beta^k(\pi^k-p)s^{(k)}(0).
}
\tag{4}
$$
平方格 sigma 满足
$$
s(w)=-w^4/60+O(w^8).
$$
故前三阶没有原点 carry：
$$
\boxed{
17(\log r_\pi)^{(k)}(P)
=ph_{P,k}-\pi^kh_{[\pi]P,k},
\qquad k=1,2,3.
}
\tag{5}
$$
第四阶首次留下准确原点项
$$
\boxed{
17(\log r_\pi)^{(4)}(P)
=ph_{P,4}-\pi^4h_{[\pi]P,4}
-\frac25\beta^4(\pi^4-p).
}
\tag{6}
$$
这里的 $-2/5$ 是原 sigma 的四阶系数，不能以局部常数的规范变化删除。

## 2. 所有固定局部系数均有显式有理式

为避免以“可求导”隐藏输入，写 $f_j=r_\beta^{(j)}(P)$、$f_1=c_P$。
前三个正规化 jet 为
$$
\begin{aligned}
h_{P,1}&=\frac{f_2}{2f_1},\\
h_{P,2}&=\frac{f_3}{3f_1}-\frac{f_2^2}{4f_1^2},\\
h_{P,3}&=\frac{f_4}{4f_1}
 -\frac{f_2f_3}{2f_1^2}+\frac{f_2^3}{4f_1^3}.
\end{aligned}
\tag{7}
$$
这些式子由 $\log(1+aw+bw^2+cw^3+\cdots)$ 直接展开。

令 $\kappa=x(P)^2$，并记
$$
A_P=4x(P)y(P),\quad
B_P=4x(P)(5\kappa-3),\quad
C_P=24y(P)(5\kappa-1),
$$
$$
D_P=24(35\kappa^2-28\kappa+1).
\tag{8}
$$
它们分别为 $U_z,U_{zz},U_{zzz},U_{zzzz}$ 在 $P$ 的值。于是
$$
\begin{aligned}
f_1&=A_PK'(\kappa),\\
f_2&=A_P^2K''(\kappa)+B_PK'(\kappa),\\
f_3&=A_P^3K'''(\kappa)+3A_PB_PK''(\kappa)+C_PK'(\kappa),\\
f_4&=A_P^4K''''(\kappa)+6A_P^2B_PK'''(\kappa)\\
&\hspace{10mm}+(3B_P^2+4A_PC_P)K''(\kappa)+D_PK'(\kappa).
\end{aligned}
\tag{9}
$$
全部来自 $x'=2y$、$y'=3x^2-1$，无需数值选择挠点。

特别地，对 $\log r_\pi/p$ 的 $z$ jets，(5) 等价于
$$
\begin{aligned}
17\,p^{-1}(\log r_\pi)'(P)
 &=h_{P,1}-b_0^{-1}h_{[\pi]P,1},\\
17\,p^{-1}(\log r_\pi)''(P)
 &=h_{P,2}-p b_0^{-2}h_{[\pi]P,2},\\
17\,p^{-1}(\log r_\pi)'''(P)
 &=h_{P,3}-p^2b_0^{-3}h_{[\pi]P,3}.
\end{aligned}
\tag{10}
$$
**第一 jet 的 Frobenius 置换项仍为单位阶**；不能把它与第二、第三 jet 一起忽略。

## 3. 在 $K^4$ 上的完整整 Hermite 投影

现在把 $R$ 的自变量写为 $v$，令
$$
L_p(v)=p^{-1}\log R(v)\in\mathcal O\langle v\rangle.
$$
在 $\kappa=x(P)^2$ 处，其零阶值由 R270 的准确互反给出：
$$
17pL_p(\kappa)
=(1-p)\log_p\beta+p\log_pc_P-\log_pc_{[\pi]P}.
\tag{11}
$$
令 $G_k=p^{-1}(\log r_\pi)^{(k)}(P)$，其中 $k=1,2,3$ 由 (10) 给出。
链式法则得到真正的 $v$ jets：
$$
\boxed{
\begin{aligned}
L_p'(\kappa)&=G_1/A_P,\\
L_p''(\kappa)&=(G_2-B_PG_1/A_P)/A_P^2,\\
L_p'''(\kappa)&=
\bigl(G_3-3B_PG_2/A_P
 +(3B_P^2/A_P^2-C_P/A_P)G_1\bigr)/A_P^3.
\end{aligned}}
\tag{12}
$$
$P\mapsto iP$ 时各 $z$ jet 与 $A_P,B_P,C_P$ 的相位准确相消，
所以 (11)–(12) 只依赖四元轨道参数 $\kappa$。
当前素位上 $A_P$ 为单位，所有 jets 整。

由于 $K$ 首系数和判别式均为单位，存在唯一
$$
\boxed{
J_p(v)\in\mathcal O[v]_{<16},\qquad
L_p-J_p\in K^4\mathcal O\langle v\rangle.
}
\tag{13}
$$
这是真实十六维 Hermite 投影。其全部输入就是 (7)–(12)：
四个固定对数值和十二个明确的代数 jet，不含额外未知函数。

一个不需要巨大系数表的构造如下。写
$$
J_p=I_0+KI_1+K^2I_2+K^3I_3,\qquad \deg I_j<4.
$$
先由 (11) 唯一插值 $I_0$。随后在 $K=0$ 的四维代数中依次解
$$
\begin{aligned}
K'I_1&=L_p'-I_0',\\
2(K')^2I_2&=L_p''-I_0''-K''I_1-2K'I_1',\\
6(K')^3I_3&=L_p'''-I_0'''-K'''I_1
 -3K''I_1'-3K'I_1''\\
&\hspace{13mm}-6K'K''I_2-6(K')^2I_2'.
\end{aligned}
\tag{14}
$$
每个 $I_j$ 取次数小于四的代表。
所有求逆因子是 $2,3,K'$，均为单位，故这是整的固定矩阵运算。

### 3.1 一个确切的十六维残数配对

对次数小于十六的多项式 $P$ 定义
$$
\mathcal H_P(L_p)
=\sum_{K(\kappa)=0}\operatorname{Res}_{v=\kappa}
 \frac{P(v)L_p(v)}{K(v)^4}\,dv.
\tag{15}
$$
这里各点仅用原解析局部展开；不把 $L_p$ 当作全局有理函数。
它准确等于把 $L_p$ 换成 (13) 的 $J_p$ 后的同一和。

记
$$
c_1=\frac{K''(\kappa)}{2K'(\kappa)},\quad
c_2=\frac{K'''(\kappa)}{6K'(\kappa)},\quad
c_3=\frac{K''''(\kappa)}{24K'(\kappa)}.
$$
若 $F=PL_p$，单点残数是
$$
\boxed{
\frac1{K'(\kappa)^4}
\left\{
\frac{F'''(\kappa)}6-2c_1F''(\kappa)
 +(10c_1^2-4c_2)F'(\kappa)
 +(-20c_1^3+20c_1c_2-4c_3)F(\kappa)
\right\}.
}
\tag{16}
$$
因此它是 (11)–(12) 的完整显式线性组合。

在 $\mathcal O[v]/K^4$ 上，(15) 给出的 residue 配对为整完美配对。
证明可将两个输入换为次数小于十六的多项式，
再用无穷点的 Laurent 系数：按 $1,v,\ldots,v^{15}$，
反对角首项为 $1/\beta^4$，为单位。
这说明全部十六个方向确实可被这些有限残数观测。
它没有说明原中央泛函就是这个 residue 配对。

## 4. 原三来源的正确四层部分式及第十七方向

沿用 R270 的 $Q_A,Q_B,Q_H$，它们次数均为十六，最高系数分别为
$1,-1,-1/55$。在 $v=x^{-2}$ 中，R248 的**真实 theta** division 是
$$
\frac{\vartheta(\beta z)}{\vartheta(z)^{17}}=iK(v).
$$
因此
$$
\boxed{
\vartheta(\beta z)^4=\vartheta(z)^{68}K(v)^4.
}
\tag{17}
$$
这与反序 sigma division 不同：
若 $k_\sigma(v)=v^4K(1/v)$，则
$$
\sigma(\beta z)^4=v\,\vartheta(z)^{68}k_\sigma(v)^4.
\tag{18}
$$
不能将 (18) 的商冒充 (17) 的 theta frame。
$\vartheta(\beta z)^4$ 是四次幂；本篇不因 $\vartheta$ 的秩零参考性质而
把这个四次幂的 Mellin 变换视为已知秩零单位。

对 $i=A,B,H$ 唯一作固定多项式除法
$$
\boxed{
\frac{Q_i(v)}{K(v)^4}
=c_i+\sum_{j=1}^4\frac{N_{i,j}(v)}{K(v)^j},
\qquad \deg N_{i,j}<4,
}
\tag{19}
$$
其中
$$
(c_A,c_B,c_H)=\beta^{-4}(1,-1,-1/55).
\tag{20}
$$
四层分子完全固定：将 $Q_i-c_iK^4$ 反复除以 $K$，
其 $K$ 进制第 $4-j$ 位就是 $N_{i,j}$。这给出每个系数的有限精确算法，
所有分母只来自固定 $\beta$、$5$、$11$ 和 Gaussian 整数。

原来源因而准确为
$$
\begin{aligned}
S_A&=\vartheta(\beta z)^4
 \left(c_A+\sum_{j=1}^4N_{A,j}/K^j\right),\\
S_B&=\vartheta(\beta z)^4
 \left(c_B+\sum_{j=1}^4N_{B,j}/K^j\right),\\
S_H&=\vartheta(\beta z)^4\sqrt{1-v}
 \left(c_H+\sum_{j=1}^4N_{H,j}/K^j\right).
\end{aligned}
\tag{21}
$$
第三条的 $\sqrt{1-v}$ 必须保留；它只在 R270 的实际 Lagrange Jacobian 中相消。
特别地，第三条常商并不是单独的 $\vartheta(\beta z)^4$ 方向。

在合法的原常数线性组合 $S_A+S_B$ 中，(20) 的 frame 常商准确抵消，
所以 $Q_A+Q_B$ 次数至多十五，完全落在 (19) 的 proper 部分。
若原 $A,B$ 完整中央零，则该和的完整中央零也成立。
对 $H$ 用 $1/\sqrt{1-v}$ 作类似消去却是**非恒定来源乘法**，
原三中央零不自动控制它。

在有限 residue 配对 (15) 中，次数十六的 $K^4$ 方向被杀掉：
它的局部 integrand 为 $L_p\,dv$，在各根处正则。
原完整 Mellin 中这个方向可能具有非零质量，故比较时必须另付原点和该方向的完整边界。

## 5. 为什么此时不能对 theta 指数作固定根求值

$L_p$ 在闭单位圆盘整，并不意味着
$$
R(v)^{-68/p}=\exp(-68L_p(v))
$$
可在 $K(v)=0$ 的点上按 $p$-adic 指数求值。
(11) 只给 $L_p(\kappa)\in\mathcal O$；它可能是单位。
此时指数不在通常的收敛圆盘内。
R270 的原来源只使用次数至多 $3r<p$ 的**形式截断**，
其中阶乘已逐项支付；这不足以授权全局求值。

(13) 是除法**对数**的 Hermite 投影。
若把原有限系数中的指数直接投到它上面，
就额外引入了未支付的 $p$ 次 Kummer 分支。
本篇不作这个扩张，也不将其算作免费的有限 theta 来源。

## 6. 原权密度的真正 formal adjoint 及不可省的零因子

本节的根处阶数和不解性结论均指特征零中准确成立的有理伴随恒等式；
它们不排除模 $p^k$ 的近似伴随或低次数截断消去。
特别是 R274 的次数至多 $r$ 范围内 $L_p\equiv\ell_r\pmod{p^3}$ 仍可用于原有限系数。

下面直接在原有限系数上作分部积分，不假设上述指数可在固定根处求值。
对第一 principal 权，原公共密度是形式 Laurent 函数
$$
\boxed{
\rho_p(v)=
\frac{R(v)^{p-68/p}E(v)^{-p}}
 {v^{r+1}\sqrt{1-v}},\qquad E=R^*/\pi.
}
\tag{22}
$$
因此 R270 的三个有限系数准确为
$$
B_{A,1}=\operatorname{Res}_0\rho_pQ_A\,dv,\quad
B_{B,1}=\operatorname{Res}_0\rho_pQ_B\,dv,\quad
B_{H,1}=\operatorname{Res}_0\rho_p\sqrt{1-v}\,Q_H\,dv.
\tag{23}
$$
其真正对数导数为
$$
\boxed{
\frac{\rho_p'}{\rho_p}
=(p^2-68)L_p'-p\,\frac{E'}E
 +\frac1{2(1-v)}-\frac{r+1}v.
}
\tag{24}
$$
特别地 reciprocal 项 $-pE'/E$ 并未消失。

若 $\mathcal P=\sum_{j=0}^k a_j(v)\partial_v^j$ 为固定阶算子，
其相对于此原密度的 formal adjoint 是
$$
\boxed{
\mathcal P_{\rho_p}^*X
=\rho_p^{-1}\sum_{j=0}^k(-\partial_v)^j
 (a_j\rho_pX).
}
\tag{25}
$$
直接用形式 Laurent 系数分部积分，得到准确恒等式
$$
\operatorname{Res}_0\rho_pX\,\mathcal P(Y)\,dv
=\operatorname{Res}_0\rho_pY\,\mathcal P_{\rho_p}^*X\,dv.
\tag{26}
$$
这适用于所有使各系数有定义的原形式级数；不需要固定根处的指数。

**定理 2。** 设 $k=1,2,3$、$p>k$。
假设 $\mathcal P$ 的系数在 $R,R^*$ 的所有根处正则，
且最高系数 $a_k$ 在那里为单位。
若有理函数 $X$ 的加权伴随输出 $\mathcal P_{\rho_p}^*X$
在这些根处都正则，则 $X$ 在每个 $R$ 根及每个 $R^*$ 根至少有 $k$ 阶零。
特别地，若 $X$ 的分母只在固定 $0,1,\beta$ 根及无穷点有极，
则它的分子必须含
$$
\boxed{(RR^*)^k,}
\tag{27}
$$
其次数为 $2kr$。

**证明。** $R$ 的根为非零 $\pi$ 核的四元轨道；$R^*$ 的根为这些轨道的倒数，
对应其 $T_0=(0,0)$ 平移。
两组各有 $r$ 个简单根，互不相交：否则
$T_0$ 属于奇数阶的 $\pi$ 核。
它们也不在 $0,1$ 或非零 $\beta$ 核中。
这都是原 good-characteristic-zero 椭圆曲线上的准确除子事实。

在一个 $R$ 根处，$\rho_p$ 的局部指数是
$$
\lambda=p-68/p\notin\mathbb Z,
$$
因为 $p\ne2,17$。若 $m=\operatorname{ord}X$，
(25) 的最高阶局部项为非零单位乘
$$
(m+\lambda)(m+\lambda-1)\cdots(m+\lambda-k+1)\,t^{m-k}.
$$
所有因子均非零；较低阶项的阶严格较高。
因此输出正则迫 $m\ge k$。

在 $R^*$ 的根处，$\rho_p$ 的指数是 $-p$。
若 $m<k$，同一乘积为
$(m-p)(m-p-1)\cdots(m-p-k+1)$，因 $p>k$ 而非零，
仍产生负阶项。故这里也必须 $m\ge k$。
两组根互异，得到 (27)。$\square$

这一定理直接适用于 R274 的二阶
$\mathcal D=16v(1-v)\partial^2+(12-20v)\partial$
及同类最高系数仅在固定 $0,1,\beta$ 根消失的三阶算子。
对 $H$ 可在 $\sqrt{1-v}$ 的真实二次覆盖上应用同一局部证明：
这些 Frobenius 根均非分歧点，阶数结论不变。

所以，用一个固定次数、只在固定十七根有极的 primitive，
不能把 (23) 的 reciprocal 和原 theta 权全部分部积分掉。
二阶、三阶分别至少要求 $4r$、$6r$ 次的实际零因子。
若允许随 $p$ 的乘子，或使用本身在这些根有极的连接系数，
仍可继续研究，但必须把这份次数、极和完整来源成本列入。


### 6.1 对原二阶算子的一个实际不解性结论

对 $\mathcal P=\mathcal D$，还可把上面的次数成本变成直接的原来源结论。
若 $X$ 为非零有理函数，记 $m=\deg_\infty X$（分子次数减分母次数）。
在无穷点，(22) 的指数为
$$
\kappa_\infty=-r-\frac{37}{2}+\frac{17}{p}.
$$
由 (25) 直接比较最高项，
$$
\mathcal D_{\rho_p}^*X
=\bigl[-4(m+\kappa_\infty+1)(4m+4\kappa_\infty+3)\bigr]
 \operatorname{lc}_\infty(X)v^m+\cdots.
\tag{28}
$$
方括号不为零：若任一因子为零，整数 $m,r$ 会迫 $p\mid68$，
与当前 $p\ge13,\ p\ne17$ 矛盾。
故原二阶加权伴随**准确保持无穷阶 $m$**。

因此，若 $X$ 的分母次数至多十六，极只在固定 $0,1,\beta$ 根，
而输出是次数至多十六的多项式，那么 (27) 迫
$$
m\ge4r-16.
$$
对所有 $p=4r+1\ge41$，右边大于十六，与 (28) 矛盾。
特别地，在这个明确的原四层极空间中，不存在把非零 $Q_A$、
$Q_B$ 或合法的 $Q_A+Q_B$ 写成 $\mathcal D_{\rho_p}^*X$ 的 primitive。
即使允许 $X$ 的系数随 $p$ 改变，这个结论也成立。
它只排除此处列出的原二阶／极次数条件；没有排除带已付新极或更大返回成本的来源恒等式。

本篇给出了可用于后续比较的全十六维 jets 和原 formal adjoint，
同时明确了它与原第十七来源方向、原点边界及第一 Frobenius 商层的准确关系。
没有将有限残数的完美观测误写成原完整中央导数的非零。


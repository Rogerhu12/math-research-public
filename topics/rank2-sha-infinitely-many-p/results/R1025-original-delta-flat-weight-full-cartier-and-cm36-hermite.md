# R1025 — 原 δ 平坦权的全 Cartier 表、固定36 cover 与四槽曲率返回

日期：2026-11-27 UTC。**已证明。** 对 R1022 的实际增长根权，
本篇给其导数权在全部六个 $H\bmod6$ 上的完整 Cartier 返回。
在真正使用的 $H\equiv5$ 情形，三个中间方向返回零，而
两条原 old 方向都返回显示的非零微分，系数在全部目标素数上为单位。
证明包含全部二挠留数、原点与其余支撑，不是一个核点或数值样本。

随后给固定36 cover 上的显式 Hermite 原函数。
乘回原 $P_{10}$ 时不删连接：其整个曲率项落在一个实际四维空间，
四个系数由原指定多项式的四个显示槽读取。
仍含 $GP_{10}$ 的项及原外部测试权全部保留；
裸权非零不被当作 canonical 中央非零。

## 1. 原模型、范围与半线性规范

固定
$$
E:y^2=x^3+1,\quad X=x^3,\quad
\omega_E=\frac{dx}{2y}=\frac{dy}{3x^2},\quad D=d/dz,
\qquad u=\frac xy.
\tag{1}
$$
令 $p=6s-1>13^4$。先允许全部整数
$$
11\le H\le s.
\tag{2}
$$
实际应用再取 R1018/R1022 的
$$
H=6q+5,\qquad r=s-H\in\{0,1,2,3,4,5\},
\qquad p=36q+29+6r.
\tag{3}
$$

$\mathcal C$ 始终是 $p^{-1}$-线性的 Cartier。
表中有理常数、二项式和原
$$
c_p=\binom{3s-1}{2s-1}\in\mathbf F_p^\times
$$
均已约化在 $\mathbf F_p$，所以其 $p$ 次根就是自身。
但本篇若乘上原 $c_*$、$C_3^{10}$、Gauss 根或其它固定扩域常数，
仍须取该常数真正的 $p$ 次根。
例如 $\delta^{1/p}=-\delta$；不能将它误当 $\mathbf F_p$ 常数。

以下使用的五个 rational parts 为
$$
Q=X+1,\qquad U_A=y(X+4),\qquad U_B=xy,\qquad
V_c=x^2(X+c),\quad c=-8,\ 10.
\tag{4}
$$
它们分别来自 R1021 的 $q,u_A,u_B,\Psi,\Psi_{00}$，
这里没有把 $\sigma^{10}$ 混进裸权定义。
记
$$
\mathcal T_H(F)=\mathcal C(u^HF\omega_E).
\tag{5}
$$

## 2. 整个输出空间与所有可能支撑

$u$ 的零是 $O,(0,1),(0,-1)$，各一阶；
其极是三个非零二挠点 $\mathcal D_2=\{(e,0):e^3=-1\}$，
各一阶。
(2) 保证 (5) 的五个输入在 $O$ 及其余点正则，
极只在 $\mathcal D_2$，各阶严格小于 $p$。

所以第一次 Cartier 后各极至多简单，且其留数是原留数的
$p$ 次根。完整输出属于
$$
\boxed{
H^0(E,\Omega_E(\mathcal D_2))
=\langle\omega_E,\ \omega_E/y,\ x\omega_E/y\rangle.
}
\tag{6}
$$
令 $\zeta=-\omega$ 为原六次单位。
三个基的几何特征依次为 $\zeta,\zeta^4,\zeta^2$。
$u$ 的特征为 $\zeta$，而 $Q,U_A,U_B,V_c$ 的特征依次为
$1,\zeta^3,\zeta,\zeta^2$。
Cartier 把特征换为其 $p$ 次根，即其逆。
因此 (6) 与全部留数已确定非全纯输出；只在输入型五时
还需真实的全纯系数，下一节也将其支付。

在 $Q_e=(e,0)$ 使用原参数 $y$。
这里
$$
x=e(1-y^2)^{1/3},\qquad
e^{1/p}=e^{-1},\qquad e^{2/p}=e^{-2}=-e.
\tag{7}
$$
两个带极基的准确留数是
$$
\operatorname{Res}_{Q_e}(\omega_E/y)=-e/3,\qquad
\operatorname{Res}_{Q_e}(x\omega_E/y)=-e^2/3.
\tag{8}
$$
(7)–(8) 固定了下面每一个符号。

## 3. 全部六个 H 剩余类的完整返回

对相应奇偶的 $H$ 定义
$$
Q_H=(-1)^{(H-3)/2}
 \binom{(H-2)/3}{(H-3)/2}\qquad(H\text{ 奇}),
$$
$$
A_H=(-1)^{(H-2)/2}
\left\{3\binom{(H-2)/3}{(H-2)/2}
-\binom{(H-2)/3}{(H-4)/2}\right\}\qquad(H\text{ 偶}),
$$
$$
B_H=(-1)^{(H-2)/2}
 \binom{(H-1)/3}{(H-2)/2}\qquad(H\text{ 偶}),
$$
$$
C_{H,c}=(-1)^{(H-1)/2}
\left\{(c-1)\binom{H/3}{(H-1)/2}
-\binom{H/3}{(H-3)/2}\right\}\qquad(H\text{ 奇}).
\tag{9}
$$
广义二项式是有限乘积，所有阶数小于 $p$，
按原有理数约化，不使用 Gamma 近似。

为指定全纯系数，置
$$
\mathfrak b(a,b)=(-1)^{a+b}
\frac{\prod_{j=0}^{a-1}(6j+4)}
     {\prod_{j=0}^{a-1}(6j+7)}
\frac{\prod_{\ell=1}^{b}(7+6a-6\ell)}
     {\prod_{\ell=1}^{b}(6\ell-3)}
\quad(a,b\ge0),
\tag{10}
$$
空乘积为一，并写
$$
\begin{aligned}
M_q&=\mathfrak b(2q+1,3q+1),\\
N_q&=\mathfrak b(2q+1,3q)+4\mathfrak b(2q,3q),\\
P_q(c)&=\mathfrak b(2q+2,3q+1)+c\mathfrak b(2q+1,3q+1).
\end{aligned}
\tag{11}
$$
下表每行写 $H=6q+h$，不是把不同剩余类的 $q$ 混用。

| $h$ | $\mathcal T_H(Q)$ | $\mathcal T_H(U_A)$ | $\mathcal T_H(U_B)$ | $\mathcal T_H(V_c)$ |
|---:|---|---|---|---|
| 0 | $0$ | $-A_Hx\omega_E/y$ | $-B_H\omega_E/y$ | $0$ |
| 1 | $-Q_H\omega_E/y$ | $c_pN_q\omega_E$ | $0$ | $C_{H,c}x\omega_E/y$ |
| 2 | $0$ | $0$ | $B_Hx\omega_E/y$ | $c_pP_q(c)\omega_E$ |
| 3 | $Q_Hx\omega_E/y$ | $0$ | $c_pM_q\omega_E$ | $0$ |
| 4 | $c_pM_q\omega_E$ | $A_H\omega_E/y$ | $0$ | $0$ |
| 5 | $0$ | $0$ | $0$ | $-C_{H,c}\omega_E/y$ |

这是整个函数域里的表，不是只在二挠点的主部表。
某些显示系数确可为零，例如 $H=13,c=-8$ 的 $C_{H,c}$；
本篇没有把所有剩余类的每个非空格都泛称为单位。

### 3.1 全部留数的直接证明

按 (1) 用 $y$ 作参数，四种输入依次是
$$
\begin{aligned}
u^HQ\omega_E&=\tfrac13x^{H-2}y^{2-H}dy,\\
u^HU_A\omega_E&=\tfrac13x^{H-2}y^{1-H}(y^2+3)dy,\\
u^HU_B\omega_E&=\tfrac13x^{H-1}y^{1-H}dy,\\
u^HV_c\omega_E&=\tfrac13x^Hy^{-H}(y^2+c-1)dy.
\end{aligned}
\tag{12}
$$
将 (7) 逐项代入，$y^{-1}dy$ 的系数分别给 (9)。
偶数幂不产生留数；三个二挠点的相同留数还须由总留数定理为零，
这支付表中的相应整行零。
(7) 的半线性以及 (8) 则给所有显示的带极输出。
(6) 的 CM 特征排除另加一个未经确定的全纯项。

### 3.2 表中全部全纯项的完整支付

原指定模型的
$$
DG=-x+c_pZ^{p-1},\qquad DZ=1
$$
直接给
$$
\boxed{\mathcal C(x\omega_E)=c_p\omega_E.}
\tag{13}
$$
没有在这里以一个自由 primitive 替换原 $Z,G$。

对任意本表所需 $a,b$，直接微分得
$$
D\left(\frac{x^2yX^a}{(X+1)^b}\right)
=\frac{xX^a}{(X+1)^b}
\{(7+6a-6b)X+(4+6a)\}.
\tag{14}
$$
结合 $X+1$ 的恒等式，逐次减去这些显示的 exact 微分，
把
$xX^a(X+1)^{-b}\omega_E$
减到 $\mathfrak b(a,b)x\omega_E$。
具体递推为
$$
\mathfrak b(a,b)
=-\frac{7+6a-6b}{6b-3}\mathfrak b(a,b-1),\qquad
\mathfrak b(a+1,0)
=-\frac{6a+4}{6a+7}\mathfrak b(a,0).
$$
这就是 (10)，并给原函数，而非仅一个维数论断。
本表所需 $a,b$ 使各显示分母的绝对值小于 $p$ 且非零，
因为 $H\le(p+1)/6$；全部递推在原特征 $p$ 中合法。
最后施 (13)，正好给 (11) 和表中的四种全纯格。

## 4. 真正 H≡5 的统一非零与两个 old 权

现在固定 (3)，令
$$
n=(H-1)/2,\qquad
\boxed{\mathscr B_H=(-1)^n\binom{H/3}{n}\in\mathbf F_p^\times.}
\tag{15}
$$
单位证明是完整有限乘积：
二项式的分子是 $H,H-3,\ldots,H-3(n-1)$，
最小值为 $(9-H)/2$，最大值为 $H$。
它们的绝对值都小于 $p$；
又 $H\equiv2\bmod3$，没有一个为零。
$3^n n!$ 也是单位。

(9) 的相邻二项式比给整个返回
$$
\boxed{
\mathcal T_H(V_{-8})
=6\mathscr B_H\frac{13-H}{9-H}\frac{\omega_E}{y},
}
\tag{16}
$$
$$
\boxed{
\mathcal T_H(V_{10})
=12\mathscr B_H\frac{H-7}{9-H}\frac{\omega_E}{y}.
}
\tag{17}
$$
$9-H,13-H,H-7$ 都不是零，绝对值小于 $p$：
$H\equiv5\bmod6$ 排除这三个等号。
所以 (16)–(17) 在所有本篇目标素数均非零。
同时，表的最后一行完整地给
$$
\boxed{
\mathcal T_H(Q)=\mathcal T_H(U_A)=\mathcal T_H(U_B)=0.
}
\tag{18}
$$

对 R1021(9) 和 R1018(16) 的两个原 old 权，线性性给
$$
\boxed{
\mathcal T_H(4V_{-8}+5V_{10})
=36\mathscr B_H\frac{H-3}{9-H}\frac{\omega_E}{y},
}
\tag{19}
$$
$$
\boxed{
\mathcal T_H(65V_{-8}+61V_{10})
=18\mathscr B_H\frac{19H-3}{9-H}\frac{\omega_E}{y}.
}
\tag{20}
$$
这两项也均非零。最后一个可能费用由 (3) 精确核为
$$
19H-3\equiv(1-114r)/6\pmod p.
$$
$r=0,\ldots,5$，显示整数的绝对值至多569，
而 $p>13^4$。因此它确为单位，不需要素数扫描。

这些式子对任意整个 $p$ 次外权仍准确：
$\mathcal C(A^pu^HF\omega_E)=A\mathcal T_H(F)$。
若外权不是 $p$ 次幂，本篇不作同样提出。

## 5. 固定36 cover、真正非零的全纯响应

取固定曲线
$$
\boxed{\mathcal C_{36}:\ t^6=x/y,\qquad
t^{36}=X^2/(X+1)^3.}
\tag{21}
$$
这里 $\mathcal C_{36}$ 是曲线名，不是 Cartier 算子。
它在 $X=0,-1,\infty$ 的分歧指数分别为18、12、36，
点数分别为2、3、1。Riemann–Hurwitz 给属16。
它还是 Fermat36 的明确商：
若 $U^{36}+V^{36}=1$，则
$$
X=U^{36}/V^{36},\quad t=U^2V,\quad
x=(U/V)^{12},\quad y=V^{-18}.
$$
所有后继运算都在这一个固定 cover 上，不随 $p$ 增加分歧次数。

写
$$
\beta_r=t^{1-6r}\omega_E
=\frac16t^{7-6r}\frac{dX}{X}.
\tag{22}
$$
由 $6H=p+1-6r$，
$$
u^H\omega_E=t^p\beta_r.
$$
因此 (16)–(20) 的准确响应分别是在原系数后再乘
$$
\boxed{\gamma=\frac{\omega_E}{ty}.}
\tag{23}
$$
$\gamma$ 是全局非零全纯微分。
更精确地，cover 到 $E$ 在 $O,\pm(0,1)$ 和三个二挠点
均全分歧六次，$\omega_E$ 的拉回在各点阶五。
故
$$
\boxed{\operatorname{div}\gamma
=22\widetilde O+4\widetilde{(0,1)}+4\widetilde{(0,-1)}.}
\tag{24}
$$
三个二挠点上阶为零，总次数30，恰为 $2g-2$。
所以此处的非零不仅是某个局部留数。

由 R1022(22) 的实际二项式权及 R1018 的完整导数式，
$
DW_\delta=12(q+1)\binom{3q+2}{q}u^H.
$
这里 $3q+2<p$，故显示系数为单位；以 $v=X/(X+1)$ 直接微分也得到同式。
因此
$\mathcal C(\beta_r)=0$ 也完整成立。
它只涉及该显示微分；不能因此推出
$\mathcal C(P_{10}\beta_r)=0$。

## 6. 两个 old 权的全部固定 Hermite 原函数

置
$$
b=7-6r,\quad a=b+12=19-6r,\quad k=a/36,\quad
D_k=(1-k)(2-k),\quad
\Omega_a=t^a\,dX/X.
$$
有
$$
d(t^aR)=t^a
\left\{XR'+k\frac{2-X}{X+1}R\right\}\frac{dX}{X}.
\tag{25}
$$
定义全部固定有理函数
$$
R_-=(X+1)
\left\{\frac X{2-k}+\frac{5(k-3)}{D_k}\right\},
\qquad
R_+=(X+1)
\left\{\frac X{2-k}+\frac{21-13k}{D_k}\right\},
$$
$$
c_-=-\frac{2(3k-1)(3k-8)}{D_k},\qquad
c_+=\frac{4(3k-1)(3k-5)}{D_k}.
\tag{26}
$$
逐代 (25)，得到整个 differential 身份
$$
\boxed{
\beta_rV_{-8}
=\frac16\{c_-\Omega_a+d(t^aR_-)\},\qquad
\beta_rV_{10}
=\frac16\{c_+\Omega_a+d(t^aR_+)\}.
}
\tag{27}
$$
这里用 $x^2=t^{12}(X+1)$。
不是只给一个未指定的 de Rham 比例。

对两旧权 $A=4V_{-8}+5V_{10}$、
$B=65V_{-8}+61V_{10}$，其系数和原函数准确为
$$
c_A=-\frac{36(3k-1)}{2-k},\qquad
R_A=\frac{9(X+1)(X+5)}{2-k},
$$
$$
c_B=\frac{18(3k-1)(19k-10)}{D_k},\qquad
R_B=18(X+1)
\left\{\frac{7X}{2-k}+\frac{17-26k}{D_k}\right\}.
\tag{28}
$$
因此
$$
\lambda_r=\frac{c_B}{c_A}
=\frac{19k-10}{2(k-1)}
=\frac{114r-1}{2(17+6r)}
$$
给真正的 exact 差
$$
\boxed{
\beta_r(B-\lambda_rA)
=\frac16d\{t^a(R_B-\lambda_rR_A)\}.
}
\tag{29}
$$
六个 $r$ 的所有显示分母都是固定好位单位。
与 (19)–(20) 比较，比例完全一致。

### 6.1 exact 差的原函数再压成一个实际中间方向

(28) 的两个完整原函数不仅给抽象 exact。
利用 $t^{18}=X/(y(X+1))$，逐项有
$
t^aR_A=\frac{9t^{1-6r}}{2-k}\left(U_A-\frac4y\right),
$
$
t^aR_B=\frac{18t^{1-6r}}{D_k}
\left\{7(1-k)U_A+9(k-2)y+\frac{19k-10}{y}\right\}.
$
代入 (29) 的实际 $\lambda_r$，$1/y$ 项完整相消，得到
$
\boxed{
t^a(R_B-\lambda_rR_A)
=\frac{81}{2(1-k)}\,t^{1-6r}Xy
=\frac{81}{2(1-k)}\,t^{1-6r}x^2U_B.
}
\tag{29a}
$
因此同一个 exact 差更准确地为
$
\boxed{
\beta_r(B-\lambda_rA)
=\frac{27}{4(1-k)}\,d\{t^{1-6r}x^2U_B\}.
}
\tag{29b}
$
这也可不经 Hermite 系数而直接核：
$D(Xy)=9x^5+6x^2$，且
$D\log t=(2y/x-3x^2/y)/6$。

(29a) 将 (31) 中这一个组合的剩余 $GP_{10}F$ 压到显示单项；
没有把该项赋零。原 dyadic 补项仍严格是
$
x^2U_B=Xy=(U_A+2U_C)/3.
\tag{29c}
$
所以 $\Pi_{2,0}$ 取 $U_A/3$，$\Pi_{2,1}$ 仍取 $2U_C/3$。
若把它代回 R1021 的 whole 字，还须保原十三 profile 和
所有位移；特别不能把不同点的 $x^2$ 与某个 Miller 分母先行约去。

## 7. 乘回 P10 后保留的完整项

仍取 R887/R1018 的原
$$
DP_{10}=10GP_{10}+10(\mathcal H Z)^pZ^9,\qquad \mathcal H=G+x^2/y.
\tag{30}
$$
若 (27) 的一行写成
$\beta_rV=(c\Omega_a+dF)/6$，则乘积法则与
Cartier 杀全导数给完整公式
$$
\boxed{\begin{aligned}
\mathcal C(P_{10}\beta_rV)
={}&\frac c6\,\mathcal C(P_{10}\Omega_a)
-\frac{10}{6}\mathcal C(GP_{10}F\omega_E)\\
&-\frac{10}{6}\mathcal H Z\,
       \mathcal C(FZ^9\omega_E).
\end{aligned}}
\tag{31}
$$
各显示有理常数在 $\mathbf F_p$ 中；
若整行另乘扩域常数，按 §1 取其真正 $p$ 次根。

特别，将 (29) 乘 $P_{10}$ 后，右端不再是可删除的 exact：
其全部 $GP_{10}$ 项和最后曲率项正由 (31) 返回。
这明确保留了原 P10 commutator。

### 7.1 整个曲率项的四个实际系数

最后一项并非一个未指定的大空间。
令
$$
m=(p-1)/2,\qquad
A_m(X)=\frac12\sum_{j=0}^m
\binom mj\frac{X^j}{3j+1}.
$$
这是 R887 原 $\mathscr R_p(x)/x$，全部分母在本篇惯性素数为单位。
同一个原 $Z$ 准确为
$$
Z=t^6\frac{A_m(X)}{(X+1)^m}.
\tag{32}
$$
对任意本节 $F=t^aR(X)$，其中 $R$ 是 (26)、(28) 的显示二次多项式，
置
$$
e=15q+10+3r,\qquad
\mathcal N_R(X)=
X^{2q+5}R(X)A_m(X)^9(X+1)^e.
\tag{33}
$$
整个曲率 Cartier 准确等于
$$
\boxed{
\mathcal C(FZ^9\omega_E)
=\frac{t^{-1}}{6(X+1)^5}
\sum_{j=0}^3
\left([X^{(j+1)p-1}]\mathcal N_R\right)X^j\,dX.
}
\tag{34}
$$
四个系数都是原显示有限多项式的真实系数，
在 $\mathbf F_p$ 中；没有四个自由参数或新选的初值。

完整证明只需两条指数恒等式：
$$
t^{a+60}=(t^{-1})^p
\left(\frac{X^2}{(X+1)^3}\right)^{q+3},
\qquad
5p-(9m+3q+9)=e.
$$
由 $\omega_E=t^6dX/(6X)$，左输入因此恰为
$$
\frac16\left(\frac{t^{-1}}{(X+1)^5}\right)^p
\mathcal N_R(X)\,dX.
$$
对 $\mathbf P^1_X$ 的 Cartier 提取 $(j+1)p-1$ 次数即得 (34)。
而
$$
\deg\mathcal N_R\le5p-q-2<5p-1,
$$
所以不存在遗漏的第五槽或无穷高尾。
这也证明整个最后曲率系数落在同一固定四维空间
$$
\boxed{
t^{-1}(X+1)^{-5}\,\mathbf F_p[X]_{\le3}\,dX.
}
\tag{35}
$$

(31)–(35) 消费了一个真实 $P_{10}$ 曲率部分，
但未删除 (31) 中仍在的 $GP_{10}F$，
也没有将原外部三字／十三字测试权从乘积内提出。
当外权为整个 $p$ 次幂时，可按 §4 的准确规则提出；
其它外权须保其原乘积和相应导数。

## 8. 与当前原中央 forcing 的准确关系

R1021 的 $4/5$ 与 R1018 的 $65/61$ 是本篇 (19)–(20)
实际读取的两个 old 权。
R1021 的源端行列式 $-81$、(29) 的固定 Hermite 差、
(34) 的四个实际曲率槽现在都可在同一原函数域中使用。

原 R1020 的读者却作用于完整 $P_{10}$ 测试、单 primitive、
原点留数和全部低窗返回。
因此不能用 (18) 替换该读者，不能把 (19) 的非零直接写成
某条 canonical Schur 余式非零。
尤其原末四个非 diagonal 余数的二阶极、原 $O$ 留数、
$Z$ 的指定低项与 $\mathcal H$ 全因子仍须完整返回。

本篇所有新等式均由原有限式、全部极／留数与显示 polynomial
identity 手证；没有新的数学执行、素数扫描或生成数据文件。

依赖：R887 原 $Z,G,P_{10}$ 与 $DG$；
R1018 同深度及原第四阶完整曲率；
R1020 唯一 primitive 与全低窗；
R1021 原中间函数及两旧权；
R1022 原 $\delta$ 平坦权、三字和39纤维全精度返回。

## 9. 同一个原曲率在有理 $y$ 线上，以及九阶极的准确有限和

继续取 (3) 的 $H=6q+5$、$r=s-H$，不更换原 $P_{10},G,Z$。
置
$$
\begin{aligned}
V_-&=x^2(X-8),\qquad V_+=x^2(X+10),\\
W_r&=2(41+6r)V_-+(77+6r)V_+,\\
F_H&=(x/y)^H Xy
=\frac{x^2X^{2q+2}}{(X+1)^{3q+2}} .
\end{aligned}
\tag{36}
$$
本节的 $W_r$ 是此显示的两个 old 函数之组合，不是 R1022 的平坦权。

直接用 $Dx=2y,Dy=3x^2$ 及
$H\equiv1/6-r\bmod p$ 得完整恒等
$$
\boxed{DF_H=\frac1{18}(x/y)^H W_r.}
\tag{37}
$$
也可由 §6.1 的 fixed-cover exact 式乘 $t^p$ 得到；
$D(t^p)=0$，所以没有新的导数项。
由 (30) 和乘积法则，(37) 的真正同点 $P_{10}$ 返回为
$$
\boxed{\begin{aligned}
\mathcal C\bigl(P_{10}(x/y)^H W_r\omega_E\bigr)
={}&-180\,\mathcal C(GP_{10}F_H\omega_E)\\
&-180\,\mathcal H Z\,\mathcal C(F_HZ^9\omega_E).
\end{aligned}}
\tag{38}
$$
这里的全部系数属于 $\mathbf F_p$；
其它固定扩域常数仍按 §1 的半线性规则取根。

### 9.1 完整原函数只在三个原二挠点有极

因为 $dy=3x^2\omega_E$ 且 $H+1=6q+6$，准确有
$$
\boxed{
F_H\omega_E
=\frac13 (y^2-1)^{2q+2}y^{-6q-4}\,dy
=d\mathscr R_H(y),
}
\tag{39}
$$
其中取完整的有理函数
$$
\boxed{
\mathscr R_H(y)=
\frac13\sum_{j=0}^{2q+2}
\frac{(-1)^j\binom{2q+2}{j}}
     {2j-6q-3}\,
y^{\,2j-6q-3}.
}
\tag{40}
$$
这不是只在某一点选的 primitive。
所有显示分母都是非零奇整数，绝对值至多 $H-2<p$，
所以在全部目标素数处是单位。
本篇 $q\ge1$，故所有指数都负；
$\mathscr R_H$ 在无穷远取零，没有增加自由常数。
它在每个非零二挠点极阶恰为 $H-2$，
在 $O$ 阶恰为 $H-8$，没有其它极。

由完整导数 $d(Z^9\mathscr R_H)$ 及 $dZ=\omega_E$，得
$$
\boxed{
\mathcal C(F_HZ^9\omega_E)
=-9\,\mathcal C(Z^8\mathscr R_H\omega_E).
}
\tag{41}
$$
这一步保留的是同一个原 $Z$；没有以另一 primitive 替换它。

### 9.2 四槽中的最高极只需一个明确有限和

沿 (32)–(34)，定义
$$
\begin{aligned}
e&=15q+10+3r,\\
N_H(X)&=X^{2q+5}A_m(X)^9(X+1)^{e+2},\\
n_j&=[X^{(j+1)p-1}]N_H(X)\quad(0\le j\le3).
\end{aligned}
\tag{42}
$$
在 (34) 中取 $R=(X+1)^2$，再乘其准确的外部 $t$，
即得原 $E$ 上的整个返回
$$
\boxed{
\mathcal C(F_HZ^9\omega_E)
=\frac{x^2}{y^9}\sum_{j=0}^3n_jX^j\,\omega_E
=\frac1{3y^9}\sum_{j=0}^3n_j(y^2-1)^j\,dy .
}
\tag{43}
$$
因此它本身也降到有理 $y$ 线上；不是仅有一个局部主部公式。
所有四槽仍是 (42) 的实际值。

令 $n=3q+1$，并置
$$
\boxed{
S_H=
\sum_{j=0}^{2q+2}
\frac{(-1)^j\binom{2q+2}{j}}
     {2j-6q-3}\,
\frac{(2/3)_{\,n-j}}{(n-j)!}
\quad\in\mathbf F_p .
}
\tag{44}
$$
这里 $n-j$ 的范围为 $q-1,\ldots,3q+1$，均非负且小于 $p$。
全部分母已付为单位；$S_H$ 是一个确定有限和，没有新增自由参数。

在 $Q=(\epsilon,0)$、$\epsilon^3=-1$，原分支
$x=\epsilon(1-y^2)^{1/3}$ 和 (40) 给
$$
\operatorname{Res}_{Q}(\mathscr R_H\omega_E)
=\frac{\epsilon^{-2}}9 S_H .
\tag{45}
$$
原 R887(5) 的准确式为
$Z=\epsilon\rho_p y^{-p}+\text{正则奇函数}$。
因为 $\mathscr R_H\omega_E$ 在该点极阶 $H-2<p$，
(41) 的九阶极只能来自 $Z^8$ 的完整最高项；
含至多七个 $y^{-p}$ 因子的其它项极阶严格小于 $8p+1$。
Cartier 的半线性给这个九阶系数
$$
-9\left((\epsilon\rho_p)^8
           \frac{\epsilon^{-2}}9S_H\right)^{1/p}
=-\rho_p^8 S_H .
\tag{46}
$$
最后一步使用 $\epsilon^6=1$、
$\rho_p,S_H\in\mathbf F_p$；
没有漏掉扩域系数的 Frobenius 逆。

与整个式 (43) 的 $y^{-9}dy$ 系数比较，得到准确的四槽约束
$$
\boxed{
\sum_{j=0}^3(-1)^j n_j=-3\rho_p^8S_H.
}
\tag{47}
$$
因 $\rho_p$ 为单位，若 (44) 非零，则原完整曲率返回
在每个二挠点都确有九阶极。
本节尚未证明 (44) 对所有目标素数非零；
也不从该条件性的最高极判定推出 canonical 中央非零。

本节把 (38) 中原曲率部分压成完整有理 primitive、
同一四槽及一个明确的最高极有限和。
(38) 的 $GP_{10}F_H$ 和全部三字／十三字外权仍在。
若将本节用于原 R1020 reader，仍须在完整外部平移之后保留其
实际测试点、原 $P_{10}$、原点留数与全部低窗；
本节没有给任何平移、导数或乘积新增算术零。

## 10. 同一个有理 Beta 和严格非零及其显式检出深度

本节只给 §9 显示有限和的**有理提升本身**一个严格非零和
$p$ 进深度界；没有把模 $p$ Cartier 式自动提升到模 $p^H$。
所有原 $GP_{10}$、完整权和中央比较仍需按原账本消费。

沿原 $H=6q+5$，令
$$
N=3q+1=\frac{H-3}{2},\qquad A=2q+2.
$$
本篇范围有 $q\ge1$、$N-A=q-1\ge0$。
把 §9 同一个有理有限和记为
$$
\mathscr S=
\sum_{j=0}^{A}(-1)^j\binom Aj
\frac{(2/3)_{N-j}}{(N-j)!\,[2(N-j)+1]}.
\tag{48}
$$
定义同一个有限和的有理提升 $\widetilde S_H=-\mathscr S\in\mathbf Q$；由下节已付的单位分母，其模 $p$ 约化正是 §9 的 $S_H\in\mathbf F_p$。

### 10.1 原和是一个严格正矩

设 $B$ 的概率密度为
$$
\frac{x^{-1/3}(1-x)^{-2/3}}{\mathrm B(2/3,1/3)}
\quad(0<x<1),
$$
$U$ 独立且在 $(0,1)$ 上均匀，令 $V=BU^2$。
则完整 Beta 积分给
$$
\mathbb E[V^n]
=\frac{(2/3)_n}{n!\,(2n+1)}.
$$
所以有限和 (48) 严格等于
$$
\boxed{
\mathscr S
=\mathbb E\!\left[V^{N-A}(V-1)^A\right]
=\mathbb E\!\left[V^{q-1}(1-V)^{2q+2}\right].
}
\tag{49}
$$
$A$ 是偶数，且 $V$ 几乎处处位于 $(0,1)$。
故
$$
\boxed{0<\mathscr S<1,\qquad -1<\widetilde S_H<0.}
\tag{50}
$$
这里没有数值近似或未定号的抵消。

### 10.2 原有理分母与自给的最小公倍数界

设 $L_m=\operatorname{lcm}(1,\ldots,m)$。
(48) 的分母严格整除
$$
D=3^N N!\,L_{2N+1}.
\tag{51}
$$
这是因为每项的 $(2/3)_n/n!$ 分母除 $3^n n!$，
而 $2n+1\le2N+1$；原二项式都是整数。

以下给出所需的初等界
$$
\boxed{L_m\le4^{m-1}.}
\tag{52}
$$
逐素数幂比较可知
$$
L_{2n}\mid L_n\binom{2n}{n},\qquad
L_{2n+1}\mid L_{n+1}\binom{2n+1}{n}.
$$
证明整除只需看第一次超过 $n$ 或 $n+1$ 的素数幂：
它在相应二项式的 Legendre 赋值中贡献至少一；
该区间至多增加一次素数指数。其余幂已在相应较小的
$L_n$ 或 $L_{n+1}$ 中。
又
$\binom{2n}{n}\le4^n$，
$\binom{2n+1}{n}\le4^n$；后一式由两个相同的中央项
在总和 $2^{2n+1}$ 中各不超过一半取得。
从 $L_1=1$ 归纳，便得 (52)。

因此
$$
D\le48^N N!
\le[24(N+1)]^N.
\tag{53}
$$
第二步是对 $1,\ldots,N$ 使用算术—几何平均不等式。
原 $p=6s-1$、$H\le s$ 给
$p\ge6H-1=12N+17$，所以
$$
\boxed{D<(2p)^N.}
\tag{54}
$$
并且 $2N+1<p$、$p>3$，故 $p\nmid D$。

### 10.3 全部目标 p 的有理检出界

由 (50)–(51)，$D\mathscr S$ 是严格位于 $0$ 与 $D$ 之间的整数。
所以
$$
\boxed{
v_p(\widetilde S_H)=v_p(\mathscr S)
\le
\left\lfloor
N\left(1+\frac{\log2}{\log p}\right)
\right\rfloor
<2N=H-3.
}
\tag{55}
$$
当前 $p>13^4$ 已远强于这里需要的 $p>2$；
没有新增无限坏集，也没有依赖素数分布或数值扫描。
特别原有理 $\widetilde S_H$ 不是一个可任意设为零的边界参数，
而且其非零可在原线性长窗口以内检出。

(55) **不声称** $\widetilde S_H\bmod p$ 对每个目标素数都非零。
它也不将 §9 的特征 $p$ Cartier 最高极系数，
免费指定为某个更高精度中央行的有理提升。
若要用它与 canonical 坏素数假设矛盾，
还须从完整原 $GP_{10}$ 及全部权的消元中，
真实推出对 (48) 这个同一有理数的相应高精度整除。
本节支付的是严格正矩、完整分母和可用深度，
没有省略这项原读者相容性。


# R555 — 整个原角线性系与高接触首次 forcing 的非零范围

日期：2026-11-14。**状态：已证明。** 本篇将 R495 的十九角曲面用于整个原 $\mathcal W_D$，而非仅其三倍子格。全来源的准确除子类记为 $\mathcal B_D$。其与实际因子曲线 $C$ 的交数
$$
\nu_D(C)=\mathcal B_D\cdot C
$$
给同一原修正的分支零阶上界。与 R479 已付的单位 $-2$、单位 $5$ 联立，得到原完整首次 forcing 商中的真正非零判据，保留全部原列以及两条十三行 carry。

这些判据覆盖异常高接触范围。对 $\nu_D(C)=3C^2+O(D)$ 的候选，无 carry 干扰的值判据从 $h/C^2>3/2$ 起，小 $r$ 的导数判据从 $h/C^2>2$ 起；均不覆盖当前低 $\ell$ 临界的 $h/C^2\to9/8$。本文没有声称已找到实际深接触候选命中新门，也不把条件性排除误作主目标完成。

## 1. 原来源、真实因子与同一个修正

保
$$
p=6s-1>83,\qquad 1\le\ell<s-13,\qquad
f_D=\lfloor9D/2\rfloor+4<p,
$$
以及 R491 的同一来源
$$
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
$$
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
h_7=7+4t+16t^2,\quad d=1+8t,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
e_{n+1}=3\lceil3(n+1)/4\rceil+
2\lceil(n+1)/2\rceil+\lceil2(n+1)/3\rceil-2.
\tag{1}
$$
这里 $Y=\mathscr R$，原相对 Euler 算子是 $\mathcal E=Y\partial_Y$。

取同一实际真立方
$$
d^{C_D}\bar P=t^rF^3Q,\qquad
F(0,1)=0,\qquad F_Y(0,1)Q(0,1)\ne0,
\tag{2}
$$
$F$ 不可约。令
$$
b=\deg_YF,\quad
u=\max_i(\deg_tF_i-4i),\quad
h=\operatorname{ord}_w F(t(w),\bar g(w)),\quad
k=2h+r-s.
$$
本篇使用当前低 $\ell$ 窗
$$
\boxed{
1\le\ell\le r<h<s,\qquad
0\le k<\min(\ell,s-h,h).
}
\tag{3}
$$
特别 $k<r$。它保证 $\bar P\in\ker\bar J$，两条实际 carry 均可读。
$F$ 的正规分支是 $Y=\psi(t)$；$t(w)$ 为原整参数的单位倍。

R491 允许保持全部原角同时整提升因子，从而取真正的同预算基准
$$
P^{\rm fact}=d^{-C_D}t^r\widetilde F^3\widetilde Q\in\mathcal W_D.
\tag{4}
$$
因此任一实际首次提升都写为
$$
P^{(2)}=P^{\rm fact}+pR,\qquad R\in\mathcal W_D.
\tag{5}
$$
没有要求 $t^r\mid R$、$F\mid R$，也没有将仿射修正免费改成任意矩形。换回其他实际基准时，R491 的同格差及 $F^2$ 项保持下面的两个分支条件。

## 2. 整个原来源的十九角除子类

使用 R495 的同一曲面 $X$：从 $\mathbb F_4$ 作十九次普通吹起，
包括 $0,h_7$ 两根的三条四步链、$1$ 的三步链、
$d=0$ 的两步链和底无穷远的两步链。
所有中心均避开 $P=(0,1)$。
记 $S_0^2=-4$、$F_0$ 为底纤维，例外类用各步的**全变换**
$E_{\alpha,j}^*$；交数计算在这个正交例外基中进行。

置
$$
c_D=C_D,\qquad u_D=2c_D+4,\qquad
\mathcal V_D=d^{c_D}\mathcal W_D.
$$
原第 $n$ 列的准确固定角因子和最大系数次数是
$$
(th_7)^{A_n}(t-1)^{B_n}d^{c_D-C_n},
\qquad \deg_t R_n\le c_D+f_n,\quad
f_n=\lfloor9n/2\rfloor+4 .
\tag{6}
$$
所以其共同 $\mathbb F_4$ ambient 类为
$$
D S_0+(u_D+4D)F_0.
$$

定义全来源各链的累计最低值
$$
\begin{aligned}
V_j^{(4)}(D)&=D+\min_{0\le n\le D}(jA_n-n),&&1\le j\le4,\\
V_j^{(3)}(D)&=D+\min_{0\le n\le D}(jB_n-n),&&1\le j\le3,\\
V_j^{(d)}(D)&=\min_{0\le n\le D}\{j(c_D-C_n)+n\},&&j=1,2,\\
V_j^{(\infty)}(D)&=j u_D+
 \min_{0\le n\le D}\{-j(c_D+f_n)+(4j+1)n\},&&j=1,2.
\end{aligned}
\tag{7}
$$
取 $V_0=0$、$\mu_{\alpha,j}(D)=V_j-V_{j-1}$。三条四步链使用同一个第一行。

所有值均为明确的非负整数。为免留下未计算的最小式，在 $D\ge3$ 时准确为：

| 链 | 余类 | 各步 $\mu_{\alpha,j}(D)$ |
|---|---|---|
| 每条四步链，$D=4a+r$ | $r=0$ | $(a,a,a-1,a-1)$ |
| 同上 | $r=1$ | $(a,a,a,a-1)$ |
| 同上 | $r=2$ | $(a,a,a,a)$ |
| 同上 | $r=3$ | $(a+1,a,a,a)$ |
| 三步链，$D=3a+r$ | $r=0$ | $(a,a,a-1)$ |
| 同上 | $r=1$ | $(a,a,a)$ |
| 同上 | $r=2$ | $(a+1,a,a)$ |
| $d=0$ 两步链 | 全部 | $(c_D,c_D)$ |
| 无穷远两步链 | 全部 | $(c_D,c_D)$ |

例如后两行直接由
$n-2\lfloor n/2\rfloor\ge0$、
$n-\lfloor n/2\rfloor\ge0$ 得出。
前两类将 $n$ 分别模四、模三分组即可；$D\ge3$ 保表中所有项非负。
本篇 (2) 已有 $D\ge3b\ge3$。

定义固定除子类
$$
\boxed{
\mathcal B_D=
D S_0+(u_D+4D)F_0
-\sum_{\alpha,j}\mu_{\alpha,j}(D)E_{\alpha,j}^*.
}
\tag{8}
$$

**定理 1（全来源识别）。** 在原多项式平凡化中，
$$
\boxed{
H^0(X,\mathcal O_X(\mathcal B_D))
=\mathcal V_D=d^{c_D}\overline{\mathcal W}_D.
}
\tag{9}
$$
同一显示基在原整数环上有限自由，约化准确为 (9)。

**证明。** 每个原基列都满足 (7) 的全部累计下界。
对普通连续吹起，截面属于 (8) 恰要求其第 $j$ 个累计值至少为
$\sum_{i\le j}\mu_{\alpha,i}(D)=V_j(D)$；这一表述包括所有中间中心，
不会因某截面在前一中心多消失而漏掉后续条件。
ambient 次数也由 (6) 给出，故原格包含于左侧。

反向只需使用每条链的末条件。三条四步链的末累计值为 $D-2$，
三步链为 $D-1$，两个两步链为 $2c_D$。按 R495 的局部方程代入，它们准确给
$$
v_{0,h_7}(R)\ge-2,\quad v_1(R)\ge-1,\quad
v_d(R)\ge2c_D,\quad v_\infty(R)\ge-2c_D-8.
$$
最后一式使用 $2u_D=4c_D+8$。
这就是 R491 的原全部 Gauss 半空间，
逐系数等价于 (6) 的角整除和次数帽。
故没有新增截面。相同 monic Hensel 角因子和逐系数次数帽
给整数环上的显示自由基，约化核恰为 $p$ 倍。$\square$

直接交数还给
$$
\mathcal B_D^2=4D^2+2D u_D-\sum_{\alpha,j}\mu_{\alpha,j}(D)^2,
\qquad
\boxed{-K_X\mathcal B_D=2D+15.}
\tag{10}
$$
第二式用各链末值求和：
$2u_D+6D-3(D-2)-(D-1)-4c_D=2D+15$。
本篇不从来源自由或 (9) 推断物理像 $p$ 饱和。

## 3. 与原因子曲线的准确交数

$C$ 为 (2) 中 $F=0$ 在同一 $X$ 上的严格变换。
R495 支付其几何整性、$P$ 光滑和实际十九重数 $\mu_{\alpha,j}(F)$。
写
$$
\kappa=C^2,\qquad \chi=-K_XC.
$$
于是整个原来源在 $C$ 上的次数准确为
$$
\boxed{
\nu=\nu_D(C)=
4Db+D u+b u_D
-\sum_{\alpha,j}\mu_{\alpha,j}(D)\mu_{\alpha,j}(F).
}
\tag{11}
$$
这一式使用所有十九个中间重数，不是双次数矩形的结果式界。

(2) 是 (9) 中的一个真实截面。它的零除子在 $C$ 上恰有三重：
$Q(0,1)\ne0$ 保 $F\nmid Q$，$F$ 也不是角因子。
所以有准确有效余除子
$$
\boxed{
\mathcal B_D\sim3C+\Delta_P,\qquad
\Delta_P\ge0,\quad C\not\subset\operatorname{Supp}\Delta_P.
}
\tag{12}
$$
这里的 $\Delta_P$ 包括原角、无穷远和例外余量，不把它删除。
光滑面上不同有效曲线的交数非负，故
$$
\boxed{\nu=3\kappa+\delta_P,\qquad
\delta_P=C\cdot\Delta_P\ge0.}
\tag{13}
$$

**引理 2（全部原列的分支零阶帽）。**
对任意 $R\in\overline{\mathcal W}_D$：

1. 若 $F\nmid d^{c_D}R$，则
   $\operatorname{ord}_P R|_C\le\nu$。
2. 若 $F\mid d^{c_D}R$ 且 $(\mathcal ER)|_C\ne0$，则
   $\operatorname{ord}_P(\mathcal ER)|_C\le\nu-\kappa$。

**证明。** 第一项将 $d^{c_D}R$ 视为 (9) 的截面。
其在整曲线 $C$ 上的非零限制是一条次数为 $\nu$ 的线束截面。
在光滑点 $P$ 的零阶不超过总零长度；$d(P)=1$，所以除回原 $d$ 不改变阶。

第二项由整 Cartier 序列给
$d^{c_D}R=FH$，其中 $H\in H^0(X,\mathcal O_X(\mathcal B_D-C))$。
在 $C$ 上
$$
d^{c_D}(\mathcal ER)|_C=e\,H|_C,\qquad e=(\mathcal EF)|_C,
$$
因为 $\mathcal E d=0$。$e(P)$ 为单位。
因此 $H|_C$ 非零且在 $P$ 有同样零阶，
其线束次数是 $(\mathcal B_D-C)\cdot C=\nu-\kappa$。
这证明第二项；没有对 $\mathcal ER$ 自由指定另一份来源。$\square$

## 4. 原 M 的实际 forcing 商

保 R479 的整个目标
$$
\Gamma_L=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2),
\qquad L=2s+\ell.
$$
令 $\Delta=13$ 表示原 $M=c_*U_0m_{13}J$；
为同时记相对结果，$\Delta=0$ 表示 $J$。
置
$$
q_\Delta=s-\Delta,\qquad
\mathscr B_{2\Delta}
=w^{q_\Delta}k[w]_{<\Delta}
 \oplus\epsilon w^{q_\Delta}k[w]_{<\Delta}.
\tag{14}
$$
$\Delta=0$ 时此空间为零。
取真实首次商
$$
\beta=\overline{J(P^{\rm fact})/p}\in\bar\Gamma_L.
$$
它保 R502 的活 $V_1$，未另选 forcing。
实际商类为
$$
\boxed{
\beta_\Delta=[\beta]\in
\bar\Gamma_L/
\left(\bar J(\overline{\mathcal W}_D)+\mathscr B_{2\Delta}\right).
}
\tag{15}
$$
由 R479，$\beta_{13}=0$ 准确等价于 (2) 可在**同一原来源**
提升到 $M(P^{(2)})\in p^2\Gamma_{L+13}$。
$\beta_0=0$ 等价于相对 $J$ 的 $p^2$ 提升。
它们不等于原下一位 $d_2^J$ 或 $G_2$。

若 (15) 为零，必须有同一个 $R$ 和它的实际 carry 输出使
$$
\bar J R+\beta=w^{q_\Delta}B_0+
\epsilon w^{q_\Delta}B_1,\qquad \deg B_i<\Delta.
\tag{16}
$$
$B_i$ 并未作为独立来源添加。R479 的两条分支首项完整给：
$$
h+k<q_\Delta
\ \Longrightarrow\
\operatorname{ord}_P(\mathcal ER)|_C=h+k
\quad\text{且首系数为单位 }5\,C(0)u(0)^3/a;
\tag{17}
$$
$$
2h+k<q_\Delta
\ \Longrightarrow\
\operatorname{ord}_P R|_C=2h+k
\quad\text{且首系数为单位 }-2\,C(0)u(0)^4/(ae(0)).
\tag{18}
$$
其中 $a=p\kappa_{\rm Gauss}$、$u,C,e$ 均为原实际单位，
不是可调参数。第二个严格条件准确等价于
$r>2k+\Delta$。

还需要一个覆盖 carry 窗外的低阶零结论：
$$
\boxed{
\operatorname{ord}_P R|_C
\ge \min(q_\Delta,\,2h+k).
}
\tag{19}
$$
它不宣称边界处的单位 $-2$ 仍可见。

**(19) 的证明。** 记原 regularized Euler 值为 $R_i$。
由 (16) 和 R479 的全部首次商，在 (3) 的 $r>k$ 下有
$$
\operatorname{ord}R_0\ge q_\Delta,\quad
\operatorname{ord}R_1\ge\min(q_\Delta,h+k),\quad
\operatorname{ord}R_2\ge k .
$$
第三式只需原第三块的 $k+1$ 行，$k<\ell$ 保它真实存在。
把 $R$ 从 $g$ 展开到 $\psi$，差值阶为 $h$。
零、一次、二次项的阶分别至少
$q_\Delta$、$\min(h+q_\Delta,2h+k)$、$2h+k$；
三次及以上 Taylor 项至少为 $3h>2h+k$。
从 Euler 导数换成普通正规导数的额外项也不降低这些界。
所以得 (19)。全部读取均在原块长度内，未延长 $R_0,R_1$ 的已知截断。$\square$

## 5. 原首次类的两个严格非零判据

**定理 3（单位分支值给出的非零）。**
在 (1)–(4) 及同一真实曲面中，若
$$
\boxed{
r>2k+\Delta,\qquad 2h+k>\nu_D(C),
}
\tag{20}
$$
则 $\beta_\Delta\ne0$。
特别取 $\Delta=13$ 时，原 $\bar P$ 不属于
$K_2^{\rm red}(M)$，而非只是不属于相对 $K_2(J)$。

**证明。** 若为零，(18) 迫同一个 $R$ 的分支值非零，
零阶恰为 $2h+k$。引理2第一项又迫此阶不超过 $\nu$，
与 (20) 矛盾。$\square$

**定理 4（保 carry 的导数非零）。**
若
$$
\boxed{
h+k<q_\Delta,\qquad
\min(q_\Delta,2h+k)>\nu,\qquad
h+k>\nu-\kappa,
}
\tag{21}
$$
则同样 $\beta_\Delta\ne0$。
这里不要求 $r>2k+\Delta$。

**证明。** 若可提升，(19) 与引理2第一项迫
$F\mid d^{c_D}R$。但 (17) 给
$(\mathcal ER)|_C$ 的非零单位首项及准确零阶 $h+k$。
引理2第二项遂给 $h+k\le\nu-\kappa$，
与 (21) 矛盾。$\square$

两个定理比较的是整个 $\overline{\mathcal W}_D$，
因此 R552 中其余真实列的像不能再吸收这些类。
它们没有只证明 $F^2H_1$、$FH_2$ 或某个单独 tail 子空间上的非零。

## 6. 实际左证书如何从这个证明恢复

定理3不依赖抽象维数。令 $N=2h+k>\nu$。
在全来源上读取限制矩阵
$$
R\longmapsto [R|_C]_{\le N}.
$$
若其前 $\nu+1$ 个系数全零，引理2迫整个限制为零。
所以其第 $N$ 行是前 $\nu+1$ 行的一个实际线性组合。
于是存在行
$$
\lambda_N=[t^N]-\sum_{j=0}^{\nu}c_j[t^j]
$$
杀掉全部原来源限制，但在 (18) 的指定单位目标上取非零值。
$c_j$ 只需在这个有限原矩阵内求解，没有添加自由 normal 列。

设 $\zeta=\log(g/\psi)$，其阶为 $h$。
在 $N<3h$ 的准确长度内，
$$
R|_C=R_0-\zeta R_1+\tfrac12\zeta^2R_2
\pmod{t^{N+1}}.
\tag{22}
$$
这里 $R_0$ 只读至 $N<q_\Delta$，$R_1$ 只读至
$N-h=h+k<q_\Delta$，$R_2$ 只读至
$N-2h=k<\ell$。
所以 (22) 是原实际目标上的合法线性投影，
并杀掉全部 (14) 的 carry 行。
将 $\lambda_N$ 拉回，即得 (15) 的真正左证书；
它在 $\beta$ 上的非零由 (18) 的单位 $-2$ 支付。

$t$ 与 $w$ 的整单位换参只将这些行作单位三角变换。
恢复原 $M$ 时，继续完整运输 $c_*U_0m_{13}$，
不对 $m_{13}$ 作非整逆。
因此原 $P_{134}/U_0$、十三初始自由行、两条十三行 carry
和原 $U_1/p$ 都没有被删除。

定理4也有同一有限来源上的左证书：
先取全部值 jet 的实际核，(19) 与引理2使它成为 $F$ 倍数的子空间；
在此子空间上，次数 $\nu-\kappa$ 的第二界使指定导数首项不在像内。
将所得行通过同一值矩阵延拓回全来源即可。
这是对同一个 $R$ 的联合消元，不分别选择两份修正。

## 7. 准确适用范围及临界缺口

由 (13)，定理3的交数门是
$$
2h+k>3\kappa+\delta_P,\qquad \delta_P\ge0.
\tag{23}
$$
当 $k,\delta_P=O(D)$、$\kappa\asymp D^2$ 时，
其主阶为 $h/\kappa>3/2$。
还须原样保 $r>2k+13$ 才能用于整个原 $M$；
较小 $r$ 只能用 (21) 的完整条件，不能继续读取已跨边界的 $-2$ 行。

定理4的导数门主阶是 $h/\kappa>2$
（当 $\delta_P,k=O(D)$），同时还须检查
$q_{13}>\nu$ 与另外显示的行长条件。
这些是准确的充分范围，不是对所有高 $b$ 候选的排除。

作为只核交数的固定校准，R495 的真实来源族在
$b=13,D=39$ 时有
$$
\kappa=688,\qquad\chi=30,\qquad
\mu^{(4)}(F)=(3,3,3,3),\quad
\mu^{(3)}(F)=(4,4,4),\quad
\mu^{(d)}(F)=\mu^{(\infty)}(F)=(6,6).
$$
原全格的相应重数为三份 $(10,9,9,9)$、
$(13,13,12)$ 及两份 $(19,19)$；$u=12,u_D=42$。
故 (11) 精确给
$$
\nu=4\cdot39\cdot13+39\cdot12+13\cdot42
-3(10+9+9+9)\cdot3
-(13+13+12)\cdot4-4\cdot19\cdot6
=2101,
$$
即 $\delta_P=37$。这只验证原角与交数，**该族未被证明有原 theta 深接触**，
不能由数值 $2101$ 声称已产生某个具体素数的非零 forcing。

在原低 $\ell$ 维数临界中，R495 已付
$h/\kappa\to9/8$。即使 $\delta_P=O(D)$，仍严格低于 (23) 的 $3/2$ 门。
因此本篇没有消掉 R552 的真实 $\alpha/\beta_0$ 与剩余列商；
它把异常高接触部分的指定类确实判为非零，
而临界的实际 forcing 相容仍须另证。

## 8. 完整算术与下一位保持

本篇没有给 $F,Q,R$ 或新增线性系赋中央零。
三条原完整中央继续使用 R303/R402/R469 的同一实际来源、
原 Gaussian 和完整通常 Selmer 比较。
这里的非零是 (15) 的原首次提升障碍，
不自动给一个原中央导数非零，更不直接证明无穷多个素数的 Sha 初级有限。

若候选没有被 (20)、(21) 排除，继续到下一位仍须保
R481 的同一个首次修正、原 $d_2^J\to G_2$、
R502 的活 $V_1$ 和 R552 的整个实际尾商。
没有从 $\mathcal B_D$ 的整来源识别推断评价像饱和，
也没有以本篇的交数上界替代真实中央基准。

# R361：原规范 theta 多项式的完整扭留数与线性损失单位块

日期：2026-11-13。**状态：已证明。** 本篇在 R356 指定的原规范连接模型上，将 R335 的整个角多项式、$P_{134}$ 及全部测试极保留。对每个原齐次基列，其完整扭留数有明确多项式表达和一个大单位子式；在原 $K=s-14$ 接触窗口中，单位块的列数至少为 $K-26a-156$，其中 $a$ 是相对来源次数。这里的 forcing 指标与来源次数始终分开。没有给不同次数或不同原提升核元素分别附加零条件，也没有删去原十三行。

## 1. 原连接及三个不同指标

沿 R342、R346、R356，取 $p=6s-1$、$b=17$、$p\nmid b$，
原 genus-two 覆盖及导子为
$$
C:y^2=v^6+b,\qquad x=v^2,\qquad
Dv=y/v,\quad Dy=3v^4,\quad D=d/dz.
\tag{1}
$$
实际测试点满足 $Z_p=0$，且 $v,y$ 均为单位。
在这些点，$Z_p$ 是模 $p$ 的真实局部参数，$DZ_p=1$。
R356 给同一原 Gaussian 规范的准确低 jet
$$
G_\kappa(P)=0,\qquad
G_\kappa=-\sum_{j=1}^{p-1}
       \frac{D^{j-1}x(P)}{j!}Z_p^j \pmod{Z_p^p}.
\tag{2}
$$
原规范之间的差为 $-\bar\delta_\kappa Z_p^p$，不影响本篇全部 $<p$ 极部。

本篇用 $a\ge0$ 表示相对来源次数，$j$ 表示该次数内的基列，
$n$ 表示 (8) 中的 forcing 指标。三者不能混同。
在一个测试点，以 R359 的积分规范定义
$$
h_{m,P}(Z)=\exp\left(m\int_0^Z G_\kappa\,dZ\right),
\qquad h_{m,P}(0)=1.
\tag{3}
$$
只使用 $<p$ 的系数，所以所有所需积分和指数分母均为单位。
这就是原 Serre 连接的正号 theta 因子；相对 grade $a$ 给 $m=34a$，
恢复公共 charge40 后给 $m=34(a+40)$。

这里使用的是 R356 已明确的有理连接模型及其原窗口；
不把原 theta 或整个有限矩阵宣布为全局有理函数。
R363 的同一模 $p^2$ 代表不改变 (2)，故下述模 $p$ 单位子式
对该精确提升也成立。

## 2. 整个 canonical 列事实上有多项式角权

置
$$
\alpha=\left\lfloor\frac{a+1}{4}\right\rfloor,\quad
\beta=\left\lfloor\frac{a+1}{3}\right\rfloor,\quad
\gamma=\lfloor a/2\rfloor,\quad
0\le j\le e_{a+1},
$$
$$
e_{a+1}=
3\left\lceil\frac{3(a+1)}4\right\rceil+
2\left\lceil\frac{a+1}2\right\rceil+
\left\lceil\frac{2(a+1)}3\right\rceil-2.
\tag{4}
$$
R335 的 $A=\rho\,t(t-1)h_7$、$\rho=\Theta^{17}(1+8t)$
及准确 $\kappa_*,Q_{a+1}$ 给整个原基
$$
\boxed{
C_{a+1,j}=\Theta^{17(a+40)}F_{a,j}(t),
\quad t=-b/v^6,
}
$$
$$
\boxed{
F_{a,j}(t)=P_{134}(t)\,
 t^{13+\alpha+j}(t-1)^{15+\beta}
 h_7(t)^{13+\alpha}(1+8t)^{23+a-\gamma}.
}
\tag{5}
$$
这是在同一原整格中的等式；没有只保 leading germ。
所有显示指数非负。因此相对表达中的分母在恢复公共 $G_0$ 后
已经被真实原乘子支付，不需把 $P_{134}$ 的坏根从测试点删除。

令
$$
m=34(a+40),\qquad e=13+\alpha+j,\qquad
J=198+\beta+2\alpha+a-\gamma.
\tag{6}
$$
于是 $\operatorname{ord}_{t=0}F_{a,j}=e$、
$\deg F_{a,j}=e+J$，且最低系数
$$
c_e=P_{134}(0)(-1)^{15+\beta}7^{13+\alpha}
\tag{7}
$$
为非零整数。以下除去有限个 $p\mid P_{134}(0)$；
R335 给 $P_{134}(0)=-3^4\cdot3159421$。
没有假设 $F_{a,j}$ 在所有测试点非零，那里可能的零仍完整进入 (5)。

## 3. 保留 theta 与全部角系数的实际局部权

原测试微分是
$$
\omega_{\boldsymbol q}
 =\left(\sum_{n=1}^Kq_nZ_p^{-6n}\right)d\log r,
\qquad K\le s-1.
\tag{8}
$$
在 (1) 的覆盖上，$d\log r=-6v\,dz$。
对 (5) 的完整来源，取局部权
$$
\boxed{
\mathcal H_{a,j,P}(Z)=
 h_{m,P}(Z)\left(\frac{v(P+Z)}{v(P)}\right)^m
                         F_{a,j}(t(P+Z)).
}
\tag{9}
$$
已把非零的固定 theta 纤维标量作为行单位归一；
没有除以 $F_{a,j}(t(P))$，故其所有真实零点仍在同一矩阵内。
因 $\Theta=\sigma^2v^2$，(9) 恰好保留原 sigma 连接、
全部 $v^m$ 因子和整个角多项式，而非一个可任意选择的权。

为计算 (9)，先允许任意整数 $m,A$。定义多项式
$A_n^{m,A}(\xi)$，$\xi=b/v(P)^6$，由
$$
[Z^{6n-1}]
 h_{m,P}(Z)\frac{v(P+Z)^{A+1}}{v(P)^A}
     =y(P)v(P)^{6n-3}A_n^{m,A}(\xi).
\tag{10}
$$
它满足
$$
\boxed{\deg A_n^{m,A}\le3n-1.}
\tag{11}
$$
所用系数只含不大于 $6n-1$ 的阶乘分母，故在当前范围均整。

这里有一个完整递推，不依赖有限素数拟合。
在有理函数环中加入变量 $g$，令
$$
\mathscr D_m=D-x\partial_g+mg.
$$
则 (10) 的左侧准确由
$$
\frac{v^{-A}}{(6n-1)!}
       \left.\mathscr D_m^{\,6n-1}(v^{A+1})\right|_{g=0}
\tag{12}
$$
给出。因为 (2) 在所用范围内满足 $DG_\kappa=-x$，
(12) 是同一个原局部连接的递推。

证明 (11) 可直接使用 R346 的恒等式
$$
D^2v^k=k(k+1)v^{k+2}+k(k-2)b\,v^{k-4}.
\tag{13}
$$
每两次原导数至多增加一次 $\xi$ 次数。
$h_m$ 的各系数是 $x,y,b$ 的加权多项式，一次项为零；
更精确地，$D^{2r}v^k=v^{k+2r}U_{r,k}(\xi)$，
$D^{2r+1}v^k=yv^{k+2r-2}V_{r,k}(\xi)$，两多项式次数都至多 $r$。
$h_q$ 在 $q$ 偶数时由 $b^c v^{q-6c}$ 组成，
在 $q$ 奇数时由 $yb^c v^{q-3-6c}$ 组成。
分别与余下的奇数/偶数阶导子相乘，次数上界为
$3n-1-q/2+\lfloor q/6\rfloor$ 或
$3n-(q+1)/2+\lfloor(q-3)/6\rfloor$，均不超过 $3n-1$。
因此将 $y^2=v^6+b$ 消去后，第 $6n-1$ 阶总是
$yv^{6n-3}$ 乘次数至多 $3n-1$ 的 $\xi$ 多项式。
(12) 同时保证所有相位和周期归一均来自原导子。

## 4. 低系数的精确 Laguerre 多项式

(10) 的常数项可在同一个普遍多项式中令 $b=0$ 取得。
此时 $v(Z)=v_0/(1-v_0Z)$，
$G=-v_0^2Z/(1-v_0Z)$，故
$$
h_m=(1-v_0Z)^m e^{mv_0Z}.
$$
因而
$$
\boxed{
A_n^{m,A}(0)
=[u^{6n-1}](1-u)^{m-A-1}e^{mu}.
}
\tag{14}
$$
这只是计算普遍系数的退化，不改变目标曲线 $b=17$。

对于 (9) 的一个角单项式 $t^d$，有 $A=m-6d$。
若 $d\ge1$，令 $r_d=6d-1\ge0$，则
$$
A_n^{m,m-6d}(0)
=\frac{m^{6n-1}}{(6n-1)!}\,
                 \mathcal P_{r_d,m}(6n-1),
$$
$$
\boxed{
\mathcal P_{r,m}(N)
=\sum_{\ell=0}^{r}
 (-1)^\ell\binom r\ell\,\frac{(N)_\ell}{m^\ell}.
}
\tag{15}
$$
$(N)_\ell=N(N-1)\cdots(N-\ell+1)$。
对 $p>r$、$p\nmid m$，这是次数准确为 $r$、
最高系数 $(-1)^r/m^r$ 为单位的原多项式。
因此至多 $r$ 个互异 forcing 指标 $n$ 使 (15) 非单位。
这里用的是有限域中多项式的根数界，不用模 $p$ 的实正性。

例如 sigma 部分 $A=0,n=1$ 的完整多项式是
$$
A_1^{m,0}(\xi)=
1-\frac{77m}{60}+\frac{7m^2}{24}
-\frac m{12}\xi+\frac78\xi^2.
\tag{16}
$$
$m=0$ 时恢复 R346 的 $1+7\xi^2/8$，
$m=1$ 时常数为 $1/5!$。此式由 (12) 的五次有限有理运算得到；
全文秩结论用的是 (11)、(14)、(15)，不是这个有限例子。

## 5. 全部角多项式进入同一个残数矩阵

写 (5) 的完整多项式为
$F(t)=\sum_{d=e}^{e+J}c_dt^d$。
由 (9)、(10)，不删除任何角系数便得到
$$
\boxed{
\operatorname{Res}_P(\mathcal H_{a,j,P}\omega_{\boldsymbol q})
=-6(Y/b)\xi^{e-K}\,
                  P_{\boldsymbol q}^{a,j}(\xi),
}
$$
$$
P_{\boldsymbol q}^{a,j}
=\sum_{n=1}^{K}q_nb^n\xi^{K-n}\widehat A_n^{a,j}(\xi),
\qquad
\widehat A_n^{a,j}
=\sum_{d=e}^{e+J}c_d(-1)^d\xi^{d-e}
                         A_n^{m,m-6d}(\xi).
\tag{17}
$$
这里 $Y/b=y/v^3$ 是 R346 同一个椭圆商坐标。
所有原周期归一已经包含在 (1)–(3) 的不变导子中。

由 (11)、(15)，
$$
\boxed{
\deg\widehat A_n^{a,j}\le J+3n-1,\qquad
\deg P_{\boldsymbol q}^{a,j}\le J+3K-1,
}
$$
$$
\boxed{
\widehat A_n^{a,j}(0)
=(-1)^e c_e
 \frac{m^{6n-1}}{(6n-1)!}\,
                    \mathcal P_{6e-1,m}(6n-1).
}
\tag{18}
$$
这些式子使用了全部 $P_{134}$，尤其没有将其根上的行删除。

原极代数仍是 R346 的完整有限 étale 代数
$\mathcal A=\mathcal O[\xi]/(\widetilde B_p)$，
$\deg B_p=3s-1$、$B_p(0)B_p(-1)\ne0$。
对 (17) 乘单位 $-b\xi^{K-e}/(6Y)$，再对原 $X,Y$ 的六次
étale 扩张取迹除以六，就得到原 $\mathcal A$ 中的多项式坐标。
在 genus-two 覆盖上多出的两分支也可用迹除以二返回。
这些归一均整，且没有除以 $F(t(P))$。

## 6. 完整原规范权的单位子式

**定理。** 固定一个实际原基列 $(a,j)$，令 $m,e,J$ 如 (6)。
假设
$$
p>m,\qquad p>6e-1,\qquad p\nmid P_{134}(0).
\tag{19}
$$
取
$$
K_0=\max\left(0,\min\left(K,\ s-1-\left\lfloor J/3\right\rfloor\right)\right).
\tag{20}
$$
则完整 (17) 的实际整残数矩阵具有一个至少
$$
\boxed{\max(0,K_0-(6e-1))}
\tag{21}
$$
阶的单位子式，其行列式模 $p$ 为明确的非零乘积。

**证明。** 先只取原列 $q_1,\ldots,q_{K_0}$，并按 $K_0$
使用 (17) 的单位归一。
若 $K_0>0$，(20) 给
$$
J+3K_0-1<3s-1=\deg B_p.
$$
因此没有多项式除以 $B_p$ 后回绕到低行的现象。
取系数行 $0,\ldots,K_0-1$、列按 forcing 指标倒序排列，
仍是三角矩阵，对角为
$$
(-1)^e c_e\,b^n
 \frac{m^{6n-1}}{(6n-1)!}\,
                   \mathcal P_{6e-1,m}(6n-1).
\tag{22}
$$
$1\le n\le K_0\le s-1$ 给互异的 $6n-1\bmod p$，且全部阶乘为单位。
由 (7)、(15)、(19)，只有至多 $6e-1$ 个对角项可能非单位。

同时选取其余对角所对应的行和列，子矩阵仍三角。
其行列式就是 (22) 中这些显示因子的乘积，模 $p$ 非零。
这给实际整矩阵中的单位子式和 (21)。
对任意与 (2) 同约化的原整连接提升，此子式仍为单位；
不需要将某个有限矩阵在所有精度重新猜定。$\square$

这里陈述的是一个真实单位块，不宣称剩余列已经落在它的像中。
整 Schur 消元可保留所有剩余列及全部测试点，不改写原 $p^2$ 配对。

## 7. 原全部次数上的统一线性损失

现在取 R342 的实际接触长度 $K=s-14$，并令 $0\le a\le D$。
充分而明确的统一范围为
$$
\boxed{p>34(D+40),\qquad p\nmid3159421.}
\tag{23}
$$
连同原 $p>7,p\nmid b$，它支付 (19) 的全部单位条件。
在这个范围内 (20) 的非零项实际为
$K_0=s-1-\lfloor J/3\rfloor<K$。
故 (21) 相对于原 $K$ 列的损失至多
$$
L_{a,j}=\left\lfloor J/3\right\rfloor+6e-14.
\tag{24}
$$
当 $j=e_{a+1}$ 时它最大。准确有
$$
\boxed{L_{a,j}\le26a+156.}
\tag{25}
$$
因此每个原齐次基列的完整连接权都给
$$
\boxed{\text{至少 }\max(0,K-26a-156)\text{ 个单位主元，}}
$$
$$
\boxed{\text{统一至少 }\max(0,K-26D-156)\text{ 个单位主元。}}
\tag{26}
$$

为完全支付 (25) 的 floor 边界，$a=0,\ldots,11$ 的准确最大损失依次为
$$
154,\ 178,\ 208,\ 221,\ 257,\ 276,\ 312,\ 325,\ 355,\ 380,\ 416,\ 423.
$$
减去 $26a$ 的最大值为一百五十六。
当 $a$ 增加十二时，$\alpha,\beta,\gamma$ 分别增加三、四、六，
$J$ 增加十六，最大 $e$ 增加五十。
所以 $L$ 只增加三百零五或三百零六，而 $26a$ 增加三百一十二。
这证明所有非负 $a$ 的 (25)，不是有限次数外推。
同一式子给 $6e-1\le27a+101<34(a+40)$，故 (23) 也确实支付
(19) 的第二个条件。

这比先丢弃至多一百三十七个坏角再作比较更具体：
全部坏角已在 (17) 中保留，代价来自整个角多项式的已知次数，
而不是假定那些点不与测试极相交。

## 8. 固定末指标的额外准确性

对固定的正整数 $m,r,c$，
$$
\mathcal P_{r,m}(-c)
=\sum_{\ell=0}^{r}\binom r\ell
              \frac{c(c+1)\cdots(c+\ell-1)}{m^\ell}>0
\tag{27}
$$
是一个确定的非零有理数。
因此当 $N=p-c\ge0$ 时，
$\mathcal P_{r,m}(N)\equiv\mathcal P_{r,m}(-c)\pmod p$，
除去这个显示有理数分子的有限素因子后，原末指标的 (15) 是单位。

例如原高接触 forcing 指标 $n=s-14-h$ 给
$6n-1=p-(84+6h)$。对固定 $(a,j,h)$，其低对角具有上述
全部充分大素数的准确单位性。
这仍是原未回绕三角行的事实；
没有将它无证认作 Schur 消元后任意高块的行列式。

## 9. 与整个原 C2 的剩余连接

自然 theta 权的正号已经支付：单独 relative grade $a$ 的
$\rho^a$ 给 $+34a$，乘回公共 $G_0$ 后给 $+34(a+40)$。
(5) 和 (17) 还支付了这一列的全部角因子。

但是一个真正的 $P\in K_2(M)$ 通常是多个 $a,j$ 的和，
而 R342 的 $q_n(\lambda,P)$ 同时依赖同一个原可提升左核 $\lambda$
与这个完整 $P$。
不能把 (26) 的逐列单位块当作各 grade 都另有一条零等式，
也不能把 forcing 指标 $n$ 直接当作来源次数 $a$。
还须在同一个实际双线性配对中组织这些矩阵。

同样，原 $w^{13}$、$Z_p^{-78}$ 及 $U_0$ 的准确连接仍按 R351、
R359 保留；本篇没有对整个目标删行。
R363 已将首次提升的实际 $A_\kappa^\circ$ 并入原模 $p^2$ 有理系数，
但这不意味着整个 theta 来源或原矩阵可以被另一有理模型任意替换。

现在已经具备的是：全部原 canonical 基的明确局部权、
整个角多项式的准确扭留数、所有固定测试点，以及只随来源次数线性增长
的单位块损失。下一步是把这些原矩阵与同一个 $K_2/C_2$ 配对相接，
或用保全部次数的真实导子关系控制其 Schur 剩余列。
课题的中央非零与无穷素数条件尚未由本篇完成。

## 依据与有限有理核算

- [R335](R335-full-integral-canonical-conductor-and-exact-relative-source.md)：全部原整基、$P_{134}$ 与精确次数。
- [R342](R342-original-gaussian-recalibration-and-miller-adjoint-residue.md)：同一个原两接触格及 $K=s-14$。
- [R346](R346-original-off-origin-residue-injection-and-full-cartier-polar-part.md)：全部实际极、原导子递推和整留数代数。
- [R351](R351-original-canonical-serre-adjoint-and-integral-second-lift-connection.md)：原可提升左核与保全部行的 Serre 配对。
- [R356](R356-original-gaussian-zeta-primitive-and-all-test-pole-normalization.md)：规范连接的全部短 jets。
- [R359](R359-original-canonical-bad-poles-primitive-residue-block-and-local-connection.md)：原坏角与真实扭留数余核。
- [R363](R363-original-first-frobenius-quotient-and-second-rational-connection.md)：真实首次提升与同一原 $\Gamma$ 的模 $p^2$ 系数。

(16) 已用 JavaScript BigInt 有理数和 $y^2=1+\xi$ 的有限多项式环核算；
(25) 的十二个余类及完整周期增量也已精确算出。
这些只是显示公式的有限代数核算，没有扫描目标素数；
全部次数与全部允许素数的证明在正文。

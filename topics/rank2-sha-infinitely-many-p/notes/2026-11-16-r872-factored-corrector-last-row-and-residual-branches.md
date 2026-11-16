# R872 后继：同一第二页修正的末行、剩余因子与二近支

日期：2026-11-16。**状态：下列同一原 $M/p^3$ 的必要条件已证明；指定第二、第三页是否可解仍未完成。** 本篇继续[最小 carry 的平方因子排除](2026-11-16-r872-first-carry-corrector-square-exclusion.md)。新增的是：在真正因子化的同预算基准上，完整第三精度支付相对矩阵的末行，强制同一个 $R$ 的 $ER|_C$ 在第 $s-1$ 阶为单位；若 $R$ 仍含一次 $F$，其剩余因子必有两条明确的近支，并付出原除子类中的联合交数成本。

这里始终保原全 $\mathcal W_D$、完整 $G_0/P_{134}/U_0$、总 charge 四十、三条十三行、第四短块和同一个 $R,S$。不把旧 $M/p^2$ 的窗口加长。

## 1. 原因子基准与三精度

使用 [R872](../results/R872-actual-quartic-third-carry-and-central-first-digit.md) 的共同 $E_1$ 及 Hasse 对齐规范。设
$$
p=6s-1>211,\qquad
\bar P=t^3F^4q\in\overline{\mathcal W}_D,\qquad
s=2h+2,\qquad
1<\ell\le h-1,\qquad h<s-4.
\tag{1}
$$
原零角满足
$$
\deg_YF(0,Y)=3,\qquad F(0,1)=0,\qquad
e_0=(EF)(0,1)\ne0,\qquad q(0,1)\ne0,\qquad E=Y\partial_Y.
\tag{2}
$$
所有分母在 $t=0$ 为单位。原接触为
$$
F(t(w),\bar g(w))=w^hu(w),\qquad u_0\ne0,\qquad
t(w)=t_1w+O(w^2),\quad t_1\ne0.
\tag{3}
$$
$\bar g$ 为同一个完整实际轴，不换成未运输的 $g_{\Theta,0}$。

[R491](../results/R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md) 定理2及式(11)适用于任意重复次数，因而可选择
$$
P^{\rm fact}=t^3\widetilde F^{\,4}\widetilde q\in\mathcal W_D.
\tag{4}
$$
这里 $\widetilde q$ 包含原固定 $d^{-C_D}$，每个有限 Gauss 角、无穷远次数及 $Y$ 帽均与给定约化相同。它不是把任意逐系数因子提升免费认作原来源。

固定同一原来源中的 $R,S$，假设
$$
M^{\rm orig}\bigl(P^{\rm fact}+pR+p^2S\bigr)\in p^3\Gamma_4.
\tag{5}
$$
后文 $R$ 及所有分支式均取其模 $p$ 约化。

原乘子 $m_{13}$ 的三个 carry 带分别只带一个 $p$；其余非零行带单位。对完整目标先施 $(c_*U_0)^{-1}$，并保其全部高尾，故 (5) 必给
$$
\boxed{J_4(P^{\rm fact}+pR)\in p^2\Gamma_{3s+\ell}.}
\tag{6}
$$
这是 R808 的精度引理在原四块上的同一证明：将 $M$ 写成 $(J_A,pJ_B)$，$B$ 现在是三条十三行；(5) 使 $J_A$ 输出被 $p^3$ 整除、$J_B$ 输出被 $p^2$ 整除，最后才去掉 $p^2S$。原乘子没有被当作整可逆，也没有丢掉三十九行。

反之，只有 $M(P^{\rm fact}+pR)\in p^2$ 时，$J_B$ 仅保证被 $p$ 整除，不能使用 (6)。以下第 $s-1$ 行的结论严格要求 (5)，或已单独付清同一个 (6)。

## 2. 同一个 R 的四个分支值

在原有限整前缀写
$$
\widetilde F(t(w),g(w))=w^hu+p\xi,\qquad
C(w)=\left(\frac{t(w)}w\right)^3
       \widetilde q(t(w),g(w)),\qquad
C_0=t_1^3q(0,1).
\tag{7}
$$
$\xi$ 是该因子提升的实际低阶修正，不可任意设零。现在已由 (6) 合法回到相对四块，所以 [R824](../results/R824-original-quartic-first-correctors-and-native-central-schur.md) 的首次商计算使用
$$
r_0=3,\qquad k=r_0+2h-s=1.
$$
$G_0$ 已通过完整整目标运输处理；本节的 $C_0$ 不含其单位首系数。以 $R_i=(E^iR)(t(w),\bar g(w))$ 记同轴值，得到
$$
\begin{aligned}
R_0&\equiv0\pmod{w^s},\\
R_1&\equiv-\frac1a w^{2h+1}Cu^4\pmod{w^s},\\
R_2&=-\frac8a C_0u_0^3e_0w^{h+1}+O(w^{h+2}),\\
R_3&=-\frac{36}a C_0u_0^2e_0^2w+O(w^2).
\end{aligned}
\tag{8}
$$
完整公式中两条含 $\xi$ 的项分别从 $h+3$、$3$ 起，故在 (8) 的两个显示首项之后；总 Euler 对 $q$ 的导数项也在原 R824 的已付误差范围内。并非在较长的整段或下一除 $p$ 页删除这些项。

令 $Y=\psi(t)$ 为 $F=0$ 通过 $(0,1)$ 的唯一光滑支。原三精度中同一个 $R$ 满足
$$
\boxed{
\begin{aligned}
\operatorname{ord}_w R(t(w),\psi(t(w)))&\ge s,\\
(ER)(t(w),\psi(t(w)))
 &=-\frac{11}{a}C_0u_0^4w^{s-1}+O(w^s),\\
(E^2R)(t(w),\psi(t(w)))
 &=\frac{28}{a}C_0u_0^3e_0w^{h+1}+O(w^{h+2}),\\
(E^3R)(t(w),\psi(t(w)))
 &=-\frac{36}{a}C_0u_0^2e_0^2w+O(w^2).
\end{aligned}}
\tag{9}
$$
**证明。** $g/\psi-1=(u_0/e_0)w^h+O(w^{h+1})$。在所读有限阶使用 Euler 流的 Taylor 多项式，其分母均为当前素数的单位。$E^2R$ 的首项由 $-8+36=28$ 得到；$ER$ 的完整二次项由
$$
-1+8-18=-11
$$
得到。此处 $2h+1=s-1<s$，故第一 Euler 块确实读到该首项。三次余项从 $3h>2h+1$ 起。值的下界为 $\min(s,3h+1)=s$，而 $E^3R$ 首阶一不受这次位移影响。这也可逐项直接应用 R824(20)、(21)、(27)，其额外读取门此时全部满足。证毕。

### 2.1 同一个短块支付的完整第二法向段

本范围还给比 (9) 的首项更长的实际段：
$$
\boxed{
(E^2R)(t(w),\psi(t(w)))
\equiv \frac{28}{a}w^{h+1}C(w)u(w)^3e(w)
\pmod{w^{h+\ell}}.
}
\tag{9a}
$$
右侧 $C,u,e$ 保 (7) 中同一个实际轴的完整系数；没有以它们的首常数替代这一段。与此同时第三法向段准确是
$$
\boxed{
(E^3R)(t(w),\psi(t(w)))
\equiv-24w^3C(w)\xi(w)e(w)^3
-\frac{36}{a}wC(w)u(w)^2e(w)^2
\pmod{w^\ell}.
}
\tag{9b}
$$
因此 (9a) 的 $\xi$ 消去不能外推为 (9b) 中也没有原根修正。

证明由 (6) 的第三长块、第四短块同时读取：
$$
\begin{aligned}
R_2&\equiv-24w^{h+3}Cu\xi e^2
-\frac8a w^{h+1}Cu^3e\pmod{w^{h+\ell}},\\
R_3&\equiv-24w^3C\xi e^3
-\frac{36}{a}wCu^2e^2\pmod{w^\ell}.
\end{aligned}
\tag{9c}
$$
第三长块中，carry 的 $C_1F^4$ 项从 $2h+1=s-1$ 起，
其它含 $F^2\xi$ 的高项从 $2h+3$ 起。
所读 $h+\ell\le2h-1$，它们都不进入 (9c)。
第四短块中，carry 的 $F^3$ 项从 $h+1$ 起，
其余一次提升项从 $h+3$ 起，均在 $\ell\le h-1$ 之外。
这里并不声称 (9c) 第一行已给第三块的全部 $s$ 行。

用同一个有限 Euler 流坐标
$v=w^hu/e+O(w^{2h})$，有
$E^2R|_C\equiv R_2-vR_3\bmod w^{h+\ell}$。
两个 $\xi$ 项在整段相消，剩余系数 $-8+36=28$。
二次 Taylor 余项及 $v-w^hu/e$ 的贡献均从至少 $2h$ 起，
严格超过所读末阶；得到 (9a)。
又由原 $t\mid R$，$vE^4R$ 从 $h+1$ 起，
所以在第四短块中 $E^3R|_C\equiv R_3\bmod w^\ell$，得到 (9b)。

## 3. 与原零角三重零联立

上一短注已经只由较弱的全 $M/p^2$ 证明
$$
R=tR^{[1]},\qquad
R^{[1]}(0,Y)=(Y-1)^3A(Y),\qquad
\deg A\le3,\qquad
A(1)=-\frac{6C_0u_0^2e_0^2}{a t_1}.
\tag{10}
$$
特别 $t$ 的因子次数恰为一，且 $F^2\nmid R$ 于 $k(t)[Y]$。式(9)给相同的平方排除，但还提供同一个修正的下一正常数据，而不是重新选择一个较短修正。

若 $F\nmid R$，(9)保留为实际全来源的高接触及指定法向必要条件；本文不证明这些条件已不相容。以下研究仍可能的 $F\mid R$。

由 $t$-Gauss 赋值及 $F(0,Y)\ne0$，准确写
$$
R=tF H,\qquad H\in k[[t]][Y].
\tag{11}
$$
令
$$
F(0,Y)=(Y-1)G_2(Y),\qquad \deg G_2=2,\quad G_2(1)=e_0.
$$
联立原 $\deg R_1\le6$，便有
$$
\boxed{
H(0,Y)=(Y-1)^2L(Y),\qquad
\deg L\le1,\qquad
L(1)=-\frac{6C_0u_0^2e_0}{a t_1}\ne0.
}
\tag{12}
$$
因此 $H$ 在原点恰为二重，而这只是原完整 $R$ 的真实商，不是新增自由来源。

沿同一 $F$ 分支，Leibniz 公式逐次给
$$
ER=t eH,\quad
E^2R=t(f_2H+2eEH),\quad
E^3R=t(f_3H+3f_2EH+3eE^2H),
\tag{13}
$$
其中 $e=EF|_C,\ f_i=E^iF|_C$。将同一个 (9) 代入，准确得到
$$
\boxed{
\begin{aligned}
H|_C&=-\frac{11C_0u_0^4}{a t_1e_0}w^{2h}
       +O(w^{2h+1}),\\
EH|_C&=\frac{14C_0u_0^3}{a t_1}w^h+O(w^{h+1}),\\
(E^2H)(0,1)&=-\frac{12C_0u_0^2e_0}{a t_1}.
\end{aligned}}
\tag{14}
$$
在第二式中 $f_2H$ 的阶为 $2h$，严格在 $h$ 之后；第三式中的 $f_2EH,f_3H$ 在原点均零。式(14)最后一项也等于 $2L(1)$，与 (12) 完全一致。

## 4. 两条近支及其实际来源成本

置 $\lambda=u_0/e_0$。由 (12) 的准确二重性，Weierstrass 准备给 $H$ 在原点的一个二次因子。用 $z=Y/\psi-1$ 作合法局部坐标，(14) 说明其权重初式在 $z=\lambda w^h v$ 下，除一个单位后正是
$$
-11+14v-6v^2.
\tag{15}
$$
较高 $z$ 次数和较高系数阶都严格在权 $2h$ 之后。这一步只用有限 Taylor；无需特征 $p$ 的无限对数。

其判别式为 $-68=4(-17)$，在当前素数为单位。因此在至多二次常数域扩张 $k'=k(\sqrt{-17})$ 后，准确有两条不同的光滑支
$$
\boxed{
\frac{\psi_H^\pm(t(w))}{\psi(t(w))}-1
=\frac{7\pm\sqrt{-17}}6\,\lambda w^h+O(w^{h+1}).
}
\tag{16}
$$
若 $-17$ 在 $k$ 非平方，两支互为常数域共轭，不声称已在原 $k$ 上分别分裂。两系数均非零、彼此不同且均不等于一。因此两支互交恰为 $h$，分别与原 $F$ 支交 $h$，与实际 $g$ 支也都只接触到 $h$。这不产生额外算术零。

这两支仍受完整来源帽。首先，原零角赋值
$$
v_0(A)=\min_n(4\operatorname{ord}_t A_n-n)
$$
在乘积上相加。由 $v_0(P)\ge-2$、$v_0(q)\le0$ 及 $\deg F(0,Y)=3$，
$$
12+4v_0(F)+v_0(q)\ge-2,\qquad v_0(F)\le-3,
$$
故 $v_0(F)=-3$。由 (11) 及 $R\in\mathcal W_D$，
$$
v_0(H)=v_0(R)-4-v_0(F)\ge-3.
$$
而 (12) 的二重根迫 $v_0(H)\le-2$。于是
$$
\boxed{-v_0(H)\in\{2,3\}.}
\tag{17}
$$
清去与零纤维互素的固定分母和底因子后，这是 R815 的真实零链亏量；不是把 $H$ 扩成任意双次数曲线。

若 $F$ 的严格变换 $C$ 几何整，原接触点光滑，且使用原 $X$ 上的来源除子 $\mathcal B_D$，还能得到明确交数门。记
$$
f_0=f-\sum_{j=1}^4E_{0,j}
$$
为**严格零纤维**。由 R815(5)、(36) 及 $v_0(F)=-3$，
$C\cdot f_0=3$。$R$ 的截面除子含一次 $f_0$ 和一次 $C$；剩余有效除子在原点含 (16) 的两支。因此
$$
\boxed{
2h\le(\mathcal B_D-f_0-C)\cdot C
=\mathcal B_D\cdot C-\kappa-3,\qquad \kappa=C^2.
}
\tag{18}
$$
所有其它固定角、例外或非原点分量仍在该有效剩余除子内。$C$ 为非边界几何整曲线，按 R815 完整锥为 nef，所以这些未删除分量不会使 (18) 失效。

这里特意不能把 $f_0$ 换成整个总纤维 $f$：原 raw $t\mid R$ 只保证严格零纤维分量，在十九角的单位框中未必含整个例外纤维。故 (18) 减的是三，不是 $b=Cf$。

## 5. 未闭的指定页

若 (18) 不成立，则本篇将 $F\mid R$ 的情况排除；若它成立，也没有证明这样的 $H$ 能在原全部角帽内存在，更没有证明全 $M$ 的第二、第三页可解。

对一般 $F\nmid R$，同一个 (9) 和 (10) 仍是必须联立的真实数据。R872 的
$$
\pi_\tau(Y)=[w^{s+\tau-4}]W_2(Y),\qquad Y\in K_1,
$$
在 $\tau=1$ 读第 $2h-1$ 阶，其完整像仍未知。不得将 (16) 的形式分裂或 (17) 的小零链亏量解释成这条尾行的自由调整；也不得将 (9) 的单位解释成指定余核已非零。

改变 $P^{\rm fact}$ 时必须同步改变同一个 $R$。本文首先固定 R491 的实际因子化整来源，全部式子均相对于该选择；同预算因子提升的改变在 $F^3$ 中，因而本文的值及首法向必要条件按同一提升运输，而更高正常尾仍按原公式保留。

本证明没有数学程序运行，也没有新增数值证书。

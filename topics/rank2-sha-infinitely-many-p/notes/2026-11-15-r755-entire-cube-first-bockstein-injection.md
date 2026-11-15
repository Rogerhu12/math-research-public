# R755 增补 — 全部原 cube 的首 Bockstein 单射

日期：2026-11-15。**状态：以下原子格结论已证明；全 $\mathcal W_D$ 的吸收及指定 forcing 非零仍未解决。**

本篇沿用 [R755](../results/R755-whole-original-cube-carry-filter-and-specified-value-class-invariance.md) 的同一个 $F$、十九角、原整数帽和整提升。它给整个实际 cube 空间的准确 Smith 结论，不只给原 $kP^{\rm fact}$ 那一列。

## 1. 准确假设

保 R755 的
$$
d_0=r-k=s-2h\in[1,13],\qquad
N_0=s-13=2h+d_0-13,\qquad h>13.
$$
记
$$
e_E=E\cdot C,\qquad
M_*=\min(h,h+2d_0-13)
=h-(13-2d_0)_+.
\tag{1}
$$
$C$ 是原几何整曲线，在 $P$ 光滑；$\kappa=C^2>0$。
保 R680 已付的 $C$ nef 性，以及同一实际
$$
\mathcal C_D=d^{-C_D}F^3H^0(X,\mathcal O_X(E))
\subset\overline{\mathcal W}_D.
$$
这里 $E\ge0$ 是 R755 的实际剩余除子，不替换成环境矩形。

**定理。** 若
$$
\boxed{e_E<\min(\kappa,M_*),}
\tag{2}
$$
则原首 Bockstein 在整个 $\mathcal C_D$ 上单射：
$$
\boxed{
P_H\longmapsto\beta_M(P_H)=M(\widetilde P_H)/p\bmod p
\quad\text{是单射。}
}
\tag{3}
$$
这里使用 R755 的同一整乘积提升及其完整目标，不能在定义 (3) 时另选任意 $pR$。

相应整 cube 子格上的限制矩阵 $M|_{\widetilde{\mathcal C}_D}$ 的非零 Smith 因子**全部恰为 $p$**，数目为 $\dim_k\mathcal C_D$。该限制矩阵满列秩，没有额外的 $p^2$ 因子或自由来源核。

## 2. 原第一 Gaussian 块已经检测所有非零 cube

沿用 R755 的
$$
H_0=(d^{-C_D}H)|_C,\qquad H_1=\mathcal E(d^{-C_D}H)|_C.
$$
其式 (16) 准确重排为
$$
\begin{aligned}
\widehat\beta_1
={}&t^{h-d_0}e^3b_su^3
\left(1+\frac{6a\,t^{d_0}\xi}{b_su^2}\right)H_0\\
&+t^{2h-d_0}b_su^4
\left(e^3H_1+\frac32e^2f_2H_0\right)
\pmod{t^{N_0}}.
\end{aligned}
\tag{4}
$$
$d_0\ge1$，而 $e,b_s,u$ 是实际整单位、$\xi$ 整，所以第一行括号是单位。第二行包含全部第四 normal 项；本篇没有令它恒零。

仅将 (4) 截到
$$
t^{\min(N_0,\,2h-d_0)}
$$
时，第二行才确实不可见。因此
$$
\boxed{
\widehat\beta_1=0
\ \Longrightarrow\
\operatorname{ord}_P H_0
\ge\min(N_0,2h-d_0)-(h-d_0)=M_*.
}
\tag{5}
$$
这是原目标内的合法截断，不延伸最后已读行。

若 $H_0\ne0$，则它是 $\mathcal O_C(E)$ 的非零截面。该线束次数为 $e_E$，而 $P$ 是光滑有理点；所以其在 $P$ 的零阶至多 $e_E$。在 (2) 下，(5) 因而迫 $H_0=0$。

这时实际 $H$ 属于 $H^0(X,\mathcal O_X(E-C))$。但
$$
(E-C)\cdot C=e_E-\kappa<0.
$$
由于 $C$ nef，任何有效除子与 $C$ 的交数都非负，故
$$
H^0(X,\mathcal O_X(E-C))=0.
\tag{6}
$$
于是 $H=0$，证明 (3)。

这里没有在奇异曲线上调用未经支付的消失定理：零阶界只使用 $P$ 光滑与线束次数，(6) 只使用原曲面上的 nef 交数。

## 3. 整来源与准确 Smith 因子

R755 的完整 Gauss 基给一个有限自由整格
$\widetilde{\mathcal H}_E$，准确约化为 $H^0(X,\mathcal O_X(E))$。其同一个整乘积
$$
H\longmapsto d^{-C_D}\widetilde F^{\,3}H
$$
属于原 $\mathcal W_D$，保全部十九角和原次数帽。它在来源端 $p$ 饱和：若这个乘积被 $p$ 整除，清去单位 $d$ 并模 $p$ 后，由多项式环无零因子及 $\bar F\ne0$ 得 $\bar H=0$。

R755 已证明整个限制矩阵被 $p$ 整除，故可写
$$
M|_{\widetilde{\mathcal C}_D}=pA.
$$
(3) 正是 $\bar A$ 满列秩。于是 $A$ 有一个满列单位子式，经过整目标、来源基变换后全部非零 Smith 因子均为单位。因此原限制矩阵的所有非零因子恰为 $p$。

逆的是整个真实 $c_*U_0$；显示的 $w^{13}$ 只在原已允许的行上除去，再使用 $t=t(w)$ 的整可逆变量。原 $P_{134}$、共同 charge、两条十三行以及第三块始终保留。证明只从其真实第一 Gaussian 块取了一个充分检测窗口；它没有把另两块或 $C_4$ 从原矩阵删除。

## 4. 何时临界家族确实满足此门

R750 给原实际不等式
$$
e_E\le\frac{\mathcal B_D^2-9\kappa}{3}.
\tag{7}
$$
因此可直接以 (7) 的右边严格小于 (2) 的右边，作为完全数值的充分条件。

若另已处于此前付清的平衡临界家族
$$
D=3b+O(1),\qquad
\kappa=\frac{47}{12}b^2+O(b),\qquad
h/\kappa\longrightarrow9/8
$$
且其中 $O(b)$ 常数统一，则原 $\mathcal B_D^2=\frac{47}{12}D^2+O(D)$ 给 $e_E=O(b)$。又 $M_*=h-O(1)$，所以充分大 $b$ 满足 (2)。

这里的 $e_E=O(b)$ 只用于这一已指定临界关系；没有对任意因子、任意 $D$ 宣称相同估计。

## 5. 全原来源的吸收仍须同一个 R

本篇确实说明：在 (2) 下，任何非零原 cube 的首 Bockstein 都非零；R755 中 primitive cube 的值投影虽然为零，另外两个完整块不能同时为零。

但它没有证明
$$
\beta_M(P_H)\notin\operatorname{im}\bar M.
$$
整 $\mathcal W_D$ 中的其它真实列仍可能提供 $R$，满足
$$
\bar M R=-\beta_M(P_H).
$$
故 (3) 不能读成整个原 $M$ 的第二余类非零，也不排除来自完整来源的 $p^2$ 提升。后续仍保这个同一 $R$ 的全部 normal 行、两条十三行以及下一位 forcing。

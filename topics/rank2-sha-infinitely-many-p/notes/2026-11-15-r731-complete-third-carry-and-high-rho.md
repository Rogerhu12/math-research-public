# R731 增补 — 指定高 rho 分支的完整第三块与真正十三行延拓门

日期：2026-11-15。**状态：已证明。**

本增补继续
[R731](../results/R731-specified-mirror-normal-jet-and-two-actual-smith-p-factors.md)
的同一个指定镜轴类 $[B]$、整提升 $P_B=qt^rF\widetilde B$、
原 cube 及全部十九角来源。
它补充 R731 的高 $\rho$ 分支，不新增来源或中央条件。

R731 的第二块低行之外，原第三块可完全从共振之前的实际模 $p$ 轴读取。
特别，原 $M$ 较短镜轴遗漏的十三行在下一位仍可见；
如果指定 $B$ 没有真正延长过这些行，
它与 cube 的首 Bockstein 已严格独立。
以下也保这十三行可能产生的活着的额外 normal 项。

## 1. 同一数据和准确读取窗口

保 R731 的 (1)–(4)，并假设 $\bar z_c=0$。
于是 $[B]\in K_{\rm mir}/kF^2$ 是满足 $B|_Z=UA|_Z\ne0$ 的唯一类。
所有下标都表示在同一曲线 $C=(F=0)$ 上的 Euler 导数：
$$
B_j=(\mathcal E^jB)|_C,\qquad
q_j=(\mathcal E^jq)|_C,\qquad
e=(\mathcal EF)|_C,\qquad f_2=(\mathcal E^2F)|_C .
$$
$q_0,e,u,b_s$ 均在原点为单位。
令
$$
\eta_0=t^hu,\qquad
\mathscr B=B_0+2\eta_0B_1,\qquad
T_J=s-r=2h-k,
$$
$$
\delta_0=0\ (J),\qquad \delta_0=13\ (M),\qquad
T=T_J-\delta_0.
\tag{1}
$$
$\mathscr B$ 是显示的**线性 normal 组合**，
不是把完整 $B(t,\psi e^{2\eta_0})$ 在更高阶仍截为一次。
仅已有
$$
\operatorname{ord}\mathscr B\ge T .
\tag{2}
$$
$B\mapsto B+cF^2$ 不改变 $\mathscr B$ 或 $B_1$。

本篇第三块所需的所有普通 $t$ 系数严格低于
$$
\boxed{T_J+\ell=s-r+\ell\le s.}
\tag{3}
$$
因此全部读取都在原首共振之前。
没有借用未知 $\xi$、更高 Gaussian 系数或新两位观察列。

## 2. 第三块的完整模 p 公式

定义同一实际级数
$$
\boxed{
\begin{aligned}
\mathscr D_B={}&q_0e\,\mathscr B
+\eta_0(q_0f_2+2q_1e)\,\mathscr B\\
&+\eta_0^2
\left(\frac32q_0eB_2-\frac12q_0f_2B_1-q_1eB_1\right).
\end{aligned}}
\tag{4}
$$

**命题 1。** 相对 $J$ 的完整第三块为
$$
\boxed{
\beta_J(P_B)^{(2)}
=a\,b_s\,t^{r-s}\mathscr D_B\pmod{t^\ell}.
}
\tag{5}
$$
对原 $M$，先只逆原整单位 $c_*U_0$，准确有
$$
\boxed{
\left[(c_*U_0)^{-1}M(P_B)/p\right]^{(2)}
=
a\,w^{13}b_s\,t^{r-s}\mathscr D_B
\pmod{w^{\ell+13}},
\qquad t=t(w).
}
\tag{6}
$$
(6) 右边允许先出现最低 $t^{-13}$ 的 Laurent 式，
但由 (2) 乘 $w^{13}$ 后是整普通级数。
保全部坐标单位；没有将 $w^{13}$ 视为 $t^{13}$。

**证明。** 在同一正规坐标中，令 $G=qFB$。
$F|_C=0$ 给
$$
\begin{aligned}
(\mathcal EG)(t,\psi e^{\eta_0})
={}&q_0eB_0\\
&+\eta_0\{2q_0eB_1+(q_0f_2+2q_1e)B_0\}\\
&+\eta_0^2
\left\{\frac32q_0eB_2+
\left(\frac32q_0f_2+3q_1e\right)B_1\right\}\\
&+O(t^{3h}).
\end{aligned}
\tag{7}
$$
其中所有省略的 $\eta_0^2B_0$ 项也属于 $O(t^{3h})$，
因为 R731 已证 $\operatorname{ord}B_0=h+\rho\ge h$。
将 $B_0=\mathscr B-2\eta_0B_1$ 代入，
(7) 的前三项恰为 (4)。

原物理评价是 $t^rG(t,g e_2(a\epsilon))$。
其显式 $\epsilon$ 项准确为
$$
a\,t^r(\mathcal EG)(t,g)\epsilon.
$$
作一次 $t^s=p\epsilon b_s$ 进位，再除 $p$，
即产生 (5)/(6)。
显式 $\epsilon^2$ 项被整个原 $t^r$ 前缀及 $r\ge\ell$ 截掉；
普通项若进位到第三块已有 $p^2$，除一次 $p$ 后仍为零。

整提升及 $p\xi$ 产生的项本身含 $p$；
它们若从显式 $\epsilon$ 项进到第三块，还须再付一次 $p$。
所以在本节约化中也为零。
原 $\xi_0$ 并未被规范掉，完整其他块照旧保留。

最后
$$
T_J+\ell=2h-k+\ell<3h
$$
由 $\ell<h$ 保证。
所以 (7) 的 $O(t^{3h})$ 真正超出 (3)，没有省掉可读尾。
相同证明适用于原 $M$ 的全部第三块；
只须按 (6) 保留真实十三行运输。证毕。

对 $J$，(4) 中的中间项从 $h+T_J$ 起，
确实在 (3) 以外，可以删去。
但对 $M$ 只知 $\mathscr B\in t^{T_J-13}$，
中间项在 (6) 的第三块从第 $h$ 行起。
若 $h<\ell+13$，它可以活着，故 (6) **不能**省略它。

代入 $B=F^2$ 时，
$B_0=B_1=0,\ B_2=2e^2$，
(5)/(6) 准确还原原 cube：
$$
\boxed{\beta(P^{\rm fact})^{(2)}
=3a\,w^{\delta_0}b_s q_0e^3u^2t^k.}
\tag{8}
$$
这核定了 (4) 的系数 $3/2$ 及全部 Gaussian 归一。

## 3. 真正的十三行延拓，以及更多 k 行

设
$$
m=\operatorname{ord}\mathscr B\in[T,\infty].
$$
若 $m<2h$，
(4) 第一项的阶为 $m$，
另外两项的阶分别至少为 $m+h$ 和 $2h$，
不能取消它。
所以 (5)/(6) 的首项准确位于第三块行
$$
\boxed{j_B=\delta_0+m-T_J<\delta_0+k,}
\tag{9}
$$
且 $j_B\ge0$。
其首系数为 $a\,b_s(0)q_0(0)e(P)[t^m]\mathscr B$
乘原 $t/w$ 的首单位，非零。
cube 的第三块却从 $\delta_0+k$ 起。

整个 $qt^r\mathcal H_3$ 的首像在该第三块为零。
因此 (9) 与 cube 的第三块首行给一个真实的 $2\times2$ 单位子式，
不需要 R731 的 $\rho<r-k$ 条件。

尤其对原 $M$，
$$
\boxed{T_M\le m<T_J}
\tag{10}
$$
给 $0\le j_B<13$：
这是原较短镜轴遗漏的十三行在下一位的实际输出。
不允许为简化镜轴而把 (10) 免费置零。
对 $J$ 或 $M$，
$m\in[T_J,2h)$ 的另外 $k$ 行同样给独立性。

从而，只要 $m<2h$，
R731 显示来源 $\mathcal N_*$ 的 Smith 因子仍准确为
$R_{\rm v}$ 个单位和两条 $p$。
若在整个同前缀 $qt^r\mathcal H_3$ 内允许更多首次修正，
也不能使 $\operatorname{span}\{\bar P^{\rm fact},\bar P_B\}$ 中
任何非零组合升到第二位；
这两条行杀整个该前缀首像。
完整 $\mathcal W_D$ 的其余低列依然不在这个结论内。

## 4. 留下来的唯一三阶 normal 不变量

现在假设
$$
\boxed{\operatorname{ord}\mathscr B\ge2h.}
\tag{11}
$$
此时 (4) 的中间项也从 $3h$ 起，
即使在原 $M$ 的全第三块中亦不可读。
除同一非零 cube 第三块，得到正规级数
$$
\boxed{
\mathscr H_B=
\frac{\mathscr B}{3e^2\eta_0^2}
+\frac{B_2}{2e^2}
-\frac{f_2B_1}{6e^3}
-\frac{q_1B_1}{3q_0e^2}
\pmod{t^{\ell-k}}.
}
\tag{12}
$$
除以 $\eta_0^2$ 在 (11) 后合法；
其余分母均是同一原点单位。
精确关系是
$$
\boxed{
\beta(P_B)^{(2)}
=\beta(P^{\rm fact})^{(2)}\,\mathscr H_B
}
\tag{13}
$$
于相应完整第三块，使用同一个 $t=t(w)$ 和 (8)。

若换 $B\mapsto B+cF^2$，
则 $B_2\mapsto B_2+2ce^2$，其余 (12) 的项不变。
因此
$$
\boxed{\mathscr H_{B+cF^2}=\mathscr H_B+c.}
\tag{14}
$$
(12) 的非常数部分是原指定类 $[B]$ 的真正不变量，
不是自由选取的第二法向数据。
整个 (12) 仍只读取 (3) 的共振前实际系数。

(13) 说明：
两条第三块向量成比例，当且仅当
$\mathscr H_B$ 在 $k[t]/t^{\ell-k}$ 中为常数。
若其非常数部分非零，仍得到 R731 的准确两条 $p$。

当 $\ell-k=1$ 时，此项测试当然没有非常数坐标；
本篇不凭形式上的「二阶 normal」宣称它仍能给独立性。

## 5. 原完整低行的精确未决分支

将 R731 的第二块低行与本篇全第三块合并。
这些行全部杀
$\overline{\mathsf M}_0(qt^r\mathcal H_3)$，
并且 cube 的第三块首行始终为单位。

因此在 $\bar z_c=0$ 的情况下，
若这组**实际低行**仍不能区分 $P_B$ 和 cube 的首 Bockstein，
则必须同时满足
$$
\boxed{
\begin{gathered}
\rho\ge r-k,\qquad
\operatorname{ord}(B_0+2\eta_0B_1)\ge2h,\\
\mathscr H_B\in k\subset k[t]/t^{\ell-k}.
\end{gathered}}
\tag{15}
$$
反过来，(15) 准确使这组低行上的两个向量成比例。
若 $\mathscr H_B=c_B$，唯一的组合
$P_B-c_BP^{\rm fact}$ 在这些行上为零；
没有据此声称其完整首 Bockstein 为零。

在 (15) 的高 $\rho$ 分支，
$\rho\ge r-k\ge\ell-k$，
所以 (12) 中最后两项在所读长度内确实消失。
于是该分支最后一条还可准确写成
$$
\boxed{
\frac{B_0+2\eta_0B_1}{3e^2\eta_0^2}
+\frac{B_2}{2e^2}
\in k\pmod{t^{\ell-k}}.
}
\tag{16}
$$
这次删项有真实阶数依据，
不同于在一般 (12) 中事先删去 $q_1$ 或 $f_2$。

(15)/(16) 是指定 $B$ 在原实际轴上的有限条件。
它们尚未由全部角帽或原 ODE 排除，
尤其不把 $\ell=1,k=0$ 的常数商误作新非零证据。
后续仍须将其与原共振前 ODE、真实剩余来源和同一 $R$ 联立。

## 6. 精度与来源边界

本增补只用 R731 的同源整提升和同一个 $P_2=P^{\rm fact}+pR$。
(5)/(6) 已保完整第三块和原两条十三行，
没有把相对 $J$ 核自动认成 $M$ 的全部核。

若原首次提升已完成，可以用两条已识别的核列调整同一个 $R$，
但其余第二障碍高尾必须随这个同一调整运输。
两条 $p$ 的存在不证明原全格 forcing 非零，
也不把来源返回赋予新算术中央零。

依赖：
[R502](../results/R502-full-low-ell-bockstein-and-actual-geometric-residue.md)；
[R547](../results/R547-zero-charge-vertical-unit-block-and-actual-cubic-schur-column.md)；
[R730](../results/R730-specified-ramification-class-linear-contact-bound-and-actual-mirror-kernel.md)；
[R731](../results/R731-specified-mirror-normal-jet-and-two-actual-smith-p-factors.md)。

# R588 增补：任意固定长塔的完整 nonlinear wild 障碍

日期：2026-11-14。**状态：已证明。**
本增补将 R588 的整个 Kummer 域独立性及非线性闭边界结论
推广到 R584 的任意固定两塔。
原七塔的较强范围 $p>19$ 不变；
长塔使用下面完全显式的充分下界，不留下一个未知有限坏素数集。
本增补不占用 R597 的原矩阵 forcing 问题。

## 1. 准确范围与实际积分

保持原 $b=17$、$f_4=x\sigma^6$、$f_1=-xy\sigma^6$。
固定
$$
R_4=2+6m_4,\qquad R_1=5+6m_1,\qquad m_4,m_1\ge0,
$$
$$
m=\max(R_4-1,R_1-1)\ge4,
\qquad
\boxed{p\equiv5\pmod6,\quad p>12m+31.}
\tag{1}
$$
考虑同一零初值的全部单积分
$$
J_{4,j}=\int_0^z u^j f_4(u)\,du\quad(0\le j<R_4),
\qquad
J_{1,j}=\int_0^z u^j f_1(u)\,du\quad(0\le j<R_1).
\tag{2}
$$
原长塔 $U_{\ell,r}$ 与 (2) 仍通过 R575/R584 的真实三角式相连，
并作同一个正幂规整
$$
V_{4,r}=z^{R_4-r}U_{4,r},\qquad
V_{1,r}=z^{R_1-r}U_{1,r}.
\tag{3}
$$
这里所有 $r$ 均在相应的 $1,\ldots,R_\ell$ 内。

完全保持 R588 的实际
$$
d=p+1,\quad c=[z^d]\log(\sigma/z),\quad
a=6c,\quad\mathscr E=e^{cz^d},\quad
S=p^{-p/(p^2-1)},\quad\rho=p^{-1/(2p)}.
$$
对每个 $S\le R\le\rho$，使用同一个
$$
F_R=\operatorname{Frac}\mathbf C_p\langle z/R\rangle,
\qquad K_R=F_R(\mathscr E).
\tag{4}
$$
R588 已证明这些是常数域为 $\mathbf C_p$ 的实际 degree $p$
Kummer 扩张，保闭 $S$ 边界及 no-pole 引理。

## 2. 一个支付全部长塔的低系数引理

**引理。**
令 $k=\overline{\mathbf F}_p$。
对次数至多 $m$、不全为零的 $A,B\in k[z]$，
原 $y=-z^{-3}+O(z^3)$ 的低 Laurent jet 满足
$$
\boxed{
\operatorname{ord}_z\{z^5(A-yB)\}\le6m-1.
}
\tag{5}
$$
所需全部系数均在原整窗口内；
不假设原特征零形式指数在特征 $p$ 下有一个无限整延拓。

先说明窗口。R301 给 $z^2x$ 在高度二圆盘的全部系数估计，
$y=Dx/2$ 因而也给原 $-z^3y$ 的对应整系数。
(1) 使以下计算只需的有限 jet（可保到 $z^{6m+12}$）
严格低于首个高度二坏分母窗口。
原特征零等式
$$
\boxed{(Dy)^3=27(y^2-b)^2}
\tag{6}
$$
因此可在这些有限整系数上约化。
这里没有引入未经支付的无限 $\mathbf F_p((z))$ 形式群指数。

若 $B=0$，则 (5) 由 $\deg A\le m$ 立即成立。
若 $B\ne0$，记 $v=\operatorname{ord}B$。
除非 $A/B$ 的首项恰为 $-z^{-3}$，
$A-yB$ 的首项不能相消，阶至多 $m$，
仍给 $m+5\le6m-1$。

只需处理首项相消情形。此时
$$
v\ge3,\qquad U=A/B=-z^{-3}+\cdots,\qquad
h=\operatorname{ord}(U-y)>-3.
$$
构造真正多项式
$$
\boxed{
N_{A,B}=(A'B-AB')^3-27B^2(A^2-bB^2)^2,
\qquad \deg N_{A,B}\le6m.
}
\tag{7}
$$
它非零。否则 $U'\ne0$（首项为 $3z^{-4}$），
且令
$$
X=\frac{3(U^2-b)}{U'}
$$
会得到 $X^3=U^2-b$。
所以 $k(X,U)\subset k(z)$ 是光滑曲线
$U^2=X^3+b$ 的函数域。
$U$ 非恒定，故这是对 genus 一函数域的嵌入；
Lüroth 定理却使 $k(z)$ 的每个一变元中间域为 genus 零，矛盾。
这个论证不需要可分性，也排除了纯不可分映射的遗漏。
$p>19$ 保持曲线光滑及所有系数有效。

若 $\lambda=\operatorname{ord}(A-yB)$，则 $h=\lambda-v$。
由 (6) 展开 $U=y+(U-y)$，
$$
\operatorname{ord}\{(U')^3-27(U^2-b)^2\}\ge h-9.
$$
确实两组线性项的阶至少都是 $h-9$；
二次及更高项因为 $h>-3$ 不会更低。
特征 $p$ 下求导可能提高某一项的阶，
只会加强这个下界，不会损坏它。
乘以 $B^6$，得到
$$
\operatorname{ord}N_{A,B}\ge5v+\lambda-9.
$$
用 $N_{A,B}\ne0$、(7) 和 $v\ge3$，
$$
\lambda\le6m-5v+9\le6m-6.
$$
这正给 (5)。

也可完全按有限 jet 读最后一步：
若 (5) 失败，则所需有限展开使
$\operatorname{ord}N_{A,B}\ge6m+1$；
(7) 会迫这个多项式恒为零，已被上一段排除。
所以证明不需要无限特征 $p$ 级数的假设。证毕。

## 3. 全部常数组合都有非中央单位 Stokes 行

取 (2) 的任意非零 $\mathbf C_p$ 常数组合 $\mathcal J$。
以一个非零常数缩放后，可以令所有系数整且至少一个为单位。
其被积函数准确为
$$
D\mathcal J=x\sigma^6\{A(z)-yB(z)\},
\qquad \deg A\le R_4-1,\quad\deg B\le R_1-1.
$$
置 $H=\mathscr E^{-6}\mathcal J$。
用 $\theta=zD$，完整方程为
$$
\boxed{
(\theta+ad z^d)H=G,\qquad
G=z^5W H_\sigma^6(A-yB),
}
\tag{8}
$$
其中 $W=z^2x$、$H_\sigma=\sigma/(z\mathscr E)$
都是 R588 的实际单位。

每个原被积项在去 Gaussian 后有范数界
$$
\|\mathscr E^{-6}z^{j+1}f_4\|_\rho\le\rho^{j+5},
\qquad
\|\mathscr E^{-6}z^{j+1}f_1\|_\rho\le\rho^{j+2},
$$
因而
$$
\boxed{G\in\mathbf C_p\langle z/\rho\rangle,\qquad
\|G\|_\rho\le\rho^2.}
\tag{9}
$$

在 $<p$ 的所需低系数中，
$W H_\sigma^6$ 是首项为一的整单位；
原 $\sigma$ 的首坏项尚在 $d=p+1$。
将归一系数约化并用 (5)，
存在明确范围内某个实际单位系数
$$
\boxed{
2\le r\le6m-1<p-1,\qquad [z^r]G\in\mathcal O_{\mathbf C_p}^\times.
}
\tag{10}
$$
可以取其首个非零剩余系数。
这一步没有由特征零独立性猜一个未知的模 $p$ 小式；
(5) 已同时覆盖每个允许素数和每个常数组合。

R580 的 Stokes 递推不要求 $r$ 是六的倍数。
对 (8) 的 $r\bmod d$ 部分，写
$$
P_rG=z^r\sum_{l\ge0}g_lz^{dl},\qquad x=r/d.
$$
完整 Stokes 和为
$$
\mathfrak s_r
=\sum_{l\ge0}(-1)^l(x)_{\overline l}a^{-l}g_l.
\tag{11}
$$
(9) 给
$$
v_p(a^{-l}g_l)\ge
\frac{l(p-1)+2-r}{2p}.
\tag{12}
$$
当 $l\ge1$ 时，(10) 使右边严格正。
所以 (11) 收敛且
$$
\boxed{\mathfrak s_r\equiv g_0=[z^r]G
\pmod{\mathfrak m_{\mathbf C_p}},\qquad
\mathfrak s_r\text{ 为单位}.}
\tag{13}
$$
使用最大理想写同余，允许组合系数在分歧扩张甚至
$\mathbf C_p$ 中任意取值；原完整尾界没有被省略。

逐项解 (8) 给
$$
P_rH=\frac{\mathfrak s_r}{d}
z^r\sum_{h\ge0}
\frac{(-a)^hz^{dh}}{(x)_{\overline{h+1}}}
+\mathcal R_r,
\qquad
\mathcal R_r\in\mathbf C_p\langle z/\rho\rangle .
\tag{14}
$$
为明确整个尾，而不只写形式解，
余项的第 $h$ 个系数是 $l>h$ 尾和。
约去 $(x)_{\overline{h+1}}$ 后，
令 $u=l-h\ge1$，其中每项的 $\rho$ 加权赋值至少为
$$
\frac{u(p-1)+2}{2p}.
$$
Pochhammer 余因子整；$u$ 大时该下界趋无穷，
固定有限个 $u$ 时由 (9) 的 Tate 尾使系数趋零。
因此确得 (14) 的整个 Tate 余项。

模型在闭 $S$ 边界不收敛为 Tate 元。
当 $h=p^n$，因为 $2\le r\le p-1$，
$$
v_p((r/d)_{\overline{p^n+1}})
=\frac{p^n-1}{p-1}.
$$
对每个 $p^a$、$a\le n$，
相应等差数列中恰有 $p^{n-a}$ 项可除；
更高 $p$ 次幂要求 $r\equiv\pm1\pmod d$，
已由 (10) 排除。
因此模型第 $r+dp^n$ 项的 $S$ 加权赋值恒为
$$
\frac1{p-1}+\frac{rp}{p^2-1},
$$
不趋于无穷。
(13) 的单位及 (14) 的更大盘余项不能消掉它。

任意积分常数 $C$ 在 $\mathscr E^{-6}(\mathcal J-C)$ 中
只新增 $-C e^{-az^d}$，仅有 $0\bmod d$ 部分。
它不能改变 (10) 的非中央余类。
故对全部非零组合及全部常数都有
$$
\boxed{\mathscr E^{-6}(\mathcal J-C)\notin
\mathbf C_p\langle z/S\rangle.}
\tag{15}
$$

## 4. 长塔的完整 nonlinear 结论

现在 R588 §5 的整个 Kummer 证明逐项适用，
不需给长塔分别猜原函数。

若 $D\mathcal J$ 在某个 $K_R$ 中有原函数，
取真实 $\mu_p$ 特征六投影后，该原函数为
$\mathscr E^6u$、$u\in F_R$。
(8) 对应的一阶非齐次方程右边在 Tate 代数中；
R588 的闭盘 no-pole 引理迫 $u\in\mathcal T_R$。
常数域仍是 $\mathbf C_p$，
所以 $u=\mathscr E^{-6}(\mathcal J-C)$，
与 (15) 矛盾。
对有限代数扩张取迹也同样排除原函数。

加性积分引理遂给
$$
\boxed{
\{J_{4,j}\}_{j<R_4}\cup\{J_{1,j}\}_{j<R_1}
\text{ 在每个 }K_R\text{ 上代数独立。}
}
\tag{16}
$$
由原真实三角变换，
全部 $R_4+R_1$ 个 (3) 也在这些 $K_R$ 上代数独立。

因此，对任意真正含这些长塔坐标的实际多项式
$$
\Phi=P(S_{34},T_{72},V_{4,1},\ldots,V_{4,R_4},
V_{1,1},\ldots,V_{1,R_1})
$$
及任意整数 $q$，
都有
$$
\boxed{
\operatorname{rad}_z(\mathscr E^q\Phi)=S,\qquad
\mathscr E^q\Phi\notin\mathbf C_p\langle z/S\rangle.
}
\tag{17}
$$
证明与 R588 §7 相同：
不属于 $K_R$ 给所有 $R\ge S$ 的上界，
全部原积分在每个 $<S$ 的盘收敛给下界。
这个结论保任意多项式次数及依赖 $p$ 的常数系数。
$S_{136}$ 如加入系数环，仍须先按真实基础来源关系收集，
不能以一个实际为零的系数制造假反例。

原正幂规整使全部坐标仍是 $w=z^6$ 的整函数，
所以共同 $w$ 半径是 $S^6$。
R584 的无 Dirac 子格是这些实际坐标的子格，
其所有真正非恒定多项式也继承 (17)。

本增补没有将 degree $p$ 域上的投影当成整来源操作，
没有判定有限饱和前缀的 Smith 因子，
没有改变原普通分布阶、两指定负矩或完整中央条件。
原七塔仍使用 R588 已付的更强 $p>19$；
(1) 是任意固定长塔的显式统一充分范围，不声称最优。

## 依赖

- [R588](../results/R588-actual-wild-kummer-disc-and-nonlinear-primitive-radius.md)：
  实际 Kummer 域、闭盘边界、no-pole 和加性积分运输。
- [R580](../results/R580-same-charge-primitive-towers-and-unit-noncentral-stokes-matrix.md)：
  完整 Stokes 递推及余项估计；本增补重新核定任意非中央余类。
- [R584](../results/R584-arbitrary-fixed-primitive-towers-dirac-jets-and-full-lattice-budgets.md)：
  固定长塔及原真实来源、分布和全格预算。
- [R301](../results/R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)：
  所用有限低 Laurent 系数的原整窗口。

本增补为全参数证明，没有增加目标素数扫描。

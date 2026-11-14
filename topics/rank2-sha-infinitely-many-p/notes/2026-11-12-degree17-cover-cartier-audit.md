# 次数十七截面的固定覆盖与一个精确 Cartier 比较反例

日期：2026-11-12。状态：以下固定曲线、微分分解和反例已证明。
尚未构造目标 prime diagonal 与某个正确 Cartier entry/minor 之间的映射。

## 1. 先把真实目标缩放到固定 $D=1$ 的系数

对 $E_D:y^2=x^3-Dx$，记 sigma、半周期 theta 及 Weierstrass
函数分别为 $\sigma_D,\vartheta_D,x_D$。已证明的真实截面为

$$
 A_{17}(z)=\frac15\vartheta_{17}(z)\sigma_{17}(z)^{16}
              (x_{17}(z)^2+17)
              (5x_{17}(z)^4-34x_{17}(z)^2+289).
$$

相应定义

$$
 A_1(z)=\frac15\vartheta_1(z)\sigma_1(z)^{16}
              (x_1(z)^2+1)(5x_1(z)^4-2x_1(z)^2+1)
        =\sum_n\beta_{4n}z^{4n}.
 \tag{1.1}
$$

在 $a^4=D$ 的变量变换下，
$x_D(z)=a^2x_1(az)$、$\sigma_D(z)=a^{-1}\sigma_1(az)$、
$\vartheta_D(z)=\vartheta_1(az)$。因此准确有

$$
 A_D(z)=D^{-1}A_1(az),\qquad b_{4n}(D)=D^{n-1}\beta_{4n}.
 \tag{1.2}
$$

对目标惰性 $p\ge7$，$17$ 是单位，故
$b_{p+1}(17)$ 与 $\beta_{p+1}$ 的单位性相同。
这只是固定截面系数的齐次换元，不是将两条全球曲线的 Selmer
群等同。

## 2. 一个自然的 genus $7$ 覆盖及其实际商

令

$$
 F(x)=(x^2+1)(5x^4-2x^2+1)=5x^6+3x^4-x^2+1.
$$

考虑光滑射影正规化

$$
 C:\quad y^2=x^3-x,\qquad v^2=F(x).
 \tag{2.1}
$$

用 $F/5$ 代替 $F$ 只作一个固定二次扭转；在 $p=11$ 两者的
Cartier 矩阵相同，因为 $5$ 为平方剩余。

$F$ 的六个单根均不在 $0,\pm1$，故在 $E_1$ 上给十二个简单
分歧点。$F(x)$ 在 $O$ 的极点阶为十二，是偶数。
Riemann--Hurwitz 因此给 $g(C)=7$。

两个平方根的符号作用给一个 $(\mathbb Z/2)^2$ 群，其三个
非平凡特征商依次为

$$
 \begin{aligned}
 E_1 &: y^2=x^3-x &&(g=1),\\
 C_2 &: v^2=F(x) &&(g=2),\\
 C_4 &: w^2=x(x^4-1)(5x^4-2x^2+1) &&(g=4),
 \end{aligned}                                               \tag{2.2}
$$

其中 $w=yv$。
三个商的正则微分的拉回属于不同特征空间，维数之和为七，
故正好给 $H^0(C,\Omega_C^1)$ 的直和分解。
对奇数好素数，特征投影只除以 $4$，与 Cartier 算子交换。
因此 (2.2) 也是判断这个固定覆盖的 Cartier 数据的准确分解。

$C_2$ 又有两个明确椭圆商：

$$
 E_a:Y^2=X^3-8X+32,\qquad
 E_b:Y^2=X^3-X^2+3X+5.                                     \tag{2.3}
$$

第一个商先取 $u=x^2$、$v$ 不变，再取
$X=5u+1,Y=5v$。第二个商取 $X=x^{-2},Y=v/x^3$。
其正则微分的拉回分别为 $x\,dx/v$ 和 $-dx/v$。
所以 $J(C_2)$ 的微分和 Frobenius 数据准确分成这两条椭圆曲线的
数据；不是仅凭两个 $j$ 不变量推测同源。
直接计算

$$
 j(E_a)=-3456/25,\qquad j(E_b)=128.
$$

这些商为寻找一个正确固定 Frobenius 接口提供了具体对象。
它们自身尚未与目标系数建立比较定理。

## 3. 选定微分的 Cartier 矩阵与 $p=11$ 的反例

对 $Y^2=f(x)$、$\deg f=2g+1$ 或 $2g+2$，使用正则微分基

$$
 \omega_j=x^{j-1}\frac{dx}{Y},\qquad 1\le j\le g.
$$

写 $f^{(p-1)/2}=\sum_nc_nx^n$。
由于

$$
 \omega_j=Y^{-p}x^{j-1}f^{(p-1)/2}dx,
$$

由 Cartier 的 $p^{-1}$-线性及
$\mathscr C(x^{pi-1}dx)=x^{i-1}dx$ 直接得到

$$
 \mathscr C(\omega_j)=\sum_i c_{pi-j}^{1/p}\omega_i.
 \tag{3.1}
$$

本篇曲线定义于 $\mathbb F_p$，所以矩阵正是
$H_{ij}=c_{pi-j}$；若采用 Hasse--Witt 的转置规范，以下行列式
与秩结论完全相同。

对 $C_4$ 和 $p=11$，直接展开

$$
 f(x)^5=(5x^9-2x^7-4x^5+2x^3-x)^5\pmod{11}
$$

并按 (3.1) 抽取系数，得到

$$
 H_4=
 \begin{pmatrix}
 0&6&0&10\\
 2&0&9&0\\
 0&8&0&6\\
 9&0&2&0
 \end{pmatrix}.
 \tag{3.2}
$$

按奇、偶指标重排后的两个 CM 块是

$$
 A=\begin{pmatrix}6&10\\8&6\end{pmatrix},\qquad
 B=\begin{pmatrix}2&9\\9&2\end{pmatrix},
 \qquad H_4\sim\begin{pmatrix}0&A\\B&0\end{pmatrix}.
$$

它们满足

$$
 \det A=\det B=0,\qquad
 AB=\begin{pmatrix}3&8\\4&7\end{pmatrix},
 \qquad\operatorname{tr}(AB)=10\ne0.                       \tag{3.3}
$$

于是 $H_4$ 的稳定秩是二。
同一计算给 $C_2$ 的矩阵为
$\operatorname{diag}(9,6)$，分别与
$a_{11}(E_b)=-2$、$a_{11}(E_a)=6$ 一致。
$E_1$ 在 $11$ 处超奇异，所以整个 $C$ 的稳定 Cartier 秩为四；
去掉 $E_1$ 后的六维 Prym 部分仍然不是 ordinary。

但目标真实系数已由全局证书认定为

$$
 \beta_{12}=\frac{b_{12}(17)}{17^2}
           =\frac{32227}{50400}\equiv7\pmod{11}.
 \tag{3.4}
$$

所以它是单位，而 (3.3) 的两个行列式均为零。
这一事实严格排除
“目标系数等于这两个行列式之一（或其乘积）乘一个单位”
的直接识别，也排除把该 Prym 的 ordinarity 当成目标单位条件的
等价表述。

全部有限算式在
[check-degree17-cover-cartier.py](../scripts/check-degree17-cover-cartier.py)
中以整数多项式运算重现。

## 4. 尚可研究、但必须另证的比较

反例不排除某个其他 Cartier entry、minor、线性组合，或
覆盖 ordinary 时推出目标单位的单向充分条件。
但是这些都需要一个把真实截面系数送到相应有限维空间的映射；
仅有相同的低阶 torsion 零点不足以构造该映射。

真实对数导子包含 $17\zeta_E$。
[惰性连接笔记](2026-11-12-inert-theta-diagonal-and-curvature.md)
§4 已精确记录其 $p$ 次算子及未消去的 $\partial_U$ 项，
§3 也说明整个相关级数不是某个固定有理线性微分方程的解。
因此不能在改用 (2.1) 的微分时默默删除这一连接。
这里只排除了实际算过的一种最直接识别，并保留精确的矩阵作为
下一次比较的检验条件。

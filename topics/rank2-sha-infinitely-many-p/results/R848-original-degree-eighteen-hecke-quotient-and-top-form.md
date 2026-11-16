# R848 — 原 degree18 模曲线商、三个 Hecke 邻点与最高微分的显式商模型

日期：2026-11-16。**状态：下列原模曲线覆盖、实际 Hecke 邻点、函数域商、微分归一及曲线推前次数已证明。**

本篇保留 R841/R847 的同一实际映射
$\Phi=(F,a q_0,a q_2)$。
将其完整 $C_3\times S_3$ 对称落实为原
$X_0(10404)\to X_0(867)$ 的 degree18 覆盖，
并把目标 $E_0^3$ 的同一个商写成一个明确三维方程。
这提供原曲线的具体商来源，不将该商方程预先认作
R814 的 canonical cycle，也不删掉原最高 Chow 投影。

## 1. 固定原曲线、映射和全部常值

记
$$
K=\mathbf Q(\omega),\quad M=2601,\quad N=4M=10404,\quad
X=X_0(N),\quad C=X_0(M),\quad B=X_0(M/3)=X_0(867).
$$
先在一个包含 $K$ 及所有当前实际 Hom 定义域的固定数域 $L$
上证明；原全部 Galois–Artin 系数仍在原有限组合中保留。
目标固定为
$$
A=E_0^3,\qquad E_0:y^2=x^3+1,\qquad
[\omega](x,y)=(\omega x,y).
$$

对 R841 的一个生成整个 $A$ 的实际项，记
$$
\Phi=(F,P_1,P_2),\qquad
P_1=a q_0,\quad P_2=a q_2,\quad
q_0(z)=z,\quad q_2(z)=4z.
\tag{1}
$$
三个坐标在 $\infty$ 取原点。
R847 已通过原 optimal $E_f$ 和有理 torsion 为零的完整论证，
消掉 $Fw_4$ 的 cusp 常值，给**实际曲线等式**
$$
\Phi S=L_2\Phi,\qquad
\Phi w_4=W_2\Phi,\qquad
\Phi R=[\omega]^{\times3}\Phi,
\tag{2}
$$
其中
$$
S(z)=z+\tfrac12,\qquad R(z)=z+\tfrac13,
$$
$$
L_2=
\begin{pmatrix}-1&0&0\\0&-1&-1\\0&0&1\end{pmatrix},
\qquad
W_2=
\begin{pmatrix}-1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\tag{3}
$$
因此这里没有尚待平均消去的平移。

## 2. 中间退化映射恰是完整 $S_3$ 覆盖

考虑原已有的中间映射
$$
q_1:X\longrightarrow C,\qquad z\longmapsto2z.
\tag{4}
$$
令 $A_2=\operatorname{diag}(2,1)$。直接共轭原群得到
$$
\boxed{
A_2\Gamma_0(4M)A_2^{-1}
=\Gamma_0(M)\cap\Gamma(2).
}
\tag{5}
$$
确实共轭后的矩阵为
$\left(\begin{smallmatrix}a&2b\\c/2&d\end{smallmatrix}\right)$，
其中 $c/2$ 被 $2M$ 整除。
反过来，$\Gamma_0(M)$ 中模2为单位阵的矩阵准确满足这些条件。

由于 $M$ 为奇数，$\Gamma_0(M)$ 模2满射到
$\operatorname{SL}_2(\mathbf F_2)$：
上幺幂矩阵
$\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$
与下幺幂矩阵
$\left(\begin{smallmatrix}1&0\\M&1\end{smallmatrix}\right)$
的约化生成该群。
因此 (5) 是正规指数6子群，给
$$
\boxed{
q_1\text{ 是 degree6 的几何 Galois 覆盖，deck 群为 }S_3.
}
\tag{6}
$$

这就是原 $S,w_4$，而非另选的抽象 $S_3$。
对 R831 的矩阵
$\mathcal W=\left(\begin{smallmatrix}4&-1\\4M&1-M\end{smallmatrix}\right)$，
有
$$
A_2SA_2^{-1}=
\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
\frac12A_2\mathcal W A_2^{-1}
=\begin{pmatrix}2&-1\\M&(1-M)/2\end{pmatrix}\in\Gamma_0(M).
\tag{7}
$$
中心标量 $1/2$ 不改变曲线作用。
因 $M\equiv1\pmod4$，(7) 模2给两个不同 transpositions，
所以它们生成 (6) 的整个 deck 群。
尤其
$$
q_1 S=q_1,\qquad q_1w_4=q_1.
\tag{8}
$$

再取
$$
q_3:C\longrightarrow B,\qquad z\longmapsto3z.
$$
同样有
$$
\operatorname{diag}(3,1)\Gamma_0(M)\operatorname{diag}(3,1)^{-1}
=\Gamma_0(M/3)\cap\Gamma^0(3).
\tag{9}
$$
由于 $3\mid M/3$，右边在 $\Gamma_0(M/3)$ 中正规、指数3：
模3的上三角群除以其对角 $\{\pm I\}$ 正是上幺幂 $C_3$。
其原 deck 生成元是 $R_C:z\mapsto z+1/3$。
这也是 R841 已付的同一个三阶商。

原 $q_1R=R_C^2q_1$，故
$$
q_6:=q_3q_1:X\longrightarrow B,\qquad z\longmapsto6z
\tag{10}
$$
由 $R,S,w_4$ 全部保持。
R847 已付它们生成忠实的 $G=C_3\times S_3$，阶18；
而 $\deg q_6=3\cdot6=18$。
因此在 $L$ 上准确有
$$
\boxed{
X/G=B,\qquad
L(X)^G=L(B),\qquad\deg q_6=18.
}
\tag{11}
$$
这不是把一个任意原像曲线的商预先当成模曲线；
(11) 说的是完整原源 $X$。

## 3. 后两坐标来自同一个椭圆曲线的三个二同源邻点

令
$$
P_3=a q_0S .
$$
在 $q_1$ 的基点 $z'=2z$ 上，原 $T_2$ 的三个实际 Hecke 邻点是
$$
2z'=4z,\qquad z'/2=z,\qquad (z'+1)/2=z+\tfrac12.
\tag{12}
$$
故它们经同一个 $a:C\to E_0$ 的像准确为
$P_2,P_1,P_3$，包含原 cyclic-$M$ 结构。
这里二同源发生在原模解释的椭圆曲线之间；
不能把 $P_i\in E_0$ 本身叫作 $E_0$ 的二挠点或另一个二同源核。

原整个有理 $g$-packet 在2处未分歧且有 CM，2在 $K$ 惰性，
所以其全部系数嵌入均满足 $a_2(g)=0$。
权一 Hom 的忠实性给 $aT_2=0$ 于实际 Jacobian 同态。
(12) 的和因此是常值；在原 cusp $\infty$ 三点均到 $\infty$，
而 $a(\infty)=0$，故常值准确为零：
$$
\boxed{P_1+P_2+P_3=0.}
\tag{13}
$$
这也恢复 (2) 的 $P_1S=-P_1-P_2$，并支付了该恒等式的
完整原 Hecke 来源。

$S$ 交换 $P_1,P_3$、固定 $P_2$；
$w_4$ 交换 $P_1,P_2$、固定 $P_3$。
第一坐标 $F$ 则按这份 $S_3$ 的 sign 作用。
这些全部是实际点映射，$q_2$ 的微分仍为
$4g(Q^4)dQ/Q$，没有把点映射乘以4。

因为当前像生成整个 $A$，三个 $P_i$ 在泛点互异且无两点互为相反数。
否则产生 $P_1,P_2$ 的非零整数线性关系，迫原像位于真阿贝尔子簇。
由椭圆平面三次的群律，(13) 给泛点处唯一非竖直直线
$$
y=mx+n
\tag{14}
$$
通过 $P_1,P_2,P_3$，其中
$$
m=\frac{y_2-y_1}{x_2-x_1},\qquad
n=\frac{x_2y_1-x_1y_2}{x_2-x_1}.
\tag{15}
$$
其三个横坐标为
$$
h(x)=x^3-m^2x^2-2mnx+1-n^2
\tag{16}
$$
的全部根。
若 $m$ 恒为零，则 $y_1=y_2$，从 $E_0$ 方程得到
$x_2=\omega^i x_1$ 的某个恒定分支，
即 $P_2=[\omega^i]P_1$，仍与生成性矛盾。
所以后文的 $m\ne0$ 开集确实遇到原曲线泛点。

## 4. 同一个目标的准确 $S_3$ 函数域商

先在整个 $A$ 上作计算，而非只在一个特殊曲线上猜方程。
写第一坐标为
$$
F=(X,Y),\qquad Y^2=X^3+1,
$$
并固定有向 Vandermonde
$$
\delta=(x_1-x_2)(x_2-x_3)(x_3-x_1).
\tag{17}
$$
$S_3$ 固定 $m,n,X$，并同时以 sign 作用于 $Y,\delta$。
因此
$$
z_0=Y\delta
$$
是不变函数。

将 (16) 的完整三次判别式展开，得到
$$
\boxed{
\delta^2=D(m^3,n),\qquad
D(u,n)=4u^2+4un(9-n^2)-27(1-n^2)^2.
}
\tag{18}
$$
例如使用三次式 $x^3+ax^2+bx+c$ 的判别式
$a^2b^2-4b^3-4a^3c-27c^2+18abc$，
代入 $a=-m^2,b=-2mn,c=1-n^2$ 即得全部常数。

泛型直线与 $E_0$ 的交点有三个；
有序取两个点共有六种，第三点由 (13) 决定。
故 $L(E_0^2)/L(m,n)$ 的次数为6，正是上述 $S_3$。
再加入独立的第一椭圆坐标，得到
$[L(A):L(m,n,X)]=12$。
不变子域的次数因而为2。
而
$$
z_0^2=(X^3+1)D(m^3,n)
$$
在 $L(m,n,X)$ 上确非平方：作为 $X$ 的函数有单零点。
于是准确得到整个函数域，而非仅一个子域：
$$
\boxed{
L(A)^{S_3}=L(m,n,X,z_0),\qquad
z_0^2=(X^3+1)D(m^3,n).
}
\tag{19}
$$

## 5. 再取原三阶中心作用的显式三维商

原 $R$ 在目标同时施 $[\omega]$。
由 (14)–(17)，其准确作用为
$$
m\longmapsto\omega^2m,\qquad n\longmapsto n,\qquad
X\longmapsto\omega X,\qquad Y\longmapsto Y,\qquad
\delta\longmapsto\delta.
\tag{20}
$$
定义同一不变函数
$$
u=m^3,\qquad v=mX,\qquad w=u z_0=uY\delta .
\tag{21}
$$
则
$$
\boxed{
\mathscr Y:\quad
w^2=u(v^3+u)
\bigl(4u^2+4un(9-n^2)-27(1-n^2)^2\bigr)
}
\tag{22}
$$
是 $A/G$ 的一个准确仿射双有理模型。

为支付“整个商”，由 $u,v,n,w$ 添入 $m$ 后，
可用
$$
m^3=u,\qquad X=v/m,\qquad z_0=w/u
$$
恢复 (19) 的全部函数。
中心 $R$ 在 $m$ 上有准确三阶作用，故该扩张次数恰为3。
于是
$$
\boxed{L(A)^G=L(u,v,n,w),\quad\text{唯一关系为 (22)}.}
\tag{23}
$$
(22) 的平方关系也确为不可约：在 $v$ 的一般单根处右侧为奇数阶。
这同时验证相应三维函数域，没有额外选择一个分支。

方程系数都在 $\mathbf Q$。
这里的几何识别在包含实际 Hom 定义域的 $L$ 上进行，
没有改变原 Artin 角色或把所有单项重新指定成一个角色。
(22) 只描述稠密开集；商的边界、奇点及原 Chow 投影仍需按原来源处理。

## 6. 最高三微分的全部绝对常数

取目标原规范不变微分
$$
\Omega_A=\frac{dX}{2Y}\wedge
          \frac{dx_1}{2y_1}\wedge\frac{dx_2}{2y_2}.
$$
在 (14) 的泛点，对 (16) 微分给
$$
\frac{dx_i}{2y_i}=\frac{x_i\,dm+dn}{h'(x_i)}.
$$
由 (17) 的取向，
$$
h'(x_1)h'(x_2)=(x_1-x_2)\delta .
$$
所以
$$
\frac{dx_1}{2y_1}\wedge\frac{dx_2}{2y_2}
=\frac{dm\wedge dn}{\delta},
\qquad
\Omega_A=\frac{dX\wedge dm\wedge dn}{2z_0}.
\tag{24}
$$
又
$$
du=3m^2dm,\qquad dv=m\,dX+X\,dm,\qquad
dX\wedge dm=\frac{dv\wedge du}{3u}.
$$
结合 $w=uz_0$，得到
$$
\boxed{
\Omega_A=
\frac{dv\wedge du\wedge dn}{6w}
}
\tag{25}
$$
的准确拉回身份，楔积次序如式中固定。
这是 (22) 上的有理三形式；在商的自由作用开集上，
它就是原不变三形式的下降。

特别，(25) 的 $1/6$ 来自显示的坐标变换，
不是再次对原 cycle 作一个 $1/6$ 平均。
它不取代原模曲线上的 $6^{-2}$、$12^{-2}$、
CM period 或临界 Hecke projector。

## 7. 原曲线在 $X_0(867)$ 上的真实函数及次数

将 (15)、(17)、(21) 限制到同一个实际 $\Phi$。
因 (2) 精确等变，四个函数 $u,v,n,w$ 在原 $X$ 上均为 $G$-不变。
由 (11)，它们来自同一个原
$$
B=X_0(867)
$$
上的有理函数，且满足 (22)。
因此原 $\Phi$ 诱导一个实际态射
$$
\bar\Phi:B=X/G\longrightarrow A/G,
\tag{26}
$$
其在 (22) 的稠密开集上由这四个已显示的函数给出。
(26) 的目标是完整的 projective 有限商；
没有声称完整射影曲线有一个非恒定的全局态射到该仿射开集。

令 $D$ 仍为原像正规化。
R847 的生成性保证 $G$ 在 $D$ 上忠实，
故 $[L(D):L(D)^G]=18$。
若 $\delta_\Phi=\deg(X\to D)$，函数域塔精确给
$$
\boxed{
\delta_\Phi
=[L(X):L(D)]
=[L(B):L(D)^G].
}
\tag{27}
$$
所以 (26) 到其像正规化的次数仍是同一个 $\delta_\Phi$；
没有因商掉 $G$ 免费丢失原有限推前次数。

令 $\pi:A\to A/G$ 为完整有限商。
对实际曲线的正常 proper pushforward，有
$$
\boxed{
\pi_*\Phi_*[X]=18\,\bar\Phi_*[B].
}
\tag{28}
$$
这直接来自 $\pi\Phi=\bar\Phi q_6$ 与 $\deg q_6=18$，
在奇异商的通常 Chow 群中也只使用合法的 proper pushforward。
此外每个 $g\in G$ 都满足
$$
g_*\Phi_*[X]=\Phi_*[X],
$$
因为原源上有对应的实际自同构。
这些等式不需要另一个自由选择的平移或角色平均。

必须区分 (28) 与原最高投影：
原对象仍为 $\Pi\Phi_*[X]$，其中 $\Pi$ 在 $A$ 上的原位置未变。
本篇没有把 $\Pi$ 删除，也没有免费构造奇异商上的同名投影，
更没有将 (28) 自动当成到 R814 canonical cycle 的同构。
若经商的光滑模型作这一比较，
必须实际运输该投影及所有边界贡献。

## 8. 对原完整端点的接续

现已对原有限 polarization 的每个生成项支付：

- 源的真实 degree18 商准确是 $X_0(867)$；
- 三个点来自同一个原 $T_2$ 的三个二同源邻点，经同一 $a$ 取像；
- 目标整个 $C_3\times S_3$ 函数域商是 (22)；
- 原最高三微分的绝对归一为 (25)；
- 原曲线到其像的次数按 (27) 保持，商推前按 (28) 保留18。

原全部 $\Gamma_f,\Gamma_g,\Gamma_h$、
Hom 平均与 polarization 系数、有限 Artin 权重继续逐项保留。
R831 的 $6^{-2}$、$X_1$ 的 $12^{-2}$ 和 $1632/816$ 原样不动。

本篇因此给出了一个可作后续比较的**指定**商曲线与最高微分，
但尚未把它辨认为某个已知 canonical cycle。
亏格至少七的原项及其总和、原 critical Abel–Jacobi 非零、
四原中央的跨素数非消失仍需继续证明。
没有使用任何高余维 realization 忠实性或未证 Chow 维数，
也没有新增数值扫描。

## 9. 依赖

- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)：
  原 $q_0,q_1,q_2$、完整 Hecke 层级、partial $W_4$ 与全部旧空间次数。
- [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)：
  原整个 rational packet、精确 $R,S$、Hom 平均/polarization 与真实三阶商。
- [R847](R847-original-dyadic-s3-and-genus-seven-lower-bound.md)：
  每个实际 $F$ 的 cusp 常值为零、完整 $C_3\times S_3$ 曲线作用和生成性。
- 本篇 (5)–(11)、(18)–(25)、(27)–(28) 均已显示自含计算与次数论证；
  不从一个相似的模块方程或有限 $j$ 扫描推定原来源。

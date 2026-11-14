# R150 附录：空谱首锚的 Newton 次数优势与普通双慢多项式

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已核查真实余数除法、系数环消元最高项、空谱逆与全部跨核自然域。
状态：已证明，完整证明。使用真实混合最大图与实际最高系数单位，处理普通点态 $f(v)-g(u)$。全部慢 Bell 修正留在证明中，不要求它们属于 $\mathcal G$。

## 1. 主结论与范围扣除

取
$$
u=a_*+\sum_j a_j\chi_j,\qquad
v=c_*+\sum_j c_j\chi_j,
\qquad a,c\in\ell^2(\mathbb C),
$$
且两者非常数。
设 $u$ 的实际 first $X_u$ 空谱；
一个已经充分的系数条件是
$$
a\notin\ell^1,\qquad
\sum_j\bigl(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\bigr)<\infty
\quad\text{对某个 }\theta.
\tag{1.1}
$$
记
$$
j_u=\min\{j:a_j\ne0\},\qquad
j_v=\min\{j:c_j\ne0\},
$$
并假设
$$
\boxed{j_u\le j_v.}
\tag{1.2}
$$
所有物理支持及相位可以任意重叠。

给任意非恒定标量多项式
$$
g,f\in\mathbb C[z],\qquad
p=\deg g,\quad m=\deg f,
$$
假设
$$
\boxed{p>m\ge1.}
\tag{1.3}
$$

**定理 1。**
对每个 $\lambda\in\mathbb C$ 及任意复 $\ell^2$ 指数权
$$
w=b_*+\sum_j b_j\chi_j,\qquad b\in\ell^2,
$$
都有
$$
\boxed{[f(v)-g(u)-\lambda]e^w\text{ 非零且对原 }A\text{ 循环}.}
\tag{1.4}
$$
不要求主行或第二行的排序、衰减、熵预算或模 $\ell^1$ 独立。

旧 [R150](R150-empty-spectrum-anchor-rectangular-polynomial-cyclicity.md)
要求非零矩形角及另一方向最高系数的首位平移互素；
$f(V)-g(U)$ 的 $U^pV^m$ 角系数为零，不能直接套用该主定理。
旧 [R155](R155-empty-anchor-bounded-auxiliary-polynomials.md) 要求全部其他模式有界；这里 $v$ 可为独立的非可和 first。
[R189 双方向附录](R189-appendix-one-empty-anchor-two-additive-direction-kernel-elimination.md)
已处理 $\mathcal G[X,Y]$，
但普通点态多项式的 Bell 系数一般只在 $\mathcal A$，不在 $\mathcal G$。
本稿以一个最高系数为实际单位的消元式绕过这一差别，
不改变快系数代数的定义。

## 2. 倾斜 first、真实 Bell 系数与闭图

令
$$
X=X_{u,b},\qquad Y=X_{v,b},\qquad \xi=e^w.
$$
[R176 §10](R176-natural-polynomial-maximal-graphs-and-bell-domains.md) 与
[R186 §§2–7、10](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)
给真实倾斜闭域、全部混合自然词和
$$
X=X_u+H_{a,b},\qquad H_{a,b}\in\mathcal A,\quad\chi(H_{a,b})=0.
$$
因此 $X$ 仍空谱，且
$$
L=X^{-1}\in\mathfrak C:=\{A\}'
$$
有界、单射、稠密像、拟幂零。

置
$$
h=2^{j_u},\quad \alpha=a_{j_u}\ne0,\quad
\tau=e^{-2b_{j_u}}\ne0,\quad d=d_{j_u}.
$$
由 (1.2)，两个模式的一切非零系数都位于 $j_u$ 之后。
故其全部真实倾斜 Bell 系数属于
$$
\mathcal A_h=\overline{\mathbb C[I,A^h]}.
\tag{2.1}
$$
这一归属来自局部归一化 Bell 乘积中所有更早位的因子准确为 $I$；
更早的指数权系数不会产生额外低位因子。

记相应单模式 Bell 多项式为
$$
\mathcal U(x)=P_{g,u,b}(x),\qquad
\mathcal V(y)=P_{f,v,b}(y).
$$
它们满足
$$
\mathcal U(X)\xi=g(u)e^w,\qquad
\mathcal V(Y)\xi=f(v)e^w,
\tag{2.2}
$$
全部系数在 $\mathcal A_h$。
若 $g_p,f_m$ 是标量首项系数，
则 $\mathcal U$ 的最高两项是
$g_px^p+g_{p-1}x^{p-1}$，
$\mathcal V$ 的最高两项是
$f_my^m+f_{m-1}y^{m-1}$；
第二项仍是标量，因为真实倾斜 Bell 的一次修正为零。

归一化为
$$
V(y)=f_m^{-1}\mathcal V(y),\qquad
U(x)=f_m^{-1}(\mathcal U(x)+\lambda I),
$$
$$
P(x,y)=V(y)-U(x).
\tag{2.3}
$$
于是 $V$ 关于 $y$ 首一、次数 $m$；
$U$ 关于 $x$ 的次数为 $p$，首项
$u_p=g_p/f_m\ne0$，次高系数同样为标量。

用 R186 的共同正则器定义 $P(X,Y)$ 的规范最大闭实现 $\mathsf P$。
它是自然混合图的闭包且 $C$ 自伴；
不把自然和的原域直接宣称为闭域。
$\xi$ 属于全部实际混合词域，且
$$
\mathsf P\xi
=f_m^{-1}[f(v)-g(u)-\lambda]e^w.
\tag{2.4}
$$
R186 的循环图核心表明，只需证明 $\ker\mathsf P=0$。

## 3. 每个系数的实际首位除法

固定 dyadic $\zeta$，记 $\gamma=\gamma_\zeta$。
真实同域协变给
$$
\gamma X=X+D_X,\qquad
\gamma Y=Y+D_Y.
$$
由首位次序，
$$
D_X=A^h d_X,\qquad
D_Y=A^h d_Y,\qquad d_X,d_Y\in\mathcal A_h,
\tag{3.1}
$$
其中这些商为实际有限解析演算，
而且
$$
\boxed{
\chi(d_X)=-\frac{2\alpha\tau}{d}(\zeta^h-1).
}
\tag{3.2}
$$
$d_Y$ 的字符允许为零。

[R124 §2](R124-dyadic-residue-factorization-and-order-one-kernels.md)
的真实 residue 分解以及 [R139 §1](R139-analytic-head-tail-algebra-gauge-kernels.md)
对尾代数的同一计算给：
对每个 $E\in\mathcal A_h$，
$$
\gamma E-E=A^h E_\zeta,\qquad E_\zeta\in\mathcal A_h.
\tag{3.3}
$$
$h=1$ 也用 R124 的原分解。
这里调用的是实际有界分解，
不是仅从形式最低阶为 $h$ 推断可以有界除以 $A^h$。
具体地，若 $\zeta$ 的阶 $n>h$，实际余数分解只有
$E=\sum_{\ell=0}^{n/h-1}A^{\ell h}E_{\ell h}$，
其中 $E_{\ell h}\in\mathcal A_n$；于是
$
E_\zeta=
\sum_{\ell=1}^{n/h-1}(\zeta^{\ell h}-1)A^{(\ell-1)h}E_{\ell h}
\in\mathcal A_h.
$
零余数被差严格消去。若 $n\le h$，则可取 $E_\zeta=0$。

定义
$$
P_\zeta(x,y)
=(\gamma V)(y+D_Y)-(\gamma U)(x+D_X).
$$
由 (3.1)–(3.3) 及有限幂差展开，
有实际有界系数多项式
$$
\boxed{
P_\zeta-P=A^h Q_\zeta,\qquad
Q_\zeta(x,y)=H_\zeta(y)-W_\zeta(x),
}
\tag{3.4}
$$
其中
$$
\deg H_\zeta\le m-1,\qquad
\deg W_\zeta=p-1.
$$
当 $\zeta^h\ne1$ 时，$W_\zeta$ 的最高系数准确为
$$
\boxed{w_\zeta=p\,u_p\,d_X\in\mathcal A_h^\times.}
\tag{3.5}
$$
理由是：$U$ 的最高两项系数均为标量，
所以系数共轭差不能贡献 $x^{p-1}$；
$x^p$ 的平移恰给 $p u_pD_Xx^{p-1}$。
所有更低 Bell 项都至多贡献 $x^{p-2}$。
(3.2) 使 (3.5) 的字符非零，
所以它是实际 Banach 代数单位，不只是形式非零。

R186 的共同域协变还给
$$
\mathsf P_\zeta=U_\zeta\mathsf P U_\zeta^*.
\tag{3.6}
$$

## 4. 一个系数环上的有限消元引理

**引理 2。**
设 $\mathcal B$ 为任意含单位交换代数，
$$
V(y)=y^m+\sum_{j<m}v_jy^j,\qquad
U(x)\in\mathcal B[x],\quad\deg U\le p,
$$
$$
H(y)\in\mathcal B[y],\quad\deg H\le m-1,
$$
$$
W(x)=w x^{p-1}+\text{低次项},\qquad p>m.
$$
置
$$
P=V(y)-U(x),\qquad Q=H(y)-W(x).
$$
则存在有限多项式 $A_0,B_0\in\mathcal B[x,y]$ 及
$E\in\mathcal B[x]$，使
$$
E=A_0P+B_0Q,
\tag{4.1}
$$
并且
$$
\boxed{
E(x)=(-w)^m x^{m(p-1)}+\text{更低 }x\text{ 次项}.
}
\tag{4.2}
$$

证明。由于 $P$ 关于 $y$ 首一，
$$
\mathcal B[x,y]/(P)
$$
是基为 $1,y,\ldots,y^{m-1}$ 的自由 $\mathcal B[x]$ 模。
令 $C(x)$ 为乘 $y$ 的矩阵，
则乘 $Q$ 的矩阵为
$$
M_Q(x)=H(C(x))-W(x)I_m.
$$
置 $E(x)=\det M_Q(x)$。
伴随矩阵乘法及对首一 $P$ 的带余除法给 (4.1)；
可以取 $\deg_yB_0\le m-1$。
这一步不使用一般二变量互素推出单位理想。

下面准确计算最高 $x$ 次数。
赋权
$$
\operatorname{wt}x=m,\qquad \operatorname{wt}y=p.
$$
在关系
$$
y^m=U(x)-\sum_{j<m}v_jy^j
$$
中，右边各项的权不超过左边的 $mp$。
因此，$H(C)$ 的第 $s,j$ 个矩阵元（$0\le s,j<m$）
所含任何 $x^\ell$ 都满足
$$
m\ell+ps\le p(j+m-1).
\tag{4.3}
$$

展开行列式，并将每个因子拆为 $H(C)$ 项或 $-W I$ 项。
若一个行列式乘积选了 $k\ge1$ 个 $H(C)$ 因子，
其余 $m-k$ 个必为对角 $-W$ 因子。
排列中的全部行列指标差总和为零，
而对角项的指标差也为零；
把 (4.3) 在所选 $k$ 项上相加，得到该乘积的 $x$ 次数至多
$$
\frac{kp(m-1)}m+(m-k)(p-1).
$$
它比 $m(p-1)$ 小
$$
k\left(\frac pm-1\right)>0.
$$
次数为整数，故这些项均为严格低次。
唯一可能贡献最高次的是全部取 $-W I$，
其行列式为 $(-W)^m$，最高系数恰为 $(-w)^m$。
(4.2) 得证。

该证明在任意交换系数环内成立；
不需要对实际算子系数取根、选 Puiseux 分支或施加标量谱代入。

## 5. 消元最高系数是真单位，空谱逆完成有界化

对 $\zeta^h\ne1$，
将引理 2 用于 (2.3)、(3.4)。
得到
$$
E_\zeta(x)
=A_\zeta(x,y)P(x,y)+B_\zeta(x,y)Q_\zeta(x,y),
$$
$$
D=m(p-1),\qquad
E_\zeta(x)=e_{\zeta,D}x^D+\cdots+e_{\zeta,0},
$$
其中全部系数在 $\mathcal A_h$，且
$$
e_{\zeta,D}=(-w_\zeta)^m\in\mathcal A_h^\times.
\tag{5.1}
$$
结合 (3.4)，
$$
\boxed{
A^hE_\zeta
=(A^hA_\zeta-B_\zeta)P+B_\zeta P_\zeta.
}
\tag{5.2}
$$

利用实际有界逆 $L=X^{-1}$，在足够深的自然域上有
$$
L^DE_\zeta(X)
=
\rho_\zeta
:=
e_{\zeta,D}+\sum_{k<D}e_{\zeta,k}L^{D-k}.
\tag{5.3}
$$
将其写成
$$
\rho_\zeta=e_{\zeta,D}(I+LK_\zeta),
\qquad K_\zeta\in\mathfrak C.
$$
$L$ 拟幂零且与 $K_\zeta$ 交换，
所以 $LK_\zeta$ 拟幂零，$I+LK_\zeta$ 可逆。
因此
$$
\boxed{\rho_\zeta,\rho_\zeta^{-1}\in\mathfrak C.}
\tag{5.4}
$$
R88 使两者保持每个闭 $A$ 不变空间，
从而
$$
\rho_\zeta M=M.
\tag{5.5}
$$

等价地，最高单位自然多项式 $E_\zeta(X)$ 的实际有界逆为
$L^D\rho_\zeta^{-1}$。
本证明只需有界单位 (5.4)，
没有假设消元系数属于 $\mathcal G$，
也没有将一般全空间稠密像外推到未知限制。

## 6. 完整混合深域上的跨核配对

令
$$
M=\ker\mathsf P.
$$
它闭且 $A$ 不变，但不预设 $M$ 整体处在两个 first 的自然域。

固定 $\zeta^h\ne1$，取 R186 的一个共同正则器 $R$。
选择有限 $N$，覆盖 (5.2) 的所有自然乘积、$E_\zeta$ 的次数和全部中间词。
于是
$$
f\in R^NM,\qquad
g\in U_\zeta R^NM
$$
时，两者处在全部必要的真实混合域，且
$$
P(X,Y)f=0,\qquad P_\zeta(X,Y)g=0.
$$
$L^D$ 为有界交换子，保持全部这些域。
将 (5.2) 作用于 $f$，左乘 $L^D$，
再用原双线性配对
$$
B(f,g)=\int f(y)g(-1-y)\,d\mu(y),
$$
得到
$$
\begin{aligned}
B(A^h\rho_\zeta f,g)
&=
B\!\left(
P_\zeta(X,Y)L^DB_\zeta(X,Y)f,g
\right)\\
&=
B\!\left(
L^DB_\zeta(X,Y)f,P_\zeta(X,Y)g
\right)=0.
\end{aligned}
\tag{6.1}
$$
这里只有原 $H$ 上完整 $C$ 自伴的 $\mathsf P_\zeta$ 被移过配对；
每个输入均已核准在其自然域中。

$R^NM$ 与 $U_\zeta R^NM$ 分别在 $M$ 与 $U_\zeta M$ 中稠密，
故 (6.1) 延为
$$
B(A^h\rho_\zeta M,U_\zeta M)=0.
$$
由 (5.5) 及原 $A^h$ 在每个不变限制上的稠密像，
$$
\boxed{B(M,U_\zeta M)=0\qquad(\zeta^h\ne1).}
\tag{6.2}
$$

所以每个反射乘积 $f(y)g(-1-y)$ 的 Fourier 支撑包含于有限群 $\mu_h$，
并在模 $h$ 柱上为常数。
若 $M\ne0$，严格正的 odometer 权及遍历性使其总本质支撑全测。
逐柱选择非零反射乘积，再比较任意向量与固定另一因子的乘积，
得每个柱上的限制维数至多1，因而 $\dim M\le h$。
这与单射拟幂零 $A$ 不允许非零有限维不变空间矛盾。

故 $M=0$。
完整 $C$ 自伴给稠密像，(2.4) 和真实循环图核心完成 (1.4)。

## 7. 普通不可约双慢三次例子

取任意 $\frac12<\sigma\le1$，
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j.
$$
第一条行为空谱相位类，
第二条行的正负质量均不可和，属于全平面谱分支。
两行模 $\ell^1$ 独立且全部支撑重叠，
首位均为0。

取 $g(U)=U^3$、$f(V)=V^2$。
定理 1 给
$$
\boxed{
(v^2-u^3-\lambda)e^w
\text{ 对每个 }\lambda\in\mathbb C
\text{ 和每个复 }\ell^2\text{ 指数权 }w\text{ 循环}.
}
\tag{7.1}
$$
形式 $V^2-U^3-\lambda$ 对每个 $\lambda$ 都不可约，
因为 $U^3+\lambda$ 不是 $\mathbb C[U]$ 中的平方。

(7.1) 是普通点态式。
实际证明中仍使用
$$
P(X,Y)=Y^2+B_{v,2}-X^3-3B_{u,2}X-B_{u,3}-\lambda I
$$
的全部慢 Bell 系数；
它们在消元中进入 $\mathcal A_h$ 系数，未被删除，也未改称快系数。
这区别于此前需要显式慢辅助修正的
$\mathfrak F_{V^2-U^3-\lambda}$。

## 8. 边界

1. $p>m$ 使 (4.3) 的最高次数比较严格。
   相同次数或反向次数需要另核消元最高系数，不能直接省略条件。
2. $j_u\le j_v$ 保证所有系数差都有同一个真实 $A^h$ 因子，
   且空谱方向的首项商为单位。
3. 指数权、物理排列和慢行幅度均无额外预算；
   实际共同域由 R186 提供，不从形式交换推断。
4. 结论不自动扩成
   $[f(v)-g(u)-\lambda]^r e^w$ 的全部点态幂。
   对这种新符号，混合 Bell 项及重复最高曲线需要另作消元。
5. 两个独立全平面 first 的一般单核仍未由这里处理。
6. R236 最新非可和二分与全阶 Sylvester 稿处理
   $F_q+v_c-\lambda$ 的比较辅助范围；
   本文没有重新登记这些单主行已闭情形。

完整 Hilbert ISP 继续保留。

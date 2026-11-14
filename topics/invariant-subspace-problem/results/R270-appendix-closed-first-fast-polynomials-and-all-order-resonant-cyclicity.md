# R270 第三附录：闭 first 的快系数多项式与全部阶共振消去

日期：2026-11-13（UTC）。作者：kernel；Astra-ISP-1cf8c51d 复核。
状态：已证明。主行只要求 $\ell^2$，不需要 R268 的熵条件。本稿是原 Haar 模型的正向中间结果；完整普通 Hilbert ISP 仍未完成。

**范围订正（2026-11-13）：** §§1–8 是已有排核定理的独立闭图重证。[R183](R183-fast-coefficient-nonmonic-polynomials-and-closed-fraction-field.md) 已处理 $a\in\ell^2\setminus\ell^1$、有界倾斜 $H\in\mathcal A$ 且 dyadic 增量属于 $\mathcal G$ 的全部非首一快系数多项式；实际 $X_b$ 符合这些条件。[R152](R152-fast-gauge-increments-analytic-germs-and-closed-quotients.md) 定理 1.3、§7 则覆盖 $a\in\ell^1$ 的有界分支，仍保实际非零条件。因此不再将 §§1–8 计为新增排核范围。本文 §§9–10 保留的应用是明确全阶共振 $F_p$ 的实际 Bell 消去及其循环性；后续快辅助应用不受此归属订正影响。

以下重证使用全 gauge 稳定因子对应的实际闭 first 加快分式；有限放大图稠密性付最大域，再由乘法代数和 odometer 遍历性迫常数。没有给非可和 first 虚构形式常数项。

## 1. 主定理与实际输入

固定任意
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
w=b_*+\sum_{j\ge0}b_j\chi_j,\qquad a,b\in\ell^2(\mathbb C),
$$
并令 $X=X_b$ 为 R176 的实际倾斜闭 first。
记
$$
\Gamma=\bigcup_{m\ge0}\mu_{2^m},\qquad
\gamma_\zeta(T)=U_\zeta TU_\zeta^*,\qquad
\mathbb K=\operatorname{Frac}\mathcal G.
$$
$\mathcal G$ 为 R151 的四次型解析逼近代数。

**定理 1.1。** 若
$$
P(t)=t^p+\sum_{k<p}E_k t^k,\qquad E_k\in\mathcal G,\quad p\ge1,
$$
且其实际自然算子
$$
T=P(X),\qquad \operatorname{Dom}T=\operatorname{Dom}X^p
\tag{1.1}
$$
不是零算子，则
$$
\boxed{\ker T=0,\qquad \overline{\operatorname{Ran}T}=H.}
\tag{1.2}
$$
对每个属于其域的 $A$ 循环向量 $\xi$，$T\xi$ 仍循环。
特别，$P(X_b)e^w$ 循环。

最高系数也可为 $\mathcal G$ 中的实际单位：先乘其在 $\mathcal G$ 中的逆，归约到首一情形。
本稿不覆盖一般非单位最高系数的自然域。

所用已证实际事实如下。

- R176 给 $X=C_0X^*C_0$；任意有界交换系数的首一自然多项式闭且 $C_0$ 自伴，其核 $M$ 满足
  $$
  M\subset\mathcal D_\infty:=\bigcap_{n\ge0}\operatorname{Dom}X^n,\qquad
  X_M\in B(M).
  \tag{1.3}
  $$
  它还给循环域向量的图核心和
  $[T\xi]_A=\overline{\operatorname{Ran}T}$。
- R151/R153 给每个非零 $e\in\mathcal G$ 在所有有限放大不变限制上的单射稠密性，及每个快分式 $g=a/e$ 的最大闭实现
  $$
  T_g=e^{-1}a,\qquad
  \operatorname{Dom}T_g=\{x:ax\in\operatorname{Ran}e\}.
  \tag{1.4}
  $$
  在原 Haar 空间它 $C_0$ 自伴，$eH$ 是原分母图核心。
- 每个 dyadic gauge 对 $X$ 有完整域恒等式
  $$
  \boxed{\gamma_\zeta(X)=X+D_\zeta,\quad
  \operatorname{Dom}\gamma_\zeta(X)=\operatorname{Dom}X,\quad
  D_\zeta\in\mathcal G.}
  \tag{1.5}
  $$
  实际上 $D_\zeta$ 是真解析有限头：若 $\zeta^{2^h}=1$、$t_j=e^{-2b_j}$，则
  $$
  D_\zeta
  =
  \sum_{j<h}a_j
  \bigl[V(t_j\zeta^{2^j}N_j)-V(t_jN_j)\bigr].
  \tag{1.6}
  $$
  在有限柱图核心先验证，再用闭性和相反 gauge 得双向域等式。
  $D_\zeta$ 完整交换 $X$ 并保全部自然幂域。
  因而 $U_\zeta\mathcal D_\infty=\mathcal D_\infty$。

(1.5) 的增量满足
$$
D_{\zeta\xi}=D_\zeta+\gamma_\zeta(D_\xi).
\tag{1.7}
$$
不需要 $a\in\ell^1$，也没有定义 $\sum_ja_j$。

## 2. 固定 first 正则器在有限放大上的稠密性

取 R128/R140 的四个正分量预解式乘积 $R(s)$，$s>0$。
对倾斜 $X$，R176 §10.1 给
$$
R(s)\in\{A\}',\qquad R(s)\text{ 单射},\qquad
S(s):=XR(s)\in\{A\}'.
\tag{2.1}
$$
$R(s)H\subset\operatorname{Dom}X$，且固定的 $R(s)H$ 是 $X$ 的图核心。
倾斜只给 $X$ 加一个有界交换项，所以原正则器可保留。

R140 §7 的真实单位关系为
$$
R(s)=R(t)U(s,t),
\tag{2.2}
$$
其中 $U(s,t)$ 及其逆是有界交换子；$R(s)\to I$ 强收敛。

固定有限 $d$ 与闭 $A^{(d)}$ 不变空间 $\mathcal M$。
R88 的强多项式逼近在有限放大仍成立，故每个
$R(s)^{(d)},U(s,t)^{(d)}$ 及逆保持 $\mathcal M$。
于是
$$
R(s)^{(d)}\mathcal M=R(t)^{(d)}\mathcal M.
$$
再令 $s\downarrow0$，得到
$$
\boxed{\overline{R(t)^{(d)}\mathcal M}=\mathcal M.}
\tag{2.3}
$$

若 $e\in\mathcal G\setminus\{0\}$，R151 对 $e^{(d)}$ 给同一结论。
两个交换因子各有稠密限制像，其乘积也有：
$$
\boxed{
B:=eR(t)\text{ 单射，且 }
\overline{B^{(d)}\mathcal M}=\mathcal M
\text{ 对所有有限 }d,\mathcal M.
}
\tag{2.4}
$$
这是以下最大闭图的真实分母性质，不是由全空间稠密性外推。

## 3. first 加快分式的真实闭和

设 $g=a/e\in\mathbb K$，$e\ne0$，固定正整数 $q$。
简写 $R=R(t)$、$S=XR$，令
$$
B=eR,\qquad N=eS+\frac aqR.
$$
二者都是有界交换子，$B$ 单射稠密。
定义最大闭商
$$
Y=B^{-1}N,\qquad
\operatorname{Dom}Y=\{x:Nx\in\operatorname{Ran}B\}.
\tag{3.1}
$$
它稠密定义，因为 $YBh=Nh$。

其图 $\mathscr G_Y$ 是闭 $A\oplus A$ 不变空间。
用 (2.4) 对 $d=2$ 和这张图，有
$$
\overline{B^{(2)}\mathscr G_Y}=\mathscr G_Y.
$$
对 $(x,Yx)\in\mathscr G_Y$，
$$
B^{(2)}(x,Yx)=(Bx,BYx)=(Bx,Nx).
$$
故
$$
\boxed{
\mathscr G_Y=
\overline{\{(Bh,Nh):h\in H\}}.
}
\tag{3.2}
$$
这证明原分母图核心。
同样的有界伴随计算还给 $Y=C_0Y^*C_0$。

在自然共同域
$$
\mathcal D=\operatorname{Dom}X\cap\operatorname{Dom}T_g
$$
上，$X+T_g/q$ 包含于 (3.1)：
若 $x\in\mathcal D$，则
$$
B(X+T_g/q)x=eRXx+(a/q)Rx=Nx.
$$
另一方面，$BH=eRH\subset\mathcal D$，在此域上
$$
(X+T_g/q)Bh=eSh+(a/q)Rh=Nh.
$$
由 (3.2)，
$$
\boxed{\overline{X+T_g/q}=Y.}
\tag{3.3}
$$
没有假定自然和本身已经闭，也没有省略最大商域。

## 4. 全 gauge 稳定因子迫 first 为快分式

Gauge 在 $\mathbb K$ 上诱导自同构 $\alpha_\zeta$。
定义 $K[t]$ 上的半线性群作用
$$
\mathcal T_\zeta f(t)
=(\alpha_\zeta f)(t+D_\zeta).
\tag{4.1}
$$
(1.7) 保证它是群作用；它保持首一性、次数及不可约性。

**引理 4.1。** 若某个首一正次数多项式
$$
f(t)=t^q+g t^{q-1}+\cdots\in\mathbb K[t]
$$
满足 $\mathcal T_\zeta f=f$ 对全部 $\zeta\in\Gamma$ 成立，则存在
$h\in\mathbb K$，使实际闭算子
$$
\boxed{X=T_h.}
\tag{4.2}
$$

证明：比较次高系数，得到
$$
\alpha_\zeta(g)+qD_\zeta=g.
\tag{4.3}
$$
快分式的最大域直接给
$$
\gamma_\zeta(T_g)=T_{\alpha_\zeta g}
=T_g-qD_\zeta
\quad\text{且域相同}.
\tag{4.4}
$$
最后的同域不是只用闭包运算：写 $g=a/e$，
则 $g-qD_\zeta=(a-qeD_\zeta)/e$，
而 $eD_\zeta x$ 总在 $\operatorname{Ran}e$；
最大域条件与原来的 $ax\in\operatorname{Ran}e$ 等价。

将 (1.5)、(4.4) 相加，真实共同域 $\mathcal D$ 被每个 $U_\zeta$ 双向保持，
且 $X+T_g/q$ 在该域上 gauge 不变。
§3 的闭包因此满足
$$
\gamma_\zeta(Y)=Y\qquad(\zeta\in\Gamma).
\tag{4.5}
$$

### 4.1 闭图的全乘法不变性

(4.5) 使 $\mathscr G_Y$ 被每个 $U_\zeta\oplus U_\zeta$ 双向保持，
故其正交投影与这些酉算子交换。
Dyadic 字符生成整个乘法 von Neumann 代数；
所以该投影是一个可测的 $2\times2$ 矩阵乘法投影。

因为 $Y$ 稠密定义，其图纤维的第一坐标不是零；
因为它是算子的图，不含任何非零竖直向量。
这两个性质逐点迫图纤维是
$\operatorname{span}(1,h(y))$，其中 $h$ 为几乎处处有限的可测函数。
因此
$$
Y=M_h,\qquad
\operatorname{Dom}Y=\{f:hf\in L^2\}.
\tag{4.6}
$$
亦可由图投影的左上角 $(I+Y^*Y)^{-1}$ 是几乎处处正的乘法算子、
左下角为乘法算子，取其比值得到同一 $h$。

由于 (3.1) 的分子、分母与 $A$ 交换，
$Y$ 完整保 $A$ 域并满足 $YA=AY$。
将 $A$ 写为实际正权 odometer
$$
(Af)(y)=\omega(y)f(y-1),\qquad\omega(y)>0\text{ a.e.}
$$
并取 $f_n=1_{\{|h|\le n\}}\in\operatorname{Dom}M_h$，
域交换给
$$
[h(y)-h(y-1)]\omega(y)
1_{\{|h(y-1)|\le n\}}=0.
$$
令 $n\to\infty$，得到 $h(y)=h(y-1)$ 几乎处处。
Haar odometer 遍历性遂给 $h=c$ 为有限常数。
因此
$$
Y=cI.
\tag{4.7}
$$

### 4.2 真实快分式等式

由 $YB=N$，
$$
eXR+(a/q)R=ceR.
$$
$RH$ 是 $X$ 的图核心，所以该有界系数等式扩到全部 $\operatorname{Dom}X$：
$$
eX=(ce-a/q)I.
$$
因此
$$
X\subseteq T_{c-g/q}.
$$
两边都是原空间的 $C_0$ 自伴闭算子。
包含关系取伴随再用 $C_0$ 共轭，给反向包含。
故
$$
X=T_{c-g/q},
$$
证明引理。

本段从未把非可和 first 当作 Laurent 级数；
形式域只用于有限多项式系数，而实际 $X$ 的识别完全由闭图完成。
R170 的“无界 first 不在 $\operatorname{Frac}\mathcal G$”与此结果相容，
但主证明无需借它额外排除一种情况。

## 5. 快分式分支

若 $X=T_{a/e}$，$a,e\in\mathcal G$、$e\ne0$，则自然幂域上的准确恒等式是
$$
e^pP(X)x=F x,\qquad
F=\sum_{k=0}^p E_k a^k e^{p-k}\in\mathcal G,\quad E_p=I.
\tag{5.1}
$$
它可在 $\operatorname{Dom}X^p$ 上逐次由 $eX=a$ 验证。

若 $F=0$，$e^p$ 单射迫 $P(X)$ 在其整个自然域上为零，
与定理的实际非零前提矛盾。
所以 $F\ne0$，R151 的单射性立即给 $\ker P(X)=0$。
$C_0$ 自伴性再给稠密值域。

这个分支还保留普遍限制稠密性：
$$
e^pH\subset\operatorname{Dom}X^p,\qquad
P(X)e^p=F.
$$
对任意闭 $A$ 不变 $M$，$F M$ 稠密于 $M$，
且 $FM\subseteq P(X)(\operatorname{Dom}X^p\cap M)$。
故该实际限制的像也稠密。
不把此额外结论扩到下一分支。

## 6. 非快分式分支的有限例外

现在假设不存在 $h\in\mathbb K$ 使 $X=T_h$。
在域 $\mathbb K$ 上作首一不可约分解
$$
P=\prod_{i=1}^s f_i^{e_i}.
$$
对每个因子，
$$
H_i=\{\zeta\in\Gamma:\mathcal T_\zeta f_i=f_i\}
$$
是子群。
引理 4.1 说明 $H_i\ne\Gamma$。
Prüfer $2$ 群的每个真子群有限，故各 $H_i$ 有限。

对固定因子对 $i,j$，集合
$\{\zeta:\mathcal T_\zeta f_i=f_j\}$
若非空就是一个有限陪集。
有限多个因子对表明，存在有限 dyadic 子群 $\mu_H$，
使
$$
\gcd_{\mathbb K[t]}(P,\mathcal T_\zeta P)=1
\qquad(\zeta\notin\mu_H).
\tag{6.1}
$$
有限 Euclidean 算法并清除全部有限个系数分母，得到
$$
\boxed{
D=U P+V\mathcal T_\zeta P,\qquad
0\ne D\in\mathcal G,\qquad U,V\in\mathcal G[t].
}
\tag{6.2}
$$
这里没有把一般快分式系数直接作为有界算子；
实际求值前已经全部清成有界 $\mathcal G$ 系数。

## 7. 全部自然域中的跨核配对

令
$$
T=P(X),\quad M=\ker T,\quad
Q_\zeta(X)=(\mathcal T_\zeta P)(X)=\gamma_\zeta(T),\quad
M_\zeta=U_\zeta M.
$$
由 (1.5)，这里最后一个等式是闭算子和自然域的等式。
$Q_\zeta$ 仍是关于 $X$ 的首一 $p$ 次多项式。
R176 对两者给
$$
M,M_\zeta\subset\mathcal D_\infty.
\tag{7.1}
$$
每个 $\mathcal G$ 系数保持 $\mathcal D_\infty$，并与 $X$ 完整域交换。

因此 (6.2) 在 $\mathcal D_\infty$ 上可以实际求值：
$$
D=U(X)T+V(X)Q_\zeta(X).
\tag{7.2}
$$
记原双线性配对为
$$
\mathcal B(f,g)=\int_{\mathbb Z_2}f(y)g(-1-y)\,d\mu(y).
$$
$X$ 和全部有界交换系数均对 $\mathcal B$ 对称。
有限多项式词因两端都在 $\mathcal D_\infty$ 而可逐字移位。

取 $f\in M$、$g\in M_\zeta$。
第一项因 $Tf=0$ 消失；
第二项先将 $V(X)$、再将 $Q_\zeta(X)$ 移到右端，
并用这些词在深域上交换，得到
$$
\mathcal B(V(X)Q_\zeta(X)f,g)
=\mathcal B(f,Q_\zeta(X)V(X)g)=0.
$$
所以
$$
\mathcal B(DM,M_\zeta)=0.
$$
R151 的实际限制结论给 $\overline{DM}=M$，因此
$$
\boxed{\mathcal B(M,U_\zeta M)=0\qquad(\zeta\notin\mu_H).}
\tag{7.3}
$$
本步使用的是同一个未知闭 $M$ 上已证的 $\mathcal G$ 稠密像；
没有从全空间稠密性推断限制，也没有越过无界词域。

## 8. Fourier 排核与图循环

对任意 $f,g\in M$，函数 $f(y)g(-1-y)\in L^1$
在有限子群 $\mu_H$ 外的 Fourier 系数全为零。
有限柱条件期望的 $L^1$ 收敛说明它在每个模 $H$ 柱上为常数。

若 $M\ne0$，闭 $A$ 不变性与 $\omega>0$ 使 $M$ 的总本质支撑全测；
证明是取可数稠密族定义支撑，利用 odometer 平移不变及遍历性。
在每个模 $H$ 柱上，可从该稠密族选 $f_0,g_0$，
使 $f_0(y)g_0(-1-y)$ 不恒为零。
此乘积已经是柱常数，故在整柱非零。
对任意 $f\in M$，$f(y)g_0(-1-y)$ 也是柱常数，
于是该柱上所有 $f$ 都是 $f_0$ 的标量倍数。
因此 $\dim M\le H$。

原 $A$ 单射且拟幂零，不允许非零有限维不变空间。
所以 $M=0$。
R176 的 $C_0$ 自伴性给稠密值域，图循环结论给定理 1.1。

如果 $X$ 无界，首一自然多项式自动不是零算子：
否则其闭性和稠密域会迫 $\operatorname{Dom}X^p=H$，
从而 $\operatorname{Dom}X=H$，与闭图定理矛盾。
有界 $X$ 时必须保留实际非零前提，例如 $X\in\mathcal G$ 时
$t-X$ 是一个确实为零的首一求值。

## 9. 二次完全共振：无任何主行衰减限制

取
$$
v_2=\sum_j a_j^2(\chi_j-1).
$$
它是真正有界 first，因为 $a\in\ell^2$。
R270 的完整混合 Bell 恒等式在此简化为
$$
(u^2+2v_2)e^w=(X_b^2-B)e^w,
$$
$$
B=\sum_j a_j^2(R_j-I)^2,\qquad R_j=V(e^{-2b_j}N_j).
\tag{9.1}
$$
[R270 第二附录](../results/R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md) 已证明局部二阶消去给
$$
\boxed{B\in\mathcal G.}
\tag{9.2}
$$
其证明用实际 $N_j^2=\eta_jN_{j+1}$ 与归一化幂重复占据，
不是把 $B$ 有界除以 $A^2$。

定理 1.1 立即给
$$
\boxed{
\left[u^2+2\sum_j a_j^2(\chi_j-1)\right]e^w
\text{ 只要实际非零就循环}.
}
\tag{9.3}
$$
这里 $a,b$ 是任意复 $\ell^2$ 行，没有熵、幅度排序或相位条件。

只要 $a$ 至少有两个非零位置 $i\ne j$，方括号的二阶 Walsh 系数
$2a_i a_j\ne0$，所以它确实非零。
只有一个非零系数 $a_j=a\ne0$ 时，
$$
u^2+2a^2(\chi_j-1)
=(a_*+a)(a_*-a+2a\chi_j),
$$
准确的零例为 $a_*=-a$。
若所有 $a_j=0$，该向量就是 $a_*^2e^w$。
因此无限主支撑的完全共振二次族全部关闭。

## 10. 全部阶的明确共振消去

对 $n\ge2$ 定义同物理位的无限辅助 first
$$
v_n=\sum_j a_j^n(\chi_j-1).
\tag{10.1}
$$
每个 $v_n$ 有界，且与主行可以完全重叠。
定义单个固定阶 $p$ 所需的点态多项式
$$
\boxed{
F_p(u,v_2,\ldots,v_p)
=
p![t^p]\exp\left(
tu+\sum_{n=2}^p\frac{2^{n-1}}n\,t^n v_n
\right).
}
\tag{10.2}
$$
置 $F_0=1,F_1=u$。
前三个新增阶为
$$
F_2=u^2+2v_2,
$$
$$
F_3=u^3+6uv_2+8v_3,
$$
$$
F_4=u^4+12u^2v_2+32uv_3+12v_2^2+48v_4.
\tag{10.3}
$$

**定理 10.1。** 对任意复 $\ell^2$ 主行和指数权，
每个实际非零 $F_p e^w$ 都循环。
更一般地，每个实际非零有限标量线性组合
$$
\left(\sum_{k=0}^p q_kF_k\right)e^w
\tag{10.4}
$$
都循环。

### 10.1 准确的一位生成恒等式

令
$$
\psi(z)=-\frac12\log(1-2z)
=\sum_{n\ge1}\frac{2^{n-1}}n z^n.
$$
在零点的小圆盘内，
$$
\frac{1-e^{-2\psi(z)}}2=z.
$$
对标量 $R$，因此有准确恒等式
$$
e^{-(\psi(z)-z)}
(\cosh\psi(z)+R\sinh\psi(z))
=e^z[1+z(R-1)].
\tag{10.5}
$$
取其零点分支的对数：
$$
z+\log[1+z(R-1)]
=
zR+\sum_{n\ge2}\frac{(-1)^{n-1}}n
z^n(R-1)^n.
\tag{10.6}
$$

在每个物理位代入 $z=ta_j$、真实 $R=R_j$。
有限位上的不同位乘法恒等式对基向量 $e^w$ 精确成立。
(10.5) 左侧对应的点态指数正是
$$
tu+\sum_{n\ge2}\frac{2^{n-1}}n t^nv_n;
$$
其中 $v_n$ 内的 $-1$ 项承担 $-(\psi(ta_j)-ta_j)$，
因此没有使用可能发散的 $\sum_ja_j$。

右侧对数给真实修正
$$
\boxed{
G_n=(-1)^{n-1}(n-1)!
\sum_j a_j^n(R_j-I)^n,\qquad n\ge2.
}
\tag{10.7}
$$
每个和按范数绝对收敛。
更强地，
$$
G_n\in\mathcal G.
\tag{10.8}
$$
因为局部函数
$a_j^n[V(e^{-2b_j}z)-1]^n$
在 $z=0$ 至少二阶消去，且对固定 $n$ 在一个与 $j$ 无关的小圆盘内
有统一解析预算；R270B 的实际归一化系数定理遂适用。
这是真实二次 carry 的结论，不是将 $\mathcal G$ 当成整个 $\mathcal A$ 的理想。

### 10.2 真实有限 jets 和首一快系数多项式

由有限位生成式及 (10.6)，到任意固定 $p$ 阶，
$$
\boxed{
F_p(u,v)e^w
=
\left[
\exp\left(\sum_{n=2}^p\frac{G_n}{n!}\partial_z^n\right)z^p
\right]_{z=X_b}e^w.
}
\tag{10.9}
$$
这里没有把全空间的 $e^{tX_b}$ 当作有界算子。

具体地，可先在有限位上验证全部 jets；
点态左端按 $L^2$ 收敛，因为第一 chaos 的所有有限矩及指数矩存在、
各 $v_n$ 有界且其截断按 $L^\infty$ 收敛。
右端的 $G_n$ 截断按算子范数收敛；
R145/R176 的倾斜自然幂 jet 恒等式给
$X_{b,m}^k e^w\to X_b^k e^w$ 对每个固定 $k$ 成立。
该自然幂收敛也可从原 Bell 恒等式归纳得到：
点态 $u_m^ke^w$ 收敛、各二阶以上 Bell 系数范数收敛，
再逐次解出最高 $X_{b,m}^k e^w$。
因此 (10.9) 是原 Haar 空间中的实际域等式。

(10.9) 右侧是首一 $p$ 次 $X_b$ 多项式，
全部低阶系数为有限个 $G_n\in\mathcal G$ 的多项式，故仍在 $\mathcal G$。
定理 1.1 证明 $F_p e^w$ 非零即循环。
对 (10.4)，取最高非零 $q_p$ 并除以它，仍是同类首一快系数自然多项式，
所以同样成立。

### 10.3 无限主支撑时的非零性

若至少存在 $p$ 个不同非零 $a_j$，$F_p$ 的最高 Walsh $p$ 层来自唯一的 $u^p$ 项，
其在 $J$、$|J|=p$ 上的系数为
$$
p!\prod_{j\in J}a_j\ne0.
\tag{10.10}
$$
(10.2) 中任何含 $v_n$、$n\ge2$ 的项，
普通 chaos 次数都严格小于其加权次数 $p$，因此不能取消这一层。
$e^w$ 几乎处处不为零。

特别，主行有无限非零支撑时，每个 $F_p e^w$、
以及每个非零标量多项式系数给出的 (10.4)，都实际非零且循环。
这是全阶无限重叠辅助模式的明确正族，适用于任意复 $\ell^2$ 主行。

## 11. 范围

主定理证明的是实际非零、首一（或实际可逆最高系数）的
$\mathcal G$ 系数自然多项式，不是任意有界系数自然多项式。
通常的点态 $q(u)$ 具有可能不在 $\mathcal G$ 的慢 Bell 修正，
不能未经额外证明套入本稿。

全阶族 (10.2) 的辅助系数是同物理位的 $a_j^n$，
其具体常数经过 (10.5) 完整设计，准确消掉每一位的一次慢项；
不能把任意辅助模式或任意耦合自动改写成这种族。
在非快分式分支，也没有证明 $P(X)$ 在每个未知不变限制上稠密。

完整普通 ISP、任意独立慢多模式以及一般系数核问题仍保持开放。

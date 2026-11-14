# R85：复强交换子的图核心与单项式精确除法

日期：2026-11-12（UTC）。经主会话逐段核验。

**状态：已证明的中间结论；完整ISP尚未完成。**

本条补充 R80 的混合芽结论。它完整覆盖 R37 第 10 节的同虚部复参数，证明尾商 $Z_N$ 强*趋于恒等，给出所有 $Y^{-m}F$ 及全部混合解析芽商的最大图核心，并取得精确的单项式范围包含判据：
$$
\boxed{
\operatorname{Ran}F(A,Y)\subseteq\operatorname{Ran}(A^mY^n)
\quad\Longleftrightarrow\quad
z^mw^n\text{ 在 }\mathbb C\{z,w\}\text{ 中整除 }F.
}
$$
这里 $F$ 是非零收敛芽，$m,n$ 是非负整数；包含指实际值域，不是值域闭包。所有非零解析芽算子本身的值域闭包都等于 $H$。

依赖：R23 的无常数项强近似单位；R24 的完整交换子共轭对称；R28/R37 的精确局部替换与强乘积；R66 的解析 gcd/Bézout 引理；R73 的真实边界商；R80 的二阶整轨道及超二阶轨道衰减障碍。本条使用的 R80 原始完整证明在
[整轨道与混合解析核笔记](../notes/2026-11-12-strong-multiplier-mixed-analytic-kernels-0c-agent.md)。

## 1. 完整参数假设和早期因子的非退化性

设
$$
s_j=a_j'+iv_j,\qquad t_j=b_j'+iv_j,\qquad
0\le a_j'\le b_j',\qquad v_j\in\mathbb R,
$$
$$
s,t\in\ell^2,\qquad
\sum_j(b_j'-a_j')=\infty. \tag{1.1}
$$
这里带撇的 $a_j',b_j'$ 是局部参数的实部，与 odometer 的权 $a_j$ 不同。记
$$
d_j'=b_j'-a_j'\ge0.
$$
于是 $d'\in\ell^2$、$\sum d_j'=\infty$。

局部函数为
$$
h_j(b)=\frac{1+s_j(-1)^b}{\sqrt{1+|s_j|^2}},\qquad
g_j(b)=\frac{1+t_j(-1)^b}{\sqrt{1+|t_j|^2}}.
$$
均值是严格正实数，分别为
$(1+|s_j|^2)^{-1/2}$、$(1+|t_j|^2)^{-1/2}$，与一的差可和。因此归一化无限乘积 $h,g$ 存在于 Haar $L^2$，范数为一，且由 R16 循环。

所有早期因子也非退化：
$$
\operatorname{Re}(1+s_j)\ge1,\qquad
\operatorname{Re}(1+t_j)\ge1.
$$
故 $h_j(0),g_j(0)$ 从不为零。第二坐标在有限多个早期指标可以为零；下文从不除以第二坐标，所以不需排除这种情形。

令
$$
\rho_z=\frac{1-z}{1+z},\qquad
\alpha_j=\frac{(1+s_j)/\sqrt{1+|s_j|^2}}
{(1+t_j)/\sqrt{1+|t_j|^2}},
$$
$$
W_j=\alpha_j(I+\rho_{s_j}N_j)(I+\rho_{t_j}N_j)^{-1},
\qquad Y_N=\prod_{j<N}W_j. \tag{1.2}
$$
由于 $\operatorname{Re}s_j,\operatorname{Re}t_j\ge0$，
$$
|\rho_{s_j}|,|\rho_{t_j}|\le1.
$$
各 $N_j$ 拟幂零，所以全部分母可逆，$W_j,W_j^{-1}\in\mathcal A$。

R37 第 10 节证明
$$
Y_N\longrightarrow Y\quad\text{强收敛},
$$
其中 $Yg=h$，$Y$ 非零、单射、值域稠密、拟幂零，并且与 $A$ 交换。它还给出
$$
\|W_j\|\le m_j:=
\sqrt{\frac{1+|t_j|^2}{1+|s_j|^2}}\ge1,\qquad
C_{\rm tot}=\prod_jm_j<\infty. \tag{1.3}
$$
这些不等式针对全部指标成立；不是只对最终的小参数成立。

## 2. 同虚部复参数仍归约到正参数半群

取 R20 的非负参数
$$
u_j=d_j'=b_j'-a_j'\ge0
$$
及半群
$$
S(t)=\operatorname*{s-lim}_{N\to\infty}
\prod_{j<N}e^{-tu_j}e^{2tu_jN_j},\qquad t\ge0. \tag{2.1}
$$
$u\in\ell^2$，故其所有强连续半群性质及 R80 的二阶整轨道定理适用。

**定理 2.1。** 存在 $\mathcal R,\mathcal R^{-1}\in\mathcal A$，使
$$
\boxed{Y=\mathcal R S(1)=S(1)\mathcal R.} \tag{2.2}
$$

**证明。** 写
$$
\kappa_j=\rho_{s_j}-\rho_{t_j}
=\frac{2u_j}{(1+s_j)(1+t_j)}.
$$
因为 $|1+s_j|,|1+t_j|\ge1$，
$$
|\kappa_j|\le2u_j.
$$
又对充分大的 $j$，
$$
|\kappa_j-2u_j|
\le C u_j(|s_j|+|t_j|)
\le C'(|s_j|^2+|t_j|^2), \tag{2.3}
$$
其中使用 $u_j=|t_j-s_j|\le|s_j|+|t_j|$。因此该差绝对可和。有限前缀不影响可和性。

定义
$$
D_j=(I+\rho_{s_j}N_j)(I+\rho_{t_j}N_j)^{-1}
e^{-2u_jN_j},\qquad
\beta_j=\alpha_je^{u_j}. \tag{2.4}
$$
便有精确恒等式
$$
W_j=\beta_jD_j\,e^{-u_j}e^{2u_jN_j}. \tag{2.5}
$$

下面证明 $\prod D_j$ 及其逆按范数收敛。令 $U=\sup_j u_j<\infty$。由于 $|\rho_{t_j}|\le1$，二次递归给出统一界
$$
\|(I+\rho_{t_j}N_j)^{-1}\|\le \frac2{1-\eta_0}.
$$
并且
$$
\begin{aligned}
&(I+\rho_{s_j}N_j)(I+\rho_{t_j}N_j)^{-1}
-(I+\kappa_jN_j)\\
&\quad=-\kappa_j\rho_{t_j}N_j^2
(I+\rho_{t_j}N_j)^{-1}.
\end{aligned}
$$
其范数至多 $C|\kappa_j|\eta_j$。另一方面，
$e^{-2u_jN_j}(I+2u_jN_j)-I$ 的常数项和一次项消失，故
$$
\|e^{-2u_jN_j}(I+2u_jN_j)-I\|
\le C_Uu_j^2\eta_j.
$$
结合 $\|e^{-2u_jN_j}\|\le e^{2U}$，得到
$$
\boxed{
\|D_j-I\|\le C_U\bigl(
|\kappa_j-2u_j|+u_j\eta_j
\bigr).
} \tag{2.6}
$$
右边可和。各 $D_j$ 可逆且属于 $\mathcal A$，尾部逆差也可和，所以其范数乘积 $D$ 可逆，$D,D^{-1}\in\mathcal A$。

对标量部分，在充分远的尾部选连续于 $1$ 的对数，得到
$$
\begin{aligned}
\log\beta_j
={}&\log(1+s_j)-\log(1+t_j)+u_j\\
&+\tfrac12\log(1+|t_j|^2)
-\tfrac12\log(1+|s_j|^2).
\end{aligned}
$$
因 $t_j-s_j=u_j$ 是实数，所有一次项抵消，故
$$
|\log\beta_j|\le C(|s_j|^2+|t_j|^2).
$$
有限前缀各 $\beta_j$ 都非零，因此
$$
\beta=\prod_j\beta_j\ne0
$$
存在。令 $\mathcal R=\beta D$。将 (2.5) 相乘后，范数因子趋于 $\mathcal R$，半群因子强趋于 $S(1)$，左边强趋于 $Y$，得到 (2.2)。证毕。

### 2.1 全部混合解析芽的单射稠密性

由 R80 的二阶整轨道定理，任何非零 $x$ 都不能满足
$$
\|S(t)x\|\le Ce^{-ct^p}\quad(t\ge0),\qquad p>2.
$$
R80 的 Weierstrass 预备与迭代证明只需：
$A,Y$ 交换且拟幂零，$A$ 单射，$\|A^n\|\le e^{-(5/4)n^4}$，以及 (2.2) 的可逆范数因子。以上在当前复参数下全部成立。因此它逐字给出
$$
\boxed{
0\ne F\in\mathbb C\{z,w\}
\ \Longrightarrow\
F(A,Y)\text{ 单射且值域稠密。}
} \tag{2.7}
$$
具体说，核方程经预备变为 $Y^dx=AQx$，迭代得
$S(dn)x=\mathcal R^{-dn}A^nQ^nx$，四阶衰减与整轨道障碍矛盾；固定共轭对称性再给稠密值域。这里没有引入复时间的有界算子半群。

## 3. 边界商也搬运到同虚部复参数

为避免未经证明地把 R73 的实参数结论用于复参数，下面明确构造归约。

取实参数 $(s_j^0,t_j^0)=(0,u_j)$，其中 $u_j=b_j'-a_j'$。它们满足 R37 的全部实有序条件，得到强交换子 $Y_0$。定理 2.1 的证明也适用于这组实参数，并使用同一个半群 (2.1)，所以
$$
Y_0=\mathcal R_0S(1),
\qquad \mathcal R_0,\mathcal R_0^{-1}\in\mathcal A.
$$
故
$$
Y=U Y_0,\qquad U=\mathcal R\mathcal R_0^{-1}\in\mathcal A,
\qquad U^{-1}\in\mathcal A. \tag{3.1}
$$

记 $\mathcal C=C^*(I,A)$。因为 $U,U^{-1}\in\mathcal C$，
$$
C^*(\mathcal C,Y)=C^*(\mathcal C,Y_0). \tag{3.2}
$$
R73 对 $Y_0$ 已构造含幺收缩 $*$-商同态。因此当前 $Y$ 也有
$$
\Pi:C^*(\mathcal C,Y)\longrightarrow\mathcal C,\qquad
\Pi|_{\mathcal C}=\operatorname{id},\qquad
\Pi(Y)=U\Pi(Y_0)=0. \tag{3.3}
$$

特别，若 $0\ne K\in\mathcal C$，则不存在任何 $B\in B(H)$ 使
$$
YB=K\quad\text{或}\quad BY=K. \tag{3.4}
$$
例如第一种关系给 $KK^*\le\|B\|^2YY^*$，应用正映射 $\Pi$ 便矛盾。这里不要求 $B$ 本身属于这个 $C^*$ 代数。

## 4. 尾商强*趋于恒等与遗传稠密值域

令
$$
Z_N=Y_N^{-1}Y.
$$
R37 的统一尾乘积界给
$$
Y=Y_NZ_N=Z_NY_N,\qquad
\|Z_N\|\le C_N:=\prod_{j\ge N}m_j,\qquad
1\le C_N\le C_{\rm tot},\quad C_N\to1. \tag{4.1}
$$

**定理 4.1。**
$$
\boxed{Z_N\longrightarrow I\text{ 强*收敛},\qquad
\|Z_N\|\longrightarrow1.} \tag{4.2}
$$

**证明。** 由精确局部替换，$Y_N^{-1}$ 将 $h$ 的前 $N$ 个因子替换为 $g$，不改变任意其余位。因此
$$
Z_Ng=Y_N^{-1}h
=g^{(N)}\otimes h_{\ge N}.
$$
另一方面 $g=g^{(N)}\otimes g_{\ge N}$，且 $\|g^{(N)}\|=1$。两个归一化乘积尾都趋于参考常向量，故
$$
\|Z_Ng-g\|
=\|h_{\ge N}-g_{\ge N}\|\longrightarrow0. \tag{4.3}
$$
每个 $Z_N$ 与 $A$ 交换，所以 (4.3) 传到 $g$ 的多项式轨道；$g$ 循环且 $\|Z_N\|\le C_{\rm tot}$，故 $Z_N\to I$ 强收敛。

由 R24，$Z_N$ 对同一个共轭 $C$ 对称，即 $Z_N^*=CZ_NC$。强收敛于是也给 $Z_N^*\to I$ 强收敛。最后 (4.1) 给 $\limsup\|Z_N\|\le1$，而对任意单位向量 $x$，
$\|Z_N\|\ge\|Z_Nx\|\to1$，故范数趋一。证毕。

**推论 4.2。** 对每个闭的 $A$ 不变子空间 $M$、每个正整数 $m$，
$$
Y^mM\subseteq M,\qquad
\overline{Y^mM}=M,
$$
且 $Y^m|_M$ 单射。

**证明。** $Y_N,Y_N^{-1}\in\mathcal A$ 都保持 $M$；$Y_N$ 强趋 $Y$，故 $Y$ 也保持 $M$。对任意 $x\in M$，
$$
Z_N^mx=Y^mY_N^{-m}x\in Y^mM,\qquad
Z_N^mx\longrightarrow x.
$$
这证明稠密性；单射性来自整个 $H$ 上的 $Y$ 单射。证毕。

这个结论只涉及 $Y$ 在既有 $A$ 不变子空间上的限制，并不证明该子空间必须是零或整个 $H$。

## 5. 任意交换子的 $Y^m$ 分母都有明确最大图核心

令 $F\in\{A\}'$ 为任意有界交换子；不要求 $F$ 属于 $\mathcal A$ 或混合解析芽类。因为 $Y$ 是 $A$ 有理函数的强极限，$F$ 与 $Y$ 交换。对正整数 $m$ 定义最大闭商
$$
T_{\max}=Y^{-m}F,\qquad
\mathcal D(T_{\max})
=\{u:Fu\in\operatorname{Ran}Y^m\},\qquad
Y^mT_{\max}u=Fu. \tag{5.1}
$$
$Y^m$ 单射，所以值唯一；其图是有界方程 $Fu=Y^mv$ 的解集，因而闭。定义域包含稠密的 $\operatorname{Ran}Y^m$。

在这条范围上有自然核心算子
$$
T_0(Y^mh)=Fh.
$$

**定理 5.1。**
$$
\boxed{\overline{T_0}=T_{\max},\qquad
T_{\max}=CT_{\max}^*C.} \tag{5.2}
$$

**证明。** 若 $(u,v)$ 满足 $Fu=Y^mv$，取
$$
h_N=Y_N^{-m}u.
$$
因为 $F$ 与 $Y_N$ 交换，
$$
(Y^mh_N,Fh_N)
=(Z_N^mu,Z_N^mv)\longrightarrow(u,v). \tag{5.3}
$$
这给出完整、逐点的图范数逼近，证明最小图等于最大图。

为验证共轭伴随关系，利用已证核心，$(v,w)$ 属于 $T_{\max}^*$ 的图当且仅当
$$
F^*v=(Y^*)^mw.
$$
R24 给所有 $F\in\{A\}'$ 的 $F^*=CFC$，也给 $Y^*=CYC$。对最后方程施加 $C$，恰得到
$F(Cv)=Y^m(Cw)$，即 (5.2) 的图恒等式。证毕。

这条结论没有把一般可闭核心与最大闭图未经证明地合并；实际逼近由 (5.3) 给出。

## 6. 全部混合解析芽商的最大图也等于自然核心闭包

设 $F,G\in\mathbb C\{z,w\}$ 都非零。由 (2.7)，
$F(A,Y)$、$G(A,Y)$ 均单射且值域稠密。定义
$$
T_{F/G}:\quad F(A,Y)u=G(A,Y)v,\qquad T_{F/G}u=v. \tag{6.1}
$$
其图闭、定义域稠密，且它单射、值域稠密：自然核心包含
$(G(A,Y)h,F(A,Y)h)$，其中第一个范围稠密，第二个范围也稠密。

下面验证 R66 的图核心机制在这一新算子对上确实适用。R66 的纯解析 gcd/Bézout 引理给出
$$
F=DF_1,\qquad G=DG_1,\qquad
UF_1+VG_1=z^r \tag{6.2}
$$
其中 $D,F_1,G_1,U,V$ 都是收敛芽，$r\ge0$。该引理是收敛幂级数环自身的陈述，不依赖之前使用的具体 $L$。

$D(A,Y)$ 单射，所以可从最大图方程中取消；它又有稠密值域，所以原自然图的闭包与约分后的自然图闭包相同。

若 $r>0$，由 R23 取多项式 $P_\nu(A)=A^rR_\nu(A)$ 强趋 $I$；每个 $R_\nu$ 为多项式。若 $r=0$，直接取 $P_\nu=R_\nu=I$。令
$$
U_\nu=U(A,Y)R_\nu(A),\qquad
V_\nu=V(A,Y)R_\nu(A).
$$
则
$$
F_1(A,Y)U_\nu+G_1(A,Y)V_\nu=P_\nu(A)\longrightarrow I
\quad\text{强收敛}. \tag{6.3}
$$
给定约分后的方程 $F_1(A,Y)u=G_1(A,Y)v$，取
$$
h_\nu=U_\nu v+V_\nu u.
$$
交换性和 (6.3) 给
$$
(G_1(A,Y)h_\nu,F_1(A,Y)h_\nu)
=(P_\nu(A)u,P_\nu(A)v)\longrightarrow(u,v). \tag{6.4}
$$
因此
$$
\boxed{
\operatorname{Graph}(T_{F/G})
=\overline{\{(G(A,Y)h,F(A,Y)h):h\in H\}},
\qquad T_{F/G}=CT_{F/G}^*C.
} \tag{6.5}
$$

这也使 R66 关于约分和闭合和积的证明适用于当前混合芽分式；这里不宣称每个非全纯分式的实现都无界。下一节完整判定的是单项式分母。

## 7. 首先排除任意有界的 $A$ 除法 $Y^r=AB$

**引理 7.1。** 对任意整数 $r\ge0$，不存在任何 $B\in B(H)$ 使
$$
Y^r=AB. \tag{7.1}
$$

**证明。** 因 $A$ 单射，(7.1) 与 $AY^r=Y^rA$ 给
$$
A(BA-AB)=0\quad\Longrightarrow\quad BA=AB.
$$
所以 $B$ 也与 $Y$、$\mathcal R$ 交换：它与所有 $A$ 有理函数及其强、范数极限交换。

若 $r=0$，由 $I=AB=BA$，$A$ 有有界逆，已与拟幂零性矛盾。也可将等式迭代，得到
$1=\|I\|\le\|A^n\|\|B\|^n\to0$。

若 $r\ge1$，从 (2.2)、(7.1) 迭代得
$$
S(rn)=\mathcal R^{-rn}Y^{rn}
=\mathcal R^{-rn}A^nB^n.
$$
于是对任意 $x$，
$$
\|S(rn)x\|
\le\|x\|\|\mathcal R^{-1}\|^{rn}\|B\|^n
e^{-(5/4)n^4}.
$$
$[0,r]$ 上的半群一致界把它扩为全部实 $t\ge0$ 的四阶轨道衰减。R80 的轨道障碍迫使每个 $x=0$，与 $H\ne\{0\}$ 矛盾。证毕。

这一步允许 $B$ 是任意有界算子；交换性是由真实方程及单射性推出的，并未作为隐含前提。

## 8. 两条坐标轴的精确有界除法判据

记 $\mathscr O=\mathbb C\{z,w\}$。

**定理 8.1。** 对 $0\ne F\in\mathscr O$、整数 $m\ge1$，
$$
\operatorname{Ran}F(A,Y)\subseteq\operatorname{Ran}A^m
\quad\Longleftrightarrow\quad z^m\mid F. \tag{8.1}
$$
若成立，唯一有界因子就是 $(F/z^m)(A,Y)$。

**证明。** 因 $A^m$ 单射，值域包含定义了全域算子
$B=A^{-m}F(A,Y)$。若 $x_\nu\to x$、$Bx_\nu\to y$，则
$A^my=F(A,Y)x$，所以 $y=Bx$；闭图定理给 $B$ 有界。因此范围包含等价于某个有界 $B$ 满足 $F(A,Y)=A^mB$。

先取 $m=1$，把芽分解为
$$
F(z,w)=zH(z,w)+f(w).
$$
若 $f\not\equiv0$，写 $f(w)=w^ru(w)$，其中 $r\ge0$、$u(0)\ne0$。于是
$$
f(Y)=A[B-H(A,Y)]
$$
给
$$
Y^r=A[B-H(A,Y)]u(Y)^{-1},
$$
与引理 7.1 矛盾。所以 $f\equiv0$，即 $z\mid F$。

对一般 $m$，先得到 $F=zH$。从
$AH(A,Y)=A^mB$ 中取消单射的 $A$，得到
$H(A,Y)=A^{m-1}B$；重复便有 $z^m\mid F$。反向由解析商直接给有界因子。唯一性来自 $A^m$ 单射。证毕。

**定理 8.2。** 对 $0\ne F\in\mathscr O$、整数 $n\ge1$，
$$
\operatorname{Ran}F(A,Y)\subseteq\operatorname{Ran}Y^n
\quad\Longleftrightarrow\quad w^n\mid F. \tag{8.2}
$$
若成立，唯一有界因子就是 $(F/w^n)(A,Y)$。

**证明。** 如上，$Y^n$ 单射和闭图定理把范围包含化为
$F(A,Y)=Y^nB$，其中 $B$ 任意有界。先取 $n=1$，写
$$
F(z,w)=wH(z,w)+g(z).
$$
则
$$
g(A)=Y[B-H(A,Y)].
$$
如果 $g\not\equiv0$，$g(A)$ 是 $\mathcal C$ 中的非零元素；非零性可由一变量首阶分解和 $A$ 单射直接得到。它与 (3.4) 的真实边界除法障碍矛盾。因此 $g\equiv0$，即 $w\mid F$。再逐次取消单射的 $Y$，得到 $w^n\mid F$。反向和唯一性同前。证毕。

## 9. 单项式分母的完整判据与范围偏序

**定理 9.1。** 对 $0\ne F\in\mathscr O$ 及 $m,n\ge0$，
$$
\boxed{
\operatorname{Ran}F(A,Y)\subseteq\operatorname{Ran}(A^mY^n)
\iff z^mw^n\mid F.
} \tag{9.1}
$$
任何满足 $A^mY^nB=F(A,Y)$ 的有界 $B$ 都唯一等于
$(F/(z^mw^n))(A,Y)$。

**证明。** 若值域包含于单项式范围，则同时包含于
$\operatorname{Ran}A^m$ 和 $\operatorname{Ran}Y^n$。定理 8.1、8.2 给
$z^m\mid F$ 及 $w^n\mid F$；在收敛幂级数的系数上，这意味着所有非零项的两个指数分别至少为 $m,n$，所以 $z^mw^n\mid F$。反向用解析商作因子。唯一性来自 $A^mY^n$ 单射。证毕。

例如，对非负整数 $a,b,c,d$，
$$
\boxed{
\operatorname{Ran}(A^aY^b)
\subseteq\operatorname{Ran}(A^cY^d)
\iff a\ge c\ \text{且}\ b\ge d.
} \tag{9.2}
$$
若两个指数对不相等且满足该偏序，则包含严格；反向包含会由 (9.2) 迫使两个指数对相等。

特别，$\operatorname{Ran}A^m$ 与 $\operatorname{Ran}Y^n$ 对所有正整数 $m,n$ 互不包含，尽管二者都稠密。

### 9.1 $Yg=h$ 给出的直接范围见证

最基本的 $\operatorname{Ran}Y\not\subseteq\operatorname{Ran}A$ 还有可见的具体见证 $h=Yg$。因为 $\operatorname{Re}s_j\ge0$，
$$
|h_j(0)|^2=\frac{|1+s_j|^2}{1+|s_j|^2}\ge1.
$$
又 $s_j\to0$，所以对充分大 $j$，$|h_j(1)|^2\ge1/2$。在 dyadic 环带
$E_j=\{y:v_2(y)=j\}$ 上，独立乘积给
$$
\int_{E_j}|h(y)|^2\,d\mu(y)
=2^{-j-1}\prod_{i<j}|h_i(0)|^2\,|h_j(1)|^2
\ge2^{-j-2}. \tag{9.3}
$$
尾部的平方范数为一，故没有额外尾因子。

实际 $A$ 写作 $Af(y)=w(y)f(y-1)$，其中 $w=a_j$ 于 $E_j$。因此
$h\in\operatorname{Ran}A$ 当且仅当 $h/w\in L^2$；但
$$
\int|h/w|^2\,d\mu
\ge\sum_{j\text{ 大}}2^{-j-2}a_j^{-2}=\infty.
$$
所以 $h\notin\operatorname{Ran}A$。这一直接见证不依赖把某个范围的闭包与实际范围混同。

## 10. 已解决的部分与仍保留的缺口

本条完成：

- R37 同虚部复参数的全部非零混合解析芽单射稠密；
- 通过可逆 $\mathcal A$ 因子搬运的真实边界商；
- 强乘积尾 $Z_N\to I$ 强*及其在每个 $A$ 不变子空间上的稠密作用；
- 对任意有界交换子 $F$ 的 $Y^{-m}F$ 最大图核心；
- 全部混合解析芽分式的自然图核心与共轭伴随关系；
- 所有单项式分母的精确有界性和实际范围包含判据。

一般非单项式分母 $G(z,w)$ 的完整有界商判据仍未在此证明。例如，不能仅从边界商就断言每个非全纯 $F/G$ 都无界，也不能从全部铅笔单射稠密就断言 $A^{-1}Y$ 的预解集为空。相应闭商已由第 6 节合法构造，但一般谱分类需要另外的除法论证。

这些结果也不等于全部交换子非零元素单射，更没有完成普通 Hilbert 不变子空间问题。


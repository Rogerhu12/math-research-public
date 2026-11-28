# R1166 — 原 Miller 源的实际 ambient-PD 比较与保序系数投影

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 本篇将 R1164 的原 pointed Miller–Čech
代表放入一个固定的 global ambient Frobenius embedding，
并把它实际送到 R1165 的两开集及原 coefficient cone。
全部几何 normal contractions、Čech overlap、divided-Frobenius
第二槽和 external-product 同伦均显示给出。
在原 supersingular CM 读取处，R1164 的两个 line frames
直接给所需 formal 两开集输入。

这不等于已经计算原 $F_0$ 或其中央槽。
实际 theta norm、已指定的中央 primitive、closed-point
corestriction 与原 ordered gauges 仍须作为输入。
本篇不给这些输入另选一个同名的 cohomology representative，
也不把一个 raw Frobenius matrix 再施一次 Frobenius。

## 1. 原底、原曲线与 formal 两开集

取原未分歧底 $\mathcal O$，$p>37$，并固定同一 good curve
$$
\mathcal E:\quad y^2=x^3+Ax+B,\qquad
t=-x/y,\quad \omega=dx/(2y),\quad \eta=x\omega .
\tag{1166.1}
$$
曲线本身在本篇不随 torsion/source 参数变化。
取 R1165 的 $U=\mathcal E\setminus O$ 和原点邻域 $V$；
可继续缩小 $V$，使 $t$ 是 étale coordinate，
$\eta_V=\eta-t^{-2}dt$ 正则，并保 R1165 (1165.37) 的
Hensel 条件。以下使用相应 $p$-adic completions。

令 $S$ 为实际 ramified base 的 $p$-完备 PD embedding ring。
原第一层 CM 读取使用
$$
e=p^2-1,\qquad g=z^e-p,\qquad
S=\mathcal O[z,\gamma_n(g):n\ge1]^\wedge_p,\qquad
\psi(z)=z^p,\quad \psi|_{\mathcal O}=\sigma .
\tag{1166.2}
$$
一般 coefficient 层也可使用实际标记域的同一
Eisenstein embedding。保留整个 base PD ideal、
$d\log z$ 及其 connection；从不将 $\psi$ 解释为
$\mathcal O_L$ 上的 field Frobenius。

### 1.1 SS 中的实际 refinement 已在每层一致

设 $P\in E[p^r]\setminus O$ 还原到 $O$，
$W=\mathcal E_{\mathcal O_L}\setminus(O\cup P)$。
则对每个 $n\ge1$，
$$
\boxed{\qquad W_n=U_n,\qquad
      \widehat W=\widehat U .\qquad}
\tag{1166.3}
$$
理由是 $P\cap U$ 完全位于 generic fibre；
其与模 $p^n$ 闭子概形的交为空。
这是开子概形的准确相等，不是仅有相同 rational points。

R1164 §13 给
$a_P=t(-P)$、$t_P(T)=t(T-P)$ 及
$$
s_U=a_P,\qquad s_V=a_P\,t/t_P,\qquad
g_{UV}=t/t_P ,
$$
$$
u_U=f_{P,N}a_P^N,\qquad
u_V=f_{P,N}(a_Pt/t_P)^N,\qquad N=p^r.
\tag{1166.4}
$$
在 generic $U$ 上，$s_U$ 可能不是 generator。
但 (1166.3) 使它在 $\widehat U$ 成为原整 line 的
真实 generator。更具体，R1164 (1164.50) 给
$\operatorname{div}_U(u_U)=N(P\cap U)$；
故 $u_U$ 在 normal affine $U$ 正则，且其 mod-$p$
像为单位，于是在 $\widehat U$ 可逆。
$u_V$ 已为整单位，$g_{UV}$ 也在 formal overlap 可逆。

因此原 R1164 总 cocycle 可以直接取此同一 formal $U,V$；
未假设原 line 在整个 generic $U$ 上平凡。
其 pointed 根、原 $t$-leading、$a_P$ 的 vertical shift
及全部 chord/tower maps 不变。

## 2. 固定的 global ambient Frobenius

将原曲线嵌入
$\mathbb P^2_{\mathcal O[z]}$：
$$
F_{\rm hom}=Y^2Z-X^3-AXZ^2-BZ^3=0 .
$$
连同实际 base equation $g=0$ 取 $p$-完备 PD envelope，
记其 log–de Rham complex 为 $\mathscr A$。
这里先作 base PD extension，再作 cubic 的 PD envelope
得到同一对象；可由两者的 universal property 验证。
regular equations 与 flat good model 满足 Tsuji
§2 的 condition 2.1。

固定字面的 ambient map
$$
\Phi_{\rm amb}[X:Y:Z]=[X^p:Y^p:Z^p],\qquad
\Phi_{\rm amb}(z)=z^p,\qquad
\Phi_{\rm amb}|_{\mathcal O}=\sigma .
\tag{1166.5}
$$
它在整个 projective ambient space 上定义。
各 affine restrictions 及 overlaps 因而严格相容。
$\Phi_{\rm amb}(g)$ 和 $\Phi_{\rm amb}(F_{\rm hom})$
在 PD envelope 中均属于 $pD$；
后一项模 $p$ 等于 $F_{\rm hom}^p$，而
$F_{\rm hom}^p=p!\gamma_p(F_{\rm hom})$。
由原 PD divisibility，weight $w<p-1$ 的 divided map
$F_w=p^{-w}F$ 在其真实 filtered domain 上整。

(1166.5) 保原点，与 $[-1]$ 严格交换；
在产品 ambient spaces 上也与 factor permutations 交换。
它不要求 $\mathcal E$ 自身有 global Frobenius lift，
并且不把 $g$ 的非零 Frobenius carry 删除。
在 $\mathcal E^d$ 上使用 $(\mathbb P^2)^d$ 的同一
factorwise map，不另选一套 scalar Frobenius。
本篇实际 scalar weights 为 $1,5,9,14$；
需要检查 ordered tensor 精度时仍只到 $28<p-1$。

## 3. 实际几何 normal retractions

这里仅约去 cubic 的几何 normal，base $g$ 保留。
记 $\mathscr B$ 为 $\mathcal E_S$ 的 actual log–de Rham
complex，$\pi_{\rm n}:\mathscr A\to\mathscr B$
为置 cubic normal 为零的 canonical quotient。
它不依赖下面选择的 section，并保 products。

### 3.1 affine $U$ 的 Newton section

在 $Z\ne0$ chart 写
$$
f(x)=x^3+Ax+B,\qquad h=y^2-f(x),\qquad
d=4A^3+27B^2\in\mathcal O^\times,
$$
$$
C(x)=6Ax^2-9Bx+4A^2,\qquad D(x)=-18Ax+27B.
$$
原 identity 为 $Cf'+Df=d$。
从 ambient $X_0=x,Y_0=y$ 开始，
用 R1165 (1165.35) 的同一 Newton 步，
但此处保原 $A,B$，初始 residual 是 $h$：
$$
R=Y^2-f(X),\quad
a=-C(X)/d,\quad b=D(X)Y/(2d),\quad
J=1+D(X)R/d ,
$$
$$
(X,Y)\longmapsto
\left(X-aR/J,\ Y-bR/J\right).
\tag{1166.6}
$$
$J\in1+(h)$ 在 PD completion 中可逆。
每步 residual 属于前一步 residual 的平方理想，
所以第 $k$ 步以后的变化属于 $h^{2^k}$。
这里没有假设 $h\in pD$：
$$
h^m=m!\gamma_m(h)
$$
本身就使这些变化 $p$-adically 趋零。
极限 $\bar x,\bar y$ 满足原曲线方程，
与 $x,y$ 模 $(h)$ 相同，给出实际 section
$$
\iota_U:\mathscr B_U\longrightarrow\mathscr A_U,
\qquad x\longmapsto\bar x,\quad y\longmapsto\bar y.
\tag{1166.7}
$$
全过程只反除 $2,d,J$ 的单位。
$\bar x$ even、$\bar y$ odd，故 section 保原 involution。

### 3.2 $V$ 的 Hensel section

令 $s=-1/y$，取 normal
$$
h_V=s-t^3-At s^2-Bs^3 .
$$
保持 $t$，在 $h_V$ 的 PD completion 中对 $s$ 作
Hensel correction，使所得 $\bar s$ 满足
$\bar s=t^3+At\bar s^2+B\bar s^3$。
导数在 $V$ 为单位；相同的平方 residual 和 factorial
论证给整 $p$-adic 收敛。于是有
$\iota_V(t)=t,\ \iota_V(s)=\bar s$。
它保持原点和 $[-1]$。
在 overlap 上两个 normal equations 相差实际单位；
所有对象仍在 (1166.5) 的同一 global PD envelope 中比较。

### 3.3 PD normal coordinates 与显式 $K$

分别使用上述 section 和其原 normal $h_i$，有实际
PD-ring isomorphism
$$
D_i\simeq B_i\langle h_i\rangle_{\rm PD}^{\wedge_p}.
\tag{1166.8}
$$
说明其整性如下。
Newton/Hensel section 首先在普通 $h_i$-adic completion
中给出 coefficient section。
以 $h_i$ 为 normal variable 的 map 在 associated graded
上是 $B_i[h_i]\to B_i[h_i]$ 的恒等，故在所有有限
$h_i$-adic quotients 上互逆。
这些 inverse series 的系数整；
把 $h_i^m$ 写为 $m!\gamma_m(h_i)$ 后，它们在
$p$-complete PD ring 中收敛，并延伸为 (1166.8) 的
互逆 PD maps。没有反除 $m!$ 来定义一个整 inverse。

将 normal differential 放在左边，定义
$$
K_i\bigl(\gamma_m(h_i)\,\xi\bigr)=0,\qquad
K_i\bigl(dh_i\wedge\gamma_m(h_i)\,\eta\bigr)
       =\gamma_{m+1}(h_i)\eta ,
\tag{1166.9}
$$
其中 $\xi,\eta$ 是实际 coefficient/base forms。
则逐项有
$$
dK_i+K_id=1-\iota_i\pi_{\rm n},\quad
\pi_{\rm n}K_i=K_i\iota_i=K_i^2=0 .
\tag{1166.10}
$$
它保全部 base log terms。

$K_i$ 同时保 total PD/Hodge filtration：
normal differential 的 form degree 降一时，
$\gamma_m$ 变成 $\gamma_{m+1}$，PD degree 增一；
base $g$ 的 PD factor 保留。
这是后续 $p^{-w}F K_i$ 整性的具体依据。
$K_i$ 对 $p$-adic coefficient tails 连续，
所以 (1166.10) 适用于 completed complexes，
不只适用于有限 normal polynomials。

## 4. 两开集上的完整 filtered SDR

统一使用总 Čech 约定
$$
d(a_U,a_V,h)=(da_U,da_V,a_V-a_U-dh).
\tag{1166.11}
$$
在 overlap 上用 $U$ 的 normal decomposition。
令 $\Pi$ 为逐项 $\pi_{\rm n}$，并定义
$$
\mathcal I(a_U,a_V,h)=
 \left(\iota_Ua_U,\ \iota_Va_V,\
             \iota_Uh+K_U\iota_Va_V\right),
\tag{1166.12}
$$
$$
\mathcal K(a_U,a_V,h)=
 \left(K_Ua_U,\ K_Va_V,\
             -K_Uh+K_UK_Va_V\right).
\tag{1166.13}
$$
各 restriction 都是真实 overlap maps。
这两式保原 coefficient/base forms 的全部 degree。

由 (1166.10)，
$$
d(K_U\iota_V)+(K_U\iota_V)d=\iota_V-\iota_U,
$$
以及
$$
d(K_UK_V)-K_UK_Vd
       =K_V-K_U+K_U\iota_V\pi_{\rm n}.
$$
代入 (1166.11) 后得到
$$
\boxed{\quad
\Pi\mathcal I=1,\qquad
d\mathcal K+\mathcal Kd=1-\mathcal I\Pi,\qquad
\Pi\mathcal K=\mathcal K\mathcal I=\mathcal K^2=0.
\quad}
\tag{1166.14}
$$
特别 (1166.13) 的最后一槽不能省去
$K_UK_Va_V$。
所有 operators 都整、连续、保 total filtration。
本式给实际 chain-level comparison，
不是只援引两份 complexes 有相同 cohomology。

## 5. 同一 actual Frobenius、overlap 与 cone 箭头

原 ambient $F$ 在 $\mathscr A$ 的 Čech complex 上
逐项作用。把它实际转移为
$$
F_{\mathscr B}=\Pi F\mathcal I .
\tag{1166.15}
$$
在 $U$ 上，
$\pi_{\rm n}F\iota_U$ 恰为 R1165 (1165.35)–(1165.36)
的 $\Phi_U$：对 (1166.6) 逐步施 $F$ 后，
起点变为 $x^p,y^p$，所有 coefficients 变为其
$\sigma$ 像，最后置 normal 为零。
在 $V$ 上同理得到原保持 $t^p$ 的 $\Phi_V$。

因此 actual overlap homotopy 是
$$
I_{\rm PD}=\pi_{\rm n}F K_U\iota_V,\qquad
\Phi_V-\Phi_U=dI_{\rm PD}+I_{\rm PD}d .
\tag{1166.16}
$$
并且
$$
F_{\mathscr B}(a_U,a_V,h)=
 \left(\Phi_Ua_U,\Phi_Va_V,\
                 \Phi_Uh+I_{\rm PD}a_V\right).
\tag{1166.17}
$$

### 5.1 与原 $p$-small $t$-interpolation 的实质一致

令 $h_F=\pi_{\rm n}F(h_U)\in pB_{U\cap V}$。
在 (1166.8) 下，
$K_U\iota_V$ 是沿 normal 从零到 $h_U$ 的积分。
施 $\pi_{\rm n}F$ 后，其 coefficient map 是 $\Phi_U$，
而上端点是 $h_F$。
所以 (1166.16) 等于下面这条实际曲线内路径的积分：
将 $\iota_V$ 的 coefficient functions施 $\Phi_U$，
并令 normal 从 $0$ 走到 $h_F$。
起点为 $\Phi_U$，终点为 $\Phi_V$，
整条路径在同一 $p$-small étale $t$ chart 内。

对 relative one-form，在起点的该 étale coordinate 中
展开为
$$
\sum_{m\ge0}b_m\,(\Delta t)^m\,d(\Delta t),
\qquad b_m\in B_{U\cap V}.
$$
其指定 primitive
$$
\sum_{m\ge0}b_m\,\frac{(\Delta t)^{m+1}}{m+1}
\tag{1166.18}
$$
在 $\Delta t\in pB$ 上整且收敛。
因此在此 formal chart 中积分只依赖这两个端点；
不涉及全曲线的 period choice。
这证明
$$
I_{\rm PD}=I
\tag{1166.19}
$$
正是 R1165 (1165.38) 的 linear-$t$ interpolation。
对 base forms 两者都只使用同一 $\psi$，
对 $d\log z$ 的 pullback 都是 $p\,d\log z$；
混合 terms 随此相同的 factor 运输。
故 (1166.17) 锁定原 (1165.40)，而非另一份
只在 cohomology 上相同的 Frobenius。

### 5.2 第二槽的完整 normal correction

对 weight $w$，在真实 $\operatorname{Fil}^w$ 上令
$$
Q^{\rm n}_w=\Pi F_w\mathcal K,\qquad
F_{\mathscr B,w}=\Pi F_w\mathcal I,\qquad F_w=p^{-w}F .
$$
它们整，因为 $\mathcal K$ 保 filtration，
而原 divided Frobenius 在该 domain 整。
从 (1166.14) 得
$$
\Pi F_w-F_{\mathscr B,w}\Pi
       =dQ^{\rm n}_w+Q^{\rm n}_wd .
\tag{1166.20}
$$
所以实际 syntomic chain map 是
$$
\boxed{\quad
(\alpha,\beta)\longmapsto
      \bigl(\Pi\alpha,\ \Pi\beta+Q^{\rm n}_w\alpha\bigr).
\quad}
\tag{1166.21}
$$
这里的加号与原 R1164/R1165 cone convention 一致。
没有将 geometric normal 置零之后再假设原
Frobenius 也已下降；(1166.20) 正支付这份差。

## 6. 接到原 $\omega,x\omega$ 与指定 coefficient cone

在调用 curve residue contraction 前，先施 R1163 的实际
$e^-=(1-[-1]^*)/2$。上述 normal maps 均与 $[-1]$
交换，所以这一步在整 cochains 上合法，并保原 root/chord
homotopies；不把 cohomology 的 odd 性冒作每个 raw 项已 odd。
原 pointed addition identity 给
$[-1]^*K_N(P)=K_N(-P)=-K_N(P)$，
因此 projector 保持原 coefficient class 及其已给比较。
令 $\pi_{\rm E},\iota_{\rm E},H_{\rm E}$ 是 R1165
(1165.6)、(1165.9) 的 actual odd residue contraction。
使用 (1166.17) 的同一 chain Frobenius，令
$$
Q^{\rm E}_w=\pi_{\rm E}F_{\mathscr B,w}H_{\rm E}.
$$
其两个 residues 正是 R1165 (1165.45)。
两个 actual cone arrows 复合给
$$
\boxed{\quad
(\alpha,\beta)\longmapsto
 \left(\pi_{\rm E}\Pi\alpha,\
       \pi_{\rm E}\Pi\beta+
       \bigl(\pi_{\rm E}Q^{\rm n}_w+
                         Q^{\rm E}_w\Pi\bigr)\alpha\right).
\quad}
\tag{1166.22}
$$
这是原 symbol 的实际 embedding/normal/Čech 比较。
它保持 base log direction，并进入原 (1165.18)；
不能再以“不同模型间尚未给 comparison”为由
把这一步留成一条抽象同调同构。

### 6.1 原 coefficient torsor 的 $H^0$ 字面读法

仍取 cover 顺序 $U,V$，用 (1166.4) 的
$G_{UV}$ lift，并设
$$
H_{UV}=U_V/(G_{UV}^{\,N}U_U).
$$
记横线为仅去 cubic normal 的 $\pi_{\rm n}$；
不表示模 $p$、不表示 $g=0$。
R1164 的原 inverse-Miller first component 在曲线模型中为
$$
(-d_E\log\bar U_U,\ -d_E\log\bar U_V,\
                           -\log_{\rm PD}\bar H_{UV}) .
$$
因此它在原 coefficient model 的元素为
$$
x_P=A_P\omega+B_P\eta,
$$
$$
\boxed{
\begin{aligned}
A_P&=\operatorname{Res}_O\left(
       -\frac{d_E\log\bar U_U}{t}
              +(\log_{\rm PD}\bar H_{UV})\eta_V\right),\\
B_P&=-\operatorname{Res}_O\left(
                   (\log_{\rm PD}\bar H_{UV})\omega\right).
\end{aligned}}
\tag{1166.23}
$$
(1166.23) 可直接对显示的 raw components 写出：
两个 residue 都自动杀 even 部分。
确实 $t,\omega,\eta_V$ 为 odd，偶函数与这些一形式的
相应 Laurent integrands 没有 residue 项；
even one-form 除以 $t$ 的 residue 同样为零。
因此此写法与先施 $e^-$ 完全相同。
它使用原 $P\mapsto e_N(P,-)$ 的 first-slot
normalization，原点 homotopy 保持 R1164 的实际值。

这里 geometric degree 为一，所以 (1166.22) 中
降 degree 后再投到 geometric degree one 的 correction
为零；这只适用于这个 coefficient $H^0$ 输入。
完整未投影 cocycle 证明
$$
x_P\in\operatorname{Fil}^1D,\qquad
\mathcal N x_P=0,\qquad p^{-1}\Phi x_P=x_P\pmod N .
\tag{1166.24}
$$
最后一式按原 divided Frobenius 的额外精度定义，
不能以较弱的 $\Phi x_P=p x_P\bmod N$ 代替。
(1166.23) 是待实际展开的函数/residue 公式，
没有将其当作已经计算出的有限数值。
含 theta、中央 primitive 或更高 tensors 时，
(1166.22) 的第二槽不能据此删除。

## 7. actual external products 的完整有序修正

这里只需要不同 elliptic factors 的 external product；
不假设同一曲线上的 Čech contraction 严格乘法。
以下代数同时适用于 normal contraction 和
R1165 的 residue contraction。

设两个输入有 actual chain maps
$\pi_iF_i-F_i'\pi_i=dQ_i+Q_id$。
在 fixed ordered tensor SDR 下取
$$
Q_{12}=Q_1\otimes\pi_2F_2+
                         F_1'\pi_1\otimes Q_2 .
\tag{1166.25}
$$
tensor maps 使用 usual Koszul convention。
因此对 degree $k$ 的 $\alpha$，
第二项作用时自带 $(-1)^k$。
这也正是从
$H_{12}=H_1\otimes1+\iota_1\pi_1\otimes H_2$
计算 $\pi_{12}F_{12}H_{12}$ 的结果。

令
$$
T_i(\alpha,\beta)=
           (\pi_i\alpha,\pi_i\beta+Q_i\alpha)
$$
并在两边使用原 ordered cone product
$$
(\alpha,\beta)(\gamma,\delta)=
 (\alpha\gamma,\ \beta\gamma+(-1)^kF_1(\alpha)\delta).
$$
这里 $F_i$ 表示相应 weight 的 divided chain map。
则
$$
P_B(T_1a,T_2b)-T_{12}P_A(a,b)
 =d\mathcal H(a,b)+\mathcal H(da,b)
                       +(-1)^k\mathcal H(a,db),
$$
$$
\boxed{\qquad
\mathcal H(a,b)=
          \left(0,\,(-1)^kQ_1\alpha\otimes\pi_2\delta\right).
\qquad}
\tag{1166.26}
$$
这是对任意 cochains 的身份，不只对 closed classes。

证明只需展开第二槽。
$Q_2$ 的项相消后，左侧为
$$
Q_1\alpha\otimes\pi_2(1-F_2)\gamma+
 (-1)^{k+1}(dQ_1+Q_1d)\alpha\otimes\pi_2\delta.
$$
对 (1166.26) 取全部三个 differential terms，
得到同一式；尤其保留了非闭 primitive 所需的
$Q_1d\alpha$ 项。

若原实际中央 cochain 满足 $dh=-P_A(a,b)$，
而 $a,b$ 闭，则 target 的指定 primitive 是
$$
\boxed{\qquad T_{12}h-\mathcal H(a,b).\qquad}
\tag{1166.27}
$$
degree-one factors 使 $\mathcal H$ 的第二槽为负；
故此处应加回 $Q_1\alpha\otimes\pi_2\delta$。
它不同于 R1165 (1165.23) 在两种 cone products
之间的 $-\beta\delta$；两份原 ordered corrections
都应保留。

对十二个 factors 以及 theta/base slots，
按固定 binary parenthesization 迭代 (1166.25)–(1166.26)。
每次复合的同伦使用准确公式
$H_2f_1+g_2H_1$；
所以给出有限的实际链运算，不需要另称一个
未写出的 $A_\infty$ comparison 存在。
最后施原 signed/paired projectors。
tensor homotopy 如需严格 permutation invariance，
按 R1165 的方法平均；只除 $d!$、$2^d$，
在 $d\le12<p$ 时均为单位。

由此原 R1163 的 $\Pi_0,\Pi_2,\Pi_4$ 和实际
Poincaré coevaluation 保持其先前归一。
没有把 paired projectors 当成互相正交，
也没有另给 $\lambda_\infty x\gamma_5$ 选择常数。
同根 chord、tower 与 norm cochains先按 R1164、
R1159–1160 的原式附上，再用上述 actual maps运输。

## 8. 有限精度、同源范围与仍待取值的量

所有 normal sections、$\Pi,\mathcal I,\mathcal K$、
$F_{\mathscr B}$ 和 $Q$ 均已由原曲线、原 PD embedding
与明确收敛级数定义。
它们保 $p$-adic continuity 和原 filtered domains；
所需 extra precision 在 divided Frobenius 之前保留。
几何 normal 已被完整积分收缩，base normal $g$
继续留在原 $S$ 中；二者不得混为一项。

在此 model 中，可直接按 R1164 (1164.30)、
(1164.32)、(1164.35) 形成实际代表，
再用 (1166.22)、(1166.26) 投影。
之后才应用 R1162 的整 $e$-blocks、
R1155 §16 的 evaluation 窗口，
以及 R1165 (1165.26)–(1165.33) 的 normal connection
和 precision ideals。
本篇不在整个 complex 中删掉 $\gamma_p(g)$，
也不把函数 Taylor 阶数与 coefficient weight 混同。

对分歧标记域的 closed-point Cor，
原 generic Galois/étale Cor 与同一 root/coset homotopies
继续按 R1163 的实际 comparison消费；
本篇不额外宣布一个尚未指定坐标的 ramified PD trace。
上述 maps 已给每个指定 coefficient/base 的字面输入，
但实际 theta/norm sums、指定中央 primitive 的各项、
以及最终 $F_0$ 的 normal/residue coefficients
仍须真正取值。

因此本篇关闭的是原 scalar Miller symbols
到 actual filtered coefficient cone 的
embedding、normal、Čech/Frobenius 与 external-product 比较。
它没有证明原中央最高项非零，
没有将某个只满足同一 cohomology 条件的局部 primitive
代替原 global canonical primitive，
也没有完成一般 $p$ 的原同点排除。

## Primary 与已登记输入

- T. Tsuji, *On p-adic nearby cycles of log smooth families*,
  Bull. Soc. Math. France **128** (2000), 529–575，
  [正式原文](https://www.numdam.org/article/BSMF_2000__128_4_529_0.pdf)。
  本篇使用 §1 的 PD differential/embedding 描述及 §2
  的实际 syntomic embedding、divided Frobenius、symbol/product。
  本篇各 normal contractions、Čech formulas、
  Frobenius matching 与有序 product homotopy均由正文自证。
- [R1164](R1164-original-pointed-Miller-coefficients-and-Cech-symbols.md)：
  原 inverse-Miller/first-slot Weil 归一、整 line、
  pointed roots、PD cocycle、chord/tower 及 SS actual frames。
- [R1165](R1165-original-integral-residue-contraction-and-log-PD-cone.md)：
  实际 $\omega,x\omega$ 收缩、base log cone，
  §§6–7 的有序修正及 §10 的 actual $\Phi_U,\Phi_V,I$。
- [R1163](R1163-original-highest-moment-integral-syntomic-comparison.md)：
  原完整四十三维 coefficient/direct-summand normalization、
  scalar comparison 与指定 primitive groupoid。

全文为纸面证明，无数学程序执行。


## 9. 原第一层 CM 标记域上的 tame PD trace

以下各节只处理原 Gaussian/cubic supersingular CM 中心的
**第一层**标记域，不把高层有 wild ramification 的域也称为 tame。
令 $F/\mathbb Q_p$ 为实际未分歧底，已包含
$\mathbb Q_{p^2}$ 及所需 prime-to-$p$ 辅助数据。
需要回到原较小未分歧底时，最后再作真实 unramified trace。

[R712 §2](R712-actual-M2-second-digit-and-Lubin-Tate-two-block-reduction.md)
及 [R978 §2](R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md)
已固定原 strict LT 坐标；在本节的 CM 情形同样使用该坐标：
$$
[-p]z=-pz+z^{p^2},\qquad
[\zeta]z=\zeta z\quad(\zeta\in\mu_e),\qquad e=p^2-1.
$$
原标记点 $P=P(\varpi)$ 满足 $\varpi^e=p$，并且
$$
L=F(\varpi),\qquad
\operatorname{Gal}(L/F)=\{\tau_\zeta:\varpi\mapsto\zeta\varpi\}
 \simeq\mu_e .
\tag{1166.28}
$$
这是同一原 $E[p]\setminus0$ 的实际单轨道；
没有用另一个只具有相同 tame 指数的形式模型替换 $P$。

### 9.1. 两个实际 PD embedding 及全部 log 尺度

为免与曲线坐标混淆，本节以 $u$ 表示较小底的 embedding
变量，而不是四线参数。定义
$$
\begin{aligned}
S_F&=\mathcal O_F[u,\gamma_r(u-p):r\ge1]^\wedge_p,\\
S_L&=\mathcal O_F[z,\gamma_r(z^e-p):r\ge1]^\wedge_p,
\qquad u\longmapsto z^e .
\end{aligned}
\tag{1166.29}
$$
两处同记 $g=u-p=z^e-p$。这些是原 log embeddings
$u\mapsto p$、$z\mapsto\varpi$ 的 PD rings；映射 (1166.29)
不在计算开始前令 $g=0$。

由单项式除法及相同的 divided powers，逐 $p$-进精度有
$$
S_L=\bigoplus_{j=0}^{e-1}z^jS_F,\qquad
S_L^{\mu_e}=S_F .
\tag{1166.30}
$$
第一式也可由
$S_L=S_F[z]/(z^e-u)$ 的 $p$-完备形式得到。
$\tau_\zeta$ 固定 $g$，在第 $j$ 块上乘 $\zeta^j$。
当 $0<j<e$ 时，存在 $\zeta$ 使 $\zeta^j-1$ 为单位，
所以第二式是整等式，不仅是有理 invariants 等式。

两处 Frobenius 分别为
$\psi_Lz=z^p$、$\psi_Fu=u^p$，系数上都是同一 $\sigma$。
实际有
$$
\psi_L\tau_\zeta=\tau_\zeta\psi_L,\qquad
N_z|_{S_F}=eN_u,\qquad
d\log u=e\,d\log z .
\tag{1166.31}
$$
第一式使用 $\sigma(\zeta)=\zeta^p$；
不能将 $\psi$ 当成固定所有 Teichmüller 系数的映射。

设 $a=\sum_{j<e}z^ja_j$。真实 trace 及 log trace 为
$$
\boxed{\quad
\operatorname{Tr}_0(a)=e\,a_0,\qquad
\operatorname{Tr}_1(a\,d\log z)=a_0\,d\log u.
\quad}
\tag{1166.32}
$$
第二式是先在 $L$ 上作 $\sum_\zeta\tau_\zeta$，
再按 (1166.31) 识别 invariant differential。
因此不能把 coefficient cone 的每一槽都机械乘 $e$。
几何 differential 因子不改变 (1166.32)：
没有 base-log 因子的项使用第一式；带一个 base-log 因子的项
使用第二式，并保其原 wedge 次序。

例如
$\operatorname{Tr}_1(d a)=e\,N_ua_0\,d\log u
=d\,\operatorname{Tr}_0(a)$。
由此及 (1166.31)，trace 与总 differential、Hodge/PD
filtration、实际 divided Frobenius 全部交换。
它给 R1165 的完整 log-PD cone 的链映射，而不是只给
$H^0$ 或一个没有 $N$ 的复形的映射。

### 9.2. 为什么这里是原 corestriction，不是平均

取实际椭圆乘积、原 coefficient projector 以及
R1163 的小权比较。Tsuji §2 的 comparison 对底的 morphism、
actual embedding refinements 和全部 $\tau_\zeta$ 都函子相容。
在本处 $e\in\mathbb Z_p^\times$，有限群 invariants 为 exact。
所以 comparison 下的 restriction 把原底 cohomology
识别为真实 $L$-cohomology 的 $\mu_e$ invariants。

这个识别也能在所选有限 group resolution 上明确实现。
对 $\mu_e$ 的 homogeneous equivariant cochain，
取
$$
(hf)(g_0,\ldots,g_{a-1})
 =\frac1e\sum_{\zeta\in\mu_e}
               f(\zeta,g_0,\ldots,g_{a-1})\qquad(a\ge1).
\tag{1166.33}
$$
在正 group degree 有 $dh+hd=1$；
degree zero 的余项是 invariant projector。
对内部复形加通常总复形符号后，同一公式仍成立。
这里的 $1/e$ 只用于消去正 group degree，
**不**把 corestriction 改成 $e^{-1}\sum\tau_\zeta$。

在 generic fibre 的原有限 étale Galois cover 上，
restriction 后的 corestriction 是 $\sum_\zeta\tau_\zeta$，
且 corestriction 后的 restriction 在原底是乘 $e$。
comparison 的函子性与上述整 invariant 识别遂唯一确定：
(1166.32) 正是原 corestriction 的实际 PD 链代表。
这没有援用一个未给出的 wild ramified trace 定理；
这里只使用同一 explicit tame embedding 和原小权比较。

对 unit lift $V$，可直接核同一结论：
$$
\sum_\zeta\tau_\zeta\,d\log V
  =d\log\prod_\zeta\tau_\zeta V,\qquad
\sum_\zeta\tau_\zeta\,
 \frac1p\log\frac{V^p}{\psi V}
 =\frac1p\log
       \frac{(\prod_\zeta\tau_\zeta V)^p}
            {\psi(\prod_\zeta\tau_\zeta V)} .
\tag{1166.34}
$$
第二式的每个 logarithm 都在 $1+pS_L$ 上。
Miller line 的 norm 也逐 frame 使用同一乘积；
overlap 的 $1+J$ PD logarithms 相加，
而实际同根 phases 沿 R1164/R1159 的 cochain 留在输入中。

## 10. Trace 与原 ambient、留数及 ordered products 的交换

曲线 $\mathcal E$ 在本节固定于 $F$。
$\tau_\zeta$ 只作用于实际 base/source 参数及其共轭值。
第 3 节的 Newton normal retractions、$K_U,K_V$、
第 4 节的 $\Pi,\mathcal I,\mathcal K$，
以及 R1165 的 residue maps $\pi_E,\iota_E,H_E$，
全部由同一曲线的固定公式构造，因而逐项与 $\tau_\zeta$ 交换。
第 5 节的 actual Frobenius 及其 $Q_w$ 也交换，
因为 (1166.31) 包括了系数的 $\sigma$。

于是可在原 ambient input 上先取 trace，
或先用 (1166.22) 投到 coefficient cone 后再取 trace；
两者是同一链映射。base-log 项必须始终使用 (1166.32)
的第二式。这里没有把 $Q_w$ 或法向 $g$-项设为零。

对原 ordered cone product $P$，若一因子来自 $F$，准确有
$$
\begin{aligned}
\operatorname{Tr}P_L(a,\operatorname{res}b)
 &=P_F(\operatorname{Tr}a,b),\\
\operatorname{Tr}P_L(\operatorname{res}a,b)
 &=P_F(a,\operatorname{Tr}b).
\end{aligned}
\tag{1166.35}
$$
这是 (1166.32) 的 module-trace identity 和 $\psi$ 相容性
逐槽给出的 projection formula。
对两个都来自 $L$ 的因子，实际表达式则是
$$
\sum_\zeta P_L(\tau_\zeta a,\tau_\zeta b),
\tag{1166.36}
$$
不能换成 $P_F(\operatorname{Tr}a,\operatorname{Tr}b)$，
也不能改成两个独立的 $\zeta,\zeta'$ 求和。

(1166.25)–(1166.27) 的 external-product correction
同样对共同的 $\tau_\zeta$ 等变。
故每个实际 central primitive 都必须连同原有序
$\mathcal H$、cone-product 修正和 R1159 的 same-coset
$R,L,K,\eta_d$ 一起进入 trace。
本节给的是这些既定 inputs 的严格传递；
没有将某个只差 cohomology class 的 primitive 任意替换为零。

若原底还需有限未分歧下降，继续对实际系数 Galois action
求和即可。这里仍取真实 field trace；
若为证明 invariants exactness 使用平均，必须另外乘回域次数。
源的 Weil 标记、原 Miller phase 与系数上的 Frobenius
各沿原作用运输，不能仅凭“未分歧”将这些作用认成恒等。

## 11. 原第一层完整 theta moment 的实际两个输入槽

### 11.1. 原 coefficient trace 精确为零

记 $x_P$ 为 (1166.23) 在 $N=p$ 的
**实际 pointed Miller** coefficient $H^0$ 代表。
这里先用其定义，不预用任何待算的 $A_P,B_P$ 显式值。
沿 R1163/R1164，它准确对应 $P\in E[p]$。
对 $d=4,8,12$，令
$x_P^{[d]}$ 为同一 normalized signed-projector 下的
pure power；它对应 $P^d$，不另乘 $d!$。

在 $\mathbb F_{p^2}$ 上，原 CM tame action 的两个
characters 是 $\zeta,\zeta^p$。
其 $\operatorname{Sym}^d$ 的 characters 因而为
$\zeta^{\,d+(p-1)i}$，$0\le i\le d$。
由于 $0<d\le12<p-1$，
所有这些指数严格介于 $0$ 与 $e=p^2-1$ 之间。
故
$$
\boxed{\qquad
\sum_{\zeta\in\mu_e}\tau_\zeta x_P^{[d]}=0
       \quad\text{in the actual coefficient }H^0 .
\qquad}
\tag{1166.37}
$$
coefficient cone 在此 degree 没有负一项，
所以 (1166.37) 也是所选 $H^0$ 链代表的字面等式；
不是把一个未知 boundary 丢掉。
此证明不需要 Bernoulli-unit 条件。

### 11.2. 正规化 theta 时哪些项确能消去

固定原实际辅助数 $c$，$(c,p)=1$，并令原
$k_d(c)=c^2-c^{-d}$ 为单位。
在原 formal group 上，trace-fixed theta 的 divisor
为 $c^2[O]-[E[c]]$；
所有非零 $c$-torsion 与原 formal identity disc 分离。
因此在 $p$-local multiplicative group 中可写
$$
[\theta_c(P(z))]
 =[a_c]+(c^2-1)[z]+[V_c(z)],
\qquad
V_c(z)\in1+z\mathcal O_F[[z]] .
\tag{1166.38}
$$
$a_c$ 是同一 theta 和 strict LT coordinate 的实际 leading
常数类，不能事先改为 $1$。

若原 theta 先以 prime-to-$p$ 次幂的实际函数给出，
先取该函数的真实 leading，再对 normalized
$1+z\mathcal O_F[[z]]$ unit 取唯一同次根：
系数递推只除这个 prime-to-$p$ 次数。
这正是原 $p$-local Kummer automorphism，
不另加一个有待选择的 field root 或 period。

原 $\kappa(a_c)$ 来自底，$\kappa(z)$ 在此 PD model 中是
$(d\log z,0)$，而 $\tau_\zeta z/z=\zeta$
的 $p$-primary Kummer class 为零。
其实际 symbol 也为零，因为
$d\log\zeta=0$、$\psi\zeta=\zeta^p$。
结合 (1166.37) 及真实 projection formula，
(1166.38) 的前两项在完整 coefficient trace 中确实消失。
这是由原 all-vector sum 付清的消去；
不允许在单点的 Kummer class 或 central primitive 中
先删除 $a_c$ 和 $z^{c^2-1}$。

定义
$$
D_c(z)=\frac{N_zV_c(z)}{V_c(z)},\qquad
L_c(z)=\frac1p\log\frac{V_c(z)^p}{\psi V_c(z)} .
\tag{1166.39}
$$
两者为整输入：第一项是实际 logarithmic derivative；
第二项的比值在 $1+p\mathcal O_F[[z]]$。
无需假定未经微分的 $\log V_c$ 本身在整格中。
这些单位按原实际 torsion specialization 给出，然后在
同一 ambient ring 中取显示 lift；
没有要求 $\psi$ 保持 $z^e-p$ 的理想。

### 11.3. 原 moment 的 literal coefficient-cone formula

R1164 (1164.25) 的原闭点集合在这里只有一个 $L/F$ 轨道。
原 all-vector moment 准确变为
$$
\boxed{\quad
\widetilde{\mathsf M}_{d,1}
 =\frac1{k_d(c)}\operatorname{Tr}_{L/F}
  \left(x_P^{[d]}\cdot
       (D_c(z)\,d\log z,\ L_c(z))\right).
\quad}
\tag{1166.40}
$$
这里是原 degree-one coefficient syntomic cone 的等式，
并保原 gauge class，不仅是一个函数域 symbol 的等式。

其 ordered-product 方向可直接检查：
theta 在第一槽，$x_P^{[d]}$ 是 degree-zero coefficient
cycle，满足原 divided-Frobenius 固定方程。
theta 因子只来自 base，故其 geometric-normal
$Q$ 为零；(1166.26) 在这次外积不增加 correction。
内部 pure coefficient power 已在同一个 $H^0$ 中，
没有可隐藏的负一次同伦。
这不表示后继两个 moments 的中央 ordered product
也没有 correction。

将实际两个系数按 (1166.30) 展开：
$$
x_P^{[d]}D_c(z)=\sum_{j<e}z^j A_{d,j},
\qquad
x_P^{[d]}L_c(z)=\sum_{j<e}z^j B_{d,j}.
$$
则原输入为
$$
\boxed{\qquad
\widetilde{\mathsf M}_{d,1}
 =\frac1{k_d(c)}
       \left(A_{d,0}\,d\log u,\ e B_{d,0}\right).
\qquad}
\tag{1166.41}
$$
所有 $A_{d,j},B_{d,j}$ 仍保其实际 $g$-normal coefficients。
本式没有把 scalar 与 base-log 两槽的域次数混为一谈，
没有额外的 $1/e$、$1/d!$ 或 half-vector 因子。

R1147 §§17–18 的 primitive moment 是
$(1-p^d)\widetilde{\mathsf M}_{d,1}$；
第一层系数中该因子约为 $1$。
若比较实际 compatible roots，仍使用原 same-root gauge，
不因第一层 class 相等而把高层 gauge 删除。

## 12. 辅助数 2 的无新根、无未知 leading 的实际单位

对原两个 moment $d=4,8$，可直接取 $c=2$。
[R1157 (1157.27)](R1157-original-integral-SV-Manin-triangle-filling.md)
由真正 norm 已锁定
$$
4[\theta_2]=[\Delta/(16y^4)].
$$
在同一 strict LT coordinate 中定义
$$
W(z)=-z^3y(P(z))\in1+z\mathcal O_F[[z]] .
\tag{1166.42}
$$
常数项为 $1$ 是因为 $t=-x/y$、$z/t\to1$，
以及 $y=-t^{-3}+\cdots$；
这里没有重新缩放原 $\omega$、$P$ 或 $z$。

直接代入给
$$
[\theta_2(P(z))]
 =\tfrac14[\Delta/16]+3[z]-[W(z)] .
\tag{1166.43}
$$
因此在 (1166.40) 中可取
$$
\boxed{\qquad
V_2(z)=W(z)^{-1}
      =-\frac1{z^3y(P(z))}.
\qquad}
\tag{1166.44}
$$
没有选择 $\Delta$ 的第四根。
$\Delta/16$ 和 $z^3$ 不是在原 theta 中被遗忘，
而是按 (1166.37)–(1166.40) 在完整 moment trace 后消去。
原 $4^{-1}$ 仍是同一个 Kummer tower automorphism。

两个原平滑系数为
$$
k_4(2)=\frac{63}{16},\qquad
k_8(2)=\frac{1023}{256};
$$
它们对所有 $p>37$ 都是单位。
所以原 $\mathsf M_4,\mathsf M_8$ 的第一层实际输入
由同一个明确的函数 (1166.44)、各自的
$x_P^{[4]},x_P^{[8]}$ 和 (1166.41) 给出。
对于 $d=12$，$k_{12}(2)$ 可能在 $p=43,127$ 非单位；
该处仍取原已允许的另一个辅助数，不反除这个非单位。

## 13. 本次读回关闭的接口和剩余计算

(1166.28)–(1166.44) 支付的是原第一层 CM 标记域的
真实 corestriction、完整 log 尺度、same-model
Frobenius/residue 交换，以及两条原 theta moments 的
实际 coefficient-cone 输入。它们对全部第一层非零点
求和，没有删去 rank-one 或 rank-two 后继点对。

原 $x_P$ 及 (1166.42) 均沿已固定的 Miller/LT 来源。
可以进一步将它们实际展开，再使用 R1162 的 $e$-block
到 $g$-normal 转换及 R1155 §16 的有限 FL 窗口。
这些公式没有把函数的 $z$-series 截成 degree $12$，
没有在 $\psi$ 前令 $g=0$，也没有由系数权幅断言
所有高 function blocks 消失。

对指定 central primitive，仍须把原完整 raw functions、
actual root gauges、ordered products 和 cochain
corestrictions 一并按 §§5–10 搬运。
尤其 (1166.41) 不是 $F_0$ 中央条目的值，
也不宣原最高组合为单位。
本篇的新增结论不依赖一个未知的 rational comparison，
但不把尚未展开的实际 source 数据冒称为已经读出的数字。

补充 primary：Tsuji 正式论文 §2 的 (2.5)–(2.8)、
Proposition 2.11 给本处 actual symbol/product 与底变换的
函子性；§4 末段及 Appendix A 的 tame-base-change
描述与 (1166.30) 相容。本篇 trace 的整分解、
log 尺度与 finite-group contraction 已在正文直接证明。

本次附节为纸面证明，无数学程序执行。


## 14. 原 Steinberg primitive 的 actual syntomic 第二槽

本节将 R1155 的同一原 $\mathscr D_U$ 接入本篇的实际
PD cone。先固定一个 $p$-torsion-free 的原 $p$-完备
PD/log differential ring $D$，以及同一个 Frobenius lift
$\Phi$。本节的 $\mathrm d$ 始终是这个 ring 上的总
de Rham differential，包括实际 base-log 方向。
不在一个含分歧的 residue field 上另造 Frobenius。

先假设 $U,1-U\in D^\times$。置
$$
\begin{gathered}
w=U^p,\qquad d_0=1-w,\qquad
v=\Phi U=w+\delta,\quad\delta=p\varepsilon,\ \varepsilon\in D,\\
a=\mathrm d\log U,\qquad b=\mathrm d\log(1-U),\\
A=\frac1p\log\frac{U^p}{\Phi U},\qquad
B=\frac1p\log\frac{(1-U)^p}{\Phi(1-U)},\qquad
B_0=\frac1p\log\frac{(1-U)^p}{1-U^p}.
\end{gathered}
\tag{1166.45}
$$
$w,d_0,v,1-v$ 全为单位，三个 logarithm 的参数在
$1+pD$。这里 $\Phi(1-U)=1-v$，不是另外独立选择的提升。
记 $\varphi_1(a)=p^{-1}\Phi(a)=p^{-1}\mathrm d\log v$。
于是原 Kummer symbols 为
$$
C_\Phi(U)=(a,A),\qquad C_\Phi(1-U)=(b,B).
$$
原 ordered product，按 R1164/R1165 的固定约定，是
$$
C_\Phi(U)C_\Phi(1-U)
 =\left(0,\ A b-\varphi_1(a)B\right),
\tag{1166.46}
$$
因为 $a\wedge b=0$。

定义
$$
\begin{aligned}
L^\dagger_2(U)&=\operatorname{Li}_2^\dagger(U),\\
J(U,\delta)&=\frac1{p^2}
 \int_0^\delta
       \frac{\log(1-t/d_0)}{w+t}\,dt,\\
\beta_\Phi(U)&=L^\dagger_2(U)+A B_0+J(U,\delta).
\end{aligned}
\tag{1166.47}
$$
这里的积分定义为下节给出的整收敛幂级数；
它不是先选一条未知 Coleman path。
$L^\dagger_2$ 也使用 R1155 已付的同一 overconvergent
normalization，常数在 $U=0$ 为零。

**原实际 primitive 公式为**
$$
\boxed{\qquad
h_{\mathrm{syn},\Phi}(U)=(0,\beta_\Phi(U)),
\qquad
d_{\mathrm{syn}}h_{\mathrm{syn},\Phi}(U)
       =-C_\Phi(U)C_\Phi(1-U).
\qquad}
\tag{1166.48}
$$
所以它与原中央 cochain 的 $dh=-\Omega$ 同号。
不要将 R1155 的 Frobenius matrix 中央坐标 $h_R$
直接写成这里的 $\beta_\Phi$；两者的差见 §16。

### 14.1. 完整微分核验

一方面，原 Eulerian series 或同一
$\operatorname{Li}_2^p(U)-p^{-2}\operatorname{Li}_2^p(U^p)$
给
$$
\mathrm dL^\dagger_2=-B_0a,\qquad
\mathrm dA=a-\varphi_1(a),\qquad
\mathrm dB_0=b-\varphi_0(b),
$$
其中
$$
\varphi_0(b)=\frac1p\,\mathrm d\log(1-U^p)
           =-\frac{\mathrm dw}{p\,d_0}.
$$
另一方面，直接对 (1166.47) 的收敛级数逐项微分，
或先对 universal variables $(w,\delta)$ 计算两个偏导，得到
$$
\mathrm dJ
 =A\,\varphi_0(b)-(B-B_0)\varphi_1(a).
\tag{1166.49}
$$
例如 $\delta$ 偏导为
$p^{-2}\log(1-\delta/d_0)/(w+\delta)$；
$w$ 偏导为
$$
\frac1{p^2}
 \left\{\frac{\log(1-\delta/d_0)}{w+\delta}
       +\frac1{d_0}\log(1+\delta/w)\right\}.
$$
两式使用 $d_0=1-w$，包括其导数；
不能在求导时把 $w,d_0$ 当成两个独立常数。

相加给
$$
\mathrm d\beta_\Phi
 =A b-\varphi_1(a)B.
\tag{1166.50}
$$
而 degree-one cone 的 differential 在第一槽为零时是
$d_{\mathrm{syn}}(0,\beta)=(0,-\mathrm d\beta)$，
故得到 (1166.48)。
这先是整复形中显式代表的等式，然后才可约模 $p^n$。

## 15. 原单位域上的整性、有限精度和完整 carry

### 15.1. 无隐藏普通 logarithm 的整定义

设 $\mathcal E_m(T)$ 为整数 Eulerian polynomial，
约定
$$
\sum_{k\ge0}k^mT^k
   =\frac{\mathcal E_m(T)}{(1-T)^{m+1}},
\qquad \mathcal E_0=1 .
$$
原 dagger dilogarithm 在这里准确为
$$
L^\dagger_2(U)=
 \sum_{j=1}^{p-1}\frac{U^j}{j^2}
  \sum_{m\ge0}(-1)^m(m+1)
       \left(\frac pj\right)^m
       \frac{\mathcal E_m(U^p)}{(1-U^p)^{m+1}}.
\tag{1166.51}
$$
这是把 $p\nmid n$ 的原级数按 $n=j+pk$ 分组；
先在 $|U|<1$ 比较，再由相同的整有理表达式作
$p$-adic continuation。因为 $d_0$ 是单位，(1166.51)
逐项整且 $p$-收敛。它不使用一个未经证明整性的
$\log U$ 或 $\log(1-U)$ 作为定义。

短积分的准确展开为
$$
\boxed{\quad
J(U,p\varepsilon)=
 \sum_{n\ge2}\frac{p^{\,n-2}\varepsilon^n}{n}
       \sum_{r=1}^{n-1}
        \frac{(-1)^{\,n-r}}{r\,d_0^r w^{\,n-r}} .
\quad}
\tag{1166.52}
$$
前项是 $-\varepsilon^2/(2wd_0)$。
因为 $nr\mid n!$，第 $n$ 项的估值至少
$n-2-v_p(n!)$，所以全部项整且尾趋于零。
这也给实际 divided weight two 的整性；
不是只说积分的有理值存在。

### 15.2. 可直接读任意所需小精度

设 $1\le M\le29$，$p>37$。
模 $p^M$ 时：

- (1166.51) 只需 $0\le m<M$；
- (1166.52) 只需 $2\le n\le M+1$；
- $A$、$B_0$ 的 $p^{-1}\log(1+pT)$ 只需前 $M$ 项。

例如 $n\ge M+2$ 的积分尾估值已至少为 $M$；
对 $n<p$ 直接由 $n-2\ge M$，
对 $n\ge p$ 用
$v_p(n!)\le n/(p-1)$ 给更强的界。
原所有 inputs 均整，故乘积 $AB_0$ 不损失这份精度。
若后续还要除 $p^i$，先按原规则计算到
$p^{i+1}$ 或所需的更高精度，再作除法；
不把本节的模 $p$ 式先当成可任意反除 $p$ 的式子。

记 $\ell_r(U)=\sum_{j=1}^{p-1}U^j/j^r$。
保留实际 $\varepsilon$ 和全部 nilpotents 的第一层公式是
$$
\boxed{\quad
\beta_\Phi(U)\equiv
 \frac{\ell_2(U)}{d_0}
 +\frac{\varepsilon\,\ell_1(U)}{w d_0}
 -\frac{\varepsilon^2}{2w d_0}
 \pmod{pD}.
\quad}
\tag{1166.53}
$$
本式的中间线性项不能删除。
它是 actual syntomic primitive 的一部分，
即使在某个 Frobenius matrix 的中央槽中该项会与
$AB$ 抵消。

## 16. 原 ordered Frobenius、同根塔和改变提升的规范

### 16.1. 与原 $\mathscr D_U$ 的中央坐标逐式匹配

这里只为核定原规范，在 rational period ring 中写
$\lambda=\log U$、$\mu=\log(1-U)$。
原 R1155 whole path variation 的 Hodge matrix 是
$$
G(U)=\mathcal H(\lambda,\mu,-\operatorname{Li}_2^p(U)),
\qquad
\mathrm d\lambda=a,\quad \mathrm d\mu=b,
$$
其左 Maurer–Cartan connection 的中央分量为零。
按照同一正向 Frobenius，
$$
R_\Phi(U)=G(U)\,
  \mathcal H\left(\frac{\log v}{p},
                 \frac{\log(1-v)}p,
                 -\frac{\operatorname{Li}_2^p(v)}{p^2}\right)^{-1}.
$$
两个一次槽准确为 $A,B$。原 ordered 群律给
$$
\begin{aligned}
h_R
 &=-\operatorname{Li}_2^p(U)
      +p^{-2}\operatorname{Li}_2^p(v)
      -A\,p^{-1}\log(1-v),\\
\boxed{\quad h_R&=AB-\beta_\Phi(U).\quad}
\end{aligned}
\tag{1166.54}
$$
第二式使用等价的 rational identity
$$
\beta_\Phi
 =\operatorname{Li}_2^p(U)
    -p^{-2}\operatorname{Li}_2^p(v)+A\log(1-U);
$$
其**整定义**仍是 (1166.47)，并非这个含普通 logarithm 的式子。

还有一个完全在短运输中的核验。设 $R=B-B_0$，则
$$
A R-J
 =-\frac1{p^2}\int_0^\delta
       \frac{\log(1+t/w)}{d_0-t}\,dt.
\tag{1166.55}
$$
这是对两 logarithm 的乘积作分部积分。
右边正是 R1155 §8 的同一个 ordered 中央运输；
因而 (1166.54) 没有反向路径、交换首槽或未知中央常数。
特别 (1166.53) 与
$$
h_R\equiv-\frac{\ell_2(U)}{d_0}
             -\frac{\varepsilon^2}{2wd_0}\pmod{pD}
$$
准确相容，而不是两个竞争的规范。



同一号也适用于原全部中心的 bilinear group，而非只适用于
这个标量例子。若群律为
$(v,z)(v',z')=(v+v',z+z'+\mathfrak b(v,v'))$，
令左 Maurer–Cartan connection 为 $(a,\eta)$，
则原 syntomic primitive 的第一槽是 $c=-\eta$，
使 $\mathrm dc=-\mathfrak b(a,a)$。
设同一 Frobenius 的一次 translation 为 $A$、中央为 $Z$。
直接计算
$\mathrm dR\,R^{-1}=\Omega-\operatorname{Ad}(R)\varphi\Omega$
给
$
\mathrm dZ=(1-\varphi)\eta
       +\mathfrak b(a,A)-\mathfrak b(A,\varphi a).
$
因此其原 primitive 第二槽 $H$ 满足
$
\boxed{\qquad Z=\mathfrak b(A,A)-H.\qquad}
\tag{1166.54a}
$
因为右边的 differential 与 primitive cone 方程完全一致，
原同一 Hodge/root 刚化固定常数。
$\mathfrak b$ 必须是原三个 $\Pi_r$ 及
$+\lambda_\infty x\gamma_5$ 所组成的完整 ordered bilinear map。
若先更换 cochain representative 或作系数收缩，
必须先运输其 product homotopy；不能把任意线性读取的
$H$ 未经这些修正就代进 (1166.54a)。

### 16.2. 先锁定整兼容塔，再作含分歧 pullback

(1166.47) 在 $D$ 中整收敛，故其全部模 $p^n$ 代表
严格约化相容。(1166.48) 因而给同一 Kummer quotient 的
**整兼容** class-two primitive；不能只取某一层的
有理解再随意选整格。

原性可先在未分歧 universal base 上核准。
取三穿孔直线的原 good formal chart，以及随后使用的
log boundary charts；它们的 generic analytic components
几何连通，且有原未分歧底上的点。
标量权一、二的 Tsuji comparison 在 $q\le2$ 精确，
并保持原 Kummer/product。
因此上述整 nullhomotopy 对应一个实际 compatible
étale Heisenberg lift，带同一两个 root quotients。

其 rational realization 的 connection、filtration 和
Frobenius 正是 (1166.54) 的原 whole path object。
R1155 §§1、15 已将该整个 variation 与原
$\alpha,\beta,\Gamma$ 函数根塔、原 Tate generator
及切向 leading 认同；不是在一个孤立 fibre 上任选同构。

这里没有剩余的“rationally zero 但 integrally different”
compatible 中央 twist。事实上，在未分歧底 $F$ 上
$$
H^0\bigl(Y,\mathbb Q_p/\mathbb Z_p(2)\bigr)=0:
$$
其任何非零有限阶不变量的最高 $p$ 倍会给一个
$\mathbb F_p(2)$ 不变量，而未分歧 $F$ 的 cyclotomic
模 $p$ 像为 $\mathbb F_p^\times$，$p>3$ 时平方字符非平凡。
由系数正合列遂有
$$
H^1\bigl(Y,\mathbb Z_p(2)\bigr)
   \hookrightarrow H^1\bigl(Y,\mathbb Q_p(2)\bigr).
\tag{1166.56}
$$
固定实际 abelian quotient 的两个 compatible lifts
之差在左边；其 rational difference 为零，故整差也为零。
这锁住原整根塔。任何 root-frame 改变仍按原 $d\rho$
作为同构携带，不声称所有选根的 cochain 字面相同。

**随后**才沿实际 source/log morphism pullback 到
含分歧的 $L$ 或本篇 $S_L$。
不能在一个已经包含 $\mu_p$ 的 $L$ 上未经核验地
使用 (1166.56)，也不能用单层模 $p$ 的类代替上述兼容塔。

改变 $\Phi U$ 时，使用原 embedding refinement 和
$p$-small mapping cylinder。
R1166 §§4–7 的 cone/product homotopies保留第一槽零，
并在 $\delta=0$ 为零。
它们给出的 transported 第二槽与 (1166.47)
具有相同 differential (1166.50)。
在 universal $(U,\delta)$ 上，两者之差是闭的 degree-zero
函数；在 $\delta=0$ 又为零，故它为零。
这给同一实际模型中的 (1166.47)，
不再添加一个随 $\Phi$ 改变的中央 Kummer class。

## 17. 同一个 log-preserving 提升下的三个坏分支

本节新增范围的前提必须明确：
使用原**共同** PD Frobenius，
且原 source parameter 具有已付的 log-monomial 形式。
不允许为每一个四线参数单独选择一个方便的提升。

### 17.1. 任意深的近零输入

设
$$
U=z^m V,\qquad m>0,\quad V\in D^\times,\qquad
\Phi U=U^p(1+p\alpha),\quad\alpha\in D .
\tag{1166.57}
$$
这里 $z$ 为原 log parameter，$U$ topologically nilpotent，
$1-U$ 因而为单位。对原
$D=S_L$ 和 $V\in\mathcal O_F[[z]]^\times$，
同一 $\psi z=z^p$ 自动给
$1+p\alpha=\psi V/V^p$。
这是一条 actual PD-ring 等式，不是 $L$ 上的 field Frobenius。

用 $\varepsilon=w\alpha$ 代入 (1166.52)，准确得到
$$
J=
 \sum_{n\ge2}\frac{p^{\,n-2}\alpha^n}{n}
       \sum_{r=1}^{n-1}
          \frac{(-1)^{\,n-r}w^r}{r(1-w)^r}.
\tag{1166.58}
$$
这里不再有 $w$ 或 $U$ 的负幂。
同一估值证明给整收敛和 §15.2 的全部有限精度；
没有浅退化的 $v_p(U)\le1/3$ 限制。

原 $L^\dagger_2(U)$ 也可直接由
$\sum_{p\nmid n}U^n/n^2$ 定义，
或用 (1166.51) 的同一有限算法。
$A=-p^{-1}\log(1+p\alpha)$ 和 $B_0$ 仍整。
因此 (1166.47)–(1166.50) 在 log differential complex
中继续成立；其中
$\mathrm d\log U=m\,d\log z+\mathrm d\log V$。

强模 $pD$ 读数是
$$
\boxed{\quad
\beta_\Phi(U)\equiv
 \frac{\ell_2(U)+\alpha\ell_1(U)-U^p\alpha^2/2}
      {1-U^p}\pmod{pD}.
\quad}
\tag{1166.59}
$$
它保留实际 nilpotents，不能把“近零”改成直接令 $U=0$。
源映射到原扭点时，仍按本篇 ambient PD comparison
保留 $g$-normal terms；不先约掉 $z^e-p$ 再做 Frobenius。

### 17.2. 近一和极点：保同一第二输入及二次修正

把 $U$ 与 $\Phi U=v$ **同时**作 $S:U\mapsto1-U$
或 $J:U\mapsto U^{-1}$。
原 R1155 的 exact Coleman/path identities
与 (1166.54) 给
$$
\begin{aligned}
A_S&=B,& B_S&=A,&
 \boxed{\beta_\Phi(1-U)&=AB-\beta_\Phi(U)},\\
A_J&=-A,& B_J&=B-A,&
 \boxed{\beta_\Phi(U^{-1})&=-\beta_\Phi(U)+A^2/2}.
\end{aligned}
\tag{1166.60}
$$
$-1$ 的 Kummer symbol 在这里为零；$p>37$ 使 $2$ 可逆。
这两式也可逐式由 (1166.50) 核：
$d(AB)$ 正好补交换两个 ordered cups 的差，
$d(A^2/2)$ 正好补同槽 cup。

若 $1-U$ 是 (1166.57) 的近零参数，第一式给原近一
primitive；若 $U^{-1}$ 是近零参数，第二式给极点 primitive。
保留 $AB$ 或 $A^2/2$ 后，所得第二槽仍整。
不能仅把 $\operatorname{Li}_2^\dagger$ 变号，
也不能只改变第一输入而保第二输入不动。

R1157 (1157.46)–(1157.53)、§12.6 与 R1155 (1155.78)
已付的原 CM formal source，先由实际 line/divisor 因子给共同 $z$
的准确整幂，再由首系数单位给每个参数及补数的 integral unit，
不是仅由一个 $L$-点的赋值推出形式整除性。这含全部 rank-one 和
rank-two 标签；固定 CM 整数提升及 $[1+\alpha]P(z)$ 保持原形式加法，
不在未付同伦时改成另一个仅在 $E[p]$ 上相同的提升。故在**该已付共同 source**上，
本节能为每个 primitive 给原整 PD 第二槽。
若更换 reference line、root branch 或 source refinement，
仍须使用原五项及 actual root/cochain comparison；
本节没有许可逐项更换 source。

## 18. 接回指定 filling 和最高中央槽的准确范围

现在对每个原四线 Steinberg term，
可以把 (1166.48) 或 (1166.58)–(1166.60) 的
actual integral representative 送进 R1156–R1159 的
同一有序上链程序，再用本篇的 actual ambient-to-coefficient
map。以下顺序仍须保留：

1. 在原同一兼容根系统中处理实际乘法关系和 $d\rho$；
   constant symbols 及 Norm 的交叉项不提前删除。
2. 使用实际 closed-point corestriction。
   第一层 CM tame 部分由 §§9–10 给逐 cochain 的明确 trace；
   两个 source 因子必须沿同一个 $\tau_\zeta$ 运输。
3. 对 coefficient 外积应用 (1166.25)–(1166.27)。
   若原 primitive 满足 $dh=-P_A$，目标仍是
   $T_{12}h-\mathcal H$；
   本节给了 $h$ 的 actual 输入，不把 $\mathcal H$ 改成零。
4. 最后才使用原 $e$-block、PD normal window 和
   强可除归一。$L^\dagger_2$、$J$ 的有限精度是
   §15.2 的整精度，不是任意 function-jet 截断。

新增结论是原 primitive 已有同一 integral syntomic
cochain 和明确的第二槽。
其与 Frobenius matrix 的中央槽通过 (1166.54) 联系，
完整 carry 与所有三个坏 log 分支均保留。
这仍不等于已完成全 27 项、原权和原最高
$\operatorname{Sym}^{12}$ projection 后的求和，
不宣原 $z_{12}$ 或全局减法组合为单位。

本节的 comparison 来源是已付的 R1155 原 whole path/root
规范、Tsuji §2 的 symbol/product 与小权比较，
以及本篇 §§3–7 的实际 refinement/cone/product 同伦。
积分公式、整尾、微分号和 (1166.54)–(1166.60)
均由正文逐式证明。无数学程序执行。

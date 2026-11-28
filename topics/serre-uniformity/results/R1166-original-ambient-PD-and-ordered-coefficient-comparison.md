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

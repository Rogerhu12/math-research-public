# R1159：原 correlation primitive 到完整 Hecke 平滑上链的实际比较

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；root。

**已证明以下连续上链身份。后继 R1160 已实际构造本篇末节的 B_n，解开最高矩的平滑；Frobenius 数值读取继续。**
本篇把 [R1158](R1158-original-weighted-Manin-pushout-and-correlation-torsor.md)
已经构造的真实 correlation torsor 接到原未平滑两个 moment。
所有 crossed projection-formula 修正、单矩的根相位和
restriction–corestriction 同伦都有明确式子。

令
$$
\mathcal M=\mathcal M_{1,1,\mathbb Q},\quad p>37,\qquad
A=\operatorname{Sym}^4\mathcal H(1),\quad
B=\operatorname{Sym}^8\mathcal H(1),\quad
Z=\operatorname{Sym}^{12}\mathcal H(2).
$$
$\Pi:A\otimes B\to Z$ 为原 $\Pi_0$，不改 symmetric-power 尺度。
固定同一个几何基点和原兼容根，将 $\mathcal M$ 的 fundamental group
记为 $G$；以下都是有限模 $p$ 系数的连续 inhomogeneous cochains。

选 R1157–1158 的合法辅助素数 $3<n<p$；$n=5$ 始终可用。
R1157 §10 已完整支付 $n=2$ 的原来源，本篇所有上链公式也适用于 $n=2$。
令 $H\subset G$ 为真实 cyclic-$n$ cover 的 stabilizer，$[G:H]=n+1$。
选定 quotient correspondence 的同一基点路径，
$\psi_C^{-1}$ 运输后的原两个 moment cocycles 记为
$$
a\in Z^1(G,A),\quad b\in Z^1(G,B),\qquad
a^C\in Z^1(H,A),\quad b^C\in Z^1(H,B).
$$
上标 $C$ 包含真实的 quotient pullback 和系数运输；
它不是先将所有同源曲线的 moment 认成原来的同一数。
同一选择下定义
$$
T_na=\operatorname{Cor}_H^G(a^C),\quad
T_nb=\operatorname{Cor}_H^G(b^C),\quad
T_n\Omega=\operatorname{Cor}_H^G\Pi(a^C\cup b^C),
\qquad \Omega=\Pi(a\cup b).
\tag{1159.1}
$$
不把 $T_n\Omega$ 写成 $(T_na)\cup(T_nb)$。

## 1. 两条 crossed projection formula 的实际一次同伦

取右陪集代表集合 $\mathcal T$，约定
$$
t g=h_{t,g}t_g,\qquad h_{t,g}\in H,\quad t_g\in\mathcal T.
$$
对任意 global cocycles $a,b$ 和 cover cocycles $c,d$，
写
$$
u_t=t^{-1}a(t),\quad v_t=t^{-1}b(t),\qquad
c_t(g)=t^{-1}c(h_{t,g}),\quad
d_t(g)=t^{-1}d(h_{t,g}).
$$
群作用与 tensor 的位置均按此约定。
特别
$$
c_t(gh)=c_t(g)+g\,c_{t_g}(h),\qquad
t^{-1}b(h_{t,g})=v_t+b(g)-g v_{t_g}.
\tag{1159.2}
$$

定义完整一次上链
$$
\boxed{\begin{aligned}
R_{c,b}(g)&=\sum_{t\in\mathcal T}c_t(g)\otimes g v_{t_g},\\
L_{a,d}(g)&=-\sum_{t\in\mathcal T}u_t\otimes d_t(g).
\end{aligned}}
\tag{1159.3}
$$
则在 $C^2(G,A\otimes B)$ 中准确有
$$
\boxed{\begin{aligned}
\operatorname{Cor}(c\cup\operatorname{res}b)
   &=(\operatorname{Cor}c)\cup b+dR_{c,b},\\
\operatorname{Cor}(\operatorname{res}a\cup d)
   &=a\cup(\operatorname{Cor}d)+dL_{a,d}.
\end{aligned}}
\tag{1159.4}
$$

为核准第一式的全部位置，左边在 $(g,h)$ 的值为
$$
\sum_t c_t(g)\otimes
 g\{v_{t_g}+b(h)-h v_{t_{gh}}\}.
$$
减去 $(\operatorname{Cor}c)(g)\otimes g b(h)$ 后，
恰剩
$\sum_t c_t(g)\otimes(gv_{t_g}-ghv_{t_{gh}})$。
用 (1159.2) 展开
$gR(h)-R(gh)+R(g)$，含 $c_{t_g}(h)$ 的两个和逐项抵消，
正好得到这个差。

第二式的差是
$$
\sum_t (u_t-g u_{t_g})\otimes g d_{t_g}(h).
$$
将 (1159.2) 用于 $d_t$，
$dL(g,h)$ 恰为此式，负号来自 (1159.3) 的定义。
所以两式保留的是**同一陪集内的乘积**，不是两个总 norm 的乘积。

记 $d_n=n+1$、$U_a=\sum_tu_t$、$V_b=\sum_tv_t$。
同样准确有
$$
\operatorname{Cor}\operatorname{res}a=d_na-dU_a,\qquad
\operatorname{Cor}\operatorname{res}b=d_nb-dV_b .
\tag{1159.5}
$$
原 R1156 的一次同伦为
$$
\boxed{
K_{a,b}(g)=
 -U_a\otimes b(g)+a(g)\otimes gV_b
 +\sum_tu_t\otimes(gv_{t_g}-v_t).
}
\tag{1159.6}
$$
它满足
$$
dK_{a,b}
=\operatorname{Cor}(\operatorname{res}a\cup\operatorname{res}b)
       -d_n(a\cup b).
\tag{1159.7}
$$
也可由第一条 (1159.4) 和 (1159.5) 重得此式：
得到的 $-U_a\cup b+R_{\operatorname{res}a,b}$
与 (1159.6) 仅差
$-d(\sum_tu_t\otimes v_t)$，故二次微分相同。
本篇固定使用 (1159.6)，不把两个一次 representative 混用。

## 2. 单 moment Hecke 本征式的全部实际根相位

对 $d=4,8$ 记原 moment cocycle 为 $a_d$，
相应的 cover cocycle 为 $a_d^C$。
令 $x_d$、$y_d$ 分别是 R1158 的实际
$X_{n,d}$、$X'_{n,C,d}$ representatives。
已付的两种原 theta 乘法关系及其兼容根给零次向量
$\rho_d,\rho'_d$，满足
$$
x_d=k_d(n)a_d+d\rho_d,\qquad
y_d=n a_d^C-n^{-d}\operatorname{res}a_d+d\rho'_d,
\qquad k_d(n)=n^2-n^{-d}.
\tag{1159.8}
$$
这些就是 R1158 (1158.23) 的实际根差。

另一个原 trace-fixed norm 是
$$
\prod_{C\subset E[n],\,|C|=n}\theta'_{n,C}(P)=\theta_n(P)
       \quad\text{于 }K_1\otimes\mathbb Z_{(p)}.
\tag{1159.9}
$$
它的 divisor 比较已在 R1138 (1138.12) 给出；
trace-fixed 规范将剩下的 base 常数消掉。
按同一个 $P^d$ 加权，再取真实 norm roots，
这给一个明确的零次相位 $\tau_d$，满足
$$
\operatorname{Cor}y_d-x_d=d\tau_d.
\tag{1159.10}
$$
具体地，$\tau_d$ 是所选各陪集 norm 的兼容根之积与
$\theta_n(P)$ 原根之比所给的 $\mu_p$ 相位，按 $P^d$ 求和；
原有限 $p$ 单位分母用对应幂映射的逆处理。
因此它是已指定乘法等式的根比，而非另假定一个本征 coboundary。
未分裂点和子群均按原有限 étale norm 执行。

令 $U_d=\sum_t t^{-1}a_d(t)$，并在零次向量上将 Cor
解释为 $\operatorname{Cor}\rho'_d=\sum_t t^{-1}\rho'_d$。
定义
$$
\boxed{
\eta_d=\frac1n\left(
 \tau_d+\rho_d-\operatorname{Cor}\rho'_d-n^{-d}U_d
\right).
}
\tag{1159.11}
$$
将 (1159.8)–(1159.10) 及 (1159.5) 全部代入，得到
$$
n\{T_na_d-(n+n^{-d})a_d\}
 +d\{n^{-d}U_d+\operatorname{Cor}\rho'_d-\rho_d-\tau_d\}=0.
$$
所以准确的一次上链本征式为
$$
\boxed{\qquad
T_na_d=(n+n^{-d})a_d+d\eta_d.
\qquad}
\tag{1159.12}
$$
这里只反除 $n$，没有反除 $n+1$ 或 $k_d(n)$，
也没有将未知的 $\eta_d$ 设零。
全部相位来自 (1159.8)–(1159.10) 的明确原根。

## 3. correlation 的完整二次上链展开

先将 R1158 的 correlation torsor 按其 (1158.24)
完整 gauge 到下列原 quotient representatives：
$$
(k_4(n)a,k_8(n)b),\qquad
(n a^C-n^{-4}\operatorname{res}a,\
 n b^C-n^{-8}\operatorname{res}b).
$$
把这个已经运输中央坐标的一次上链记为 $h_{\rm corr}$。
则
$$
dh_{\rm corr}=-\Omega_{\rm corr},
$$
其中
$$
\begin{aligned}
\Omega_{\rm corr}
={}&k_4(n)k_8(n)\Omega-n^2T_n\Omega\\
&+n^{-7}\Pi\operatorname{Cor}(a^C\cup\operatorname{res}b)
 +n^{-3}\Pi\operatorname{Cor}(\operatorname{res}a\cup b^C)\\
&-n^{-12}\Pi\operatorname{Cor}
       (\operatorname{res}a\cup\operatorname{res}b).
\end{aligned}
\tag{1159.13}
$$
同子群两槽没有拆开。指数 $-7,-3,-12$
分别来自 $n\cdot n^{-8}$、$n^{-4}\cdot n$ 和
$n^{-4}\cdot n^{-8}$，不能把它们合成两个总 trace。

在一次上链中定义
$$
\boxed{
\begin{aligned}
J_n={}&n^{-7}\Pi\{\eta_4\cup b+R_{a^C,b}\}\\
 &+n^{-3}\Pi\{-a\cup\eta_8+L_{a,b^C}\}
 -n^{-12}\Pi K_{a,b}.
\end{aligned}}
\tag{1159.14}
$$
零次与一次 cup 仍按 inhomogeneous 约定：
$(\eta_4\cup b)(g)=\eta_4\otimes b(g)$，
$(a\cup\eta_8)(g)=a(g)\otimes g\eta_8$。
尤其
$d(a\cup\eta_8)=-a\cup d\eta_8$，
所以第二行的负号是必需的。

由 (1159.4)、(1159.7)、(1159.12)，(1159.13) 准确成为
$$
\boxed{\qquad
\Omega_{\rm corr}=\mathcal V_n\Omega+dJ_n,\qquad
\mathcal V_n=(n^4+n^{-11})\,\mathrm{id}-n^2T_n .
\qquad}
\tag{1159.15}
$$
完整 scalar 核准为
$$
\begin{aligned}
&k_4(n)k_8(n)
+n^{-7}(n+n^{-4})
+n^{-3}(n+n^{-8})
-(n+1)n^{-12}\\
&\hspace{20mm}=n^4+n^{-11}.
\end{aligned}
$$
因此本篇得到一个真正的、已指定的一次 primitive：
$$
\boxed{\qquad
h_{\mathcal V_n}=h_{\rm corr}+J_n,\qquad
dh_{\mathcal V_n}=-\mathcal V_n\Omega.
\qquad}
\tag{1159.16}
$$
它由 R1158 的原四线 source、全部根比及显示的陪集和构成。
没有从 $H^2$ 等式直接选一个未知一次 cochain 来替代这些修正。

## 4. 准确的未平滑门

R1147 的几何计算给
$H^1(\mathcal M_{\overline{\mathbb Q}},Z)=L_1$，
且 $H^0$ 为零。原 degree-$12$ moment 的 Tate residue
$v_{12}=1/12$ 是单位，标定这条几何直线。
对同一实际 $12$-moment 使用单矩 norm，
$T_n$ 在该直线上为 $n+n^{-12}$。
Hochschild–Serre 的原 degree-two 识别遂给
$$
\mathcal V_n|_{H^2(\mathcal M,Z)}
=v_n,\qquad
v_n=n^4+n^{-11}-n^2(n+n^{-12})
=n^{-11}(n-1)(n^{14}-1).
\tag{1159.17}
$$
例如固定 $n=5$，$p>5^{14}-1$ 时 $v_n$ 确为单位。
另由 R1157 §10 的同一来源可取 $n=2$，此时
$v_2=3\cdot43\cdot127/2^{11}$，对 $p>37$ 仅在 $p=43,127$ 失去单位性。
这些都只是同一原 cohomology 的 scalar 结论。

由 (1159.16) **不能**直接把 $h_{\mathcal V_n}/v_n$
称作原 $\Omega$ 的 primitive：
其微分仍是 $-\mathcal V_n\Omega/v_n$。
所缺的准确一次输入是 $B_n\in C^1(G,Z)$，满足
$$
dB_n=(\mathcal V_n-v_n)\Omega.
\tag{1159.18}
$$
若从实际 Hecke 路径同伦或同源 norm source 取得这样的
$B_n$，则原 primitive 准确为
$$
h_0=\frac{h_{\mathcal V_n}+B_n}{v_n},
\qquad dh_0=-\Omega.
\tag{1159.19}
$$
式中加号由 (1159.18) 固定。
这里要求 $B_n$ 的实际构造，不能以其抽象存在性
或另一次 quasi-isomorphism 代替后继 Frobenius 读取。

全 $\mathcal M$ 上的原 $H^0(Z)=H^1(Z)=0$
保证完成该接口后能唯一识别规范 lift，
但不提供其 $F_0$ 中央值。特别本篇没有删除 SS specialization
时四线参数趋 $0,1,\infty$ 的项，也没有将单 primitive
的单位 jet 直接归给 weighted source。

## 来源与核验

- R1156：同根整 cochains、完整 Cor 约定及 (1159.6) 的原同伦。
- R1157–1158：真正 SV triangle、全 noncusp raw 延伸、
  指定 polynomial pushout、全部 quotient 相位及中央 gauge。
- R1138：原 theta divisor/norm、cyclic correlation 与 physical Hecke 方向。
- R1147：原 moment、degree-$12$ residue 及 universal cohomology。
- (1159.3)–(1159.19) 由 root 在相同右陪集约定下逐式纸推。
  无数学程序执行；未增添素数扫描。


### 后继 B_n 已实际构造

[R1160](R1160-original-explicit-arithmetic-descent-and-unsmoothing.md) 用本篇给定 ζ_n=(V_n−v_n)Ω 构造真实算术 B_n：两个有限阶 geometric lifts、复共轭的唯一标量及两个 transvection 的有限反差分给完整连续 section。因此 (1159.19) 现已实现，n2/n5 选择覆盖全部 p>37；一般 Frobenius 的第二条 conjugating-path 数值仍单独待付，不将这次下降写成已知 F0。


## 5. 实际 Norm reduction 给同源 Frobenius 的完整功能方程

本节把 §§1–3 的同根、crossed 比较改写为真实群及 torsor 图，
再读取唯一 Hodge frame 中的 Frobenius。
它得到原曲线与全部实际 $E/C$ 之间的功能方程，
不把 $\mathcal V_n$ 的作用替换成单点上的 scalar $v_n$。
尤其这里没有宣称已经求出 R1160 的 $B_n$ 的局部值。

### 5.1. 先保完整 product 群，再使用给定的 Norm 点

记原最高 quotient 群为
$$
G_0=(A\oplus B)\oplus Z,\qquad
(v,z)(v',z')=(v+v',z+z'+\Pi(v_4,v'_8)).
$$
令 $\mathscr P_0$ 是 R1147 的原 canonical 最高 torsor。
在真正 cyclic-$n$ cover 上拉回商曲线的同一对象，
并沿原 $\psi_C^{-1}$ 运输全部 coefficient，
得到 $G_C,\mathscr P_C$。
中心同样沿 $\operatorname{Sym}^{12}(\psi_C^{-1})$ 运输；
Tate $(2)$ 因子仍是原来的因子。

作真正的 product/Weil restriction
$$
G_{\rm big}=G_0\times\operatorname{Res}_C G_C,\qquad
\mathscr P_{\rm big}
 =\mathscr P_0\times\operatorname{Res}_C\mathscr P_C .
\tag{1159.20}
$$
其交换商写为
$V_{\rm big}=(v_0;(v_C)_C)$，中心是
$Z_{\rm big}=Z\oplus\operatorname{Res}_C Z$。
在一个分裂纤维中，后者有 $n+2$ 个原 $Z$ 槽。
不同 $C$ 的乘法仍在各自的槽内。

定义交换商的实际线性 map
$$
L(v_0;(v_C))=
 \left(
  \sum_Cv_{C,4}-(n+n^{-4})v_{0,4},\
  \sum_Cv_{C,8}-(n+n^{-8})v_{0,8}
 \right).
\tag{1159.21}
$$
在未分裂的底上，求和是相同实际有限 étale cover 的 trace。
$L$ 在 étale 局部满射：可只改变一个 $C$ 槽。
这里无需反除 $n+1$ 或任何 $k_d(n)$。

由 (1159.8)–(1159.12) 的原函数 Norm 和兼容根，
$L_*\mathscr P_{\rm big}^{\rm ab}$ 有一个**已给定的**
trivialization。若使用该节的 Galois cocycle 坐标，
其 coboundary 正由原 $\eta_4,\eta_8$ 表示。
本节使用这一实际 Norm 点，
不以“一个 $H^1$ 类为零”代替指定的 quotient 标识。

置
$$
H=\ker L,\qquad
G_H=\ker(G_{\rm big}\longrightarrow V_{\rm big}
                              \xrightarrow{L}A\oplus B).
\tag{1159.22}
$$
所以 $G_H$ 是 product 群中 $H$ 的**逆像**，
其中心仍为整个 $Z_{\rm big}$。
沿上述给定 Norm 点拉回 $\mathscr P_{\rm big}$，
得到一个实际 $G_H$-torsor $\mathscr P_H$。
没有先把任何中央槽商掉。

这些定义可在每个 $\mathbb Z/p^r$ 层作出。
所用 quotient Norm 点来自原兼容单位根，
各 map 只用 $n$ 的单位逆，
故约化相容。原 primitive/all-vector 的固定单位尺度
在两边相同，不改变 (1159.21)。
因此也有原 $p^\infty$ 对象及其实际 filtered realization；
这里不是仅由一个有限层的抽象同构猜一个 crystalline lift。

### 5.2. 在 $H$ 上是完整 ordered 双线性身份

记 $a=n^{-4}$、$b=n^{-8}$。定义到原 correlation 交换商的 map
$$
\begin{aligned}
\lambda(v)_d&=k_d(n)v_{0,d}\quad(d=4,8),\\
\lambda(v)'_{C,4}&=nv_{C,4}-av_{0,4},\\
\lambda(v)'_{C,8}&=nv_{C,8}-bv_{0,8},
\end{aligned}
\tag{1159.23}
$$
并定义中心 map
$$
\mu(z_0;(z_C))
 =(n^4+n^{-11})z_0-n^2\sum_Cz_C .
\tag{1159.24}
$$
保持 R1158 原
$b_{\rm corr}(x,x')=\Pi(x_4,x'_8)
-\sum_C\Pi(x_{C,4},x'_{C,8})$。

对两个独立输入 $v,v'\in H$，直接展开得
$$
\begin{aligned}
b_{\rm corr}(\lambda v,\lambda v')
={}&k_4(n)k_8(n)\Pi(v_{0,4},v'_{0,8})
     -n^2\sum_C\Pi(v_{C,4},v'_{C,8})\\
 &+nb\,\Pi\left(\sum_Cv_{C,4},v'_{0,8}\right)
  +na\,\Pi\left(v_{0,4},\sum_Cv'_{C,8}\right)\\
 &-(n+1)ab\,\Pi(v_{0,4},v'_{0,8}).
\end{aligned}
$$
分别对 $v$ 的第四次槽和 $v'$ 的第八次槽
使用 $H$ 的实际方程，首槽 scalar 为
$$
k_4(n)k_8(n)+nb(n+a)+na(n+b)-(n+1)ab
 =n^4+nab=n^4+n^{-11}.
$$
故
$$
\boxed{\quad
b_{\rm corr}(\lambda v,\lambda v')
 =\mu\bigl(b_{\rm big}(v,v')\bigr).
\quad}
\tag{1159.25}
$$
这保了两个不同输入及 ordered 槽的顺序，
不只是在 $\Lambda^2$ 或 $H^2$ 中的等式。

因而
$$
f:G_H\longrightarrow G_{\rm corr},\qquad
(v,z)\longmapsto(\lambda v,\mu z)
\tag{1159.26}
$$
是实际群同态，中央坐标没有额外的二次 $q(v)$。
不要求 $\lambda$ 满射；extension of structure group
仍按这个真实态射定义。

$f_*\mathscr P_H$ 的整个交换商通过 (1159.8) 的原根比较，
准确识别为 R1158 的指定 theta quotient。
所以它与已经构造的 $\mathscr P_{\rm corr}$
是同一 central extension 对同一个 quotient 的两个实际 lifts。
此时才在完整 $\mathcal M$ 上使用
$H^0(\mathcal M,Z_r)=H^1(\mathcal M,Z_r)=0$，
得到唯一的 quotient-preserving 同构
$$
f_*\mathscr P_H\simeq\mathscr P_{\rm corr}.
\tag{1159.27}
$$
各层同构由唯一性自动相容。
没有在单个 $E$、CM 点或一个 smaller open 上调用该消失。

(1159.27) 是 §§1–3 的另一种实际对象表达。
若改回指定 Galois cochain 坐标，其 Norm 点和 quotient
identifications 正产生 $\eta_d,\rho_d,\rho'_d$，
而 ordered transfer 产生 $R,L,K$ 及 $J_n$。
本节没有把这些上链设为零；
(1159.22)–(1159.27) 把它们放进了同一个实际群图。

### 5.3. 唯一 Hodge 点给真实 Frobenius 功能方程

在已有原 relative/pointwise comparison 的局部范围中，
写同一 Frobenius 形式为
$$
\Phi_{\mathscr P}=R(v,z)\Phi_{\rm coeff}.
$$
原 $V,Z$ 均满足 $\operatorname{Fil}^0=0$；
因此这些 torsors 的 Hodge 点唯一。
所有给定的 Norm 点、product、restriction、
群态射和 (1159.27) 都是同一 filtered realization 的 morphisms，
必须保持该点。

特别 product 的 Hodge 点落在 (1159.22) 的 reduction 中，
其 Frobenius 向量满足 $L(v)=0$。
将 (1159.26) 应用于这个**实际** Frobenius，
得到
$$
\boxed{\quad
Z_{\rm corr}(E)
 =(n^4+n^{-11})Z_0(E)
   -n^2\sum_{C\subset E[n]}
          \operatorname{Sym}^{12}(\psi_C^{-1})
                         Z_0(E/C).
\quad}
\tag{1159.28}
$$
右边商曲线的数值先在它自己的原 Hodge frame 读取，
再由显示的实际 coefficient map 运输。
若 Frobenius 重排子群或 coefficient field，
仍沿相同 finite étale correspondence 逐槽运输后求和。
不是先把每个 $Z_0(E/C)$ 当成 $Z_0(E)$。

本式也在 BCH 中央坐标成立。确实，由 (1159.25)，
$$
\mu\!\left(z-\tfrac12b_{\rm big}(v,v)\right)
 =\mu(z)-\tfrac12b_{\rm corr}(\lambda v,\lambda v).
$$
因此将 (1159.28) 中所有 $Z$ 同时换成
$Z^{\rm BCH}$，无需再补二次项。
R1166 §§20–21 与 R1168 已完成的 correlation 读取，
可直接作为该功能方程左边的值。

本式先由同一 $p^\infty$ filtered Frobenius 对象得到，
再在原整格上约模 $p$。
它没有把一个仅模 $p$ 的任意群同构当成无条件的
filtered Frobenius 同构。

### 5.4. 原二同源 coefficient map 的 exact 项与 shear

为使 (1159.28) 的方向可逐式核准，取
$C_i=\{O,(e_i,0)\}$，$K_i=3e_i^2+A$。
在同一短模型上使用标准微分归一的实际 Vélu 座标
$$
x'=x+\frac{K_i}{x-e_i},\qquad
y'=y\left(1-\frac{K_i}{(x-e_i)^2}\right),
\qquad \psi_i^*\omega_i=\omega .
\tag{1159.29}
$$
这些式子由二扭点加法与微分直接得到；
$x'$ 的 formal expansion 首项为 $v^{-2}$、常数为零，
故此处仍是归一短模型，未把 target 原点平移成另一个常数。

用 $y^2=(x-e_i)((x-e_i)^2+3e_i(x-e_i)+K_i)$，
直接微分给
$$
d\!\left(\frac y{x-e_i}\right)
 =\left(x-e_i-\frac{K_i}{x-e_i}\right)\omega .
$$
所以作为实际 meromorphic forms，
$$
\boxed{\quad
\psi_i^*\eta_i
 =2\eta-e_i\omega-d\!\left(\frac y{x-e_i}\right).
\quad}
\tag{1159.30}
$$
不能把 $\psi_i^*\eta_i$ 简写成 $2\eta$。

原 pointed Weil/Pic 识别的 pullback 是 dual isogeny：
R1164 (1164.20)–(1164.21) 给
$\psi_i^*K(P')=K(\widehat\psi_iP')$。
因此本篇要求的 $\psi_i^{-1}$ 在相同 de Rham
coefficient 上对应 $\frac12\psi_i^*$，而不是裸 pullback。
在 cohomology 中它的确切矩阵为
$$
\boxed{\quad
\omega_i\longmapsto\frac12\omega,\qquad
\eta_i\longmapsto\eta-\frac{e_i}{2}\omega .
\quad}
\tag{1159.31}
$$
对 $d=4,8,12$ 应取该**整个**矩阵的 symmetric power；
尤其 $\eta_i$ 的 shear 不能因最后求 trace 而提前删去。

若仍在 Čech/PD cochains 上计算，(1159.30) 的 exact 项
及 R1164 的实际 root-leading factor 同样保留，
然后使用 R1165–1166 的真实 residue/refinement map。
本节只在经过该已付比较的 Hodge–Frobenius coefficient
层使用 (1159.31)。
因 isogeny 是实际 horizontal/Frobenius morphism，
其半线性 Frobenius 比较也含相同矩阵的 $\sigma$；
没有把 target 与 source 的两组输入基直接等同。

### 5.5. 本节完成的归一与尚未读取的量

(1159.28) 给的是原 $\mathcal V_n$ 对同一中央 Frobenius
函数的真实作用。原 $k_4(n),k_8(n)$、两次 cross 和
$n^{-4},n^{-8},n^2$ 的方向均由实际群图支付。
左边的 raw correlation 读数与右边的原 moment 对象之间，
不再留一份未指明的 quotient normalization。

但它仍是跨 $E$ 及全部 $E/C$ 的功能方程。
(1159.17) 的 $v_n$ 是原绝对 $H^2$ 上的 scalar，
不能从这里将整个右边改成 $v_nZ_0(E)$。
R1160 的 $B_n$ 对应的正是另一份
$\mathcal V_n-v_n$ 上链同伦；它的实际局部读取
没有因 (1159.28) 自动给出。
本节不宣单点原 $F_0$ 已知、不宣其最高中央值为单位，
也没有把 $\Pi_2,\Pi_4$ 或 $\lambda$ 槽一起消去。

群的 ordered 恒等式、kernel 逆像及给定 Norm 点的用途，
已由 o2_high_coefficient 独立纸核。
二同源 (1159.30)–(1159.31) 由原短模型与
pointed Pic/Weil 方向逐式证明。无数学程序执行。

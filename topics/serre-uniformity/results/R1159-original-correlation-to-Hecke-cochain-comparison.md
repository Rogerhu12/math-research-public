# R1159：原 correlation primitive 到完整 Hecke 平滑上链的实际比较

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；root。

**已证明以下连续上链身份，尚未将平滑算子在上链层逆掉。**
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

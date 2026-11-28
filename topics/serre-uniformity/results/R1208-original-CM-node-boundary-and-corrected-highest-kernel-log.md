# R1208：原 CM 节点边界与最高 packet 核的完整首对数更正

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root / o2_high_coefficient。

**已证明。** 在原 $p\equiv11\pmod{12}$ 的最高整 packet、同一个 $P=(p-1)D_0$ 和同一个 CM 轮廓核 $T_*=(b^3-1)^{2g-1}$ 上，完整首对数为
$$
\boxed{\quad
\mathcal V_m(T_*)=
-\frac{8\,2^m\nu}{\binom m{2g-1}^{\,2}}\in k^\times,
\qquad m=(p-1)/2 .
\quad}
\tag{1208.1}
$$
这里 $\nu$ 是 R1200 由同一个 canonical Igusa–Weil character 锁定的原单位。

本篇**更正** R1199 §6 将三个支持 CM 支分别删除的论证，以及由此接到 R1200/R1201 的完整 $\mathcal V_m$ 数值。旧的 generic normal、有限收缩、canonical 相位和 R1201 的全部 SS 求积保持成立；旧数值准确是 SS 部分。遗漏处是中心 frame 在 ordinary 开集上模 $I$ 相容，并不保证它在整个 CM node 上与同一个全局模 $I$ 平凡化相容。这个差不是任意未知量：本篇从原 $e_D/e_I$ 过渡求出其静态单位，保留全部节点接口后精确计算。

新的完整值仍为单位，但不是原 SS 数值。它仍是整 packet 在 $T_*$ 上的值；不将它直接送到指定 $C$，也不证明 $\mathcal V_m|_{\ker\mathfrak c}$ 非零。R1202–1207 的独立整投影、返回、实际纯型秩和 CM 截面结论不受这项更正影响。

## 1. 全部原对象及固定符号

保持
$$
p=12g-1>37,\quad n=2g-1,\quad
m=3n+2=(p-1)/2,\quad e_0=m(p+1),\quad
\pi_0^{e_0}=p,\quad \varepsilon=\pi_0^m .
\tag{1208.2}
$$
$n,m$ 都为奇数。原点差及整角不变：
$$
D_0=2[c_1]-[c_\zeta]-[c_{\zeta^2}],\quad
P=(p-1)D_0,\quad
E_m=(e_{\tau_m}+e_{\mathrm{PS}_{m-1}})e_N .
$$
以下用 $\xi^3=1$ 标记 Igusa 的 $b=\xi$ 支。原 rational coarse 参数为 $a=b^p$，故该支对应原 $c_{\xi^p}$；因后两点的系数相同，仍可写
$$
a_1=2,\qquad a_\zeta=a_{\zeta^2}=-1 .
\tag{1208.3}
$$

记
$$
r=1-b^3,\quad h=r^{n+1}A(b),\quad
A(b)=bQ(b^3),\quad
T_*=(b^3-1)^n=-r^n .
$$
R1193–1197 给实际整 Hodge 提升 $\Omega_*$，其权为 $m^2$、natural deck 角色为 $\zeta^2$，并被 $E_m$ 固定；其首中心层为
$$
\overline{\pi_0^{-1}\Omega_*}|_I
=\frac{T_*\,db}{uA(b)},\qquad u^m=h .
\tag{1208.4}
$$
完整首对数仍按 R1196 的同一 Čech 方向定义：
$$
\mathcal V_m(T_*)=
\overline{\pi_0^{-m^2}
 \langle E_m\log P,\Omega_*\rangle}.
\tag{1208.5}
$$
并没有换成一个局部 meromorphic pairing 来重新定义它。

置
$$
L=(m-1)/2,\quad c_m=(-1)^L\binom{m-1}{L},
\quad Q_0=Q(0)=\binom mn,\quad
\nu=(-3)^L(2\gamma)^{m-1}.
\tag{1208.6}
$$
$\gamma$ 是 R1200 保持原 $\zeta_p,\varpi$ 的 Weil 首项单位，$\gamma^{p-1}=-1$。故 $c_m,Q_0,\nu$ 均非零，且本文所需平方组合在 $\mathbf F_p$ 中。原 Jacobi 反射给 $Q(1)=-Q_0$，所以 $A(1)^2=Q_0^2$。

## 2. 旧 frame 推理中必须补的接口

原零多度线丛由 R1014/R1018 的真实 vertical twister 给出。中心主化函数是
$$
G(b)^2,\qquad G(b)=\frac{(b-1)^2}{b^2+b+1},
$$
支持尾的主化函数是 $x_D^{m a_\xi}$。在 ordinary centre 上，实际 frame $G(b_{\rm lift})^{-2}$ 与全局模 $I$ 平凡化相容，$I=(\pi_0^m)$；但这只控制该普通开集。

在 node 的 tail branch 上，二者还可能相差一个以 $z_D$ 为变量、模 $\pi_0$ 非恒定的单位。该单位在 centre branch 上虽为一，代入 $z_Dw=\rho_\xi\pi_0^3$ 后却产生正 normal 项。因此，affine 的 $H^1(IO)=0$ 只能提升**已经相容的**模 $I$ frame，不能将任意非 $1+I$ 的 tail-branch 单位直接消去。

本篇保留这个单位，并始终使用两个实际接口的总 Čech residue。没有把“node 上可逆”替成“对完整配对没有贡献”。

## 3. 同一非约化 CM 尾及顶层微分

在原支持尾写
$$
D_\xi:\ y_D^2=x_D(x_D^{2g}+A_\xi^{\rm tail}),\qquad
Q_\xi=(0,0),
$$
以及 R1197 的同一个 full 分支
$$
U^2=V^{p+1}+A_\xi^{\rm tail},\quad
x_D=V^6,\quad y_D=UV^3,\quad z_D=V^{-3}.
\tag{1208.7}
$$
R1207 已在整个 $\mathcal O/(p)$ 上证明实际 CM 截面为 $V=0$、$U=\pm\sqrt{A_\xi^{\rm tail}}$。所以这里的尾主化 $x_D^{m a_\xi}$ 对同一个 horizontal divisor 有效，包含全部所需 nilpotents。将它提升为实际 affine frame时的差为 $1+p$ 乘 affine 整函数；后文给出这些差不贡献本层的估值。

R1197 的完整旗标证明所有支持尾层 $<m^2$ 为零。下一个允许层就是 $m^2$。为计算它，将同一有限角论证延到 $k=n+1=2g$。

此时微分系数模为
$$
M=\operatorname{Sym}^{(m+1)(p-1)-2}(k^2)\otimes\det^{1-m}
 =\operatorname{Sym}^{m(p+1)-2}(k^2)\otimes\det^{1-m}.
\tag{1208.8}
$$
Dickson 过滤的 $0\le j\le m-2$ 非终端因子与 R1197 相同，只有 $j=0$ 的 $W_{m-1}$ 被 $E_m$ 看见。最后 $j=m-1$ 的余次数为 $p-1$、determinant twist 为零，是 $\mathrm{St}$；$N$ 在 $\mathbf P^1(\mathbf F_p)$ 上传递，且 $p+1$ 可逆，所以 $\mathrm{St}^N=0$。因此
$$
\dim\overline E_m M=1 .
\tag{1208.9}
$$

置
$$
F=UV^{m-2},\qquad
\Theta V=2U,\quad \Theta U=V^p,\quad dF=(\Theta F)\eta,
$$
$$
H=\frac{\Theta^{m-2}F}{-(m+1)!/6},\qquad
d=(n+1)(m-1).
\tag{1208.10}
$$
同一原 $c^{1-m}$ determinant 运输在全部 Weil 分支上保留。$H$ 在无穷的最高项是 $z_D^{-d}$；$d=-1/4$ 于 $k$，为单位。故 $dH$ 非零，生成 (1208.9) 的完整微分像。

在真实 node $z_Dw=\rho_\xi\pi_0^3$ 中，中心的首 normal 为一。一个中心 Laurent 项 $\pi_0^t w^j\,dw$，$t\ge1$，在尾 normal $N=t+3(j+1)$ 的极阶为 $j+2$，因而不超过
$$
\frac{N-1}{3}+1 .
\tag{1208.11}
$$
已有 polar 部分送回尾上只给低极或 regular 项。真实 node 单位的重参数保持这个 normal–pole 滤过。它控制全部层，不只最高齐次项。对 $N=m^2$，上界就是 $d+1$。同 R1197 的 polynomial representative、framing 与全分支齐次化，整个实际当前层因此是 $dH$ 的倍数。

因 $T_*$ 在 $b=\xi$ 恰有 $n$ 阶零，前层全零，原 node 最高系数准确给
$$
\overline{\pi_0^{-m^2}\Omega_*}|_{D_\xi}
=\gamma_\xi\,dH,
$$
$$
\gamma_\xi=
\frac{m(3\xi^2)^n\kappa_\xi^{\,n+1}\rho_\xi^{\,d}}
 {\lambda_\xi A(\xi)d}.
\tag{1208.12}
$$
此式使用 $b-\xi=\kappa_\xi w^m+\cdots$、$u=\lambda_\xi w^{n+1}+\cdots$，没有将其单位设成一。

## 4. 原 Čech 方向给出的静态单位

沿 R1018/R1196 固定的方向，过渡读的是 $e_D/e_I$。在支持尾 affine 开上，twister 的系数可用底参数的幂表示；沿正则化链将全部过渡相乘，原 flux $2ma_\xi$ 和厚度三给
$$
\frac{e_D}{e_I}
=\text{底域常数}\cdot
 \pi_0^{-6ma_\xi}
 \frac{G(b_{\rm lift})^2}{x_D^{ma_\xi}} .
\tag{1208.13}
$$
这是同一个零多度线丛的两个实际 meromorphic frames，不另选一个线丛。中间有理链的 frames 逐项相消。底域常数的 log 乘节点 residue 为零，故不影响配对；原 compact-type 树没有残留图环流。

在原 full-$p$ affine 图，R1021 给同一 quotient-isogeny 的 target eigenparameter
$$
u'=\varepsilon(c_\xi\psi+pR),\qquad
\psi=\beta_Q^{p-1},\quad c_\xi\in W^\times,
\tag{1208.14}
$$
$R$ 在该 affine 图整。原 CM coarse 坐标与实际 target 参数满足
$$
b_{\rm lift}-\xi=(u')^3\,B_\xi((u')^3),\qquad
B_\xi(0)\in W^\times .
$$
有效 $\mu_3$ 来自同一六层支，零点是原 CM 提升。因 $G^2$ 在 $b=\xi$ 的阶为 $2a_\xi$，从 (1208.13) 得
$$
\frac{e_D}{e_I}
=\text{底域常数}\cdot
 \frac{\psi^{6a_\xi}}{x_D^{ma_\xi}}
 \cdot(1+(u')^3W[[ (u')^3 ]])
 \cdot(1+pR_1),
\tag{1208.15}
$$
其中在所用原 affine 图上 $R_1$ 整；必要时先局部化 $\psi$。实际上在 full 分支 $C\ne0$ 上 $\beta_Q\ne0$，所以这次局部化不引入新的 affine 极点。

R1018 §5、式 (1018.19) 对同一个 trace-zero $Q$ 已给合法 node 截断
$$
\psi^3=z_D^{-m}
 (1+A_\xi^{\rm tail}z_D^{4g})^{-3/2}
 +O\!\left(z_D^{-m+2gp}\right).
\tag{1208.16}
$$
于是所需静态 jet 正是
$$
\frac{\psi^{6a_\xi}}{x_D^{ma_\xi}}
=(1+A_\xi^{\rm tail}z_D^{4g})^{-3a_\xi}
 \pmod{z_D^{2gp}} .
$$
特别，原加法方向锁定为
$$
\boxed{\quad
J_{0,\xi}(z_D)=-3a_\xi
 \log(1+A_\xi^{\rm tail}z_D^{4g}).
\quad}
\tag{1208.17}
$$
它以正号进入原 $\operatorname{Res}\log(e_D/e_I)\Omega_*$。没有从期望的最终数值反选符号，也没有将 $e_I/e_D$ 与原约定混用。

## 5. 在原有限 Picard 复形中修正 node frame

直接使用 R1196 的有限环
$$
A_M=R/(\pi_0^{m^2+1}),\qquad I=(\pi_0^m).
$$
无需先在整个 node 上定义一个非 $1+I$ 对数。

先取 (1208.15) 的完整静态 tail-branch 单位，而不只取 (1208.17) 的有限近似。它在原 node 的模 $p$ 完成环中记为 $\bar\sigma_\xi(z_D)$。它确为该粗 node 上的单位：所选 $\psi$ 随原 ordinary line 运输，node 稳定子及辅助 $\mu_3$ 在指数 $6a_\xi$ 后作用平凡。其首项为一，且
$$
\bar\sigma_\xi(z_D)
=(1+A_\xi^{\rm tail}z_D^{4g})^{-3a_\xi}
  +O(z_D^{2gp}).
\tag{1208.17a}
$$
将全部系数提升到 $W(k)$，得到真实 formal node 单位
$\sigma_\xi(z_D)$。这只为换 frame；不把它冒称尾 affine 上的全局单位。不同整提升的差是 $1+p$ 乘 node 整函数，并按真实 Čech $0$-coboundary 处理。

设原 node frame $e_N$ 是 centre 的 $G(b_{\rm lift})^{-2}$ frame 的实际延伸，包含原 twister。原 centre–node transition 等于一，而 tail–node transition 是 (1208.13)。改取
$$
e_N'=\sigma_\xi e_N .
$$
由 (1208.15) 及完整静态单位的定义，tail–node transition 变为
$$
e_D/e_N'\in1+I:
$$
非静态项从 $u'^3$ 的 $\pi_0^{3m}$ 阶开始，另外只有 affine 的 $p$ 误差。在这个 overlap 中按 tail normal 读取，不因 $z_D$ 的 Laurent 极点反除 $\pi_0$。

与此同时，centre–node transition 准确变为
$$
e_N'/e_I=\sigma_\xi .
\tag{1208.17b}
$$
在 centre overlap 上 $w$ 可逆，$z_D=\rho_\xi\pi_0^3/w$，所以
$$
\sigma_\xi-1\in(\pi_0^{12g})=(\pi_0^{p+1})\subset I .
$$
因此两个 overlap 现在都是诚实的 $1+I$ 过渡，与同一个全局模 $I$ 平凡化相容。原先遗漏的项正是 (1208.17b)，不能只保留已被修正的 tail–node 接口。

由 $\Omega_*|_{D_\xi}\in\pi_0^{m^2}\Omega^1$，新 tail–node 上的
$\ell_I(e_D/e_N')\Omega_*$ 至少在 $\pi_0^{m^2+m}$，不贡献本层。centre–node 上则必须保留 $\ell_I(\sigma_\xi)$。其所需有限 jet 由 (1208.17a) 给出，准确是 (1208.17)。将同一个实际 node 的 Laurent residue 写在尾变量中，正得到
$$
+\operatorname{Res}_{\infty_\xi}J_{0,\xi}\Omega_* .
$$
加号来自 (1208.17b) 的 $e_N'/e_I$；它与 R1018/R1196 的 $e_D/e_I$ 方向相同。反向换 frame 会同时反转两个接口，给相同总和。

这个构造没有要求 $\sigma_\xi$ 在整条 affine 尾上可逆，也不使用 affine $H^1(IO)=0$ 来修正一个非 $I$ 差。真实两接口的变化就是同一个乘法 Čech $0$-coboundary；在各自已经属于 $1+I$ 的 overlap 上，有限 $\ell_I$ 与乘法、pullback、原有限 flat trace 相容。底域常数由 node residue 为零杀掉，正则化有理链的 frames 逐项相消。

从 (1208.17a) 开始的误差在 centre overlap 至少有
$\pi_0^{6gp}$，严格大于本篇 $m^2$ 的精度；因此不影响此有限构造的读取。下节再给一个全 normal 的独立估值，排除将这次有限读取误写成带隐藏 $p$ 分母的无限 log。

## 6. 所有高对数分母与 node 极部的统一排除

记 $a=m^2$。本节排除高层可能因 $p$ 分母返回到 $\pi_0^a$ 的问题。

### 6.1 静态 log

静态第 $j$ 项为常数乘 $z_D^{4gj}/j$。若它与 $\Omega_*$ 的 $\pi_0^N$ 层有 residue，(1208.11) 迫
$$
N\ge1+3\cdot4gj=1+(p+1)j .
$$
故该项的最终 normal 至少为
$$
1+(p+1)\bigl(j-mv_p(j)\bigr).
\tag{1208.18}
$$
若 $v_p(j)=s\ge1$，则
$j-ms\ge p^s-ms\ge p-m=m+1$，从而 (1208.18) 严格大于 $m^2$。这个证明保留了可能的 $N\ge e_0$ 层，不只是对模 $p$ 微分作形式截断。

若 $p\nmid j$，则没有分母回返；$N>m^2$ 的层亦不贡献。由于全部 $N<m^2$ 的 CM 层为零，唯一可能是
$$
N=m^2,\qquad
1\le j\le\frac{m^2-1}{p+1}=\frac{m-1}{2}=L<p .
\tag{1208.19}
$$
所以 (1208.17) 只需读取 $j\le L$，所有分母均为单位。其所需 $z_D$ 次数不超过
$4gL=d$；而 (1208.16) 的误差从 $2gp>d$ 开始，严格不能进入 residue。

### 6.2 CM analytic 因子及 affine 的 $p$ 误差

(1208.15) 的 analytic 因子是 $u'^3$ 的整单位。其第 $j$ 个 log 项的 normal 至少为
$$
3mj-e_0v_p(j)
=m\bigl(3j-(p+1)v_p(j)\bigr)>0
\qquad(j\ge1).
\tag{1208.20}
$$
不等式在 $v_p(j)=0$ 时显然，在 $v_p(j)=s\ge1$ 时由
$j\ge p^s$ 得到。$\Omega_*$ 在每个支持 affine 尾上的 normal 至少是 $a$，故这些项全超过目标层。

同理，$1+pR_1$ 的第 $j$ 个 log 项至少含
$\pi_0^{e_0(j-v_p(j))}$，仍是严格正 normal。$R_1$ 的 node Laurent 展开可以有极点，但其系数是在原 tail normal 图中整的；取 residue不会反除 $\pi_0$，不能把 centre 坐标的负幂误当成 tail 系数里的负 normal。实际 affine frame 的 $1+p$ 改变由相同估值处理。

对于真实 node 单位重参数，使用 (1208.11) 的 normal–pole 滤过；只在被 (1208.19) 允许的单位分母有限窗内，才采用 R1021/R1018 给出的准确模 $p$ 坐标。这样既保留整模型来源，也排除了所有可能的高 $p$ 分母返回。

由此，支持支的完整首层准确为
$$
\boxed{\quad
\mathcal V_{{\rm CM},\xi}(T_*)
=\gamma_\xi\operatorname{Res}_{\infty_\xi}
       J_{0,\xi}\,dH .
\quad}
\tag{1208.21}
$$

## 7. 顶层 primitive 的两个实际值

暂写 $A=A_\xi^{\rm tail}$。函数 $H$ 属于
$k[V^{p+1}]=k[x_D^{2g}]$，作为后者变量的次数为 $L$。这可直接从
$F=UV^{m-2}$、$m-2=2L-1$ 及 $\Theta$ 的作用看出；每一项的 $V$ 次数相差 $p+1$。

在 $Q$，$U=\sqrt A+O(V^{p+1})$。求 $m-2<p$ 次导数时可用
$\Theta=2\sqrt A\,\partial_V$，所以
$$
\Theta^{m-2}F(Q)=2^{m-2}(m-2)!\,A^L .
$$
因 $(m+1)m(m-1)=3/8$ 于 $k$，(1208.10) 给
$$
\boxed{\quad H(Q)=-4\,2^m A^L.\quad}
\tag{1208.22}
$$

令 $R$ 是任一 $y_D=0,\ x_D^{2g}=-A$ 的点。取其 full 提升 $U=0,V=V_R$。在所需 $<p$ jet 中，
$$
V(U)=V_R(1-U^2/A)+O(U^{2p}),\qquad
\Theta=V_R^p\partial_U+O(U^{2p})\partial_U .
$$
因此只需抽取
$U V_R^{m-2}(1-U^2/A)^{m-2}$ 的 $U^{m-2}$ 项。用
$$
\binom{m-2}{L-1}
=\frac12\binom{m-1}{L}
$$
并代入原 $a_{m-2}=-(m+1)!/6$，得
$$
\boxed{\quad H(R)=-8c_m A^L.\quad}
\tag{1208.23}
$$
全部这 $n+1=2g$ 个 $R$ 的值相同。顶层 $H$ 的无穷 Laurent 常数是 $H(Q)$，不应说该常数为零；本篇只用其实际差，减任何共同常数都不改变以下 residue。

## 8. 静态 residue 的完整求值

令 $B_D=x_D^{2g}$，则
$$
J_{0,\xi}=-3a_\xi\log(1+A/B_D).
$$
$B_D$ 在 $Q$ 的阶为 $4g=2(n+1)$；$B_D+A$ 在每个上述 $R$ 的阶为二。除这些点和无穷外没有零极。分部积分及全局 residue 定理给
$$
\operatorname{Res}_\infty J_{0,\xi}\,dH
=-\operatorname{Res}_\infty H\,dJ_{0,\xi}
=6(n+1)a_\xi\bigl(H(Q)-H(R)\bigr).
$$
代入 (1208.22)–(1208.23) 及 $n+1=1/6$ 于 $k$，
$$
\boxed{\quad
\operatorname{Res}_\infty J_{0,\xi}\,dH
=4a_\xi(2c_m-2^m)(A_\xi^{\rm tail})^L .
\quad}
\tag{1208.24}
$$
这是在原粗尾上求的 residue，不额外乘除 full 分支的六次分歧指数。前面的 full 坐标只用于计算同一个下降函数 $H$。

## 9. 在 good CM 模型上锁原 canonical 相位

这一节直接使用平滑 good 模型，不能把 R1200 的 generic $2rh'$ 公式代到 $r=0$。

作忠实 tame 基变 $q^6=r$，置 $v=q^2$，原模型经 $x=q^2X,y=q^3Y$ 成为
$$
E^{\rm good}:Y^2=X^3+3bvX+(1-2b^3),\qquad
\omega_b=q^{-1}\omega_{\rm good},\quad
\eta_b=q\eta_{\rm good}.
$$
同一个 canonical Cartier–Weil character 给
$$
h_{\rm good}=q^{-(p-1)}h_b=vA(b),\qquad
u_{\rm good}=u_b/v .
\tag{1208.25}
$$
这里没有重选 Hasse 根。

在 $v=0,b=\xi$，$E^{\rm good}$ 是 $Y^2=X^3-1$，且 $db/dv=0$。对
$Y^2=X^3+a_GX+b_G$，在 $a_G=0$ 由
$d(X^2/Y)=(X^4+4b_GX)dX/(2Y^3)$ 直接得
$\nabla_{\partial a_G}\omega=\eta/(6b_G)$。因此
$$
\nabla_{\partial v}\omega_{\rm good}
=-\frac{\xi}{2}\eta_{\rm good}.
$$
同 R1200 的实际 Frobenius/Poincaré 归一，Hasse 导数除以该连接系数给
$$
B_{\rm good}=-\frac{2A(\xi)}{\xi}=-2A(1).
\tag{1208.26}
$$

在同一个 good full-$p$ 坐标中，
$W=\pi_0V=y_{\rm good}^2+3x_{\rm good}^2$，普通 centre 上 $x_{\rm good}=0$。原 Poincaré 一阶 character 给
$u_{\rm good}=B_{\rm good}^2W+\cdots$。
由 $u_{\rm good}^m=vA(b)$，继而
$$
u_b=\frac{B_{\rm good}^{p+1}}{A(\xi)}W^{m+1}+\cdots .
$$
原 $z_D=V^{-3}$ 及 $z_Dw=\rho_\xi\pi_0^3$ 给 $w=\rho_\xi W^3$。由于 $m+1=3(n+1)$，
$$
\tau_{{\rm CM},\xi}:=\lambda_\xi\rho_\xi^{n+1}
=\frac{B_{\rm good}^{p+1}}{A(\xi)} .
\tag{1208.27}
$$
同一个 $\zeta_p,\varpi$ 和 R1200 的 Weil 两槽比较还给
$$
A_\xi^{\rm tail}=-\frac{3\gamma^2}{B_{\rm good}^{2p}} .
$$
所以
$$
\boxed{\quad
\tau_{{\rm CM},\xi}^{m-1}(A_\xi^{\rm tail})^L
=(-3)^L\gamma^{m-1}
 \left(\frac{B_{\rm good}}{A(\xi)}\right)^{m-1}
=\nu\,\xi^{-1}.
\quad}
\tag{1208.28}
$$
使用的是 $A(\xi)=\xi A(1)$ 和 $m-1\equiv1\pmod3$。

若 Cartan eigenvariables 先以其它允许单位表示，(1208.28) 仍不变：$V\mapsto tV$ 使 $A^{\rm tail}\mapsto t^{p+1}A^{\rm tail}$、$\tau_{\rm CM}\mapsto t^{-(m+1)}\tau_{\rm CM}$，组合指数为零。交换两个 eigenline 亦不改变该平方组合。

最后，从
$$
\lambda_\xi^m=(-3\xi^2\kappa_\xi)^{n+1}A(\xi)
$$
化简 (1208.12) 时必须保留 $A(\xi)^2$：
$$
\gamma_\xi=
\frac{m\tau_{{\rm CM},\xi}^{m-1}}
 {3\xi^2dA(\xi)^2},\qquad
\boxed{\quad
\gamma_\xi(A_\xi^{\rm tail})^L
=\frac{m\nu\xi}{3dA(1)^2}.
\quad}
\tag{1208.29}
$$
丢掉这个平方不但改错常数，也破坏原 natural deck 角色。

## 10. 原完整首列

将 (1208.24)、(1208.29) 代入 (1208.21)，并保留三个实际 divisor 系数。因为
$$
\sum_{\xi^3=1}a_\xi\xi=2-\zeta-\zeta^2=3,\qquad
d=-1/4,\quad m=-1/2\quad\text{于 }k,
$$
得到
$$
\boxed{\quad
\sum_{\xi^3=1}\mathcal V_{{\rm CM},\xi}(T_*)
=\frac{8(2c_m-2^m)\nu}{A(1)^2}.
\quad}
\tag{1208.30}
$$

R1201 已从同一原 generic contraction 证明、且本篇不改其证明的值为
$$
\sum_{s\in S}\mathcal B_s(T_*)
=\frac{32m c_m\nu}{Q_0^2}
=-\frac{16c_m\nu}{Q_0^2}.
\tag{1208.31}
$$
这里明确只称 SS 部分。由于 $A(1)^2=Q_0^2$，把全部支持、无支撑和节点项相加，准确得
$$
-\frac{16c_m\nu}{Q_0^2}
+\frac{8(2c_m-2^m)\nu}{Q_0^2}
=-\frac{8\,2^m\nu}{Q_0^2}.
$$
这证明 (1208.1)。所有分母均是已显示的 $p$ 单位；没有使用数值扫描或假定一个 Bernoulli/Cartier 系数非零。

## 11. 一般 PS 返回的同源周期恒等式

为继续同一个 $\mathcal V_m|_{\ker\mathfrak c}$，保留已纸核但不扩大范围的实际简化。

R1204/R1206 的返回算子为
$$
\mathscr DT=rT''-4b^2T'-\frac94bT,\qquad
T=b^2P(b^3),\quad\deg P\le n-1 .
$$
在一个普通 SS 点 $s$，用 R1198 的同一有限周期
$v=f_1/f_0$、$f_1=h/h'_s$、$v'=r_s/(rf_0^2)$。置
$$
Z(v)=\frac{r(b)^{n+1}T(b)}{f_0(b)},\qquad b=s+J_s(v).
$$
原 Hasse/Picard–Fuchs 方程逐式给
$$
\mathscr DT=r^{-n}f_0(v')^2 Z'' .
\tag{1208.32}
$$
所以同一个 R1199 周期输入满足
$$
\boxed{\quad
E_{\mathscr DT}(v)=r_s
  \left(\frac{vT(s+J_s(v))}{A(s+J_s(v))}\right)'',
\quad}
\tag{1208.33}
$$
其中右侧 $vT/A$ 的可去奇点按实际 $A'_s$ 消去。确切地，
$\widetilde E_{\mathscr DT}=r_s^2Z''$，
而 $Z=h'_s\,vT/A$；全部 $r_s,h'_s$ 因子均保留。

若 $N=m-a$，原收缩权还满足
$$
w_a(N+1)(N+2)=2(-1)^N\binom{m-1}{a-1}.
\tag{1208.34}
$$
这化简的是完整 ordinary contraction。它不删除一般 $T$ 的支持 CM 列；本文对 $T_*$ 的静态边界计算也不能直接替代一般返回向量的全部 analytic CM 项。

## 12. 更正范围及下一实际问题

本篇修正的是完整 $\mathcal V_m(T_*)$ 的识别和数值。R1199 的全部 generic normal/收缩、R1200 的 canonical phase 与 rational operator、R1201 的 SS 求积和有限 Rankin–Cohen 证明继续使用。R1205 中涉及 $T_*$ 完整单位的条件推论，可改为消费 (1208.1)；其纯型秩和 $\ker\mathfrak c$ 识别本来独立。

仍未证明 $\mathcal V_m|_{\ker\mathfrak c}$ 非零，允许它在该首层恒零。若 $\mathfrak c(T_*)=0$，R1205/R1196 的实际同底提升及首列独立性把 (1208.1) 送到纯 cuspidal 格；若 $\mathfrak c(T_*)\ne0$，不能这样做。无论哪一种情形，都不能从整个 packet 的单位直接断言指定半秩 $C$ 保留它，也没有 whole-disc 排除结论。

本文的修正来自实际 frame、全部 node 极界及完整纸面 residue；未执行数学程序，未重跑 R1201 的有限 probe，未按预期单位值选择符号。

## 来源与核验

- R1014、R1018 §§3、5–6（特别是 (1018.19)）：同一个 $P$ 的全部主化、原 $e_D/e_I$、真实 quotient-isogeny、支持尾 flux 和同一 $\psi$ 的 CM node 截断。
- R1021 §§1–4、R1023 §3：原 full-$p$ 的非约化 affine 模型、target 参数的准确 $p$ 误差及真实 node 单位正规化。
- R1196：同一个相对 Picard log、Serre 配对和实际整角；本文不将有限 Picard log 换成任意局部对数。
- R1197 §§2–6：完整有限角、全部 CM 旗标、原参考函数 $H_k$ 及其全分支 determinant 运输；本篇另付顶层 $k=2g$。
- R1199 §§1–5、R1200 §§2–7、R1201：原全部 SS 收缩、canonical Igusa–Weil phase 及 SS 有限和。R1199 §6 的支持节点接口由本文替换。
- R1204–1207：实际返回算子、纯型格、SS 的 $p$ 阶极部与非约化 CM 截面。
- canonical character 的一手来源沿 R1200 的 Ulmer 实际 Igusa 微分与刚化 Poincaré 比较；本篇在同一个 good CM 模型逐式计算，未在退化原模型上代入 generic 公式。

global_route 提出并核准原 frame 缺项、原有限 Čech frame 比较、顶层及 corrected residue；root 独立核 canonical CM 相位、全 normal 分母界和显示求和；o2_high_coefficient 独立核 (1208.22)–(1208.24) 与 (1208.32)–(1208.34) 的纸面代数。核对范围以各项实际证明为准，不作为额外发布审批。

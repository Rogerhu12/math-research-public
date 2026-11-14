# R150 附录：复加权主行与独立实受控骨架的全部首一剪切幂

日期：2026-11-13（UTC）。normal_resume_1cf；根代理独立核查共享平移、复中心全柱预算与两支拼接，kernel 独立核查相位缺陷和局部复指数。全文核验已完成。

状态：完整证明。本稿关闭此前保留的“主行再加复加权误差、辅助仍含独立实受控骨架”一支。原完整 Bell 多项式、普通点态幂和任意复指数权均保留。

## 1. 定理与未变的原点态向量

设
$$
a_j\ge0,\qquad a\in\ell^2\setminus\ell^1,
$$
并取实 $b\in\ell^2$，满足
$$
|b_j|\le C_0a_j.
$$
取任意复行 $d^0,d^1$，使
$$
d^\nu_j=0\quad(a_j=0),\qquad
K_\nu^2:=\sum_{a_j>0}\frac{|d^\nu_j|^2}{a_j}<\infty
\quad(\nu=0,1),
\tag{1.1}
$$
以及任意复 $e^0,e^1\in\ell^1$、复常数 $u_*,v_*,\gamma$。
原函数为
$$
u=u_*+\sum_j(a_j+d^0_j+e^0_j)\chi_j,
$$
$$
v=v_*+\sum_j(b_j+\gamma a_j+d^1_j+e^1_j)\chi_j.
\tag{1.2}
$$

令 $G(x,s)\in\mathbb C[x,s]$ 满足
$$
\deg_sG=m\ge1,\qquad G\text{ 关于 }s\text{ 首一},\qquad
\deg_{\rm tot}G\le m.
\tag{1.3}
$$
则对每个 $\lambda\in\mathbb C$、整数 $r\ge1$，以及任意
$$
w=w_*+\sum_jw_j\chi_j,\qquad (w_j)\in\ell^2(\mathbb C),
$$
都有
$$
\boxed{
[G(u,v-u^2)-\lambda]^r e^w
\text{ 对原实际 }A\text{ 循环。}
}
\tag{1.4}
$$

不对 $a$ 加增长、物理顺序或尾比条件。两支仍由已证的计数/全柱二分覆盖。
若 $d^0=0$，旧[实骨架加复加权误差](R150-appendix-real-controlled-skeleton-weighted-complex-errors-and-shear-powers.md)已经覆盖；本稿新增一般复 $d^0$。
一般复同阶骨架替代实 $b$ 时，本文只在下述有限计数分支另给结论，不免费扩展无限计数分支。

## 2. 一个真实空谱主锚及其局部有界系数

记
$$
X_0=X_a,\qquad L_0=X_0^{-1},\qquad Y=X_b,
\qquad U=X_{a+d^0}.
$$
加权相对域定理已证明
$$
D_\nu:=Y_{d^\nu}L_0\in
\mathcal B:=\overline{\operatorname{alg}(\mathcal A,L_0)}^{\|\cdot\|},
\qquad \chi(D_\nu)=0.
\tag{2.1}
$$
$\mathcal B$ 是交换局部 Banach 代数，$L_0$ 的字符为0。
$B_0=I+D_0$ 是实际有界单位，而且
$$
U=B_0X_0,\qquad\operatorname{Dom}U=\operatorname{Dom}X_0.
\tag{2.2}
$$
完整域识别可由同一有限柱图核心直接复核：
$B_0X_0$ 闭，且 $B_0$ 有界可逆使其图范数与 $X_0$ 图范数等价；
在有限柱上它等于原第一阶 $X_{a+d^0}$，两边的有限柱均为图核心。

稍后选择一个足够大的实 $\omega\ge0$，令
$$
Z=U+\omega I,\qquad
Q_0=I+D_0+\omega L_0.
$$
则
$$
Z=Q_0X_0,\qquad
L:=Z^{-1}=L_0Q_0^{-1}\in\mathcal B.
\tag{2.3}
$$
$Q_0-\lambda L_0$ 对每个复 $\lambda$ 的字符均为1，故为单位。
因此
$$
(Z-\lambda I)^{-1}
=L_0(Q_0-\lambda L_0)^{-1}\in A'
\quad(\lambda\in\mathbb C),
\tag{2.4}
$$
$Z$ 空谱，$L$ 拟幂零。所有这些等式均在原完整第一阶域上成立。

原主行的可和项没有塞进后面的尾预算：
它们始终留在
$H_0=u_*I+Y_{e^0}\in\mathcal A$ 中。
同样保留 $H_1=v_*I+Y_{e^1}\in\mathcal A$。
于是原实际两 first 可以写成
$$
X_u=Z+(H_0-\omega I),\qquad
X_v=Y+RZ+H_1,
\tag{2.5}
$$
其中
$$
R=(\gamma I+D_1)Q_0^{-1}\in\mathcal B.
\tag{2.6}
$$
这里没有把 $Y$ 断言为相对 $Z$ 有界。

## 3. 全部大参数共享的增生平移

写
$$
\zeta_j=a_j+d^0_j.
$$
对实 $p>0$ 和任意复 $d$，平方根的凹性给
$$
|p+d|-\operatorname{Re}(p+d)\le\frac{|d|^2}{2p}.
\tag{3.1}
$$
因此
$$
\Delta_0:=
\sum_j\left(|\zeta_j|-\operatorname{Re}\zeta_j
+8|\zeta_j|\eta_j\right)<\infty.
\tag{3.2}
$$
零 $a_j$ 位同时有 $\zeta_j=0$。

取 $c\ge c_*:=2C_0+1$。
因为
$$
p_j^\pm=ca_j\pm b_j\ge(c-C_0)a_j\ge ca_j/2,
$$
(3.1) 给
$$
\sum_j
\left(|c\zeta_j\pm b_j|
-\operatorname{Re}(c\zeta_j\pm b_j)\right)
\le\frac{c^2}{2(c-C_0)}K_0^2
\le cK_0^2.
\tag{3.3}
$$
实际 carry 的成本满足
$$
8\sum_j|c\zeta_j\pm b_j|\eta_j
\le8c\sum_j(|\zeta_j|+a_j)\eta_j.
\tag{3.4}
$$
右侧有限，且除去 $c$ 后与参数无关。

例如固定
$$
\boxed{
\omega=1+K_0^2+
8\sum_j(|\zeta_j|+a_j)\eta_j
}
\tag{3.5}
$$
已经足够同时保证
$$
\boxed{
Z,\qquad cZ+Y,\qquad cZ-Y
\text{ 对每个 }c\ge c_*\text{ 都最大增生。}
}
\tag{3.6}
$$
这里使用的是各原第一阶的完整闭实现。
准确理由是 R138 §3 的实际下界：
纯一位 $\operatorname{Re}(zS_j^0)\ge-(|z|-\operatorname{Re}z)I$，
加上 $\|V_j-S_j^0\|\le8\eta_j$，先得有限柱下界，
再由图核心传到完整域。
第一阶的 $C$ 自伴性把同一下界传到通常伴随；
加任意正实数后的下界使像闭，伴随无核使像稠密，因此满射。
这付清最大增生性，不只证明形式二次型非负。

由 (3.2)、(3.5)，$\omega\ge\Delta_0$。
后面的计数半群和所有 $cZ\pm Y$ 使用同一个固定 $\omega$。

## 4. 复局部指数、可和相位补偿与真实计数界

### 4.1 任意复时间的局部界

实际关系为
$$
N_j^2=\eta_jN_{j+1},\qquad\|N_j\|=1,\qquad
V_j=I-2N_j+E_j',
$$
$$
E_j'=2N_j^2(I+N_j)^{-1},\qquad\|E_j'\|\le6\eta_j.
$$
$E_j'$ 与 $N_j$ 交换。
奇偶幂分别求和给，对任意复 $z$，
$$
\|e^{2zN_j}\|
\le\cosh(2|z|\sqrt{\eta_j})
+\eta_j^{-1/2}\sinh(2|z|\sqrt{\eta_j})
\le(1+2|z|)e^{2|z|\sqrt{\eta_j}}.
$$
因为 $\eta_j<1/4$，可放宽为
$$
\boxed{
\|e^{-zV_j}\|
\le(1+2|z|)
\exp[-\operatorname{Re}z+6\sqrt{\eta_j}|z|].
}
\tag{4.1}
$$
这保留完整实际 $N_j$；没有在复时间下假设纯正半群收缩。

置
$$
\delta_j=|\zeta_j|-\operatorname{Re}\zeta_j
+8|\zeta_j|\eta_j,\qquad
T_j=\zeta_jV_j+\delta_jI.
$$
$T_j$ 是有界增生算子。
若 $\zeta_j\ne0$，在时间 $T/|\zeta_j|$ 用 (4.1)，得到
$$
\left\|e^{-(T/|\zeta_j|)T_j}\right\|
\le(1+2T)\exp[-(1+8\eta_j-6\sqrt{\eta_j})T].
\tag{4.2}
$$
相位已由 $\delta_j$ 准确抵消。
给任意 $\kappa<1$，先固定充分大的 $T$，
再舍去有限个物理位，使 (4.2) 对剩余全部位不超过 $e^{-\kappa T}$。
余下时间段由 $T_j$ 的增生性付收缩，所以
$$
\|e^{-tT_j}\|
\le e^{-\kappa T\lfloor t|\zeta_j|/T\rfloor}
\quad(j\ge J,\ t\ge0).
\tag{4.3}
$$
零系数位的计数为0。

### 4.2 有限集合分解支付全无界半群

对任意有限 $F$，
$$
Z=\sum_{j\in F}T_j+
\left[X_{\zeta\mathbf1_{F^c}}+
\Bigl(\sum_{j\notin F}\delta_j\Bigr)I\right]
+(\omega-\Delta_0)I.
\tag{4.4}
$$
中括号中的真实尾第一阶最大增生，理由同 §3。
有限头有界并与它的完整域、预解和半群交换；
因此 (4.4) 的半群因子分解由有界交换扰动识别，完全合法。

对给定 $t$，只取有限集合
$F=\{j\ge J:t|\zeta_j|\ge T\}$，
其余因子均为收缩。由 (4.3)，
$$
\boxed{
\|e^{-tZ}\|
\le
\exp\!\left[-\kappa T
\sum_{j\ge J}\left\lfloor\frac{t|\zeta_j|}{T}\right\rfloor
\right].
}
\tag{4.5}
$$
这不依赖一个未经识别的无穷复指数乘积。

### 4.3 加权误差保留无限计数分支

令
$$
\Theta_a(t)=\sum_j\lfloor ta_j\rfloor,\qquad
\Lambda_a=\limsup_{t\to\infty}
\frac{\Theta_a(t)}{t\log t}.
$$
对固定 $0<\varepsilon<1$，坏集合
$$
B_\varepsilon=\{j:|d^0_j|>\varepsilon a_j\}
$$
满足
$$
\sum_{j\in B_\varepsilon}a_j
\le K_0^2/\varepsilon^2<\infty.
$$
在补集上 $|\zeta_j|\ge(1-\varepsilon)a_j$。
因此
$$
\Theta_{|\zeta|}(t)
\ge
\Theta_a((1-\varepsilon)t)
-(1-\varepsilon)t\sum_{j\in B_\varepsilon}a_j.
\tag{4.6}
$$
若 $\Lambda_a=\infty$，则 $\Lambda_{|\zeta|}=\infty$。
有限物理头的删除在 (4.5) 中也只损失 $O(t)$。
所以原[好时间窄条带稿](R150-appendix-harmonic-positive-anchor-sharp-strip-budget-and-all-shear-powers.md)
§3.1 所需的任意大计数预算完全保留。

更明确地，对任意固定 $k'>0$，可先选 $k>k'$，
再由 (4.5)—(4.6) 选 $\tau_n\to\infty$，使
$$
\|e^{-\tau_n Z}\|\le e^{-k\tau_n\log\tau_n}.
$$
置 $r_n=k'\log\tau_n$。
将实际 Laplace 预解积分按长度 $\tau_n$ 分块，收缩性给
$$
\boxed{
\sup_{\operatorname{Re}z\le r_n}
\|(Z-z)^{-1}\|
\le 2e^{r_n\tau_n}/r_n
}
\tag{4.7}
$$
对充分大的 $n$ 成立。
范数积分在全平面合法，因为 (4.5) 与不可和 $|\zeta|$ 给超指数衰减；
也可先在左半平面识别，再用已付空谱继续。
所以这里不是仅在一条竖线付界。

## 5. 原完整 Bell 图归一到同一相伴问题

先对原 (1.2) 与原 $w$ 构造完整 Bell 多项式，
包括原 $d^0,d^1,e^0,e^1,\gamma$ 带来的全部 cumulant、常数和倾斜。
不把它们换成未扰动 $a,b$ 的 Bell 系数。

记 $d=mr$。R186 及原首一剪切图定理给原闭 Bell 算子
$\mathcal P_{\lambda,r,w}$；
在原倾斜 first 及其剪切变量中，它是总次数至多 $d$、
关于剪切变量首一的 $\mathcal A$ 系数多项式。
原点态向量是
$$
\mathcal P_{\lambda,r,w}e^w
=[G(u,v-u^2)-\lambda]^r e^w.
\tag{5.1}
$$

任意复指数倾斜只加入实际有界 $\mathcal A$ 系数。
因此 (2.5) 在倾斜后写为
$$
x_{\rm old}=Z+H,\qquad
y_{\rm old}=Y+RZ+K,
\qquad H,K\in\mathcal A,\ R\in\mathcal B.
$$
若 $s=Y-Z^2$，则准确代换为
$$
\boxed{
x_{\rm old}=Z+H,\qquad
s_{\rm old}=s+(R-2H)Z+K-H^2.
}
\tag{5.2}
$$
它保持总剪切次数和首一 $s^d$，只把有界系数扩大到 $\mathcal B$。

域识别用原有限族的 R186 共同正则器：
包含 $X_0,Y_{d^0},Y_{d^1},Y$ 与所需原 first。
在共同深域上 (5.2) 是逐词等式；
$e^w$ 属于全部这些词域且循环。
两边在其 $\mathbb C[A]e^w$ 轨道上相同，
该轨道是对应规范闭多项式图核心，因此仍为同一个原闭 Bell 实现。
这不是把一个形式代换直接宣布为最大域等式。

令
$$
W=(Y-Z^2)_{\rm can},\qquad
\mathscr T=WL,\qquad
\operatorname{Dom}\mathscr T
=\{h:Lh\in\operatorname{Dom}W\}.
\tag{5.3}
$$
$W$ 是规范闭多项式，$L$ 有界，所以 $\mathscr T$ 闭。
在充分深的共同域上
$$
\mathscr T=YL-Z.
\tag{5.4}
$$
用 $L^d$ 归一 (5.2) 后，得到关于 $\mathscr T$ 的首一多项式，
其全部系数在 $\mathcal B$。

原[相伴深图构造](R150-appendix-finite-order-positive-anchor-companion-graphs-and-all-shear-powers.md)
及[实骨架扩展](R150-appendix-real-controlled-skeleton-weighted-complex-errors-and-shear-powers.md)
在此适用，具体使用的只是：
$Z$ 空谱、有界 $L$ 与完整词域交换、R186 有限族共同正则器、以及首一最高项。
正系数并不是该图构造的假设。
若原 Bell 核非零，就得到某个有限放大中非零闭空间 $\mathcal M$，满足
$$
\mathcal M\text{ 被所有对角 }A'\text{ 保持},\qquad
\mathcal M\subseteq\operatorname{Dom}\mathscr T^{(d)},
$$
$$
\mathscr T^{(d)}\mathcal M\subseteq\mathcal M,\qquad
J=\mathscr T^{(d)}|_{\mathcal M}\in B(\mathcal M).
\tag{5.5}
$$
深度不同的图闭包由同一正则器一致识别，闭的对角 $\mathscr T$ 付全图域；
首一相伴矩阵保闭包。
因为相伴系数属于局部 $\mathcal B$，
其逆在字符多项式非零处由伴随矩阵的实际有界多项式给出并保该闭图，
故 $J$ 还具有有限谱。

下面两支都排除 (5.5)。

## 6. 有限计数时真实复主行的中心和尾预算

假设 $\Lambda_a<\infty$。
已证[计数/全柱二分](R150-appendix-counting-column-budget-dichotomy-and-all-real-controlled-shears.md)
给下降重排 $r_1\ge r_2\ge\cdots$ 的一列 $n\to\infty$，满足
$$
S_n=\sum_{k\le n}r_k\to\infty,\qquad
\frac{n\sum_{k>n}r_k^2}{S_n^2}\longrightarrow0.
\tag{6.1}
$$

取 $F_n$ 为最大的 $n$ 个非零 $a$ 系数所在物理位，
再并入前 $n$ 个物理位；固定一个相容的并列值选法。
于是
$$
d_n:=|F_n|\le2n,\qquad Q_{F_n}\to I\text{ 强},
$$
$$
s_n^a=\sum_{j\in F_n}a_j\ge S_n.
$$
$Q_F$ 是所有支撑于 $F$ 的 Walsh 柱投影。

对真实复主行 $\zeta=a+d^0$，设
$$
\sigma_n=\omega+\sum_{j\in F_n}\zeta_j,\qquad
t_n=\sum_{j\in F_n}b_j.
$$
加权 Cauchy–Schwarz 给
$$
\left|\sum_{j\in F_n}d^0_j\right|\le K_0\sqrt{s_n^a},
\qquad
\sum_{j\in F_n}|d^0_j|\le K_0\sqrt{s_n^a}.
$$
因此
$$
\boxed{
\sigma_n/s_n^a\to1,\qquad
|\sigma_n|\to\infty,\qquad
\frac{\sum_{j\in F_n}(|\zeta_j|+|b_j|)}
{|\sigma_n|}\le C
}
\tag{6.2}
$$
对充分大 $n$ 一致。常数 $\omega$ 已进入准确中心，不被漏掉。

再令
$$
K_{0,n}^2=\sum_{j\notin F_n,\ a_j>0}|d^0_j|^2/a_j.
$$
对 $F_n$ 外的正位，$a_j\le r_{n+1}$，所以
$$
\|d^0_{F_n^c}\|_2^2\le r_{n+1}K_{0,n}^2,
$$
$$
\frac{d_n\|d^0_{F_n^c}\|_2^2}{(s_n^a)^2}
\le\frac{2nr_{n+1}K_{0,n}^2}{S_n^2}
\le\frac{2K_{0,n}^2}{S_n}\longrightarrow0.
\tag{6.3}
$$
同时 (6.1) 控制 $a$ 尾，$|b|\le C_0a$ 控制 $b$ 尾。
结合 (6.2)，得到真实所需的总尾预算
$$
\boxed{
g_n:=\|\zeta_{F_n^c}\|_2+\|b_{F_n^c}\|_2,\qquad
\frac{\sqrt{d_n}\,g_n}{|\sigma_n|}\longrightarrow0.
}
\tag{6.4}
$$

## 7. 复中心归一全柱引理：完整域与投影配对

这里将旧归一全柱证明的每一个标量中心换成准确复中心。
只使用 §6 的三个量；不以一个形式最高单位系数代替真实主行。

令 $\mathcal D_\infty^\dagger$ 为 $Z^*,Y^*$ 全部有限自然词的共同域。
R251 的任意位集补集指数尺度以及共同 $C$ 给
$$
Q_FH\subseteq\mathcal D_\infty^\dagger.
$$
$L^*$ 保持该域并与各词交换。
仅在该深域上定义
$$
\mathscr D^\dagger=L^*Y^*-Z^*.
\tag{7.1}
$$
它保持该共同深域，所有有限迭代因而合法；
不宣称这是某个未核验的全局最大伴随域。

固定 $F=F_n$，令
$$
H_\zeta=\sum_{j\in F}\zeta_j(V_j-I),\qquad
H_b=\sum_{j\in F}b_j(V_j-I),
$$
并令 $Z_\zeta,Y_b^{\rm tail}$ 为相应补集第一阶。
在准确自然深域上，
$$
\frac{\mathscr D^\dagger+\overline{\sigma_n}I}
{\overline{\sigma_n}}
=
\frac{\overline{t_n}}{\overline{\sigma_n}}L^*
+
\frac{-H_\zeta^*+L^*H_b^*}{\overline{\sigma_n}}
+
\frac{-Z_\zeta^*+L^*(Y_b^{\rm tail})^*}
{\overline{\sigma_n}}.
\tag{7.2}
$$
复共轭的位置不能省略。三项在共同深域上交换。

第一项是统一有界标量倍的拟幂零 $L^*$；
对每个固定 $\epsilon>0$，其 $\ell$ 次幂由
$K_\epsilon\epsilon^\ell$ 控制。
第二项是
$$
\sum_{j\in F}
\frac{-\overline{\zeta_j}I+\overline{b_j}L^*}
{\overline{\sigma_n}}(V_j^*-I),
$$
系数范数总和由 (6.2) 一致控制。
R251 的真实任意位进位因此给一个固定 $A$，使其 $k$ 次幂范数不超过 $A^k$，
并在 $k\ge\max(2d_n,16)$ 时不超过
$A^k e^{-\gamma_0k^4}$。

第三项在全柱上的 $q$ 次自然幂满足
$$
\left\|
\left(
\frac{-Z_\zeta^*+L^*(Y_b^{\rm tail})^*}
{\overline{\sigma_n}}
\right)^qQ_{F_n}\right\|
\le
\left(C\frac{g_n}{|\sigma_n|}\sqrt q\right)^q.
\tag{7.3}
$$
完整域由同一补集尺度支付；
对 $Z_\zeta+zY_b^{\rm tail}$ 用算子值 Cauchy 系数提取，
先取得混合词界，再将有界 $L^*$ 移到最左端。
这里不把两个无界尾的单独作用范数相乘。

$|\zeta|$ 不可和：取 (4.6) 前的坏集合 $B_{1/2}$，其 $a$ 质量有限，而补集上 $|\zeta_j|\ge a_j/2$。所以每个有限 $F_n$ 外仍有非零 $\zeta_j$，$g_n>0$，以下除法真实有定义。

置 $\varepsilon_n=\sqrt{d_n}g_n/|\sigma_n|\to0$，
$p_n=\lceil d_n/\varepsilon_n\rceil$。
沿 (6.4) 的子列，$p_n/d_n\to\infty$ 且
$g_n\sqrt{p_n}/|\sigma_n|\to0$。
同一真实三项展开，按头因子数 $k<2d_n$ 与 $k\ge2d_n$ 分组，
低头组合熵趋零、高头进位根趋零、尾根趋零；
因此原归一全柱稿 §§3—5 的证明逐项给
$$
\boxed{
\left\|
\left(
\frac{\mathscr D^\dagger+\overline{\sigma_n}I}
{\overline{\sigma_n}}
\right)^{p_n}Q_{F_n}
\right\|^{1/p_n}\longrightarrow0.
}
\tag{7.4}
$$
$K_\epsilon$ 始终先固定 $\epsilon$ 使用，再令 $\epsilon\downarrow0$；
无随 $n$ 改变未知空间的范数。

若 (5.5) 成立，记 $P$ 为到 $\mathcal M$ 的投影。
对 $h\in\mathcal M$，用足够深的共同正则器得到 $h_\varepsilon\to h$，
保持 $\mathcal M$ 且
$\mathscr T h_\varepsilon=Jh_\varepsilon\to Jh$。
对实际伴随深域中的 $f$，(5.4) 给
$$
\langle Jh_\varepsilon,f\rangle
=\langle h_\varepsilon,\mathscr D^\dagger f\rangle.
$$
取极限并按深域迭代，得到
$$
P(\mathscr D^\dagger+\overline{\sigma_n}I)^{p_n}Q_{F_n}
=(J^*+\overline{\sigma_n}I)^{p_n}PQ_{F_n}.
\tag{7.5}
$$
这里及上式均按相应有限对角放大理解。

由于 $|\sigma_n|\to\infty$，
$$
\left\|\left(I+\frac{J^*}{\overline{\sigma_n}}\right)^{-1}\right\|
\le(1-\|J\|/|\sigma_n|)^{-1}\to1.
$$
(7.4)—(7.5) 迫 $\|PQ_{F_n}\|\to0$；
而 $Q_{F_n}\to I$ 强，所以 $P=0$，矛盾。
这一支甚至不需要 $J$ 有限谱，也允许复 $b$ 满足同一模支配。

## 8. 无限计数时的准确二次域与半条带排除

现在假设 $\Lambda_a=\infty$，并保留 $b$ 为实。
设 (5.5) 成立。
所有下述 first 的部分都定义在 $\mathcal M$ 上，
不是无证把环境全部域交进 $\mathcal M$。

### 8.1 部分生成元和自然二次式

$Z$ 与 $cZ\pm Y$ 的实际预解属于 $A'$ 并保持 $\mathcal M$。
因此它们在 $\mathcal M$ 上的自然部分最大增生；
$Z_{\mathcal M}$ 的全部预解是原预解的限制，故仍空谱。
$L_{\mathcal M}$ 是其有界拟幂零逆。
这些事实由预解/Yosida 强逼近付域的稠密性，不仅使用环境单射稠密像。

$J$ 与 $L_{\mathcal M}$ 及所有共同有界正则器交换。
在共同正则深核心上，(5.4) 给
$$
Y_{\mathcal M}f=Z_{\mathcal M}^2f+JZ_{\mathcal M}f.
\tag{8.1}
$$
对 $f\in\operatorname{Dom}Z_{\mathcal M}^2$，
同一共同正则器在 $Z_{\mathcal M}^2$ 图中逼近 $f$。
(8.1) 右侧收敛，$Y$ 的闭性遂证明
$f\in\operatorname{Dom}Y_{\mathcal M}$，且 (8.1) 仍成立。

于是自然二次多项式
$$
Q_\pm=\pm Z_{\mathcal M}^2+(cI\pm J)Z_{\mathcal M},
\qquad
\operatorname{Dom}Q_\pm=\operatorname{Dom}Z_{\mathcal M}^2
\tag{8.2}
$$
是 $(cZ\pm Y)_{\mathcal M}$ 的限制。具体地，对上述同一 $f_\varepsilon$，完整第一阶 $(cZ\pm Y)f_\varepsilon$ 在共同深域上等于 $Q_\pm f_\varepsilon$，且右侧收敛到 $Q_\pm f$；原完整第一阶闭性和 $\mathcal M$ 的闭性直接付此包含。因此未先假定自然和在交域上闭。
(8.2) 的最高系数为单位，$J$ 与 $L_{\mathcal M}$ 交换，
故对每个 $\lambda$ 可以因式分解为
$Z_{\mathcal M}^2$ 乘上 $I+$“拟幂零逆乘有界交换子”的单位。
因此 $Q_\pm$ 闭且空谱。
取一个左半平面参数，$Q_\pm-\lambda$ 满射，
而最大增生的 $(cZ\pm Y)_{\mathcal M}-\lambda$ 单射；
包含关系立即迫两域和两算子相等。
因此
$$
\boxed{
\pm(Z_{\mathcal M}^2+JZ_{\mathcal M})+cZ_{\mathcal M}
\text{ 在准确域 }\operatorname{Dom}Z_{\mathcal M}^2
\text{ 最大增生。}
}
\tag{8.3}
$$
这付清了半条带引理的自然二次域；
未把一般无界自然和预设为闭。

### 8.2 有限谱分支和真实好时间预算

$J$ 有限谱，取一个非零 Riesz 分支，写 $J=\lambda_0I+N$，
$N$ 拟幂零。
原窄条带稿 §5 的等价 Hilbert 范数可使 $\|N\|$ 任意小。
所有 $Z$、$cZ\pm Y$ 的有界半群及预解均与 $N$ 交换；
该范数按 $\sum_k\epsilon^{-2k}\|N^kf\|^2$ 定义，
所以它们的原收缩界和 (4.5)、(4.7) 的预算逐项保留，
不产生随好时间增长的新常数。

固定 $c\ge c_*$，再选任意 $k'>c/(2\pi)$。
(4.7) 给 $r_n=k'\log\tau_n$ 的整左半面界。
由 (8.3)，原窄条带稿 §§6—7.1 的实际预解因式论证把未控制区域压进
两条方向 $\arg z=\pm\pi/4$ 的固定宽半条带；
在 $\|N\|$ 足够小时，其半宽可取任意略大于 $c/(2\sqrt2)$ 的 $h$。
选择
$$
\frac{c}{2\sqrt2}<h<\frac{\pi k'}{\sqrt2},
\qquad
\frac1{\sqrt2k'}<\beta<\frac{\pi}{2h}.
$$
远端矩形取
$L_n=\sqrt2r_n-h-|\operatorname{Re}\lambda_0|-1$。
(4.7) 在这些整条远端边上控制 $\log\|R_Z\|$ 为 $O(\tau_n\log\tau_n)$；
障碍 $\exp[-\epsilon\cosh(\beta(z-z_0))]$ 的远端衰减为
$\exp[-c_\epsilon\tau_n^{\beta\sqrt2k'}]$，
其幂指数严格大于1。
按原证明先让矩形远端趋远，再令 $\epsilon\downarrow0$，
得到两半条带内的相同有界性。

条带外的界来自 (8.3) 与最大增生预解，左半平面来自 $Z$ 最大增生。
因此 $Z_{\mathcal M}$ 的整个预解函数有界。
Liouville 及负实轴上的预解衰减迫该函数恒零，和它是实际逆矛盾。
所以无限计数支也排除了 (5.5)。

此处唯一使用 $b$ 实的地方，是 §3 对 $ca\pm b$ 的正实基行；
原主误差 $d^0$、副误差 $d^1$、$\gamma$、可和项及 $w$ 都保持复值。

## 9. 两支合并与原循环性

$\Lambda_a$ 要么有限，要么为无穷。
§§6—7 与 §8 分别排除相伴非零闭图，
因此原 $\mathcal P_{\lambda,r,w}$ 核为零。

它仍是最初原完整 Bell 的规范 $C$ 自伴闭实现；
R186 的循环指数图核心于是给其像稠密，并且
$$
[\mathcal P_{\lambda,r,w}e^w]_A
=\overline{\operatorname{Ran}\mathcal P_{\lambda,r,w}}=H.
$$
结合 (5.1)，证明 (1.4)。

新结论确实允许主、副两行各有复加权误差。
没有要求原 $X_vX_u^{-1}$ 有界；
独立实骨架 $b$ 可以不属于单锚相对行类。
有限计数支还允许一般复受控 $b$；
无限计数且尾比不小的一般复同阶骨架仍未由本稿处理。
总剪切次数超过 (1.3)、非受控骨架及正常见证的聚合上界也保持开放。
普通 Hilbert 不变子空间问题仍未解决。

## 10. 有限相位缺陷的内禀旋转表述

本节只是前述主定理的等价系数改写，不另计新的算子结论。
对非负权 $a\in\ell^2$，记
$$
\mathscr J_a=
\ell^1(\mathbb C)+
\left\{d:\ d_j=0\ (a_j=0),\quad
\sum_{a_j>0}|d_j|^2/a_j<\infty\right\}.
\tag{10.1}
$$

### 10.1 权重替换不改变误差类

若 $a,\alpha\ge0$ 且
$$
\sum_j(\sqrt{a_j}-\sqrt{\alpha_j})^2<\infty,
\tag{10.2}
$$
则
$$
\mathscr J_a=\mathscr J_\alpha,\qquad
a-\alpha\in\mathscr J_a,
\tag{10.3}
$$
且
$$
\{b+\gamma a+j:\ b\text{ 实},\ |b|\le Ca
\text{ 对某 }C<\infty,\ \gamma\in\mathbb C,\ j\in\mathscr J_a\}
$$
在把 $a$ 换成 $\alpha$ 后保持不变。

证明：在
$E=\{a/2\le\alpha\le2a\}$ 上，两权可比。
在补集上，(10.2) 迫
$\sum_{E^c}(a_j+\alpha_j)<\infty$。
因此任一加权平方可和误差在 $E^c$ 上由 Cauchy–Schwarz 属于 $\ell^1$；
在 $E$ 上则可直接更换分母，得到误差类相等。
同样，$a-\alpha$ 在补集可和，而在 $E$ 上
$$
\frac{|a-\alpha|^2}{\alpha}
=(\sqrt a-\sqrt\alpha)^2
\frac{(\sqrt a+\sqrt\alpha)^2}{\alpha}
\le(1+\sqrt2)^2(\sqrt a-\sqrt\alpha)^2.
$$
最后将实骨架 $b$ 在 $E^c$ 上的可和部分放入误差，
在 $E$ 上保留它；它受 $2C\alpha$ 支配。
$\gamma a-\gamma\alpha$ 已属共同误差类。
反向完全相同。零权位也已包括在这个分解中。证毕。

特别地，若 $\zeta=a+d+e$，其中
$\sum |d|^2/a<\infty$ 且 $e\in\ell^1$，那么
$\alpha=|\zeta|$ 满足 (10.2)。
确实，令 $\alpha_0=|a+d|$，则
$$
(\sqrt{\alpha_0}-\sqrt a)^2\le |d|^2/a,\qquad
(\sqrt\alpha-\sqrt{\alpha_0})^2\le |e|.
$$
在 $\ell^2$ 中用三角不等式即可。
同时
$$
\sum_j\bigl(|\zeta_j|-\operatorname{Re}\zeta_j\bigr)
\le\frac12\sum_{a_j>0}|d_j|^2/a_j+2\sum_j|e_j|<\infty.
\tag{10.4}
$$
因为 $a\notin\ell^1$，(10.2) 也保证 $\alpha\notin\ell^1$：
否则 $\sqrt\alpha\in\ell^2$，从而 $\sqrt a\in\ell^2$，矛盾。

### 10.2 直接用原系数检验

写原函数为
$$
u=u_*+\sum_j\mu_j\chi_j,\qquad
v=v_*+\sum_j\nu_j\chi_j,
\qquad \mu,\nu\in\ell^2(\mathbb C),\quad\mu\notin\ell^1.
$$
若存在实角 $\theta$，使
$$
\Delta_\theta(\mu)
:=\sum_j\left(|\mu_j|-\operatorname{Re}(e^{-i\theta}\mu_j)\right)
<\infty,
\tag{10.5}
$$
置 $\alpha_j=|\mu_j|$。
进一步假设
$$
e^{-2i\theta}\nu=b+\gamma\alpha+j,
\qquad b\text{ 实},\quad |b|\le C\alpha,\quad
\gamma\in\mathbb C,\quad j\in\mathscr J_\alpha.
\tag{10.6}
$$
则 §1 的全部循环性结论仍成立。

证明：令
$\widetilde u=e^{-i\theta}u$、
$\widetilde v=e^{-2i\theta}v$。
原主行在该坐标中为
$$
e^{-i\theta}\mu=\alpha+d,\qquad
d=e^{-i\theta}\mu-\alpha,
$$
而逐项有准确恒等式
$$
\boxed{
\sum_{\alpha_j>0}\frac{|d_j|^2}{\alpha_j}
=2\Delta_\theta(\mu)<\infty.
}
\tag{10.7}
$$
因此主、副两行正好满足 §1，常数项照原样旋转即可。

若 $G$ 关于 $s$ 首一、$\deg_sG=m$ 且总次数至多 $m$，置
$$
\widetilde G(x,s)
=e^{-2im\theta}G(e^{i\theta}x,e^{2i\theta}s),
\qquad
\widetilde\lambda=e^{-2im\theta}\lambda.
$$
$\widetilde G$ 仍有相同总次数限制且关于 $s$ 首一，并且
$$
[G(u,v-u^2)-\lambda]^r e^w
=e^{2imr\theta}
[\widetilde G(\widetilde u,\widetilde v-\widetilde u^2)
-\widetilde\lambda]^r e^w.
$$
右侧的非零标量不影响循环性，故结论成立。
这里没有改变原指数权，也没有重新计算或替换原 Bell cumulant。证毕。

反过来，§1 的系数在 $\theta=0$ 时必满足 (10.5)，
而 §10.1 把其原 $a$ 精确换为 $|\mu|$ 后也给 (10.6)。
所以本节确实是原范围连同坐标旋转的内禀重述。

在 $\mu\notin\ell^1$ 的前提下，满足 (10.5) 的角度模 $2\pi$ 唯一。
若 $\theta,\theta'$ 都满足，则由 (10.7) 和三角不等式，
$$
|e^{i\theta}-e^{i\theta'}|^2\sum_j|\mu_j|<\infty,
$$
迫两个相位相同。
因此不能再任意选择角度去实化一个不满足 (10.6) 的独立复辅助行；
一般复同阶骨架的剩余缺口没有被这个坐标改写消去。

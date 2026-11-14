# R150 附录：高次全柱多项式测试、可逆归一化部分与复辅助的全部非零最高簇

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。可逆部分的投影回传与 Cauchy 系数接口由根代理提出；全柱多项式幂预算由 normal_resume_1cf 逐项证明。

状态：完整证明；根代理与 kernel_resume_1cf 已全文独立核查。本稿不使用两个实正 first、整预解的有限阶或辅助行的实性。新增对象是自然 $S=YZ^{-k}$ 的任意有界可逆完整部分，不是旧线性剪切归一化算子的有界部分。

## 1. 实际全柱假设与算子结论

取原模型中的两个复第一阶
$$
Z=z_*I+X_\zeta,\qquad Y=X_c,
\qquad \zeta,c\in\ell^2(\mathbb C).
$$
假设 $Z$ 空谱，记
$$
L=Z^{-1}\in\mathfrak C=A'.
$$
它有界、单射、拟幂零。所有 first、有限词和有界 $\mathfrak C$ 系数均使用 R186 的真实域。

设有限位集 $F_n$ 递增并穷尽全部物理位。记
$$
d_n=|F_n|,\qquad
\sigma_n=z_*+\sum_{j\in F_n}\zeta_j,\qquad
t_n=\sum_{j\in F_n}c_j,
$$
$$
g_n=\|\zeta_{F_n^c}\|_2+\|c_{F_n^c}\|_2.
$$
假设
$$
\boxed{
|\sigma_n|\to\infty,\qquad
\frac{\sum_{j\in F_n}(|\zeta_j|+|c_j|)}{|\sigma_n|}
\le C_0,\qquad
\frac{\sqrt{d_n}\,g_n}{|\sigma_n|}\to0.
}
\tag{1.1}
$$
只需这些条件沿同一递增子列成立。

固定整数 $k\ge2$，定义真实自然闭算子
$$
S=YL^k,\qquad
\operatorname{Dom}S=\{h:L^kh\in\operatorname{Dom}Y\}.
\tag{1.2}
$$

**定理 1。** 在任何固定有限放大中，不存在非零闭空间 $\mathcal M$，使
$$
\mathcal M\text{ 被全部对角 }\mathfrak C\text{ 保持},\qquad
\mathcal M\subseteq\operatorname{Dom}S,\qquad
S\mathcal M\subseteq\mathcal M,
$$
且其完整部分
$$
\boxed{J=S|_\mathcal M}
\tag{1.3}
$$
为有界可逆算子。

不要求 $J$ 有限谱；也不要求 $\mathcal M$ 被 $C$、$Z^*$ 或 $Y^*$ 保持。

## 2. 两个头及两个尾的全部实际混合词

省略 $n$。置
$$
H_\zeta=\sum_{j\in F}\zeta_j(V_j-I),\qquad
H_c=\sum_{j\in F}c_j(V_j-I),
$$
$$
Z_0=X_{\zeta\mathbf1_{F^c}},\qquad
Y_0=X_{c\mathbf1_{F^c}}.
$$
有限去项是完整域等式：
$$
Z=\sigma I+H_\zeta+Z_0,\qquad
Y=tI+H_c+Y_0.
\tag{2.1}
$$

记 $\mathcal D_\infty^\dagger$ 为 $Z^*,Y^*$ 以及这些有限去项尾的全部有限自然词共同域。R251 补集指数次数尺度和原 $C$ 共轭逐词运输给
$$
Q_FH\subseteq\mathcal D_\infty^\dagger,
\tag{2.2}
$$
其中 $Q_F$ 保留全部 $2^{|F|}$ 维选中 Walsh 头。所有下述有限迭代都先在此域上运算。

定义归一化的两个有界头和两个实际尾
$$
A=\frac{H_\zeta^*}{\overline\sigma},\qquad
B=\frac{H_c^*}{\overline\sigma},\qquad
T=\frac{Z_0^*}{\overline\sigma},\qquad
U=\frac{Y_0^*}{\overline\sigma}.
\tag{2.3}
$$
它们在共同深域上交换；$A,B$ 有界并保持该域。

### 2.1 混合头的四次进位界

由 (1.1)，对全部 $|w|=1$，
$$
A+wB=\sum_{j\in F}
\frac{\overline{\zeta_j}+w\overline{c_j}}{\overline\sigma}
(V_j^*-I)
$$
的系数绝对值总和一致有界。[R251 §2](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md) 的逐单项式实际进位给固定 $C_1\ge1$ 和 $\gamma_0>0$，使
$$
\|(A+wB)^h\|\le C_1^h
$$
对全部 $h$ 成立，且
$$
\|(A+wB)^h\|\le C_1^h e^{-\gamma_0h^4}
\quad(h\ge\max(2d,16)).
$$
对 $w$ 作有限多项式 Cauchy 系数提取，可得
$$
\boxed{
\|A^{h-j}B^j\|\le C_1^h
}
\tag{2.4}
$$
以及
$$
\boxed{
\|A^{h-j}B^j\|
\le C_1^h e^{-\gamma_0h^4}
\quad(h\ge\max(2d,16)).
}
\tag{2.5}
$$
实际还带有有利的 $\binom hj^{-1}$，这里只将它丢掉。阈值只依位数 $d$，不依最大物理位号。

### 2.2 混合尾的全柱界

R251 §3 的同一补集指数尺度对 $Z_0+wY_0$ 逐步付域。算子值 Cauchy 系数提取和共同共轭运输给固定模型常数 $C_2$，使
$$
\boxed{
\|T^{q-j}U^jQ_F\|
\le\left(C_2\frac g{|\sigma|}\sqrt q\right)^q
\quad(q\ge1,\ 0\le j\le q).
}
\tag{2.6}
$$
$q=0$ 按 $Q_F$ 解释。这是同一个全柱输入上的真实混合词估计，不是两个无界尾的作用范数相乘。

所有混合头可以移到最左端。由有界头保域及真实词交换，(2.4)—(2.6) 可同时用于任一
$A^{h_1}B^{h_2}T^{q_1}U^{q_2}Q_F$。

## 3. 固定次数多项式的全柱高次根趋零

取固定半径 $R_0<\infty$。仅在共同深域上定义
$$
\mathscr P_n(z)
=I-\left(\frac{Z^*}{\overline{\sigma_n}}\right)^k
+z\frac{Y^*}{\overline{\sigma_n}^{\,k}},
\qquad |z|\le R_0.
\tag{3.1}
$$
由 (2.1)—(2.3)，准确有
$$
\mathscr P_n(z)
=I-(I+A+T)^k+
z\overline{\sigma_n}^{\,1-k}
\left(\frac{\overline{t_n}}{\overline{\sigma_n}}I+B+U\right).
\tag{3.2}
$$
其常数项为
$$
\delta_n(z)=z\frac{\overline{t_n}}{\overline{\sigma_n}^{\,k}},
\qquad
\delta_n^*:=\sup_{|z|\le R_0}|\delta_n(z)|
\le C R_0|\sigma_n|^{1-k}\to0.
\tag{3.3}
$$
除此之外，(3.2) 是 $A,B,T,U$ 的次数介于1与 $k$ 之间的有限多项式，其系数绝对值总和一致有界于某个固定 $C_{k,R_0}$。

由 (1.1) 可选整数 $p_n\to\infty$，满足
$$
\frac{p_n}{d_n}\to\infty,\qquad
\epsilon_n:=C_2\frac{g_n}{|\sigma_n|}\sqrt{kp_n}\to0.
\tag{3.4}
$$
例如当 $g_n>0$ 时取
$$
\eta_n=\sqrt{d_n}g_n/|\sigma_n|,\qquad
p_n=\left\lceil d_n/\eta_n\right\rceil.
$$
若某个尾为零，可直接选择 $p_n/d_n\to\infty$；原不可和正主行的应用中所有 $g_n$ 均非零。

展开 $\mathscr P_n(z)^{p_n}$。记录一项使用了多少个常数因子，记为 $u$；其余头的总次数为 $h$，尾的总次数为 $q$。由于每个非常数单项式次数至少1、至多 $k$，
$$
h+q\ge p_n-u,\qquad h+q\le k(p_n-u).
\tag{3.5}
$$
把常数项 $\delta_n(z)$ 暂作一个标记变量；除显式 $\delta_n(z)^u$ 外，所有展开系数的绝对值总和最多为某个 $C_3^{p_n}$，一致于 $|z|\le R_0$。使用 (2.4)—(2.6) 后，固定常数的 $C_1^{h}$ 也可吸收到一个新的 $C_3^{p_n}$ 中。

把每项分为以下三类：

1. 若 $u\ge p_n/3$，则其常数部分至多
   $(\delta_n^*)^{p_n/3}$。
2. 若 $u<p_n/3$ 而 $h\ge p_n/3$，则 (3.4) 使充分大 $n$ 时
   $h\ge\max(2d_n,16)$。由 (2.5)，此项至多另带
   $\exp(-\gamma_0p_n^4/81)$。
3. 其余情况有 $u<p_n/3$、$h<p_n/3$，所以 (3.5) 迫
   $q>p_n/3$。因 $q\le kp_n$，(2.6) 给至多
   $\epsilon_n^{p_n/3}$。

充分大时 $\delta_n^*,\epsilon_n\le1$，未选中的有利因子均可丢掉。于是
$$
\sup_{|z|\le R_0}
\|\mathscr P_n(z)^{p_n}Q_{F_n}\|
\le C_3^{p_n}
\left[
(\delta_n^*)^{p_n/3}
+e^{-\gamma_0p_n^4/81}
+\epsilon_n^{p_n/3}
\right].
\tag{3.6}
$$
取 $p_n$ 次根，得到
$$
\boxed{
\sup_{|z|\le R_0}
\|\mathscr P_n(z)^{p_n}Q_{F_n}\|^{1/p_n}\to0.
}
\tag{3.7}
$$
这正是新需要的高次多项式全柱预算；旧线性三项式不被直接当作它的证明。

## 4. 可逆部分给原空间上的真实投影恒等式

反设存在定理1中的 $\mathcal M,J$。所有算子按其有限对角放大理解，记 $\Pi$ 为到 $\mathcal M$ 的正交投影。

$J$ 与限制在 $\mathcal M$ 上的 $L$ 及所有对角 $\mathfrak C$ 交换。这里不假设复 $Z$ 最大增生，故明确支付受限部分的稠密域：[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) 的共同强正则器 $R_t^N$ 在固定足够大的 $N$ 下满足 $R_t^N\to I$ 强，且全部所需 $Z^jR_t^N$ 均为有界 $\mathfrak C$ 元。它们保持 $\mathcal M$，所以 $R_t^N\mathcal M\subseteq\operatorname{Dom}(Z_\mathcal M)^k$；尤其 $L_\mathcal M$ 的像在 $\mathcal M$ 中稠密。对每个 $\lambda\in\mathbb C$，实际全空间预解 $(Z-\lambda)^{-1}=L(I-\lambda L)^{-1}\in\mathfrak C$ 保持 $\mathcal M$，并给受限部分的双侧逆。因此 $X=Z_\mathcal M$ 是稠定闭空谱算子，$L_\mathcal M=X^{-1}$。对每个
$x\in\operatorname{Dom}X^k$，
$$
Yx=JX^kx.
\tag{4.1}
$$
确实，$X^kx\in\mathcal M\subseteq\operatorname{Dom}S$，而
$S X^kx=YL^kX^kx=Yx$。

对任意 $h\in\mathcal M$，取 R186 同一共同正则器的足够深幂
$h_t\to h$，保持 $\mathcal M$ 并支付全部所需 first 词域。$J$ 与该正则器交换，故 $Jh_t\to Jh$ 且同样在深域中。

对 $f\in\mathcal D_\infty^\dagger$，(4.1) 和 $JX^k=X^kJ$ 给
$$
\langle h_t,Y^*f\rangle
=\langle Yh_t,f\rangle
=\langle JX^kh_t,f\rangle
=\langle Jh_t,(Z^*)^kf\rangle.
$$
取极限，得到
$$
\boxed{
\Pi Y^*f=J^*\Pi(Z^*)^kf
\qquad(f\in\mathcal D_\infty^\dagger).
}
\tag{4.2}
$$
这只在原 Hilbert 空间的已付伴随深域上配对。没有将 $J^*$ 宣称为环境某个通常伴随的限制。

## 5. Cauchy 系数回传排除可逆 $J$

固定 $n$，在同一深域中写
$$
A_n'=\left(\frac{Z^*}{\overline{\sigma_n}}\right)^k,\qquad
B_n'=\frac{Y^*}{\overline{\sigma_n}^{\,k}},\qquad
D_n'=I-A_n'.
$$
(4.2) 等价于
$$
\Pi B_n'=J^*\Pi A_n',
$$
所以
$$
\Pi=\Pi D_n'+(J^*)^{-1}\Pi B_n'.
\tag{5.1}
$$
$D_n',B_n'$ 交换并保持共同深域。对 (5.1) 逐次代入，所有输入域均由 (2.2) 支付，得到
$$
\boxed{
\Pi Q_{F_n}
=\sum_{q=0}^{p_n}\binom{p_n}{q}(J^*)^{-q}
\Pi(B_n')^q(D_n')^{p_n-q}Q_{F_n}.
}
\tag{5.2}
$$

取固定
$$
R_0>\|J^{-1}\|.
$$
算子值有限多项式
$$
\mathscr P_n(z)^{p_n}Q_{F_n}
=(D_n'+zB_n')^{p_n}Q_{F_n}
=\sum_{q=0}^{p_n}z^q C_{n,q}
$$
的 Cauchy 系数界给
$$
\|C_{n,q}\|
\le R_0^{-q}
\sup_{|z|=R_0}\|\mathscr P_n(z)^{p_n}Q_{F_n}\|.
$$
因此 (5.2) 得
$$
\boxed{
\|\Pi Q_{F_n}\|
\le
\frac{1}{1-\|J^{-1}\|/R_0}
\sup_{|z|=R_0}
\|\mathscr P_n(z)^{p_n}Q_{F_n}\|
\longrightarrow0.
}
\tag{5.3}
$$
最后一步由 (3.7)。因为 $Q_{F_n}\to I$ 强，(5.3) 迫 $\Pi=0$，矛盾。定理1得证。

关键是 Cauchy 系数把所有 $(J^*)^{-q}$ 的费用变成一个固定几何和；没有付随 $p_n$ 增长的粗二项式逆成本。

## 6. 正主行、复加权误差及任意复受控辅助

现回到具体可检验的系数范围。取
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
c\in\ell^2(\mathbb C),\quad |c_j|\le C_0a_j.
$$
原函数为
$$
u=u_*+\sum_j(a_j+d^0_j+e^0_j)\chi_j,\qquad
v=v_*+\sum_j(c_j+\gamma a_j+d^1_j+e^1_j)\chi_j,
\tag{6.1}
$$
其中 $d^\nu$ 为原 weighted 误差、$e^\nu\in\ell^1(\mathbb C)$。令
$$
\zeta=a+d^0,\qquad
Z=X_\zeta+\omega,\qquad Y=X_c.
$$
$Z$ 的真实空谱、有界逆和原 first 到 $Z,Y$ 的有界系数代换均已由复加权主行稿支付；这些步骤不要求 $c$ 实。

设正 $a$ 的非零下降重排为 $r_1\ge r_2\ge\cdots$，记
$$
S_n=\sum_{j\le n}r_j,\qquad G_n^2=\sum_{j>n}r_j^2.
$$
假设
$$
\boxed{
\liminf_{n\to\infty}\frac{nG_n^2}{S_n^2}=0.
}
\tag{6.2}
$$
取 $F_n$ 为最大 $n$ 个 $a$ 系数的原物理位，再并入前 $n$ 个物理位，沿 (6.2) 子列重新编号。令
$s_n^a=\sum_{F_n}a_j\ge S_n$，则 $d_n\le2n$。

加权 Cauchy–Schwarz 给
$$
\left|\sum_{F_n}d_j^0\right|,\ 
\sum_{F_n}|d_j^0|
\le K_0\sqrt{s_n^a}.
$$
故
$$
\sigma_n=\omega+\sum_{F_n}\zeta_j\sim s_n^a,\qquad
\frac{\sum_{F_n}(|\zeta_j|+|c_j|)}{|\sigma_n|}\le C.
$$
对尾，令
$$
K_{0,n}^2=\sum_{j\notin F_n,\ a_j>0}|d_j^0|^2/a_j.
$$
因为 $a_j\le r_{n+1}$ 于 $F_n^c$，
$$
\frac{d_n\|d^0_{F_n^c}\|_2^2}{(s_n^a)^2}
\le\frac{2nr_{n+1}K_{0,n}^2}{S_n^2}
\le\frac{2K_{0,n}^2}{S_n}\to0.
$$
原 $a$、$c$ 尾由 (6.2) 及 $|c|\le C_0a$ 控制。因此 (1.1) 的全部实际条件成立。

## 7. 原完整 Bell 的全部非零最高簇

令 $F(x,y)$ 关于 $y$ 首一、次数 $M$，满足
$$
i+kj\le kM,\qquad k\ge2,
$$
且最高符号
$$
H(s)=\sum_{i+kj=kM}[x^iy^j]F\,s^j
$$
满足 $H(0)\ne0$。

对 (6.1) 的原指定向量 $[F(u,v)-\lambda]^r e^w$，完整 Bell 归一仍为
$$
\widehat P(t,s)=H(s)^rI+tE(t,s),
\qquad \deg_sE<rM.
$$
同一单射正则器先将假想规范核向量送入自然 $S=YL^k$ 多项式核。由真实闭相伴图 $\Gamma$，得到有界
$J=S|_\Gamma$ 和
$$
H(J)^r=-L_\Gamma E[L_\Gamma](J).
$$
右侧拟幂零，故 $\sigma(J)\subseteq H^{-1}(0)$。因为 $H(0)\ne0$，这个有界 $J$ 本身就是单位。

这些域和有限谱步骤在[有限阶非零簇稿 §§4—5](R150-appendix-finite-order-resolvent-narrow-sectors-and-all-nonzero-leading-clusters.md)已逐项支付；它们本身没有使用有限阶或实辅助。这里直接应用定理1排除 $\Gamma$，不再使用那篇的窄扇形部分。

原完整 $C$ 自伴性和循环指数图核心最终给
$$
\boxed{
[F(u,v)-\lambda]^r e^w
\text{ 对全部 }\lambda,r,w\text{ 循环。}
}
\tag{7.1}
$$

例如任意复受控辅助 $|c_j|\le C/(j+1)$、调和正主行
$a_j=1/(j+1)$ 都满足 (6.2)。因此该范围内
$$
[(v-u^k)^m+u^{km-1}-\lambda]^r e^w
$$
的所有 $k\ge2,m>1,\lambda,r,w$ 都已覆盖，且无需固定复直线。

一般复辅助在 (6.2) 失败时仍未由本文处理。真正的零最高簇、非整数 Newton 斜率、原正常见证专属源预算以及普通复 Hilbert ISP 也保持开放。

# R576 — 原两个单 sigma 深补项与完整三线单位余域

日期：2026-11-14。**状态：已证明。**

本篇计算同一个原 $q_n\ell$ 的整个 $c\in p^m$、$d_0\in p^m$
补项，保原 carry 深度 $n$、全部七行右逆、$\kappa^{-n}$、
两个独立 Mellin 单位条件及其常数 log。两个完整正交框架给所有
$n,m\ge1$ 的准确双参数式。首层同时包含原 log 质量、一次位移行
和原 sigma 的第七矩，不能把最后一项删掉。

把这两个补项与 R571 的整个 $c,d_0$ 共同深项合并后，
原算术总行只剩一个新的未计算部分：
$c,d_0,u$ 同时为单位的完整混合测试。
它在 R553 的真实 Norm2 坐标中恰为三条线的单位域；
两个完整低度张量及全部 $C$ 伴随仍保留。
这不是把该余域或原 native 残差赋零。

## 1. 同一原来源与两个完整单深补项

沿用
[R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)、
[R553](R553-original-norm2-two-theta-source-and-mixed-unit-domain.md)、
[R566](R566-original-third-state-fourteen-core-and-native-complements.md)、
[R571](R571-original-common-deep-complement-and-two-sigma-tail.md)、
[R572](R572-original-c-splitting-and-simple-pole-unit.md)
的原普通射线、全部固定坏集与周期。本篇不新增射线。
记
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1.
\tag{1}
$$
把最后一个原输入 $d_0$ 简写为 $d$，其余原输入为
$(\xi_1,\xi_2,\xi_3,x,c,d)$。仍取
$$
\rho_0=-\nu_\sigma^{\otimes6}/84,\qquad
\mu_0=\mathcal P_C\rho_0
=\nu_4\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),
\quad \nu_4=-\mathcal P_C\nu_\sigma^{\otimes4}/84.
\tag{2}
$$
$\mathcal P_C$ 只操作前四输入。

为完整列出测试，置
$$
\begin{gathered}
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\quad
C=(\xi_1-\xi_3+x)/\delta,\\
H_1=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x,\quad
a=2+3\omega,\quad l=1+3\omega,\quad g=3-2\omega,\\
D=D_4+c+ad,\quad F=D+C,\quad E=D+14C,\quad
G=13H_1+gF,\\
A=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,\quad
Y=A+c+2d,\quad W=A+3\delta c+4d .
\end{gathered}
\tag{3}
$$
$Na=Nl=7$、$la=-7$。
$E,G,Y,W$ 全部与 $D$ 正交。

原三个 carry 仍为
$$
\zeta_j=\omega^{2j},\quad D_j=F-\zeta_jC,\quad E_j=F+13\zeta_jC,
\quad
\Gamma_{n,j}=\{C,F\ {\rm unit},\,D_j\in p^n\}.
$$
原测试准确为
$$
q_n=\frac1{3b\Omega^6}\sum_{j=0}^2
 1_{\Gamma_{n,j}}\widehat P_p(D_j/\kappa^n,E_j,G),
\qquad \widehat P_p=\mathcal R_pP_p ,
\tag{4}
$$
$$
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
          -1_{W\ {\rm unit}}\log\langle W\rangle\},\qquad a_n=q_n\ell .
\tag{5}
$$
$\widehat P_p$ 是 R536 的准确整齐次六次多项式，保所有
$(1+\lambda\kappa^j)^{-1}$ 和实际右逆。引入以下参数不会改变它。

定义两个**整个**原补项
$$
\boxed{
C_{c;n,m}=\int_{\{c\in p^m\}}a_n\,d\rho_0,\qquad
C_{d;n,m}=\int_{\{d\in p^m\}}a_n\,d\rho_0,\qquad n,m\ge1 .
}
\tag{6}
$$
这里不额外要求另一个 sigma 输入为单位，也不附加 $u$、$L$ cut。

## 2. 两个完整原框架及其绝对核心

### 2.1 c 侧的 odd13 与 even182

令
$$
T_c=D_4+ad,\qquad R_{182}=13c-T_c,\qquad D=T_c+c .
\tag{7}
$$
$T_c\perp c$，范数为 $13,1$；$D\perp R_{182}$，范数为 $14,182$。
定义四个共同伴随
$$
\begin{aligned}
C_c&=C+T_c/13,& H_c&=H_1+gT_c/13,\\
E_c&=14C_c,& G_c&=13H_c+gC_c,\\
Y_c&=Y-c+T_c/13,&
W_c&=W-3\delta c+3\delta T_c/13 .
\end{aligned}
\tag{8}
$$
它们全与 $T_c,c$ 正交。置 $e_c=c-T_c/13$，准确有
$$
\boxed{
E=E_c+e_c,\quad G=G_c+ge_c,\quad
Y=Y_c+e_c,\quad W=W_c+3\delta e_c .
}
\tag{9}
$$
整个六行框架 $(T_c,c,E_c,G_c,Y_c,W_c)$ 的行列式为
$$
\det=6188+1092\omega,\qquad
N\det=32726512=2^4\,7^2\,13^3\,19 .
\tag{10}
$$
四个伴随之间不必正交；它们不被当成独立测度。
将四个伴随都乘 $39$，得到完整整数框架。
三个纯 $C$ 共轭的全部行仍整，$T_c,c,D,R_{182}$ 的非零
mod $2$ 系数数目依次为
$$
(3,1,4,4),\quad(5,1,6,6),\quad(5,1,6,6).
\tag{11}
$$
所以两个奇轴和两个偶轴各自属于正确的 standard 半特征，
没有用边际来省略 gluing。

使用 [R370](R370-original-degree-five-core-and-common-infinite-six-phase-primes.md)
第3–5节的 odd 半特征 trace 规范及 R553 第3节的完整中心规范。
当前 ray 给 $g_\pi=\pi_0/\bar\pi_0\equiv1\bmod26$。
whole standard odd $\mathcal S_{13}$ 的 Heisenberg lift 因此恒等；
用真实非零锚 $\sigma((4+\omega)z)$ 与原 sigma 核定标，
实际核心为 $\beta$。

对 $N=182$，原 $g_\pi\equiv3\bmod4$、
$g_\pi\equiv1\bmod7,13$ 准确合成
$$
g_\pi\equiv183=1+182\pmod{364}.
\tag{12}
$$
在标准 even 的 canonical lift 中，这个整标量不改变 $X,Z$ 标签，
且其中心商
$$
(183^2-1)/182=184\in2\mathbf Z
$$
使完整 cocycle 也不变。故 whole 核只差一个标量。
$\gamma_7\gamma_{13}=11+6\omega$、范数 $91$，真实拉回
$\Theta((11+6\omega)z)\in\mathcal S_{182}$ 非零。
固定 CM 拉回与原普通核心严格交换，而原 $\Theta$ 核为 $\beta$，
所以 whole $\mathcal S_{182}$ 的实际核心也是 $\beta$。

这与已经支付的 whole $D_{14}$ 核、独立 sigma 核合起来，给
$$
\boxed{
\begin{aligned}
\mu_0|_{\{D\in p^n,R_{182}\in p^m\}}
 &=\beta^{n+m}(P_{D,\kappa^n}P_{R_{182},\kappa^m})_*\mu_0,\\
\mu_0|_{\{T_c\in p^n,c\in p^m\}}
 &=\beta^{n+m}(P_{T_c,\kappa^n}P_{c,\kappa^m})_*\mu_0 .
\end{aligned}}
\tag{13}
$$
两个矩形都保 (8) 的全部四个伴随。

### 2.2 d 侧的 odd7 与两个 even14

令
$$
T_d=D_4+c,\qquad z=ad,\qquad R_{14}'=T_d-z,\qquad D=T_d+z.
\tag{14}
$$
$T_d,z$ 正交且范数均为 $7$；$D,R_{14}'$ 正交且范数均为 $14$。
定义
$$
\begin{aligned}
C_d&=C+T_d/7,&H_d&=H_1+gT_d/7,\\
E_d&=14C_d,&G_d&=13H_d+gC_d,\\
Y_d&=Y-2d-(2l/7)T_d,&
W_d&=W-4d-(4l/7)T_d .
\end{aligned}
\tag{15}
$$
四个伴随全与 $T_d,z$ 正交。置 $e_d=z-T_d$，准确有
$$
\boxed{
E=E_d+e_d,\quad G=G_d+ge_d,\quad
Y=Y_d+(2/a)e_d,\quad W=W_d+(4/a)e_d .
}
\tag{16}
$$
整个框架 $(T_d,z,E_d,G_d,Y_d,W_d)$ 满足
$$
\det=43316+7644\omega=7(6188+1092\omega),\qquad
N\det=2^4\,7^4\,13^3\,19 .
\tag{17}
$$
把四个伴随乘 $21$ 后，三个纯 $C$ 共轭的完整框架均整；
$(T_d,z,D,R_{14}')$ 的奇因子计数仍正好是 (11)。

当前 $g_\pi\equiv1\bmod14$，whole odd $\mathcal S_7$ 用
$\sigma((3+\omega)z)$ 绝对定标为 $\beta$。
$R_{14}'$ 是 standard even14；
$g_\pi\equiv15\bmod28$ 的中心商为 $16$，故整个 lift 恒等，
真实 $\Theta((3+\omega)z)$ 锚给同一个 $\beta$。
独立 $z=ad$ 是原 sigma 的固定单位 CM 推前，也有同一核心。
因而
$$
\boxed{
\begin{aligned}
\mu_0|_{\{D\in p^n,R_{14}'\in p^m\}}
 &=\beta^{n+m}(P_{D,\kappa^n}P_{R_{14}',\kappa^m})_*\mu_0,\\
\mu_0|_{\{T_d\in p^n,z\in p^m\}}
 &=\beta^{n+m}(P_{T_d,\kappa^n}P_{z,\kappa^m})_*\mu_0 .
\end{aligned}}
\tag{18}
$$

以上 whole 身份逐个伴随系数成立。所有完整 frame 的分母、
行列式和固定 CM 锚在当前素位为单位。它们没有假设新轴的边际
非零就能控制所有隐藏坐标。

## 3. 两个完整双参数函数

对 $s\in p\mathcal O,t\in\mathcal O$，定义
$$
\begin{aligned}
\mathscr C_c(s,t)=\int_{\{E_c\ {\rm unit}\}}
&\widehat P_p(T_c+tc,\ E_c+s(tc-T_c/13),\
                       G_c+gs(tc-T_c/13))\\
{}\cdot d_p\{&
1_{Y_c\ {\rm unit}}\log\langle Y_c+s(tc-T_c/13)\rangle\\
&-1_{W_c\ {\rm unit}}\log\langle W_c+3\delta s(tc-T_c/13)\rangle\}\,d\mu_0 ,
\end{aligned}
\tag{19}
$$
$$
\begin{aligned}
\mathscr C_d(s,t)=\int_{\{E_d\ {\rm unit}\}}
&\widehat P_p(T_d+tz,\ E_d+s(tz-T_d),\
                       G_d+gs(tz-T_d))\\
{}\cdot d_p\{&
1_{Y_d\ {\rm unit}}\log\langle Y_d+(2/a)s(tz-T_d)\rangle\\
&-1_{W_d\ {\rm unit}}\log\langle W_d+(4/a)s(tz-T_d)\rangle\}\,d\mu_0 .
\end{aligned}
\tag{20}
$$
每个 log 只在它自己的显示单位条件下使用。
$Y_c,W_c$ 或 $Y_d,W_d$ 不被假定同时为单位。
位移在 $p\mathcal O$，所以这些条件与移动后真实条件准确相同。

**定理1（全部单深补项）。** 对所有 $n,m\ge1$，置
$$
s_{n,m}=\kappa^{\min(n,m)},\qquad
t_{n,m}=\kappa^{(m-n)_+}.
$$
则
$$
\boxed{
C_{c;n,m}=\frac{\beta^{n+m}}{b\Omega^6}
 \mathscr C_c(s_{n,m},t_{n,m}),\qquad
C_{d;n,m}=\frac{\beta^{n+m}}{b\Omega^6}
 \mathscr C_d(s_{n,m},t_{n,m}) .
}
\tag{21}
$$

**证明。** 原纯 $C$ 三分支平均在 (6) 上准确变成单支：
$$
\frac1{b\Omega^6}
\int_{\{D\in p^n,E\ {\rm unit},\ c\ {\rm 或}\ d\in p^m\}}
\widehat P_p(D/\kappa^n,E,G)\ell\,d\mu_0 .
\tag{22}
$$
这里 $c,d,Y,W$ 由纯 $C$ 旋转固定，而 $\mu_0$ 对该旋转不变；
原 $C,F$ 单位与 $D$ 深、$E$ 单位等价。没有删去 carry 指示。

若 $m\le n$，在 $D\in p^n$ 内，$c\in p^m$
当且仅当 $R_{182}=14c-D\in p^m$。
应用 (13) 第一式。$D/\kappa^n$ 回到 $D=T_c+c$，
$e_c=R_{182}/13$ 乘 $\kappa^m$，四个伴随不动。
得到 (19) 的 $(s,t)=(\kappa^m,1)$。
同样，$d\in p^m$ 当且仅当
$R_{14}'=D-2z\in p^m$；用 (18) 第一式得到 (20) 的同一参数。

若 $m\ge n$，在 $c\in p^m$ 内，$D\in p^n$
当且仅当 $T_c\in p^n$。应用 (13) 第二式：
$D/\kappa^n$ 变成 $T_c+\kappa^{m-n}c$，
$e_c$ 变成 $\kappa^n(\kappa^{m-n}c-T_c/13)$。
同理 (18) 第二式给 $T_d+\kappa^{m-n}z$ 和
$\kappa^n(\kappa^{m-n}z-T_d)$。
其余四个伴随固定；外部标量都是 $\beta^{n+m}$。
两种范围在 $m=n$ 完全一致。这支付 (21) 的全部真实域和测试。证毕。

## 4. 完整首层：常数 log、位移行及第七 sigma 矩

先定义两条五输入测度
$$
\nu_5^{(c)}=\nu_4\otimes\nu_\sigma(d),\qquad
\nu_5^{(d)}=\nu_4\otimes\nu_\sigma(c).
\tag{23}
$$
它们仍是同一原四输入来源加一个原 sigma。
$T_c,E_c,G_c,Y_c,W_c$ 不含原 $c$，
$T_d,E_d,G_d,Y_d,W_d$ 不含原 $d$，所以以下积分次序合法。

把 $P=\widehat P_p(T_c,E_c,G_c)$、
$Q=(\partial_2+g\partial_3)\widehat P_p(T_c,E_c,G_c)$，
并记 $a_6=[D^6]\widehat P_p$。$a_6$ 保原完整 $p$ 依赖，
不是一个预先固定的代数常数。
令
$$
\ell_{c,0}=d_p\{1_{Y_c\ {\rm unit}}\log\langle Y_c\rangle
 -1_{W_c\ {\rm unit}}\log\langle W_c\rangle\},
$$
$$
\ell_{c,1}=d_p\{1_{Y_c\ {\rm unit}}/Y_c
 -3\delta\,1_{W_c\ {\rm unit}}/W_c\}.
$$
在 $\{E_c\ {\rm unit}\}$ 上定义
$$
\boxed{
\begin{aligned}
L_{c,0}&=\Omega\int P_D\ell_{c,0}\,d\nu_5^{(c)},\\
L_{c,1}&=\Omega\int\{(Q-\tfrac{T_c}{13}Q_D)\ell_{c,0}
 +(P-\tfrac{T_c}{13}P_D)\ell_{c,1}\}\,d\nu_5^{(c)},\\
L_{c,7}&=24b\Omega^7a_6\int\ell_{c,1}\,d\nu_5^{(c)} .
\end{aligned}}
\tag{24}
$$
这里 $L_{c,0}\in p\mathcal O$，后两行在 $\mathcal O$；
没有理由将第一行的原 log 质量删掉。

对 d 侧，把 $P,Q$ 改为在 $(T_d,E_d,G_d)$ 取值，置
$$
\ell_{d,0}=d_p\{1_{Y_d\ {\rm unit}}\log\langle Y_d\rangle
 -1_{W_d\ {\rm unit}}\log\langle W_d\rangle\},
$$
$$
\ell_{d,1}=d_p\{(2/a)1_{Y_d\ {\rm unit}}/Y_d
 -(4/a)1_{W_d\ {\rm unit}}/W_d\}.
$$
在 $\{E_d\ {\rm unit}\}$ 上定义
$$
\boxed{
\begin{aligned}
L_{d,0}&=a\Omega\int P_D\ell_{d,0}\,d\nu_5^{(d)},\\
L_{d,1}&=a\Omega\int\{(Q-T_dQ_D)\ell_{d,0}
 +(P-T_dP_D)\ell_{d,1}\}\,d\nu_5^{(d)},\\
L_{d,7}&=24ba^7\Omega^7a_6\int\ell_{d,1}\,d\nu_5^{(d)} .
\end{aligned}}
\tag{25}
$$
$L_{d,0}\in p\mathcal O$。$a^7$ 是原物理输入 $z=ad$ 的七次矩
因子，不能改成 $a$。

**定理2（准确首层和统一尾）。** 对 $\alpha=c,d$，
$$
\boxed{
\mathscr C_\alpha(s,t)
=tL_{\alpha,0}+stL_{\alpha,1}+st^7L_{\alpha,7}
+s^2t\,R_\alpha(s,t),\qquad R_\alpha(s,t)\in\mathcal O
}
\tag{26}
$$
于全部 $s\in p\mathcal O,t\in\mathcal O$ 的实际取值成立。
不声称除掉收敛权后的形式 log 系数一开始就整。

**证明。** 原 sigma 矩为
$$
m_0=0,\quad m_1=\Omega,\quad m_2=\cdots=m_6=0,\quad
m_7=24b\Omega^7.
$$
对任意 $\deg P\le6$，逐项精确有
$$
\int P(T+tc)\,d\nu_\sigma(c)=t\Omega P'(T),
$$
$$
\int(tc-rT)P(T+tc)\,d\nu_\sigma(c)
=t\Omega\{P(T)-rTP'(T)\}
 +24b\Omega^7t^7[D^6]P .
\tag{27}
$$
若 $\deg Q\le5$，第二式的第七矩项为零。
取 $r=1/13$，先展开 (19) 的多项式与两个独立 log，
其零阶、一次多项式位移及一次 log 位移分别给 (24) 三行。
$d$ 侧取 $r=1$ 并用
$m_z(1)=a\Omega$、$m_z(7)=24ba^7\Omega^7$，得 (25)。

所有更高项中，原被积分的 sigma 变量每出现一次均带 $t$；
它的零质量使无该变量的项消失。因此全部尾含 $t$。
二阶及以上的 log 项唯一可能的分母为其次数 $r$，
而 $s^{r-2}/r$ 在 $p\ge71$、$v_p(s)\ge1$ 下整；
加上有限多项式只增加非负 $s$ 次数。
由有界测度和一致收敛逐项积分，得到 $s^2t\mathcal O$。
这证明 (26)。证毕。

特别对每个 $n\ge1$，
$$
\boxed{
C_{\alpha;n,1}
=\frac{\beta^{n+1}}{b\Omega^6}
\{L_{\alpha,0}+\kappa(L_{\alpha,1}+L_{\alpha,7})
 +p^2\mathcal O\}.
}
\tag{28}
$$
其 $\beta^{-n}$ 倍事实上由 (21) 准确与 $n$ 无关，
不是仅模 $p^2$ 相同。
一般 $m$ 时 (21)、(26) 给
$v_p(C_{\alpha;n,m})\ge1+(m-n)_+$，
故固定 $n$ 后 $m\to\infty$ 的真正尾部趋零。
整个环带就是 $C_{\alpha;n,m}-C_{\alpha;n,m+1}$；
没有用一个不同的未归一测试代替它。

## 5. 原全部算术总行的准确分区

保
$$
\eta=\omega^2\mathsf H_*\rho_0,\quad h=\eta+\rho_0/2,\quad
\Delta=\rho_0-\eta,\qquad \Delta-R_{c,*}\Delta=3\rho_0,
$$
其中 $R_c$ 为原 $c$ 符号反射，$\mathsf H$ 为 R553 原两输入矩阵。
再置
$$
u=\{\omega c+(1-\omega)d\}/2,\qquad L=lc+d .
$$
R571 的完整恒等式为
$$
3\beta^n(J'_S-6\delta J'_T)=\mathcal N_n+U_n+3I_{n,1},
\tag{29}
$$
其中
$$
\mathcal N_n=\int_{\{u\in p,L\ {\rm unit}\}}
(a_n-a_n\circ R_c)\,d\Delta,\quad
U_n=\int_{\{u\ {\rm unit}\}}(a_n-a_n\circ R_c)\,d\Delta,
$$
$$
I_{n,1}=\int_{\{c,d\in p\}}a_n\,d\rho_0 .
$$
定义现在唯一保留的单位余域
$$
\boxed{
U_n^{\times,\times}
=\int_{\{c,d,u\ {\rm unit}\}}(a_n-a_n\circ R_c)\,d\Delta .
}
\tag{30}
$$

在 $\{c\in p,d\ {\rm unit}\}$ 以及
$\{c\ {\rm unit},d\in p\}$ 上，$u$ 自动为单位。
两域分别由 $R_c$ 保持，所以真实换元给
$$
\int_B(a_n-a_n\circ R_c)\,d\Delta
=\int_Ba_n\,d(\Delta-R_{c,*}\Delta)
=3\int_Ba_n\,d\rho_0 .
$$
这适用于这两个完整域，不要求 $q_n\circ R_c=q_n$。
因此准确有
$$
\boxed{
U_n=U_n^{\times,\times}
 +3\{C_{c;n,1}+C_{d;n,1}-2I_{n,1}\},
}
\tag{31}
$$
$$
\boxed{
3\beta^n(J'_S-6\delta J'_T)
=\mathcal N_n+U_n^{\times,\times}
 +3\{C_{c;n,1}+C_{d;n,1}-I_{n,1}\}.
}
\tag{32}
$$
共同深项的系数在 (32) 为负，来自完整包含排除；
不能再次把它认成一个已删去的零质量项。

为给原首层的实际比较，令
$$
L_0=L_{c,0}+L_{d,0},\qquad
L_1=L_{c,1}+L_{c,7}+L_{d,1}+L_{d,7}.
$$
R567 的 $C_0\in p\mathcal O,C_1\in\mathcal O$ 与 R571 的
原四 sigma 条件积分 $K_1$ 保持其原定义。由 (28)、(32) 得
$$
\boxed{
\begin{aligned}
\frac{3b\Omega^6}{p}(J'_S-6\delta J'_T)
\equiv{}&
\beta(C_0/p+\lambda^2C_1)
+3\beta(L_0/p+\lambda^2L_1)\\
&-3\lambda^4K_1
+\frac{b\Omega^6}{p\beta^n}U_n^{\times,\times}
\pmod p .
\end{aligned}}
\tag{33}
$$
每一个除以 $p$ 的原 log 行都已证明属于 $p\mathcal O$。
$K_1$ 仍带完整 $E_*,A_*$ 单位条件，不被换成独立单位见证。
由 (21)、R566 和 R571 的准确全深公式，
$\beta^{-n}U_n^{\times,\times}$ 对全部 $n\ge1$ 准确相同；
单纯增加 $n$ 不产生另一条独立的算术零式。

## 6. 唯一余域的真实 Norm2 两张量

用 R553 的原实际坐标
$$
U=c+\omega d,\quad V=c-\omega d,\qquad
c=(U+V)/2,\quad d=\omega^2(U-V)/2 .
\tag{34}
$$
原 $u$ 准确为 $-(U+\omega^2V)/2$，所以 (30) 的域恰为
$$
\boxed{
U+V,\quad U-V,\quad U+\omega^2V\quad\text{全部为单位}.
}
\tag{35}
$$
它不是 $\{U,V\ {\rm unit}\}$，也没有额外的 $L$ 单位条件。
原 $L=\omega U+\delta V$ 在此仍可能深。
$R_c$ 准确作用为 $(U,V)\mapsto(-V,-U)$，
其对 $a_n$ 的整个转置须保在 (30) 内。

令 $\Sigma=\sigma^2,\Theta=x_\wp\sigma^2$。将原 $-1/84$ 保在
$\nu_4$ 中后，末两原输入的整个来源分别为
$$
\rho_{\rm pair}=\omega(\Sigma_U\Theta_V-\Theta_U\Sigma_V),\qquad
\eta_{\rm pair}=\Sigma_U\Theta_V-\omega^2\Theta_U\Sigma_V .
$$
因此
$$
\boxed{
\Delta_{\rm pair}
=-\delta\{\Theta_U\Sigma_V+\omega^2\Sigma_U\Theta_V\}.
}
\tag{36}
$$
这是整个两变量恒等式，且两轴 entire $S_2$ 的实际核心均为
$\beta$。它不支付任何额外混合方向的 whole 核。

为不把四个共享输入缩成质量，保 R572 的
$$
v=\delta C=\xi_1-\xi_3+x,\quad
Z=\xi_1-\xi_3-2x,\quad Q=\xi_1+\xi_3,\quad r=\xi_2 .
$$
记 $P_3=\sigma^3,B=-y_\wp\sigma^3$ 和 R572 的完整
$f_1,f_3,f_4,\mathcal H_6$。原四维来源准确为
$$
\nu_4=\nu_B(v)\otimes\Theta_B+\nu_{P_3}(v)\otimes\Theta_P,
$$
$$
\boxed{
\begin{aligned}
\Theta_B&=\frac1{42}
(\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
 -\nu_{f_3}(Z)\otimes\nu_\Theta(Q))\otimes\nu_\sigma(r),\\
\Theta_P&=\frac1{84}
(\nu_{\mathcal H_6}(Z)\otimes\nu_\Theta(Q)
 -6b\nu_{f_4}(Z)\otimes\nu_\Sigma(Q))\otimes\nu_\sigma(r).
\end{aligned}}
\tag{37}
$$
于是 (30) 可在整个六维
$(v,Z,Q,r,U,V)$ 上，用
$$
(\nu_B\otimes\Theta_B+\nu_{P_3}\otimes\Theta_P)
 \otimes\Delta_{\rm pair}
\tag{38}
$$
准确计算。纯 $C$ 投影与原 pair 操作交换。
$P_3$ 项的质量零不允许把它从这个混合 cut 中删掉。

实际旧观察在 (38) 上是
$$
A_0=\frac{-2+\omega}{2}Z+\frac{4+3\omega}{2}Q+2\delta r,\qquad
J_0=\frac{\delta}{6}Z+\frac{1-2\omega}{2}Q+\omega^2r,
$$
$$
\boxed{
\begin{aligned}
F&=J_0+(1-\omega)U+\omega V,\\
Y&=A_0-\delta U/2+(3+2\omega)V/2,\\
W&=A_0+(-1+2\omega)U/2+(7+10\omega)V/2,\\
C&=v/\delta,\qquad
H_1=\omega^2Z/2+(\omega-1)Q/2+2r,\quad G=13H_1+gF .
\end{aligned}}
\tag{39}
$$
(4) 的全部 $D_j/\kappa^n,E_j$ 及 (5) 的两单位 log
均按这些行和 $R_c$ 转置。
所以 (35)–(39) 是同一原余域的完整低度表达，
没有用自由伴随积分代替它，也没有把 (32) 的原算术行改名为一个
辅助正矩或负矩。

## 7. 当前结论的范围与证书

本篇新增 (13)、(18) 的真实完整矩形，
(21) 的两个整个单深补项，
(24)–(28) 保原 log 质量和第七矩的准确首层，
以及 (32)、(35)–(39) 对剩余混合单位部分的完整定位。
这些与 R572 (29) 的原测试比较共用同一个 $q_n\ell$；
其中原 $c$ 深支已由 (21) 直接支付。

尚须控制的是 (32) 中保留下来的真实三线单位行，
连同已经明确的 native 与共同深项之比较。
本篇未将原负二、负五矩赋非零，
也未由单个非零区域推出原完整中央非零；主目标仍未完成。

- [精确 JS](../scripts/check-r576-original-single-sigma-complements-and-three-line-domain.js)
- [完整系数证书](../scripts/check-r576-original-single-sigma-complements-and-three-line-domain.json)

证书以 BigInt 的 $\mathbf Q(\omega)$ 运算核定两个完整六行框架、
全部三个纯 $C$ 共轭、整数半特征、Gram、行列式、实际正交投影、
中心模数及绝对锚的度数。它还逐次数核定整个六次多项式上的
(27)，包括 $a^7$ 第七矩，以及 Norm2 的完整来源和原观察行。
所有无穷深度、log 收敛和全域分区由正文直接证明，不用有限素数
样本或边际质量替代。

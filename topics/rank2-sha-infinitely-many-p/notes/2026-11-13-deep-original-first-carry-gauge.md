# 原 q=2 首次障碍的低阶 theta 规范式与第三层径向余差

日期：2026-11-13。**状态：下述有限环同构、原模 p² 规范式与第三层余差均已证明。** 本篇继续 R242，把原首次障碍实际还原到非共振的低阶 theta 系数。原源始终是同一个 $E_d=\mathbf Z_p[A,C]_{\le d}$，不另添偏导列，不对各齐次块分别选择目标变换。

## 1. 同一个 q=2 目标环

取 $p=4r-1\ge19$，$k=2r+s$、$0\le s<r$，并记 $a=17pu_0\in O^\times$。在这个第一带前缀内，$e_n=\lfloor n/r\rfloor$。R233 的原加权目标环在任意精度 $N$ 有明确表示
$$
T_N=L_k/p^NL_k\simeq
(O/p^N)[w,z]/(w^r-pz,\ z^3,\ w^sz^2),
\qquad z=p^{-1}w^r.
\tag{1}
$$
当 $s=0$ 时第三个关系就是 $z^2=0$。一组自由基是
$$
w^l,\ zw^l\quad(0\le l<r),\qquad
z^2w^l\quad(0\le l<s).
$$
这些元素分别映到原基 $p^{-h}w^{rh+l}$；乘法的进位正是 $w^r=pz$，终端截断给另外两个关系。因此 (1) 保留完整原行，没有在模 $p$ 之后擅自恢复被进位删除的信息。

对任意整轴 $f,c$，用原准确第一带式定义 $J_f$。R199 在 (1) 中等价于
$$
J_f(P)=P\bigl(e_2(az)f(w),\ e_2(az)c(w)\bigr),
\qquad e_2(t)=1+t+t^2/2.
\tag{2}
$$
这里 $z^3=0$，$2!$ 可逆；(2) 在所有 $N$ 都准确成立。后文的轴比较均使用同一个 $a$、同一个 $k$ 和同一个有限次数源。

## 2. 整径向轴变换对第一次提升完全不可见

取任意 $U(w)\in O[[w]]$，只读取前缀实际需要的有限项，令
$$
(f_U,c_U)=e^{w^rU(w)}(f,c).
\tag{3}
$$
在当前窗口，(3) 的指数只用到次数二，故整性没有阶乘损失。

**定理 1。** 在 $T_2$ 上存在同一个目标环自同构
$$
\sigma_U(w)=w,\qquad
\sigma_U(z)=z\left(1+\frac p a U(w)\right),
\qquad \sigma_U\equiv1\pmod p,
\tag{4}
$$
使得在整个 $E_d$ 上
$$
\boxed{\quad J_{f_U}=\sigma_U J_f\pmod{p^2}.\quad}
\tag{5}
$$

**证明。** (4) 把 $w^r-pz$ 改变为
$-p^2zU/a$，在 $T_2$ 中为零；另外两个截断关系乘上单位，仍为零。逆映射为 $w\mapsto w,z\mapsto z(1-pU/a)$。由 (2) 与 $w^r=pz$，
$$
\sigma_U(e_2(az)f(w))
=e_2(az+pzU(w))f(w)
=e_2(az)e^{w^rU(w)}f(w).
$$
$c$ 同理，代入任意原多项式即得 (5)。$\square$

所以两个矩阵的完整原模 $p$、模 $p^2$ 核相同。更强的是，若 $\overline P$ 属于共同模 $p$ 核，则任何同一原整提升满足
$$
\overline{J_{f_U}(P)/p}=\overline{J_f(P)/p}\quad\text{于 }T_1.
\tag{6}
$$
因而 R233 的首次 Bockstein 和 R242 的缩小障碍 $\omega_F^{\mathrm{nor}}$ 都逐类相等。后者的共同分母仍为原有限次数像
$S_F=j(FE_{d-e})$，没有放大为 $j(F)T_1$。

这不是给每个次数 $m$ 另乘一个 $e^{-mw^rU}$；(4) 是对全部混合列同时使用的一个目标自同构。

## 3. 原首次障碍由非共振 theta jet 准确计算

令 $s=s(w)$ 为 R224 的原严格角参数，
$$
w=s\mathcal F(s)^4,\qquad
\mathcal F(s)=\sum_{n\ge0}
\frac{\binom{2n}{n}}{4^n(4n+1)}s^n.
$$
为免与余数 $s$ 混淆，本节在复合式中把这个角参数写成 $\xi(w)$。于是
$$
R(w)=\Pi(\xi(w)),\qquad S(w)=\mathcal Z(\xi(w)),
\qquad R=w+\cdots,\quad S=-22w+\cdots.
\tag{7}
$$
原 $\Pi,\mathcal Z$ 就是 R224 的固定有理函数。R215 的首角参数坏系数在 $R_p+1=r(p-1)+1$ 才出现，远在 $k<3r$ 之外，所以 (7) 所读的全部系数均整。

原整轴给一个实际单位
$$
Y_{\mathrm{ax}}(w)=f(w)/R(w),\qquad
c(w)=S(w)f(w),
\tag{8}
$$
等式只需读取当前有限前缀。因 $k<3r<p$，$\log Y_{\mathrm{ax}}$ 和它的指数在这整个前缀中只用到 $p$ 单位分母。写
$$
\log Y_{\mathrm{ax}}(w)=L_{<r}(w)+w^rU_1(w),
\qquad L_{<r}(w)=\sum_{1\le n<r}\ell_nw^n,
\qquad U_1\in O[[w]].
\tag{9}
$$
这里的 $\ell_n$ 正是原 $\log\vartheta^{68}$ 的实际有理系数：R199 去掉的非整指数项从 $w^r$ 才开始，不影响 $n<r$。

任选 $a_0\in O^\times$ 满足 $a_0\equiv a\pmod p$。定义一个完全明确的同源规范矩阵 $J_*$，其两生成像为
$$
\begin{aligned}
A_*(w)&=R(w)e^{L_{<r}(w)}e^{a_0w^r/p},\\
C_*(w)&=S(w)A_*(w).
\end{aligned}
\tag{10}
$$
所有系数都按原权 $p^{\lfloor n/r\rfloor}$ 整化，不能直接把 (10) 当作普通整级数。

**定理 2。** 对任意原有限次数 $d$，同一个 $k$ 上有
$$
\boxed{\quad
\ker(J\bmod p^2)=\ker(J_*\bmod p^2),
\quad
\beta_1(J)=\beta_1(J_*).
\quad}
\tag{11}
$$
在 R242 的范围，进一步有
$$
\boxed{\omega_F^{\mathrm{nor}}(J)
=\omega_F^{\mathrm{nor}}(J_*).}
\tag{12}
$$

**证明。** 原准确第一带给
$$
(A,C)=e^{(a/p)w^r}Y_{\mathrm{ax}}(R,RS).
$$
代入 (9)，把
$$
U=U_1+(a-a_0)/p\in O[[w]]
$$
合并为 (3)。对基础标量 $a_0$ 使用定理 1，即得全部结论。若选另一个 $a_0$，二者的差又是一个整常数径向变换，所以 (11)—(12) 不依赖这个选择。$\square$

因此首次实际障碍不读取 $\log Y_{\mathrm{ax}}$ 的 $w^r$ 及以后项，也不读取 $a$ 的下一位。它仍读取 **$\ell_1,\ldots,\ell_{r-1}$ 的真实模 $p^2$ 值**，以及 (7) 的原角系数；不能只给这些数选任意模 $p$ 提升。

这些低系数可由原 ODE
$$
4\xi(1-\xi)\Lambda''+(3-5\xi)\Lambda'=17,
\qquad\Lambda'(0)=17/3
$$
和原 $\xi(w)$ 直接计算。所用递推在此尚未遇到 $4n+3=p$ 的共振，故没有未知 Stokes 量。定理 2 把整个 $\omega_F^{\mathrm{nor}}$ 还原成这个确定的原低阶 Padé 提升系统；它本身尚未证明这个系统的核非零或某个障碍为单位。

R211 的 $\log h$ 强迫与共同 gauge 也都落在 (9) 的 $w^rU_1$ 中，所以首次障碍看不见它们的独立径向贡献。这里使用的是原实际 $U_1$ 的整分解，不把 R211 的某个模 $p$ 代表任意提升为整轴。

## 4. 到模 p³ 的参数修复及其实际剩余项

(4) 在 $T_3$ 上不再保持 $w^r=pz$。这个失败可以用一个合法的目标换参修复，但修复会改变实际轴的参数。

置
$$
v(w)=\left(1+\frac p a U(w)\right)^{1/r}\pmod{p^3},
\qquad \theta(w)=wv(w).
\tag{13}
$$
$r$ 为单位，二项式只需二阶，$2$ 亦可逆。定义
$$
\widetilde\sigma_U(w)=\theta(w),\qquad
\widetilde\sigma_U(z)=zv(w)^r
=z(1+pU(w)/a).
\tag{14}
$$
它准确保持 (1) 的所有关系：第一个关系整体乘 $v^r$，后两个也乘单位。模 $p$ 为恒等，故在有限自由 $O/p^3$ 模上可逆。若 $U(0)=0$，$\theta=w+O(w^2)$ 是严格参数；一般情形还包含一个 $1\bmod p$ 的单位线性缩放，不能把它误称为线性系数恰一。

令 $f^\flat=f\circ\theta^{-1}$、$c^\flat=c\circ\theta^{-1}$。同一 $E_d$ 上准确有
$$
\boxed{\quad J_{f_U}=
\widetilde\sigma_U J_{f^\flat}\pmod{p^3}.\quad}
\tag{15}
$$
证明只需将 (14) 代入 (2)：指数变为 $az+pzU$，而 $f^\flat(\theta(w))=f(w)$。这说明目标关系虽可修复，剩下的轴参数变化必须保留；并没有因此允许把源换成任意次数的形式函数。

例如它的第一项就是
$$
f^\flat=f-\frac p{ar}wU f'\pmod{p^2},
\qquad
c^\flat=c-\frac p{ar}wU c'\pmod{p^2}.
\tag{16}
$$
这是沿原轴的切向变化，通常不是一个共同径向倍数。原图作为形式曲线没有变，但原指数与角参数的配合变了。不能以图相同为由删去 (16) 对加权连续像的作用。

若需二阶，严格反演给
$$
\theta^{-1}(w)=w-\frac p{ar}wU
 +\frac{p^2}{a^2r^2}
 \left(\frac{r+1}{2}wU^2+w^2UU'\right)
 \pmod{p^3}.
\tag{17}
$$
所以这里的第三层余差也没有未记录的换参误差。

## 5. 第三层只由一个原 carry 映射记录

这一余差还可直接在原矩阵中表达，无须选择 (14)。由 (3) 及 $w^r=pz$，在整个 $E_d$ 上
$$
J_{f_U}(P)=J_f(P)+pzU\,J_f(\mathcal EP)
 +\frac{p^2z^2U^2}{2}J_f(\mathcal E^2P)
 \pmod{p^3}.
\tag{18}
$$
$\mathcal E=A\partial_A+C\partial_C$ 保持原次数。因此 (18) 没有使用新增或免费的源列。

记 $\Lambda_T=\{P:J_f(P)\in p^TL_k\}$，$\mathcal F_T$ 为其模 $p$ 影。对 $\overline P\in\mathcal F_1$，模 $p$ 的 $z\partial_z$ 作用于 (2)，给
$$
zj_f(\mathcal EP)=0,
\qquad z^2j_f(\mathcal E^2P)=0.
\tag{19}
$$
第二式也可逐块读出：$j_f(P)=0$ 已经令部分块的 $\mathcal E^2P$ 低角系数为零。

于是对 $\overline P\in\mathcal F_2$，任选实际 $P\in\Lambda_2$，可定义
$$
\boxed{\quad
\eta(\overline P)=
\overline{\frac{zJ_f(\mathcal EP)}p}\in T_1.
\quad}
\tag{20}
$$
这是一个良定义的线性映射。除法由 (19) 合法；若换提升，差为 $pQ$、$Q\in\Lambda_1$，(20) 的变化就是 $zj_f(\mathcal EQ)=0$。

两矩阵的 $\Lambda_2$ 和一次除幂像 $\mathcal V_1$ 都相同。把两份第二 Bockstein 放入共同环境商 $T_1/\mathcal V_1$，由 (18)—(20) 得
$$
\boxed{\quad
\beta_2^{,U}(\overline P)-\beta_2(\overline P)
=\overline U\,\eta(\overline P)\pmod{\mathcal V_1}.
\quad}
\tag{21}
$$
二次指数项在这里由 (19) 准确消失；没有把它提前从 (18) 中省略。

同一个 $\eta$ 也不随 (3) 改变：把 (18) 用于 $\mathcal EP$，再乘 $z/p$ 后模 $p$，额外项就是 $\overline U z^2j_f(\mathcal E^2P)=0$。而 $T_1$ 中 $w^r=0$，所以 (21) 只读取 $U$ 的前 $r$ 个角系数。特别，原轴 log 的 $w^{2r}$ 及以后项对第三层核仍无作用；$w^r$ 到 $w^{2r-1}$ 的真实余项则由同一个 (20) 准确记录。

(20) 还有可直接计算的原行公式。写
$$
g_j(w)=(\mathcal E^j\overline P)(f(w),c(w)).
$$
读取 $P\in\Lambda_2$ 的第一、第二块并消去各自的低角项，得到
$$
\begin{aligned}
\eta_{r+l}(\overline P)&=-a^{-1}[w^{r+l}]g_0,
&&0\le l<r,\\
\eta_{2r+l}(\overline P)&=-[w^{r+l}]g_1,
&&0\le l<s,\\
\eta_l(\overline P)&=0,&&0\le l<r.
\end{aligned}
\tag{22}
$$
具体地，$J_{r+l}(P)=a[w^l]\mathcal EP+p[w^{r+l}]P$，除以 $p$ 后模 $p$ 得第一式；第二块同理使用
$J_{2r+l}(P)=a^2[w^l]\mathcal E^2P/2+pa[w^{r+l}]\mathcal EP+p^2[w^{2r+l}]P$。

因此 p³ 修复之后剩下的正是一个有原有限源定义、可由 (22) 读取的 carry 类。(21) 不保证它消失，也不把目标乘数 $\overline U$ 解释为原低次多项式。要从这里得到新的深关系，仍须研究规范模型 (10) 的实际低次核及这个类在原 $\mathcal V_1$ 中的值。

依赖：R199 原准确第一带指数；R215 原角参数整性范围；R224 原径向 ODE 与有理角源；R233 原目标环及 Hensel 层；R242 原首次因子修正。R211 的实际 log 强迫仅用于说明规范式覆盖了原已知共振贡献；没有以辅助 theta 族替代原对象。

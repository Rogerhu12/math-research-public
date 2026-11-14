# 逐位对数变换的全部次数：精确快系数抵消与任意 $\ell^2$ 循环性

日期：2026-11-13（UTC）。作者：central_next（Astra-ISP-0c017065）。
状态：已证明。全部阶循环性与并行 [R270 第三附录](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) 重合，本文作为逐位恒等式和旧接口的独立记录；新增登记仅为 §7 的有限支撑充要零条件及准确首阶。普通 ISP 未完成。

本稿把精确二次共振 $u^2+2\sum_j a_j^2(\chi_j-1)$ 推广成一个明确的全次数族。
逐位对数变换使实际乘子的所有高阶修正都至少重复占据同一位两次，
所以每个固定阶修正落入 R270 第二附录的快类 $\mathcal G$。
随后使用旧 R152/R180 的快系数多项式定理。
这里的点态多项式含有指定辅助项，并非一般原始 $q(u)$。

## 1. 明确的点态多项式

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2(\mathbb C),
$$
$$
w=b_*+\sum_{j\ge0}b_j\chi_j,\qquad b\in\ell^2(\mathbb C).
$$
对每个 $n\ge2$，令
$$
S_n(y)=\sum_j a_j^n(\chi_j(y)-1).
\tag{1.1}
$$
因 $a$ 有界且 $\sum|a_j|^2<\infty$，
$$
\sum_j|a_j|^n
\le\|a\|_\infty^{\,n-2}\|a\|_2^2<\infty,
$$
故每个 $S_n$ 是有界连续函数，级数一致绝对收敛。

定义 $F_0=1$、$F_1=u$，并对 $p\ge2$ 定义有限 Taylor 系数
$$
\boxed{
F_p
=p![t^p]\exp\!\left(
tu+\sum_{n=2}^p\frac{2^{n-1}}n\,t^n S_n
\right).
}
\tag{1.2}
$$
右端只涉及有限个普通点态乘积。
最初几项是
$$
F_2=u^2+2S_2,
$$
$$
F_3=u^3+6uS_2+8S_3,
$$
$$
F_4=u^4+12u^2S_2+32uS_3+12S_2^2+48S_4.
\tag{1.3}
$$

对标量多项式 $q(z)=\sum_{p=0}^d q_pz^p$，置
$$
F_q=\sum_{p=0}^d q_pF_p.
\tag{1.4}
$$
不是把 $q$ 直接作用于 $u$；(1.2)--(1.4) 准确给出所有抵消项。

**主定理。** 对任意非零 $q$，
$$
\boxed{F_qe^w\ne0\quad\Longrightarrow\quad
F_qe^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.5}
$$
没有熵、排序、相位、物理排列或额外衰减条件。
若 $a$ 有无限支撑，则每个非零 $q$ 的输出自动非零。

可和有限支撑时的准确零输出条件在 §7 给出。

## 2. 真实倾斜 first 与逐位变量

记
$$
t_j=e^{-2b_j},\qquad
R_j=V(t_jN_j),\qquad
V(z)=(I-z)(I+z)^{-1},
$$
并令 $X=X_b$ 为原实际倾斜闭 first。
置
$$
Q_j=a_j(R_j-I).
\tag{2.1}
$$
各 $Q_j\in\mathcal A$，相互交换且对原 $C$ 对称。

固定 $b$ 后，真实 $N_j^2=\eta_jN_{j+1}$ 给高位有理逆一致界，
有限低位以各自准幂零预解式支付。
所以有固定 $C_b$ 使
$$
\|Q_j\|\le C_b|a_j|,\qquad
\sum_j\|Q_j\|^2<\infty.
\tag{2.2}
$$
不要求 $\sum_jQ_j$ 按范数收敛；
在 $a\notin\ell^1$ 时也不使用没有定义的总和 $\sum_j a_j$。

令 $X_0=X_u$ 为未倾斜 first。
准确有理差给
$$
R_j-V(N_j)
=-2(t_j-1)N_j
(I+t_jN_j)^{-1}(I+N_j)^{-1}.
$$
由 $|t_j-1|\le C_b'|b_j|$ 与 Cauchy--Schwarz，
$$
H_{a,b}=\sum_j a_j(R_j-V(N_j))\in\mathcal A
$$
按范数绝对收敛，且
$$
X=X_0+H_{a,b},\qquad
\operatorname{Dom}X^k=\operatorname{Dom}X_0^k.
\tag{2.3}
$$
每个固定 dyadic gauge 的 $H_{a,b}$ 差只是有限真解析和。
这正是 R180 §12.2 已付清的实际指数倾斜，
符合其无界快系数定理的全部假设。

## 3. 每个固定高阶修正都在 $\mathcal G$

对 $n\ge2$，定义
$$
K_n=(-1)^{n-1}(n-1)!\sum_jQ_j^n.
\tag{3.1}
$$
由 (2.2)，这个和按实际算子范数绝对收敛。

进一步，固定 $n$ 时逐位函数
$$
f_{j,n}(z)=a_j^n(V(t_jz)-1)^n
$$
在一个统一小圆盘上解析且一致有界；
常数项、一次项均为零。
R270 第二附录 §2 的局部二阶消去引理因此给
$$
\boxed{K_n\in\mathcal G\qquad(n\ge2).}
\tag{3.2}
$$
这里只对每个固定 $n$ 应用该引理。
即使 $n>2$，仍可使用已证的至少二阶重复占据界，
不需要新增任何无限和封闭性。

定义规范乘积
$$
C_N(t)=\prod_{j<N}e^{-tQ_j}(I+tQ_j).
\tag{3.3}
$$
对每个固定紧 $t$ 盘，
$$
\|e^{-tQ_j}(I+tQ_j)-I\|
\le C_R\|Q_j\|^2
$$
由局部 Taylor 展开及 (2.2) 得到。
因此 (3.3) 在每个紧盘上按算子范数一致收敛到整函数 $C(t)$。

在足够小的 $t$ 盘上可逐项取局部对数，并绝对交换求和：
$$
\log C(t)
=\sum_{n\ge2}\frac{K_n}{n!}t^n.
\tag{3.4}
$$
每个固定 Taylor 系数
$$
C_k=C^{(k)}(0)
$$
是有限个 $K_2,\ldots,K_k$ 的 Bell 多项式。
由 $\mathcal G$ 的有限加乘封闭，
$$
C_k\in\mathcal G,\qquad C_0=I,\quad C_1=0.
\tag{3.5}
$$
没有据此声称整个 $C(t)$ 都属于 $\mathcal G$；
一般范数极限并不自动保该类。

## 4. 点态对数变换的准确局部恒等式

取小 $t$，令
$$
h_j(t)=-\frac12\log(1-2ta_j)
=\sum_{n\ge1}\frac{2^{n-1}}n a_j^nt^n.
\tag{4.1}
$$
对任意有限截断，有限位倾斜的真实乘子恒等式为
$$
(\cosh h_j(t)I+R_j\sinh h_j(t))e^w
=e^{h_j(t)\chi_j}e^w
$$
与其他不同位因子的乘积相容。
利用 $z_j=t_jN_j$，有准确有理式
$$
\cosh h_j I+R_j\sinh h_j
=e^{h_j}(I+e^{-2h_j}z_j)(I+z_j)^{-1}.
$$
由于 $e^{-2h_j}=1-2ta_j$，遂得
$$
\boxed{
e^{-h_j(t)}(\cosh h_j(t)I+R_j\sinh h_j(t))
=I+tQ_j.
}
\tag{4.2}
$$
(4.2) 保留整个实际 $N_j$，没有使用 $N_j^2=0$。

令
$$
u_N=a_*+\sum_{j<N}a_j\chi_j,\qquad
X_N=a_*I+\sum_{j<N}a_jR_j.
$$
有限截断的点态指数可写为
$$
\mathcal F_N(t)
=\exp\!\left[
tu_N+\sum_{j<N}(\chi_j-1)(h_j(t)-ta_j)
\right].
\tag{4.3}
$$
反复用 (4.2) 得到完整有限位等式
$$
\boxed{
\mathcal F_N(t)e^w
=e^{tX_N}C_N(t)e^w.
}
\tag{4.4}
$$
这里有限 $N$ 时 $X_N$ 有界；所有乘积和指数均有通常意义。

## 5. 极限只取固定 jets，并使用完整自然域

对任意固定 $p$，
$$
\sum_j(\chi_j-1)(h_j(t)-ta_j)
$$
在足够小 $t$ 盘中按 $L^\infty$ 范数一致收敛，
因为逐位余项由 $C|t|^2|a_j|^2$ 控制。
其到 $p$ 阶的 Taylor 展开正是
$$
\sum_{n=2}^p\frac{2^{n-1}}n t^nS_n.
$$
Rademacher 的有限指数矩保证 $e^{tu+w}$ 在这些紧盘上属于 $H$，
并允许固定阶 $H$ 值求导。
也可将每个固定系数展开为有限个 $u^k$ 与有界 $S_n$ 的乘积，
由所有有限矩及 Cauchy--Schwarz 直接得到相同的 $H$ 极限。

右侧 $C_N^{(k)}(0)\to C_k$ 按范数收敛。
R176 的倾斜 first 全部自然幂及有限截断 Bell jets 给
$$
X_N^\ell e^w\longrightarrow X^\ell e^w,\qquad
e^w\in\bigcap_{\ell\ge0}\operatorname{Dom}X^\ell.
\tag{5.1}
$$
这一已有接口可直接从有限 Bell 恒等式逐阶读出：
普通点态 $u_N^\ell e^w$ 在 $H$ 中收敛，
固定阶原 Bell 累积量按范数收敛，
而 R176 的自然图识别给其极限为同一个实际 $X^\ell e^w$。

对 (4.4) 取第 $p$ 阶导数并使用这些有限 jets，得到
$$
\boxed{
F_pe^w
=\left[\sum_{k=0}^p\binom pk C_kX^{p-k}\right]e^w.
}
\tag{5.2}
$$
这不要求 $e^{tX}$ 在全 $H$ 上有界，
也不将它当作已构造的全空间半群。

对给定非零 $q$，令 $d=\deg q$，定义
$$
P_q(z)
=\exp\!\left(\sum_{n=2}^d\frac{K_n}{n!}\partial_z^n\right)q(z)
\in\mathcal G[z].
\tag{5.3}
$$
指数在有限多项式空间上截断。
由 (3.4)--(5.2)，
$$
\boxed{T_qe^w=F_qe^w,\qquad T_q=P_q(X).}
\tag{5.4}
$$
其最高系数是 $q_dI$，可逆。
R176 给闭自然域
$$
\operatorname{Dom}T_q=\operatorname{Dom}X^d
$$
及完整 $C$ 自伴性、指数向量图核心和
$$
[F_qe^w]_A=\overline{\operatorname{Ran}T_q}.
\tag{5.5}
$$
常数 $q$ 单独直接处理，或按 $d=0$ 理解。

例如
$$
K_2=-\sum_jQ_j^2,\qquad K_3=2\sum_jQ_j^3,
$$
所以
$$
T_2=X^2-\sum_jQ_j^2,
$$
$$
T_3=X^3-3X\sum_jQ_j^2+2\sum_jQ_j^3.
$$
第二式准确对应 (1.3) 的三次点态表达，而非未经验证的点乘同态。

## 6. 已有快系数多项式定理完成排核

若 $a\notin\ell^1$，(2.3) 使 $X$ 属于 R180 的真正无界方向加有界加性倾斜。
(5.3) 的全部系数在 $\mathcal G$，关于 $X$ 的最高系数可逆。
除以 $q_d$ 后，R180 定理1.2(1) 与 §9 的秩零结论给
$$
\ker T_q=0,\qquad
\overline{\operatorname{Ran}T_q}=H.
\tag{6.1}
$$
R183 的同一首一特例也可替代引用。
R180 的完整核自然幂域、有限快 Bézout 和限制稠密性都已先行证明，
因此这里没有把有界变量定理无证搬到无界 first。

若 $a\in\ell^1$，$X\in\mathcal A$，
且每个 dyadic gauge 差只是有限真解析和。
减去其字符后，R152 定理1.3/§7 给每个实际非零 $P_q(X)$
单射且值域稠密。
是否非零由 §7 完整判定。

由 (5.5)，这些结论证明 (1.5)。
无界分支还由 R171 的非零 UHF 最高系数障碍知 $T_q\ne0$；
若 $F_qe^w=0$，真实图核心会迫使 $T_q$ 为零，矛盾。
所以真正无界行上的非零输出自动成立。

## 7. 可和行的全部零输出与准确首阶

假设 $a\in\ell^1$，置
$$
s=a_*+\sum_j a_j,\qquad
L=\#\{j:a_j\ne0\}\in\mathbb N_0\cup\{\infty\}.
$$
此时 $\sum_jQ_j$ 按范数绝对收敛且 $X=sI+\sum_jQ_j$，
所以由 (3.3) 有真实局部等式
$$
e^{tX}C(t)
=e^{ts}\prod_j(I+tQ_j).
\tag{7.1}
$$
右侧乘积按范数在紧盘上一致收敛。
记 $e_r(Q)$ 为实际第 $r$ 个基本对称和，
$$
e_0(Q)=I,\qquad
e_r(Q)=\sum_{j_1<\cdots<j_r}Q_{j_1}\cdots Q_{j_r}.
$$
绝对收敛由
$$
\sum_{j_1<\cdots<j_r}\|Q_{j_1}\|\cdots\|Q_{j_r}\|
\le\frac1{r!}\left(\sum_j\|Q_j\|\right)^r
$$
保证。从 (7.1) 取有限 Taylor 系数得
$$
\boxed{
T_q=\sum_{r=0}^{\deg q}q^{(r)}(s)e_r(Q).
}
\tag{7.2}
$$

令 $\mu$ 为 $q$ 在 $s$ 的零点重数；若 $q(s)\ne0$，约定 $\mu=0$。
非零 $q$ 保证 $\mu<\infty$。
若 $L<\mu$，(7.2) 的全部非零可能项都消失，故 $T_q=0$。

若 $L\ge\mu$ 且 $\mu\ge1$，
记非零系数的最早 $\mu$ 个物理位为
$j_1<\cdots<j_\mu$。
$Q_j$ 的准确首阶为 $2^j$，首系数为 $-2a_jt_j/d_j$。
在 (7.2) 中最低阶唯一来自 $r=\mu$ 的这组位置：
$$
\boxed{
\operatorname{ord}T_q=\sum_{\ell=1}^{\mu}2^{j_\ell},
}
$$
$$
\boxed{
\gamma_{\sum_\ell2^{j_\ell}}(T_q)
=q^{(\mu)}(s)(-2)^\mu
\prod_{\ell=1}^{\mu}\frac{a_{j_\ell}t_{j_\ell}}{d_{j_\ell}}\ne0.
}
\tag{7.3}
$$
$r>\mu$ 的最小阶严格更高；同一个 $r=\mu$ 的其他位置组也严格更高。
所以 $T_q\ne0$。
若 $\mu=0$，$\chi(T_q)=q(s)\ne0$，$T_q$ 是单位。

由指数向量循环性，$T_qe^w=0$ 当且仅当 $T_q=0$。
因此得到完整判据
$$
\boxed{
F_qe^w=0
\iff L<\operatorname{mult}_s(q).
}
\tag{7.4}
$$
当 $L=\infty$ 时，右边对任何非零 $q$ 都不成立。
这补上主定理的无限支撑非零性。

对 $q(z)=z^p$，若 $s=0$，
$$
T_p=p!e_p(Q).
$$
所以支持至少 $p$ 个位置时循环，支持少于 $p$ 个位置时实际输出为零。
$s\ne0$ 时为单位情形。
$p=2$ 正好恢复精确二次共振的零输出例外。

## 8. 结论的准确位置

全次数族 (1.2) 及其循环范围已由并行 R270C 正式登记。本稿独立记录真正局部恒等式 (4.2)、全部快修正 (3.1)--(3.5) 和旧定理的完整自然域接口；本次补充为可和行的精确零输出与首阶判据。
排核使用旧 R152/R180 的已证快系数定理，
没有宣称新证明了该一般定理。

这些多项式包含与原主模式处处重叠的无限辅助 $S_2,\ldots,S_p$，
而系数处于精确共振大小。
其特殊逐位对数选择支付了所有同位抵消。
一般同阶辅助共振没有因此全部关闭；
也没有把未修正的 $q(u)$ 混合重根问题、多个独立无限慢方向、
正常湮灭者、实际边界缺陷或普通 ISP 宣告完成。

## 依赖

R152：有界加性方向的 $\mathcal G$ 系数多项式；
R176：真实倾斜 jets、首一自然域及图循环；
R180 §§7--9、12.2：无界方向的快系数秩零排核和任意 first 权；
R183：同一闭快系数多项式的替代接口；
R270 第二附录 §2：真实局部二阶消去属于 $\mathcal G$。

# R1056：原核行最低 CM 泛函的单系数公式

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o2_high_coefficient / root。

**已证明：对 R1048 的同一个原核多项式 $T_0$，实际最低 CM 泛函准确等于一个安全截断的 $q^3/j$ 系数。** 本篇保原核、实际参数和全部常数；不宣称该系数、核范数或指定 $DQ(1-Q)\lambda$ 最低值非零。

## 1. 固定范围和结论

使用 R1048 的原 $r=2$ 行
$$
p=12g-1\ge41,\quad p\equiv2,5\pmod9,\quad
N=2g-1,\quad \ell=(p+1)/3=2N+2.
$$
不以本篇扩张原 bare-norm 桥到另一行。置
$$
r=1-b^3,\quad A=bQ(b^3)=A_1bq(r),\quad A_1=A(1)\ne0,
$$
$$
\mathcal L=r\partial_b^2-4b^2\partial_b-\frac94b,\quad
\mathcal LA=0,\quad \mathcal LT_0=A,
$$
其中 $T_0\in\mathbf F_p[b^3]$、$\deg T_0=3N$、首系数 $-1$，与 R1048 完全相同。$q(0)=1$、$j(0)=1$，二者为 R1050 的原安全 period 系数；$q$ 是次数 $N$ 的多项式，$j$ 仅取次数小于 $\ell$。

令
$$
d=\ell-1,\quad k=\ell-2,\qquad
\mathcal C_{\rm CM}(T_0)
=[Z^d]\left(\frac{T_0}{A}\right)(B_{\rm CM}(Z)).
$$
这里 $d$ 只是系数次数，**不是** $\deg A$。原真实参数保持
$$
Z=-\frac r3(q/j)^3,\qquad b=B_{\rm CM}(Z).
$$
则
$$
\boxed{\qquad
\mathcal C_{\rm CM}(T_0)
=\frac{(-3)^{\ell-1}}2
 [r^{\ell-2}]\frac{q(r)^3}{j(r)}.
\qquad}
\tag{1056.1}
$$
右侧只需 $j$ 到次数 $\ell-2$，严格早于第一个坏分母。公式没有遗漏 $A_1$ 或原参数的一次尺度。

## 2. 原 Hasse 平方 primitive 给准确导数

R1048 的规范多项式
$$
H=r^{\ell+1}(AT_0'-T_0A')
$$
准确满足
$$
H_b'=h^2,\qquad h=r^{N+1}A.
\tag{1056.2}
$$
它在 $r=0$ 的值为零。换成同一实际局部 $r$ 参数，使用 $dr/db=-3b^2$ 与 $A=A_1bq$，得到
$$
H_r'=-\frac{A_1^2}{3}r^\ell q(r)^2.
\tag{1056.3}
$$
定义无任何积分常数歧义的多项式
$$
I(r)=r^{-\ell-1}\int_0^r t^\ell q(t)^2\,dt
=\sum_{n=0}^{k}
 \frac{[r^n]q(r)^2}{\ell+n+1}r^n.
\tag{1056.4}
$$
这里 $\deg q^2=2N=k$，所有分母位于
$\ell+1,\ldots,2\ell-1$，均严格小于 $p=3\ell-1$，所以是单位。$H(0)=0$ 保证
$$
H=-\frac{A_1^2}{3}r^{\ell+1}I(r).
\tag{1056.5}
$$

写 $F_0=T_0/A$。从原定义先对 $b$ 求导，再换到 $r$，有
$$
(F_0)'_b=\frac{H}{r^{\ell+1}A^2}
=-\frac{I}{3b^2q^2},
$$
$$
\boxed{\quad
(F_0)'_r=\frac{I(r)(1-r)^{-4/3}}{9q(r)^2}.
\quad}
\tag{1056.6}
$$
$A_1^2$ 在 (1056.5) 与 $A^2=A_1^2b^2q^2$ 中明确相消；原 $9$ 来自这两个实际坐标导数，不能省略。

## 3. 实际参数的 Lagrange 公式

因 $Z=-r(q/j)^3/3$ 的一次系数为 $-1/3$，而 $d<p$，合法的有限 Lagrange 反演给
$$
\mathcal C_{\rm CM}(T_0)
=\frac{(-3)^d}{9d}
 [r^k]I(r)(1-r)^{-4/3}q(r)^{-2}
       (j(r)/q(r))^{3d}.
\tag{1056.7}
$$
$F_0$ 的常数项不影响这个正次读数，没有通过另选原函数改变它。

准确 $3d=p-2$。在全部所需次数 $k<p$ 内，常数项一的 $\mathbf F_p$ 级数满足
$$(j/q)^p=1\pmod{r^p}.$$
所以 (1056.7) 严格化为
$$
\mathcal C_{\rm CM}(T_0)
=\frac{(-3)^d}{9d}
 [r^k]I(r)(1-r)^{-4/3}j(r)^{-2}.
\tag{1056.8}
$$
这里选择任意安全截断的延拓多项式都给同一结果，未将 $j$ 延伸为跨共振的特征 $p$ period。

## 4. Wronskian 逐项消掉全部积分分母

令 $u=q/j$。同一原 Wronskian 在所需范围给
$$
u+3ru'=(1-r)^{-4/3}j^{-2}.
\tag{1056.9}
$$
将 (1056.4) 和 (1056.9) 代入所需系数，逐项是
$$
[r^k]I(u+3ru')
=\sum_{n=0}^{k}
 \frac{[r^n]q^2}{\ell+n+1}
 \bigl(1+3(k-n)\bigr)[r^{k-n}]u.
\tag{1056.10}
$$
由于 $k=\ell-2$、$3\ell=p+1$，
$$
1+3(k-n)=-3(\ell+n+1)\quad\text{于 }\mathbf F_p.
$$
每个分母都是已经验证的单位，故所有项逐个约去，得到
$$
[r^k]I(1-r)^{-4/3}j^{-2}
=-3[r^k]q^2u=-3[r^k]q^3/j.
\tag{1056.11}
$$
最后 $3d=p-2=-2$ 于 $\mathbf F_p$，所以 (1056.8) 的总因子
$$
\frac{(-3)^d(-3)}{9d}=\frac{(-3)^d}{2},
$$
恰为 (1056.1)。

## 5. 原对象间已付与未付的关系

$T_0$ 是原 $Q_{\rm op}$ 核行的插值多项式。R1048 的规范核满足
$$
c_0(s)^p=T_0(s)A'(s)/f(s),
$$
故与 R1037 的 $T_c$ 约定一致，并非另取的一个同次数解。因此 (1056.1) 是这条原核行的**实际最低列读数**。

它与以下读数仍须区别：

- R1043 的原端点 $f_N=-T_0(1)/6$；
- R1048 的原 bare 核范数 $B(c_0,c_0)$；
- R1052 的实际指定消去行
  $\mathcal C_{\rm CM}(T_{DQ_{\rm op}(1-Q_{\rm op})\lambda})$。

本篇没有证明这些读数互相相等，也没有给其中任何一个的全 $p$ 单位性。特别地，不能用一个未支付的 log-系数等同或原函数相差“常数”来省掉真实 $p$ 次歧义及 Riccati 平方项。后继仍须沿实际源推进这些明确的指定值。

## 来源

- [R1048](R1048-original-AS-primitive-and-kernel-critical-value-norm.md)，原 $r=2$、$H'=h^2$、$T_0$ 与核的规范。
- [R1050](R1050-actual-CM-parameter-short-PD-and-Picard-Fuchs.md)，同一实际 CM 参数与全部安全分母。
- [R1052](R1052-original-complete-CM-profile-and-actual-lowest-functional.md) §§7–8，完整 CM 轮廓、实际最低泛函和 Wronskian。

o2_high_coefficient 给出逐项推导；root 独立核对 $H_r'$ 的负号、两个坐标因子、Lagrange 次数、全部分母区间和最终 $1/2$。本文为纸面证明，无数学程序执行，无旧窗口重算。主目标仍 OPEN。

## 6. 同一纯代数公式对两种临界列的推广

本节把**核行的列公式**扩到全部 $p=6N+5\ge41$，不扩张 R1048 的原 bare-norm 身份。R1043/R1040 给该范围内同一个唯一 $T_0$，满足 $\mathcal LT_0=A$。不必借用带 $r=2$ 限制的 AS 源，直接作代数消元即得
$$
\begin{aligned}
H_b'
&=r^\ell\{r(AT_0''-T_0A'')
 -3(\ell+1)b^2(AT_0'-T_0A')\}\\
&=r^\ell\{A^2+(4-3(\ell+1))b^2(AT_0'-T_0A')\}
=r^\ell A^2=h^2 .
\end{aligned}
$$
最后用 $3\ell=p+1$。因此 §2 的 $I$ 及准确导数 (1056.6) 在全范围成立。

取 $s\in\{2,8\}$，写
$$
d_s=(p-s)/3,\qquad
C_s=[Z^{d_s}](T_0/A)(B_{\rm CM}(Z)).
$$
此处 $s$ 是标号，非 CM 根或原范数。则
$$
\boxed{\quad
C_s=\frac{(-3)^{d_s}}{s(s-1)}
 [r^{d_s-1}]\frac{q^{s+1}}{j^{s-1}}.
\quad}
\tag{1056.12}
$$
特别地，$s=8$ 给
$$
[Z^{\ell-3}](T_0/A)(B_{\rm CM}(Z))
=\frac{(-3)^{\ell-3}}{56}
 [r^{\ell-4}]q^9/j^7.
$$

证明保留 §3 的同一 Lagrange 过程。令 $u=q/j$、$W=(1-r)^{-4/3}q^{-2}$。因为 $3d_s=p-s$，所需系数严格在 $p$ 以下，
$$
C_s=\frac{(-3)^{d_s}}{9d_s}
 [r^{d_s-1}]I W u^s.
$$
原 Wronskian 是 $u+3ru'=Wu^2$，所以
$$
Wu^s=u^{s-1}+\frac{3r}{s-1}(u^{s-1})'.
$$
卷积中与 $I_n=[r^n]q^2/(\ell+n+1)$ 配对的因子为
$$
1+\frac{3(d_s-1-n)}{s-1}
=-\frac{3(\ell+n+1)}{s-1}\quad\text{于 }\mathbf F_p.
$$
逐项消去原已付分母，再用 $3d_s=-s$，便得 (1056.12)。全部 $s(s-1)$、$d_s$ 及被使用的 $\ell+n+1$ 都是单位，且 $j$ 的最高使用次数仍小于 $\ell$。

这两条都是原核 $T_0$ 的实际轮廓列。即便它们的次数与两行 bare 临界次数相同，也没有因此把该核列等同于原 bare 系数或实际 $DQ(1-Q)\lambda$ 行。本文仍未证明这些系数非零。此推广由 o2_high_coefficient 给出，root 独立核全 $H'$、Lagrange 幂和卷积因子；无数学执行。

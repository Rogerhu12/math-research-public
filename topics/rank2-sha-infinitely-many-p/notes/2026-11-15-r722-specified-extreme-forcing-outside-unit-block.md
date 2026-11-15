# R722 增补：极端 carry 的指定目标确实退出这个原单位块

日期：2026-11-15。**状态：下述指定子像中的非零已证明；整个 $\mathcal W_D$ 的像问题仍开。**

本增补把 R722 的真实单位块用于
[极端 carry 的完整短行](2026-11-15-extreme-carry-multiplied-actual-forcing.md)，
不是任选一个抽象余核向量。

## 1. 原目标及准确长度

保同一个实际来源、因子提升、$Q$、$a$、$u$、$\xi$，
并取
$$
\ell=r,\quad k=r-1,\quad s=2h+1,\quad1\le r<h.
\tag{1}
$$
原 R697/R701 乘子满足
$\mu_{\rm phys}=t\,m_\mu(t,Y_{\rm phys})$，$m_\mu(P)$ 为单位。
只使用其已付同预算或明确扩大后预算，未添加新来源。

选定 R722 的一个原切向返回，将其写为
$$
\mathcal T(H)=d^{-C_D}t^{r+1}Q\,m_{\rm tan}(t,Y)\mathcal V_FH ,
\tag{2}
$$
其中 $m_{\rm tan}(P)$ 为单位。
对相对 $J$ 取
$$
T=2h-r;
$$
对完整 $M$ 取
$$
T=2h-r-13.
\tag{3}
$$
后一个长度已经保同一 $U_0w^{13}$ 及两条十三行。

令 $v$ 是指定的
$\overline{\mu J(P^{\rm fact})/p}$；
在 $M$ 情形，使用其完整原 carrier 运输。
由前述 short-row note 的全目标计算，
剥 (2) 的真实共同前缀后，
$$
\boxed{
v_{\rm tan}=\epsilon\,t^{h-1}v_*(t)
\quad\text{于 }k[t,\epsilon]/(t^T,\epsilon^2),
}
\tag{4}
$$
并且
$$
\boxed{
v_*(0)=
\frac{m_\mu(P)}{m_{\rm tan}(P)}
\,e(P)^3\,b_s(0)\,u(0)^3\in k^\times .
}
\tag{5}
$$
$\xi_0$ 保原值，但它只从 (4) 的下一阶进入，所以不影响 (5)。

(4) 的推导先在完整原目标中乘 $\mu$：
第三块从 $t^{k+1}=t^\ell$ 起，准确消失；
活 $V_1$ 和非恒定 normal 单位项乘后才达到 $2h$，
再除一份 $t$ 后从 $2h-1$ 起。
由 $T\le2h-1$，这些项此时才能删除。
没有先令 raw $\bar\Gamma$ 中的 $\zeta^3$ 为零。

## 2. 指定目标不在 R722 的整单位块像中

假设
$$
\boxed{
T\ge h,\qquad T>2\kappa,\qquad h-1>\kappa .
}
\tag{6}
$$
其中 $\kappa=C^2$。
在原主阶 $9/8$ 接触窗，(6) 对充分大参数严格成立。
相对 $J$ 的 $T\ge h$ 由 $r<h$ 自动成立；
原 $M$ 须保 $h\ge r+13$ 这一准确额外门。

**定理。** (4) 的指定目标不在
$$
\overline{\mathsf B}:
\overline{\mathcal H}_2^{00}/kF^2
\longrightarrow\overline{\mathscr T}
$$
的像中。故其在 R722 整饱和单位块商
$\overline{\mathscr Q}_{\rm u}$ 中的类确实非零。

**证明。** 假设有同一个
$H\in\overline{\mathcal H}_2^{00}$
使 $G=\mathcal V_FH$ 达到 (4)。
记 $G_i=(\mathcal E^iG)|_C$、$\eta_0=t^hu$。
整个两块 Taylor 条件为
$$
G_0+\eta_0G_1=0,\qquad
a(G_1+\eta_0G_2)=t^{h-1}v_*(t)\pmod{t^T}.
\tag{7}
$$
由第二式模 $t^h$，
$$
G_1\equiv a^{-1}t^{h-1}v_*(t)\pmod{t^h}.
$$
所以第一式中 $\eta_0G_1$ 从 $t^{2h-1}$ 起；
(3) 保 $2h-1\ge T$，得到 $G_0=0\bmod t^T$。

沿 $C$，
$G_0=e\,t\,d(H|_C)/dt$。
$T<p$，故 $H|_C-H(P)=0\bmod t^T$。
$H(P)=0$，而该真实截面所在的线束次数为 $2\kappa<T$。
R722 的原 jet 单射因此迫
$$
H|_C=0,\qquad H=FH_1,\quad H_1\in\overline{\mathcal H}_1 .
$$
同一个 $H$ 还满足 $(\mathcal EH)(P)=0$，
故 $H_1(P)=0$。

因 $\mathcal V_FF=0$，
$$
G=F\mathcal V_FH_1,\qquad
G_1=e^2\,t\,\frac d{dt}(H_1|_C).
$$
代回 (7) 的最低非零行，得
$$
e^2t\,\frac d{dt}(H_1|_C)
\equiv a^{-1}t^{h-1}v_*(t)\pmod{t^h}.
\tag{8}
$$
$1\le h-1<p$，所有较低正次数及 $h-1$ 的 Euler 系数都是单位。
由 $H_1(P)=0$、(5)、(8)，实际有
$$
\operatorname{ord}_P(H_1|_C)=h-1.
$$
但它是次数为 $\kappa$ 的原线束截面，
且 $h-1>\kappa$，矛盾。证毕。

## 3. 两条实际残余列及尚未排掉的全原像

在 $Z=0$ 情形，R722 已证整个切向像就等于该单位块像。
所以 (6) 下，指定目标不在**整个这个实际切向子来源**的像中。

在 $Z>0$ 情形，令 $c_0,c_1$ 为 R722 的两条指定整残余列。
这次切向吸收的准确条件是
$$
[\bar v]\in k\bar c_0+k\bar c_1
\quad\text{于同一个 }\overline{\mathscr Q}_{\rm u},
\qquad [\bar v]\ne0.
\tag{9}
$$
若 (9) 成立，任何实际切向原像的
$(H(P),(\mathcal EH)(P)/e(P))$ 都不能同时为零。
若两残余列模 $p$ 都为零，则 (9) 失败。
没有由两列的数量猜测它们的秩或指定向量是否在其张成中。

原 $\mathcal W_D$ 还有其它真实列，
包括垂直返回、$F^2\mathcal H_1$ 和未分解的来源部分。
它们必须与 (9) 一起投到同一个商；
两个单独子像的非吸收不推出其和的非吸收。

本增补的非零只属于一个已明确、整饱和、同预算的实际子像商。
原完整 $M$ 的指定第二类、同一个 $R$、两条十三行 carry
和第三位仍保持，主课题未由此完成。

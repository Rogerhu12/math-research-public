# 原临界中模三支持的光滑立方来源排除

日期：2026-11-15。**状态：以下必要条件及其临界排除已证明；一般首核和指定同修正 forcing 仍开放。**

本 note 将 R680 着色增补中保留的负项用于 R697/R701 的一个实际候选范围。
它不把整个多项式的 charge 对称分别赋给因子，也不假设一般首核可写成立方。

## 1. 原范围

保持同一个 $p=6s-1>101$、$D\ge3$、$f_D<p$、
原 $\mathcal W_D$ 和完整相对 $\bar J$。令
$$
N_D=\dim\mathcal W_D,\qquad L=2s+\ell,\qquad
\delta_D=N_D-L,\qquad 1\le\ell<s-13.
$$
$\delta_D$ 可以为负。取实际非零候选
$$
\bar P=d^{-C_D}t^rQF^3\in\ker\bar J,\qquad
Q(0,1)\ne0,\quad F(0,1)=0,\quad
(\mathcal EF)(0,1)\ne0,
\tag{1}
$$
其中 $F,Q$ 为同一清分母框中的多项式，$F$ 不含全局 $t$ 因子。
设整个 $\bar P$ 的非零 charge 同余模三，记 $b=\deg_YF$。
由于 $F$ 在 $(0,1)$ 光滑且 $Q$ 在该点是单位，
该点的唯一几何不可约因子在 $\bar P$ 中的重复次数准确为三。

若 $r\ge s$，已有原简单门 $s\le M_D$。以下保 $r<s$。
原帽给
$$
r\le M_D=5D+4-(D\bmod2),\qquad b\le D/3.
\tag{2}
$$

## 2. 保留下来的重复因子负项

在 R680 的三个实际点 $(0,\zeta)$、$\zeta\in\mu_3$，
分解同一个 $\bar P$ 的全部接触因子，记严格曲线和重复次数为
$C_i,m_i$。定义
$$
\Xi=\sum_{m_i\ge2}(m_i-2)^2C_i^2\ge0.
$$
R680 着色增补的准确式给
$$
12(s-r)\le3\mathcal B_D^2-3\Xi+32D.
\tag{3}
$$
这里 $m_i=1$ 的负项是零，不计入 $\Xi$；
$m_i=2$ 也不贡献负项。来源对称只用来产生三个点并置换整个实际因子集合。

原 canonical 帽和十九重数直接给准确整数身份
$$
\mathcal B_D^2=2N_D-2D-17.
\tag{4}
$$
它也可由 R680 的十二余类式与
$N_D=\sum_{n=0}^D(e_{n+1}+1)$ 逐余类相减验证，不要求一个额外的像饱和假设。
把 $N_D=2s+\ell+\delta_D$ 代入 (3)，得
$$
\boxed{
\Xi\le
2\delta_D+2\ell+4r+\frac{26}{3}D-17.
}
\tag{5}
$$
因此在维数临界 $\delta_D=o(D^2)$、$\ell=o(D^2)$ 下，
所有重复次数至少三的实际接触曲线的自交总量只能是 $o(D^2)$。

## 3. 原光滑立方支不可能满足这个临界限制

令 $C$ 为 (1) 中经过 $(0,1)$ 的几何不可约因子的严格变换，
$b_C=\deg_Y C\le b$。光滑性给同一 $k[[t]]$ 上的唯一单位支
$Y=\psi(t)$。记 $h=\operatorname{ord}_t(\psi-g)$；
所有超过 $s$ 的阶只按原截断读取。

原两个长行是
$$
\bar P(t,g),\quad(\mathcal E\bar P)(t,g)\in t^s.
$$
因为 $Q$ 和 $\mathcal EF$ 在该点都是单位，$p>3$，
后一个式子的局部首项准确为 $3t^rQF(t,g)^2(\mathcal EF)(t,g)$，
其余项多含一份 $F$。所以
$$
\boxed{\min(h,s)\ge\frac{s-r}{2}.}
\tag{6}
$$
这不假设 $h<s$；若已超过截断，(6) 仍成立。

R680 的同一个单支 Euler forcing、全十九角极帽与原共振给
$$
\min(h,s)\le3C^2+8b_C.
$$
因此
$$
\boxed{C^2\ge\frac{s-r-16b}{6}.}
\tag{7}
$$
$C$ 在实际因子集合中的重数是三，故 $\Xi\ge C^2$。
(5)–(7) 于是给以下完整有限必要条件：
$$
\boxed{
s\le
12\delta_D+12\ell+25r+52D+16b-102.
}
\tag{8}
$$
没有使用其它分支具有算术零，也没有使用 $F$ 的 charge 自己同余模三。

如果 $D\to\infty$ 且
$$
\delta_D=o(D^2),\qquad\ell=o(D^2),\qquad
p/D^2\longrightarrow47/8,
$$
则 (2) 使 (8) 右侧为 $o(D^2)$，而
$s/D^2\to47/48>0$，矛盾。
因此该真实临界中不存在 (1) 的模三支持光滑立方来源。
如果 $\delta_D,\ell=O(D)$，(8) 已直接给 $s=O(D)$ 的有限排除门。

## 4. 对当前 forcing 的准确范围

原 $M$ 的第二、第三提升核必须先落入相对 $\ker\bar J$，
所以当同一个候选确实具有 (1) 时，本 note 可在继续
R697/R701 的顶 charge cap 或 $\mu J(P^{\rm fact})/p$ 之前排除它。
这保持原 $w^{13}$、两条十三行与同一个修正的要求，没有以较弱的
$\ker\bar M$ 冒充相对首核。

没有满足 (1) 的一般候选仍未被排除，特别是：

- 没有真实立方分解、或 $Q(0,1)=0$ 的来源；
- 原支奇异或 $\mathcal EF(0,1)=0$ 的来源；
- 整个多项式的 charge 差最大公因数为一或二的来源。

这些范围仍须处理原实际像及同 $R$ 的完整第二 forcing。
(8) 是已付着色负项的新实际候选排除，不是主目标的非零结论。

依赖：[R680](../results/R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)；
[着色增补](2026-11-15-r680-colored-root-energy-with-linear-multiplicity-cost.md)；
[R697](../results/R697-full-third-normal-top-reduction-and-same-correction-cap.md)；
[R701](../results/R701-sharp-two-charge-clearing-and-complete-same-correction-cap.md)。

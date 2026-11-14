# 原真正最小选择子的纯高返回：对角头局部化

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明的技术应用，不另计主要结果。** 本文直接把已有全部孔数高旗右逆限制到一个真实小头前缀，作用于同一个原真正 $\psi=\mathcal G^\dagger\zeta(r)$。它支付纯 $S_H^\dagger$ 费用的低对角头部分，并给完整 dyadic 加权尾接口。没有证明后一个加权尾已被实际两费预算控制，也不从源头支撑推出最小选择子的同支撑。

依赖：[全部孔数高出生右逆](../results/R271-appendix-all-hole-high-birth-right-inverse-and-return-energy.md)、[真实平衡 Jordan 相似](../results/R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)、[原真幂底项和两道桥](../results/R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)、[明确增长的原源头余商](../results/R271-appendix-dyadic-original-heads-birth-one-repair-and-explicit-growing-quotient.md)。

## 1. 在真正出生一坐标中切头，保原源不变

固定原 $m\ge5,d=2^m$ 和同一个合法 $q,r$。沿原桥坐标，令
$$
\psi=\mathcal G^\dagger\zeta(r),\qquad
\psi_j\in F_{d-j}\otimes K_{q+1},\quad
F_a=\operatorname{span}(e_0,\ldots,e_{a-1}).
$$
原裸费用精确支付
$$
\boxed{\|\psi\|\le\alpha(r).}
\tag{1.1}
$$
第二桥 $\mathcal R$ 只读取 $j\ge2$，其第 $j$ 个物理高输出不改变头坐标，
并属于 $F_{d-j}\otimes E_{j-1,q+j}$。

对 dyadic $H=2^n$、$5\le n\le m$，定义真正正交投影
$$
(P_H\xi)_j=
\begin{cases}
(P_{F_{H-j}}\otimes I)\xi_j,&2\le j\le H-1,\\
0,&j=0,1\text{ 或 }j\ge H.
\end{cases}
\tag{1.2}
$$
因此它保留的准确头指标是 $i+j\le H-1$。
这些 $P_H$ 嵌套且相互交换；它们作用于原坐标 Hilbert 空间，
没有改变 $\psi$ 的来源或重新选择最小者。

## 2. 低对角部分的真正纯高费用

$\mathcal R P_H\psi$ 的第 $j$ 行属于
$$
F_{H-j}\otimes E_{j-1,q+j},\qquad2\le j\le H-1.
\tag{2.1}
$$
这恰是旧高旗右逆的 $H$ 维头输出旗，但尾仍是原 $D_m$。
原头嵌套给 $A_m|_{F_H}=A_n$；用同一个实际 $A_n$ 的平衡相似，
旧稿逐项构造的向左高修正位于
$$
F_{H-j+1}\otimes E_{j-1,q+j}.
$$
它是原宽度 $d$ 中的合法高输入：头至多 $H-j\le d-j$，
尾深度 $j-1\le d-i$，首段为零，最左输出因 $D^{j-1}$ 核条件而为零。
所以这里确实是纯高补量，不含首段 primitive 或其它低域改动。

旧范数证明只使用尾范数不超过 $1$，因此对
$\nu_m=\|D_m\|\le m^{-1}$ 同样给一个高右逆 $\mathcal Q_H$，满足
$$
\|\mathcal Q_H\|\le e^{20H^4}.
$$
第二桥是 $D_m\mathcal I$ 的物理高投影，故
$\|\mathcal R\xi\|\le\nu_m\|\xi\|$。
真正 MP 逆不比该合法候选更贵，于是
$$
\boxed{
\|S_H^\dagger\mathcal R P_H\psi\|
\le\nu_m e^{20H^4}\|P_H\psi\|.
}
\tag{2.2}
$$
下标 $H$ 在 $P_H,\mathcal Q_H$ 表示小头维数；
$S_H$ 沿全篇原记号仍表示原完整高输入算子，并未换成另一个最小逆。

## 3. 好顶部中低对角纯费用指数趋零

取明确增长稿的
$$
Q_m=\lfloor e^{d^3/4}\rfloor,\qquad
H_m=2^{\lfloor3m/4-2\rfloor},\qquad m\ge10,
$$
以及真实不交未来带数 $K_m\ge e^{d^3/4}/(8d)$。
若同一个好顶部源满足
$$
\alpha_b(r)^2\le\Xi_b(r)^2\le2\varepsilon_m^2/K_m,
\tag{3.1}
$$
则 (1.1)、(2.2) 及 $H_m^4\le d^3/256$ 给
$$
\boxed{
\|S_H^\dagger\mathcal R P_{H_m}\psi\|
\le\frac{4\sqrt d}{m}\,
e^{-3d^3/64}\varepsilon_m.
}
\tag{3.2}
$$
这个结论对原好顶部源成立，也适用于保持 (3.1) 的真实两费投影残源；
不需要它在物理源头 $F_{H_m}$ 中。

由同一个有界 MP 逆的线性性，准确有
$$
\boxed{
\begin{aligned}
&\|S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)
-S_H^\dagger\mathcal R(I-P_{H_m})
       \mathcal G^\dagger\zeta(r)\|\\
&\hspace{2cm}\le
\frac{4\sqrt d}{m}\,
e^{-3d^3/64}\varepsilon_m.
\end{aligned}}
\tag{3.3}
$$
所以在这一实际预算下，纯高问题可收窄到同一真正选择子的高对角头部分。
没有给这个剩余部分另选一个裸链。

## 4. 完整 dyadic 加权尾接口

记
$$
\Delta_5=P_{32},\qquad
\Delta_n=P_{2^n}-P_{2^{n-1}}\quad(6\le n\le m).
$$
它们是相互正交的投影，且
$\mathcal R\psi=\sum_{n=5}^m\mathcal R\Delta_n\psi$，
因为 $\mathcal R$ 消灭 $j=0,1$。
每项用 (2.2)，再作带权 Cauchy--Schwarz，得到
$$
\|S_H^\dagger\mathcal R\psi\|
\le\nu_m\sum_{n=5}^m e^{20\cdot16^n}\|\Delta_n\psi\|.
$$
进一步
$$
\boxed{
\|S_H^\dagger\mathcal R\psi\|^2
\le2\nu_m^2
\sum_{n=5}^m2^{n-5}e^{40\cdot16^n}
\|\Delta_n\psi\|^2.
}
\tag{4.1}
$$
第二行使用 $\sum_{n\ge5}2^{-(n-5)}=2$。
这里没有假定不同高补量彼此正交；原输出分组正交不足以推出其 MP 原像正交。

也可在任意一个 dyadic 切口保留两项式
$$
\boxed{
\|S_H^\dagger\mathcal R\psi\|
\le\nu_m e^{20H^4}\|P_H\psi\|
+\nu_m e^{20d^4}\|(I-P_H)\psi\|.
}
\tag{4.2}
$$
右端后一个范数可以含 $j=0,1$，它们只增加非负上界。

## 5. 准确范围

源旗 $r\in F_H$ 与坐标旗 $P_H\psi=\psi$ 是两件不同的事：
原 $\mathcal G^\dagger$ 是整个 Hilbert 空间的真正最小逆，一般会跨头。
已经支付的原源头 $M_2$ 投影也不使 $P_H\psi=\psi$。

本笔记的新用途是 (3.3)：在实际好顶部预算中，低对角纯高贡献已经指数趋零。
未支付的量准确留在同一个
$(I-P_{H_m})\mathcal G^\dagger\zeta(r)$，
或更细的 (4.1) dyadic 加权尾中。
(4.1) 是原费用的充分上界，未被宣布为实际源已有的尾估计；
普通 ISP、原 $N=M$ 及一般纯高窄源界仍 OPEN。

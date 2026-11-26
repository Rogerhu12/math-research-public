# R271 附录：指数强前缀上的实际方差完整源极限

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本补充把
[联合 carry 有限 Fock 乘子稿](R271-appendix-joint-carry-finite-fock-multiplier-and-exponential-strong-prefix-gram.md)
的完整 inverse 比较接到原真实头的已证强极限。
这里始终使用完整头 inverse，不能将结论移到未知移动真子空间的压缩 inverse。

## 1. 实际增长范围和结论

令 $m\to\infty$、$d=2^m$，选择整数 $x_m,J_m$ 及正数 $s_m$ 满足
$$
 d\le x_m,\qquad x_m+1\le\frac14e^{26d^3},\qquad
 1\le J_m\le h_m-1,\quad h_m=d+x_m-m,
 \tag{1.1}
$$
$$
 s_m\ge S_{x_m},\qquad s_m\longrightarrow0.
 \tag{1.2}
$$
原强头为
$$
 C_m=A_m+D_{[m,x_m)},\qquad
 H_{C_m,J_m}(s_m)
 =\sum_{j=0}^{J_m}\frac{(C_m^*)^jC_m^j}{j!s_m^j}.
$$
令 $\iota_x$ 为前 $x$ 位的完整物理真空嵌入，$M=\ker T$。则
$$
 \boxed{
 \iota_{x_m}H_{C_m,J_m}(s_m)^{-1}\iota_{x_m}^*
 \xrightarrow{\mathrm{strong}}P_M.
 }
 \tag{1.3}
$$
不要求 $s_m\ge S_m$。特别，原实际方差 $s_m=S_{x_m}$
和确定的大辅助方差 $s_m=(x_m+1)S_{x_m}$ 都合法。
高度 $J_m=1$ 以及整个强头有限塔 $J_m=h_m-1$ 同样被包含。

## 2. 完整 inverse 的证明

原真实头 $A_x$ 在同一物理坐标上的完整 inverse 强极限，见
[放大方差与阻尼代表稿](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)
§§2--3。以其基头指标取 $x_m$、强长度取零，它准确给
$$
 \iota_{x_m}H_{A_{x_m},J_m}(s_m)^{-1}\iota_{x_m}^*
 \xrightarrow{\mathrm{strong}}P_M.
 \tag{2.1}
$$
所需 $J_m\le2^{x_m}-1$ 成立，因为
$J_m<h_m\le2x_m<2^{x_m}$。没有把 $A_x$ 的有限截断 Gram
换成无穷塔，也不需要 $J_m$ 先趋于无穷。

另一方面，联合 carry 乘子稿 §6.2 已经在 (1.1)--(1.2) 内证明
$$
 \|H_{C_m,J_m}(s_m)^{-1}
     -H_{A_{x_m},J_m}(s_m)^{-1}\|
 \le e^{-d^4}.
 \tag{2.2}
$$
两边是同一个完整 $2^{x_m}$ 维空间上的 inverse。
同一真空嵌入保持这个算子范数界。(2.1)--(2.2) 立即给 (1.3)。

## 3. 原固定 forcing 的完整正高度能量

固定原有限物理 $f$，充分大 $m$ 后令
$g_m=\iota_{x_m}^*f$，并记
$$
 a_m=H_{C_m,J_m}(s_m)^{-1}g_m,\qquad
 q_m=\langle g_m,a_m\rangle.
$$
由 (1.3)，
$$
 \iota_{x_m}a_m\to P_Mf,\qquad
 q_m\to\|P_Mf\|^2,
$$
因此原完整正能量准确满足
$$
 \boxed{
 \varepsilon_m:=q_m-\|a_m\|^2
 =\sum_{j=1}^{J_m}\frac{\|C_m^ja_m\|^2}{j!s_m^j}
 \longrightarrow0.
 }
 \tag{3.1}
$$
这没有指定 $\varepsilon_m$ 的速率。
在共同物理空间张量辅助 Fock 中，整个有限源列遂有
$$
 \sum_{j=0}^{J_m}
 \frac{\iota_{x_m}C_m^ja_m}{\sqrt{j!s_m^j}}\otimes e_j
 \longrightarrow P_Mf\otimes e_0
 \quad\text{强收敛}.
 \tag{3.2}
$$
正辅助高度彼此正交，其总平方范数正好是 (3.1)，故不需逐高度换极限。

## 4. 同一物理来源与母窗口

原阻尼相干代表的同源身份只要求 $s\ge S_x$、完整头 inverse
及 $Q\ge R+J$，其中 $R=x-m$。本补充没有改变这些对象。
在 (1.1) 中
$$
 R+J<3(x+1)<e^{26d^3},
$$
所以可在同一个原 c26 母窗口内选合法整数 $Q$。
相干代表继续给同一个原 $V_Q/K_Q/U_Q$ 投影；现在其实际正高度能量
在全部 (1.1) 的指数强前缀上由 (3.1) 趋零。

例如取 $s=(x+1)S_x$ 和 $J=h-1$，原大辅助方差稿的共同头反馈
$36/x$ 行收缩、物理 $16\varepsilon_m/x$ 平方预算仍可直接使用。
其额外母支持 $Q\ge R+h+1$ 在此同样合法，因为
$R+h+1<3(x+1)<e^{26d^3}$。
这里仍是同一个固定 $C_m$ 的并行行；没有把不同顺次硬化头的来源拼合免费化。

特别，本补充的完整 inverse 强极限不证明
$(P_{F_0}H_{C_m,J_m}|_{F_0})^{-1}$ 的相同极限，
也不支付该真核 Galerkin 残余的绝对 $\mathcal Z_\gamma$。

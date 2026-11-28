# 原 Haar 自然高位有限平方根的全部强图聚点为零

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127  
作者：root；stable_kernel_return 独立核对全部尺度情形；AI-assisted GPT-6 Astra Pro。

**状态：已证明的具体构造障碍。** 下列有限根的平方在算子范数下趋于原 Haar 算子，但对任意非零复标量尺度，其图没有非零强聚点。该结论只处理这里明确写出的移动高位根，不排除其它非局部闭根，也不决定普通 ISP。

## 1. 保持原 Haar 表示的有限根

沿用 [R9 的原算子和有限头近似](R9-radial-odometer-and-nilpotent-approximants.md)，令
$$
A_m=J_m\otimes I,\qquad \|A_m-A\|=\alpha_m\longrightarrow0.
\tag{1}
$$
这里 $A_m$ 是作用于最低 $m$ 位的幂零近似，**不是**原尾 $A^{(m)}$。$A$ 单射且拟幂零。

令 $E_m=e_{10}$ 仅作用于第 $m$ 个物理位，
$$
P_m^0=E_m^*E_m,\qquad P_m^1=E_mE_m^*,\qquad P_m^0+P_m^1=I.
$$
$A_m$ 与该位全部矩阵单位交换。对任何非零复数 $c_m$，定义全域有界算子
$$
S_m=c_mE_m+c_m^{-1}E_m^*A_m.
\tag{2}
$$
由两次同向翻转为零及互补投影恒等式，准确有
$$
\boxed{S_m^2=A_m.}
\tag{3}
$$
因此这些确实是原有限近似的代数平方根，且 $S_m^2\to A$ 于算子范数。不假设 $\sup_m\|S_m\|<\infty$。

原 Haar 无限乘积的参考向量为每位 $(1,1)/\sqrt2$。所以
$$
P_m^0,P_m^1,E_m,E_m^*\longrightarrow\tfrac12I\quad\text{于 WOT}.
\tag{4}
$$
证明只需先取依赖有限低位的两个柱函数；当 $m$ 超过其支持时，对第 $m$ 位的矩阵元恰等于 $1/2$。再由柱函数稠密性及各算子范数不超过一推广。特别，对任意固定 $h\in H$，
$$
\|P_m^i h\|^2\longrightarrow\tfrac12\|h\|^2,\qquad i=0,1.
\tag{5}
$$
若 $h_m\to h$ 强，因投影一致有界，(5) 对 $P_m^i h_m$ 同样成立。

## 2. 完整强图定理

**定理。** 对任意非零复数列 $c_m$，若沿任意趋于无穷的指标子列有
$$
f_m\longrightarrow f,\qquad S_m f_m\longrightarrow g
\quad\text{于 }H\text{ 的范数},
\tag{6}
$$
则 $f=g=0$。换言之，在 $H\oplus H$ 的强拓扑中，这族图的全部聚点只有 $(0,0)$。

记 $g_m=S_m f_m$。两个真实输出位给
$$
P_m^1g_m=c_mE_m f_m,\qquad
P_m^0g_m=c_m^{-1}E_m^*A_m f_m.
\tag{7}
$$
同时 (1)、(6) 给 $A_m f_m\to Af$ 强。

### 2.1 尺度模趋于无穷

若 $|c_m|\to\infty$，第一式给
$$
\|P_m^0f_m\|=|c_m|^{-1}\|P_m^1g_m\|\longrightarrow0.
$$
由 (5) 得 $f=0$。第二式中 $A_m f_m$ 有界，故 $P_m^0g_m\to0$，再由 (5) 得 $g=0$。

### 2.2 尺度模趋于零

若 $|c_m|\to0$，第二式给
$$
\|P_m^1A_m f_m\|=|c_m|\|P_m^0g_m\|\longrightarrow0.
$$
由 $A_m f_m\to Af$ 和 (5) 得 $Af=0$。原 $A$ 单射，所以 $f=0$。第一式给 $P_m^1g_m\to0$，再次由 (5) 得 $g=0$。

### 2.3 尺度留在非零有限极限

若 $c_m\to c\ne0$，则 $S_m$ 一致有界，故
$$
S_m f_m-S_m f\longrightarrow0.
$$
利用 (4) 及 $A_m f\to Af$，(6) 的弱极限必为
$$
g=\tfrac12(cf+c^{-1}Af).
\tag{8}
$$
(2) 的两个输出位正交，因此
$$
\|S_m f\|^2
=|c_m|^2\|P_m^0f\|^2
 +|c_m|^{-2}\|P_m^1A_m f\|^2
\longrightarrow\tfrac12\bigl(\|cf\|^2+\|c^{-1}Af\|^2\bigr).
\tag{9}
$$
由于这里确有强收敛，(9) 必等于 (8) 的平方范数。由平行四边形恒等式，差准确为
$$
\tfrac14\|cf-c^{-1}Af\|^2=0.
$$
于是 $Af=c^2f$。拟幂零 $A$ 不可能有非零特征值 $c^2$，所以 $f=0$，(8) 随即给 $g=0$。

最后，任意非零复数列总可抽子列，使其模趋于 $0$、趋于无穷，或留在某个紧环带内；在最后一种情形再抽相位收敛子列即得 $c_m\to c\ne0$。原有的强极限 $f,g$ 不随抽子列改变，故三种情形穷尽，定理得证。

## 3. 对实际原闭根构造的含义

[原 Haar 全普通格的共同旗与闭稳定根](R12-appendix-all-ordinary-invariant-common-coordinate-flags-and-stable-closed-roots.md)要求在同一个实际尾子商上有闭、稠密定义、定义域稳定的算子根。式 (3) 只说明各有限近似有代数根，不能提供这样的非零图。

本定理严格排除如下直接构造：选取任意尺度 $c_m$，让同一原向量及其在 (2) 下的像同时强收敛，试图得到所需根的非零图向量。即使源允许随 $m$ 变化而强趋固定向量，结论仍为零。

这里不排除不同于 (2) 的有限根、混合真实低位与尾的非局部来源、弱图极限、或未知实际旗子商上的闭根。没有把该具体近似失败合成为原 $A$ 无普通不变子空间的结论；后续仍须构造实际非局部闭域或原旗。

本条为自含纸面证明，不执行旧数学门，不创建系数载荷或新的数值复核门。

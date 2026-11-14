# 奇数硬端的倒数权桥平方与物理提升接口

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态：本文的同源等价及正交分解已证明；权与出生均无关的有限费用界尚未证明。** 本文继续[奇数硬端消逆](R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md)，没有增加一个有限模型的数值验证作为数学结论。

## 1. 原硬端与倒数权之间的真实同构

固定任意正权 \(b=(b_i)_{i=1}^{2r+1}\)、\(r\ge1\)。写
\[
d_b=\sum_i b_iE_i,\qquad
U_b=K_r(b),\qquad V_b=K_{r-1}(b),
\]
\[
A_b=\left.\sum_i b_i^{-1}E_i\right|_{U_b}:U_b\to V_b,
\quad G_1(b)=\Gamma_{1,r}(b),
\quad L_j(b)=\Gamma_{j,r-1}(b)\quad(1\le j\le3).
\]
已付硬端消逆把全部加强首费用写成
\[
\mathcal K_b=A_b^*L_1(b)L_3(b)^{-1}L_1(b)A_b.
\tag{1.1}
\]
令倒数权 \(a_i=b_i^{-1}\)、\(Z=\prod_i b_i^2\)，并将以下完整对角算子限制为所列真实 primitive 空间间的同构
\[
D_s:K_s(b)\longrightarrow K_s(a),\qquad
D_se_I=b_I^2e_I.
\tag{1.2}
\]
它是有限维可逆同构，其伴随按各自继承的物理内积取。由 [R239 全出生倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)，低出生高度三给出
\[
L_1(b)=Z^{-1}D_{r-1}^*L_2(a)D_{r-1},
\qquad
L_3(b)=Z^{-1}D_{r-1}^*D_{r-1}.
\tag{1.3}
\]
特别
\[
L_3(b)^{-1}=Z D_{r-1}^{-1}D_{r-1}^{-*}.
\tag{1.4}
\]
这一步只在两个真实 primitive 源之间取逆，不把完整对角算子的逆与正交压缩互换。

倒数权的真实三次桥记为
\[
B_a=\left.\sum_i a_i^3E_i\right|_{U_a}:U_a\to V_a.
\]
逐集合比较系数得到
\[
\boxed{D_{r-1}A_b=B_aD_r.}
\tag{1.5}
\]
例如从 \(I\) 删去 \(i\) 时，两边系数同为 \(b_I^2/b_i^3\)。上出生高度一的同一对偶在阶数零给
\[
\boxed{I_{U_b}=Z^{-1}D_r^*G_1(a)D_r.}
\tag{1.6}
\]

## 2. 精确的桥平方目标

把 (1.3)–(1.5) 按原非交换次序代入 (1.1)，可得
\[
\boxed{
\mathcal K_b=Z^{-1}D_r^*B_a^*L_2(a)^2B_aD_r.
}
\tag{2.1}
\]
因此，对任意 \(\kappa>0\)，
\[
\boxed{
\mathcal K_b\preceq\kappa I_{U_b}
\quad\Longleftrightarrow\quad
B_a^*L_2(a)^2B_a\preceq\kappa G_1(a).
}
\tag{2.2}
\]
也就是
\[
\boxed{\|L_2(a)B_aG_1(a)^{-1/2}\|^2\le\kappa.}
\tag{2.3}
\]
反向倒数变换仍覆盖全部正权，故该等价没有损失原硬端的全称量词。

这里的平方是必要的：已知占据 Schur 界只控制 \(B_a^*L_2(a)B_a\)，它没有支付 (2.2) 中第二个 \(L_2(a)\)。没有一致条件数时，不能从一次 Gram 费用免费增加这个因子。

## 3. 最小逆的物理投影表述

本节省去权下标，仍在奇数硬端。记
\[
R=\mathcal J_{1,r-1}:V\to\mathcal H_r,
\qquad E=\mathcal J_{1,r}:U\to\mathcal H_{r+1},
\qquad J_2=\mathcal J_{2,r-1}:V\to\mathcal H_{r+1}.
\]
真实两带式在同一个物理层给
\[
dJ_2=2R-B^*L_2,
\qquad
R(V)\perp U.
\tag{3.1}
\]
因此
\[
\boxed{L_2B=-J_2^*d^*|_U.}
\tag{3.2}
\]
同时中间层 \(d:\mathcal H_{r+1}\to\mathcal H_r\) 可逆，且 \(E=d^{-1}|_U\)。于是 (2.3) 等价于
\[
\boxed{
\|J_2^*d^*d v\|\le\sqrt\kappa\,\|v\|
\quad(v\in E(U)).
}
\tag{3.3}
\]
这里
\[
E(U)=\ker d^2|_{\mathcal H_{r+1}}
=\ker e|_{\mathcal H_{r+1}},
\qquad e=\sum_i b_i^{-1}E_i^*,
\tag{3.4}
\]
而 \(J_2(V)\subset(E(U))^\perp\)。第一处核等式由中间层删除可逆及 \(dE=I_U\) 得到；第二处由有限 \((d,e)\) 的完整 \(\mathfrak{sl}_2\) 分解：在第 \(r+1\) 层，仅出生 \(r\) 的高度一塔被 \(e\) 消去，其余塔的上升系数非零。也可用 \(eE=0\) 加核维数核对。

(3.3) 使目标成为一个实际正算子 \(d^*d\) 的跨正交块，经完整最小逆后的费用。一个任意正算子的跨块不会自动收缩；必须使用乘积权 Boolean 来源，不能把 (3.3) 仅凭投影记号当成已得范数界。

## 4. 原权侧另一个无顶逆的等价式

回到原权 \(b\)，仍写 \(e=\sum_i b_i^{-1}E_i^*\)。因为 \([d_b,e]=3I\) 在 \(V_b\) 所在的 \(r-1\) 层，且 \(d_bv=0\)，故
\[
d_bev=3v.
\]
在 \(\mathcal H_r=U_b\oplus\operatorname{Ran}d_b^*\) 中作真正正交分解，得到
\[
\boxed{e|_{V_b}=3\mathcal J_{1,r-1}+A_b^*.}
\tag{4.1}
\]
于是
\[
\boxed{A_bA_b^*=P_{V_b}e^*e|_{V_b}-9L_1(b).}
\tag{4.2}
\]
注意右侧整体非负；没有把其中两项分别估计。

矩形算子 \(F=L_3(b)^{-1/2}L_1(b)A_b\) 的 \(F^*F\) 与 \(FF^*\) 有相同的非零谱，所以
\[
\boxed{
\mathcal K_b\preceq\kappa I_{U_b}
\quad\Longleftrightarrow\quad
L_1(b)A_bA_b^*L_1(b)\preceq\kappa L_3(b).
}
\tag{4.3}
\]
结合 (4.2)，还可写成不含顶层压缩逆的同源形式
\[
\boxed{
L_1(b)\bigl(P_{V_b}e^*e|_{V_b}\bigr)L_1(b)
\preceq \kappa L_3(b)+9L_1(b)^3.
}
\tag{4.4}
\]
(4.4) 只是准确减少需要控制的逆，尚不是一个新的已付上界。它保留低源完整第一 MP Gram 与其余两项的共同来源。

## 5. 一次有界定向数值剖面的范围

独立脚本 [targeted profile](../notes/2026-11-14-odd-hard-top-targeted-profile-789f.py) 及其 [JSON](../notes/2026-11-14-odd-hard-top-targeted-profile-789f.json) 记录一次 \(M=7,9\) 的研究剖面：地址空间限制 512 MiB、CPU 上限 55 秒、禁止 core；实际耗时约 0.493 秒。脚本用完整第一 MP 后压缩，并以矩形顶逆因子的 QR 白化计算 (1.1)，没有直接形成 \(L_3\) 的病态平方逆。

66 个预设尺度点中，50 个通过所记源残差、方程残差和两个条件阈值。最大接受值在
\[
M=9,\quad r=4,\quad
b=(30,30,1,1,1,1,1,1/30,1/30),
\]
约为 \(0.4986146616\)。另有 16 个病态点被拒绝，其中确有普通双精度给出的很大假费用。这些点不构成反例，也没有把任何浮点结果当成证明。该一次剖面结束，不追加相同路线采样。

本文留下的真正需求是 (2.3)、(3.3) 或 (4.4) 的一个统一有限界，或者严格的完整物理反例。已有硬端归约保证它足以决定全部加强高度的同常数问题；它仍不自动支付原 graph 接口。

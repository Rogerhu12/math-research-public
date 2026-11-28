# R150：两个完整个别奇部的原六次范数与同点值边界

日期：2026-11-29（Asia/Taipei；推导于2026-11-28 UTC）。会话：Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**状态：已证明；纯代数纸证，无新执行。** 从同一个原 singleton 值参数的第二矩和完整个别 N/P 误差，得到两条至多六次的必要式。它们有不正乘 D、也不倒 D 的直接原理想来源；不把分别取范数后的零点混配成同一个原值解。

本页不改变当前 W 十一原首项输入 c55c2aa7a11099914626844ce203f2a64c726b91，也不续接任何冻结的旧计算。

## 1. 原环、两个 singleton 与同一个值参数

取一般原 $2+1+1$ Gram，使用真正 double-germ 乘法
$$
(vz)_1=v_0z_1+v_1z_0.
$$
沿[全一般 N4 三系数](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)的原迹和原 Gram 算子，记
$$
\delta=\rho^2,\quad \ell=b+c,\quad m=\rho(b-c),\quad
M=4bc\delta=\ell^2\delta-m^2.
$$
本页的系数环只要求 $2,\ell,M,\delta$ 为单位；它们在本文应用的原图中已经支付。无需 m 单位，也不预设 D 非零。涉及旧 Low 的比较在第5节另加 m 单位，范围明确分开。

令
$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_\lambda-T^2,\quad
K=\ell^2B_\lambda-3\ell TA_\lambda+2T^3,\quad
A_0=1+T/\ell.
$$
保留**同一个**原参数 $\sigma$，令
$$
v_0=A_0+\frac m\ell\sigma,\qquad
h=v_0-\rho\sigma,\qquad k=v_0+\rho\sigma.
\tag{1}
$$
这只是原一次矩 $b(h-1)+c(k-1)=T$ 的完整参数化，两个符号都保留。原第二移位矩误差
$$
E_2=b(h-1)^2+c(k-1)^2-A_\lambda
$$
满足
$$
q:=M\sigma^2-D=\ell E_2.
\tag{2}
$$
第三矩的原身份也保持：
$$
H:=K-2mD\sigma=(3T+2m\sigma)q-\ell^2E_3,
\quad E_3=b(h-1)^3+c(k-1)^3-B_\lambda.
\tag{3}
$$
后面的两个新范数只需 q；不删除完整系统中的 H。

## 2. 完整奇部误差及其含义

从原同一点四行构造完整二次型和 centered 三次型：
$$
N_4(v)=2\tau(dv^2)-2f\tau(v^2)
-4\tau(v)\tau(dv)+4f\tau(v)^2+\tau(v\mathcal Kv),
$$
$$
P_2(v)=\tau\bigl((v-\tau(v)\mathbf1)^3\bigr).
\tag{4}
$$
令两个共轭 singleton 行为 $g_B,g_C$，写
$$
N_4(g_B)=N_a+\rho N_b,\quad N_4(g_C)=N_a-\rho N_b,
$$
$$
P_2(g_B)=P_a+\rho P_b,\quad P_2(g_C)=P_a-\rho P_b.
\tag{5}
$$
这里 $N_b,P_b$ 是完整原形式的奇坐标，不是 weighted NS/PS 的某个选定分量，也不是最高齐次替代式。

原四条个别误差为
$$
\mathcal E_{N,B}=N_4(g_B)-2\lambda P_{02}h^2,\quad
\mathcal E_{N,C}=N_4(g_C)-2\lambda P_{02}k^2,
$$
$$
\mathcal E_{P,B}=P_2(g_B)-P_{02}h^3,\quad
\mathcal E_{P,C}=P_2(g_C)-P_{02}k^3.
$$
其准确奇部是
$$
\boxed{
E_N=\frac{\mathcal E_{N,B}-\mathcal E_{N,C}}{2\rho}
=N_b+4\lambda P_{02}v_0\sigma ,
}
\tag{6}
$$
$$
\boxed{
E_P=\frac{\mathcal E_{P,B}-\mathcal E_{P,C}}{2\rho}
=P_b+P_{02}(3v_0^2\sigma+\delta\sigma^3).
}
\tag{7}
$$
式(6)–(7)由 $(v_0-\rho\sigma)^2$、$(v_0-\rho\sigma)^3$ 的奇部直接得到，符号均为正。$\delta$ 单位保证 $\rho^{-1}=\rho/\delta$，所以这确实是两条原 singleton 误差的组合。

**两个 singleton 同时满足各自原方程，必使相应奇部为零；奇部为零本身不充分。** 若把任一对误差写为 $e_a\pm\rho e_o$，其原加权误差为
$$
b(e_a+\rho e_o)+c(e_a-\rho e_o)=\ell e_a+me_o.
\tag{8}
$$
因此保留原加权误差与 $e_o$ 后，由 ell 单位可完整恢复两个误差。本文的范数只增加必要条件，不以范数替换 (6)、(7)、加权误差或其它原条件。

## 3. 两条完整线性余式及 q 的实际乘子

定义以下纯原 Gram 系数，它们不含 $\sigma$：
$$
\begin{aligned}
a_N&=N_b+\frac{4\lambda P_{02}mD}{\ell M},
&b_N&=4\lambda P_{02}A_0,
&c_N&=\frac{4\lambda P_{02}m}{\ell M},\\
a_P&=P_b+\frac{6P_{02}A_0mD}{\ell M},
&b_P&=P_{02}\left[
3A_0^2+\left(\frac{3m^2}{\ell^2}+\delta\right)\frac D M\right].
\end{aligned}
\tag{9}
$$
另置
$$
c_P(\sigma)=
\frac{P_{02}}{M}\left[
\frac{6A_0m}{\ell}
+\left(\frac{3m^2}{\ell^2}+\delta\right)\sigma
\right].
\tag{10}
$$
由 $\sigma^2-D/M=q/M$ 和
$\sigma^3-D\sigma/M=\sigma q/M$，有**完整多项式身份**
$$
\boxed{\ E_N=a_N+b_N\sigma+c_Nq,\qquad
E_P=a_P+b_P\sigma+c_P(\sigma)q.\ }
\tag{11}
$$
第一式的差只是
$4\lambda P_{02}m(\sigma^2-D/M)/\ell$。
第二式先展开
$$
E_P=P_b+3P_{02}A_0^2\sigma+
\frac{6P_{02}A_0m}{\ell}\sigma^2+
P_{02}\left(\frac{3m^2}{\ell^2}+\delta\right)\sigma^3,
$$
再分别减去 (9) 的常数和一次项，即得 (10)。因此(11)不是只在约化点集上成立的同余；其完整 q 乘子已经显示。

## 4. 两条无 D 乘子的原六次范数

令
$$
\boxed{\quad C_N=M a_N^2-D b_N^2,\qquad
C_P=M a_P^2-D b_P^2.\quad}
\tag{12}
$$
对任一 $E=a+b\sigma+cq$，直接展开得到
$$
\boxed{
M a^2-D b^2
=M(a-b\sigma)E+
\bigl[b^2-M(a-b\sigma)c\bigr]q .
}
\tag{13}
$$
右侧的 $\sigma^2$ 项恰为
$-Mb^2\sigma^2+b^2(M\sigma^2-D)$，其它 q 项取消。因此
$$
C_N\in(q,E_N),\qquad C_P\in(q,E_P).
\tag{14}
$$
结合(2)、(6)、(7)，两者都有原第二矩及两 singleton 原误差的完整来源。没有正乘 D，没有 D 逆，也没有除范数、$a_i$、$b_i$ 或任何新头。

等价地，在首一二次代数
$$
\mathcal B=\mathcal A[\sigma]/(\sigma^2-D/M)
$$
中，$1,\sigma$ 是环境的自由基，而
$$
C_N=M\operatorname{Norm}_{\mathcal B/\mathcal A}(a_N+b_N\sigma),
\qquad
C_P=M\operatorname{Norm}_{\mathcal B/\mathcal A}(a_P+b_P\sigma).
\tag{15}
$$
这里的环境自由性来自首一二次，不把完整原方程商当作自由模。

当 D=0 时，环境仍是 $\mathcal A[\sigma]/(\sigma^2)$；(13) 原样成立，保留其非约化信息。此时
$$
C_N=M N_b^2,\qquad C_P=M P_b^2.
\tag{16}
$$
不能由 (16) 在任意非约化商中直接删平方，也不能把双数环境替换为一个约化点。

以 $\lambda,T$ 及原 Gram 的线性几何变量总次数计，$N_b,P_b$ 至多三次，$A_0$ 至多一次，D 至多二次。因此
$$
\deg a_N,\deg a_P\le3,\quad
\deg b_N,\deg b_P\le2,\quad
\deg C_N,\deg C_P\le6.
\tag{17}
$$
任何同点仿射恢复，例如已刊 W/b0 的 $(\lambda,t)$ 恢复，保持这个上界；分母仅为旧纯权。本文只证明上界，没有执行系数展开或宣称两式必定达到六次、非零、不可约或互素。

## 5. 与旧 Nlow、Plow 的精确 D² 关系

只在本节另沿已付 m 的原图。令
$$
L_N=D a_N+\frac K{2m}b_N,\qquad
L_P=D a_P+\frac K{2m}b_P.
\tag{18}
$$
代入(9)，恰得已经发表的完整
$N_{\rm low}$、$P_{\rm low}$，没有改换奇部、值符号或同点参数：
$$
\begin{aligned}
L_N&=DN_b+2\lambda P_{02}
\left(\frac{KA_0}{m}+\frac{2mD^2}{\ell M}\right),\\
L_P&=DP_b+P_{02}\left[
\frac K{2m}\left(3A_0^2+
\frac{(3m^2/\ell^2+\delta)D}{M}\right)
+\frac{6A_0mD^2}{\ell M}\right].
\end{aligned}
$$
记 $R_6=MK^2-4m^2D^3$。对 N 或 P 都有
$$
\boxed{
4m^2D^2 C_i
=(2mD a_i-Kb_i)(2mM L_i)+b_i^2R_6,
\qquad i=N,P .
}
\tag{19}
$$
证明只需 $2mL_i=2mDa_i+Kb_i$，作差平方后加上 $b_i^2R_6$。

(19)说明在原 D 开图，旧 $R_6,L_i$ 已推出新范数；但它们在未倒 D 的必要代数中显示的来源带 D²。新的(13)直接来自原第二矩和完整个别误差，没有这个正乘子。这就是本次不同的原输入，而非把旧 Low 再投影一次。

形式边界 D=K=0 上，旧 $R_6,L_N,L_P$ 可以同时自动为零；(16)仍保存完整个别奇部的必要信息。这里只比较原多项式来源，不据形式边界断言物理图有解或无解。

## 6. 同根条件必须继续保留

两个范数各自消失，可能分别来自二次代数的不同根。即使再加完整 NV 的同类范数，也不能推出三条原线性余式选取同一个 $\sigma$。原 q、H、两条(11)、完整 NV 和所有原均值仍须在同点系统中保留，或用已经证明的完整双向替换。

特别地，(12)–(14)只给新的原必要条件。本文没有新的 W/Phi/HK 排空、权有限性、首项单位或点数结论；不把某个模范数或目标正幂提升成 QQ 原理想结论。

## 7. 来源与无执行记录

本页只作(11)、(13)、(19)的完整代数展开，不新增 Actions 或整数运算门：

- [原个别 N/P 与完整 NV 的低 D 次压缩](R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)，blob f4e6d79b9956e5a8b39e4a4f88bfbe17eee945f0；用于核对(18)的旧原式。
- [正确 I10 的同点二矩、三矩与完整奇部](R150-appendix-unit211-Phi-zero-corrected-individual-NP-full-NV-I10-and-two-decics.md)，blob ef4bad0b9f5a762c57c9e54695fd4a4247111f32，§2–3；这里只引用其显示的一般原身份，不借 Phi 的权特化或单位。
- [一般完整 N4](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md)；保证(4)使用整个原二次型和真 double-germ 乘法。

所有式均在明确列出的原环和同一 $\sigma$ 上成立。源强度的比较不等于几何充分性；普通不变子空间问题尚未由本文解决。

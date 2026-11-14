# R147 — 无穷可选 Heegner 域与完整类群的两个有限域迹

**状态：已证明。日期：2026-11-12。**

固定目标曲线 $E=389\mathrm a1$。固定合法
$p\ge7$、$p\ne13,389$ 与 $\ell+1=pu$、$p\nmid ua_\ell$。
Wiles（2015）Theorem 0.0.1 允许把 $p$ 本身列为分裂素数。
因此存在无穷多个虚二次域 $F$，满足
$$
 p\nmid h_F,\qquad p,389\text{ split }F,\qquad \ell\text{ inert }F.
$$
无限性由不断另指定一个新分歧素数得到，不含判别式上界。
对固定 E 的有限 p 例外以外，所有这些 F 的 Tate 像统一为
$\mathrm{GL}_2(\mathbb Z_p)$：可能的唯一二次下降域在 p 分歧，
已被上述条件排除。

令 $C=\operatorname{Cl}(F)$、$F_1=F[1]$、$H=F[\ell]$，
$L/F$ 为唯一 $C_p$ 子扩张，$U$ 为相对环类群的阶 u 子群。
则 $H^U=LF_1$、$\operatorname{Gal}(LF_1/F)=C_p\times C$。
原整数点始终是全部 $uh_F$ 项之和
$Q=[t_F]\operatorname{Tr}_{H/L}P[\ell]$，其中 p 单位 $t_F$
杀掉基层完整扭迹。

对实际去 p 函数 $g_p=\Theta^{p-2}\bar f_\pi/\mathrm{Ha}^p$，
先令 $\beta=\bar t_F\operatorname{Tr}_U g_p(x_\ell)$，再取
$\beta_F=N_C\beta$。共同 AS 坐标 $\tau y=y+1$ 可在真实
$L/F$ 剩余代数中选取，并被 C 固定。若
$$
 D_1\beta=-ny+a,\qquad
 D_2\beta=\frac n2y(y+1)-ay+g,
$$
则完整范数零条件是 $N_Cn=0$，且准确有
$$
 D_2\beta_F=-A_Fy+G_F,
 \qquad A_F=N_Ca,\quad G_F=N_Cg\in\mathbb F_p.
$$
若 $d$ 是 $[\mathfrak p]$ 在 C 中的阶，则
$$
 (A_F,G_F)=\sum_{r\in C/\langle[\mathfrak p]\rangle}
       \operatorname{Tr}_{\mathbb F_{p^d}/\mathbb F_p}(a_r,g_r).
$$
两个完整迹不同时零，等价于实际半局部 $D_2$ 行非零；由
R134 的增广单位比较及 R146，足以推出
$\Sha(E/\mathbb Q)[p^\infty]=0$。

[完整证明](../notes/2026-11-12-varying-field-full-class-artin-schreier-traces.md)
保留 canonical lift、全部 Frobenius 轨道、两条 torus 轨道及
不同 AS 坐标间的补偿项。没有证明上述两个迹在某个候选 F 上
非零。单个 CM 点非零或 p 素类数的存在不能代替完整类群和。

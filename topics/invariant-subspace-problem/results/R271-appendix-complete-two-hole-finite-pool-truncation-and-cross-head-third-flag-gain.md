# R271 附录：完整二远孔核的有限池截尾与原首头跨 m 第三旗增益

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿把完整二远孔核的 Stieltjes Schur 与原跨头有限前缀修复合并。所得截尾估计保持整个强头及全部零源，费用不含强头 inverse 的范数。对原固定物理首头 $f_1=e_1$，进一步支付第三核旗上的真实 Schur 增益之跨 $m$ 总和。

这个增益只读取 $q_{\flat}$ 在 $K\cap\operatorname{Ran}C^2$ 上的通道；其高旗补没有被删除，完整 $\gamma_{\flat}$ 仍未付。

依据：

- [完整二远孔核的 Stieltjes Schur](R271-appendix-complete-two-far-hole-kernel-stieltjes-schur-and-flag-source.md)，尤其 §§2–5；
- [原跨头有限前缀修复与第一行增益](R271-appendix-cross-head-finite-prefix-kernel-comparison-and-summable-first-row-gain.md)，§§3–6；
- [真实低链与无罚二远孔来源](R271-appendix-true-low-chain-two-hole-range-and-unpenalized-return-source.md)。

## 1. 同一物理核和完整二孔源度量

固定原 $x=m+R$ 与真实强头
$$
C=A_m+D_{[m,x)},\qquad C^h=0,\qquad h=2^m+R.
$$
记 $b_i=(i+1)^{-2}$、$z_i=b_i^2$。对 $y>x$ 定义
$$
D_\infty=D_{[x,\infty)},\quad
D_y=D_{[x,y)},\quad
S=S_x,\quad S_f=S_x-S_y,\quad t=S_y/S_x.
$$
所有空间均嵌在原物理 Hilbert 空间中。有限池列在 $i\ge y$ 置真空。令
$$
\mathscr K_{2,\infty}
=\ker(C+D_\infty)\cap\{\mathcal N_{[x,\infty)}\le2\},
$$
$$
\mathscr K_{2,y}
=\ker(C+D_y)\cap\{\mathcal N_{[x,y)}\le2\}
\otimes\Omega_{[y,\infty)}.
$$
它们是闭子空间，且准确有
$$
\mathscr K_{2,y}\subset\mathscr K_{2,\infty}.
\tag{1.1}
$$
记其正交投影为 $\Pi_{2,y},\Pi_{2,\infty}$。

假设
$$
\varepsilon_f:=\frac{2z_x}{S_f}<1.
\tag{1.2}
$$
这也保证有限池至少有三个非零位置。对有限或无限池，完整第二删除满足
$$
D_2D_2^*=S_\bullet I-2Z+bb^*
\succeq(S_\bullet-2z_x)I>0 .
$$
故 $D_2$ 满射，$D_2^\dagger$ 有界。完整二孔最小化的自然域和所有
$\ker D_2$ 零源都包括在引用的 Schur 定理中。

令 $\mathcal F_3=\ker C^3$。完整二孔源 Gram 记为
$\mathcal H_{2,\bullet}$，其 bosonic 比较矩阵为
$$
\mathcal H_b(S_\bullet)
=I_{\mathcal F_3}
+\frac{C^*C|_{\mathcal F_3}}{S_\bullet}
+\frac{(C^*)^2C^2|_{\mathcal F_3}}{2S_\bullet^2}.
$$
这里每个乘积都指 $\mathcal F_3$ 上的真压缩二次型，不假定
$\mathcal F_3$ 保持 $C^*$。已有完整 Schur 给
$$
\mathcal H_b(S_\bullet)
\preceq\mathcal H_{2,\bullet}
\preceq(1-\varepsilon_\bullet)^{-1}\mathcal H_b(S_\bullet),
\qquad
\varepsilon_\bullet=2z_x/S_\bullet .
\tag{1.3}
$$
对任意完整头源 $g$，令 $g_3=P_{\mathcal F_3}g$，则
$$
q_{2,\bullet}(g)
:=\|\Pi_{2,\bullet}(g\otimes\Omega)\|^2
=\langle g_3,\mathcal H_{2,\bullet}^{-1}g_3\rangle.
\tag{1.4}
$$
(1.4) 是全部零源短缩之后的真实物理投影；没有把单独的非零源图当成整个核。

## 2. 不含头条件数的完整物理截尾

因为 $S_f=(1-t)S$，三个正项逐一比较给
$$
\mathcal H_b(S_f)
\preceq(1-t)^{-2}\mathcal H_b(S).
$$
结合 (1.3)，
$$
\mathcal H_{2,y}
\preceq
\frac{1}{(1-\varepsilon_f)(1-t)^2}\,
\mathcal H_{2,\infty}.
$$
所有矩阵都至少为恒等；取正逆并使用 (1.4)，得到
$$
\boxed{
q_{2,y}(g)\ge
(1-\varepsilon_f)(1-t)^2q_{2,\infty}(g).
}
\tag{2.1}
$$
再由真正物理包含 (1.1)，投影差的平方恰为范数平方之差：
$$
\begin{aligned}
\|(\Pi_{2,\infty}-\Pi_{2,y})i_0g\|^2
&=q_{2,\infty}(g)-q_{2,y}(g)\\
&\le
[1-(1-\varepsilon_f)(1-t)^2]q_{2,\infty}(g)\\
&\le(\varepsilon_f+2t)\|g\|^2 .
\end{aligned}
\tag{2.2}
$$
这是同一物理内积中的完整投影比较，不是仅比较某个核列的坐标，也没有先对
$C^\dagger$ 或 $(CC^*)^\dagger$ 取环境范数。

## 3. 原跨头参数和真实 carry 修复

取 $m\ge10$，$d_m=2^m$、偶数 $R_m$，令
$$
x_m=m+R_m,\qquad
x_m\ge d_m,\qquad
\log x_m\le13d_m^3,
$$
$$
y_m=(m+1)^4x_m,\qquad
y_m+6d_m\le x_{m+1}.
\tag{3.1}
$$
引用的原跨头定理给真实 N/Y 同一重分组
$$
A_{m+1}=A_m+b_mE_m+\Delta_m,\qquad
\|\Delta_m\|\le18\kappa_{m-1},
$$
$$
-\log\kappa_{m-1}
=\frac{175}{2}d_m^4-\frac{315}{4}d_m^3+150d_m .
\tag{3.2}
$$
这不是仅引用 $T-L_m$ 的整体尾界。

这里复写修复所需的最窄事实，说明它也适用于本稿的整个二孔核列。
若 $k$ 支撑于原有限位置 $[0,y_m)$ 且 $L_mk=0$，置
$$
A_0=A_m+b_mE_m,\quad A_1=A_{m+1},\quad
D_{\rm old}=D_{[m+1,y_m)},\quad r=\Delta_mk .
$$
$A_0^{d_m+1}=0$，$A_1^{2d_m}=0$；由原方程和独立尾交换，
$$
D_{\rm old}^j r=\Delta_m(-A_0)^jk .
$$
所以对 $B=A_1+D_{\rm old}$，准确有
$$
B^{3d_m}r=0.
\tag{3.3}
$$
这只要求 $k$ 是同一个有限物理真核向量，不要求其远孔恰为一孔。

在 fresh pool $[y_m,y_m+6d_m)$ 上，令 $N=6d_m$，
$$
v_q=\frac{(N-q)!}{N!}
\sum_{\substack{I\subset[y_m,y_m+N)\\|I|=q}}b_I^{-1}e_I,
\qquad 0\le q\le3d_m.
$$
逐位计数给
$$
D_{\rm pool}v_q=v_{q-1},\qquad
\|v_q\|^2\le
\frac{(N-q)!}{N!\,q!}\,b_{\min}^{-2q}.
\tag{3.4}
$$
于是
$$
Ur=\sum_{\ell=0}^{3d_m-1}(-B)^\ell r\otimes v_{\ell+1}
$$
满足 $(B+D_{\rm pool})Ur=r$。各 $\ell+1$ 孔层正交。
使用 (3.1)–(3.2) 的已付明确常数，
$$
\|Ur\|
\le18\kappa_{m-1}\sqrt{3d_m}\,
14^{3d_m}(y_m+6d_m)^{6d_m}\|k\|
\le e^{-9d_m^4}\|k\|.
\tag{3.5}
$$
故 $\widetilde k=k-Ur$ 是下一头的有限物理真核，并且
$$
\widetilde k\in\mathscr K_{0,m+1}
:=\ker C_{m+1}\otimes\Omega_{[x_{m+1},\infty)} .
\tag{3.6}
$$
(3.1) 的最后一式保留了所有 fresh 位均落在下一强头中的门。

## 4. 固定原首头的真实增益可和

取固定物理 $f_1=e_1$，$\|f_1\|=1$。它对所有上述 $m$ 都处于强头，
且原 N/Y 均有 $C_mf_1=e_0$、$C_me_0=0$。
定义
$$
q_{r,m}=\|\Pi_{r,m}f_1\|^2,\qquad r=0,1,2,
$$
其中 $\Pi_{r,m}$ 投到同一 $L_m$ 的远孔 $\le r$ 真核，
$\Pi_{0,m}$ 的空间为 (3.6) 中的旧 $m$ 版本。
这些核嵌套，所以 $0\le q_{0,m}\le q_{1,m}\le q_{2,m}\le1$。

置
$$
t_m=S_{y_m}/S_{x_m},\quad
\varepsilon_{f,m}=2z_{x_m}/(S_{x_m}-S_{y_m}),
$$
$$
e_m=\sqrt{\varepsilon_{f,m}+2t_m}+e^{-9d_m^4}.
\tag{4.1}
$$
连续权积分估计给
$$
t_m\le\frac8{(m+1)^{12}}\le\frac12,\qquad
\varepsilon_{f,m}\le\frac{12}{x_m+1}.
$$
因此
$$
e_m\le
\frac4{(m+1)^6}
+\sqrt{\frac{12}{x_m+1}}
+e^{-9d_m^4}.
\tag{4.2}
$$
在 (3.1) 的 $x_m\ge2^m$ 下，$\sum_m e_m<\infty$。

令 $k=\Pi_{2,y_m}f_1$。由 (2.2)、(3.5)，有
$\widetilde k\in\mathscr K_{0,m+1}$，且
$$
\|\widetilde k-\Pi_{2,m}f_1\|\le e_m .
$$
用投影的最小距离性质，
$$
\boxed{
q_{0,m+1}\ge q_{2,m}-(2e_m+e_m^2).
}
\tag{4.3}
$$
所以
$$
\boxed{
\sum_{m\ge m_0}(q_{2,m}-q_{0,m})
\le 1+\sum_{m\ge m_0}(2e_m+e_m^2)<\infty.
}
\tag{4.4}
$$
这个结论不要求 $f_1\in W$，也没有把逐个固定列收敛当作整个移动行的估计。
参数可取原 $\tau_{14}$ 切点，相关 $Q$ 母窗仍按引用跨头证明的原门槛独立使用。

## 5. 对唯一未付 qflat 源的准确已付部分

沿用同一个 $m$ 的原记号：
$$
K=\ker C,\quad G=(CC^*)^\dagger,\quad
\Gamma=P_KG|_K,\quad v=(I+S\Gamma)^{-1}e_0,
$$
$$
r=(I-P_K)Gv,\qquad
q_{\flat}=(C^{*2})^\dagger C^*r .
$$
令
$$
\mathcal U_3=\ker C^3\ominus\ker C^2.
$$
在完整二孔 Gram 相对
$\ker C^3=\ker C^2\oplus\mathcal U_3$ 的真正 Schur 中，记正矩阵为
$\mathcal S_3$。此前精确来源公式为
$$
q_{2,m}-q_{1,m}
=
\left\langle
P_{\mathcal U_3}C^*r,\,
\mathcal S_3^{-1}P_{\mathcal U_3}C^*r
\right\rangle .
\tag{5.1}
$$
由 (4.4) 立即得到
$$
\boxed{
\sum_m
\left\langle
P_{\mathcal U_{3,m}}C_m^*r_m,\,
\mathcal S_{3,m}^{-1}P_{\mathcal U_{3,m}}C_m^*r_m
\right\rangle<\infty .
}
\tag{5.2}
$$
这里没有以 $\mathcal S_3^{-1}$ 的环境范数放大来源。

其精确范围是
$$
P_{\mathcal U_3}C^*r=(C^2|_{\mathcal U_3})^*q_{\flat},
\qquad
\operatorname{Ran}(C^2|_{\mathcal U_3})
=K\cap\operatorname{Ran}C^2 .
$$
因此 (5.2) 支付的是这个真实 primitive 通道的完整 Schur 能量。
它不控制 $q_{\flat}$ 在 $\operatorname{Ran}C^2\ominus K$ 中的补，
也没有证明
$\sigma_2^2\|q_{\flat}\|^2$ 可和或有界。
原高旗、完整返回和帽来源仍须在同一源上继续处理，$N=M$ 仍未证明。

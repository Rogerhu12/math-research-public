# R271 附录：一位完整 Schur 的双恢复反馈与加权投影返回

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 并行一位构造的完整逆产生两个次序不同的头反馈源。本稿在同一个 $H_i^{-1}$ 源度量中同时支付它们，特别支付新头首源 $H_i a_{0,i}-g$ 的投影整行。对其中实际 creation 返回的指定源，再用已付创建合成行得到整个连续尾的原权加权投影交换误差。全部估计保同一完整 Schur 来源，不给任意头源或原 MP 返回一个环境逆界。

依据：[并行一位完整 Schur](R271-appendix-parallel-one-bit-schur-common-head-restoration-and-compressed-creation-row.md)、[一位正 commutator 因子](R271-appendix-one-bit-positive-commutator-and-complete-moving-source-occupation-row.md)、[删除正 Gram](R271-appendix-actual-low-end-forcing-positive-deletion-grams-and-compressed-adjoint-descendants.md)、[创建合成行](R271-appendix-adjoint-creation-synthesis-and-common-source-adjacent-flag-return.md)。

## 1. 同一真实来源与自然域

保原
$$
C=A_m+D_{[m,x)},\quad R=x-m,\quad d=2^m,\quad h=d+R,\quad C^h=0,
$$
$$
D=\sum_{i\ge x}b_iE_i,\quad b_i=(i+1)^{-2},\quad
z_i=b_i^2,\quad S=\sum_{i\ge x}z_i .
$$
取
$$
x\ge2,\qquad h\le2x,\qquad Q\ge R+h+1.
\tag{1.1}
$$
标准 $R=d,x=m+d,h=2d$ 满足这里的 $h\le2x$；其余原母窗门另保不变。

原强头真空嵌入仍记为 $i_0$。对
$E\in\{V_Q,K_Q,U_Q\}$ 置
$$
Z_E=P_Ei_0,\qquad G_E=Z_E^*Z_E .
$$
$U_Q=V_Q\ominus K_Q$，故这三个 $P_E$ 都是原物理正交投影。

固定 forcing $g$，使用并行稿同一个参数
$t\in[S,2S]$，并记
$$
s_i=S+t-z_i,\qquad u_i=z_i/s_i,\qquad
H_i=H_C(s_i),\qquad
T_i=H_i^{1/2}CH_i^{-1/2}/\sqrt{s_i}.
$$
第 $i$ 个新头为 $C_i=C+b_iE_i$，其完整最小来源是
$(a_{0,i},a_{1,i})$。令
$$
x_i=H_i^{1/2}a_{1,i}.
$$
可在所有后续 cut 之前选择同一个 $t$ 使
$$
\boxed{
\sum_i\|x_i\|^2\le V_g,\qquad
V_g=q_g(3S)-q_g(2S-z_x)\le\Delta_{g,Q}^2.
}
\tag{1.2}
$$
可同时保留并行 loss 加 gain 的更强预算；本稿只需要 (1.2)。

完整一位 Gram 是
$$
H_{C_i}(s_i)=
\begin{pmatrix}
H_i&(b_i/s_i)C^*H_i\\
(b_i/s_i)H_iC&
(1+u_i)H_i+(b_i^2/s_i^2)C^*H_iC
\end{pmatrix}.
\tag{1.3}
$$
因此两个非对角块的次序严格不同。

定义一 mode 的等距核列
$\mathcal I_i=\mathcal R_C(s_i)H_i^{-1/2}$。
它的像在 Fock 次数 $\le h-1$，并有
$T_i=-\mathcal I_i^*a\mathcal I_i$。所以
$$
\boxed{\|T_i\|^2=\|T_i^*\|^2\le h-1.}
\tag{1.4}
$$
这里仅在有限次数核列上使用闭 annihilator，域没有歧义。头空间虽可能很大，却仍是原有限强头；$H_i\ge I$ 的完整逆和平方根都是其真实算子，不是逐 birth 压缩逆。

## 2. 两个次序不同的恢复源同时可付

定义
$$
\boxed{
\sigma_i=\frac{b_i}{s_i}H_iCa_{1,i},
\qquad
\alpha_i=\frac{b_i}{s_i}C^*H_i a_{1,i}.
}
\tag{2.1}
$$
它们都是原共同头空间的向量。此处 $\sigma_i$ 是一个反馈源，不是 coherent 塔的标量归一因子。

同一个白化准确给
$$
H_i^{-1/2}\sigma_i=\sqrt{u_i}\,T_ix_i,\qquad
H_i^{-1/2}\alpha_i=\sqrt{u_i}\,T_i^*x_i.
\tag{2.2}
$$
特别不交换 $H_i$ 与 $C$，也不交换两种反馈源。

令
$$
M_x=\frac{h z_x}{2S-z_x}.
$$
原连续权有
$$
S\ge\int_{x+1}^{\infty}r^{-4}\,dr
=\frac1{3(x+1)^3},\qquad
\frac{z_x}{S}\le\frac3{x+1}.
$$
因而
$$
u_i(h-1)\le M_x
\le\frac{3h}{2x-1}\le\frac{6x}{2x-1}\le4 .
\tag{2.3}
$$

并行稿已经对同一个原 $Z_E$ 证明
$G_E\preceq H_i^{-1}$。结合 (1.2)、(2.2)，遂有
$$
\boxed{
\sum_i\|Z_E\sigma_i\|^2\le M_xV_g,\qquad
\sum_i\|Z_E\alpha_i\|^2\le M_xV_g,
\quad E=V_Q,K_Q,U_Q.
}
\tag{2.4}
$$
两行共同相加的右端至多 $8V_g$。这是真正恢复后的来源；没有估
$\|H_i\|\,\|Ca_{1,i}\|$ 或 $\|C^*H_i\|\,\|a_{1,i}\|$。

完整新源的第一行方程由 (1.3) 准确是
$$
H_i a_{0,i}+\alpha_i=g .
$$
因此首源反馈也已支付：
$$
\boxed{
\sum_i
\|Z_E(H_i a_{0,i}-g)\|^2
=\sum_i\|Z_E\alpha_i\|^2
\le M_xV_g.
}
\tag{2.5}
$$
(2.5) 保整个完整头源及同一个 $g$，不是只在某个低头子空间估计恢复。

## 3. 实际 creation 返回对三个原投影都成立

并行物理列 $F_i$ 及 $r_i=H_i a_{1,i}$ 满足
$$
P_E E_iF_i=Z_Er_i+P_EE_i^*i_0\sigma_i,
\qquad E=V_Q,K_Q,U_Q .
\tag{3.1}
$$
虽然并行稿将主式写在 $U_Q$ 上，(3.1) 对其余两投影并不需要新不变性：对新头来源 $(a_{1,i},0)$，
$$
H_{C_i}(s_i)\binom{a_{1,i}}0
=\binom{H_i a_{1,i}}{(b_i/s_i)H_iCa_{1,i}},
$$
再使用同一个真实低 forcing 恒等式即可分别得到 $P_{V_Q}$、$P_{K_Q}$ 版本。

该低门正是 (1.1)：对于 $j\le h$，
$$
(D_{\widehat i}^*)^j-(-C_i^*)^j
=L_m^*\sum_{k=0}^{j-1}
(D_{\widehat i}^*)^{j-1-k}(-C_i^*)^k .
$$
右侧中间 forcing 的原总尾孔至多 $R+j\le Q-1$，故被
$P_{V_Q}L_m^*$ 及 $P_{K_Q}L_m^*$ 杀掉。并未假设原 $V_Q$ 对 $C_i$ 或单个 $E_i$ 不变。

由并行原式，
$$
\sum_i\|E_iF_i\|^2\le V_g,\qquad
\sum_i\|Z_Er_i\|^2\le V_g .
$$
每个 $P_E$ 为收缩，所以 (3.1) 对三个原投影共同给
$$
\boxed{
\sum_i\|P_EE_i^*i_0\sigma_i\|^2\le4V_g.
}
\tag{3.2}
$$
这一步完整保留物理压缩，不把 Fock 投影的等式替成物理列的等式。

## 4. 原权加权的真实投影交换误差

对同一指定源 $\sigma_i$，记
$$
\mathcal R_{E,i}
=P_EE_i^*i_0\sigma_i-E_i^*Z_E\sigma_i .
\tag{4.1}
$$
此式保 $P_E$ 的准确位置。第二项通常有第 $Q+1$ 孔输出，本稿在原完整物理环境估计它，不偷偷重新截断。

先取有限指标族及任意 $|c_i|\le1$。由 (3.2) 和 $\sum b_i^2=S$，
$$
\left\|\sum_i b_ic_iP_EE_i^*i_0\sigma_i\right\|
\le2\sqrt{S V_g}.
\tag{4.2}
$$
对第二项使用真实创建合成行。置
$$
c_x=\frac43+\frac1{x+1}\le\frac53 .
$$
对 $E=V_Q$ 或 $K_Q$，原源度量给
$$
\left\|\sum_i b_ic_iE_i^*Z_E\sigma_i\right\|^2
\le c_x\sum_i b_i^2(i+1)\,
       \langle G_E\sigma_i,\sigma_i\rangle
\le3c_x S M_x V_g,
\tag{4.3}
$$
其中
$\sup_{i\ge x}b_i^2(i+1)=(x+1)^{-3}\le3S$。
对于 $U_Q$，先写 $Z_U=Z_V-Z_K$，再对两个真实来源使用 (4.3)，得到
$$
\left\|\sum_i b_ic_iE_i^*Z_U\sigma_i\right\|^2
\le12c_x S M_xV_g.
\tag{4.4}
$$
这里仍是 $G_V+G_K$ 的合法预算，没有使用未证的
$G_\Delta\preceq H_i^{-1}$。

由 $M_x\le4$、$c_x\le5/3$，得统一结论
$$
\boxed{
\sup_{|c_i|\le1}
\left\|\sum_{i\ge x}b_ic_i\mathcal R_{E,i}\right\|
\le11\sqrt{S V_g},
\qquad E=V_Q,K_Q,U_Q .
}
\tag{4.5}
$$
单独 $V_Q$ 或 $K_Q$ 可将 $11$ 改为 $7$。
精确中间常数分别是
$2+\sqrt{3c_xM_x}$ 与 $2+2\sqrt{3c_xM_x}$。

第一项的级数由 (4.2) 的 Cauchy 实际绝对范数收敛；第二项在创建合成的平方可和源域中收敛。由于其源尾能量可求和，有限部分和的尾界趋零。故 (4.5) 保无限连续尾，亦等价地蕴含对任意物理 $z$ 的绝对标量行
$$
\boxed{
\sum_{i\ge x}b_i
|\langle\mathcal R_{E,i},z\rangle|
\le11\sqrt{S V_g}\,\|z\|.
}
\tag{4.6}
$$
相位选择先用于有限和，再用非负极限，不需要假设整个向量级数绝对收敛。

## 5. 首源反馈的不同来源合成同样保原权

对 $\alpha_i$，(2.4) 已给与 $\sigma_i$ 相同的原源度量。
因此两者任取 $\xi_i\in\{\alpha_i,\sigma_i\}$，旧删除合成行给
$$
\boxed{
\sup_{|c_i|\le1}
\left\|\sum_{i\ge x}b_ic_i E_iZ_U\xi_i\right\|
\le8\sqrt{S V_g}.
}
\tag{5.1}
$$
证明先对 $Z_V,Z_K$ 分别用 $4/3$，再合并；其中唯一位置代价仍为
$\sup_i b_i^2(i+1)\le3S$。创建版本同理满足
$$
\sup_{|c_i|\le1}
\left\|\sum_i b_ic_i E_i^*Z_U\xi_i\right\|
\le4\sqrt5\,\sqrt{S V_g}.
\tag{5.2}
$$
这些是不同真实头来源的完整合成，不从逐列收敛推出总行。$\alpha_i$ 和 $\sigma_i$ 虽受同一上界，却不被视为同一向量；(2.5) 中首源反馈始终使用 $\alpha_i$。

## 6. 精确推进与仍保留的门

本稿已经支付三件同源事情：完整恢复后的 $\sigma_i,\alpha_i$ 行，原 $H_i a_{0,i}-g$ 的投影反馈行，以及指定 $\sigma_i$ 的真实创建投影交换误差。

这些来源由同一个一位 Schur 逆明确指定；(4.5) 不是任意 head 来源的
$[P_E,E_i^*]$ 算子范数，也没有把它直接认作
$E_iP_UF_i-P_UE_iF_i$ 的全部原返回。后一项或原完整 MP 帽测试若要使用本稿，仍需在保全相邻旗、零源 Schur 和实际 forcing 的条件下，准确识别其来源。普通 $N=M$ 未由此完成。

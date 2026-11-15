# 同一物理 gap 的内在跨切口耗散与固定测试配对

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明的结构性附录。** 既有物理夹逼已经给出全切口两费总和界，本稿不把该数值总界重计为新结论。新增的是：原同一固定测试的两费差源由**同一个递减物理 gap 投影本身的跨 $d$ 层下降**支付。若
$
g_q(f)=\langle f,\mathsf G_qf\rangle,\qquad
\mathsf G_q=P_{\mathcal M_q}-P_{\mathcal K_{q+d}},
$
则对 $q\ge s+d$ 有
$
\boxed{\Xi_q(e_q)^2\le4\{g_{q-d}(f)-g_q(f)\},}
$
$
\boxed{0\le g_q(f)-\mu_q(e_q)^2
\le2\{g_{q-d}(f)-g_q(f)\}.}
$
真正 bare 与普通完整右费分别保持原定义；没有把二者互换。本稿不提供 $g_q$ 的移动窗口衰减率，也不支付正向 gauge 恢复。

来源与已有范围：

- [原首物理头商、准确 $L+B$ 与两右链](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)；
- [同一物理 $\mathcal M_q$ 的闭和、支撑和 Riesz 源](2026-11-14-physical-joined-decreasing-projections-and-fixed-test-bare-budget-789f-next.md)，尤其 §§2–3；
- [物理夹逼与同源三费](2026-11-14-physical-joined-sandwich-and-same-increment-three-fee-fixed-test-budget-789f-next.md)，尤其 §§1、3–6。

## 1. 同一物理空间、闭空间与原测试

固定原 $m,d=2^m,A=A_m,D=D_m$，令
$
\mathcal H=\mathbb C^d\otimes\bigoplus_{p\ge0}\mathcal H_p,\qquad
C=A+D,\qquad \mathcal K=\ker C .
$
这是原全部物理头和平方自由尾空间。原 $b_j=(j+1)^{-2}\in\ell^1$，故 $D,C$ 在此全孔 Hilbert 空间上有界。

记
$
E_{h,p}=\ker D^h\cap\mathcal H_p,\qquad
\mathcal K_q=\mathcal K\cap\mathcal H_{\le q},
$
$
\mathcal H_{{\rm hi},q}
=\mathbb C^d\otimes\bigoplus_{p\ge q+2}E_{p-q-1,p},
\qquad
\mathcal M_q=\mathcal K+\mathcal H_{{\rm hi},q}.
\tag{1.1}
$
引用稿已用完整首头提升证明代数和闭，并且
$
\mathcal M_q=\ker(Q_qC),\qquad
Q_q=P_{\mathcal H_{{\rm hi},q}^{\perp}}.
\tag{1.2}
$
因此 $\mathcal M_q$ 递减，$\mathcal K_q$ 递增，且
$
\mathcal K_{q+d}\subseteq\mathcal M_q.
\tag{1.3}
$
这里的 $\mathcal M_q$ 是同一物理空间中的闭和；没有把原商核当成物理 $\ker C$。

固定 $f\in\mathcal H_{\le s}$。对 $q\ge s$，令
$
z_q=P_{\mathcal M_q}f,\qquad k_q=P_{\mathcal K_q}f.
\tag{1.4}
$
由于 $f\perp\mathcal H_{{\rm hi},q}$，其 joined 投影 $z_q$ 也是原商的最小物理代表。完整首头公式给
$
\boxed{\operatorname{supp}_{\rm holes}z_q\subseteq[0,q+d].}
\tag{1.5}
$
这条实际支撑界是下面跨切口估计的输入，不是额外的截断或重选源。

在每个固定 $(m,q)$ 的原源空间保留
$
L_q=U_q^*U_q,\qquad B_q=\mathcal A_q^*\mathcal A_q,\qquad
G_q^{-1}=(\mathcal C_q^{\min})^*\mathcal C_q^{\min}.
$
其中 $U_q$ 是真正左最小逆，$\mathcal A_q$ 是**整个原 bare 最小右链**，$\mathcal C_q^{\min}$ 是普通完整右最小链。全部固定层受限逆及旗的自然域沿原文；本稿不使用全孔 $D^\dagger$ 有界。

相应费用为
$
\mu_q(r)^2=\langle L_qr,r\rangle,\quad
\alpha_q(r)^2=\langle B_qr,r\rangle,\quad
\lambda_q(r)^2=\langle G_q^{-1}r,r\rangle,
$
$
\lambda_{{\rm flat},q}(r)^2=\langle G_qL_qr,L_qr\rangle,
\qquad \Xi_q(r)^2=\alpha_q(r)^2+\lambda_{{\rm flat},q}(r)^2 .
\tag{1.6}
$
普通 $\lambda_q$ 不属于 $\Xi_q$ 的定义。

令 $t_q$ 为原固定测试伴随流的同一源。原 Riesz 身份是
$
z_q=(k_q+U_qu_q^{\rm b},-\mathcal A_qu_q^{\rm b}),
\qquad u_q^{\rm b}=(L_q+B_q)^{-1}L_qt_q,
$
$
k_{q+d}=(k_q+U_qu_q^{\rm f},-\mathcal C_q^{\min}u_q^{\rm f}),
\qquad u_q^{\rm f}=(L_q+G_q^{-1})^{-1}L_qt_q.
\tag{1.7}
$
左右分块是原物理孔层 $\le q$ 与 $>q$。以下始终用这两个同源最小者，置
$
e_q=u_q^{\rm b}-u_q^{\rm f},\qquad
h_q=\mathcal A_qu_q^{\rm b}-\mathcal C_q^{\min}u_q^{\rm f}.
\tag{1.8}
$

## 2. 同一个 gap 的正交差

由 (1.3)，
$
\mathsf G_q=P_{\mathcal M_q}-P_{\mathcal K_{q+d}}
\tag{2.1}
$
是正交投影。其像是
$\mathcal M_q\cap\mathcal K_{q+d}^{\perp}$，随 $q$ 递减。因此
$\mathsf G_{q-d}-\mathsf G_q$ 也是正交投影。

对 $q\ge s+d$，定义
$
\mathfrak d_q(f)=g_{q-d}(f)-g_q(f),\qquad
g_q(f)=\|\mathsf G_qf\|^2.
\tag{2.2}
$
准确有
$
\mathsf G_{q-d}-\mathsf G_q
=(P_{\mathcal M_{q-d}}-P_{\mathcal M_q})
 +(P_{\mathcal K_{q+d}}-P_{\mathcal K_q}).
\tag{2.3}
$
右边第一项的像正交于整个 $\mathcal K$，第二项的像包含于 $\mathcal K$，所以它们正交。由此
$
\boxed{\mathfrak d_q(f)
=\|z_{q-d}-z_q\|^2+\|k_{q+d}-k_q\|^2.}
\tag{2.4}
$

现在直接使用 (1.5)：$z_{q-d}$ 支撑至多 $q$，所以
$
P_{>q}z_q=-P_{>q}(z_{q-d}-z_q).
$
由 (1.7)，得到
$
\boxed{\alpha_q(u_q^{\rm b})^2
\le\|z_{q-d}-z_q\|^2.}
\tag{2.5}
$
另一方面，真正有限核的两个物理部分正交，故
$
\mu_q(u_q^{\rm f})^2+\lambda_q(u_q^{\rm f})^2
=\|k_{q+d}-k_q\|^2.
\tag{2.6}
$
合并即得本附录的基础预算
$
\boxed{
\alpha_q(u_q^{\rm b})^2+
\mu_q(u_q^{\rm f})^2+
\lambda_q(u_q^{\rm f})^2
\le\mathfrak d_q(f).
}
\tag{2.7}
$
所有形式都在当前切口 $q$ 计算；没有把不同切口的源度量识别为同一个矩阵。

## 3. 同源两费与主左能量之间的准确缺项

由 (1.7)–(1.8)，
$
\mathsf G_qf=z_q-k_{q+d}=(U_qe_q,-h_q).
$
因此
$
\boxed{g_q(f)=\mu_q(e_q)^2+\|h_q\|^2.}
\tag{3.1}
$
一次 Hilbert 空间二次不等式与 (2.7) 给
$
\|h_q\|^2
\le2\{\alpha_q(u_q^{\rm b})^2+
              \lambda_q(u_q^{\rm f})^2\}
\le2\mathfrak d_q(f).
\tag{3.2}
$
所以
$
\boxed{0\le g_q(f)-\mu_q(e_q)^2
\le2\mathfrak d_q(f).}
\tag{3.3}
$

原物理夹逼稿 §4 已证明同一个未来差的两个真实投影为
$
P_{{\rm b},\min}h_q=\mathcal A_qe_q,\qquad
P_{\rm f}h_q=-F_{\rm f}^*L_qe_q.
\tag{3.4}
$
第二式给的是原 flat 链，不是普通右最小链。两个投影各自收缩，不要求相互正交，于是
$
\Xi_q(e_q)^2\le2\|h_q\|^2.
$
与 (3.2) 合并，
$
\boxed{\Xi_q(e_q)^2\le4\mathfrak d_q(f).}
\tag{3.5}
$

同一源正规方程还给
$
(L_q+B_q)e_q=(G_q^{-1}-B_q)u_q^{\rm f}.
$
原首源头约化 $B_q,G_q$，且该头上 $G_q^{-1}=B_q$，故 $e_q$ 仍属于原首头负图。这里没有改用任意负图投影，也没有扩大旧联合旗的适用窗口。

## 4. 原固定测试功能也由该 gap 差支付

对任意同切口原源 $r$，两个 Riesz 方程给准确等式
$
\langle L_qr,t_q-e_q\rangle
=\langle B_qr,u_q^{\rm b}\rangle
 +\langle L_qr,u_q^{\rm f}\rangle.
\tag{4.1}
$
第一项用真正 bare Cauchy；第二项用同一个 $G_q$ 的
flat／普通右 Cauchy：
$
|\langle L_qr,u_q^{\rm f}\rangle|
\le\lambda_{{\rm flat},q}(r)\lambda_q(u_q^{\rm f}).
$
再用二维 Cauchy 与 (2.7)，
$
\boxed{
|\langle L_qr,t_q-e_q\rangle|
\le\Xi_q(r)\sqrt{\mathfrak d_q(f)}.
}
\tag{4.2}
$
因此这一新差分资源仍保留原同一固定测试的功能，不是把 $t_q$ 或实际 $r$ 换成另一个来源。

(4.2) 不提供 $\mu_q(t_q-e_q)^2\le\mathfrak d_q(f)$；
原左误差的已付界仍按先前夹逼稿的 $\Delta_q(f)$ 使用。
二者不能仅因都可求和而逐切口互换。

## 5. 真正的 gap 尾和与尚未支付的速率

对任意 $q_0\ge s+d$ 和整数 $N\ge0$，
$
\sum_{\ell=0}^{N}\mathfrak d_{q_0+\ell d}(f)
=g_{q_0-d}(f)-g_{q_0+Nd}(f).
\tag{5.1}
$
所以本稿给出的尾预算是
$
\boxed{
\sum_{\ell\ge0}\Xi_{q_0+\ell d}(e_{q_0+\ell d})^2
\le4g_{q_0-d}(f),
}
\tag{5.2}
$
$
\boxed{
\sum_{\ell\ge0}
\bigl[g_{q_0+\ell d}(f)
 -\mu_{q_0+\ell d}(e_{q_0+\ell d})^2\bigr]
\le2g_{q_0-d}(f),
}
\tag{5.3}
$
以及 (2.7) 三项之和的同网格尾预算至多 $g_{q_0-d}(f)$。
对全部 $q\ge Q\ge s+d$，按 $d$ 个余类求和，可分别把右边改成
$4d\,g_{Q-d}(f)$、$2d\,g_{Q-d}(f)$、$d\,g_{Q-d}(f)$。

固定 $m$ 时，既有闭空间证明给 $\mathsf G_q\to0$ 强收敛；
(5.1) 可以相应取到零终点。这里没有额外交换任何 $m,q$ 极限。
新的结构是费用由同一个 $g_q$ 的下降支付，而不是仅再给一个
$\sum\Xi^2\le C d\|f\|^2$ 的数值估计。

特别，(3.3) 允许主 $\mu_q(e_q)^2$ 接近尚未衰减的 $g_q(f)$。
(3.5) 的可求和性不提供 $g_q(f)$ 在 $q\le\exp(26d^3)$
或旧联合旗窗口中的定量衰减率；也不控制正向 gauge 的两个共同恢复项。
原主左配对、完整高返回与普通边界 $N=M$ 仍未完成。

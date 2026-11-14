# R234 附录：全部固定孔层的真实形式原像与三次正则核饱和

日期：2026-11-13（Asia/Taipei）。作者：boundary。状态：以下各节已证明；全次数无权平方和仍开放。

本稿先用一个实际高位右逆把 R234 的固定次数估计合法传到未知缺陷的形式原像，再构造与稳定闭像 $N$ 相容的右逆。所有正三次孔次数正则核均落在 $N$；因此 R234 原始右逆与有限三角右逆之差也确在 $N$。最后给出真实 carry 在每个固定输出次数上的绝对范数求和。

**后续预算加强：** [第二附录](R234-appendix-quartic-head-powers-and-super-four-thirds-hole-weights.md) 保持本稿构造不变，已把三次权扩到每个 $p>4/3$，并给真正缺陷的次数尾必要下界。

## 1. 输入与形式配对

取 $T=T_N$ 或 $T=T_Y$，并记
$$
H_-=\ell^2(\mathbb N_0),\qquad
M=\ker T,\qquad N=\overline{BM},\qquad W=M\ominus N.
$$
第 $q$ 孔次数层为 $H_q$，投影为 $\mathsf P_q$；有限整数头仍写 $\mathcal F_m$，其投影写 $\Pi_m$。

固定 $w\in W$。旧结论给唯一逐行形式序列 $h$，满足 $T^*h=w$。暂不假设 $h\in H_-$。内积对第一变量线性。对每个有限整数支持的 $v$，由 $T$ 的形式首阶为 1，可解一个有限三角方程，取有限向量 $J_Tv$ 使 $TJ_Tv=v$。因此逐行有限和给
$$
\boxed{\langle h,v\rangle=\langle w,J_Tv\rangle.}
\tag{1.1}
$$
这里左侧只对有限 $v$ 使用。

R200 已证
$$
\boxed{M\cap\operatorname{Ran}B
=BM\mathbin{\dotplus}\mathbb Ce_0\subseteq N.}
\tag{1.2}
$$
特别，(1.2) 没有假设 $N=M$。

定义
$$
\mathscr X_c=
\left\{f:\|f\|_{\mathscr X_c}
=\sum_{q\ge0}e^{c(q+1)^3}\|\mathsf P_qf\|<\infty\right\},
\qquad c>0.
\tag{1.3}
$$
R234 的空间是 $\mathscr X_1$，它给实际有界右逆
$$
\mathcal G_1:\mathscr X_1\to H_-,
\qquad T\mathcal G_1=I.
$$
记 $C_1=\|\mathcal G_1\|_{\mathscr X_1\to H_-}<\infty$。

## 2. 高位夹置使所有完整固定次数层平方可和

实际递推
$$
N_i=E_i+\eta_iE_i^*N_{i+1},\qquad \|N_i\|=1
$$
给出：若 $v$ 的第 $i$ 位真空，则
$$
\boxed{N_iE_i^*v=v.}
\tag{2.1}
$$
首项 $E_iE_i^*v=v$；第二项中 $N_{i+1}$ 保持第 $i$ 位，而 $E_i^*$ 已将该位置为占据，再作用一次 $E_i^*$ 为零。因此 (2.1) 是实际等式，没有舍弃 carry。

给定有限 $v\in H_q$，选 $i$ 超过它的全部孔位，令
$$
u_i=N_i\mathcal G_1E_i^*v.
\tag{2.2}
$$
由于 $E_i^*v\in H_{q+1}$，此式在 R234 的真实域内，并且
$$
\|u_i\|\le C_1e^{(q+2)^3}\|v\|,
\qquad
Tu_i=N_iT\mathcal G_1E_i^*v=N_iE_i^*v=v.
\tag{2.3}
$$
这里使用 $T$ 与 $N_i$ 交换。

同时
$$
u_i\in\operatorname{Ran}N_i
=\operatorname{Ran}B^{2^i}\subseteq\operatorname{Ran}B.
$$
有限 $J_Tv$ 也有有限 $B$ 右移原像。因此
$$
\boxed{u_i-J_Tv\in M\cap\operatorname{Ran}B\subseteq N.}
\tag{2.4}
$$
由 $w\perp N$ 与 (1.1)，
$$
|\langle h,v\rangle|
=|\langle w,u_i\rangle|
\le C_1e^{(q+2)^3}\|w\|\,\|v\|.
\tag{2.5}
$$
虽然 $i$ 随有限测试 $v$ 改变，右侧常数完全不依赖 $i$、最大孔位或测试支撑。有限向量在完整 $H_q$ 稠密，故 Riesz 表示给实际向量 $h_q\in H_q$，其坐标与形式 $h$ 的第 $q$ 层相同，且
$$
\boxed{\|h_q\|\le C_1e^{(q+2)^3}\|w\|
\qquad(q\ge0).}
\tag{2.6}
$$
这覆盖整个二孔层及任意固定孔层，允许孔位无限远。

一般地，若一个实际右逆在 $H_{q+1}$ 上的范数界是 $b_{q+1}$，同一证明便给 $\|h_q\|\le b_{q+1}\|w\|$。没有对未定义的全空间形式向量擅自取伴随。

## 3. 同一个 R234 构造适用于任意较小正三次权

R234 固定
$$
m(q)=10+\lceil\log_2(q+1)\rceil,\qquad d(q)=2^{m(q)},
$$
以及 $R_q:H_q\to H_-$，并已证明
$$
\log M_q=O((q+1)^2\log(q+2)),\qquad \|R_q\|\le M_q,
\tag{3.1}
$$
$$
\|(TR_q-I)v\|_{\mathscr X_1}
\le2e^{-40d(q)^4}\|v\|.
\tag{3.2}
$$
以下保留每个原有 $R_q$，不改变其局部右逆和 carry 计算。

对每个 $0<c\le1$，由 (3.1) 有
$$
C_R(c):=\sup_q M_qe^{-c(q+1)^3}<\infty.
$$
所以
$$
R=\sum_qR_q\mathsf P_q:\mathscr X_c\to H_-
$$
有界。又 $\mathscr X_c$ 范数不超过 $\mathscr X_1$ 范数，故由 (3.2)，逐层绝对求和给 $E=TR-I$ 在 $\mathscr X_c$ 上有界，且
$$
\boxed{
\|E\|_{\mathscr X_c\to\mathscr X_c}
\le\sup_q2e^{-40d(q)^4-c(q+1)^3}
\le2e^{-40\cdot1024^4}<\frac14.
}
\tag{3.3}
$$
因此同一 Neumann 公式
$$
\boxed{
\mathcal G_c=R(I+E)^{-1}:\mathscr X_c\to H_-,
\quad T\mathcal G_c=I,\quad
\|\mathcal G_c\|\le\tfrac43 C_R(c)
}
\tag{3.4}
$$
成立。各扩张在共同定义域上一致：例如对 $\mathscr X_1$ 的输入，$E$ 的逐层和、Neumann 的每一项及其 $H_-$ 极限都与原构造相同。

重复第 2 节立即给
$$
\|h_q\|\le\|\mathcal G_c\|e^{c(q+2)^3}\|w\|,
\qquad 0<c\le1.
\tag{3.5}
$$
第 6 节将去掉这里的次数平移。

## 4. 与 $N$ 相容的实际右逆

记 $\mathscr X_c^+$ 的范数为
$$
\|f\|_{\mathscr X_c^+}
=\sum_{q\ge0}e^{c(q+2)^3}\|\mathsf P_qf\|.
\tag{4.1}
$$
对每个 $i$ 定义
$$
C_i=N_i\mathcal G_cE_i^*:\mathscr X_c^+\to H_-.
$$
纯创建 $E_i^*$ 在每个 $q$ 层的范数不超过 1，并将其送到 $q+1$ 层，所以
$$
\sup_i\|C_i\|\le\|\mathcal G_c\|.
\tag{4.2}
$$
真实等式 $N_iE_i^*=I-E_i^*E_i$ 给
$$
TC_i=I-E_i^*E_i.
\tag{4.3}
$$
对每个固定 $\mathscr X_c^+$ 向量，右侧强趋于 $I$：先对有限整数支持检查，再用占据投影在该范数中为压缩及有限支持稠密。

$\mathscr X_c^+$ 可分，$H_-$ 自反。对一个稠密可数测试集逐一选弱收敛子列，再用 (4.2) 延拓，得到弱算子聚点
$$
C_c:\mathscr X_c^+\to H_-,
\qquad
\|C_c\|\le\|\mathcal G_c\|,\qquad TC_c=I.
\tag{4.4}
$$
没有要求 $C_i$ 强收敛。

若 $v$ 有限，则 $i$ 充分大时，第 2 节给 $C_iv-J_Tv\in N$。闭线性子空间 $N$ 弱闭，因而
$$
C_cv-J_Tv\in N\qquad(v\text{ 有限}).
\tag{4.5}
$$
对任意有限 $x$，$Tx$ 仍有限，而 $x-J_T(Tx)$ 是有限核向量，属于 $\mathbb Ce_0\subset N$。结合 (4.5)，得到
$$
\boxed{x-C_cTx\in N\qquad(x\text{ 有限}).}
\tag{4.6}
$$

## 5. 任意正三次孔次数正则核均属于 $N$

先验证所需的实际连续性。R234 给局部
$$
K_L=T^{[L+1]}-T^{[L]},\qquad
\|K_L\|\le52e^{-770\,16^{L-1}},
\tag{5.1}
$$
且 $K_L$ 只作用前 $L+1$ 位，因此最多改变 $L+1$ 个孔。两个符号都有
$$
T^{[1]}=D=\sum_ja_jE_j,
\qquad T=D+\sum_{L\ge1}K_L.
\tag{5.2}
$$

固定 $c>0$，取 $0<\varepsilon<\min(c,1)$。对输入 $v_q\in H_q$，有
$$
\|K_Lv_q\|_{\mathscr X_\varepsilon^+}
\le\sqrt{q+L+2}\,
e^{\varepsilon(q+L+3)^3}\|K_L\|\,\|v_q\|.
\tag{5.3}
$$
存在只依赖 $\varepsilon,c$ 的常数 $A,C$，使
$$
\sup_{q\ge0}
\sqrt{q+L+2}\,
e^{\varepsilon(q+L+3)^3-c(q+1)^3}
\le Ce^{A(L+2)^3}.
\tag{5.4}
$$
为核对 (5.4)，取 $\varepsilon<\varepsilon'<c$，先用
$\sqrt{t+s}\le C e^{(\varepsilon'-\varepsilon)(t+s)^3}$；
再令 $t=q+1$、$s=L+2$。函数
$\varepsilon'(y+1)^3-cy^3$ 在 $y\ge0$ 有有限上界，齐次性即给 (5.4)。

因为 $e^{-770\,16^{L-1}}$ 压倒 $e^{A(L+2)^3}$，(5.1)—(5.4) 按算子范数绝对求和，得到
$$
\boxed{T:\mathscr X_c\to\mathscr X_\varepsilon^+\text{ 有界}.}
\tag{5.5}
$$
纯 $D$ 只降低一个孔且 $\|D\|<2$，它的同一连续性直接成立。这一证明支付了全部实际 carry，不能仅用 $T$ 的无权有界性替代。

若 $f\in M\cap\mathscr X_c$，令有限头 $f_m=\Pi_mf$。$\Pi_m$ 与次数投影交换，逐层强收敛，并由 $\mathscr X_c$ 的可和范数控制，所以 $f_m\to f$ 于 $\mathscr X_c$。由 (5.5)，$Tf_m\to Tf=0$ 于 $\mathscr X_\varepsilon^+$。第 4 节给
$$
f_m-C_\varepsilon Tf_m\in N,
$$
而左侧在 $H_-$ 中趋向 $f$。因此
$$
\boxed{M\cap\mathscr X_c\subseteq N
\qquad\text{对每个 }c>0.}
\tag{5.6}
$$
这里没有声称 $M\cap\mathscr X_c$ 在 $M$ 中稠密。

## 6. R234 原始右逆的有限测试差也确实属于 $N$

R234 的 $R_q$ 输出次数不超过
$$
r_q=q+m(q)+d(q).
$$
其数值范围给一个统一的简单界
$$
r_q+1\le4096(q+1).
\tag{6.1}
$$
例如 $d(q)<2048(q+1)$、$m(q)\le d(q)/2$、$q+1\le d(q)/1024$ 足以推出 (6.1)。

固定 $0<c\le1$，取
$$
\gamma=\frac{c}{4\cdot4096^3}>0.
$$
由 (6.1) 和逐层 Cauchy–Schwarz，
$$
\|R_qv\|_{\mathscr X_\gamma}
\le\sqrt{r_q+1}\,e^{\gamma(r_q+1)^3}M_q\|v\|.
$$
利用 (3.1) 的 $\log M_q=o(q^3)$，右侧至多为
$C_ce^{c(q+1)^3}\|v\|$，其中 $C_c$ 与 $q$ 无关。因此
$$
R:\mathscr X_c\to\mathscr X_\gamma
\quad\text{有界}.
\tag{6.2}
$$
$E$ 在 $\mathscr X_c$ 上严格收缩，所以
$$
\boxed{\mathcal G_c:\mathscr X_c\to\mathscr X_\gamma
\quad\text{也有界}.}
\tag{6.3}
$$

对每个有限 $v$，$\mathcal G_cv-J_Tv\in M\cap\mathscr X_\gamma$，故由 (5.6)，
$$
\boxed{\mathcal G_cv-J_Tv\in N.}
\tag{6.4}
$$
特别 $c=1$ 时，(6.4) 正是 R234 §7 原先待补的条件 (7.4)，现在对其原始 $\mathcal G_T$ 已成立。

所以有限 $v\in H_q$ 满足
$$
\langle h,v\rangle=\langle w,\mathcal G_cv\rangle.
$$
这次 $\mathcal G_c|_{H_q}$ 是一个固定有界 Hilbert 空间映射；有限测试稠密后可合法写
$$
\boxed{
h_q=(\mathcal G_c|_{H_q})^*w,\qquad
\|h_q\|\le\|\mathcal G_c\|e^{c(q+1)^3}\|w\|.
}
\tag{6.5}
$$
式 (6.5) 对每个 $0<c\le1$ 成立，但常数 $\|\mathcal G_c\|$ 可以依 $c$ 增大。

## 7. 真实 carry 在每个固定输出层的 Hilbert 范数和

固定输出次数 $q$，定义实际 Hilbert 向量
$$
z_{L,q}=\mathsf P_qK_L^*
\left(\sum_{p=0}^{q+L+1}h_p\right).
\tag{7.1}
$$
高于 $q+L+1$ 的输入次数不能被局部 $K_L^*$ 送到 $q$ 层，因此这里包含该输出的全部形式源。

由 (6.5)，例如取 $c=1$，得到
$$
\boxed{
\|z_{L,q}\|
\le52\|\mathcal G_1\|\,\|w\|\sqrt{q+L+2}\,
e^{-770\,16^{L-1}+(q+L+2)^3}.
}
\tag{7.2}
$$
对每个固定 $q$，(7.2) 对 $L$ 绝对可和，所以
$\sum_{L\ge1}z_{L,q}\in H_q$。

逐整数坐标上，这正是 $(T^*-D^*)h$：$K_L$ 严格杀掉 $\mathcal F_L$，所以 $K_L^*$ 在低于 $2^L$ 的输出行全部为零；每个固定输出行只涉及有限个 $L$。因此范数极限与既有形式三角方程一致，得到真正的 $H_q$ 等式
$$
\boxed{
\mathsf P_qw=D^*h_{q-1}+\sum_{L\ge1}z_{L,q},
\qquad h_{-1}=0.
}
\tag{7.3}
$$
式 (7.2) 也给删去 $L<m$ 后的明确尾预算，并对固定 $q$ 随 $m\to\infty$ 趋于零。

旧 carry 反例的形式数组仅满足有限头增长及每个固定低头加单高孔的平方和；它的高孔层范数有 $\alpha_j^{-1}$ 量级，不满足 (6.5)。因此该反例不与本稿的新 Hilbert 层结论冲突。

## 8. 剩余缺口

已经严格得到全部固定孔层 $h_q\in H_q$、任意小正三次权下的层界、R234 原始右逆的有限测试差属于 $N$，以及每个固定输出层真实 carry 的绝对范数和。

仍不能从 (6.5) 推出 $\sum_q\|h_q\|^2<\infty$，也不能在 (7.2) 未控制 $q$ 依赖时再对全部输出层求和。式 (5.6) 只覆盖正三次孔次数正则核，不证明这一类在整个 $M$ 中稠密。必须进一步控制跨次数截断的能量通量，或直接排除、构造 $W$，才能决定 $N=M$。原 Haar 问题同样未完成。

# 工作笔记：左侧最小源 Gram 与一个由真实未来带支付的右修复源

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf。
状态：已核工作接口；root、normal、kernel 全文核查。不作为无权能量上界或独立主定理登记。

本笔记继续[完整链与降孔](../results/R271-appendix-complete-repair-chain-lowering-defects-and-true-schur-contraction.md)、[真实头移段](2026-11-13-actual-narrow-head-flux-shifts-and-paid-last-source-1cf.md)以及[首段先消元](../results/R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)。
新接口保留完整左源的真实 Hilbert Gram。下文小费用属于明确变换源，不把它改称原返回源。

## 1. 同一模型与左侧源空间

固定同一个 $m\ge5$、$d=2^m$ 及整数
$$
4d\le q\le e^{d^3/4}.
$$
取两个实际边界之一，记
$$
L=A_m+D_m,\qquad
D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad
W=M\ominus N.
$$
所有孔层和头基均为原模型的物理正交分解。
右修复继续记作
$$
\mathcal R_q=F_q^*G_q^{-1}:\mathscr R_q\longrightarrow\mathscr C_q\cap\ker S_q,
\qquad G_q=F_qF_q^*,
$$
其中
$$
\mathscr R_q
=\bigoplus_{i=0}^{d-2}
e_i\ker(D_m^{d-i-1}|_{\mathcal H_q^{(m)}}),
\qquad
\|\mathcal R_q\|\le e^{d^4}.
$$
$F_q$ 是内部零链上的首输出；其范数至多 $\|D_m\|\le1/m<1$。

定义完整左空间
$$
\mathscr V_q
=\{v\in P_{\le q}^{(m)}H:P_{<q}^{(m)}Lv=0\},
\qquad
E_qv=A_mv_q.
\tag{1.1}
$$
它是闭空间。对 $v\in\mathscr V_q$，内部方程给
$$
D_m^kv_q=(-A_m)^kv_{q-k}\qquad(0\le k\le q).
$$
由于 $A_m$ 严格下降物理头指标，
$$
(v_q)_i\in\ker D_m^{d-i},
\qquad E_qv\in\mathscr R_q.
\tag{1.2}
$$
这里只为 (1.2) 使用 $q\ge d$。下一节给 $E_q$ 到整个 $\mathscr R_q$ 的有界满射，因而可定义
$$
J_q=E_qE_q^*>0,\qquad
\mathcal V_q=E_q^*J_q^{-1}.
\tag{1.3}
$$
这是原范数中的左侧最小原像，不是任选的构造原像。
记
$$
\mu_q(r)=\|\mathcal V_qr\|.
$$
右、左孔支撑分离：
$$
\operatorname{supp}\mathcal V_qr\subset[0,q],
\qquad
\operatorname{supp}\mathcal R_qr\subset[q+1,q+d].
\tag{1.4}
$$

## 2. 与 q 无关、保全部头代价的真实左原像

[R249 §§1–4](../results/R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md)给实际上三角矩阵 $S_m$ 和正数 $\gamma_m$：
$$
A_m=S_m(\gamma_mJ_d)S_m^{-1},\qquad
J_de_i=e_{i-1},
$$
$$
\gamma_m=e^{20-L_m},\quad
L_m=\frac{25d^4}{2(d-2)},
$$
$$
\log\kappa_m\le\Psi_m
=L_m(d-1)-\omega_{d-1}+d\log12+2\log d,
\quad \kappa_m=\|S_m\|\|S_m^{-1}\|,
$$
$$
\omega_{d-1}
=\frac{20}{3}d^4-15d^3+(150m-275)d+\frac{850}{3}.
\tag{2.1}
$$
因为 $S_m,S_m^{-1}$ 都上三角，且逐头尾核阶随头指标递减，它们保持 (1.2) 的旗和 $\mathscr R_q$。

给定 $r\in\mathscr R_q$，置 $\widetilde r=S_m^{-1}r$。定义一个具体左原像，只有以下孔层非零：
$$
v^{\rm con}_{q-k}
=S_m\left[
(-1)^k\gamma_m^{-k-1}(J_d^*)^{k+1}D_m^k\widetilde r
\right],
\qquad 0\le k\le d-2.
\tag{2.2}
$$
每个尾核阶准确合法。若原项位于头 $i$，经 $(J_d^*)^{k+1}$ 后位于头 $i+k+1$；其尾属于
$$
\ker D_m^{d-i-1-k}
=\ker D_m^{d-(i+k+1)}.
$$
会越过头末端的原项已因 $D_m^k\widetilde r_i=0$ 消失。

在最上孔层，$\gamma_mJ_d(\gamma_m^{-1}J_d^*\widetilde r)=\widetilde r$。
在相邻孔层，(2.2) 的两个项
$\gamma_mJ_dv'_{q-k}+D_mv'_{q-k+1}$ 准确相消；所需
$J_d(J_d^*)^{k+1}=(J_d^*)^k$ 只在已核的无溢出支撑上使用。
最下端因 $D_m^{d-1}\widetilde r=0$ 没有额外输出。
因此
$$
Lv^{\rm con}=r,\qquad
v^{\rm con}\in\mathscr V_q.
\tag{2.3}
$$
这证明 $E_q$ 满射。不同 $k$ 位于正交孔层，所以
$$
\|\mathcal V_q\|
\le\|r\mapsto v^{\rm con}\|
\le\kappa_m
\left(\sum_{k=0}^{d-2}\gamma_m^{-2k-2}\|D_m\|^{2k}\right)^{1/2}
\le\sqrt d\,\kappa_m\gamma_m^{-(d-1)}.
\tag{2.4}
$$
最后只用 $\gamma_m<1$、$\|D_m\|\le1$。

保留 (2.1) 的实际常数后，
$$
\begin{aligned}
\log(\sqrt d\,\kappa_m\gamma_m^{-(d-1)})
&\le
\left(\frac{55}{3}+\frac{25}{d-2}\right)d^4+15d^3\\
&\quad-(150m-255-\log12)d-\frac{790}{3}
+\frac52\log d\\
&<20d^4\qquad(m\ge5).
\end{aligned}
\tag{2.5}
$$
最后一行可直接用 $d\ge32$：
$55/3+25/30+15/32<20$，剩余一行对 $m\ge5$ 为负。
于是
$$
\boxed{\|\mathcal V_q\|\le e^{20d^4}.}
\tag{2.6}
$$
这个界不含 $q$；它并不隐藏头条件数。

## 3. 所有同源有限核的真实 W 投影

对任意 $r\in\mathscr R_q$，
$$
k_q(r)=\mathcal V_qr-\mathcal R_qr
$$
满足 $Lk_q(r)=0$、孔支撑在 $[0,q+d]$。
同一窗口满足
$q+d\le e^{d^3/3}$，故已付 lift 到 $N$ 给
$$
\|P_Wk_q(r)\|\le e^{-75d^4}\|k_q(r)\|.
\tag{3.1}
$$
左右支撑正交，还准确有
$$
\|k_q(r)\|^2=\mu_q(r)^2+\lambda_q(r)^2.
\tag{3.2}
$$
使用 (2.6) 及原 $\|\mathcal R_q\|\le e^{d^4}$，
$$
\boxed{
\|P_W(\mathcal V_q-\mathcal R_q)\|
\le2e^{-55d^4}.
}
\tag{3.3}
$$
取完整伴随得到
$$
\boxed{
\|(\mathcal V_q^*-\mathcal R_q^*)P_W\|
\le2e^{-55d^4}.
}
\tag{3.4}
$$
这保留整个最小左/右算子；没有把某个 Gram 逆与 $P_W$ 交换。

## 4. 来自实际 w 的小费用变换源

取 $w\in W$，令
$$
v=P_{\mathscr V_q}w,\qquad r=E_qv,
\qquad
\beta_q=\|P_{[q+1,q+d]}^{(m)}w\|.
$$
这正是原低投影与原实际源。因为 $\mathcal V_q$ 的像在 $\mathscr V_q$，
$$
\boxed{\mathcal V_q^*w=J_q^{-1}r.}
\tag{4.1}
$$
定义同一源空间中的明确变换源
$$
\boxed{r_q^\flat=G_qJ_q^{-1}r.}
\tag{4.2}
$$
它的右侧最小费用准确为
$$
\lambda_q(r_q^\flat)
=\|G_q^{1/2}J_q^{-1}r\|.
\tag{4.3}
$$

另一方面，
$$
\mathcal R_q^*\mathcal R_q=G_q^{-1},
$$
所以 $G_q^{1/2}\mathcal R_q^*$ 是范数1的部分等距算子，且只读原右窗口。
因此
$$
\|G_q^{1/2}\mathcal R_q^*w\|\le\beta_q.
\tag{4.4}
$$
将 (3.4)、(4.1) 乘 $G_q^{1/2}$，并用
$\|G_q^{1/2}\|=\|F_q\|\le1$，得到
$$
\boxed{
\lambda_q(r_q^\flat)
\le\beta_q+2e^{-55d^4}\|w\|.
}
\tag{4.5}
$$
右端是真实未来带范数。没有声称 $r_q^\flat$ 等于同一 $w$ 的相邻源、某个 $D_3$ 源或原返回源。

还可准确识别左最小费用。$\ker E_q$ 是孔支撑不超过 $q$ 的有限 $L$ 核，故
$$
v-\mathcal V_qr=P_{\ker E_q}w,\qquad
\|v-\mathcal V_qr\|\le e^{-75d^4}\|w\|.
\tag{4.6}
$$
于是 $\mu_q(r)^2=\|v\|^2-\|P_{\ker E_q}w\|^2$。
此处极限明确取 $m\to\infty$、$d=2^m$ 及合法的 $q=q_m$；原低投影估计给 $v_{m,q_m}\to w$，故固定非零 $w$ 的 $\mu_{m,q_m}(r_{m,q_m})\to\|w\|$。并非在固定 $m$ 的有限合法窗口内令 $q$ 无限制趋于无穷。

## 5. 去重、当前用途和剩余源匹配

Cauchy–Schwarz 给
$$
\mu_q(r)^2
=\langle G_q^{1/2}J_q^{-1}r,G_q^{-1/2}r\rangle
\le\lambda_q(r_q^\flat)\lambda_q(r).
\tag{5.1}
$$
结合 (4.5)，这重得旧必要的未来带/修复费下界，不另计进展。

本笔记保存的具体接口是：完整左 Gram $J_q$ 的实际定义与不含 $q$ 的
$e^{20d^4}$ 右逆预算，以及明确源 $G_qJ_q^{-1}r(w)$ 的完整右修复小费用。
(3.3)–(4.5) 本质来自对所有同源有限核的原正交测试；
不把它登记为一个新的无权定理。

旧右侧返回源
$\mathsf F Kc_L$、移段剩余源
$G_{q+k}z_k-A_mc_k$ 与 (4.2) 之间，尚未证明可付的同源关系。
特别，$J_q$ 不是首段先消元稿中的右低链 Gram
$\mathsf F\mathsf F^*$，两者不得仅凭都称“低链”而相等或交换。

真正双宽头商仍应保
$$
\|h^\perp\|^2
=\|h\|^2-\lambda_d(r)^2+\lambda_{2d}(r)^2.
$$
本笔记不从加入 $\mu_q(r)^2$ 自动得到该商的统一上界。
无权 $N=M$ 与普通复 Hilbert ISP 继续开放。

## 6. 与真实未来带廉价源的准确匹配

本节对照[首段先消元稿 §§9.6—9.7](../results/R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)。该稿 §9.7 已独立写出左源的状态坐标和廉价源匹配；下文 §§6.1—6.4 是同一接口的准确字典与直接图投影复核，并给原 $M$ 上的正压缩恒等式，不重复登记为新能量定理。§6.5 再把原源校正到保留完全相同返回向量的两侧最小类。原返回费仍未控制。

本节由 boundary_resume_1cf 撰写，Astra-ISP-1cf8c51d、kernel_resume_1cf 独立复核。

### 6.1 左 Gram 在低链状态上的正坐标

沿首段先消元稿，令
$$
\mathcal U_q=Z_q\ominus\ker\mathsf F_q,\qquad
\mathsf f_q=\mathsf F_q|_{\mathcal U_q}:
\mathcal U_q\longrightarrow\mathscr R_q.
$$
在当前固定合法窗口内，$\mathsf f_q$ 是有界双射。其逆就是低链裸最小原像映射。原图嵌入及其严格正度量为
$$
\mathcal J_q a=a-\mathcal T_q a,\qquad
\mathcal P_q=\mathcal J_q^*\mathcal J_q=I+\mathscr L_q.
$$
完整最小链满足
$$
\mathcal R_q=\mathcal J_q\mathsf f_q^{-1}.
$$
结合 $\mathcal R_q^*\mathcal R_q=G_q^{-1}$，准确得到
$$
\boxed{G_q=\mathsf f_q\mathcal P_q^{-1}\mathsf f_q^*.}
\tag{6.1}
$$

定义左侧状态度量
$$
\boxed{
\mathcal Q_{L,q}=\mathsf f_q^*J_q^{-1}\mathsf f_q>0.
}
\tag{6.2}
$$
它与 $\mathcal P_q$ 是不同正算子。对原 $r$ 及 $a=\mathsf f_q^{-1}r$，有
$$
\mu_q(r)^2=\langle\mathcal Q_{L,q}a,a\rangle.
$$
由 (4.2)、(6.1)，$r_q^\flat$ 的裸状态及能量协向量准确为
$$
\boxed{
\vartheta_q^\flat=\mathsf f_q^{-1}r_q^\flat
=\mathcal P_q^{-1}\mathcal Q_{L,q}a,\qquad
\eta_q^\flat=\mathcal P_q\vartheta_q^\flat
=\mathcal Q_{L,q}a=\mathsf f_q^*J_q^{-1}r.
}
\tag{6.3}
$$
特别
$$
\lambda_q(r_q^\flat)=\|\mathcal P_q^{-1/2}\eta_q^\flat\|.
\tag{6.4}
$$
没有交换 $J_q,G_q$ 或这两个状态度量。

### 6.2 对原 M 的精确正压缩及真正 W 重建

保持原实际源提取
$$
\mathcal A_q:M\longrightarrow\mathcal U_q,\qquad
\mathcal A_q=\mathsf f_q^{-1}E_qP_{\mathscr V_q}|_M.
$$
记 $\Pi_{L,q}$ 为整个环境 Hilbert 空间中到
$\mathscr V_q\ominus\ker E_q$ 的正交投影。由
$E_q^*J_q^{-1}E_q$ 是 $\mathscr V_q$ 内的对应投影，
准确有
$$
\boxed{
\mathcal A_q^*\mathcal Q_{L,q}\mathcal A_q
=P_M\Pi_{L,q}|_M,\qquad
0\le\mathcal A_q^*\mathcal Q_{L,q}\mathcal A_q\le I_M.
}
\tag{6.5}
$$
这个恒等式对整个 $M$ 成立。证明只需代入各真实受限伴随：
$\mathsf f_q^{-1}$ 与其伴随在相邻位置相消，
剩下 $P_MP_{\mathscr V_q}E_q^*J_q^{-1}E_qP_{\mathscr V_q}|_M$。
没有让 $P_M$ 与任一其他算子交换。

对本笔记的原 $w\in W$，(6.3)、(6.5) 给
$$
\boxed{\mathcal A_q^*\eta_q^\flat=P_M\mathcal V_qr.}
\tag{6.6}
$$
再用 (4.6) 的有限核投影费用，以及
$\|v-P_{\le q}^{(m)}w\|\le e^{-74d^4}\|w\|$，得到
$$
\boxed{
\|\mathcal A_q^*\eta_q^\flat-w\|
\le\tau_q(w)+(e^{-74d^4}+e^{-75d^4})\|w\|,
\quad
\tau_q(w)=\|P_{>q}^{(m)}w\|.
}
\tag{6.7}
$$
这是原 $M$ 中的范数结论。它没有把
$\mathcal A_q^*\mathscr L_q\mathcal A_qw$ 认成 $w$。

### 6.3 两个廉价源在完整修复度量中相同到 carry 精度

首段先消元稿的原真实未来输入为
$$
\overline u=u+\widehat a-a,\qquad
\|u-P_{\mathscr C_q}w\|\le e^{-74d^4}\|w\|,
\qquad
\|\widehat a-a\|\le12e^{-73d^4}\|w\|.
$$
其廉价源满足
$$
\mathcal R_q r_q^{\rm small}
=P_{\operatorname{Ran}\mathcal J_q}\overline u.
\tag{6.8}
$$
另一方面，$\operatorname{Ran}\mathcal R_q=\operatorname{Ran}\mathcal J_q$，所以
$$
\mathcal R_qG_q\mathcal R_q^*
=P_{\operatorname{Ran}\mathcal J_q},\qquad
\|\mathcal R_qG_q\|=\|G_q^{1/2}\|\le1.
\tag{6.9}
$$
由 (3.4)、(4.1)，
$$
\|\mathcal R_q^*w-J_q^{-1}r\|
\le2e^{-55d^4}\|w\|.
$$
在 (6.8) 中减去 $\mathcal R_qG_qJ_q^{-1}r$，用 (6.9) 得
$$
\begin{aligned}
\lambda_q(r_q^{\rm small}-r_q^\flat)
&\le
\|\overline u-P_{\mathscr C_q}w\|
+\|\mathcal R_qG_q\|\,
\|\mathcal R_q^*w-J_q^{-1}r\|\\
&\le(e^{-74d^4}+12e^{-73d^4}+2e^{-55d^4})\|w\|\\
&\le3e^{-55d^4}\|w\|.
\end{aligned}
$$
故准确的匹配是
$$
\boxed{
\lambda_q(r_q^{\rm small}-r_q^\flat)
=\|\mathcal P_q^{-1/2}(\eta_q-\eta_q^\flat)\|
\le3e^{-55d^4}\|w\|.
}
\tag{6.10}
$$
首段校正 $\widehat a-a$ 只经过范数1的图投影；没有再乘一般完整右逆成本。

### 6.4 与原窄通量的同窗关系及尚余返回项

继续保留首段先消元稿 §9.6.D 的实际高输出 $\overline f$。
该稿准确给
$$
r_q^{\rm small}=-r+F_q^{\rm full}S_q^\dagger\overline f,
$$
其中 $F_q^{\rm full}$ 表示完整修复输入上的首输出，避免与本笔记只作用在 $\ker S_q$ 上的 $F_q$ 混淆。因此 (6.10) 等价于
$$
\boxed{
\lambda_q\!\left(
r+r_q^\flat-F_q^{\rm full}S_q^\dagger\overline f
\right)
\le3e^{-55d^4}\|w\|.
}
\tag{6.11}
$$
在状态坐标中，同一个式子是
$$
\boxed{
\left\|
\mathcal P_q^{1/2}
\left[
a+\mathcal P_q^{-1}\mathcal Q_{L,q}a
-B_{A,q}^*(\mathcal H_{2,q}^{\rm old})^{-1}\overline f
\right]
\right\|
\le3e^{-55d^4}\|w\|.
}
\tag{6.12}
$$
这里必须保留原真实 $\overline f$ 和旧 $\mathcal H_2^{\rm old}$；不能把它换成旧有效源 $\sigma_q$。

原返回状态仍为 $\mathscr L_qa$，而已付小源状态是
$\mathcal P_q^{-1}\mathcal Q_{L,q}a$。其完整差额准确为
$$
\boxed{
\lambda_q(r_{\rm ret}-r_q^\flat)
=
\left\|\mathcal P_q^{-1/2}
(\mathcal P_q\mathscr L_q-\mathcal Q_{L,q})a
\right\|.
}
\tag{6.13}
$$
本节没有给 (6.13) 的小费用上界，也未识别移段源 $\rho_k$。
新增的是两个已付小源的对应及 (6.5) 的明确正压缩；并非把原返回费用消去。

### 6.5 保留原返回向量的两侧最小源校正

令
$$
\mathcal K_{0,q}=\ker\mathscr L_q
=\ker\mathcal T_q=\ker B_{A,q}.
$$
这些核相同，分别由
$\mathscr L_q=\mathcal T_q^*\mathcal T_q
=B_{A,q}^*(\mathcal H_2^\circ)^{-1}B_{A,q}$
和新末块严格正性得到。$\mathcal K_{0,q}$ 是闭子空间，不假设
$\mathscr L_q$ 在其正交补上有正下界。

原 $\eta_q=-a-\mathcal T_q^*g$ 给准确的
$$
P_{\mathcal K_{0,q}}(\eta_q+a)=0.
$$
而 $\mathcal P_q=I+\mathscr L_q$ 在 $\mathcal K_{0,q}$ 上等于 $I$，所以
(6.10) 直接给
$$
\boxed{
\|P_{\mathcal K_{0,q}}(I+\mathcal Q_{L,q})a\|
\le3e^{-55d^4}\|w\|=:\varepsilon_{\rm match}.
}
\tag{6.14}
$$
这里无须把误差乘 $\mathscr L_q$ 的逆。

记
$$
\mathcal D_q=I+\mathcal Q_{L,q}\ge I,\qquad
D_{0,q}=P_{\mathcal K_{0,q}}\mathcal D_q|_{\mathcal K_{0,q}}\ge I.
$$
取真正有界的压缩逆，定义
$$
e_q=D_{0,q}^{-1}P_{\mathcal K_{0,q}}\mathcal D_q a
\in\mathcal K_{0,q},\qquad
a^\sharp=a-e_q,\qquad r^\sharp=\mathsf f_q a^\sharp.
$$
则
$$
\boxed{
P_{\mathcal K_{0,q}}\mathcal D_q a^\sharp=0,\qquad
\|e_q\|_{\mathcal D_q}\le\varepsilon_{\rm match}.
}
\tag{6.15}
$$
范数界来自
$\|e_q\|_{\mathcal D_q}^2
=\langle D_{0,q}^{-1}b,b\rangle\le\|b\|^2$，
$b=P_{\mathcal K_{0,q}}\mathcal D_qa$。

因此 $a^\sharp$ 是下列同一高源问题的准确最小者：
$$
\boxed{
a^\sharp=
\arg\min_{B_{A,q}u=B_{A,q}a}
\left(\|u\|^2+\mu_q(\mathsf f_qu)^2\right).
}
\tag{6.16}
$$
约束集是闭仿射集 $a+\mathcal K_{0,q}$，
$\mathcal D_q\ge I$ 保证存在唯一最小值；不要求 $B_{A,q}$ 闭像。

这一步完整保留原返回量：
$$
\mathscr L_qa^\sharp=\mathscr L_qa,\qquad
B_{A,q}a^\sharp=B_{A,q}a,\qquad
r_{\rm ret}(r^\sharp)=r_{\rm ret}(r).
\tag{6.17}
$$
因 $\mathcal P_qe_q=e_q$、$\mathcal T_qe_q=0$，
完整最小链只改变 $e_q$：
$$
c_q(r)-c_q(r^\sharp)=\mathcal J_qe_q=e_q,\qquad
\lambda_q(r-r^\sharp)=\|e_q\|\le\varepsilon_{\rm match},
$$
$$
\mu_q(r-r^\sharp)=\|\mathcal Q_{L,q}^{1/2}e_q\|
\le\varepsilon_{\rm match}.
\tag{6.18}
$$
新高对偶 $z_2=(\mathcal H_2^\circ)^{-1}B_Aa$、旧有效高源
$\sigma=\mathcal H_2^{\rm old}z_2$、旧末块能量以及只读取高出生对偶的窄头通量也全部保持。
这只是把真实源限制到 (6.16) 的准确两侧最小类；
未给这个类上的返回能量上界。

# R271 附录：右链首段损耗、完整源的精确收缩与无损解析演算

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本稿锐化 [强尾联块源的 Stein 缺陷与完整 Schur 解析演算](R271-appendix-strong-tail-source-stein-defect-and-full-schur-analytic-calculus.md)。完整右链和裸链在头算子作用下均丢掉第一段能量；这段能量准确支付源的原物理范数平方，恰与左端的 $+I$ 抵消。因此两个真实源 Schur 度量都满足
$$
C_{\rm s}^*S_bC_{\rm s}\le\delta^2S_b,\qquad
C_{\rm s}^*S_fC_{\rm s}\le\delta^2S_f.
$$
原来的 $\sqrt{k+1}$ 幂损失可以全部删除。本文给出完整正平方缺陷和自足的有限 nilpotent 模型证明，进而得到没有几何级数损失的圆盘解析演算。仍不比较 $S_b$ 与 $S_f$，不把其差额当成已付的返回费用。

依赖：[强物理尾位并头后的同一顶部源流与完整两费预算](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md) 中的准确源、自然域、完整与裸链，以及上一附录的左最小化身份。本文只在一个固定 $m,R,n$ 的闭源上运算，不使用全孔直和上有界的尾右逆。

## 1. 同源记号和两种最小右链

固定
$$
C=A_m+D_<,\qquad C^h=0,\qquad D=D_>,\qquad \delta=\|D\|>0,
$$
及原完整源 $\mathscr R=\mathscr R_n^C$。记
$$
U=(E_n^C)^\dagger,\quad L=U^*U,\quad
F:\mathcal Y_f\longrightarrow\mathscr R,\quad
F_b:\mathcal Y_b\longrightarrow\mathscr R,
$$
$$
H=(FF^*)^{-1}=G^{-1},\qquad
B=(F_bF_b^*)^{-1},\qquad
S_f=L+H,\quad S_b=L+B.
\tag{1.1}
$$
两条源映射均为完整固定源上的有界满射，且都是 $D$ 作用在第一段：
$$
Fc=Dc_1,\qquad F_bb=Db_1.
$$
以
$$
J_f=F^\dagger,\qquad J_b=F_b^\dagger
$$
表示真正最小右链；所以 $H=J_f^*J_f$、$B=J_b^*J_b$。源上的头算子是准确限制
$$
C_{\rm s}=C|_{\mathscr R},\qquad C_{\rm s}^h=0.
$$

$\mathcal C_\sigma$ 表示在 $\mathcal Y_\sigma$ 上逐段作用 $C$，$\sigma=f,b$。全部头旗、尾旗及内部方程均被它保持，且
$$
F_\sigma\mathcal C_\sigma=C_{\rm s}F_\sigma.
\tag{1.2}
$$
令 $P_\sigma^0$ 为 $\ker F_\sigma$ 的物理正交投影。真正最小化准确给
$$
J_\sigma C_{\rm s}
=(I-P_\sigma^0)\mathcal C_\sigma J_\sigma.
\tag{1.3}
$$
这里没有把一个可行右链直接当作最小右链。

## 2. 第一段的精确支付

完整链和裸链分别满足
$$
Cc_j=-Dc_{j+1},\qquad
Cb_j=-P_j^{\rm lo}Db_{j+1}\quad(1\le j<h),
\qquad Cc_h=Cb_h=0.
\tag{2.1}
$$
对完整链令 $Q_{f,j}=I$，对裸链令 $Q_{b,j}=P_j^{\rm lo}$。取
$x=J_\sigma r=(x_1,\ldots,x_h)$。由 (1.3) 和 (2.1)，有精确平方身份
$$
\begin{aligned}
&\delta^2\|J_\sigma r\|^2
-\|J_\sigma C_{\rm s}r\|^2-\|r\|^2\\
&\quad=
\bigl(\delta^2\|x_1\|^2-\|Dx_1\|^2\bigr)
+\sum_{j=2}^{h}
 \bigl(\delta^2\|x_j\|^2-\|Q_{\sigma,j-1}Dx_j\|^2\bigr)
+\|P_\sigma^0\mathcal C_\sigma J_\sigma r\|^2.
\end{aligned}
\tag{2.2}
$$
每一项都非负：$\|D\|=\delta$，各 $Q_{\sigma,j}$ 是物理正交投影，而 $r=Dx_1$。因此
$$
\boxed{
C_{\rm s}^*BC_{\rm s}+I_{\mathscr R}\le\delta^2B,\qquad
C_{\rm s}^*HC_{\rm s}+I_{\mathscr R}\le\delta^2H.
}
\tag{2.3}
$$
$I_{\mathscr R}$ 是原源物理内积的单位算子，不是 $B$ 或 $H$ 度量中的单位。它来自首段的源范数，不能在 (2.1) 求和时把这个首段丢失再粗估回整条链。

还可迭代得到一个完整源的观测预算。对 $K=B,H$，
$$
\boxed{
K\ \ge\
\sum_{j=0}^{h-1}\delta^{-2(j+1)}
 (C_{\rm s}^*)^jC_{\rm s}^j.
}
\tag{2.4}
$$
证明是将
$K\ge\delta^{-2}I+\delta^{-2}C_{\rm s}^*KC_{\rm s}$
逐次代入，末项由 $C_{\rm s}^h=0$ 消失。此式保同一源，不把不同高度的源独立选取。

## 3. 与左端的准确正平方相消

令 $\mathscr K=\ker E_n^C$ 为真实左零源核。对 $v=Ur$，原低输出方程及物理孔支撑给
$$
Cv=-Dv+\iota_n r,\qquad
Dv\perp\iota_n r.
$$
而 $UC_{\rm s}r=(I-P_{\mathscr K})CUr$，所以
$$
C_{\rm s}^*LC_{\rm s}
=I+U^*D^*DU-(P_{\mathscr K}CU)^*(P_{\mathscr K}CU).
\tag{3.1}
$$
于是对 $\sigma=f,b$，将 (2.2) 与 (3.1) 相加，得到完整缺陷
$$
\begin{aligned}
\langle(\delta^2S_\sigma-C_{\rm s}^*S_\sigma C_{\rm s})r,r\rangle
={}&\delta^2\|Ur\|^2-\|DUr\|^2
+\|P_{\mathscr K}CUr\|^2\\
&+\bigl(\delta^2\|x_1\|^2-\|Dx_1\|^2\bigr)\\
&+\sum_{j=2}^{h}
 \bigl(\delta^2\|x_j\|^2-\|Q_{\sigma,j-1}Dx_j\|^2\bigr)\\
&+\|P_\sigma^0\mathcal C_\sigma J_\sigma r\|^2,
\qquad x=J_\sigma r.
\end{aligned}
\tag{3.2}
$$
其中 $S_f=L+H$、$S_b=L+B$。这给出所需的真实同源正平方分解：左最小化、右最小化及裸商投影各自保留。特别
$$
\boxed{
C_{\rm s}^*S_\sigma C_{\rm s}\le\delta^2S_\sigma,\qquad
\|C_{\rm s}^k\|_{S_\sigma}\le\delta^k
\quad(k\ge0,\ \sigma=f,b).
}
\tag{3.3}
$$
常数与 $h,n,R$ 及头 Jordan 条件数无关。这里相消的是 (2.3) 和 (3.1) 的同一个物理 $I$；没有对两个不同的右不等式相减。

## 4. 有限模型和无损圆盘演算

以下证明 (3.3) 还给出更强的解析结论。固定 $S=S_b$ 或 $S_f$，把 $\mathscr R$ 视为内积 $\langle S\cdot,\cdot\rangle$ 的 Hilbert 空间，令
$$
T=C_{\rm s}/\delta,\qquad
\Delta=(I-T^\dagger T)^{1/2},
$$
其中 $\dagger$ 为这个 $S$ 内积的伴随。$T^h=0$、$T^\dagger T\le I$。定义
$$
\mathcal V r=(\Delta r,\Delta Tr,\ldots,\Delta T^{h-1}r).
$$
有限望远镜给
$$
\|\mathcal V r\|^2
=\sum_{j=0}^{h-1}
(\|T^jr\|_S^2-\|T^{j+1}r\|_S^2)
=\|r\|_S^2.
\tag{4.1}
$$
因此 $\mathcal V$ 是等距，且
$$
\mathcal V T=\mathcal S\mathcal V,\qquad
\mathcal S(x_0,\ldots,x_{h-1})=(x_1,\ldots,x_{h-1},0).
\tag{4.2}
$$

对任意复多项式 $p$，将向量序列识别为圆周上向量值多项式
$\sum_{j=0}^{h-1}x_jz^j$。$p(\mathcal S)$ 是乘以 $p(\bar z)$ 后投影回这些次数的算子，因此
$$
\|p(\mathcal S)\|\le\max_{|z|=1}|p(z)|.
$$
结合 (4.1)–(4.2)，得到
$$
\|p(C_{\rm s})\|_S\le\max_{|z|\le\delta}|p(z)|.
\tag{4.3}
$$
若 $f$ 在半径大于 $\delta$ 的圆盘解析，Taylor 多项式在闭 $\delta$ 圆盘一致收敛，而代入 $C_{\rm s}$ 后从第 $h$ 项起严格为零，故
$$
\boxed{
\|f(C_{\rm s})\|_{S_b},\
\|f(C_{\rm s})\|_{S_f}
\le\sup_{|z|\le\delta}|f(z)|.
}
\tag{4.4}
$$
这里使用的是 $f$ 的真实 Taylor 函数与其在 nilpotent 源上的有限代入，不是对一个任意截断多项式另假小的圆盘上界。

例如，对 $|z|>\delta$，
$$
\boxed{
\|(zI-C_{\rm s})^{-1}\|_{S_b},\
\|(zI-C_{\rm s})^{-1}\|_{S_f}
\le\frac1{|z|-\delta}.
}
\tag{4.5}
$$
以上有限模型证明也适用于固定孔层无限维的 $\mathscr R$；只有直和的长度 $h$ 是有限的。

## 5. 原逆芽的进一步锐化及范围

保持前稿的真实原头逆芽规范
$$
d_0=e^{-20},\qquad
\rho_m=e^{-25d^3/2},\qquad
r_m=\rho_m/(2d_0),\qquad
\varepsilon_m=e^{-d^3/4}.
$$
令 $f_m(z)=\psi_m(z)/z$，$f_m(0)=d_0$。已付芽估计为
$$
|f_m(z)-d_0|\le2d_0^2\varepsilon_m
\qquad(|z|\le r_m).
$$
函数 $f_m-d_0$ 在零点为零，所以圆盘 Schwarz 估计给
$$
|f_m(z)-d_0|
\le2d_0^2\varepsilon_m\,|z|/r_m.
$$
若 $\delta<\rho_m$，由 (4.4) 得
$$
\boxed{
\|d_0^{-1}f_m(C_{\rm s})-I\|_{S_b},\
\|d_0^{-1}f_m(C_{\rm s})-I\|_{S_f}
\le4d_0^2\varepsilon_m\,\delta/\rho_m.
}
\tag{5.1}
$$
原先的常数 $16$ 因而可降为 $4$。准确代入仍须保到 $h-1$ 次；当 $h>d$ 时不能换成仅到 $d-1$ 次的旧头多项式。其逆、同余近恒等及 $S_b$ 伴随保持真实负图的后果按上一稿原式成立，使用 (5.1) 的新误差即可。

本稿没有证明
$$
C_{\rm s}^*(H-B)C_{\rm s}\le\delta^2(H-B).
$$
即使 (2.3) 的两个式子都成立，它们的差仍无确定序；(3.2) 的两套右平方也没有被宣布可相减。完整返回费用 $H-B$、同一个实际来源的 $\mu^2\le\kappa\Xi^2$ 及普通右链封口仍未付。新的确定输入是带首段观测损耗的两条 Stein 不等式、完整源上的精确收缩，以及真正的圆盘有界演算。

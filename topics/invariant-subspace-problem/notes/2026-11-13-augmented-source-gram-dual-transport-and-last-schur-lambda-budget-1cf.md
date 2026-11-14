# 工作笔记：增广源 Gram 的对偶运输与末 Schur 块的真实 λ 预算

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。根独立复算完整正交分解；boundary_resume_1cf 继续负责将运输源与真正返回源匹配。

状态：完整推导；根代理与 boundary_resume_1cf 已全文独立核查。这是已证联合旗满射、完整降孔交织及正交投影的具体后果，不登记独立主定理。本文明确补出内部对偶链及末 Schur 块的原能量身份；没有证明运输源等于相邻层同一见证的最优源，也不据此推出无权 $N=M$。

## 1. 与旧完整修复及 W 投影缺陷的扣除

沿用[联合旗右逆](../results/R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)、
[完整链与真 Schur](../results/R271-appendix-complete-repair-chain-lowering-defects-and-true-schur-contraction.md)
及[嵌套旗商能量稿](../results/R271-appendix-nested-birth-flags-quotient-energy-and-complete-schur-defects.md)。

固定同一个合法头
$$
m\ge5,\qquad d=2^m,\qquad
4d\le q,\qquad q+1\le e^{d^3/4}.
$$
取完整纯尾降孔
$$
C=D_{3,m}=\sum_{\ell\ge m}b_\ell^3E_\ell,\qquad
s_3=\sum_{\ell\ge m}b_\ell^3\le(5m^5)^{-1}.
$$

旧完整链稿 §§3—3.2 已有：

- 前向最小修复交换缺陷
  $C\mathcal R_{q+1}-\mathcal R_qC_{\mathscr R,q}$ 的准确有限核来源、正交能量与 $W$ 投影小量；
- 准确源 Gram 和内部完整 Gram 的降孔收缩；
- 高出生旗的正确逆压缩 Schur 度量。

这些结论不重计。本笔记的对偶分解来自同一完整交织，但其余量位于内部伴随像 $\operatorname{Ran}S_{q+1}^*$，不是旧前向差所在的零源修复核。下面把它准确识别为
$z'_{q+1}-C_{\mathscr Y,q}^*z_q$，给同一个实际最小修复的 $\lambda$ 费用，并把这个预算同时拆到三个真实 Schur 坐标。仅有旧 $W$ 投影差式并未写出这些内部链坐标及其运输源。

## 2. 全部源、内部输出与真实受限伴随

对 $j=q,q+1$，取旧实际联合输入 $\mathscr C_j$、实际源旗 $\mathscr R_j$、内部输出 $\mathscr Y_j$ 和
$$
S_j:\mathscr C_j\to\mathscr Y_j.
$$
令
$$
\mathsf F_j:\mathscr C_j\to\mathscr R_j,\qquad
\mathsf F_jc=D_mc_1
$$
为整个联合输入上的首输出。
其与 $S_j$ 的联合算子
$$
\mathcal T_j=(\mathsf F_j,S_j):
\mathscr C_j\to\mathscr R_j\oplus\mathscr Y_j
$$
由旧同时右逆满射。记
$$
P_j=P_{\ker S_j},\qquad
F_j=\mathsf F_j|_{\ker S_j},\qquad
G_j=F_jF_j^*,\qquad
\mathcal G_j=S_jS_j^*.
$$
固定 $m,j$ 时 $G_j,\mathcal G_j$ 都严格正，全部逆有界。
准确有
$$
F_j^*=P_j\mathsf F_j^*,\qquad
G_j=\mathsf F_jP_j\mathsf F_j^*.
\tag{2.1}
$$

完整 $C$ 的三条真实限制分别为
$$
C_{\mathscr C,q}:\mathscr C_{q+1}\to\mathscr C_q,\quad
C_{\mathscr R,q}:\mathscr R_{q+1}\to\mathscr R_q,\quad
C_{\mathscr Y,q}:\mathscr Y_{q+1}\to\mathscr Y_q.
$$
它们的范数均不超过 $s_3$，并且
$$
\boxed{
\mathsf F_qC_{\mathscr C,q}
=C_{\mathscr R,q}\mathsf F_{q+1},\qquad
S_qC_{\mathscr C,q}
=C_{\mathscr Y,q}S_{q+1}.
}
\tag{2.2}
$$
这是 $C$ 与原头、纯删除算子的真实交织，包含全部联合旗。

下文所有星号都是这些实际 Hilbert 空间之间的受限伴随。特别
$$
C_{\mathscr R,q}^*
=P_{\mathscr R_{q+1}}C^*|_{\mathscr R_q},
\qquad
C_{\mathscr C,q}^*
=P_{\mathscr C_{q+1}}C^*|_{\mathscr C_q}.
\tag{2.3}
$$
这些正交投影不能删掉。

## 3. 准确运输源与 Pythagoras

给定任何实际 $r\in\mathscr R_q$，置
$$
y=G_q^{-1}r,\qquad
b=\mathsf F_q^*y,\qquad
D_j=S_j\mathsf F_j^*,\qquad
R_j=\mathcal G_j^{-1}D_j,
$$
$$
z=R_qy,\qquad
c=F_q^*y=b-S_q^*z,\qquad
\lambda=\|c\|.
\tag{3.1}
$$
所以 $c$ 是 $r$ 的原完整最小修复，
$$
\lambda^2=\langle G_qy,y\rangle.
$$

定义运输后的对偶源、实际残量及其真正最优链：
$$
\boxed{
y'=C_{\mathscr R,q}^*y,\qquad
r'=G_{q+1}y'
=G_{q+1}C_{\mathscr R,q}^*G_q^{-1}r,
}
\tag{3.2}
$$
$$
z'=R_{q+1}y',\qquad
c'=F_{q+1}^*y',\qquad
\lambda'=\|c'\|=\lambda_{q+1}(r').
$$
固定参数下这些均为有界算子作用，且 $r'\in\mathscr R_{q+1}$。
$r'$ 是明确构造的实际源，但目前不能识别为同一 $w$ 的
$r_{m,q+1}(w)$，也不能识别为原尾理想作用后的那个源。

对 (2.2) 取准确伴随，代入 (3.1)，得到
$$
\begin{aligned}
C_{\mathscr C,q}^*c
&=\mathsf F_{q+1}^*C_{\mathscr R,q}^*y
-S_{q+1}^*C_{\mathscr Y,q}^*z\\
&=c'+S_{q+1}^*\bigl(z'-C_{\mathscr Y,q}^*z\bigr).
\end{aligned}
$$
因此
$$
\boxed{
C_{\mathscr C,q}^*c
=c'+S_{q+1}^*\delta z,\qquad
\delta z:=z'-C_{\mathscr Y,q}^*z.
}
\tag{3.3}
$$
第一项属于 $\ker S_{q+1}$，第二项属于其正交补。于是
$$
\boxed{
(\lambda')^2+\|\delta z\|_{\mathcal G_{q+1}}^2
=\|C_{\mathscr C,q}^*c\|^2
\le s_3^2\lambda^2.
}
\tag{3.4}
$$
这里 $\|h\|_A^2=\langle Ah,h\rangle$。
这是实际正交分解，费用为原 $\lambda$，没有 $\|b\|$、
$\|y\|$、$\|z\|$ 或一般右逆常数。

同时，
$$
c'=P_{q+1}C_{\mathscr C,q}^*c,\qquad
S_{q+1}^*\delta z=(I-P_{q+1})C_{\mathscr C,q}^*c.
\tag{3.5}
$$
所以其源能量收缩部分与旧源 Gram 收缩同源；本笔记显式保留并识别了正交余量及其内部对偶坐标。

## 4. 增广 Gram 的同一个完整式

为核对没有误交换任何逆，置
$$
A_j=\mathsf F_j\mathsf F_j^*,\qquad
\mathcal K_j=\mathcal T_j\mathcal T_j^*
=\begin{pmatrix}A_j&D_j^*\\D_j&\mathcal G_j\end{pmatrix}.
$$
由 (2.1)，
$$
G_j=A_j-D_j^*\mathcal G_j^{-1}D_j.
$$
令
$$
\mathcal U_j=
\begin{pmatrix}I&R_j^*\\0&I\end{pmatrix},
\qquad
\mathcal A_j=\operatorname{diag}(G_j,\mathcal G_j).
$$
直接相乘给
$$
\boxed{\mathcal K_j=\mathcal U_j\mathcal A_j\mathcal U_j^*.}
\tag{4.1}
$$
这是准确合同分解，不是等距换基。

由 (2.2)，
$$
\operatorname{diag}(C_{\mathscr R,q},C_{\mathscr Y,q})
\mathcal K_{q+1}
\operatorname{diag}(C_{\mathscr R,q},C_{\mathscr Y,q})^*
\le s_3^2\mathcal K_q.
$$
将它用 (4.1) 合同，完整变换后的降孔为
$$
\widehat C=
\begin{pmatrix}C_{\mathscr R,q}&E_q\\0&C_{\mathscr Y,q}\end{pmatrix},
\qquad
\boxed{
E_q=C_{\mathscr R,q}R_{q+1}^*
-R_q^*C_{\mathscr Y,q}.
}
\tag{4.2}
$$
其左上块预算为
$$
\boxed{
C_{\mathscr R,q}G_{q+1}C_{\mathscr R,q}^*
+E_q\mathcal G_{q+1}E_q^*
\le s_3^2G_q.
}
\tag{4.3}
$$
而
$$
E_q^*y=R_{q+1}C_{\mathscr R,q}^*y-C_{\mathscr Y,q}^*z=\delta z.
$$
对 (4.3) 以真 $y$ 作二次型，正好重得 (3.4)。
这个写法同时展示原 $G_j^{-1}$ 和 $\mathcal G_j^{-1}$ 的位置；
没有让它们与 $C$ 交换。

## 5. 末 Schur 块和两次逆同时保 λ 费用

在第 $q+1$ 层，继续使用真实出生三块
$\mathscr Y_0\oplus\mathscr Y_1\oplus\mathscr Y_2$。
为简化本节下标，以下 $B_0,Q_1,\mathcal H_2,T_0,T_1$ 都取在第 $q+1$ 层。

嵌套旗稿的准确分解为
$$
\mathcal G_{q+1}
=\mathcal L\operatorname{diag}(B_0,Q_1,\mathcal H_2)\mathcal L^*,
\qquad
\mathcal L=
\begin{pmatrix}I&0&0\\T_0&I&0\\0&T_1&I\end{pmatrix}.
$$
若 $\delta z=(\delta z_0,\delta z_1,\delta z_2)$，则
$$
\boxed{
\begin{aligned}
\|\delta z\|_{\mathcal G_{q+1}}^2
={}&\|\delta z_0+T_0^*\delta z_1\|_{B_0}^2\\
&+\|\delta z_1+T_1^*\delta z_2\|_{Q_1}^2
+\|\delta z_2\|_{\mathcal H_2}^2.
\end{aligned}
}
\tag{5.1}
$$
所以这三个准确正能量和 $(\lambda')^2$ 的总和均由
$s_3^2\lambda^2$ 控制。不对各裸坐标使用错误的普通压缩逆。

完整 $C_{\mathscr Y,q}$ 在出生旗中下三角，其高旗对角块为
$C_{22}=C_{2,q}$。因此其伴随作用的第三块准确是
$$
(C_{\mathscr Y,q}^*z)_2=C_{22}^*z_2.
$$
由 (3.4)、(5.1)，
$$
\boxed{
\|z'_2-C_{22}^*z_2\|_{\mathcal H_{2,q+1}}^2
\le s_3^2\lambda_q(r)^2-\lambda_{q+1}(r')^2.
}
\tag{5.2}
$$

$y'\in\mathscr R_{q+1}$，所以 $D_{q+1}y'$ 仍是实际的首段
$\mathscr Y_0$ 型源，写为 $(g_0',0,0)$。
故 $z'_2$ 保留两次真实逆：
$$
\boxed{
z'_2
=\mathcal H_{2,q+1}^{-1}
V_{2,q+1}Q_{1,q+1}^{-1}
V_{1,q+1}B_{0,q+1}^{-1}g_0',
\qquad
g_0'=(D_{q+1}C_{\mathscr R,q}^*y)_0.
}
\tag{5.3}
$$
(5.2) 是这个完整复合链与 $C_{22}^*z_2$ 的真实正 Schur 能量差。
它不同于嵌套旗稿中前向有效源的逆 Schur 能量差；两者的方向、源和度量都必须保持。

## 6. 对真实窄通量的可直接配对预算

任给 $\mathfrak f\in\mathscr Y_{2,q+1}$，由 (5.2) 及同一正度量的 Cauchy--Schwarz，
$$
\boxed{
\begin{aligned}
&|\langle\mathfrak f,z'_2\rangle
-\langle C_{22}\mathfrak f,z_2\rangle|\\
&\quad\le
\|\mathfrak f\|_{\mathcal H_{2,q+1}^{-1}}
\sqrt{s_3^2\lambda_q(r)^2-\lambda_{q+1}(r')^2}\\
&\quad\le
s_3\lambda_q(r)\,
\|\mathfrak f\|_{\mathcal H_{2,q+1}^{-1}}.
\end{aligned}
}
\tag{6.1}
$$
这里 $C_{22}\mathfrak f$ 是旧完整降孔在真实高旗上的限制。

特别，取完整链稿 §7.B 中由同一实际 $w\in W$ 产生的下一层窄通量
$\mathfrak f=\mathfrak f_{m,q+1}(w)$，其已付实际原像给
$$
\|\mathfrak f\|_{\mathcal H_{2,q+1}^{-1}}
\le
\beta_{q+1,+}(w)
:=
\|P_{[q+2,q+d+1]}^{(m)}w\|
+e^{-74d^4}\|w\|.
$$
于是 (6.1) 的误差为
$$
\boxed{s_3\lambda_q(r)\,\beta_{q+1,+}(w).}
\tag{6.2}
$$
两层都使用同一个头 $m$ 和原合法窗口，没有改变头后比较不同度量。
此处 $r$ 可以取第 $q$ 层同一 $w$ 的真实最优源；所得 $r'$ 仍只能按 (3.2) 识别。

## 7. 未付的主项与返回残量

已证的是准确构造的源映射
$$
r\longmapsto r'=G_{q+1}C_{\mathscr R,q}^*G_q^{-1}r
$$
在完整最小修复能量中收缩，以及其内部对偶链的完整正交缺陷。
(5.2) 与 (6.2) 可以不付 $\|b\|$ 地处理这个缺陷，但未处理配对主项本身。

仍未证明：

- $r'$ 等于相邻层同一 $w$ 的最优残量，或等于其原尾理想作用后残量；
- (6.1) 的主项可以替代实际正通量中的
  $\langle\mathfrak f_{m,q}(w),z_{2,q}\rangle$；
- [真实返回源笔记](2026-11-13-actual-last-block-return-source-and-complete-low-chain-projection-1cf.md)中的
  $\mathsf F Kc_L$ 属于本稿这条已付源族，或具有由此控制的完整低链 $Q=I+K$ 修复。

这些源身份不能从一个 Gram 合同分解免费取得。本笔记只把可用的
$\lambda$ 费用、实际受限伴随、两次 Schur 逆和可配对的末块度量写到同一个准确公式中。

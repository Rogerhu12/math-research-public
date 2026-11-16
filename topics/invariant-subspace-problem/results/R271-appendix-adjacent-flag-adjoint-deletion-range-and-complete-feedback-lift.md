# R271 附录：原相邻旗上的 adjoint-D 来源证书与首反馈的完整最小原像

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 原方差一位 Schur 的首反馈 $\alpha_i$ 具有一个准确的相邻旗 adjoint-$D$ 原像。对整个原权加权反馈合并后，这个原像由同一个实际缺陷 $\Delta$ 控制，因而真正最小原像也受控制。证明直接给出合法原像，不假设相邻压缩算子值域闭，也不先估环境 Moore--Penrose 逆。

目标是下文明确的 $A_E^*$。本稿不将它换成某一固定孔层的未压缩 $D_n^*$，也不将它自动等同于完整右链／帽返回的残量算子。另一个反馈 $\sigma_i$ 的次序不同，未被本稿的 adjoint 来源身份覆盖。

依据：[原方差完整恢复及辅助 mode 清零](R271-appendix-native-variance-one-bit-restoration-and-auxiliary-clearing-pairing.md)、[原一位完整 Schur](R271-appendix-one-bit-hardcore-complete-source-schur-and-joint-height-moments.md)、[原实际相邻旗](R271-appendix-adjoint-creation-synthesis-and-common-source-adjacent-flag-return.md)。

## 1. 原空间、两个相邻 cut 及参数

保原 N/Y 模型
$$
L_m=A_m+D_{[m,\infty)}=C+D,\quad
C=A_m+D_{[m,x)},\quad D=\sum_{i\ge x}b_iE_i,
$$
$$
b_i=(i+1)^{-2},\quad z_i=b_i^2,\quad
S=\sum_{i\ge x}z_i,\quad
R=x-m,\quad d=2^m,\quad h=d+R,\quad C^h=0.
$$
假设
$$
x\ge64,\qquad h\le2x,\qquad Q\ge R+h+2.
\tag{1.1}
$$
最后一个门同时保留原 $Q$ 与 $Q-1$ 来源，不将上一层的来源预算免费用于下一层。

$V_q$ 是原总尾孔支撑 $\le q$、所有输出孔 $<q$ 均为零的左可行空间；
$K_q=\ker L_m\cap\{\mathcal N\le q\}$ 是其完整零源核；
$U_q=V_q\ominus K_q$。相应正交投影均为原物理投影。以
$i_0$ 嵌入全部强头张量远真空，记
$$
Z_{E,q}=P_{E_q}i_0,\qquad E\in\{V,K,U\}.
$$

由于 $D$ 与 $L_m$ 交换并使原总尾孔数恰下降一，
$$
\boxed{
D V_Q\subseteq V_{Q-1},\qquad
D K_Q\subseteq K_{Q-1}.
}
\tag{1.2}
$$
具体而言，$L_m v$ 对 $v\in V_Q$ 只可能在第 $Q$ 输出孔，故
$L_mDv=DL_mv$ 只可能在第 $Q-1$ 输出孔，且 $Dv$ 支撑 $\le Q-1$。
这证明第一个包含；第二个再使用 $L_mk=0$。

## 2. 准确的相邻受限算子与伴随来源

定义有界算子
$$
A_V=D|_{V_Q}:V_Q\longrightarrow V_{Q-1},
$$
$$
A_U=D|_{U_Q}:U_Q\longrightarrow V_{Q-1},
\qquad
A_K=D|_{K_Q}:K_Q\longrightarrow K_{Q-1}.
\tag{2.1}
$$
所有定义域和值域空间都带原物理内积。特别，$A_U$ 的目标是完整
$V_{Q-1}$，不是未经证明的 $U_{Q-1}$。

统一记目标空间为
$$
\mathcal T_V=\mathcal T_U=V_{Q-1},\qquad
\mathcal T_K=K_{Q-1},
\quad Z_{\mathcal T_E}=P_{\mathcal T_E}i_0 .
$$
由 (1.2) 取真正伴随，
$$
A_E^*=P_{E_Q}D^*|_{\mathcal T_E},\qquad
P_{E_Q}D^*(I-P_{\mathcal T_E})=0.
\tag{2.2}
$$

对任意完整强头向量 $g$，$i_0g$ 的原尾孔支撑至多 $R$。由于
$R\le Q-1$，原低 forcing 恒等式给
$$
P_{V_Q}L_m^*i_0g=0,\qquad
P_{K_Q}L_m^*i_0g=0.
$$
而 $L_m^*i_0g=i_0C^*g+D^*i_0g$。所以
$$
\boxed{
A_E^*Z_{\mathcal T_E}g
=P_{E_Q}D^*i_0g
=-Z_{E,Q}C^*g,
\qquad E=V,K,U.
}
\tag{2.3}
$$
第一步用了真实相邻包含，第二步用了原低 forcing 域；没有把正交投影移过 $D^*$ 或一个逆。

## 3. 原方差一位完整源及上一层预算

设
$$
H=H_C(S),\quad s_i=S-z_i,\quad
H_i=H_C(s_i),\quad u_i=z_i/s_i,\quad K_0=e^8.
$$
对固定 forcing $g$，用原方差的完整最小来源
$$
a=H^{-1}g,\quad
E_j=\frac{\|C^ja\|^2}{S^jj!},\quad
\varepsilon=\sum_{j\ge1}E_j,\quad
\mathfrak F_1=\sum_{j\ge1}jE_j.
$$
前稿给
$$
\varepsilon\le\Delta_{g,Q}^2,\qquad
\mathfrak F_1\le2x\varepsilon.
\tag{3.1}
$$
第 $i$ 位的新完整最小源为 $(a_{0,i},a_{1,i})$。记
$$
r_i=H_i a_{1,i},\qquad
\boxed{\alpha_i=(b_i/s_i)C^*r_i.}
\tag{3.2}
$$
第一行源方程仍是 $H_i a_{0,i}+\alpha_i=g$。

在 $Q-1$ 上，原方差稿的完整源比较及新位增益给
$$
\boxed{
\sum_{i\ge x}\|Z_{\mathcal T_E}r_i\|^2
\le K_0^2\mathfrak F_1,
\qquad E=V,K,U.
}
\tag{3.3}
$$
说明：这里实际使用 $Z_{V,Q-1}$ 或 $Z_{K,Q-1}$；
由 (1.1)，它们分别满足
$G_{\mathcal T_E}\preceq H^{-1}\preceq K_0H_i^{-1}$。
再用
$\sum_i\|H_i^{1/2}a_{1,i}\|^2\le K_0\mathfrak F_1$，即得 (3.3)。
没有把 $Q$ 层的度量当作 $Q-1$ 层度量。

原连续尾还给
$$
\sum_i u_i^2
\le\frac{\sum_i p_i^2}{(1-p_{\max})^2}
\le\frac{3(x+1)}{(x-2)^2}
\le\frac4x,\qquad p_i=z_i/S.
\tag{3.4}
$$
最后一步在 $x\ge64$ 成立。

## 4. 完整加权反馈的显式原像

先取有限指标族及任意 $|c_i|\le1$。目标向量为
$$
Y_E(c)=\sum_i b_i c_i Z_{E,Q}\alpha_i.
\tag{4.1}
$$
由 (2.3)、(3.2)，它有准确原像
$$
\boxed{
X_E(c)=-\sum_i u_i c_i Z_{\mathcal T_E}r_i
\in\mathcal T_E,\qquad
A_E^*X_E(c)=Y_E(c).
}
\tag{4.2}
$$
注意 $b_i(b_i/s_i)=u_i$，没有额外丢失一个原权系数。

(3.3)--(3.4) 与整个合并来源上的 Cauchy 给
$$
\boxed{
\sup_{|c_i|\le1}\|X_E(c)\|
\le2e^8\sqrt{\mathfrak F_1/x}
\le2\sqrt2\,e^8\sqrt\varepsilon
\le3e^8\Delta_{g,Q}.
}
\tag{4.3}
$$
这个界不含 $\|H_i\|$、环境 $\|C^\dagger\|$ 或完整头 condition number。
它保同一个原 forcing、完整上一层零源与所有新位的真实最小来源。

对于无限尾，(3.3)--(3.4) 还证明
$$
\sum_i u_i\|Z_{\mathcal T_E}r_i\|<\infty.
$$
故 (4.2) 的原像在 $\mathcal T_E$ 中绝对范数收敛。
有界算子 $A_E^*$ 可过此极限；(4.1) 亦由前稿的恢复行和
$\sum_i b_i^2=S$ 在绝对范数下收敛。于是 (4.2)--(4.3) 是整个实际无限尾的身份和预算。

## 5. 真正 Moore--Penrose 规范，无闭值域假设

这里只对 (4.1) 已明确落在 $\operatorname{Ran}A_E^*$ 的目标使用 MP。
对任意 $Y=A_E^*X$，其全体原像是
$X+\ker A_E^*$，最小范数原像准确为
$$
(A_E^*)^\dagger Y
=P_{(\ker A_E^*)^\perp}X.
$$
$\ker A_E^*$ 闭，所以这个投影有意义；不需要
$\operatorname{Ran}A_E^*$ 闭。这个构造也给出了目标位于 MP 自然定义域的证书。

因此
$$
\boxed{
\sup_{|c_i|\le1}
\left\|(A_E^*)^\dagger
 \sum_{i\ge x}b_i c_i Z_{E,Q}\alpha_i\right\|
\le2e^8\sqrt{\mathfrak F_1/x}
\le3e^8\Delta_{g,Q}.
}
\tag{5.1}
$$
这在全部目标空间 $\mathcal T_E$ 中真正最小化，而不是先保一个较小 primitive 子块后冒称原 MP。对 $U_Q$，完整 $V_{Q-1}$ 中的 $K_{Q-1}$ 反馈没有删除。

等价地，对任何 $v\in E_Q$，完整配对可直接写成
$$
\left\langle v,\sum_i b_ic_i Z_{E,Q}\alpha_i\right\rangle
=\langle A_Ev,X_E(c)\rangle.
\tag{5.2}
$$
这给出了在该实际相邻旗上的无逆配对表示。

## 6. 与原完整返回仍有的区别

本稿支付的是首源反馈 $\alpha_i=(b_i/s_i)C^*H_i a_{1,i}$。
$\sigma_i=(b_i/s_i)H_iCa_{1,i}$ 没有这个 $C^*$ 左因子，
不能用 (2.3) 改写为同一个来源。

另须保 $A_E^*$ 的投影。对显式原像 $X_E(c)$，
$$
D^*X_E(c)=Y_E(c)+(I-P_{E_Q})D^*X_E(c).
\tag{6.1}
$$
第二项不因此消失。故 (5.1) 不自动给未压缩 $D^*$ 的 MP 原像，也不将相邻左旗逆等同于原完整右链或帽返回的残量逆。原帽空间的真投影和两端 partial 仍需在后续来源识别中保留。

已经得到的是一个带完整自然域、真实最小规范和实际 $\Delta$ 的 adjoint-$D$ 读数。其余原返回仍开，普通 $N=M$ 未由此证明。

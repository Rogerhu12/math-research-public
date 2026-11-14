# R271 附录：首源先消元后的中间 Schur 恰是 primitive 差分 Gram

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_continue。

状态：**已证明。** 本文只处理[首段边界先消元稿](R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md)中带 $\circ$ 的新 Gram。原首源置零后，出生不超过零的输入到同类输出是有界双射，所以第一次 Schur 的整块输入贡献准确抵消。新中间 Schur 因而就是[准确真幂底项稿](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)的出生一差分 Gram。它不是旧强制通量所用 $Q_1$ 的替代式，且不提供高块逆的温和上界。

## 1. 原联合旗与首源为零的最低出生输入

固定原合法 $m,q$，$d=2^m$，记 $A=A_m,D=D_m$。输入和输出沿相对出生 $a=t-h+1$ 作原正交分解
$$
\mathscr C_q=\mathscr X_{\le0,q}\oplus\mathscr X_{1,q}\oplus\mathscr X_{H,q},
\qquad
\mathscr Y_q=\mathscr Y_{0,q}\oplus\mathscr Y_{1,q}\oplus\mathscr Y_{H,q}.
\tag{1.1}
$$
这里 $\mathscr Y_0$ 包含全部出生 $a\le0$，$\mathscr Y_H$ 包含全部 $a\ge2$。逐段准确为
$$
\mathscr X_{\le0,q,t}
=\bigoplus_{i=0}^{d-t}e_i
\left(E_{d-i,q+t}\ominus E_{t,q+t}\right),
\tag{1.2}
$$
$$
\mathscr Y_{0,q,t}
=\bigoplus_{i=0}^{d-t-1}e_i
\left(E_{d-i-1,q+t}\ominus E_{t,q+t}\right).
\tag{1.3}
$$
相应零空间按零块理解。首源和内部算子为
$$
Fc=Dc_1,\qquad(Sc)_t=Ac_t+Dc_{t+1}.
$$
所有出生一首段都是 primitive，且高出生没有首段；所以 $F$ 只读取 $\mathscr X_{\le0}$ 的首段。

置
$$
\mathscr U_0=\ker F\cap\mathscr X_{\le0,q},
\qquad R_0=P_{\mathscr Y_0}S|_{\mathscr U_0}.
\tag{1.4}
$$
由于 (1.2) 的第1段与 $\ker D$ 正交，$c\in\mathscr U_0$ 当且仅当其第1段为零。于是
$$
\ker F=\mathscr U_0\oplus\mathscr X_{1,q}\oplus\mathscr X_{H,q}
\tag{1.5}
$$
是原正交直和。

## 2. $R_0$ 是真正有界双射

先证注入。若 $c\in\mathscr U_0$ 且 $R_0c=0$，则每个内部残量的尾核深度至多为 $t$：
$$
D^t(Ac_t+Dc_{t+1})=0.
$$
因此
$$
D^{t+1}c_{t+1}=-A D^tc_t.
\tag{2.1}
$$
从 $c_1=0$ 归纳，得到 $D^tc_t=0$ 对全部 $t$ 成立。然而 (1.2) 同时给 $c_t\perp E_{t,q+t}$，故每段都为零。即 $\ker R_0=\{0\}$。

再证满射。[原联合旗同时右逆](R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md)已证明 $(F,S)$ 到完整首源和内部输出的直和满射。给定 $y_0\in\mathscr Y_0$，取完整 $c$ 满足
$$
Fc=0,\qquad Sc=(y_0,0,0).
$$
纯尾两带删除和头 $A$ 都不降低相对出生，所以 $S$ 的出生不超过零输出只依赖 $P_{\mathscr X_{\le0}}c$。又 $F$ 只读取该部分，故
$$
u_0=P_{\mathscr X_{\le0}}c\in\mathscr U_0,
\qquad R_0u_0=y_0.
$$
这证明满射。两个空间都是 Hilbert 闭子空间，$R_0$ 有界；由有界逆定理，其逆也有界。这里仅证明固定参数下的合法性，未赋予该逆温和范数。

## 3. 新第一次 Schur 的准确全抵消

在 (1.5) 和 (1.1) 的正交坐标中，记
$$
T_{10}=P_{\mathscr Y_1}S|_{\mathscr U_0},\quad
L_1=P_{\mathscr Y_1}S|_{\mathscr X_1},\quad
L_{21}=P_{\mathscr Y_H}S|_{\mathscr X_1},\quad
S_H=S|_{\mathscr X_H}.
$$
两带结构保证出生不超过零的输入不能直接到出生至少二，因此
$$
\boxed{
S|_{\ker F}=
\begin{pmatrix}
R_0&0&0\\
T_{10}&L_1&0\\
0&L_{21}&S_H
\end{pmatrix}.
}
\tag{3.1}
$$
其 Gram 正是首源先消元的新 $\mathcal G_q^\circ=SP_{\ker F}S^*$。相应块满足
$$
B_0^\circ=R_0R_0^*,\qquad
V_1=T_{10}R_0^*,\qquad
B_1=T_{10}T_{10}^*+L_1L_1^*.
$$
由 §2 的双射性，
$$
R_0^*(R_0R_0^*)^{-1}R_0=I_{\mathscr U_0}.
$$
故第一次完整 Schur 准确为
$$
\boxed{
Q_1^\circ
=B_1-V_1(B_0^\circ)^{-1}V_1^*
=L_1L_1^*.
}
\tag{3.2}
$$
抵消的是同一个原低输入块的全部贡献；没有交换投影与逆，也没有放宽或缩小源空间。

## 4. 与真实 primitive 差分的等距识别

置 $p=q+1$，沿用准确真幂底项稿的
$$
J_j=(D^j|_{\mathcal H_{p+j}})^\dagger|_{K_p},
\qquad H_j=J_j^*J_j,
$$
以及等距满射 $\mathcal I:\mathcal E\to\mathscr X_1$ 和
$\mathcal O:\mathcal F\to\mathscr Y_1$：
$$
(\mathcal I\xi)_{j+1}=(-1)^jJ_jH_j^{-1/2}\xi_j,
\qquad
(\mathcal O\zeta)_t=(-1)^{t-1}J_{t-1}H_{t-1}^{-1/2}\zeta_t.
$$
这里 $\mathcal E_j$ 的头指标为 $0,\ldots,d-j-1$，$\mathcal F_t$ 的头指标为 $0,\ldots,d-t-1$。
真实差分算子为
$$
(\mathcal G\xi)_t
=A\xi_{t-1}-H_{t-1}^{1/2}H_t^{-1/2}\xi_t.
\tag{4.1}
$$
原下降相容式给 $L_1=\mathcal O\mathcal G\mathcal I^*$。故 (3.2) 精确变成
$$
\boxed{Q_1^\circ=\mathcal O(\mathcal G\mathcal G^*)\mathcal O^*.}
\tag{4.2}
$$
$\mathcal G$ 的满射、真实核和最小逆已由前稿的有限递推支付；每个 $H_j$ 都保持原完整幂逆压缩的定义。

若要直接读取其三对角块，记
$$
A_t=A|_{\operatorname{span}\{e_0,\ldots,e_{d-t}\}}:
\operatorname{span}\{e_0,\ldots,e_{d-t}\}
\to\operatorname{span}\{e_0,\ldots,e_{d-t-1}\},
$$
并张量 $I_{K_p}$；另记 $L_t=H_{t-1}^{1/2}H_t^{-1/2}$。则
$$
(\mathcal G\mathcal G^*)_{t,t}=A_tA_t^*+L_tL_t^*,
\qquad
(\mathcal G\mathcal G^*)_{t,t+1}=-L_tA_{t+1}^*.
\tag{4.3}
$$
其余非邻近块为零，下邻块取真正伴随。$A_t^*$ 含显示的实际头截断，不能直接换成未截断 $A^*$。

## 5. 新前两项 LDU 能量的具体身份

对原首源 $r$，令 $b^\circ=F^\dagger r$；它只有首段 $D^\dagger r$。于是 $g_0=Sb^\circ$ 只有 $\mathscr Y_0$ 分量。消去第零输出的唯一低输入修正是
$$
u_0=-R_0^{-1}g_0.
$$
前稿的真幂底链
$$
b_t=(-1)^{t-1}(D^t|_{\mathcal H_{q+t}})^\dagger A^{t-1}r
$$
是唯一具有首源 $r$、输入出生不超过零，且出生不超过零的内部输出为零的链；其唯一性也直接由 (2.1) 得到。因此
$$
b=b^\circ+u_0.
\tag{5.1}
$$
首段与其余段正交，所以新第零项正能量准确为
$$
\boxed{
\mathcal E_0^\circ
=\langle(B_0^\circ)^{-1}g_0,g_0\rangle
=\sum_{t=2}^{d-1}\|(D^t)^\dagger A^{t-1}r\|^2.
}
\tag{5.2}
$$

记前稿中的实际出生一残量为 $Sb=\mathcal O\zeta(r)$。新 Schur 记号的
$\zeta^\circ=V_1(B_0^\circ)^{-1}g_0$ 与之相差一个准确负号：
$$
\zeta^\circ=T_{10}R_0^{-1}g_0=-\mathcal O\zeta(r).
\tag{5.3}
$$
结合 (4.2)，新第一项正能量为
$$
\boxed{
\mathcal E_1^\circ
=\langle(Q_1^\circ)^{-1}\zeta^\circ,\zeta^\circ\rangle
=\|\mathcal G^\dagger\zeta(r)\|^2.
}
\tag{5.4}
$$
这与前稿的
$\alpha_q(r)^2=\|(D^1)^\dagger r\|^2+\mathcal E_0^\circ+\mathcal E_1^\circ$
完全一致。

## 6. 新末块和原同源返回保持原顺序

令 $\mathcal R=L_{21}\mathcal I$，并沿用
$$
Q\xi=\sum_j(A^j)^*H_j^{1/2}\xi_j,\qquad
\Pi=I-Q^*(QQ^*)^{-1}Q=\mathcal G^\dagger\mathcal G.
$$
由 (3.1)，$V_2=L_{21}L_1^*$、$B_2=L_{21}L_{21}^*+S_HS_H^*$。再次作真正 Schur 得
$$
\boxed{
\mathcal H_2^\circ
=S_HS_H^*+\mathcal R(I-\Pi)\mathcal R^*.
}
\tag{6.1}
$$
同时由 (5.3)，
$$
\boxed{
\sigma^\circ
=V_2(Q_1^\circ)^{-1}\zeta^\circ
=-\mathcal R\mathcal G^\dagger\zeta(r)
=B_qa_q(r).
}
\tag{6.2}
$$
因此本次识别确实保留同一个原裸最小链的返回源；并没有通过去掉一个 Schur 逆更换测试向量。

式 (6.1) 的 $I-\Pi$ 正是首段自由 primitive 所产生的零首源低链投影。它仍然在真实高链 Gram 之外贡献正项；不能删掉后把剩余逆宣称同样温和。

本稿没有将 (4.2) 移植给旧 $Q_1$，也没有把新末块正能量认作旧强制通量的全部末块费用。准确真幂底项稿的 $\zeta(r)$ 仍含完整孔层逆滤波，最终 $S_H$ 及 (6.1) 的逆费用仍需在该实际源上支付。

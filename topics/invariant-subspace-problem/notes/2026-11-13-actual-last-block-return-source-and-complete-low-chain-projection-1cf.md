# 工作笔记：真实末块能量的返回残量与完整低链投影

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf。
状态：以下恒等式及固定参数闭像已逐式核对；尚未给返回残量的低成本完整修复，不单独登记为无权能量改进。

本笔记续 [真实头角/正 Gram](../results/R271-appendix-actual-middle-source-corner-elimination-and-positive-gram.md)、[低旗完整头换序](../results/R271-appendix-low-flag-full-head-commutators-and-weighted-source.md) 及 [完整链](../results/R271-appendix-complete-repair-chain-lowering-defects-and-true-schur-contraction.md) §7。保留原 $m,q,d=2^m,A_m,D_m$、全部联合旗及原 Hilbert 范数。

## 1. 低链、高链和固定参数闭像

把原输入写成
$$
\mathscr C=\mathscr X_L\oplus\mathscr X_H,\qquad
\mathscr X_L=\mathscr X_{\le0}\oplus\mathscr X_1,\quad
\mathscr X_H=\mathscr X_{\ge2},
$$
输出写成 $\mathscr Y_L=\mathscr Y_0\oplus\mathscr Y_1$ 与 $\mathscr Y_H=\mathscr Y_2$。记
$$
S_L=P_{\mathscr Y_L}S|_{\mathscr X_L},\quad
S_H=S|_{\mathscr X_H}:\mathscr X_H\to\mathscr Y_H,\quad
Z=\ker S_L.
$$
高出生输入不产生低出生输出。定义
$$
B=P_{\mathscr Y_H}S|_Z=P_{\mathscr Y_H}S^{(1)}|_Z.
$$
这里必须保留输出投影；$S^{(1)}$ 对 $Z$ 的其他低出生部分并非各自为零。

固定 $m,q$ 时 $S_H$ 满射。具体而言
$$
\mathscr X_{H,t}=W_{d-t+1}\otimes E_{t-1,q+t},\qquad
\mathscr Y_{H,t}=W_{d-t}\otimes E_{t-1,q+t}\quad(t\ge2),
$$
而首段为空。对 $f\in\mathscr Y_H$，置 $c_2=0$，逐行使用旧固定孔层相容删除右逆
$$
c_{t+1}=R_D(f_t-A_mc_t),\qquad 2\le t\le d-1.
$$
$R_D$ 将 $E_{t-1,q+t}$ 送入 $E_{t,q+t+1}$；头指标不变，故每步保真实头宽。末项 $c_d$ 只有头 $e_0$，于是 $A_mc_d=0$。这是一个有界有限递推，证明满射；未改善其一般常数。因此
$$
A_H=S_HS_H^*>0,\qquad R_H=S_H^*A_H^{-1}
$$
均合法，$R_H$ 是这个高链的真正最小右逆。

$S_L$ 也满射，因为原 $S$ 满射且高输入不产生低输出。故其核投影 $P_Z$ 合法。最终实际 Schur 补准确为
$$
\mathcal H_2=A_H+BB^*.
$$

## 2. 最优链的正低链度量

写实际最优修复
$$
c^{\min}=c_L+c_H,\qquad \lambda=\|c^{\min}\|.
$$
原 $b$ 只在 $\mathscr X_{\le0}$，且 $Sc^{\min}=0$。所以
$$
c_L\in Z,\qquad c_H=-S_H^*z_2,\qquad A_Hz_2=Bc_L.
$$
定义真正的低链正算子
$$
K=B^*A_H^{-1}B\ge0,\qquad Q=I_Z+K.
$$
于是
$$
z_2=A_H^{-1}Bc_L,\qquad B^*z_2=Kc_L,
$$
$$
\lambda^2=\langle Qc_L,c_L\rangle,
$$
$$
\mathcal E_2
=\langle\mathcal H_2z_2,z_2\rangle
=\langle Kc_L,c_L\rangle+\|Kc_L\|^2.
\tag{2.1}
$$
这些全是原范数中的恒等式。特别，已知的高链部分
$\|c_H\|^2=\langle Kc_L,c_L\rangle\le\lambda^2$；未付的只是 $Kc_L=B^*z_2$。

令 $\mathsf F=D_{\rm first}|_Z$。由于首段没有高出生输入，
$$
\mathsf F c_L=r.
$$
对任意 $u\in Z$，其最小高链完成是
$$
\mathcal E u=(u,-R_HBu)\in\ker S,\qquad
\|\mathcal E u\|^2=\langle Qu,u\rangle.
$$
原极小性因此准确等价于
$$
c_L=\arg\min_{\mathsf Fu=r}\langle Qu,u\rangle,\qquad
Qc_L\perp\ker\mathsf F.
\tag{2.2}
$$
所以
$$
P_{\ker\mathsf F}Kc_L=-P_{\ker\mathsf F}c_L,\qquad
\|P_{\ker\mathsf F}Kc_L\|\le\lambda.
\tag{2.3}
$$
若 $\mathsf FKc_L=0$，在 (2.2) 中以 $Kc_L$ 作零源测试便给
$$
0=\langle Qc_L,Kc_L\rangle=\mathcal E_2.
$$
故真正剩余目标是可见的返回残量 $\mathsf FKc_L$，不是一般环境 $\|K\|$。

更一般地，只要 $a\in Z$ 满足
$\mathsf Fa=\mathsf FKc_L$，则
$$
\mathcal E_2=\langle Qc_L,a\rangle
\le\lambda\|a\|_Q,\qquad
\|a\|_Q^2=\langle Qa,a\rangle.
\tag{2.4}
$$
对 $a$ 取真正最小值，
$$
\mathcal E_2
\le\lambda\,
\lambda_q(\mathsf FKc_L).
\tag{2.5}
$$
右侧 $\lambda_q$ 是同一个完整旧窗的最小修复范数。仅有返回源的原范数上界不能替代它。

## 3. 完整低链投影的精确展开

沿用头角稿的
$$
R_0=S^*|_{\mathscr Y_0},\quad
Z_0=\mathscr X_{\le0}\ominus\operatorname{Ran}R_0,
$$
$$
T_0=S^{(0)*}|_{\mathscr Y_1},\quad
K_{\rm raw}=S^{(1)*}|_{\mathscr Y_1},\quad
K_0=P_{Z_0}K_{\rm raw},
$$
$$
B_0=R_0^*R_0,\qquad
V_1^*=R_0^*K_{\rm raw},\qquad
Q_1=T_0^*T_0+K_0^*K_0.
$$
这里 $K_0$ 与第 2 节的 $K$ 是不同算子。

对任意 $z\in\mathscr Y_H$，令 $P_2$ 表示其中相对出生层恰为 $2$ 的投影，置
$$
u=S^{(1)*}P_2z\in\mathscr X_1,\qquad
\xi=Q_1^{-1}T_0^*u=Q_1^{-1}V_2^*z.
\tag{3.1}
$$
低投影只看 $P_2z$；更高出生的第二下降伴随仍在高输入中。

按 $Z_0\oplus\mathscr X_1$ 记分量，完整低链正交投影准确是
$$
\boxed{B^*z=P_Zu=(-K_0\xi,\ u-T_0\xi).}
\tag{3.2}
$$
证明：将 $u$ 投到 $\operatorname{Ran}S_L^*$ 时，低对偶方程第一行给
$z_0=-B_0^{-1}V_1^*\xi$；代回第二行得到 (3.1)。其输入像为
$(K_0\xi,T_0\xi)$，减去即得 (3.2)。

现在把 $\mathsf F$ 暂按同一 $D_{\rm first}$ 扩到整个低输入，记作 $F$。
$S^{(1)*}$ 向后移动一个段号，故
$$
Fu=0,\qquad FK_{\rm raw}=0.
$$
还有一个需要使用真实高度的消失：
$T_0\xi$ 的首段在 $U_{1,q+1}=\ker D\cap\mathcal H_{q+1}$，所以
$$
FT_0\xi=0.
$$
因此
$$
\boxed{
FB^*z
=-FK_0Q_1^{-1}V_2^*z
=FR_0B_0^{-1}V_1^*Q_1^{-1}V_2^*z.
}
\tag{3.3}
$$
这里完整保留 $P_Z$ 所产生的 $B_0^{-1},Q_1^{-1}$。原始的 $FS^{(1)*}=0$ 不允许把 (3.3) 误写为零。

$FR_0$ 只读取第一段，准确为
$$
FR_0z_0=D\,P_{C_1}A_m^*(z_0)_1.
\tag{3.4}
$$
$P_{C_1}$ 依头坐标限制纯删除核，不能未经证明移过 $D$ 或 $A_m^*$。

## 4. 原第三矩在外桥中的准确位置

对 $t\ge2$，$P_2z_t$ 的高度是 $t-1$。0c 外源分解给
$$
u_{t+1}
=-t(t-1)\,
J_{t+1,q+t+1}\,C\,D^{t-2}(P_2z_t),
\qquad C=D_3.
\tag{4.1}
$$
各项保原头坐标；由于 $i\le d-t-1$，高度 $t+1$ 的输出确在 $C_{t+1}$。
此外
$$
u_1=u_2=0,\qquad V_2^*z=T_0^*u=S^{(0)}u.
\tag{4.2}
$$
特别 $V_2^*z$ 的首段为零，而 $S^{(0)}u$ 必须保留全部 $A_m u_t+D^{(0)}u_{t+1}$。

(4.1) 定位了前向 $D_3$，但它在 (3.3) 中位于真正的
$S^{(0)},Q_1^{-1},V_1^*,B_0^{-1},FR_0$ 之前。这里没有把它移到最终源的最左边；也没有把后续混合造成的第五矩项宣布消失。

## 5. 再消头角及原源范数的半收缩

沿头角稿记 $\mathscr Y_1=\mathscr R\oplus\mathscr E$，
$$
J=T_0|_{\mathscr R},\quad T=T_0|_{\mathscr E},\quad
K_E=K_0|_{\mathscr E},
$$
$$
\Pi=I-J(J^*J)^{-1}J^*,\qquad
\widehat Q_1=T^*\Pi T+K_E^*K_E.
$$
对 (3.1) 这个右侧并非角上为零的方程，仍可准确消元：
$$
\xi_{\mathscr E}
=\widehat Q_1^{-1}T^*\Pi u.
$$
因此
$$
\boxed{
FB^*z=-F K_E\widehat Q_1^{-1}T^*\Pi u.
}
\tag{5.1}
$$
定义 $U=(\Pi T)\widehat Q_1^{-1/2}$、
$V=K_E\widehat Q_1^{-1/2}$，则 $U^*U+V^*V=I$，故
$$
\|K_E\widehat Q_1^{-1}T^*\Pi\|
=\|VU^*\|\le\tfrac12.
$$
于是
$$
\boxed{\|FB^*z\|\le\frac{\|D\|}{2}\|\Pi u\|.}
\tag{5.2}
$$
这只是返回源的原范数预算，未包含 (2.5) 的完整最小修复成本。

对实际 $z=z_2$，原头对角链
$$
\mathscr X_\Delta=\bigoplus_{t=1}^de_{d-t}U_{t,q+t}
$$
及其单链 $\mathcal F$ 满足
$$
\Pi=I_{\mathscr X_1\ominus\mathscr X_\Delta}\oplus P_{\ker\mathcal F}.
$$
旧真实角关系给
$$
P_{\mathscr X_\Delta}\Pi u
=-c_\Delta
-P_{\ker\mathcal F}P_{\mathscr X_\Delta}A_m^*P_{\mathscr E}z_1,
\qquad \|c_\Delta\|\le\lambda.
\tag{5.3}
$$
这里 $z_1$ 是完整对偶中间分量，并非 $Q_1^{-1}\zeta$。
$\Pi u$ 的其他部分是 $u$ 在严格正头缺口的部分。式 (5.3) 把已经支付的角和真实长头跳跃分开，不能删去后一项。

## 6. 尚开的具体预算

可用的变分目标是 (2.4)：构造真正 $a\in Z$，保
$\mathsf Fa=\mathsf FKc_L$，并控制其原完整完成范数
$\|a\|_Q$。若能证明
$\|a\|_Q\le C_{m,q}\sqrt{\mathcal E_2}$，则
$\mathcal E_2\le C_{m,q}^2\lambda^2$。

目前 (3.3)--(5.3) 准确定位该返回源及其已付头角；它们没有给所需 $q^{o(1)}$ 的 $C_{m,q}$。用裸 $\|Q_1^{-1}\|$、删长 $A_m^*$、把原源范数当最小修复范数，或把 $P_ZS^{(1)*}$ 换成 $S^{(1)*}$，都会重新引入未支付的一步。

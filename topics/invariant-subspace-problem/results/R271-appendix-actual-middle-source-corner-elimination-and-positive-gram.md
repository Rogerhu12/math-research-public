# R271 附录：真实中间源的头角消灭、收缩消元与剩余正 Gram

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：已证明。根完整核验实际出生层/头角、正交 Schur 消元、交叉收缩与原能量恒等式。

本稿把实际两出生桥中的中间源进一步限制到一个具体头角的正交补，并在原 Hilbert 范数中消去该角。消元后保留准确的正 Gram 和实际有效源；不把剩余逆当成已获无权上界。

## 1. 全部空间与实际源

固定原合法 $m,q$，$d=2^m$。沿用 [联合旗右逆](R271-appendix-joint-flag-right-inverse-energy-and-head-jump-flux.md) 和 [完整 Gram 及真实低先消元](R271-appendix-complete-repair-chain-lowering-defects-and-true-schur-contraction.md) §7 的空间：
$$
C_t=\bigoplus_{i=0}^{d-t}e_iE_{d-i,q+t},\qquad
Y_t=\bigoplus_{i=0}^{d-t-1}e_iE_{d-i-1,q+t},
$$
$$
\mathscr C=\bigoplus_{t=1}^d C_t,\qquad
\mathscr Y=\bigoplus_{t=1}^{d-1}Y_t,
\qquad
E_{h,p}=\ker D^h\cap\mathcal H_p,\quad
U_{h,p}=E_{h,p}\ominus E_{h-1,p}.
$$
$U_{h,p}$ 的相对出生层为 $a=p-h+1-q$；在第 $t$ 段即 $a=t-h+1$。

写 $D=D^{(0)}+D^{(1)}$ 为第一、第二下降，分别将正交高度下降一、二。准确链
$$
(Sc)_t=A_mc_t+Dc_{t+1}
$$
分解为 $S=S^{(0)}+S^{(1)}$，其中
$$
(S^{(0)}c)_t=A_mc_t+D^{(0)}c_{t+1},\qquad
(S^{(1)}c)_t=D^{(1)}c_{t+1}.
\tag{1.1}
$$
$S^{(0)}$ 保相对出生层，$S^{(1)}$ 将它增加一。

在 $\mathscr C$ 中记 $\mathscr X_{\le0}$ 为出生层 $\le0$ 的部分，$\mathscr X_1$ 为出生层恰为1的部分。后者明确为
$$
\mathscr X_1=
\bigoplus_{t=1}^d\bigoplus_{i=0}^{d-t}
e_iU_{t,q+t}.
\tag{1.2}
$$
在 $\mathscr Y$ 中按 $\le0$、$=1$、$\ge2$ 分成
$\mathscr Y_0,\mathscr Y_1,\mathscr Y_2$，其中
$$
\mathscr Y_1=
\bigoplus_{t=1}^{d-1}\bigoplus_{i=0}^{d-t-1}
e_iU_{t,q+t}.
\tag{1.3}
$$
$\mathscr Y_2$ 是实际通量所用的低核空间。

对真正最优修复，仍取
$$
y=G_q^{-1}r,\qquad b=P_{\mathscr C}D_{\rm first}^*y,\qquad
g=Sb=(g_0,0,0),\qquad z=(SS^*)^{-1}g.
$$
这里 $D_{\rm first}c=Dc_1$，与尾部第一下降 $D^{(0)}$ 不同。旧稿已逐项证明 $b\in\mathscr X_{\le0}$，且 $g$ 只有 $\mathscr Y_0$ 分量。

令
$$
SS^*=
\begin{pmatrix}
B_0&V_1^*&0\\
V_1&B_1&V_2^*\\
0&V_2&B_2
\end{pmatrix},\qquad
Q_1=B_1-V_1B_0^{-1}V_1^*,
$$
$$
\zeta=V_1B_0^{-1}g_0,\qquad
x=Q_1^{-1}\zeta,\qquad
\sigma=V_2x,\qquad
\mathcal H_2=B_2-V_2Q_1^{-1}V_2^*.
\tag{1.4}
$$
故 $z_2=\mathcal H_2^{-1}\sigma$。注意 $x$ 是构成有效源的中间向量；完整对偶的中间分量是
$$
z_1=-x-Q_1^{-1}V_2^*z_2,
\tag{1.5}
$$
不能把二者混同。

旧右逆给某个已支付的 $\gamma>0$ 使
$SS^*\ge\gamma I$。所有以下固定 $m,q$ 的逆和闭像均由此保证；本文不改进这个一般常数。

## 2. 具体头角被第二下降伴随杀掉

定义中间头角
$$
\boxed{
\mathscr R=
\bigoplus_{t=1}^{d-1}e_{d-t-1}U_{t,q+t}
\subset\mathscr Y_1.
}
\tag{2.1}
$$
对该角第 $t$ 段的向量，未压缩的 $D^{(1)*}$ 保头指标
$i=d-t-1$，送到第 $t+1$ 段的高度 $t+2$。
然而 $C_{t+1}$ 在这个头指标只允许
$$
E_{d-i,q+t+1}=E_{t+1,q+t+1}.
$$
高度 $t+2$ 与之正交。因此真实带旗伴随准确满足
$$
\boxed{S^{(1)*}|_{\mathscr R}=0.}
\tag{2.2}
$$

这也是 $\mathscr Y_1$ 上唯一可能发生这种旗外项的头坐标：若
$i\le d-t-2$，则 $d-i\ge t+2$，原 $D^{(1)*}$ 的整个输出都在 $C_{t+1}$ 中。该断言只定位旗边界，不断言这些其他块单射。

由出生层，$S^*\mathscr Y_0\subset\mathscr X_{\le0}$；
而 (2.2) 给
$S^*\mathscr R=S^{(0)*}\mathscr R\subset\mathscr X_1$。
两者正交，所以
$$
\boxed{V_1^*|_{\mathscr R}=0,\qquad P_{\mathscr R}\zeta=0.}
\tag{2.3}
$$
这是原真实 $\zeta=V_1B_0^{-1}g_0$ 的约束，不是另选了一个有利的源。

## 3. 先把低出生层消元写成两个正平方

令
$$
R_0=S^*|_{\mathscr Y_0}:
\mathscr Y_0\longrightarrow\mathscr X_{\le0}.
$$
$B_0=R_0^*R_0\ge\gamma I$，故 $\operatorname{Ran}R_0$ 闭。
置
$$
\mathscr Z_0=\mathscr X_{\le0}\ominus\operatorname{Ran}R_0,\qquad
P_0=R_0B_0^{-1}R_0^*.
$$
$\mathscr Z_0$ 等于仅保留低出生输出行的准确零源核，不是整个 $\ker S$。

定义
$$
T_0=S^{(0)*}|_{\mathscr Y_1}:\mathscr Y_1\to\mathscr X_1,\qquad
K_0=P_{\mathscr Z_0}S^{(1)*}|_{\mathscr Y_1}:
\mathscr Y_1\to\mathscr Z_0.
\tag{3.1}
$$
两个像空间正交。直接展开第一个 Schur 补，得到
$$
\boxed{Q_1=T_0^*T_0+K_0^*K_0.}
\tag{3.2}
$$
具体地，$S^*|_{\mathscr Y_1}=S^{(0)*}+S^{(1)*}$；
第一项在 $\mathscr X_1$，第二项在 $\mathscr X_{\le0}$。
减去 $V_1B_0^{-1}V_1^*$ 恰好只从第二项中投掉 $\operatorname{Ran}R_0$。

还令
$$
b_{\mathscr Z}=P_{\mathscr Z_0}b.
$$
由于 $P_{\mathscr Y_1}Sb=0$，
$$
0=(S^*|_{\mathscr Y_1})^*b,
$$
而 $b\in\mathscr X_{\le0}$，所以
$$
\boxed{\zeta=-K_0^*b_{\mathscr Z}.}
\tag{3.3}
$$
式 (2.2) 同时给 $K_0|_{\mathscr R}=0$。因此 $x=Q_1^{-1}\zeta$ 的角方程是
$$
\boxed{P_{\mathscr R}T_0^*T_0x=0.}
\tag{3.4}
$$
它只针对 (1.4) 的 $x$；不能把它套给 (1.5) 的完整 $z_1$。

## 4. 原 Hilbert 范数中的头角消元

记
$$
\mathscr E=\mathscr Y_1\ominus\mathscr R,\qquad
J=T_0|_{\mathscr R},\quad
T=T_0|_{\mathscr E},\quad K=K_0|_{\mathscr E}.
$$
这里 $J$ 是本节的头角列算子，不是旧固定高度逆 $J_{h,p}$。

由 (3.2)、$K_0\mathscr R=0$ 和 $Q_1\ge\gamma I$，
$$
J^*J\ge\gamma I_{\mathscr R}.
$$
故 $\operatorname{Ran}J$ 闭，可以定义真正正交投影
$$
\boxed{\Pi=I_{\mathscr X_1}-J(J^*J)^{-1}J^*.}
\tag{4.1}
$$
特别 $\|\Pi\|\le1$；并没有把 $(J^*J)^{-1}$ 的范数称为小量。

写 $x=x_{\mathscr R}+x_{\mathscr E}$。
角方程 (3.4) 准确给
$$
x_{\mathscr R}=-(J^*J)^{-1}J^*Tx_{\mathscr E},\qquad
T_0x=\Pi Tx_{\mathscr E}.
\tag{4.2}
$$
将其代入剩余行，得到
$$
\boxed{
\widehat Q_1=T^*\Pi T+K^*K,\qquad
x_{\mathscr E}=\widehat Q_1^{-1}\zeta_{\mathscr E}.
}
\tag{4.3}
$$
$\widehat Q_1$ 是 $Q_1$ 对 $\mathscr R$ 的 Schur 补，所以
$\widehat Q_1\ge\gamma I_{\mathscr E}$。
等价地，它就是两个实际列算子的正 Gram：
$$
\widehat Q_1=(\Pi T)^*(\Pi T)+K^*K.
\tag{4.4}
$$

出生层恰为1的输入经 $S^{(1)}$ 只到出生层恰为2。
因此在原 $\mathscr Y_2$ 中，真实有效源准确为
$$
\boxed{
\sigma=
S^{(1)}\Pi T\,\widehat Q_1^{-1}\zeta_{\mathscr E}.
}
\tag{4.5}
$$
它不仅在 $\mathscr Y_2$，而且只在其中相对出生层恰为2的部分。

### 4.1 投影 Π 的具体单链含义

在 $\mathscr X_1$ 中定义头对角链
$$
\mathscr X_\Delta=
\bigoplus_{t=1}^{d}e_{d-t}U_{t,q+t}.
\tag{4.6}
$$
$J=S^{(0)*}|_{\mathscr R}$ 的像完全在 $\mathscr X_\Delta$。

为核对这点，令
$$
a_t=\langle A_me_{d-t},e_{d-t-1}\rangle,\qquad1\le t\le d-1.
$$
这些是实际头的第一超对角系数。对 $z_t\in U_{t,q+t}$，
$A_m^*$ 从头 $d-t-1$ 向右移动时，联合旗只留下到 $d-t$ 的第一步；再远的头指标已超过 $C_t$ 的头界。另一项 $D^{(0)*}$ 到第 $t+1$ 段、高度 $t+1$，同样落在 (4.6)。

因而 $J$ 正是下列实际单链的伴随：
$$
\mathcal F:\mathscr X_\Delta\to\mathscr R,\qquad
(\mathcal F u)_t=a_tu_t+D^{(0)}u_{t+1}.
\tag{4.7}
$$
这里各 $u_t$ 已按 (4.6) 去掉头基向量。该链满射，因为
$\mathcal F\mathcal F^*=J^*J\ge\gamma I$。
所以
$$
\boxed{
\Pi=
I_{\mathscr X_1\ominus\mathscr X_\Delta}
\oplus P_{\ker\mathcal F}.
}
\tag{4.8}
$$
尤其 (4.2) 给
$$
P_{\mathscr X_\Delta}T_0x\in\ker\mathcal F.
\tag{4.9}
$$
此处已经保留全部真实系数 $a_t$ 和 $D^{(0)}$，没有把该单链换成等权模型。

## 5. 中间逆的交叉输出是一个收缩块

令
$$
U=(\Pi T)\widehat Q_1^{-1/2},\qquad
V=K\widehat Q_1^{-1/2}.
$$
由 (4.4)，
$$
U^*U+V^*V=I_{\mathscr E}.
$$
故
$$
UV^*VU^*=UU^*-(UU^*)^2\le\tfrac14I_{\mathscr X_1},
$$
即
$$
\boxed{\|UV^*\|\le\tfrac12.}
\tag{5.1}
$$
这也可看作 $h\mapsto(Uh,Vh)$ 的等距嵌入所给正交投影的一个非对角块。

由于 $\zeta_{\mathscr E}=-K^*b_{\mathscr Z}$，(4.2)--(4.5) 成为
$$
u_1:=T_0x=-UV^*b_{\mathscr Z},\qquad
\sigma=S^{(1)}u_1.
\tag{5.2}
$$
因此在原 Hilbert 范数中，无需单独估计 $\widehat Q_1^{-1}$，就有
$$
\boxed{
\|u_1\|\le\tfrac12\|b_{\mathscr Z}\|,\qquad
\|\sigma\|\le\tfrac{\|D^{(1)}\|}{2}\|b_{\mathscr Z}\|
\le\frac1{2m}\|b_{\mathscr Z}\|.
}
\tag{5.3}
$$

还能保留准确的能量信息。记
$$
\mathcal E_0=\langle B_0^{-1}g_0,g_0\rangle,\quad
\mathcal E_1=\langle Q_1^{-1}\zeta,\zeta\rangle,\quad
\mathcal E_2=\langle\mathcal H_2^{-1}\sigma,\sigma\rangle.
$$
旧正交分解给
$$
\|b_{\mathscr Z}\|^2
=\|b\|^2-\mathcal E_0
=\lambda^2+\mathcal E_1+\mathcal E_2,
\qquad \lambda=\|c^{\min}\|.
\tag{5.4}
$$
同时
$$
\mathcal E_1=\|V^*b_{\mathscr Z}\|^2,\qquad
\|u_1\|^2=\mathcal E_1-\|VV^*b_{\mathscr Z}\|^2.
$$
若 $b_{\mathscr Z}\ne0$，Cauchy--Schwarz 给
$$
\|VV^*b_{\mathscr Z}\|^2
\ge\frac{\mathcal E_1^2}{\|b_{\mathscr Z}\|^2}.
$$
故真正源还满足
$$
\boxed{
\|\sigma\|^2
\le
\|D^{(1)}\|^2
\frac{\mathcal E_1(\lambda^2+\mathcal E_2)}
{\lambda^2+\mathcal E_1+\mathcal E_2}.
}
\tag{5.5}
$$
全零时右侧按零解释。这是未加权的源范数约束；不是把
$\mathcal E_2=\|\mathcal H_2^{-1/2}\sigma\|^2$
替成 $\|\sigma\|^2$。

## 6. 与完整最优链的一个准确角关系

因为 $Sc^{\min}=0$ 且 $S^{(1)*}\mathscr R=0$，
$\mathscr R$ 行只读取 $S^{(0)}c^{\min}$。
进一步由 (4.7) 的具体头坐标，这些行只读取
$c^{\min}$ 的 $\mathscr X_\Delta$ 部分。因此
$$
\boxed{
c_\Delta:=P_{\mathscr X_\Delta}c^{\min}\in\ker\mathcal F,
\qquad \|c_\Delta\|\le\lambda.
}
\tag{6.1}
$$

又因 $b$ 只在出生层 $\le0$，
$c^{\min}=b-S^*z$ 在 $\mathscr X_\Delta$ 上给
$$
c_\Delta=-P_{\mathscr X_\Delta}
\bigl(S^{(0)*}z_1+S^{(1)*}z_2\bigr).
$$
对 $\ker\mathcal F$ 投影会杀掉 $S^{(0)*}P_{\mathscr R}z_1=JP_{\mathscr R}z_1$。
而 $D^{(0)*}$ 保头指标，只能从 $\mathscr R$ 到 $\mathscr X_\Delta$；
因此余下的 $S^{(0)*}P_{\mathscr E}$ 部分准确只来自头 $A_m^*$ 的较长跳跃。得到
$$
\boxed{
P_{\ker\mathcal F}P_{\mathscr X_\Delta}S^{(1)*}z_2
=-c_\Delta-
P_{\ker\mathcal F}P_{\mathscr X_\Delta}A_m^*P_{\mathscr E}z_1.
}
\tag{6.2}
$$
其中 $A_m^*$ 逐段作用，并仍按上式的实际坐标投影。第一项已经由 $\lambda$ 支付；第二项是明确保留下来的真实头跳跃项。式 (6.2) 不把完整 $z_1$ 与 (1.4) 的 $x$ 混同。

## 7. 当前得到和仍需支付的部分

真实源 $\zeta$ 确实对具体头角 $\mathscr R$ 为零；该角可通过收缩 $\Pi$ 消去，剩下 (4.4) 的准确正 Gram，且实际 $\sigma$ 有 (5.3)--(5.5) 的原范数约束。完整最优链还给 (6.1)--(6.2) 的原 $\lambda$ 角测试。

剩余 $\widehat Q_1$ 和最终 $\mathcal H_2$ 仍须保留。这里没有证明它们与 $D_3$、各高度逆或占据算子交换，也没有给 $\mathcal E_2/\lambda^2$ 或实际 $\widetilde C_{\rm tot}$ 所需的无权上界。连续出生桥的交换子最小能量界，只能按其已证的真实次序再接入这些算子。

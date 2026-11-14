# R239 附录：修复链闭像、准确旗链 Riccati 与末端泄漏

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：下述有限链和无限窗口结论已证明；没有得到原真实 $\lambda_q(w)$ 的所需无权增长界。

承接[实际修复 Gram](../results/R239-appendix-exact-repair-gram-schur-complement-and-single-block-lift.md)以及[配对纯核观测稿](../notes/2026-11-13-paired-primitive-witnesses-local-minimal-energy-lower-bound-and-true-range-suppression-boundary-resume.md)。先前 Gram 稿只使用 inf，没有假定内部输出闭像；本稿补证固定有限 $m,q$ 的闭像和极小值取得。所有有界常数可以依赖 $m,q$，不把它们宣布为可直接吸收实际 carry 的统一常数。

## 1. 固定有限尾塔的有界 Jordan 分解

固定 $m,q$，记 $d=2^m$、$A=A_m$、$D=D_m$，以及
$$
H_t=\mathcal H_{q+t}^{(m),{\rm tail}}\qquad(1\le t\le d).
$$
此处先只记尾空间；原头张量因子随后完整补回。

取 R254J 同一个有限源层相容族 $R_k$，输入上界至少为 $q+d$、最大原像阶至少为 $d-1$，使以下出现的所有 $R_k$ 均有界，且 $DR_k=R_{k-1}$、$R_0=I$。定义
$$
K_1=H_1,\qquad K_s=\ker(D:H_s\to H_{s-1})\quad(2\le s\le d).
$$
对每个 $t$ 令
$$
V_t:\bigoplus_{s=1}^tK_s\longrightarrow H_t,\qquad
V_t(h_1,\ldots,h_t)=\sum_{s=1}^tR_{t-s}h_s.
\tag{1.1}
$$
这是有界同构。证明可从最高删除幂开始逐次剥离：
对 $u\in H_t$，先取 $h_1=D^{t-1}u$；减掉 $R_{t-1}h_1$ 后，
再取剩余项的 $D^{t-2}$ 像为 $h_2\in K_2$；如此继续。
相容等式使每次更高坐标准确为零，也证明唯一性。只有有限步且每个算子有界，所以逆有界。这里 $h_1$ 是任意 $H_{q+1}$ 向量，绝非仅在 $\ker D$ 内。

对 $t\ge2$，同一相容族给
$$
D V_t(h_1,\ldots,h_t)
=V_{t-1}(h_1,\ldots,h_{t-1}).
\tag{1.2}
$$
因此有限尾塔算子
$$
\mathbb D(c_1,\ldots,c_d)=(Dc_2,\ldots,Dc_d,0)
$$
经 $V=\bigoplus_tV_t$ 相似，成为
$$
\bigoplus_{s=1}^d J_{d-s+1}\otimes I_{K_s},
\tag{1.3}
$$
其中 $J_r$ 是长度 $r$、非零边权均为1的有限后移。各 $K_s$ 可以无限维。

把原头完整张量补回后，$I_{\rm head}\otimes V$ 与 $A$ 交换。于是内部输出
$$
S=A+\mathbb D
$$
相似于有限直和
$$
\bigoplus_{s=1}^d
 \left(A\otimes I_{d-s+1}
       +I_{\rm head}\otimes J_{d-s+1}\right)
 \otimes I_{K_s}.
\tag{1.4}
$$
括号内都是有限矩阵。有限矩阵张量任意恒等算子的像闭，有限直和仍闭，故
$$
\boxed{\operatorname{Ran}S\text{ 与 }\operatorname{Ran}S^*\text{ 均闭。}}
\tag{1.5}
$$
本节没有要求原无限尾 $D$ 在整个 Hilbert 空间上满射。

## 2. Gram 伴随极小值准确取得

令 $\mathscr K=\ker S$，$D_0^*y=(D^*y,0,\ldots,0)$。原实际能量为
$$
\mathcal E_{m,q}(y)
=\|P_{\mathscr K}D_0^*y\|^2
=\inf_z\|D_0^*y-S^*z\|^2.
$$
由 (1.5)，这个 inf 取得。选择
$$
z_y\in(\ker S^*)^\perp,\qquad
S^*z_y=P_{\operatorname{Ran}S^*}D_0^*y,
\tag{2.1}
$$
则 $z_y$ 唯一，而且 $y\mapsto z_y$ 有界，常数可以依赖 $m,q$。
记
$$
f_y=D_0^*y-S^*z_y=P_{\mathscr K}D_0^*y.
$$
于是
$$
\|f_y\|^2=\mathcal E_{m,q}(y),\qquad S f_y=0.
\tag{2.2}
$$
(2.1) 是实际极小链，不是另选一个便于估计的右逆链。

## 3. 头旗子上的正 Riccati 递推

任何 $c\in\mathscr K$ 都满足
$$
Dc_t=-Ac_{t-1}\quad(t\ge2),\qquad Ac_d=0.
$$
从末端向前应用 $A$，得到
$$
\boxed{
c_t\in V_t^{\rm head}\otimes H_t,\qquad
V_t^{\rm head}=\ker A^{d-t+1}.
}
\tag{3.1}
$$
特别 $V_1^{\rm head}$ 是完整原头，$V_d^{\rm head}=\ker A$。

令 $A_t$ 为 $A:V_t^{\rm head}\to V_{t+1}^{\rm head}$ 的限制，
作用于同一尾层；其伴随必须取这两个头子空间之间的伴随。
令
$$
D_t:V_{t+1}^{\rm head}\otimes H_{t+1}
 \longrightarrow V_{t+1}^{\rm head}\otimes H_t
$$
为纯尾删除。固定层上 $D_t$ 满射且有有界右逆。

从 $W_d=I$ 开始，倒序定义
$$
\boxed{
\begin{aligned}
Q_t&=D_tW_{t+1}^{-1}D_t^*,\\
W_t&=I+A_t^*Q_t^{-1}A_t
\qquad(t=d-1,\ldots,1).
\end{aligned}
}
\tag{3.2}
$$
每个 $W_t$ 都是对应 $V_t^{\rm head}\otimes H_t$ 上有界且
$W_t\ge I$ 的正可逆算子。每个 $Q_t$ 也严格正有界可逆：
若 $\|W_{t+1}\|\le C$，则
$Q_t\ge C^{-1}D_tD_t^*>0$，最后一步使用固定层的满射。

其含义可直接归纳验证：
$$
\langle W_tu,u\rangle
=\min\left\{\sum_{s=t}^d\|c_s\|^2:
 c_t=u,\ Dc_{s+1}=-Ac_s,\ Ac_d=0\right\}.
\tag{3.3}
$$
归纳步使用带正权的最小原像公式：给定
$D_tc_{t+1}=-A_tu$，
$$
\min\langle W_{t+1}c_{t+1},c_{t+1}\rangle
=\langle Q_t^{-1}A_tu,A_tu\rangle.
$$
由 (3.1)，没有遗漏真正可行链；反过来递推给出的每段都满足所需约束。

最后令 $D_0$ 为完整头上的第 $q+1$ 层到第 $q$ 层删除。
则原实际 Gram 和最小能量准确为
$$
\boxed{
\mathsf G_{m,q}=D_0W_1^{-1}D_0^*,\qquad
\lambda^2=\langle\mathsf G_{m,q}^{-1}r,r\rangle.
}
\tag{3.4}
$$
这保留每段可自由选择的 $\ker D$ 分量。不能把 (3.2) 中的逆换成标量算子范数而仍称其为最小能量。

## 4. 最末极小链的实际伪逆动力学

由 (2.1)，任意只在第 $d$ 个坐标取值于 $\ker A^*$ 的向量都属于
$\ker S^*$，所以
$$
z_{y,d}\in\operatorname{Ran}A.
$$
再用 (2.2) 的末端方程 $Af_{y,d}=0$，得到
$$
AA^*z_{y,d}=-A D^*z_{y,d-1}.
$$
因 $AA^*$ 在有限头 $\operatorname{Ran}A$ 上正可逆，
$$
\boxed{
z_{y,d}=-(A^*)^\dagger D^*z_{y,d-1}.
}
\tag{4.1}
$$
这里 $\dagger$ 是原头 Moore--Penrose 逆。

虽然 $A^d=0$，实际的 $(A^*)^\dagger$ 不幂零。可在两个原有限头直接核实，不需要抽象校准例。

置 $W=N_0^{[m]}$，按原二进标准基有 $We_n=w_ne_{n-1}$、$w_n>0$。两型均有
$$
A=P(W),\qquad P(z)=z+c_2z^2+\cdots,
$$
其中
$$
c_2=\frac{b_1}{\eta_0}\quad(N),\qquad
c_2=\frac{b_1}{\eta_0}-1\quad(Y),\qquad
b_1=\frac14,\quad\eta_0=e^{-1070}.
\tag{4.2}
$$
因此 $c_2>0$。一次系数非零使
$$
\ker A^*=\operatorname{span}\{e_{d-1}\},\qquad
\operatorname{Ran}A^*=\operatorname{span}\{e_1,\ldots,e_{d-1}\}.
$$
从 $\operatorname{span}(e_0,\ldots,e_{d-2})$ 到该像的 $A^*$ 矩阵是可逆下三角矩阵 $M$，主对角线为
$w_1,\ldots,w_{d-1}$，首条次对角线为
$c_2w_iw_{i+1}$。故 $M^{-1}$ 的首条次对角线准确为 $-c_2$。
在完整头中补零得到 $(A^*)^\dagger$，于是
$$
\boxed{
\operatorname{Tr}((A_m^*)^\dagger)=-(d-2)c_2\ne0
\qquad(m\ge2).
}
\tag{4.3}
$$
所以 (4.1) 的真实末端传播不能因 $A_m^d=0$ 自动截断。这只排除该截断推理，不推出一般最小能量或无权逼近失败。

## 5. 真实核配对的准确末端泄漏恒等式

取真实 $w\in M=\ker T$，令
$v=v_{m,q}(w)$、$r=A v_q$、$E_m=L-T$。
对任意源 $y\in\mathcal H_q^{(m)}$ 与任意有限链 $z=(z_1,\ldots,z_d)$，置
$$
\psi=y-\sum_{t=1}^dz_t,\qquad
f=D_0^*y-S^*z.
$$
所有项按其尾孔层嵌入全空间。直接逐层展开给
$$
L^*\psi
=A^*y+f-D^*z_d,
$$
三部分分别在第 $q$ 层、$q+1$ 至 $q+d$ 层、第 $q+d+1$ 层。
用 $Lw=E_mw$ 得到
$$
\boxed{
\begin{aligned}
\langle r,y\rangle
={}&-\sum_{t=1}^d\langle w_{q+t},f_t\rangle
+\langle w_{q+d+1},D^*z_d\rangle\\
&+\langle E_mw,\psi\rangle
+\langle A(v_q-w_q),y\rangle.
\end{aligned}
}
\tag{5.1}
$$
这是对任意链成立的恒等式，不依赖极小值取得。

取 (2.1) 的实际极小链 $z=z_y$，合法窗口中已有
$\|E_m\|\le26\eta_{m-1}$、
$\|v-P_{\le q}^{(m)}w\|\le e^{-74d^4}\|w\|$。故
$$
\boxed{
\begin{aligned}
|\langle r,y\rangle|
\le{}&
\|P_{[q+1,q+d]}^{(m)}w\|\sqrt{\mathcal E_{m,q}(y)}
+|\langle w_{q+d+1},D^*z_{y,d}\rangle|\\
&+26\eta_{m-1}\|w\|
 \sqrt{\|y\|^2+\|z_y\|^2}
+6e^{-74d^4}\|w\|\,\|y\|.
\end{aligned}
}
\tag{5.2}
$$
特别，若 $r\ne0$，取 $y=\mathsf G_{m,q}^{-1}r$，则
$\langle r,y\rangle=\mathcal E(y)=\lambda^2$。
此式把真实最小能量的未控项准确集中到末端配对以及相应的对偶范数预算。固定 $m,q$ 的有界性并不足以吸收这些项；不能删除末端配对，也不能只因 $\eta$ 小就忽略乘在它后面的对偶范数。

## 6. 加宽窗口、正末端罚项与无限高尾极限

对任意长度 $h\ge1$，定义相应内部输出 $S_h$、核 $\mathscr K_h$ 和伴随能量
$$
\mathcal E_{m,q}^{[h]}(y)
=\inf_{z_1,\ldots,z_h}
\left[\|D^*y-A^*z_1\|^2
+\sum_{t=2}^h\|D^*z_{t-1}+A^*z_t\|^2\right].
$$
$h=d$ 是原 Gram 能量；$h<d$ 时该形式可以退化，不宣布正可逆。

把长度 $d+h$ 的链在第 $d$ 段分开，准确得到
$$
\boxed{
\mathcal E_{m,q}^{[d+h]}(y)
=\inf_z\left[
\|D_0^*y-S_d^*z\|^2+
\mathcal E_{m,q+d}^{[h]}(z_d)
\right].
}
\tag{6.1}
$$
第二项是非负的真正末端罚项。使用 $z=z_y+u$ 以及
$f_y\perp\operatorname{Ran}S_d^*$，还可写成
$$
\boxed{
\mathcal E_{m,q}^{[d+h]}(y)
=\mathcal E_{m,q}^{[d]}(y)
+\inf_u\left[
\|S_d^*u\|^2+
\mathcal E_{m,q+d}^{[h]}(z_{y,d}+u_d)
\right].
}
\tag{6.2}
$$
所以加宽窗口使 Gram 形式增大、同一源的最小修复范数减小。

固定 $m$ 时，有限窗口最小值下降到整个无限高尾的最小值。
证明如下。取一次有界可逆的有限头 Jordan 相似，把 $A$ 化为若干后移链，并赋予每条头链的基向量级数 $0,\ldots,r-1$。
于是 $A+D$ 按“头链级数加尾孔数”严格降低1；投影到尾孔 $>q$ 与此分级交换。故内部核
$$
\mathscr K_\infty=
\ker\bigl(P_{>q}^{(m)}L|_{\mathcal H_{>q}^{(m)}}\bigr)
$$
在这个总级数下逐级分解。截取有限总级数保持内部核，并强收敛到原向量；把有限头相似变回去仍强收敛。
当截断级数至少为 $q+d$ 时，第 $q$ 输出也准确保持，因为它只来自第 $q+1$ 尾层及有限头级数 $0,\ldots,d-1$。

因此每个无限高尾可行修复都可由具有同一源的有限窗口修复强逼近。记两者最小值为 $\lambda^{[h]}(r)$、$\lambda^{[\infty]}(r)$，则
$$
\boxed{
\lambda^{[h]}(r)\downarrow\lambda^{[\infty]}(r)
\quad(h\to\infty,\ m,q\text{固定}).
}
\tag{6.3}
$$
相似常数可以依赖 $m$；本证明没有给随 $m,q$ 一致的收敛速率。

最后，配对纯核稿的坏族下界对任意加宽窗口仍成立：
它只使用前 $t$ 段的
$D^tc_t=(-1)^{t-1}A^tv_q$，不使用末端 $Ac_h=0$。
同一论证也适用于无限高尾可行修复。因此该稿的单位低输出输入满足
$$
\lambda_{m(q),q}^{[\infty]}(v_q^{\rm bad})
\ge\exp[(c_0-o(1))(\log q)^{4/3}],
\qquad c_0=0.1747818284\ldots.
\tag{6.4}
$$
单靠加宽窗口不能绕开整个低输出空间的障碍；真实投影范围上的额外条件仍然必需。原 $\lambda_q(w)$ 的增长控制尚未完成。

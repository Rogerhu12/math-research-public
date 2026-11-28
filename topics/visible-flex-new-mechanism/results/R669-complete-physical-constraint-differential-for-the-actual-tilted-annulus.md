# R669：真实斜圈环带的两主曲率、双轴法向与经线长活动行

2026-11-28。从 [R659](R659-finite-angle-unit-latitudes-and-full-displacement-port.md) 的真实 810 维末场继续，在实际曲面上同时求度量和厚度约束。本文给出新增全部有限系数的微分。它们可在已离开等距方程的候选上使用，因为第一、第二基本形式均从同一实际位置 $F$ 求得。公开有限输入见[续算范围](../notes/2026-11-28-r669-actual-finite-tilt-reach-continuation-scope.md)。

## 真实主曲率行

使用 $Q^T$ 刚框。令 $D=Q^TF_r,Y=Q^TF_\varphi,A=D\times Y,n=A/|A|$，$Z_{ij}=Q^TF_{ij}$，$g_{ij}=\langle Q^TF_i,Q^TF_j\rangle,~b_{ij}=n\cdot Z_{ij}$。在任一活动的简单主曲率方向 $v=(v_r,v_\varphi)$，取 $v^Tgv=1,bv=\kappa gv$。对原始参数的任意方向，
$$
 \delta n=(I-nn^T)(\delta D\times Y+D\times\delta Y)/|A|,
$$
$$
 \boxed{\delta\kappa=\delta n\cdot Z(v,v)+n\cdot\delta Z(v,v)
       -2\kappa(v_rD+v_\varphi Y)\cdot(v_r\delta D+v_\varphi\delta Y).}
$$
这是广义 Rayleigh 商的变化，微分特征方向的项由特征方程和归一化消去。它不以参考旋转度量代替真实 $g$。两个法向门的微分是 $\delta n\cdot Q^Te_z$ 和 $\delta n\cdot Q^TR_y(\vartheta)e_z$。本有限输入用 $T\kappa_{\max}-.92,-T\kappa_{\min}-.92$ 与 $.22-n\cdot Q^Tv$ 的正部作附加行；取样物理严格目标为 $T=.03$、$T|\kappa|\le1$ 与双点积为正。正部折点、特征值重合或不同网点并列最大时只是分段可微；实际全非线性试步重新取全部最大值，不能用单一选定方向声称跨折点的经典导数。

每个标量物理量同时保留正权全网正部和单个最坏超额；后者防止靠缩窄内接圈尖峰降低积分。组装时只跳过当前正部导数严格不活动的几何行，原度量的整网、全部原始列和完整小奇异值方向保留。活动物理行、其真实试步和所有列接受独立中心差分核对。

## 形状列的一、二阶精确组装

每个体场列是 $B(r)\sin(j\varphi)$。固定 $w=u$ 或 $v$，记 $V=T_w\sin(j\varphi)$，$P_0$ 为零均值原函数，$M_0$ 为减均值。则
$$
 \delta T=BV,\quad \delta T_r=B V_r+B'V,\quad
 \delta T_{rr}=B V_{rr}+2B'V_r+B''V .
$$
$V_r,V_{rr}$ 用实际 $u_r,v_r,u_{rr},v_{rr}$ 对单位切向的完整链式微分取得。置 $U= P_0 V,H=M_0V$，并同样对 $V_r,V_{rr}$ 定义 $U_r,U_{rr},H_r$。令 $\Omega=\omega'J$，$Jx=e_y\times x$。对 $B,B',B''$ 的三个通道，分别有下表，所有进入曲率的径向加速度列均出现。

| 物理变化 | $B$ | $B'$ | $B''$ |
|---|---|---|---|
| $\delta D$ | $U+rU_r+r\Omega U$ | $rU$ | $0$ |
| $\delta Y$ | $rH$ | $0$ | $0$ |
| $\delta Z_{rr}$ | $2U_r+rU_{rr}+2\Omega(U+rU_r)+r\omega''JU+r\Omega^2U$ | $2U+2rU_r+2r\Omega U$ | $rU$ |
| $\delta Z_{r\varphi}$ | $H+rH_r+r\Omega H$ | $rH$ | $0$ |
| $\delta Z_{\varphi\varphi}$ | $r\partial_\varphi H$ | $0$ | $0$ |

中心导数列 $\delta C'=B e_k$ 则给 $\delta D=BQ^Te_k,\delta Z_{rr}=B'Q^Te_k$。数值奇角原函数和角导数取同一 Fourier 插值位置自身，连续全角误差保留独立加密读数。

## 真实端姿和固定度量

设计阶段用 $E=\langle |D|^2\rangle$，物理半径经线长
$$
 S=\int_a^b\sqrt E\,dr,\qquad \delta S=\int_a^b
        \frac{\langle D\cdot\delta D\rangle}{\sqrt E}\,dr .
$$
[R665](R665-end-tangent-and-length-cost-for-finite-tilt.md) 的每个反向成对方位给 $S\ge (D_0\pm C)\cdot e_\beta+T[q(|\vartheta+\beta|)+q(|\beta|)]$，其中 $q(v)=v-\sin v$，两个绝对值角距不超过 $\pi$。所选 $\beta\in[-.25,.65]$ 均满足 $T(|\vartheta+\beta|+|\beta|)< b-a$，故一切满足裸弦的候选都适用。$\delta C=\int_b^a\delta C' dr$ 由同一基的准确原函数给出。在 181 个 $\beta$ 和两个符号的真实最大处取实际活动行微分，再以所有方向评价试步。全范围 $\beta$ 的最大值不由有限角网的值自称已包围。

若将一次形状和 513 角均值函数定义的 $E_*(r)$ 冻结，后继始终对同一 $E_*$ 求解，$\delta S_*=0$；端圈中心仍可改变。首次冻结另要求实测度量、主曲率、双法向、R665 经线长、R662 实际姿态和闭合组件的细网预算过门。若固定度量精化发生，继续独立评价源 513/1025 角估计差以及候选径向、角向单独和联合加密。本文给方程和有限候选上的微分，并未给出已满足这些门的实际解。

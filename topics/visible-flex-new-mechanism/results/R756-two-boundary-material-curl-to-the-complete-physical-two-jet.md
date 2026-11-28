# R756　真实两边环带的旋度、相对位置、二阶导数与双向法球

使用 [R750](R750-two-rigid-core-disks-and-all-prescribed-annulus-chords.md) 的真实环带。$r\in[\alpha,1]$ 从已给刚芯开带到已给外领；$\alpha$ 是同一条固定材料截线，取数值截线须证明它仍在刚芯开带内。$s\in\mathbb R/\mathbb Z$ 是原物质周标。设 $X_0$ 为真实源，$R\in SO(3)$，$\beta_j=R X_{0,j}$。其点态 Gram 就是原 $g$，允许 $g_{rs}\ne0$。给出两个实际位置圈 $P_i,P_o$ 及相邻规定片。以下依赖 $\beta$ 的真实一阶导数和 $K_s$；可分片核算，但必须在真结有使积分原函数为 $C^2$ 的共同迹。每一所用角导数须能在全径域积分下交换；无穷尾需相应全尾控制。相位先固定，统一的相位胞证据才覆盖连续运动。

## 相对位置只有一个周向原函数

令

$$
 K=\partial_r\beta_s-\partial_s\beta_r,\quad
 B_j=P_j'-\beta_s(r_j),\quad r_i=\alpha,\quad r_o=1,\quad
 \Delta(s)=\int_\alpha^1\beta_r\,dr-(P_o-P_i).
$$

R750 归档的物理 Cartesian 旋度乘上有符号 $r\varphi_s$ 才是 $K$。取 $K_s$ 必须微分整个乘积。两条位置原函数为

$$
 F_o=P_o-\int_r^1\beta_r,\qquad F_i=P_i+\int_\alpha^r\beta_r,\qquad
 F_i-F_o=\Delta,\qquad \Delta'=B_i-B_o-\int_\alpha^1K.
$$

最后两式分别由消去同一积分区间及对 $s$ 求导得到。$\int_\alpha^1(\beta_r-X_{0,r})$ 形式的原计费 ray 与该 $\Delta$ 相同，只须从原给定的位移差中包含真实内、外点。沿周胞宽 $h$，已知两端真实 $|\Delta|\le A_L,A_R$（包含积分误差），且 $D'\ge |B_i|+|B_o|+\int|K|$ 全胞有效。按到左、右或最近端的材料路程积分，得

$$
 |\Delta|\le\min(A_L+hD',\,A_R+hD',\,\max(A_L,A_R)+hD'/2).
$$

这条式子以真正全胞 $K$ 界连接有限端 ray。源场整体误差不为零时，即便两边硬钉，未校正的 $\Delta$ 仍然需要独立读取。

## 同一代表的六项误差

令 $\chi(\alpha)=1,\chi(1)=0$，在各规定边近旁取相应常值，$0\le\chi\le1$。实际混合 $F=F_o+\chi\Delta$ 满足

$$
 A_o=B_o+\int_r^1K,\qquad A_i=B_i-\int_\alpha^rK,\qquad
 F_r=\beta_r+\chi'\Delta,\quad F_s=\beta_s+(1-\chi)A_o+\chi A_i .
$$

又有

$$
 F_{rr}=\partial_r\beta_r+\chi''\Delta,\quad
 F_{rs}=\partial_s\beta_r+\chi'\Delta',\quad
 F_{ss}=\partial_s\beta_s+(1-\chi)\partial_sA_o+\chi\partial_sA_i .
$$

$\partial_sA_o=B_o'+\int_r^1K_s,\ \partial_sA_i=B_i'-\int_\alpha^rK_s$。位置相对两支分别为 $\chi\Delta$ 与 $-(1-\chi)\Delta$。这些是同一 $F$ 的导数。R750 实现从更内侧中心扣掉的残差在整个 $\alpha$ 以内刚运时，等于 $-\Delta$：从原中心至 $\alpha$ 的积分正好是该刚姿的端点差。因此径向权相同且芯边两侧均在常值带，精确积分定义的原实现给同一混合。有限 Gauss、角差分、轴下标和所有表示舍入如要计入连续结论，需给被选 $C^2$ 代表相对该精确积分的六项独立误差并分别加到上述项。

在 $r_j$，位置、$s,ss$ 等于 $P_j,P'_j,P_j''$；$r,rr,rs$ 分别等于 $\beta_r,\partial_r\beta_r,\partial_s\beta_r$，须与实际规定片的同三迹逐项比较。$\chi'=\chi''=0$ 是这里使用的真边迹。若已知 $\beta=dP_{\rm given}$ 于整个相邻开领，则六迹一致且该领逐点按给定片实现。只有端点三迹时只得端迹结论。非零实现误差逐项保留。

## 真 $g$ 的混项、物理曲率和正投影

记两列误差在材料坐标的范数上界为 $b_r,b_s$。取实上三角 $J$ 使 $J^TgJ=I$：

$$
 J_{11}=g_{rr}^{-1/2},\quad J_{12}=-g_{rs}/\sqrt{g_{rr}\det g},
 \quad J_{21}=0,\quad J_{22}=\sqrt{g_{rr}/\det g}.
$$

于是归一两列误差至多 $e_1=|J_{11}|b_r,\ e_2=|J_{12}|b_r+|J_{22}|b_s$。置 $e=(e_1^2+e_2^2)^{1/2}$。由于 $\beta J$ 正交，$G=F^*\mathrm e$ 的相对 Gram 算子误差 $\le2e+e^2$。$e<1$ 时 $G\ge(1-e)^2 g$，同定向归一法向与 $N_\beta$ 之差至多 $n=\min(2,2c)$，其中 $c=e_1+e_2+e_1e_2$ 是未归一叉积误差。若 $N_\beta\cdot v\ge m$ 对某真实单位轴成立，则 $N_F\cdot v\ge m-n$。若 $m>c$，还得 $N_F\cdot v\ge(m-c)/(1+e)^2$。每个投影轴独立支付；全局图另需同一扩展的 proper 条件。

用 $\Gamma^k_{ij}$ 表示原 $g$ 的真实联络，置 $T_{rr}=\partial_r\beta_r-\Gamma^k_{rr}\beta_k$，$T_{rs}=T_{sr}=\partial_s\beta_r-\Gamma^k_{rs}\beta_k$，$T_{ss}=\partial_s\beta_s-\Gamma^k_{ss}\beta_k$。允许 $T$ 在 $K\ne0$ 时仅是比较用对称二张量。由上述微分式取得实际物理二阶残差 $b_{ij}$ 后，每项协变残差至多 $d_{ij}=b_{ij}+\sum_k|\Gamma^k_{ij}| b_k$。$h=\|\,|J|^T (d_{ij}) |J|\,\|_\infty$（矩阵绝对行和范数）界 $\sup_{|v|_g=1}\|(\nabla^g dF-T)(v,v)\|$。若 $t$ 界同一单位球上 $\|T(v,v)\|$，且 $k$ 界 $|N_\beta\cdot T(v,v)|$，则实际两主曲率满足

$$
 \|S_F\|_{G,\mathrm{op}}\le (k+nt+h)/(1-e)^2 .
$$

因为 $N_F\cdot\nabla^g dF=II_F$，联络的切向项在法向投影中消失。也可用真实六 jet 直接验证 $MG\pm II_F\succeq0$。这里始终是**实际混合代表**的主曲率。

## 法球的近材料对和其余有序对

设某一实际 $G$ 单速测地线全长 $\ell$，其经过区域的实际主曲率绝对值 $\le M$。若 $M\ell\le\pi/2,\ M\tau\le1$，则其两端互过双向半径 $\tau$ 法球。证明令 $T=\gamma',\ d(t)=\gamma(t)-\gamma(0)$。有 $\|T'\|\le M$，从任意两时刻切向夹角至多 $M|t-u|$ 得

$$
 d(t)\cdot T(t)\ge\int_0^t\cos(M(t-u))\,du=\sin(Mt)/M,\qquad
 |N(0)\cdot T(t)|\le\sin(Mt).
$$

故 $|d(t)|^2\pm2\tau N(0)\cdot d(t)$ 的导数均非负，从零起算即得。反向同理。$M=0$ 时即直线。正长时 $d(t)\cdot T(t)>0$ 给点分离。必须有真正的短测地线及其全程曲率覆盖；闭壳上可先由可验证物质路径和 $G\le(1+e)^2g$ 界真内距，再对最短测地线支付。环境近邻不保证物质近邻。

其余点对可由全胞近似位置、定向单位法向和付费误差处理。设 $\bar d=\bar P(q)-\bar P(p)$，两位置误差和为 $b$，第一点法向误差为 $n_p$。一个有序法球的真实平方余量至少为

$$
 (\|\bar d\|-b)_+^2-2\tau
 (|\bar N_p\cdot\bar d|+b+n_p\|\bar d\|).
$$

交换 $p,q$ 再付一次。远对若已证 $\|\bar d\|-b\ge2\tau$ 则自动通过；异材料标签的点分离独立核对。要推出完整 reach，必须对闭合的嵌入曲面穷尽各片内与跨片有序对；源径、物理帽和所有相位的直径、宏观握持/移动量也各有自己的门。

[有向舍入消费者](../scripts/r756_two_boundary_curl_transfer.py) 逐角、逐径接受原 $g$、两条 ray、相向的 $K,K_s$ 积分胞界、真实帽迹与代表的六项误差。另有近材料测地对与远方有序对的条件入口。当前没有供其消费的全域输入证据，也未将已付的有限 R750 网格计作连续证书。

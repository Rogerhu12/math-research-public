# R266　准确极坐标连接的原度量下界与必要的侧向半径总变差

[R265](R265-accurate-weighted-polar-connector-global-embedding.md) 的准确原加权位置相对于原 $g$ 的连续误差严格大于 $.93572118$。即使重新选择时钟、任意单调高度和径向目标，只要保留该真实射线的原半径与两端高度，仍有误差严格大于 $.43150655$。维持原材料长度并要求误差 $B=2\,10^{-9}$ 时，该射线的径向总变差至少须增加 $.19574768$。对象是明确的原极坐标几何与所述保留条件；允许改变物理半径、标签的径向坐标或者高度单调性时须按新场计算。

## 实际材料切向与严格单点

对 R246 的 $X(s,u)=Y(s,\Theta(s,u))$，$Y=\rho e_r+z e_z$，R265 已付全域 $\Theta_u>0$。在固定极角 $\theta_*$ 的物理射线上，材料提升及其切向为
$$
u(s)=\Theta(s,\cdot)^{-1}(\theta_*),\qquad
w=\partial_s-\frac{\Theta_s}{\Theta_u}\partial_u.
$$
于是 $dX(w)=\rho_se_r+z_se_z$。任意正径向半径 $a_*(s)$ 的目标 $g=ds^2+a_*^2du^2$ 满足 $g(w,w)=1+a_*^2(\Theta_s/\Theta_u)^2\ge1$。若 $\delta=\sup\|g^{-1/2}(X^*e-g)g^{-1/2}\|_{op}$，Rayleigh 商给
$$
\delta\ge1-\frac{|dX(w)|^2}{g(w,w)}\ge1-(\rho_s^2+z_s^2).
$$

本次射线取 R265 准确 Γ95 入口原生傅里叶角 $\eta=\pi/2$ 所输送到 $\sigma=.02$ 真端口的平面极角。所有谐波在该点的正余弦是准确整数。右端在同一极角，从 R205 的投影收缩 $\rho_R\le r$ 得
$|\cos u_R|=(\rho_R/r)|\cos\theta_*|\le|\cos\theta_*|$；
反射给对应右端所有所需高度/半径端迹。没有假设准确左端落在浮点的对称轴上。

在 $t=51/64$、$s=b_d+tL\simeq .8156151788040041$，实际区间为
$$
.0028438<\rho_s<.0088976,\qquad
.2384858<z_s<.2533765,\qquad |dX(w)|^2<.06427882.
$$
此处的 $\rho_s$ 按本射线对数半径的六个真实 quintic 控制计算；$z_s$ 保留全部 28 个权、同一正归一化分母、$\sin^8\theta_*$ 凸混合和全部四个端控制。log 用 $2\operatorname{atanh}((r-1)/(r+1))$ 含几何尾界，exp 用实际最大参数为 3 的 48 次 Taylor 及 $e^3<27$ 余项。选择有理见证后，正确性只来自该见证的外包。对于 $X+W$，若还用同一个材料 $w$ 及 $g_{ss}=1,g_{su}=0$，误差不超过 $B$ 要求 $|d(X+W)(w)|\ge\sqrt{1-B}$；三角不等式给
$$
|dW(w)|>.74646733 .
$$

## 整射线覆盖所有正高度重分配

保留原 $\rho$、两端 $z_0,z_1$，高度在该固定极角关于 $s$ 单调，材料时钟可以任意保向。整射线长满足
$$
\ell=\int_b^S\sqrt{\rho_s^2+z_s^2}\,ds
\le \operatorname{TV}_{[b,S]}\rho+(z_1-z_0).
$$
以 256 个闭二进子区间对原 quintic $Q=\log\rho$ 及四次 $Q_s$ 作 de Casteljau 分割。每格以控制凸包给 $\int|\rho_s|\le |I|\exp(\max Q)\max|Q_s|$，全覆盖相加。准确得到
$$
\operatorname{TV}\rho<.452668262,\qquad z_1-z_0<.147258000,
\qquad \ell<.599926260.
$$
若 $\delta<1$，每个点有 $|dX(w)|\ge\sqrt{(1-\delta)g(w,w)}\ge\sqrt{1-\delta}$，故 $\ell\ge L\sqrt{1-\delta}$；$\delta\ge1$ 时以下下界直接成立。用 $L$ 的有理下端与 $\ell$ 的有理上端合成，得到
$$
\delta\ge 1-\ell^2/L^2>.43150655.
$$
这允许所有次数、所有正控制分配和其他单调高度。若释放 $\rho$，保持全材料长度和该极角的两端高度并要求 $\delta\le B$，则
$$
\operatorname{TV}\rho_{\rm new}\ge L\sqrt{1-B}-(z_1-z_0)
>\operatorname{TV}\rho_{\rm old}+.19574768 .
$$
R247 的一般点控制预算与 R255 的一般径向目标下界分别处理不同自由度。本条付的是 R265 的真端口、真权重和整条侧射线。已改变几何的强后缀数值态须用自己的 $dX$ 及总变差。

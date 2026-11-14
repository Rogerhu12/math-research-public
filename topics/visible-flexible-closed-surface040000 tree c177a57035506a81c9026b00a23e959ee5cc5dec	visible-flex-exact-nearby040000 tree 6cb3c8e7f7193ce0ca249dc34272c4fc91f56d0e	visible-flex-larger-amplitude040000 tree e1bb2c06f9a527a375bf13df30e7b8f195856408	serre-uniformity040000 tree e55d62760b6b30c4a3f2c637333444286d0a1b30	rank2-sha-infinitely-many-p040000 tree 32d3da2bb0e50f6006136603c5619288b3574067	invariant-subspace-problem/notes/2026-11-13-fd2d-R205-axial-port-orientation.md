# R202 在 R205 弯环的长轴经线上仍然适用

本说明是 [R202](../results/R202-d2-axial-meridian-length-necessary-condition.md) 与 [R205](../results/R205-complete-bent-annulus-cut-lifting-and-fixed-collar.md) 的直接消费。它区分中央椭圆的两个轴，保留 R202 的适用条件；不把一个必要条件当成曲面的存在证明，也不排除 R201 的非反射表示。

## 1. 准确方向：被弯曲的是短轴端口

记中央椭圆的准确半轴为 $A_q>B_q$，中央柱长为 $c$，外切口半径为 $a_c=4/5$，弯环幅度为 $\alpha\in[0,6/5]$。当前 R187/R205 材料角的准确端点是

$$
\Gamma(0)=(A_q,0,0),\qquad
\Gamma(\pi/2)=(0,B_q,0).
$$

弯环定义为

$$
F_\alpha(r,u)=
\bigl(r\cos u,\ C_\alpha(r\sin u),\
Z_c-H_\alpha(r\sin u)\bigr),
$$

其中 $C_\alpha'(y)=\cos\beta_\alpha(y)$、$H_\alpha'(y)=\sin\beta_\alpha(y)$，两原函数在 $y=0$ 都取零，且 $\beta_\alpha(y)=0$ 于 $|y|\le17/50$。因而对所有合法 $\alpha$，

$$
F_\alpha(a_c,0)=(a_c,0,Z_c),\qquad
\partial_sF_\alpha(a_c,0)=(-1,0,0).
\tag{1}
$$

这里 $s$ 从中央向外切口增加，切口处 $r_s=-1$。式 (1) 是定义恒等式，不是从浮点角采样推出的零。

在另一条轴上，利用 $\beta_\alpha(a_c)=\alpha$，

$$
F_\alpha(a_c,\pi/2)
=(0,C_\alpha(a_c),Z_c-H_\alpha(a_c)),\qquad
\partial_sF_\alpha(a_c,\pi/2)
=(0,-\cos\alpha,\sin\alpha).
\tag{2}
$$

因此增加弯环幅度改变的是短轴方向的外切口位置和切向。把式 (2) 的中央起点误写为 $A_q$ 会混淆两个轴；其中央起点是 $B_q$。当前固定帽握持测试中的点 $(0,A_q,0)$ 是用于另一相位的几何见证点，并不是本相位的中央短轴端点。

## 2. 长轴必要条件完整保留

设完整前缀为 $C^2$ 正则浸入，保留 R205 的两反射对称。取 $u=0$ 的长轴经线，从准确中央柱末端 $s=c$ 到外切口 $s=S$。它位于 $xz$ 平面，切向量 $\partial_uX$ 垂直该平面，而 $\partial_sX$ 位于该平面。于是曲面法向位于该平面；这条正则平面曲线的曲率向量是曲面法向方向。因此它是曲面测地线，且其空间曲率不超过曲面的主曲率绝对值上界 $C$。

中央柱给出起点 $(A_q,0,c)$ 和单位切向 $e_z$，式 (1) 给出终点 $(a_c,0,Z_c)$ 和单位切向 $-e_x$。若完整准确目标度量为 $ds^2+a(s)^2du^2$，该经线长度为 $S-c$。若仅有全域相对度量误差上界 $\varepsilon$，则长度至多

$$
(S-c)\sqrt{1+\varepsilon}.
\tag{3}
$$

令 $r=1/C$。R202 的校准因此仍然给出

$$
\frac{\pi r}{2}
+\sqrt{(A_q-a_c-r)^2+(Z_c-c-r)^2}
\ \le\ (S-c)\sqrt{1+\varepsilon}.
\tag{4}
$$

式 (4) 的所有量都与弯环幅度 $\alpha$ 无关。尾部整体具有更大的非零起伏，不会改变这条长轴上的切口位置和切向。改变 $Z_c$、准确前缀长度、中央半轴或实际曲率预算，才会改变式 (4) 的输入。

为避免单调转角假设，现重述校准。以单位弧长参数表示平面切向

$$
T=(-\sin\theta,\cos\theta),
$$

起点 $\theta=0$，终点 $\theta=\pi/2+2\pi k$。任取单位向量 $v$，令 $w(\theta)=1-v\cdot(\sin\theta,\cos\theta)\ge0$。由 $|\theta'|\le C$，

$$
L-v\cdot(D_x,D_z)
=\int w(\theta)\,d\ell
\ge r\int w(\theta)|d\theta|.
$$

一整周的 $w$ 积分为 $2\pi$。短端弧的积分
$q=\pi/2-v\cdot(1,1)$ 满足
$0\le q\le\pi/2+\sqrt2<\pi$。
故不论反向转动或绕圈，$\int w|d\theta|\ge\min_{k\in\mathbb Z}|q+2\pi k|=q$。
从而

$$
L\ge r\pi/2+v\cdot(D_x-r,D_z-r).
$$

对 $v$ 取上确界得到 (4)。这不要求转角沿经线单调，也不把采样曲率上界当成准确 $C$。

## 3. 短轴的相应式及其范围

同样校准可用于式 (2)。令 $\theta_f=\pi/2-\alpha$。本域内 $0<\theta_f\le\pi/2$，且
$q=\theta_f-v\cdot(1-\cos\theta_f,\sin\theta_f)$ 满足
$0\le q\le\theta_f+2\sin(\theta_f/2)<\pi$。
上述绕圈论证逐字成立，得到

$$
r\theta_f+
\sqrt{
 [B_q-C_\alpha(a_c)-r(1-\cos\theta_f)]^2+
 [Z_c-H_\alpha(a_c)-c-r\sin\theta_f]^2
}
\le (S-c)\sqrt{1+\varepsilon}.
\tag{5}
$$

此式允许第一位移 $B_q-C_\alpha(a_c)$ 为负，不假定短轴经线的径向位置单调。式 (5) 中的 $B_q$ 不能替换成 $A_q$。它通常比式 (4) 宽松；这仍只是必要条件。

## 4. 本次实际有限消费

输入是已经公开保存的固定幅度 $\alpha=1/4$、第 8 个接受步：

- [完整状态](2026-11-13-fd2d-R205-fixed-A025-geometry-eight-accepted-04.json)，SHA256 为 `f95abce8124c3b5a85da839a0e6d4370ffcdfa40e13011d9d5e0d1408d940bc6`。
- [只读小消费者](../scripts/fd2d-R205-axial-port-orientation-check.cjs) 调用冻结 R205 完整位置与端口，未运行 whole F、J、body 或求解器。
- [真实报告](2026-11-13-fd2d-R205-axial-port-orientation-01.json) 保存全部实际端点、切向与参数来源。

有限计算使用 $A_q\approx1.3620341722637315$、$B_q\approx0.5620341722637314$、$c=13/128$、$S\approx0.8856739498716915$、$Z_c\approx0.5680962429930927$、假设曲率预算 $C=9.5$。其可用长度约 $0.7841114498716915$；长轴下界约 $0.7477181651423608$，有限差约 $0.03639328472933068$。对 $\alpha=0,1/4,1,6/5$，长轴数值相同，短轴下界分别约

$$
0.6636667308,\quad0.5765589551,\quad
0.3252231832,\quad0.2715868577.
$$

把同一有限输入的 $Z_c$ 改成 $0.625$，长轴下界约 $0.7846284525$，高于该有限长度。严格排除须使用 R202 已付的准确有理域，不能仅依赖这里的浮点差。反之，当前有限高度下有正裕量，也不证明存在解。实际第 8 步的采样曲率约 $12.43$、最大度量残差约 $0.409$，显然不能把这里假设的 $C=9.5$ 和小 $\varepsilon$ 当成该场已经满足的界。

## 5. 不延用到一般 R201 场

R201 的完整半周期表示允许破坏上述两镜面对称。中央与切口端点仍可固定，但中间材料经线不必在同一平面，亦不必是曲面测地线。因此仅凭曲面主曲率上界，不能给该空间曲线相同的总曲率上界。式 (4) 的这份证明不能移植为 R201 全空间的障碍。破对称新初始方向仍需完整位置、度量、曲率和固定帽几何验证。

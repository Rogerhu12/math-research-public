# R259　准确完整前缀的双侧法球与非局部 reach

**已证明。** 令 $S$ 为 [R233](R233-entire-ramp-accurate-coast-normalization.md) 准确积分归一化的全部 16 格 ramp、[R232](R232-new-gap-complete-accurate-terminal-port-bounds.md) 同一准确出口的真实 coast、中央椭圆柱及下半反射合成的完整闭环带，包括两条边界圈。作为 $\mathbb R^3$ 的紧子集，
$$
\operatorname{reach}(S)\ \ge\ 1/K=1/9.867915>.1013>.097.
$$
此外，任意 $p,q\in S$ 和 $p$ 处任一单位曲面法向 $n$ 均满足 $2|n\cdot(q-p)|\le K|q-p|^2$。这个双侧界覆盖同半段、跨中央、两侧互相以及边缘所有有序点对。给此环带接新后段或帽时，含新点的点对须另外支付。以下采用 [R257](R257-accurate-whole-prefix-global-embedding.md) 已证的嵌入与整圈高度，并保留 R233 的准确 $C^2$ 端口及已经证明的非零度量误差。

## 1. 末圈高度同时约束整条材料经线

写中央母椭圆为 $p(\theta)=(A\cos\theta,B\sin\theta)$，其速度为 $e(\theta)=\sqrt{A^2\sin^2\theta+B^2\cos^2\theta}$，平均速度为 $a_\ell$。材料角 $u=a_\ell^{-1}\int_0^\theta e(t)dt$。令 $X(s,u)=(x,z)$，上下采用同一有符号材料坐标 $-b\le s\le b$，中央柱为 $(p(\theta),s)$。取 $\epsilon=6.100\cdot10^{-7}$。R233 给实际 ramp 的 $1-\epsilon\le|X_s|^2\le1+\epsilon$，R232 给 coast 的 $|X_s|=1$。上半中央端口 $s=c$ 到 $b$ 的经线弧长至多 $h=r(1+\epsilon/2)+l$。R257 对每个材料角给末端 $z(b,u)-c>.07874442$。故整段非负积分
$$
\int_c^b(|X_s|-z_s)\,ds\le h-\min_u(z(b,u)-c)=:d<.001256 .
$$
右式可取经认证的末圈高度下界代替真实最小值。任一子段 $[c,s]$ 的同一积分也至多 $d$。而 $\left|\int_c^s(|X_s|-1)ds\right|\le\epsilon r$，故 $|z-s|<.00126$。由 $|x_s|^2=(|X_s|-z_s)(|X_s|+z_s)$ 与 Cauchy–Schwarz，
$$
|x-p(\theta)|\le\int_c^s|x_s|\,ds\le\sqrt{2hd}<.0142 .
$$
中央柱准确成立，反射保范数，故全带上 $|X(s,u)-(p(\theta(u)),s)|<.0143$。

## 2. 小空间弦的内在最短路

任取 $P=X(s,u),Q=X(t,v)$，且 $|P-Q|\le2/K<.203$。令 $d_e$ 为相应中央椭圆两点的平面弦长。由上节 $d_e\le.203+2(.0142)=.2314$。两 native 角用较短的参数弧表示为 $m-h_0,m+h_0$，$0\le h_0\le\pi/2$。此处选取的是一条可用的弧，毋须先证明它是最短弧。椭圆恒等式 $d_e=2\sin(h_0)e(m)$，以及 $e(m)\ge B$ 和 $\sin(.294)\ge.294-.294^3/6$，给出 $h_0<.294$。直接微分有
$$
e''(\theta)=\frac{(A^2-B^2)\cos(2\theta)}{e(\theta)}
-\frac{(A^2-B^2)^2\sin^2\theta\cos^2\theta}{e(\theta)^3}\le M:=(A^2-B^2)/B .
$$
因此该弧的长度 $L_e\le2h_0e(m)+Mh_0^3/3$。结合 $\sin h_0\ge h_0(1-h_0^2/6)$，得到 $L_e\le C_e d_e$，其中
$$
C_e=\frac{1+M(.294)^2/(6B)}{1-(.294)^2/6}<1.195 .
$$
$h_0=0$ 时弧长与弦长同为零。

在展开角上取以上材料弧对应的 lift，$a_\ell|u-v|=L_e$。连接两材料点的坐标直线完全留在 $[-b,b]$。准确目标 $g=ds^2+f(s)^2du^2$，ramp 的 $f'=v_0 S_9$、coast 的 $f'=v_0$（外向坐标，$v_0$ 为 master 中速度）。故 $f/a_\ell\le W:=1+v_0(r/2+l)/B<1.006$。R233 在 ramp 上的完整相对谱界、其余段的准确等距共同给出实际路径长度上界
$$
\sqrt{1+\epsilon}\sqrt{(s-t)^2+(W L_e)^2}
\le (1+\epsilon/2)W C_e\sqrt{(s-t)^2+d_e^2}
\le (1+\epsilon/2)W C_e(|P-Q|+2\cdot.0143)<.279<\pi/K .
$$
上式使用准确中央 $a_\ell$，并保留实际 $\epsilon$。两点在同一侧或异侧都适用。

紧致连通光滑环带的内在长度度量实现最短路。其两个真边界各有光滑的准确 coast 邻域，度量是 $dw^2+f(w)^2du^2$，其中 $w$ 向对应的带外增加，$f'=v_0>0$。在开放小 collar 中延伸此度量。取任一边界点的充分小凸正规邻域，任意两域内邻点的延伸度量短测地线满足 $w''=ff'(u')^2\ge0$，其 $w$ 的最大值在端点取到。因此这条局部短测地线全在原域中，原内在极短路在该邻域必须与它一致。内部更是通常的测地线。于是极短路作为空间单位速曲线满足 $|\gamma''|=|\mathrm{II}(\dot\gamma,\dot\gamma)|\le K$，两端按单侧理解。中央曲率 $A/B^2<K$，准确 coast 曲率 $<8.892834503<K$，ramp 用 R233 全部 16 格的 $K$。两条真正拼缝空间两 jet 连续，穿缝没有角点；该论证不需要把 R233 的 ramp 度量当成准确等距。

## 3. 曲率受限短弧的双侧球

对任意单位速空间弧 $\gamma:[0,L]\to\mathbb R^3$，设 $|T'|\le K$、$0<L<\pi/K$、$T=\gamma'$、$h_1=KL/2$。弧中点切向与 $T(t)$ 的夹角至多 $K|t-L/2|$。积分沿中点切向的投影，得到 $C=\gamma(L)-\gamma(0)$ 满足
$$
|C|\ge 2\sin(h_1)/K .
$$
又 $\angle(C,T(0))\le h_1$。为证后式，任取与 $T(0)$ 成 $\pi/2+h_1$ 角的单位向量 $m$。球面路长界给 $\angle(m,T(t))\ge\pi/2+h_1-Kt$，右侧在 $(0,\pi)$，故 $m\cdot T(t)\le\sin(Kt-h_1)$。全程积分恰为零上界，即 $m\cdot C\le0$。这些半空间的交是绕 $T(0)$ 的半角 $h_1$ 圆锥。

若单位向量 $a$ 满足 $a\cdot T(0)\le0$，所得弦角界给 $a\cdot C\le|C|\sin h_1\le K|C|^2/2$。取上节的真极短路即涵盖所有 $0<|P-Q|\le2/K$；$|P-Q|>2/K$ 时由 $a\cdot C\le|C|$ 已得同式。取 $a=\pm n_P$ 即为全部有序双侧法球不等式，故对于 $|\tau|<1/K$，$P+\tau n_P$ 到 $S$ 的唯一最近点是 $P$。

最后须包括边界的外共法向。若有空间点 $Y$ 距 $S$ 为 $0<r_*<1/K$ 且有两个不同最近点 $P,Q$，则 $|Q-P|\le2r_*<2/K$。取从 $P$ 出发通向 $Q$ 的上述极短路，令 $a=(Y-P)/r_*$。即使 $P$ 在边界，距离平方沿这条允许的单侧路径在起点取最小值，仍有 $a\cdot T(0)\le0$。但等距给
$$
|Q-P|^2=2r_*a\cdot(Q-P)\le r_*K|Q-P|^2<|Q-P|^2,
$$
矛盾。紧致性给所有外点存在最近点。这就按闭子集的定义证明所述 reach。相位作用若在本前缀上由空间刚体运动及材料重参数化实现，则同一结论在其全部相位成立。

[准确分数与可重生命令](../notes/2026-11-28-2ecf-accurate-prefix-secant-reach-budget.md)

# 精确桥根与已认证前缀 metric 的转移预算

2026-11-09，root / Astra-visible-flex-db6f0b0e。完整条件证明及有理程序，待独审。解决冻结浮点桥参数与共同精确旋转 metric 之间的一个定义缺口；不解决公共 Cartesian 两阶接缝、尾方程或完整闭解。

## 1. 精确目标桥

令 $c$ 为固定 `rCut` 的精确二进有理数，$w=1/2$。在当前 cut-preserving 尾的外端，精确物理背景应满足
$$
r=c,\qquad w_r=-7w/c.
\tag{1}
$$
这里前缀向内走，取 $\sigma=-1$。设
$$
E=1+w^2,\quad p_t=\arctan(1/w),\quad
p_s=-\sigma w_r/E^{3/2}=w_r/E^{3/2}.
$$
对 $L>0$ 定义
$$
\phi_L(t)=p_t(3t^2-2t^3)+Lp_s(t^3-t^2),
\quad f(L)=L\int_0^1\sin\phi_L(t)dt-(1-c).
$$
在指定小区间内取 $f(L)=0$ 的唯一根 $L_*$. 桥为
$$
a_*(u)=1-\int_0^u\sin\phi_{L_*}(v/L_*)dv,
\quad 0\le u\le L_*.
$$
起端 $a=1,a'=a''=0$，与 flat prefix 匹配。末端
$$
a=c,\quad a'=-1/\sqrt E,\quad a''=-ww_r/E^2.
$$
这些恰为同一尾用向内经线弧长参数表示的径向两阶导数。因此 (1) 及尾的正精确径向归一成立时，此桥支付旋转目标 metric 的精确接口。

(1) 的来源须保持明确：外端原始 flat profile 有 $w\propto r_o^{-7}$；cut-preserving 覆盖在最后端完全恢复该 profile，权重端值为一，径向混合 $\chi=0$、$j_0=c/r_{o,cut}$。故 $dr/dx=|r_o'|c/r_{o,cut}$，得到 $w_r=-7w/c$。正的全局归一常数用真积分将外端送到 c；不能仅从浮点程序的 `cutRadiusError` 很小推断这一恒等式。精确背景归一另证。

## 2. 完全有理的根证书

`db6f-root-exact-bridge.py` 的根初猜仅用标准库 Decimal；它不进入证明。真正证据如下。

1. 用交错 atan 有理级数包围 $\arctan(1/5),\arctan(1/239),\arctan(1/2)$，再由 Machin 恒等式得到 $\pi$、$p_t$ 的区间。用整数平方根包围 $\sqrt E$，得到 $p_s$。区间统一向外取到二进格点。
2. 取两个相隔 $2\cdot10^{-40}$ 的有理 L 端点。相位为三次多项式，用32个有理子区间的 Bernstein 凸包证明 $0\le\phi<\pi/2$（t>0 时严格为正）。
3. 写 $\phi=A t^2+B t^3$。每个奇次幂的积分严格等于
   $$
   \int_0^1\phi^kdt=\sum_{j=0}^k\binom kj\frac{A^{k-j}B^j}{2k+j+1}.
   $$
   将 sin 的53阶 Taylor 多项式逐项精确有理积分，并加 $2^{54}/54!$ 的一致余项。所有乘加、除法、幂及最终符号检查均使用 Fraction 区间。
4. 左端 f 的整个区间为负，右端整个区间为正。连续性给根存在。由于 $p_s<0$、$t^3-t^2\le0$ 及 $\cos\phi>0$，
   $$
   f'(L)=\int\sin\phi+L\int\cos\phi\,p_s(t^3-t^2)>1/8.
   $$
   最后一界由 $t\in[1/2,1]$ 时 $\phi\ge p_t/2>1/2$，以及 $\sin\phi\ge2\phi/\pi>1/4$ 得到。于是根在所述区间内唯一。

报告保存了可直接检查符号的有理端点、相位界和参数区间；显示用的浮点数不作为证明数据。

## 3. 与已经认证的冻结桥比较

已有前缀证书的目标 $a_0$ 使用冻结的 binary $L_0,p_{t,0},p_{s,0}$ 和真 sin 积分。两者用同一精确 flat prefix；记其精确终点为 $s_p$。有限图的参数终点为保存的 $S_0$，新目标终点为 $S_*=s_p+L_*$。

为将有限图的整个域与精确目标对应，取一个常数伸缩
$$
u=\lambda s,\quad \lambda=S_0/S_*,\quad 0\le s\le S_*.
$$
先将原有限图变换到它的物理材料角 $\theta$，再作这个径向伸缩。原来的辅助角 e 仍按 u 求反函数，不把数值角直接当作材料角。

设 $d_L,d_t,d_s$ 是精确参数与冻结参数的绝对差上界，$d_S=|S_*-S_0|$。在输入核查的参数盒
$$
L\in[.6,.7],\quad p_t\in[1,1.2],\quad p_s\in[-5,0],
\quad 0\le v\le.7
$$
中，固定 v 的桥相位对三参数的偏导绝对值依次不超过 64、8、3。验证可直接代入 $t=v/L\le7/6<1.2$：
$$
\partial_{p_t}\phi=3t^2-2t^3,\quad
\partial_{p_s}\phi=L(t^3-t^2),
$$
$$
\partial_L\phi=-p_t(6t^2-6t^3)/L+p_s(t^2-2t^3).
$$
用三角不等式即分别小于8、3、64。$|\sin'|\le1$，积分长度小于一；此外 $a_0$ 在整个必要延伸域速度不超过一。因此
$$
|a_0(\lambda s)-a_*(s)|\le d_a:=d_S+64d_L+8d_t+3d_s.
$$
若 s 在 flat 部分，两个未伸缩的半径本来相同；跨过 piece 接点时仍由共同的全局 Lipschitz 界处理。新目标半径始终大于 $.59$。

将已认证的目标拉回后为
$$
\bar g=\lambda^2ds^2+a_0(\lambda s)^2d\theta^2,
\qquad g_*=ds^2+a_*(s)^2d\theta^2.
$$
所以
$$
\|g_*^{-1/2}(\bar g-g_*)g_*^{-1/2}\|_{op}
\le\eta:=\max\{|\lambda^2-1|,\ 2d_a/.59+(d_a/.59)^2\}.
$$
若原有限图的相对误差为 $\epsilon_0$，新图相对 $g_*$ 的误差不超过
$$
\boxed{\epsilon_*\le\epsilon_0(1+\eta)+\eta.}
$$
这是两个对称形式的直接范数比较，不把端点错配当成精确相等。

## 4. 当前真实宏观输入的结果与范围

报告 `2026-11-09-db6f-root-exact-bridge.json` 绑定原图、v2目标、metric证书及尾参数清单的哈希。当前核得
$$
d_a<9.7920\cdot10^{-14},\qquad \eta<3.3194\cdot10^{-13},
$$
$$
\epsilon_*\le3.622553187875372\cdot10^{-7}.
$$
这表示可以把已认证的真实宏观有限前缀解释为同一个精确匹配旋转目标的近似，而无需修改物理 profile 或用固定 taper 掩盖桥缺陷。只是参数域有明确的极微小重新参数化。

仍然需要：尾的正精确归一与共同背景定义、有限全尾对该背景的 metric 误差、前缀/尾的精确 Cartesian 共享两阶 jet、固定 g 收敛、完整闭嵌入与其余 README 指标。尤其本证书不证明非线性无限尾已经存在。

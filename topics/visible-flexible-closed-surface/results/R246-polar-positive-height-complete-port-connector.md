# R246：完整二阶端口的极坐标正高度连接及定量非退化条件

日期：2026-11-26。状态：**有条件的准确构造定理**；另含本题 R205 真 cut 的一个已支付全角解析推论。它不声称当前数值输入已满足全部连续假设，不声称等距、全闭嵌入或全闭 reach。

本定理把 [R233](R233-entire-ramp-accurate-coast-normalization.md) 后的完整端口连接问题落实为明确位置场。实现和真实失败基线见 [极坐标完整基线记录](../notes/2026-11-26-6a65-geometry-nonfold-polar-complete-baseline.md)。R233 的准确末端与 literal 数值端口仍须分别识别；本定理本身对所输入的准确端口函数成立。

## 1. 数据、正则性与条件

令 $I=[b,S]$、$L=S-b>0$、$u\in\mathbb R/(2\pi\mathbb Z)$。在两端 $s_0=b,s_1=S$ 给定周期函数

$$
P_i(u)\in C^4,\qquad V_i(u)\in C^3,\qquad A_i(u)\in C^2,
\qquad i=0,1,
$$

作为 $X,X_s,X_{ss}$ 的完整端迹。其角导数使用这些函数本身的导数；不是分别指定的互不兼容数据。若需与已有邻片相接，假定这些就是邻片的实际端迹。

记 $p_i=(P_{i,x},P_{i,y})$。假定 $p_i\ne0$，且存在连续 lift

$$
\phi_i(u)=\arg(P_{i,x}+{\rm i}P_{i,y}),\qquad
\phi_i(u+2\pi)=\phi_i(u)+2\pi,\qquad \phi_{i,u}>0.
$$

每个端口的平面投影因而是相对原点的单值正半径极坐标图。后文所有端迹取其准确函数值，不使用有限采样替代这些全角假设。

给定任意独立的正目标半径 $a_*(s)>0$，它不随以下位置构造更改。最终度量仍是

$$
g=ds^2+a_*(s)^2du^2.
$$

## 2. 固定材料角到固定平面极角的完整变换

以下公式在每个端口固定材料角 $u$ 求导，最后通过 $u=\phi_i^{-1}(\theta)$ 视作周期 $\theta$ 函数。暂省端标 $i$，令 $p=(P_x,P_y)$、$v=(V_x,V_y)$、$a=(A_x,A_y)$，$[x,y]=x_1y_2-x_2y_1$、$r=|p|$。先定义

$$
\phi_u=\frac{[p,p_u]}{r^2},\qquad
\phi_s=\frac{[p,v]}{r^2},
$$

$$
\phi_{ss}=\frac{[p,a]}{r^2}
-\frac{2p\cdot v}{r^2}\phi_s,
$$

$$
\phi_{su}=\frac{[p_u,v]+[p,v_u]}{r^2}
-\frac{2p\cdot p_u}{r^2}\phi_s,\qquad
\phi_{uu}=\frac{[p,p_{uu}]}{r^2}
-\frac{2p\cdot p_u}{r^2}\phi_u.
$$

这些是端口位置 $P+(s-s_i)V+(s-s_i)^2A/2$ 的平面极角二阶 jet，所以无须假设一个尚未解出的邻域等距场。

固定 $\theta$ 的材料角导数由隐函数链式法则确定：

$$
w=u_s=-\frac{\phi_s}{\phi_u},\qquad
w_2=u_{ss}
=-\frac{\phi_{ss}+2\phi_{su}w+\phi_{uu}w^2}{\phi_u}.
$$

固定 $u$ 的半径导数为

$$
r_s=\frac{p\cdot v}{r},\qquad r_u=\frac{p\cdot p_u}{r},
$$

$$
r_{ss}=\frac{|v|^2+p\cdot a-r_s^2}{r},\quad
r_{su}=\frac{p_u\cdot v+p\cdot v_u-r_s r_u}{r},\quad
r_{uu}=\frac{|p_u|^2+p\cdot p_{uu}-r_u^2}{r}.
$$

故固定 $\theta$ 的端半径二阶 jet 是

$$
\rho_i=r,\qquad
\dot\rho_i=r_s+r_u w,\qquad
\ddot\rho_i=r_{ss}+2r_{su}w+r_{uu}w^2+r_u w_2.
$$

高度的对应 jet 是

$$
z_i=P_z,\quad
\dot z_i=V_z+P_{u,z}w,\quad
\ddot z_i=A_z+2V_{u,z}w+P_{uu,z}w^2+P_{u,z}w_2.
$$

点号仅表示这些固定 $\theta$ 的物理 $s$ 导数。需要它们的 $\theta$ 导数时，若 $h=h(u)$，使用

$$
h_\theta=\frac{h_u}{\phi_u},\qquad
h_{\theta\theta}=\frac{h_{uu}}{\phi_u^2}
-\frac{h_u\phi_{uu}}{\phi_u^3}.
$$

上述正则性恰能支付二阶位置构造：涉及的最高端口角导数是 $P_{uuuu}$、$V_{uuu}$、$A_{uu}$。

## 3. 完整物理时钟与对数半径

令 $\Theta(s,u)$ 为关于 $s$ 的唯一 degree-at-most-five Hermite 多项式，满足

$$
(\Theta,\Theta_s,\Theta_{ss})(s_i,u)
=(\phi_i,\phi_{i,s},\phi_{i,ss})(u).
$$

因为角 lift 增加 $2\pi$、其径向导数周期，且左右值 Hermite 基函数之和为 $1$，

$$
\Theta(s,u+2\pi)=\Theta(s,u)+2\pi.
$$

$t=(s-b)/L$ 下，$\Theta_u$ 的六个 degree-five Bernstein 控制函数恰为

$$
\begin{aligned}
d_0&=\phi_{0,u},\\
d_1&=\phi_{0,u}+\frac L5\phi_{0,su},\\
d_2&=\phi_{0,u}+\frac{2L}5\phi_{0,su}
+\frac{L^2}{20}\phi_{0,ssu},\\
d_3&=\phi_{1,u}-\frac{2L}5\phi_{1,su}
+\frac{L^2}{20}\phi_{1,ssu},\\
d_4&=\phi_{1,u}-\frac L5\phi_{1,su},\\
d_5&=\phi_{1,u}.
\end{aligned}
$$

假定所有 $d_j(u)>0$。则 Bernstein 凸组合给出全域 $\Theta_u>0$；对每个 $s$，$\Theta$ 是圆周 degree-one 微分同胚。若已付统一下界 $d_j\ge d_*>0$，则 $\Theta_u\ge d_*$。

定义 $Q(s,\theta)$ 为端迹

$$
Q_i=\log\rho_i,\quad
\dot Q_i=\frac{\dot\rho_i}{\rho_i},\quad
\ddot Q_i=\frac{\ddot\rho_i}{\rho_i}
-\left(\frac{\dot\rho_i}{\rho_i}\right)^2
$$

的完整径向 quintic Hermite 插值，并令 $\rho=e^Q$。它全域严格为正，且准确恢复端口 $\rho_i,\dot\rho_i,\ddot\rho_i$。这是位置插值，不是目标半径 $a_*$ 的新定义。

## 4. 正高度速度及准确积分约束

取整数 $N\ge4$。在固定 $\theta$ 下置 $\Delta z=z_1-z_0$，并定义

$$
b_0=\dot z_0,\qquad
b_1=\dot z_0+\frac L N\ddot z_0,\qquad
b_{N-1}=\dot z_1-\frac L N\ddot z_1,\qquad
b_N=\dot z_1.
$$

令

$$
M(\theta)=\frac{N+1}{L}\Delta z-b_0-b_1-b_{N-1}-b_N.
$$

假定四个端控制非负，且 $M>0$。可选任意 $C^2$、严格正、周期的内部控制函数 $b_2,\ldots,b_{N-2}$，只要

$$
\sum_{j=2}^{N-2}b_j=M.
$$

例如 $b_j=M/(N-3)$。也可对任意正 $C^2$ 权 $w_j$ 取 $b_j=Mw_j/\sum w_k$；或将它与均匀分配作任何 $C^2$ 的 $[0,1]$ 凸混合。因此可以在不改变高度积分和端迹的条件下，把正速度移向已定位的径向转弯处。

令 $B_j^N(t)=\binom Nj t^j(1-t)^{N-j}$，定义

$$
v(s,\theta)=\sum_{j=0}^N b_j(\theta)B_j^N(t),
\qquad
z(s,\theta)=z_0(\theta)+L\int_0^t
\sum_{j=0}^N b_j(\theta)B_j^N(q)\,dq.
$$

由 $\int_0^1B_j^N=1/(N+1)$，准确得到 $z(S,\theta)=z_1(\theta)$。同时

$$
z_s(b)=b_0=\dot z_0,\quad z_s(S)=b_N=\dot z_1,
$$

$$
z_{ss}(b)=\frac NL(b_1-b_0)=\ddot z_0,\quad
z_{ss}(S)=\frac NL(b_N-b_{N-1})=\ddot z_1.
$$

对 $0<t<1$，每个 Bernstein 基函数严格为正；内部控制有正项，端控制非负，故全角内部 $z_s=v>0$。因此 $z$ 在固定 $\theta$ 下严格单调，且严格介于两个端高度之间。端点允许 $z_s=0$。

这些端迹都是关于 $\theta$ 的函数恒等式，因此它们的所有所需角导数也相符；无须另外拼接独立角 jets。

## 5. 六个位置 jets、准确 C2 接合和非折叠

定义

$$
Y(s,\theta)=\rho(s,\theta)e_r(\theta)+z(s,\theta)e_z,
\qquad
X(s,u)=Y(s,\Theta(s,u)),
$$

其中 $e_r=(\cos\theta,\sin\theta,0)$、$e_\theta=(-\sin\theta,\cos\theta,0)$。

全部六个 jets 为

$$
X=Y,\qquad
X_s=Y_s+Y_\theta\Theta_s,\qquad
X_u=Y_\theta\Theta_u,
$$

$$
X_{ss}=Y_{ss}+2Y_{s\theta}\Theta_s
+Y_{\theta\theta}\Theta_s^2+Y_\theta\Theta_{ss},
$$

$$
X_{su}=Y_{s\theta}\Theta_u
+Y_{\theta\theta}\Theta_s\Theta_u+Y_\theta\Theta_{su},
$$

$$
X_{uu}=Y_{\theta\theta}\Theta_u^2+Y_\theta\Theta_{uu}.
$$

第 2 节就是端口极坐标变换的完整二阶逆链。第 3–4 节恢复固定 $\theta$ 的全部径向端迹，时钟同时恢复 $\phi_i,\phi_{i,s},\phi_{i,ss}$，故

$$
(X,X_s,X_{ss})(s_i,u)=(P_i,V_i,A_i)(u).
$$

再对 $u$ 求导，得到 $X_u=P_{i,u}$、$X_{su}=V_{i,u}$、$X_{uu}=P_{i,uu}$。因此与实际邻片在全角完整 C2 接合。

时钟径向导数在叉乘中消去：

$$
X_s\times X_u=\Theta_u(Y_s\times Y_\theta).
$$

利用

$$
Y_s=\rho_s e_r+z_s e_z,\qquad
Y_\theta=\rho_\theta e_r+\rho e_\theta+z_\theta e_z,
$$

可得准确恒等式

$$
\boxed{
|X_s\times X_u|^2=
\Theta_u^2\left[
\rho^2z_s^2+(z_s\rho_\theta-\rho_s z_\theta)^2+\rho^2\rho_s^2
\right].
}
$$

在内部，$\Theta_u,\rho,z_s$ 严格正，所以 $X$ 是浸入。边界另需实际给定端口满足 $V_i\times P_{i,u}\ne0$；该假设通过准确端迹恒等式保证边界浸入。不能从内部正性直接删除这个边界条件。

任意两个相同的像点有相同且非零的平面位置，所以其极角 $\theta$ 相同。固定该 $\theta$，$z(s,\theta)$ 严格随 $s$ 增加，故二者的 $s$ 相同；再由 $\Theta(s,\cdot)$ 是圆周微分同胚，材料角也相同。于是 $X$ 在整个闭环带 $[b,S]\times S^1$ 单射。紧性和 Hausdorff 性给出到像的同胚，结合内外边界浸入，得到 C2 自嵌入的连接环带。

此结论只排除连接环带自身的自交。与其他前缀、另一半核和帽的相交、非局部法割线以及定量 reach 必须另付。

## 6. 相对于原目标度量的面积与 Gram 下界

令 $\sigma=|X_s\times X_u|/a_*$。叉乘恒等式给出

$$
\boxed{\quad
\sigma\ge\frac{\Theta_u\rho}{a_*}
\sqrt{z_s^2+\rho_s^2}.
\quad}
$$

特别地，在任何已支付连续常数

$$
\Theta_u\ge d_*,\quad \rho\ge r_*,\quad
z_s^2+\rho_s^2\ge v_*^2,\quad a_*\le a^*
$$

的区域上，$\sigma\ge d_*r_*v_*/a^*>0$。内部仅有定性的 $z_s>0$ 不自动给出有用的数值下界；这正是实际初场仍可出现很大曲率的原因。

目标正交标架中的 Gram 矩阵为

$$
H=\begin{pmatrix}|X_s|^2&X_s\cdot X_u/a_*\\
X_s\cdot X_u/a_*&|X_u|^2/a_*^2\end{pmatrix},
\qquad
\det H=\sigma^2,\quad T=\operatorname{tr}H.
$$

因此

$$
\lambda_{\min}(H)=
\frac{2\sigma^2}{T+\sqrt{T^2-4\sigma^2}}
\ge\frac{\sigma^2}{T}.
$$

若另有 $T\le T^*$，则 $\lambda_{\min}(H)\ge d_*^2r_*^2v_*^2/((a^*)^2T^*)$。这些只是非退化界，完全没有推出 $H=I$；$E=1,F=0,G=a_*^2$ 仍是后续完整位置求解必须支付的方程。

## 7. 本题 R205 真 cut：一个已支付的全角高度端控制

本节只支付第 4 节的右端高度控制，不冒充其余左端或时钟假设已成立。

考虑半径 $r=4/5$ 的 R205 真 cut，转角幅度 $0<A\le7/8$，平区 $y\le17/50$。在 $y\ge0$ 写

$$
C(y)=\frac{17}{50}+\int_{17/50}^y\cos\alpha(t)\,dt,\qquad
H(y)=\int_{17/50}^y\sin\alpha(t)\,dt,
$$

并在平区取 $C(y)=y,H(y)=0$。其中 $\alpha$ 是非减的原 S9 转角，$0\le\alpha\le A$，位置为 $(x,C(y),Z-H(y))$。其余象限由原反射定义处理。

记 $p=C'=\cos\alpha$。有 $C''\le0$、$H''=\alpha'\cos\alpha\ge0$，且

$$
yp\le C\le y,\qquad p\ge\cos A>\frac{16}{25}.
$$

最后一个严格有理下界不依赖浮点三角函数：由交错 Taylor 余项，

$$
\cos(7/8)>
1-\frac{(7/8)^2}{2}+\frac{(7/8)^4}{24}-\frac{(7/8)^6}{720}
=\frac{120982511}{188743680}
>\frac{16}{25};
$$

后二者之差为 $932779/943718400>0$。

固定平面极角 $\theta$，令 $t=\cot^2\theta$。在 active 区域 $y>17/50$，由 $x=C(y)\cot\theta$，

$$
r(y)^2=y^2+C(y)^2t,\qquad
r_y=\frac{y+Cp\,t}{r}>0.
$$

真实物理尾坐标满足 $r_s=-1$，因而

$$
z_s=\frac{H'}{r_y}\ge0,\qquad
z_{ss}=-\frac{H''}{r_y^2}
+\frac{H'r_{yy}}{r_y^3}.
$$

记 $A_1=y+Cp\,t$。准确求导得到

$$
\frac{r_{yy}}{r_y^2}
=\frac{t(C-yp)^2+CC''\,t\,r^2}{rA_1^2}
\le\frac{t(C-yp)^2}{rA_1^2}.
$$

令 $q=yp/C\in[16/25,1]$、$x=C^2t/y^2\ge0$，则

$$
\frac{r_{yy}}{r_y^2}
\le\frac{x(1-q)^2}{r(1+qx)^2}
\le\frac{(1-q)^2}{4rq}
\le\frac{81}{1280},
$$

其中使用 $r=4/5$ 及 $(1-q)^2/q$ 在 $q\in(0,1]$ 上递减。因此全 active 角域

$$
z_{ss}\le\frac{81}{1280}z_s.
$$

若 $L<4/5$、$N=31$，右端 Bernstein 控制满足

$$
b_{30}=z_s-\frac L{31}z_{ss}
\ge\left(1-\frac{81L}{31\cdot1280}\right)z_s
\ge\frac{49519}{49600}z_s\ge0,\qquad b_{31}=z_s\ge0.
$$

平区直接有 $z_s=z_{ss}=0$；边界由连续性延伸。$\theta=\pi/2$ 取 $t=0$，其余轴落在直接处理的平区，所以没有遗漏极角轴点。

本题准确输入 $A=0.8746432018013935<7/8$、$L=0.7956739498716915<4/5$，故这一右端控制条件已经连续支付。左 coast 极角/高度预算、两个端时钟控制和内部质量 $M$ 的连续正下界仍须另行证明；现有 $1024$ 角采样不能替代它们。

## 8. 结论范围

本条提供准确可消费的完整 C2 位置构造、其显式非折叠假设，以及相对于独立冻结 $g$ 的定量面积/Gram 下界。它允许后继在正内部控制之间重新分配高度积分，不改变完整端口或目标度量。

目前只单独支付了 R205 右端的全角高度控制。当前新场自己的有限完整基线已失败于 metric/曲率门槛；无完整闭曲面、无非平凡同一 $g$ 等距族、无全闭 reach 或 README 完成声明。

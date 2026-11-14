# 常斜率段的准确线性传递与强二模核心的 outward 设计

作者：visible-larger-astra-20261110 / alternative_mechanism，2026-11-10。

**可信度分开记：** 第 1–4 节是完整证明的有限维线性恒等式和条件性非线性入口公式；第 5 节是有限 Fourier / 常斜率设计数值，不是闭曲面存在定理。平滑转弯、非线性整体联解、真实尾反馈仍未支付。

## 1. 旋转背景的模方程

取旋转背景

$$
F_0(s,\theta)=(a(s)\cos\theta,a(s)\sin\theta,z(s)),
\qquad a'=v,\quad z'=b=\sqrt{1-v^2}>0.
$$

在固定材料角中，第 $m\ge2$ 模的一阶等距扰动可写为

$$
\dot F=f(s)\cos(m\theta)e_r
-\frac{f(s)}m\sin(m\theta)e_\theta
+g(s)\cos(m\theta)e_z.
\tag{1}
$$

角向等距式 $\langle F_{0,\theta},\dot F_\theta\rangle=0$ 给出式 (1) 的切向系数。由 $\langle F_{0,s},\dot F_s\rangle=0$ 得

$$
v f'+b g'=0.
\tag{2}
$$

再由混合等距式
$\langle F_{0,s},\dot F_\theta\rangle+
\langle F_{0,\theta},\dot F_s\rangle=0$，其 $\sin(m\theta)$ 系数为

$$
-\left(m-\frac1m\right)vf-mbg-\frac am f'=0.
$$

于是

$$
\frac d{ds}\binom fg=
\frac1a M_m(v)\binom fg,
\qquad
M_m(v)=
\begin{pmatrix}
-(m^2-1)v&-m^2b\\
(m^2-1)v^2/b&m^2v
\end{pmatrix}.
\tag{3}
$$

(2)–(3) 对任何 $|v(s)|<1$ 都成立，不要求 $v$ 常值。这里的 $f$ 是在固定材料角中的径向变分；在平面初始核心，一阶上也是支撑函数的该模系数。它不是未经定义的高度振幅。

## 2. 常斜率传递定理

**定理。** 在一段上 $a(s)=a_0+v(s-s_0)>0$，其中 $v\ne0$ 为常数、$|v|<1$，则 (3) 从 $a_0$ 到 $a_1$ 的准确基本矩阵为

$$
\boxed{T_m(a_0,a_1;v)
=I+\left(\frac{a_1}{a_0}-1\right)\frac{M_m(v)}v.}
\tag{4}
$$

若 $v=0$、段长 $L$、$a\equiv a_0$，则

$$
\boxed{T_m(a_0,L;0)=
\begin{pmatrix}1&-m^2L/a_0\\0&1\end{pmatrix}.}
\tag{5}
$$

**证明。** 直接乘法给

$$
M_m(v)^2=vM_m(v).
\tag{6}
$$

例如左上元为 $(m^2-1)^2v^2-m^2(m^2-1)v^2=-(m^2-1)v^2$，即 $vM_{11}$；其余三元同样展开即得。于是 $P=M_m(v)/v$ 是幂等矩阵。积分

$$
\int_{s_0}^{s_1}\frac{ds}{a(s)}=
\frac1v\log(a_1/a_0)
$$

并利用矩阵在这一段常值，得到

$$
T=\exp\!\bigl(P\log(a_1/a_0)\bigr).
$$

对任意幂等矩阵 $P$，由绝对收敛的幂级数与 $P^k=P$（$k\ge1$），
$e^{xP}=I+(e^x-1)P$，这就是 (4)。当 $v=0$，方程为 $g'=0,f'=-m^2g/a_0$，直接积分给 (5)。证毕。

特别地 $\det T=a_1/a_0$，且相邻同速段满足准确组合律
$T(a_1,a_2;v)T(a_0,a_1;v)=T(a_0,a_2;v)$。这两条也可由 (4) 和 $P^2=P$ 直接验证，不依赖数值 ODE。

若入口是平面方向 $(f,g)=(A,0)$，则

$$
f(a)=A\left[m^2-(m^2-1)\frac a{a_0}\right],
\qquad
 g(a)=\frac v{\sqrt{1-v^2}}\,[A-f(a)].
\tag{7}
$$

式 (7) 是线性化方程的准确解，不能称为有限振幅嵌入。

## 3. 多段同时共振的准确有限计算

设依次有常速段 $(a_{j-1},a_j,v_j)$；允许在指定半径插入 (5) 的零速停留。每个模的总传递是按物理顺序相乘的准确 $2\times2$ 矩阵

$$
\mathcal T_m=T_{m,k}\cdots T_{m,1}.
\tag{8}
$$

假设尾及末端固定平滑桥的入口允许直线由一个非零向量 $q_m$ 张成。一个平面核心的 $m$ 模可以沿整个线性问题到达该直线，当且仅当

$$
\boxed{\det(\mathcal T_m e_1,q_m)=0.}
\tag{9}
$$

**证明。** 各段的行列式均为正，故 $\mathcal T_m e_1\ne0$。式 (9) 正是两个非零向量线性相关，等价于终端满足那条一维 Robin 线。证毕。

因而 $m=2,4$ 的双线性共振是两个明确标量方程，而不是观察某个有极点的比值换号。设计器采用

$$
R_m=\det\left(\frac{\mathcal T_m e_1}{|\mathcal T_m e_1|},
\frac{q_m}{|q_m|}\right)
$$

以避开 $f=0$ 的除法；有限浮点根仍须标为数值根。各段旋转背景的高度增加准确为

$$
\Delta z_j=\frac{|a_j-a_{j-1}|}{|v_j|}\sqrt{1-v_j^2},
\tag{10}
$$

零速停留贡献其长度。这是设计背景高度，不能替代强非轴对称图的真实高度。

瞬时变换 $v_j\to v_{j+1}$ 不是 $C^2$ 转弯。若用经线倾角 $\phi$ 表示 $v=\sin\phi$，曲率上界 $K$ 迫使一段单调转弯的长度至少 $|\Delta\phi|/K$，高度增加至少 $|\Delta v|/K$。证明分别积分 $|\phi'|\le K$ 和 $\cos\phi\ge0$；达到等号的圆弧仍要在拼点平滑其曲率。这个额外成本不能在设计器的瞬时转弯高度中默默省略。

## 4. 强平面核心的瞬时均匀化公式

在一个平面凸入口，用法向角 $\varphi$ 表示曲线

$$
\gamma=h e_r+h_\varphi e_\varphi,
\qquad \rho=h+h_{\varphi\varphi}>0.
$$

设当前周长为 $2\pi a$、径向速度为 $a'=v$，且 $|v|\rho/a<1$。Frenet 正向速度的水平外法分量与竖直分量分别是

$$
V_h=\frac va\rho\,e_r,
\qquad V_z=\sqrt{1-(v\rho/a)^2}.
\tag{11}
$$

**证明。** 平面曲线的单位 Frenet 主法向为 $-e_r$，曲率 $\kappa=1/\rho$，向上的副法向为 $e_z$。保持 $|F_s|=1$、$F_s\perp F_\theta$ 及角向长度按 $a$ 变化的速度为
$V=\alpha N+\beta B$，其中 $\alpha=-v/(a\kappa)$、$\beta=\sqrt{1-\alpha^2}$。代入即得 (11)。

在随当前法向角重参数化的平面投影中，支撑函数的瞬时导数为法向速度，因此

$$
\partial_s h=\frac va(h+h_{\varphi\varphi}).
\tag{12}
$$

这给出每个支撑模的瞬时趋势
$\partial_s(h_m/a)=-m^2(v/a)(h_m/a)$。但 $V_z$ 对非圆曲线一般依赖角度，后续曲线随即非平面；所以 $h_m/a\propto a^{-m^2}$ 不是整段非线性传播定理。式 (7) 已展示即便在线性问题里，高度耦合也会改变整段衰减律。

对 $h=1+.38\cos2\varphi-.38/(10\sqrt2)\cos4\varphi$，初始
$\rho_{\max}=1+(3+3/(2\sqrt2))(.38)$，所以平面入口的瞬时速度门是
$|v|<1/\rho_{\max}\approx.3932$。这个是**当前入口**的门；在真实 outward 传播令最小空间曲率升高以后，不能继续把旧门当整段固定限制。

## 5. 实际数值文件与仍缺内容

`computations/alternative-segment-designer.py` 实现 (4)–(10)，在本题现成有限线性 tail port 上，用原平滑 bridge 的实际反向积分产生 $q_2,q_4$。四类结果在
`notes/alternative-segment-resonance-{one,dwell,two,valley}.json`。

其中一个单周期数值双根为

$$
\Delta a=.071364329881761,\quad
v_+=.9068949317256971,\quad v_-=-.94.
$$

两模归一行列式残差均小于 $3.3\times10^{-15}$，计入原平滑桥的背景高度约 $.46149208693$。这仍是高速度、瞬时转弯的线性种子；强核心不能在原位置直接跳到这一速度。

较温和的三段数值根为

$$
a:1\to1.0382964649\to.8968453110\to1,
$$
$$
v:(.4866043316,-.4271961599,.3311541402),
$$

两残差小于 $4\times10^{-11}$、背景高度约 $1.0644941536$，总转角约 $2.57423$。同样未支付平滑与强非线性域。

强核心传播使用独立脚本 `computations/alternative-outward-probe.py`。固定

$$
a(s)=1+\tfrac12(s^3-\tfrac12s^4),\quad 0\le s\le.8
$$

及同一上述强核心，以初始法向角为固定计算角；材料角导数恒为 $\rho_0(\varphi)$，故目标度量是
$ds^2+a(s)^2\rho_0(\varphi)^2d\varphi^2$。M24、M48、M72 使用同一物理度量和区间，末端最大分量相对 metric 采样误差依次约

$$
4.03115\times10^{-5},\quad1.13215\times10^{-7},\quad4.04003\times10^{-10}.
$$

M72 末端 $a=1.1536,a'=.448$，Frenet 实域余量约 $.572773$，曲线曲率范围约 $[.594146,3.509940]$，实际有限图的主曲率绝对值采样上界约 $3.488390$，最大水平半径约 $1.389231$，高度范围约 $[.670217,.798758]$。这实际越过了初始速度门且并未增加很多横向直径。

这些数值仍只是有边前缀、离散采样与有限模收敛证据；没有称作全域严格界或闭面解。继续任务是：完整记录整区间采样误差和导数；将入口的加速度平滑收尾到常斜率，使用准确可展片公式继续；最终接到同一真实尾反馈并同时做整个闭面的指标。

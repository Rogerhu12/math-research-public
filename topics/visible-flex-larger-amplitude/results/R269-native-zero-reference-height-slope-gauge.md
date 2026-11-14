# R269. 原生尾零形状参考的高度斜率坐标与完整块坐标变换

2026-11-14，/root，GPT-6 Astra Pro，AI辅助。本文给出完整实数代数证明，不使用新数值计算。

结论针对已经核定的**精确零形状参考局部矩阵**，并给出任意完整 shooting 矩阵的可逆块坐标变换。它不把 actual28 的非零场、计算出的长 J 或第41次逐步 J 代作零参考，也不预断某次浮点求解改善。完成证明直接保存于 results，不以额外评审或数值门为条件。

## 269.1. 对象、源码与假设

[原 stage J 来源记录](../notes/2026-11-14-native-stage-J-generation-and-propagation-scope.md) 已按实际 consumed-source SHA 核过局部解析组装。这里使用其中的零形状块；其源是 `78718-tail-fourier-product-jacobian.mjs`，SHA

`205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25`。

原 root/geometry 源 `78718-tail-fourier-root-momentum.mjs` 的 SHA 为

`cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88`。

在本文中，$w=\exp(\mathrm{profile.logw})$，原径向度量系数是 $E=1+w^2$。这一定义不能与另一个弧长坐标下同名的 $w$ 混用。

固定一个 profile 区间。设 $r,w$ 为正的 $C^1$ 函数，$r_x\ne0$；固定 $\mu>0$、方向 $\varepsilon\in\{-1,1\}$ 和一个非零频率 $m$。$\mu,\varepsilon,m$ 在这个区间内为常数。记

$$
\gamma=\frac{r_x}{r},\qquad
\omega=\frac{w_x}{w},\qquad
a=m^2-4,\qquad
b=\frac{\varepsilon\sqrt{12}\,\mu}{r^7w}.
\tag{269.1}
$$

于是 $b\ne0$ 且

$$
\frac{b_x}{b}=-7\gamma-\omega.
\tag{269.2}
$$

精确零形状 $Q=\Pi=0$ 时，隐式根为 $L=0$，原 Gram 为单位矩阵，非线性角矩消失。对该参考的一个形状模态，令 $q,p$ 分别为 $Q_m,\Pi_m$ 的线性变分。实际源的实数局部块给出

$$
\begin{pmatrix}q\\p\end{pmatrix}_x
=\gamma
\begin{pmatrix}
a&b\\
-m^2(m^2-1)/b&-a
\end{pmatrix}
\begin{pmatrix}q\\p\end{pmatrix}.
\tag{269.3}
$$

两个额外 mean 积分坐标不反馈这个形状块。这里没有删去实际非零场中可能存在的模式耦合；(269.3) 的适用对象从始至终只是零形状参考。

## 269.2. 一次剪切与尺度变换

**命题。** 定义

$$
v=aq+bp.
\tag{269.4}
$$

则 (269.3) 与下列系统双向等价：

$$
q_x=\gamma v,\qquad
v_x=(-12\gamma+a\omega)q-(7\gamma+\omega)v.
\tag{269.5}
$$

**证明。** 第一式直接来自 (269.3)。对第二式逐项求导并以 $bp=v-aq$ 代入，得

$$
\begin{aligned}
v_x
&=a\gamma v+\frac{b_x}{b}(v-aq)
  -\gamma m^2(m^2-1)q-\gamma a(v-aq)\\
&=\frac{b_x}{b}v+
  \left\{\gamma\bigl(a^2-m^2(m^2-1)\bigr)
                  -a\frac{b_x}{b}\right\}q.
\end{aligned}
$$

由于

$$
a^2-m^2(m^2-1)=16-7m^2,
\qquad
(16-7m^2)+7a=-12,
$$

代入 (269.2) 即得 (269.5)。反之，$p=(v-aq)/b$ 在全区间有定义；对其求导，用 (269.2)、(269.5) 反代即恢复 (269.3)。因此这里是可逆变换，没有丢失一个解或一个约束。证毕。

若用 $s=\log r$ 作局部独立变量，并记 $\ell=\omega/\gamma$，则 (269.5) 等价于

$$
q_{ss}+(7+\ell)q_s+
\bigl(12-(m^2-4)\ell\bigr)q=0.
\tag{269.6}
$$

这里 $q_s=v$，所以 (269.6) 不需要在 $x$ 坐标先求 $r_{xx}$。$r_x\ne0$ 保证这个局部换元合法。式中保留了实际 $w$ 的变化，不能未经证明就置 $\ell=0$。

## 269.3. 高度尺度与径向斜率变量

进一步定义

$$
u=r^4q,\qquad
k=r^3(4q+v)=r^3(m^2q+bp).
\tag{269.7}
$$

其完整矩阵为

$$
\binom{u}{k}=G(x)\binom{q}{p},\qquad
G(x)=\begin{pmatrix}
r^4&0\\
m^2r^3&br^3
\end{pmatrix},\qquad
\det G=r^7b=\frac{\varepsilon\sqrt{12}\mu}{w}\ne0.
\tag{269.8}
$$

**定理。** 原零参考系统 (269.3) 与

$$
u_x=r_x k,\qquad
k_x=\omega\left(\frac{m^2}{r}u-k\right)
\tag{269.9}
$$

双向等价。以 $r$ 为独立变量时，$k=u_r$ 且

$$
u_{rr}+\frac{w_r}{w}u_r-
\frac{m^2w_r}{rw}u=0,
\qquad
(wu_r)_r=\frac{m^2w_r}{r}u.
\tag{269.10}
$$

**证明。** 由 (269.5)、(269.7)，

$$
u_x=r^4\gamma(4q+v)=r_x k.
$$

对第二个变量求导，完整消去项为

$$
\begin{aligned}
k_x
&=r^3\{3\gamma(4q+v)+4\gamma v+v_x\}\\
&=r^3\omega(aq-v)\\
&=\omega\{r^3(a+4)q-k\}
=\omega\left(\frac{m^2}{r}u-k\right).
\end{aligned}
$$

因为 $G$ 可逆，反代 $q=u/r^4$、$p=(k/r^3-m^2q)/b$ 就得到等价的原系统。由 $r_x\ne0$ 可用 $r$ 作参数，第一式给 $u_r=k$，第二式除以 $r_x$ 给 (269.10)。所有等式均是完整导数，$G_x$ 的项没有省略。证毕。

原实际 seed 的 cut 条件是 $Q_m=H_m/r_{\rm cut}^4$，其完整身份由 [逐步捕获接口](../notes/2026-11-14-native-rawcell0-original-step-capture-interface.md) 绑定。因此 $u$ 在这个参考 cut 正是相应的 $H_m$ 尺度。不过本证明无需把一般非零 finite 场的所有几何读出归约成 $u,k$；其非线性根和完整 mean 仍属于原系统。

## 269.4. 常 $w$ 子区间的完整传播

**推论。** 如果这个区间上的 $w$ 确实为常数，则任意两个径向位置 $r_0,r_1$ 之间，(269.9) 的精确传播为

$$
\binom{u(r_1)}{k(r_1)}=
\begin{pmatrix}1&r_1-r_0\\0&1\end{pmatrix}
\binom{u(r_0)}{k(r_0)}.
\tag{269.11}
$$

相应原坐标完整传播为

$$
\Phi_m(x_1,x_0)=G(x_1)^{-1}
\begin{pmatrix}1&r_1-r_0\\0&1\end{pmatrix}G(x_0).
\tag{269.12}
$$

**证明。** $\omega=0$ 时 $k_x=0$、$u_x=r_xk$，积分即得 (269.11)，再用 (269.8) 的两端逆变换即得 (269.12)。等价地，$u=Ar+B$，故

$$
q=Ar^{-3}+Br^{-4},\qquad
p=b^{-1}\{(1-m^2)Ar^{-3}-m^2Br^{-4}\}.
\tag{269.13}
$$

代入原两行也直接给出该完整二维解空间。证毕。

作为一致性检查，(269.3) 的迹恒为零，故原精确基本矩阵的行列式为1。一般可变 $w$ 下，(269.9) 的迹为 $-\omega$，其基本矩阵行列式为 $w(x_0)/w(x_1)$；再乘两端 $G$ 的行列式比，仍恢复原传播行列式1。这是 Liouville 公式的直接积分，也可由两解的 Wronskian 求导得到。

常 $w$ 结论消除了该特定参考在 $u,k$ 中的频率依赖，但**没有**给出原 $q,p$ 坐标传播的统一条件数界：两端 $G$ 含 $m^2,\mu,r,w$，可以有很大或很小的尺度。对于可变 $w$，(269.9) 仍有 $m^2\omega/r$ 项。两种情形不得混用，也没有据此证明 actual28 某一段满足常 $w$ 假设。

## 269.5. 实际有限 shooting 矩阵的独立代数结论

下面不再假设零参考。取任意实际保存的完整有限矩阵，其 stage 方程是

$$
J_n\delta_{n+1}-\delta_n+r_n=0,
\qquad 0\le n<D.
\tag{269.14}
$$

原 cut、far 方程也完整保留。对每个节点任取一个可逆矩阵 $G_n$，定义新未知量 $\xi_n=G_n\delta_n$，并以 $G_n$ 左乘第 $n$ 个 stage 方程。所得方程为

$$
(G_nJ_nG_{n+1}^{-1})\xi_{n+1}-\xi_n+G_nr_n=0.
\tag{269.15}
$$

若某原边界行为 $C\delta_0+d=0$ 或 $F\delta_D+e=0$，则变成

$$
CG_0^{-1}\xi_0+d=0,
\qquad FG_D^{-1}\xi_D+e=0.
\tag{269.16}
$$

**命题。** (269.14) 连同全部原边界与 (269.15)–(269.16) 的解一一对应；没有改变零点、原参数或方程数量。若新 stage 缺陷为 $\widetilde e_n$，则原缺陷精确为

$$
e_n=G_n^{-1}\widetilde e_n.
\tag{269.17}
$$

**证明。** 逐节点代入可逆未知量替换，再逐stage左乘可逆矩阵，就是 (269.15)。按 (269.16) 保留边界后反向代入可恢复每个原方程。对非零缺陷作同一等式变换即得 (269.17)。证毕。

对于各频率的 (269.8) 下三角二元块，在 node-major 全 $(Q,\Pi)$ 顺序中，stage 的当前节点系数仍是 $-I$；cut 的 Q 选择只涉及新 $u$，原逐频率 far Robin 行变成同频率 $u,k$ 的完整组合。其节点邻接关系没有扩成远距稠密耦合。这里是结构结论，不是已经组装或求解了一个新矩阵。

选择 $G_n$ 必须使用该节点实际坐标及原 port 约定；不同原 stage 的 $\mu$ 和出口 Pi 重标度不能擅自共用一个值。本命题允许任意已明确的可逆 $G_n$，因此不依赖把参考 $G$ 错当实际流的精确对角化。

实际浮点重组还会引入矩阵形成、三角代回和坐标恢复误差。原 norm 使用原 sigma，必须回原变量和原完整方程读取缺陷，不能以新坐标的小数值直接代替；[R266](R266-native-block-Newton-defect-and-original-scaled-descent.md) 的误差区分继续适用。对已经舍入的长 J 作两端变换，也不能恢复此前传播中丢失的信息。

## 269.6. 连续变换、离散 RK 与当前工作的界限

对一般线性变分 $y_x=J(x)y$ 和可逆 $C^1$ 矩阵 $G(x)$，逐项求导得到

$$
z=Gy\quad\Longrightarrow\quad
z_x=(GJG^{-1}+G_xG^{-1})z.
\tag{269.18}
$$

省略 $G_xG^{-1}$ 就不是同一连续方程。对一般非线性 RHS $f$，同一换元给

$$
z_x=Gf(G^{-1}z,x)+G_xG^{-1}z,
$$

其完整状态导数仍需保留所有实际非线性项与模态耦合。

把一个随 $x$ 变化的坐标变换放进 RK4 的各级，通常得到与“先按原 RK4 算出离散映射，再只变换两端”不同的有限算法。一个简单的反例已足以排除普遍相同：原标量方程 $y_x=0$ 配 $G(x)=e^x$，变换后为 $z_x=z$；一步 RK4 的四次多项式不恒等于 $e^h$。所以即使连续方程严格等价，也不能宣称两种离散执行逐字节相同，或省去原接受检查。

第41次只捕获原状态路径上每个已有 RK 步的局部 J，没有实施本节的新坐标积分。本文也没有计算任何新的条件数、矩阵缺陷、native 试步、全 BVP 或闭面几何。它给出后继若需改变表示时可用的精确代数，并明确哪些原变量、边界、port、尺度和非线性检查必须继续保留。

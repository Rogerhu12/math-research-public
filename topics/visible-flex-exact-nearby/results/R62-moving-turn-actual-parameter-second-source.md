# R62：移动转折的固定 $\tau$ 实际参数二阶源

**状态：已证明的是本条恒等式、端点消奇及完整参数变分接口。** 附带程序是这些恒等式在当前精确 affine 对象上的浮点评价器；它尚未给出整条射线的连续有向 Taylor 上界。该区别不把课题完成标准降为线性或有限维结果。

## 1. 同一实际族与坐标

取 R57–R58 的精确 affine 原始控制点族，再按已明确的径向偶奇平均定义 $a,\beta$ 偶、$Z,\gamma$ 奇的无限 R33 图 $F(x,\theta,p)$。原始控制点与 mean 参数先作准确的 affine 加法，而非先把全向量舍入成另一 NPZ。$p$ 是这个实际族的坐标 $\delta$。

当前冻结输入中的 phase、base、shift、mean 及 height-slope 样条均为五次，在 $|x|\le0.24$ 的全部内节点重数为一；显式反射平均仍为 $C^4$。因此 $F_x$ 至少为 $C^3$，下面的 $K$ 至少为 $C^2$。共同根 collar 内没有这些输入的节点或其反射点，那里各系数解析。评价器逐字段核查这两个有限输入事实并记录到报告；这补上了在样条接缝处使用二阶参数依赖所需的正则性，未假定整核解析。

目标径向度量随参数同步输出：

$$
g_0(p)=E(x,p)\,dx^2+a(x,p)^2\,d\theta^2,
\qquad E=\langle|F_x|^2\rangle_\theta,
$$

$$
C_0=a_xE_x-2a_{xx}E,\qquad K=\frac{C_0}{2aE^2}.
\tag{62.1}
$$

这里 $K$ 是目标度量曲率，不替代候选曲面的实际高斯曲率。记

$$
\mathcal C=F_\theta\times F_x,\quad
m=\mathcal C\cdot F_{x\theta},\quad
n=\mathcal C\cdot F_{\theta\theta},\quad G=|\mathcal C|^2,
\quad b=-m/n,\quad w=G/n.
\tag{62.2}
$$

在已经支付的实角 $n<0$ 图内，R37 的两个主速度可按选支写成
$b+\sigma w\sqrt{-K}$，$\sigma\in\{-1,1\}$。
用 $x=t(p)\sin\tau$ 固定两端 $\tau=\pm\pi/2$，其中 $t(p)>0$ 是该同族目标曲率的简单正根。定义

$$
Q(\tau,p)=\frac{-K(t(p)\sin\tau,p)}{\cos^2\tau}.
\tag{62.3}
$$

内核中 $Q>0$，在根处作下节的连续延拓。由于实际目标曲率准确为偶函数，下节计算 $Q$ 时可用 $s=|\sin\tau|$。几何量 $b,w$ 仍在带符号的 $x=t\sin\tau$ 评价，不能把非径向实际图的两侧直接替换。

固定 $\tau$ 的完整标量场为

$$
f_\sigma(\tau,\theta,p)
=t\cos\tau\,\bar b
 +\sigma t\cos^2\tau\,\bar w\sqrt Q,
\qquad \bar b=b(t\sin\tau,\theta,p),
\tag{62.4}
$$

其中 $\bar w$ 同义。所有 $G$ 均为实际 $G$，没有令 $G=Ea^2$。

## 2. 根与 $Q$ 的二阶参数导数

从 $C_0(t(p),p)=0$ 及 $C_{0x}\ne0$，隐函数微分逐次给出

$$
t_p=-\frac{C_{0p}}{C_{0x}},\qquad
t_{pp}=-\frac{C_{0pp}+2C_{0xp}t_p+C_{0xx}t_p^2}{C_{0x}}.
\tag{62.5}
$$

这正是 R58 已有向包住的真实参数根导数，不是径向作用量对人为参数的导数。

在远离端点处可直接对 (62.3) 微分。令 $s=|\sin\tau|$，则

$$
Q_p=-\frac{K_p+t_psK_x}{1-s^2},\qquad
Q_{pp}=-\frac{K_{pp}+2t_psK_{xp}+t_p^2s^2K_{xx}+t_{pp}sK_x}{1-s^2},
\tag{62.6}
$$

右端 $K$ 的各导数在 $(ts,p)$ 取值。这些分子因根移动而在 $s=1$ 消失；逐项分开估计会产生不存在的奇性。

为给近端点可直接计算的表达式，置

$$
\xi=1-u(1-s),\qquad I=\int_0^1K_x(t\xi,p)\,du.
$$

微积分基本定理及 $K(t,p)=0$ 给出

$$
-K(ts,p)=t(1-s)I,\qquad Q=\frac{tI}{1+s}.
\tag{62.7}
$$

在根的共同光滑 collar 内可在积分号下求导。由 $\xi$ 与 $p$ 无关，得到

$$
I_p=\int_0^1(K_{xp}+t_p\xi K_{xx})\,du,
$$

$$
I_{pp}=\int_0^1
\left(K_{xpp}+2t_p\xi K_{xxp}+t_p^2\xi^2K_{xxx}
+t_{pp}\xi K_{xx}\right)du,
\tag{62.8}
$$

$$
Q_p=\frac{t_pI+tI_p}{1+s},\qquad
Q_{pp}=\frac{t_{pp}I+2t_pI_p+tI_{pp}}{1+s}.
\tag{62.9}
$$

分母 $1+s\ge1$。这些式子同时给两个端点的连续二阶参数延拓；例如 $Q(\pm\pi/2,p)=tK_x(t,p)/2$。没有除以零的参数分子，也没有把求解器的端点样本当作极限证明。

对当前共同根括号 $t\in[0.238394,0.2384]$，$s\ge0.999$ 的整条积分段落在

$$
[0.238152859375,0.23864114062500003]
$$

这一 R58 已用的共同 collar 内：最小下端 $0.999\cdot0.238394=0.238155606$ 大于左界，最大上端 $0.2384$ 小于右界。因此现有 R58 的混合目标 jet 输入可直接用于 (62.8)，不需把整个跨样条节点的核心假定为一个解析片。核心其他位置使用 (62.6)，只需目标曲率的二阶混合导数。

## 3. 实际非径向系数的路径微分

若 $h(x,\theta,p)$ 是任一实际几何标量，定义 $\bar h=h(t\sin\tau,\theta,p)$，固定 $\tau$。设 $x_p=t_p\sin\tau$、$x_{pp}=t_{pp}\sin\tau$。链式法则给出

$$
\bar h_p=h_p+x_ph_x,
\qquad
\bar h_{pp}=h_{pp}+2x_ph_{xp}+x_p^2h_{xx}+x_{pp}h_x.
\tag{62.10}
$$

角导数与这些参数导数可交换。因此同式用于 $b_\theta,w_\theta$；全部角向耦合仍保留，没有把系数径向化。

对于原始 affine profile $h$，固定 $x$ 的 $h_{pp}=0$。其路径二阶 Taylor 系数因而是

$$
[p^2]\bar h=x_ph_{xp}+	frac12x_p^2h_{xx}+	frac12x_{pp}h_x.
\tag{62.11}
$$

这只适用于 profile 本身；$T,F,m,n,G,b,w,K$ 都是非线性函数，不能将它们的实际 $p^2$ 项设为零。

具体构造全部所需场 jet 的办法如下。以圆柱旋转基表示

$$
T=(-\cos\gamma\sin\beta,\ \cos\gamma\cos\beta,\ \sin\gamma),
\qquad B=a_xT+aT_x.
$$

因为 $F=a\mathcal P_\theta T+Ze_z$ 且 $\mathcal P_\theta$ 是固定的线性原函数算子，

$$
F_x=\mathcal P_\theta B+Z_xe_z,\quad
F_\theta=aT,\quad F_{x\theta}=B,\quad
F_{\theta\theta}=a(\partial_\theta T+JT),
\tag{62.12}
$$

其中 $J(v_r,v_\theta,v_z)=(-v_\theta,v_r,0)$ 是旋转基的连接项。先按 (62.11) 形成 $a,a_x,Z_x,\beta,\beta_x,\gamma,\gamma_x$ 的路径参数 jet，再把普通角 jet 与其做有限多项式乘除、sin/cos，即得 (62.2) 的完整混合 jet。交叉积和点积的标量值对基旋转不变；但 (62.12) 内的连接项必须保留。

该步骤与有限频率截断无关；对无限原函数是准确恒等式。程序的 FFT 仅为这个线性原函数提供尚待支付尾项的数值实现，并未把有限原函数的角导数宣称为无限 $aT$。

## 4. 可直接积分的二阶源

令 $r=\sqrt Q$，则

$$
r_p=\frac{Q_p}{2r},\qquad
r_{pp}=\frac{Q_{pp}}{2r}-\frac{Q_p^2}{4r^3}.
\tag{62.13}
$$

将 $t,\bar b,\bar w,r$ 的二阶参数 jet 代入 (62.4)，便同时得到
$f,f_\theta,f_p,f_{\theta\theta},f_{\theta p},f_{pp}$。例如记 $c=\cos\tau$，则

$$
f_p=c(t_p\bar b+t\bar b_p)
+\sigma c^2(t_p\bar w r+t\bar w_pr+t\bar w r_p),
$$

$$
\begin{aligned}
f_{pp}={}&c(t_{pp}\bar b+2t_p\bar b_p+t\bar b_{pp})\\
&+\sigma c^2\bigl(t_{pp}\bar w r+2t_p\bar w_pr+2t_p\bar w r_p
+t\bar w_{pp}r+2t\bar w_pr_p+t\bar w r_{pp}\bigr).
\end{aligned}
\tag{62.14}
$$

这是实际族的导数；它们不是保存的 DOP853 多项式对某个数组标签的导数。

设 $Y$ 解 $Y_\tau=f(\tau,Y,p)$，初始角固定且与 $p$ 无关。写
$z=Y_p$、$v=Y_{pp}$、$L=\log(\partial_{\theta_0}Y)$。常微分方程逐次求导给出

$$
\begin{aligned}
Y_\tau&=f, &L_\tau&=f_\theta,\\
z_\tau&=f_\theta z+f_p,&
v_\tau&=f_\theta v+f_{\theta\theta}z^2+2f_{\theta p}z+f_{pp}.
\end{aligned}
\tag{62.15}
$$

第一支的 $L,z,v$ 初值均为零。第一支终值直接作为第二支初值，切换选支并反向积分 $\tau$ 后，末端 $z,v$ 就是完整返回的 $R_p,R_{pp}$。不再另外加端点移动项，因为固定 $\tau$ 的场已包含全部 $t_p,t_{pp}$。

若同时需要 $R_{\theta p}$，再积分

$$
\ell_\tau=f_{\theta\theta}z+f_{\theta p},\quad\ell(\tau_0)=0,
\qquad R_{\theta p}=e^{L_{\rm end}}\ell_{\rm end}.
\tag{62.16}
$$

这些式子的角变量是物理 $\theta$。接 R31 的归一角 $\varphi=4\theta$ 时，
$R_{\rm norm}(\varphi,p)=4R_{\rm phys}(\varphi/4,p)$，所以
$$
(R_{\rm norm})_p=4z,\qquad (R_{\rm norm})_{pp}=4v,\qquad
(R_{\rm norm})_\varphi=e^{L_{\rm end}},\qquad
(R_{\rm norm})_{\varphi p}=e^{L_{\rm end}}\ell_{\rm end}.
\tag{62.17}
$$
源程序的 rhs 始终使用物理 $\theta$，比例转换在输出或应用层完成。

有 $Q>0$、$n\ne0$ 的共同管时，上述系数在两端连续。式 (62.4) 的 $c,c^2$ 因子还显示 $f,f_p,f_{pp}$ 在准确端点都为零。常规参数依赖与逐次微分因此可在整个固定时间区间应用；不需跨过非可积的伪端点源。

## 5. 当前实际评价器与剩余费用

新源 `scripts/fourfold_phase_affine_second_variation.py` 的
`ActualAffineSecondField.evaluate(tau,theta,sign)` 返回 (62.15)–(62.16) 所需全部六个场；`rhs` 支持四行状态 $(Y,L,z,v)$，或增加第五行 $\ell$。所有参数导数由有限 nilpotent jet 运算产生。目标 jet 使用真实 affine profile 的径向五阶/参数二阶输入及 Fourier Parseval；实际非径向场使用 (62.11)–(62.12)，没有有限差分导数源。

在当前准确 $\delta_3=-7832869216826619/4611686018427387904$ 点，浮点评价得到

$$
t_p\simeq6.110800376546802\cdot10^{-5},\qquad
t_{pp}\simeq-9.402869185378746\cdot10^{-7},
$$

均落在 R58 的整管有向区间内。近端点的 $Q$ 和二阶源被有限地评价出来。源码内还保留独立的实际参数移点/重新解根差分核对，以及旧固定 $x$ 一阶实际几何列加链式法则的对比；这些只是定位数值实现误差的诊断。

还需要在同一准确参数点/小盒上支付：目标和几何各混合 jet 的连续区间、无限原函数尾与全部舍入、近根积分商的有向积分、根中心不确定性以及 ODE 参考残差。只有完成这些输入，(62.15) 才能给 R31/R60 的实际返回参数 Taylor 常数。本条不把浮点二阶源或有限差分吻合当成该常数。
